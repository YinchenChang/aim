# L5-P#6 生成卡｜儲存與 IO：守恆（HDD 媒體之釕質量守恆：釕為 PGM 採礦之副產品，年供給 ≈ 30 t 且對釕價無彈性；HDD 端釕需求 ≡ 出貨 EB × 每 TB 釕強度 g/TB，HAMR 世代強度下降 → 「EB 成長＝釕需求成長」之代理在 HAMR 換代期失效，方向取決於 EB 成長率與強度下降率之差）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；AIM_FUNNEL.md；archive/drive/USED_20260927_L5-P_generate_GK.md；archive/drive/USED_20260929_L5-P_T_GK.md；archive/work/20261011_L5-P#2_generate_CL.md；archive/work/20261017_L5-P#3_generate_CL.md；archive/work/20261025_L5-P#4_generate_CL.md；archive/work/20261101_L5-P#5_generate_CL.md；archive/work/20261011_L5-A#2_generate_CL.md；archive/work/20261011_L5-I#2_generate_CL.md | EMITS: work/20261109_L5-P#6_generate_CL.md -->
**日期：** 2026-11-09　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L5-P　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L4-I#6 於 2026-11-09 已測一）。最後測試日最舊＝2026-11-01（L5-P#5、L5-A#5、L5-I#5、L12-A#5、L12-I#5 同日）；依表序取 **L5-P**；非已殺、非刻意排除。既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py HDD heads exabyte`，命中 3 筆（皆為模型 attention heads，無關）；未引用。選格先於查線索。
- 比對之舊檔與死因型態，本卡須異型：
  - **L5-P#1**（HBM 頻寬×時間守恆）：裝置內資料搬移；本卡為**原料質量**守恆。
  - **L5-P#2**（快閃寫入耐久預算）：裝置壽命預算；本卡在上游原料。
  - **L5-P#3**（HDD 每碟 IO 守恆）：IO 密度；本卡不涉 IO。
  - **L5-P#4**（HDD 裝機 EB 存量—流量）：EB 存量；本卡以出貨 EB 為**輸入**，守恆量為釕噸數。
  - **L5-P#5**（站址功率守恆下介質選擇）：電力；本卡為金屬。
  - **L5-A#2**（HDD 營收 ≡ 台數×TB×價）：營收恆等；本卡不看 HDD 商營收，看原料端。
  - **L5-I#2**（NAND JV 資本配置誘因）：供給誘因；本卡供給為副產品，無擴產誘因可言。
  - **ARCH_dead C-P1**（checkpoint 方向翻負）：構成不同。
  - 重疊照記：L3 層（半導體互連用釕）為另一需求端；本卡只主張 HDD 端，ANALYST 須拆 HDD vs 半導體 vs 化學／電化學。
- §7-10 領域最近公開：JM 2026 PGM 市場報告（2026-05-14）；IPA 釕事實表（2026-05，JM 2026-01 資料）；Seagate FQ1 FY27 法說（2026-10 下旬，Blocks & Files 2026-10-29 轉述）；CMP 釕價（2026-10-13）。下一檢查點＝JM 2027 PGM 報告（約 2027-05）、Seagate FQ2 FY27（約 2027-01）、WDC FQ2 FY27。

## 1. 落差一句

