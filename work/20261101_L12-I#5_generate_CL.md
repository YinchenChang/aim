# L12-I#5 生成卡｜監理與法制：誘因（IEEPA 關稅退款之請求權歸屬——退款付給進口人、經濟負擔已轉嫁下游；終局清算款只付起訴者）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260922_L12-I_generate_GK.md；archive/work/20261008_L12-I#2_generate_CL.md；archive/work/20261016_L12-I#3_generate_CL.md；archive/work/20261025_L12-I#4_generate_CL.md；work/20261025_L12-I#4_test1_CL.md | EMITS: work/20261101_L12-I#5_generate_CL.md -->
**日期：** 2026-11-01　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 6／6）　**格：** L12-I　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。非「已殺／刻意排除」格中最後測一最舊＝L12-I（#4，2026-10-25）；其次 L5-I／L6-P／L6-A／L6-I／L13-A（2026-10-26）。既有生成 4 份 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tariff`／`IEEPA`／`refund`，命中 0 筆。內部數字（§12）未取用。
- 比對（本卡須異型）：
  - **L12-I#1**（GK）：法規合規成本落部署者。本卡非合規成本，為**已徵收稅款之返還**之歸屬。
  - **L12-I#2**：AI 產出 IP 補償＝賣方零保費賣權；死於觸發事件 0 件。本卡事件已發生（最高法院判決已出、CBP 已付款），不待第三方求償觸發。
  - **L12-I#3**：§232 配額在建期倍數；選擇變數＝時點。本卡選擇變數＝**是否起訴保全終局清算款**與**退款是否轉付下游**；稅基為 IEEPA，非 §232。
  - **L12-I#4**：HSR 申報形式 vs ASC 805 雙重定性。本卡無併購。
  - L12-A#1–#5（營收權重、法定賠償 vs ASC 450、所得稅時序、營業動產稅、REIT 資格）：本卡不以會計認列（ASC 450-30 時點）為落差——認列差異只作可觀測載體；落差在**請求權人與經濟負擔者分離**所生之誘因。
  - L4-A#5（H20／H200 承諾提列）、L12-P#3（出口管制質量平衡）：出口端，非進口稅返還。
  - ARCH_dead #1–#19：無關稅返還型。
- §7-10 領域最近公開：Supply Chain Dive 2026-10-08（引 10-06 法院文件）——CBP 已開始處理起訴者之終局清算款；10-02 止約 US$136.6B 退款受理／核定、US$126B 送財政部撥付；聯邦巡迴上訴法院上訴未決。CAPE Phase 3 2026-10-06 開放（僅 CIT 起訴者）。下一檢查點＝聯邦巡迴法院判決、V.O.S. Selections 集體認證裁定（Corporate INTL 稱 08-06 言詞辯論未裁）、SMCI 1Q FY27 10-Q（約 2026-11 上旬）、HP FY26 10-K（約 2026-12）。

## 1. 落差一句

