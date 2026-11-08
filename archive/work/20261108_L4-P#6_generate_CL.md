# L4-P#6 生成卡｜運算硬體系統：守恆（CPU—GPU 工作流量守恆：代理型工作負載之穩態 CPU 核需求 ＝ GPU token 吞吐 × 每 token 工具／編排 CPU 核·秒；「CPU:GPU 由 1:4–8 走向 1:1」為顆數比口徑，非核·秒守恆量）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260926_L4-P_generate_GK.md；archive/work/20261011_L4-P#2_generate_CL.md；archive/work/20261017_L4-P#3_generate_CL.md；archive/work/20261024_L4-P#4_generate_CL.md；archive/work/20261031_L4-P#5_generate_CL.md；archive/work/20261104_L15-P#5_generate_CL.md | EMITS: work/20261108_L4-P#6_generate_CL.md -->
**日期：** 2026-11-08　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 6／6）　**格：** L4-P　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。最後測試日最舊＝2026-10-31，L4-P#5 與 L4-A#5 同日；依表內欄序 [P] 先於 [A] 取 L4-P。非已殺、非刻意排除。既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `tokenomics_leads.py CPU agentic`，命中 2 筆（SRC_PERF_014 InferenceX GB200 agentic traces；SRC_PERF_039 ROLL Flash 框架基準）。皆 GPU 側吞吐，未用於本卡；只作測一「去哪找每 GPU token/s」之線索，須回原文實讀。內部數字（§12）未用。
- 比對之舊檔與死因型態，本卡須異型：
  - L4-P#1（GK）：SerDes 通道損耗（介質）。L4-P#2：封裝供電 I²R → VPD（密度門檻迫使技術）。L4-P#3：HBM 位元供給之分配。L4-P#4：Clos 埠數 → 光模組條數（拓撲）。L4-P#5：GPU-小時 Little 定律／停機半徑（可靠度）。本卡物件＝**異質處理器間之工作流量平衡**（CPU 核·秒 vs GPU token），非介質、供電、記憶體位元、拓撲或可用率。
  - L15-P#5（`archive/work/20261104_L15-P#5_generate_CL.md`）：元件供給配給 → 企業伺服器與混合雲軟體；CPU:GPU 比只作其反向證據。本卡為**需求端**之導出式，不涉供給配給與軟體。
  - L3-P#5（老化熱量）、L2-P#2（散熱介質）：不涉熱。
  - ARCH_dead：N-01（機隊世代組成）、N-02（CPO 未分列）、C-I3′（UL 型）物件不同；C-P1（checkpoint 儲存）不同層。無「CPU—GPU 流量平衡」型。不併。
- §7-10 領域最近公開：Futurum「AMD Q3 FY 2026」（2026-11-05，轉述 AMD 伺服器 CPU 市場口徑上修）；AMD 部落格（2026-05-07）；Tom's Hardware 轉述 Intel（2026-04-24）；TrendForce（2026-04-14，修 04-23）；arXiv:2511.00739 v3（2026-04-16）。下一檢查點：Intel／AMD 4Q26 業績（約 2027-01 下旬至 02 初）、NVIDIA 3Q FY27（約 2026-11 下旬）、Arm FQ3 FY27（約 2027-02）。

## 1. 落差一句

穩態下 GPU 不閒置之條件為 CPU 側流量 ≥ GPU 側導出之 CPU 工作：`N_core × u_cpu ≥ N_gpu × τ × u_gpu × c`（τ 每 GPU 每秒 token、c 每 token 之工具執行／沙箱／編排／檢索 CPU 核·秒、u 利用率）；所需**核數**比 `N_core/N_gpu ＝ τ·u_gpu·c / u_cpu` 由 c 之工作負載分布決定。公開層以**顆數比**敘述：AMD「Instead of the previous 1:4-8 CPU-to-GPU ratio with chatbot AI, we are seeing agentic AI moving toward a 1:1 ratio」（2026-05-07）、Intel「could reach 1:1」（Tom's Hardware 轉述，2026-04-24）、TrendForce「toward 1:1–1:2」、Arm「120 million CPU cores per GW」（TrendForce 轉述，二手）；並據此上修伺服器 CPU 市場（AMD：> 35%／年至 2030 年逾 1,200 億美元；Futurum 2026-11-05 轉述上修為約 50%／年、約 2,200 億美元）。而唯一具名量測（arXiv:2511.00739，Georgia Tech／Intel）顯示 CPU 占端到端延遲依負載自 ~12%（Toolformer）至「up to 88%」（工具主導）——**c 跨負載差逾一個數量級**，且延遲占比 ≠ 核·秒需求（批次、重疊與 τ 決定後者）。**落差＝以顆數比 × GPU 出貨外推之 CPU 顆數／核數，與 `τ·c` 守恆式在實際負載組合下導出之核·秒需求是否一致**；方向不主張（c 上升、每顆核數增加、GPU τ 提升三者方向不同）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（多段管線之流量平衡；穩態下各段處理率相等，瓶頸段決定整體）：`Σ_w s_w·τ_w·c_w ≤ N_core·u_cpu / (N_gpu·u_gpu)`，w 為負載類別、s_w 為 GPU 時間占比 |
| 量綱 | τ［token／GPU·s］× c［核·s／token］＝［核／GPU］；顆數比需再除以每顆核數 k［核／顆］。不以美元代核·秒 |
| 可見端 | 顆數比主張（AMD、Intel、TrendForce）；Arm 每 GW 核數（二手）；arXiv:2511.00739 之分負載 CPU 延遲占比與硬體（64 核 GNR＋RTX Pro 6000；72 核 Grace＋H200）；AMD／Futurum 伺服器 CPU 市場口徑 |
| 指名不可見端 | 生產環境之負載組合 s_w；每 token 之工具呼叫頻率與每次 CPU 核·秒；CPU 是否與 GPU 同機櫃（head node）或獨立沙箱機群；每顆核數 k 之世代上升（如 192／288 核）對顆數比之稀釋 |
| 主張 | 伺服器 CPU 需求受 `τ·c` 約束；若外推以顆數比而非核·秒，k 上升或負載組合偏推論／聊天時，顆數外推與守恆式不一致；反之 c 高之負載（沙箱、RL rollout）擴大時外推偏低 |
| 表達工具型態（只指名，不選券） | 美股上市伺服器 CPU 商、Arm 架構授權商、伺服器整機商普通股及上市選擇權。不選券；不寫 T-15 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| arXiv:2511.00739 v3「Towards Understanding, Analyzing, and Optimizing Agentic AI Execution: A CPU-Centric Perspective」（分負載延遲占比、COMB 批次上限、能耗；後半未逐字讀） | https://arxiv.org/abs/2511.00739 |
| AMD 部落格「Agentic AI Changes the CPU/GPU Equation」（顆數比、TAM） | https://www.amd.com/en/blogs/2026/agentic-ai-changes-the-cpu-gpu-equation.html |
| TrendForce「The Great Rebalance」（1:1–1:2 預測；Arm 每 GW 核數轉述；「up to 90.6%」與 arXiv 讀得之 88% 不符，待測一核對） | https://insights.trendforce.com/p/agentic-ai-cpu-gpu |
| Tom's Hardware 轉述 Intel 比率與 CPU 漲價 | https://www.tomshardware.com/pc-components/cpus/shifting-need-for-cpus-in-ai-workloads-drives-intensifying-shortages-price-hikes |
| Futurum「AMD Q3 FY 2026」（伺服器 CPU 市場上修，二手；與 05-07 口徑衝突） | https://futurumgroup.com/insights/amd-q3-fy-2026-a-2x-server-outlook-positions-amd-to-outgrow-the-ai-market/ |
| AMD、INTC、NVDA、ARM 最近 10-K／10-Q／20-F 與 8-K 業績稿之伺服器 CPU 分列、單位、ASP、核數 | 測一以 `sec.py filings`／`doc --grep` 取得 |

