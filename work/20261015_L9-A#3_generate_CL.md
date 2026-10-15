# L9-A#3 生成卡｜受規管 HITL：會計恆等（風險調整收入之變動對價——人審編碼之診斷存量 vs RADV 全量稽核與未連結病歷審查排除）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260921_L9-A_generate_GK.md；archive/drive/USED_20260922_L9-A_test1_GK.md；archive/work/20261007_L9-A#2_generate_CL.md；work/20261007_L9-A#2_test1_CL.md | EMITS: work/20261015_L9-A#3_generate_CL.md -->
**日期：** 2026-10-15　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain，配額 4／6）　**格：** L9-A　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L8-I#3 本日測一不通過）。非「已殺／刻意排除」格中最後測一最舊＝L9-A#2（2026-10-07，`work/20261007_L9-A#2_test1_CL.md`）；既有生成 2 份 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `RADV risk adjustment "Medicare Advantage" coding`，回 5 筆，皆為 GPU 折舊／快取命中率等無關模糊匹配，相關命中 0 筆；未使用。
- 比對（本卡須異型）：
  - **L9-A#1**（`archive/drive/USED_20260921_L9-A_generate_GK.md`；測一 `archive/drive/USED_20260922_L9-A_test1_GK.md`）：SaaS 每席次交付成本（推論＋支援）÷席次；死於席次與成本不同表。本卡不涉席次、不涉 AI COGS。
  - **L9-A#2**（`work/20261007_L9-A#2_test1_CL.md`）：Claritev PSAV 毛節省計費 vs 客戶端 IDR 回吐；死於否決 (2)：NSA／IDR 收入不分列。本卡逆轉方為 **CMS 公式本身**（風險分數輸入被稽核或被規則排除），收入對象為按人頭給付（capitation PMPM × RAF），非節省分成；分解變數為**診斷來源**（就診連結 vs 未連結病歷審查），且有已定日之規則變更（CY2027）。
  - C-A1（#6）、C-I5（#18）、L9-P（#1：核可率／HITL 工時）：不涉。L9-I／#2 屬誘因格，不比。
- §7-10 領域最近公開：CMS CY2027 Final Rate Announcement 2026-04-06（KFF 2026-04-08）；CMS RADV HPMS memo 2026-01-27；Humana v. Becerra（N.D. Tex. 2025-09-25 撤銷 2023 RADV 規則部分條文；CMS 2025-11-01 上訴，待決）；AGL 10-Q 2Q26（2026-08-05）。下一檢查點＝兩家 3Q26 10-Q（約 2026-11）、上訴判決、CY2028 Advance Notice（約 2027-02）。

## 1. 落差一句

風險承擔型醫療主體（MA 保險人與其下游之按人頭承包醫師組織）之收入＝Σ 成員 × PMPM × 風險分數（RAF）；RAF 由人審編碼（醫師紀錄 → 編碼員核定 HCC，近年大量以 AI 輔助、人工簽核）提交之診斷決定，按 ASC 606 以「most likely amount」入帳為變動對價。三個外生變動同時改寫該恆等式之輸入：① CMS 2025-05 宣布每年稽核全部 MA 合約（RADV），2026-01 memo 稱以 AI 加速人工病歷審查；② CY2027 起排除未連結就診之病歷審查診斷（KFF 估平均給付 −1.5%）；③ 外推法遭法院撤銷、上訴待決。種子主張：若某上市主體之 RAF 中來自未連結病歷審查或補編碼之比重顯著高於平均，則 2026 帳上之風險調整收入含有一段 2027 起失效之輸入，且稽核機率由抽樣升為全量而未見計提；讀者把 RAF 成長讀成病情組合或經營成果時，部分讀到的是編碼存量。**方向未定**：上訴勝敗決定外推是否回來；比重若接近業界平均，則已由 −1.5% 之公開估算定價。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：收入＝成員 × PMPM × RAF；RAF＝Σ 診斷係數；診斷可按來源分解（就診連結／未連結病歷審查／補編碼） |
| 已讀事實 | AGL 10-Q 2Q26：「The transaction price for the Company’s capitation contracts is variable, as the PMPM fees … are subject to periodic adjustment under CMS’s risk adjustment payment methodology」「Risk adjustment-related revenues are estimated using the most likely amount method」；「RADV」0 筆（10-Q）。AGL 10-K FY25：「For the 2027 plan year. CMS is proposing to exclude diagnoses identified in chart reviews (i.e., diagnoses not linked to a specific patient encounter)」；RADV 14 筆，皆風險段。ALHC 10-K FY25：RADV 19 筆；「chart review」0 筆；AI 用於住院／退保預測（AVA），非編碼。KFF：CY2027 已定案排除未連結病歷審查診斷，平均 −1.5%；總給付約 +5%。HMA：2026-01-27 memo「using AI … to streamline human coding reviews」；PY2020 起逐年稽核。Mintz：外推規則 2025-09-25 遭撤銷。 |
| 未證之連結 | 上市主體 RAF 中未連結病歷審查之占比；是否計提 RADV 回收；風險調整應收之期後調整（final sweep）歷史偏差 |
| 量綱 | 未連結病歷審查 RAF ÷ 總 RAF（無因次）；風險調整收入 ÷ 總收入（%）；RADV 計提 ÷ 風險調整應收（%）；期後調整 ÷ 原估（%） |
| 選擇變數 | 主體：病歷審查強度、AI 輔助編碼廣度；CMS：稽核樣本、外推、排除規則；法院：上訴 |
| 半衰期 | 規則變更一次性（2027-01-01）；RADV 回收 2–6 年遞延；final sweep 次年 |

