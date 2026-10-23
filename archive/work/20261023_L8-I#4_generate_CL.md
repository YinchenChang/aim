# L8-I#4 生成卡｜標註／驗證：誘因（買方內製／替代誘因——可隨時終止之專案合約 × 兩大客戶占營收七成）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260918_L8-I_generate_GK.md；archive/drive/USED_20260918_L8-I_test1_GK.md；archive/work/20261007_L8-I#2_generate_CL.md；work/20261007_L8-I#2_test1_CL.md；archive/work/20261015_L8-I#3_generate_CL.md；work/20261015_L8-I#3_test1_CL.md；archive/work/20261023_L8-A#4_generate_CL.md | EMITS: work/20261023_L8-I#4_generate_CL.md -->
**日期：** 2026-10-23　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 4／6）　**格：** L8-I　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L8-A#4 本日測一）。非「已殺／刻意排除」格中最後測一最舊者＝2026-10-15 批：L8-I#3、L9-A#3、L9-I#3、L12-P#3（L8-A#3 已於 L8-A#4 輪處理）；依 QUEUE 序次（Q-0048 最先）取 **L8-I**；既有生成 3 份 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `synthetic data annotation insourcing`，命中 13 筆，皆硬體／資料中心／需求指標，與本格無關，未採用。
- 比對（本卡須異型）：
  - **L8-I#1**（`archive/drive/USED_20260918_L8-I_generate_GK.md`；測一 `archive/drive/USED_20260918_L8-I_test1_GK.md`）：品質不可契約；死於爭議／重工率申報層不存在。本卡不涉品質。
  - **L8-I#2**（`work/20261007_L8-I#2_test1_CL.md`）：買方持股**競爭供應商** → 量在供應商之間轉移；死於不分服務線、反向證據。本卡之選擇者同為買方，但選項是**不買**（內製、合成資料、RL 環境自建、直接僱用專家），不是換供應商；且以客戶集中度 × 合約可終止性為可觀測結構。
  - **L8-I#3**（`work/20261015_L8-I#3_test1_CL.md`）：供應商之勞動分類；不涉買方。
  - **L8-A#4**（Meta 持 Scale 股權帳面）、L8-A#3（客戶預付轉付）：會計恆等，不涉買方選擇。
  - **C-I2**（ARCH_dead #12）：專家勞動逆選擇、單價。本卡不在單價。L8-P（分鐘／條）：不涉。重疊不構成丟棄。
- §7-10 領域最近公開：INOD 10-Q 2Q26（期 2026-06-30，2026-08 申報）；TaskUs 10-Q 2Q26；Panabee 2026-08-06。下一檢查點＝INOD／TaskUs 3Q26 10-Q（約 2026-11 上旬）。

## 1. 落差一句

前沿實驗室向標註／資料工程商外購之動機，部分是**暫時性**的（流程未內化、模型尚不足以自產偏好或推理資料）；一旦流程被買方學會、或合成資料／自建 RL 環境之邊際成本低於外購，買方有誘因內製或替代，而外購合約為「primarily at-will」之專案制，替代可在一季內映入供應商營收。INOD 2Q26 兩大客戶合計約 71% 營收（37%＋34%），營收增量「primarily due to higher volume … from existing customer programs」；TaskUs Client A 20%、前十大 64%。種子主張：讀者若把集中客戶之量成長讀成可延續之需求，讀到的部分是買方尚未完成內化之過渡需求。**方向未定**：反向亦成立——實驗室對專家人類資料與 RL 環境之外購可能擴大（Epoch 2026-01：環境合約季六至七位數；Anthropic 討論逾十億之 RL 環境支出），則替代誘因不支配。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：買方之 make-or-buy 選擇；供應商可見營收含買方內化前之過渡量 |
| 已讀事實 | INOD 10-Q 2Q26 Note 13：「One customer generated approximately 37 % and 58 % of the Company's total revenues for the three months ended June 30, 2026 and 2025, respectively. Another customer generated approximately 34 % of the Company's total revenues for the three months ended June 30, 2026.」六個月：46%／26%。MD&A：「Revenue increased primarily due to higher volume for AI data engineering services from existing customer programs.」前瞻聲明：「continuing reliance on project-based work and the primarily at-will nature of such contracts and the ability of these customers to reduce, delay or cancel projects; potential inability to replace projects that are completed, canceled or reduced」。全文「in-house」0 筆、「synthetic」0 筆。TaskUs 10-Q 2Q26：Client A 20%（26%）、Client B 11%、前十大 64%（58%）；「in-house」0 筆。Anthropic Transparency Hub（經 Sacra 轉述，2026-02-26）：訓練使用「a mix of third party data, paid contractors, and data generated internally」；Anthropic 職缺（2026-01-12）Data Operations Manager 職掌含 vendor management 與 pipeline ownership（Sacra 轉述，未讀原文）。 |
| 未證之連結 | 任一大客戶是否已以內製或合成資料替代外購量之一手證據；INOD 兩大客戶之身分與合約剩餘期；供應商營收中「過渡流程」與「持續性專家資料」之可分性。此即測一第一關。 |
| 量綱 | 前二大客戶占營收（%）；季營收增量中既有客戶專案占比（%）；客戶量變動 ÷ 總營收（%）；買方內部資料比重（定性→若有則 %） |
| 選擇變數 | 買方：外購／內製／合成／直接僱用專家；供應商：轉向 RL 環境或平台以提高轉換成本 |
| 半衰期 | 專案制合約一季可調；內化需 2–6 季（假設 `[A]`，待測） |

