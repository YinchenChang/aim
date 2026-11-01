# L5-P#5 生成卡｜儲存與 IO：守恆（站址功率守恆下之儲存介質選擇：P_site ≡ P_compute ＋ P_storage ＋ P_other；功率綁定時，每 W 儲存功耗之影子價格＝同一 W 給加速器之邊際收入 λ → 介質之有效成本 c_TB ＋ λ·w_TB·T，排序可與每 TB 購置價相反）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/work/20261011_L5-P#2_generate_CL.md；archive/work/20261017_L5-P#3_generate_CL.md；archive/work/20261025_L5-P#4_generate_CL.md；work/20261025_L5-P#4_test1_CL.md | EMITS: work/20261101_L5-P#5_generate_CL.md -->
**日期：** 2026-11-01　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L5-P　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L4-I#5 本日測一，Q-0142 done）。各格最後測試日最舊＝2026-10-25（L5-P#4、L5-A#4、L12-A#4、L12-I#4）；依表序取 **L5-P**；非已殺、非刻意排除。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `"watts per TB" storage power`：命中 1 筆（ChatGPT 搜尋次數，無關，未用）；`storage`：命中 0 筆。本卡載體全部來自下列原文 fetch。
- 比對之舊檔與死因型態，本卡須異型：
  - **L5-P#1**（HBM 頻寬守恆 decode ≤ BW／V_byte）：不同守恆量（頻寬 vs 功率）。
  - **L5-P#2**（快閃寫入耐久預算；死因 生產 W 不可觀測、申報無分列）：本卡不涉寫入量；守恆量為站址電力。
  - **L5-P#3**（HDD 每 TB IO 守恆；死因 WDC 已以 IO／TB 框定）：本卡不涉 IO。
  - **L5-P#4**（HDD 裝機 EB 存量—流量；死因 退役年齡不可觀測、配額封頂）：本卡不涉退役世代。
  - **L5-A#3**（Everpure 毛利混合）、**L5-A#4**（Sandisk 合資表外 capex）、**L5-I#3**（記憶體長約保障比）：不同型；本卡與 L5-A#3 共用 Everpure 為載體，但主張落在功率影子價格對介質排序，不拆毛利。
  - **C-P1**（ARCH_dead #11，checkpoint 讀取占復原）、**C-P4**（#19，水耗非科目）：不涉 checkpoint；本卡為電力而非水，且 C-P4 之死因（非損益科目）已預寫為否決 (4)。
  - **L2-P 系列**（資料中心實體守恆）：本卡不主張站址電力供給（T-11 不碰），只取「站址功率既定」為邊界條件，落點為儲存介質組合。
- §7-10 領域最近公開：iTWire 2026-08-28（Everpure 第二家前五大超大規模勝單、「power that is not consumed by storage can instead be allocated to compute」）；Seagate FY26 10-K（2026-08-04）；TrendForce 2025-09-15（QLC 較 nearline HDD 功耗約低 30%）。下一檢查點＝Everpure 3Q FY27 法說（約 2026-11 下旬）、Seagate／WDC 下季法說。

## 1. 落差一句

