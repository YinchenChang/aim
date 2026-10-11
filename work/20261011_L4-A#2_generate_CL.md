# L4-A#2 生成卡｜運算硬體系統：會計恆等（AI 伺服器整機商之營運資本恆等：OCF ＝ 淨利 − ΔWC，ΔWC ≈ 成長 × 現金轉換週期；同品類兩家 CCC 正負相反，OCF 由供應商付款條件而非獲利決定）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260926_L4-A_generate_GK.md；archive/drive/USED_20260926_L4-A_test1_GK.md；archive/drive/USED_20260926_L4-I_generate_GK.md | EMITS: work/20261011_L4-A#2_generate_CL.md -->
**日期：** 2026-10-11　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L4-A　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L4-P#2 已於本日測一）。最後測試日最舊＝2026-09-26 一批尚無 #2 者：L4-A／L4-I、L5-A／L5-I；依表序取 **L4-A**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py "AI server backlog" "inventory" "working capital"`，命中 **0** 筆；本卡載體全由 `sec.py` 原文取得。
- 比對之舊檔與死因型態，本卡須異型：
  - **L4-A#1**（`archive/drive/USED_20260926_L4-A_generate_GK.md`；測一 `archive/drive/USED_20260926_L4-A_test1_GK.md`）：**損益**恆等（系統售價＝四項 BOM＋整機商毛利，`s_accel` 移動）；死於否決 (1)(2)——系統 vs 元件、GPU 轉售成本、四項 BOM 皆不在申報層。本卡換為**資產負債／現金流量**恆等：所需量（存貨、應收、應付、遞延收入、OCF）**全部是申報表行**，不需 BOM 拆分。
  - **L6-I**（backlog 變厚≠對手方變好）：雲端層、對手方信用；本卡為整機商自身之營運資本，不涉對手方品質。
  - **L13-I**（應收總額／載具評等；帳齡不可並列）：本卡將 **financing receivables（客戶融資）排除於核心恆等之外**，只列為重疊項，以免滑入 L13。
  - **L13-A**（租賃義務上界）、**C-I3′**（分部毛利由非機制項解釋）、**N-01**（機隊世代）、**L4-I**（開放機櫃誘因）：構成不同。
- §7-10 領域最近公開：Dell FQ2'27 10-Q（期末 2026-07-31）；SMCI FY26 10-K（期末 2026-06-30）；HPE FQ3'26 10-Q（期末 2026-07-31，本輪未讀）。下一檢查點＝SMCI FQ1'27 10-Q（約 2026-11 初）、Dell FQ3'27 10-Q（約 2026-12 初）。

## 1. 落差一句

整機商 `OCF = NI − ΔAR − ΔInv + ΔAP + ΔDefRev（± 其他）`；在日數不變下 `ΔWC ≈ ΔCOGS_daily × CCC`，`CCC = DIO + DSO − DPO`。同一 AI 伺服器品類、同期，兩家申報主體之營運資本符號相反：**Dell** 6M FY27 存貨 −10,940、應收 −5,428、應付 **+16,203**、遞延收入 +3,089（百萬美元），營運資本（不含融資應收）淨**流入**約 +2.9B，OCF +6,306；**SMCI** FY26 存貨 −8,877、應收 −3,922、應付僅 +963，OCF **−6,810**、融資活動 +9,479。即 AI 成長期之 OCF 主要是「成長率 × CCC 符號」之函數，而 CCC 之 DPO 端由上游（GPU 供應商、ODM／代工）之付款條件決定，非整機商獲利；**落差＝市場把整機商 OCF／FCF 讀成獲利品質，而恆等式指出其符號與量級在成長減速或上游條款變動時階躍反轉，且觸發點可由申報表行事前計算**。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（間接法現金流量表；營運資本 ＝ 日數 × 日均成本）；非守恆、非誘因 |
| 選擇者 | GPU／加速器供應商與 ODM（對整機商之付款條件與預付要求）；整機商（備料深度 DIO）；客戶（付款條件、預付／遞延收入） |
| 可見端 | Dell 10-Q：資產負債表 Inventories 21,290（vs 10,437，2026-01-30）、其中 Production materials 15,894；Accounts payable 49,723（vs 33,630）；ISG 主要品類 AI-optimized servers 16,401（3M）；MD&A「significant increase in backlog」「inherent non-linearity in the timing of demand and subsequent shipments」；OCF 驅動句「net revenue growth, profitability, and working capital dynamics」。SMCI 10-K：現金流量表與 key cash flow metrics |
| 指名不可見端 | AI 品類專屬之存貨與應付（兩家皆合併列）；上游付款條件（天數）；Dell 與代工間之元件售回（non-trade receivables，10-Q 載其會計處理）對 AP 之放大 |
| 主張 | `CCC_AI < 0` 之整機商，其 OCF 在成長期被放大、在成長減速或 DPO 縮短時反轉；`CCC_AI > 0` 者反之。翻轉點＝成長率 × CCC 之符號變化，可由季度申報表行反算 |
| 表達工具型態（只指名，不選券） | 已上市、美股可交易之 AI 伺服器整機商（Dell、SMCI、HPE）。不選券 |
| 重疊 | L13-I（融資應收；本卡排除）；L6-I（backlog）；L4-A#1（同格損益恆等）。重疊不構成丟棄 |