不宣稱缺口已存在、不宣稱市場未校驗、不宣稱淨方向。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 顆數比只是溝通口徑，賣方與 CPU 商內部模型已以核數或每 GW 核數建模（Arm「cores per GW」即核口徑） | TrendForce 轉述 Arm（2026-04） | 落差已揭露 |
| R2 | 需求證據不靠比率：Intel／AMD 已實現 CPU 漲價與缺貨（「server CPU prices have risen 10% to 20% since March」），出貨受供給約束，守恆式不改短窗可見量 | Tom's Hardware 2026-04-24 | 機制無可觀測差 |
| R3 | c 之分布雖寬，但工具主導負載（「up to 88%」）正是代理型主流，加權後與 1:1 量級相符 | arXiv:2511.00739 | 量級吻合 |
| R4 | 伺服器 CPU 收入不分 AI head node／沙箱／通用，錯價主體不可指認（N-02 型） | AMD／Intel 分部口徑（資料中心分部含 GPU） | 表達層 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) ≥ 1 位具名賣方、產業研究機構或 CPU 商之 CPU 需求模型已明示以核數或核·秒（每 GPU 或每 GW）建模並列出負載組合（R1 成立且及於單位或收入預測）。
- (2) 以一手數值代入（τ 取公開推論基準、c 取 arXiv:2511.00739 或其他一手量測），`[D]` 加權所需核／GPU 落於顆數比 1:1 × 當代每顆核數之 ±50% 內（門檻凍結於此），使守恆式與顆數外推無可觀測差（R3）。
- (3) τ、c、s_w、k 四者中 ≥ 3 項無公開量級（一手或具名二手），使 `[D]` 無法對帳（§7-2：記失敗歸因，不作存在性主張）。
- (4) 本卡只能以 L15-P#5（元件供給配給）、L4-P#3（記憶體位元分配）、N-01（世代組成）或 L4-A 系（會計口徑）重述（重疊判讀）。
- (5) 上市 CPU 商之伺服器 CPU 收入或單位不分列（含於含 GPU 之資料中心分部且無單位／ASP 揭露），使錯價主體不可指認（N-02 型；R4）。
- (6) 12 個月內 CPU 出貨受供給封頂之一手證據（交期、配貨、價格）足以使需求端守恆式不改可觀測量（R2）。

複查觸發器（若日後殺）：CPU 商或雲端商揭露每 GPU 之 CPU 核數或 head node／沙箱 CPU 機群規模；具名研究公開分負載之每 token CPU 核·秒；CPU 商分部首次分列 AI 相關伺服器 CPU 單位或收入；顆數比口徑被正式改為核數口徑。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：伺服器 CPU 收入、單位、ASP（若分列）；資料中心分部；授權與權利金（Arm 架構）。
2. 可交易工具：美股上市 CPU 商、Arm 架構授權商、伺服器整機商普通股與選擇權；T-15 主體不適用。
3. 半衰期：伺服器 CPU 世代約 12–18 個月（每顆核數上升）；代理型負載組合變動以季計。

## 7. 本輪寫入

本卡；QUEUE 新列 Q-0181（ANALYST 測一）；ARCH_matrix L4-P 格標「#6 已生成」；FUNNEL §3。`export/LEADS_算力收支.md` 追加 1 筆（AMD 伺服器 CPU 市場口徑，一手利害方）；Futurum 上修口徑為二手且未經 AMD 原文核對，不寫。不改 L4-P#1–#5、L4-A#1–#5、L4-I#1–#5、L15-P#5、N-01、N-02、C-I3′。
