# L15-A#3 生成卡｜基礎設施軟體與資料：會計恆等（託管成本轉嫁恆等：產品毛利 ≡ 1 − 第三方雲託管成本÷產品營收；AI 推論／GPU 消耗以低毛利轉嫁進入營收，營收成長與毛利率不可同時外推）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20261007_L15-A_generate_GK.md；archive/drive/USED_20261007_L15-A_test1_GK.md；archive/work/20261014_L15-A#2_generate_CL.md | EMITS: work/20261021_L15-A#3_generate_CL.md -->
**日期：** 2026-10-21　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 5→6／6）　**格：** L15-A　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L15-P#3 本日測一，Q-0085 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-14 之 L15-A／L15-I（#2），依表序取 **L15-A**。既有 #1–#2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `hosting` `gross margin` `cloud infrastructure cost`，2 筆（SRC_DEM_004／005，OpenAI 推論支出，模型層）；與本格 B 端無關，未用。
- 比對（須異型）：
  - **L15-A#1**（`archive/drive/USED_20261007_L15-A_generate_GK.md`）：營收 ≡ 使用量 × 有效單價（死於不可並列）。本卡在**成本側**：\(GM \equiv 1 - H/R\)，只需申報之託管成本美元增量與毛利率，不拆量與價；若測一只能寫成量×價即觸發 (4)。
  - **L15-A#2**（`archive/work/20261014_L15-A#2_generate_CL.md`）：遞延收入浮存（資產負債表／現金時序）。本卡為損益表毛利恆等，不涉開票。
  - **C-A1**（ARCH_dead #6：AI COGS／席次 vs token 不可分列）：本卡不要求 AI COGS 分列；載體為**總託管成本**比與公司自述歸因句。若測一只能靠 AI COGS 分列才可讀即觸發 (2)，歸 C-A1。
  - **L5-A#3**（產品毛利混合恆等，儲存硬體／權利金）、**L3-A#3**（材料轉嫁分母）：同屬「轉嫁入分母」家族，但層與轉嫁對手方不同（本卡對手方＝超大雲，轉嫁項＝AI 推論／GPU）；測一須證明非 L3-A#3 已殺之「公司已逐季歸因」型，否則觸發 (3)。
  - **L15-P#3**（觀測份額守恆，買方預算）：本卡為賣方成本恆等，不涉買方份額。**L7-A#3**（市集總額×分潤）：不涉市集認列。
- §7-10 領域最近公開：SNOW 10-Q 2Q FY27（期 2026-07-31）；DDOG 10-Q 2Q26（期 2026-06-30）；MDB 10-Q 2Q FY27（期 2026-07-31）。下一檢查點＝DDOG 3Q26 10-Q（2026-11 上旬）、SNOW／MDB 3Q FY27 10-Q（2026-12）。

## 1. 落差一句