最高法院 2026-02-20（*Learning Resources v. Trump*）判 IEEPA 關稅無法源；退款依 19 C.F.R. §24.36 付**登記進口人（IOR）**，但 IOR 多已以附加費或調價把關稅轉嫁給下游（AI 伺服器、網通、電力冷卻設備之買方＝超大規模雲與新雲）。同一筆退款因此有兩個主張者：**IOR 認列為銷貨成本減項**（HP：已收 US$127M＋期後 US$91M，「recognized as a reduction of Products cost of net revenue when received」，GAAP 與非 GAAP 皆計入），**下游以變更法令條款、不當得利追索**（UPS、FedEx、Costco、EssilorLuxottica 已被訴；FedEx 公開稱將轉付）。另一層：政府主張終局清算款（估 US$30B+）只退予已向 CIT 起訴者——退款之有無取決於 IOR 是否付出訴訟成本，而轉嫁越完整之 IOR 起訴誘因越弱。**落差＝市場以「IOR 之一次性利益」計價退款，未計下游追索與「未起訴即喪失」兩項；方向未定**（亦可能下游無合約權利、IOR 全留）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：規則端（退款付 IOR；終局清算款僅付起訴者——政府上訴主張）× 合約端（附加費／變更法令條款決定下游追索權）× 行為端（IOR 選擇起訴與否、轉付與否、認列時點） |
| 選擇者 | IOR（HPQ、HPE、SMCI、VRT、ANET、DELL 等 AI 硬體與設施設備進口人）；對手方＝下游大客戶 |
| 誘因式（僅定義） | IOR 留存退款之期望值＝Σ 可退關稅 × [1 − 下游追索成功機率 × 轉嫁比例] − 起訴成本（終局清算部分）；下游以議價力（續約、未來價格）實現追索，不必經訴訟 |
| 已讀事實 | HPQ 10-Q 3Q FY26：已申請約 US$0.3B，已收 US$127M、期後 US$91M，收到時沖減成本。HPE 10-Q 3Q FY26：「received certain tariff refunds … not … material」。SMCI 10-K FY26：「we have not recognized an asset related to the potential refund … will recognize … when … realized or realizable」；FY26 關稅費用增加 US$237.7M（+228.3%）；另列 §232 求償應收 US$65.4M。VRT 10-Q 3Q26：CAPE Phase 1（2026-04）、Phase 2（2026-06），「In accordance with ASC 450-30 … gains will only be recognized once … realized or realizable」，未揭露金額。ANET 10-Q 2Q26：只敘判決，未提退款。DELL 10-Q 2Q FY27：無「IEEPA」字樣。 |
| 未證之連結 | AI 硬體 IOR 對大客戶是否以附加費（可追索）或一般調價（難追索）轉嫁；大客戶合約有無變更法令／稅費調整條款；IOR 是否為 CIT 原告（決定終局清算款）；是否已有 B2B 追索訴訟或轉付聲明；HTS 8471／8517 等 AI 硬體品項於 IEEPA 期間實際課徵範圍（多項電子品曾獲豁免） |
| 量綱 | 可退 IEEPA 關稅 ÷ 最近 4 季營業利益（%）；已認列退款中可被下游追索之比例；終局清算未起訴部分 ÷ 可退總額 |
| 半衰期 | 聯邦巡迴法院判決（未定）；CAPE 各階段（月）；下游追索（續約週期，年）；下游消費者集體訴訟（年） |

## 3. B 端可觀測載體（只指名）

1. HPQ 10-Q 3Q FY26 https://www.sec.gov/Archives/edgar/data/47217/000004721726000051/hpq-20260731.htm （Note 11 Tariffs、MD&A 毛利；本輪 sec.py 實讀）；HP FY26 10-K（未出）。
2. HPE 10-Q 3Q FY26 https://www.sec.gov/Archives/edgar/data/1645590/000164559026000080/hpe-20260731.htm （Trade and Tariffs Update；本輪實讀）。
3. SMCI 10-K FY26 https://www.sec.gov/Archives/edgar/data/0001375365/000137536526000022/smci-20260630.htm （Note 15 Other matters、Other Assets「Tariff receivable」、成本結構；本輪實讀）；1Q FY27 10-Q（未出）。
4. VRT 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/1674101/000162828026067893/vrt-20260930.htm （IEEPA 段；本輪實讀）；ANET 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1596532/000159653226000175/anet-20260630.htm （本輪實讀，只敘判決）；DELL 10-Q 2Q FY27 https://www.sec.gov/Archives/edgar/data/1571996/000157199626000046/dell-20260731.htm （0 筆）。
5. 規則與程序：Tradlinx 2026-04-08（19 C.F.R. §24.36、CAPE、*Atmus Filtration v. US*）https://blogs.tradlinx.com/ieepa-tariff-refunds-where-the-166-billion-refund-process-actually-stands-and-what-importers-should-do-now/ ；Foley 2026-06-11（政府上訴、終局清算款 US$30B+）https://www.foley.com/insights/publications/2026/06/what-every-multinational-should-know-about-the-governments-appeal-of-judge-eatons-universal-ieepa-tariff-refunds-order-and-why-it-is-claiming-it-can-keep-billions-of-dolla/ ；Thompson Hine 2026-06-03 https://www.thompsonhinesmartrade.com/2026/06/trump-administration-appeals-cits-ieepa-tariff-refund-order/ ；Corporate INTL 2026-09-17（CAPE Phase 1–3）https://corp-intl.com/news/what-is-the-status-of-ieepa-refunds ；Supply Chain Dive 2026-10-08 https://www.supplychaindive.com/news/cbp-starts-paying-out-ieepa-tariff-refunds-for-finally-liquidated-entries/832411/ 。
6. 下游追索：Foley 2026-06-18 https://www.foley.com/insights/publications/2026/06/what-every-multinational-should-know-about-the-emerging-battle-over-who-ultimately-keeps-ieepa-tariffs/ ；S&C 2026-03-26（UPS、EssilorLuxottica、FedEx、Costco 訴訟；退款請求權買賣）https://www.sullcrom.com/SullivanCromwell/_Assets/PDFs/Memos/Tariff-Refund-Claims-Spur-Litigation-Potential-Deals.pdf 。
7. 未讀：CIT 原告名單（AI 硬體 IOR 是否在列）；V.O.S. Selections 集體認證（Steptoe 頁擷取失敗，客戶端錯誤）；超大規模雲 10-Q 是否揭露向供應商追索退款；具名賣方就退款歸屬之建模。

