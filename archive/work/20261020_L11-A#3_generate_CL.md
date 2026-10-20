# L11-A#3 生成卡｜人類注意力：會計恆等（訂閱預收遞延恆等：營收 ≡ bookings − Δ遞延收入；12 個月按比例認列使營收成長滯後 bookings 約 2–4 季，注意力〔DAU〕與付費意願〔bookings／DAU〕分岔時營收為落後量）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20261001_L11-A_generate_GK.md；archive/drive/USED_20261002_L11-I_generate_GK.md；archive/work/20261013_L11-A#2_generate_CL.md | EMITS: work/20261020_L11-A#3_generate_CL.md -->
**日期：** 2026-10-20　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 1→2／6）　**格：** L11-A　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L10-I#3 本日測一，Q-0075 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-13（L11-A、L11-I、L13-P、L13-I、L14-P、L14-A）；依表序取 **L11-A**。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `tokenomics_leads.py Duolingo deferred revenue language learning`，12 筆皆 OpenAI／ChatGPT 營收、訂閱數，與本卡載體無直接關係＝相關命中 0；未用。載體全由本輪 sec.py／WebSearch／WebFetch 實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L11-A#1**（測一不通過，`archive/drive/USED_20261001_L11-A_test1_GK.md`）：損益流量 廣告收入＝曝光 × 單價；死因＝兩因子水準不可並列。本卡為**預收存量恆等**，三項（bookings、營收、遞延收入餘額）同檔皆有水準，不含曝光或單價。
  - **L11-A#2**（測一不通過，`archive/work/20261013_L11-A#2_generate_CL.md`）：內容資產攤銷估計；死因＝(5) 增量歸組合非估計變更。本卡無會計估計，認列期為合約條款（多數 12 個月），滯後為機械。
  - **L11-I#1／#2**（條款權利型態；版稅池分配）：本卡不涉條款或分配。**L11-P**（ARCH_dead #3）：不論清醒時間總量，不恢復。
  - **L15-A#2**（遞延收入浮存之開票條件轉向，基礎設施軟體）：同屬遞延收入，但其可拒絕主張＝開票頻率改變浮存；本卡開票條件不變，主張＝消費者注意力與付費意願分岔時營收之滯後。重疊不構成丟棄。
  - **L7-P#2**（資料授權 RPO，賣方側）、**L10-A#2**（商戶預收浮存，旅遊）：不同主體與驅動。C-A5 不重開。
- §7-10 領域最近公開：Duolingo 2Q26 10-Q（申報 2026-08-06）與 8-K 股東信（2026-08）。下一檢查點＝3Q26 10-Q／股東信（約 2026-11 初）；FY27 指引（約 2027-02）。

## 1. 落差一句

