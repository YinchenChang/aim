# L6-I#4 生成卡｜雲端與基礎設施服務：誘因（買方持有之交付終止權：投資級買方對未交付批次握有「逾寬限期即可終止」之選擇權，行使誘因隨市場租價與自有容量而變 → 投資級 backlog ≠ 確定 backlog）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260928_L6-I_generate_GK.md；archive/work/20261011_L6-I#2_generate_CL.md；archive/work/20261018_L6-I#3_generate_CL.md；archive/work/20261013_L13-I#2_generate_CL.md；archive/work/20261015_L2-I#3_generate_CL.md；work/20261026_L6-A#4_generate_CL.md | EMITS: work/20261026_L6-I#4_generate_CL.md -->
**日期：** 2026-10-26　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 5／6）　**格：** L6-I　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L6-A#4 本日測一，Q-0108 done）。各格最後測試日最舊＝**L6-I**（#3 測一 2026-10-19）；非已殺、非刻意排除。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py termination delivery milestone contract neocloud`，命中 1 筆（SRC_DC_014 IREN／Microsoft 每 MW 設備 capex，新聞稿）；與終止權無關，**未使用**；本卡 IREN 事實取自 10-K 原文。
- 比對之舊檔與死因型態，本卡須異型：
  - **L6-I#1**（GK；逆選擇）：最願簽長約者替代選項**最少**、信用差。本卡相反：對手方為替代選項**最多**之投資級買方，風險不在違約而在**合法之選擇性退出**。
  - **L6-I#2**（賣方代理人 bookings 計酬）：選擇者＝賣方內部。本卡選擇者＝買方。
  - **L6-I#3**（融資可貸性讓價，首約單價 `Δp`）：簽約時之定價。本卡為簽約**後、交付前**之選擇權，不涉首約單價。
  - **C-A4**（ARCH_dead #4，續約單價比 `k`）：到期續約。本卡為交付前終止，不涉續約。
  - **L13-I#2**（Google 對 Fluidstack 租約之擔保／終止費二選一）：擔保人選擇權，L13 融資結構。本卡為 L6 雲供給方與買方之服務合約條款。
  - **L6-P#2**（RPO 之實體交付上界）、**L2-I#3**（設備商 backlog 可取消）：前者為物理可交付量；後者為 L2 上游訂單。本卡問的是**交付延誤時買方是否選擇行使**，行使與否應隨租價變動；若行使只由物理不可能驅動，即退化為 L6-P#2 型（否決 (3)）。
  - **L6-A#1**（RPO 領先比）、**L6-P#4**（氣冷／液冷存量）、**L6-A#4**（capex 現金流分類）：不涉。
  - 重疊列為否決 (5)。
- §7-10 領域最近公開：IREN 10-K 期 2026-06-30（2026-08-27）；CoreWeave 10-Q 期 2026-06-30（2026-08-12）；Nebius 6-K 2026-10-22（最新）；Microsoft 終止 Nscale Loughton 報導 2026-10-19。下一檢查點＝CoreWeave、Nebius 3Q26（約 2026-11）；IREN FQ1 FY27 10-Q（約 2026-11）；IREN Horizon 2–4 寬限期屆滿（2027 Q2 初）。

## 1. 落差一句

新雲（neocloud）對超大規模業者之分批 GPU 容量合約，買方對**未交付批次**握有終止權（Nebius 6-K 原文：「In the event that, following a grace period, Company fails to meet agreed delivery dates for a GPU Service and the Company cannot provide alternative capacity, Microsoft has the right to terminate that GPU Service」；IREN 10-K：「our customers may have the right to reduce their committed capacity or terminate their contracts in certain circumstances if we fail to meet our obligations」）。交付延誤為常態（IREN：設備延遲曾影響 Horizon 1；Horizon 2–4 寬限期延至 2027 Q2 初），故該權利實為買方之**選擇權**：買方可選擇展延豁免或行使。誘因：當同等容量之市場租價低於合約價、或買方自建容量到位時，行使價值為正。種子主張：市場與賣方以「投資級對手方 TCV」視未交付批次為近確定收入，未扣除買方選擇權；而選擇權之行使與租價下行同向，正落在供給方最弱之時。觀測量 `ω ≡ 仍在可終止窗內之未交付批次 TCV ÷ 總 RPO`、價內度 `m ≡ (合約租價 − 市場租價) ÷ 合約租價`。本卡不定方向與量級。

