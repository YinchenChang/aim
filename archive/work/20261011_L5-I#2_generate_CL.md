# L5-I#2 生成卡｜儲存與 IO：誘因（NAND 供給者之資本配置誘因：JV 雙邊同意＋固定成本共擔＋DRAM／HBM 爭奪潔淨室 → 高峰價下仍不擴晶圓、以製程遷移與股東回饋代替）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/RETRIG_2.md；archive/drive/USED_20260926_L5-I_generate_GK.md；archive/drive/USED_20260926_L5-I_test1_GK.md；archive/work/20261011_L5-A#2_generate_CL.md | EMITS: work/20261011_L5-I#2_generate_CL.md -->
**日期：** 2026-10-11　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L5-I　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L5-A#2 已於本日測一，Q-0019 done）。最後測試日最舊＝2026-09-26 一批尚無 #2 者僅餘 **L5-I**（L5-A 已取 #2）。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py NAND SSD flash`，回 19 筆，**相關 0 筆**（全為模型名含「Flash」之 SRC_MOD／PRC／PERF／CAP 列）；載體由 `sec.py` 與 WebSearch 原文取得。
- 比對之舊檔與死因型態，本卡須異型：
  - **L5-I#1**（`archive/drive/USED_20260926_L5-I_generate_GK.md`；測一 `archive/drive/USED_20260926_L5-I_test1_GK.md`）：雲端出站費＝結構性取用權、Data Act 型態轉換；部分通過｜不進 T，失敗在量綱（清單 `P_list` ≠ 切換段 `P_egr`，無連續參數）。本卡**換選擇者與物件**：選擇者＝NAND 晶圓供給者（非雲端業者），物件＝晶圓產能擴充決策（非價目）；所需量為申報層連續量（資本支出、EB 出貨變動率、每 GB 營收變動率、JV 預付／承諾），非價目表列名。RETRIG R-29 不受本卡影響。
  - **L5-A#2**（`archive/work/20261011_L5-A#2_generate_CL.md`）：HDD 營收乘積恆等、台數封頂；邊界明文「不及 NAND／eSSD 週期」。本卡為 NAND、型態為誘因（選擇），非恆等。
  - **L5-P**（HBM 頻寬守恆）、**L3-P#2**（HBM 堆疊良率／投入比）：本卡只用「DRAM／HBM 爭奪潔淨室」作為 NAND 擴產之機會成本，不主張 HBM 良率或頻寬。重疊列為否決 (5)。
  - **C-P1**（ARCH_dead #11，L5）：儲存需求以訓練 checkpoint 歸因、方向翻負。本卡不做需求歸因，只做供給者誘因。
  - **L5-A#1**（KV IO 可分離，雲端總額）：不同層物件。
- §7-10 領域最近公開：Sandisk FY26 10-K（期末 2026-07-03，申報 2026-08-17）；Micron FY26 10-K（期末 2026-09-03，申報 2026-10-09）；TrendForce 2026-07-21 NAND 月報；TrendForce 引 Nikkei 2026-06-18 Kioxia 資本支出。下一檢查點＝Sandisk FQ1'27 10-Q（約 2026-11 上旬）、Micron FQ1'27（約 2026-12 下旬）、Kioxia FY26 上半年財報（約 2026-11）。

## 1. 落差一句

NAND 歷史為蛛網週期：高峰價 → 擴晶圓 → 約兩年後供過於求。**種子主張：本輪供給者之誘因結構不同——(i) Sandisk／Kioxia Flash Ventures 擴產須雙方同意、固定成本各擔 50% 且不論下單與否皆須付；(ii) 三家 DRAM／NAND 兼營者之邊際潔淨室與資本優先給 DRAM／HBM；(iii) 2022–23 虧損後之資本紀律（Kioxia FY26–28 年均資本支出仍低於 FY23 峰值約一成）——使高峰價轉成股東回饋與製程遷移，而非新晶圓。** 落差＝若市場以蛛網半衰期（供給於 2H27 追上）折現 NAND 業者，而誘因使晶圓擴充延後，則價格高原較長；反之若誘因已被中國業者擴產（TrendForce：中國份額近 19%）抵銷，則無落差。本卡不定方向之大小，只立可拒絕之誘因機制。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因（供給者資本配置選擇）；非會計恆等、非物理上界 |
| 選擇者 | NAND 晶圓供給者：Sandisk＋Kioxia（Flash Ventures，50/50）、Samsung、SK hynix（含 Solidigm）、Micron；中國供給者（YMTC 等）為外生擴產方 |
| 可見端 | Sandisk FY26 10-K：營收 +175%；EB 出貨 +中十位數%；Datacenter EB 近 +120%、每 GB 營收近 +150%；Edge 每 GB 營收近 +180%；購置 PP&E 177 百萬（前兩年 204／166）、對 Flash Ventures 票據發行 462、回收 187；回購 4,524；營業現金流 11,671。JV：50% 固定成本「regardless of whether we order」；擴產「requires significant investments by both Kioxia and us」、「cannot unilaterally direct」；2026-01-29 延長至 2034-12-31 並另付 Kioxia 1.2 十億（2026–2029）換「continued availability of supply」 |
| 指名不可見端 | Flash Ventures 晶圓投片數與新潔淨室決議；各家 NAND 專屬資本支出（多為與 DRAM 合併揭露）；中國供給者擴產實量 |
| 主張 | 高峰價下供給者之邊際選擇＝回購／製程遷移＞新晶圓；EB 出貨成長受製程遷移節奏封頂；蛛網回歸延後 |
| 表達工具型態（只指名，不選券） | 美股可交易 NAND 供給者（Sandisk、Micron；Samsung／SK hynix／Kioxia 非美股或 OTC）。不選券 |
| 重疊 | L5-A#2（同層供給封頂）；L3-P#2／L5-P（HBM）；C-P1。重疊不構成丟棄 |

