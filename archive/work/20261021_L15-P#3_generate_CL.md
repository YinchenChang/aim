# L15-P#3 生成卡｜基礎設施軟體與資料：守恆（觀測預算占基礎設施支出之份額守恆：AI 工作負載推高遙測量，但觀測美元受份額上限約束，量增經取樣／分層／自建吸收，商業觀測商營收不隨 AI 遙測量等比成長）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20261005_L15-P_generate_GK.md；archive/drive/USED_20261005_L15-P_test1_GK.md；archive/work/20261014_L15-P#2_generate_CL.md | EMITS: work/20261021_L15-P#3_generate_CL.md -->
**日期：** 2026-10-21　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 4→5／6）　**格：** L15-P　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L14-I#3 本日測一，Q-0084 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-14 之 L15-P／A／I#2，依表序取 **L15-P**。既有 #1–#2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `observability telemetry Datadog`，0 筆；未用。
- 比對（須異型）：
  - **L15-P#1**（`archive/drive/USED_20261005_L15-P_generate_GK.md`）：守恆量＝資安分析師注意力（人×秒）。本卡守恆量＝**觀測美元占基礎設施美元之份額**，不涉人力。
  - **L15-P#2**（`archive/work/20261014_L15-P#2_generate_CL.md`）：雲承諾池之市集抵扣（通路）。本卡不涉承諾、市集或通路。
  - **L15-A**（使用量×有效單價不可並列）：本卡主張之可觀測量為**跨主體比值**（觀測商營收 ÷ 超大雲營收），不需拆單價與量；若測一只能寫成單價×量即觸發 (4)。
  - **L15-I／#2**（遙測出站權、開源託管定價權）、**L15-A#2**（遞延收入浮存）、**L14-P#2**（ISV 預付池）：皆異型。
  - **L6-I 系**、**L7-I#3**（大客戶換供應）：本卡之 AI-native 大客戶縮量只作量級證據，主張在份額上限，不在對手方集中；測一若只剩集中度即觸發 (4)。
- §7-10 領域最近公開：DDOG 10-Q 2Q26（期 2026-06-30）；MSFT 10-K FY26；AMZN／GOOGL 10-Q 2Q26。下一檢查點＝各家 3Q26 10-Q（2026-11）。

## 1. 落差一句

市場把觀測商（DDOG 等）來自 AI 工作負載之營收成長讀成隨 AI 遙測量擴張之持續需求；種子主張：企業觀測支出受「占基礎設施帳單份額」之預算慣例約束（Honeycomb／Charity Majors：「around 15-25% of your infra bill」），AI 使遙測量 \(V\) 增速高於基礎設施美元 \(C\)，份額 \(s = B/C\) 觸頂後，量增只能經取樣、分層或自建吸收，觀測商營收 \(R \le s_{\max} C\) 而非 \(\propto V\)。DDOG 10-Q 2Q26 已見樣態：AI-native cohort「rapidly increased their usage of our product, and may in the future optimize their usage」，且「Beginning in the third quarter of 2026, we saw our largest customer reduce their usage」。可拒絕之主張＝存在可觀測序列顯示 \(R/C\) 有上限而市場以 \(V\) 外推。不主張任何主體價值方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆（P）**：\(B = R_{商業} + B_{管線} + B_{自建}\)，\(B \le s_{\max} C\)；\(V\) 只經單位美元密度 \(B/V\) 下降被吸收 |
| 量綱 | \(s\)、\(R/C\) 無因次；\(V\)（GB／span／series）只作方向，不入載入 |
| 選擇者 | 企業平台工程／FinOps（取樣、保留期、分層、OpenTelemetry 自建）；觀測商（分層價目、Flex 類低價層） |
| 可見端 | 觀測商 10-Q／10-K：營收、NRR、「optimization」敘述、AI-native cohort 貢獻；超大雲雲營收（同季）→ `[D]` \(R/C\) 序列；顧問與廠商之份額基準 |
| 指名不可見端 | 單一企業之 \(B\)、\(C\)、\(V\)；取樣率；自建占比 |
| 表達工具型態（只指名，不選券） | 美股觀測或日誌分析商；不選券 |
| 重疊 | L15-A（量×價）；L7-I#3／L6-I（大客戶） |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Datadog 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1561550/000162828026054458/ddog-20260630.htm ：「our AI-native cohort, which cohort includes our largest customer, contributed high single digit percentage points to the total Company year-over-year revenue growth」；「trailing 12-month dollar-based net retention rate was about 120%」；「reduction in usage from our largest customer starting in the third quarter of 2026, which may cause a deceleration in revenue growth」；「Certain customers … increase usage of our product and then seek to optimize their usage」。
2. 分母：Microsoft 10-K FY26 https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm （「Azure and other cloud services revenue increased 41%」）；AMZN 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm ；GOOGL 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm （AWS／Google Cloud 分部營收，測一取）。
3. 份額基準：Honeycomb（Charity Majors，2025-04-16，更新 2025-05-20）https://www.honeycomb.io/blog/how-much-should-i-spend-on-observability-pt1 ：「around 15-25% of your infra bill」，自述 2018 年 20–30% 估計「based on personal experience rather than data」。廠商部落格（OneUptime，2026-03）https://oneuptime.com/blog/post/2026-03-11-the-monitoring-tax-how-observability-vendors-take-5-percent-of-cloud-spend/markdown （標題「5% of Cloud Spend」，未讀）；monitoringcost.com https://monitoringcost.com/observability-cost-as-percent-of-cloud （未讀）。皆為有立場之來源。

