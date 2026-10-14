# L15-P#2 生成卡｜基礎設施軟體與資料：守恆（雲端承諾池之市集抵扣——第三方基礎設施軟體經雲端市集購買時，與雲端原生服務〔含原生 AI〕共用同一客戶承諾額度）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/FILEIDS.tsv；archive/drive/USED_20261005_L15-P_generate_GK.md；archive/drive/USED_20261005_L15-P_test1_GK.md | EMITS: work/20261014_L15-P#2_generate_CL.md -->
**日期：** 2026-10-14　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1→2／6）　**格：** L15-P　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L14-I#2 已於本日測一，Q-0040 done）。非已殺／刻意排除、無 #2 之格＝L15-P／A／I；`archive/FILEIDS.tsv` 測一時間最舊＝L15-P（2026-10-05T14:38Z；L15-A 10-07T10:57Z；L15-I 10-07T11:25Z）→ **L15-P**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `marketplace`、`commit`，命中 2 筆（DeepSeek V4-Flash config 參數），與本格無關；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L15-P#1**（測一不通過，`archive/drive/USED_20261005_L15-P_test1_GK.md`）：守恆量＝資安分析師注意力（秒×人）；死因＝人數與每人秒數不能在同一序列並列。本卡守恆量是**客戶對雲端商之承諾金額**（美元），不涉人力或注意力。
  - **L14-P#2**（測一不通過）：持池者＝單一 ISV（SNOW 預付容量），池內分 AI／非 AI 消耗。本卡持池者＝**雲端商**（AWS／Azure／GCP 之承諾合約），池內分「原生服務」與「市集上第三方 ISV」；ISV 端只看經市集之通路占比。不涉 SNOW 自家 RPO 滾存條款。
  - **L15-A**（使用量×有效單價）、**L15-I**（遙測出站取用權）、**L6-P#2**（RPO ≤ ρ×MW）、**L6-I#2**（雲端賣方計酬）、**L14-A#1／#2**、**C-A1／C-A5**：不涉單價、出站、電力、計酬、IT ÷ 營收、資本化、AI COGS 分列。
  - **L11-P／L8-P／L9-P**（已殺）：不涉。
- §7-10 領域最近公開：Amazon 10-Q 2Q26（2026-07-30 前後）；Microsoft 10-K FY26（2026-07）；市集抵扣規則最近一次改動＝AWS 2025-05-01「fully deployed on AWS」資格限縮（下列 §3-3）；本輪未見 2026 年規則變更（檢索失敗，非不存在）。

## 1. 落差一句

市場把基礎設施軟體商（觀測、資料庫、資安、搜尋）「經雲端市集成交」之成長讀成新增需求；種子主張：市集成交多為客戶以既有雲端承諾額度抵扣（AWS／GCP 上限約承諾之 25%，Azure 合格品 100%），與雲端原生服務（含原生 AI 推論）共用同一守恆池——原生 AI 消耗吃滿承諾後，市集抵扣之「燒完承諾」誘因消失，ISV 市集通路成長即失其來源。錯價只在把池內再分配讀成池外增量。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆**：客戶承諾額 \(C\)（美元／期）＝原生消耗 \(N\)＋合格市集購買 \(M\)＋短缺費；約束 \(M_{抵扣} \le \kappa C\)（κ≈0.25 AWS／GCP；Azure 合格品 κ=1）。超過 \(C\) 之支出不受池約束 → 守恆只在「預算≈承諾」時綁定 |
| 量綱 | 美元／期（承諾額、市集成交額、原生消耗皆同量綱）；κ 無量綱 |
| 選擇變數 | 客戶採購：同一功能買原生（如 Bedrock／Azure OpenAI）或經市集買 ISV；雲端商：κ 與資格規則 |
| 可見端 | 雲端商 RPO／承諾未認列額；ISV 10-K／10-Q 之市集通路敘述或占比、市集手續費入成本或遞延佣金；第三方市集規模估計 |
| 指名不可見端 | 個別客戶之 \(N\)、\(M\)、\(C\)；市集成交中實際用於抵扣之比例 |
| 表達工具型態（只指名，不選券） | 美股可交易、市集通路占比可觀測之基礎設施軟體商；或雲端商。不選券 |

