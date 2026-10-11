# L5-P#2 生成卡｜儲存與 IO：守恆（快閃寫入預算：KV 快取卸載層之所需容量下界 C ≥ W·86400／DWPD，非保留容量）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260927_L5-P_generate_GK.md；archive/drive/USED_20260927_L5-P_test1_GK.md；archive/drive/USED_20260929_L5-P_T_GK.md；archive/work/20261011_L5-A#2_generate_CL.md；archive/work/20261011_L5-I#2_generate_CL.md；work/20261009_L3-P#2_test1_CL.md | EMITS: work/20261011_L5-P#2_generate_CL.md -->
**日期：** 2026-10-11　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L5-P　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L6-A#2 已於本日測一，Q-0021 done）。尚無 #2 且非已殺／刻意排除之格中，最後測試日最舊者並列 2026-09-29（L5-P、L6-P、L6-I、L13-A 之 T）；以測一日再分：L5-P 測一 2026-09-27 最舊 → **L5-P**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py KV cache SSD endurance DWPD`，**命中 14 筆**（DeepSeek 線上服務磁碟 KV 快取命中率等 SRC_PERF_041–051、SRC_MOD_009／028、SRC_DEM_048）；均為「去哪找」，未取數值；本卡載體以下列原文 fetch 為準。測一可回 DeepSeek open-infra-index 原文實讀（線索：Tokenomics SRC_PERF_044）。
- 比對之舊檔與死因型態，本卡須異型：
  - **L5-P#1**（T `archive/drive/USED_20260929_L5-P_T_GK.md`）：HBM 頻寬守恆 `decode 吞吐 ≤ BW／V_byte`。本卡**換守恆量與介質**：快閃之**寫入耐久預算**（位元組寫入總量），介質＝NAND SSD，非 HBM 頻寬、非 decode 吞吐。
  - **C-P1**（ARCH_dead #11，L5）：訓練 checkpoint 讀取占復原比。本卡為推論 KV 快取寫入，不涉 checkpoint、不涉訓練。
  - **L5-A#2**（HDD 台數×每台 TB×每 TB 價）、**L5-I#2**（NAND 供給者資本配置誘因）：本卡不主張 NAND 價格或供給，只立需求側之容量下界恆等。
  - **L3-P#2**（HBM 堆疊良率）、**L2-P#2**（kW/櫃封頂）：不同守恆量。
- §7-10 領域最近公開：StorageReview KV 卸載實測 2026-07-22；ScaleFlux KV SSD 平台 2026-07-31；Sandisk FMS 2026 預測（二手轉述）2026-08-13；Micron FY26 10-K 申報 2026-10-09。下一檢查點＝NVIDIA Inference Context Memory Storage／CMX 2H26 出貨後之業者揭露；Sandisk FQ1'27 10-Q（約 2026-11 上旬）。

## 1. 落差一句

