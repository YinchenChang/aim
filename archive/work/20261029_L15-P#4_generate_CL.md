# L15-P#4 生成卡｜基礎設施軟體與資料：守恆（位元組單一駐留守恆：一份表資料只駐留、只計費一次；開放表格式／零拷貝使「資料在哪裡被儲存」與「在哪裡被運算」分離，儲存計費移往客戶自有物件儲存，資料平台商營收變成逐查詢可競爭之純運算份額）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20261005_L15-P_generate_GK.md；archive/work/20261014_L15-P#2_generate_CL.md；archive/work/20261021_L15-P#3_generate_CL.md；archive/work/20261021_L15-P#3_test1_CL.md；archive/work/20261014_L15-I#2_generate_CL.md；archive/work/20261021_L15-A#3_generate_CL.md | EMITS: work/20261029_L15-P#4_generate_CL.md -->
**日期：** 2026-10-29　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 1→2／6）　**格：** L15-P　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L14-I#4 已測，Q-0123 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-21 之 L15-P#3／L15-A#3（同日），依表序取 **L15-P**。既有 #1–#3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `Iceberg Snowflake storage`，0 筆；未用。內部數字（§12）未用。
- 比對（須異型）：
  - **L15-P#1**（`archive/drive/USED_20261005_L15-P_generate_GK.md`）：守恆量＝分析師注意力（人×秒）。本卡守恆量＝**位元組駐留位置**（TB），不涉人力。
  - **L15-P#2**（雲承諾池之市集抵扣）：本卡不涉承諾池、市集、通路。若測一只能寫成「客戶預付容量在 AI 與非 AI 功能間互抵」即屬 P#2／L14-P#2 型 → 觸發 (4)。
  - **L15-P#3**（觀測美元占基礎設施帳單份額上限）：本卡不主張任何預算份額上限；守恆在物理資料之單一駐留，非美元占比。
  - **L15-A**（使用量×單價）、**L15-A#3**（託管成本轉嫁毛利）：本卡主張之可觀測量為**營收組成中之儲存項占比**與「外部表」占比，非單價×量分解、非毛利率。
  - **L15-I#2**（雲端商共同出資相容開源引擎之託管定價權）：該卡為引擎授權與託管價差之誘因；本卡為**資料格式**使儲存與運算分屬不同計費主體之守恆，不涉授權條款。
  - **L5 系**（儲存與 IO 硬體／出站切換費）：本卡不涉硬體與出站法規。
  - 已殺 L8-P／L9-P／L11-P、C-A1–C-A5：不涉。
- §7-10 領域最近公開：SNOW 10-Q 2Q FY27（期 2026-07-31，2026-09-04 申報）；SNOW 8-K 2Q FY27 業績（2026-09-02）。下一檢查點＝SNOW 3Q FY27 業績與 10-Q（約 2026-12）。

## 1. 落差一句

種子主張：一份分析表之位元組只駐留一處、只被儲存計費一次；開放表格式（Apache Iceberg）與零拷貝共享使該位置可落在客戶自有物件儲存，資料平台商對該表之儲存營收歸零、只剩運算，而運算可由多引擎逐查詢競逐。市場若把平台商產品營收成長（SNOW 2Q FY27 產品營收 +37%、NRR 126%）讀為「企業資料管理量」隨 AI 擴張之持續佔有，則忽略：AI 帶來之新增資料（非結構化、向量、代理寫回）愈多落在開放格式，平台商之**位元組駐留份額** \(b = \text{平台內計費 TB} / \text{企業分析 TB}\) 下降，營收對資料量之彈性下降、對逐查詢運算份額之敏感上升。SNOW 10-Q 已自述：「open data formats allow customers to use our platform for compute services without requiring storage」。可拒絕之主張＝存在可觀測序列顯示儲存項占比或 \(b\) 下降而市場仍以資料量外推。不主張任何主體價值方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆（P）**：\(\text{TB}_{企業} = \text{TB}_{平台內} + \text{TB}_{開放格式外部}\)，每 TB 只計一次儲存費；平台商營收 \(R = R_{儲存}(\text{TB}_{平台內}) + R_{運算}\)，\(R_{運算}\) 為多引擎對同一份外部位元組之查詢份額 |
| 量綱 | \(b\)、儲存項占營收比（無因次）；TB 只作方向 |
| 選擇者 | 企業資料平台團隊（表格式、目錄、引擎選擇）；平台商（外部表定價、目錄託管）；超大雲（S3 Tables／BigLake 等物件儲存表服務） |
| 可見端 | 平台商 10-Q／10-K 收入組成敘述與風險段；業績電話會議之儲存占比原文；超大雲表服務公告 |
| 指名不可見端 | 單一企業之 TB 分布；外部表查詢份額；Databricks（私有、無申報層）之對應數 |
| 表達工具型態（只指名，不選券） | 美股資料平台／資料倉儲商；不選券 |
| 重疊 | L15-I#2（開源引擎）；L15-A（量×價）；L15-P#2（承諾池） |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Snowflake 10-Q 2Q FY27（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1640147/000164014726000037/snow-20260731.htm ：「we have adopted open data formats like Apache Iceberg tables to allow customers to use our platform to process data stored in external customer-controlled environments outside of Snowflake … These changes are driving increased competition, both because there is less customer “lock in” when our products are used in external en[vironments]」；「open data formats allow customers to use our platform for compute services without requiring storage. To the extent these improvements do not result in an offsetting increase in new workloads, we may experience lower revenue」；「optimize consumption, including by reducing storage through shorter data retention policies and optimizing AI usage」；「For storage resources, consumption for a given customer is based on the average terabytes per month of all of such customer’s data stored in our platform」。
2. Snowflake 8-K 2Q FY27 業績（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/0001640147/000164014726000033/fy2027q2earnings.htm ：「Product revenue of $1.49 billion … 37% year-over-year growth」；「Net revenue retention rate of 126%」；CFO「third consecutive quarter of product revenue growth acceleration」。未見儲存項分列（grep `Iceberg` 0 筆）。
3. 儲存占比之既往具名口徑：The Stack（2024-08-22）https://www.thestack.technology/snowflake-losses-iceberg/ 引 CFO Scarpelli：「Storage is still running about 11% of our revenue」、「We haven't seen customers move storage out of Snowflake」；Futuriom（2024-02-29）https://futuriom.com/articles/news/whats-up-with-snowflake/2024/02 作者轉述「a dip in revenue for storage, which represents roughly 10% to 11% of overall sales」（二手）；BBAE（2024-02-28）https://bbae.com/?p=13717 作者評「data storage and duplication revenue headwinds」（二手）。

