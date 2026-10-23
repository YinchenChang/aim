# L12-P#4 生成卡｜監理與法制：守恆（中國出口許可下之 InP 基板質量平衡——雷射晶粒出貨上界 ≤ 許可放行量＋非中國產能＋Δ在庫）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260922_L12-P_generate_GK.md；archive/work/20261008_L12-P#2_generate_CL.md；archive/work/20261015_L12-P#3_generate_CL.md；work/20261015_L12-P#3_test1_CL.md；archive/work/20261017_L4-P#3_generate_CL.md；archive/work/20261016_L1-I#3_generate_CL.md | EMITS: work/20261023_L12-P#4_generate_CL.md -->
**日期：** 2026-10-23　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 0→1／6）　**格：** L12-P　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。非「已殺／刻意排除」格中最後測一最舊＝2026-10-15（L12-P#3；同日之 L2-I#3、L8-A#3、L8-I#3、L9-A#3、L9-I#3 已於 10-23 補 #4）→ L12-P；既有生成 3 份 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `indium phosphide germanium gallium export`，命中 0 筆；未使用。內部數字（§12）：未取用。
- 比對（本卡須異型）：
  - **L12-P#1**（`archive/drive/USED_20260922_L12-P_generate_GK.md`）：受測產品端物理暴露時長；死於證書庫不可加總。本卡不涉 TIC。
  - **L12-P#2**（`archive/work/20261008_L12-P#2_generate_CL.md`）：監理機關審查佇列 L＝λW；死於機關端流量持平。本卡之「許可」為**貨品放行閘**，守恆量為實體基板，非審查工時或佇列長度。
  - **L12-P#3**（`work/20261015_L12-P#3_test1_CL.md`）：**美國**管制 AI 伺服器**出口外流**之轉運差額（洩漏型）；死於 (1) 出貨地序列不可得、(2) 落地 MW 不可加總。本卡方向相反：**中國**管制**上游材料流入**全球光通訊供應鏈（閘門型）；守恆在原料／基板層，不需落地容量或出貨地營收。測一 D⑤ 之鏡像貿易差屬 #3 型，本卡不用。
  - **L4-P#3**（HBM 位元供給上界）：同為「供給上界 × 每單位用量」形式，但上界由產能決定、非監理；本卡上界之可變部分由**許可放行**決定，屬 L12。
  - **L1-I#3**（Scope 2 屬性）：不同。不碰 L1-P（T-11）。
  - ARCH_dead：無材料出口管制型死因；N-02（CPO 營收未分列）為 L4 表達層，本卡不靠 CPO 分列。
- §7-10 領域最近公開：AXT 10-Q 2Q26（2026-08-13）；AXT 2Q26 電話會（2026-07-30）；TrendForce／Reuters JX 擴產（2026-06-16）；Borecraft 2026-06-22（彙整 DigiTimes／Nikkei）；MOFCOM 2025-11-09 暫停對美 Ga／Ge／Sb 禁令至 2026-11-27（Fastmarkets 2025-11-11）。下一檢查點＝2026-11-27 暫停期滿、AXT 3Q26 10-Q（約 2026-11）。

## 1. 落差一句

AI 資料中心光模組之雷射（EML／CW）長於 InP 基板，故**可出貨雷射晶粒 ≤（中國許可放行之 InP 基板＋非中國基板產能＋Δ在庫）× 每片晶粒數 × 良率**；中國 2025-02-04 將 InP 基板納入出口管制、按單核發許可，使此上界之一大項由**監理放行節奏**而非產能決定。種子主張：市場以光模組需求（800G→1.6T）外推雷射商出貨，未以許可放行量閉合上游質量平衡；**方向未定**——可能是非中國雷射商受限（上界緊）、中國境內雷射／模組商相對受益（境內不受出口閘），亦可能非中國擴產（JX 7–10 倍至 FY2030）與許可常規化已使上界鬆弛。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [P] 守恆：實體基板質量平衡；規則端＝中國 MOFCOM 兩用物項出口許可（2023-08 Ga／Ge、2025-02-04 InP 等）、2024-12 對美禁令及 2025-11-09 暫停（至 2026-11-27）、美國關稅（IEEPA 部分 2026-02-20 遭最高法院撤銷） |
| 恆等（僅定義） | 非中國可用基板（6 吋當量／期）＝中國許可放行＋非中國產出＋Δ在庫；雷射晶粒上界＝可用基板 × 每片晶粒 × 良率；缺口＝需求晶粒 − 上界 |
| 已讀事實 | AXT 10-Q 2Q26：「On February 4, 2025, China added indium phosphide substrates to its export control list … the three wafer substrate product families manufactured by Tongmei all require permits from China’s Ministry of Commerce」；「InP export permits represent the most significant challenge we currently face」；「we have a backlog of orders for which we have not yet received permits and … still cannot predict when a permit application will be reviewed and approved」；GaAs 對美「no permits … have yet been approved」；Tongmei STAR 申請撤回（2026-07-08）。電話會 2Q26：營收 47.6M、InP 30.7M（史高）、「Customer demand continues to outpace supply」、backlog「exceeds 2 quarters」、3Q 可實現約 66M 視許可而定。TrendForce 2026-06-16（引 Reuters）：「AXT and Sumitomo account for nearly 80% of global InP substrate production」、JX 約 10%、JX 產能「7–10 times its fiscal 2025 level」至 FY2030、6 吋 InP 均價自管制後 +250% 至約 5,000 美元。Borecraft 2026-06-22：2026 首批約 4,000 片於 5 月下旬放行、2025-08 約 8,000 片（未引海關）。 |
| 未證之連結 | AXT 中國外產能占比（電話會稱擴產於「adjacent location」，未明地點）；Sumitomo 產能與出貨（非 SEC 申報）；中國境內他家 InP 基板商產出；每片晶粒數 × 良率之換算；雷射商（COHR、LITE）自製基板比例 |
| 量綱 | 6 吋當量片／季；雷射晶粒／季；缺口 ÷ 需求（%）；許可放行 ÷ AXT 在手訂單（季） |
| 半衰期 | 許可按單核發（週～月）；暫停期 2026-11-27；擴產年度級（JX 至 FY2030） |

