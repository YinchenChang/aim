# L15-I#3 生成卡｜基礎設施軟體與資料：誘因（收購方收割誘因——不可終止多年約把俘虜裝機基之價格上調前置認列；客戶轉換誘因受 18–24 個月遷移時滯約束，首波三年約於 2027 到期時才被綁定）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261007_L15-I_generate_GK.md；archive/work/20261014_L15-I#2_generate_CL.md；work/20261014_L15-I#2_test1_CL.md；archive/work/20261021_L15-P#3_generate_CL.md；archive/work/20261021_L15-A#3_generate_CL.md；archive/work/20261014_L15-P#2_generate_CL.md；archive/work/20261014_L15-A#2_generate_CL.md | EMITS: work/20261022_L15-I#3_generate_CL.md -->
**日期：** 2026-10-22　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 0→1／6）　**格：** L15-I　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。不主張任何主體價值方向。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 全表已測、已生成未測 0 格。非已殺／刻意排除之格中，最後測試日最舊＝L15-I（#2 測一 2026-10-14；其餘格最舊者 2026-10-15）→ **L15-I**，#3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `VMware`、`Broadcom`、`Nutanix`、`virtualization`，命中 0 筆。選格先於查線索。
- 比對（須異型）：
  - **L15-I#1**（`archive/drive/USED_20261007_L15-I_generate_GK.md`；測一不通過，否決(1)）：遙測出站費使取用權為結構性。本卡不涉資料出站或保留期。
  - **L15-I#2**（`archive/work/20261014_L15-I#2_generate_CL.md`；測一不通過，否決(4) R1 支）：雲端商出資相容開源引擎，以替代品報價封頂 ISV 託管價差。死因＝申報層無法把流失歸因於相容替代。本卡主體相反：**在位收購方對俘虜裝機基之收割誘因**（提價、捨棄中小客戶、以不可終止多年約鎖定），替代品報價不是機制；機制之時鐘是合約到期與遷移時滯。
  - **L15-A#2**（遞延收入浮存）、**L15-A#3**（託管成本轉嫁毛利恆等）：會計恆等。本卡之 upfront license 僅作誘因之可觀測後果，不以恆等式為主張。
  - **L15-P#2**（市集承諾池）、**L15-P#3**（觀測份額上限）、**L14-I#3**（承諾內再分配）：守恆／承諾池。不涉。
  - **L4-I#3、L7-P#3**（Broadcom 半導體 XPU）：同主體、不同分部與機制。不改。
  - 已殺 L8-P／L9-P／L11-P、C-A1–C-A5、C-I1–C-I5、VEEV：不涉。`grep VMware|Nutanix` 全 repo 0 筆。
- §7-10 領域最近公開：AVGO 10-Q 3Q FY26（期末 2026-08-02，提交 2026-09-10）；NTNX 8-K FY26 財報（2026-08-26）；Channel Insider 2026-06-11；Trefis 2026-05-26；heise／CloudBolt 調查（2026-01 執行）。

## 1. 落差一句