缺段（§7-2）：未取 2025–2026 任何儲存占比更新原文；未取 AWS S3 Tables／Google BigLake 之採用量；未取具名賣方就 Iceberg 對 SNOW 儲存／運算組成之 2026 模型原文；Databricks 無申報層。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 2024-02 FY25 指引已計入 Iceberg 儲存逆風，市場當時已定價 | Futuriom／BBAE 2024；SNOW 電話會議 | 已定價（→(3)） |
| R2 | 儲存僅約 11% 營收，且開放格式拉動運算（外部表查詢仍付運算），淨效果正 | Scarpelli 2024-08-22；SNOW 2Q FY27 加速 | 量級不足（→(6)） |
| R3 | 儲存占比停揭後無序列，\(b\) 不可觀測 | 8-K／10-Q 未分列 | 不可觀測（→(2)） |
| R4 | 運算多引擎競逐屬引擎競爭（L15-I#2 型），非位元組守恆 | — | 歸他型（→(4)） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 儲存項占營收比（或可替代之外部表／Iceberg 占比）無 ≥ 2 時點之一手或具名原文，或 ≥ 2 時點顯示占比未降，致位元組駐留份額之變動無證據；或
(2) 申報層（SNOW 10-K FY26／10-Q 1Q–2Q FY27，sec.py）無可並列之收入組成或外部表敘述（僅風險段定性句），落差不可觀測（記失敗歸因）；或
(3) 具名賣方或公司原文已就開放格式使儲存營收移出、營收轉為純運算份額作量化或已入指引（含 2024-02 以降之更新）；或
(4) 可運作對照只能寫成 L15-I#2（引擎授權／託管定價）、L15-A（量×價）或 L15-P#2／L14-P#2（承諾池互抵）；或
(5) 12 個月內無檢驗事件（SNOW 3Q FY27、FY27 10-K、Summit 2027 外部表定價變更）；或
(6) 儲存項 ≤ 營收 10% 且開放格式外部表之運算拉動 ≥ 儲存流失（具名原文），使守恆不影響總營收讀數。

複查觸發器（若日後殺）：任一平台商首次以數值揭露外部表／Iceberg 工作負載占比或儲存項占比之多期序列；超大雲首次揭露物件儲存表服務之容量或營收；平台商改變外部表之計價（如對外部表收目錄／治理費）。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：產品營收、儲存／運算組成、NRR、RPO。2. 可交易工具：資料平台商普通股（不選）。3. 半衰期：容量合約續約週期；外部表遷移時程。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0124；`query/ARCH_matrix.md` L15［P］加「#4 已生成」；`AIM_FUNNEL.md` §3 一句與日期行；`export/LEADS_算力收支.md` 追加 2 列（SNOW 雲端基礎設施採購承諾，10-Q 一手）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L15-P#1–#3、L15-A#1–#3、L15-I#1–#3、L14-P#2、L5 系；不碰 L1-P；不寫 T。
