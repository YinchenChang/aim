# L8-A#6 生成卡｜標註／驗證：會計恆等（服務線組成恆等——「AI Services」收入＝標註／LLM 資料工程＋自駕／機器人遠端與現場作業＋自 Trust & Safety 移入之工作；3Q26 起定義擴寫、前期未重編）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/INDEX.json；archive/work/20261007_L8-A#2_generate_CL.md；archive/work/20261015_L8-A#3_generate_CL.md；archive/work/20261023_L8-A#4_generate_CL.md；archive/work/20261030_L8-A#5_generate_CL.md；work/20261030_L8-A#5_test1_CL.md | EMITS: work/20261106_L8-A#6_generate_CL.md -->
**日期：** 2026-11-06　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1→2／6）　**格：** L8-A　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。非「已殺／刻意排除」格中最後測一最舊＝2026-10-30（L8-A#5、L8-I#5、L9-A#5、L9-I#5、L12-P#5）→ 依表序取 **L8-A**（L8-P 已殺不取）；既有生成 5 份 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `TaskUs`／`autonomous vehicle`／`annotation`，命中 0 筆。內部數字（§12）：未取用。
- 比對（本卡須異型）：
  - **L8-A#1**（GK）：支出 ÷ 有效條數（產出單位分母）；死於分母不可得。本卡不用產出單位。
  - **L8-A#2**：賣方未開票收入（認列時點）。本卡不涉認列時點。
  - **L8-A#3**：INOD 客戶預付轉付成本（主理人／代理人、營運資本）。本卡不涉營運資本。
  - **L8-A#4**：買方（META）持 Scale 股權之衡量替代法帳面。本卡不涉投資帳面。
  - **L8-A#5**：匯兌損益之科目路由（INOD vs TASK）；測一死於 (2)（非標註層特有）。本卡之組成問題**只存在於標註層**：「AI 服務」標籤下混入非標註之實體作業，且移入原內容審核工作；不涉匯兌、不跨兩家比較口徑。
  - **L8-I#2**（Meta→Scale 持股轉單、TaskUs 客戶量轉移；誘因）：本卡不以客戶流向或集中度為落差（Client A 27%→17% 僅背景）。
  - **C-I2**（專家單價歸因）：本卡不涉單價。L8-P（分鐘／條）：不涉。
  - 他層同族：L14-A 型（AI 行與非 AI 行可對帳與否）屬買方；本卡為賣方服務線標籤之組成，主體與科目異。重疊不構成丟棄。
- §7-10 領域最近公開：TASK 10-Q 3Q26（申報 2026-11-05，acc `0001829864-26-000156`）與 8-K 業績稿（2026-11-04，acc `0001829864-26-000154`）。下一檢查點＝TASK 10-K FY2026（約 2027-03 上旬）。

## 1. 落差一句

TASK 之「AI Services」服務線被市場與公司本身作為標註／LLM 資料需求之代理（業績稿：「AI Services eclipsed $250 million in trailing twelve-month revenue」「fastest growing service line for the seventh quarter in a row」），但其定義於 **3Q26 10-Q 首次擴寫**：「Also included in this offering are our remote operations and field services for developers of autonomous vehicles and robotics」（FY2025 10-K、1Q26、2Q26 10-Q 之同段無此句；`field services` 於該三檔 0 命中），而 3Q25 比較數 58,678 千與 3Q25 10-Q 原數相同（未重編）。恆等：**AI Services ≡ 標註／LLM 資料工程 ＋ 自駕／機器人遠端與現場作業 ＋ 自 Trust & Safety 移入之模型維護／評測**。3Q26 地理拆解（10-Q MD&A 以各地前期基數之百分點列示）`[D]`：美國交付 AI Services 年增 ≈ 80.5% × 32,310 ≈ 26.0 百萬，菲律賓 ≈ −6.5% × 160,942 ≈ −10.5 百萬，印度 ≈ −4.5% × 38,973 ≈ −1.8 百萬，其他 ≈ +3.5% × 66,488 ≈ +2.3 百萬；合計 ≈ +16.1 百萬，與表列 +16,281 千對帳。即**美國以外之 AI Services 年減約 10 百萬，全線成長全數且超額來自美國交付**；而成本段同檔稱「expansion into field services for developers of autonomous vehicles」。9M26 同法：美國 AI ≈ 62.5% × 97,924 ≈ +61.2 百萬 vs 全線 +46.3 百萬 `[D]`。種子主張：以「AI Services」成長率推估標註層需求者，量到的主要是自駕現場／遠端作業（onshore、低毛利）與重分類，離岸標註本體可能在收縮。**方向未定**：若現場作業本身被視為 AI 需求之延伸，則無落差。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：ASC 606 收入分拆（disaggregation）之服務線歸屬 × 定義擴寫未重編 → 標籤成長 ≠ 標註成長 |
| 已讀事實 | 3Q26 10-Q：AI Services 74,959 千（3Q25 58,678，+27.7%）；T&S 63,867（−15.8%）；美國交付 56,444（+74.7%），「AI Services contributed 80.5% of the total increase primarily driven by clients in Mobility, Logistics & Travel」；菲律賓「AI Services contributed 6.5% of the total decrease primarily driven by clients in Social Media」；Cost of services「costs associated with our expansion into field services for developers of autonomous vehicles」。業績稿：「accelerating growth in AI Services, where we support developers of autonomous vehicles, robots, and frontier AI models」。1Q26 電話會（MarketBeat 摘要，二手）：「critical remote assistance and roadside emergency response」「some Trust & Safety revenues have shifted into AI Services」「shift toward lower-margin U.S.-based delivery」。 |
| 未證之連結 | 三組成之金額拆分（10-Q 未分列）；T&S→AI 移轉之金額與起點；定義擴寫前之 AV 現場收入是否已在 AI Services 內（即「描述補寫」vs「範圍擴張」）；賣方是否以 AI Services 作標註需求代理並據以給倍數。此即測一第一關。 |
| 量綱 | 非標註組成 ÷ AI Services（%）；美國以外 AI Services 年增率（%）；AI Services 成長中重分類成分（pp） |
| 選擇變數 | 管理層：服務線定義、客戶工作之服務線歸屬、是否重編前期 |
| 半衰期 | 每季重報；FY2026 10-K 為首個年度分拆檢查點 |

