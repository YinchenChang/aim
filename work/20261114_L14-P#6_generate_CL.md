# L14-P#6 生成卡｜企業終端需求：守恆（企業 AI 專案漏斗之件數守恆：`N_{t-1} + new_t = conv_t + drop_t + N_t`——每一筆生產部署必先經過試點；試點存量之流出只有「轉生產」與「放棄」兩口，生產端新增受「試點存量 × 轉換率」上界約束）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261005_L14-P_generate_GK.md；archive/work/20261013_L14-P#2_generate_CL.md；archive/work/20261020_L14-P#3_generate_CL.md；archive/work/20261028_L14-P#4_generate_CL.md；archive/work/20261104_L14-P#5_generate_CL.md；work/20261104_L14-P#5_test1_CL.md | EMITS: work/20261114_L14-P#6_generate_CL.md -->
**日期：** 2026-11-14　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 5→6／6）　**格：** L14-P　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L13-I#6 本日測一，Q-0202 done）。非已殺／刻意排除格中最後測試日最舊＝2026-11-04（L14-P#5、L14-A#5、L14-I#5、L15-P#5）；依表序取 **L14-P**。既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `pilot production enterprise adoption`，命中 3 筆（SRC_DEM_020／045／049，皆 ChatGPT 用戶與訊息量），與專案漏斗無關，相關命中 0；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L14-P#1**（席次 ≤ 員工數、工時上限）：不涉席次、員工、工時。
  - **L14-P#2**（預付容量承諾池，美元／credit）：本卡守恆量為**專案件數**，非合約美元池；ARR 只作生產端旁證。
  - **L14-P#3**（客服人工處理量 H ≡ V(1−a)）：不涉人工處理量。
  - **L14-P#4**（端點裝機量存量—流量；死因＝D_t 為負／前拉）：本卡亦為存量—流量，但對象為**狀態轉移漏斗**（試點 → 生產／放棄），非實體裝機之跨期替換；不以壽命、機齡為樞紐。
  - **L14-P#5**（企業推論工作量跨場所分配 W_pub＋W_priv）：本卡不涉放置場所與工作量。
  - **L14-A／#2–#5**（支出比重、會計分流）、**L14-I／#2–#5**（採購、揭露誘因）：揭露口徑變動只列為可觀測性風險（否決 (1)），不作樞紐。
  - **C-A2**（ARCH_dead，企業預算單位經濟）：不主張每單位毛利。**L11-P／L8-P／L9-P**：不恢復。不寫 T。
- §7-10 領域最近公開：Salesforce Q2 FY27 新聞稿（期末 2026-07-31，2026-08-26）；C3.ai Q3 FY26 IPD 數（Zacks 2026-03-18 轉述）；Gartner／Forrester 轉述（TNW 2026-07-28）。下一檢查點＝Salesforce Q3 FY27（約 2026-12 初）、C3.ai Q2 FY27（約 2026-12）、ServiceNow 4Q26（2027-01）。
- 宿主：`tools/sec.py` 本輪被執行宿主之隱私外掛拒絕（同 `work/20261114_HEALTH_CL.md` 第 1 項），本卡未實讀 EDGAR；載體以公司新聞稿與二手報導指名，測一須回 10-Q／10-K 原文。

## 1. 落差一句

