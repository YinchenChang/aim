# L12-A#3 生成卡｜監理與法制：會計恆等（稅法時序：OBBBA 研發即時費用化追溯補扣＋100% 紅利折舊 → 現金稅 ≡ 帳面稅 − Δ遞延）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260922_L12-A_generate_GK.md；archive/drive/USED_20260922_L12-A_test1_GK.md；archive/work/20261008_L12-A#2_generate_CL.md；work/20261008_L12-A#2_test1_CL.md；archive/work/20261015_L12-P#3_generate_CL.md | EMITS: work/20261016_L12-A#3_generate_CL.md -->
**日期：** 2026-10-16　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1／6）　**格：** L12-A　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。非「已殺／刻意排除」格中最後測一最舊＝2026-10-08（L12-A#2、L12-I#2、L3-A#2、L1-A#2；L12-P 已於 10-15 測 #3）；同日依測一先後（QUEUE Q-0009 最早）取 L12-A。既有生成 2 份 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `cash tax`／`bonus depreciation`／`R&D expensing`，命中 0 筆；未使用。
- 比對（本卡須異型）：
  - **L12-A#1**（`archive/drive/USED_20260922_L12-A_generate_GK.md`；測一 `archive/drive/USED_20260922_L12-A_test1_GK.md`）：TIC 集團法定／自願**營收權重**；死於申報層無兩欄。本卡不用營收拆分，載體為**所得稅附註與現金流量表補充欄**。
  - **L12-A#2**（`work/20261008_L12-A#2_test1_CL.md`）：著作權或有負債 N×s vs ASC 450；不進 T 因量級（一次性、對 OCF 1–25%）與 N 不可重算。本卡為**法定稅制之時序恆等**（ASC 740），非訴訟負債；量數由申報直接給出（現金稅、當期／遞延稅），不需重算件數。
  - L12-P#3（出口管制質量平衡）、L12-I#2（IP 補償賣權）：非稅。
  - 同為「現金≠損益」之鄰型：L13-A#2（客戶預付入 OCF）、L15-A#2（遞延收入浮存）、L4-A#2（營運資本 CCC）、L8-A#3（轉付）——皆為**營運科目**時序；本卡時序源頭為**立法**（可由法律變動開關），非商業條款。C-A3／C-A4（帳面折舊年限）：本卡為**稅務**折舊，與帳面年限無關。
  - ARCH_dead 無稅制型死因。
- §7-10 領域最近公開：OBBBA 2025-07-04 簽署；IRS Rev. Proc. 2025-28（2025-08）；META 10-Q 2Q26（2026-07-30）；AMZN 10-Q 2Q26（2026-07-31）；GOOGL 10-K FY25（2026-02-05）；Yahoo Finance 2026-02-10。下一檢查點＝各家 3Q26 10-Q（2026-10 下旬至 11 月）；FY26 10-K（2027-01／02）之當期／遞延聯邦稅分列。

## 1. 落差一句

稅法造出之會計恆等：**現金稅 ≈ 當期稅 ＝ 帳面稅 − Δ淨遞延稅負債**。OBBBA 同時給大型 AI 資本支出者兩種扣除：(a) §174A 境內研發即時費用化，且 2022–2024 未攤銷餘額可於 2025 一次或 2025–2026 兩年補扣（**一次性、會回轉之時序項**）；(b) 2025-01-19 後取得之資產 100% 紅利折舊永久化（**只要資本支出成長即不回轉之時序項**）。兩者合流使 FY25 當期聯邦稅驟降（AMZN 9,039→1,220、META 9,569→2,820 百萬美元，遞延聯邦 +11,134／+18,379），自由現金流中有一段**由立法時序而非營運產生**。種子主張：市場以 2025–2026 FCF 外推時，未把 (a) 之一次性補扣與 (b) 之依賴資本支出成長之遞延分開。**方向未定**：Morgan Stanley 2025-07 已公開估 >70B 之 FCF 增量、Amazon 自述「不改變應納總額」（可能已定價）；META 遞延項另混入 15.93B 評價備抵之非現金一次項。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等（ASC 740）：現金稅 ＝ 帳面稅 − Δ遞延稅負債 ＋ Δ應付稅；規則端＝國會（OBBBA／未來稅法）、IRS（Rev. Proc. 2025-28） |
| 恆等（僅定義） | ΔFCF_稅 ＝ t ×〔(稅務折舊 − 帳面折舊) ＋ (研發即時扣除 − 帳面研發攤銷差) ＋ 補扣餘額 × 當年比例〕；補扣項於 2027 起歸零 |
| 已讀事實 | sec.py facts（XBRL）：AMZN 現金稅 FY24 12,308 → FY25 8,295；1H26 3,978 vs 1H25 5,638；當期聯邦 9,039 → 1,220；遞延聯邦 −4,101 → +11,134。META 現金稅 FY24 10,554 → FY25 7,578；1H26 1,999 vs 1H25 5,544；當期聯邦 9,569 → 2,820；遞延聯邦 −4,709 → +18,379；1H26 帳面稅 −2,113（含 8.03B 利益「partially offsets the $15.93 billion discrete charge recognized in the third quarter of 2025 upon enactment of the One Big Beautiful Bill Act」，10-Q 2Q26）；1H26 遞延稅 +1,568 vs −2,163。GOOGL 現金稅 FY23 19,164／FY24 27,353／FY25 21,526。Eide Bailly：大型納稅人補扣三擇一（2025 全額／2025–2026 均攤／續五年攤銷）；境外研發仍 15 年攤銷。 |
| 未證之連結 | 各家選哪一補扣方案（申報層未見）；補扣額 vs 紅利折舊額之分離；季度當期／遞延分列（10-Q 只給合計） |
| 量綱 | 立法時序現金稅節省（美元／年）÷ 營業現金流或 FCF（%）；一次性補扣占比（%） |
| 半衰期 | 補扣：至 FY26 結束；紅利折舊：隨資本支出成長率；立法：不定期 |

