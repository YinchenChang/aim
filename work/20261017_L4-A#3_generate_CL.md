# L4-A#3 生成卡｜運算硬體系統：會計恆等（客戶認股權證之收入減項：報告收入＝帳單額 − 已歸屬權證公允價值；權證價值隨發行人股價上升）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260926_L4-A_generate_GK.md；archive/drive/USED_20260926_L4-A_test1_GK.md；archive/work/20261011_L4-A#2_generate_CL.md；work/20261011_L4-A#2_test1_CL.md；work/20261011_L4-I#2_test1_CL.md | EMITS: work/20261017_L4-A#3_generate_CL.md -->
**日期：** 2026-10-17　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain）　**格：** L4-A　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L4-P#3 本日已測一）。最後測試日最舊＝2026-10-11（L4-A／I、L5-P／A／I、L6-P／A／I、L13-A）；依表序取 **L4-A**；非已殺、非刻意排除。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py warrant "contra revenue" AMD OpenAI`，命中 26 筆，皆為 OpenAI 模型價格／速度／需求與 Supermicro 保固（SRC_PERF、SRC_PRC、SRC_DEM、SRC_DC_016），**與本機制無關，未採用**。
- 比對之舊檔與死因型態，本卡須異型：
  - **L4-A#1**（`archive/drive/USED_20260926_L4-A_generate_GK.md`）：損益之 BOM 份額恆等；死於 BOM 不在申報層。本卡不涉 BOM，所需量（收入減項、權證分類、歸屬條件）為申報附註項。
  - **L4-A#2**（`archive/work/20261011_L4-A#2_generate_CL.md`）：整機商營運資本 CCC 恆等；本卡為加速器商之**收入計量**恆等，非現金流量表。
  - **L4-I#2**（`work/20261011_L4-I#2_test1_CL.md`）：把 AMD 權證當作「以或有負債代替降價」之**誘因**檢視，判定其歸屬綁採購量與股價、不綁 GPU 租價（(4) 未觸發）；**未檢視其會計計量路徑**。本卡物件＝ASC 606 對「應付客戶之對價」之收入減項與負債分類下之重評價——會計恆等，非誘因。重疊照記，不構成丟棄。
  - **L13-I**（擔保／違約路徑）、**C-I3′**（分部毛利由非機制項解釋）、**N-01**、**N-02**：構成不同。
- §7-10 領域最近公開：AMD 2Q26 10-Q（期末 2026-06-27，申報 2026-08-05）：「no warrant shares had vested or become exercisable, and the warrants had no impact」。下一檢查點＝AMD 3Q26 財報／10-Q（約 2026-11 初）；MI450 首個 1 GW 部署（首批歸屬條件）。

## 1. 落差一句

