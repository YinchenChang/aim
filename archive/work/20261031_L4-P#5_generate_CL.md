# L4-P#5 生成卡｜運算硬體系統：守恆（GPU-小時流量守恆／Little 定律：機櫃級 scale-up 域使單一故障之停機半徑 b 由節點擴至整域，停機在庫 GPU＝λ_g·W·b·N，交付 GPU-小時 ≠ 安裝 GPU × 時數）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260926_L4-P_generate_GK.md；archive/work/20261011_L4-P#2_generate_CL.md；archive/work/20261017_L4-P#3_generate_CL.md；archive/work/20261024_L4-P#4_generate_CL.md；work/20261024_L4-P#4_test1_CL.md；archive/work/20261014_L2-P#3_generate_CL.md | EMITS: work/20261031_L4-P#5_generate_CL.md -->
**日期：** 2026-10-31　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 6／6）　**格：** L4-P　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。各格最後測試日最舊＝2026-10-24（L4-P#4）；非已殺、非刻意排除。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py reliability failure spare goodput`，命中 1 筆（SRC_PERF_037，Llama 3 有效訓練時間比 > 90%，出處 arXiv 2407.21783）。只作「去哪找」，原文由測一實讀；不作證據、先驗或外部參照物。線索：Tokenomics SRC_PERF_037。
- 比對之舊檔與死因型態，本卡須異型：
  - L4-P#1（`archive/drive/USED_20260926_L4-P_generate_GK.md`）：SerDes 通道損耗封頂銅纜距離（介質）。本卡不涉介質選擇；銅背板只作故障源之一。
  - L4-P#2（`archive/work/20261011_L4-P#2_generate_CL.md`）：封裝供電 I²R → VPD。無供電。
  - L4-P#3（`archive/work/20261017_L4-P#3_generate_CL.md`）：位元總量之需求端分配。非頻寬。
  - L4-P#4（`archive/work/20261024_L4-P#4_generate_CL.md`；測一不通過）：Clos 埠數守恆 → 光模組條數。本卡物件為**時間域之 GPU-小時存量／流量**，非拓撲條數。
  - L2-P#3（`archive/work/20261014_L2-P#3_generate_CL.md`）：功率擺盪之設施能量平衡。本卡不涉電力。
  - ARCH_dead：N-01（機隊世代組成：新舊世代之混合比）——本卡取世代為給定，主張**同一世代內**之可用率由停機半徑決定；N-02（CPO 營收未分列）、C-I3′（UL 型）物件不同。無「故障半徑／Little 定律」型。不併。
- §7-10 領域最近公開：GMI Cloud GB200 NVL72 託管營運稿（2026-09-25）；Introl NVL72 部署稿（2026-04-15）；SemiAnalysis「H100 vs GB200 NVL72 Training Benchmarks」（2025-08-20，修改 2025-10-03；付費段未讀）；NVIDIA Multi-Node NVLink 調校指南（2025-04-21）。下一檢查點：NVIDIA 3Q FY27 10-Q（約 2026-11 下旬）、Dell／HPE／SMCI 下一季申報、ORCL 2Q FY27（約 2026-12）。

## 1. 落差一句

