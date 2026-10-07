<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.0@CL | CONSUMES: 20260913_HUB-to-AIS_02_GK.md §1 僅研究任務；AIM_CHARTER.md；AIM_FUNNEL.md | EMITS: L2-A 測二終態；不發 T／L／M -->
# L2-A 測二｜表達點 (i) 產業構件成本指數 B 端實讀

**角色：** ANALYST@GK　**日期：** 2026-09-13　**候選：** L2-A（資料中心實體：會計恆等）
**任務邊界：** 只測表達點 (i)。不測冷卻設備商、不測建照工料清單、不寫 T／L／M、不取 LEDGER／P。
**原陳述（生成物）：** 每 MW 建置成本＝(土建+機電+冷卻)÷可用 MW；高熱密度下冷卻佔比非線性上升，故每 MW 線性外推系統性低估。
**測一已否：** REIT 10-K／EX-99.1 合計欄。本輪不得再用 DLR／EQIX 同型交差。

---

## 終態

**部分通過（載體可讀；原陳述未完整證實）。不進 T。**

| 測試項 | 結果 |
|---|---|
| 具名產業指數、非 REIT、已實讀 | **通過**　Turner & Townsend *Data Centre Construction Cost Index 2025–2026* |
| 土建／機電／冷卻三分 | **不通過**　指數切的是「核心／殼＋建築｜機械（含設備）｜電氣（含設備）｜總包」；冷卻 ⊂ 機械，未單列 |
| 冷卻佔比對熱密度 | **弱通過**　僅空冷 vs 液冷兩檔（同 IT 容量），無 kW／櫃連續軸，無非線性擬合 |
| 線性 $/MW 外推低估 | **方向支持**　美液冷相對同 IT-MW 空冷總成本 +7–10% `[V]`；機械美元約 +60%，殼體美元約 −30% 部分對沖 |
| 升格 T | **否**　缺可單位化「冷卻佔比＝f(熱密度)」；先驗無外部連續參照物 |

失效歸因（CHARTER §7-2）：不是檢索失敗。載體存在且已讀。失敗在量綱：指數給的是架構二分的成本結構，不是熱密度函數。

---

## 已實讀載體

### 主載體（通過「產業構件指數」門檻）

**Turner & Townsend, Data Centre Construction Cost Index 2025–2026**（第 9 年；2025-11-05 公開頁）。領域最近一次指數更新＝2025-11（CHARTER §7-10）。2026–2027 版至本輪日未見。

| 欄 | 值 | 標記 |
|---|---|---|
| 樣本 | >300 件在建／近完；>20 國；專家調查 ~250–280 | `[V]` |
| 基準模型 | 空冷、build-to-suit 超大規模、IT 負荷 30–50 MW | `[V]` |
| 單位 | US$/W（IT 負荷） | `[V]` |
| 計入 | 殼與核心、建築裝修、機電裝修、總包預備／利潤／或有、機電設備（含稅／關／運） | `[V]` |
| 不计 | 業主直接費、土地、公用事業外線、異常地盤、場地工程、主動 IT、辦公室光纖、專業服務費 | `[V]` |

美國空冷 vs 液冷（同 IT 容量）指示性結構 `[V]`：

| 類 | 空冷 | 液冷 |
|---|---|---|
| 總包／GR／總包費 | 10% | 10% |
| 核心／殼＋建築 | 14% | 9% |
| 機械（含設備） | 22% | 33% |
| 電氣（含設備） | 54% | 48% |
| 合計 | 100% | 100% |

液冷總成本相對空冷：**+7–10%**（Hive；美國；同 IT 容量）`[V]`。指數正文自述：高功率密度可縮小建築面積；AI「全球基準資料尚未充分」。無 kW／櫃數字。

**算術（分析者，非指數原文）`[A]`：** 令空冷總成本＝1.00／IT-W，液冷＝1.07–1.10。

- 機械美元：0.22 → 0.353–0.363（約 +60–65%）
- 殼＋建築美元：0.14 → 0.096–0.099（約 −29–31%）
- 電氣美元：0.54 → 0.514–0.528（約 −5% 至 −2%）

含義：用空冷 $/IT-MW 直線套到液冷／高密，總額低估 7–10%；低估集中在機械桶，殼體桶反向縮小。此為兩點階躍，不是非線性曲線。

### 次載體（讀過；不能當 (i) 的主證明）

