# L14-I#5 生成卡｜企業終端需求：誘因（AI 使用量被寫入員工考核與高管激勵——「使用即績效」之 Goodhart 誘因：企業內部 AI 使用量〔活躍用戶、token、AI 產碼行數、部署數〕部分由考核／獎金誘因而非任務價值驅動；賣方以使用量／DAU／用量計費成長作企業 AI 需求可持續之證據，未分離誘因成分）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261005_L14-I_generate_GK.md；archive/work/20261014_L14-I#2_generate_CL.md；archive/work/20261021_L14-I#3_generate_CL.md；archive/work/20261028_L14-I#4_generate_CL.md；work/20261028_L14-I#4_test1_CL.md；archive/work/20261104_L14-P#5_generate_CL.md | EMITS: work/20261104_L14-I#5_generate_CL.md -->
**日期：** 2026-11-04　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 5→6／6）　**格：** L14-I　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L14-A#5 本日測一，Q-0163 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-28（L14-I#4；L15-P／A／I#4 為 10-29）→ **L14-I**。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `Copilot seats usage adoption`，命中 3 筆（SRC_DEM_010／059／088：OpenAI API 量、美國成人使用率、Codex token），皆消費者或 API 總量，非企業內部誘因，相關命中 0；未用。內部數字（§12）未取。
- 比對之舊檔與死因型態，本卡須異型：
  - **L14-I#1**（`archive/drive/USED_20261005_L14-I_generate_GK.md`）：人力節省是否回流採購預算（預算擁有者 × 採購 KPI；死因＝採購績效與節省去向不可並列）。本卡不涉預算歸屬；選擇者是**員工與高管**，誘因是**個人考核／獎金**，作用量是**使用量**而非採購額。
  - **L14-I#2**（`archive/work/20261014_L14-I#2_generate_CL.md`）：裁員理由之措辭。本卡不涉裁員或揭露措辭。
  - **L14-I#3**（承諾退抵之採購路由；否決 (6)）：本卡無市集、無承諾。
  - **L14-I#4**（`work/20261028_L14-I#4_test1_CL.md`，牌價階梯＋續約鎖價；部分通過，歸因口徑屬常態）：本卡不涉價格或續約時點；落差在**量**（使用強度）之成因，非 ARPU 之價格成分。
  - **L14-P#1**（席次 ≤ 員工數）、**L14-P#5**（推論工作量放置守恆）、**L14-A 系列**（支出比重、會計分流、簽約滾存、本人／代理人）：本卡不是守恆或會計口徑，是行為誘因。
  - **C-A2**（ARCH_dead #9，單位經濟／無可交易主體）、**C-I5**（#18，按 AI 採用時序之留存 cohort）：本卡不主張單位經濟；C-I5 之複查觸發器（AI vs 非 AI 之 NRR）可作本卡旁證，但本卡不重開 C-I5。
  - **L11-P／L8-P／L9-P**（已殺）：不涉人時上界、標註分鐘、核可率。不寫 T。
- §7-10 領域最近公開：Amazon 軟體工程師 AI 指引（2026-10-27 公開；TNW 2026-10-28）；Microsoft 10-Q 1Q FY27（期末 2026-09-30）；Pearl Meyer 2026 proxy 季研究（2026-06-27）；Mercer S&P 500 早申報者研究（2026 初）。下一檢查點＝2027 proxy 季（DEF 14A，約 2027-03–04）、Microsoft 2Q FY27 10-Q（約 2027-01）。

## 1. 落差一句

