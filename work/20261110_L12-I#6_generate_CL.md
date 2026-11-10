# L12-I#6 生成卡｜監理與法制：誘因（H-1B 受配額申請之法定價格——US$100k 公告費〔已被撤銷、延長至 2027-09-21〕與擬議 US$103,265 規則費並行；雇主在「付費／免配額管道／離岸／自動化」間選擇，與 AI 取代入門人力之敘事同向而混淆歸因）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260922_L12-I_generate_GK.md；archive/work/20261008_L12-I#2_generate_CL.md；archive/work/20261016_L12-I#3_generate_CL.md；archive/work/20261025_L12-I#4_generate_CL.md；archive/work/20261101_L12-I#5_generate_CL.md；work/20261101_L12-I#5_test1_CL.md；archive/work/20261101_L12-A#5_generate_CL.md；archive/work/20261031_L4-A#5_generate_CL.md；archive/work/20261014_L14-I#2_generate_CL.md | EMITS: work/20261110_L12-I#6_generate_CL.md -->
**日期：** 2026-11-10　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1／6）　**格：** L12-I　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。非「已殺／刻意排除」格中最後測一最舊＝L12-I（#5，2026-11-01）；其次 L6-P／L6-A／L6-I／L7-P／L7-A（2026-11-02）。既有生成 5 份 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `H-1B`／`visa`／`IT services`／`offshore`，命中 0 筆。內部數字（§12）未取用。
- 先行放棄之候選（記錄，不生成）：USG 對 H200 對華出貨之 25% 抽成（經美國檢驗再進口課稅）。NVDA 10-Q 2Q FY27 原文：「Those shipments account for less than 1% of Data Center revenue」，且 H200 提列已由 L4-A#5／L12-A#5 觸及 → 量級不足且型態重疊，不採。
- 比對（本卡須異型）：
  - **L12-I#1**（GK）：法規合規成本落部署者。本卡為**勞動投入之法定價格**，非合規成本；選擇者為雇用人力之服務商，非 AI 部署者。
  - **L12-I#2**：IP 補償零保費賣權；觸發待第三方。本卡價格已公告、規則已擬議，不待第三方求償。
  - **L12-I#3**：§232 配額之時點選擇（保持在建）。本卡選擇變數＝**人力管道**（受配額 H-1B／免配額／L-1／離岸／自動化），非資本支出時點。
  - **L12-I#4**：HSR 門檻下之交易法律形式。本卡無併購。
  - **L12-I#5**：已徵稅款退還之歸屬。本卡為前瞻之新增費用，且其法律地位二元未定。
  - **L14-I#2**（企業自報裁員歸因 AI）：該卡為自願揭露層之歸因選擇；本卡為**法規價格**造成之同向人力替代，供給端（服務商）而非需求端（企業客戶），可觀測載體為申請數據與在岸／離岸組合，不用自報理由。
  - ARCH_dead #6／#18（C-A1、C-I5：不可分列）：本卡之主要死法預期相同（簽證成本併入營業成本；見 §3-1），已列為否決 (2)，不迴避。

## 1. 落差一句

市場把 IT 服務商在岸入門人力縮減、在岸／離岸組合移動、營收單價下行一併歸因於「AI 取代入門工程」；但同一窗內，受配額 H-1B 申請之法定價格由近零跳至約 US$100k 級（Proclamation 10973 公告費 2025-09-21 起；D. Mass. 2026-06-08 撤銷、1st Cir. 2026-07-24 拒絕暫停；2026-09-18 公告延長至 2027-09-21；DHS 2026-08-25 另擬 US$103,265 規則費，適用「all H-1B cap-subject petitions」），雇主之最適反應（改走免配額／L-1、離岸交付、或以自動化取代）與 AI 敘事**在營收上同向、在毛利上可能反向**（離岸化提毛利、AI 單價通縮壓毛利）——歸因錯配之方向與量級未被分離。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：規則端（公告費／規則費二軌，法律狀態二元）× 選擇端（雇主之人力管道）× 時點端（撤銷窗內提前申請之選擇權；規則生效前之前移） |
| 選擇者 | 受配額 H-1B 之大量申請人（IT 服務商：CTSH、INFY、WIT、ACN、EPAM 等；亦含超大雲與晶片商之入門工程招聘） |
| 誘因式（僅定義） | 每一在岸入門職位之管道成本＝min{ 薪資＋F_cap（受配額費），薪資′＋F_L1（免配額／L-1），離岸成本＋協作折損，自動化成本 }；F_cap 之期望值＝Σ_狀態 P(狀態) × 費額（狀態＝撤銷維持／上訴翻轉／規則生效／二者並課——DHS 原文「the petitioner would be required to pay both amounts」） |
| 已讀事實 | (a) D. Mass. 2026-06-08 撤銷；1st Cir. 2026-07-24 拒絕暫停（Clark Hill 2026-07-28）。(b) 2026-09-18 公告延長至 2027-09-21；N.D. Cal. 2026-09-30 *Global Nurse Force v. Trump* 阻止施行政策；政府 2026-10-09 上訴 9th Cir.；D.C. Cir.（*Chamber v. DHS*，地院 2025-12 維持該費）2026-03 言詞辯論、未判（Ahluwalia 2026-11-05；單一來源）。(c) 91 FR 54817（2026-08-25）：US$103,265／件、受配額（含碩士豁免額）、預估 85,000 件、回收約 US$8.78B；意見期至 2026-09-24；生效日未載；註 4「Proclamation 10973, unless extended, will expire before the fee proposed in this rule will take effect」。(d) FY2027 抽籤首次採工資級距加權（2026-02-27 生效；Ogletree 2026-04-01）。(e) CTSH 10-Q 3Q26：營業成本含「project-related immigration and travel」，**未分列**；全文 0 筆「H-1B」 |
| 未證之連結 | 各 IT 服務商受配額新申請件數（USCIS H-1B Employer Data Hub）；在岸／離岸營收或人力組合之季揭露（INFY／WIT 資料表）；費用是否轉嫁客戶（費率卡、合約）；撤銷窗內申請是否前移；規則終版與生效日；工資加權抽籤使入門級（Level I）中籤率下降之幅度 |
| 量綱 | 受配額新申請件數 × 費額 ÷ 最近 4 季營業利益（%）；在岸人力占比季變動（百分點）；FY2028 登記數（2027-03）÷ FY2027 |
| 半衰期 | 規則終版（月）；1st／9th／D.C. Cir. 判決（月至年）；FY2028 配額登記 2027-03；公告費至 2027-09-21 |

