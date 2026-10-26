# L6-A#4 生成卡｜雲端與基礎設施服務：會計恆等（資本支出之現金流分類：`I ≡ capex_cash ＋ ΔAP_PPE ＋ ROU_FL ＋ OEM_debt`；供應商融資與融資租賃之還款列籌資，永不入投資現金流）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260927_L6-A_generate_GK.md；archive/work/20261011_L6-A#2_generate_CL.md；archive/work/20261018_L6-A#3_generate_CL.md；archive/work/20261016_L12-A#3_generate_CL.md | EMITS: work/20261026_L6-A#4_generate_CL.md -->
**日期：** 2026-10-26　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 4／6）　**格：** L6-A　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L6-P#4 本日測一，Q-0107 done）。各格最後測試日最舊＝**L6-A**（#3 測一 2026-10-18）；非已殺、非刻意排除。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py accrued capex finance lease payable`，回 11 筆（硬體價格、模型評分、Anthropic 營收），**相關 0 筆**；未使用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L6-A#1**（GK；RPO／已簽未交付÷已交付營收領先比）：營收時序。本卡為**投資現金流之分類**，不涉營收。
  - **L6-A#2**（電費轉嫁 θ，總額法）：營收組成。不同型。
  - **L6-A#3**（CIP 折舊管線；折舊**起點**）：損益之折舊時點。本卡不涉折舊，涉**同一筆投資之現金流出列於哪一節（投資 vs 籌資）與何時**。
  - **C-A3**（ARCH_dead #5，折舊年限）：不涉。
  - **L13-A**（未開始租約／RVG／JV：表外義務）：本卡只計**已入表**之資產（已取得之設備與已開始之融資租賃）；營運租賃 ROU（如 CoreWeave 1H26 8,359M 資料中心租約）明文排除於 `I` 外，以免與 L13-A 重疊。
  - **L13-A#2**（客戶預付入 OCF）：OCF 端；本卡為投資／籌資端。**L5-A#4**（Sandisk 合資表外 capex）：表外；本卡表內。**L4-A#2**（整機商 CCC 營運資本）：營運面 ΔWC；本卡為**資本支出應付款**（非營運資本科目）。**L6-I#3**（DDTL 融資可貸性讓價）：誘因、單價；本卡不涉單價。**L12-A#3**（OBBBA 現金稅時序）：稅；不涉。
  - 重疊列為否決 (5)。
- §7-10 領域最近公開：Alphabet 10-Q 期 2026-06-30（2026-07-23）；CoreWeave 10-Q 期 2026-06-30（2026-08-12）；Oracle FQ1 FY27 10-Q 期 2026-08-31（2026-09-11）。下一檢查點＝Alphabet／Microsoft／Amazon 3Q26（2026-10 下旬）；CoreWeave 3Q26 10-Q（約 2026-11）；Oracle FQ2 FY27（約 2026-12）。

## 1. 落差一句

