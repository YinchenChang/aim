# L10-A#4 生成卡｜分發與中介：會計恆等（自保準備恆等：保險成本_t ≡ 當年事故年估計終局損失 ＋ 前期事故年發展；準備_t ≡ Σ（估計終局 − 已付）；平台把乘客／司機事故責任自留於自營 captive，損益表保險成本是一個精算估計，而非付款）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20261001_L10-A_generate_GK.md；archive/work/20261013_L10-A#2_generate_CL.md；archive/work/20261020_L10-A#3_generate_CL.md；work/20261020_L10-A#3_test1_CL.md；work/20261013_L10-A#2_test1_CL.md | EMITS: work/20261027_L10-A#4_generate_CL.md -->
**日期：** 2026-10-27　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 4→5／6）　**格：** L10-A　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L10-P#4 本日測一，Q-0114 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-20（L10-A#3、L10-I#3、L11-A#3、L11-I#3、L13-P#3、L13-I#3、L14-P#3）；依表序取 **L10-A**。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py insurance reserve breakage loyalty`，命中 0。載體全由本輪 sec.py／WebSearch／WebFetch 實讀。內部數字（§12）未取。§12 線索輸出：本輪事實皆非 AI 算力收支，未寫 LEADS。
- 比對之舊檔與死因型態，本卡須異型：
  - **L10-A#1**（測一不通過）：TAC＝轉介量 × 分潤率，量與率不可並列。本卡無分潤率；恆等兩側（準備增減、已付、前期發展）皆於同一 10-K Schedule II 申報。
  - **L10-A#2**（測一部分通過）：商戶預收浮存（ΔDMB 入 FCF），屬現金**時序**。本卡之可拒絕主張落在**估計**（終局損失之精算選擇與前期發展），不在時序；若實讀後只剩「Δ準備入 OCF」之浮存敘事即滑回 #2 型（否決 (3)）。
  - **L10-A#3**（測一不通過）：主事人／代理人列報切換，發行人已自行量化。本卡不論營收列報口徑。
  - **L13-A#2**（客戶預付入 OCF）、**L6-A#4**（capex 繞道）：皆現金分類／時序型；本卡異型同上。
  - **L12 系列**：驅動含侵權改革（SB 371、加州票決／立法交易），但主張落在準備恆等之損益傳導；若只剩「法案過不過」即 L12（否決 (4)）。
  - **L11-P**（死 #3）不恢復；C-A5 不重開；不寫 T-15。
- §7-10 領域最近公開：Uber 2Q26 10-Q（2026-08-05）；Daily Journal 2026-06-18（Uber 與 Consumer Attorneys of California 交易）；CalMatters 2026-06-24。下一檢查點＝Uber 3Q26 10-Q（約 2026-11 初）、加州 2026-11-03 選舉結果、Uber FY26 10-K Schedule II（約 2027-02）、SB 371 節省報告（2027-02-01 前）。

## 1. 落差一句

