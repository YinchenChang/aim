# L13-A#6 生成卡｜資本與融資結構：會計恆等（未部署募集現金之利息收入遞減：淨利息 ≡ 利息發生額 − 資本化利息 − r × 未部署募集現金；預先募足之 AI 資料中心建置資金於部署前以存款／短債孳息，抵銷利息費用；隨 capex 付出，第三項機械遞減，與利率路徑無關）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；AIM_FUNNEL.md；archive/drive/USED_20260928_L13-A_generate_GK.md（首行）；archive/work/20261011_L13-A#2_generate_CL.md；archive/work/20261020_L13-A#3_generate_CL.md；archive/work/20261026_L13-A#4_generate_CL.md；archive/work/20261103_L13-A#5_generate_CL.md；work/20261103_L13-A#5_test1_CL.md；work/20261026_L13-A#4_test1_CL.md；L2-A#2、L3-A#5、L2-A#6、L13-P#3 生成卡首行 | EMITS: work/20261114_L13-A#6_generate_CL.md -->
**日期：** 2026-11-14　**角色：** SCOUT@CL（排程 SCOUT-GEN，pick 配額 2→3／6）　**格：** L13-A　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額配置、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L11-I#6 已於 2026-11-14 測一，Q-0199 done）。非已殺／刻意排除格中最後測試日最舊＝**L13-A**（#5 測一 2026-11-03；次舊 L13-P／L13-I／L14-*／L15-P 之 2026-11-04）。既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py "interest income" convertible proceeds`，**命中 0 筆**。內部數字（§12）未取用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L13-A#1**（T 不進 L：未開始租／RVG／專案槓桿 vs 合併槓桿）：本卡不涉表外義務上界。
  - **L13-A#2**（客戶預付之融資成分入 OCF）：本卡不涉客戶端現金。
  - **L13-A#3**（EPS 分母）、**L13-A#4**（可轉債全成本：capped call、誘導轉換）：本卡不論股數，也不論利息費用**低估**全成本；物件為利息**收入**側之抵銷項及其遞減。
  - **L13-A#5**（子公司可贖回優先 NCI；死因 (3)＝同型工具只見一家）：本卡須先驗**可推廣性**（否決 (3)），對照組至少兩家。
  - **L2-A#2／L3-A#5**（利息資本化）：資本化項於恆等中只作並列項；本卡不以資本化率或轉固翻轉為落差，若測一發現落差主要來自資本化停止，即觸發否決 (5)。
  - **L2-A#6**（以認股權支付第三方信用支撐之遞延費用）：本季 WULF／CIFR 淨利主要來自認股權負債公允值變動，本卡**不**以此為落差，只作「淨利不可讀」之背景。
  - **L13-P#2／#3**（現金掃款、母公司現金封閉）、**L13-I#3**（依評等債務含量選工具）：本卡不論現金取用優先序或工具選擇。
  - **L6-A#4**（capex 現金流分類）、**L7-A#2**（持股公允值）、**L12-A#3**（稅務時序）：不涉。**T-15**：不寫。
- §7-10 領域最近公開：WULF 10-Q（期末 2026-09-30，申報 2026-11-06）；CIFR 10-Q（期末 2026-09-30，申報 2026-11-02）。下一檢查點＝兩家 10-K FY2026（約 2027-02／03）。
- SEC：`tools/sec.py` 本輪仍被宿主隱私外掛拒絕（同 `work/20261114_HEALTH_CL.md` 第 1 項）；10-Q 原文未實讀，數字多為二手或工具摘要，測一須實讀或記「無法判定（失敗歸因：宿主）」。

## 1. 落差一句

