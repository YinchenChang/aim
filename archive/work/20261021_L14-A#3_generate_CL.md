# L14-A#3 生成卡｜企業終端需求：會計恆等（AI 歸因重組費用之 GAAP／調整後橋接：GAAP 營業費用 ≡ 調整後營業費用 ＋ 排除項 X；重組準備滾存 R_t ≡ R_{t−1} ＋ 提列 − 現金支付 ± 調整——當「一次性」AI 重組逐年再現，X 之長期均值實為經常性人力成本，調整後毛利率之「AI 節省」部分為排除項之時序與口徑）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261005_L14-A_generate_GK.md；archive/drive/USED_20261005_L14-A_test1_GK.md；archive/work/20261013_L14-A#2_generate_CL.md；work/20261013_L14-A#2_test1_CL.md；archive/work/20261014_L14-I#2_generate_CL.md；work/20261014_L14-I#2_test1_CL.md；archive/work/20261020_L14-P#3_generate_CL.md | EMITS: work/20261021_L14-A#3_generate_CL.md -->
**日期：** 2026-10-21　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 0→1／6）　**格：** L14-A　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L14-P#3 測一 2026-10-20，Q-0080 done）。非已殺／刻意排除格中最後測試日最舊＝L14-A（#2 測一 2026-10-13；L14-I#2、L15-P／A／I#2 皆 2026-10-14）→ **L14-A**。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `restructuring severance non-GAAP`，0 筆；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L14-A#1**（`archive/drive/USED_20261005_L14-A_test1_GK.md`）：IT 支出 ÷ 總營收比重；死因＝同一申報無法並列 IT 支出、營收與 AI 行。本卡不需 IT 支出總額；樞紐是**損益表重組行／調整後橋接表／重組準備滾存表**，三者為 ASC 420 與 Reg G 下之例行揭露。
  - **L14-A#2**（`work/20261013_L14-A#2_test1_CL.md`）：費用化／資本化分流；死因＝資本化軟體分列僅 1 家、量級 < 10%。本卡不涉資本化；分流是 GAAP vs 調整後（排除項），非資產負債表。
  - **L14-I#2**（`work/20261014_L14-I#2_test1_CL.md`）：裁員**理由文字**之 AI 歸因分岔（誘因）。本卡不判讀理由真偽，只用金額與再現頻率；AI 歸因僅作樣本納入條件（附註原文寫明 AI）。
  - **L14-P#1／#2／#3**（席次 ≤ 員工數、承諾池、客服人工處理量）：不涉。
  - **C-A2**（ARCH_dead #9，企業 AI 預算單位經濟）：不主張每單位毛利或 ROI。
  - **L13-I#3**（Oracle 融資工具選擇，評等觸發線）：同主體、不同機制；本卡不涉融資。
- §7-10 領域最近公開：Accenture 10-K FY26（2026-10-16 申報）；Oracle 10-Q FQ1 FY27（2026-09-11）；Salesforce 10-Q FQ2 FY27（2026-08-27）；SEC Non-GAAP C&DI 100.01（2022-12-13 修訂）。下一檢查點＝Oracle 10-Q FQ2 FY27（約 2026-12）、Salesforce 10-Q FQ3 FY27（約 2026-12）、Accenture 10-Q FQ1 FY27（約 2027-01）。

## 1. 落差一句