## 3. B 端可觀測載體（只指名）

1. INOD 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/903651/000110465926092021/inod-20260630x10q.htm （Note 13 集中度、MD&A、前瞻聲明）
2. INOD 8-K 2026-08-06 https://www.sec.gov/Archives/edgar/data/903651/000110465926092133/tm2622364d1_8k.htm 、8-K/A 2026-09-30 https://www.sec.gov/Archives/edgar/data/903651/000110465926112351/tm2626575d1_8ka.htm （測一判讀內容）
3. TaskUs 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/0001829864/000182986426000149/task-20260630.htm （Revenue by Top Clients）
4. Panabee 2026-08-06 https://www.panabee.com/news/innodata-earnings-q2-2026 ——「Two customers account for 71% of total revenue」
5. Sacra「Labs Internalize Data Operations」https://sacra.com/chat/h/88041c4f-930f-4454-8ac5-9513d986553c/ （轉述 Anthropic 職缺與 Transparency Hub；須回原文）
6. Epoch AI 經 CXO Digital Pulse（2026-01-14）https://www.cxodigitalpulse.com/?p=42733 （RL 環境外購規模；反方）
7. 待測一指名讀：INOD 2Q26 電話會逐字稿（StatementDog https://statementdog.com/analysis/INOD/earnings_calls/317212 或 Nasdaq https://www.nasdaq.com/articles/innodata-q2-earnings-call-highlights ）就客戶內製／多元化之原文；Anthropic Transparency Hub 原文；INOD／TaskUs 3Q26 10-Q。

缺段（§7-2）：客戶身分、合約剩餘期、買方內部資料比重；本輪只讀上列；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 外購需求正擴大：RL 環境與專家資料合約規模上升，實驗室傾向向 Mercor／Surge／Turing 等外購 | 載體 6（Epoch） | 誘因方向相反 |
| R2 | 集中度正在下降（最大客戶 58% → 37%），第二大客戶新增，即為多元化，非內化前兆 | 載體 1、4 | 集中風險已在價格中且趨緩 |
| R3 | 「at-will」與集中度為 10-Q 例行風險揭露，讀者早已據以折價 | 載體 1 前瞻聲明 | 已定價 |
| R4 | 內製只限核心資料（Sacra 推論），長尾與專業領域仍外購 | 載體 5 | 替代量級小 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後找不到任一前沿實驗室或 INOD／TaskUs 主要客戶以內製、合成資料或自建環境替代外購之一手或具名原文（只剩推論）；或
(2) 可運作對照只能寫成 L8-I#2（供應商間轉移）或一般之「客戶集中風險」而無買方 make-or-buy 之特有結構（流程可學習 × 專案制可終止）；或
(3) 具名賣方或評等機構已明確以「客戶內製／合成資料替代」量化 INOD 或 TaskUs 營收風險（已定價）；或
(4) `[D]` ≥ 4 季序列顯示既有前二大客戶之美元營收單調上升且新增客戶貢獻增量過半，替代誘因無任何可觀測痕跡；或
(5) 12 個月內無可觀測驅動：無合約到期、客戶揭露或申報期之時點可指名。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：營收集中度附註、剩餘履約義務、客戶預付。2. 可交易工具：上市標註商或其大客戶（不選）。3. 半衰期：專案制調整 vs ≥ 12 個月窗。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L8［I］格加「#4 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0090。不改 L8-I#1–#3、L8-A#1–#4、L8-P、C-I2 結論。
