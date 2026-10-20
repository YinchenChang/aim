# L13-I#3 生成卡｜資本與融資結構：誘因（評等觸發線附近之發行人，依「機構調整後槓桿」最小化而非經濟成本選融資工具：每募一元，選機構債務含量最低者——普通股／ATM、強制可轉特別股、客戶預付、表外——故觸發線距離決定工具組合）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20261002_L13-I_generate_GK.md；archive/drive/USED_20261002_L13-I_test1_GK.md；archive/work/20261013_L13-I#2_generate_CL.md；work/20261013_L13-I#2_test1_CL.md；work/20261020_L13-A#3_test1_CL.md；work/20261020_L13-P#3_test1_CL.md | EMITS: work/20261020_L13-I#3_generate_CL.md -->
**日期：** 2026-10-20　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 4→5／6）　**格：** L13-I　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L13-P#3 本日測一，Q-0078 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-13（L13-I、L14-P、L14-A）；依表序取 **L13-I**。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `Blue Owl data center joint venture`，15 筆皆硬體／PUE／模型列，相關命中 0；未用。
- 棄用種子（記錄，不生成）：資產管理人費基誘因（Blue Owl FPAUM 以承諾／成本計費，hyperscaler JV 之殘值由 RVG 回轉承租方）。OWL 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1823945/000182394526000040/owl-20260630.htm ：「Digital infrastructure 35,260」（千美元／季）對 Real Assets 管理費 112,865、總 FRE 392,180；暴露過小，且 RVG 面與 L13-A#1 重疊。
- 比對之舊檔與死因型態，本卡須異型：
  - **L13-I#1**（`archive/drive/USED_20261002_L13-I_generate_GK.md`）：供應商兼股東／債權人之私有資訊使**公開信評資訊含量下降**；死因＝同一客戶應收帳齡與股權餘額不可並列。本卡不論評等之資訊含量，評等只作**發行人之約束線**；可見端為發行人自身申報之融資組合與機構公開觸發線。
  - **L13-I#2**（`work/20261013_L13-I#2_test1_CL.md`）：擔保人「付終止費／承接租約」二擇一；死因＝F 遮蔽。本卡選擇者為發行人財務長，選項為公開工具，無遮蔽條款。
  - **L13-A#1**（表外義務上界）、**L13-A#2**（客戶預付入 OCF）、**L13-A#3**（EPS 分母時滯，Oracle）、**L13-P#3**（現金按季封閉，Alphabet／Meta；死因＝表外與有價證券吸收）：本卡不估義務、不論 OCF 組成、不論 EPS、不用守恆；上述各項只作「工具清單」之成員，被排序的是**機構債務含量**。
  - **C-A4／C-A3**（ARCH_dead #4–5）、**T-15**：不涉；不重開。
- §7-10 領域最近公開：Oracle FQ1 FY27 10-Q（2026-09-11）；S&P 對 Oracle 降至 BBB-（2026-07，Reuters 轉述）；Alphabet 10-Q 2Q26（2026-07-23）。下一檢查點＝Oracle FQ2 FY27 10-Q（約 2026-12）、三家機構對 Oracle 之下次評等行動。

## 1. 落差一句

