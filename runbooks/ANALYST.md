# ANALYST@CL 手冊（CHARTER §4：T／L／M；深挖須實際 fetch 並列 URL）

SEC 申報（10-K／10-Q／20-F／8-K）實讀一律 `python tools/sec.py doc <URL> --grep <詞>`，不用 WebFetch（CLAUDE.md §10）；全文讀取，不得再記「末 N 字未讀」。

固定載入：`AIM_CHARTER.md`＋該候選之生成卡／T／L／M（≤ 28 KB）。禁 LEDGER、任何 P、`aim-pm`。一輪只做 QUEUE 指定之一件事。

內部研究數字（CLAUDE.md §12）：`python tools/internal_numbers.py tok|cm …` 可取每 GW 參數與公司模型數字作對照；一律標 `[I-內部研究（算力收支）]`，衝突依證據規則處理、不優先，不得作 T 先驗之外部參照物；與原始出處同源者只計一個來源。

## 測一（任務「測一 <碼>」或「重測 <碼>」）
- 檔：`work/YYYYMMDD_<碼>_test1_CL.md`；結構沿用 `archive/drive/USED_*_test1_GK.md`：終態｜A 指名 B 端實讀（URL＋日期）｜B 次級路徑（10-K／10-Q 同檔分列）｜C 否決檢核（逐條 (1)…(k)：觸發／未觸發＋證據）｜D 本輪寫入／不寫入。
- 終態只四種：`測一通過｜進 T`、`測一通過｜不進 T`（附理由）、`測一部分通過｜不進 T`、`測一不通過｜不進 T`。
- 轉入個股層時必問三題（§7-4）：財報科目／可交易工具／半衰期。
- 寫入前確認該領域最近一次公開更新日期（§7-10）。
- 下一步：`進 T` → QUEUE 新增 `ANALYST`「寫 T <碼>」；否則不新增。`query/ARCH_live.md` 該碼全列、FUNNEL §1 該碼狀態欄（只寫狀態短語，不寫細節）與 ARCH_matrix 該格原地更新。

## T（任務「寫 T <碼>」；≤ 8 KB）
落差陳述、最強反方（具名出處＋URL）、機制型態與數值窗、競爭假說與 `N_d`、先驗（須有外部參照物）。檔 `work/YYYYMMDD_<碼>_T_CL.md`。不得由目標反推、不得以研究深度提高後驗（§1）。下一步：判斷進 L 者 → QUEUE「寫 L <碼>」；否則 FUNNEL 標「T 已寫｜不進 L」。

## L／M（凍結；各 ≤ 4 KB）
- L：機制參數（單位）、市場隱含值、第一原理值、載入恆等式、`H1`／`H5` 區間（`[A]`／`[AS]` 只給區間）、翻轉點、表達工具型態、流動性。量綱先於量級（§7-1）。
- M：`| M-x | YYYY-MM-DD | 來源 | 事前機率 p | 極性（「發生」定義釘死） | 結果(空) |`，檔名 `work/M_<碼>_CL.md`。
- 寫完即凍結。QUEUE 新增 `AUDITOR`「稽核 <碼> L／M；撰寫者 MODEL＝<你自報之模型>」。**ANALYST 不得自行稽核。**
- 稽核維持後，由 AUDITOR 輪 `git mv` 至 `cards/`；否決則 FUNNEL 標否決、檔移 `archive/work/`。

## 禁止
不選券、不寫尺碼與金額、不改他碼、不補章程未定義之參數（τ／s 等）、不把「檢索失敗」寫成「不存在」。