缺段（§7-2）：未取其他觀測商（DT、ESTC、CSCO-Splunk）序列；未取具名賣方就 DDOG AI-native 外推或份額上限之原文；未取任何調查型（Gartner／IDC）份額序列。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 份額基準為個人經驗估計、口徑分歧（5% vs 15–25%），無上限可言 | Honeycomb 自述 | 守恆約束不可觀測 |
| R2 | DDOG 已自揭 AI-native 貢獻與最大客戶縮量，賣方據此下修 | DDOG 10-Q | 已定價 |
| R3 | 觀測商營收占超大雲營收極小，份額遠未觸頂 | 測一 `[D]` | 約束不綁定 |
| R4 | 縮量為單一客戶自建（對手方事件），非份額守恆 | DDOG 10-Q | 歸 L6-I／L7-I#3 型 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) `[D]` \(R/C\)（DDOG 等 ≥ 2 家 ÷ 三雲雲營收）≥ 6 季無上限跡象且份額基準無 ≥ 2 個獨立具名來源；或
(2) 申報層無 AI-native／optimization 之可並列序列（僅 1 家 1 期），致落差不可觀測（記失敗歸因）；或
(3) 具名賣方或評等機構原文已就觀測支出份額上限或 AI-native cohort 不可外推定價；或
(4) 可運作對照只能寫成 L15-A（量×價）、L6-I／L7-I#3（大客戶集中／換供應）；或
(5) 12 個月內無檢驗事件（3Q26 起各季 10-Q 之 cohort 揭露、份額調查更新）；或
(6) AI-native cohort 對觀測商營收成長貢獻 < 5 個百分點且非 AI 客群 NRR 不受影響，使份額守恆不影響總營收讀數。

複查觸發器（若日後殺）：任一觀測商首次以美元揭露 AI-native 營收或取樣／分層價目層占比；具名調查發布觀測支出占雲支出之多年序列；DDOG NRR 連續 2 季下降且公司歸因於優化。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：營收、NRR、cohort 貢獻、RPO。2. 可交易工具：觀測商普通股（不選）。3. 半衰期：年約續約週期；縮量自 3Q26 起。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0085；`query/ARCH_matrix.md` L15［P］加「#3 已生成」；`AIM_FUNNEL.md` §3 一句與日期行。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L15-P#1／#2、L15-A／#2、L15-I／#2、L14-P#2、L6-I 系、L7-I#3；不碰 L1-P；不寫 T。
