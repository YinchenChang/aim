# L11-A#5 生成卡｜人類注意力：會計恆等（商譽減損測試之市值調節恆等：搜尋流量依賴之出版商，管理層報告單位公允價值合計 ΣFV_RU 與市場企業價值之隱含控制溢價 κ；κ 超出可辯護帶時，須由「減損追上市價」或「交易／分拆實現追上 FV」二者之一收斂）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261001_L11-A_generate_GK.md；archive/work/20261013_L11-A#2_generate_CL.md；work/20261013_L11-A#2_test1_CL.md；archive/work/20261020_L11-A#3_generate_CL.md；work/20261020_L11-A#3_test1_CL.md；archive/work/20261027_L11-A#4_generate_CL.md；work/20261027_L11-A#4_test1_CL.md；archive/work/20261020_L14-P#3_generate_CL.md；archive/work/20261025_L12-I#4_generate_CL.md | EMITS: work/20261103_L11-A#5_generate_CL.md -->
**日期：** 2026-11-03　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 5→6／6）　**格：** L11-A　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。不主張價值方向。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。非已殺／刻意排除格中最後測試日最舊＝2026-10-27（L11-A，#4 測一）；L11-I／L13-P／L13-I／L14-* 為 10-28 起。取 **L11-A**，既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `tokenomics_leads.py publisher traffic goodwill "AI Overviews"`＝命中 0；未用。內部研究數字（§12）：未查（本卡非算力收支量）。載體全由本輪 sec.py／WebSearch 實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L11-A#1**（曝光 × 單價流量恆等；死因＝兩因子水準不可並列）：本卡不拆價量，恆等在資產負債表（帳面值 vs 公允價值 vs 市值）。
  - **L11-A#2**（內容資產按觀看型態攤銷之估計變更；死因＝驅動無可觀測證據）：本卡非攤銷估計；減損測試結果與「無超額」報告單位已於申報一手可見（§3）。
  - **L11-A#3**（訂閱預收遞延滯後；死因＝公司自供收斂、滯後 ≤ 4 季）：本卡無認列滯後。
  - **L11-A#4**（有限存量池一次性轉換；死因＝收斂事件 < 12 個月且前導已公開）：本卡之檢驗事件為年度測試日（10-01）之兩個循環（FY26 10-K 約 2027-02；FY27 10-K 約 2028-02），測一須驗第二循環是否實質，否則依 (3) 殺。
  - **L14-P#3**（BPO 人工處理量守恆；Concentrix 商譽減損僅作已定價反方）、**L12-I#4**（併購申報與 ASC 805）：前者減損為旁證，後者為併購定性；本卡之恆等為 ASC 350 報告單位 FV 對市值之調節，不同。
  - **ARCH_dead C-A3／C-A4**（折舊年限／續約單價樞紐）：不涉年限與單價。**C-A1**（可分離性）：本卡之分離單位為申報揭露之報告單位與分部商譽，測一驗可分離。**L11-P**：不恢復。
- §7-10 領域最近公開：Ziff Davis 10-Q 2Q26（申報 2026-08-07）；People Inc 10-Q 3Q26（acc 0001628280-26-068882）。下一檢查點＝Ziff Davis 3Q26 10-Q（約 2026-11 上旬，日期待測一確認）、兩家 FY26 10-K（2027-02，含 2026-10-01 年度測試結果）。

## 1. 落差一句

