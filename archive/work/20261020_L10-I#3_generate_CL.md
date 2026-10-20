# L10-I#3 生成卡｜分發與中介：誘因（在位市集對第三方購物代理之准入閘：以頁面曝光變現之廣告收入，使市集在「封鎖／收費開放／自建代理」間之選擇成為誘因變數；法律封鎖工具於 2026-08 被上訴審拿掉）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；AIM_FUNNEL.md；archive/drive/USED_20261001_L10-I_generate_GK.md；archive/work/20261013_L10-I#2_generate_CL.md；work/20261013_L10-I#2_test1_CL.md；archive/work/20261020_L10-A#3_generate_CL.md | EMITS: work/20261020_L10-I#3_generate_CL.md -->
**日期：** 2026-10-20　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 0→1／6）　**格：** L10-I　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L10-A#3 本日測一，Q-0074 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-13（L10-I、L11-A、L11-I、L13-P、L13-I、L14-P、L14-A；L10-A 已於本日 #3 測一，移出）；依表序取 **L10-I**。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `tokenomics_leads.py agentic commerce shopping agent advertising`，命中 7 筆皆推論效能／代理評測／ChatGPT 搜尋次數，與本格載體無直接關係＝相關命中 0（SRC_DEM_056 ChatGPT 每週搜尋次數僅為背景，未用）。載體全由本輪 sec.py／WebSearch／WebFetch 實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L10-I#1**（測一不通過，`archive/drive/USED_20261001_L10-I_test1_GK.md`）：預設槽位由法定選擇畫面改變；死因＝轉換前結構性預設份額與轉換後選擇次數不可並列。本卡不論預設槽位；選擇者為**在位市集本身**（准入政策），其決策為離散、可具日期之事件（訴訟、API 計畫、代理收費）。
  - **L10-I#2**（測一不通過，`work/20261013_L10-I#2_test1_CL.md`）：佣金率由法院設定、開發者路由；死因＝(1) 歸因句 < 4 季、(3) 公司與具名賣方（BofA）已將節省寫成待裁定參數之敏感度。本卡無法院設定之價格參數；上訴審只移除一種法律工具（CFAA 禁制），價格（代理收費、廣告位）由市集自定。
  - **L10-A#1／#2／#3**（轉介分潤、DMB 浮存、主事人／代理人列報）：本卡非會計恆等。**L10-P#2／#3**（通道份額、車隊容量）：本卡非守恆。
  - **L11-A**（曝光 × 價，測一不通過）與 **L11-P**（死 #3，結構性不可表達）：本卡觸及「曝光」，但可拒絕之主張落在**准入決策之誘因**（誰、何時、以何價開閘），非曝光量 × 單價；若實讀後只能寫成曝光 × 價即滑入 L11-A（否決 (4)）。不恢復 L11-P。C-A5 不重開。
  - ARCH_dead／ARCH_live 無「agent」「代理准入」前例（本輪人工比對 §1／§2 列）。
- §7-10 領域最近公開：Ninth Circuit 撤銷 Amazon v. Perplexity 初步禁制令（2026-08-04，Northeast Times 2026-08-06）；Amazon 2Q26 10-Q（2026-07-31）。下一檢查點＝Amazon 3Q26 10-Q／法說（約 2026-10-29／30）；Amazon v. Perplexity 地院續審。

## 1. 落差一句