賣方以企業內 AI **使用量**（Microsoft：M365 Copilot「daily active users increasing 10X year-over-year」、付費席次 15M；1Q FY27 10-Q：商業雲營收成長部分來自「increased consumption of usage-based services, primarily in GitHub Copilot」）作為企業 AI 需求已紮根之證據；種子主張：2025–2026 大型雇主把 AI 使用寫入員工考核與獎金（Meta 2026 起正式納入評等、200%／300% 獎金倍數；Amazon 設「more than 80% of its developers to use AI each week」目標並出現 KiroRank 排行與「tokenmaxxing」），且約 2% 上市公司把 AI 寫入高管激勵、其中多為**採用／部署**而非成果指標——使用量之一部分是**誘因誘發之量**，當考核口徑由「用量」轉為「成果」（Amazon 2026-10 指引已稱 token／採用指標「deeply flawed」）時，該成分會在用量計費與續約擴席上回吐。可拒絕之主張＝(i) 考核／激勵誘因於主要買方真實存在且以**用量或採用**計（非成果）；(ii) 用量計費或擴席之可見端對該誘因有可辨之敏感度（口徑轉向後用量成長放緩）；若誘因只在少數雇主、或口徑轉向後用量無變化，本卡死。本卡不主張任何公司營收或股價方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因（I）**：使用量 `U = U_task + U_kpi`；`U_kpi` 由考核權重 `w`（使用量進評等／獎金之比重）與被考核員工數 `N_m` 驅動；`U_kpi → 0` 當 `w` 改為成果口徑。賣方收入對 `U` 之彈性：用量計費（GitHub Copilot 用量、API token）≈ 1；席次制經續約擴席滯後 1–3 年 |
| 選擇者 | 員工（為評等而用）、管理層與董事會薪酬委員會（設定 `w`）；賣方只觀測 `U` |
| 驅動（因果層，§7-5） | 考核制度與獎金倍數；高管激勵之採用指標；內部排行／儀表板；口徑轉向事件（成果化、排行關閉） |
| 量綱 | 使用量（DAU、token、AI 產碼行數、部署數）；`w` 為無因次權重；`N_m` 人數；美元只作賣方端代理 |
| 可見端 | 雇主公開之考核制度報導與內部備忘錄公開版（Meta、Amazon）；DEF 14A 之激勵指標原文（sec.py 可實讀）；賣方 10-Q 之用量計費歸因句與席次／DAU 陳述 |
| 指名不可見端 | `U_kpi` 占 `U` 之比；各賣方用量收入中受考核雇主之占比；口徑轉向後之同客戶用量序列 |
| 外部參照物（測一查證） | Goodhart 型考核前例：Wells Fargo 2016 交叉銷售配額（CFPB 同意令；指標誘發之帳戶數 vs 真實需求）；軟體業「每開發者程式碼行數」KPI 之歷史廢棄。測一須找一手（同意令、10-K 揭露） |
| 表達工具型態（只指名，不選券） | 美股企業 AI 軟體（席次制／用量制）普通股；不選券 |
| 重疊 | C-I5（cohort 留存）、L14-P#1（席次）、L7（API 用量）；重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Microsoft 10-Q 1Q FY27（期末 2026-09-30）https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm （`sec.py doc --grep Copilot` 實讀，8 筆）：「Microsoft 365 commercial cloud revenue increased 17% driven by higher revenue per user, reflecting continued upsell to premium seat offerings, including Microsoft 365 Copilot, E5, and E7, as well as increased consumption of usage-based services, primarily in GitHub Copilot.」——用量制收入直接對 `U` 有彈性；未分客群或使用成因。
2. office365itpros（2026-01-30；Microsoft FY26 Q2 財報 2026-01-28）https://office365itpros.com/2026/01/30/microsoft-fy26-q2-results/ ：首次揭露 M365 Copilot 付費席次 15 million（年增 160%）；「daily active users increasing 10X year-over-year」；「24 billion Copilot interactions were audited by Purview this quarter, up 9X」；GitHub Copilot 付費 4.7M。（二手轉述官方，測一取 IR 逐字稿）
3. HR Grapevine（2026-02-05）https://www.hrgrapevine.com/us/content/article/2026-02-05-meta-links-ai-adoption-usage-to-reviews-rewards 與 eWeek（2026-02-04）https://www.eweek.com/news/meta-ai-performance-reviews/ ：Meta「tying performance reviews and bonuses more closely to how workers deploy AI tools」；Checkpoint 追蹤「how many lines of code are generated using AI tools, alongside more than 200 additional data points」；最高評等「200% individual bonus multiplier」、「Meta Award」300%；「dashboards monitoring AI tool adoption across teams」。（二手，引 The Information 與內部溝通）
4. HCA Mag（2026-06-01）https://www.hcamag.com/ca/news/general/amazon-shuts-down-ai-leaderboard-after-tokenmaxxing/577190 ：「Amazon has set a target for more than 80% of its developers to use AI each week」；Kirorank 排行關閉（引 FT）；SVP Treadwell「Please don't use AI just for the sake of using AI」。TNW（2026-10-28）https://thenextweb.com/news/amazon-tokenmaxxing-memo-engineers-ai-metrics ：Amazon 指引（Terkowitz）稱 token 用量、採用率與 code-change 計數「deeply flawed」；「If your work does not benefit from current AI tooling, that is a finding, not a failing.」；「tokenmaxxing is at odds with frugality」——**口徑轉向事件**之一例。一手：aboutamazon.com 該指引頁（測一實讀）。
5. Pearl Meyer／Harvard Law Forum（2026-06-27）https://corpgov.law.harvard.edu/2026/06/27/ai-in-incentive-plans-opportunity-risk-and-the-role-of-the-compensation-committee/ ：約 2,500 份 2026 proxy 中「58 companies … just 2%」把 AI 納入高管激勵；「only 12% use an explicit AI metric」；「most companies are rewarding AI adoption, capability building, and transformation efforts rather than measurable AI-driven financial outcomes」；「a metric based on AI deployment may reward the rollout of tools, even if those tools are not meaningfully used」。Mercer（2026 初，145 家 S&P 500 早申報者）https://www.mercer.com/en-us/insights/total-rewards/executive-compensation/ai-adoption-in-executive-incentive-plans/ ：「14% … STI metric … Only 2% … LTI」；Communication Services 33%、Financials 25%、IT 18%。（兩樣本口徑不同，不可相比）