市場把企業 AI 之「簽約／試點」計數（Salesforce FY26 Q3「over 18,500 Agentforce deals since launch; over 9,500 paid deals」；C3.ai 累計 IPD 408）讀成即將轉化之生產需求；種子主張：生產部署之每一筆新增必來自試點存量之流出，`conv_t ≤ N_{t-1} + new_t − drop_t − N_t`，而第三方調查之放棄率（S&P Global：平均「scrapped 46% of AI proof-of-concepts before they reached production」）意味生產端新增之上界遠低於簽約計數之外推。可拒絕之主張＝(i) 至少一家供應商可逐期解出 conv_t 與 drop_t（或其和）≥ 3 期；(ii) 簽約計數之外推與該上界之差，在具名賣方生產端模型中可見；若轉換率接近 1、或揭露已改為不可分之 ARR（市場不再用件數），本卡死。本卡不主張任何公司營收或股價方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆（P）**：件數守恆 `N_t = N_{t-1} + new_t − conv_t − drop_t`；累計 `C_t = C_{t-1} + new_t`；`exit_t ≡ conv_t + drop_t = (C_t − C_{t-1}) − (N_t − N_{t-1})`。生產端新增 `ΔP_t ≥ conv_t`（另含直接生產簽約，須分列） |
| 選擇者 | 企業買方（續行／放棄試點之決策） |
| 驅動（因果層，§7-5） | 試點 ROI 之可證性、資料就緒度（Gartner：無 AI-ready data 之專案 60% 放棄）、供應商資格審查（C3.ai 收緊試點條件） |
| 量綱 | 件／期；無因次轉換率 `q ≡ conv/exit`；美元只作生產端代理 |
| 可見端 | C3.ai IPD 累計與 active 數（可解 exit_t）；Salesforce deals／paid deals／「accounts in production」Q/Q；ServiceNow、UiPath 等同型揭露（測一查）；第三方放棄率調查 |
| 指名不可見端 | conv_t 與 drop_t 之拆分（C3.ai 只給 active，不給轉換數——測一查 10-Q）；直接生產簽約（不經試點）之件數；各供應商「deal」定義是否一致 |
| 外部參照物（測一查證） | 企業軟體 POC → 生產漏斗之具名前例（如 2010s Hadoop／大數據專案放棄率之 Gartner 2015–2017 調查與 Cloudera／Hortonworks 客戶數 vs 營收落差） |
| 表達工具型態（只指名，不選券） | 美股企業 AI 應用軟體普通股；不選券 |
| 重疊 | L14-P#2（承諾池）、L14-A（揭露口徑）、L15（平台軟體）；重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Salesforce Q3 FY26 新聞稿（期末 2025-10-31，2025-12-03）https://investor.salesforce.com/news/news-details/2025/Salesforce-Delivers-Record-Third-Quarter-Fiscal-2026-Results-Driven-by-Agentforce--Data-360/ ：「Salesforce has closed over 18,500 Agentforce deals since launch; over 9,500 paid deals, up 50% quarter-over-quarter」；「Agentforce accounts in production increased 70% quarter-over-quarter」；「Agentforce ARR surpassed half a billion in Q3, up 330% Y/Y」。
2. Salesforce Q2 FY27 新聞稿（期末 2026-07-31，2026-08-26）https://s205.q4cdn.com/626266368/files/doc_financials/2027/q2/CRM-Q2-FY27-Earnings-Press-Release.pdf ：「Agentforce ARR exceeded $1.5 billion, up over 240% Y/Y.」；「Effective Q2 FY27, Agentforce ARR includes our AI offerings, Slackbot and Headless 360」；「7.0 billion Agentic Work Units ("AWUs") delivered to date」。已讀部分（前 39,885／48,147 字元）**無** deals／paid deals／production 件數——揭露口徑已由件數轉為 ARR／AWU（否決 (1) 之直接風險）。
3. Zacks（Nasdaq，2025-12-18）https://www.nasdaq.com/articles/can-c3ais-ipd-led-sales-reset-support-more-durable-growth-path ：Q2 FY26「signed 20 new IPDs … bringing cumulative IPDs to 394」「with 269 currently active」。
4. Zacks（MetaTrader 轉載，2026-03-18）https://www.metatrader.com/it/news/1392043-c3ai-tightens-ai-pilot-strategy-what-does-it-mean-for-conversions ：Q3 FY26「signed 14 IPDs」「cumulative total to 408 IPDs, of which 258 remain active」。→ `[D]` exit_{Q3} = 14 − (258 − 269) = 25 件（轉生產＋放棄之和；拆分不可見）。二手轉述，測一回 C3.ai 10-Q／新聞稿原文。
5. CIO Dive（2025-03-14；S&P Global Market Intelligence，n > 1,000）https://www.ciodive.com/news/AI-project-fail-data-leaders-strategy/742590/ ：「The share of businesses scrapping most of their AI initiatives increased to 42% this year, up from 17% last year」；「The average organization scrapped 46% of AI proof-of-concepts before they reached production.」
6. TNW（2026-07-28）https://thenextweb.com/news/most-enterprise-ai-spend-still-hasnt-left-the-lab ：轉述 Gartner「through 2026, organizations will abandon 60 percent of AI projects unsupported by AI-ready data」；Forrester「only a small minority have it running in anything beyond limited pilots」。（二手；Gartner 原文測一查）
7. Computerworld（2024-07-30；Gartner n＝822）https://www.computerworld.com/article/3478532/nearly-one-in-three-genai-projects-will-be-scrapped.html ：「nearly a third of those projects will be abandoned by the end of next year」——2024 年事前預測，可於測一對照事後實現（外部參照物候選）。

