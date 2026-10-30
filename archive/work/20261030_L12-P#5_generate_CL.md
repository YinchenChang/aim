# L12-P#5 生成卡｜監理與法制：守恆（臭氧非達標區 NOx 排放預算——新增現場燃燒發電之 NOx ≤ 抵銷額度 ÷ 抵銷比）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260922_L12-P_generate_GK.md；archive/work/20261008_L12-P#2_generate_CL.md；archive/work/20261015_L12-P#3_generate_CL.md；archive/work/20261023_L12-P#4_generate_CL.md；archive/work/20261023_L12-P#4_test1_CL.md | EMITS: work/20261030_L12-P#5_generate_CL.md -->
**日期：** 2026-10-30　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 0→1／6）　**格：** L12-P　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。非「已殺／刻意排除」格中最後測一最舊＝2026-10-23（L12-P#4）→ L12-P；既有生成 4 份 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `NOx nonattainment turbine permit`，命中 0 筆；未使用。內部數字（§12）：未取用。
- 比對（本卡須異型）：
  - **L12-P#1**（`archive/drive/USED_20260922_L12-P_generate_GK.md`）：TIC 物理測試時長底板；死於證書庫不可加總。本卡不涉測試。
  - **L12-P#2**（`archive/work/20261008_L12-P#2_generate_CL.md`）：審查佇列 L＝λW；死於機關端流量持平。本卡之守恆量為**排放噸數**（存量額度），非審查工時或佇列。
  - **L12-P#3**（`archive/work/20261015_L12-P#3_generate_CL.md`）：美國出口管制下 AI 伺服器外流質量平衡；死於出貨地序列不可得。本卡為**國內**、**地理封閉之排放預算**，無跨境流。
  - **L12-P#4**（`archive/work/20261023_L12-P#4_generate_CL.md`）：中國出口許可下 InP 基板流入閘門；上界由許可放行節奏決定。本卡上界由**既存可抵銷減量之存量**（ERC）× 法定抵銷比決定，非許可節奏；守恆量在空氣品質區（airshed）內。
  - **T-11／L1-P**（刻意排除）：T-11＝電力物理／設備敘事。本卡不主張電網容量、機組交期或電力物理約束；守恆在監理工具（NNSR 抵銷）層。不碰 L1-P。
  - **C-P4**（ARCH_dead #19：水耗非損益科目）：同為「環境約束」，死因屬可觀測性；本卡之可觀測載體為**州機關 ERC 登錄／交易報告**（序列）與許可檔，否決 (1)(3) 即檢此死因是否重演。
  - **L1-A#2**（Bloom 保固認列）：同一主體，不同機制；本卡不用保固或收入認列。
- §7-10 領域最近公開：EPA NNSR 抵銷指引（2026-07-01，Szabo 備忘錄）；Williams Mullen 解讀（2026-09-09）；ALL4「Data Centers 2026 Look Ahead」（2026-01-29，修訂 2026-08-18）；Newsweek 引 HARC 德州資料中心排放模擬（2026-10-28）；SJVAPCD 2026 ERC 交易成本表（2026-07-22）。下一檢查點＝Abbott 指示 TCEQ 暫停資料中心許可至 ERCOT 稽核完成（Newsweek 2026-10-28）之解除日；EPA DFW／HGB 2015 臭氧標準重分類。

## 1. 落差一句

