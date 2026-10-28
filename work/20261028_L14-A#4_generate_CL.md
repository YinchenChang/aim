# L14-A#4 生成卡｜企業終端需求：會計恆等（AI 專項簽約之滾存：未轉換餘額 U_t ≡ U_{t−1} ＋ 簽約 B_t − 認列營收 R_t ± 取消／匯率；累計「AI book of business」為存量而非流量——當專項口徑停揭，B/R 轉換率與未轉換餘額不再可觀測）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261005_L14-A_generate_GK.md；archive/work/20261013_L14-A#2_generate_CL.md；archive/work/20261021_L14-A#3_generate_CL.md；work/20261021_L14-A#3_test1_CL.md；work/20261013_L14-A#2_test1_CL.md | EMITS: work/20261028_L14-A#4_generate_CL.md -->
**日期：** 2026-10-28　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 5→6／6）　**格：** L14-A　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L14-P#4 測一 2026-10-28，Q-0121 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-21（L2-P、L2-A、L14-A、L14-I、L15-P、L15-A）；其中既有生成數最少（3）且延續 L14 輪序者＝**L14-A** → #4。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `bookings backlog "book of business" consulting`，0 筆；未用。內部數字（§12）未取。
- 比對之舊檔與死因型態，本卡須異型：
  - **L14-A#1**（`archive/drive/USED_20261005_L14-A_test1_GK.md`）：IT 支出 ÷ 營收；死因＝同一申報無法並列 IT 支出、營收與 AI 行。本卡不用買方 IT 支出，樞紐為**賣方（系統整合／顧問）之 AI 專項簽約與 AI 專項營收**兩流量及其滾存。
  - **L14-A#2**（`work/20261013_L14-A#2_test1_CL.md`）：費用化／資本化分流；死因＝分列僅 1 家、量級 < 10%。不涉。
  - **L14-A#3**（`work/20261021_L14-A#3_test1_CL.md`）：重組排除項 GAAP／調整後橋接；死因＝否決 (1)，同口徑並列不足且再現多為非 AI 計畫。本卡不涉成本端。
  - **L14-I#1–#3、L14-P#1–#4**（裁員理由、席次、承諾池、人工處理量、PC 汰換）：不涉。
  - **C-A2**（ARCH_dead #9）：不主張單位經濟。**C-I5**（ARCH_dead #18，cohort NRR）：不涉留存。
  - **L13-P#4**（供應商 RPO 對單一對手方預算約束）：彼為算力供應商對 OpenAI；本卡為企業買方對 SI 之 AI 專案，主體與方向不同。
- §7-10 領域最近公開：Accenture Q4 FY26 8-K 新聞稿（申報 2026-09 下旬）、Accenture Q4 FY26 電話會議逐字稿（singjupost 2026-10-03 刊）；IBM Q4 2025 新聞稿（2026-01-28）；Trefis（2026-07-30）。下一檢查點＝Accenture Q1 FY27（約 2026-12 中旬）、IBM Q4 2026（約 2027-01 下旬）、Accenture FY26 10-K RPO 附註（已申報 2026-10-16，待測一讀）。

## 1. 落差一句

市場以「AI 簽約／book of business」之累計值讀企業 AI 終端需求；種子主張：此類數字為**存量（累計簽約）**，與營收流量之關係受恆等式 U_t ≡ U_{t−1} ＋ B_t − R_t 約束——Accenture FY25 AI 簽約 $5.9B、AI 營收 $2.7B（B/R ≈ 2.2），IBM 累計 book of business > $12.5B（含軟體交易與顧問簽約混合口徑）；兩家均於 2025 年末後不再單列（Accenture FY26 改以「AI 與資料夥伴」併組敘述，IBM 自 2026 年起未再提），故自 FY26 起 B/R 與 U 不再可由公司口徑重算。可拒絕之主張＝在專項口徑仍可得之期間，`[D]` 轉換率 R/B 與未轉換餘額 U 之走勢，與停揭後整體 book-to-bill／RPO 所能推得之 AI 成分，存在可量化、市場未讀之落差；若 U 可由整體 RPO 附註或其他一手口徑重建、或停揭後賣方已以整體 RPO 替代讀數（R2），本卡死。本卡不主張任何主體營收或股價方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等（A）**：(i) \(U_t \equiv U_{t-1} + B_t - R_t \pm C_t\)（C＝取消、範圍縮減、匯率）；(ii) 累計口徑：\(BoB_t = \sum_{s\le t} B_s\)（若含已認列者則 \(U_t = BoB_t - \sum R_s\)）；(iii) 轉換率 \(\rho_t = R_t / B_{t-k}\)，k＝專案平均認列期；(iv) 整體：\(RPO_t \equiv RPO_{t-1} + Book_t - Rev_t \pm\)，AI 份額 \(a_t = U_t / RPO_t\) |
| 選擇者 | 賣方管理層（AI 專項之定義邊界、是否單列、何時停揭、累計 vs 年度口徑） |
| 可見端 | 電話會議逐字稿之 AI 專項簽約與營收（停揭前）；8-K 新聞稿之總簽約與 book-to-bill；10-K／10-Q 之 RPO 附註（ASC 606）與認列時程 |
| 指名不可見端 | 停揭後之 AI 專項 B、R；取消 C；IBM 口徑中軟體交易 vs 顧問簽約之拆分 |
| 量綱 | 美元／期（B、R）、美元（U、BoB、RPO 為存量）；ρ、a 無因次；k 為期數 |
| 外部參照物（測一查證） | 系統整合業過去專項口徑（如雲端遷移、數位轉型）之單列→停揭先例及其後營收走勢 |
| 表達工具型態（只指名，不選券） | 美股、揭露 AI 專項簽約之 IT 服務／顧問商普通股；不選券 |
| 重疊 | L14-I 型（停揭之誘因）可能為下一型；本卡只用金額與恆等，不判讀停揭動機 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Accenture Q4 FY25 電話會議逐字稿（2025-09-25）https://www.investor.accenture.com/~/media/Files/A/Accenture-IR-V3/quarterly-earnings/2025/q4-fy-25/accenture-fourth-quarter-fiscal-2025-conference-call-transcript.pdf ：「In FY25, we tripled our revenue over FY24 from Gen AI and increasingly agentic AI to $2.7 billion.」「And we nearly doubled our Gen AI bookings to $5.9 billion.」「these numbers only reflect revenue and bookings specifically related to advanced AI」；Q&A「we'll think about how to share that」。
2. Accenture Q4 FY26 8-K 新聞稿（sec.py）https://www.sec.gov/Archives/edgar/data/0001467373/000146737326000037/q4fy26earnings8-kexhibit.htm ：「New bookings for fiscal 2026 were $84.54 billion … with a book-to-bill of 1.1」「Revenues for fiscal 2026 were $74.18 billion」；新聞稿全文無 AI 專項簽約或營收數字（grep `advanced AI|AI|bookings` 實讀，僅見風險因子與公司簡介）。
3. Accenture Q4 FY26 電話會議逐字稿 https://singjupost.com/transcript-accenture-plc-acn-q4-2026-earnings-call/ ：emerging AI and data partners「bookings more than tripled and revenue more than doubled compared with fiscal 2025」；「we will now report our top 10 ecosystem partners and emerging AI and data partners together as one group」；未見 AI 專項簽約／營收金額（二手轉錄，測一以官方逐字稿核對）。
4. IBM Q4 2025 新聞稿（2026-01-28）https://newsroom.ibm.com/2026-01-28-IBM-RELEASES-FOURTH-QUARTER-RESULTS ：「Our generative AI book of business now stands at more than $12.5 billion.」定義含「Consulting signings related to specific offerings」；未拆軟體／顧問。
5. 停揭錨（二手）：Trefis 2026-07-30 https://www.trefis.com/stock/ibm/articles/609339/ibm-swapped-its-ai-scoreboard-for-a-quantum-one/2026-07-30 ：管理層稱該季「would be the last quarter reporting the metric separately」，其後兩季未提。