為 AI 資料中心建置**預先**募足可轉債與有擔保票據之開發商，部署前之現金與受限現金孳息，在損益表上抵銷利息費用；恆等：
`淨利息費用_t ≡ 利息發生額_t − 資本化利息_t − y_t × C_t`，`C_t ≡ C_{t−1} ＋ 新募集_t − capex 付現_t − 償債_t`。
在無新募集時，`y × C` 隨 capex 付出**機械遞減**，與利率路徑分開（利率只改 y）。種子載體（TeraWulf Q3 2026；期末 2026-09-30）：
- 資產負債表（capital.com 轉載新聞稿，千美元，逐字）：Cash and cash equivalents 1,602,127（2025-12-31：3,266,389）；Restricted cash, current 486,702（189,933）；non-current 266,491（266,453）；Long-term debt 3,032,094；Convertible notes 1,627,342；Short-term convertible notes 491,544。
- 損益（247wallst 逐字）：「Interest expense reached $53.6 million in the quarter, compared with $9.8 million a year earlier」；利息收入 28.6（fourweekmba「partly offset by $28.6 million of interest income」——**工具摘要層，非逐字**；capital.com 摘要層 9M 利息收入 86,947 vs 利息費用 177,014，同屬摘要）。
- `[D]`（待測一以 10-Q 原文核）：Q3 利息收入 ÷ 利息費用 ≈ 28.6 ÷ 53.6 ≈ 0.53；利息收入 ÷ 營收 76.2 ≈ 0.38；非受限現金九個月 −1.66 bn（−51%）。
- 對照（CIFR）：Q1 2026 interest income 31.59M（opencapital.sh，轉述 2026-05-05 10-Q，二手）；Q3 2026「Interest expense rose to $59.0 million」、「Pro forma unrestricted cash fell to about $724 million from $832 million」（Earnings Whispers 經 finviz）；Q3 利息收入未取得。
種子主張：以「淨利息」、「利息費用淨額」或以未部署現金計之淨負債讀融資負擔者，把一個隨建置進度歸零之抵銷項當作持續項。本卡不主張方向或量級，只立可拒絕之恆等與其遞減路徑可由已申報之 capex 承諾事前推算。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（利息收入與利息費用分列；ASC 835-20 資本化只對利息費用、不得以利息收入抵減〔一般借款〕之處理差異列為測一必問）；非守恆、非誘因 |
| 量綱 | 利息收入、利息費用、資本化利息［$／季］；C（現金＋受限現金）［$］；y＝利息收入 ÷ 平均 C［%／年］；ρ＝利息收入 ÷ 利息費用［無量綱］；剩餘 capex 承諾［$］ |
| 可見端 | 10-Q／10-K 損益表 Interest income／Interest expense、利息資本化附註、現金與受限現金、capex 承諾附註、MD&A 流動性段（剩餘建置成本、資金來源）；非 GAAP 調節中利息收入之處理 |
| 指名不可見端 | C 中已承諾於特定工程之比例；受限現金之用途（利息準備、工程託管）與其孳息歸屬；未來募集之時點 |
| 主張 | 已申報之 capex 承諾與 C 可推出 12 個月內 `y × C` 之下界路徑；若主流口徑（共識、評等、公司非 GAAP）以淨額讀利息，即錯置。可由「主流已逐項分列並預測遞減」或「量級不足」或「C 由滾動募集維持不降」拒絕 |
| 外部參照物（測一查證） | 先募後建之同型前例（例：2021–2023 SPAC／IPO 募資後之 EV、太空、生技公司利息收入隨燒錢遞減之一手揭露；公用事業建置期之 AFUDC 借款部分以短期投資收益抵減之規則〔FERC〕作會計路徑先例） |
| 表達工具型態（只指名，不選券） | 美股上市 AI 資料中心開發商／HPC 託管商普通股、可轉債（WULF 為主載體；CIFR、IREN、APLD、CORZ、GLXY、HUT 為待查對照）。不選券 |
| 重疊 | L2-A#2、L3-A#5（資本化）、L13-A#4（全成本）、L13-P#3（現金封閉）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. WULF 10-Q（期末 2026-09-30）https://www.sec.gov/Archives/edgar/data/1083301/000162828026071671/wulf-20260930.htm ——本輪未實讀（§0）。
2. CIFR 10-Q（期末 2026-09-30）https://www.sec.gov/Archives/edgar/data/1819989/000181998926000050/cifr-20260930.htm ——本輪未實讀。
3. capital.com 轉載 WULF Q3 2026 新聞稿 https://capital.com/en-ae/news/terawulf-reports-third-quarter-2026-results ：資產負債表逐字（§1）；「Ended the quarter with approximately $2.4 billion of cash, cash equivalents and restricted cash」；淨利 709.9M「benefiting from a non-cash change in fair value of warrants」。頁面截斷，損益行為摘要層。
4. 247wallst https://247wallst.com/cards/terawulf-q3-2026-earnings-wulf-01m6rdt7bk68j2t95rvrc7bqpa ：利息費用 53.6M、總債務約 5.8 bn（可轉 2.5、有擔保 3.2）。二手。
5. fourweekmba https://fourweekmba.com/ai-terawulfs-710m-profit-came-from-warrants-ops-lost-88m/ ：利息收入 28.6M（摘要層）。二手。
6. Earnings Whispers 經 finviz https://finviz.com/news/414953/cipher-digital-beats-on-eps-but-misses-badly-on-revenue-as-backlog-grows-and-costs-leverage-and-leasing-delays-mount ：CIFR 利息費用 59.0M、總債務約 6.7 bn、pro forma 非受限現金 ~724M。二手。
7. opencapital.sh https://www.opencapital.sh/stocks/cifr/metrics/interest_income ：CIFR Q1 2026 利息收入 31.59M；頁標「Discontinued — last reported Q1 '26」。二手。
8. 讀取失敗（非存在性主張，§7-2）：financialcontent.com WULF 新聞稿（SERVER_ERROR）；investors.cipherdigital.com 靜態檔（RTF 二進位，無文字）。

