# L2-P#4 生成卡｜資料中心實體：守恆（設施邊界功率守恆之口徑——P_grid ≡ P_IT × PUE ＋ 冗餘／輔助；公告「MW」混用電網接入量、可交付電力與 critical IT 負載，跨主體以 MW 加總或比價時量綱不一）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/work/20261007_L2-P#2_generate_CL.md；work/20261007_L2-P#2_test1_CL.md；archive/work/20261014_L2-P#3_generate_CL.md；work/20261014_L2-P#3_test1_CL.md；work/20261011_L6-P#2_test1_CL.md | EMITS: work/20261021_L2-P#4_generate_CL.md -->
**日期：** 2026-10-21　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 1→2／6）　**格：** L2-P　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L14-A#3 測一本日，Q-0081 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-14 之六格（L2-P#3、L2-A#3、L14-I#2、L15-P／A／I#2；git 加入時刻相同），依表序取第一 → **L2-P**。既有生成 #1–#3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `contracted power active MW backlog`，9 筆，無一涉 MW 口徑（SRC_DC_014 為每 IT MW 資本支出，非本機制）；未用。
- 比對（本卡須異型）：
  - **L2-P#1**（PUE 受濕球封頂）：PUE **水準**之物理上界。本卡不主張 PUE 高低，只用 PUE 作口徑換算因子；樞紐是**申報 MW 之定義**。
  - **L2-P#2**（`work/20261007_L2-P#2_test1_CL.md`）：每櫃 kW 受介質封頂（空間密度）。不涉。
  - **L2-P#3**（`work/20261014_L2-P#3_test1_CL.md`）：時域功率擺盪。本卡為穩態容量口徑。
  - **L6-P#2**（`work/20261011_L6-P#2_test1_CL.md`）：RPO 之電力-時間預算（ρ＝每 MW 營收）；死因為 ρ 無申報值。本卡不用 RPO 或 ρ；惟 L6-P#2 之 MW 分母口徑即本卡之問題——重疊不構成丟棄，本卡須獨立可測。
  - **L2-I#3**（設備可取消訂單）、**L1-I#2**（大負載費率）、**C-P4**（ARCH_dead #19，水）：不涉。L1-P 刻意排除（T-11）：本卡不涉發電或燃料。
- §7-10 領域最近公開：IREN 10-K FY26（2026-06-30 期）；APLD 10-K FY26（2026-05-31 期）；CRWV、WULF 10-Q（2026-06-30 季）。下一檢查點＝各家 2026-09-30 季 10-Q（2026-11）。

## 1. 落差一句