搜尋流量依賴之數位出版商於 AI 摘要／AI 搜尋擴張期，以 ASC 350「收益法＋市場法」各報告單位公允價值通過（或僅小額未通過）減損測試；恆等 ΣFV_RU − ΣCV_RU ≥ 0（未減損單位）與 ΣFV_RU ≡ (市值＋淨債) × (1＋κ) 要求：若隱含控制溢價 κ 超出審計實務可辯護帶，則下一測試循環必由「減損把帳面拉向市價」或「出售／分拆以接近管理層 FV 實現」二者之一收斂——Ziff Davis 2026-06 以 $1.2B 出售 Connectivity、認列稅前利得 $860.6M，即後者之一手前例；同期 Health & Wellness 單位減損 $54.8M、另一 Cybersecurity & Martech 單位「no excess fair value」，即前者。種子主張：市場把注意力出版商之減損讀為非現金雜訊，而未以 κ 讀出管理層 FV 與市價之間待解之落差。本卡不主張收斂方向與量級，只立可拒絕之「κ 可由申報與市價界定，且其收斂事件落在 ≥ 12 個月窗」。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等（A）**：減損 ≡ max(0, CV_RU − FV_RU)；FV_RU ≡ w·DCF_RU ＋ (1−w)·(同業倍數 × EBITDA_RU)（ZD：w＝0.5，一手）；調節 ΣFV_RU ≡ EV_mkt × (1＋κ)；出售時 利得 ≡ 價款 − CV_RU（≥ 0 證 FV_RU ≥ CV_RU 於該單位） |
| 驅動（因果層，§7-5） | AI 搜尋／摘要使搜尋轉介流量下滑 ⇒ 報告單位預測營收與 EBITDA 下修 ⇒ DCF 端 FV 下降；同業倍數壓縮 ⇒ 市場法端 FV 下降；與之競爭之驅動為非注意力單位（Cybersecurity & Martech、Connectivity）之交易價值 |
| 量綱 | 商譽、CV_RU、FV_RU［美元］；κ［無量綱］；headroom h＝(FV−CV)/CV［無量綱］ |
| 可見端 | 10-K／10-Q 商譽分部表、減損金額、「no excess fair value」與「< 10%／< 20% headroom」揭露、年度測試日（10-01）、FV 方法權重、出售利得；股價 × 流通股、淨債 |
| 指名不可見端 | 各報告單位 FV 數值本身（僅揭 headroom 帶）、DCF 折現率與終值成長、同業清單、審計師可接受之 κ 帶 |
| 外部參照物（測一查證） | 控制溢價實證帶（具名研究或評價實務，如 Mergerstat 類統計）；審計／SEC 意見函對「市值低於帳面卻未減損」之詢問先例 |
| 表達工具型態（只指名，不選券） | 美股上市數位出版／媒體控股普通股；不選券 |
| 重疊 | L14-P#3（他層減損作反方）、L13 系列（帳面 vs 市值）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Ziff Davis 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/0001084048/000108404826000046/zd-20260630.htm ：Goodwill impairment 54,839（千美元，Health & Wellness 一報告單位）；「following a period of declining results and reductions in forecasted revenue and EBITDA」；FV 以「equal weighting of an income approach … and a market approach that uses the guideline public company approach」；「following impairment at one reporting unit within the Cybersecurity & Martech reportable segment during the year ended December 31, 2025, there was no excess of fair value over the carrying value at that reporting unit」；分部商譽 6/30/26：Tech & Shopping 322,172、Gaming & Ent 80,506、Health & Wellness 350,968、Cyber & Martech 537,356、合計 1,291,002；股東權益 2,237,458（XBRL）；Connectivity 售予 Accenture，「aggregate purchase price of $ 1.2 billion」、稅前利得「approximately $ 860.6 million」（2026-06-17 完成）。
2. Ziff Davis 10-K FY25（sec.py）https://www.sec.gov/Archives/edgar/data/1084048/000108404826000005/zd-20251231.htm ：「tests goodwill for impairment annually on October 1st」；FY25「performed quantitative fair value tests of all of its reporting units following a sustained decline in the Company's stock price」；減損 FY23／24／25＝56.9／85.3／17.6M；「There were no other reporting units with less than 10% excess fair value over carrying value」（截至 2025-12-31）。
3. Ziff Davis 8-K 2Q26 新聞稿（sec.py）https://www.sec.gov/Archives/edgar/data/0001084048/000108404826000043/zd20260630pressrelease.htm ：Q2 回購 $121.5M；CEO「focused on deploying capital strategically」。
4. People Inc 10-Q 3Q26（sec.py）https://www.sec.gov/Archives/edgar/data/0001800227/000162828026068882/ppli-20260930.htm ：Goodwill 1,507,959（千美元）；Google 服務協議不續約通知（2025-12-10），Search 分部結束並列停業；本季無商譽減損字句（grep 命中僅方法與定義句）。
5. People Inc（時名 IAC）10-K FY25（sec.py）https://www.sec.gov/Archives/edgar/data/1800227/000162828026009997/iaci-20251231.htm ：年度測試日 10-01；2025-10-01「elected to perform a qualitative assessment for each of its reporting units」且無減損；「The aggregate carrying value of goodwill for which the most recent estimate of the excess of fair value over carrying value is less than 20% is $283.4 million」；2024-Q4 因股價下跌做全單位定量測試、無減損。
6. 二手線索（不作證據）：Relevant Audience「People Inc. says Google search traffic is down 40%」https://www.relevantaudience.com/geo/people-inc-google-search-traffic-down-40-percent/ ；madrimasd 轉載「Ziff Davis mulls strategic review as stock trades 86% below analyst sum-of-parts valuation」https://ecosystem.madrimasd.org/news/feed/ziff-davis-mulls-strategic-review-as-stock-trades-86-below-analyst-sum-of-parts-valuation ——測一須回一手（法說逐字稿、8-K）。