已見事例（`[V]` 二手）：Microsoft 終止 Nscale Loughton（50 MW、原計畫 23,040 顆 GB300）合約，報導歸因電網接入延至 2030 年代（DCK 2026-10-19）——屬**物理**驅動，尚不證明價格驅動之行使。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因（買方持有之實質選擇權；行使為買方最適化）；非守恆、非會計恆等 |
| 選擇者 | 投資級買方（Microsoft 等）：展延寬限、接受替代容量、或終止該批 |
| 可見端 | 6-K／8-K／10-K 合約摘要之終止條款、寬限期、預付比例（IREN 每批 20% 交付前預付，第 24 個月後抵扣）、違約金（Nebius「liquidated damages for late delivery」）；10-Q 交付／驗收里程碑（IREN Horizon 1「delivered to, and accepted by, Microsoft in August 2026」）；CoreWeave RPO 之變動對價（「amounts that may not be recognized as revenue due to delivery delays」）；DDTL「delayed data center site amortization date」條款；公開租價指數（Ornn：B200 2026-03 初 2.31 → 2026-04 4.95 美元／GPU·小時，二手） |
| 指名不可見端 | 合約單價（`m` 之分子）；寬限期豁免是否已發生；批次別 TCV；買方內部自建容量時程 |
| 對照式（生成用） | 可拒絕：(a) 終止只在物理不可能時發生、與 `m` 無關；或 (b) 預付＋違約金使買方行使之淨值恆負；或 (c) 供給方 RPO 已按交付延誤估計扣減且賣方已折價 |
| 表達工具型態（只指名，不選券） | 美股可交易之 GPU 雲供給方（Nebius、IREN、CoreWeave；次為 Applied Digital、TeraWulf、Cipher、Galaxy 之 HPC 承租合約）。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Nebius 6-K 2025-09-08（Microsoft 合約：五年、分批、TCV 約 17.4B／可增至 19.4B、終止條款、違約金、融資條件成就始生效）。https://www.sec.gov/Archives/edgar/data/1513845/000110465925088312/tm2525580d1_6k.htm
2. IREN 10-K 期 2026-06-30（Microsoft 合約 TCV 約 9.7B、四批 Horizon、寬限期、20% 預付、可減量或終止之風險因素、設備延遲史）。https://www.sec.gov/Archives/edgar/data/1878848/000187884826000052/iren-20260630.htm
3. CoreWeave 10-Q 期 2026-06-30（RPO 變動對價含交付延誤；DDTL 4.0 延誤場址攤還條款；隨需客戶可短通知終止）。https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm
4. Data Center Knowledge 2026-10-19「Microsoft exits Nscale data center deal over UK power delays」（二手；Nscale 未上市，僅作事例）。https://datacenterknowledge.com/build-design/microsoft-exits-nscale-data-center-deal-over-uk-power-delays
5. 租價：Tomasz Tunguz 2026-04-27 引 Ornn Compute Price Index（二手）。https://tomtunguz.com/b200-gpu-pricing-spot-market-model-releases/
6. 測一須另取：Nebius 最新 6-K／20-F 之 Microsoft、Meta 批次交付狀態；CoreWeave／Applied Digital／TeraWulf／Cipher 合約之同型條款；已公開之終止或減量事例（含 2025 Microsoft–CoreWeave 報導）之原因歸屬；具名賣方或評等機構是否已以交付終止權折價 TCV。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | RPO 已按歷史經驗估計扣減交付延誤之不認列額，選擇權已入帳 | CoreWeave 10-Q 收入附註（#3） | 無落差 |
| R2 | 預付（IREN 20%）、違約金與替代容量條款使終止僅於物理失敗時發生，與租價無關 | IREN 10-K；Nebius 6-K；Nscale 事例歸因電網 | 退化為交付上界（L6-P#2 型） |
| R3 | 租價上行（Ornn B200 六週 +114%），選擇權價外，12 個月內無行使誘因 | Ornn／Tunguz | 窗內不可檢驗 |
| R4 | 買方自身容量短缺，終止即喪失容量，行使成本高 | Microsoft 向多家新雲採購之公開敘述（待原文） | 誘因弱 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 交付終止／減量條款與未交付批次 TCV 於 ≥ 3 家美股可交易 L6 供給方之申報中不可並列，使 `ω` 無判別力。
(2) 供給方 RPO 已扣減交付延誤估計（R1）**且**具名賣方或評等機構已以買方終止權折價超大規模業者 TCV。
(3) 已知終止／減量事例（含 Nscale Loughton）之原文歸因全屬物理不可能（電力、設備、建設），無一涉及租價或買方需求變動，且條款無買方任意展延／豁免空間（R2 成立）。
(4) 代表性供給方（Nebius、IREN、CoreWeave 中 ≥ 2 家）於 2026-12-31 之 `ω` ＜ 10%（多數批次已交付驗收），量級不足。
(5) 可運作對照只能寫成逆選擇／對手方信用（L6-I#1）、首約讓價（L6-I#3）、續約單價（C-A4）、擔保人選擇權（L13-I#2）、實體交付上界（L6-P#2）或上游訂單取消（L2-I#3）。
(6) 12 個月內（至 2027-10）無任何批次之寬限期屆滿或交付里程碑可檢驗，使本卡無可觀測事件。

複查觸發器（若日後殺）：任一美股可交易 L6 供給方於 10-K／10-Q／6-K 揭露買方以終止或減量權退出已簽批次，且原文歸因含價格、需求或自有容量；或公開租價指數對同世代 GPU 連續 2 季下跌逾 30%。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：RPO 與其變動對價、遞延收入（預付）、違約金／服務抵減、PP&E 減損（終止批次之設備）。
2. 可交易工具：Nebius、IREN、CoreWeave 等美股與選擇權（不選券）。
3. 半衰期：寬限期至交付驗收約 1–3 季；`[V]` 不寫。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L6［I］標「#4 已生成」；`AIM_FUNNEL.md` §3 一句（未測格數）；`export/LEADS_算力收支.md` 4 筆（Nebius／IREN 合約值、Nscale 終止、Ornn B200 租價）。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L6-I#1–#3、L6-A#1–#4、L6-P#1–#4、L13-I#2、L2-I#3、C-A4 結論。
