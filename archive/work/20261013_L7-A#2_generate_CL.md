# L7-A#2 生成卡｜模型層：會計恆等（實驗室持股之計量制度：上市主體淨利 ≡ 營業利益＋持股比 × 實驗室估值變動；實驗室上市即由「可觀測交易時重估」轉「每季按市價」）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/FILEIDS.tsv；archive/drive/USED_20260930_L7-A_generate_GK.md；archive/drive/USED_20260930_L7-A_test1_GK.md；work/20261013_L7-I#2_test1_CL.md；work/20261013_L7-P#2_test1_CL.md | EMITS: work/20261013_L7-A#2_generate_CL.md -->
**日期：** 2026-10-13　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 2→3／6）　**格：** L7-A　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L7-I#2 測一 2026-10-13，Q-0027 done）。非已殺／刻意排除之格中最後測試日最舊者：`archive/FILEIDS.tsv` archive_work 時戳 L7-A 測一 2026-09-30T09:30:52Z，早於 L10-P 09:47Z、L10-A 10-01 → **L7-A**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py Anthropic OpenAI valuation equity stake`，命中 30 筆，皆為 API 價目、harness token 倍數、OpenAI 支出口徑——屬 L7-A#1（列表價 − FLOP 成本）之載體，**與本卡無關**；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L7-A#1**（測一不通過，`archive/drive/USED_20260930_L7-A_test1_GK.md`）：token 毛利＝列表價 − FLOP × 每 FLOP 成本；死因＝每百萬 token FLOP 與每 FLOP 成本不可並列。本卡不論 token、不論 FLOP、不論價目；恆等式兩側皆為申報行（營業利益、其他收益、持股帳面值）。
  - **C-A5**（死 #13）：API 已實現單價不可分離／L7 未上市。本卡不需 API 單價；其複查觸發器「任一前沿 API 商 IPO」恰為本卡之制度轉換點，但本卡不恢復 C-A5（不主張單價可重算）。
  - **C-P3**（死 #16）：權重更新支出非科目。無關。
  - **C-I1**（死 #10）：估值可歸因權重能力。本卡**不**主張實驗室估值由能力決定；估值只作持股比 × ΔV 之輸入，方向不主張。
  - **L7-I#2**（測一部分通過）：實驗室估值作研究者外部選擇權。本卡用同一估值，但傳導為投資人持股之損益計量，不是人才報酬。
  - **L13-A#2**（客戶預付入 OCF）、**L13-A**（租賃義務）、**L6-A#2**（電力轉嫁）：資本／雲端層之現金與義務恆等。本卡為模型層主體之**權益**經由投資人計量制度進入上市主體損益；雲端承諾（RPO）只作反方 R3 之相關通道，不作主恆等式。
- §7-10 領域最近公開：Amazon 2Q26 10-Q（2026-07-31）、Alphabet 2Q26 10-Q（2026-07-23）、Microsoft FY26 10-K（2026-07-29）；Anthropic S-1 仍秘密遞交（Yahoo Finance 2026-10-04）。下一檢查點＝Anthropic 公開 S-1（報導指 10 月下旬）、Amazon／Alphabet 3Q26 10-Q。

## 1. 落差一句

市場把 Amazon／Alphabet 之實驗室持股收益當成一次性非營業雜項（剔除於「核心」盈餘），並把對模型層之曝險只經雲端承諾通道估值；種子主張：會計恆等 \(NI = OI + s \cdot \Delta V_{\text{lab}} - \text{tax}\) 下，實驗室上市後持股由「僅於可觀測交易時重估」轉為「每季按市價入損益」，使上市主體 GAAP 盈餘與遞延稅負成為實驗室股價之槓桿函數，且與同一實驗室之雲端承諾履約能力同向——錯價只在把兩通道分開估值、或把制度轉換當成會計雜訊。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等／計量制度轉換**：\(NI_t = OI_t + s\cdot\Delta V_t \cdot \mathbb{1}[\text{observable}] - T_t\)（上市前，ASC 321 measurement alternative）→ \(NI_t = OI_t + s\cdot\Delta P_t - T_t\)（上市後，readily determinable fair value） |
| 選擇者 | 實驗室是否於窗內上市；上市後持股是否改採權益法（重大影響）而非公允價值；禁售期與限制股折價；持股比 \(s\) 之稀釋 |
| 可見端 | 10-Q「Other income (expense), net」分列「upward adjustments … equity investments in private companies」；持股帳面值；所得稅之離散稅負；MD&A 指名發行人；非 GAAP 是否剔除 |
| 指名不可見端 | 精確持股比 \(s\)；Alphabet 未具名之「a private company」身分；上市後之計量分類 |
| 表達工具型態（只指名，不選券） | 美股可交易、持有未上市前沿實驗室重大股權且於 10-Q 分列重估損益之大型平台。不選券 |

