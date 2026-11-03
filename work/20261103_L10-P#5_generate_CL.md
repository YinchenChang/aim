# L10-P#5 生成卡｜分發與中介：守恆（命名登錄世代存活守恆：.com／.net 註冊基數 `B_{t+1} ≡ B_t + N_t − D_t`，到期刪除 `D_t ≈ Σ_c N_c·(1 − f_{age(c)})`；AI 建站／編碼工具帶來之 2026 新註冊世代於 2027 首次續約，首續率 `f_1` 約 mid-40% 而續過者 mid-80%——新註冊之超額在一年後以刪除形式約半數回吐，且整體續約率分母因首續世代占比上升而被機械拉低）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260930_L10-P_generate_GK.md；archive/work/20261013_L10-P#2_generate_CL.md；archive/work/20261020_L10-P#3_generate_CL.md；archive/work/20261027_L10-P#4_generate_CL.md；work/20261027_L10-P#4_test1_CL.md；archive/work/20261028_L14-P#4_generate_CL.md | EMITS: work/20261103_L10-P#5_generate_CL.md -->
**日期：** 2026-11-03　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 2→3／6）　**格：** L10-P　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L7-I#5 本日測一，Q-0154 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-27（L10-P#4、L10-A#4、L10-I#4、L11-A#4）；依表序取 **L10-P**。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py domain registration Verisign`，命中 0。載體全由本輪 WebSearch／web-fetch 子代理／sec.py 實讀。內部數字（§12）未取。
- 比對之舊檔與死因型態，本卡須異型：
  - **L10-P#1**（不通過）：端側能量／殼溫分流；死因＝功能類不可並列。本卡守恆量為**登錄基數**，兩端（新註冊、續約率）皆季揭露。
  - **L10-P#2**（不通過，(4)）：需求通道守恆 → 承接價入行銷費用率。本卡不論通道份額或獲客成本。
  - **L10-P#3**（部分通過）：自駕車隊實體容量上界。本卡非實體容量。
  - **L10-P#4**（不通過，(1)(2)…）：CDN 位元組 ≡ 請求 × 每請求位元組。本卡非流量量綱。
  - **L14-P#4**（企業端點裝機量存量—流量，IB 固定、壽命 L 延長之遞延替換）：同為存量—流量形式，但本卡基數**非固定**、無「替換」，約束來自**世代別首續率之非均勻存活**（`f_1 ≪ f_{≥2}`），刪除為不可回補之流出，非遞延需求。若實讀後只能寫成 IB × T ÷ L 即滑回 L14-P#4（否決 (4)）。
  - **L13-A#2**（客戶預付）、**L15-A**（消費式計價恆等）、**L10-A#2**（浮存）：本卡不以遞延收入或預收為落差；遞延收入只作時序載體。**L11-A／L11-P**：不論曝光或注意力；不恢復 L11-P。
- §7-10 領域最近公開：Verisign 3Q26 10-Q 與新聞稿（2026-10-22）；Verisign 1Q26 法說（2026-04-23）、2Q26 法說（2026-07-23）；GoDaddy 3Q26 prepared remarks（2026-10-29）。.com 批發價 $10.26 → $10.97 自 2026-11-01 生效。下一檢查點＝Verisign 4Q26 財報（約 2027-02）之 3Q26 最終續約率與 2027 基數指引。

## 1. 落差一句