## 3. B 端可觀測載體（只指名）

1. TASK 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/1829864/000182986426000156/task-20260930.htm （Note 1 服務線定義、收入分拆附註、MD&A 服務線與地理表、Cost of services 敘述、Top clients 表）
2. TASK 8-K 3Q26 業績稿 https://www.sec.gov/Archives/edgar/data/1829864/000182986426000154/earningsreleaseex991q32026.htm
3. 對照定義：TASK 10-K FY2025 https://www.sec.gov/Archives/edgar/data/1829864/000182986426000012/task-20251231.htm ；10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1829864/000182986426000149/task-20260630.htm ；10-Q 1Q26 https://www.sec.gov/Archives/edgar/data/1829864/000182986426000113/task-20260331.htm ；10-Q 3Q25 https://www.sec.gov/Archives/edgar/data/1829864/000182986425000132/task-20250930.htm
4. 二手（電話會摘要，非逐字稿）：https://www.marketbeat.com/instant-alerts/taskus-q1-earnings-call-highlights-2026-05-07/ ；https://www.marketbeat.com/instant-alerts/taskus-q2-earnings-call-highlights-2026-08-06/
5. 待測一指名讀：1Q–3Q26 官方電話會逐字稿（AV 現場收入、T&S 移轉之量化句）；TASK FY2026 10-K；同層 INOD 10-Q 3Q26 之分部定義是否同型擴寫；具名賣方以 AI Services 估值之原文；AV 客戶（Mobility 垂直）之公開外包公告。

缺段（§7-2）：組成金額、移轉起點、賣方原文、逐字稿；本輪只讀上列；非「不存在」。Barchart 1Q26 分析師問答頁 fetch 回空白，失敗歸因＝頁面渲染，非內容不存在。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 公司已在 10-Q 定義、MD&A 地理拆解與業績稿明言自駕／機器人為成長來源；資訊公開，屬已揭露之組成 | 載體 1、2 | 無資訊落差（已定價） |
| R2 | 自駕遠端協助、資料採集與場景驗證本即「physical AI」訓練／驗證鏈之一環，屬 L8 之延伸而非異質業務 | 載體 2（CEO 句） | 組成之分界不具經濟意義 |
| R3 | 定義擴寫可能只是補寫既有範圍，前期數字已含 AV 作業，無重編需要 | 載體 1、3 | 恆等無時序斷點 |
| R4 | 量級：AI Services 佔 3Q26 服務收入約 24% `[D]`；組成誤讀對全公司估值影響有限 `[A]` | 載體 1 | 終端條件，本輪不篩（§7-3），僅列 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法確認 3Q26 10-Q 之 AI Services 定義相對 FY2025 10-K／1Q–2Q26 10-Q 有擴寫，或地理百分點拆解不能重算出「美國以外 AI Services 年減」；或
(2) 公司於 10-Q／10-K／業績稿／官方逐字稿已量化 AV 現場作業或 T&S 移入之金額（組成已公開，恆等無落差）；或具名賣方已以剔除 AV 現場之標註本體成長率估值（已定價）；或
(3) 可運作對照只能寫成一般「服務線重分類」，而無標註層特有結構（標註需求代理之標籤含非標註實體作業、離岸 vs 美國交付之毛利差）；或
(4) `[D]` 量級：最近 4 季內，美國以外 AI Services 年增率 ≥ 0（即離岸標註本體未縮），且可歸 T&S 移入者 < AI Services 之 5%；或
(5) 12 個月內無可觀測驅動：無 4Q26 業績／FY2026 10-K 之可指名日期，或該等申報恢復前期重編使組成可分離。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：收入分拆附註（服務線 × 地理）、Cost of services、Adjusted EBITDA margin。2. 可交易工具：TASK（不選）。3. 半衰期：季度重報 vs ≥ 12 個月窗。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L8［A］格加「#6 已生成」；`AIM_FUNNEL.md` 日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0172；`export/LEADS_算力收支.md` 追加 1 列（TASK 3Q26 AI Services 季收入）。不改 L8-A#1–#5、L8-I／#2–#5、L8-P、C-I2 結論。