恆等式（生成用，非正式載入）：持股收益占稅前淨利 \(\phi = s\Delta V/(OI + s\Delta V)\)。種子只主張 \(\phi\) 之**波動來源**在上市時改變；**不主張實驗室估值方向，不把重估收益當成錯價證據，不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Amazon 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm ：「Operating income 19,171 27,461」「Other income (expense), net 1,117 53,415」「Income before income taxes 20,857 80,857」（2Q25／2Q26，百萬美元）；「upward adjustments relating to equity investments in private companies of $ 50.5 billion in Q2 2026 … primarily from our nonvoting preferred stock in Anthropic」；「$ 15.9 billion of net discrete tax expense primarily attributable to the upward adjustments to our investments in Anthropic」；「our equity investments in private companies, which primarily relate to our equity investments in Anthropic and OpenAI」；AWS–Anthropic 承諾擴大「more than $ 100.0 billion over 10.0 years」。
2. Alphabet 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm ：「Income from operations 31,271 40,770」「Other income (expense), net 2,662 97,983」「Gain (loss) on equity securities, net 1,286 99,031」；「primarily related to unrealized gains in our equity securities portfolio from SpaceX and a private company」（未具名）；measurement alternative 帳面「$ 124.3 billion, of which $ 87.9 billion was remeasured」。
3. Microsoft FY26 10-K https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm ：「$6.5 billion of net gains and $4.8 billion of net losses for fiscal years 2026 and 2025, respectively, from investments in OpenAI, primarily … equity method」「dilution gain from the OpenAI Recapitalization」；非 GAAP「exclude net gains and losses from investments in OpenAI」——對照：權益法＋公司自行剔除。
4. Yahoo Finance（Park，2026-10-04）https://finance.yahoo.com/markets/stocks/articles/anthropic-public-1-still-missing-210349323.html ：「EDGAR database remains silent regarding Anthropic」；報導指 11 月上市。Bloomberg（Ludlow，2026-06-26）https://news.bgov.com/artificial-intelligence/openai-weighs-ipo-in-2027-after-expected-anthropic-public-debut ：OpenAI「as soon as in 2027」。

缺段（§7-2）：≥ 4 季 Amazon／Alphabet 重估收益序列；Amazon／Alphabet 非 GAAP 或賣方模型是否剔除；持股比；上市後計量分類（公允價值 vs 權益法）之公司原文；禁售條款。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | 公司已自行剔除投資損益於非 GAAP，市場不以其定價 | Microsoft FY26 10-K（§3-3） | 已分離＝已定價（§7-4） |
| R2 | 上市後可能改採權益法（重大影響），不按市價入損益 | ASC 323 條件；Microsoft 對 OpenAI 即採權益法（§3-3） | 制度轉換不發生 |
| R3 | 雲端承諾與持股同向為已知集中風險，已於風險因子揭露 | Amazon 10-Q「variable interest … maximum exposure to loss」（§3-1） | 相關性已揭露 |
| R4 | 收益為非現金、稅後亦部分遞延，對自由現金流與回購無影響 | Amazon 10-Q 離散稅負句（§3-1） | 對估值之淨效應小 |
| R5 | 禁售期／限制股使上市後首 6–12 個月按折價計量 | Alphabet 10-Q SpaceX「subject to long-term restrictions」（§3-2） | 制度轉換延後、窗內效應小 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法就 ≥ 2 家上市主體取得 ≥ 4 季「實驗室持股重估收益」申報行序列，或發行人未具名致不可歸屬於模型層主體；或
(2) 可運作對照只能寫成 API 單價（滑回 C-A5）、估值歸因權重能力（滑回 C-I1）、或客戶預付／RPO 之現金恆等（滑回 L13-A#2／L6）；或
(3) Amazon 與 Alphabet 之公司指引或具名賣方原文已把實驗室持股收益自盈餘剔除並單獨估值（同 Microsoft 型，已定價）；或
(4) 公司原文或會計政策表明實驗室上市後持股改採權益法，或 12 個月內無前沿實驗室上市；或
(5) 持股帳面值占上市主體股東權益 < 5%，或 ≥ 4 季重估收益占稅前淨利 < 10%（量級不足，非機制否證）。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：重估收益能否按發行人歸屬（Amazon 具名、Alphabet 未具名）。2. 可交易工具：平台美股可交易，但該通道是否已被非 GAAP／賣方剔除。3. 半衰期：實驗室上市日與禁售期決定制度轉換何時生效。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L7［A］格加「#2 已生成」；`AIM_FUNNEL.md` §3 一句；`query/QUEUE.md` 新列 Q-0028。不寫：ARCH_live／INDEX／ARCH_dead。不改 L7-A#1、L7-I#2、L7-P#2、C-A5／C-I1／C-P3、L13-A／L13-A#2、L6-A#2。
