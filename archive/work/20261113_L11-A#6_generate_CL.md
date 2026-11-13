# L11-A#6 生成卡｜人類注意力：會計恆等（授權積壓覆蓋恆等：UGC 平台對 AI 實驗室之內容授權收入 ≡ 既有合約 RPO 之逐期轉列 ＋ 新簽／續約之增量 ＋ 非合約其他收入；現行合約期滿時 RPO 尾段遠小於收入年化值，續約價格結構〔固定費 → 用量計價〕決定其後收入）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261001_L11-A_generate_GK.md；archive/drive/USED_20261001_L11-A_test1_GK.md；archive/work/20261013_L11-A#2_generate_CL.md；work/20261013_L11-A#2_test1_CL.md；archive/work/20261020_L11-A#3_generate_CL.md；work/20261020_L11-A#3_test1_CL.md；archive/work/20261027_L11-A#4_generate_CL.md；work/20261027_L11-A#4_test1_CL.md；archive/work/20261103_L11-A#5_generate_CL.md；work/20261103_L11-A#5_test1_CL.md；archive/work/20261103_L15-A#5_generate_CL.md | EMITS: work/20261113_L11-A#6_generate_CL.md -->
**日期：** 2026-11-13　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 0→1／6）　**格：** L11-A　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。不主張價值方向。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L10-I#6 已於 2026-11-12 測）。非已殺／刻意排除格中最後測試日最舊＝2026-11-03（L11-A #5 與 L11-I #5 同日）；依表序取 **L11-A**，既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `tokenomics_leads.py Reddit licensing`＝命中 0；未用。內部研究數字（§12）：未查。
- **宿主限制（同日 `work/20261113_HEALTH_CL.md` 第 1 項）：** 本輪 `tools/sec.py filings RDDT` 被宿主隱私外掛拒絕；依 CLAUDE.md §10 不以 WebFetch 讀 sec.gov。故 §3 之申報數字均為**二手轉述**（sec-api.io 申報分析、edgar.tools 揭露頁），測一須以 sec.py 回一手；若宿主仍阻，記「無法判定（失敗歸因：宿主）」，不得記為不存在（§7-2）。
- 比對之舊檔與死因型態，本卡須異型：
  - **L11-A#1**（曝光 × 單價；死因＝價量水準不可並列）：本卡不拆價量；恆等在合約積壓（RPO）與收入之間。
  - **L11-A#2**（攤銷估計變更；死因＝驅動無可觀測證據）：本卡無管理層估計；RPO 與其認列年度為申報揭露之合約事實。
  - **L11-A#3**（消費訂閱預收遞延滯後；死因＝公司自供收斂、滯後 ≤ 4 季）：本卡非預收滯後；收入不因遞延而落後 bookings，而是以合約期限為界之**懸崖／重議價**。測一須驗公司是否已自供 2027 授權收入指引（若有 → (4)）。
  - **L11-A#4**（有限存量池一次性轉換；死因＝收斂事件 < 12 個月且前導已公開）：本卡之第一檢驗事件（現行條款期滿／續約公告）可能落在 12 個月內——測一須以 (3) 嚴格驗：續約之**價格結構**（用量計價）於其後 ≥ 12 個月之逐季兌現是否構成窗內不可消化之第二事件，否則殺。
  - **L11-A#5**（商譽減損之市值調節；死因＝收斂路徑已由公司公告）：不涉商譽與市值。
  - **L15-A#5**（消費制 ISV 對供應商之最低承諾地板）：彼為買方成本側承諾，本卡為賣方收入側積壓。**L8-A#4**（買方持有供應商股權）：不涉股權。
  - **ARCH_dead C-A4**（續約單價樞紐；(c) 工具屬性）：本卡亦涉續約，測一須先比對 C-A4 死因原文；若落差只能寫成「續約單價高或低」之單點樞紐 → 依 (5) 殺。**C-A1**（可分離性）：授權收入於申報置於「Other revenue」，測一驗其中非授權成分可否分離。**L11-P**：不恢復。
- §7-10 領域最近公開：Reddit 10-Q 期末 2026-09-30（8-K／10-Q 2026-10-29，二手轉述）；WSJ 續約報導 2026-07-22。下一檢查點＝Reddit FY26 10-K（約 2027-02，RPO 與「current terms」句更新）及任何續約 8-K／新聞稿。

