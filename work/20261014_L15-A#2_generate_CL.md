# L15-A#2 生成卡｜基礎設施軟體與資料：會計恆等（遞延收入浮存——營業現金流中 Δ合約負債項隨開票時點由「年度預收」轉向「季度／月付後收」而機械縮小）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/FILEIDS.tsv；archive/drive/USED_20261007_L15-A_generate_GK.md；archive/drive/USED_20261007_L15-A_test1_GK.md | EMITS: work/20261014_L15-A#2_generate_CL.md -->
**日期：** 2026-10-14　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 2→3／6）　**格：** L15-A　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】或已生成未測格（L15-P#2 已於本日測一，Q-0041 done）。非已殺／刻意排除、無 #2 之格＝L15-A、L15-I；`archive/FILEIDS.tsv` 測一時間較舊＝L15-A（2026-10-07T10:57Z；L15-I 11:25Z）→ **L15-A**，#2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `billing`、`deferred revenue`，命中 0 筆。
- 比對（本卡須異型）：
  - **L15-A#1**（測一不通過，`archive/drive/USED_20261007_L15-A_test1_GK.md`）：營收＝使用量×有效單價；死因＝兩因子不能同檔並列。本卡不拆營收，只看**現金流恆等中之營運資金項**，每項皆為現金流量表單行。
  - **L13-A#2**（測一不通過）：Oracle 客戶預付之重大融資成分、資助資本支出。本卡不涉融資成分與 capex，主體為訂閱／消費制 ISV，變數為開票條件組合。
  - **L14-P#2**（測一不通過）：SNOW 預付容量池內 AI vs 非 AI 消耗分配。本卡不分池內用途，只看預收與後收之時點。
  - **L14-A#2**（費用化／資本化分流）、**C-A1**（AI COGS 分列）、**L6-A#2**（電力轉嫁）、**L10-A#2**（商戶浮存，分發層）、**L15-P#2**（市集抵扣）：不涉。L10-A#2 同屬「浮存」，但為旅遊中介之商戶預收，非軟體合約負債，層不同、恆等項不同。
  - 已殺 L8-P／L9-P／L11-P、C-A3／C-A4：不涉。
- §7-10 領域最近公開：各主體 10-Q（CRWD 2026-08-27、DDOG 2026-08-06、MDB 2026-09-01、SNOW 2026-09-04）；ASC 606 合約負債定義無 2026 年變動（未檢得變更，非不存在）。

## 1. 落差一句

市場以 FCF 利潤率（或 EV／FCF）為基礎設施軟體之估值錨；種子主張：其 OCF 中相當比例為 Δ合約負債（預收浮存），而 AI 時代之消費制／信用點數／「依消耗開票」使年度預收比例下降，浮存項機械縮小——同營收、同利潤之下 FCF 利潤率下修。錯價只在把浮存當經常性盈餘。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等**：OCF ≡ NI＋非現金項（SBC、折舊）＋ΔCL（合約負債）− ΔAR（含未開票）＋其他營運資金。穩態下 ΔCL ≈ g·CL；CL ≈ b·R（b＝預收開票占營收之週期份額）。開票條件由年度預收轉向季付／月付後收 → b↓ → ΔCL 一次性負衝擊＋穩態 ΔCL 下降，同時未開票 AR↑ |
| 量綱 | 美元／期；b、g 無量綱；ΔCL／OCF、ΔCL／R 無量綱 |
| 選擇變數 | 客戶：要求依消耗付款；ISV：開票條件、信用點數之預收與否 |
| 可見端 | 現金流量表「Increase (Decrease) in Contract with Customer, Liability」（XBRL 逐季累計）；資產負債表遞延收入、未開票應收；10-K 開票條件敘述 |
| 指名不可見端 | 合約層開票條件組合（年付／季付／月付後收之金額分配） |
| 表達工具型態（只指名） | 美股可交易、ΔCL 占 OCF 高之基礎設施軟體商。不選券 |

**不主張方向、不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. XBRL `IncreaseDecreaseInContractWithCustomerLiability` 與 OCF（`sec.py facts`，10-K 年度，百萬美元）：CRWD FY26 1,024／1,612；SNOW FY26 755／1,222；DDOG FY25 273／1,050；MDB FY26 112／505。ΔCL／OCF `[D]` ≈ 64%／62%／26%／22%。
2. Snowflake 10-K FY26 https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm （sec.py 實讀）：「Under capacity arrangements, from which a majority of our revenue is derived, we typically bill our customers annually in advance of their consumption. However, in future periods, we expect to see an increase in capacity contracts providing for quarterly upfront billings and monthly in arrears billings as our customers increasingly want to align consumption and timing of payme[nts]」。
3. MongoDB 10-K FY26 https://www.sec.gov/Archives/edgar/data/1441816/000162828026016799/mdb-20260131.htm ：Atlas「73% of our total revenue」；self-serve「charged monthly in arrears based on their usage」；銷售簽約者「pay in advance or are invoiced monthly in arrears」。
4. CrowdStrike 10-K FY26 https://www.sec.gov/Archives/edgar/data/1535527/000153552726000010/crwd-20260131.htm ：grep `Flex` 未見 Falcon Flex 開票條款（檢索失敗，非不存在；待測一以電話會補）。

缺段（§7-2）：未取 ≥ 4 期季度 ΔCL 單季值（XBRL 為年初至今累計，須差分 `[D]`）；未取任何具名賣方以浮存調整 FCF 之原文；CRWD Flex 開票條件未取得。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | ΔCL ≈ g·CL：浮存縮小主因為成長放緩，非開票條件；兩者在申報層不可分 | 恆等本身；SNOW FY25 ΔCL 383 → FY26 755（§3-1）隨成長回升 | 可分離性 |
| R2 | 市場已以「billings」「cRPO」並列 FCF 追蹤，浮存已被定價 | 待測一指名賣方原文 | 已定價 |
| R3 | 改為季付／月付後收之客戶多屬容量合約續約，浮存轉為未開票 AR，現金僅延後一季，量級小 | Snowflake 10-K（§3-2）「quarterly upfront」 | 量綱過小 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法就 ≥ 2 家美股上市基礎設施軟體商，自 10-Q／10-K 取得 ≥ 4 期季度 ΔCL（或遞延收入期末額）與 OCF 同口徑並列，且無法就其中 ≥ 1 家取得開票條件變動之申報或電話會原文；或
(2) 可運作對照只能寫成使用量×單價（L15-A#1）、預付池內用途分配（L14-P#2）、重大融資成分／capex（L13-A#2）、費用化分流（L14-A#2）、商戶浮存（L10-A#2）或 AI COGS 分列（C-A1）；或
(3) 具名賣方已以「剔除 ΔCL 之 FCF」或 billings 調整量化並為市場所引用（已定價）；或
(4) `[D]` 量綱不可連接：開票條件由年付轉季付之一次性 ΔCL 衝擊 < 指名主體 OCF 之 10%；或 R1 成立（申報層無法區分成長效果與開票條件效果）；或
(5) 12 個月內無可觀測驅動：無開票條件變動之揭露、無季度 ΔCL／未開票 AR 變化。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：ΔCL（現金流量表）、遞延收入、未開票應收、cRPO。2. 可交易工具：ΔCL／OCF 高之 ISV（不選）。3. 半衰期：年度合約續約週期（約 1 年），衝擊在續約年內兌現。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L15［A］格加「#2 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0042。不改 L15-A#1、L15-P#1／#2、L15-I、L13-A#2、L14-P#2、L14-A#2、L10-A#2、C-A1 結論。