對照式（生成用，非正式載入）：`ΔlnBits_supply ≈ Δln(wafers) + Δln(bits/wafer)`；誘因主張 ⇒ `Δln(wafers) ≈ 0`（至新潔淨室決議前），`Δln(bits/wafer)` 由層數遷移決定。本輪不估參數、不寫 H1。

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Sandisk FY26 10-K（MD&A Net Revenue 段 EB／每 GB 營收、Flash Ventures 附註、現金流量表、風險因子 JV 段）。https://www.sec.gov/Archives/edgar/data/2023554/000162828026057406/sndk-20260703.htm
2. Sandisk FQ1–FQ3 FY26 10-Q（季序列）。https://www.sec.gov/Archives/edgar/data/2023554/000162828025050698/sndk-20251003.htm ；https://www.sec.gov/Archives/edgar/data/2023554/000162828026004407/sndk-20260102.htm ；https://www.sec.gov/Archives/edgar/data/2023554/000162828026029401/sndk-20260403.htm
3. Micron FY26 10-K（NAND 分部或產品別、資本支出配置敘述；本輪未讀）。https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm
4. TrendForce 2026-07-21 NAND 月報：2026 供給缺口 4–5%；「existing fab space remains constrained and manufacturers continue prioritizing DRAM capacity expansion」；2H27 轉正；中國份額近 19%。https://www.trendforce.com/presscenter/news/20260721-13148.html
5. TrendForce 2026-06-18（引 Nikkei）：Kioxia FY26–28 年均資本支出約 ¥470B，較 FY23 峰值 ¥510.4B 低約 10%；集中 Kitakami。https://www.trendforce.com/news/2026/06/18/news-kioxia-adopts-cautious-capex-strategy-despite-nand-upcycle-reportedly-10-below-fy23-peak-key-concerns-in-focus/

測一須另取：Flash Ventures 新潔淨室／投片決議之原文（8-K、Kioxia 公告）；Samsung／SK hynix 法說 NAND 資本支出原文；Micron 10-K NAND 配置句；中國供給者擴產量之具名原文；具名賣方是否已以「供給者誘因／蛛網延後」建模。**不宣稱已錯價。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 供給於 2H27 追上需求，蛛網照常 | TrendForce 2026-07-21（上列 #4） | 半衰期 < 窗 |
| R2 | 中國供給者擴產抵銷寡占紀律 | 同上（中國份額近 19%） | 誘因不綁全市場 |
| R3 | 紀律已為共識且已定價（「NAND tight through 2028」） | Goldman 對 Kioxia 報告之報導 https://borecraft.com/2026/05/31/goldman-nearly-doubles-kioxias-target-sees-nand-tight-through-2028/ | 共識 |
| R4 | Kioxia 資本支出 FY26–28 較 FY25 +66%，已在擴產 | TrendForce 2026-06-03 https://www.trendforce.com/news/2026/06/03/news-kioxia-targets-%C2%A5470b-yearly-capex-in-fy26-28-up-66-from-fy25-reportedly-weighing-third-kitakami-fab-and-ma/（搜尋結果標題層，本輪未實讀） | 誘因不成立 |
| R5 | 每 GB 營收大漲主因組合（eSSD 高容量）而非同品漲價 | Sandisk 10-K 混合「revenue per gigabyte」定義 | 拆分不可辨 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 任一主要供給者（Flash Ventures、Samsung、SK hynix、Micron）於 2026 年內原文宣布新 NAND 晶圓產能（新潔淨室投片、非製程遷移），使「晶圓不擴」不成立。
(2) 公開層（業者原文或具名賣方／研究機構）已明文以「供給者誘因延後擴產」量化 NAND 價格高原期，使落差為共識（R3 之原文須實讀，非報導轉述）。
(3) 申報層無法分出 NAND 專屬資本支出或晶圓數（只剩與 DRAM 合併之總資本支出、混合每 GB 營收），誘因之選擇變數不可觀測。
(4) 中國供給者擴產量（具名原文）足以使全市場位元供給成長不受寡占誘因約束（R2 成立）。
(5) 可運作對照只能寫成 HBM 良率／頻寬（L3-P#2／L5-P）、HDD 恆等（L5-A#2）、需求歸因（C-P1）或雲端出站費（L5-I#1）。

複查觸發器（若日後殺）：任一美股可交易 NAND 供給者於 10-K／10-Q／8-K 分列 NAND 專屬資本支出或晶圓投片，或 Flash Ventures 宣布新潔淨室投片／擴產決議，或具名研究機構下修 NAND 供給回正時點至 2028 之後。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：營收、EB 變動率、每 GB 營收變動率、Flash Ventures 預付與承諾、資本支出、回購。
2. 可交易工具：Sandisk、Micron 美股；Samsung／SK hynix／Kioxia 非美股主上市。
3. 半衰期：新潔淨室決議至量產約 18–24 個月；TrendForce 回正時點 2H27 是否 < 12 個月窗。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L5［I］標「#2 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L5-I#1／L5-A#1／L5-A#2／L5-P／C-P1／L3-P#2 結論。