**不主張方向、不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Amazon 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm （sec.py 實讀）：「performance obligations, primarily related to AWS, associated with commitments in customer contracts … approximately $496 billion as of June 30, 2026. The weighted-average remaining life of our long-term contracts is 6.4 years」；同段提及 2026 Q1 AWS 與 OpenAI 之協議（集中度待測）。
2. Microsoft 10-K FY26 https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm （sec.py 實讀）：「Commercial remaining performance obligation increased 84% to $678 billion」；「approximately 30% … over the next 12 months」。申報層未見 MACC／市集抵扣字樣（grep `marketplace` 只有通路敘述）。
3. 抵扣規則：Redress Compliance https://redresscompliance.com/aws-edp-marketplace-isv-commitment-offset.html ：「up to 25% of your annual EDP commitment can be retired through AWS Marketplace transactions」；「only SaaS products fully deployed on AWS infrastructure qualify」（2025-05）。Omdia（Red Hat 託管 PDF）https://www.redhat.com/rhdc/managed-files/cl-omdia-hyperscalers-procurement-platform-analyst-material-3613126-202602-en.pdf ：市集銷售「$163 billion by 2030, up from $45 billion in 2025」；註「UP TO 25% FOR AWS AND GOOGLE CLOUD; 100% OF SPEND ON AZURE ELIGIBLE OFFERS」。Partner Insight https://partnerinsight.substack.com/p/inside-439b-cloud-commits-milestone ：「Customer cloud commits now reach $439B」（1Q25；Azure 部分為估計）。
4. ISV 申報（sec.py 實讀 10-K）：Datadog FY25 https://www.sec.gov/Archives/edgar/data/1561550/000162828026008819/ddog-20251231.htm ：「An increasing number of sales through cloud provider marketplaces could reduce … our profit margins」；「the pricing of subscriptions from customers in our cloud-provider marketplaces」。MongoDB FY26 https://www.sec.gov/Archives/edgar/data/1441816/000162828026016799/mdb-20260131.htm ：遞延佣金含「fees paid to marketplace vendors」。Elastic FY26 https://www.sec.gov/Archives/edgar/data/1707753/000170775326000018/estc-20260430.htm ：「offer Elastic Cloud on AWS, GCP, and Azure … through direct purchase from us or their respective marketplaces」。Snowflake FY26 10-K 之 marketplace 為自家資料市集，非雲端市集。**四家 10-K 均未見市集通路占比之數字。**

缺段（§7-2）：未取任何 ISV ≥ 4 期市集通路金額或占比；未取雲端商分列市集成交或抵扣額；原生 AI 消耗占承諾之比例不可見；EDGAR FTS 不可用。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 承諾是下限非上限；超額支出不受池約束，雲端承諾以 84%（MSFT）速度擴張 → 池在擴大，守恆不綁定 | Microsoft 10-K FY26（§3-2）；Amazon 10-Q（§3-1） | 機制只在預算≈承諾時成立 |
| R2 | 市集是「已核准預算」之加速通路，縮短銷售週期，屬新增可及市場 | Omdia（§3-3：budgets already approved） | 再分配與增量並存 |
| R3 | 抵扣上限 25% 與 2025-05 資格限縮已把抵扣量壓小 | Redress Compliance（§3-3） | 落差量綱可能過小 |
| R4 | 承諾額集中於少數 AI 實驗室大單（AWS–OpenAI），與企業市集買方非同一池 | Amazon 10-Q（§3-1） | 總承諾額不能代表企業池 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法就 ≥ 2 家美股上市基礎設施軟體商，於 10-K／10-Q 或財報電話會原文取得 ≥ 4 期「經雲端市集成交」之金額或占比（或同口徑代理，如市集手續費），且無法就 ≥ 1 家雲端商取得承諾額之企業（非 AI 實驗室）部分或市集抵扣之申報／原文；或
(2) 可運作對照只能寫成 ISV 自家預付池（L14-P#2）、使用量×單價（L15-A）、出站取用權（L15-I）、RPO ≤ ρ×MW（L6-P#2）、雲端賣方計酬（L6-I#2）或 AI COGS 分列（C-A1）；或
(3) 具名賣方／產業分析已量化「市集成交中抵扣既有承諾 vs 新增預算」之比例並為市場所引用（已定價）；或
(4) `[D]` 量綱不可連接：κ·C 上限相對 ISV 營收、或市集成交額相對承諾總額之比例，使池約束對任一指名 ISV 之營收成長貢獻 < 10%；或 R1 成立（企業承諾 ≈ 實際支出之證據無法取得）；或
(5) 12 個月內無可觀測驅動：無 ISV 市集占比揭露、無雲端商抵扣規則變更、無承諾額企業部分之分列。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：市集手續費（成本或遞延佣金）、通路占比、RPO 企業部分。2. 可交易工具：市集通路占比可觀測之 ISV 或雲端商（不選）。3. 半衰期：抵扣規則改動或企業承諾續約週期（約 1–3 年）。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L15［P］格加「#2 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0041。不改 L15-P#1、L15-A、L15-I、L14-P#2、L6-P#2、L6-I#2、C-A1 結論。
