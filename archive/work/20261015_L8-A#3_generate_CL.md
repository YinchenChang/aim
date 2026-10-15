# L8-A#3 生成卡｜標註／驗證：會計恆等（客戶預付之轉付成本——現金與營運現金流內含之代收代付）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260918_L8-A_generate_GK.md；archive/drive/USED_20260918_L8-A_test1_GK.md；archive/work/20261007_L8-A#2_generate_CL.md；work/20261007_L8-A#2_test1_CL.md | EMITS: work/20261015_L8-A#3_generate_CL.md -->
**日期：** 2026-10-15　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 2／6）　**格：** L8-A　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L2-I#3 本日測一）。非「已殺／刻意排除」格中最後測一最舊者＝2026-10-07 批之 L8-A#2、L8-I#2、L9-A#2（L2-I#2 已於 L2-I#3 輪處理）；依 QUEUE 序次（Q-0004 先於 Q-0005、Q-0006）取 **L8-A**；既有生成 2 份 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `annotation labeling Innodata`，命中 0 筆。
- 比對（本卡須異型）：
  - **L8-A#1**（`archive/drive/USED_20260918_L8-A_generate_GK.md`；測一 `archive/drive/USED_20260918_L8-A_test1_GK.md`）：支出 ÷ 有效條數之分母上界；死於分母不可得。本卡不用產出單位。
  - **L8-A#2**（`work/20261007_L8-A#2_test1_CL.md`）：未開票收入（營收先於帳單、先於現金）；死於不可依服務線分離且與 AI 段無同向。本卡方向相反：**現金先於成本結算**，且問題在代收代付是否入營收（主理人／代理人），不在認列時點。
  - L8-P（分鐘／條）、C-I2（專家單價）、L8-I／#2（誘因、客戶量轉移）：不涉。
  - 他層同族：L4-A#2（整機商 OCF＝NI−ΔWC）、L10-A#2（商戶預收浮存）、L2-A#3（電力轉嫁總額認列）——本卡主體與科目異（標註供應商之客戶預付轉付成本），重疊不構成丟棄。
- §7-10 領域最近公開：INOD 10-Q 2Q26（2026-08-06 申報）與 8-K ex99.1（2026-08-06）。下一檢查點＝INOD 3Q26 10-Q（約 2026-11 上旬）。

## 1. 落差一句

標註／AI 資料供應商替集中之 AI 實驗室買方承辦專案，買方先付款、供應商代付第三方成本：恆等式 現金 ＝ 自有現金 ＋ 客戶預付 −（已付轉付成本），營運現金流 ＝ NI ＋ 非現金 ＋ Δ預付 ＋ Δ未付專案成本 ＋ …。INOD 1H26 營運現金流 164.4（NI 29.3），其中 Δ預付 65.2、Δ應付與應計 71.9（US$百萬）；公司稱該預付為「pass-through」，並自行揭露扣除後現金約 134。種子主張：讀者若把預付讀成「pre-funded backlog」將轉為營收（次級彙編已如此讀），或把營運現金流／現金當獲利能力，讀到的部分是**代收代付**；反之若轉付成本以主理人入營收，營收成長含低毛利轉付。**方向未定**：轉付之會計歸屬（營收總額、淨額或不入損益）尚未讀到。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：現金與營運現金流之代收代付分解；營收 ＝ 自有服務 ＋（主理人時之）轉付 |
| 已讀事實 | INOD 10-Q 2Q26：「Advances from Customers – Represent cash received from customers in advance of the delivery of goods or services or the incurrence of project-related costs」；「advances from customers for unfulfilled obligations were $ 67.0 million and $ 1.8 million」（2026-06-30／2025-12-31）；「$ 61.8 million of such project costs that had been incurred but remained unpaid and is included in accounts payable and accrued expenses」；「The cash is not required to be segregated.」收入政策：「The Company may also enter into arrangements to resell third-party goods or services … evaluates whether it acts as a principal or an agent」。Q2 營收 92,142、直接營運成本 49,682（千）；Q1 營收 90.1M。最大客戶占 Q2 營收 37%（Q1 56%）、第二客戶 34%（Q1 17%）；兩客戶占應收 66%。1Q26 10-Q 無「Advances from customers」定義句（`--grep` 0 筆）＝新科目。8-K ex99.1：「Cash as of June 30, 2026 includes customer prepayments related to pass-through costs; net of these prepayments, cash was approximately $134 million」。 |
| 未證之連結 | 已發生未付之專案成本 61.8 > 同季直接營運成本 49.7，故不可能全數已入損益；其資產端去向（預付、其他流動資產 6.7→22.8、或與預付互抵）與營收歸屬未讀。此即測一第一關。 |
| 量綱 | 客戶預付 ÷ 季營收（無因次）；（Δ預付＋Δ未付專案成本）÷ 營運現金流（無因次）；轉付入營收額 ÷ 營收（%） |
| 選擇變數 | 買方：預付或由自身直接採購；供應商：主理人／代理人判斷、是否分列轉付 |
| 半衰期 | 每季重報；轉付結清即解消（1–4 季） |

