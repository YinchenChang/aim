# L3-P#2 生成卡｜半導體製造測試：守恆（HBM 堆疊良率為乘積：每好位元之晶圓投入隨堆疊高度非線性上升，公開「3:1」為靜態常數）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/INDEX.json；archive/drive/USED_20260926_L3-P_generate_GK.md；archive/drive/USED_20260926_L3-P_test1_GK.md；archive/drive/USED_20260927_L5-P_generate_GK.md | EMITS: work/20261009_L3-P#2_generate_CL.md -->
**日期：** 2026-10-09　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L3-P　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L1-I#2 已測畢，`work/20261009_L1-I#2_test1_CL.md`）。最後測試日最舊＝2026-09-26 一批（L3-P、L3-I、L4-P／A／I、L5-A／I；L1-I、L1-A 已於 10-08／10-09 重測）；依表序取 **L3-P**（非已殺、非刻意排除）。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py HBM "trade ratio" "stack yield"`，命中 13 筆，皆為 HBM 容量／頻寬／存取能量規格（SRC_HW_020…059），與本卡載體無關，**未採用**。
- 比對之舊檔與死因型態，本卡須異型：
  - L3-P#1（`archive/drive/USED_20260926_L3-P_generate_GK.md`；測一 `archive/drive/USED_20260926_L3-P_test1_GK.md`）：曝光機 **時間守恆**上界（WPH × 機台 × 可用率 ÷ 每層曝光次數）；死於可觀測性——賣方只給認列台數與條件化 WPH，客戶側層曝光產能不可對帳。本卡型態換為**乘積良率**（複合機率，非機時守恆），選擇者換為記憶體廠（非曝光機賣方），載體為**記憶體廠自報之晶圓投入比與堆疊高度路線**（非 ISO／賣方出貨）。
  - L5-P（`archive/drive/USED_20260927_L5-P_generate_GK.md`）：decode 吞吐上界＝BW／V_byte——**需求側**頻寬守恆。本卡為**供給側**良率乘積，不涉 decode。
  - L3-A#1／#2（有效晶粒單價恆等；政府補助淨額法）、L3-I（預付款取用權）：會計／誘因，構成不同。
  - ARCH_dead C-P1（L5，checkpoint 儲存）：不同物件。N-05（3h 相鄰）不入死母體，不併。
- §7-10 領域最近公開：Micron FY26 10-K（期末 2026-09-03，acc `0000723125-26-000023`，**2026-10-09 申報**）；Micron FQ4'26 法說（約 2026-09 下旬：「completed agreements for the vast majority of our calendar 2027 HBM bit supply」，經 The Next Platform 2026-10-02 轉述）；Hot Chips 2026（2026-08-23）Micron 堆疊高度與良率發言（經 XenoSpectrum 2026-08-27 轉述 Tom's Hardware）。下一檢查點＝Micron FQ1'27 法說（約 2026-12 中）、SK hynix 3Q26 法說（約 2026-10 下旬）。

## 1. 落差一句

HBM 之好堆疊良率是乘積：`Y_stack ≈ Y_KGD-escape^n × Y_bond^(n−1) × Y_base × Y_final`，故每顆好 HBM 之 DRAM 晶圓投入隨堆疊高度 `n` 與單晶粒面積**非線性**上升；公開層只有 Micron 2026-03 之 HBM3E「**3:1** 對 DDR5 投入比」一個靜態常數，HBM4 投入比**未揭露**（XenoSpectrum 2026-08-27），而 2027 HBM 位元已多數以協議鎖定（Micron FQ4'26）——**落差＝若 12→16 層與 HBM4 大晶粒使投入比顯著 > 3，則 (a) 非 HBM DRAM 之有效位元供給被擠壓多於以「3:1 × HBM 位元份額」外推之量，或 (b) 已鎖價之 2027 HBM 協議之單位成本上升**。**方向未定**：(a) 對記憶體廠為正（傳統 DRAM 偏緊）、(b) 為負（鎖價後成本升）；若 KGD 篩選使晶粒良率不入乘積（R2），落差縮為只剩接合良率。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 物理：乘積良率（複合機率）→ 每好位元晶圓投入 `W/bit ∝ (die area × n) ÷ (bits × Y_stack)`；非機時守恆、非頻寬守恆 |
| 選擇者 | 記憶體廠（堆疊高度、晶粒尺寸、KGD 篩選嚴格度、接合法：TC-NCF／MR-MUF／混合接合）；GPU／ASIC 買方（12-high vs 16-high 規格）；JEDEC（封裝高度上限） |
| 可見端 | Micron FY26 10-K：「In 2026, HBM3E 12-high represented the majority of our HBM shipments」、HBM4 36GB 12-high 量產、HBM4 48GB 16-high 送樣、「new products that may require relatively larger die sizes or advanced packaging technologies」列成本風險；3:1（HBM3E，2026-03 財報材料）；Hot Chips 2026：16 層有路徑、更高「still requires substantial further development」、單一晶粒缺陷影響整顆封裝 |
| 指名不可見端 | HBM4／16-high 之晶圓投入比；`Y_bond`、`Y_final` 逐高度；KGD 篩選後之逃逸率；HBM 收入與位元份額（Micron 已不分列——The Next Platform 2026-10-02） |
| 主張 | 公開之 3:1 為 12-high HBM3E 之點值；以之外推 2027 HBM4／16-high 混合低估晶圓投入；觸發事件＝記憶體廠揭露 HBM4 投入比、16-high 良率爬坡延誤、或 2027 協議價重議 |
| 表達工具型態（只指名，不選券） | 美股上市之 DRAM／HBM 製造商；KRX 上市者只作 B 端參照，不入表達集（§2-8 台股禁；韓股不在可交易範圍）。不選券 |