市場把基礎設施軟體商（資料平台、觀測、資料庫）來自 AI 工作負載之營收成長以既有產品毛利率外推；種子主張：雲託管之 ISV 產品毛利恆等 \(GM_{prod} \equiv 1 - H/R_{prod} - O/R_{prod}\)，AI 推論與 GPU 消耗以近成本轉嫁進入 \(H\)，使 AI 驅動之營收增量 \(\Delta R\) 伴隨 \(\Delta H/\Delta R > H/R\)，邊際毛利低於平均；另多年最低支出承諾（take-or-pay）使 \(H\) 對消耗放緩呈部分固定。SNOW 10-Q 2Q FY27 已見樣態：COGS 增量「primarily due to an increase of $113.6 million … in third-party cloud infrastructure expenses (including those related to AI inference and GPUs)」，產品毛利「71% … compared to 72%」，歸因「newly launched product capabilities and features that have not yet reached economies of scale」；DDOG 2Q26 COGS +45% vs 營收 +36%，「increase of $64.1 million in third-party cloud infrastructure hosting」。可拒絕之主張＝存在可並列序列顯示邊際託管比 \(\Delta H/\Delta R\) 持續高於平均且市場未扣。不主張任何主體價值方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等（A）**：\(GM_{prod} \equiv 1 - h - o\)，\(h = H/R_{prod}\)；邊際式 \(\Delta GP = \Delta R (1 - \Delta H/\Delta R) - \Delta O\) |
| 量綱 | \(h\)、\(\Delta H/\Delta R\) 無因次；\(H\)、\(R\) 美元／季；承諾為美元／合約年 |
| 選擇者 | ISV（價目：AI 功能是否加價轉嫁；雲採購折扣談判）；超大雲（承諾折扣）；客戶（AI 功能消耗） |
| 可見端 | 10-Q／10-K MD&A 之託管成本美元增量與歸因句；產品毛利率；COGS 附註；購買承諾附註（最低支出、期限） |
| 指名不可見端 | AI 推論 COGS 單列（C-A1 已殺之分列）；每單位消耗之託管單價 |
| 表達工具型態（只指名，不選券） | 美股雲託管基礎設施軟體商；不選券 |
| 重疊 | L15-A#1（量×價）；C-A1（AI COGS 分列）；L3-A#3／L5-A#3（轉嫁入分母） |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Snowflake 10-Q 2Q FY27（sec.py）https://www.sec.gov/Archives/edgar/data/1640147/000164014726000037/snow-20260731.htm ：COGS 定義「third-party cloud infrastructure expenses, including those related to AI inference and graphics processing units」；「Accrued third-party cloud infrastructure expenses 168,836 121,727」；「In June 2026, the Company amended an existing third-party cloud infrastructure agreement that provides for a total purchase commitment of $ 6.0 billion over a five-year contract term ending March 2031」；「required to pay the difference if it fails to meet the minimum spend」。
2. Datadog 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1561550/000162828026054458/ddog-20260630.htm ：「Cost of revenue $ 240,113 $ 165,978 … 45 %」；「Gross margin 79 % 80 %」；「increase of $64.1 million in third-party cloud infrastructure hosting and software costs」。
3. MongoDB 10-Q 2Q FY27 https://www.sec.gov/Archives/edgar/data/1441816/000162828026059830/mdb-20260731.htm （Atlas 託管成本與毛利，測一取）；ESTC、CFLT 同類（測一取 ≥ 1 家）。

缺段（§7-2）：未取 ≥ 6 季 \(\Delta H/\Delta R\) 序列；未取具名賣方就 AI 毛利稀釋之原文；未查各公司價目是否對 AI 功能另計（轉嫁是否保毛利）。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 公司已逐季自揭並指引產品毛利（SNOW 歸因新功能未達規模、雲採購折扣抵銷） | SNOW 10-Q | 已定價（L3-A#3 型） |
| R2 | 毛利變動 ≤ 1pp，量級不足 | 測一 `[D]` | 不影響讀數 |
| R3 | 雲承諾擴大帶來更高折扣，\(h\) 隨規模下降 | SNOW「higher discounts for our purchases」 | 方向相反 |
| R4 | AI 功能另行計價，轉嫁保毛利 | 價目頁 | 恆等不綁定 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) ≥ 2 家 ≥ 6 季之 `[D]` \(\Delta H/\Delta R\)（或 COGS 增量 ÷ 營收增量）不持續高於 \(H/R\)，或產品毛利率變動 < 1pp 且無方向；或
(2) 託管成本與 AI 推論之關聯只能經 AI COGS 分列才可讀（歸 C-A1），申報層歸因句僅 1 家 1 期；或
(3) 公司指引或具名賣方／評等機構原文已就 AI 推論對毛利之稀釋量化（含公司逐季歸因已成慣例，L3-A#3 型）；或
(4) 可運作對照只能寫成 L15-A#1（量×價）、L5-A#3／L3-A#3（他層轉嫁）、L7-A#3（市集總額）；或
(5) 12 個月內無檢驗事件（3Q 起各季 10-Q 毛利與託管成本句、承諾修訂）；或
(6) `[D]` 邊際毛利缺口 \((\Delta H/\Delta R - H/R) \times \Delta R\) 占該公司營業費用或營業利益 < 5%，使恆等不影響總讀數。

複查觸發器（若日後殺）：任一 ISV 首次以美元分列 AI 推論／GPU 成本或 AI 功能毛利；SNOW／DDOG 產品毛利連續 2 季下降 ≥ 1pp 且公司歸因於 AI 消耗；購買承諾附註首次揭露未達最低支出之差額付款。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：產品營收、COGS、產品毛利率、購買承諾。2. 可交易工具：雲託管基礎設施軟體商普通股（不選）。3. 半衰期：季報毛利；承諾期 5 年。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0086；`query/ARCH_matrix.md` L15［A］加「#3 已生成」；`AIM_FUNNEL.md` §3 一句與日期行。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L15-A#1／#2、L15-P#1–#3、L15-I／#2、C-A1、L3-A#3、L5-A#3、L7-A#3；不碰 L1-P；不寫 T。
