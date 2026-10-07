#!/usr/bin/env python3
"""
aimctl.py — AIM 機械層（CHARTER C1.2 §6）。只選、記、算；不做判斷。

    python tools/aimctl.py pick                 # 印出本輪角色與任務（JSON）；不改檔
    python tools/aimctl.py lock  --role R       # 建 work/.lock；已有未逾時鎖即 exit 3
    python tools/aimctl.py unlock
    python tools/aimctl.py beat  --role R --task T --result S   # 覆寫 query/MECH.md、追加 query/RUNLOG.tsv
    python tools/aimctl.py due                  # work/M_*.md 逾期未解析里程碑
    python tools/aimctl.py loadcheck [--role R] # 固定載入位元組數；> 30,000 exit 1
    python tools/aimctl.py fileid <id>          # 舊 Drive fileId → repo 路徑

佇列 query/QUEUE.md：每列 `| Q-#### | 角色 | 任務 | 輸入 | open/done | 建立日 | 建立者 |`。
各角色收尾時把 HANDOFF 寫成佇列列（取代交接給使用者）。pick 之優先序：
AUDITOR > ANALYST > SCOUT（佇列）> SCOUT-WATCH（配額內）> SCOUT-GEN（配額內）> IDLE。
"""
import argparse, csv, json, re, subprocess, sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
Q, LOG, MECH = ROOT / "query/QUEUE.md", ROOT / "query/RUNLOG.tsv", ROOT / "query/MECH.md"
LOCK, WORK = ROOT / "work/.lock", ROOT / "work"
TPE = timezone(timedelta(hours=8))           # 配額以台北日界計
LOCK_TTL = timedelta(hours=3)                 # 排程 2h；逾 3h 之鎖視為殘鎖
QUOTA = {"SCOUT-GEN": 2, "SCOUT-WATCH": 4}    # CHARTER §8
PRIO = {"AUDITOR": 0, "ANALYST": 1, "SCOUT": 2}
LOAD = {"SCOUT": ["AIM_CHARTER.md", "AIM_FUNNEL.md"],
        "ANALYST": ["AIM_CHARTER.md"], "AUDITOR": ["AIM_CHARTER.md"]}
CAP = 30_000
ROW = re.compile(r"^\|\s*(Q-\d+)\s*\|\s*(\w+)\s*\|([^|]*)\|([^|]*)\|\s*(open|done)\s*\|([^|]*)\|([^|]*)\|")


def now():
    return datetime.now(timezone.utc)


def queue():
    if not Q.exists():
        return []
    rows = []
    for line in Q.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if m:
            qid, role, task, inp, st, made, by = [x.strip() for x in m.groups()]
            rows.append(dict(id=qid, role=role, task=task, inputs=inp, status=st, made=made, by=by))
    return rows


