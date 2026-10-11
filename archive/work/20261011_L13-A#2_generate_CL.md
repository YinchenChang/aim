# L13-A#2 生成卡｜資本與融資結構：會計恆等（客戶預付之重大融資成分：類債務流入入營業現金流；認列期營收＞當期現金）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260928_L13-A_generate_GK.md；archive/drive/USED_20260928_L13-A_test1_GK.md；archive/drive/USED_20260929_L13-A_T_GK.md；work/20261011_L6-I#2_test1_CL.md；work/20261011_L6-P#2_test1_CL.md；work/20261011_L4-A#2_test1_CL.md | EMITS: work/20261011_L13-A#2_generate_CL.md -->
**日期：** 2026-10-11　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 5→6／6）　**格：** L13-A　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L6-I#2 本日測一，Q-0024 done）。尚無 #2 且非已殺／刻意排除之格中，最後測試日最舊者＝**L13-A**（T 2026-09-29，`archive/drive/USED_20260929_L13-A_T_GK.md`）；其餘無 #2 格最後測試日 2026-09-30 以後（L7、L10、L11、L13-P／I、L14、L15）。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py prepayment "financing component" "customer prepaid"`，**命中 0 筆**。
- 比對之舊檔與死因型態，本卡須異型：
  - **L13-A#1**（T 不進 L）：入表租賃負債≠義務上界（未開始租／RVG／JV）——**負債端之量測時點**。本卡換到**現金流量表之分類**與**營收／利息之拆分**：客戶預付（重大融資成分）入營業活動現金流，不入負債之有息債欄。
  - **L13-I**（測一不通過）：融資載具比例／應收總額。本卡不論載具。
  - **L13-P**、**C-A3／C-A4**（死）：折舊年限、重定價窗。本卡不論年限。
  - **L4-A#2**：整機商 ΔWC／CCC（應付帳款延展）。本卡為客戶預付之融資成分，非供應商帳期。
  - **L2-A#2**：利息資本化。本卡為利息自營收拆出，方向相反（營收含融資增額、利息費用在營業利益之下）。
  - **L6-I#2**（本日測一不通過）：bookings 計酬；**L6-P#2**：MW 守恆，曾引預付現金流一行但未論其分類。本卡不論計酬、不換算 MW。
  - **T-15**（委託資本外）：不寫；不以 CoreWeave 為主載體。
- §7-10 領域最近公開：Oracle FQ1 FY27 10-Q（申報 2026-09-11）；FY26 10-K（2026-06-22）。下一檢查點＝FQ2 FY27 10-Q（約 2026-12）。

## 1. 落差一句

