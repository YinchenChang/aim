# L3-I#3 生成卡｜半導體製造測試：誘因（測試機台「指定者≠付款者」：設計商選平台與測試強度，OSAT／代工出資本支出並承擔稼動）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260926_L3-I_generate_GK.md；archive/work/20261009_L3-I#2_generate_CL.md；work/20261009_L3-I#2_test1_CL.md；work/20261016_L3-A#3_test1_CL.md；work/20261016_L3-P#3_test1_CL.md | EMITS: work/20261017_L3-I#3_generate_CL.md -->
**日期：** 2026-10-17　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L3-I　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。各格最後測試日最舊＝L3-I（#2 測一 2026-10-09）；其餘格皆 ≥ 2026-10-11。L3-I 非已殺、非刻意排除。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py tester ATE "test time" OSAT Teradyne Advantest`，命中 17 筆，皆為 GPU 機櫃功率／保固、模型與需求統計（SRC_HW_004/005/052、SRC_DC_015、SRC_DEM_*），與本卡無關，**未採用**。
- 比對之舊檔與死因型態，本卡須異型：
  - L3-I#1（`archive/drive/USED_20260926_L3-I_generate_GK.md`）：**產能預付款＝合約性排序權**（客戶↔代工，損失歸屬）。本卡不涉預付；物件為**設備選擇權與資本支出負擔之分離**。
  - L3-I#2（`archive/work/20261009_L3-I#2_generate_CL.md`）：政府股東認股權證＝分拆選擇權之或有稀釋。本卡無政府、無股權工具。
  - L3-A#3（`work/20261016_L3-A#3_test1_CL.md`）：OSAT 材料轉嫁／寄售之毛利率分母（會計恆等）。本卡之寄售指**測試設備**寄售，作為否決觸發 (2) 之反例，不涉毛利率分母。
  - L3-P#3（`work/20261016_L3-P#3_test1_CL.md`）：探針卡觸壓壽命守恆（物理消耗）。本卡不主張插入次數或消耗量，只主張**誰決定**測試強度與平台、**誰付**。
  - L4-I#2（加速器商表外回租／擔保）、C-I3′（UL 型）：物件不同。ARCH_dead 無「指定者／付款者分離」型。不併。
- §7-10 領域最近公開：Teradyne FY25 10-K（2026-02-19）、2Q26 10-Q（期末 2026-06-28，2026-07-31 申報）；Amkor FY25 10-K。下一檢查點＝Teradyne 3Q26 財報與 10-Q（約 2026-10 下旬至 11 初）；Advantest FY26 上半年結果（約 2026-10 下旬）。

## 1. 落差一句

Teradyne 10-K 明言其銷售有「specifying customer such as an OEM, IDM, or Fabless company, who chooses platforms and drives demand, and a purchasing customer who actually places the order and receives the equipment」；FY25 兩家**指定客戶**驅動 12% 與 10% 合併營收，另一家**直接採購客戶**占 19%（「including certain revenues specified by other customers」）。**落差＝選擇權與資本負擔分離**：設計商（AI 加速器、手機 SoC）決定測試平台與每顆測試強度（測試時間、插入次數），其邊際成本經每測試秒報價轉嫁、占 ASP 小；OSAT／代工出測試機資本支出並承擔稼動風險（Amkor 10-K：「focus our capital expenditures on standardized tester platforms」「In some cases, our customers will consign test equipment to us」）。故 ATE 需求之驅動者為少數指定者之平台與品質偏好，而非付款者之稼動經濟；以直接客戶口徑讀集中度或以 OSAT 資本支出週期讀 ATE 訂單，可能錯置風險（單一指定者換平台，同時移動多家付款者之訂單）。**方向未定**：可使 ATE 需求較 OSAT 週期鈍化（指定者不承擔稼動），亦可使其對單一指定者之平台切換更敏感。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因：委託—代理（指定者選、付款者付）；選擇成本外部化至付款者之資本支出與稼動 |
| 選擇者 | 設計商／OEM（平台、測試強度）；OSAT／代工（是否接受指定平台、要求寄售或預付、定價每測試秒）；ATE 商（以指定者為銷售對象） |
| 可見端 | Teradyne 10-K：指定／採購客戶定義、指定者 12%／10%、直接客戶 19%、前五大直接客戶 44%／36%／32%（2025／2024／2023）、應收 22%／20% 兩家；10-Q：「A few customers drive significant demand … through direct sales and sales to the customer's supply partners」。Amkor 10-K：標準化平台、客戶寄售測試設備、測試設備年限 5→7 年（「increased interchangeability」）、無重大 backlog、稼動影響毛利。二手：AI 加速器測試時間「well over 20 minutes」vs 手機 SoC 30–60 秒；測試成本占 ASP 約 2% → 5–7%；Advantest SoC 測試機份額 CY25 +10 個百分點 |
| 指名不可見端 | 指定者名稱與其平台切換史；OSAT 測試報價是否含平台專屬溢價或稼動保證；寄售 vs OSAT 自購之比重；指定平台之機台在 OSAT 帳上之再部署率 |
| 主張 | 指定者不承擔稼動與閒置，故其平台與測試強度選擇對 ATE 需求之影響未經付款者經濟過濾；集中度之經濟單位為指定者，非直接客戶 |
| 表達工具型態（只指名，不選券） | 美股上市 ATE 商普通股與上市選擇權；美股上市 OSAT。不選券 |

