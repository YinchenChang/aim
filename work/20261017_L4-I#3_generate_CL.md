# L4-I#3 生成卡｜運算硬體系統：誘因（外部選項商品化：自研加速器轉為對外銷售後，買方切換門檻對全市場下移，加速器商之訂價上限隨之下移）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260926_L4-I_generate_GK.md；archive/drive/USED_20260926_L4-I_test1_GK.md；archive/work/20261011_L4-I#2_generate_CL.md；work/20261011_L4-I#2_test1_CL.md；work/20261017_L4-A#3_test1_CL.md；work/20261017_L4-P#3_test1_CL.md | EMITS: work/20261017_L4-I#3_generate_CL.md -->
**日期：** 2026-10-17　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain）　**格：** L4-I　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L4-A#3 本日已測一）。最後測試日最舊＝2026-10-11（L4-I、L5-P／A／I、L6-P／A／I、L13-A）；依表序取 **L4-I**；非已殺、非刻意排除。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `ASIC TPU Broadcom "custom accelerator"`、`TPU`：0 筆；`NVIDIA "gross margin"`：命中 15 筆，多為規格；唯 **SRC_HW_010**（GB300 NVL72 採購單價；Data Gravity 2026-08-31）與本卡之「每單位算力價格」對照有關，**列為線索，未採為證據**（線索：Tokenomics SRC_HW_010；ANALYST 須回原文）。
- 比對之舊檔與死因型態，本卡須異型：
  - **L4-I#1**（`archive/drive/USED_20260926_L4-I_generate_GK.md`）：開放機櫃參考設計＝commoditize-the-complement，壓**整機商**。本卡之對象為**加速器商自身之訂價上限**，由**買方外部選項**決定，非互補品。
  - **L4-I#2**（`work/20261011_L4-I#2_test1_CL.md`）：讓價之**形式**（回租承諾、擔保、權證取代降價）；死於 (1) 已揭露。本卡為讓價之**原因與門檻**（外部選項何時對第三方可得）；形式不論。重疊：若讓價以 #2 之形式出現，觀測端會重疊——照記，ANALYST 以 (5) 判。
  - **C-I3′**（ARCH_dead #14）：生態鎖定支撐毛利，死於分部毛利由非機制項解釋。本卡為其鏡像（鎖定之上限由外部選項設定）；死因型態（UL 型）是否同樣適用由 (5) 判。
  - **N-01**（ARCH_dead #17）：機隊世代組成非科目；其觸發器「GOOGL 首次分列 TPU 外部產品線」。**觀察（非本卡結論）：** Alphabet 2Q26 10-Q（2026-07-23）載「in the second quarter of 2026, we began recognizing revenue from the sale of TPU systems」、Google Cloud「Product sales, primarily the sale of TPU systems」——是否構成 R-17「分列」由 SCOUT-WATCH 判；本輪於 QUEUE 另立一列，不改 RETRIG。
  - **L4-A#3**（權證會計）、**L4-P#3**（HBM 守恆）、**L13-I**、**N-02**：構成不同。
- §7-10 領域最近公開：Alphabet 2Q26 10-Q（2026-07-23）；Broadcom 3Q FY26 10-Q（2026-09-10，期末 2026-08-02）；NVIDIA 2Q FY27 10-Q（2026-08-26）；AMD 2Q26 10-Q（2026-08-05）。下一檢查點：Alphabet 3Q26（約 2026-10 末）、AMD 3Q26（約 2026-11 初）、NVIDIA 3Q FY27（約 2026-11 下旬）、Broadcom 4Q FY26（約 2026-12）。

## 1. 落差一句

