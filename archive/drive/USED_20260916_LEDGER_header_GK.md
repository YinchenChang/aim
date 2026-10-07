<!-- BY: PM@GK | MODEL: Grok Build【自報】 | CHARTER: AIM-C1.1 | NOTE: CL 不可用，GK 代行 PM | CONSUMES: CHARTER §2-6 §5 §8；aim_config.json 17pxTe8XkUvYInPgOf8rKq8d7CAHPiQkd | EMITS: LEDGER 標頭擬稿（正本 fileId 1uKfYqf1Dr3uyMTI84Sgq0Pw2gU4Ldlmm，須 drive_update／sync --role PM）；不發 EXECUTE -->
# LEDGER — 委託資本帳本（標頭；腳本生成段自起算日後覆寫本檔數字表，須保留本標頭）

**寫入：** 2026-09-16 PM@GK　**起算日：** 2026-10-15　**地位：** 標頭已指定；NAV 表空
**正本：** `AIM/pm/LEDGER.md` fileId `1uKfYqf1Dr3uyMTI84Sgq0Pw2gU4Ldlmm`

## 預設袋 ＝ 基準 (a)

| 權重 | 代號 | 名稱 | 備註 |
|---|---|---|---|
| 0.70 | VTI | Vanguard Total Stock Market ETF | 美股寬基；≠ (b) |
| 0.30 | IBIT | iShares Bitcoin Trust ETF | BTC ETF（§2-8）；取代 config 佔位 `BTC-USD` |

- 再平衡：§2-4 季切同日（每年 01-15／04-15／07-15／10-15）
- 基準 (b)：S&P 500 總報酬
- 委託資本上限：US$20,000 `[V-使用者]`（§2-1）
- 結算現金：≤ 池 NAV 5%；開倉保證金另計為該部位佔用
- 主動部位：無（起算前）

`aim_config.json` 之 `benchmark_a` 須改為 `{"VTI": 0.7, "IBIT": 0.3, "rebalance": "Q"}`，否則 `aim.py benchmark` 與預設袋裂開（CHARTER_HIST §3：(a) 以預設袋兩支 ETF 計）。本輪不新建 config 檔。

## 數字表（起算前）

**時間加權報酬：** —　**對數成長：** —

| 月末 | 現金 | 部位市值 | NAV | 部位 |
|---|---|---|---|---|
| — | — | — | — | — |

EXECUTE（資本轉入 US$20,000 ＋ VTI／IBIT 建倉）僅 2026-10-15 發。`cmd_ledger` 覆寫時必須保留「預設袋＝基準 (a)」表。

**（完）**
