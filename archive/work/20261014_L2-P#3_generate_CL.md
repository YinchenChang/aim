# L2-P#3 生成卡｜資料中心實體：守恆（訓練負載功率擺盪之設施邊界能量平衡——電網斜率／振盪上限迫使儲能或空燒）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/work/20261007_L2-P#2_generate_CL.md；work/20261007_L2-P#2_test1_CL.md；query/QUEUE.md | EMITS: work/20261014_L2-P#3_generate_CL.md -->
**日期：** 2026-10-14　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 5／6）　**格：** L2-P　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 全表已測（L15-I#2 本日測一，Q-0043 done）。所有非已殺／刻意排除之格均已有 #2；最後測一最舊者為 2026-10-07 之六格（L2-P#2／L2-A#2／L2-I#2／L8-A#2／L8-I#2／L9-A#2；git 加入時刻同為遷移批次），以 QUEUE 序取最早之 Q-0001 → **L2-P**，#3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `power smoothing`、`ride-through`、`energy storage`、`power swing`，命中 0 筆。
- 比對（本卡須異型）：
  - **L2-P#1**（PUE 受濕球封頂）：穩態能效比；本卡為**時域**能量平衡（MW/s、Hz），不是 PUE。
  - **L2-P#2**（測一不通過，`work/20261007_L2-P#2_test1_CL.md`）：每櫃 kW 受散熱介質封頂；空間密度。本卡不涉散熱介質或 kW/櫃。
  - **C-P4**（ARCH_dead #19，水約束）：不涉水。
  - **L2-A**（每 MW 建置成本）、**L2-A#2**（利息資本化）、**L2-I／L2-I#2**（許可、JV promote）：本卡之量綱為能量／功率時間導數，不是會計或誘因。
  - **L1-I#2**（大負載最低需量／擔保費率）：費率；本卡為物理約束。**L4-P#2**（封裝供電 I²R）：晶片層；本卡在設施—電網邊界。
- §7-10 領域最近公開：ERCOT NOGRR282 PUCT 核准 2026-07-09、生效 2026-08-01；NERC Level 3 Alert 2026-05-04（回覆期限 2026-08-03）；VRT／EQIX／DLR 10-Q（2026-06-30 季）。

## 1. 落差一句

能量守恆於設施邊界：`P_grid(t) = P_load(t) − P_store(t)`。同步訓練負載在數秒內於峰值與低谷間擺盪（數十至數百 MW、0.1–30 Hz），而電網端以斜率（MW/s）、振盪頻譜與穿越（ride-through）要求限制 `P_grid` 之變動；差額只有三條出路——**空燒**（GPU 功率下限，論文模擬能量開銷 10.5%）、**儲能**（`E_store ≥ ∫ΔP dt`，資本支出）、或**不交付**（降載／延後併網）。市場以「IT MW」為同質單位計容量與單價；種子主張訓練用 MW 之可用算力每電網 MW 低於穩態負載 MW，差額為 ε（空燒）或每 MW 儲能，錯價只在把兩者以同一 MW 讀。方向未定。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [P] 守恆：設施邊界能量平衡；電網斜率／振盪上限為邊界條件 |
| 量綱 | 擺幅 ΔP（MW 或 % 峰值）；頻率（Hz）；斜率上限（MW/s）；空燒開銷 ε（無量綱）；儲能（J/GPU、MWh/MW） |
| 選擇變數 | 營運商／租戶：空燒 vs 儲能 vs 降載；晶片商：PSU 內儲能與功率下限；電網：斜率、振盪、穿越規則 |
| 可見端 | NVIDIA GB300 規格；ERCOT／NERC 規則文件；儲能商案例 |
| 指名不可見端 | 營運商／REIT 申報之每 MW 儲能成本或空燒能量；租約是否依負載型態分價 |
| 表達工具型態（只指名） | 美股可交易之資料中心營運商／REIT、設施電力與儲能設備商。不選券 |

