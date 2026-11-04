# L15-P#5 生成卡｜基礎設施軟體與資料：守恆（期內伺服器元件供給守恆：AI 建置吸收記憶體與 CPU 供給，企業通用伺服器交付被價格與交期配給；以「已部署硬體」為消耗前提之混合雲／虛擬化軟體，其可消耗容量受企業端伺服器交付量約束）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；query/QUEUE.md；archive/drive/USED_20261005_L15-P_generate_GK.md；archive/work/20261014_L15-P#2_generate_CL.md；archive/work/20261021_L15-P#3_generate_CL.md；archive/work/20261029_L15-P#4_generate_CL.md；archive/work/20261022_L15-I#3_generate_CL.md；archive/work/20261013_L7-P#2_generate_CL.md | EMITS: work/20261104_L15-P#5_generate_CL.md -->
**日期：** 2026-11-04　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 0→1／6）　**格：** L15-P　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（Q-0160–Q-0164 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-29（L2-P/A/I#5、L15-P/A/I#4 同日）；同日以 QUEUE 測一序決，最早為 Q-0124 L15-P#4 → 取 **L15-P**，既有 #1–#4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `server CPU Nutanix`，命中 15 筆，皆 MLPerf GPU 推論吞吐（SRC_Perf），與企業通用伺服器無關，未用。內部數字（§12）未用。
- 比對（須異型）：
  - **L15-P#1**（分析師注意力 人×秒）：本卡守恆量為**實體伺服器元件之期內供給**，不涉人力。
  - **L15-P#2**（雲承諾池市集抵扣）：本卡不涉承諾池、市集。
  - **L15-P#3**（觀測支出占基礎設施帳單份額上限）：本卡不主張預算份額上限；約束來自硬體可得性（交期、單價），非支出慣例。若測一只能寫成「客戶把預算移往 AI」即屬預算再分配型 → 觸發 (4)。
  - **L15-P#4**（位元組單一駐留）：不涉資料格式。
  - **L15-I#3**（VMware 續約定價誘因）：本卡不以 VMware 價格或遷移誘因為落差；VMware 遷移只作需求面背景，若測一只能寫成遷移速度問題 → 觸發 (4)。
  - **L5-I#2／L5-I#3**（記憶體供給者擴產與長約誘因）：本卡位於下游軟體消耗端，不涉記憶體廠資本配置或長約保障比。
  - **L7-P#2**（公開人類文本存量）：不涉。
  - 已殺 L8-P／L9-P／L11-P、C-A1–C-A5、VEEV：不涉。
- §7-10 領域最近公開：NTNX 10-K FY26（期 2026-07-31，2026-09-18 申報）；NTNX 8-K FY26 Q4 業績（2026-08-26）；IDC 2Q26 Worldwide Server Tracker（2026-09-10）。下一檢查點＝NTNX 1Q FY27 業績與 10-Q（約 2026-11 下旬）、IDC 3Q26 tracker（約 2026-12）。

## 1. 落差一句

