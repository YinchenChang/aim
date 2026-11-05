# L2-P#6 生成卡｜資料中心實體：守恆（加速器—通電容量之存量守恆：`I_dark,t+1 = I_dark,t + S_t·w − ΔK_energized,t`；已出貨加速器之功率需求若超過同期新增通電 IT MW，差額必以「未上電存量」累積於買方資產負債表，而市場以出貨／營收讀「已部署算力」）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/work/20261007_L2-P#2_generate_CL.md；archive/work/20261014_L2-P#3_generate_CL.md；archive/work/20261021_L2-P#4_generate_CL.md；archive/work/20261029_L2-P#5_generate_CL.md；archive/work/20261026_L6-P#4_generate_CL.md；work/20261026_L6-P#4_test1_CL.md；work/20261015_L12-P#3_test1_CL.md | EMITS: work/20261105_L2-P#6_generate_CL.md -->
**日期：** 2026-11-05　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 3→4／6）　**格：** L2-P　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額配置、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L15-I#5 已測，Q-0167 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-29（L2-P#5、L2-A#5、L2-I#5；L15-I#4 已由 #5 更新至 11-05）；依表序取第一 → **L2-P**。既有生成 #1–#5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `placed in service`、`inventory energized`，0 筆；未用。內部數字（§12）未用。
- 比對（須異型）：
  - **L2-P#1**（PUE 受濕球封頂）、**L2-P#2**（每櫃 kW 受散熱介質封頂）、**L2-P#3**（訓練負載時域擺盪）：皆設施內之物理上界；本卡為**跨層存量**（硬體件數 × 瓦 vs 通電 MW），不涉散熱、PUE 水準或電氣動態。
  - **L2-P#4**（MW 口徑：接入 vs critical IT）：本卡須用單一口徑（critical IT MW），口徑換算為測一之前置，不是樞紐。
  - **L2-P#5**（單一主體在建存量 → 12 個月 RFS 指引之上界）：其存量為**建築物**，流量為交付 MW；本卡之存量為**已交貨未上電之加速器**，流量為晶片出貨，L2-P#5 之 MW 交付僅為本卡之匯（sink）。L2-P#5 若成立則加大本卡之 `I_dark`，但兩者可分別否證。
  - **L6-P#2**（RPO 認列 ≤ ∫ 通電 MW × 每 MW 營收）：營收端；本卡不用 RPO 或 ρ。
  - **L6-P#4**（`work/20261026_L6-P#4_test1_CL.md`，否決 (1)：氣冷／液冷 MW 不可觀測）：該卡引 Nadella「chips sitting in inventory」作載體，樞紐為冷卻型態存量；本卡不分冷卻型態。
  - **L12-P#3**（`work/20261015_L12-P#3_test1_CL.md`，出口管制下出貨地 vs 落地容量之轉運差額）：其差額為**地理再出口**；本卡為需求地本地之**時間差**（未上電在庫），不涉轉運。死因 (1)「出貨地列示不可觀測」同型風險列為本卡否決 (1)。
  - **L4-P#3**（HBM 位元守恆）、**L6-A#3**（CIP 折舊管線，會計）：前者為上游供給、後者為損益時點；本卡為物理件數平衡，CIP 只作觀測載體。
  - ARCH_dead #19 C-P4（水）、L1-P（刻意排除 T-11）：不涉。
- §7-10 領域最近公開：NVDA 10-Q 2Q FY27（2026-08-26）；META、MSFT 10-Q（2026-09-30 季，2026-10-22／10-28）；SemiAnalysis「Datacenters 2027」（2026-10-19，二手轉述）。下一檢查點＝NVDA 3Q FY27 10-Q（約 2026-11 下旬）。

## 1. 落差一句

