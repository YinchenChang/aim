# L14-P#3 生成卡｜企業終端需求：守恆（客服互動之人工處理量守恆：H ≡ V × (1 − a)——AI 自助解決率 a 上升時，外包坐席工時（BPO）與雲端客服坐席（CCaaS）共用同一人工處理量 H，CCaaS 坐席成長只能來自雲遷移份額，非 H 本身）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20261005_L14-P_generate_GK.md；archive/drive/USED_20261005_L14-P_test1_GK.md；archive/work/20261013_L14-P#2_generate_CL.md；work/20261013_L14-P#2_test1_CL.md | EMITS: work/20261020_L14-P#3_generate_CL.md -->
**日期：** 2026-10-20　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 5→6／6）　**格：** L14-P　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L13-I#3 本日測一，Q-0079 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-13（L14-P、L14-A）；依表序取 **L14-P**。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `contact center BPO deflection`，6 筆皆硬體／PUE 列，相關命中 0；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L14-P#1**（`archive/drive/USED_20261005_L14-P_test1_GK.md`）：席次 ≤ 員工數（單一買方之員工存量上界）；死因＝同一 10-K 付費席次水準與員工數不可並列。本卡守恆量是**互動量之人工處理部分 H**（跨買方、跨供應商之流量），不以買方員工數為上界；坐席只作 H 之一個下游計量。
  - **L14-P#2**（`work/20261013_L14-P#2_test1_CL.md`）：預付容量承諾池；死因＝滾存條款 ≥ 2 家不可得。本卡不涉承諾池、RPO。
  - **L14-A**（IT 支出比重）、**L14-A#2**（費用化／資本化）、**L14-I**／**L14-I#2**（採購誘因、裁員 AI 歸因揭露）：本卡不以支出比重、會計分流或揭露誘因為樞紐。
  - **C-A2**（ARCH_dead #9，企業預算單位經濟）：本卡不主張每單位毛利或預算單位經濟。
  - **L9-I#3**（判讀 RVU 時間）、**L11-***（消費者注意力秒數）、**L8-P**（標註工時，已殺）：不涉；本卡之人工時間是企業客服坐席工時，選擇者為企業買方。
- §7-10 領域最近公開：Concentrix 10-Q 期末 2026-08-31（2026-10-07）；Five9 10-Q 期末 2026-06-30（2026-08-06）。下一檢查點＝Five9 3Q26 10-Q（約 2026-11 初）、Concentrix 10-K FY26（約 2027-01）。

## 1. 落差一句

市場分開讀兩條線：外包客服（BPO）已因 AI 自動化而定價下修（Concentrix 3Q FY26 商譽減損 1,050M、管理層稱 AI 部署壓縮傳統業務），而雲端客服平台之坐席仍被讀為隨 CCaaS 營收約 8% 成長。種子主張兩者計量的是同一個人工處理量 H ≡ V × (1 − a)：同一位人工坐席在 BPO 端以工時計費、在 CCaaS 端以坐席計費；若 a 上升而 V 不足以抵銷，H 下降，CCaaS 坐席之成長只能來自「地端 → 雲」遷移份額（有限存量），遷移率趨緩之時點即坐席成長轉負之時點。可拒絕之主張＝在 a 上升期間，CCaaS 坐席淨增 ≤ 遷移份額增量；若 H 持平或上升（V 成長抵銷），本卡死。本卡不主張任何公司營收方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆（P）**：H_t ≡ V_t × (1 − a_t)；H_t ＝ H^{BPO}_t ＋ H^{in-house}_t；雲坐席 S^{cloud}_t ≈ H_t × m_t ÷ 每坐席工時，m＝雲遷移份額。dS^{cloud}/S ≈ dV/V − da/(1−a) ＋ dm/m |
| 選擇者 | 企業買方（自建 vs 外包、地端 vs 雲、AI 自助比例） |
| 可見端 | BPO 10-Q：營收按垂直、重組影響人數、管理層對自動化壓縮之敘述；CCaaS 10-Q／電話會：坐席成長敘述、AI 營收 run rate、訂閱與用量營收；機構調查之 a（自助解決率）與 V |
| 指名不可見端 | 坐席絕對數（Five9 10-Q 2Q26 `seat` 0 筆，只見管理層口述）；m 之逐期值；V 之跨產業總量 |
| 量綱 | 互動數／期、工時、坐席數、無因次比例 a、m |
| 外部參照物（測一查證） | 1990s–2000s IVR／網路自助對話務中心坐席之前例（自助率上升而坐席總數何時轉折） |
| 表達工具型態（只指名，不選券） | 美股 CCaaS 平台普通股、美股 BPO 普通股；不選券 |
| 重疊 | L14-P#1（坐席，但上界不同）、L11（注意力）；重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Concentrix 10-Q 3Q FY26（sec.py）https://www.sec.gov/Archives/edgar/data/1803599/000180359926000155/cnxc-20260831.htm ：「Our revenue decreased by 1.2% for the three months ended August 31, 2026」；Healthcare「145,173 174,106」（−16.6%）；「These actions affected approximately 30,000 employees」；「non-cash goodwill impairment charge of $ 1,050,000」（千美元）。
2. Concentrix 3Q 電話會（MarketBeat 摘要，2026-09-29）https://www.marketbeat.com/instant-alerts/transcript-concentrix-q3-earnings-call-highlights-2026-09-29/ ：CFO 歸因「accelerated AI deployment for clients」、管理層預期「work is compressed」影響 Q4／Q1（轉述，非逐字稿）。
3. Five9 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1288847/000128884726000123/fivn-20260630.htm ：「real-time orchestration engine for every customer interaction across all channels, whether it is with a human or AI agent」；`seat` 0 筆。
4. CX Magazine（2026-05-04）https://cxm.world/customer-experience/five9-reports-125-million-ai-run-rate-new-ceo-pushes-humantic-vision-for-cx/ ：「Five9's actual seat count continues to grow at a rate roughly in line with its 8% CCaaS revenue growth」；CEO Amit Mathradas「As AI replaces seats, those dollars are not leaving the contact centre」；AI run rate「exceeding $125 million」。
5. 待讀：NICE 20-F／6-K（CXone 雲營收、坐席敘述）；第二家 BPO（TTEC、TaskUs 之申報狀態待查）；機構調查之自助解決率 a 序列。

