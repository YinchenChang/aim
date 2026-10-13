# L11-I#2 生成卡｜人類注意力：誘因（按播放占比分配之版稅池：Royalty_j ≡ Pool × s_j ／ Σs；邊際成本近零之 AI 生成曲目以占比進池，分配規則由 DSP 與權利人改寫）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/FILEIDS.tsv；archive/drive/USED_20261002_L11-I_generate_GK.md；archive/drive/USED_20261002_L11-I_test1_GK.md；work/20261013_L11-A#2_test1_CL.md | EMITS: work/20261013_L11-I#2_generate_CL.md -->
**日期：** 2026-10-13　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1→2／6）　**格：** L11-I　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L11-A#2 測一 2026-10-13，Q-0034 done）。非已殺／刻意排除且無 #2 之格中最後測試日最舊者：`archive/FILEIDS.tsv` L11-I 測一 2026-10-02T07:05Z，早於 L13-P（07:31Z）、L13-I（08:00Z）、L14-*／L15-*（10-05 起）→ **L11-I**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `royalty pool`、`AI-generated music`、`streaming royalties`，0 筆；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L11-I#1**（測一不通過，`archive/drive/USED_20261002_L11-I_test1_GK.md`）：代理議價使注意力存量轉為買方可代理之合約權利；死因＝否決 (1)：同一條款頁上「存量為權利」與「權利為合約性」兩句不可並列（OpenAI 廣告條款明文否認獨立權利）。本卡不涉代理、廣告存量或條款權利型態；對照為**分配規則**下之占比與池，兩側皆為平台／申報之數量。
  - **L11-A#1**（曝光數 × 每次曝光價）、**L11-A#2**（內容資產按觀看型態攤銷，`work/20261013_L11-A#2_test1_CL.md`）：本卡不含曝光單價或攤銷估計。
  - **L11-P**（ARCH_dead #3）：清醒秒數總量。本卡不論注意力總量；不恢復 L11-P。
  - **L10-I#2**（應用商店佣金→開發者路由）：本卡無佣金率。**L7-P#2**（內容授權給 AI 實驗室之收入）：本卡不涉訓練授權收入或和解金，只論消費端播放池之分配。**L10-A／P 系列、C-A5**：不涉。

- §7-10 領域最近公開：Deezer 2026-07（AI 曲目 >50% 每日交付，6 月均 ~90,000 首／日）；Deezer 2026-01-29（AI 曲目占總播放「up to 3%」、其中 up to 85% 判為詐欺並去貨幣化）；WMG 10-Q 季期 2026-06-30。下一檢查點＝WMG FY26 10-K（2026-11 下旬）、Spotify 3Q26 6-K（2026-11 初）、Deezer 下一次 AI 數據更新。

## 1. 落差一句

市場把「AI 生成曲目已占每日上傳 >50%」讀成對人類權利人版稅之稀釋；種子主張 pro-rata 池之分配**規則**（最低播放門檻、詐欺判定、AI 標記與推薦排除）由 DSP 與主要權利人共同設定，AI 曲目之上傳占比與其**播放占比**、更與其**可分配占比**之間有兩道規則閘——錯價只在把上傳占比當作池占比讀，或反之把規則閘當作永久。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因**：\(R_j = Pool \times s_j / \sum_k s_k\)，\(Pool\) ≈ DSP 收入 × 權利人分成；上傳者之邊際成本 → 0 ⇒ 以量進占比之誘因；DSP 與權利人之反向誘因 ⇒ 改寫 \(s\) 之計入規則（門檻、去貨幣化、推薦排除）。可觀測鏈：上傳占比 \(u\) → 播放占比 \(v\) → 可分配占比 \(v(1-d)\)，\(d\)＝去貨幣化率 |
| 選擇者 | DSP（Spotify、Deezer）之政策；主要權利人與 DSP 之授權合約（artist-centric、"artist-first framework"） |
| 可見端 | Deezer 公布之 \(u\)、\(v\)、\(d\)；Spotify 政策公告（移除數、門檻）；上市權利人 10-K／10-Q 之串流收入、風險因子原文 |
| 指名不可見端 | Spotify 之 AI 播放占比與去貨幣化率；各權利人池占比；授權合約條款 |
| 表達工具型態（只指名，不選券） | 美股可交易之串流 DSP 或錄音／詞曲版權主體。不選券 |

