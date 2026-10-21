# L14-I#3 生成卡｜企業終端需求：誘因（既有雲端承諾之「退抵」誘因：企業把第三方 AI 與 ISV 採購路由至超大雲市集以消化 MACC／EDP 承諾，AI 消耗成長部分為承諾內再分配而非增量需求）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20261005_L14-I_generate_GK.md；archive/work/20261014_L14-I#2_generate_CL.md；work/20261013_L14-P#2_test1_CL.md | EMITS: work/20261021_L14-I#3_generate_CL.md -->
**日期：** 2026-10-21　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 3→4／6）　**格：** L14-I　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L2-A#4 本日測一，Q-0083 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-14 之四格（L14-I#2、L15-P／A／I#2），依表序取第一 → **L14-I**。既有 #1–#2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `marketplace commitment MACC EDP`，0 筆；未用。
- 比對（須異型）：
  - **L14-I#1**（`archive/drive/USED_20261005_L14-I_generate_GK.md`）：人力節省是否回流採購預算。本卡不涉人力節省。
  - **L14-I#2**（`archive/work/20261014_L14-I#2_generate_CL.md`）：裁員理由措辭之敘事誘因。本卡選擇變數是**採購路由**（直購 vs 經雲市集退抵承諾），非措辭。
  - **L14-P#2**（`work/20261013_L14-P#2_test1_CL.md`）：單一供應商之預付容量池（AI 與非 AI 共用）守恆。本卡為**跨供應商**：第三方 AI／ISV 之支出計入超大雲承諾，選擇者為買方、誘因為未達承諾之差額罰則（shortfall）。
  - **L6-I**（backlog 對手方）、**L6-I#2**（賣方計酬）、**L6-I#3**（融資讓價）、**L6-P#3**（容量分割）：皆賣方／雲端側；本卡為買方採購誘因。
  - **C-A1**（已殺，ARCH_dead #6：AI 營收不可分列）：本卡不主張 AI 單位經濟，只主張「增量 vs 再分配」之拆分。
- §7-10 領域最近公開：MSFT 10-K FY26（期 2026-06-30）；SNOW 10-Q 2Q FY27（期 2026-07-31）；CRWD 10-Q（期 2026-07-31）；DDOG 10-Q 2Q26。下一檢查點＝MSFT 10-Q 1Q FY27（2026-10 下旬）、SNOW 3Q FY27（2026-12）。

## 1. 落差一句

市場把超大雲 AI 消耗與商業 RPO 之成長（MSFT 10-K FY26：「Commercial remaining performance obligation increased 84% to $678 billion」）與雲市集交易額之成長讀成**增量**企業 AI 終端需求；種子主張：既有多年承諾（MACC／EDP）使買方有誘因把原本可直購之第三方 AI 模型與 ISV 支出改經雲端帳單以退抵承諾（Claude 於 Foundry「eligible for Microsoft Azure Consumption Commitment (MACC)」；AWS 市集退抵上限「up to 25% of your annual EDP commitment」），故雲端報表上之 AI／市集成長有一部分是承諾內**再分配**（替代原本會落在非 AI 雲服務或直購之支出），不是新增預算。可拒絕之主張＝存在可觀測序列顯示承諾退抵占 AI／市集增量之比例不可忽略，而具名賣方未拆。不主張任何主體價值方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因（I）**：買方承諾 \(K\)、自然消耗 \(U\)；若 \(U < K\)，差額罰則使「把外部支出 \(X\) 改路由入帳」之邊際成本 ≈ 0；雲端認列 \(\Delta R = \Delta R_{增量} + \Delta R_{退抵}\)，\(\Delta R_{退抵} \le \min(X, K-U)\)（AWS 另受 25% 上限） |
| 選擇者 | 企業買方之採購／FinOps（路由選擇）；超大雲（資格規則）；ISV／模型商（是否上架並宣傳「counts toward commit」） |
| 可見端 | 模型商／ISV 之 MACC／EDP 資格頁；SNOW 10-Q「Accrued customer liabilities related to Snowflake Marketplace」（同機制之單一平台版）；ISV 10-Q／10-K 對雲市集銷售之風險與費用敘述；MSFT／AMZN／GOOGL 之 RPO 與存續期 |
| 指名不可見端 | 各雲之承諾退抵占 AI 營收比；承諾未達之 shortfall 金額；承諾續約時之加碼 vs 平移 |
| 量綱 | 比例 \(\phi \equiv \Delta R_{退抵}/\Delta R_{AI}\)（無因次）；不寫金額 |
| 表達工具型態（只指名，不選券） | 美股超大雲或以雲市集為主要通路之 ISV；不選券 |
| 重疊 | L14-P#2（同為承諾池，但單一供應商、守恆型）；L6-I 系（賣方側） |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Microsoft 10-K FY26（sec.py）https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm ：「Commercial remaining performance obligation increased 84% to $678 billion」；「weighted average duration of approximately 2.3 years」；「consumption commitment」0 筆、「Anthropic」僅 1 筆非相關語境。
2. Snowflake 10-Q 2Q FY27（sec.py）https://www.sec.gov/Archives/edgar/data/1640147/000164014726000037/snow-20260731.htm ：「Accrued customer liabilities related to Snowflake Marketplace (1) 162,196 122,893」（千美元，2026-07-31 vs 2026-01-31）；註「estimated portion of contractual customer commitments expected to be utilized towards the purchases of third-party products and services on the Snowflake Marketplace」。
3. Datadog 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1561550/000162828026054458/ddog-20260630.htm ：「An increasing number of sales through cloud provider marketplaces could reduce … our profit margins」；「the pricing of subscriptions from customers in our cloud-provider marketplaces」。CRWD 10-Q https://www.sec.gov/Archives/edgar/data/1535527/000153552726000031/crwd-20260731.htm ：僅「cloud marketplace partners」通路敘述。
4. Anthropic 夥伴頁 https://claude.com/ja/partners/microsoft-foundry ：「Claude models in Microsoft Foundry are eligible for Microsoft Azure Consumption Commitment (MACC)」。
5. Redress Compliance（顧問，非具名分析師）https://redresscompliance.com/aws-edp-marketplace-isv-commitment-offset.html ：「up to 25% of your annual EDP commitment can be retired through AWS Marketplace transactions」；2025-05 起限 AWS 部署之 SaaS。頁無日期。
6. 聚合者：Canalys（Jay McBain，經 partnerinsight 轉述）雲市集「86% compounded growth」；無承諾退抵歸因、無 AI 占比。CrowdStrike 新聞稿稱 AWS 市集累計逾 10 億美元（搜尋結果，未讀）。