臭氧非達標區內，新增主要源之 NOx 須以同區既存減量（ERC）按法定比率抵銷，故**區內新增現場燃燒發電（燃氣輪機／往復機）之 NOx ≤ 可取得 ERC 存量 ÷ 抵銷比**；DFW 於三年內兩度重分類、主要源門檻 100→25 tpy NOx，Chicago 100→50 tpy，使資料中心「自建電源」敘事在非達標區之上界由**排放預算**而非機組供給決定。種子主張：市場以「表後燃氣發電解決 time-to-power」外推現場發電需求（輪機商、往復機商、燃料電池商），未以區內 NOx 預算閉合；**方向未定**——可能使非達標區需求轉向低 NOx 技術（燃料電池；Bloom 10-K 自稱「significant air permitting advantages」）或轉往達標區，亦可能因 EPA 2026-07-01 指引（允許先發許可、運轉前才須取得 ERC）、DOE 202(c) 緊急令、或採 < 門檻之合成次要源設計而使預算不綁定。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [P] 守恆：空氣品質區內 NOx 質量預算；規則端＝CAA §173 NNSR 抵銷、40 CFR 51.165、州 SIP（TX 30 TAC Ch.116 Subch. B Div.5、TX ch.101 Subch. H ERC 計畫）、NSPS KKKKa（含暫置輪機子類） |
| 恆等（僅定義） | 區內新增許可 NOx（tpy）× 抵銷比 ≤ 可取得 ERC（tpy）＋ 同源內部減量；可新增現場發電 MW ≤ 上式 ÷（每 MW 年 NOx 排放率 × 容量因子）；門檻下設計：每設施 < 主要源門檻（DFW 25 tpy）則免抵銷 |
| 已讀事實 | ALL4（2026-01-29）：「The Dallas/Fort Worth (DFW), TX area has been redesignated twice in three years, reducing the major source threshold from 100 tpy of NOX to its current 25 tpy NOX.」；「The Greater Chicago, IL area was redesignated in January 2025 to serious nonattainment, lowering the major source threshold from 100 tpy NOX to 50 tpy NOX.」；Maricopa 資料中心「proactively accepted a potential emissions threshold of less than 50 tons per year (tpy) of nitrogen oxides」；暫置輪機子類「up to 850 MMBtu/hr, used in a single location for up to 24 months」。EPA 指引（2026-07-01）：「ERCs must be obtained 'from the same source or other sources in the same nonattainment area'」；NNSR 許可得先發，條件為「an express prohibition on commencing operations until the required ERCs are identified, approved, and secured」。SJVAPCD 2026 ERC 交易：NOx 兩筆 $20,000／ton 與 $9,500／ton（欄位對應待 ANALYST 以 PDF 核對）。Newsweek（2026-10-28，引 HARC）：若資料中心以燃料自發電，NOx「two to 10 times higher」於純電網情境；ERCOT「more than 474 gigawatts」併網請求「about 90 percent were from data centers」；Abbott 指示 TCEQ「halt permits sought by data centers until the ERCOT audit was completed」。Bloom 10-K FY25（sec.py 實讀）：「the Energy Server’s emission profile provides for significant air permitting advantages versus competing technologies」；「New York, New Jersey and North Carolina, have specific air permitting exemptions for fuel cells」；grep `NOx`／`nonattainment` 0 筆。 |
| 未證之連結 | 法定抵銷比（CAA §182：severe 1.3:1、serious 1.2:1，本輪未實讀條文）；TCEQ DFW／HGB NOx ERC 存量與成交價序列（TCEQ EBT 交易報告未讀）；資料中心現場發電個案是否為主要源或合成次要源；每 MW NOx 率（輪機 vs 往復機 vs 燃料電池）一手數；現場發電商非達標區訂單占比 |
| 量綱 | NOx tpy；ERC 存量 tpy；$／ton；可支撐 MW（`[D]`）；非達標區訂單 ÷ 總訂單（%） |
| 半衰期 | 許可案（月）；EPA 重分類（年）；ERC 交易季報；暫置輪機 12–24 個月窗 |

## 3. B 端可觀測載體（只指名）

