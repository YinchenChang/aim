# L11-I#5 生成卡｜人類注意力：誘因（推薦分配者以版稅折讓出售演算法注意力：Discovery Mode 類「marketplace programs」以降低版稅換取 Radio／Autoplay／Mixes 曝光，折讓沖減版稅成本、不分列；誘因為把注意力導向折讓供給）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261002_L11-I_generate_GK.md；archive/work/20261013_L11-I#2_generate_CL.md；archive/work/20261020_L11-I#3_generate_CL.md；work/20261020_L11-I#3_test1_CL.md；archive/work/20261028_L11-I#4_generate_CL.md；work/20261028_L11-I#4_test1_CL.md | EMITS: work/20261103_L11-I#5_generate_CL.md -->
**日期：** 2026-11-03　**角色：** SCOUT@CL（排程 SCOUT-GEN，pick 配額 0→1／6）　**格：** L11-I　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L11-A#5 本日測一，Q-0158 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-28（L11-I、L13-P、L13-I、L14-P、L14-A、L14-I）；依表序取 **L11-I**（與 #3、#4 選格同一平手規則）。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `tokenomics_leads.py Spotify Discovery Mode royalty recommendation`，回傳皆模型參數／速度／價格列，相關命中 0；未用。載體全由本輪 sec.py／WebSearch／WebFetch 實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L11-I#1**（代理議價使注意力存量轉為合約權利；死因＝同一條款頁兩句不可並列）：本卡不涉代理或權利型態。
  - **L11-I#2**（pro-rata 版稅池 Pool × s／Σs，AI 曲目以占比進池；死因＝AI 占比無水準序列、可分配殘量 < 1%）：本卡非池內占比分配，而是**每串流單價之折讓換曝光**（價格歧視於供給側、以推薦位為對價）；不以 AI 生成曲目為主張。
  - **L11-I#3**（DevEx 兌現率分級；死因＝選擇變數不可分離、基期污染）：本卡選擇變數為**推薦系統之分配規則對價**（供給者自選讓利換位），非平台單方對族群定價。
  - **L11-I#4**（違規廣告主執法門檻；死因＝R_v 無可界定下界）：本卡不涉違規收入或執法。
  - **反覆死因（#2–#4）＝不可分離。** 本卡測一須**先驗 (2)**：申報層「net of certain marketplace programs」是否有任何量化或可界定上下界。
  - **L11-A#1**（曝光 × 單價）：價量只作讀數。**L10-I#2**（應用商店佣金→開發者路由）：本卡無佣金率。**L12 系列**（訴訟或有負債）：本卡不賭訴訟勝負或賠償額。**L7-P#2**（內容授權給 AI 實驗室）：不涉。**L11-P**（ARCH_dead #3）：不恢復。
- §7-10 領域最近公開：Spotify 6-K 期末 2026-09-30（申報 2026-10-22）與 3Q26 法說（2026-10-22 前後）；Capolongo v. Spotify 強制仲裁裁定（報導 2026-05-01）。

## 1. 落差一句

Spotify Premium 毛利率 3Q26 35% vs 33%（9M 同），6-K 歸因「revenue growth outpacing music royalty costs **net of certain marketplace programs**」、成本段「partially offset by benefits from certain marketplace programs」——讓利換曝光之收益以**沖減版稅成本**入帳、從未分列；Q4 指引毛利率 33.8%（+70 bps）。若推薦系統（Radio／Autoplay／Mixes 等演算法面）以版稅折讓分配注意力，則毛利擴張之一部分＝分配者出售注意力之租，其持續性取決於權利人（主要唱片公司續約條款）與外部（payola／揭露規範、訴訟）是否容許。種子主張：若市場把 Premium 毛利擴張全讀為定價與規模槓桿，錯價只在 marketplace 份額。本卡不主張方向與量級，只立可拒絕之「marketplace 份額可界定，且 12 個月內有外生改寫事件」。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因（I）**：平台同時為注意力分配者（推薦系統）與版稅付款人。Royalty ≡ Σ_j r_j·s_j，對選入方案之供給 r_j' ＝ r_j·(1 − d)，以演算法面曝光為對價；分配者之邊際誘因＝把串流導向 d > 0 之供給 |
| 驅動（因果層，§7-5） | 分配者對推薦權重之自定權；權利人之議價（續約是否限制或要求分享此類方案）；外部強制（payola／贊助揭露規範、消費者訴訟、監理） |
| 量綱 | Premium 營收、版稅成本［€／季］；毛利率［%］；d［折讓率］；s_DM［方案內串流占比］；marketplace 收益÷Premium 毛利變動［比率］ |
| 可見端 | 6-K 毛利段與成本段之「marketplace programs」歸因句（定性）；Premium／Ad-Supported 分部毛利；訴訟報導與 Spotify 回應（方案只作用於 Radio、Autoplay、certain Mixes） |
| 指名不可見端 | d 之現值（Spotify 方案頁未讀到，§3 #5）；s_DM；marketplace 收益絕對額；主要唱片公司合約中之相關條款 |
| 外部參照物（測一查證） | 廣播 payola 規範（47 U.S.C. §317／§508）之適用範圍；他串流平台同類「讓利換位」方案之存廢前例 |
| 表達工具型態（只指名，不選券） | 美股上市串流平台普通股；不選券 |
| 重疊 | L11-I#2（版稅）、L11-A#1（價量）、L12（訴訟）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Spotify 6-K（期末 2026-09-30，申報 2026-10-22；sec.py）https://www.sec.gov/Archives/edgar/data/1639920/000162828026066889/spot-20260930x6xk.htm ：毛利 Premium 1,549／1,274、Ad-Supported 90／77（€M，3Q26／3Q25）；毛利率 Premium 35%／33%、Ad-Supported 19%／18%、合併 33%／32%；Premium 成本 2,938／2,561；「partially offset by benefits from certain marketplace programs. These collectively resulted in higher content costs of €353 million」；「certain offerings within our two-sided marketplace result in advertising revenues」。全文 `payola`、`Capolongo`、`pay-for-play`、`Discovery Mode` 0 命中。
2. 3Q26 法說（Investing.com 逐字稿，2026-10-22）https://www.investing.com/news/transcripts/earnings-call-transcript-spotify-shares-jump-on-q3-2026-margin-gains-93CH-4966266 ：CFO「gross margin came in at 33% … year-over-year expansion of around 140 basis points」；Q4 毛利率指引 33.8%（+~70 bps）。已讀逐字部分 marketplace／royalty 0 處（逐字稿於約 39k／106k 字截斷，餘為摘要；測一應以 IR 原稿複核）。
3. Capolongo v. Spotify（S.D.N.Y. 1:25-cv-09216，2025-11-04 提起）：MBW 2025-11-06 https://www.musicbusinessworldwide.com/spotify-calls-payola-lawsuit-nonsense-as-class-action-targets-playlist-practices ——訴稱 Discovery Mode 為「modern payola」；Spotify：「Discovery Mode isn't used in all algorithmic playlists, or even Discover Weekly or DJ」，只作用於 Radio、Autoplay、certain Mixes。
4. DMN 2026-05-01 https://www.digitalmusicnews.com/2026/05/01/spotify-payola-lawsuit-arbitration/ ——Koeltl 法官准強制仲裁、去除集體請求、案件停止待仲裁。消費者集體訴訟管道實質關閉（外生化路徑之一已窄化）。
5. Spotify Discovery Mode 方案頁（d 現值、適用面、資格）https://support.spotify.com/us/artists/article/discovery-mode/ ——本輪 WebFetch 逾時未讀（失敗歸因：權限請求逾時；非存在性主張）。

