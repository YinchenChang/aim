# L5-I#6 生成卡｜儲存與 IO：誘因（配給下之「第二介質」選擇權：近線 HDD 交期 > 52 週時，雲端買方投入 QLC SSD 之冷／溫資料認證與資料管理軟體——認證成本一經沉沒，且 QLC 成為對 HDD 雙寡頭議價之外部選項，則 HDD 供給正常化後介質份額不回復（遲滯），而非「短缺期替代、短缺後回流」）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260926_L5-I_generate_GK.md；archive/work/20261011_L5-I#2_generate_CL.md；archive/work/20261018_L5-I#3_generate_CL.md；archive/work/20261026_L5-I#4_generate_CL.md；archive/work/20261101_L5-I#5_generate_CL.md；archive/work/20261025_L5-P#4_generate_CL.md；archive/work/20261101_L5-P#5_generate_CL.md；archive/work/20261011_L5-A#2_generate_CL.md；archive/work/20261109_L4-I#6_generate_CL.md | EMITS: work/20261109_L5-I#6_generate_CL.md -->
**日期：** 2026-11-09　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L5-I　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L5-A#6 本日測一，Q-0185 done）。最後測試日最舊＝2026-11-01（L5-I#5、L12-A#5、L12-I#5）；依表序取 **L5-I**；非已殺、非刻意排除。既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `QLC`、`HDD`、`nearline`，**命中 0 筆**。內部數字（§12）未取用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L5-I#1**（出站費／資料重力之法定上限）：彼為雲端對客戶之鎖定；本卡為雲端對**供應商**之介質選擇，不涉出站費。
  - **L5-I#2**（NAND JV 雙邊同意下之不擴產誘因）：彼為供給者資本配置；本卡為買方認證決策，不以供給者擴產紀律為落差。
  - **L5-I#3**（記憶體長約之違約／重議誘因）：本卡不以長約可執行性為落差；HDD 長約（Seagate 稱至 2028）在此為**反方**（R2），非機制。
  - **L5-I#4**（退役 DDR4 經 CXL 再部署之外部選項）：彼為同介質舊品再用、需求彈性；本卡為**跨介質**、新品、且主張不可逆（沉沒認證），非價格彈性。
  - **L5-I#5**（STaaS 固定 $/TiB 之逆選擇）：不涉訂閱合約。
  - **L5-P#5**（站址功率影子價格使介質排序翻轉）：彼為守恆／功率；本卡**不以功耗**為驅動——驅動為配給（交期）與議價外部選項；若測一只能以功率說明份額移轉 → 否決 (6)。
  - **L5-P#4**（HDD 裝機 EB 存量流量）、**L5-A#2**（HDD 營收量價恆等）：本卡不以存量退役或營收分解為落差。
  - **L4-I#6**（漲價預期下跨期前移）、**L3-I#5**（重複下單）：本卡非時點前移或虛增訂單；方向相反（為 HDD 需求之**永久移出**主張）。
  - **C-P1**（ARCH_dead #11，checkpoint 儲存）：不同型。
- §7-10 領域最近公開：Seagate 10-Q FQ1 FY27（2026-10-29）與法說（2026-10-27）；Sandisk 10-Q 1Q FY27（2026-10-30）；TrendForce 近線短缺稿（2025-09-15，**逾一年，測一須找 2026 更新**）。下一檢查點＝WDC FQ2 FY27 法說（約 2027-01）、Seagate FQ2 FY27（約 2027-01）。

## 1. 落差一句

誘因結構：買方 j 於期 t 之介質選擇最小化 `TCO_HDD(p_H, 交期) vs TCO_QLC(p_Q) + K_j·1{未認證}`，其中 `K_j`＝冷／溫層 QLC 認證與資料管理演算法調整之一次性成本（TrendForce 2025-09-15：「they will need to account for adjustments to data management algorithms」）。配給期交期成本 → `K_j` 被支付；支付後，後續期之比較不再含 `K_j`，且「可切換」本身壓低 HDD 議價力。

可見值（`[V]` 原文；`[S]` 二手；比值 `[D]` 留測一）：

