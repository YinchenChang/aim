# L6-P#3 生成卡｜雲端與基礎設施服務：守恆（可互換機群之容量分割守恆：`K_t = K_ext + K_1P + K_RD`，外部雲成長率＝供給受限下之分配殘差）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260928_L6-P_generate_GK.md；archive/drive/USED_20260928_L6-P_test1_GK.md；archive/drive/USED_20260929_L6-P_T_GK.md；archive/work/20261011_L6-P#2_generate_CL.md；work/20261011_L6-P#2_test1_CL.md | EMITS: work/20261018_L6-P#3_generate_CL.md -->
**日期：** 2026-10-18　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 2／6）　**格：** L6-P　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L5-I#3 本日測一，Q-0065 done）。最後測試日最舊＝2026-10-11（L6-P#2、L6-A#2、L6-I#2、L13-A#2）；依表序取 **L6-P**；非已殺、非刻意排除。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py Azure allocation first-party capacity`，回 3 筆，相關 1 筆（SRC_DEM_018：OpenAI 於 Azure 之推論帳單，二手、文件未公開）；只作「去哪找」，未取數值，本卡未以之為載體。
- 比對之舊檔與死因型態，本卡須異型：
  - **L6-P#1**（T `archive/drive/USED_20260929_L6-P_T_GK.md`）：同步作業 MTTF∝1/N（可靠度守恆）。本卡守恆量＝**機群容量於用途間之分割**，非可靠度。
  - **L6-P#2**（`archive/work/20261011_L6-P#2_generate_CL.md`；(1) 觸發）：RPO 交付之 MW·h 上界，死於 ρ 不可界定。本卡不需 ρ、不換算 MW；只用「總量固定時一用途之增＝他用途之減」，可觀測端為管理層之分配反事實與分部營收。
  - **L6-I#2**（Oracle 計酬誘因）、**L6-A#2**（電費轉嫁）、**L13-A／#2**（租約、預付）、**C-A3／C-A4**（折舊年限）：不同型。
  - 重疊列為否決 (4)。
- §7-10 領域最近公開：Microsoft FY26 10-K（期末 2026-06-30，申報 2026-07-29）；FY26 Q4 法說 2026-07-29；Alphabet Q2 2026 法說 2026-07-22。下一檢查點＝Microsoft FY27 Q1 法說與 10-Q（約 2026-10 下旬）、Alphabet Q3 2026（約 2026-10 下旬）。

## 1. 落差一句

