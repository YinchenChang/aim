# L10-P#3 生成卡｜分發與中介：守恆（自駕車隊容量守恆：聚合平台之自駕行程 ≤ Σ 夥伴已部署車數 × 單車日行程上界；城市需求守恆下，開發商自營 App 行程自聚合平台人駕行程中扣出）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260930_L10-P_generate_GK.md；archive/drive/USED_20260930_L10-P_test1_GK.md；archive/work/20261013_L10-P#2_generate_CL.md；work/20261013_L10-P#2_test1_CL.md | EMITS: work/20261020_L10-P#3_generate_CL.md -->
**日期：** 2026-10-20　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 4→5／6）　**格：** L10-P　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L7-I#3 本日測一，Q-0072 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-13（L10-P、L10-A、L10-I、L11-A、L11-I、L13-P、L13-I、L14-P、L14-A）；依表序取 **L10-P**。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py robotaxi Uber Waymo autonomous`，命中 0。載體全由本輪 WebSearch／WebFetch／sec.py 實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L10-P#1**（測一不通過）：端側能量／殼溫上界分流功能；死因＝留端 vs 回雲功能類不可並列。本卡不論裝置能量。
  - **L10-P#2**（測一不通過，(4) 觸發）：需求側通道守恆（room nights ≡ Σ 通道），承接價入行銷費用率。本卡守恆量為**供給側之實體車隊容量**（車數 × 日行程），不經行銷費用率；若實讀後只能寫成「通道份額 × 單價」即滑回 #2（否決 (4)）。
  - **L10-A**（轉介量 × 分潤率不可並列）、**L10-A#2**（商戶預收浮存）：本卡不論分潤或浮存。
  - **L10-I**（預設份額與選擇次數不可並列）、**L10-I#2**（導出佣金路由）：本卡之 Uber 派單「配到自駕可改人駕」屬預設，但守恆約束不需預設份額——上界只用車數與單車利用率。
  - **L11-P**（死 #3）：不論注意力。不恢復。
- §7-10 領域最近公開：Uber 2Q26 10-Q 與 prepared remarks（2026-08-05）；AV Market Strategist（2026-08-10）；Waymo 拉斯維加斯無人上線（Electrek 2026-07-08）。下一檢查點＝Uber 3Q26 10-Q（約 2026-11 初）、Waymo 年底 1M／週目標。

## 1. 落差一句