快閃寫入耐久為守恆預算：`TBW ≡ C × DWPD × 365 × 年`。KV 快取卸載層之持續寫入率 W（B/s）因而給出容量下界 `C_min ≡ W × 86400 ／ DWPD`，與保留所需容量 `C_ret ≡ 活躍 token × B/token` 無關。實測（StorageReview 2026-07-22）：8×12.8 TB 陣列持續寫入 1.9 GB/s → RAID10 每碟約 3.2 DWPD，已超出該盤 3 DWPD 額定。種子主張：若公開之「KV 快取驅動 AI 資料中心 NAND」敘事以保留容量（每碟 TB、256 TB 盤）計量，而約束實為寫入預算，則在低 DWPD 之高容量 QLC 上 `C_min > C_ret`——所需位元數或高耐久品類組合、或更換週期，皆由 W／DWPD 決定而非 TB。本卡不定方向之大小，只立可拒絕之守恆。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（寫入耐久預算；位元組總量）；非會計恆等、非誘因、非頻寬 roofline |
| 選擇者 | 無（物理）；W 由 KV 每 token 位元組 × 卸載 token 率 × 寫入放大決定；DWPD 由 NAND 品類（SLC／TLC／QLC）與 FDP／過度配置決定 |
| 可見端 | StorageReview：「sustained writes ran 1.9GB/s」；「roughly 3.2 drive writes per day on each 12.8TB drive, slightly above the D7-PS1030's 3 DWPD sustained rating」；RAID0「about 1.6 DWPD」；FP8 每 token「roughly 124 KiB」；「the failure mode of a worn drive is recompute, not data loss」。ScaleFlux：「7 to more than 10 effective drive writes per day at five years for KV cache workloads」；KV 區塊「written frequently … These patterns increase garbage collection activity and write amplification」。NVIDIA：Inference Context Memory Storage Platform 2026-01-05 發布、「available in the second half of 2026」 |
| 指名不可見端 | 生產環境每 GPU 之 KV 層寫入率；業者 KV 層所用 NAND 品類組合；申報層 KV／推論 SSD 營收或耐久分級（Sandisk FY26 10-K「KV cache」「endurance」「inference」0 筆；Micron FY26 10-K「KV cache」0 筆，「endurance」1 筆為品類泛述） |
| 主張 | 同一 KV 工作負載：QLC 低 DWPD → `C_min` 主導，所需 TB ∝ 1／DWPD；高耐久 TLC → `C_ret` 主導。兩者以 W／DWPD 換算，可被實測拒絕 |
| 表達工具型態（只指名，不選券） | 美股可交易之 NAND／企業 SSD 供給者（Sandisk、Micron 等）。不選券 |
| 重疊 | L5-I#2（NAND 供給）、L5-P#1（HBM 頻寬）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. StorageReview（Divyansh Jain）2026-07-22 KV 卸載實測。https://www.storagereview.com/review/the-token-efficient-path-for-long-context-inference-kv-cache-offload-to-flash
2. StorageReview 2026-07-31 ScaleFlux KV SSD 平台。https://storagereview.com/news/scaleflux-kv-cache-ssd-platform-claims-7-10-dwpd-and-200-fdp-streams
3. NVIDIA 新聞稿 2026-01-05 Inference Context Memory Storage Platform。https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-BlueField-4-Powers-New-Class-of-AI-Native-Storage-Infrastructure-for-the-Next-Frontier-of-AI/default.aspx
4. Sandisk FMS 2026 預測（二手）「KV cache … 35% of all AI data center NAND flash workloads by 2030」。https://cryptobriefing.com/sandisk-kv-cache-nand-ai-data-centers/ ——測一須取 Sandisk 原簡報或法說原文
5. Sandisk FY26 10-K https://www.sec.gov/Archives/edgar/data/2023554/000162828026057406/sndk-20260703.htm ；Micron FY26 10-K https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm
6. 測一須另取：主流高容量 QLC 企業盤之 DWPD 額定原文（規格頁）；DeepSeek open-infra-index 磁碟 KV 快取統計原文；任一業者或具名賣方以 DWPD／寫入率而非 TB 估 KV 層 NAND 需求之原文。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 耐久約束已被產業明文處理（7–10 DWPD 專用盤、FDP），市場已知 | ScaleFlux（#2）；NVIDIA 與其合作「characterize how KV cache offload affects storage requirements」 | 已定價 |
| R2 | KV 層為可拋棄快取，磨損後果為重算非資料遺失；業者可接受超額定運轉或縮短壽命 | StorageReview（#1）原句 | 約束非硬 |
| R3 | DRAM／CXL 層先吸收寫入，只有逐出才落快閃；前綴快取命中降低重寫 | DeepSeek 磁碟 KV 快取命中統計（線索：Tokenomics SRC_PERF_044，待原文） | W 遠低於實驗室值 |
| R4 | 需求敘事本就以 workload 份額（非 TB）表述 | Sandisk「35% of … NAND flash workloads」（#4） | 無計量錯置 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 生產環境 KV 層寫入率 W 或其區間無任何原文（只剩單一實驗室實測），守恆之輸入不可觀測。
(2) 業者或具名賣方已明文以寫入率／DWPD（耐久預算）而非保留 TB 估算 KV 層 NAND 需求（R1、R4 成立）。
(3) 主流高容量 QLC 企業盤之額定 DWPD × 典型容量 ≥ 可得之 W 區間所需，使 `C_min ≤ C_ret`（約束不綁）。
(4) 申報層（10-K／10-Q／補充包）無任何可交易主體分列 KV／推論 SSD 或耐久品類營收，且無替代科目可拒絕（§7-4 財報科目題不可答）。
(5) 可運作對照只能寫成 NAND 價格／供給（L5-I#2）、HBM 頻寬（L5-P#1）或 checkpoint（C-P1）。

複查觸發器（若日後殺）：NVIDIA CMX／ICMS 出貨後任一業者揭露 KV 層每 GPU 寫入率或 TB；或美股可交易 NAND／SSD 供給者首次於申報層分列推論或高耐久企業 SSD。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：企業 SSD／Datacenter 營收、EB 與每 GB 營收（Sandisk 年度）、品類組合。
2. 可交易工具：Sandisk、Micron 美股（不選券）。
3. 半衰期：ICMS／CMX 2H26 出貨；耐久約束於部署後 1–2 年磨損期顯現——或長於 12 個月窗，測一須查。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L5［P］標「#2 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L5-P#1 之 T／L、L5-A#2、L5-I#2、C-P1、L3-P#2 結論。