對照式（生成用，非正式載入）：`TR(n) = TR_0 × (n/n_0) × (Y_stack(n_0)/Y_stack(n)) × (A_die(n)/A_die(n_0))`；`TR_0 = 3`（HBM3E 12-high）。`Y_bond → 1` 且 KGD 逃逸 → 0 時，`TR(n)` 只隨晶粒面積線性變，本卡落差消失。本輪不估參數、不寫 H1。

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| Micron FY26 10-K（Item 1 HBM 產品組合句；Item 1A 成本風險「larger die sizes or advanced packaging」；Item 2「will need to add new DRAM wafer capacity」） | https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm |
| Micron FQ3'26 10-Q（HBM 僅見於術語表與 Netlist 訴訟；無投入比） | https://www.sec.gov/Archives/edgar/data/723125/000072312526000015/mu-20260528.htm |
| Micron 2026-03 財報材料（3:1）；測一須回原始 IR 材料或逐字稿 | 二手錨：https://xenospectrum.com/en/micron-hbm-ddr-silicon-gap/ |
| Hot Chips 2026 Micron 發言（16 層路徑、熱阻、單晶粒缺陷）；測一須回原講稿或 Tom's Hardware 原文 | https://www.tomshardware.com/tag/hot-chips-2026 （標籤頁；原文待測一定位） |
| Micron FQ4'26 法說（2027 HBM 協議）、HBM 不再分列 | https://www.nextplatform.com/store/2026/10/02/microns-numbers-show-why-hbm4-memory-is-worth-15x-its-weight-in-gold/5300701 |
| SK hynix／Samsung 法說之 HBM4／16-high 良率與投入比（參照，不表達） | 測一自行定位 |

不宣稱 HBM4 投入比 > 3、不宣稱 16-high 良率不足、不宣稱 2027 協議會重議。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 投入比已公開且管理層明言「this gap will not narrow」——市場已按「HBM 吃三倍晶圓」定價，DRAM 緊缺為共識 | Micron 2026-03 財報材料／Q&A（XenoSpectrum 2026-08-27 轉述 Tom's Hardware） | 已定價；落差只剩「3 之後之斜率」 |
| R2 | KGD（已知良晶粒）測試在堆疊前剔除壞晶粒，晶粒良率對晶圓投入只線性作用；乘積只剩接合與最終測試 | 記憶體廠 HBM 流程（測一須取 SK hynix／Micron 原文） | 指數項縮小 → 量級不足 |
| R3 | 2027 主力仍為 12-high（10-K：2026 以 12-high 為主；16-high 僅送樣），16-high 份額在 ≥ 12 個月窗內小 | Micron FY26 10-K | 窗內不可見 |
| R4 | 協議多含成本轉嫁或年度重議；鎖價不等於鎖成本承擔 | Micron FQ4'26 法說（協議條款未公開） | (b) 通道無股東損失 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) 任一記憶體廠（Micron／SK hynix／Samsung）已公開 HBM4 或 16-high 之晶圓投入比或堆疊良率，且市場共識已據以更新（R1 延伸）——落差已被揭露。
- (2) 實讀製程原文後，KGD 篩選使晶粒良率不入乘積，且接合良率公開 ≥ 99% 級（或同等陳述），`TR(n)` 對 `n` 近線性（R2 成立）。
- (3) 16-high 與 HBM4 大晶粒於 2027 之出貨份額在公開層不可見或明示居次，使效果在 ≥ 12 個月窗內不可辨（R3）。
- (4) 本卡只能以 L3-P#1 之機時上界、L5-P 之頻寬守恆、或 L3-A 之有效晶粒單價恆等重述（重疊判讀）。
- (5) 美股可交易主體之 HBM 收入、位元或成本不分列（Micron 已停揭露），使 (a)(b) 兩通道均無法與申報科目對帳。

複查觸發器（若日後殺）：任一美股上市記憶體廠於 10-K／10-Q 或法說原文揭露 HBM4／16-high 之晶圓投入比或堆疊良率，或重新分列 HBM 收入／位元；或 2027 HBM 協議價重議之公開事件。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：投入比之變動落在 COGS／毛利、存貨（在製堆疊）或產能資本支出；HBM 是否分列。
2. 可交易工具：(a) 傳統 DRAM 偏緊（記憶體廠受益）與 (b) 鎖價成本上升（記憶體廠受損）同落一主體，淨方向須先拆。
3. 半衰期：16-high 量產爬坡約 2027；協議年度週期；觸發事件是否在 ≥ 12 個月窗內可見。

## 7. 本輪寫入

本卡；QUEUE 新列（ANALYST 測一）；ARCH_matrix L3-P 格標「已生成 #2」；FUNNEL §3 未測格計數。不改 L3-P#1／L3-A#1／L3-A#2／L3-I／L5-P／C-P1。
