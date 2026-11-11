# L7-I#6 生成卡｜模型層：誘因（互補品捕獲決定開放邊界：擁雲之發行者只開放「推論不落在自家雲」之小尺寸權重、旗艦閉源只經自家雲 API → 下載量／衍生模型數與雲營收之連結被誘因本身切斷）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；AIM_FUNNEL.md；archive/drive/USED_20260930_L7-I_generate_GK.md；archive/work/20261013_L7-I#2_generate_CL.md；archive/work/20261020_L7-I#3_generate_CL.md；archive/work/20261027_L7-I#4_generate_CL.md；archive/work/20261103_L7-I#5_generate_CL.md；work/20261103_L7-I#5_test1_CL.md | EMITS: work/20261111_L7-I#6_generate_CL.md -->
**日期：** 2026-11-11　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 2→3／6）　**格：** L7-I　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L7-A#6 本日測一，Q-0193 done）。非已殺／刻意排除格中最後測試日最舊＝2026-11-03（L7-I#5、L10-P／A／I#5、L11-A／I#5、L13-A#5）；依表序取 **L7-I**。既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py open-weight Qwen "open source" Llama`，命中 9 筆（SRC_MOD_047／048、SRC_PERF_036／037、SRC_PRC_038–040、SRC_CAP_006、SRC_DEM_052），皆為單價／效能／訓練效率，**與本格誘因無關**；未用。內部數字（§12）未取用。載體全由本輪 WebSearch／WebFetch 實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L7-I#1**（不通過）：評測取用權合約性。本卡不論評測。
  - **L7-I#2**（部分通過）：人才外部選擇權 × SBC。不論人才。
  - **L7-I#3**（部分通過）：實驗室直營與 API 大客戶之通路衝突。本卡不論客戶集中或換供應商；主體是**權重開放與否之決策**。
  - **L7-I#4**（部分通過）：照付不議承諾 → 降價填充。本卡不論承諾容量或定價。
  - **L7-I#5**（不通過；(3)(6) 觸發）：RSP 自我約束。本卡不論安全門檻；且表達主體為**已上市**擁雲發行者，避開 #5 之 (6)。
  - **L15-I#2**（測一不通過）：雲商共同出資之中立開源**軟體引擎**之授權防線。本卡為模型**權重**、發行者自釋出、無基金會；測一須查 L15-I#2 死因是否同樣適用。
  - **L6-I#6**（部分通過）：雲供給方兼實驗室股東之總報酬誘因。本卡不論持股。
  - **C-I1**（死 #10）：估值歸因權重能力。本卡不主張估值歸因於權重。
  - **C-A5**（死 #13）：模型層價格不可分離／L7 未上市。本卡表達主體已上市；但「API 營收不分列」風險相同，列否決 (2)。
  - **C-A1**（死 #6）：AI COGS 不可分列。同 (2)。
- §7-10 領域最近公開：Alibaba 2026-06 季業績（2026-08-20 新聞稿）；Asia Times（2026-11-07，Qwen4 預告無名稱／規格）；Meta Muse Glimmer（2026-08-10）。下一檢查點＝Alibaba 2026-09 季業績、Qwen4 發布型態。

## 1. 落差一句

