# L10-I#6 生成卡｜分發與中介：誘因（計費單位由中介自身生成：求職市集以「已開始之應徵」計費，且自營 AI 代投工具〔Apply For Me〕所送出之應徵計入該單位——中介同時控制可計費事件之供給端，AI 使每份應徵之邊際成本趨零後，ARPJ 成長中「計費事件量」與「雇主每次雇用價值」可分離）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；AIM_FUNNEL.md；query/ARCH_live.md；archive/drive/USED_20261001_L10-I_generate_GK.md；archive/work/20261013_L10-I#2_generate_CL.md；archive/work/20261020_L10-I#3_generate_CL.md；archive/work/20261027_L10-I#4_generate_CL.md；archive/work/20261103_L10-I#5_generate_CL.md；archive/work/20261103_L11-I#5_generate_CL.md；archive/work/20261021_L14-I#3_generate_CL.md | EMITS: work/20261112_L10-I#6_generate_CL.md -->
**日期：** 2026-11-12　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1→2／6）　**格：** L10-I　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（Q-0196 done）。非已殺／刻意排除格中最後測試日最舊＝2026-11-03（L10-I#5、L11-A#5、L11-I#5、L13-A#5；L10-A 已於本日 #6 測畢）；依表序取 **L10-I**。既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py Indeed ZipRecruiter recruiting`，命中 0。內部數字（§12）未取。§12 線索輸出：0 筆（本輪實讀事實不屬算力收支範圍）。
- 比對之舊檔與死因型態，本卡須異型：
  - **L10-I#1**（不通過）：預設槽位之法定選擇畫面。本卡不涉預設槽位。
  - **L10-I#2**（不通過）：應用商店佣金差驅動**支付路由**（供給方繞道）。本卡無繞道：計費單位之**定義與生成者**為落差，非費率差。
  - **L10-I#3**（不通過）：在位市集對第三方代理之准入閘。本卡之代理為**中介自營**且其輸出即計費事件；不論准入。
  - **L10-I#4**（不通過）：代理失誤損失承保。本卡不涉損失分攤。
  - **L10-I#5**（不通過）：主事媒體之未揭露加價（代理→本人）。本卡中介角色不變，價格公開，落差在數量端。
  - **L11-I#5**（不通過）：以版稅折讓出售演算法注意力。本卡不涉供給方折讓。
  - **L14-I#3／L15-P#2**：雲承諾退抵。無關。
  - L11-P（死 #3）不恢復；L8-P／L9-P 不恢復；不寫 T-15。
- §7-10 領域最近公開：Recruit Holdings Q2 FY2026 法說（2026-11-10／11）；ZipRecruiter 10-Q 期 2026-09-30（2026-11-09 申報）；Indeed 雇主條款版本 2026-09-29（第三方擷取）。下一檢查點＝Recruit Q3 FY2026（約 2027-02）、ZIP 10-K FY2026（約 2027-03）、Indeed 條款更版。

## 1. 落差一句

