# L10-P#4 生成卡｜分發與中介：守恆（邊緣交付位元組守恆：CDN 計費位元組 ≡ Σ_k 請求數_k × 每請求位元組_k；AI 代理／爬蟲以「請求數」占比敘事，其位元組權重受 HTML 占頁重約 1% 所限，且代理答案取代人類造訪時，同一造訪之交付位元組由整頁降為 HTML）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260930_L10-P_generate_GK.md；archive/work/20261013_L10-P#2_generate_CL.md；archive/work/20261020_L10-P#3_generate_CL.md；work/20261020_L10-P#3_test1_CL.md | EMITS: work/20261027_L10-P#4_generate_CL.md -->
**日期：** 2026-10-27　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3→4／6）　**格：** L10-P　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L7-I#4 本日測一，Q-0113 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-20（L10-P#3、L10-A#3、L10-I#3、L11-A#3、L11-I#3、L13-P#3、L13-I#3、L14-P#3）；依表序取 **L10-P**。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py crawler CDN bot Cloudflare Fastly Akamai`，命中 1（SRC_DEM_052 LMSYS 提示 token 數），與本卡無關，未用。載體全由本輪 WebSearch／WebFetch／sec.py 實讀。內部數字（§12）未取。
- 比對之舊檔與死因型態，本卡須異型：
  - **L10-P#1**（不通過）：端側能量／殼溫分流留端或回雲；死因＝功能類不可並列。本卡守恆量為**邊緣網路交付位元組**，兩端（請求數、位元組／請求）皆有公開量測。
  - **L10-P#2**（不通過，(4)）：需求通道守恆（room nights ≡ Σ 通道）→ 承接價入行銷費用率。本卡不論通道份額或獲客成本；若實讀後只能寫成「AI 通道份額 × 單價」即滑回 #2（否決 (4)）。
  - **L10-P#3**（部分通過，(2) 窗內不重大）：自駕車隊實體容量上界。本卡非車隊、非行程；死因須另驗（否決 (6)）。
  - **L10-A／#2／#3**（分潤可並列性、浮存、主事人／代理人列報）、**L10-I／#2／#3**（預設槽位、導出佣金、市集代理准入）：本卡不論列報、分潤、准入；bot 管理訂閱（Security 線）不作落差。
  - **L15-P#3**（觀測預算份額守恆）、**L15-A**（消費式計價恆等）：本卡之計價量綱為 GB／請求，非遙測量或消費單位總額。**L11-A**（曝光 × 單價）：不論廣告曝光。**L11-P**（死 #3）不恢復。
- §7-10 領域最近公開：Fastly 2Q26 10-Q（2026-08-05）；Fastly AI 流量研究（2026-06-12 報導）；Cloudflare Radar 機器人 HTML 請求過半（2026-07-09 報導）；HTTP Archive Web Almanac 2025 Page Weight。下一檢查點＝Fastly 3Q26 財報 2026-11-04 盤後。

## 1. 落差一句