## 3. B 端可觀測載體（只指名）

1. agilon health 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1831097/000162828026053355/agl-20260630.htm ；10-K FY25 https://www.sec.gov/Archives/edgar/data/1831097/000162828026011655/agl-20251231.htm
2. Alignment Healthcare 10-K FY25 https://www.sec.gov/Archives/edgar/data/1832466/000162828026012545/alhc-20251231.htm
3. KFF 2026-04-08 https://www.kff.org/quick-insights/medicare-advantage-insurers-will-see-higher-payments-as-cms-backs-off-a-key-payment-update/
4. HMA Weekly Roundup 2026-02-11 https://www.healthmanagement.com/insights/weekly-roundup-v2/february-11-2026/
5. Mintz 2025-10-01 https://www.mintz.com/insights-center/viewpoints/2146/2025-10-01-radv-odyssey-extrapolation-vacated
6. 未讀：Astrana（CIK 0001083446）、Privia、大型 MA 保險人之 10-K；CMS Final Rate Announcement 原文；具名賣方對各主體病歷審查依賴度之估算（如 HHS-OIG 2024 年病歷審查報告）。

缺段（§7-2）：各主體病歷審查診斷占比、RADV 計提；本輪只讀上列；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | CY2027 排除已定案並公告平均 −1.5%，2027 年費率整體 +5%，市場已據以調整 | 載體 3 | 已定價 |
| R2 | 外推被撤銷 → 非外推之 RADV 回收僅限樣本，量級小 | 載體 5 | 量級小 |
| R3 | 按人頭承包醫師組織之風險調整收入經保險人結算，RADV 回收是否轉嫁依合約；部分合約保險人自承 | 載體 1（風險段） | 機制轉嫁 |
| R4 | 主體不揭露診斷來源分解，則不可分列（同 L9-A#2 死因） | L9-A#2 測一 | 表達層 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) ≥ 2 家上市風險承擔主體之 10-K／10-Q／財報稿無法量化或代理其 RAF 中未連結病歷審查（或補編碼）之占比，亦無 RADV 計提或特定合約稽核揭露；或
(2) 可運作對照只能寫成 L9-A#2（收入基數 vs 客戶端回吐、收入不分列）或 L9-P（HITL 工時／核可率）而無診斷來源分解之結構；或
(3) `[D]` 量級：可得之最佳代理（主體特有之排除影響 − 業界平均 −1.5%，或 RADV 預期回收 ÷ 風險調整收入）< 1% 收入；或
(4) 12 個月內無可觀測驅動：上訴未決且 CMS 未公布 PY2020+ 稽核結果、無主體特有排除影響揭露；或
(5) 公司或具名賣方已逐家量化 CY2027 排除與 RADV 影響（已定價）。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：風險調整應收、變動對價限制、期後調整、或有負債。2. 可交易工具：MA 保險人／按人頭承包醫師組織（不選）。3. 半衰期：規則日 2027-01-01、RADV 結果公布時點。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L9［A］格加「#3 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0049。不改 L9-A#1／#2、L9-I／#2、L9-P、C-A1、C-I5 結論。
