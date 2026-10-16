# L3-P#3 生成卡｜半導體製造測試：守恆（探針卡觸壓壽命守恆：卡片消耗量 ＝ 總觸壓數 ÷ 每卡壽命觸壓數；HBM 晶圓測試插入次數上升使需求隨量而非隨設計）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260926_L3-P_generate_GK.md；archive/drive/USED_20260926_L3-P_test1_GK.md；archive/work/20261009_L3-P#2_generate_CL.md；work/20261009_L3-P#2_test1_CL.md | EMITS: work/20261016_L3-P#3_generate_CL.md -->
**日期：** 2026-10-16　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain，配額 6／6）　**格：** L3-P　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L1-I#3 已於本日測一）。非「已殺／刻意排除」格中最後測試日最舊＝2026-10-09（L3-P、L3-I）；依表序取 **L3-P**。既有生成 2 份 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `probe card`／`FormFactor`／`wafer sort`／`touchdown`，命中 0 筆。
- 比對（本卡須異型）：
  - **L3-P#1**（GK）：曝光機**機時守恆**產能上界；死於可觀測性（賣方只給認列台數與條件化 WPH）。本卡為**耗材壽命守恆**（觸壓數 ÷ 壽命），選擇者為測試耗材賣方與其客戶之測試流程，載體為**上市耗材商之按市場別分列營收**（DRAM 一列可對帳）。
  - **L3-P#2**：HBM 堆疊**良率乘積** → 晶圓投入比；死於方向已由 Micron 揭露並定價（trade ratio 上升、CY27 HBM 價格重設）。本卡不談晶圓投入或記憶體廠毛利，談**測試耗材之需求函數**（隨量 vs 隨設計）；記憶體廠之 trade ratio 只作輸入，不作落差。
  - L3-A#1–#3、L3-I#1／#2：會計／誘因，構成不同。ARCH_dead C-I3′／N-02（利益未分列）：本卡之載體已分列 DRAM 市場營收，非同型；HBM 子項未分列屬測一 (1) 題。
- §7-10 領域最近公開：FormFactor 10-Q 2Q26（期末 2026-06-27）；FormFactor 10-K FY25（期末 2025-12-27）；FormFactor SWTest 2026 部落格。下一檢查點＝FormFactor 3Q26 財報（約 2026-10 下旬至 11 初）；SK hynix 3Q26 法說（約 2026-10 下旬）。

## 1. 落差一句

探針卡為有限壽命之耗材：`N_cards ≈ Σ(晶圓數 × 每晶圓插入次數 × 每插入觸壓數) ÷ 每卡壽命觸壓數 ＋ 新設計首套`。公司口徑把 DRAM 成長歸因於「**HBM designs**」（10-Q 2Q26：「increased demand for high-bandwidth memory ("HBM") designs … approximately 75% … of the year-over-year increase in DRAM product revenues」；10-K：「our probe card products require that we develop custom designs for our customers' new product designs」），市場因此可能把 DRAM 探針卡讀成**設計週期驅動（世代切換時尖峰、其後回落）**。種子主張：若 HBM 核心晶粒之 KGD 要求（16 層堆疊使單晶粒逃逸代價放大）使每晶圓插入次數（多溫、at-speed）與晶圓數同時上升，則消耗量隨 **HBM 晶圓投入 × 插入次數** 增長，需求之持續性高於設計週期讀法。**方向未定**（壽命延長、平行度提升、一觸全片（one-touchdown）可使每晶圓消耗下降；10-K 自列「probe card lifetime」為競爭因素）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [P] 守恆：觸壓數守恆（總需觸壓 ＝ 卡片數 × 每卡壽命觸壓）；耗材流量 ＝ 測試量 ÷ 壽命 |
| 選擇者 | 記憶體廠（KGD 測試流程、插入次數、溫度點）；探針卡商（壽命、平行度、一觸全片）；HBM 客戶（堆疊高度與逃逸容忍度） |
| 已讀事實 | FORM 10-K FY25：DRAM 探針卡營收 247.4M（+8.8%）、FY24 227.4M（+99.9%）；「probe card lifetime」「frequency and effectiveness of any required cleaning」列為競爭因素；全文 grep「consumable」「touchdown」「wear」0 筆。10-Q 2Q26：DRAM 85.0M vs 57.1M（+49.0%），HBM 成長占 DRAM 年增約 75%（三個月）／69%（六個月）；營收認列「Products transferred at a point in time」為主 |
| 未證之連結 | 每卡壽命觸壓數與 HBM 每晶圓插入次數（公開數值）；耗材補貨 vs 新設計首套之營收占比；HBM 晶圓投入之年增；壽命延長／一觸全片對每晶圓消耗之抵銷幅度 |
| 量綱 | 卡片數／月 ＝ （晶圓／月 × 插入／晶圓 × 觸壓／插入）÷（觸壓／卡）；營收持續性以「DRAM 營收 ÷ HBM 晶圓投入」之期間變動衡量 |
| 半衰期 | 季至年（HBM 世代 12→16 層、HBM4 量產爬坡；壽命改良週期） |