def runs_today(kind):
    """今日（台北）已跑之某類輪數；RUNLOG 欄：utc, role, task, result, commit。"""
    if not LOG.exists():
        return 0
    today = now().astimezone(TPE).date()
    n = 0
    with LOG.open(encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            d = datetime.fromisoformat(r["utc"].replace("Z", "+00:00")).astimezone(TPE).date()
            if d == today and r["role"] == kind and r["result"] != "aborted":
                n += 1
    return n


def lock_state():
    if not LOCK.exists():
        return None
    try:
        t = datetime.fromisoformat(LOCK.read_text(encoding="utf-8").split()[0])
    except Exception:
        return "stale"
    return "held" if now() - t < LOCK_TTL else "stale"


def cmd_pick(a):
    if lock_state() == "held":
        print(json.dumps({"role": "SKIP", "why": "work/.lock 未逾時"}, ensure_ascii=False)); return
    open_rows = sorted((r for r in queue() if r["status"] == "open"),
                       key=lambda r: (PRIO.get(r["role"], 9), r["id"]))
    if open_rows:
        r = open_rows[0]
        print(json.dumps({"role": r["role"], "kind": r["role"], "queue": r}, ensure_ascii=False)); return
    for kind in ("SCOUT-WATCH", "SCOUT-GEN"):
        used = runs_today(kind)
        if used < QUOTA[kind]:
            print(json.dumps({"role": "SCOUT", "kind": kind, "quota_used": used,
                              "quota": QUOTA[kind]}, ensure_ascii=False)); return
    print(json.dumps({"role": "IDLE", "why": "佇列空且配額用罄"}, ensure_ascii=False))


def cmd_lock(a):
    if lock_state() == "held":
        sys.exit(3)
    LOCK.write_text(f"{now().isoformat()} {a.role}\n", encoding="utf-8")


def cmd_unlock(a):
    if LOCK.exists():
        LOCK.unlink()


def git(*args):
    try:
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    except Exception:
        return ""


def cmd_beat(a):
    ver = "unknown"
    m = re.search(r"AIM-C[\d.]+@\w+", (ROOT / "AIM_CHARTER.md").read_text(encoding="utf-8"))
    if m:
        ver = m.group(0)
    utc = now().isoformat(timespec="seconds").replace("+00:00", "Z")
    head = git("rev-parse", "--short", "HEAD")
    MECH.write_text("\n".join([
        "# MECH — 機械層心跳（aimctl beat 自動生成；手寫無效）",
        f"version: {ver}", f"role: {a.role}", f"task: {a.task}", f"result: {a.result}",
        f"last_run_utc: {utc}", f"prev_commit: {head}", ""]), encoding="utf-8")
    new = not LOG.exists()
    with LOG.open("a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        if new:
            w.writerow(["utc", "role", "task", "result", "commit"])
        w.writerow([utc, a.role, a.task, a.result, head])
    print("MECH", utc, a.role, a.result)


MROW = re.compile(r"^\|\s*(M-[\w′']+)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|")


def cmd_due(a):
    today = now().astimezone(TPE).date().isoformat()
    hits = []
    for p in sorted([*WORK.glob("M_*.md"), *(ROOT / "cards").glob("M_*.md")]):
        for line in p.read_text(encoding="utf-8").splitlines():
            m = MROW.match(line)
            if m and not m.group(6).strip() and m.group(2) <= today:
                hits.append(f"{p.name} | {m.group(1)} | {m.group(2)}")
    print("\n".join(hits) if hits else "無逾期未解析里程碑")


def cmd_loadcheck(a):
    files = LOAD.get(a.role, LOAD["SCOUT"])
    tot = 0
    for name in files:
        b = (ROOT / name).stat().st_size
        tot += b
        print(f"{name}: {b:,} B")
    print(f"合計 {tot:,} / {CAP:,}", "OK" if tot <= CAP else "超載 CHARTER §8")
    sys.exit(0 if tot <= CAP else 1)


def cmd_fileid(a):
    tsv = ROOT / "archive/FILEIDS.tsv"
    with tsv.open(encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r["fileId"] == a.id:
                cand = ROOT / "archive/drive" / r["title"]
                print(r["folder"], r["title"], str(cand.relative_to(ROOT)) if cand.exists() else "（repo 無副本；Drive 唯讀）")
                return
    sys.exit(f"{a.id} 不在 FILEIDS.tsv")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("pick").set_defaults(fn=cmd_pick)
    s = sub.add_parser("lock"); s.add_argument("--role", required=True); s.set_defaults(fn=cmd_lock)
    sub.add_parser("unlock").set_defaults(fn=cmd_unlock)
    s = sub.add_parser("beat")
    for k in ("role", "task", "result"):
        s.add_argument(f"--{k}", required=True)
    s.set_defaults(fn=cmd_beat)
    sub.add_parser("due").set_defaults(fn=cmd_due)
    s = sub.add_parser("loadcheck"); s.add_argument("--role", default="SCOUT"); s.set_defaults(fn=cmd_loadcheck)
    s = sub.add_parser("fileid"); s.add_argument("id"); s.set_defaults(fn=cmd_fileid)
    args = ap.parse_args(); args.fn(args)