缺段（§7-2）：未取 Accenture FY24 AI 簽約／營收原文（僅由「tripled」「nearly doubled」反推）；未讀 Accenture FY26 10-K 與 IBM 10-K 之 RPO 附註；未找到賣方以累計 AI 簽約讀需求之具名原文；未查其他 SI（Cognizant、Infosys、Capgemini、Deloitte 非上市）是否仍單列。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 停揭因 AI 已嵌入幾乎所有專案，專項口徑失去區分力，非隱藏轉換惡化 | Accenture Q4 FY25「we'll think about how to share that」；需測一找管理層明確理由 | 落差為定義性，非資訊性 |
| R2 | 市場已改讀整體 book-to-bill 與 RPO；AI 專項為敘事指標，不入估值 | Accenture Q4 FY26 新聞稿 book-to-bill 1.1（§3-2） | 已定價／無關 |
| R3 | 量級：Accenture AI 營收 $2.7B ÷ FY25 營收約 4% | §3-1 `[D]` | 轉換率變動不足以重定價 |
| R4 | IBM 口徑混合軟體交易（即時認列）與顧問簽約（遞延），恆等式 (i) 不可同口徑套用 | §3-4 | (ii) 不成立 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後 < 2 家主體能於一手口徑（逐字稿官方版、8-K、10-K／10-Q）取得 ≥ 3 期之 AI 專項簽約 B 與 AI 專項營收 R 同口徑並列（年度或季度皆可）；或
(2) `[D]` 停揭前之 ρ（R/B，取 k＝0 與 k＝1 兩版）期間變動 < 10 個百分點、或 U ÷ 主體總 RPO < 3%（量級不足）；或
(3) 具名賣方、公司原文或評等機構已以整體 RPO／book-to-bill 重建或替代 AI 專項讀數，或管理層停揭理由原文明確為定義失效（R1）且有可驗證之替代口徑（已定價或無資訊）；或
(4) 可運作對照只能寫成 IT 支出 ÷ 營收（L14-A#1）、費用化／資本化（L14-A#2）、重組排除項（L14-A#3）、停揭動機（L14-I 型）、席次／承諾池／人工處理量／PC 汰換（L14-P#1–#4）或供應商對單一對手方 RPO（L13-P#4）；或
(5) 12 個月內無檢驗事件（Accenture FY27 各季、IBM 2026 年報 RPO 附註、任一主體恢復單列或新主體開始單列）；或
(6) 唯一可用主體之 B 口徑為累計且混合即時與遞延認列（R4），使 (i) 不可 `[D]`。

複查觸發器（若日後殺）：任一 SI 恢復單列 AI 專項簽約與營收；10-K RPO 附註首次分列 AI 相關剩餘履約義務；SEC 意見函要求說明停揭之 KPI。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：新簽約（非 GAAP 營運指標）、營收、RPO 附註。2. 可交易工具：揭露 AI 專項之 IT 服務商普通股（不選）。3. 半衰期：專案認列期（季至數年）；揭露頻率每季。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0122；`query/ARCH_matrix.md` L14［A］加「#4 已生成」；`AIM_FUNNEL.md` §3 一句與日期行；`export/LEADS_算力收支.md` 3 列（Accenture FY25 AI 營收／簽約、IBM 累計 book of business）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L14-A#1–#3、L14-I#1–#3、L14-P#1–#4、C-A2、C-I5、L13-P#4 結論；不恢復 L11-P／L8-P／L9-P；不寫 T。