Duolingo 注意力仍升（DAU 2Q26 58.7M vs 47.7M，+23%），但付費流入放緩（total bookings $289.1M vs $268.0M，+8%；bookings ÷ DAU 4.92 vs 5.62，−12%［D］），而營收因 12 個月按比例認列仍 +18%（$298.5M vs $252.3M），2Q26 bookings < 營收。恆等式 營收 ≡ bookings − Δ遞延收入（6M26 ΔDR 8,897 vs 6M25 58,293 千美元）要求未來 4 季營收成長向過去 4 季 bookings 成長收斂；種子主張：若市場或公開模型仍以營收成長（或注意力 DAU）外推 FY27，錯價只在把營收讀成當期需求量。本卡不主張方向與量級，只立可拒絕之「營收為 bookings 之落後量、FY27 營收成長上界由 2H26–1H27 bookings 決定」。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等（A）**：\(R_t ≡ B_t − ΔDR_t\)（訂閱部分）；\(DR_t ≈ Σ_{k<12m}\) 未認列預收；FY27 營收 ≈ f(2026Q2–2027Q3 bookings) |
| 驅動（因果層，§7-5） | 人類學習注意力是否付費：公司 2026 策略「prioritizing user growth」降低付費門檻；通用 LLM 家教替代付費意願（假說，測一驗） |
| 量綱 | bookings、營收、遞延收入［美元／季］；DAU［人］；bookings ÷ DAU［美元／人·季］ |
| 可見端 | 10-Q 資產負債表 Deferred revenues、現金流量表 ΔDR、MD&A bookings／DAU／paid subscribers；股東信季度與全年 bookings、營收指引 |
| 指名不可見端 | 年訂 vs 月訂組合、續訂率、家庭方案折價、bookings 中 AI 分級（Max）占比 |
| 外部參照物（測一查證） | 訂閱軟體之 billings ≈ revenue + ΔDR 前例（遞延收入分析之標準恆等）；Duolingo 自身 2022–2025 bookings 領先營收之歷史序列 |
| 表達工具型態（只指名，不選券） | 美股上市消費訂閱普通股；不選券 |
| 重疊 | L15-A#2（遞延收入）、L11-A#1（注意力貨幣化）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Duolingo 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1562088/000162828026053603/duol-20260630.htm ：「Subscription bookings $ 250,316 $ 227,259 $ 518,381 $ 459,443 Total bookings $ 289,054 $ 268,020 $ 597,538 $ 539,668」；「Deferred revenues $ 505,102 $ 496,205」（2026-06-30／2025-12-31）；現金流量「Deferred revenue 8,897 58,293」（6M26／6M25）；「we recognize subscription revenues ratably over the lifetime of a subscription, the majority of which are twelve months in duration」；DAU「58.7 million and 47.7 million … increase of 23% … driven largely by an increase in retention」；paid subscribers 12.7M vs 10.9M（+17%）；全文「ChatGPT」0 筆。
2. Duolingo 8-K 2Q26 股東信（sec.py）https://www.sec.gov/Archives/edgar/data/0001562088/000162828026053299/q2fy26duolingo6-30x26share.htm ：「10-12% year-over-year bookings growth and 15-18% year-over-year revenue growth」；Q3 2026 指引 bookings $307M（+8.9%）、營收 $302M（+11.1%）；FY26 bookings $1,285M（+10.9%）、營收 $1,207M（+16.3%）；「prioritize the first two, while working on ways to monetize that are not at odds with user growth」；無 FY27 指引。
3. 前期 10-Q（測一取 ≥ 4 季）：1Q26 https://www.sec.gov/Archives/edgar/data/1562088/000162828026029976/duol-20260331.htm ；3Q25 https://www.sec.gov/Archives/edgar/data/1562088/000162828025049743/duol-20250930.htm 。
4. TIKR（Rexielyn Diaz，2026-04-26）https://www.tikr.com/blog/duolingo-stock-is-down-41-in-2026-heres-why-investors-are-repricing-growth ：引 Reuters「expects 2026 bookings growth of about 11%」；「the market is no longer paying a premium multiple for growth without cleaner bookings visibility」；自建估值以 20% 營收 CAGR 至 2028——公開模型，非具名賣方；文內數字自相矛盾，只作線索。

缺段（§7-2）：具名賣方 FY27 營收／bookings 共識；年訂占比與續訂率；通用 LLM 語言學習功能之使用量與 Duolingo 付費轉換之任何並列資料；3Q26 實際 bookings。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 公司同時指引 bookings 與營收，Q3 營收指引已收斂至 +11.1%，恆等已由公司自供 | #2 | 已定價 |
| R2 | 市場已以 bookings 重定價（股價 2026 年大跌、「bookings visibility」） | #4 | 已定價 |
| R3 | bookings 放緩為公司刻意（減少付費提示），非注意力付費意願下降；DAU 加速可回轉為 bookings | #2 | 驅動錯置 |
| R4 | 遞延收入恆等為通用分析常識，無資訊含量 | 參照物 | 無錯價空間 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 公司指引或具名賣方已給 FY27 營收（或 bookings）且其與恆等式由 2H26 bookings 推得之上界一致——已定價（R1、R2）。
(2) 實讀 ≥ 4 季 bookings、營收、ΔDR 後，恆等之滯後不成立（營收與 bookings 成長同步、或差額由非訂閱項／一次性解釋）。
(3) 重定價窗（≥ 12 個月）內無可觀測之收斂事件（3Q26／4Q26 10-Q、FY27 指引）或其已全部於窗前公告。
(4) 可運作對照只能寫成曝光 × 價（L11-A#1）、開票條件浮存（L15-A#2）、或公司策略選擇（I 型，非恆等）。
(5) bookings ÷ DAU 下降經公司原文歸因於刻意之定價／方案調整且已量化（如 Max 功能下放之影響額），使驅動層落在公司決策而非注意力付費意願。

複查觸發器（若日後殺）：公司停止揭露 bookings 或改口徑；首次給 FY27 營收指引且高於恆等上界；10-Q 首次揭露年訂／月訂組合或續訂率；任一具名賣方以 bookings 滯後恆等建模 FY27。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Deferred revenues、ΔDR、Revenues；MD&A bookings、DAU、paid subscribers。
2. 可交易工具：消費訂閱普通股。不選券。
3. 半衰期：季度 10-Q 與股東信；12 個月認列期即滯後上限。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0076；`query/ARCH_matrix.md` L11［A］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L11-A#1／#2、L11-I#1／#2、L11-P、L15-A#2、L7-P#2、L10-A#2、C-A5 結論；不寫 T-15。
