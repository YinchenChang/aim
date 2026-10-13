# L14-P#2 生成卡｜企業終端需求：守恆（企業預付容量承諾池：AI 消耗與非 AI 消耗共用同一份已承諾容量——承諾期內 AI_draw + nonAI_draw + 未用 = 已購容量，AI 消耗之增量於承諾耗盡前為池內替代，非新增企業支出）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/FILEIDS.tsv；archive/drive/USED_20261005_L14-P_generate_GK.md；archive/drive/USED_20261005_L14-P_test1_GK.md | EMITS: work/20261013_L14-P#2_generate_CL.md -->
**日期：** 2026-10-13　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 4→5／6）　**格：** L14-P　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L13-I#2 測一 2026-10-13，Q-0037 done）。非已殺／刻意排除且無 #2 之格＝L14-P／A／I、L15-P／A／I；`archive/FILEIDS.tsv` 測一時間最舊者＝L14-P（2026-10-05T13:39Z；L14-A 13:59Z、L14-I 14:19Z、L15-P 14:38Z、L15-A／I 10-07）→ **L14-P**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `capacity commitment`、`committed spend`、`rollover`、`Snowflake`，0 筆；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L14-P#1**（測一不通過，`archive/drive/USED_20261005_L14-P_test1_GK.md`）：席次 ≤ 員工數、工時存量；死因＝否決 (1)：同一 10-K 付費席次水準與期末員工數不可並列。本卡不涉席次、員工數、工時；守恆量是**買方已預付之容量承諾（美元或 credit）**，以賣方 RPO、遞延收入、容量合約條款為可見端。
  - **L14-A**（IT 支出 ÷ 總營收）、**L14-I**（採購績效 vs 人力節省去向）：本卡不以買方 IT 支出比重或預算回流誘因為樞紐。
  - **C-A2**（已殺，ARCH_dead #9，企業預算單位經濟）：本卡不重開單位經濟，不主張每單位毛利。
  - **L15-A**（使用量 vs 有效單價）、**L6-P#2**（RPO 之電力-時間預算 ρ）、**L6-I#2**（bookings 計酬）、**C-A1**（席次 vs token 不可分列）：本卡不以單價、MW、計酬或 AI COGS 分列為樞紐；RPO 只作承諾池存量之可見端。
  - **L11-P／L8-P／L9-P**（已殺）：不涉。
- §7-10 領域最近公開：Snowflake 10-Q 期末 2026-07-31（2026-09-04）；Microsoft 10-K 期末 2026-06-30（2026-07-29）；Datadog 10-Q 期末 2026-06-30（2026-08-06）。下一檢查點＝Snowflake 3Q FY27 10-Q（2026-12 初）。

## 1. 落差一句

市場把消費型平台上的「AI 驅動消耗成長」讀成企業端新增 AI 支出；種子主張企業以多年期**預付容量合約**購入可通用於任何服務（含 AI 功能）之容量，承諾期內 AI 消耗與非 AI 消耗共用同一池——在池耗盡或續約加購之前，AI 消耗之增量是池內替代與提前燒耗，企業總承諾不因此增加；只有在「耗盡→加購／提前續約」或「超額按需計費」時，AI 消耗才轉為新增支出。錯價只在把池內燒耗之加速讀成承諾池之擴張。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆**：對單一容量合約 \(K\)（已購容量）：\(\sum_t (D^{AI}_t + D^{other}_t) + U_T = K\)，\(U_T\)＝期末未用（可滾存，通常須加購）。彙總：RPO\(_t\) ≈ RPO\(_{t-1}\) + 新簽/加購 − 認列消耗。AI 消耗之加速若未伴隨新簽/加購之加速，則為燒耗時序前移 |
| 選擇者 | 企業買方（工作負載在池內之配置；何時加購／提前續約）；賣方（滾存條款、提前續約誘因） |
| 可見端 | 賣方 10-Q：RPO 存量與 12 個月認列比例、容量合約加權剩餘年限、容量合約占營收比、「roll over unused capacity … upon the purchase of additional capacity」條款原文、產品營收；>1M 客戶數；管理層對 AI 功能消耗之敘述 |
| 指名不可見端 | AI 功能消耗占產品營收（申報層未分列）；池內燒耗 vs 超額按需之分拆；加購中歸因於 AI 之部分 |
| 表達工具型態（只指名，不選券） | 美股可交易、以預付容量合約為主要營收、且宣稱 AI 功能帶動消耗之消費型平台。不選券 |