缺段（§7-2）：未取 AWS／Google 之 Bedrock／Vertex 第三方模型是否計入承諾之官方原文；未取任何超大雲對承諾退抵占比之揭露；未取具名賣方就雲 AI 營收「增量 vs 再分配」之原文。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 承諾本身於續約時加碼；退抵只是時間差，承諾規模已反映新增 AI 預算 | MSFT 商業 RPO +84%（10-K） | φ 之「替代」部分在承諾簽署時已是增量 |
| R2 | 第三方模型在超大雲之營收認列為淨額或分成，對雲端 AI 營收貢獻小 | 待測一（MSFT／AMZN 主理人／代理人判斷） | 量級不足 |
| R3 | 退抵上限（AWS 25%）與資格限制（須 AWS 部署）使 φ 有硬上界 | Redress 頁 | 落差有上界 |
| R4 | 賣方已以「cloud marketplace 抽成與承諾退抵」分析 ISV 毛利（DDOG 自述） | DDOG 10-Q | ISV 側已定價 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) ≥ 2 家超大雲之申報或官方頁顯示第三方 AI 模型**不**計入承諾（或計入比例受上限使 φ 上界 < 10%）；或
(2) 申報層與聚合者皆無任何可把承諾退抵與增量分開之序列（SNOW 類科目僅 1 家且非 AI），致落差不可觀測（§7-2 記失敗歸因）；或
(3) 具名賣方或評等機構原文已就雲 AI 營收／RPO 拆「承諾內再分配 vs 增量」（已定價）；或
(4) 可運作對照只能寫成 L14-P#2（單一供應商預付池）、L6-I 系（賣方 backlog／計酬／融資）或 C-A1（AI 營收分列）；或
(5) 12 個月內無檢驗事件（承諾資格規則變更、超大雲首次揭露市集／第三方模型營收、ISV 揭露市集占比）；或
(6) 第三方模型於超大雲之營收以淨額認列且合計占雲 AI 營收 < 5%（`[D]`），使 φ 無論如何不影響 AI 營收讀數。

複查觸發器（若日後殺）：任一超大雲首次揭露承諾退抵或市集交易額；AWS／Google 改變第三方模型計入承諾之規則；SNOW 市集應計負債突破後續 2 季連續加速。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：RPO 與存續期、主理人／代理人判斷、市集應計負債。2. 可交易工具：超大雲或 ISV 普通股（不選）。3. 半衰期：承諾多年（MSFT 加權 2.3 年）；續約時重定價。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0084；`query/ARCH_matrix.md` L14［I］加「#3 已生成」；`AIM_FUNNEL.md` §3 一句與日期行。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L14-I／#2、L14-P#1–#3、L14-A#1–#3、L6-I／#2／#3、L6-P#3、C-A1、C-A2；不碰 L1-P；不寫 T。