市場把 Broadcom 基礎設施軟體分部之成長（3Q FY26 單季 +29%）讀成 VCF 需求與定價權之持續；種子主張：收購方之誘因是對俘虜裝機基收割（提價、退出中小客戶、接受流失以極大化留存者利潤），並把新約改為**不可終止多年約**，使授權部分**前置一次認列**；客戶之轉換誘因真實但受 18–24 個月遷移時滯約束，首波三年過橋約（2024 初轉換）於 **2027 年初**到期時才第一次被綁定。分部成長之相當部分是認列時點與俘虜提價，不是裝機基擴張。可拒絕之主張＝存在可並列序列顯示分部增量主要來自 upfront license，且續約期之流失或降配可觀測而市場以分部成長外推。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因**：賣方選擇〔提價幅度 × 合約可終止性 × 客戶分層〕以極大化鎖定期現值；客戶選擇〔續約／部分遷移／雙平台〕，受遷移成本與時滯約束。兩方誘因在續約點交會 |
| 量綱 | upfront license 增量 ÷ 分部營收增量（%，`[D]`）；續約時之客戶保留率／核心數保留（%）；遷移時滯（月）；首波到期日（`[V]`） |
| 選擇變數 | 賣方：價格、T4C 條款、目標客戶數；客戶：續約核心數、遷移比例；第三方：雲端商遷移補貼 |
| 可見端 | AVGO 10-Q 分部營收、upfront license 揭露、合約負債中 T4C 占比、RPO；NTNX ARR／新客戶數；調查與報導之續約時點 |
| 指名不可見端 | VMware 單獨營收（分部含 CA／Symantec 等）；續約保留率；客戶層價格變化 |
| 表達工具型態（只指名） | 美股可交易之在位基礎設施軟體收購方或其替代供應商。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. AVGO 10-Q 3Q FY26 https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm （sec.py 實讀）：「Infrastructure software 8,752 6,786 1,966 29 %」（百萬美元，單季）；「we included upfront license revenue of $ 3,465 million and $ 7,184 million」，並重分類去年同季「$ 1,916 million」→ upfront 增量 1,549 ÷ 分部增量 1,966 ≈ 79% `[D]`（單季，一期，非序列）；「primarily due to strong demand for our VMware Cloud Foundation (“VCF”) product, including additional license revenue recognized on contracts where customers do not have the right to terminate. As of the fiscal quarter ended August 2, 2026, we no longer have termination for convenience provisions for the majority of new software contracts.」；「approximately 58 % of contract liabilities related to contracts subject to termination for convenience provisions」；「the timing and extent of renewals and relative volume of customer contracts without the right to terminate causes variations in revenue recognized」。
2. NTNX 8-K Ex.99.1（2026-08-26）https://www.sec.gov/Archives/edgar/data/0001618732/000117184326005752/exh_991.htm ：ARR「$2.55 billion $2.20 billion 16%」；「added over 3,000 new customers」；新聞稿未把新客戶歸因於 VMware（只指名）。
3. Channel Insider 2026-06-11（David Curry）https://www.channelinsider.com/infrastructure/vmware-renewals-broadcom-migration-alternatives/ ：「a new wave of contracts set to expire in early 2027」；客戶「typically partially migrate some systems or run them on dual platforms」。
4. heise（CloudBolt 調查 n=302，2026-01）https://heise.de/-11193449 ：完全替換 4%、86% 正在縮減用量；遷移相依「18 to 24 months」；Gartner 預測份額約 70%（2024）→ 約 40%（2029）（次級轉述，未實讀 Gartner 原文）。
5. Trefis 2026-05-26 https://www.trefis.com/articles/600381/broadcoms-hidden-risk-vmware-under-pressure/2026-05-26 ：2026–2027 續約期為「first real test」；前 2,000 大客戶流失 10–15% 之情境（無出處）。
6. 只指名未實讀：CISPE 對 VMware 授權之歐盟申訴與臨時措施；AVGO 4Q FY26 10-K（約 2026-12）。

缺段（§7-2）：未取 ≥ 4 期 upfront license 與分部營收並列序列；未取首波合約到期分布之一手（申報或公司說法）；未取任何續約保留率；VMware 與 CA／Symantec 未分離。失敗歸因＝本輪只讀一期 10-Q，非不存在。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 大逃亡未發生：完全替換 4%；60% 對 VMware 策略信心高於 2024 | heise／CloudBolt（§3-4） | 客戶誘因不綁定 |
| R2 | 不可終止約本身延長鎖定：2027 到期者若已以多年不可終止約提前續約，續約點後移出 12 個月窗 | AVGO 10-Q（§3-1）；Redress Compliance 早續約研究（未讀） | 無驅動 |
| R3 | 續約期風險已被具名點出並情境化 | Trefis 2026-05-26 | 已定價 |
| R4 | 分部成長亦來自真實 VCF 私有雲／私有 AI 需求 | AVGO 10-Q 歸因句 | 可分離性 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法就 AVGO 取得 ≥ 4 期（單季，年初至今差分 `[D]`）分部營收與 upfront license 並列（sec.py），且無法取得首波合約到期時點之一手或具名來源；或
(2) 可運作對照只能寫成相容替代品封頂價差（L15-I#2）、出站／保留期（L15-I#1）、遞延收入／開票時點恆等（L15-A#2）、RPO／認列恆等本身（滑入 A 格）、承諾池（L15-P#2／L14-I#3）；或
(3) 具名賣方或研究機構已以續約保留率 × upfront 占比量化分部營收並為市場引用（已定價；R3 須判是情境或建模）；或
(4) `[D]` 量綱不可連接：≥ 4 期 upfront 增量 ÷ 分部增量 < 30%，或 VMware 不可自分部分離致歸因不成立；或
(5) 12 個月內無可觀測驅動：首波到期已大量提前續成不可終止多年約（R2），無續約揭露、無歐盟裁定、無替代供應商可歸因之轉換；或
(6) 客戶側證據（NTNX、雲端商、調查 ≥ 2 期）顯示轉換誘因於窗內不綁定（R1 成立）。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：分部營收、upfront license、T4C 合約負債占比、RPO。2. 可交易工具：在位收購方或替代供應商（不選）。3. 半衰期：首波續約時點與遷移時滯。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L15［I］格加「#3 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列。不改 L15-I#1／#2、L15-A#1–#3、L15-P#1–#3、L14-I#3、L4-I#3、L7-P#3 結論。