缺段（§7-2）：兩家 10-Q 原文之利息收入行、資本化利息、受限現金用途、剩餘 capex 承諾；CIFR Q3 利息收入；具名賣方模型之利息收入預測；公司非 GAAP 口徑是否含利息收入。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 利息收入與費用分列於損益表，任何讀者可見；賣方建模本即逐項 | #3、#4、#5 | 已定價 |
| R2 | 公司持續滾動募集（WULF 2026 多次發債／可轉），C 不降 | #4 | 機制自消 |
| R3 | 本季淨利由認股權公允值主導（WULF +728M、CIFR +127M），利息收入相對不重大 | #3、#6 | 量級 |
| R4 | 受限現金屬利息準備／工程託管，其孳息依契約歸屬，非自由抵銷 | #3 | 可分離性 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 公司指引或具名賣方已逐項預測利息收入並隨 capex 時程遞減（R1）——已定價。
(2) `[D]` 12 個月內利息收入之機械遞減額（以 10-Q capex 承諾與 C 推，y 固定於最近一季）÷ 次 12 個月營收指引或共識 < **5%**——不重大（R3）。**門檻凍結於此。**
(3) 對照組（CIFR、IREN、APLD、CORZ、GLXY、HUT）最新一季中，ρ ≥ 0.25 者少於 **2** 家（不含 WULF）——單一主體，不可推廣（L13-A#5 死因）。**先驗本條。**
(4) 最近三季 C（現金＋受限現金）未下降，或公司已公告之募集足以於 12 個月內補回 capex 付出（R2）——機制自消。
(5) 實讀後落差主要只能寫成利息資本化停止（L2-A#2／L3-A#5 型）、可轉全成本（L13-A#4 型）、現金封閉（L13-P#3 型）或認股權公允值（L2-A#6 型）。
(6) 利息收入多數來自受限現金且契約上專用於償債或工程（R4），使其與利息費用為同一融資之內部淨額，非可遞減之抵銷項。

複查觸發器（若日後殺）：對照組任一家單季 ρ 由 ≥ 0.25 降至 < 0.10；具名賣方首次分列利息收入遞減；WULF 或 CIFR 10-K FY2026 新揭露剩餘 capex 承諾大於 C。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Interest income、Interest expense、資本化利息、現金與受限現金、capex 承諾附註、非 GAAP 調節。
2. 可交易工具：AI 資料中心開發商普通股與可轉債。不選券。
3. 半衰期：按季（10-Q）；完工起租節點依各租約交付時程。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0200；`query/ARCH_matrix.md` L13［A］標「#6 已生成」；`AIM_FUNNEL.md` §3「已生成未測」與日期行。不寫入：INDEX.json、ARCH_dead、RETRIG、ARCH_live、LEADS（本輪實讀之 AI 算力類數值〔WULF HPC 租賃收入〕已於 2026-11-07 登錄，不重複）。不改 L13-A#1–#5、L13-P、L13-I、L2-A#2、L2-A#6、L3-A#5 結論；不寫 T-15。
