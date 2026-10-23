#!/usr/bin/env python3
# BY: PM@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: YinchenChang/Tokenomics (model/CURRENT)；YinchenChang/company-models (*/dist/*.xlsx) | EMITS: tools/internal_numbers.py
"""tools/internal_numbers.py — 內部研究（算力收支）數字，唯讀（CLAUDE.md §12）。

只輸出「數字」：標籤、單位、數值、工作表!儲存格、檔名、commit。
不輸出任何文字結論、論點、投資標的、評等；估值類工作表與列一律排除。
每一行輸出都帶來源標記 [I-內部研究（算力收支），非獨立來源]。

用法：
  python tools/internal_numbers.py tok  <詞…>            # Tokenomics IF_／L1_ 具名範圍（版本＝model/CURRENT）
  python tools/internal_numbers.py tok  --list            # 列出全部 IF_／L1_ 名稱
  python tools/internal_numbers.py cm   --list            # 列出公司與其最新 dist 成品
  python tools/internal_numbers.py cm   <公司> <詞…>      # 該公司最新 dist xlsx 之數值儲存格（排除估值類）
  詞＝不分大小寫之子字串，比對名稱／標籤／單位；多詞為 OR。--n 限筆數（預設 40）。
"""
import argparse
import datetime as dt
import glob
import os
import re
import subprocess
import sys

TAG = "[I-內部研究（算力收支），非獨立來源]"
BASE = "/home/claude/yinchenchang"
REPOS = {"tok": ("https://github.com/YinchenChang/Tokenomics", f"{BASE}/tokenomics"),
         "cm": ("https://github.com/YinchenChang/company-models", f"{BASE}/company-models")}

# company-models：不取之工作表（估值／敏感度／檢查／來源轉錄／他模型或 Tokenomics 之副本／說明頁）
SKIP_SHEET = re.compile(
    r"^(README|導覽|摘要|Val|Valuation|評價_.*|Reverse|反向.*|.*可比.*|Sens.*|Sensitivity|Checks|檢查_.*|"
    r"Sources|來源|SRC_.*|TK_Link|OAI_Link|Tokenomics_取數|Feedback|Requests|_Defaults|Map_.*|公司實況驗證)$",
    re.I)
# 任何工作表中，標籤含下列詞之列一律不取（估值、評等、投資標的類）
SKIP_LABEL = re.compile(
    r"目標價|評等|評價|估值|估計價|合理價|機率加權|上檔|下檔|潛在報酬|買進|賣出|持有|加碼|減碼|"
    r"target|rating|upside|downside|valuation|fair value|price target|DCF|P/E|EV/|本益比|股價淨值|"
    r"implied price|multiple", re.I)