種子主張：同一期內記憶體、CPU 等伺服器元件之供給近似固定，AI 加速伺服器（2Q26 GPU 加速伺服器占全球伺服器營收 52.6%）以更高單價優先吸收；企業通用伺服器因此面臨漲價與交期延長（IDC：非加速伺服器 ASP 年增 33.5%）。混合雲／超融合／虛擬化軟體（指名 Nutanix）之訂閱可消耗容量以「客戶已部署之合格硬體」為前提，故其 ARR 轉營收、擴充與新落地速率受企業端伺服器交付量約束，而非受軟體需求本身約束。市場若把 ARR 成長與 VMware 遷移管線讀成軟體需求之持續轉化，則忽略：軟體與硬體在交付端守恆綁定，硬體配給期間之訂單只能以「未來起始日」或「與硬體脫鉤購買」形式記帳（NTNX FY26 Q3 起允許脫鉤購買；FY26 Q1 起 ARR 改以授權可用時點計）。可拒絕之主張＝存在可觀測序列顯示硬體配給使授權可用／部署量落後於訂單，而市場仍以訂單外推。不主張任何主體價值方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆（P）**：期內元件供給 \(Q_t = Q_t^{AI} + Q_t^{ent}\)；混合雲軟體可消耗容量 \(K_t^{sw} \le K_{t-1}^{sw} + \kappa \cdot Q_t^{ent}\)（\(\kappa\)＝每單位企業伺服器承載之授權量）；軟體營收 \(R_t \approx p \cdot K_t^{sw}\)，訂單 \(B_t\) 超過 \(p\kappa Q_t^{ent}\) 之部分只能遞延（未來起始日）或脫鉤記帳 |
| 量綱 | 授權可用量／訂單量（無因次）；伺服器 ASP 年增率、交期（週）；TB／核只作方向 |
| 選擇者 | 記憶體／CPU 供給者（配給優先序）；OEM（Dell、HPE、Lenovo、Supermicro）之企業與 AI 客群分配；企業 IT（延後專案或改脫鉤購買）；軟體商（ARR 口徑、脫鉤購買政策） |
| 可見端 | NTNX 10-K／10-Q 風險段與 MD&A 之硬體交期句；ARR 口徑變更註；RPO；IDC 季度伺服器 tracker（非加速 ASP 與單位數）；OEM 10-Q 之 ISG 傳統伺服器營收 |
| 指名不可見端 | 未來起始日訂單之金額與占比；客戶已購未部署授權量；單一客戶硬體交期 |
| 表達工具型態（只指名，不選券） | 美股混合雲／虛擬化軟體商；不選券 |
| 重疊 | L15-P#3（預算份額）；L15-I#3（VMware 續約）；L5-I 系（記憶體供給者）；L4 系（OEM） |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. NTNX 10-K FY26（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1618732/000119312526394793/ntnx-20260731.htm ：「Beginning in the latter half of the second quarter of fiscal 2026, constraints affecting the availability of certain hardware components at manufacturers became increasingly acute. These constraints have resulted in higher hardware pricing in the market and extended hardware lead times … have impacted, and may continue to impact, customers' ability to deploy and consume our software, which affects the timing of revenue recognition and cash flows」；「beginning in the third quarter of fiscal 2026, we enabled these customers to purchase our software independently of hardware delivery」；「increases in hardware platform prices … could reduce customer demand for our software if customers delay or scale back purchases of the hardware platforms」；遷移段「availability, cost and procurement lead times of server hardware」。grep `per core|GPU|memory` 0 筆。
2. NTNX 8-K Ex.99.1 FY26 Q4（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/0001618732/000117184326005752/exh_991.htm ：ARR「$2,201,672 $2,548,797」（千美元，2025-07-31／2026-07-31）；FY26 營收「$2.85 billion $2.54 billion 12%」；「Beginning with the first quarter of fiscal 2026, our methodology for calculating ARR was updated to align more closely with the timing of when licenses are made available to customers」；FY27 指引「Revenue $3.180 - $3.230 billion」。
3. IDC 2Q26 Worldwide Server Tracker（2026-09-10，Stolarski／Seminara／Fernandez）https://www.idc.com/resource-center/press-releases/2q2026-wwserver-tracker/ ：「$166.3 billion … 52.0% year-over-year increase」；「GPU-accelerated servers generated $87.4 billion (+28.1% YoY), representing 52.6% of total market revenue」；「Worldwide server unit shipments grew 15.4%」；非加速「a 16.7% increase in units」；「In the non-accelerated segment, average selling prices climbed from roughly $9,800 to nearly $13,000 (+33.5% YoY)」。
4. 具名賣方（二手轉述）：Morgan Stanley（MT Newswires，2026-02-25）https://www-web.itiger.com/news/2614745920 ：「revenue timing, higher server costs and original equipment manufacturer mix continue to limit top-line visibility」；「Servers, meanwhile, are facing higher memory costs, but Morgan Stanley said it does see meaningful pull-forward demand」。William Blair（Jason Ader，Blocks & Files 2026-08-27 轉引）https://www.blocksandfiles.com/hci/2026/08/27/nutanix-grows-despite-hardware-price-rises/5292962 ：「Continued server supply constraints, elevated lead times, and additional hardware price increases … could impact the size and timing of customer projects and/or result in a higher mix of future-start-date deals」。
5. 反向證據：TrendForce（2026-09-29，無具名作者）https://www.trendforce.com/insights/agentic-ai-cpu-gpu ：代理型 AI 使 CPU:GPU 由「1:4 to 1:8」往「1:1 and 1:2」；「Intel and AMD responded by raising prices across select CPU product lines toward the end of 1Q26」——CPU 需求擴張可同時推高企業伺服器價格（支持配給）與擴大 CPU 承載軟體之總基數（反方）。
6. 只指名未實讀：NTNX 10-Q 1Q FY27（約 2026-12 初）；Dell／HPE 10-Q 之傳統伺服器營收與交期句；Red Hat（IBM 分部）是否有同型揭露。