能量守恆於設施邊界：電網接入功率 \(P_{grid} \equiv P_{IT}\times PUE_{design} + P_{aux}\)，加上冗餘（N+1／2N）使可租售之 critical IT MW 系統性小於接入 MW（因子約 1.3–1.6）。主體以不同口徑公告「MW」（電網接入協議、可交付電力、critical IT），市場以 GW 管線加總、EV／MW、$／MW 跨主體比價時若混用，管線被高估一個 PUE 量級之因子。可拒絕之主張＝樣本中 ≥ 2 家之頭條 MW 為接入／電力口徑而另 ≥ 2 家為 critical IT 口徑，且具名賣方或聚合者跨口徑加總或比價而未換算。若各家申報已並列兩口徑、或賣方已換算，本卡死。本卡不主張任何主體價值方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆（P）**：(i) \(P_{grid} \equiv P_{IT}\cdot PUE + P_{aux}\)；(ii) \(P_{IT}^{sellable} = P_{IT}^{installed}/r\)，\(r\)＝冗餘因子；(iii) 口徑換算 \(k \equiv MW_{grid}/MW_{IT} \approx PUE\cdot r\)；(iv) 跨主體比價誤差＝\(k_A/k_B\) |
| 選擇者 | 發行人（頭條 MW 之口徑）；賣方／聚合者（是否換算） |
| 可見端 | 10-K／10-Q 業務段之 MW 文字（「grid connection agreements … approximately 5GW of total power capacity」vs「critical IT load」vs「MW of electrical power remained undelivered」）；租約附註之 MW；設計 PUE（若揭露） |
| 指名不可見端 | 各站設計 PUE 與冗餘級；接入協議之可用率與分期；賣方模型之 MW 口徑 |
| 量綱 | MW（電）；\(k\) 無因次；$／MW（須同口徑） |
| 外部參照物（測一查證） | Uptime Institute 2025 全球調查 PUE 均值 1.54（次級標題，[mgrid](https://mgrid.org/2025/10/01/uptime-institute-data-center-pue-stagnation-2025-liquid-cooling/)；原報告 [UII 180](https://intelligence.uptimeinstitute.com/resource/uptime-institute-global-data-center-survey-2025) 未讀） |
| 表達工具型態（只指名，不選券） | 美股、以 MW 管線為主要估值錨之資料中心開發／轉型主體普通股；不選券 |
| 重疊 | L6-P#2（MW 分母）；L2-P#1（PUE） |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. IREN 10-K FY26（sec.py）https://www.sec.gov/Archives/edgar/data/1878848/000187884826000052/iren-20260630.htm ：「executed grid connection agreements, letters of agreement or equivalents representing approximately 5GW of total power capacity」；「operating AI Cloud Services capacity represented approximately 40MW」（口徑未述）；全文「PUE」0 筆、「IT load」1 筆（RSU 里程碑「fully operational IT load」）。
2. Applied Digital 10-K FY26（sec.py）https://www.sec.gov/Archives/edgar/data/1144879/000114487926000048/apld-20260531.htm ：「approximately 100 MW of critical IT load」；「15-year lease … for 200 MW of critical IT load」；「Delta Forge 1, a 300 MW critical IT load campus」。
3. TeraWulf 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1083301/000108330126000166/wulf-20260630.htm ：「energized 81 critical IT MW of HPC leasing capacity」；「168 MW critical IT load datacenter campus in Abernathy」。
4. CoreWeave 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm ：「393 MW of electrical power remained undelivered at the site」；「355 MW of electrical power remains undelivered」（電力口徑，未述 IT／接入）；「active power」0 筆。

缺段（§7-2）：未取具名賣方或聚合者跨主體 GW 加總／EV／MW 原文；未查 DLR／EQIX 之 MW 口徑（IT vs utility）；各站設計 PUE 未揭露（IREN 0 筆）；IREN 40MW 之口徑未定。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 賣方模型以 critical IT MW 為單位並自行換算接入量 | 待測一取具名賣方原文 | 已定價 |
| R2 | 接入協議 MW 本為選擇權性質，市場本已對管線大幅折價（可用率、分期），PUE 因子淹沒於折價 | 待測一 | 量級不可分離 |
| R3 | 液冷新建站設計 PUE 降至 ~1.1–1.2，\(k\) 收斂，誤差小 | Uptime 趨勢（§2 參照物） | 量級不足 |
| R4 | 租約與營收以 critical IT 計價，接入 MW 不入損益，口徑差異不進財報科目 | §3-2、§3-3 | §7-4 財報科目題不成立 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後樣本中以接入／電力口徑公告頭條 MW 者 < 2 家，或以 critical IT 口徑者 < 2 家（口徑實已一致）；或
(2) 各家申報已於同檔並列兩口徑或揭露設計 PUE／換算因子，使 \(k\) 可由公開原文直接取得（無資訊落差）；或
(3) 具名賣方、評等機構或聚合者原文已按 critical IT 換算後加總或比價（R1，已定價）；或未能取得任何跨口徑加總／比價之具名原文（落差無市場端）；或
(4) 可運作對照只能寫成 PUE 水準上界（L2-P#1）、kW／櫃（L2-P#2）、功率擺盪（L2-P#3）、RPO 電力-時間預算（L6-P#2）或費率（L1-I#2）；或
(5) 12 個月內無檢驗事件（10-Q／10-K 口徑變更、接入量轉 critical IT 之交付公告、賣方口徑更正）；或
(6) `[D]` 樣本之 \(k\) 跨主體差異 < 1.2 倍（R3，量級不足）或口徑差異不進任何財報科目且無可交易表達（R4）。

複查觸發器（若日後殺）：任一主體於 10-K／10-Q 首次並列接入 MW 與 critical IT MW；SEC 意見函就 MW 口徑提問；具名賣方發布 MW 口徑更正。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：業務段 MW 文字、租約附註 MW、PP&E 在建分期。2. 可交易工具：以 MW 管線為估值錨之主體普通股（不選）。3. 半衰期：接入轉交付之分期（季至 3 年）；10-Q 每季。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0082；`query/ARCH_matrix.md` L2［P］加「#4 已生成」；`AIM_FUNNEL.md` §3 一句與日期行。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L2-P#1–#3、L2-A／#2／#3、L2-I／#2／#3、L6-P#2、L1-I#2、C-P4；不碰 L1-P（刻意排除）；不寫 T。