## 3. B 端可觀測載體（只指名）

1. META 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm （現金稅補充欄、遞延稅調節、OBBBA 段）；10-K FY25（2026-01-29，未讀全文，經 XBRL 取數）。
2. AMZN 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm （TTM 現金稅）；10-K FY25（2026-02-06，經 XBRL 取數）。
3. GOOGL 10-K FY25（acc 0001652044-26-000018，經 XBRL 取數）；MSFT 10-K FY26（acc 0001193125-26-323660，現金稅 21,188，未讀全文）。
4. Yahoo Finance 2026-02-10 https://finance.yahoo.com/news/amazon-meta-and-alphabet-report-plunging-tax-bills-thanks-to-ai-investment-and-new-rules-in-washington-161229652.html （三家當期稅、Amazon 聲明、Susan Li「substantial cash tax savings」、ITEP）。
5. Sherwood 2025-07-22 https://sherwood.news/markets/morgan-stanley-touts-a-usd70-billion-boost-free-cash-flow-megacap-tech-companies-tax-changes/ （Morgan Stanley >70B FCF 增量；未分一次性 vs 時序）。
6. Eide Bailly https://www.eidebailly.com/insights/alerts/2025/section-174-expenses （§174A 與補扣規則）。
7. 未讀：Morgan Stanley 原報告；ORCL／CRWV 等高資本支出者之稅附註；各家財報電話會稅務指引原文；JCT／CBO 對 §168(k)／§174A 之年度分布估計；WSJ Heard on the Street（連結不可用）。

缺段（§7-2）：補扣方案選擇與補扣額之個別揭露；本輪未讀；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | Morgan Stanley 2025-07 已公開量化 >70B FCF 增量，市場知情 | 載體 5 | 已定價 |
| R2 | Amazon：遞延稅終將繳納、「doesn't change the amount of tax we pay」——公司自述為時序 | 載體 4 | 已揭露 |
| R3 | 紅利折舊永久化：資本支出持續成長則 DTL 不回轉，FCF 增量非一次性 | 載體 6、法條 | 方向 |
| R4 | 對市值十年期之衝擊僅為現金時序之折現差，量級可能同 L12-A#2 之低個位數 | L12-A#2 測一 | 量級 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) ≥ 2 家高資本支出上市主體（如 AMZN、META、GOOGL、MSFT、ORCL）之 10-K／10-Q 無法提供 ≥ 4 期同口徑之現金稅與當期／遞延稅（至少年度）序列，恆等不可閉合；或
(2) 研發補扣（一次性）與紅利折舊（持續）於申報層及公司說明中皆不可分離，只得合計遞延（C-A1／C-I3′ 型可分離性死因）；或
(3) `[D]` 量級：可得最佳估計之一次性補扣現金效果 < 該主體 FY25 營業現金流 5%，或其折現至十年期權益價值 < 2%；或
(4) 公司指引或具名賣方已分列一次性 vs 持續之現金稅效果並據以調整 FCF（已定價）；或
(5) 12 個月內無可觀測驅動：無主體揭露 FY26 現金稅回升、資本支出指引不降（DTL 不回轉）、無稅法變更；或
(6) 現金稅下降主要由非 OBBBA 項（評價備抵、移轉訂價和解、境外稅、股份酬勞超額利益）解釋。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：現金稅補充欄、當期／遞延聯邦稅、DTL 調節、評價備抵。2. 可交易工具：高資本支出大型股（不選）。3. 半衰期：補扣至 FY26；紅利折舊隨資本支出週期；10-K 年度分列。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L12［A］格加「#3 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0052。不改 L12-A#1／#2、L12-P#1–#3、L12-I、L13-A#2、L15-A#2、L4-A#2、C-A3、C-A4 結論。
