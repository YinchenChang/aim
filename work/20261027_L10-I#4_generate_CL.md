# L10-I#4 生成卡｜分發與中介：誘因（代理下單之「代理失誤」損失由誰承保＝支付憑證之路由誘因：網路／錢包以承保補貼爭取代理結帳之預設憑證）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261001_L10-I_generate_GK.md；archive/work/20261013_L10-I#2_generate_CL.md；archive/work/20261020_L10-I#3_generate_CL.md；work/20261020_L10-I#3_test1_CL.md；archive/work/20261027_L10-A#4_generate_CL.md；work/20261008_L12-I#2_test1_CL.md | EMITS: work/20261027_L10-I#4_generate_CL.md -->
**日期：** 2026-10-27　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 5→6／6）　**格：** L10-I　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L10-A#4 本日測一，Q-0115 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-20（L10-I#3、L11-A#3、L11-I#3、L13-P#3、L13-I#3、L14-P#3）；依表序取 **L10-I**。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py agentic chargeback "purchase protection"`，命中 2（SRC_PERF_014、SRC_PERF_039，皆推論效能基準，與本格無關，未用）。內部數字（§12）未取。§12 線索輸出：本輪事實屬支付損失／保障，非 AI 算力收支，未寫 LEADS。
- 比對之舊檔與死因型態，本卡須異型：
  - **L10-I#1**（測一不通過）：預設槽位取用權由結構性轉為法定（選擇畫面義務）。本卡無監理義務；誘因變數是**私人承保條款**，由網路／錢包自選。
  - **L10-I#2**（測一不通過）：App Store 導出購買之佣金差路由。本卡不論佣金率或費率差；路由變數是損失承保，不是價差。
  - **L10-I#3**（測一不通過）：在位市集對第三方代理之准入閘（封鎖／收費開放／自建）。本卡之決策者不是市集，而是**支付憑證提供者**（網路、發卡、錢包）；問題不是代理能否進入，而是代理用誰的憑證結帳。死因 (5)「自建代理變現併入單一行」與 (2)「代理流量 < 1%」本卡須正面回應（否決 (2)(5)）。
  - **L10-A#4**（測一不通過）：自保準備之精算估計恆等。本卡若只剩「保障準備估計／前期發展」即滑回該型（否決 (4)）。
  - **L12-I#2**（測一不通過）：AI 產出 IP 補償＝賣方寫給買方之賣權（ASC 460 無法估計）。本卡之保障亦為賣方寫出之或有義務；若可拒絕之主張只剩「或有義務不可估計」即滑回該型（否決 (4)）。
  - **L10-A#1**（TAC 量 × 分潤率）、**C-A5**（API 單價）不重開；L11-P（死 #3）不恢復；不寫 T-15。
- §7-10 領域最近公開：American Express 10-Q 3Q26（2026-10-23 申報）；Chargeflow（2026-10-25 頁面日期）；Visa 2026-04-18 框架（Law360 2026-05-28 轉述）。下一檢查點＝PayPal 3Q26 10-Q（約 2026-11 初）、Visa FY26 10-K（約 2026-11）、2026 年假期季代理訂單之爭議窗（卡組織爭議時限約 120 日 → 約 2027-04 前反映於 1Q27 申報）、Amex Agent Purchase Protection 上線日與條款。

## 1. 落差一句