擁雲之模型發行者（Alibaba）以「開源 Qwen → 生態採用 → 雲端變現」敘述其 AI 雲成長（蔡崇信 2026-02-06：「Our Qwen model is open source, but we also run our cloud business and today we're monetizing」；2026-08-20 新聞稿：開源策略「turning ecosystem adoption into cloud monetization opportunities」，下載 > 30 億、衍生 > 30 萬），市場亦以下載／衍生數作雲營收之領先指標；但互補品捕獲誘因預測：發行者只開放**推論不在自家雲**之尺寸（單卡／本機；「developer-friendly sizes」、Qwen-27B「for local deployment」），而能在資料中心規模服務、可經自家雲收費之旗艦一律閉源（Qwen3-Max 2025-09 起、Qwen3.5-Omni／3.6-Plus 2026-03／04「accessible only via its official cloud platform」）。若然，下載與衍生量集中於**捕獲率最低**之區段，對雲營收之解釋力應趨零，雲營收實由閉源 API 與通用算力驅動。種子主張：以開源採用指標外推擁雲發行者 AI 雲營收者，高估開源之貢獻、低估其閉源化（開源邊界內縮）之營收意義。本卡不定方向與量級，只立可拒絕之誘因鏈。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因（互補品捕獲：開放與否 ＝ 該尺寸推論落在自家雲之機率之函數；捕獲率高 → 閉源經 API；捕獲率低 → 開放換生態） |
| 量綱 | `[D]` 開放邊界 s*＝當期最大開放權重參數量 ÷ 當期旗艦參數量（或「旗艦是否開放」之二元序列）；`[D]` c＝自家雲上執行之開源衍生推論占比（若揭露）；AI-related product revenue 與 AI Cloud and Compute Services 營收季序列；MaaS（API）營收分列（若揭露） |
| 可見端 | 發行日與授權型態（Hugging Face／官方部落格）；季業績新聞稿與 20-F／6-K 分部；管理層對開源與雲之歸因句 |
| 指名不可見端 | c（自家雲捕獲率）；MaaS 與 IaaS 之營收拆分（新聞稿未見）；開源衍生在他雲／本機之推論量 |
| 主張 | 旗艦閉源化持續、開放邊界 s* 不升；且揭露可分離時，AI 雲營收增量主要來自閉源 API 與通用算力而非開源衍生；可由「旗艦全尺寸開放」「無擁雲同業對照」「c 高（開源推論主要在自家雲）」「已被具名建模」或「不可分列」拒絕 |
| 外部參照物（測一查證） | 互補品商品化前例（例：Google 開放 Android 換搜尋廣告；Red Hat／MongoDB 授權收緊）；測一取具名一手案例 |
| 表達工具型態（只指名，不選券） | 擁雲之模型發行者普通股／ADR；不選券 |
| 對照 | Meta（無對外雲；2026-08 開放 30B Muse Glimmer、旗艦 Muse Spark 閉源、稱將開放 Spark 1.2 權重）：若無互補雲者呈相同「小開大閉」型態，則型態非互補品捕獲所致（否決 (5)） |
| 重疊 | L15-I#2（開源×雲）、L6-I#6（雲×實驗室）、L7-I#3（通路）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. A1 Alibaba 2026-06 季業績新聞稿（2026-08-20）https://www.alibabagroup.com/document-2027233133950140416 ——「AI Cloud and Compute Services revenue reached US$7.1 billion, up 45% year-over-year」；「AI-related product revenue of US$1.8 billion extended triple-digit year-over-year growth for the twelfth consecutive quarter」；Qwen 下載 > 30 億、衍生 > 300,000；開源策略「turning ecosystem adoption into cloud monetization opportunities」；季資本支出近 US$10B（YoY +75%）；本季改四分部。
2. A2 Alibaba 2025-12 季業績新聞稿（2026-03-19）https://www.alibabagroup.com/document-1971445322303406080 ——Cloud Intelligence Group 營收 +36% 至 RMB43,284M；AI-related 第 10 季三位數；Hugging Face 累計下載逾 10 億（2026-01-21）；「Our Model-as-a-Service (MaaS) platform is showing strong growth, emerging as a new engine driving cloud business growth」。
3. A3 Alibaba〈Joe Tsai on the Future of Open-Source AI〉（2026-02-06）https://www.alibabagroup.com/document-1956438710056648704 ——全端開源者「capture value in other layers of tech stack, such as selling cloud computing services」；「Our Qwen model is open source, but we also run our cloud business and today we're monetizing」；投資逾 RMB380B。
4. A4 SCMP（Vincent Chow；日期待測一定位）https://www.scmp.com/tech/big-tech/article/3348844/chinese-ai-giants-pivot-toward-proprietary-models-drive-revenue-performance ——Alibaba Cloud、Zhipu「opted not to open-source some of their latest artificial intelligence models … to capture the full value of their usage through official revenue generating channels」；Alibaba 發言人：Qwen3.5-Omni 不開源因「less popular among developers」。
5. A5 Implicator（2026-04-02，AI 生成經編輯審）https://www.implicator.ai/alibaba-releases-third-closed-source-ai-model-in-three-days-signals-profit-first-strategy.md ——「continue releasing open-source models in "developer-friendly sizes," but the company's flagship releases are moving behind paid APIs」；「The pattern started in September 2025 with Qwen3-Max」。
6. A6 Asia Times（Noman Shah，2026-11-07）https://asiatimes.com/2026/11/what-alibaba-left-blank-about-qwen4/ ——Qwen4 預告無名稱、無規格、無日期；Eddie Wu「praised the existing open-weight Qwen-27B and promised better models for local deployment」；引 Lambert & Brand（arXiv 2604.07190）：2026-02 新上傳衍生 69% 以 Qwen 為底；開源權重「running on machines far from Alibaba's own cloud」。
7. A7 對照：AI Business（2026-08-10）https://aibusiness.com/agentic-ai/meta-reverses-course-with-open-weight-muse-glimmer ——Muse Glimmer 30B、Apache 2.0、單 GPU 本機；Tekonyx Sid Nag：「By releasing weights, Meta lets customers bear much of the infrastructure cost」；Fortune（2026-08-10）https://fortune.com/2026/08/10/meta-brandishes-open-source-ai-models-again-as-zuckerberg-media-blitz-emphasizes-battle-against-chinese-rivals/ ——Glimmer 由閉源 Muse Spark 蒸餾；「plans to open the weights for Muse Spark 1.2」。
8. 指名未讀：Barchart（2026，WebFetch 回 0 字）https://www.barchart.com/story/news/881624/alibaba-stock-is-getting-hit-again-but-qwen-and-cloud-growth-are-surging ；Lambert & Brand arXiv 2604.07190 原文。
9. 測一須另取：Alibaba 最新 20-F／6-K（sec.py）是否分列 MaaS／API 營收或 AI 營收組成；Qwen 各代開放尺寸與旗艦參數量序列；Qwen 開源衍生於他雲（AWS Bedrock／Azure 等）上架與否；具名賣方是否以開源下載換算雲營收或已拆閉源 API。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 開源衍生之訓練、微調、推論確實大量落在 Alibaba 雲（蔡崇信「people are training, developing and running inference … on our infrastructure」），c 高 | A3 | 無洩漏、無落差 |
| R2 | 閉源只為「冷門型號」（Omni 系列 less popular），非系統性；Alibaba 未稱離開開源 | A4 | 無邊界內縮 |
| R3 | 開放權重之理由為成本轉嫁（客戶自付基礎設施），與雲捕獲無關 | A7（Sid Nag） | 誘因型態不同 |
| R4 | 市場已以閉源 API／算力計價（HSBC：AI 變現「systematically underestimated」，方向相反） | A5 轉述 | 錯價方向不同或已定價 |
| R5 | AI 雲營收不分列 MaaS／IaaS／開源衍生，機制不可分離 | A1、A2 | C-A1／C-A5 型 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 具名賣方／研究已拆分擁雲發行者 AI 雲營收為閉源 API vs 開源生態（或已以開源下載換算雲營收並被反駁）——已定價。（僅定性稱「開源帶動雲」不算建模。）
(2) Alibaba 申報（20-F／6-K／業績稿）及他處皆無可把 AI 雲營收分離為 MaaS／API 與其他之揭露，且無替代可觀測量（API 單價 × 用量、token 量）——不可分離（C-A1／C-A5 型）。
(3) 測一日前 Qwen 最新旗艦（Qwen4 或同期最大型號）以開放權重全尺寸釋出——誘因前提（旗艦閉源）被否。
(4) 有一手揭露顯示開源 Qwen 衍生之推論／微調主要（> 50%）在 Alibaba 雲執行——c 高，無洩漏（R1）。
(5) 無對外雲之發行者（Meta）在同期呈相同「小開大閉」型態且最大開放權重比例 s* 不低於 Alibaba——型態非互補品捕獲所致（R3）。門檻凍結：同一 12 個月內兩者 s* 之差 ≤ 0 即觸發。
(6) 可運作對照只能寫成 L7-I#1–#5、L15-I#2、L6-I#6、C-I1 或 C-A5。

複查觸發器（若日後殺）：Alibaba 首次分列 MaaS／API 營收；Qwen4 釋出型態公布；任一擁雲發行者揭露開源模型推論在自家雲之占比；具名賣方發布開源→雲轉換模型。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：AI Cloud and Compute Services 營收、AI-related product revenue、MaaS 歸因句、資本支出。
2. 可交易工具：擁雲發行者 ADR／普通股。不選券。
3. 半衰期：Qwen4 發布型態 → 下一季業績（2026-09 季）→ 20-F 年報分部附註。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` Q-0194；`query/ARCH_matrix.md` L7［I］標「#6 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 3 列（A1 數字）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L7-I#1–#5、L7-A#1–#6、L7-P#1–#6、L15-I#2、L6-I#6、C-A5、C-I1 結論。