缺段（§7-2）：d 之一手數值；marketplace 收益之任何量化（含歷年 20-F／6-K、Investor Day）；主要唱片公司 2025–2026 續約是否涉及此類方案；FTC 或其他監理之一手；具名賣方是否把 marketplace 分列入毛利模型。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | Spotify：方案只作用於部分演算法面、旗艦歌單與 AI DJ 不受影響 | #3 | 份額小到不重大 |
| R2 | 6-K 只定性列「certain marketplace programs」，與 audiobook、Partner Program 合併成 €353M 之淨增，不可拆 | #1 | 不可分離（L11-I#2–#4 型死因） |
| R3 | 方案自 2020 年起即存在、歷年申報同句，市場已知 | 歷年 6-K／20-F | 已定價 |
| R4 | 消費者集體訴訟已遭強制仲裁（2026-05），外生化事件稀少 | #4 | 窗內無檢驗事件 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 公司或具名賣方已量化 marketplace programs 對毛利之貢獻，且入 2026／2027 指引或共識——已定價（R3）。
(2) 實讀後 marketplace 收益÷Premium 毛利年變動無可界定上下界（申報層只有定性句、無 d 或 s_DM 之一手數值），使 `[D]` 份額區間寬於 [0, 50%] 之一半以上、或上界 < 10%（約 < 20 bps 毛利率）——不可分離或不重大（R1、R2）。**先驗本條。**
(3) 重定價窗（≥ 12 個月）內無可觀測之外生改寫事件（主要唱片公司續約公告觸及方案、監理或立法對推薦位贊助揭露之行動、仲裁或他訴之裁定附方案條款），或其已於窗前全部公告（R4）。
(4) 可運作對照只能寫成版稅池占比（L11-I#2 型）、曝光 × 單價（L11-A#1 型）或訴訟或有負債（L12 型）。
(5) 權利人側一手證據顯示主要唱片公司已以合約上限或分潤吸收折讓（對分配者之淨收益 ≈ 0）。
(6) 申報顯示方案收益主要以廣告收入（two-sided marketplace 之 Marquee／Showcase 類）而非版稅沖減入帳，使本卡之沖減機制非主體。

複查觸發器（若日後殺）：Spotify 首次量化 marketplace 對毛利之貢獻；主要唱片公司續約新聞稿或申報觸及推薦位讓利；FTC 或國會對串流推薦位贊助揭露立案；任一司法或仲裁裁定認定此類方案屬須揭露之贊助。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Premium cost of revenue（music royalty costs net of marketplace programs）、Premium／合併毛利率、毛利指引。
2. 可交易工具：串流平台普通股。不選券。
3. 半衰期：唱片公司合約多年期、續約不定期；監理立案不定期；季報讀數按季。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0159；`query/ARCH_matrix.md` L11［I］標「#5 已生成」；`AIM_FUNNEL.md` §3「已生成未測」。不寫入：INDEX.json、ARCH_dead、RETRIG、ARCH_live、LEADS（本輪無 AI 算力收支類新數值）。不改 L11-I#1–#4、L11-A#1–#5、L11-P、L12 系列、L10-I 系列結論；不寫 T-15。
