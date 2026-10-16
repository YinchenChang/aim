# L1-A#3 生成卡｜能源與電力：會計恆等（受管電業 AFUDC 權益：淨利 ≡ 現金盈餘 ＋ 資本化權益報酬 → 擴建期 EPS 成長含非現金項）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260926_L1-A_generate_GK.md；archive/drive/USED_20260926_L1-A_test1_GK.md；archive/work/20261008_L1-A#2_generate_CL.md；archive/work/20261008_L1-A#2_test1_CL.md；archive/work/20261009_L1-I#2_generate_CL.md | EMITS: work/20261016_L1-A#3_generate_CL.md -->
**日期：** 2026-10-16　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain，配額 4／6）　**格：** L1-A　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L3-A#3 已於本日測一）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-08（L1-A#2；L1-P＝刻意排除 T-11 不取）。既有生成 2 份 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `AFUDC`／`utility`／`rate base`，命中 0 筆。
- 比對（本卡須異型）：
  - **L1-A#1**（GK）：PPA 鎖定價 − 現貨＝存量；死於鎖定價與現貨無法同主體分離。本卡不談電價，談**受管電業損益之資本化收益**。
  - **L1-A#2**：Bloom 產品／服務營收認列時差；死於服務段毛利已轉正。本卡主體為受管電業、恆等為 AFUDC，不涉營收認列。
  - **L1-I#2**：大負載擔保只及新約、成本落於其他費率類別（誘因型）。本卡不涉費率分攤，談同一電業損益表內之非現金收益。
  - ARCH_dead：C-A3（折舊年限樞紐）為折舊假設；C-I3′／N-02「利益未分列」——本卡之 AFUDC 權益**已分列**（XBRL `PublicUtilitiesAllowanceForFundsUsedDuringConstructionCapitalizedCostOfEquity`），型態不同。
- §7-10 領域最近公開：Xcel 1Q26 8-K 業績稿（2026-04）；Dominion／Southern／AEP FY25 10-K（2026-02）；各家 3Q26 財報預計 2026-10 下旬至 11 月初（下一檢查點）。

## 1. 落差一句

受管電業淨利 ≡ 現金盈餘 ＋ AFUDC 權益（在建工程以核定 ROE 計提、計入其他收入、待投產後經折舊回收之非現金收益）。資料中心負載擴建使在建工程（CWIP）驟增，AFUDC 權益機械上升：XBRL 年值 Dominion 41→50→109→152（百萬美元，FY22–FY25；約占 FY25 淨利 5%）、Southern 268→235→340（FY23–FY25；約占 FY25 淨利 8%）、AEP 175→211→245（FY23–FY25）；Xcel 1Q26 EPS 由 0.84 增至 0.89，其中「Higher AFUDC equity & debt 0.10」大於全部 EPS 增量。種子主張：市場以「6–8%（或更高）EPS 成長」讀電業資料中心紅利，未區分其中**資本化權益報酬（非現金、依賴日後費率認可與如期投產）**與已入費率基之現金盈餘。**方向未定**（AFUDC 亦可視為已鎖定之未來費率基）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：NI ＝ NI_cash ＋ AFUDC_eq；AFUDC_eq ≈ CWIP（非入費率基部分）× 權益比 × 核定 ROE（期間比例）；投產時 AFUDC 併入費率基、轉為折舊＋授權報酬之現金回收 |
| 已讀事實 | XBRL `PublicUtilitiesAllowanceForFundsUsedDuringConstructionCapitalizedCostOfEquity`（sec.py facts）：D、SO、AEP 年值如 §1；`NetIncomeLoss` D FY25 2,998、SO FY25 4,341（百萬美元）。Xcel 1Q26 業績稿：「Higher AFUDC equity & debt 0.10」；「AFUDC increased $61 million for the first quarter of 2026, largely the result of system investment.」 |
| 未證之連結 | AFUDC_eq 占淨利或 EPS 增量之比在 ≥ 4 期是否持續上升；CWIP 是否部分已入費率基（CWIP in rate base 州別差異，此時不計 AFUDC）；指引 EPS 成長率是否含 AFUDC；具名賣方是否以「現金 EPS／FFO」口徑剔除 |
| 量綱 | AFUDC_eq ÷ NI（%）；AFUDC_eq 對 EPS 年增量之貢獻（每股美元、% of ΔEPS） |
| 半衰期 | 年（投產時轉換；大型在建 2–5 年） |