`[D]` 可重算對照（申報數，非測一結論）：Snowflake 2Q FY27 RPO 約 9.0B、54% 預期 12 個月內認列、容量合約加權剩餘年限 2.4 年、容量合約占營收約 97%（三個月）。**不主張 AI 消耗為替代或新增之方向、不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Snowflake 10-Q 2Q FY27 https://www.sec.gov/Archives/edgar/data/1640147/000164014726000037/snow-20260731.htm ：「Customers choose to consume our platform under either capacity arrangements, in which they commit to a certain amount of consumption at specified prices」；「our customer contracts permit customers to roll over any unused capacity to a subsequent order, generally upon the purchase of additional capacity」；「Consumption for most customers accelerates from the beginning of their usage to the end of their contract terms and often exceeds their initial capacity」；RPO 約 9.0B／54%／2.4 年；容量合約約 97% 營收；AI 產品（Cortex AI、CoWork、Cortex Code）於風險因子列名，未分列營收。
2. Microsoft 10-K FY26 https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm ：Commercial RPO 678B、加權存續約 2.3 年、約 30% 於 12 個月內認列；申報層「consumption commitment」0 筆（企業承諾池與 AI 實驗室大單未分列）。
3. Datadog 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1561550/000162828026054458/ddog-20260630.htm ：「AI-native cohort … contributed high single digit percentage points to the total Company year-over-year revenue growth」——可觀測端以客群而非承諾池分列（對照用）。
4. MongoDB 10-Q 2Q FY27 https://www.sec.gov/Archives/edgar/data/1441816/000162828026059830/mdb-20260731.htm ：候選第二同型主體（Atlas 承諾／按需分列待查；未實讀）。
5. 市場讀法錨（未實讀）：Futurum「Snowflake Q4 FY 2026 Results Highlight AI-Led Consumption」https://futurumgroup.com/insights/snowflake-q4-fy-2026-results-highlight-ai-led-consumption-and-platform-expansion/

缺段（§7-2）：AI 消耗占比未見申報行；新簽／加購與 RPO 變動之分拆未查；第二同型主體之滾存條款未讀。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | 公司明文「consumption … often exceeds their initial capacity」並須加購；燒耗加速即帶動提前續約，池內替代只是時序 | Snowflake 10-Q（§3-1） | 替代與新增之差只在時序，量級可能不足 |
| R2 | RPO 與 12 個月認列比、容量合約剩餘年限每季揭露，市場可自行比對消耗 vs 承諾 | Snowflake 10-Q（§3-1） | 落差可能已定價 |
| R3 | 承諾池以美元計價，AI 功能若單價高於傳統工作負載，同池燒耗更快即實質提高 ARPU | — | 守恆在美元層成立、在工作負載層不構成約束 |
| R4 | Datadog 以「AI-native cohort」分列成長，顯示市場讀法已區分新增客群 vs 既有客戶池內消耗 | Datadog 10-Q（§3-3） | 讀法可能非種子所稱 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法就同一主體取得 ≥ 4 期 RPO、12 個月認列比、容量合約剩餘年限與產品營收之同口徑序列，或無法於 ≥ 2 家同型主體取得「容量可通用於 AI 功能」與滾存／加購條款原文；或
(2) 可運作對照只能寫成席次 ≤ 員工數（L14-P#1）、IT 支出比重（L14-A）、預算回流（L14-I）、單位經濟（C-A2）、有效單價（L15-A）、ρ／MW（L6-P#2）或 AI COGS 分列（C-A1）；或
(3) 具名賣方或公司原文已就「AI 消耗為池內替代 vs 新增承諾」分列量化（已定價）；或
(4) `[D]` AI 功能消耗占產品營收 < 5%，或 RPO 變動中加購／新簽已與消耗同步加速（池內替代之量級不足）；或
(5) 12 個月內無可觀測驅動：無 RPO／認列比之揭露變更、無 AI 消耗之申報分列、無容量合約條款修訂。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：RPO、遞延收入、產品營收；AI 消耗無單一行。2. 可交易工具：消費型平台股權（不選）。3. 半衰期：容量合約加權剩餘年限約 2.4 年；池內替代於續約時解消。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L14［P］格加「#2 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列。不改 L14-P#1、L14-A、L14-I、C-A2、L15-A、L6-P#2 結論。
