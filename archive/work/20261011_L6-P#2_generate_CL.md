# L6-P#2 生成卡｜雲端與基礎設施服務：守恆（RPO 交付之電力-時間預算：窗內可認列營收 ≤ ∫ 已通電 MW dt × 每 MW·時營收）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；query/CHARTER_HIST.md；archive/drive/USED_20260928_L6-P_generate_GK.md；archive/drive/USED_20260928_L6-P_test1_GK.md；archive/drive/USED_20260929_L6-P_T_GK.md；archive/work/20261011_L6-A#2_generate_CL.md；work/20261011_L6-A#2_test1_CL.md；work/20261007_L2-P#2_test1_CL.md | EMITS: work/20261011_L6-P#2_generate_CL.md -->
**日期：** 2026-10-11　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3→4／6）　**格：** L6-P　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L5-P#2 已於本日測一，Q-0022 done）。尚無 #2 且非已殺／刻意排除之格中，最後測試日最舊者並列 2026-09-29（L6-P、L6-I、L13-A 之 T）；測一日亦並列 2026-09-28（`archive/drive/USED_20260928_L6-P_test1_GK.md`、`…L6-I…`、`…L13-A…`）；再以 ARCH_matrix 列序（層序、P 先於 I）→ **L6-P**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py RPO backlog "active power" MW energized`，**命中 1 筆**（SRC_DC_014：IREN 每 IT MW 之 GPU 資本支出，2025-11-03 新聞稿）；只作「去哪找」，未取數值；本卡未以之為載體。
- 比對之舊檔與死因型態，本卡須異型：
  - **L6-P#1**（T `archive/drive/USED_20260929_L6-P_T_GK.md`）：同步作業 MTTF∝1/N、ETTR。本卡**換守恆量**：電力-時間（MW·h）為交付之容量預算，非可靠度、非作業級 ETTR。
  - **L6-I**：backlog 變厚≠對手方變好（信用／誘因）。本卡不論對手方品質，只論交付端物理上界。
  - **L6-A#2**：電費轉嫁之營收會計。本卡不論電費誰付，論 MW 是否已通電。
  - **L13-A**：入表租賃≠義務上界（未開始租約）。本卡用未交付 MW 作**交付上界**之輸入，不估義務金額。
  - **L2-P#2**（kW/櫃封頂）、**L1-I#2**（電業大負載擴建誘因）：不同守恆量與主體層。
  - **T-15**（CoreWeave 空方，委託資本外，CHARTER_HIST v0.2）：本卡不寫該表達，不以 CRWV 為唯一載體。
- §7-10 領域最近公開：Oracle FQ1 FY27 10-Q（期 2026-08-31，申報 2026-09-11）；CoreWeave Q2 2026 10-Q（期 2026-06-30）。下一檢查點＝CoreWeave Q3 10-Q（約 2026-11 中）、Oracle FQ2 FY27 10-Q（約 2026-12 中）。

## 1. 落差一句

