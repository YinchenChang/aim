# L2-I#3 生成卡｜資料中心實體：誘因（設備稀缺下之買方保位——可取消／可延後訂單之選擇權，backlog 計入而買方承諾薄）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260917_L2-I_generate_GK.md；archive/work/20261007_L2-I#2_generate_CL.md；work/20261007_L2-I#2_test1_CL.md；archive/work/20261014_L2-A#3_generate_CL.md；query/QUEUE.md | EMITS: work/20261015_L2-I#3_generate_CL.md -->
**日期：** 2026-10-15　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1／6）　**格：** L2-I　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L2-A#3、L2-P#3 皆於 2026-10-14 測一）。非「已殺／刻意排除」格中最後測一最舊者為 2026-10-07 批（L2-I#2／L8-A#2／L8-I#2／L9-A#2）；同日依 QUEUE 序次（Q-0003 先於 Q-0004）取 **L2-I**；既有生成 2 份 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `backlog "double ordering" Vertiv cancellation`，命中 0 筆。
- 比對（本卡須異型）：
  - **L2-I#1**（`archive/drive/USED_20260917_L2-I_generate_GK.md`；許可／併網可撤回 × 損失歸屬錯配）：本卡不涉許可，是**設備訂單之買方保位選擇權**。
  - **L2-I#2**（`work/20261007_L2-I#2_test1_CL.md`；開發 JV 之 GP 兼買方 promote）：關係人定價；本卡為獨立買賣雙方，誘因在**取消／延後權之定價**。
  - **L6-I**（backlog 變厚≠對手方變好）：該卡為雲端 RPO 之對手方信用；本卡對手方信用良好，問題在**同一需求於多家供應商重複佔位**與取消代價。
  - **L6-I#2**（bookings 計酬）、**L4-I#2**（加速器商回租／擔保）、**L4-A#2**（整機商營運資本）、**L13-I**（擔保違約路徑）：不涉。
  - ARCH_dead C-A3／C-A4（折舊／續約單價）、C-P4（水）：不涉。
- §7-10 領域最近公開：VRT 10-Q 2Q26（2026-07-29 申報）；VRT 8-K ex99.1 Q2 2026（2026-07-29）；VRT 10-K FY2025（2026-02-13）。下一檢查點＝VRT 3Q26 10-Q（約 2026-10 下旬）。

## 1. 落差一句

電力與熱管理設備（UPS、開關設備、匯流排、液冷）交期長於資料中心建設週期時，買方（超大規模業者、共置營運商、開發商）之最適策略為**先下單保位**：取消／延後之代價（違約金、訂金沒收）低於失去生產槽位之代價時，同一 MW 需求可在多家供應商、多個時點同時成為「確定訂單」。供應商 backlog 依「已收採購單或採購承諾、未交貨」計，含可取消／可延後部分；backlog 增速因此可高於終端 MW 需求增速，差額為買方持有之免費或低價選擇權。種子主張：以 backlog 或訂單增速外推營收者，讀到的部分是**保位誘因**而非需求。**方向未定**（交期縮短時保位訂單可撤出，亦可轉為實際出貨；買方訂金比例上升則選擇權變貴、落差收窄）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：買方在稀缺下之保位選擇權；供應商以 backlog 揭露，買方以低承諾成本持有 |
| 已讀事實 | VRT 10-K FY2025：「estimated combined order backlog was $15.0 billion and $7.2 billion as of December 31, 2025 and 2024」，「as continued strong demand has contributed to an increase in customer orders being placed in advance of our ability to fulfill them」；「Orders may be subject to cancellation or rescheduling by the customer」；「Our customers have the right in some circumstances, usually with penalties or other termination consequences, to reduce or defer firm orders in backlog」。同檔收入政策：「cancellation, termination or refund provisions apply only in the event of contract breach. These provisions have historically not been invoked.」（兩段口徑待測一調和）。VRT 10-Q 2Q26 正文 backlog 僅見於前瞻風險句；8-K ex99.1 Q2 2026 亦無 backlog 數（`sec.py --grep` 各 1／0 筆，大小寫敏感，待測一以他詞複核）。 |
| `[D]` 承諾強度代理 | 流動合約負債（XBRL `ContractWithCustomerLiabilityCurrent`）：2024-12-31 1,063.3M；2025-12-31 1,814.7M；2026-03-31 2,461.8M；2026-06-30 3,633.7M。÷ 年末 backlog：14.8%（2024）→ 12.1%（2025）。CFO（Q2 2026 電話會）：「our deferred revenue is a read-through in terms of those advanced deposits on orders」。 |
| 量綱 | 合約負債／backlog（%）；backlog ÷ 過去 12 月營收（年）；取消或延後金額／backlog（%）；買方採購義務（10-K purchase obligations）覆蓋供應商 backlog 之比（無因次） |
| 選擇變數 | 買方：下單家數、下單提前期、訂金比例；供應商：取消條款、訂金要求、backlog 揭露與否 |
| 半衰期 | 交期正常化之時點（數季至數年） |