站址電力為守恆量：`P_site ≡ P_compute + P_storage + P_net + P_overhead`。若站址功率綁定（電網容量既定），每多 1 W 儲存即少 1 W 加速器，故儲存介質之有效年成本為 `c_eff = c_TB/T + λ·w_TB`，其中 `w_TB` 為每 TB 功耗、`λ` 為加速器每 W 年邊際收入（影子價格）。可見值：Seagate Exos M 32 TB 資料表 idle 6.9 W、最大運作 9.5 W `[V]` → `[D]` ≈ 0.22／0.30 W/TB；TrendForce 稱 QLC 較 nearline HDD 功耗約低 30% `[I-利害方 二手]`；Solidigm 稱 122 TB 型「90% less power」（無基準）`[I-利害方]`。**種子主張：** 公開介質比較以 $/TB 購置價（HDD 低數倍）為主軸，而在功率綁定之 AI 站址，`λ·w_TB` 項可能與 `c_TB/T` 同量級，使 HDD→QLC 之轉換點由價格曲線改由 λ 決定；或反之，儲存功耗占站址比例過小（`P_storage/P_site` 若 < 數 %），λ 項無論多大都不改排序。本卡不定方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（站址功率預算加總固定；儲存與計算為零和分配）；非營收恆等、非誘因 |
| 選擇者 | 站址營運者（超大規模、新雲）決定介質；λ 由其加速器營收／W 決定 |
| 可見端 | 硬碟／SSD 資料表 W；Everpure 稱「second top-five hyperscaler」與功率重分配敘述（iTWire 2026-08-28）；Meta 2025 部落格「we expect our workloads to consume lower power with QLC SSDs」（Blocks & Files 2025-04-07 轉述）；TrendForce 2025-09-15 nearline HDD 短缺與 QLC 2026 放量 |
| 指名不可見端 | 超大規模站址之 `P_storage/P_site` 實測或規劃比例；`λ`（每 W 加速器營收）之業者口徑；QLC 大容量碟實際 W/TB（資料表須另取）；實際購置決策是否以功率影子價格計 |
| 主張 | 介質份額轉換由 `λ·Δw_TB` vs `Δc_TB/T` 之比決定，可事前計算；可被儲存功耗占比過小、超大規模原文仍以 $/TB 決策、或供給者已明文以功率 TCO 定價拒絕 |
| 表達工具型態（只指名，不選券） | 美股可交易之 HDD 供給者（Seagate、Western Digital）、QLC／全快閃供給者（Sandisk、Micron、Everpure）。不選券 |
| 重疊 | L5-A#3（同 Everpure）、L5-P#3／#4（同 HDD 機群）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Seagate Exos M／X 資料表 DS2045.4-2511：https://www.seagate.com/content/dam/seagate/en/content-fragments/products/datasheets/exos-m-v1-2/exos-v1-2-DS2045-4-2511-en_US.pdf
2. Seagate 10-K FY26（sec.py 實讀：「power consumption|watts|per terabyte|energy」0 筆，僅「energy-efficient」一句敘述）：https://www.sec.gov/Archives/edgar/data/1137789/000113778926000159/stx-20260703.htm
3. iTWire 2026-08-28（Everpure 第二家超大規模；功率重分配原句）：https://itwire.com/business-it-news/storage/everpure-lands-second-hyperscaler-win-as-ai-data-centres-chase-power-and-rack-efficiency
4. Blocks & Files 2025-04-07（Meta 對 QLC 功耗之評估）：https://blocksandfiles.com/2025/04/07/metas-positive-assessment-of-pure-storages-flash-mettle/
5. TrendForce 2025-09-15（QLC 約低 30% 功耗；nearline 短缺）：https://www.trendforce.com/presscenter/news/20250915-12714.html
6. Signal65（Solidigm 委託）100 MW AI 資料中心儲存功耗模型（2024-12-17；白皮書 PDF 未取）：https://signal65.com/research/ai/building-power-efficient-ai-data-centers-with-solidigm-qlc-ssds/
7. Solidigm D5-P5336 122.88 TB（經銷商頁，「90% less power」無基準）：https://www.mouser.in/new/solidigm/solidigm-d5-p5336-122-88tb-ssds/
8. 測一須另取：QLC 122／245 TB 資料表 W；Everpure 10-Q／法說原文就功率 TCO 與超大規模勝單；WDC、Sandisk、Micron 10-Q／10-K（sec.py）是否以 W/TB 或功率 TCO 敘述；超大規模（Meta、Microsoft、Google）原文之儲存功耗占比；具名賣方或 TrendForce／IDC 是否以功率影子價格建模介質份額；Signal65 白皮書原文。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 每 TB 功耗相近：HDD 32 TB ≈ 0.22–0.30 W/TB，QLC 只低約 30%（非數量級） | #1、#5 | `Δw_TB` 小 → λ 項不足以翻轉排序 |
| R2 | 「power not consumed by storage can be allocated to compute」已是供給者公開敘事 | #3 | 機制已入共識（否決 (2)） |
| R3 | AI 站址功率主要在加速器，儲存占比小 | 生成假說，測一須找原文 | λ 項乘上小占比，總效應不顯 |
| R4 | nearline HDD 短缺本身已驅動 QLC 替代（TrendForce），非功率 | #5 | 所測轉換由相鄰機制（供給）驅動（C-I2 型） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 無任何一手或具名原文給出超大規模／AI 站址之儲存功耗占站址比例（或可反解之區間）——守恆式之 `P_storage/P_site` 不可觀測。
(2) 儲存供給者或具名賣方／研究機構已明文以功率影子價格（每 W 計算收入或「功率換 GPU」）量化介質選擇或份額（R2；已入共識）。
(3) `[D]` `λ·Δw_TB ÷ (Δc_TB/T)` < 0.3（以可得 W/TB 與 $/TB、T＝5 年、λ 取可得最高口徑；門檻於此凍結），或 `P_storage/P_site` < 3%——λ 項不改排序。
(4) 申報層（10-K／10-Q）除敘述外無任何與功率／W/TB 相關之可拒絕科目，且介質份額無分列（§7-4 財報科目題不可答；C-P4 型）。
(5) 可運作對照只能寫成供給短缺替代（R4）、毛利混合（L5-A#3）或 IO 密度（L5-P#3）。
(6) 12 個月內無可檢驗事件（法說、申報、超大規模規格公布）可使本機制被拒絕。

複查觸發器（若日後殺）：任一儲存供給者於申報層或法說揭露以功率 TCO 計之勝單／份額；或任一超大規模業者公開儲存功耗占站址比例。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：HDD 出貨 EB 與 ASP；全快閃／QLC 企業級營收分列；超大規模營收分列。
2. 可交易工具：Seagate、Western Digital、Sandisk、Micron、Everpure 美股（不選券）。
3. 半衰期：超大規模介質決策周期（新站址設計 12–24 個月）與 12 個月窗之相容性，測一須查。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0143；`query/ARCH_matrix.md` L5［P］標「#5 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 一筆。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L5-P#1–#4、L5-A#1–#4、L5-I#1–#4、C-P1、C-P4 結論。