## 1. 落差一句

Reddit「Other revenue（主要為內容授權）」年增逐季加速（8%→15%→24%→35%，3Q26 $48.0M，TTM $165.9M），但 2026-09-30 之 RPO 僅 $62.4M，其中 2027 年起可認列 $30.5M（2025-12-31 時為 $143.7M），10-Q 自述兩大授權方之協議「approaching the end of their respective current terms」並新增可能不續約之風險句；恆等 \(Other_{2027} ≡ RPO^{2027}_{9/30/26} + New_{2027} + NC_{2027}\) 要求 2027 授權收入中約 `[D]` 80% 以上須來自尚未簽署之續約／新約——而續約之定價結構（WSJ 轉述：管理層要「按用量計價、非固定費」）同時受 AI 答案替代所致之自身流量下滑（US DAUq −1.7%，登出 −4.2%）牽動。市場可見之加速與合約可見之覆蓋率指向不同的 2027 收入路徑；**本卡不主張方向**。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等（A）**：\(Other_t ≡ ΔRPO^{burn}_t + New_t + NC_t\)；\(RPO_{T} ≡ Σ_i TCV_i − Σ_{τ≤T} R_{i,τ}\)（固定費合約）；用量計價合約之變動對價不入 RPO（ASC 606 可變對價／按開票權宜），故結構轉換本身會使 RPO 縮小而收入不必然縮小——此為測一須拆之混淆項 |
| 驅動（因果層，§7-5） | AI 實驗室對人類討論語料之需求（訓練＋即時檢索）⇒ 授權價值↑；同一 AI 答案替代搜尋點擊 ⇒ 平台登出流量↓ ⇒ 平台議價之替代選項（封鎖存取、訴訟未授權爬取）與定價結構改變 |
| 量綱 | RPO、Other revenue［美元］；覆蓋率 c＝RPO^{next4Q}÷Other_{TTM}［無量綱］；授權占營收比［無量綱］ |
| 可見端 | 10-Q／10-K 之 Other revenue、RPO 金額與分年、遞延收入、集中度句（兩夥伴占幾乎全部授權合約價值）、「current terms」與不續約風險句；續約 8-K 或新聞稿 |
| 指名不可見端 | 各合約 TCV、起訖日、固定費 vs 用量成分、Other revenue 中非授權成分（NC） |
| 外部參照物（測一查證） | 其他 UGC／出版商與 AI 實驗室之授權合約續約前例（具名、一手公告之期限與計價結構） |
| 表達工具型態（只指名，不選券） | 美股上市 UGC／社群平台普通股；不選券 |
| 重疊 | L15-A#5（承諾地板）、L10 系列（搜尋轉介）、ARCH_dead C-A4（續約樞紐）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. sec-api.io 申報分析（2026-11-06，二手，轉述 10-Q 期末 2026-09-30）https://sec-api.io/insights/reddit-rddt-q3-2026-earnings-revenue-53-as-us-daily-users-fall-and-search-referrals-drop-sec-filing-analysis ：Other revenue 季序列 35.6／35.9／38.7／43.3／48.0（$M，3Q25–3Q26）；RPO $62.4M（$31.9M 於 2026 餘期、$30.5M 其後）；遞延收入 $38.8M；兩授權方協議「approaching the end of their respective current terms」；新增未授權爬取、AI 代理不訪站、搜尋流量下滑之風險因子；US DAUq 50.7M（3Q25 51.6M）。測一一手：https://www.sec.gov/Archives/edgar/data/0001713445/000171344526000116/rddt-20260930.htm （sec.py）。
2. edgar.tools 揭露頁（轉述 10-K FY2025）https://app.edgar.tools/companies/RDDT/disclosures/revenue ：Other revenue FY25 $140,026k vs FY24 $114,749k；RPO 2025-12-31 $143.7M（2026 $118.9M、2027 $24.8M）；遞延收入 $18.1M。
3. Quartz（約 2026-07-22，轉述 WSJ）https://qz.com/reddit-stock-google-ai-content-deal-072226 ：「That agreement is ending soon, and the two companies are in talks about potentially renewing it」；Reddit 內部討論終止 Google 之 AI 訓練存取；$60M／年（2024，轉述 CNBC）。
4. The Next Web（2026-07-23）https://thenextweb.com/news/reddit-google-ai-content-deal-publishers-traffic ：管理層「want the next deal priced by usage, not a flat fee」（轉述）；IPO 時內容合約總值 $203M。
5. Sherwood（2025-09-17，轉述 Bloomberg）https://www.sherwood.news/business/reddit-bounces-on-report-that-its-in-talks-with-google-openai-on-fresh-data ：「dynamic pricing」；Huffman「Every variable has changed since we signed those first deals.」
6. Motley Fool（2026-08-17）https://www.fool.com/investing/2026/08/17/reddits-data-revenue-openai-google-buyers/ ：Google 與 OpenAI 為兩大授權客戶；「could shrink quickly if agreements aren't renewed」。
7. 二手線索（不作證據）：FourWeekMBA「set to expire in the first half of 2027」無出處 https://fourweekmba.com/ai-reddit-ai-curse-q2-2026-earnings/ 。