## 3. B 端可觀測載體（只指名）

1. AXT 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1051627/000143774926027677/axti20260630_10q.htm ；10-Q 1Q26 https://www.sec.gov/Archives/edgar/data/1051627/000143774926017054/axti20260331_10q.htm ；10-Q 3Q25 https://www.sec.gov/Archives/edgar/data/1051627/000143774925034843/axti20250930_10q.htm ；10-K FY25 https://www.sec.gov/Archives/edgar/data/1051627/000143774926008612/axti20251231_10k.htm （產品別營收、地區別、許可段、在手訂單）
2. AXT 2Q26 電話會（Motley Fool 2026-07-30）https://www.fool.com/earnings/call-transcripts/2026/07/30/axt-axti-q2-2026-earnings-call-transcript/
3. TrendForce 2026-06-16（JX 擴產；引 Reuters 份額）https://www.trendforce.com/news/2026/06/16/news-jx-advanced-metals-to-invest-jpy-120b-through-fy2030-expand-inp-capacity-up-to-10x-as-cpo-demand-accelerates/
4. Borecraft 2026-06-22（放行批量彙整）https://borecraft.com/2026/06/22/chinas-inp-export-trickle-leaves-the-ai-optics-bottleneck-intact/
5. Fastmarkets 2025-11-11（MOFCOM 暫停至 2026-11-27）https://fastmarkets.com/insights/china-suspends-export-prohibition-on-superhard-materials-us
6. COHR 10-K FY26 https://www.sec.gov/Archives/edgar/data/820318/000082031826000020/iivi-20260630.htm （「limited number of suppliers … indium phosphide (“InP”)」；「expanding our indium phosphide capacity in Sherman」）；LITE 10-K FY26 https://www.sec.gov/Archives/edgar/data/1633978/000162828026057358/lite-20260627.htm （grep `indium|InP` 0 筆，待以他詞複查；非「不存在」）
7. 未讀：MOFCOM 公告原文（2025 年第 10 號等）；中國海關 HS 3818／8541 相關 InP 出口月度；Sumitomo Electric、JX 財報 InP 段；McKinsey InP-EML 缺口估計原文；Innolight／Eoptolink 年報上游基板來源；具名賣方量化。

缺段（§7-2）：中國放行量之官方序列本輪未見；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 瓶頸已被廣泛報導、價格已漲 250%，JX／Sumitomo 擴產公告在前；已定價 | 載體 3、4 | 已定價 |
| R2 | AXT 自稱許可「more regularity … in certain geographic regions」，放行常規化使閘門鬆弛 | 載體 2 | 方向 |
| R3 | 雷射瓶頸主因為磊晶／晶粒良率與 EML 產能，非基板；基板缺口不綁定 | 載體 4（McKinsey 缺口指 InP-EML） | 機制歸因 |
| R4 | 放行量無官方週期序列，只有零散報導；守恆不可閉合 | 載體 4、7 | 可觀測 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 中國 InP 基板許可放行量或 AXT InP 出貨量**無 ≥ 4 期**可對齊序列（AXT 10-Q 產品別營收可作美元代理；若連美元代理亦缺 → 觸發）；或
(2) 非中國 InP 基板產能／產出（Sumitomo、JX、雷射商自製）無公開可加總數，質量平衡不可閉合（L12-P#3 型可觀測性死因）；或
(3) `[D]` 量級：可得最佳代理之缺口（需求 − 上界，或 AXT 未放行在手訂單）÷ 下游雷射／光模組商（COHR、LITE 等）相關營收 < 1%，或基板成本 ÷ 光模組售價使閘門不綁定；或
(4) 公司或具名賣方已以許可放行量量化雷射出貨上界（已定價）；或
(5) 機制歸因：具名一手來源明示雷射瓶頸主因在磊晶／晶粒而非基板（R3 成立）；或
(6) 12 個月內無可觀測驅動：2026-11-27 暫停期滿無變化、無新 MOFCOM 公告、AXT 季報許可段無變化。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：AXT 產品別營收（InP／GaAs／Ge／原料 JV）、在手訂單、存貨；雷射商之供應商集中與採購承諾。2. 可交易工具：基板商／雷射商／模組商（不選）。3. 半衰期：許可按單；季報季度；暫停期限固定日；擴產年度級。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L12［P］格加「#4 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0093；`export/LEADS_算力收支.md` 追加 2 筆（AXT InP 營收、JX InP 投資）。不改 L12-P#1–#3、L12-A、L12-I、L4-P#3、L1-I#3、N-02 結論。