| 載體 | 最近公開 | 讀到什麼 | 為何不夠 |
|---|---|---|---|
| JLL 2026 Global Data Center Outlook（轉引） | 2026 展望 | 全球 shell-and-core 均 $11.3M／MW；AI 承租適配可至 $25M／MW | 合計層，無構件切、無密度函數 |
| Cushman & Wakefield 2026 Data Center Development Cost Guide | 2026-09-03 | 美加全新綠地均 $17.6M／MW（不含晶片）；較 2024Q4 版 +21%／MW；電力基礎設施佔 21%，核心＋殼＋場地 17%，或有 16% | 電力≠冷卻；無空／液或 kW／櫃切 |
| Mortenson Construction Cost Index（先進製造／總指數，2025Q4） | 2026 初 | 投入品通膨（HVAC、銅管、電氣） | 非資料中心構件×密度指數 |
| BCS Q1 2026 commercial DC costing | 2026 Q1 | 單一樣本結構：電氣 43%、機械 16.8%、CSA 冷殼 11.2% 等 | 一點、非對熱密度 |
| RSMeans 2026 Mechanical Costs | 2026 目錄 | 有冷卻產生系統單價章節 | 付費單位成本書，非產業 DC／MW 指數；本輪未購全文 |

未用 REIT 10-K。未宣稱 RSMeans 可分離（未讀全書）。

---

## 對原陳述的對應

1. **恆等式形式：** 指數可讀的是 (殼+機械+電氣+總包)／IT-MW，不是 (土建+機電+冷卻)／可用 MW。「機電」被劈成機械／電氣；「冷卻」未獨立；「可用 MW」≈ IT 負荷 MW（指數單位），不是賣出櫃位或總設施電力。
2. **冷卻佔比↑：** 只觀察到機械佔比 22%→33%。冷卻是機械的子集，佔比升幅的分子分母都可能動。
3. **非線性：** 未測。兩架構點不能證 f''>0。
4. **線性外推低估：** 在「空冷 $/IT-MW → 液冷同 IT-MW」這一個外推上，方向成立（+7–10%）。指數同時寫密度可縮殼，故組成在變，不是單一冷卻項膨脹。

**競爭讀法：** 液冷溢價是技術系統複雜度＋設備，不完全是「熱密度的連續函數」；同 IT-MW 下殼體變便宜，可能使部分高密案的土建／MW 下降。mega-campus 規模經濟是另一項對沖。

---

## 讀取 URL

1. https://www.turnerandtownsend.com/insights/data-centre-construction-cost-index-2025-2026/
2. https://reports.turnerandtownsend.com/data-centre-construction-cost-index-2025/
3. https://reports.turnerandtownsend.com/data-centre-construction-cost-index-2025/data-centre-cost-trends
4. https://reports.turnerandtownsend.com/data-centre-construction-cost-index-2025/methodology
5. https://reports.turnerandtownsend.com/data-centre-construction-cost-index-2025/foreword
6. https://www.communicationstoday.co.in/wp-content/uploads/2025/11/Data-centre-cost-trends-Data-centre-construction-cost-index-2025.pdf
7. https://assets.foleon.com/eu-central-1/de-uploads-7e3kk3/48604/protected_2025-2026_data_centre_construction_cost_index_jp_.639addcd825f.pdf
8. https://datacenterscope.com/cooling/data-center-cooling-cost/
9. https://www.cushmanwakefield.com/en/united-states/insights/data-center-development-cost-guide
10. https://ir.cushmanwakefield.com/news/press-release-details/2026/Cushman--Wakefield-Releases-2026-Data-Center-Development-Cost-Guide-Citing-21-Rise-in-Per-MW-Construction-Costs/default.aspx
11. https://axis-intelligence.com/data-center-construction-cost-statistics/
12. https://news.constructconnect.com/data-center-construction-input-costs-rise-significantly

無封存檔可取（Drive `query`／`work` 本輪列出為空）。外部檢索＝上列。

---

## 不進 T 的理由（CHARTER §1／§3）

進 T 需要機制數值窗與外部參照先驗。本輪可寫入的只有「美液冷相對空冷總成本 +7–10%、機械佔比 +11 ppt」。這不夠把 H1 寫成倍數，也不夠把冷卻項從機械桶拆出後再對 12 個月重定價窗。L2-A 維持漏斗「已測、未升級」。表達點 (ii)(iii) 本角色不派。

複查觸發器：T&T 2026–2027 指數若首次公布 kW／櫃或冷卻單列；或任一公開指數給出 ≥3 個密度點的構件切。

**（檔結束。）**