## 3. B 端可觀測載體（只指名）

1. FormFactor 10-K FY25 https://www.sec.gov/Archives/edgar/data/1039399/000103939926000009/form-20251227.htm （市場別營收、競爭因素；已讀 §2 所錄）；10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1039399/000103939926000033/form-20260627.htm （DRAM 分列、HBM 占年增；已讀）；FORM 法說逐字稿（補貨／耗材口徑，未讀）。
2. 記憶體廠 HBM 晶圓投入與測試流程：SK hynix、Micron、Samsung 法說與技術發表（KGD、多溫測試；未讀）；Micron 10-K FY26（trade ratio，作輸入，未讀本卡用途段）。
3. 同業：Technoprobe（義大利上市）年報／半年報之 DRAM／HBM 與耗材口徑；MJC（日本）（未讀）。
4. 技術載體：SWTest 2026 FormFactor 發表 https://www.formfactor.com/blog/2026/driving-the-future-of-wafer-test-formfactor-at-swtest-2026/ ；COMPASS19「HBM Probing Challenges」https://compass.formfactor.com/wp-content/uploads/COMPASS19-Taiwan-HBM-Probing-Challenges-Liao.pdf ；one-touchdown 300 mm 燒機探針新聞稿 https://www.formfactor.com/?p=594 （未讀）。
5. 具名賣方對 FORM DRAM 營收之建模驅動（設計 vs 量；未讀）。

缺段（§7-2）：每卡壽命與插入次數之數值、補貨占比；本輪未讀；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 公司已把 HBM 成長分列並口述；需求函數之「量」成分已被市場知悉 | 載體 1（10-Q 量化 HBM 占年增） | 已定價 |
| R2 | 壽命延長、平行度與一觸全片使每晶圓消耗下降，抵銷插入次數上升 | 載體 1（競爭因素）、4 | 方向 |
| R3 | 探針卡為客製、按設計首套採購，補貨占比低；守恆式之耗材流量對營收不重要 | 載體 1（「custom designs for our customers' new product designs」） | 機制 |
| R4 | HBM 子項營收、每卡壽命與插入次數皆不揭露 → 不可對帳 | 載體 1、2 | 可觀測性 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 補貨／耗材 vs 新設計首套之營收占比，在申報、法說或具名可信估計中均不可得，且 HBM 每晶圓插入次數與每卡壽命無任何公開量級，致守恆式不可對帳；或
(2) 公司或具名同業明示 DRAM／HBM 探針卡營收主要為新設計首套（補貨占比低，R3 成立）；或
(3) 公開資料顯示每卡壽命或平行度之改良幅度 ≥ 插入次數上升幅度（R2 成立，方向對本卡之「隨量」讀法為零或負）；或
(4) `[D]` 量級：可估之 HBM 耗材補貨營收 < FORM 總營收 10%，或其變動不足以改變 DRAM 營收之持續性讀法；或
(5) 公司或具名賣方已以「量 × 插入 ÷ 壽命」或等價之耗材口徑揭露或建模 DRAM 探針卡需求（已定價，R1 成立）；或
(6) HBM 晶圓投入之年增率已公開且 FORM DRAM 營收與其同步（無落差：市場讀法與守恆式一致）。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Probe Cards 分部、DRAM 市場營收、point-in-time 認列、存貨與交期。2. 可交易工具：美股上市測試耗材商（不選）。3. 半衰期：季至年（HBM 世代；壽命改良週期）。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L3［P］格加「#3 已生成」；`AIM_FUNNEL.md` §3 句與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0057。不改 L3-P#1／#2、L3-A#1–#3、L3-I#1／#2、C-I3′、N-02、L1-I#3 結論。