市場以調整後營業利益率（排除重組／「business optimization」）讀企業 AI 導入之人力節省；種子主張：當 AI 歸因重組逐年再現，恆等式 GAAP OpEx ≡ Adj OpEx ＋ X 使調整後毛利率之改善有一部分是 X 被移出之結果——節省出現在調整後線，取得節省之成本（遣散）只出現在 GAAP 線與準備滾存表；若 X 之多年均值 ÷ 營收為正且穩定，調整後毛利率對 GAAP 有持續性高估，「一次性」之標籤不成立。可拒絕之主張＝樣本主體之排除項於最近 4 個會計年度中 ≥ 3 年非零，且賣方／評等機構未以多年均值回加；若排除項確為單次、或市場已回加（R1），本卡死。本卡不主張任何主體利潤或股價方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等（A）**：(i) \(OpEx^{GAAP}_t \equiv OpEx^{Adj}_t + X_t\)；(ii) \(R_t \equiv R_{t-1} + X^{sev}_t - Pay_t \pm Adj_t\)；(iii) 長期：\(\overline{m}^{GAAP} = \overline{m}^{Adj} - \overline{X}/Rev\)，\(\overline{X}=\frac1N\sum X_t\)。(iv) 回收：\(\text{Payback} = \sum Pay \div S^{ann}\)，\(S^{ann}\)＝公司揭露之年化節省（若有） |
| 選擇者 | 發行人管理層（是否排除、計畫邊界與「完成」宣告、計畫追加） |
| 可見端 | 損益表「Restructuring」／「Business optimization costs」行；重組附註之滾存表（期初、提列、調整、現金支付、期末、累計、預期總額）；8-K／10-K 之 non-GAAP 橋接表；計畫追加之 8-K 或附註原文 |
| 指名不可見端 | 被遣散職能中 AI 可替代之比例；年化節省 \(S^{ann}\)（多數不揭露）；重組後之回補招聘 |
| 量綱 | 美元／期；X ÷ 營收、X ÷ OpEx（無因次）；年數 N |
| 外部參照物（測一查證） | 2000s 起之「recurring special items」研究與 SEC C&DI 100.01 執法前例（排除「normal, recurring, cash operating expenses」之意見函） |
| 表達工具型態（只指名，不選券） | 美股、重組附註寫明 AI 之大型企業普通股；不選券 |
| 重疊 | L14-I#2（同一事件之理由層）；重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Accenture 10-K FY26（sec.py）https://www.sec.gov/Archives/edgar/data/0001467373/000146737326000049/acn-20260831.htm ：損益表「Business optimization costs 307,541 615,324 438,440」（千美元，FY26／25／24）；「We recorded a total of $ 923 million under the program, including $ 628 million of employee severance」；「Costs recorded in connection with business optimization actions initiated in fiscal 2023 and completed in fiscal 2024 totaled $ 1.5 billion, primarily for employee severance」；「Adjusted operating margin for fiscal 2026 was 15.8% compared to … 15.6%」，GAAP 「Operating margin of 15.4%, compared to 14.7%」。`[D]` X ÷ 營收：FY24 0.68%、FY25 0.88%、FY26 0.41%（三年連續非零）。
2. Oracle 10-Q FQ1 FY27（sec.py）https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm ：「plans to restructure … including through the adoption and integration of artificial intelligence technologies across certain functions」；「up to $ 2.1 billion as of August 31, 2026. Subsequent to August 31, 2026, our management supplemented the 2026 Restructuring Plan by approximately $ 700 million」；滾存表「Total 2026 Restructuring Plan $ 567 $ 161 $ 6 $ ( 324 ) $ — $ 410 $ 1,971 $ 2,103」；損益表「Restructuring and other 94 415」（百萬，三個月）。
3. Salesforce 10-Q FQ2 FY27（sec.py）https://www.sec.gov/Archives/edgar/data/1108524/000110852426000190/crm-20260731.htm ：損益表「Restructuring 94 4 174 40」（百萬，三／六個月）；MD&A「We expect to continue to experience improvements in our operating expenses as a percentage of revenue, which could include various restructuring initiatives」。AI 歸因原文待測一查（本卡未見附註寫 AI）。
4. 反方錨：Griffin & McInnis（2025，*Journal of Accounting & Economics*，DOI 10.1016/j.jacceco.2025.101799；摘要經 https://academicnewsletter.sufe.edu.cn/info/411876 ）：「in general, investors ignore firms' exclusion of recurring expenses」——惟樣本為 SBC 與併購攤銷，非重組。
5. 監理錨：SEC Non-GAAP C&DI 100.01（經 Barnes & Thornburg 2023-07-20 轉錄 https://securitiesandcapmarkets.btlaw.com/post/102kzht/sec-staff-continues-to-put-pressure-on-non-gaap-adjustments-that-it-views-as-norm ）：「Presenting a non-GAAP performance measure that excludes normal, recurring, cash operating expenses」可能誤導。

缺段（§7-2）：未取任何主體 ≥ 4 年之排除項序列（Accenture 僅 3 年於同一 10-K）；未找到賣方以調整後利益率讀「AI 節省」之具名原文；未查評等機構對重組之調整口徑；年化節省 \(S^{ann}\) 之揭露未查。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 投資人本已無視排除項，以含排除項之盈餘定價 | Griffin & McInnis 2025（§3-4） | 已定價；惟樣本非重組，須測一確認可外推 |
| R2 | SEC C&DI 100.01 已約束經常性排除，發行人自我節制 | §3-5 | 排除項自然收斂，落差無驅動 |
| R3 | 量級小：Accenture X ÷ 營收 < 1% | §3-1 `[D]` | 毛利率偏差不足以重定價 |
| R4 | Accenture 之 GAAP 利益率改善（+0.7pt）大於調整後（+0.2pt）——排除項下降反使 GAAP 改善更多 | §3-1 | 方向在計畫結束年反轉，非持續高估 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後 < 2 家附註原文將重組歸因 AI 之主體，能於 10-K／10-Q／8-K 取得 ≥ 4 個會計年度之排除項金額、重組準備滾存（提列／現金支付／期末）與 non-GAAP 橋接表之同口徑並列；或
(2) 樣本主體之排除項於最近 4 個會計年度中非零 < 3 年（確為單次）；或 `[D]` \(\overline{X}\) ÷ 營收 < 0.5%（量級不足）；或
(3) 具名賣方、評等機構或公司原文已以多年均值回加重組（或以 GAAP 口徑為共識基準），或 R1 之研究結論已有涵蓋重組之具名原文（已定價）；或
(4) 可運作對照只能寫成 IT 支出 ÷ 營收（L14-A#1）、費用化／資本化（L14-A#2）、裁員理由文字（L14-I#2）、席次／承諾池／人工處理量（L14-P#1–#3）或單位經濟（C-A2）；或
(5) 12 個月內無檢驗事件（計畫追加或完成宣告、FY27 10-K、SEC 意見函公開）；或
(6) 無任何樣本主體揭露年化節省或可重算之節省代理，使 (iv) 回收式不可 `[D]`，且 (i)–(iii) 單獨不足以區分「AI 節省」與「排除項時序」。

複查觸發器（若日後殺）：任一 AI 歸因重組計畫連續第 3 次追加；SEC 公開對 AI 重組排除項之意見函；評等機構發布重組回加口徑變更。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：損益表重組行、重組附註滾存表、non-GAAP 橋接表。2. 可交易工具：附註寫明 AI 之重組主體普通股（不選）。3. 半衰期：計畫期（季至 2 年）與追加頻率；10-Q 每季。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0081；`query/ARCH_matrix.md` L14［A］加「#3 已生成」；`AIM_FUNNEL.md` §3 一句與日期行。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L14-A#1／#2、L14-I／#2、L14-P#1–#3、C-A2、L13-I#3 結論；不恢復 L11-P／L8-P／L9-P；不寫 T。
