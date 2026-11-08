# L3-A#6 生成卡｜半導體製造測試：會計恆等（存貨成本與淨變現價值孰低之準備流：新節點早期量產先提 LCNRV 準備〔損益先認〕→ 已提準備之存貨售出時銷貨成本以減記後基礎認列〔毛利回補〕；回補存量有限，下一節點爬坡重提）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md（經 FUNNEL §2）；archive/work/20261008_L3-A#2_generate_CL.md；archive/work/20261016_L3-A#3_generate_CL.md；archive/work/20261024_L3-A#4_generate_CL.md；archive/work/20261031_L3-A#5_generate_CL.md；archive/work/20261108_L3-P#6_generate_CL.md（格式與相鄰否決） | EMITS: work/20261108_L3-A#6_generate_CL.md -->
**日期：** 2026-11-08　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3→4／6）　**格：** L3-A　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L3-P#6 已於本日測一）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-31（L3-A#5、L3-I#5、L4-P#5、L4-A#5；L3-P 已取）→ 依表序取 **L3-A**；既有生成 5 份 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `underutilization`／`absorption`／`start-up costs`，命中 0 筆。內部數字（§12）：未取用。
- 比對（本卡須異型）：
  - **L3-A#1**（GK）：有效晶粒單價（晶圓價 ÷ 良率 × 顆數），死於層別良率不可由申報反解。本卡不反解良率；載體為申報之準備提列／回補金額。
  - **L3-A#2**：補助淨額法沖減 PP&E（折舊基數），死於量級。本卡不涉 PP&E；動的是**存貨成本基礎之時點移轉**。
  - **L3-A#3**：封測材料轉嫁（毛利率分母），死於已揭露。本卡分母不變。
  - **L3-A#4**：Intel 合資廠 NCI 歸屬。同一主體、不同恆等（合併邊界）；不改其結論。
  - **L3-A#5**：Intel／Micron 利息資本化（融資成本經 CIP→折舊）。同一主體；彼為 PP&E 成本之時點，本卡為**存貨**成本之時點（ASC 330，非 ASC 835-20）；不改其結論。
  - **L3-P#6**：Micron WIP 天數（Little 定律）之否決 (3) 已列「存貨跌價／迴轉」為**干擾項**；本卡把該項當**主機制**，主體為 Intel，不改 L3-P#6。
  - ARCH_dead：C-A3（折舊年限離散）不同物件；C-I3′／N-02（利益未分列）——本卡準備提列與回補於 10-K／10-Q MD&A 以美元列示（見 §1），但季別、節點別是否可分 → 否決 (1)。
- §7-10 領域最近公開：Intel 10-Q 3Q26（2026-10-30，acc `0000050863-26-000191`）；Intel 3Q26 業績稿 8-K（2026-10-29，acc `0000050863-26-000188`）；Intel 10-K FY25（2026-01-23，acc `0000050863-26-000011`）；ASC 330-10（ASU 2015-11 LCNRV）未見 2026 修訂（測一核）。下一檢查點＝Intel 4Q26 業績稿與 10-K FY26（約 2027-01 下旬）。

## 1. 落差一句

