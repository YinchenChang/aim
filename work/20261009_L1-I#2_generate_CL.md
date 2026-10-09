# L1-I#2 生成卡｜能源與電力：誘因（受管公用事業以費率基礎報酬為誘因、依「已簽約大負載」擴建；擱淺風險由最低需量條款轉移之程度不入帳、不揭露）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/INDEX.json；archive/drive/USED_20260926_L1-I_generate_GK.md；archive/drive/USED_20260926_L1-I_test1_GK.md；archive/work/20261008_L1-A#2_generate_CL.md | EMITS: work/20261009_L1-I#2_generate_CL.md -->
**日期：** 2026-10-09　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L1-I　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L1-A#2 已測畢，`work/20261008_L1-A#2_test1_CL.md`）。最後測試日最舊＝2026-09-26 一批（L1-I、L3-P、L3-I、L4-P／A／I、L5-A／I；L1-A 已於 10-08 重測）；同日依表序取 **L1-I**（L1-P 刻意排除 T-11）。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py utility "rate base" "large load" tariff`，命中 0 筆。
- 比對之舊檔與死因型態，本卡須異型：
  - L1-I#1（`archive/drive/USED_20260926_L1-I_generate_GK.md`；測一 `archive/drive/USED_20260926_L1-I_test1_GK.md`）：**發電側**互聯佇列近零成本佔位 → `Q_pub` 高估；死於 `Q_commit` 不可由 ISO 公開檔分離（否決(1)）、近零成本前提在 PJM／MISO 被改革改寫（(2) 部分）。本卡選擇者換為**受管公用事業**（非開發商），誘因為**費率基礎報酬**（非佔位成本），載體為**10-Q 分列之大負載收入行＋州監理費率條款＋LSE 負載預測文件**（非 ISO 佇列）。L1-I#1 生成卡明示「大負載佇列＝滑到 L2-I」；本卡不以大負載**申請量**為落差，只用已簽 ESA 作分母，落差在**擱淺風險之歸屬**。
  - L2-I#1／L2-I#2：開發商／REIT 之許可撤回損失歸屬；DLR JV promote。本卡主體為受管電業，損失承擔者為股東 vs 其他費率類別，非 REIT 租戶。
  - L6-I（backlog 變厚 ≠ 對手方變好）：雲端 RPO。本卡相近處＝「已簽 ≠ 已實現」；相異處＝本卡之合約**不入 RPO**（Dominion 10-Q：無多年期合約之未來收入），風險移轉由費率條款而非合約餘額表達。重疊須於測一判讀，不得合併。
  - L1-A#1／#2（PPA 鎖價存量；Bloom 收入認列時序）、T-11（物理層方向負）、C-P4（水）：構成不同。
- §7-10 領域最近公開：Dominion 2Q26 10-Q（至 2026-06-30，acc `0001193125-26-327487`，2026-07-31）；Dominion 對 PJM LAS 之負載預測文件（2026-09-29，合約至 2026-07）；AEP 2Q26 10-Q（acc `0000004904-26-000059`）。下一檢查點＝Dominion／AEP 3Q26 10-Q（約 2026-10 底／11 初）與 PJM 2027 負載預測定稿。

## 1. 落差一句

受管電業之盈餘＝核准 ROE × 費率基礎，故**誘因**是把資本計畫建立在「已簽約大負載」上；擱淺風險名義上由大負載費率之最低需量（Dominion GS-5 類：輸 85%／配 85%／發 60%，14 年；AEP Ohio：85%，至多 12 年，4 年爬坡）轉移給資料中心客戶——但此承諾**不入 RPO**、爬坡期內不全額生效、發電段只 60%，且履約取決於簽約實體之信用與擔保；**落差＝市場把 ESA GW 讀成「受保護之費率基礎成長」，而最低需量覆蓋率（承諾現值 ÷ 該負載所致增量收入需求）與擔保形式在公開層不可見，未覆蓋部分落回其他費率類別或股東（費率案不准列）**。**方向未定**：若覆蓋率接近 1，落差不存在。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因（Averch-Johnson 型：報酬依資本 → 偏好依合約負載擴建；風險移轉以費率條款而非資產負債表承載） |
| 選擇者 | 受管電業（是否依 ESA／CLOA／ELOA 擴建輸配與發電）；州監理（最低需量比例、年限、擔保要求）；資料中心客戶（以何實體、何擔保簽約） |
| 可見端 | Dominion 10-Q Note 3「High load」收入行（定義：≥ 25 MW 且年負載率 ≥ 75%）2Q26 814 vs 2Q25 422（百萬）；同附註「無多年期合約之未來收入」；PJM LAS 文件：ESA 11,997 MW、CLOA 9,356 MW、ELOA 32,473 MW（59% 不入預測）、爬坡 5 年成熟利用率 63%；SCC GS-5 與 PUCO AEP Ohio 費率條款 |
| 指名不可見端 | 每 ESA 之擔保形式／金額與簽約實體信評；最低需量承諾現值；資料中心驅動資本支出之增量收入需求；實際利用率對 63% 之逐 cohort 序列 |
| 主張 | 覆蓋率 < 1 且未覆蓋部分不在任何申報科目 ⇒ 公用事業「受管成長」之風險被低估；觸發事件＝ESA 終止／降約、爬坡不及、費率案中之不准列或跨類別分攤爭議 |
| 表達工具型態（只指名，不選券） | 美股上市、資本計畫以大負載為主驅動之受管電業或其控股公司。不選券 |