ASC 606 下，客戶於交付前之大額預付若含重大融資成分，現金於收取時入**營業活動**（Oracle FQ1 FY27 現金流量表原文「Increase in deferred revenues from customer prepayments with significant financing component 11,363」，同表「Net cash provided by operating activities 23,103」）；其後交付期營收＝預付額＋按增額借款利率累積之融資增額，增額同時以利息費用列於營業利益之下（原文「We recognize interest expense related to significant financing components separately from revenue … such amounts were immaterial」）。恆等：**交付期 OCF ≈ 營收 − 預付已收部分**；**非 GAAP 營業利益含融資增額，利息費用不含**。種子主張：預付流入使當期 OCF／FCF 含類債務資金，交付期則反向（營收有、現金無），且營業利益指標含一筆以公司自身借款利率計之融資收益；若市場以 OCF 或營業利益之趨勢外推，即錯置。本卡不定方向與量級，只立可拒絕之恆等。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（現金流分類＋營收／利息拆分）；非守恆、非誘因、非負債量測時點 |
| 可見端 | 現金流量表「customer prepayments with significant financing component」行；附註「Customer Prepayments and Sales of Financing Receivables」（FY26「$ 4.6 billion」、FQ1 FY27「$ 11.4 billion」；折現率「generally consistent with our incremental borrowing rate」）；8-K「prepaid and customer supplied hardware portions … $75 billion」；Nebius 20-F 利息費用「$4.5 million of interest accretion related to the significant financing component」；CoreWeave 10-Q 利息費用含「revenue agreements with significant financing components」 |
| 指名不可見端 | 各預付合約之交付期程；累積融資增額餘額；非 GAAP 營業利益是否調整該增額 |
| 主張 | 預付占 OCF 比重高且交付期分布遠 → 未來數期 OCF 低於營收所示；可由逐季預付流入／耗用之揭露、或公司非 GAAP 現金流已剔除預付之原文拒絕 |
| 表達工具型態（只指名，不選券） | 美股上市雲供給者（Oracle 為主載體；Nebius、CoreWeave 為對照） |
| 重疊 | L13-A#1（同格不同科目）、L6-P#2（同載體不同量）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Oracle FQ1 FY27 10-Q https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm （現金流量表預付行；附註預付段——`sec.py` 本輪實讀）
2. Oracle FY26 10-K https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm （「During fiscal 2026, we received $ 4.6 billion of prepayments … No prepayments … during fiscal 2025 and 2024」——本輪實讀）
3. Oracle FY26 Q4 8-K Ex.99.1 https://www.sec.gov/Archives/edgar/data/0001341439/000119312526265848/orcl-ex99_1.htm （預付／客供 GPU「$75 billion」）
4. Nebius FY25 20-F https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/nbis-20251231x20f.htm ；CoreWeave Q2 2026 10-Q https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm （利息費用含融資成分增額——本輪實讀）
5. 測一須另取：Oracle 非 GAAP 自由現金流定義原文（新聞稿是否剔除預付）；預付對應之交付期程或耗用揭露；具名賣方／信評機構是否將預付視為類債務（Moody's／S&P 調整負債方法）；其他雲業者同類預付揭露。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 媒體已明文剔除：「Record operating cash flow of $23 billion softened the blow, but customer prepayments inflated it.」「Net of those prepayments, cash capex was $18 billion.」 | ERP Today（Radhika Ojha，2026-09-11）https://erp.today/oracle-q1-fy27-results-664b-backlog-ai-contracts/ | 已定價 |
| R2 | 第三方分析已把預付列為資本來源：「operating cash flow $23.10bn, of which $11.36bn was customer prepayments」；表列「Customer prepayments with a financing component」$16.0bn | sec-api.io Insights（2026-10-06）https://sec-api.io/insights/financial-analysis-of-oracle-q1-fy2027-cloud-backlog-capital-spending-and-scenarios-to-fy2030 | 已定價 |
| R3 | 公司揭露融資增額「immaterial」——營收／利息拆分量級可忽略 | 10-K／10-Q 原文（#1、#2） | 量級不足 |
| R4 | 預付對應 GPU 採購，現金於投資活動同期流出，淨額中性 | 8-K「customer prepaid Oracle for the purchase of the GPUs」（#3） | 恆等無錯置 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 公司自身非 GAAP 現金流或法說已剔除預付（或分開報告），且具名賣方／信評機構將其視為類債務或剔除（R1／R2 擴及主流口徑）——已定價。
(2) 融資增額占營業利益 < 1% 且依揭露之預付額與增額借款利率估算未來數期仍 < 1%（R3 成立）。
(3) 預付之耗用期程未於申報層揭露，且無法以 RPO 分段或遞延收入滾動界定交付期 OCF 之反向量（不可觀測）。
(4) 預付流入與 GPU 採購流出可於同表逐項配對且淨額近零（R4 成立，無錯置）。
(5) 可運作對照只能寫成 L13-A#1 負債時點、L4-A#2 營運資本、L6-P#2 MW 守恆或 T-15。

複查觸發器（若日後殺）：任一雲供給者預付流入連兩季占 OCF ≥ 三分之一而法說未剔除；或信評機構公布將客戶預付調入調整後負債之方法；或公司首次揭露融資增額為重大。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：現金流量表預付行；遞延收入（流動／非流動）；利息費用中之融資成分；非 GAAP 營業利益調節。
2. 可交易工具：美股雲供給者（不選券）。
3. 半衰期：預付季度揭露；交付期反向落在 RPO 13–60 月段，長於 12 個月窗。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L13［A］標「#2 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L13-A#1 之 T、L13-I、L13-P、L4-A#2、L2-A#2、L6-I#2、L6-P#2 結論；不寫 T-15。