恆等骨架：`T_AV,Uber(t) ≤ Σ_i N_i(t) · u_i`（`N_i`＝夥伴 i 於 Uber 已部署車數；`u_i`＝單車日行程，Uber 自稱「mid to high 20s, low 30s」）；城市 c 內 `D_c ≈ T_human,c + T_AV,Uber,c + T_dev-app,c + T_其他`，需求短期守恆 ⇒ 開發商自營 App 行程增量須自他項扣出。已見數點：Uber Q2 Trips 3,867M（含 Delivery，約 42.5M／日［D］）；夥伴「committed approximately 120,000 vehicles … over the coming years」（承諾，非部署）；AV 7 城、年底至多 15 城；Waymo 約 500k 付費行程／週、車隊約 3,000–3,500（Electrek 自相矛盾），即約 20–24 行程／車／日［D］。種子主張：市場以「夥伴數、承諾車數、城市數」計 Uber 之自駕聚合價值，而實體上界只隨**已部署車數**爬升——120k 輛全數上線 × 30 ≈ 3.6M／日 ≈ 現 Trips 之 8.5%［D］；1,000 輛 ≈ 0.07%［D］——承諾到部署之時間路徑決定窗內可兌現量；反向地，開發商自營 App 於重疊城市之行程以同一守恆自人駕行程扣出。本卡不定方向與量級，只立可拒絕之上界鏈。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（實體容量上界 × 城市需求守恆） |
| 量綱 | 車數［輛］；單車日行程［次／輛·日］；平台行程［次／日］；比值［無量綱］ |
| 可見端 | Uber 10-Q Trips（季，含 Delivery）、AV 城市數、承諾車數（prepared remarks）；Waymo 週付費行程、車隊規模（公司發言）；夥伴召回申報之車數（如 Zoox 約 105） |
| 指名不可見端 | Uber 平台上各夥伴**已部署**車數；Mobility 與 Delivery 之 Trips 拆分；城市層各 App 行程 |
| 主張 | 部署車數 × 利用率上界領先於 AV 對 Trips／Gross Bookings 之可見貢獻；可由「具名者已以此上界建模」或「上界於窗內不重大」拒絕 |
| 外部參照物（測一查證） | 共享運輸車隊爬坡前例（如電動滑板車／共享單車之部署車數 → 行程上界），僅作路徑先例 |
| 表達工具型態（只指名，不選券） | 美股上市之聚合平台與自駕開發商母公司普通股；不選券 |
| 重疊 | L10-P#2（通道守恆）、L10-I（派單預設）、L14（終端需求）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Uber 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1543151/000154315126000032/uber-20260630.htm ：「Trips (2) 3,268 3,867 18 %」；「Waymo has introduced a commercialized ridehailing fleet of autonomous vehicles on its own platform in addition to a fleet … through our platform」；風險段「remove their vehicles from our platform」。
2. Uber 2Q26 prepared remarks https://s23.q4cdn.com/407969754/files/doc_earnings/2026/q2/transcript/Uber-Q2-26-Prepared-Remarks.pdf ：「AVs are live on Uber in 7 cities, on track for as many as 15 by year-end」；「committed approximately 120,000 vehicles」；「over $10 billion of capital」；無 AV 行程數、無部署車數。
3. AV Market Strategist（Daniel Abreu Marques，2026-08-10）https://avmarketstrategist.substack.com/p/uber-q22026-10-billion-av-investment ：「less than 0.5% of trips」；Uber CEO「mid to high 20s, low 30s in terms of trips per vehicle per day」；未由車數推上界。
4. Electrek（Fred Lambert，2026-07-08）https://electrek.co/2026/07/08/waymo-driverless-las-vegas-four-new-cities/ ：約 500k／週、車隊 3,500 與 3,000 兩說、10 城。
5. Claims Journal／Bloomberg（Ed Ludlow，2026-02-12）https://amp.claimsjournal.com/news/national/2026/02/12/335668.htm ：約 400k／週；年底 >1M／週目標；自營 App 與 Uber 並行。
6. TechCrunch（Kirsten Korosec，2025-06-24）https://techcrunch.com/2025/06/24/uber-and-waymos-commercial-robotaxi-service-is-open-for-business-in-atlanta ：亞特蘭大「dozens」、奧斯汀 >100 輛（2025 年點）。
7. 測一須另取：Uber 3Q26 10-Q 是否首揭部署車數或 AV 行程；Mobility／Delivery Trips 拆分；具名賣方之 AV 滲透模型；CPUC 自駕季報（加州城市層行程）；車隊爬坡前例。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 「<0.5% of trips」與利用率已公開；賣方普遍建 AV 滲透情境 | #3 | 已定價 |
| R2 | 上界於 12 個月窗內遠低於 1%，對聚合平台任一方向皆不重大 | #1、#2［D］ | 不重大（窗內不可表達） |
| R3 | 部署車數不揭露、Trips 含 Delivery，上界無法逐季計算 | #1、#2 | 不可並列（L10-P#1 型死因） |
| R4 | 城市需求非守恆：自駕擴大總需求（新乘客、價格彈性） | Waymo／Uber 發言（測一取） | 守恆前提失效 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 具名賣方／研究機構已以「部署車數 × 單車日行程」上界估 Uber 自駕行程或開發商自營 App 之替代量——已定價（R1）。
(2) 以可得之部署路徑計，上界於重定價窗（≥ 12 個月）內對 Trips 或 Gross Bookings 不重大（< 1%）且無加速證據——不重大（R2）。
(3) 部署車數與 Mobility Trips 皆無季度序列、亦無可替代之城市層資料——上界不可並列（R3，同 L10-P#1 死因型）。
(4) 可運作對照只能寫成 L10-P#2（通道份額 × 單價）、L10-I（派單預設）或 L14 系列。
(5) 具名證據顯示自駕行程主要為新增需求而非自人駕替代——守恆失效（R4）。

複查觸發器（若日後殺）：Uber 10-Q／prepared remarks 首次揭露 AV 行程數或部署車數；Waymo 揭露分城市或分通道（自營 vs Uber）行程；CPUC 季報顯示城市層自駕行程占比顯著上升。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Trips、Gross Bookings（Mobility）、AV 相關資本承諾與購車承諾附註。
2. 可交易工具：聚合平台與自駕開發商母公司普通股。不選券。
3. 半衰期：季度 Trips 揭露 → 部署車數首揭（未定）。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L10［P］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L10-P#1／#2、L10-A／#2、L10-I／#2、L11-P、L14 系列、C-A5 結論；不寫 T-15。