| 項 | 值 | 出處 |
|---|---|---|
| 近線 HDD 交期 | 「from just a few weeks to over 52 weeks」 | TrendForce 2025-09-15 `[S]` 產業研究 |
| 雲端轉向 QLC | 「some providers to consider deploying SSDs for cold data」（一手稿僅「consider」）；Tom's Hardware 2025-11-09 轉述 DigiTimes：「hyperscalers are now switching to QLC」 | `[S]`；兩者強度不一，測一須拆 |
| Seagate 近線 EB | FQ1 FY27（截至 2026-10-02）近線 198 EB（前季 195、去年同期 160）；營收增加「primarily due to favorable pricing actions」 | Seagate 10-Q `[V]` |
| Seagate 對替代之自述 | 「nearline HDDs and enterprise grade SSDs complement one another for most workloads, however, for certain high-performance workloads, the two storage media can compete」 | Seagate 10-Q 風險因素 `[V]` |
| 認證週期 | 「Our sales cycle for nearline storage solutions could exceed one year … time required for developing, testing and evaluating our products before deployment」 | Seagate 10-Q `[V]`（HDD 側；同理適用 QLC 側之推論為本卡主張，非證據） |
| Seagate 長約 | 「the vast majority of our nearline exabyte supply is now allocated under long-term supply agreements through calendar 2028」；「we do not see any demand destruction at all」 | 24/7 Wall St. 2026-10-28 轉述法說 `[S]`，測一取官方逐字稿 |
| NAND 側 | Sandisk Datacenter 營收 $4,802M（去年同期 $269M）；2H FY26 起與 Datacenter 客戶簽多年 NBM 承購量 | Sandisk 10-Q `[V]` |