缺段（§7-2）：供應合約之附加費與變更法令條款未公開；本輪未讀 CIT 原告名單；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 下游一般無合約權利：消費者「purchased products at prevailing market prices, not contractual rights to future tariff recoveries」；無轉付之法律義務 | Foley 2026-06-18 | 追索一側可能為零 |
| R2 | AI 伺服器與網通（HTS 8471／8517）於 IEEPA 對等關稅多獲豁免、墨西哥 USMCA 合格品免課；AI 硬體 IOR 之 IEEPA 稅基可能小，關稅費用主為 §232／§301 | SMCI 另列 §232 求償；HPE「not … material」 | `[D]` 量級不足 |
| R3 | 終局清算款爭議只涉未起訴者；大型 IOR 多已起訴或在 Phase 1 未清算範圍內 | Corporate INTL 2026-09-17；Supply Chain Dive | 「未起訴即喪失」層空 |
| R4 | 退款屬一次性、非經常項，市場本就不給倍數；歸屬錯誤不改持續盈利 | HPQ 以 EPS 影響單列（Pulse 2.0 2026-08-28） | 無重定價 |
| R5 | FedEx 已公開轉付，顯示壓力已公開可見 | S&C 2026-03-26 | 已定價 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) `[D]` 量級：所列 AI 硬體／設施 IOR（HPQ、HPE、SMCI、VRT、ANET、DELL）之可退 IEEPA 關稅（已申請或已揭露者；未揭露以申報之關稅費用中 IEEPA 部分推估）÷ 最近 4 季營業利益絕對值皆 < 2%；或
(2) 追索端空：所列 IOR 之申報、法說原文與主要客戶合約揭露皆無附加費／變更法令轉嫁之證據，且 12 個月內（至 2027-11-01）無 B2B 追索訴訟或轉付聲明（下游無權利）；或
(3) 起訴端空：聯邦巡迴法院維持全面退款（含未起訴者之終局清算款），或所列 IOR 均為 CIT 原告／其可退款全在未清算範圍（「未起訴即喪失」層無作用）；同時 (2) 亦觸發（兩側皆空）；或
(4) 已定價：具名賣方或評等機構已明示將退款歸屬（留存比例或追索風險）入模，或所列 IOR 已一律宣告轉付；或
(5) 誘因反向：所列 IOR 已主動以退款抵減下游價格（無需追索），使 IOR 留存與下游追索之衝突不存在；或
(6) 已觀測之毛利或股價變動由非本機制項（記憶體價格、AI 出貨組合、§232 新稅）解釋，且一手原文如此歸因。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：銷貨成本（退款沖減）、其他應收、或有利得（ASC 450-30）、訴訟附註、合約負債。2. 可交易工具：IOR（不選）。3. 半衰期：上訴判決不定期；CAPE 逐階段；下游追索隨續約。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L12［I］格加「#5 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0146；`export/LEADS_算力收支.md` 追加 1 筆（SMCI FY26 關稅費用增量）。不改 L12-I#1–#4、L12-A#1–#5、L12-P#1–#5、L4-A#5、L12-P#3 結論。