ASC 230 之分類恆等：當期取得之資本資產 `I_t ≡ capex_cash,t ＋ ΔAP_PPE,t（已取得未付，日後付款仍入投資節）＋ ROU_FL,t（融資租賃，本金還款入籌資節）＋ OEM_debt,t（供應商／OEM 融資轉債，還款入籌資節）`。報告之 FCF ＝ OCF − capex_cash 只扣第一項；第二項為**時序**（回轉時壓 FCF），第三、四項為**永久繞道**（投資永不經投資節）。無量綱 `γ ≡ (I − capex_cash) ÷ capex_cash`，可再拆 `γ_時序` 與 `γ_繞道`。`[D]` 本輪初算（皆 `[V]` 一手申報、`[D]` 自算）：
- Alphabet 1H26：計入應計負債及應付帳款之 PP&E 餘額 15,090M → 29,113M（Δ 14,023M）÷ 現金 capex 80,598M → `γ_時序` ≈ 17.4%（1H25：10,326→10,635M，≈ 0.8%）；融資租賃 ROU 902M（≈ 1.1%）。
- Oracle FQ1 FY27：未付 capex 5,279M → 6,247M（Δ 968M）＋融資租賃 ROU 1,539M ÷ 現金 capex 28,499M → `γ` ≈ 8.8%；另籌資節有「short-term financing related to capital expenditures, net」（−830M；前年同季 +1,958M），其與 capex 行之毛／淨關係待測一。
- CoreWeave 1H26：非現金「Liabilities related to property and equipment additions, including OEM financed additions」9,796M vs 現金 capex 14,117M（毛 `γ` ≈ 69%，含日後經投資節付款者）；其中轉為債務之 OEM 融資 1,469M（`γ_繞道` 下界 ≈ 10.4%）；OEM 融資未償 3.8B → 4.8B。
種子主張：若市場與賣方以「現金 capex」作為投資步調、以 OCF − capex_cash 作 FCF 比較主體，則 (a) `γ_時序` 上升之主體 FCF 暫時被墊高、日後回轉；(b) `γ_繞道` 高之主體（OEM 融資、融資租賃）FCF 結構性高估，償債只見於籌資節。本卡不定方向與量級是否足以定價。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等（ASC 230 現金流分類：賣方融資／融資租賃本金列籌資；未付款列非現金揭露）；非守恆、非誘因 |
| 選擇者 | 無（恆等）；`γ` 由付款條件、OEM 融資與融資租賃之採用決定 |
| 可見端 | 現金流量表「Purchases of property and equipment／Capital expenditures」；補充揭露非現金投資（Alphabet「Property and equipment included in accrued liabilities and accounts payable」；Oracle「Unpaid capital expenditures」；CoreWeave 上列兩行）；租賃附註之融資租賃 ROU；債務附註之 OEM Financing Arrangements 餘額；XBRL `CapitalExpendituresIncurredButNotYetPaid`、`RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability`（MSFT、ORCL、CRWV、AMZN、GOOGL 皆有標） |
| 指名不可見端 | 主體間口徑不一（Alphabet／Oracle 為期末餘額，CoreWeave 為期間流量）；CoreWeave 9,796M 中後續經投資節付款 vs 轉債之拆分僅部分揭露；Microsoft 10-Q 是否揭應付設備款流量（L6-A#3 記其 10-K 應付設備款 26.7B，本輪未實讀 10-Q） |
| 對照式（生成用） | `FCF_adj ≡ OCF − capex_cash − ΔAP_PPE − 融資租賃本金 − OEM 還款`；可拒絕：若 `γ` 於 ≥ 4 季平穩（`ΔAP_PPE` 無趨勢、繞道項 < capex 數 %），則報告 FCF 與調整後 FCF 之差無判別力 |
| 表達工具型態（只指名，不選券） | 美股可交易之雲端／AI 基礎設施服務商（Alphabet、Oracle、CoreWeave；次為 Microsoft、Amazon）。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Alphabet 10-Q 期 2026-06-30（現金流量表、非現金投資補充揭露、應計費用附註「Accrued purchases of property and equipment 8,877→16,196」）。https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm
2. CoreWeave 10-Q 期 2026-06-30（非現金投資及籌資活動、債務附註 OEM and Software License Financing Arrangements、OEM 短期債加權利率 9%、MD&A 資金來源句）。https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm
3. Oracle FQ1 FY27 10-Q（現金流量表「Unpaid capital expenditures」、籌資節「short-term financing related to capital expenditures, net」、MD&A 非 GAAP FCF 定義）。https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm
4. 測一須另取：Microsoft、Amazon 最近 10-Q／10-K 之同列（`sec.py facts` 已見 XBRL 標）；Amazon 新聞稿「free cash flow less principal repayments of finance leases and financing obligations」與 Microsoft「capital expenditures including finance leases」之原文（R1）；具名賣方或評等機構是否以 OEM 融資／應付設備款調整 CoreWeave 或 Oracle FCF；≥ 4 季 `γ` 序列；OEM 融資之到期分布。
5. 二手（未實讀）：Seeking Alpha「CoreWeave: Strong Backlog Isn't Enough To Offset Leverage Risks」https://seekingalpha.com/article/4857938-coreweave-strong-backlog-isnt-enough-to-offset-leverage-risks

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 超大規模業者已自行公布含融資租賃之 capex 與扣融資租賃本金之 FCF，繞道項已被分開定價 | Amazon 季報新聞稿 FCF 三定義；Microsoft 新聞稿／法說「including finance leases」（待原文） | 繞道項無落差 |
| R2 | 應付設備款為正常付款條件，季間回轉，`γ_時序` 無持續性 | Alphabet 1H25 ≈ 0.8% vs 1H26 ≈ 17.4% 之變動需 ≥ 4 季檢驗 | 時序項為雜訊 |
| R3 | CoreWeave 以 EBITDA／backlog／債務總額定價，FCF 本已為負，分類不改判讀 | 債務附註 OEM 餘額已單列（#2） | 不可分離於槓桿論述（L6-I#3／L13） |
| R4 | 量級：繞道項（融資租賃＋OEM 轉債）占 capex 僅數 % | Alphabet ROU_FL ≈ 1.1%；Oracle ≈ 5.4% | 量級不足 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) `capex_cash`、`ΔAP_PPE`、融資租賃 ROU 與 OEM 轉債於 ≥ 3 家 L6 主體 ≥ 4 季不可並列，或口徑（餘額 vs 流量）無法統一，使 `γ` 區間無判別力。
(2) 業者原文或具名賣方已以含融資租賃／應付設備款／OEM 融資之 capex 或 FCF 報告或比較主體（R1 成立，含 CoreWeave 與 Oracle）。
(3) `γ_繞道` ＜ capex 5% 且 `γ_時序` 於 ≥ 4 季無單向趨勢（R2＋R4 成立，量級不足）。
(4) 管理層原文已就應付設備款回轉或 OEM 還款之時點給量化指引，使恆等式無資訊增量。
(5) 可運作對照只能寫成未開始／營運租約（L13-A）、客戶預付入 OCF（L13-A#2）、表外合資 capex（L5-A#4）、折舊起點（L6-A#3）、融資讓價（L6-I#3）或營運資本 CCC（L4-A#2）。
(6) Oracle 籌資節之「capex 相關短期融資」經原文確認為 capex 行已含之毛額（無繞道），且 CoreWeave 為唯一具繞道項之主體，使表達只剩單一主體。

複查觸發器（若日後殺）：任一 L6 主體首次於 10-K／10-Q 以美元分列「供應商／OEM 融資取得之設備」流量並給還款表；或 `γ_時序` 連續 2 季 ＞ 15% 之主體出現 ≥ 3 家。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Purchases of PP&E、非現金投資補充揭露、融資租賃 ROU 與本金還款、OEM 融資債務、非 GAAP FCF 定義。
2. 可交易工具：Alphabet、Oracle、CoreWeave 等美股與選擇權（不選券）。
3. 半衰期：應付設備款回轉約 1–2 季；OEM 融資到期（CoreWeave 短期為主）約 1 年內；`[V]` 不寫。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L6［A］標「#4 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 5 筆（CoreWeave／Alphabet／Oracle 申報數字）。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L6-A#1–#3、L6-P#1–#4、L6-I#1–#3、L13-A／#2、L5-A#4、L4-A#2、L12-A#3、C-A3／C-A4 結論。