加速器商（NVIDIA、AMD）之 DC 毛利受買方「自研或外購替代」之切換門檻約束：`P_merchant − P_alt × (性能比) ≤ S`（S＝軟體／遷移成本）。過去替代品（TPU、Trainium、客製 XPU）只對**其擁有者**可得，門檻只約束少數買方；2026 年 Alphabet 開始**對外出售 TPU systems**、Broadcom 稱 XPU 需求來自「leading frontier AI labs」，替代品成為**第三方可購之商品**，門檻對所有大買方同時下移。落差＝市場若仍以「替代品只影響自研者之份額」建模，則加速器商之有效價格（毛利、或 #2 型非價格讓步）之下修時點與幅度可能被低估；反之若加速器商之毛利或讓步已隨外部選項可得而變動、且已被具名機構量化，則落差不存在。**方向未定**；本卡不主張份額或毛利之變動方向與量級。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因（訂價上限／外部選項）：`GM_merchant` 之上界由買方切換門檻 `S` 與替代品之性能調整價 `P_alt` 決定；替代品由「自用」轉「可購」使受約束之買方集合擴大。非守恆、非會計恆等 |
| 量綱 | 價格比無量綱：`P_merchant／(P_alt × perf)`［($／單位算力)÷($／單位算力)］；`S` 以［$／單位算力］或［月遷移工時］表示；毛利率［%］ |
| 可見端 | Alphabet 10-Q：TPU systems 產品銷售自 2Q26 起認列、「significant majority to be recognized in 2027」；Broadcom 10-Q：「unprecedented demand for our custom AI accelerators or XPUs」及 AI XPV 融資平台；NVIDIA／AMD 10-Q：DC 分部毛利／營業利益 |
| 指名不可見端 | TPU systems 收入金額是否分列；買方之替代品報價與性能比；`S` 之量級；NVIDIA 對個別買方之實際折讓 |
| 主張 | 外部選項由自用轉可購之日（2Q26 起）為門檻下移之可觀測事件；若加速器商之毛利或非價格讓步在其後數季出現與此日對齊之變化，且未被具名賣方歸因於此，則存在落差 |
| 外部參照物（測一查證） | 前例：x86 伺服器 CPU 對 Arm 自研（Graviton）之價格反應；或 Intel 於 AMD EPYC 可購後之毛利路徑。僅作機制先例，非量級 |
| 表達工具型態（只指名，不選券） | 美股上市加速器商、客製晶片設計商、雲端商之普通股與上市選擇權。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| Alphabet 2Q26 10-Q（TPU systems 產品銷售、存貨、TPU 供應協議） | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm |
| Broadcom 3Q FY26 10-Q（XPU 需求、AI XPV 平台） | https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm |
| NVIDIA 2Q FY27 10-Q（DC 毛利、直接客戶集中度） | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm |
| AMD 2Q26 10-Q（DC 分部營業利益） | https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm |
| GB300 NVL72 採購單價（線索：Tokenomics SRC_HW_010） | https://www.datagravity.dev/p/how-much-does-an-nvidia-nvl72-cost |
| 第三方 TPU 採購（Anthropic、Meta 等）之公司公告與報導 | 測一以 WebSearch 取得，回原始公告實讀 |

不宣稱門檻已下移、不宣稱毛利方向。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 外部 TPU／XPU 對加速器商訂價之壓力已被具名賣方或研究機構量化 | 測一查（如 SemiAnalysis TPU 系列、賣方 TPU 外售估算） | 落差已揭露 |
| R2 | 需求遠大於總供給（CoWoS／HBM 受限），替代品可購不改變加速器商之邊際訂價 | 測一查 NVIDIA／TSMC 供給敘述、L4-P#3 已記之 HBM 約束 | 機制在 12 個月窗內不綁定 |
| R3 | `S`（CUDA 遷移成本）遠大於價差，門檻未實際移動 | 測一查 | 機制弱化 |
| R4 | TPU systems 收入不分列，門檻事件不可量化 | Alphabet 10-Q | 可觀測性不足 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) ≥ 1 位具名賣方或研究機構已公開量化「外部可購替代品 → 加速器商價格或毛利」之連動（R1）。
- (2) 主要加速器商之 DC 毛利或分部營業利益率在 2Q26 前後 ≥ 2 期無與門檻事件對齊之變化，且管理層以供給／產品組合解釋（C-I3′ 型）。
- (3) 加速器商與替代品均受同一上游約束（CoWoS／HBM）而供給受限，使 12 個月窗內門檻不綁定（R2）。
- (4) TPU systems 或 XPU 之第三方銷售量級無一手可得，且二手量級 < 加速器商 DC 收入之門檻（測一自定，如 5%）。
- (5) 本卡只能以 L4-I#2（讓步形式）、C-I3′（生態鎖定）或 N-01（機隊組成）重述。
- (6) 前例（Graviton／EPYC 等）顯示外部選項可得後，既有供應商毛利於 12 個月內未變動，或前例結構不可比。

複查觸發器（若日後殺）：Alphabet 首次以金額分列 TPU systems 收入；NVIDIA／AMD 毛利指引首次以競爭定價為因；Broadcom 或 Alphabet 揭露 XPU／TPU 第三方客戶數或量級；第三方大型實驗室公告以替代品取代加速器商之已簽量。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：加速器商 DC 毛利率／分部營業利益；Alphabet Google Cloud 產品銷售與存貨；Broadcom 半導體分部收入。
2. 可交易工具：美股上市加速器商、客製晶片設計商、雲端商之普通股與上市選擇權（不選）。
3. 半衰期：季至年（TPU systems 收入「significant majority … in 2027」；加速器商世代約年度）。

## 7. 本輪寫入

本卡；QUEUE 新列（ANALYST 測一）；QUEUE 另列（SCOUT：R-17／N-01 複查，因 §0 觀察）；ARCH_matrix L4［I］格標「#3 已生成」；FUNNEL §3 未測格計數。不改 L4-I#1／#2、L4-A#1–#3、L4-P#1–#3、C-I3′、N-01、N-02、L13-I、RETRIG。
