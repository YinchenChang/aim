#!/usr/bin/env python3
# BY: PM@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: — | EMITS: tools/leads.py
"""tools/leads.py — 追加與檢查 export/LEADS_算力收支.md（CLAUDE.md §12、runbooks/SCOUT.md §D）。

  python tools/leads.py add --date 2026-10-23 --claim "<一句主張>" --value 1.2 --unit "GW" \
      --url https://... --grade "[V] 一手" --by "SCOUT@CL Q-0091"
  python tools/leads.py check        # 全檔重驗；有違規 exit 1（commit 前必跑）

拒收：出處為 YinchenChang/Tokenomics 或 YinchenChang/company-models（避免循環驗證）；
主張含部位、尺碼、金額配置、候選判斷或 AIM 候選代碼；出處非 http(s)；日期非 YYYY-MM-DD。
"""
import argparse
import os
import re
import sys

PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "export", "LEADS_算力收支.md")
HEAD = "| 登錄日 | 出處日期 | 主張 | 數值 | 單位 | 出處網址 | 來源等級 | 登錄者 |"
CIRC = re.compile(r"yinchenchang/(tokenomics|company-models)", re.I)
BANNED = re.compile(
    r"部位|尺碼|凱利|配置|加碼|減碼|買進|賣出|做多|做空|建倉|出場|目標價|評等|進 ?T\b|不進 ?T|候選|標的|權重|"
    r"\bH1\b|\bH5\b|LEDGER|EXECUTE|"
    r"\b(L\d{1,2}|C)-[PAI]\d*(#\d+)?\b", re.I)
GRADE = re.compile(r"^\[(V|I-[^\]]+|D)\]\s*(一手|二手)$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def problems(cells):
    reg, src_date, claim, value, unit, url, grade, by = cells
    out = []
    if not DATE.match(reg) or not DATE.match(src_date):
        out.append("日期須 YYYY-MM-DD")
    if not re.match(r"^https?://\S+$", url):
        out.append("出處須為單一 http(s) 網址")
    if CIRC.search(url) or CIRC.search(claim):
        out.append("出處為 Tokenomics／company-models（循環驗證，不寫）")
    if BANNED.search(claim) or BANNED.search(unit) or BANNED.search(value):
        out.append("含部位／尺碼／配置／候選判斷字樣或候選代碼")
    if not GRADE.match(grade):
        out.append("來源等級須為 `[V]`／`[I-<利害方>]`／`[D]` ＋ 一手／二手")
    if not value.strip() or not unit.strip():
        out.append("數值與單位必填")
    if any("|" in c for c in cells):
        out.append("欄位不得含 |")
    return out


def rows():
    with open(PATH, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if line.startswith("| 20"):
                yield i, [c.strip() for c in line.strip().strip("|").split("|")]


def cmd_check(_):
    bad = 0
    for i, cells in rows():
        p = problems(cells) if len(cells) == 8 else ["欄數須為 8"]
        if p:
            bad += 1
            print(f"L{i}: " + "；".join(p))
    print(f"# {'FAIL' if bad else 'OK'}: {bad} bad row(s)")
    sys.exit(1 if bad else 0)


def cmd_add(a):
    import datetime as dt
    cells = [a.reg or dt.date.today().isoformat(), a.date, a.claim, str(a.value), a.unit, a.url, a.grade, a.by]
    p = problems(cells)
    if p:
        sys.exit("拒收：" + "；".join(p))
    with open(PATH, encoding="utf-8") as f:
        txt = f.read()
    if a.url in txt and a.claim in txt:
        sys.exit("拒收：同出處同主張已登錄")
    with open(PATH, "a", encoding="utf-8") as f:
        f.write("| " + " | ".join(cells) + " |\n")
    print("ok")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("add")
    for k in ("date", "claim", "value", "unit", "url", "grade", "by"):
        s.add_argument(f"--{k}", required=True)
    s.add_argument("--reg", help="登錄日；預設今日")
    s.set_defaults(fn=cmd_add)
    sub.add_parser("check").set_defaults(fn=cmd_check)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