交付雲端運算受電力-時間守恆約束：`Rev_[t,t+Δ] ≤ ρ × ∫ MW_on(τ) dτ`（ρ＝每 MW·時可認列營收）。故 RPO 認列時程隱含一條**最低通電曲線** `MW_req(Δ) ≥ RPO × f_Δ ／ (ρ × Δ)`。Oracle 原文：RPO「$ 664 billion as of August 31, 2026, of which we expect to recognize approximately 13 % as revenues over the next twelve months, 37 % over the subsequent month 13 to month 36」，同檔「megawatt」「gigawatt」0 筆。種子主張：若市場以 RPO 金額與認列百分比計量交付，而約束為 MW·時，則在 ρ 可界定時，RPO 之 13→37% 跳升需要之通電斜率可與業者揭露之 MW 交付時程（CoreWeave 原文「393 MW of electrical power remained undelivered … delivered in phases in 2026 and 2028」）對拒。本卡不定缺口方向，只立可拒絕之守恆。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（電力-時間預算；MW·h 為交付之容量積分）；非會計恆等、非誘因、非可靠度 |
| 選擇者 | 無（物理）；ρ 由合約型態決定——Oracle 原文：RPO 增量多為「large scale AI contracts where the customer prepaid Oracle for the purchase of the GPUs, or the customer bought and supplied the GPUs to Oracle」（8-K Ex.99.1，2026-06-10）→ ρ 隨「誰供 GPU」離散 |
| 可見端 | Oracle 10-Q RPO 與認列分段（0–12／13–36／37–60 月）；CoreWeave 10-Q 未交付 MW 與分期年份（「355 MW … between 2026 and 2028」；DCSP「up to 78 MW」）；CoreWeave 風險句「Limitations on generation, transmission, and distribution may limit our ability to obtain sufficient power capacity」；紐約州 50 MW 以上資料中心暫停令（2026-07，CoreWeave 10-Q 原句） |
| 指名不可見端 | Oracle 之已通電／合約 MW（10-Q 0 筆）；各業者 ρ（每 MW 營收）；RPO 對應之站點與通電日 |
| 主張 | 同一 RPO：ρ 高（業者自購 GPU）→ 所需 MW 低；ρ 低（客供 GPU）→ 所需 MW 高。守恆以 `RPO×f／ρ` 換算 MW·h，可被業者揭露之 MW 時程或 ρ 原文拒絕 |
| 表達工具型態（只指名，不選券） | 美股上市雲／AI 雲供給者（Oracle、Nebius、IREN 等）；CRWV 表達屬 T-15 委託資本外，不在本卡 |
| 重疊 | L13-A（未交付租約）、L6-I（backlog）、L1-I#2（電業）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Oracle FQ1 FY27 10-Q https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm （RPO 664B、13%／37%／34%；「megawatt」「gigawatt」0 筆——`sec.py` 本輪實讀）
2. Oracle FY26 Q4 8-K Ex.99.1 https://www.sec.gov/Archives/edgar/data/0001341439/000119312526265848/orcl-ex99_1.htm （RPO 638B；客戶預付／自供 GPU 句；「natural gas fuel cells」）
3. CoreWeave Q2 2026 10-Q https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm （未交付 393 MW／355 MW 與分期年份；「active power」「contracted power」0 筆——口徑僅在法說／投資人簡報）
4. 測一須另取：Oracle 法說原文中之 GW／站點通電時程（Abilene 等）；CoreWeave／Nebius／IREN 法說之 active vs contracted MW；具名賣方以 MW 或 GW 換算 Oracle RPO 交付之原文（候選：https://www.tikr.com/blog/how-to-value-oracles-stock-in-the-ai-era 、https://btw.media/en/oracle-database-rent-ai-infrastructure-risk ，均未讀）；任一業者每 MW 年營收（ρ）原文。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | RPO 認列分段本身即管理層對交付時程（含通電）之預期；13% 已內含電力約束 | Oracle 10-Q 原句「we expect to recognize approximately 13 %」（#1） | 已定價 |
| R2 | ρ 因客供／預付 GPU 而離散，MW 換算無單一係數 | Oracle 8-K（#2） | 守恆不可算 |
| R3 | 業者以燃料電池／自建發電繞過電網，MW 時程不受電網佇列約束 | Oracle 8-K「clean energy from natural gas fuel cells」（#2） | 約束非硬 |
| R4 | 市場與賣方早已以 GW 計量 Oracle／OpenAI 交付（Stargate 以 GW 命名） | 待測一取具名原文 | 無計量錯置 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) ρ（每 MW·時營收）無任何原文，或原文區間跨度 ≥ 3 倍（客供 vs 自購 GPU），使 `MW_req` 不可界定。
(2) 業者或具名賣方已明文以 MW／GW 換算 RPO 交付時程（R1、R4 成立）。
(3) 依可得 ρ，`MW_req(12 個月、13–36 個月)` ≤ 業者已揭露之通電／交付時程（約束不綁）。
(4) 申報層（10-K／10-Q／8-K）無任何可交易主體並列 RPO 與 MW，且無替代科目可拒絕（§7-4 財報科目題不可答）。
(5) 可運作對照只能寫成 L13-A 租賃義務、L6-I 對手方信用、L1-I#2 電業擴建或 T-15。

複查觸發器（若日後殺）：任一美股可交易雲供給者於 10-Q／10-K 同檔並列 RPO 與已通電／合約 MW；或 Oracle 首次於申報層揭露 MW／GW；或具名賣方發布 RPO→MW 換算。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：RPO 與認列分段；未交付 MW（附註）；資本支出；客戶預付（遞延收入）。
2. 可交易工具：Oracle、Nebius、IREN 美股（不選券）；CRWV 屬 T-15，不在此。
3. 半衰期：Oracle 13–36 月段為 37%，交付壓力集中於 2027-09 至 2029-08，長於 12 個月窗——測一須查是否有更早可觀測點（季度 RPO 認列實現率）。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L6［P］標「#2 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L6-P#1 之 T、L6-I、L6-A#2、L13-A、L2-P#2、L1-I#2 結論；不寫 T-15。
