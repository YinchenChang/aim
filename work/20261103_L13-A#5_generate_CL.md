# L13-A#5 生成卡｜資本與融資結構：會計恆等（子公司層可贖回優先權益融資：AI 資料中心子公司向外部投資人發行附固定優先報酬、可贖回之優先單位，列「可贖回非控制權益」〔暫時權益〕；其 PIK 優先股利不入利息費用、不入 EBITDA／Adjusted EBITDA，而於淨損益之下以歸屬非控制權益扣除；嵌入之贖回選擇權公允值變動入非營業損益）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；AIM_FUNNEL.md；archive/work/20261026_L13-A#4_generate_CL.md；work/20261026_L13-A#4_test1_CL.md；archive/work/20261020_L13-A#3_generate_CL.md；archive/work/20261011_L13-A#2_generate_CL.md；archive/drive/USED_20260928_L13-A_generate_GK.md；L13-P#2–#4、L13-I#2–#4、L2-A#2、L6-A#4、L2-I#4 生成卡首行 | EMITS: work/20261103_L13-A#5_generate_CL.md -->
**日期：** 2026-11-03　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 0→1／6）　**格：** L13-A　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額配置、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（Q-0147–Q-0152 皆 done）。非已殺／刻意排除格中，最後測試日最舊＝**L13-A**（#4 測一 2026-10-26；次舊為 L7-I／L10-P/A/I／L11-A 之 2026-10-27）。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py "preferred equity" noncontrolling Macquarie`，**命中 0 筆**。內部數字（§12）未取用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L13-A#1**（T 不進 L）：入表租賃負債 ≠ 義務上界（未開始租／RVG／JV）。本卡物件為**已入表之權益分類工具之成本歸屬**，非租賃、非表外義務上界。
  - **L13-A#2**（客戶預付之融資成分入 OCF）：本卡不涉客戶端現金。
  - **L13-A#3**（EPS 分母：ATM 時滯、強制可轉 if-converted）：本卡不以股數為落差；子公司優先股利經「歸屬普通股東淨損」影響 EPS **分子**，若測一引用 EPS 只作重疊記載。
  - **L13-A#4**（可轉債全成本：capped call、誘導轉換、自身股票衍生品）：本卡工具為**子公司層非可轉之優先權益**，成本以 PIK 股利入 NCI，非籌資節付現、非母公司自身股票合約。同屬「利息費用 < 融資全成本」族，型態差在**科目落點（權益／NCI vs 籌資節）與層級（子公司 vs 母公司）**。
  - **L13-P#2**（子公司有擔保票據現金掃款）、**L13-P#3**（母公司現金封閉）、**L13-I#3**（依評等債務含量選工具）：本卡不論現金優先順序或工具選擇誘因，只論既定工具之成本落點。L13-I#3 之「機構債務含量」若被測一引用，只作重疊。
  - **L13-I#2**（擔保人認股權）、**L13-I#4**（壽險 RBC 買方）、**L13-P#4**（OpenAI 跨供應商預算）：不涉。
  - **L2-A#2**（利息資本化墊高 AFFO）：本卡不論資本化；若 PIK 優先股利**不得資本化**而利息可資本化之差異被測一發現，只作重疊記載。**L6-A#4**（capex 現金流分類）、**L7-A#2**（持股公允值）、**L7-A#5**（融資租賃利息落 OI 之下）：不涉。
  - **L2-I#4** 之「非控制權益（JV）」僅為必問科目，非落差。**T-15**：不寫。
- §7-10 領域最近公開：APLD 10-Q（期末 2026-08-31，申報 2026-10-07）；APLD 10-K FY2026（期末 2026-05-31）。下一檢查點＝APLD FQ2 FY27 10-Q（期末 2026-11-30，約 2027-01）。

## 1. 落差一句