**種子主張：** 市場以「HDD 長約覆蓋至 2028 ＋ 每 TB 成本差」外推近線 HDD 之 EB 份額與定價力；若配給期已使主要雲端完成 QLC 冷／溫層認證，則 2028 續約時 HDD 面對的是**已可執行之外部選項**，份額或價格（或兩者）在續約窗低於外推。反之，若 QLC 同遭配給（NAND 亦漲價、長約化）使認證未發生，或每 TB 價差過大使選項不可行，則無落差。本卡不定方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因（沉沒認證成本 → 遲滯；外部選項 → 議價力）；非守恆、非會計恆等 |
| 決策者 | 雲端／大型企業儲存採購（介質選擇、認證投入）；HDD 雙寡頭（＋Toshiba）之長約定價 |
| 可見端 | HDD 商 10-Q 近線 EB、價格歸因句、長約期限；NAND 商 Datacenter 營收與 NBM；產業研究之 QLC 高容量出貨與交期 |
| 指名不可見端 | 各雲端冷／溫層實際介質組成；QLC 認證完成與否（多不公告）；長約之量承諾型態（take-or-pay 或指示量）；續約價格 |
| 主張 | 「短缺期 QLC 增量是否於 HDD 交期回落後仍維持」可由 EB 份額序列觀測；可被 QLC 同步配給、價差、長約鎖量、或已入共識所拒絕 |
| 表達工具型態（只指名，不選券） | 美股可交易之 Seagate、Western Digital、Sandisk、Micron、Pure Storage。不選券、不定方向 |
| 重疊 | L5-P#5（介質排序，但為功率）、L5-I#3（長約，但為違約誘因）、L5-I#4（外部選項，但為同介質再用）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Seagate 10-Q FQ1 FY27（近線 EB、價格歸因、HDD／SSD 互補句、銷售週期、market share based inventory purchase commitments）：https://www.sec.gov/Archives/edgar/data/1137789/000113778926000309/stx-20261002.htm
2. Sandisk 10-Q 1Q FY27（Datacenter 營收、NBM 長約）：https://www.sec.gov/Archives/edgar/data/2023554/000162828026068601/sndk-20261002.htm
3. TrendForce 2025-09-15 近線短缺與 QLC：https://www.trendforce.com/presscenter/news/20250915-12714.html
4. Tom's Hardware 2025-11-09（轉述 DigiTimes：交期兩年、雲端轉 QLC、QLC 產能訂滿 2026）：https://www.tomshardware.com/pc-components/hdds/ai-triggers-hard-drive-shortage-amidst-dram-squeeze-enterprise-hard-drives-on-backorder-by-2-years-as-hyperscalers-switch-to-qlc-ssds
5. 24/7 Wall St. 2026-10-28（Seagate 法說轉述：長約至 2028、無需求破壞、以面密度而非台數擴產）：https://247wallst.com/investing/2026/10/28/seagate-says-it-cant-make-hard-drives-fast-enough-for-ai/
6. 測一須另取：Seagate FQ1 FY27 法說官方逐字稿（長約量承諾型態、替代問答）；WDC 10-Q FQ1 FY27 與法說（近線 EB、長約、替代）；Sandisk／Micron／Kioxia／Solidigm 法說之高容量 QLC 用於冷／溫層之一手句；TrendForce 或 IDC 2026 年之 QLC 高容量出貨與近線 HDD EB 份額；雲端業者（Meta OCP、Microsoft、Google）公開之冷層介質架構文件；QLC vs 近線 HDD 合約 $/TB 比。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | Seagate：HDD 與企業 SSD「complement one another for most workloads」；每 TB 成本差使冷層替代不經濟 | #1 | 選項存在但不可行 → 無遲滯（否決 (4)） |
| R2 | 近線 EB 大部分已以長約配置至 2028 年，部分雲端合約至 2030 | #5（測一取一手） | 鎖量使替代於 ≥ 12 個月窗內不可執行（否決 (3)） |
| R3 | NAND 亦短缺：QLC 產能訂滿 2026、Sandisk 漲價、NBM 長約化 | #2、#4 | QLC 同遭配給 → 認證未必轉為實際部署 |
| R4 | TrendForce 一手僅言「consider」，且列「cost and supply chain constraints」為障礙 | #3 | 「轉向」為二手誇大 → 機制未發生（否決 (1)） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 找不到任何一手（雲端業者、NAND／SSD 商申報或法說官方逐字稿、OCP 規格文件）證據顯示有雲端因 HDD 配給而完成或進行 QLC 冷／溫層認證或部署——只有二手轉述。
(2) 已入共識：具名賣方、TrendForce／IDC 或主流財經媒體已明文以「短缺後 QLC 份額不回流」建模近線 HDD EB 份額或續約價；或 Seagate／WDC 管理層已於法說量化此風險。
(3) 長約鎖量：Seagate／WDC 申報或官方逐字稿顯示長約為量承諾（take-or-pay 或等效）且覆蓋 ≥ 80% 近線 EB 至 2028 年底，使選項於 2028 前不可執行，且無 2028 年前續約／重議窗。
(4) 經濟不可行：2026–27 高容量 QLC 與近線 HDD 合約 $/TB 比 ≥ 4（門檻於此凍結），且無一手證據顯示雲端以非價格因素（交期）接受該比值。
(5) 量級：`[D]` 12–24 個月內歸因於冷／溫層之高容量 QLC EB ÷ 同期近線 HDD EB（三家合計）< 3%（門檻於此凍結）。
(6) 可運作對照只能寫成 L5-P#5（站址功率）、L5-I#4（同介質再用之需求彈性）、L5-I#3（長約違約誘因）或 L4-I#6／L3-I#5（時點前移／重複下單）。
(7) 12 個月內無可檢驗事件（Seagate／WDC FQ2–FQ4 FY27 近線 EB 與價格句、Sandisk／Micron 高容量 QLC 出貨句、2028 續約定價揭露）可使本機制被拒絕。

複查觸發器（若日後殺）：近線 HDD 交期回落至 < 26 週後連續 2 季，HDD 商近線 EB 年增率低於同期雲端儲存容量成長且管理層歸因於 flash；或任一雲端公開冷層採用 QLC；或 HDD 商首次揭露長約重議或量下修。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：HDD 商近線 EB 與價格歸因、長約；NAND 商 Datacenter 營收與 NBM——皆可拒絕之科目。
2. 可交易工具：Seagate、WDC、Sandisk、Micron、Pure Storage 美股（不選券）。
3. 半衰期：遲滯效應顯現於 HDD 交期回落後與 2028 續約窗，距今 12–26 個月；測一須查與 ≥ 12 個月重定價窗之相容性。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0186；`query/ARCH_matrix.md` L5［I］標「#6 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 一筆（Seagate 近線 EB，10-Q）。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L5-I#1–#5、L5-P#1–#6、L5-A#1–#6、L4-I#6、L3-I#5、C-P1 結論。