**不主張方向、不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Microsoft／OpenAI／NVIDIA，arXiv 2508.14318（2025-08-20）https://arxiv.org/html/2508.14318v1 ：「these swings can amount to tens or hundreds of megawatts」；FFT「concentrated between 0.2–3 Hz」；公用事業規格「20% of total harmonic energy」於 0.1–20 Hz；GPU 功率下限 90% TDP 時「total energy overhead of 10.5%」；儲能「does not waste energy」但成本高。
2. NVIDIA 技術部落格（2025-07-28）https://developer.nvidia.com/blog/how-new-gb300-nvl72-features-provide-steady-power-for-ai/ ：GB300 PSU「65 joules/GPU of energy storage」；電網峰值需求降「30%」；power burner 模式。
3. ERCOT NOGRR282（PUCT 2026-07-09 核准，2026-08-01 生效）https://www.ercot.com/mktrules/issues/NOGRR282 ：Large Computational Load 頻率／電壓穿越要求；數值於附件 docx（未讀）。ERCOT 說明 https://www.ercot.com/files/docs/2026/07/28/ERCOT-Trending-Topic-Ride-Through.pdf ：「multiple instances where large computational facilities were unable to ride through」；部分舊設施豁免。
4. NERC Level 3 Alert（2026-05-04；轉述 https://letsdatascience.com/news/nerc-issues-level-3-alert-on-data-center-loads-5b6e48df ）：Northern Virginia 約 1,500 MW 電壓敏感負載事件；「significant oscillations that occur in seconds」；回覆期限 2026-08-03。原文未讀。
5. Tesla，ERCOT LLWG 簡報（2025-05-16）https://www.ercot.com/files/docs/2025/05/15/11-Megapack-at-Data-Centers-_-ERCOT-LLWG_5.16.25_vShare.pdf ：「Up to 90% power demand fluctuations」；xAI「10-20 MW shifts several times per second」；「reduce 70%+ of variability」；Megapack 2 XL「2 MW / 4 MWh」。
6. 申報層（`sec.py doc --grep`）：VRT 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1674101/000162828026050609/vrt-20260630.htm 「energy storage solutions」僅產品列舉；`ride-through` 0 筆。EQIX https://www.sec.gov/Archives/edgar/data/1101239/000110123926000147/eqix-20260630.htm 、DLR https://www.sec.gov/Archives/edgar/data/1297996/000110465926089296/dlr-20260630x10q.htm 10-Q：`ride-through`／`energy storage`／`battery` 皆 0 筆（檢索失敗，非不存在）。

缺段（§7-2）：無營運商申報之每 MW 儲能成本或空燒能量；NOGRR282 數值條款未讀；NERC Alert 原文未讀；無租約依負載型態分價之原文。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 晶片層已內化：GB300 PSU 儲能＋power burner 使擺盪於機櫃內解決，成本入 GPU 價，設施 MW 仍同質 | NVIDIA（§3-2） | 機制不在 L2 |
| R2 | 10.5% 為模擬值；軟體＋儲能組合可壓至近零，ε 不構成持續楔子 | arXiv 2508.14318 自身建議（§3-1） | 量級 |
| R3 | 規則限 ERCOT 且舊設施豁免；PJM 等尚無強制 | ERCOT 說明（§3-3） | 範圍 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法就 ≥ 1 家美股上市營運商／REIT／設備商取得儲能或功率平滑之成本、容量或能量開銷之申報或電話會原文，且無法取得 ≥ 1 份電網端規則之數值條款（NOGRR282 附件、NERC Alert 原文或公用事業規格）；或
(2) 可運作對照只能寫成 PUE（L2-P#1）、每櫃 kW／介質（L2-P#2）、每 MW 建置成本（L2-A）、費率最低需量（L1-I#2）或封裝供電（L4-P#2）；或
(3) 具名賣方已量化訓練負載平滑對 MW 價值或每 MW 資本支出之影響並為市場所引用（已定價）；或
(4) `[D]` 量綱不可連接：ε 或每 MW 儲能成本 < 每 MW 全成本 5%，或 R1 成立（成本全數於晶片層吸收、設施申報無落點）；或
(5) 12 個月內無可觀測驅動：無穿越／振盪規則執行或擴及他 ISO、無新一代晶片平滑規格、無營運商儲能部署揭露。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：每 MW 資本支出、電力成本轉嫁、儲能資產。2. 可交易工具：營運商／REIT、電力與儲能設備商（不選）。3. 半衰期：規則執行期（ERCOT 2026-08 起）與晶片世代（約 1 年）。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L2［P］格加「#3 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0044。不改 L2-P#1／#2、L2-A／#2、L2-I／#2、C-P4、L1-I#2、L4-P#2 結論。