缺段（§7-2）：坐席絕對數之申報序列；m（雲遷移份額）之逐期值；V 之總量。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 「As AI replaces seats, those dollars are not leaving the contact centre」——CCaaS 以 AI 營收承接坐席流失 | #4 Five9 CEO | 坐席 ≠ 營收；守恆在坐席層成立、在美元層不約束 |
| R2 | BPO 之下修已反映於股價與商譽減損，市場已把 a 上升讀進人工量 | #1 | 已定價（至少 BPO 端） |
| R3 | 雲遷移份額 m 仍低、剩餘存量大，dm/m 可長期抵銷 −da/(1−a) | — | 轉折點超出重定價窗 |
| R4 | V 隨 AI 降低互動邊際成本而上升（Jevons），H 未必下降 | — | 守恆成立但方向不定 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 無法就 ≥ 2 家 CCaaS 或 BPO 主體取得 ≥ 4 期同口徑人工量代理（坐席數、計費工時、交付人數或可重算之等價量）；或坐席成長只有管理層口述、無申報或具名第三方數列。
(2) a 或 V 無具名公開序列（≥ 2 個時點），使 H 不可 `[D]` 重算方向。
(3) 公司或具名賣方已就「坐席成長 ＝ 遷移 − AI 壓縮」分解量化（已定價）。
(4) 雲遷移份額 m 之剩餘空間使轉折點落在 > 剩餘實驗期，或 CCaaS AI 營收已大於坐席流失之營收（R1 成立：坐席層守恆對可交易主體無約束）。
(5) 可運作對照只能寫成席次 ≤ 員工數（L14-P#1）、承諾池（L14-P#2）、IT 支出比重（L14-A）、單位經濟（C-A2）或裁員揭露誘因（L14-I#2）。
(6) 重定價窗（≥ 12 個月）內無檢驗事件（CCaaS／BPO 季報、年度坐席或自助率調查）。

複查觸發器（若日後殺）：任一家 CCaaS 首次申報坐席絕對數；具名機構發布自助解決率 a 之年度序列；BPO 揭露計費工時或交付人數序列；CCaaS 坐席成長由正轉負之首次口述。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：BPO 營收（垂直）、重組人數、商譽；CCaaS 訂閱與用量營收、AI 營收、坐席敘述。
2. 可交易工具：CCaaS、BPO 普通股；不選券。
3. 半衰期：季度 10-Q；坐席口述不定期。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0080；`query/ARCH_matrix.md` L14［P］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L14-P#1／#2、L14-A／#2、L14-I／#2、C-A2 結論；不恢復 L11-P／L8-P／L9-P；不寫 T。