恆等骨架：`B_t ≡ Σ_k R_k,t · b_k`（k ∈ 人類整頁載入、AI 爬蟲、AI 擷取／代理、無頭瀏覽器代理、API、媒體／下載）；Network Services 計費 ≈ 承諾或實用之 GB 與請求數 × 合約單價。造訪守恆：若代理答案取代 n 次人類造訪、新增 m 次代理擷取，`ΔB ≈ −n·b_page + m·b_html`。已見數點：Cloudflare Radar 機器人約占 **HTML 請求** 57.4%（非位元組）；Web Almanac 2025 中位首頁 2.56 MB（行動）／2.86 MB（桌面），HTML 中位 33／35 KB，首頁 HTML 22 KB ⇒ HTML 約占頁重 0.9–1.4%［D］，即每造訪位元組差約 75–115 倍［D］；Fastly 10-Q 自述「autonomous agent consumption is driving the bulk of internet traffic」，同份 10-Q 計費量綱為「gigabytes and requests」；Fastly 研究：AI 請求須回源 51% vs 人類 < 9%（成本端 ∝ 請求 × 未命中率）。種子主張：市場以**請求數**之 AI 占比與成長（「6.5x faster」「bulk of internet traffic」）為邊緣交付商之營收順風計價，而計費位元組由媒體與整頁主導，AI 請求之位元組權重上界約為其請求占比 × 1%；替代關係下 AI 流量對交付位元組可為負，回源成本則按請求數上升。本卡不定方向與量級，只立可拒絕之量綱鏈（§7-1）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（交付位元組 ≡ Σ 請求 × 每請求位元組；造訪守恆下之替代） |
| 量綱 | 請求［次］；位元組［GB］；每請求位元組［KB／次］；回源率［無量綱］；營收［US$／季］ |
| 可見端 | Fastly 10-Q 產品線營收（Network Services 133.9M，+17%，占 73%）與計費量綱句；Fastly／Cloudflare 以請求計之 AI 流量研究；HTTP Archive 頁重與 HTML 大小 |
| 指名不可見端 | 邊緣交付商之 GB 總量與 AI 類位元組占比；GB 費與請求費在 Network Services 之拆分；無頭瀏覽器代理（整頁渲染）占 AI 請求比 |
| 主張 | AI 流量對使用量計費交付營收之位元組加權貢獻遠小於請求占比；可由「具名者已以位元組建模」「請求費主導計費」「代理多為整頁渲染」拒絕 |
| 外部參照物（測一查證） | 行動網路／OTT 時期「請求成長 ≠ 位元流成長」之交付商前例；Akamai delivery 營收因續約降價而下滑（2Q26 10-Q） |
| 表達工具型態（只指名，不選券） | 美股上市之使用量計費邊緣交付商普通股；不選券 |
| 重疊 | L15-A（消費式計價）、L10-P#2（通道）、L11-A（曝光）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Fastly 2Q26 10-Q（sec.py）https://www.sec.gov/Archives/edgar/data/1517413/000151741326000213/fsly-20260630.htm ：「we charge fees based on their committed or actual use of our platform, as measured in gigabytes and requests」；「autonomous agent consumption is driving the bulk of internet traffic」；Network Services 133,897 vs 114,877（+17%）、Security 41,723（+43%）；Network Services 增幅「primarily driven by growth in usage from existing customers」。
2. Akamai 2Q26 10-Q（sec.py）https://www.sec.gov/Archives/edgar/data/1086222/000108622226000086/akam-20260630.htm ：delivery 營收下滑「due to downward pricing of contract renewals」；「agentic」0 筆。
3. Dan Rayburn（StreamingMediaBlog，2026-05-08）https://www.streamingmediablog.com/2026/05/wallstreet-cdn.html ：「AI agents are not watching videos … or downloading large software files」；點名 KeyBanc 之代理流量多頭觀點；Fastly 1Q26 後單日 −40%。
4. ITBrief（2026-06-12）https://itbrief.co.uk/story/ai-traffic-on-fastly-network-grows-30-in-five-months ：AI 請求 1–5 月 +30%；51% AI 請求須回源 vs 人類 < 9%；無位元組。
5. Pulse 2.0（2026-08-11）https://pulse2.com/fastly-ai-traffic-grows-6-5x-faster-than-human-traffic-as-skyfire-brings-agent-commerce-to-the-edge/ ：「6.5 times faster than human traffic」，單位未標。
6. Let's Data Science 轉述 Cloudflare Radar（2026-07-09）https://letsdatascience.com/news/bots-overtake-humans-in-web-page-requests-9abb8b52 ：機器人約 57.4% HTML 請求，「specifically about HTTP requests for HTML content」；無位元組。
7. HTTP Archive Web Almanac 2025 Page Weight https://almanac.httparchive.org/nl/2025/page-weight ：中位首頁 2.56／2.86 MB；HTML 中位 33／35 KB。
8. Benzinga（Erica Kollmann，2026-02-12）https://finviz.com/news/309688/fastly-stock-skyrockets-88-on-agentic-ai-tailwinds ：CEO「tailwind for our business with increasing agentic AI traffic」；單日 +88.61%。
9. 測一須另取：Fastly 3Q26 法說（2026-11-04）是否給 AI 位元組或 AI 歸因營收；KeyBanc／Oppenheimer／Piper Sandler 原文之代理流量建模單位；Cloudflare Radar 位元組或 content-type 分列；無頭瀏覽器代理占比一手。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | Rayburn 已公開「代理位元組極小、媒體主導位元」；1Q26 後股價 −40% | #3 | 已定價 |
| R2 | 計費含請求費；且 AI 回源 51% 使 Compute／Security 而非 GB 承接價值 | #1、#4 | 量綱鏈不適用（價值落在請求或安全訂閱） |
| R3 | 代理型瀏覽器（無頭 Chromium）整頁渲染，b_agent ≈ b_page | 測一取 | 位元組比失效 |
| R4 | AI 流量為新增而非替代人類造訪 | Fastly／Cloudflare 研究（測一取） | 造訪守恆失效 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 具名賣方／研究機構已以**位元組**（或 GB 加權）估 AI 流量對邊緣交付商營收之貢獻——已定價（R1；Rayburn 為質性，須見量化）。
(2) 一手揭露顯示請求費或非 GB 項主導 Network Services 計費，或 AI 價值主要經 Security／Compute 認列——量綱鏈不承重（R2）。
(3) 具名一手量測顯示 AI 代理請求之每請求位元組與人類整頁同量級（比 < 10 倍）——位元組比失效（R3）。
(4) 可運作對照只能寫成 L10-P#2（通道份額 × 單價）、L15-A（消費單位總額）、L11-A（曝光 × 單價）或 bot 管理訂閱。
(5) AI 類位元組占比與 GB／請求拆分皆無一手序列、亦無可替代之第三方位元組量測——不可並列（L10-P#1 死因型）。
(6) 市場與管理層皆未以 AI 請求成長歸因交付營收或估值（只歸因 Security），或 2026-11-04 單季即可全數解析——無可修正之錯價或重定價窗 < 12 個月。

複查觸發器（若日後殺）：任一交付商首揭 AI 類位元組占比或 GB／請求營收拆分；Cloudflare Radar 發布位元組或 content-type 分列之 AI 流量；具名研究以位元組量測代理流量。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Network Services 營收、使用量承諾 RPO、頻寬採購承諾、cost of revenue。
2. 可交易工具：使用量計費之邊緣交付商普通股。不選券。
3. 半衰期：季度財報與法說（下一次 2026-11-04）→ 位元組揭露（未定）。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L10［P］標「#4 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live、export/LEADS（所讀事實非 AI 算力投入／收入／硬體／雲約／資料中心）。不改 L10-P#1–#3、L10-A／#2／#3、L10-I／#2／#3、L11-P、L15 系列、C-A5 結論；不寫 T-15。