代理下單產生一種既有爭議碼未乾淨涵蓋之損失：**已授權但非本意**（代理買錯、買多、買到不符意圖之品項）——持卡人授權了代理，故不是盜刷（Visa 10.4／MC 4837），商品可能如實描述，故未必是 13.3／4853。誰承保這類損失由各家自定：Amex 2026-04-14 宣布 Agent Purchase Protection「will protect eligible customers from charges related to AI agent error」（「In the future」、條款另定）；PayPal 2025-10-28 稱 agent ready「will enable fraud detection, buyer protection, and dispute resolution」；Visa 之規則（2026-04）要求依 Visa Intelligent Commerce 規格驗證身分，但「has not published how disputes are treated」，Mastercard 交易處理規則對代理交易「stay silent」（Chargeflow 轉述）。代理結帳時用誰的憑證，由代理／平台選擇；承保代理失誤即是爭取該預設憑證之**補貼**。種子主張：市場把代理商務讀成網路／錢包之量與費率選擇權（take rate × 代理 TPV），而本格之誘因變數是承保成本，它落在損失與持卡人福利費用行（PayPal transaction losses；Amex Card Member services），不在費率行；若承保競爭化，代理量之邊際收益可被承保成本吃回。本卡不定方向與量級，只立可拒絕之分離：代理失誤損失 vs 既有盜刷／未收貨損失。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因（路由競爭：承保條款 → 代理之預設憑證選擇）；不是監理義務（#1）、費率差（#2）、市集准入（#3） |
| 選擇者 | 憑證提供者：是否承保代理失誤、上限、適用代理（registered／trusted agents）；代理／平台：預設以哪個憑證結帳 |
| 可見端 | PayPal 10-Q：transaction losses、transaction loss rate（÷ TPV）、保障方案備抵 roll-forward（provision／realized／recoveries）；Amex 10-Q：Card Member services 費用與驅動敘述；網路規則與方案頁（VIC、Trusted Agent Protocol、Agent Pay、AP2、ACP） |
| 指名不可見端 | 代理發起 TPV 占比；代理失誤類爭議數與金額；各方案之承保上限與排除 |
| 量綱 | 損失率［bp of TPV 或 billed business］；代理占比［%］；代理失誤率［次／千筆］；`[D]` 承保成本上界 ≈ 代理占比 × 失誤率 × 平均票額 ÷ 總 TPV［bp］ |
| 外部參照物（測一查證） | 既有「買家保障擴張 → 損失率上升」之具名前例（PayPal 或發卡行歷史揭露） |
| 表達工具型態（只指名，不選券） | 美股上市之支付網路、閉環發卡網路、數位錢包普通股。不選券 |
| 重疊 | L10-I#3（代理流量）、L10-A#4（準備估計）、L12-I#2（或有承諾）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. PayPal 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/0001633917/000163391726000082/pypl-20260630.htm ：Transaction losses 323／383（3M，2026／2025）、599／661（6M）；Transaction loss rate 0.07%／0.09%（3M）；「decreased … due to lower fraud losses, benefits realized from risk mitigation strategies, and higher recoveries」；保障方案「considered assurance-type warranties … within the allowance for transaction losses」；備抵 roll-forward 期初 310、provision 323、realized（373）、recoveries 53、期末 313；全文「agentic」0 命中。
2. PayPal 新聞稿 2025-10-28 https://newsroom.paypal-corp.com/2025-10-28-PayPal-Launches-Agentic-Commerce-Services-to-Power-AI-Driven-Shopping ：agent ready 含 buyer protection；Store Sync 下商戶「remain the merchant of record」。
3. Amex 新聞稿 2026-04-14 https://www.nasdaq.com/press-release/american-express-debuts-agentic-commerce-experiences-acetm-developer-kit-and ：Agent Purchase Protection；觸發「agent sends American Express the customer's authenticated purchase intent」；上線日未定；「Merchants will benefit from lower disputes and chargebacks」。
4. Amex 10-Q 3Q26（sec.py）https://www.sec.gov/Archives/edgar/data/4962/000000496226000409/axp-20260930.htm ：前瞻因素點名「Amex Agent Purchase Protection™」與「Card Member usage of agentic technologies」；Card Member services 2,006／1,477（3Q，+36%）、5,930／4,106（9M），驅動敘述為持卡人福利使用與 Platinum 改版，未拆代理。
5. Visa：Trusted Agent Protocol 2025-10-14 https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21716.html ；VIC 2025-12-18 https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-partners-complete-secure-agentic-transactions.html （「hundreds of secure, agent-initiated transactions」；> 100 夥伴）；2026-04-18 框架（Law360，Witherspoon／Carroll／Perfetti，2026-05-28）https://www.law360.com/articles/2479142 （付費牆，僅首段）。
6. Chargeflow（Dan Moshkovich）https://www.chargeflow.io/blog/ai-agent-chargeback-liability ：爭議碼對照、VAMP 1.5%（2026-04-01 起）、Visa 未公布代理爭議處理、MC 規則未規範；二手，須回網路規則原文。
7. 測一須另取：Visa Core Rules／Mastercard 規則之代理條款原文；ACP（OpenAI／Stripe）與 AP2（Google）之爭議與責任條款；Amex APP 條款與上線日；PayPal 3Q26 10-Q 是否首揭代理 TPV 或代理爭議；具名賣方／評等機構是否把代理失誤承保成本單列；代理占比任何水準值。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 代理發起占比 < 1%，承保成本不重大 | L10-I#3 測一（Similarweb 0.4%；Bain「less than 1%」）；#5 VIC「hundreds」筆 | 不重大 |
| R2 | 代牌化與身分驗證把盜刷責任移至發卡行，代理失誤由驗證後之意圖紀錄（Cart Context、purchase intent）大幅降低，承保近乎零成本 | #3、#6 | 無落差 |
| R3 | 商戶仍為 merchant of record，非本意購買走退貨而非爭議，損失在商戶 | #2 | 誘因不在憑證方 |
| R4 | 保障成本併入既有行、發卡方稱不重大，不可分離 | #1、#4 | 不可觀測 |
| R5 | 責任配置終將由網路規則統一寫定，不是競爭變數 | #5、#6 | 誘因消失 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 具名賣方、評等機構或公司指引已公開把代理失誤承保／代理保障成本單列建模（或以「代理 TPV × 費率 − 保障成本」口徑呈現）——已定價。
(2) 窗內（≥ 12 個月）任一可得代理占比與失誤率所得 `[D]` 承保成本上界 < 0.5 bp of 該主體 TPV／billed business，或無任何來源給出代理占比水準值——不重大或不可觀測（R1）。門檻 0.5 bp 於本卡凍結。
(3) Visa／Mastercard 規則原文或 ACP／AP2 條款已把代理失誤損失統一配置給商戶或代理營運者，憑證方無承保選擇——誘因變數不存在（R3、R5）。
(4) 實讀後可拒絕之主張只剩：保障備抵之估計與前期發展（L10-A#4 型）、或有承諾不可估計（L12-I#2 型）、市集准入（L10-I#3 型）、預設槽位監理（L10-I#1 型）或費率差路由（L10-I#2 型）。
(5) 承保成本於所有指名申報皆併入既有行（transaction losses／Card Member services）且無任何代理拆分或量化敘述，並經發行人一手稱不重大——不可分離（R4；L10-I#3 死因 (5) 同型）。

複查觸發器（若日後殺）：Visa 或 Mastercard 發布代理專屬爭議碼或代理責任規則；PayPal／Amex 首次揭露代理 TPV、代理爭議數或保障成本；Amex APP 上線並公布承保上限；任一發卡行或錢包於申報中將代理失誤損失列為驅動因素。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：transaction losses、transaction loss rate、保障方案備抵；Card Member services；網路之 client incentives（若承保以誘因形式支付）。
2. 可交易工具：支付網路／閉環網路／錢包普通股。不選券。
3. 半衰期：季度（10-Q 損失率）；假期季爭議窗約 120 日。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L10［I］標「#4 已生成」；`AIM_FUNNEL.md` §3 一句（只改「已生成」未測格名）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live、LEADS。不改 L10-I#1–#3、L10-A#1–#4、L10-P#1–#4、L12-I#2、L11-P、C-A5 結論；不寫 T-15。