恆等骨架：`Add_t ≡ U_t(當年事故年) + Dev_t(前期發展)`；`R_t ≡ R_{t−1} + Add_t − Paid_t (+ 可回收對應之 Other)`；損益表保險成本＝`Add_t`，OCF 含 `ΔR_t`。已見數點（Uber 10-K FY2025 Schedule II，sec.py）：準備 4,754 → 6,986 → 9,796 → 12,463［百萬美元，2022→2025 年末］；Additions 3,544／4,489／4,879；Deductions（已付）1,526／1,696／2,421；Dev＝+158／−78／−21（2023／24／25）。［D］Paid÷Add（2025）≈ 50%；|Dev|÷Add（2025）≈ 0.4%；R÷Paid（2025）≈ 5.1 年；OCF 之「Accrued insurance reserves」2,230／2,819／2,660 ÷ OCF 3,585／7,137／10,099 ≈ 62%／39%／26%。2Q26 10-Q：準備 12,463 → 13,286（6 個月 +823），1H 現金流量表同行 1,487 → 830（欄序 2025／2026，待測一確認）。外部主張兩向：Consumer Watchdog（2026-05）估所需準備 4.5–5.4B、稱「over-reserve」並指 Aleka 自留近 95%；公司稱準備「adequate」而風險因素列 mass tort／社會通膨。種子主張：市場以調整後 EBITDA／FCF 讀聚合平台之單位經濟，而其保險成本是由管理層終局損失假設決定之估計；侵權規則改變（SB 371 降 UM/UIM 至 60k／300k；加州醫療損害限制交易；NY／IN／NV 改革）改變**已發生事故年**之終局，經恆等式只能以 `Dev_t`（一次性、計入當期）出現。本卡不定方向與量級，只立可拒絕之分離：當年估計 vs 前期發展 vs 浮存。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（損失準備 roll-forward；ASC 450／自保 captive；Schedule II） |
| 量綱 | R、Add、Paid、Dev［美元／年或季］；Paid÷Add、Dev÷Add、ΔR÷OCF［無量綱］；R÷Paid［年］ |
| 可見端 | 10-K Schedule II（年度 roll-forward 與前期發展註腳）；10-Q 資產負債表短／長期準備、現金流量表 Accrued insurance reserves；10-K 關鍵查核事項（PwC：loss development patterns、expected loss costs） |
| 指名不可見端 | 事故年別三角形（loss triangle）；Aleka 法定報表（夏威夷保險局）之準備與發展是否公開；季度 Dev |
| 主張 | 保險成本之事故年分解未被市場分離；可由「公司或賣方已分離」或「Dev 永遠小」拒絕 |
| 外部參照物（測一查證） | Lyft 過往 adverse development（10-K FY2025 風險因素「we have in the past experienced adverse development … prior periods」）之期別、金額與當時股價／共識反應 |
| 表達工具型態（只指名，不選券） | 美股上市、自留乘車／外送責任之聚合平台普通股。不選券 |
| 重疊 | L12（侵權改革）、L10-A#2（浮存時序）、L13-A#2。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Uber 10-K FY2025（sec.py）https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm ：Schedule II 準備列與註 (1)「Additions to insurance reserves include $158 million, $(78) million and $(21) million … for changes in estimates resulting from new developments in prior period claims」；註 (3) 第三方可回收 264／473；政策「Adjustments to reserves … relating to accidents that occurred in prior years are reflected in the current year results of operations」；CAM「Valuation of Insurance Reserves … totaled $12.5 billion」。
2. Uber 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1543151/000154315126000032/uber-20260630.htm ：短期 3,387→3,758、長期 9,076→9,528；Accrued insurance reserves 1,487／830；MD&A「accrued insurance reserves primarily due to liabilities recorded during the period exceeding claims paid out」。
3. Lyft 10-K FY2025 https://www.sec.gov/Archives/edgar/data/1759509/000162828026006960/lyft-20251231.htm ：adverse development 前例句；CalMatters 稱 Lyft 準備約 2.2B、DoorDash 約 1.1B。
4. Insurance Business（Mav Rodriguez，2026-05-26）https://www.insurancebusinessmag.com/us/news/auto-motor/uber-insurance-reserves-face-scrutiny-over-robotaxi-plans-576585.aspx 與（Matthew Sellers，2026-07-07）https://www.insurancebusinessmag.com/us/news/breaking-news/ubers-insurance-story-has-a-5-8-billion-problem-581507.aspx ：Consumer Watchdog 報告；約 4.1B「moved from reserves to cash」；Uber 回應「take rate of about 21% after insurance」。
5. CalMatters（Levi Sumagaysay，2026-06-24）https://calmatters.org/economy/2026/06/uber-california-insurance-liability/ ：SB 371 1M → 60k／300k；Uber「45%」LA 票價歸於保險；節省報告 2027-02-01。
6. Daily Journal（Malcolm Maclachlan，2026-06-18）https://dailyjournal.com/articles/392264-uber-trial-lawyers-reach-deal-to-avert-ballot-fight ：醫療損害限制交易，票決撤回待立法。
7. 測一須另取：交易是否立法、生效日與溯及範圍（已發生事故是否適用）；Uber 法說／投資人簡報是否量化 SB 371 對保險成本或準備之影響；季度 Dev 是否揭露；Aleka 法定報表；具名賣方是否以事故年或「ex-準備發展」口徑建模、是否以 ΔR 調整 FCF；Lyft adverse development 前例之金額與反應。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 公司年度揭露前期發展且 PwC 獨立精算，估計已受查核 | #1 | 已揭露／不重大 |
| R2 | 2023–2025 前期發展僅 +158／−78／−21，相對 Additions < 5%，準備估計歷史上準確 | #1［D］ | 無可拒絕之落差 |
| R3 | 侵權改革只影響新保單／新事故，已發生事故年終局不變；效果走 `U_t` 而非 `Dev_t` | #5、#6 | 機制只剩成本下降之營運敘事 |
| R4 | 市場已將保險視為過路成本（公司以「take rate after insurance」溝通） | #4 | 已定價 |
| R5 | 真正可拒絕之事件是法案或票決，屬 L12 | #5、#6 | 滑入他格 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 公司指引／法說或具名賣方／評等機構已公開以事故年分解、「排除前期發展」或「排除 Δ準備」之口徑呈現保險成本或 FCF——已定價（R1、R4）。
(2) Uber 2026 年（10-Q 季度揭露或 FY26 10-K Schedule II）之 |Dev| ÷ Additions < 3%，且窗內（≥ 12 個月）無任何適用於**已發生事故**之侵權規則變更——落差不重大（R2、R3）。門檻 3% 於本卡凍結。
(3) 實讀後可拒絕之主張只剩「Δ準備入 OCF」之浮存時序——L10-A#2／L13-A#2 型。
(4) 可運作對照只能寫成 L12 系列（法規／票決成立與否）、L10-A#1 或 L10-A#3。
(5) 公司已量化侵權改革之保險成本變化並以票價轉嫁抵銷（具名一手證據），致恆等式各項對貢獻利潤不變。

複查觸發器（若日後殺）：Uber／Lyft 10-Q 或 10-K 揭露單期前期發展 ≥ 該期 Additions 5%；加州醫療損害限制立法明定適用於未決案件；Aleka 法定報表公開事故年三角形；具名賣方首次以 ex-Δ準備口徑出 FCF。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：cost of revenue 內保險成本、Schedule II、短／長期準備、Accrued insurance reserves（OCF）、保險可回收。
2. 可交易工具：聚合平台普通股。不選券。
3. 半衰期：年度 Schedule II（FY26 10-K 約 2027-02）；季度只見準備餘額。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L10［A］標「#4 已生成」；`AIM_FUNNEL.md` §3 一句（只改「已生成」未測格數）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live、LEADS。不改 L10-A#1–#3、L10-P#1–#4、L10-I#1–#3、L12 系列、L13-A#2、L11-P、C-A5 結論；不寫 T-15。