缺段（§7-2）：任一供應商一手申報中 conv_t 與 drop_t 之分列；Salesforce Q1–Q2 FY27 是否仍揭露件數（全文含 10-Q 與法說逐字稿）；ServiceNow／UiPath／Palantir 同型件數；具名賣方以件數外推生產端之模型。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 供應商已不揭露件數（Salesforce Q2 FY27 改 ARR／AWU），市場直接看 ARR——件數外推不存在，守恆無定價對象 | #2 | 可觀測性／不存在 |
| R2 | ARR 已含試點與生產混合，且 ARR 成長（+240% Y/Y）遠大於件數漏斗之約束；件數 ≠ 金額 | #1、#2 | 量綱 |
| R3 | 放棄率已廣為報導（MIT「95%」、S&P 46%、Gartner 30%），已定價 | #5、#6、#7 | 已定價 |
| R4 | 調查之放棄率為受訪者自報、跨供應商平均，不能套用於單一供應商之 q | #5 | 可觀測性 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後 < 2 家上市供應商能於一手揭露（10-Q／10-K／新聞稿／法說逐字稿）中提供可解出 exit_t（或 conv_t）之件數序列 ≥ 3 期。
(2) 可得之最佳數據下，`[D]` 轉換率 q ≥ 0.8，或試點存量 N_t 相對生產端可忽略（< 10%）——漏斗不約束。
(3) 件數與生產端 ARR／營收無可辨連結（件數變動與 ARR 變動同期相關不可量），即件數不是生產端之有效領先指標（R2）。
(4) 放棄證據只有受訪者比例型調查，無一手供應商件數（R4）。
(5) 具名賣方或研究機構已以供應商之件數漏斗（試點存量 × 轉換率）量化生產端並公開——已定價（R3）。只點名「多數試點失敗」不算。
(6) 重定價窗（≥ 12 個月）內無可觀測檢驗事件（季報件數揭露、年度調查），或揭露已全面停止。
(7) 可運作對照只能寫成承諾池（L14-P#2 型）、裝機跨期替換（L14-P#4 型）、工作量跨場所分配（L14-P#5 型）或支出比重（L14-A 型），而非試點→生產之件數守恆。

複查觸發器（若日後殺）：任一上市企業 AI 應用供應商於 10-Q／10-K 分列試點轉生產件數與放棄件數；Salesforce 恢復 deals／production 件數揭露；第三方（非供應商）發布以專案件數計之逐年轉換率序列。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：IPD／deals 之件數、active 存量、ARR 分項；RPO 之試點 vs 生產。
2. 可交易工具：企業 AI 應用軟體普通股。不選券。
3. 半衰期：季報；試點期（C3.ai IPD 初始期間，測一查）。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0203、本輪 SCOUT-GEN 無佇列列可改 done；`query/ARCH_matrix.md` L14［P］標「#6 已生成」；`work/20261114_HEALTH_CL.md` 補記第 6 項（sec 腳本被拒）。線索檔（`export/LEADS_算力收支.md`）：本輪實讀事實不屬算力投入／AI 收入硬體／雲端合約／資料中心之核心口徑，Salesforce Agentforce ARR 屬 AI 收入——追加 1 筆。不寫入：FUNNEL（留給測一）、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L14-P#1–#5、L14-A、L14-I 結論；不寫 T。