缺段（§7-2）：一手 10-Q 原文（宿主阻 sec.py）；各合約起訖日與計價結構；Other revenue 中非授權成分；3Q26 法說逐字稿授權段（MarketBeat 頁抓取失敗）；具名賣方 2027 Other revenue 模型。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 授權僅占營收約 5%，無論續約與否對總收入與估值影響小 | #6（Fool：「Investors shouldn't overemphasize data-licensing growth」） | 量級不足 |
| R2 | RPO 下降只是固定費合約接近期滿之機械結果，續約談判、期滿與風險已由 WSJ 公開報導、股價當日反應（≈ −9%） | #3、#4 | 已定價 |
| R3 | 轉向用量計價使 RPO 機械性縮小而收入不縮，覆蓋率 c 低不含資訊 | §2 混淆項 | 恆等不緊 |
| R4 | 收入加速來自合約內遞增或真實用量，並無期滿懸崖 | #1 | 驅動非期限 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 一手 10-Q／10-K 無法讀得 RPO 之分年金額、Other revenue 序列或「current terms」句（含宿主阻擋而無一手替代），或 Other revenue 中非授權成分不可分離至區間寬度 < 0.5 倍中點——不可觀測／不可分離（C-A1 型）。
(2) 一手揭露顯示現行合約已含用量計價成分、且其變動對價依 ASC 606 不入 RPO，使 c 無法解讀為覆蓋率（R3）。
(3) 重定價窗（≥ 12 個月）內只有單一檢驗事件（續約公告或期滿），其後無可逐季觀測之兌現序列；或續約已於測一日前公告（已消化）。
(4) `[D]` 授權收入 2027 情境差（續約 vs 不續約，以 TTM 授權收入為上界）÷ FY2026 總營收 < 3%（R1；門檻已凍結於此）；或公司／具名賣方已明示 2027 授權收入路徑（R2）。
(5) 可運作對照只能寫成單一續約單價高低（ARCH_dead C-A4 型）、曝光 × 單價（L11-A#1 型）或預收滯後（L11-A#3 型）。
(6) 一手原文將 Other revenue 加速主因歸於非授權因素，或將續約條件主要繫於非注意力層變數（如法律和解），使因果驅動不在本層。

複查觸發器（若日後殺）：任一 UGC 平台公告與 AI 實驗室之續約並揭露期限與計價結構；Reddit 10-K 揭露各授權合約期限或用量計價成分；Reddit 公告終止任一授權方之存取。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Other revenue、RPO 分年、遞延收入、集中度與風險因子句。
2. 可交易工具：UGC／社群平台普通股。不選券。
3. 半衰期：續約公告（事件）→ 其後逐季 Other revenue 與 RPO 更新（10-Q／10-K）。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0198；`query/ARCH_matrix.md` L11［A］標「#6 已生成」；`AIM_FUNNEL.md` §3 待測格一句；`export/LEADS_算力收支.md` 2 筆（AI 內容授權收入、RPO；二手）。不寫入：INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L11-A#1–#5、L11-I#1–#5、L11-P、L15-A#5、L8-A#4、C-A1／C-A4 結論；不寫 T-15。