恆等骨架：`B_{t+1} ≡ B_t + N_t − D_t`；`D_t ≈ Σ_c N_c · (1 − f_{age(c)})`（多數為一年期，45 日寬限後刪除）；整體續約率 `r_t ≈ w_1·f_1 + (1−w_1)·f_{≥2}`，`w_1`＝當期到期中首次續約者占比。已見數點：新註冊 1Q／2Q／3Q26＝11.5／12.7／13.1M vs 1Q／2Q／3Q25＝10.1／10.4／10.6M，三季超額約 6.2M［D］；基數 182.5M（+6.1% YoY）；首續率「mid-40% range」、續過者「mid-80% range」；2Q26 最終續約率 75.2% vs 75.5%（已見下滑一格）；1Q26 76.3%（20 年高）。管理層與 10-Q 將基數成長歸因於「registrar … marketing programs, as well as the evolution of AI tools used in content and website creation」；GoDaddy 稱「AI coding tools are driving strong growth in our industry」且新世代「buy differently」並伴隨「sharper discounting … on products like domains」。種子主張：市場以 2026 基數成長（指引 3.1–4.3% → 5.2–6%）外推登錄商與登錄局之續約年金，而世代存活守恆意味 2026 新增之約半數將於 2027 首續時刪除［D：6.2M × (1 − 0.45) ≈ 3.4M，若 AI／開發者世代 `f_1` 低於歷史則更多］，`w_1` 上升使 2027 整體續約率機械下行，收入因按期認列再滯後 1–4 季。本卡不定方向與量級，只立可拒絕之量綱鏈（§7-1）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（登錄基數存量—流量；世代別存活） |
| 量綱 | 註冊數［百萬筆］；首續率 `f_1`、續過者續約率 `f_{≥2}`、整體續約率 `r`［無量綱］；首續占比 `w_1`［無量綱］；批發單價［US$／筆·年］ |
| 可見端 | Verisign 10-Q／新聞稿：季新註冊、基數、初值與最終續約率；法說：`f_1`、`f_{≥2}` 區間；遞延收入；GoDaddy 域名營收與 prepared remarks |
| 指名不可見端 | 依獲客通路（AI 建站／編碼工具 vs 行銷補貼 vs 一般）分列之 `f_1`；登錄商補貼世代之 `f_1`；多年期註冊比例 |
| 主張 | AI／補貼世代之超額新增在首續時約半數回吐，且整體 `r` 因 `w_1` 上升而下行；可由「具名者已以世代存活建模」「`f_1` 對 AI 世代顯著上升」「多年期註冊延後首續」拒絕 |
| 外部參照物（測一查證） | 2020–21 疫情註冊潮之 2021–22 首續回吐與基數轉負（Verisign 2022–23 揭露）；新 gTLD 促銷世代之首續崩落 |
| 表達工具型態（只指名，不選券） | 美股上市之域名登錄局／登錄商普通股；不選券 |
| 重疊 | L14-P#4（存量—流量）、L15-A、L13-A#2。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Verisign 3Q26 10-Q（sec.py）https://www.sec.gov/Archives/edgar/data/1014473/000101447326000039/vrsn-20260930.htm ：「Growth in the domain name base has been positively impacted by continued registrar focus on customer acquisition and engagement with our marketing programs, as well as the evolution of AI tools used in content and website creation」；遞延收入段。
2. Verisign 3Q26 新聞稿（2026-10-22）https://finviz.com/news/406822/verisign-reports-third-quarter-2026-results ：基數 182.5M、+6.1%；新註冊 13.1M vs 10.6M；2Q26 最終續約率 75.2% vs 75.5%；「Renewal rates are not fully measurable until 45 days after the end of the quarter」；風險句含「autonomous agents」。
3. Verisign 1Q26 法說（2026-04-23）https://www.fool.com/earnings/call-transcripts/2026/04/23/verisign-vrsn-q1-2026-earnings-transcript/ ：Callis「first-timer renewals are still averaging in the mid-40% range」「previously renewed names are in the mid-80% range」「a higher proportion of first-time renewing names through 2026」；Bidzos「it is difficult to really separate the two」（AI vs 行銷）。
4. Verisign 2Q26 法說摘要（MarketBeat／Nasdaq，2026-07-23）https://www.nasdaq.com/articles/verisign-q2-earnings-call-highlights ：新註冊創紀錄 12.7M；指引 5.2–6%；首續率「mid-40% area for several quarters」。
5. GoDaddy 3Q26 prepared remarks https://s23.q4cdn.com/406380394/files/content_files/GDDY-Q3-2026-Earnings-Prepared-Remarks.pdf ：「AI coding tools are driving strong growth in our industry」；「New cohorts are increasingly starting inside coding assistants, command line tools and agent interfaces, and they buy differently」；「sharper discounting across the industry on products like domains」；Airo 年化 bookings run rate 逾 $100M。
6. InsiderMonkey 轉述 MinusCherry 空方論（2025-12-04）https://finviz.com/news/246123/verisign-inc-vrsn-a-bear-case-theory ：「As these first-year promotional domains renew at lower rates … .Com domain base is expected to decline in FY2026」（未提 AI；預測 FY2026 淨負，與實際相反）。
7. PitchGrade（2026-02-22）https://pitchgrade.com/research/verisign-ai-margin-pressure ：新註冊 AI 影響「Neutral」、續約率「Slightly Negative」。
8. 測一須另取：Verisign 3Q26 法說逐字稿（`f_1` 最新值、2027 指引口徑）；4Q25 10-K 之多年期註冊與續約揭露（sec.py）；GoDaddy 10-Q（sec.py）域名續約或首年留存；具名賣方（Baird、Citi、JPMorgan、Morgan Stanley）是否以世代首續建模 2027 基數；2021–22 疫情世代回吐之 Verisign 原文。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 世代首續回吐為已知、已公開之空方論點；管理層亦預告首續占比上升 | #3、#6 | 已定價 |
| R2 | Verisign 行銷計畫設計誘導登錄商推銷「better renewal-rate characteristic」之名稱；2026 世代 `f_1` 可能高於歷史 | #3 Callis | `f_1` 假設失效 |
| R3 | AI 工具世代為真實建站（非投機／停泊），`f_1` 可高於 mid-40% | #7、#5 | 方向翻轉 |
| R4 | 多年期註冊或 11-01 漲價前提前續約改變首續時序 | 測一取 | 窗位移 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 具名賣方／研究機構已以**世代首續率 × 2026 超額新增**量化 2027 基數或續約率——已定價（R1；MinusCherry 為 2025-12 質性且未涉 AI 世代，須見量化）。
(2) 一手揭露顯示 2026 新世代 `f_1`（任一可得分列）較 2025 前世代高 ≥ 10 pp，或管理層揭露 AI 歸因世代之首續率接近 `f_{≥2}`——量綱鏈不承重（R2／R3）。
(3) `[D]` 回吐量 `ΔD ≈ ΔN_2026 × (1 − f_1)` 小於 2026 基數淨增之 25%，或多年期占比使 2027 首續到期 < 超額新增之 50%——不重大（門檻已凍結於本條）。
(4) 可運作對照只能寫成 L14-P#4（IB × T ÷ L 遞延替換）、L10-P#2（通道份額 × 單價）、L15-A（消費單位總額）或 L13-A#2（預收／遞延收入）。
(5) `f_1` 與新註冊之世代別序列皆無一手、亦無可替代之第三方量測（如 ICANN 月報、DomainTools 世代統計）——不可並列（L10-P#1 死因型）。
(6) 市場與管理層皆未以 AI 歸因或 2026 新註冊外推 2027 基數／收入，或 4Q26 財報（約 2027-02）單季即可全數解析——無可修正之錯價或重定價窗 < 12 個月。

複查觸發器（若日後殺）：Verisign 揭露依世代或依登錄商計畫分列之首續率；2027 年任一季最終續約率較前年同季下滑 ≥ 2 pp；具名研究以世代存活模型估 2027 基數。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：.com／.net 營收、遞延收入（流動／非流動）、新註冊、基數、續約率（初值／最終）。
2. 可交易工具：域名登錄局／登錄商普通股。不選券。
3. 半衰期：2026 世代首續 2027-01 起逐季到期 → 最終續約率滯後一季揭露 → 收入按期認列再滯後；全數解析約 2027-Q4／2028-02。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L10［P］標「#5 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 一列（GoDaddy Airo 年化 bookings，AI 收入）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L10-P#1–#4、L10-A#1–#4、L10-I#1–#4、L14-P#4、L13-A#2、L15 系列、L11-P、C-A5 結論；不寫 T-15。