`[D]` 可重算對照（公開數，非測一結論）：Deezer 2025 有效可分配占比上界 ≈ 3% × (1 − 0.85) ≈ 0.45%，與上傳占比 39%（2026-01）／>50%（2026-07）差兩個數量級。**不主張稀釋方向、不主張規則持續、不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Deezer 新聞稿（2026-01-29）https://newsroom-deezer.com/2026/01/deezer-confirms-demonetization-of-ai-music/ ：「equaling roughly 39% of all music delivered every day」；「only a small share of the total streams on Deezer (up to 3%) come from AI-generated tracks」；up to 85% 判為詐欺並「excludes the streams from the royalty payments」；全 AI 曲目「automatically removed from algorithmic recommendations」「not included in editorial playlists」；「around 60,000 tracks in January 2026」。
2. RightsTech（2026-07-22）https://rightstech.com/2026/07/music-streamer-deezer-says-more-than-50-of-daily-uploads-are-ai-generated/ ：「a monthly average of 90,000 tracks per day」（2026-06）；標題 >50%。另 2026-04「44%」https://rightstech.com/2026/04/deezer-says-44-of-songs-uploaded-to-its-platform-daily-are-ai-generated/ （未開，標題）。
3. Spotify 政策（BetaNews 2025-09-26）https://betanews.com/2025/09/26/spotify-removes-75-million-spam-tracks-and-introduces-stronger-ai-rules/ ：「we've removed over 75 million spammy tracks」；「large volumes of spam threaten to dilute the royalty pool」；filter「prevent them from being recommended」。1,000 播放門檻（2024 起）：MusicTech https://musictech.com/news/industry/update-spotify-royalty-model-threshold-1000-streams/ （未開，標題）。
4. WMG 10-K FY25（期末 2025-09-30）https://www.sec.gov/Archives/edgar/data/1319161/000131916125000034/wmg-20250930.htm ：「the proliferation of such AI-generated material could lead to market saturation and a consequent devaluation of human-created music. Additionally, AI-driven streaming fraud may impact compensation for artists, songwriters and rightsholders. As a proactive measure, WMG and other major music rightsholders are collaborating with technology platforms, such as Spotify, to establish a responsible, artist-first framework」。
5. WMG 10-Q 3Q FY26（2026-06-30）https://www.sec.gov/Archives/edgar/data/1319161/000131916126000032/wmg-20260630.htm ：「Total streaming revenue increased by $135 million」；「streaming fraud」「artist-centric」0 筆，「artificial intelligence」僅前瞻聲明 1 筆。

缺段（§7-2）：Deezer 之 \(v\)、\(d\) 僅年度／不定期公布，≥ 4 期同口徑序列未確認；Spotify 不公布 AI 播放占比；Deezer 於巴黎上市（非可交易範圍），僅作觀測端；上市權利人申報未把池占比或 AI 稀釋量化。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | AI 播放占比 ≤ 3% 且多數去貨幣化；稀釋量級微小 | Deezer（§3-1） | 種子之「錯價」可能兩側皆不存在 |
| R2 | 權利人串流收入仍年增 | WMG 10-Q（§3-5） | 稀釋不可見於收入行 |
| R3 | 規則閘由 DSP 單方調整，時點不可預期 | Spotify 政策（§3-3） | 半衰期與可觀測性不足 |
| R4 | 唯一揭露 \(u, v, d\) 之 DSP 不在可交易範圍 | Deezer（巴黎） | 觀測端與表達端分離 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法就同一平台取得 ≥ 4 期同口徑之 AI 上傳占比 \(u\)、播放占比 \(v\) 與去貨幣化率 \(d\) **水準**，或無法並列一家美股可交易主體 ≥ 4 期串流收入或版稅成本序列；或
(2) 可運作對照只能寫成代理合約權利（L11-I#1）、曝光 × 單價（L11-A#1）、攤銷估計（L11-A#2）、清醒秒數（L11-P）、佣金率（L10-I#2）或 AI 訓練授權收入（L7-P#2）；或
(3) 上市權利人、DSP 或具名賣方原文已量化 AI 播放對版稅池之稀釋（已定價）；或
(4) `[D]` 有效可分配占比 \(v(1-d)\) × 池 < 美股可交易權利人最近年度串流收入 1%（量級不足）；或
(5) 12 個月內無可觀測驅動：無新增 DSP 分配規則變更、Deezer \(v\) 未升、且美股可交易主體申報無 AI 串流詐欺或稀釋之金額揭露。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：池占比與 AI 稀釋不入申報行，只能由串流收入與 DSP 揭露旁證。2. 可交易工具：DSP 與權利人方向可能相反；Deezer 不在範圍。3. 半衰期：規則閘可於一個政策公告內改寫，錯價窗 ≥ 12 個月存疑。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L11［I］格加「#2 已生成」；`AIM_FUNNEL.md` §3 一句；`query/QUEUE.md` 新列 Q-0035。不寫：ARCH_live／INDEX／ARCH_dead。不改 L11-I#1、L11-A#1／#2、L11-P、L10-I#2、L7-P#2、C-A5。