骨架：中介營收 `R = Σ_j n_j · p_j`，`n_j`＝職缺 j 之可計費事件（已開始應徵／點擊），`p_j`＝單價；可計費事件 `n = n_human + n_AA`，`n_AA`＝經中介**自營**代投工具送出者。雇主之價值單位為雇用 `h`。只要計費單位為 `n` 而非 `h`（或合格應徵），中介對 `n_AA` 之供給即有誘因：`∂R/∂n_AA = p > 0`，而 `∂h/∂n_AA` 可 ≈ 0。Indeed 條款（2026-09-29 版，第三方擷取）列「an Auto Apply where a user has activated Indeed's Apply For Me tool and an application has been sent to you」為 Started Application 之一種；Recruit Q2 FY2026 美國 ARPJ +39%、職缺數約持平、HR Tech 美元營收 +27.5%；管理層同時稱計費正由點擊轉向績效（「cost per qualified application／interview」試行，摘要層）。可分離之主張：**ARPJ 成長中有一部分來自中介自己生成之計費事件量，而非雇主每次雇用之願付價格**；當計費單位遷移（點擊/開始應徵 → 合格應徵/面試/雇用）時，該部分即重定價。市場若以 ARPJ 讀「AI 提升配對價值」，錯價在**計費單位之定義**。**不主張方向或時點，不寫 H1。**

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因（中介同時設定計費單位並控制該單位之生成工具；生成邊際成本 → 0） |
| 量綱 | `n`［事件／職缺·期］、`p`［美元／事件］、ARPJ［美元／職缺·期］、`h`［雇用／職缺］；`s_AA ≡ n_AA / n`［無量綱］ |
| 選擇者 | 中介（計費單位、代投工具預設與上限、無效應徵退費規則）；雇主（預算、轉單位或轉通路）；求職者（啟用代投） |
| 可見端 | Indeed 雇主條款（Started Application 定義、退費／拒絕窗）；Recruit 季報 ARPJ、職缺數、Career Scout／Talent Scout 使用者增幅；ZIP 10-Q Quarterly Paid Employers、Revenue per Paid Employer、績效型營收；ZIP 法說「qualified applications」 |
| 指名不可見端 | `s_AA`；按計費單位分列之營收；每雇用成本之時間序列 |
| 主張 | `s_AA` × 計費事件占營收比 ≥ 門檻，且計費單位遷移或代投限流於窗內可觀測；可由「代投不計費／已排除」「計費已以合格應徵或雇用為單位」「ARPJ 成長全屬單價或層級升級」拒絕 |
| 外部參照物（測一查證） | 前例：Indeed 2023 推 pay-per-application 後於 2023-12-18 撤回（小雇主帳單暴增）；搜尋廣告之無效點擊退費制度（計費單位品質爭議之先例） |
| 表達工具型態（只指名，不選券） | 美股上市之求職市集普通股；Recruit 為東證上市（美國僅 OTC ADR，可交易性測一記錄）。不選券 |
| 重疊 | L11（人類注意力：應徵者注意力）、L14（企業終端需求：招募預算）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Indeed 雇主條款第三方擷取（ConductAtlas，版本 2026-09-29）https://conductatlas.com/platform/indeed/indeed-terms-of-service/provision/CA-P-028405/pay-per-started-application-charges-include-auto-apply/ ：「A Started Application includes: 1) a click on a button or link to start or continue an application...」「and 5) an Auto Apply where a user has activated Indeed's Apply For Me tool and an application has been sent to you.」「A Started Application is considered complete even if the user does not proceed further.」；2026-07-03 變更紀錄「automatically draft application content for particular jobs」。**測一須取 Indeed 官方條款原文**（indeed.com legal）以確認，第三方擷取不作證據。
2. Recruit Q2 FY2026 法說逐字稿（Investing.com，2026-11-11）https://www.investing.com/news/transcripts/earnings-call-transcript-recruit-holdings-posts-strong-q2-2026-growth-shares-slip-93CH-5018043 ：「up 27.5% year-on-year in U.S. dollar terms and up 36.6% year-on-year in the U.S.」「the revenue per sponsored job posting, continue to show strong sustained growth」「Our AI tools and advertising products are simply evolving ways to monetize that core value.」「user numbers for our AI agent for job seekers, Career Scout, grew by 65 percentage points」；Goldman Sachs 問個人 AI 代理是否動搖 Indeed 商業模式；摘要層（非逐字）：「receiving many applications by AI agents, so 100 or 1,000 per person and per case」「Cost per interview or cost per qualified application is now being tried.」。測一須取 Recruit IR 原始逐字稿／簡報。
3. Investing.com 簡報摘要（2026-11-11）https://www.investing.com/news/company-news/recruit-holdings-q2-2026-slides-hr-tech-drives-68-eps-surge-93CH-5018064 ：「higher average revenue per job posting, which increased 39% year-over-year in the second quarter」「even as total job postings on the platform remained relatively flat」。
4. SIA（2026-11-11）https://www.staffingindustry.com/news/global-daily-news/recruit-holdings-posts-record-high-revenue-in-q2-hr-tech-surges ：「revenue rose 27.5% year on year to USD 3.07 billion」「US average revenue per job, or US ARPJ, growth of 39%」。
5. ZipRecruiter 10-Q 期 2026-09-30（sec.py）https://www.sec.gov/Archives/edgar/data/1617553/000161755326000056/zip-20260930.htm ：「Quarterly Paid Employers 63,466 66,302 66,959 59,104 63,329 70,721 73,929 Revenue per Paid Employer $ 1,734 $ 1,693 $ 1,717 $ 1,889 $ 1,698 $ 1,669 $ 1,683」；營收分列「Subscription $ 93,591 $ 87,729 … Performance-based 30,853 27,253」（千美元，3Q26／3Q25）；風險因素「If internet search or generative AI engines’ methodologies … are modified to our disadvantage」。績效型營收之計費事件定義本輪 grep 未命中，測一須讀 10-K 收入認列節。
6. Panabee（AI 生成摘要，2026-11-09，數字已由 #5 校）https://www.panabee.com/news/ziprecruiter-earnings-q3-2026 ：「helped push qualified applications up 49% quarter-over-quarter」「employer response rates tripled year-over-year」（須以 ZIP 股東信原文確認）。
7. HeroHunt（2026-09-08）https://www.herohunt.ai/blog/indeed-pricing-for-employers-2026-costs-and-alternatives/ ：「Pay-per-application arrived, blew up small employers' bills and was withdrawn on December 18, 2023.」「with a monthly budget you are charged when they click to apply」（前例；二手）。
8. SHRM（2022-10-17）https://www.shrm.org/in/topics-tools/news/talent-acquisition/indeed-shifts-pricing-to-pay-per-application ：「pay-per-started-application is primarily applicable for jobs indexed by Indeed from across the Web」（計費單位沿革；二手）。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | ARPJ +39% 來自層級升級（Premium Sponsored Jobs）與單價，非事件量；CEO 稱「customers upgrading to higher-priced tiers」 | #2 | 落差不可分離 |
| R2 | 月預算制有上限，事件量增只改變預算耗用速度、不增營收 | #7 | 無量效果 |
| R3 | Indeed 已轉向合格應徵／面試計費，自身正在消除誘因 | #2（摘要層） | 已自我修正、已揭露 |
| R4 | 代投應徵經篩選（AI screening：只有符合條件者能應徵），`s_AA` 之計費占比小 | #2（摘要層） | 不重大 |
| R5 | 本質是 L11（注意力）或 L14（招募預算）問題 | — | 滑入他格 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) Indeed 官方條款原文（或 ZIP 對應條款）顯示自營代投應徵**不計費**、或可無條件退費，或該條已刪除——誘因不存在。
(2) 一手證據（Recruit IR 原文、ZIP 10-K／股東信）將 ARPJ／Revenue per Paid Employer 之成長**全數**歸因於單價、層級或組合，且計費事件量（應徵、點擊）未增或已揭示不入營收——落差不可分離（R1、R2）。
(3) `[D]` 以測一可得最佳證據估 `s_AA`（代投占計費事件）× 事件計費營收占比之區間，上端 < 5%——不重大（R4）。門檻 5% 於本卡凍結。
(4) 計費單位已於一手來源宣告全面改為合格應徵／面試／雇用（非「試行」），且生效於 2026-11-12 之前——已自我修正並已公開（R3）。僅「試行」或摘要層說法不觸發，但測一須記錄。
(5) 實讀後可拒絕之主張只剩「求職者注意力被代理稀釋」（L11 型）或「企業招募預算增減」（L14 型）或單純之佣金差繞道（L10-I#2 型）。
(6) 美國券商無可交易之求職市集工具（ZIP 流動性不足以承載且 Recruit 僅 OTC）——表達層不可表達；記錄後不殺機制。

複查觸發器（若日後殺）：Indeed 條款更版（Started Application 定義或代投計費）；Recruit 或 ZIP 宣告計費單位遷移；雇主集體訴訟或 FTC 就應徵計費提出；ZIP 分列合格應徵或每雇用成本。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Recruit HR Technology 營收、ARPJ、職缺數；ZIP 訂閱／績效型營收、Quarterly Paid Employers、Revenue per Paid Employer。
2. 可交易工具：美股求職市集普通股；東證主體之 OTC ADR。不選券。
3. 半衰期：季度；條款更版與計費單位公告為事件。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列（Q-0197）；`query/ARCH_matrix.md` L10［I］標「#6 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live、LEADS。不改 L10-I#1–#5、L10-P#1–#6、L10-A#1–#6、L11-I#5、L14-I#3 結論；不寫 T-15。