GPU-小時為守恆量：`安裝 GPU·時 ＝ 交付 GPU·時 ＋ 熱備 GPU·時 ＋ 停機在庫 GPU·時`，而 Little 定律給 `停機在庫 GPU ＝ λ_g × W × b × N`（λ_g 每 GPU 需維修之故障率、W 平均恢復時間、b 每次故障被移出服務之 GPU 數＝停機半徑、N 安裝數）。HGX 時代 b ≈ 8（一節點）；NVL72 域內「one failed GPU can destabilize the entire system due to NVLink topology dependencies」（Introl 2026-04-15），轉述 SemiAnalysis「the NVL72 recommends training AI on 64 GB200 GPUs and keeping 8 more in reserve」（HostZealot 2025-08-26，二手；熱備 s ≈ 8/72），GMI 轉述 CoreWeave 文件「If more than two nodes in a rack are unavailable, the whole rack is cordoned and drained for service」（b 可達 72），且 NVIDIA 指南要求更換運算 tray 時「cold rack reboot」（W 含整櫃）。**落差＝以「安裝 GPU × 單價 × 利用率」外推之交付 GPU-小時（容量、收入、每 MW 產出），與 `(1−s)(1−λ_g·W·b)` 之守恆上界是否一致**；方向不主張（b 若隨 GB300／VR200 tray 級可維護性下降，差反向收斂）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（流量／存量；Little 定律 `L＝λW`）：可用比 `a ＝ (1−s)·(1 − λ_g·W·b)`（λ_g·W·b ≪ 1 時之一階近似）；scale-up 域大小 D 上升使 b ∈ [tray GPU 數, D]，W 加上整櫃冷重啟 |
| 量綱 | λ_g［次／GPU·時］× W［時］× b［GPU／次］＝［無因次比］；s［無因次］；交付 GPU·時［GPU·時］。不以美元代 GPU·時 |
| 可見端 | Meta Llama 3：16,384 H100、54 日 419 次非預期中斷、「one failure every three hours」、GPU 30.1％＋HBM3 17.2％、有效訓練時間 > 90％（DCD 轉述 arXiv:2407.21783）；NVL72 熱備 8/72（二手）；CoreWeave 每櫃容忍 2 節點不可用、超過即整櫃排空（GMI 轉述，一手未讀）；NVIDIA 冷重啟要求 |
| 指名不可見端 | λ_g 於 GB200／GB300 之實測值；W（tray 更換、整櫃 RMA）分布；營運商實際 s；GPU-小時合約按安裝或按可用計價、SLA 抵減之落點 |
| 主張 | 交付 GPU-小時受 `a(s, λ_g, W, b)` 約束；若外推未經此式校驗，scale-up 域擴大（NVL144／NVL576）會使交付量與外推不一致 |
| 表達工具型態（只指名，不選券） | 美股上市 GPU-小時賣方（雲端／neocloud）、機櫃整合與服務合約商、加速器商普通股及上市選擇權。不選券；不寫 T-15 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| Meta「The Llama 3 Herd of Models」（λ、中斷分類、有效訓練時間） | https://arxiv.org/pdf/2407.21783 |
| DCD 轉述 Llama 3 中斷統計 | https://datacenterdynamics.com/en/news/meta-report-details-hundreds-of-gpu-and-hbm3-related-interruptions-to-llama-3-training-run |
| NVIDIA Multi-Node NVLink 調校指南（18 運算 tray／9 交換 tray；維護冷重啟） | https://docs.nvidia.com/multi-node-nvlink-systems/multi-node-tuning-guide/system.html |
| SemiAnalysis H100 vs GB200 NVL72（可靠度、perf/TCO 含停機；付費段） | https://newsletter.semianalysis.com/p/h100-vs-gb200-nvl72-training-benchmarks |
| HostZealot 轉述 64＋8 熱備（二手） | https://www.hostzealot.com/blog/news/nvidia-gb200-nvl72-is-not-yet-ready-for-training-advanced-ai-models |
| GMI Cloud 託管營運稿（停機半徑、CoreWeave 2 節點規則轉述） | https://www.gmicloud.ai/en/blog/hosted-gb200-nvl72-rack-power-cooling-operations |
| Introl NVL72 部署稿（單 GPU 失效影響、整櫃備援） | https://introl.com/blog/gb200-nvl72-deployment-72-gpu-liquid-cooled |
| CoreWeave GB200 文件（一手；本輪 fetch 被拒：權限逾時，非不存在） | https://docs.coreweave.com/docs/products/instances/gb200 |
| NVIDIA、DELL、HPE、SMCI、ORCL、NBIS 最近 10-K／10-Q／20-F 之保固、服務、可用率、SLA 段 | 測一以 `sec.py filings`／`doc --grep` 取得 |