件數—功率守恆：已交貨加速器只有三個去處——上電運轉、未上電在庫（買方倉儲或 CIP）、報廢，故 `Σ S_t·w·PUE ≤ ΔK_energized + ΔI_dark·w·PUE`。NVDA 2Q FY27 Data Center 營收 $89.0B（+117%），供應承諾自 $119B 增至 $279B；以 BofA 口徑（每 MW 開發成本約 $49M、其中 IT 設備約 78%，經 KuCoin 轉述 Reuters 2026-10-23）作錨，單季 NVDA DC 營收隱含 ≥ 約 2.3 GW critical IT 之硬體 `[D]`（NVDA 占 IT 設備支出 < 100%，故為下界），年化 ≥ 約 9 GW，僅單一供應商。同期需求方一手語句：Microsoft CEO「you may actually have a bunch of chips sitting in inventory that I can't plug in」（2025-11，Tom's Hardware 等報導；原文待測一回訪談逐字稿）；SemiAnalysis 研究員稱「obtaining GPUs has become easier than securing sufficient power」（二手）；IDC 稱約 7 GW 美國 2026 規劃容量因電力不足延後或取消（二手）。Meta CIP 自 $50.5B（2025-12-31）增至 $89.5B（2026-09-30），附註「mostly related to construction of data centers, servers and network infrastructure」——伺服器與建物未分列。可拒絕之主張＝以同一 critical IT 口徑，某一 ≥ 2 季窗內之加速器出貨隱含 MW 顯著大於同窗通電 MW 增量（差額 ≥ 出貨隱含 MW 之 15%），且買方未上電硬體不可由市場常用指標（供應商營收、資本支出、「deployed」敘述）分辨；若出貨隱含 MW ≤ 通電增量，或買方已分列未上電硬體，本卡死。方向未定：差額可能於通電追上時被吸收（延後而非損失），亦可能於世代更替時轉為減損。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆（P）**：件數與功率之存量—流量平衡；`I_dark` 為唯一可容納差額之存量（報廢可忽略於 ≤ 2 年窗） |
| 量綱 | 件數（GPU 封裝或機櫃）× 每件全系統瓦 `w`（kW）→ critical IT MW；PUE 只在換算接入 MW 時用 |
| 選擇者 | 買方（超大規模／新雲）之採購時點 vs 通電時點；供應商出貨認列（交貨即認列） |
| 可見端 | 供應商 DC 營收與存貨、供應承諾；買方 CIP、「servers and network assets」、尚未起租租約；通電容量聚合者（CBRE／SemiAnalysis／IDC） |
| 指名不可見端 | 買方未上電加速器件數或金額（未分列）；每期新增通電 critical IT MW 之一手全球值 |
| 表達工具型態（只指名，不選券） | 加速器供應鏈與超大規模／新雲普通股；不選券 |
| 重疊 | L2-P#5（匯端）、L12-P#3（地理差額）、L6-A#3（損益時點） |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. NVDA 10-Q 2Q FY27（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm ：「Data Center revenue was $89.0 billion, up 117% from a year ago」；供應承諾「from $ 119 billion last quarter to $ 279 billion」；存貨 $31,575M（2026-01-25 為 $21,403M）。
2. META 10-Q 3Q26（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm ：Note 6 CIP $89,499M vs $50,521M；Servers and network assets $133,626M vs $98,040M；「Construction in progress includes costs mostly related to construction of data centers, servers and network infrastructure」。
3. MSFT 10-Q 1Q FY27（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm ：「additional leases, primarily for datacenters, that had not yet commenced of $ 364.6 billion」；風險因子「Limitations in power availability, delays in obtaining power connections … could restrict our ability to develop or expand datacenter capacity」。
4. 二手（測一須回原文）：KuCoin 轉述 SemiAnalysis「Datacenters 2027」（2026-10-19）https://www.kucoin.com/blog/ai-data-center-overcapacity-gpu-supply-2028 ——2027 全球新增 > 50 GW、2028 末相對可用晶片約 10 GW 容量**過剩**（方向與本卡相反，列 R1）；Benzinga／Yahoo（2025-12-18）https://finance.yahoo.com/news/michael-burry-asks-photos-warehoused-223107967.html ——X 使用者 Kakashii 估「6 million GPUs … would require 8.5 to 11 gigawatts」vs 美國 2024–25 新增約 8.5 GW（未驗證，只作反方／同向線索，不作證據）。
5. Microsoft CEO 語句：二手 https://www.techradar.com/pro/you-may-actually-have-a-bunch-of-chips-sitting-in-inventory-that-i-cant-plug-in-satya-nadella-admits-an-embarrassing-shortcoming-so-lets-hope-it-doesnt-set-the-company-back-in-the-ai-arms-race （Tom's Hardware 原頁 fetch 失敗：URL 過長被代理拒）。