缺段（§7-2）：兩家現行市值與淨債（測一取申報封面股數 × 收盤價，日期釘死）；各報告單位 headroom 之逐單位數；Ziff Davis 3Q26 10-Q 與 2026-10-01 年度測試結果；具名賣方 SOTP 原文；控制溢價參照帶。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 減損為非現金，市場已以股價先行反映；κ 之收斂若走減損一端，不改現金流，無錯價可捕捉 | #1、#2（股價下跌觸發定量測試） | 已定價／無可捕捉 |
| R2 | FV 合計含非注意力單位（Cyber & Martech；People Inc 之 MGM 持股、Care.com），κ 之落差由非 L11 資產驅動，非搜尋流量 | #1、#4 | 驅動不在本層 |
| R3 | 公司已自行以出售實現（Connectivity）並大額回購，收斂路徑已公告 | #1、#3 | 已公告 |
| R4 | κ 在控制溢價常態帶內，無待解落差 | 待測一參照物 | 恆等不緊 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 以申報日股數 × 收盤價＋淨債計之 EV_mkt 與 ΣCV_RU（或股東權益）比較，κ 之下界（僅以 CV 代 FV）落在具名控制溢價參照帶內——恆等不緊（R4）。
(2) 扣除非注意力單位（Cybersecurity & Martech、MGM 持股、Care.com 等）後，注意力單位之 CV 與可歸屬市值無法分離至區間寬度 < 0.5 倍中點——不可分離（R2；C-A1 型）。
(3) 重定價窗（≥ 12 個月）內無可觀測收斂事件：2026-10-01 測試結果（FY26 10-K）之外，下一循環（2027-10-01 → FY27 10-K）或已公告之出售／分拆時程不構成第二事件，或兩者皆已於窗前公告。
(4) 公司或具名賣方已以 SOTP／減損 headroom 明示 κ 之落差並給出收斂路徑（出售、分拆或減損指引）——已定價（R1／R3）。
(5) 可運作對照只能寫成曝光 × 單價（L11-A#1 型）、攤銷估計（L11-A#2 型）或認列滯後（L11-A#3 型）。
(6) 一手原文把報告單位 FV 下修主因歸於非搜尋流量之因素（如廣告技術訴訟、課程收入、單一客戶），使因果驅動不在 AI 搜尋流量層。

複查觸發器（若日後殺）：任一搜尋依賴出版商揭露逐報告單位 headroom 數值；SEC 意見函就市值低於帳面未減損提問；出售某注意力單位且價款與 CV 可並列。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：商譽分部表、Goodwill impairment、出售利得（停業部門）、股東權益；Critical Accounting Estimates 之 headroom 句。
2. 可交易工具：數位出版／媒體控股普通股。不選券。
3. 半衰期：年度測試 10-01 → 10-K 次年 2 月；定量測試另由股價持續下跌觸發。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0158；`query/ARCH_matrix.md` L11［A］標「#5 已生成」；`AIM_FUNNEL.md` §3 待測格一句。不寫入：INDEX.json、ARCH_dead、RETRIG、ARCH_live、`export/LEADS_算力收支.md`（本輪實讀事實非 AI 算力收支類）。不改 L11-A#1–#4、L11-I#1–#4、L11-P、L14-P#3、L12-I#4、C-A1／C-A3／C-A4 結論；不寫 T-15。