對照式（生成用，非正式載入）：`ATE 訂單 ≈ Σ_s [ 指定者 s 之量 × 每顆測試秒(s) ÷ 每機每年可用秒 × 平台份額(s) ]`；付款者稼動 `u` 不入指定者之決策式。本輪不估參數、不寫 H1。

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| Teradyne FY25 10-K（Sales and Distribution；Note V Significant Customer；應收集中） | https://www.sec.gov/Archives/edgar/data/97210/000119312526059002/ter-20251231.htm |
| Teradyne 2Q26 10-Q（「supply partners」句；分部營收） | https://www.sec.gov/Archives/edgar/data/97210/000119312526327715/ter-20260628.htm |
| Amkor FY25 10-K（Equipment 段寄售句；測試設備年限 5→7 年；稼動風險因子） | https://www.sec.gov/Archives/edgar/data/1047127/000104712726000014/amkr-20251231.htm |
| Teradyne 2Q26 二手摘要（Compute 占 SOC 70%、首張 merchant GPU 訂單、第二家超大規模客戶 correlation） | https://futurumgroup.com/insights/teradyne-q2-fy-2026-doubles-semiconductor-test-revenue-on-ai-compute-and-memory-demand/ |
| 測試時間與份額之二手（Wing VC，2026-05；測一須回 Advantest IR／Teradyne 法說原文） | https://wing.vc/content/the-chip-testing-bottleneck |
| Advantest IR Q&A（2026-07-29，日文；測一實讀） | https://www.advantest.com/document/ja/investors/ir-library/result/JE_BIZ_260729_QA.pdf |

不宣稱指定者將換平台、不宣稱市場以直接客戶口徑定價、不宣稱 ATE 需求鈍化或放大。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 已揭露：Teradyne 10-K 已分列指定者 12%／10% 與直接客戶 19%，集中度之經濟單位已公開 | Teradyne FY25 10-K Sales and Distribution | 落差已被揭露 |
| R2 | 付款者不承擔殘餘風險：客戶寄售測試設備，或預付／保量合約，使指定者即付款者 | Amkor FY25 10-K 寄售句；L3-I#1 預付型 | 委託—代理分離不成立 |
| R3 | 平台可攜：OSAT 聚焦標準化平台、測試設備可互換而延長年限，指定平台不擱淺付款者資本 | Amkor 10-K 5→7 年「increased interchangeability」 | 外部化成本小 |
| R4 | 份額移動已被具名分析以平台層歸因（Advantest +10pp） | Wing VC 2026-05（二手） | 無錯價 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) Teradyne（或 Advantest）申報／法說已逐期揭露指定者口徑集中度與其平台份額變化，且 ≥ 1 位具名賣方以指定者為單位建模 ATE 需求（R1、R4 成立）。
- (2) ≥ 1 家上市 OSAT 或代工之申報／法說顯示 AI 加速器測試設備主要為客戶寄售、客戶出資或附保量／預付條款（指定者＝付款者；R2）。
- (3) OSAT 申報顯示指定平台機台可跨客戶再部署、閒置或減損未見與單一指定者相關之事件（R3）。
- (4) 本卡只能以 L3-I#1 之預付取用權、L3-A#3 之寄售材料轉嫁、L3-P#3 之觸壓消耗、或 L4-I#2 之回租擔保重述（重疊判讀）。
- (5) 指定者口徑之量級：測一自定門檻並寫明（如指定者合計占 ATE 商營收之比、單一平台切換對營收之 `[D]` 量級），低於門檻即否決。
- (6) 平台資格認證與切換週期 < 12 個月或公開層不可見，使效果在重定價窗內不可辨。

複查觸發器（若日後殺）：Teradyne／Advantest 改變指定者揭露口徑或新增指定者 ≥ 10%；OSAT 揭露寄售測試設備比重或指定平台減損；具名賣方以指定者為單位建模。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：ATE 商營收與應收（直接客戶口徑）、指定者占比（敘述口徑）；OSAT 測試 PP&E、折舊年限、稼動敘述。
2. 可交易工具：美股 ATE 商與 OSAT 普通股及選擇權；Advantest 為東證主上市，非本池可交易範圍。
3. 半衰期：平台換代（新測試機世代）與 AI 加速器世代同步（約年度）；份額移動於年度市占報告可見。

## 7. 本輪寫入

本卡；QUEUE 新列（ANALYST 測一）；ARCH_matrix L3-I 格標「已生成 #3」；FUNNEL §3 未測格計數。不改 L3-I#1／#2、L3-A#1–#3、L3-P#1–#3、L4-I#2、C-I3′。