缺段（§7-2）：員工層考核納入 AI 使用之**雇主覆蓋率**（目前只有個案報導）；`U_kpi` 之任何量化；賣方用量收入之客群／成因拆分；口徑轉向前後之用量序列；DEF 14A 具名公司原文（測一以 sec.py 實讀）。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 考核納入 AI 只見於少數科技雇主（Meta、Amazon 等），高管層僅約 2%；`N_m × w` 相對企業 AI 總用量過小 | #3、#4、#5 | 非邊際 |
| R2 | 被誘發之用量會轉為真實技能與任務價值（學習曲線），`U_kpi` 隨時間轉成 `U_task`，口徑轉向不致回吐 | Amazon 指引「AI will be at the center of software engineering practice」（#4） | 機制方向 |
| R3 | 「tokenmaxxing」與 shelfware 風險已被廣泛報導（FT、CNBC、Business Insider、AlphaStreet），已定價 | #4 | 已定價 |
| R4 | 賣方主力為席次制，與員工使用強度無關；用量制收入占比小 | #1 | 可捕捉性 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後，以**用量或採用**（非成果）計之 AI 考核／激勵，於一手或 ≥ 2 家獨立二手中可確認之大型雇主 < 3 家，且 DEF 14A 具名採用型指標 < 3 家——誘因不具規模（R1）。
(2) 可得最佳數據下，`[D]` 受考核雇主之員工數 × 用量份額占任一具名賣方用量制或 AI 席次之上界 < 5%（門檻凍結於此）——非邊際。
(3) 至少一例口徑轉向（Amazon 2026-05 排行關閉／2026-10 指引、或他例）之後，可得之用量或賣方用量收入序列無放緩，或無任何可對齊之序列——敏感度不可辨。
(4) 賣方用量制收入（GitHub Copilot 用量、API）不可與席次制分離，且賣方不揭露 DAU／用量之任何序列——可見端不存在。
(5) 具名賣方或研究機構已**量化**「考核誘發用量 → 企業 AI 軟體收入或續約」並公開——已定價（R3）。只點名 tokenmaxxing 現象不算。
(6) 重定價窗（≥ 12 個月）內無可觀測檢驗事件（2027 proxy 季 DEF 14A 指標改版、賣方季報用量歸因、具名雇主考核改制），或已全部於窗前公告。
(7) 可運作對照只能寫成預算回流（L14-I#1 型）、裁員措辭（L14-I#2 型）、承諾退抵（L14-I#3 型）、牌價階梯（L14-I#4 型）、席次 ≤ 員工數（L14-P#1 型）或 AI cohort 留存（C-I5 型），而非考核誘發之使用量。

複查觸發器（若日後殺）：任一 AI 軟體賣方於 10-K／10-Q 揭露用量或 DAU 之客群或成因拆分；任一大型雇主公開考核口徑由用量改成果並揭露前後用量；DEF 14A 中採用型 AI 指標之家數年增 ≥ 2 倍。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：賣方用量制收入（GitHub Copilot 用量、API）與席次制之拆分；擴席／淨留存。
2. 可交易工具：企業 AI 軟體普通股。不選券。
3. 半衰期：季報；年度 proxy 季；考核週期（年度評等，多於 1–3 月）。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` Q-0164（ANALYST）；`query/ARCH_matrix.md` L14［I］標「#5 已生成」；`export/LEADS_算力收支.md` 追加 1 筆（Microsoft 365 Copilot 付費席次 15M〔二手轉述官方〕）。不寫入：FUNNEL（留給測一）、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L14-I#1–#4、L14-P、L14-A、C-I5、C-A2 結論；不寫 T。