對照式（生成用，非正式載入）：`Cov = PV(min-bill × 契約 MW × 年限) ÷ ΔRR_DC`；`Exposure = (1 − Cov) × ΔRR_DC`。`Cov → 1` 時本卡落差消失。本輪不估參數、不寫 H1。

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| Dominion 2Q26 10-Q Note 3（High load 收入行、RPO 句） | https://www.sec.gov/Archives/edgar/data/715957/000119312526327487/d-20260630.htm |
| Dominion 對 PJM LAS 負載預測文件（ESA／CLOA／ELOA、63% 利用率） | https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/las/2026/20260929/20260929-item-5ai---dominion_energy.pdf |
| SCC 2025-11 雙年審查終局令（GS-5 類條款；ROE 9.8%）；報導錨 | https://virginiamercury.com/2025/11/25/scc-approves-chesterfield-gas-plant-and-dominion-rate-hike-creates-new-rate-class-for-data-centers/ （測一須回 SCC 原令） |
| PUCO 2025-07-09 AEP Ohio 資料中心費率令（85%／12 年／4 年爬坡）；報導錨 | https://www.powermag.com/regulator-approves-aep-ohios-landmark-data-center-tariff/ （測一須回 PUCO 原令與 AEP Ohio 費率表） |
| AEP 2Q26 10-Q（資料中心預測不確定性風險句） | https://www.sec.gov/Archives/edgar/data/4904/000000490426000059/aep-20260630.htm |
| 季度 ESA GW 時序（Dominion 財報簡報；第二手錨） | https://www.marketbeat.com/instant-alerts/dominion-energy-q2-earnings-call-highlights-2026-07-31/ ；https://datacenterdynamics.com/en/news/dominion-energy-nearly-doubles-data-center-capacity-under-contract-to-40gw |

不宣稱覆蓋率已知、不宣稱擔保不足、不宣稱任何 ESA 已終止。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 最低需量＋長約＋退出費正是為完全轉移成本而設；監理已明示「成本由造成者承擔」 | PUCO 2025-07-09 令（Power Magazine 報導）；SCC GS-5 令 | `Cov ≈ 1` → 無落差 |
| R2 | 反方向：成本轉嫁其他費率人是**已知且已被廣泛論述**，非未定價 | Harvard ELI, Peskoe & Martin, *Extracting Profits from the Public*（2025-03）https://eelp.law.harvard.edu/wp-content/uploads/2025/03/Harvard-ELI-Extracting-Profits-from-the-Public.pdf | 機制成立但非錯價；且受損方為費率人而非股東 |
| R3 | 公用事業本身已以 63% 成熟利用率、59% ELOA 排除折減預測，市場讀的不是毛 GW | PJM LAS Dominion 文件 2026-09-29 | 「市場讀 ESA GW」前提可能錯 |
| R4 | 費率基礎報酬與資本回收由監理保障；擱淺成本歷史上多經 securitization 回收，股東端損失有限 | 監理實務 | 量級不足 H1 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) 實讀 SCC GS-5 原令／Dominion 費率表與 PUCO 原令／AEP Ohio 費率表後，最低需量＋擔保＋退出費按其文字已涵蓋該負載之全部增量資本回收（`Cov ≥ 1` 於條款層可證），且爬坡期另有擔保。
- (2) `Cov` 之分子或分母在公開層皆不可得（擔保、承諾現值、DC 驅動資本支出均未分列），且 High load 收入行無法與 ESA MW 同窗對帳成實現率序列（≥ 2 期）。
- (3) 最近 ≥ 4 季無 ESA 終止／降約、爬坡落後或費率案不准列之公開事件，且公用事業預測已按實現率折減（R3 成立），使「市場讀毛 GW」不可辨。
- (4) 本卡只能以 L2-I 之開發商撤回損失、L1-I#1 之佇列灌水、或 L6-I 之 backlog 對手方品質重述（重疊判讀）。
- (5) 未覆蓋部分依令文明定由其他費率類別承擔、股東無承擔路徑（R2＋R4），使落差不落在任何美股可交易主體。

複查觸發器（若日後殺）：任一美股上市受管電業於 10-K／10-Q 或費率案文件分列大負載客戶之擔保金額／形式、最低需量承諾現值、或資料中心驅動之資本支出，使 `Cov` 可重算；或發生首例 GS-5／AEP Ohio 資料中心費率下之 ESA 終止與退出費結算。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：最低需量承諾、擔保、退出費能否在附註拆出；High load 收入行是否持續分列。
2. 可交易工具：未覆蓋風險落在股東（不准列）還是費率人；前者才有美股表達。
3. 半衰期：爬坡 4–5 年＋契約 12–14 年；觸發事件是否在 ≥ 12 個月窗內可見。

## 7. 本輪寫入

本卡；QUEUE 新列（ANALYST 測一）；ARCH_matrix L1-I 格標「已生成 #2」；FUNNEL §3 未測格計數。不改 L1-I#1／L1-A#1／L1-A#2／L2-I／L6-I／T-11／C-P4。