**不主張方向、不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. VRT 10-K FY2025 https://www.sec.gov/Archives/edgar/data/1674101/000167410126000008/vrt-20251231.htm （backlog 定義、取消／延後條款、收入政策句）
2. VRT 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1674101/000162828026050609/vrt-20260630.htm ；8-K ex99.1 Q2 2026 https://www.sec.gov/Archives/edgar/data/0001674101/000162828026050323/q22026exhibit991vrt07292026.htm （backlog 是否續揭露）
3. VRT Q2 2026 電話會逐字稿（次級彙編）https://earningswhispers.com/transcript/VRT/Q22026 ——訂金／deferred revenue 句。
4. 同型主體（待測一指名讀）：Eaton 10-Q 電氣美洲段 backlog 與資料中心訂單；Schneider Electric（非美股，只作對照）；GE Vernova Electrification backlog。
5. 買方端：MSFT／META／AMZN／GOOGL 10-K purchase obligations 是否分列基礎設施設備。
6. 交期與預付之產業報導：Reuters 2026-07-09（轉載）https://www.kitco.com/news/off-the-wire/2026-07-09/us-power-companies-scramble-secure-equipment-surging-data-center ——「paying upfront, to secure earlier production slots」、「asking customers to pre-pay for equipment that has long lead times」（電業端，非資料中心營運商）。

缺段（§7-2）：重複下單之直接證據 0 筆（Reuters 稿與 VRT Q2 逐字稿均無 double ordering／cancellation 語句）；backlog 2026 季度數未取得；取消實際發生額未揭露。失敗歸因＝本輪只讀上列；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 取消條款「historically not been invoked」；訂單附違約金與訂金，非免費選擇權 | VRT 10-K 收入政策句；CFO 訂金句（載體 3） | 選擇權代價不低 → 無保位誘因 |
| R2 | 合約負債 2026 上半年翻倍（1.81B→3.63B），承諾強度上升而非下降 | XBRL（§2） | 方向相反 |
| R3 | 公司自述 backlog「not necessarily indicative of our net sales」，市場已折價 backlog | VRT 10-K backlog 段 | 已定價 |
| R4 | 終端 MW 需求本身超過設備產能；保位訂單終將交貨 | Reuters 2026-07-09（交期 > 3 年） | 落差只是時點 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後 ≥ 2 家美股上市資料中心電力／熱管理設備商（如 VRT／ETN／GEV 電氣段）10-Q／10-K 或財報稿無 ≥ 4 期 backlog（或訂單）與合約負債之同口徑序列，且無取消／延後條款原文；或
(2) 可運作對照只能寫成雲端 RPO 之對手方信用（L6-I）、許可撤回（L2-I#1）、關係人定價（L2-I#2）或供應商融資（L4-I#2）；或
(3) 具名賣方／公司已公開量化保位或重複訂單（或取消率）並為市場所引用（已定價）；或
(4) `[D]` 量級：合約負債／backlog 不降反升（R2 成立），或揭露之取消／延後額 < backlog 2%，或買方採購義務足以覆蓋供應商 backlog；或
(5) 12 個月內無可觀測驅動：無交期變化、無 backlog 揭露變更、無取消或延後揭露。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：backlog（非 GAAP）、合約負債、訂單。2. 可交易工具：電力／熱管理設備商（不選）。3. 半衰期：交期正常化。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L2［I］格加「#3 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0046。不改 L2-I#1／#2、L2-A#1／#2／#3、L2-P#1／#2／#3、L6-I／#2、L4-I#2、C-P4 結論。