AI 資料中心開發商以**子公司層可贖回優先單位**募建置資金時，固定優先報酬（PIK）在 GAAP 上是權益之分配而非利息：利息費用、EBITDA、Adjusted EBITDA、利息覆蓋率與「淨負債／EBITDA」皆不含它；它只在淨損益之下以「歸屬（可贖回）非控制權益」扣除，本金列暫時權益而不入債務。恆等：
`融資全成本_t ≡ 利息費用_t ＋ NCI 優先股利_t（PIK 或現金）＋ 贖回／股利率調升嵌入衍生品之公允值變動_t`；`類債務本金 ≡ 帳列債務 ＋ 可贖回 NCI（暫時權益）`；其中只有第一項進利息費用與 EBITDA 調節。
種子載體（Applied Digital 10-Q，期末 2026-08-31，本輪 `sec.py doc --grep` 實讀）：APLD HPC TopCo 2 於 FY2026 向 MIP HPC Holdings, LLC（Macquarie）發行 1,825,000 優先單位，「proceeds of approximately $ 1.8 billion」，「resulted in a redeemable noncontrolling interest」；資產負債表「Redeemable noncontrolling interest 2,010,873」（千美元；前季 1,956,303）列於負債與股東權益之間（「TOTAL LIABILITIES, TEMPORARY EQUITY AND STOCKHOLDERS' EQUITY」）；當季「Interest expense 77,383」；「Noncontrolling interest preferred stock dividends … (60,051)」、「Non-cash dividends paid in-kind $ 60,051」；「Loss on change in fair value of derivatives 49,511」，附註 11：優先單位之「Redemption features and the Contingent Dividend Rate Increase feature, requiring bifurcation and remeasurement at fair value … recorded through earnings」；Adjusted EBITDA 64,412 之調節加回 interest expense 與 loss on change in fair value of derivatives，未見 NCI 優先股利行。`[D]` κ＝NCI 優先股利 ÷ 利息費用 ≈ 60.1 ÷ 77.4 ≈ 0.78（單季）；隱含年化優先報酬 ≈ 60.1 × 4 ÷ 1,825 ≈ 13%（以發行單位數 × 面額 1,000 推，面額未實讀，`[D]` 待測一核）。
種子主張：以利息費用、EBITDA 覆蓋或淨負債倍數衡量 AI 建置之資本成本與槓桿者，漏計可由已申報科目事前加總之子公司優先成本與暫時權益本金。本卡不定方向與量級，只立可拒絕之恆等。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（ASC 810 非控制權益歸屬；ASC 480-10-S99 可贖回權益列暫時權益；ASC 815-15 嵌入衍生品分拆）；非守恆、非誘因 |
| 量綱 | 利息費用、NCI 優先股利、衍生品 FV 變動［$／季］；全成本 ÷（債務＋可贖回 NCI）［%／年］；κ＝NCI 優先股利 ÷ 利息費用［無量綱］；λ＝可贖回 NCI ÷ 帳列債務［無量綱］ |
| 可見端 | 10-K／10-Q：資產負債表暫時權益、損益表「Net loss attributable to noncontrolling interest and redeemable noncontrolling interest」、權益變動表 NCI 優先股利行、補充現金流「Non-cash dividends paid in-kind」、Temporary Equity 附註、Derivative 附註、MD&A 非 GAAP 調節 |
| 指名不可見端 | 優先單位面額、股利率、調升條件與贖回價之完整條款（A&R UPA 原文；測一取 8-K 附件）；共識模型與評等是否將可贖回 NCI 計入債務、PIK 股利計入固定費用 |
| 主張 | 全成本 − 利息費用、類債務 − 帳列債務兩差額可由已申報科目算出；若市場與評等以利息費用、Adjusted EBITDA 覆蓋或淨負債倍數衡量，即錯置。可由「主流口徑已把可贖回 NCI 計為債務、PIK 股利計為固定費用」或「差額不足量」拒絕 |
| 外部參照物（測一查證） | 評等機構對混合工具／子公司優先股之債務含量方法論（Moody's hybrid basket、S&P intermediate equity content）；REIT／公用事業子公司優先股之慣常處理（只作會計路徑先例） |
| 表達工具型態（只指名，不選券） | 美股上市之 AI 資料中心開發商／HPC 託管商普通股或其優先股、子公司票據（APLD 為主載體；Core Scientific、TeraWulf、Cipher、IREN、Galaxy 為待查對照）。不選券 |
| 重疊 | L13-A#4（同族：利息費用 < 全成本）、L13-I#3（債務含量）、L13-A#3（EPS）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. APLD 10-Q（期末 2026-08-31）https://www.sec.gov/Archives/edgar/data/1144879/000114487926000059/apld-20260831.htm （本輪實讀：暫時權益 2,010,873、PIK 60,051、利息費用 77,383、衍生品 FV 損 49,511、Adjusted EBITDA 調節、附註 11／16）
2. APLD 10-K FY2026 https://www.sec.gov/Archives/edgar/data/0001144879/000114487926000048/apld-20260531.htm （全年 NCI 優先股利、四次交割序列、條款；未實讀）
3. APLD 10-Q（期末 2025-11-30、2026-02-28）https://www.sec.gov/Archives/edgar/data/1144879/000114487926000006/apld-20251130.htm ；https://www.sec.gov/Archives/edgar/data/1144879/000114487926000030/apld-20260228.htm （季序列；未實讀）
4. APLD 8-K 附件（Macquarie 交易公告）https://www.sec.gov/Archives/edgar/data/1144879/000149315225002040/ex99-1.htm ；Macquarie 新聞稿 https://www.macquarie.com/about/news/2025/macquarie-asset-management-agrees-to-form-a-partnership-with-applied-digital.html （條款、上限；未實讀）
5. 對照（未實讀）：Core Scientific 10-Q（期末 2026-06-30）https://www.sec.gov/Archives/edgar/data/0001839341/000183934126000014/core-20260630.htm ；TeraWulf 2026 財報新聞稿 https://investors.terawulf.com/sec-filings/all-sec-filings/content/0001083301-26-000026/a_wulfearningsrelease2026-.htm ——是否存在子公司優先／可贖回 NCI，測一以 `sec.py` 查。
6. 報導（未實讀，反方候選）：Motley Fool〈Why Shares of Applied Digital Are Getting Crushed〉https://www.fool.com/investing/2025/11/13/why-shares-of-applied-digital-are-getting-crushed ；Lowenstein〈$150M convertible preferred equity facility … Ellendale〉https://www.lowenstein.com/news-insights/firm-news/lowenstein-represents-applied-digital-in-150m-convertible-preferred-equity-facility-to-advance-development-of-ellendale-hpc-campus

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 可贖回 NCI 與 PIK 股利逐行列於資產負債表、損益表下方與補充現金流——讀 10-Q 者可得 | APLD 10-Q 原文（#1） | 資訊已公開，無落差 |
| R2 | 評等機構對子公司優先股／混合工具本有債務含量規則，賣方 EV 計算慣例含少數股權與優先股（EV ＝ 市值＋債務＋優先股＋NCI − 現金） | 測一須取 Moody's／S&P 方法論原文與具名賣方 EV 表 | 已定價（EV 口徑已含） |
| R3 | 優先報酬只在 TopCo 2 層，若子公司現金流足以支付且最終以出售／再融資贖回，母公司股東承擔之經濟成本＝稀釋子公司權益而非固定費用 | 測一須找具名來源 | 機制不入價格／方向不定 |
| R4 | 嵌入衍生品之 FV 變動可正可負，使單季「全成本」波動、方向不可定 | APLD 10-Q 附註 11（#1） | 方向不定 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 公司指引／法說原文已以含 NCI 優先股利之口徑說明融資成本或覆蓋率，或 ≥ 1 家具名賣方／評等機構已將 APLD 可贖回 NCI 計為債務、PIK 股利計為固定費用——已定價（R1／R2 擴及主流口徑）。
(2) `[D]` κ＝NCI 優先股利 ÷ 同期利息費用 < 0.3，或（NCI 優先股利 ÷ 同期 OCF 絕對值）< 5%，於可觀測 ≥ 2 季——量級不足。
(3) 主載體以外無 ≥ 1 家上市 AI 資料中心／HPC 發行人採同型子公司可贖回優先權益（`sec.py` 查對照 #5 與 IREN、CIFR、GLXY）——單一發行人特異。
(4) 可運作對照只能寫成 L13-A#4 可轉全成本、L13-A#3 EPS、L13-I#3 工具排序、L13-A#1 表外義務或 T-15。
(5) 主流估值口徑以已含 NCI 與優先股之 EV 倍數為主，且無具名證據顯示利息費用、Adjusted EBITDA 覆蓋或淨負債倍數入定價或契約（R2 成立）。
(6) 12 個月內無可檢驗事件（例：APLD FQ2／FQ3 FY27 10-Q 之 PIK 累積、股利率調升條件觸發、贖回／Sale 事件；或其他發行人新增同型工具）。

複查觸發器（若日後殺）：任一 AI 資料中心／HPC 上市發行人於 10-K／10-Q 或法說以「含優先／NCI 之全融資成本」口徑揭露；或評等機構公開將子公司可贖回優先計入調整後債務；或 APLD 之 Contingent Dividend Rate Increase 觸發或優先單位被贖回。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：暫時權益（可贖回 NCI）、歸屬 NCI 淨損益、權益變動表 NCI 優先股利、補充現金流 PIK、Derivative 附註 FV 變動、非 GAAP 調節。
2. 可交易工具：美股 AI 資料中心開發商普通股、其優先股或子公司票據（不選券）。
3. 半衰期：PIK 逐季累積；贖回／Sale 事件與股利率調升條件依 A&R UPA；APLD 2026 Revolving Credit Facility 到期與「Preferred Equity Purchase Agreement」特定日掛鉤（10-Q 原文），測一取該日。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L13［A］標「#5 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 一列（APLD TopCo 2 優先單位約 1.8B，10-Q 原文）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L13-A#1–#4、L13-P#1–#4、L13-I#1–#4、L2-A#2、L6-A#4、L7-A#2、L7-A#5、C-A3／C-A4 結論；不寫 T-15。