不宣稱缺口已存在、不宣稱市場未校驗、不宣稱淨方向。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 停機已納入具名研究之 perf/TCO：「Downtime from poor reliability and lost engineering time is one of the main factors that we will capture in our perf per TCO calculations」 | SemiAnalysis 2025-08-20 | 落差已揭露（若及於容量／收入模型） |
| R2 | 量級小：Llama 3 於 H100 已維持 > 90％ 有效訓練時間；λ_g·W·b 一階項對 GPU-小時之影響可能 < 數個百分點 | arXiv:2407.21783 | 機制量級不足 |
| R3 | 暫態：軟體成熟、診斷工具改善與 GB300／後續 tray 級熱插拔使 b → tray、W 縮短；「reliability challenges are worked through」 | SemiAnalysis 同篇 | 半衰期短於 12 個月窗 |
| R4 | 損失落點不在可交易主體：GPU-小時按可用計價、SLA／保固使損失移轉至整合商或 NVIDIA，且各方不分列 | GMI 託管稿交接表（目標更換時間、現場備品、是否整櫃停機） | 表達層不可指認 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) ≥ 1 位具名賣方或產業研究機構之 GPU-小時、容量或收入模型已明示以熱備比 s 或可用率 a 校驗（非安裝數 × 利用率），或 ≥ 1 家上市 GPU-小時賣方／整合商於申報或電話會量化機櫃級可用率（R1 成立且及於單位或收入預測）。
- (2) 以一手數值代入，`b` 由 8 → 72（或 s 由 0 → 8/72）對交付 GPU-小時之變動 < 3％（門檻凍結於此），使守恆式不產生可觀測差（R2）。
- (3) ≥ 1 份一手證據（NVIDIA、OEM 或營運商）顯示 GB300 或後續世代已達 tray 級更換不停整櫃且無熱備需求，且 12 個月內為主流出貨（R3）。
- (4) λ_g、W、b、s 四者中 ≥ 3 項於機櫃級系統無公開量級（一手或具名二手），使 `[D]` 無法對帳。
- (5) 本卡只能以 N-01（世代組成）、L4-P#4（拓撲條數）、L2-P#3（功率擺盪）或 L4-A（BOM 加總）重述（重疊判讀）。
- (6) 可交易主體之相關營收或成本不分列（GPU-小時賣方不揭可用率、SLA 抵減或保固準備之 AI 系統部分），使錯價主體不可指認（N-02 型表達層；R4）。

複查觸發器（若日後殺）：營運商或 OEM 揭露機櫃級可用率、熱備比或 RMA 週期；具名賣方公開以可用率建模之 GPU-小時預測；下一代 scale-up 域（NVL144／NVL576）之可維護性規格發布；GPU-小時合約公開條款改按可用計價。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：雲端／neocloud 之 GPU 服務收入、剩餘履約義務、SLA 抵減；整合商之保固準備與服務收入；加速器商之保固與退貨準備。
2. 可交易工具：美股上市雲端、neocloud、伺服器整合商、加速器商普通股與選擇權；T-15 主體不適用（委託資本外）。
3. 半衰期：加速器世代約 1 年（GB200 → GB300 → VR200）；可維護性改善以世代計。

## 7. 本輪寫入

本卡；QUEUE 新列 Q-0140（ANALYST 測一）；ARCH_matrix L4-P 格標「#5 已生成」；FUNNEL §3。`export/LEADS_算力收支.md` 未追加（本輪新事實為可靠度轉述，Llama 3 數字與 Tokenomics SRC_PERF_037 同源，依 SCOUT.md §D 不重複寫）。不改 L4-P#1–#4、L4-A#1–#4、L4-I#1–#4、L2-P#3、N-01、N-02、C-I3′。