市場把 Oracle FQ1 FY27 之 ATM 19.9 bn 加償債 4.2 bn（優先票據 128.1→125.0 bn）讀成「現金不足之被動籌資」。種子主張：當機構調整後槓桿距下調觸發線（S&P「sustains leverage exceeding 4.5 times」、Fitch「above 3.5, or above 4 if rents were included」）不足一個量級內之緩衝時，發行人之最適反應是**依機構債務含量排序工具**，而非依稅後資金成本；故新融資中優先債占比應接近 0、股本與零債務含量工具（客戶預付、合作方出資之場址）占比上升，且此組合由觸發線距離可事前推出。可拒絕之主張＝在調整後槓桿 > 4x 期間，Oracle 下一季（FQ2 FY27）淨新增融資中優先債占比 ≤ 少量，而距觸發線遠之發行人（Alphabet：S&P 觸發線 1x、預期 ≤ 0.5x）之工具選擇不受此約束。本卡不主張評等方向、不主張股價。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因（I）**：發行人 max 評等存續 s.t. 募資 ≥ 缺口；目標函數之代理＝機構調整後債務 ÷ EBITDA ≤ 觸發線。選項 k ∈ {優先債、普通股／ATM、強制可轉特別股、客戶預付、表外場址} 之機構債務含量 c_k ∈ [0,1]；距離 d＝觸發線 − 現值；d 小 → 選 c_k 最低者，即使資金成本較高 |
| 選擇者 | 發行人財務長（受董事會與評等承諾約束） |
| 可見端 | 10-Q 融資段（股本、特別股、優先債發行／償還、短期資本支出融資）、資產負債表借款；機構新聞稿／轉述之觸發線；424B／8-K 工具條款 |
| 指名不可見端 | 機構對各工具之實際債務含量 c_k（多在付費報告）；客戶預付與合作方出資是否被機構調入債務 |
| 量綱 | 倍（槓桿）、無因次比例（優先債 ÷ 淨新增融資）、美元／季 |
| 外部參照物（測一查證） | 降評邊緣發行人以股本與混合資本守住投資級之前例（如 2010 年代公用事業、電信以強制可轉守評等之案例） |
| 表達工具型態（只指名，不選券） | 美股雲供給者普通股、強制可轉特別股、投資級邊緣公司債；不選券 |
| 重疊 | L13-I#1（評等，但不同角色）、L13-A#2（預付）、L13-A#3（Oracle 股數）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Oracle 10-Q FQ1 FY27（sec.py）https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm ：「net proceeds from the issuance of common stock via the ATM Program of $19.9 billion」「Repayments of senior notes, term loan credit agreements and other borrowings ( 4,202 )」「(Repayments of) proceeds from short-term financing related to capital expenditures, net ( 830 ) 1,958」；「$ 125.0 billion and $ 128.1 billion of senior notes and other long-term borrowings」（2026-08-31／05-31）；「$11.4 billion of customer prepayments with a significant financing component」；Series D 強制可轉 4,954。
2. Reuters（Vidya Ranganathan，2026-08-04；The Star 轉載）https://www.thestar.com.my/tech/tech-news/2026/08/05/analysis-oracle-corp-goes-for-high-stakes-ratings-gamble-in-ai-strategy ：S&P BBB-（7 月）、Andrew Chang「We could downgrade Oracle if Oracle sustains leverage exceeding 4.5 times」；Moody's Baa2 負向；Fitch BBB、「above 3.5, or above 4 if rents were included」；債務 129.5 bn、約 4.3x。
3. Outlook Business（2026-06-11，引 Reuters）https://www.outlookbusiness.com/corporate/oracle-forecasts-95-bn-in-capex-for-fy27-plans-to-raise-40-bn-in-debt-and-equity ：FY27 capex「up to $95 billion」、「$40 billion financing plan includes a previously announced $20 billion at-the-market equity issuance」；餘額未分債／股。
4. 對照（遠離觸發線）：iTiger／Deep News（2026-02-27）https://www.itiger.com/news/1145150869 ：S&P Javed Hussain，Alphabet AA+「unless its debt-to-EBITDA ratio reaches 1」、三家「0.5x」以下；S&P 債務計算含「future data center lease obligations」。Alphabet 10-Q 2Q26 普通股 30.50＋強制可轉 19.06＋債 56.23 bn（`work/20261020_L13-P#3_test1_CL.md` A1）。
5. 機構對 Alphabet 股本之評語（線索，未實讀正文）：Moody's https://ratings.moodys.com/ratings-news/466727 （標題「$84 Billion equity raise」；WebFetch 只得 metadata）；Investing.com 轉述「Moody's calls Alphabet's $84.75 billion equity raise positive」https://www.investing.com/news/stock-market-news/moodys-calls-alphabets-8475-billion-equity-raise-positive-93CH-4727515 。

缺段（§7-2）：各機構對強制可轉、客戶預付、合作方出資之債務含量 c_k；Oracle 機構調整後槓桿之逐季序列；FY27 剩餘 20 bn 之工具組合。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 「analysts expect Oracle to raise equity capital and cut share buybacks」——組合已被預期 | #2 Reuters | 已定價 |
| R2 | 公司自 2026-06 已公告 40 bn 計畫含 20 bn ATM；組合由公司揭露非由觸發線推出 | #3 | 揭露先於推論 |
| R3 | Alphabet 遠離觸發線仍發 49.6 bn 股本——股本選擇另有原因，觸發線非主因 | #4 | 競爭假說 |
| R4 | 機構債務含量 c_k 不公開，觸發線距離無法於事前算出 | — | 不可觀測 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 觸發線距離 d 無法由公開數 `[D]` 算到 ±0.5x 內（機構調整後債務定義或 Oracle 之 EBITDA 口徑不可重算），或 ≥ 2 家機構之數值觸發線無具名出處。
(2) 公司或具名賣方已量化 FY27 剩餘融資之債／股組合且與本卡可拒絕主張一致——已定價。
(3) 強制可轉、客戶預付或合作方出資之機構債務含量，於公開資料中與優先債無差（c_k ≈ 1）——排序不存在。
(4) 距觸發線遠之對照組（Alphabet、Meta）與近觸發線之 Oracle 工具組合無差（皆以股本為主）——觸發線不具解釋力（R3）。
(5) 可運作對照只能寫成評等資訊含量（L13-I#1）、預付入 OCF（L13-A#2）、EPS 分母（L13-A#3）或現金封閉（L13-P#3）。
(6) 重定價窗（≥ 12 個月）內無檢驗事件（FQ2／FQ3 FY27 10-Q、機構行動），或 Oracle 已跌出投資級／獲升評致約束消失。

複查觸發器（若日後殺）：任一家機構公開強制可轉或客戶預付之債務含量；Oracle 被降至投資級以下或展望轉穩定；Oracle 公告 FY27 剩餘融資之工具組合；另一家距觸發線 ≤ 0.5x 之 AI 基建發行人出現。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：融資段各列、借款餘額、客戶預付、特別股；EBITDA 口徑。
2. 可交易工具：普通股、強制可轉特別股、投資級邊緣公司債。不選券。
3. 半衰期：季度 10-Q；機構行動不定期。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0079；`query/ARCH_matrix.md` L13［I］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L13-I#1／#2、L13-P#1–#3、L13-A#1–#3、C-A3／C-A4 結論；不寫 T-15。