恆等式（生成用，非正式載入）：`ΔWC_t ≈ (COGS_t/365) × CCC_t − (COGS_{t−1}/365) × CCC_{t−1}`。本輪不估參數、不寫 H1。

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Dell FQ2'27 10-Q（Statements of Financial Position、Cash Flows、Note 補充：Inventories 組成；MD&A 流動性與 ISG 品類）。https://www.sec.gov/Archives/edgar/data/1571996/000157199626000046/dell-20260731.htm
2. Dell FQ1'27 10-Q（前一季同表，供季序列）。https://www.sec.gov/Archives/edgar/data/1571996/000157199626000030/dell-20260501.htm
3. SMCI FY26 10-K（Consolidated Statements of Cash Flows；key cash flow metrics；AP 含關係人）。https://www.sec.gov/Archives/edgar/data/1375365/000137536526000022/smci-20260630.htm
4. HPE FQ3'26 10-Q（Server 分部、存貨、應付；本輪未讀）。https://www.sec.gov/Archives/edgar/data/1645590/000164559026000080/hpe-20260731.htm
5. Dell 財報 8-K／投影片之 AI orders、shipments、backlog 季序列（測一須定位原件；本輪未讀）。

測一須另取：≥ 4 季兩家之 DIO／DSO／DPO 序列（由申報行計算）；Dell 10-K 對供應商付款條件或 supply chain financing 之揭露；SMCI 10-K 對 GPU 預付或供應商條款之敘述；管理層對「working capital」之前瞻句。**不宣稱 AI 品類 CCC 已可分列，不宣稱已錯價。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 存貨與應付為全公司合併數，Dell 之 CSG（PC）與傳統伺服器混同；AI 品類 CCC 不可分離 | Dell 10-Q 資產負債表只一行 Inventories／AP | 量綱不對（重演 L4-A#1 (1) 之風險，但此處所缺為品類拆分而非整張 BOM） |
| R2 | 日數不變時成長放緩只使 ΔWC→0，不必然反轉；反轉需「衰退」或「條款變動」，兩者時點不可事前排序 | 恆等式本身 | 翻轉點可能只是「成長率」之重述，無獨立資訊 |
| R3 | 營運資本季節性與一次性（大單出貨時點、元件售回代工之會計）可完全解釋 AP 躍升 | Dell 10-Q non-trade receivables 會計處理段 | 變動由非機制項解釋（C-I3′ 型） |
| R4 | 市場與賣方已以 FCF 轉換率、營運資本為常規追蹤（SMCI 融資需求與 OCF 為負早為公開議題） | SMCI 10-K 融資活動 +9.5B | 機制真、價已反映 |
| R5 | OCF 階躍不改變長期價值，只移時點；12 個月窗內財富倍數無法到 5x 級 | §1 准入 | 可表達但不過門檻（測一不判 H1，但須記） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 對 ≥ 4 季申報實讀後，AI 品類之存貨／應付／應收無法與 CSG／傳統伺服器分離，且全公司 CCC 之變動不能以 AI 品類營收占比變動解釋（只剩合併數）。
(2) Dell AP 躍升可完全由季節性、元件售回代工會計或單一大單時點解釋，並有管理層原文佐證（C-I3′ 型）。
(3) 公開層（10-K／10-Q／法說／具名賣方）已明文量化 AI 營運資本反轉風險或 OCF 之成長依賴，使落差為共識。
(4) 兩家 CCC 符號差異可完全由客戶結構（預付／遞延收入）或融資應收解釋，即機制落入 L13-I 或 L6-I 而非整機商營運資本。
(5) 恆等式之翻轉點只能寫成「成長率下降」，無任何獨立於營收預測之可觀測前導（上游條款、DPO 變動）。

複查觸發器（若日後殺）：任一美股可交易整機商於 10-K／10-Q 分列 AI 品類之存貨或應付，或揭露上游（GPU／ODM）付款條件或供應鏈融資餘額 ≥ 2 期。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：AI 營運資本能否自合併存貨／AP 拆出；能否拒絕 PC 與傳統伺服器季節性。
2. 可交易工具：恆等落在美股可交易整機商，而非私有 ODM（Quanta、Wiwynn 等台股禁）。
3. 半衰期：上游條款變動或成長減速之時點是否落在 ≥ 12 個月窗內，且不被一季內之訂單時點雜訊淹沒。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L4［A］標「#2 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L4-A#1／L4-P／L4-P#2／L4-I／L6-I／L13-I／C-I3′ 結論。