AMD 於 2025-10 與 2026-02 對 OpenAI、Meta 各發 160M 股、行權價 $0.01 之權證，「vest in tranches based on specified AMD Instinct GPU purchase milestones … and achievement of specified stock price targets」，且「will be classified as liabilities until certain conditions for equity classification are met」（2Q26 10-Q）。在 ASC 606「應付客戶之對價」下，歸屬之權證公允價值通常沖減交易價格，故 **報告 DC GPU 收入 ≈ 帳單額 − 歸屬權證公允價值**；因歸屬本身綁股價門檻、且負債分類需逐期重評，**AMD 股價越高 → 越多批次歸屬、每股價值越高 → 收入減項越大**。落差＝市場（共識收入／毛利模型）若以帳單額或 non-GAAP 讀 AMD 之 MI450 收入，則首批歸屬後之 GAAP 收入與毛利可能與預期顯著不同；反之若 AMD 將其排除於 non-GAAP 且市場只讀 non-GAAP，則落差不存在。**方向未定**；減項落入收入或營業外（重評價），本卡不預設。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（收入計量）：`Rev_reported = Billing − Σ_tranche 1[vested] × N_tranche × FV(P_AMD)`；非守恆、非誘因 |
| 量綱 | `N`［股］× `FV`［$／股，≈ 股價 − 0.01］＝［$］；對照 `Billing`［$］＝ GW × $／GW。減項／帳單比無量綱 |
| 可見端 | AMD 2Q26 10-Q Note（Warrants）：權證條款、負債分類、尚未歸屬；MD&A：「each customer intends to deploy up to 6 gigawatts」「first gigawatt … MI450」；8-K（OpenAI 2025-10、Meta 2026-02）：歸屬階梯與 $600 終批股價門檻 |
| 指名不可見端 | 各批次之 GW 對應與股價門檻全表；公允價值模型（蒙地卡羅）參數；減項在收入與營業外之切分；non-GAAP 是否排除；共識模型是否含減項 |
| 主張 | 報告收入與毛利對 AMD 自身股價有機械性負彈性（在權證存續與歸屬期內）；此彈性若未入共識，首批歸屬季之 GAAP 讀數將偏離 |
| 外部參照物（測一查證） | 前例：供應商對 Amazon／Walmart 發權證而以收入減項入帳（如 Plug Power FY2020 重編後之負收入）。僅作會計路徑之先例，非量級 |
| 表達工具型態（只指名，不選券） | 美股上市加速器商普通股與上市選擇權。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| AMD 2Q26 10-Q（Warrants 附註、MD&A 6 GW 敘述） | https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm |
| AMD 8-K（OpenAI 權證，2025-10-06） | https://www.sec.gov/Archives/edgar/data/2488/000119312525230895/d28189d8k.htm |
| AMD 8-K（Meta 權證，2026-02-24） | https://www.sec.gov/Archives/edgar/data/2488/000000248826000045/amd-20260223.htm |
| SemiAnalysis 權證模型（轉載；以「rebate on GPU capital cost」計，未談會計） | https://www.kucoin.com/fr/blog/ae-semi-analysis-amd-meta-openai-warrant-deals-could-slash-gpu-costs-near-zero |
| AMD 3Q26 10-Q／法說（約 2026-11 初；首批歸屬、non-GAAP 處理） | 測一以 `sec.py filings AMD` 取得 |
| 前例：Plug Power 10-K／10-K/A FY2020（權證收入減項） | 測一以 `sec.py` 取得 |

不宣稱減項已入或未入共識、不宣稱方向。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 權證之經濟效果已被具名機構公開建模（GPU 成本折讓） | SemiAnalysis（轉載 2026-08） | 落差已揭露（僅經濟面；會計面待查） |
| R2 | AMD 將權證費用排除於 non-GAAP，市場只讀 non-GAAP，GAAP 減項不影響定價 | 測一查 AMD 法說／non-GAAP 調節 | 落差不存在 |
| R3 | 負債分類下之重評價入營業外，非收入；收入減項只在歸屬時以當時價值一次入帳，無持續反身性 | 測一查 AMD 會計政策附註 | 機制弱化 |
| R4 | 減項量級相對 AMD DC 收入小，或首批歸屬落在 12 個月窗外 | 測一以 8-K 階梯 × 股價估 `[D]` | 量級不足／窗不足 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) AMD 申報或法說已明言權證之收入減項計量方法並給出量級或 non-GAAP 排除口徑（R2），或 ≥ 1 位具名賣方已將減項納入 GAAP 收入／毛利模型。
- (2) 會計政策顯示重評價變動入營業外而非收入（R3），使「股價 → 收入」之連動只剩歸屬當期一次性。
- (3) 首批（1 GW MI450）歸屬在 12 個月內不構成 probable，或公開層無法判定歸屬時點。
- (4) `[D]` 量級：測一自定門檻（如 12 個月窗內預期減項 ÷ AMD Data Center 分部收入），低於門檻即否決。
- (5) 本卡只能以 L4-I#2（權證作為讓價誘因）、L13-I（擔保違約）或 C-I3′ 重述（重疊判讀）。
- (6) 前例（Plug Power 等）顯示市場於首次大額減項時未重定價，或前例會計路徑與 AMD 條款（負債分類、股價門檻）不可比。

複查觸發器（若日後殺）：AMD 首次揭露權證歸屬或收入減項金額；non-GAAP 口徑變更；新增他家加速器商對客戶發行權證；SEC 對應付客戶之股份對價發布新指引或意見信。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：收入（減項）、毛利率、權證負債（Other long-term liabilities）、重評價（Other income／expense）、non-GAAP 調節表。
2. 可交易工具：美股上市加速器商普通股與上市選擇權（不選）。
3. 半衰期：季（歸屬按 GW 里程碑；重評價逐季）；權證存續至 2030-10／2031-02。

## 7. 本輪寫入

本卡；QUEUE 新列（ANALYST 測一）；ARCH_matrix L4［A］格標「#3 已生成」；FUNNEL §3 未測格計數。不改 L4-A#1／#2、L4-P#1–#3、L4-I#1／#2、L13-I、C-I3′、N-01、N-02。