釕為 PGM 採礦之副產品（IPA 2026-05：2025 年一次礦產 ≈ 30 t、精煉 31 t、南非 > 90%；「produced almost entirely as a byproduct」），供給對釕價近乎無彈性。釕價：≈ 1,750 美元/oz（2026-03-13，Reuters／LSEG，上年同期 ≈ 560）、1,780.14 美元/oz（2026-10-13，CMP，年增 109.43%，investornews 2026-10-21 轉述）；市場敘事稱釕為「precious proxy for the AI buildout」（MKS PAMP，Reuters 2026-03-16）。JM（2026-05-14）：資料中心使硬碟用釕升至五年高，但化學用量下降，2026 總需求 −6%，仍「significant deficit」（investornews 轉述 JM：一次供給 977 koz vs 需求 1,193 koz）。但 HDD 端之釕需求 ≡ 出貨 EB × 每 TB 釕強度，而 IPA 稱 HAMR「uses much lower amounts of ruthenium」；Seagate FQ1 FY27 出貨 220 EB、預期 2026 年底 HAMR ≈ 50% nearline EB 出貨率（Blocks & Files 2026-10-29）。落差＝「EB 成長＝釕需求成長」之代理在 HAMR 換代期可能翻向（強度下降率 > EB 成長率），亦可能 PMR 世代延長而強度不降；兩者未被拆分。方向未定。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（質量）：`Ru_supply,t ＋ ΔStocks_t ≡ Σ_s D_s,t`；HDD 端 `D_HDD ≡ EB_t × [(1−h_t)·g_PMR ＋ h_t·g_HAMR]`（h＝HAMR 之 EB 份額；g＝每 TB 釕克數，含濺鍍靶材利用率與回收閉環）。供給 ≡ 採礦 PGM 籃量 × 釕占比（≈ 7%），由鉑／鈀經濟決定 |
| 量綱 | 噸（或 koz）／年；g/TB；h 無量綱。先對齊 JM「demand net of closed-loop recycling」與毛用量口徑（§7-1） |
| 須拆分 | ① HDD vs 半導體（互連／阻障層）vs 化學／電化學；② 每碟強度 vs 每 TB 強度（HAMR 單碟 TB 高，即使每碟用量相同，g/TB 亦降）；③ 靶材閉環回收（毛 vs 淨）；④ 價格驅動之投機囤貨 vs 實需 |
| 可見端（實讀） | IPA 供給噸數與南非占比；JM 2026 需求方向；釕價兩點；Seagate EB 出貨與 HAMR 份額指引（上） |
| 指名不可見端 | g_PMR、g_HAMR 數值；HDD 釕需求噸數序列；WDC（PMR／ePMR／HAMR 時程）之 EB 組成；靶材供應商（Heraeus、田中、Furuya）出貨 |
| 主張 | 若 `ΔEB/EB < −Δg/g`，HDD 端釕需求於 12–24 個月內下降，現行「AI 儲存→釕赤字」敘事高估需求端；反之若 HAMR 份額爬升慢或 g_HAMR 未顯著下降，赤字持續。本卡只主張此分解未被公開拆分 |
| 外部參照物（測一查證） | 前例：2006–2007 垂直記錄（PMR）導入使 HDD 用釕驟增、釕價自 ≈ 100 升至 ≈ 870 美元/oz，2008 後回落；只作路徑先例 |
| 表達工具型態（只指名，不選券） | 美股掛牌之 PGM 礦商 ADR／普通股、HDD 商普通股與上市選擇權。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| IPA 釕事實表（SFA Oxford，2026-05） | https://ipa-news.com/assets/pdfs/factsheets/2026-05-ipa-ruthenium-factsheet.pdf |
| JM 2026 PGM 市場報告新聞稿（2026-05-14） | https://matthey.com/media/2026/johnson-matthey-publishes-2026-pgm-market-report1 |
| Reuters／Mining.com 釕價（2026-03-16） | https://www.mining.com/web/ruthenium-prices-hit-record-high-as-ai-boom-squeezes-supply |
| investornews 釕價與 JM 供需（2026-10-21，二手） | https://investornews.com/market-opinion/ruthenium-prices-double-as-ai-storage-demand-meets-limited-supply/ |
| Blocks & Files Seagate FQ1 FY27（2026-10-29） | https://www.blocksandfiles.com/disk/2026/10/29/seagate-hyperscalers-hot-for-hamr/5306231 |
| Crux Investor（2026-08-07；稱 HAMR「does not use ruthenium」，無出處，與 IPA 衝突） | https://www.cruxinvestor.com/posts/pgm-deficit-set-to-widen-as-ai-data-center-demand-exceeds-forecasts |
| JM 完整報告分項表；Seagate／WDC 10-K／10-Q（sec.py）之媒體材料與供應商風險段；Valterra／Implats／Sibanye 釕產量與籃價；HAMR 媒體層結構之專利或論文 | 測一取得 |

不宣稱釕強度變化已入或未入共識、不宣稱方向。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | HDD 用釕升至五年高，市場仍顯著赤字 | JM 2026-05-14 | 強度下降未抵銷 EB 成長 |
| R2 | 電氣與電化學需求自 2019 起近乎持平，成長來自化學 | IPA 2026-05 | HDD 非邊際買方，本卡無量級 |
| R3 | HAMR 媒體仍需釕中間層；g_HAMR 降幅小 | 測一查 HAMR 媒體結構 | 機制不成立 |
| R4 | 研究機構已依技術拆分 HDD 用釕預測 | JM／SFA／Metals Focus 付費報告 | 落差已揭露 |
| R5 | 釕價由副產品供給（南非產量）主導，HDD 需求變動不改價格 | Reuters 2026-03-16（南非產量 −3.8%） | 需求端無定價力 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) ≥ 1 位具名研究機構（JM、SFA、Metals Focus、Heraeus）公開已按 PMR／HAMR 拆分 HDD 用釕或已量化 HAMR 換代對釕需求之淨效果（R4）。
- (2) 公開層無 g_PMR、g_HAMR 或 HDD 用釕噸數序列之任何一手或具名二手代理，致分解不可觀測（可觀測性）。
- (3) 一手證據（論文、專利、媒體商申報）顯示 HAMR 媒體每 TB 釕強度不低於 PMR 之 0.7 倍（R3）——門檻 0.7 已凍結。
- (4) `[D]` 量級：HDD 用釕占全球釕需求 < 15%，或測一估算之 12–24 個月 HDD 用釕淨變動 < 全球需求 3%（R2）——門檻已凍結。
- (5) 釕價變動可完全由南非供給與化學需求解釋，HDD 端需求變動無可分離之價格效果（R5）。
- (6) 12 個月內無檢驗事件（JM 2027 報告、Seagate／WDC HAMR 份額季報、PGM 礦商釕產量季報）。

複查觸發器（若日後殺）：任一研究機構首次發布按技術拆分之 HDD 用釕；WDC 公告 HAMR 量產時程；JM 報告之 HDD 用釕首次年減。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：PGM 礦商之釕產量與籃價收入；HDD 商之媒體材料成本與供應商集中風險段。
2. 可交易工具：美股掛牌 PGM 礦商 ADR／普通股、HDD 商普通股與上市選擇權（不選）。
3. 半衰期：12–24 個月（HAMR 份額爬升期）。

## 7. 本輪寫入

本卡；QUEUE 新列（ANALYST 測一）；ARCH_matrix L5［P］格標「#6 已生成」；`export/LEADS_算力收支.md` 追加 1 列（Seagate FQ1 FY27 出貨 EB）。不改 L5-P#1–#5、L5-A#1–#5、L5-I#1–#5、C-P1。