## 3. B 端可觀測載體（只指名）

1. CTSH 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/1058290/000105829026000041/ctsh-20260930.htm （成本科目口徑；本輪 sec.py 實讀，簽證成本併入營業成本）。
2. INFY 6-K 2026-10（2Q FY27 結果）https://www.sec.gov/Archives/edgar/data/0001067491/000106749126000044/exv99w01.htm （本輪 sec.py 實讀 exv99w01，「onsite」「visa」0 筆；資料表其他附件未讀）。
3. 規則：91 FR 54817 https://www.federalregister.gov/documents/2026/08/25/2026-17324/fee-for-certain-h-1b-petitions （本輪讀至 III.B 與註 1–59；RIA 本體與註 60–116 僅摘要，未逐字）。
4. 訴訟狀態：Clark Hill 2026-07-28 https://www.clarkhill.com/news-events/news/first-circuit-blocks-reinstatement-of-100k-h-1b-fee/ ；Ahluwalia 2026-11-05 https://www.ahluwalialaw.com/what-is-happening-to-the-100000-h-1b-fee-where-things-stand-in-november-2026/ 。
5. 抽籤：Ogletree 2026-04-01 https://ogletree.com/insights-resources/blog-posts/uscis-completes-fiscal-year-2027-h-1b-lottery/ 。
6. 未讀：USCIS H-1B Employer Data Hub（雇主別核准數）；USCIS 登記頁（擷取失敗：PROVENANCE_REQUIRED，非不存在）；DOL OFLC LCA 季揭露檔；Fragomen 延長公告頁（客戶端錯誤）；WIT／ACN／EPAM 申報；具名賣方對費用影響之建模。

缺段（§7-2）：FY2027 登記與中籤數本輪未取得（USCIS 頁擷取失敗；FY26 登記 343,981 僅見於 FR 註摘要，二手）；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 費用目前不生效（撤銷＋施行政策被阻），規則生效日未定且公告費將先到期 | D. Mass.／1st Cir.；91 FR 54817 註 4 | 無誘因作用之期間可能覆蓋整個窗 |
| R2 | DHS 自估 H-1B 申請需求「inelastic」 | 91 FR 54817 RIA（摘要，未逐字） | 無替代行為 → 無錯配 |
| R3 | 大型 IT 服務商早已以在地招聘降低簽證依賴；簽證成本併入營業成本、不分列 | CTSH 10-Q 3Q26 口徑 | 量級與可分離性 |
| R4 | 費用若生效，雇主可轉嫁客戶（費率上調），毛利不變 | 待讀：費率卡、法說 | 誘因不改毛利 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) `[D]` 量級：所列 IT 服務商（CTSH、INFY、WIT、ACN、EPAM）FY2026 受配額新申請（或初次核准）件數 × US$100k ÷ 最近 4 季營業利益絕對值皆 < 2%；或
(2) 不可分離：所列發行人之申報、資料表、法說原文皆無在岸／離岸組合或簽證成本之季揭露（C-A1／C-I5 型），且無第三方雇主別申請序列可對應；或
(3) 規則端空：1st／9th Cir. 維持撤銷且 DHS 規則於 2027-09-21 前未發布終版（或撤回），即窗內無任一費用可施行；或
(4) 已定價：具名賣方或發行人已明示量化費用影響（每股或毛利基點）並入指引，或所列發行人已宣告全額轉嫁客戶；或
(5) 誘因不作用：FY2028 受配額登記數（2027-03 公布）÷ FY2027 ≥ 0.9，且所列發行人在岸人力占比無季變動（需求不彈性，R2 成立）；或
(6) 已觀測之在岸人力或毛利變動由非本機制項（AI 單價通縮、客戶裁量支出、匯率）解釋，且一手原文如此歸因；或
(7) 重定價窗 < 12 個月：唯一檢驗事件（規則終版、上訴判決、FY2028 登記）皆落於 2026-11-10 起 12 個月內且結果二元可即時定價。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：營業成本（簽證／差旅併列）、在岸人力占比、分包成本。2. 可交易工具：IT 服務商 ADR／普通股（不選）。3. 半衰期：規則終版不定期；上訴判決；FY2028 配額登記 2027-03。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L12［I］格加「#6 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0188。線索輸出（§D）：本輪實讀事實無 AI 算力投入／收入／硬體／雲端／資料中心新事實（NVDA H200 <1% 已由前輪觸及），未追加。不改 L12-I#1–#5、L12-A#1–#6、L12-P#1–#6、L4-A#5、L14-I#2 結論。