## 3. B 端可觀測載體（只指名）

1. Xcel 1Q26 業績稿 8-K https://www.sec.gov/Archives/edgar/data/0000072903/000007290326000070/xcelearningsreleaseq12026.htm （EPS 變動拆解含 AFUDC 列）。
2. SEC XBRL companyconcept：Dominion（CIK 715957）、Southern、AEP 之 AFUDC 權益與淨利（經 `tools/sec.py facts`）；各家 10-K／10-Q 損益表「Allowance for equity funds used during construction」列與 CWIP 附註。
3. Xcel 2Q26 法說逐字稿 https://www.fool.com/earnings/call-transcripts/2026/07/30/xcel-energy-xel-q2-2026-earnings-call-transcript/ （EPS 指引與資本計畫；本輪未讀）。
4. NextEra 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/0000753308/000075330826000060/nee-20260630.htm 、WEC Energy 子公司 Wisconsin Electric 10-Q 1Q26 https://www.sec.gov/Archives/edgar/data/0000107815/000010781526000017/wep-20260331.htm （AFUDC 與資本計畫；本輪未讀）。
5. 各州 CWIP 入費率基規則（州公用事業委員會令文；未讀）。
6. 具名賣方或評等機構（Moody's／S&P FFO／debt 口徑）是否剔除 AFUDC（未讀）。

缺段（§7-2）：AFUDC 占 EPS 指引之比與賣方口徑之原文；本輪未讀；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | AFUDC 於損益表與 XBRL 逐期分列，電業分析慣例即看「AFUDC 占淨利」與 FFO／債務；已定價 | 載體 1、2、6 | 落差 |
| R2 | AFUDC 占淨利僅約 5–8%，即使全數剔除，EPS 成長率改變 < 1–2 個百分點 | 載體 2 | 量級 |
| R3 | AFUDC 依法定公式計提且投產後幾乎必入費率基，等同延遲現金而非品質瑕疵 | 會計準則 ASC 980（未讀原文） | 機制 |
| R4 | 受管電業波動低，重定價幅度難達准入門檻 | CHARTER §1（H1 ≥ 5 為後段，不在此執行） | 表達 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) ≥ 2 家受管電業無法取得 ≥ 4 期 AFUDC 權益與淨利（或 EPS）同口徑序列；或
(2) `[D]` 量級：各主體 AFUDC 權益占淨利 < 5%，且剔除後 EPS 年成長率變動 < 1 個百分點；或
(3) 主要擴建在建工程依州規已入費率基（CWIP in rate base），AFUDC 非擴建之主要計提方式；或
(4) 公司指引或具名賣方／評等機構已明示以剔除 AFUDC 之口徑（現金 EPS、FFO）衡量或建模（已定價）；或
(5) 歷史上 AFUDC 計提之在建工程投產後被拒入費率基之比例可忽略，且無延期／減損先例，使「非現金」與「現金」無經濟差；或
(6) AFUDC 占淨利比 ≥ 4 期未上升（擴建未經此恆等式傳導）。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：AFUDC 權益（其他收入）、CWIP、法規資產。2. 可交易工具：美股上市受管電業（不選）。3. 半衰期：年。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L1［A］格加「#3 已生成」；`AIM_FUNNEL.md` §3 句與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0055。不改 L1-A#1／#2、L1-I#1／#2、L1-P（T-11）、C-A3、C-I3′、N-02、L3-A#3 結論。