def clone(key):
    url, dest = REPOS[key]
    if not os.path.isdir(os.path.join(dest, ".git")):
        os.makedirs(BASE, exist_ok=True)
        env = dict(os.environ, GIT_LFS_SKIP_SMUDGE="1")
        subprocess.run(["git", "clone", "-q", "--depth", "1", url, dest], check=True, env=env, timeout=600)
    head = subprocess.run(["git", "-C", dest, "rev-parse", "--short", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    return dest, head


def num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def hit(terms, *fields):
    blob = " ".join("" if f is None else str(f) for f in fields).lower()
    return not terms or any(t in blob for t in terms)


def header(repo, head, path):
    print(f"# {TAG}")
    print(f"# source: {repo} @ {head} | file: {path} | extracted: {dt.date.today()}")
    print("# 只作數字；衝突依 AIM 證據規則（不因內部而優先）；不得作 T 先驗之外部參照物；AUDITOR 不得使用")


def cmd_tok(a):
    import openpyxl
    dest, head = clone("tok")
    cur = open(os.path.join(dest, "model", "CURRENT")).read().strip()
    wb = openpyxl.load_workbook(os.path.join(dest, "model", cur), data_only=True)
    names = sorted(n for n in wb.defined_names
                   if (n.startswith("IF_") and not n.startswith("IF_Hdr")) or n.startswith("L1_"))
    header(REPOS["tok"][0], head, f"model/{cur}")
    if a.list:
        print("\n".join(names)); return
    def rng(n):
        s, r = next(iter(wb.defined_names[n].destinations))
        c = wb[s][r]
        return s, r, (c if isinstance(c, tuple) else ((c,),))
    gen = [c.value for c in rng("IF_HdrGen")[2][0]] if "IF_HdrGen" in wb.defined_names else []
    cost = [c.value for c in rng("IF_HdrCost")[2][0]] if "IF_HdrCost" in wb.defined_names else []
    terms = [t.lower() for t in a.terms]
    print("名稱 | 標籤 | 單位 | 世代／情境 | 數值 | 位置")
    k = 0
    for n in names:
        s, r, cells = rng(n)
        row0 = cells[0][0]
        ws = wb[s]
        label = ws.cell(row0.row, 1).value
        unit = ws.cell(row0.row, 2).value if s == "Interface" else ws.cell(row0.row, 3).value
        if not hit(terms, n, label, unit):
            continue
        for row in cells:
            for i, c in enumerate(row):
                if not num(c.value):
                    continue
                col = c.column - 3
                gc = f"{gen[col]}／{cost[col]}" if s == "Interface" and 0 <= col < len(gen) else "—"
                print(f"{n} | {label} | {unit} | {gc} | {c.value:.6g} | {s}!{c.coordinate}")
        k += 1
        if k >= a.n:
            break
    print(f"# {k} name(s)")


def latest_dist(dest):
    out = {}
    for f in glob.glob(f"{dest}/**/dist/*.xlsx", recursive=True):
        if "_待刪除" in f:
            continue
        co = os.path.relpath(os.path.dirname(os.path.dirname(f)), dest)
        if co not in out or os.path.basename(f) > os.path.basename(out[co]):
            out[co] = f
    return out


def cmd_cm(a):
    import openpyxl
    dest, head = clone("cm")
    dist = latest_dist(dest)
    if a.list or not a.terms:
        header(REPOS["cm"][0], head, "*/dist/")
        for co, f in sorted(dist.items()):
            print(f"{co} | {os.path.relpath(f, dest)}")
        return
    co, terms = a.terms[0], [t.lower() for t in a.terms[1:]]
    if co not in dist:
        sys.exit(f"unknown company '{co}'; run: cm --list")
    f = dist[co]
    header(REPOS["cm"][0], head, os.path.relpath(f, dest))
    wb = openpyxl.load_workbook(f, data_only=True)
    print("工作表 | 標籤 | 欄首 | 數值 | 位置")
    k = 0
    for ws in wb.worksheets:
        if SKIP_SHEET.match(ws.title):
            continue
        hdr = {}
        for row in ws.iter_rows():
            texts = [c for c in row if isinstance(c.value, str) and c.value.strip()]
            nums = [c for c in row if num(c.value)]
            if texts and not nums and len(texts) >= 2:
                hdr = {c.column: c.value.strip() for c in texts}   # 最近一列純文字＝欄首
                continue
            if not nums:
                continue
            label = " ".join(c.value.strip() for c in texts[:2])[:80]
            if not label or SKIP_LABEL.search(label):
                continue
            for c in nums:
                colh = hdr.get(c.column, "")
                if SKIP_LABEL.search(colh) or not hit(terms, label, colh, ws.title):
                    continue
                print(f"{ws.title} | {label} | {colh} | {c.value:.6g} | {ws.title}!{c.coordinate}")
                k += 1
                if k >= a.n:
                    print(f"# {k} cell(s) (truncated)"); return
    print(f"# {k} cell(s)")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    for name, fn in (("tok", cmd_tok), ("cm", cmd_cm)):
        s = sub.add_parser(name)
        s.add_argument("terms", nargs="*")
        s.add_argument("--list", action="store_true")
        s.add_argument("--n", type=int, default=40)
        s.set_defaults(fn=fn)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