1. ALL4「Data Centers 2026 Look Ahead」https://www.all4inc.com/4-the-record-articles/data-centers-2026-look-ahead/
2. EPA NNSR ERC 指引（2026-07-01）https://www.epa.gov/system/files/documents/2026-06/nonattainment-new-source-review-emission-reduction-credits-erc-guidance_0.pdf ；Williams Mullen 解讀 https://www.williamsmullen.com/insights/news/legal-news/epa-clarifies-timing-emission-reduction-credit-requirements-under
3. SJVAPCD ERC 2026 交易成本 https://apps.valleyair.org/busind/pto/erc/ERCCost2026.pdf
4. Newsweek（HARC 模擬、TCEQ 暫停令）https://newsweek.com/map-shows-texas-data-center-boom-pollution-warning-issued-12624915
5. Bloom Energy 10-K FY25 https://www.sec.gov/Archives/edgar/data/1664703/000162828026006516/be-20251231.htm （Permits and Approvals、Government Regulation 段）
6. TCEQ 185 費／交易會（2026-05-20）https://www.tceq.texas.gov/downloads/air-quality/point-source/185fee/20260520-185fee-tradefair.pdf （未讀）
7. 未讀：TCEQ Emissions Banking and Trading（ERC／DERC）交易季報；TX 30 TAC ch.101 Subch. H；CAA §182(c)(10)/(d)(2) 條文；EPA DFW／HGB 重分類 FR；GEV、CAT（Solar Turbines）、BE、Wärtsilä 等申報之非達標區或空氣許可段；xAI Southaven（MS）、Memphis 輪機許可檔。

缺段（§7-2）：德州 NOx ERC 價格與存量序列本輪未見；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | EPA 2026-07-01 指引允許先發許可、運轉前才取得 ERC，且可分期；抵銷不再卡建設 | 載體 2 | 方向／時序 |
| R2 | DOE 202(c) 緊急令與白宮表態「protect facilities from environmental exceedances」；監理約束可被行政豁免 | 載體 1 | 機制歸因 |
| R3 | 資料中心刻意設計為 < 門檻（Maricopa < 50 tpy 例）或選址達標區（Abilene 等），預算不綁定 | 載體 1 | 量級 |
| R4 | 主約束為電網核准／TCEQ 行政暫停（ERCOT 稽核），非 NOx 預算 | 載體 4 | 機制歸因 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 任一主要非達標區（DFW、HGB、Chicago、Maricopa、DC／NoVA）之 NOx ERC 存量或成交價**無 ≥ 4 期**可對齊公開序列（C-P4 型可觀測性死因）；或
(2) 已知資料中心現場燃燒發電案在非達標區者，多數以 < 主要源門檻（合成次要源）或暫置輪機子類取得許可，免 NNSR 抵銷（R3 成立）；或
(3) `[D]` 量級：可得最佳代理之區內 ERC 存量可支撐 MW ÷ 該區資料中心現場發電規劃 MW > 3（預算鬆弛），或 ERC 成本 ÷ 現場發電每 MW 資本支出 < 1%（不綁定）；或
(4) 公司（輪機／往復機／燃料電池商）或具名賣方已以非達標區 NOx 預算量化訂單上界或地區組合（已定價）；或
(5) 機制歸因：具名一手來源明示非達標區資料中心現場發電之延宕主因為電網／行政暫停／機組交期而非抵銷（R4 成立）；或
(6) 12 個月內無可觀測驅動：無重分類、無 TCEQ 暫停解除或延長、ERC 價格無新交易、無新 EPA／州抵銷規則。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：現場發電商之地區別訂單／backlog、許可延宕之收入遞延；資料中心開發商之 ERC 取得成本（資本化或費用）。2. 可交易工具：輪機商／往復機商／燃料電池商（不選）。3. 半衰期：許可案月級；重分類年級；ERC 交易季級。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L12［P］格加「#5 已生成」；`AIM_FUNNEL.md` 日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0135；`export/LEADS_算力收支.md` 追加 1 筆（ERCOT 併網請求，Newsweek 轉述）。不改 L12-P#1–#4、L12-A、L12-I、L1-P（T-11）、L1-A#2、C-P4 結論。