## 3. B 端可觀測載體（只指名）

1. INOD 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/903651/000110465926092021/inod-20260630x10q.htm （預付定義、未付專案成本、收入政策、客戶集中、現金流量表）
2. INOD 10-Q 1Q26 https://www.sec.gov/Archives/edgar/data/903651/000110465926057270/inod-20260331x10q.htm （前期對照；新科目確認）
3. INOD 8-K ex99.1 Q2 2026 https://www.sec.gov/Archives/edgar/data/0000903651/000110465926092010/tm2621499d1_ex99-1.htm （扣除預付之現金口徑）
4. 電話會彙編（Nasdaq／MarketBeat 2026-08-06）https://www.nasdaq.com/articles/innodata-q2-earnings-call-highlights ——CFO 稱預付為「pass-through items」；「a program with a large AI lab」。
5. 次級讀法（反向讀者）：Panabee 2026-08-06 https://www.panabee.com/news/innodata-earnings-q2-2026-report ——「this pre-funded backlog provides critical visibility」「the rate at which the $67 million in customer advances is recognized as revenue」。
6. 同型主體（待測一指名讀）：TaskUs 10-Q（客戶預付／合約負債科目是否出現同型）；INOD 10-K FY2026（年度主理人／代理人判斷附註）。

缺段（§7-2）：轉付之損益歸屬、轉付性質（第三方算力、外包人力或其他）、預付之客戶別；本輪只讀上列；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 公司已於季稿頭條段自行扣除預付報現金（約 134），CFO 稱 pass-through | 載體 3、4 | 已定價 |
| R2 | 預付 67.0 與未付成本 61.8 近乎相抵，現金淨效果小，且於 1–2 季內結清 | 載體 1 | 量級小、半衰期短 |
| R3 | 營收季增僅約 2%（90.1→92.1），轉付若入營收，Q2 營收應有跳升；跡象指向不入營收或淨額 | 載體 1、2 | 營收端無落差 |
| R4 | 單一中小型主體之營運資本事件，非層級機制 `[A]` | — | 終端條件，本輪不篩（§7-3），僅列 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後轉付之會計歸屬（入營收總額／淨額／不入損益）與資產端去向仍不可由 INOD 10-Q／10-K／8-K／電話會原文判定；或
(2) 可運作對照只能寫成 L8-A#2（未開票時點）、L4-A#2（OCF＝NI−ΔWC 一般式）、L10-A#2（商戶浮存）或 L2-A#3（轉嫁總額認列）而無標註層特有之買方預付結構；或
(3) 公司或具名賣方已以扣除轉付之口徑同時報現金、營運現金流與營收（R1 擴及三者），市場引用之（已定價）；或
(4) `[D]` 量級：轉付入營收額 < 營收 5%，且（Δ預付＋Δ未付專案成本）於下一期 10-Q 已結清至 < 營運現金流 10%；或
(5) 12 個月內無可觀測驅動：3Q26／FY2026 申報不再出現該科目，且無同層第二主體出現同型預付。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：客戶預付、應付與應計之專案成本、營運現金流、營收（主理人／代理人）。2. 可交易工具：標註／AI 資料服務商（不選）。3. 半衰期：轉付結清週期。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L8［A］格加「#3 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0047。不改 L8-A#1／#2、L8-I／#2、L8-P、C-I2、L4-A#2、L10-A#2、L2-A#3 結論。