缺段（§7-2）：每件全系統瓦 `w` 之一手（NVDA GB300 NVL72 規格頁）未取；全球／美國季度新增通電 critical IT MW 之一手或具名聚合者原文未取；買方未上電硬體之任何分列未見；AMD、自研 ASIC 出貨未計。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 容量將過剩而非晶片過剩：2028 末約 10 GW 資料中心容量相對晶片過剩 | SemiAnalysis（二手 KuCoin 2026-10-26） | 符號相反（→(2)） |
| R2 | 營收 ≠ 件數：NVDA 營收含網路、軟體與預付／整櫃之 ODM 時差；每 MW 硬體價高於 BofA 平均則隱含 MW 下降 | NVDA 10-Q；BofA | 量級不足（→(2)） |
| R3 | 未上電在庫為短暫在途（交貨至上電 1–2 季之正常管線），非可累積之錯配 | 買方法說（待測一實讀） | 存量穩定（→(2)） |
| R4 | 市場已知並已追蹤（Burry／Kakashii 之「warehoused」爭論、賣方 GPU-vs-power 模型） | Benzinga 2025-12-18；具名賣方（待測一） | 已定價（→(3)） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 出貨端（NVDA ≥ 4 季 DC 營收或件數＋一手每件全系統瓦或每 MW 硬體成本錨）或通電端（同窗 ≥ 4 季新增通電 critical IT MW 之一手或具名聚合者原文，口徑可對齊）任一無法以 `[V]` 或可錨定 `[A]` 區間取得；或
(2) `[D]` 同窗（≥ 2 季）`(出貨隱含 MW − 通電 MW 增量) ÷ 出貨隱含 MW` < 15%（含 R2 之營收→件數折算區間取不利端；門檻凍結於此）；或
(3) 任一主要買方（MSFT、META、GOOGL、AMZN、ORCL、CRWV）10-Q／10-K 已分列「未上電／未投入使用之伺服器」金額，或具名賣方原文已以同口徑量化出貨 vs 通電差額；或
(4) 差額之匯可證為非本地在庫（轉運、出口 → L12-P#3 型），或為建物在建（→ L2-P#5 型）而非硬體在庫；或
(5) 可運作對照只能寫成 L6-P#2（營收—MW）或 L6-A#3（CIP 折舊時點）；或
(6) 12 個月內無檢驗事件（NVDA 3Q FY27–2Q FY28 10-Q、買方 2026 10-K PP&E 附註、聚合者 2027 年中容量報告）。

複查觸發器（若日後殺）：任一超大規模／新雲首次分列未投入使用之伺服器或 GPU；NVDA 首次揭露出貨件數或客戶在庫；聚合者首次發布季度通電 critical IT MW 序列。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：PP&E 附註（CIP、servers）、存貨、供應承諾、減損。2. 可交易工具：加速器供應鏈／超大規模普通股（不選）。3. 半衰期：通電追上之季數（1–4 季）或世代更替減損（Rubin 量產）。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0168；`query/ARCH_matrix.md` L2［P］加「#6 已生成」；`AIM_FUNNEL.md` §3 一句與日期行；`export/LEADS_算力收支.md` 2 筆（Meta CIP、NVDA 存貨）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L2-P#1–#5、L6-P#2、L6-P#4、L12-P#3、L4-P#3、L6-A#3；不碰 L1-P；不寫 T。