缺段（§7-2）：未取未來起始日訂單之任何數值；未取 NTNX 法說會逐字稿原文（僅 rallies.ai 轉述 2026-03-02 MS TMT 會議）；未取記憶體合約價外部指數；未取其他同型軟體商之同句。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 硬體交期與漲價已由公司揭露、賣方點名並入 FY27 指引保守因子 | NTNX 10-K；Morgan Stanley 2026-02；William Blair 2026-08 | 已定價（→(3)） |
| R2 | 只是時點遞延，非容量上限：脫鉤購買使 ARR／帳單照記，部署後營收補回 | NTNX 10-K「timing of revenue recognition」 | 不構成守恆約束（→(6)） |
| R3 | 非加速伺服器單位數仍 +16.7%，企業伺服器交付未減 | IDC 2Q26 | 守恆不綁定（→(1)） |
| R4 | 實為預算移往 AI（MS「some budget is reallocated to artificial intelligence」），屬預算份額型 | Morgan Stanley 2026-02 | 歸他型（→(4)） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) IDC 或 OEM 申報顯示企業／非加速伺服器單位數於 2025–2026 各季未低於趨勢（無 ≥ 2 季之交付減速或交期延長一手），致 \(Q^{ent}\) 未被配給；或
(2) NTNX 10-Q／10-K（sec.py）無可並列之數值（ARR 新舊口徑差、RPO 中未來起始部分、脫鉤購買占比、遞延營收變動）≥ 2 期，僅風險段定性句，落差不可觀測（記失敗歸因）；或
(3) 具名賣方或公司原文已就硬體配給對 ARR→營收轉換作**量化**（金額或百分點）或已明示入 FY27 指引之數值；或
(4) 可運作對照只能寫成 L15-P#3（預算份額）、L15-I#3（VMware 續約／遷移速度）或 L5-I 系（記憶體供給者誘因）；或
(5) 12 個月內無檢驗事件（NTNX 1Q–3Q FY27 業績與 10-Q、IDC 3Q26／4Q26 tracker、記憶體合約價轉向）；或
(6) 授權已購未部署之遞延量 ≤ 年營收 3%（`[D]`，由 RPO／ARR 口徑差推算），或公司原文顯示部署落後於一季內全數補回，使守恆不影響年度讀數。

複查觸發器（若日後殺）：NTNX 首次以數值揭露未來起始日訂單或脫鉤購買之占比；IDC 首次單列企業（非雲、非 AI）伺服器交期或單位數下滑；另一家以硬體部署為消耗前提之軟體商於申報中出現同句。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：ARR、RPO（含未來起始部分）、遞延營收、訂閱營收。2. 可交易工具：混合雲軟體商普通股（不選）。3. 半衰期：記憶體／CPU 供給週期；企業伺服器更新週期。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0165；`query/ARCH_matrix.md` L15［P］加「#5 已生成」；`export/LEADS_算力收支.md` 追加 2 列（IDC 2Q26 GPU 加速伺服器營收、非加速伺服器 ASP 年增）。不寫入：AIM_FUNNEL.md、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L15-P#1–#4、L15-A 系、L15-I 系、L5-I 系、L7-P#2；不碰 L1-P；不寫 T。