Amazon 以自家頁面曝光變現之廣告服務（2Q26 US$19,809M vs 2Q25 US$15,694M，+26.2%［D］；含 sponsored ads）依賴買方經過其排序頁；第三方購物代理直接下單即繞過該曝光。市集因此面對離散選擇：**封鎖**（2025-11 起訴 Perplexity Comet；2026-03 地院初步禁制令；2026-08 上訴審 3–0 撤銷）、**收費開放**（Jassy 2025-10：「expect, over time, to partner with third-party agents」「the right exchange of value」；2026-04 加入 UCP Tech Council；2026-06 於 ChatGPT 購買 Prime Day 廣告）、**自建代理**（Rufus、Buy for Me）。種子主張：上訴審移除法律封鎖工具後，准入政策成為由廣告誘因驅動、可具日期觀測之決策變數，其結果決定第三方代理流量以何種價格回到市集收入；本卡不主張方向（廣告增或減）與量級，只立可拒絕之「准入決策＝誘因變數」。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因（I）**：市集准入選擇 \(g\) ∈ {封鎖, 收費開放, 自建} ＝ f（每筆人類導購之廣告收入、代理流量占比、代理之議價力、法律工具可得性） |
| 選擇者 | 在位市集（Amazon）；代理方（Perplexity、OpenAI 等）是否接受識別／收費；法院（只決定封鎖工具可得性，不定價） |
| 量綱 | 廣告服務收入［美元／季］；代理導購占比、廣告收入 ÷ 線上＋第三方收入［無量綱］ |
| 可見端 | Amazon 10-Q／10-K 分列「Advertising services」；訴訟程序文件與裁定；市集代理 API／合作公告；第三方零售流量量測（AI 導流占比） |
| 指名不可見端 | 代理發起訂單占比；每筆代理訂單之廣告收入替代額；Rufus 內廣告之變現 |
| 外部參照物（測一查證） | 在位平台對中介之准入前例：Amazon Selling Partner API／Advertising API 之受控開放；Google 對比價購物之處理；航空公司 NDC 對 GDS 之收費（直連 vs 中介，具名一手） |
| 表達工具型態（只指名，不選券） | 美股上市市集普通股；不選券 |
| 重疊 | L11-A（曝光 × 價）、L12（訴訟結果）、L10-I#2（平台收費）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Amazon 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm ：「Advertising services (4) 15,694 19,809 29,615 37,052」；附註「(4) Includes sales of advertising services to sellers, vendors, publishers, authors, and others, through programs such as sponsored ads, display, and video advertising.」；全文 grep「agentic」「AI agent」「Perplexity」0 筆。
2. Amazon 10-K FY25（sec.py）https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm ：競爭段「virtual assistants, and other online and app-based means of discovering, using, or acquiring goods and services … including through artificial intelligence」；「agentic」「AI agent」0 筆。
3. Northeast Times（Maya Brooks，2026-08-06）https://northeasttimes.com/2026/08/06/appeals-court-sides-with-perplexity-ai-in-amazon-shopping-dispute/ ；Sovereign Magazine https://www.sovereignmagazine.com/article/ninth-circuit-perplexity-comet-amazon-cfaa-ruling ：第九巡迴（Smith、Tung、Hinderaker）3–0 撤銷 Chesney 法官 3 月之初步禁制令；「On the facts before us, we answer no」；不「establish a new legal regime governing agentic AI」；本案續行。
4. Modern Retail（Allison Smith，2025-10-31）https://www.modernretail.co/technology/amazon-ceo-expects-to-find-ways-to-partner-with-third-party-ai-shopping-agents-in-the-future/ ：Jassy「We're also having conversations with and expect, over time, to partner with third-party agents」「We've got to find a way to make the customer experience better and have the right exchange of value」。
5. Modern Retail（Allison Smith，2026-06-26）https://www.modernretail.co/technology/amazon-buys-ads-in-chatgpt-to-promote-prime-day/ ：Amazon 於 ChatGPT 購買 Prime Day 贊助位；Kaziukėnas「is really just a test」；Amazon 之代理限制「generally keep ChatGPT from promoting specific Amazon products」。
6. TechCrunch（Bort、Bellan，2025-11-04）https://techcrunch.com/2025/11/04/amazon-sends-legal-threats-to-perplexity-over-agentic-browsing ；Practical Ecommerce（Armando Roggio，2026-01-29）https://www.practicalecommerce.com/why-marketplaces-block-ai-shopping-agents ：Perplexity 主張封鎖為保護廣告與置入；Roggio「advertising revenue is likely a chief concern」（作者推論，非公司立場）。Amazon 公開理由＝安全、代理須自我識別。
7. ShopAppy（Ryan O'Donnell，2026-07-19）https://shopappy.com/ecommerce/amazon/amazon-external-ai-agents-2026 ：2026-04-24 Amazon 加入 UCP Tech Council；2026-05「Agentic Commerce Experiences」職缺（建第三方代理 API）；作者預測，非公司公告——只作線索。
8. Forrester（無署名部落格，最遲引 2026-03-11）https://www.forrester.com/blogs/power-couple-openai-amazon-may-have-just-won-consumer-agentic-commerce ：OpenAI–Amazon 2026-02-27 策略合作；ChatGPT Instant Checkout 2026-03-04 下架。

缺段（§7-2）：代理發起訂單或 AI 導流占零售流量之 ≥ 2 期數值（Adobe Analytics、Similarweb 等）；Amazon 3Q26 10-Q／法說是否揭露代理准入或 Rufus 廣告；具名賣方是否量化「代理繞過 sponsored ads」情境；Walmart（已與 OpenAI 合作）之 Walmart Connect 同期序列作對照。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 公司已公開表態將「partner」並求「exchange of value」，准入走向已透明 | #4 | 已定價／無錯價空間 |
| R2 | 廣告服務 +26.2%［D］，代理繞過尚無可見侵蝕 | #1 | 量級不足 |
| R3 | 代理流量極小，Instant Checkout 已下架（#8），窗內無重大流量 | #5、#8 | 不可並列（窗內） |
| R4 | 准入之實質決定在訴訟（地院續審）而非誘因 | #3 | 滑入 L12 |
| R5 | Amazon 已在代理介面內買廣告（#5），收費開放形同既成，只是曝光 × 價之延伸 | #5 | 滑入 L11-A |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 具名賣方／研究機構已公開以「第三方代理繞過 sponsored ads」或「代理准入收費」情境量化 Amazon 廣告收入（或公司指引已提供此口徑）——已定價（R1）。
(2) 實讀後無任何來源提供代理發起訂單或 AI 導流占美國電商流量之 ≥ 2 期數值；或可得數值皆 < 1% 且無上升序列——不可觀測或量級不足（R2、R3）。
(3) 至重定價窗（≥ 12 個月）內無可觀測之准入決策事件（代理 API／試點上線、代理收費條款、永久禁制或和解、Rufus 廣告變現揭露）——不可並列（R3）。
(4) 可運作對照只能寫成曝光 × 價（L11-A）、預設槽位（L10-I#1）、法定佣金路由（L10-I#2）或訴訟勝敗（L12 系列）。
(5) Amazon 10-Q／法說原文顯示自建代理（Rufus／Buy for Me）已承載廣告且其變現與頁面廣告同口徑揭露——第三方准入之誘因差已由自建路徑消化。

複查觸發器（若日後殺）：Amazon 宣布第三方代理 API／收費准入或試點；Amazon v. Perplexity 永久禁制、和解或駁回；Amazon 10-Q 首次出現「agent」相關營收或風險揭露；任一具名賣方首次以代理繞過情境模型化 Amazon 廣告。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Advertising services、Third-party seller services、Online stores；任何代理相關附註。
2. 可交易工具：市集普通股。不選券。
3. 半衰期：季度 10-Q 揭露；地院續審與代理准入公告。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0075；`query/ARCH_matrix.md` L10［I］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L10-I#1／#2、L10-A#1–#3、L10-P#1–#3、L11-A／L11-P、L12 系列、C-A5 結論；不寫 T-15。