供給受限期，可互換之 CPU／GPU 機群滿足守恆 `K_t = K_ext + K_1P + K_RD`（外部雲客戶＋自家應用＋研發）。外部雲成長率（Azure KPI）因此是**分配殘差**，不是需求讀數。Microsoft CFO 已給一個反事實點（FY26 Q2，2026-01-29）：若 Q1–Q2 上線之 GPU 全數配給 Azure，KPI「would have already exceeded 40%」（報導轉述）；FY26 Q4 法說：「think about that infrastructure as being pretty fungible」「Customer demand continues to exceed available capacity」；FY26 10-K：「we may modify capacity allocations, deployment priorities, pricing」。種子主張：只要約束仍綁，外部雲 KPI 之季變動主要反映 `K_1P＋K_RD` 之變動與上線時點，而非外部需求；約束解除之季，KPI 之意義改變（由分配殘差轉為需求讀數）。本卡不定方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（容量分割；總量於季內近乎固定，用途間互斥）；非會計恆等、非誘因（分配由管理層決定，但約束本身為守恆） |
| 選擇者 | 管理層之分配（Nadella：依「optimal long-term LTV portfolio」分配，報導轉述）；本卡不論分配動機，只論守恆對 KPI 之含意 |
| 可見端 | Microsoft 法說之反事實與「fungible」句；Azure 成長率（FY26 Q4 43%、全年 41%、FY27 Q1 指引約 45%）；「added another gigawatt of capacity this quarter」「roughly double our overall capacity in just 2 years」；10-K 分部營收（Intelligent Cloud vs Productivity and Business Processes）；10-K 風險因子之分配句；Alphabet：「still in a supply-constrained environment」、Q3 增用第三方容量 |
| 指名不可見端 | 各用途之容量份額 `K_ext／K_t`；自家 Copilot 與研發用量（10-K「GPU」0 筆）；反事實點只有一季一點 |
| 對照式（生成用） | `g_ext ≈ g_K + Δ(K_ext／K_t)／(K_ext／K_t)`（價格與組合不變時）。可拒絕：若 `K_1P＋K_RD` 份額上升之季 Azure KPI 未受壓，或管理層反事實與分部營收不一致 |
| 表達工具型態（只指名，不選券） | 美股超大規模雲（Microsoft；次為 Alphabet、Amazon）。不選券 |
| 重疊 | L6-P#2（容量上界，但不同守恆量）；L6-I#2（backlog 與計酬）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Microsoft FY26 10-K（風險因子分配句；分部附註）。https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm （`sec.py` 本輪：「capacity constraint」5 筆、「GPU」0 筆）
2. Microsoft FY26 Q4 法說逐字稿（2026-07-29）。https://www.fool.com/earnings/call-transcripts/2026/08/07/microsoft-msft-q4-2026-earnings-call-transcript/
3. Microsoft FY26 Q2 法說反事實之報導（2026-01-29）。https://www.itiger.com/news/1159749691 ；官方活動頁 https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2 （測一須取官方逐字稿原文）
4. Alphabet Q2 2026 法說摘要（2026-07-22）。https://www.marketbeat.com/instant-alerts/alphabet-q2-earnings-call-highlights-2026-07-22/
5. 測一須另取：Microsoft FY26 Q1–Q3 與 FY27 Q1 法說之分配原文序列；10-Q 分部營收與 Microsoft Cloud 毛利率；Amazon／Alphabet 是否有任何分配反事實原文；具名賣方是否以分配份額建模 Azure KPI；訓練叢集與推論叢集之可互換性原文（硬體世代、地點）。**不宣稱已錯價。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 管理層已公開反事實，市場已據以讀 KPI（共識） | Microsoft FY26 Q2 法說（#3）；FourWeekMBA「the Hidden 40%+ Story」等二手 | 落差消失 |
| R2 | 「fungible」只對推論成立；研發訓練叢集不可互換，分割不綁 | 待原文 | 守恆不成立 |
| R3 | 約束將解除（容量兩年倍增），殘差解讀只剩數季 | Microsoft FY26 Q4（#2） | 半衰期過短 |
| R4 | KPI 變動主要由合約組合與上線時點決定，非分配 | Hood：「Azure growth rates can vary quarter-to-quarter based on capacity timing and contract mix」（#2） | 被相鄰驅動 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 用途份額或反事實於 ≥ 2 季不可得（只有 FY26 Q2 一點），使守恆無可並列之時間序列（量綱／可觀測性失敗）。
(2) 具名賣方或研究機構原文已以容量分配份額建模外部雲 KPI，使落差為共識（R1 原文須實讀）。
(3) 管理層原文確認需求已不超過供給（約束不綁），或約束解除時點早於 12 個月重定價窗。
(4) 可運作對照只能寫成 MW·h 交付上界（L6-P#2）、計酬誘因（L6-I#2）、預付／租約會計（L13-A／#2）或可靠度（L6-P#1）。
(5) 原文顯示訓練與推論／外部雲機群不可互換（世代、地點、網路拓撲），使分割不構成守恆（R2）。
(6) 只有單一主體（Microsoft）有分配原文，且 KPI 季變動經原文主要歸因於上線時點與合約組合（R4）。

複查觸發器（若日後殺）：任一美股超大規模雲於法說或申報給出第二個分配反事實或用途份額；10-K／10-Q 首次揭露 GPU 容量或用途分割；管理層宣告供給不再受限。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Intelligent Cloud 分部營收、Azure 成長率（非 GAAP KPI）、Microsoft Cloud 毛利率、資本支出與融資租賃、研發費用。
2. 可交易工具：Microsoft、Alphabet、Amazon 美股與選擇權。
3. 半衰期：季度法說；約束解除時點（管理層稱容量兩年倍增）為上界；`[V]` 不寫。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L6［P］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L6-P#1／#2、L6-A#1／#2、L6-I#1／#2、L13-A／#2、C-A3／C-A4 結論。