ASC 330：存貨按成本與淨變現價值孰低計價；**銷貨成本_t ≡ 售出單位之（已減記）成本基礎 ＋ 本期新提準備 ＋ 超額產能費用（正常產能外之固定製造費用）**。新節點早期量產單位成本高於淨變現價值 → 準備**先於銷售**認列；該批存貨售出時以減記後基礎入銷貨成本 → 售出期毛利**含已前置之成本**。故 **新節點爬坡期之毛利「改善」≡ 真實成本下降 ＋ 前期準備之售出回補 ＋ 本期未再提準備**；後兩項有限且不重複，下一節點（18A-P／14A）早期量產將重提。
**已讀事實 `[V]`（Intel，sec.py 實讀）：** 10-K FY25：「$878 million of higher 2025 inventory reserves, primarily related to lower of cost or net realizable value charges for products manufactured on the early ramp of our Intel 18A process node」（Intel Foundry 分部間 849M）；「Excess capacity charges were $493 million in 2025, $174 million in 2024 and $834 million in 2023」；會計政策：「Lower of cost or net realizable value inventory reserves fluctuate as we ramp new process technologies」。10-Q 3Q26：Intel Foundry YTD 營業損失 6.4B（YTD25 7.8B），含「$601 million of lower inventory charges driven by the intersegment sell-through of inventory with lower of cost or net realizable value intersegment reserves during the early ramp of our Intel 18A process node」，同時「$936 million of lower product profit … increased mix of higher-cost wafers manufactured on our Intel 18A」；合併毛利亦列「lower inventory-related charges driven by the sell-through of inventory with lower of cost or net realizable value reserves」。業績稿：3Q26 GAAP 毛利率 43.0%；**4Q26 指引 GAAP 37.1%／非 GAAP 38.0%**。
**種子主張：** 公開層以 18A 良率／成本曲線解讀 Intel（Foundry）毛利軌跡；但 2026 之改善部分為 2025 已提準備（≤ 878M）之售出回補，回補存量用盡後此項歸零，且 14A／18A-P 爬坡重提——**以 2026 毛利改善外推成本曲線者高估改善斜率**。`[D]` 粗算：601 ÷ 9M26 營收（測一取數）之毛利率點數為量級上界。方向未定：4Q26 指引下修已可能吸收（否決 (2)）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：`COGS_t ≡ Σ(C_i − R_i)·q_i,t ＋ ΔR_new,t ＋ X_t`（C 單位成本、R 已提單位準備、q 售出量、ΔR 新提、X 超額產能費用）；`ΣR` 售出回補 ≤ 期初準備存量 |
| 選擇者 | 公司（NRV 估計、正常產能定義、FIFO；早期量產是否「qualify for sale」）；稽核（10-K CAM：LCNRV 判斷）；客戶需求（決定售出速度＝回補速度） |
| 已讀事實 | 見 §1 |
| 未證之連結 | 季別回補額與期末剩餘準備存量；Intel Products 端（準備於轉入時才記）與 Foundry 端、合併消除之對應；4Q26 指引下修之構成（PC 需求、產品組合、準備用盡何者主導）；14A／18A-P 重提時點；具名賣方是否已拆出準備回補 |
| 量綱 | 美元 ＝ 美元／片 × 片；毛利率點 ＝ 回補美元 ÷ 營收 |
| 半衰期 | 季（存貨周轉；FIFO 下回補於 1–3 季內流盡） |

## 3. B 端可觀測載體（只指名）

1. Intel 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/50863/000005086326000191/intc-20260926.htm （MD&A Intel Foundry、合併毛利；存貨附註）
2. Intel 10-K FY25 https://www.sec.gov/Archives/edgar/data/50863/000005086326000011/intc-20251227.htm （LCNRV 政策、CAM、分部間消除、超額產能費用）
3. Intel 3Q26 業績稿 8-K https://www.sec.gov/Archives/edgar/data/0000050863/000005086326000188/q326earningsrelease.htm （4Q26 毛利率指引）
4. Intel 10-Q 1Q26／2Q26（季別回補序列）
5. 未讀：3Q26 電話會原文（CFO 對 4Q26 毛利率之歸因）；247wallst 2026-10-25「Intel's Make-or-Break Margin Test」；investinglive「weak q4 guidance」報導；具名賣方對 18A 毛利率之模型；Micron／TSMC 同型 LCNRV 序列（對照）。

## 4. 不寫

H1／H5、表達工具選擇、方向判斷。

## 5. 否決觸發（測一逐條實讀）

1. **可分離性：** 10-K／10-Q 只給年度或 YTD 回補額，無法得季別回補或期末剩餘 18A 準備存量（含 Products 端與合併消除）之任一可量化值 → 否決（C-I3′／N-02 型）。
2. **已被定價／已揭露：** 公司（電話會／業績稿）或具名賣方已明言準備回補對毛利率之貢獻與其終止時點，或 4Q26 指引下修已明列「absence of reserve sell-through」 → 否決（無錯價）。
3. **量級：** 回補額 ÷ 同期合併營收 < 1 個毛利率點，或 < 同期毛利變動之 20% → 否決（同 L3-A#2 死因型）。
4. **重提抵銷：** 18A-P／14A 或其他新品之新提準備與回補同季同量級、公司已以淨額揭露且指引已含 → 否決（恆等成立但無淨效果）。
5. **主體錯置：** 落差主要落於 Intel Products 端而 Foundry 端只為分部間轉列（合併層消除後無淨額）→ 只讀合併層，不在生成階段否決。
6. **口徑：** 準備變動主要來自需求／組合（如 CCPG「aligned product mix with customer demand」之存貨費用）而非節點爬坡 → 標方向分歧，拆分後再判。

## 6. 測一入口

依 §5 (1)–(6) 逐條實讀；SEC 一律 `tools/sec.py`；季別回補 `[D]` 由 1Q26／2Q26／3Q26 10-Q 相減並列算式；12 個月內檢驗事件：Intel 4Q26 業績稿與 10-K FY26（約 2027-01）、1Q27 10-Q、14A 風險量產。
