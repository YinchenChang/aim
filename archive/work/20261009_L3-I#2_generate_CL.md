# L3-I#2 生成卡｜半導體製造測試：誘因（政府股東之「51% 代工持有」認股權證＝分拆選擇權之或有稀釋懸崖，成本隨股價上升）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260926_L3-I_generate_GK.md；archive/drive/USED_20260926_L3-I_test1_GK.md；work/20261008_L3-A#2_test1_CL.md | EMITS: work/20261009_L3-I#2_generate_CL.md -->
**日期：** 2026-10-09　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain 續跑）　**格：** L3-I　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L3-P#2 已測畢，`work/20261009_L3-P#2_test1_CL.md`）。最後測試日最舊＝2026-09-26 一批（L3-I、L4-P／A／I、L5-A／I）；依表序取 **L3-I**（非已殺、非刻意排除）。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py Intel foundry warrant CHIPS`，命中 14 筆，皆為 GPU 機櫃規格、保固、模型評測（SRC_HW_061/062、SRC_DC_016、SRC_CAP_*），與本卡無關，**未採用**。
- 比對之舊檔與死因型態，本卡須異型：
  - L3-I#1（`archive/drive/USED_20260926_L3-I_generate_GK.md`；測一 `archive/drive/USED_20260926_L3-I_test1_GK.md`）：**產能預付款＝合約性取用權**（客戶↔代工之排序權與下修損失歸屬）；已測｜不進 T。本卡換為**股東層或有權利**（政府↔發行人之認股權證條件），選擇者為發行人董事會之結構決策，非客戶產能配置。
  - L3-A#2（`work/20261008_L3-A#2_test1_CL.md`）：政府補助**淨額法**沖減 PP&E（會計恆等）。本卡不涉補助會計；同一協議中之**股權工具條件**為誘因型，構成不同。
  - L3-P#1／#2（曝光機時、HBM 良率乘積）：物理型，不同。
  - ARCH_dead：無政府持股／認股權證型；C-I3′（L4，UL 型）、C-I1（L7，P1 無錯價）物件不同。不併。
- §7-10 領域最近公開：Intel 2Q26 10-Q（期末 2026-06-27，2026-07-24 申報）；Intel 8-K 2026-08-12（US$20B 增資，每股 95 美元）；Intel FY25 10-K（2026-01-23）。下一檢查點＝Intel 3Q26 10-Q（約 2026-10 下旬）；14A 外部客戶確定承諾（報導窗 2H26–1H27）。

## 1. 落差一句

2025-08 美國商務部（DOC）入股 Intel，另取得**認股權證**：Intel 若「cease to directly or indirectly own at least 51% of our foundry business」，DOC 可按每股 20 美元認購至多 2.41 億股（Intel FY25 10-K）。此條款使「分拆／出售代工多數股權」這一選擇權附帶**或有稀釋**，其成本＝2.41 億 ×（股價 − 20）：入股時股價約 20 美元、成本近零；2026-08 增資定價 95 美元時約 2.41 億 × 75 ≈ US$18B 級（以增資價粗算，非估值）。**落差＝誘因隨成功而收緊**：14A 若取得外部客戶、股價上升，分拆代工之稀釋懸崖等比放大，董事會越不可能跨越 51% 門檻——市場若仍以「代工可分拆」之分部加總選擇權定價，則該選擇權之履約成本被低估；反之若 14A 失敗、股價下跌，懸崖縮小、分拆選擇權反而變便宜。**方向未定**，且 DOC 依約隨董事會投票（10-K），治理影響與經濟影響須分拆。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因：或有權利（條件式認股權證）＋表決權讓渡；分拆選擇權之履約價內生於股價 |
| 選擇者 | Intel 董事會（代工持股比例、合資／出售結構）；DOC（是否行使、「保護政府利益」之表決例外）；14A 潛在外部客戶（承諾與否決定股價路徑） |
| 可見端 | 10-K：權證 2.41 億股、20 美元、51% 條件；「neither currently nor expected to become exercisable」；DOC「agreed to vote its shares … as recommended by our board」並有「exceptions to protect the U.S. government's interests」；風險因子「may substantially limit our ability to pursue potential future strategic transactions」；14A 若無重大外部客戶可能暫停。2Q26 10-Q：代工營收 5,765／營業損失 (2,089)（百萬，2Q26），「substantially all … supports internal manufacturing」；權證排除於稀釋 EPS。8-K：每股 95 美元增資 |
| 指名不可見端 | 權證到期日與「indirectly own」之計算口徑（合資、VIE、優先股是否計入）；DOC 表決例外之觸發範圍；董事會對分拆之內部評估 |
| 主張 | 權證把分拆選擇權之成本綁在股價上；以 49% 少數股權引資（不觸發）與多數股權出售（觸發）之價值差，公開層未被分列討論 |
| 表達工具型態（只指名，不選券） | 美股上市之 IDM／代工發行人普通股與上市選擇權。不選券 |

對照式（生成用，非正式載入）：`C_split(S) = N_w × max(S − K, 0)`，`N_w = 241M`、`K = 20`；分拆淨值 `= V_SOTP(S) − V_integrated(S) − C_split(S)`。本輪不估參數、不寫 H1。

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| Intel FY25 10-K（U.S. Government Agreement；Note「Warrant Condition」；風險因子：表決、策略交易受限、14A 外部客戶） | https://www.sec.gov/Archives/edgar/data/50863/000005086326000011/intc-20251227.htm |
| Intel 2Q26 10-Q（Note 4 EPS 權證排除；代工分部損益；外部客戶句） | https://www.sec.gov/Archives/edgar/data/50863/000005086326000157/intc-20260627.htm |
| Intel 8-K 2026-08-12 增資新聞稿（95 美元） | https://www.sec.gov/Archives/edgar/data/0000050863/000119312526346806/d117670dex992.htm |
| 權證條件之二手轉述（5 年期；CFO Zinsner「didn't want to see us take the business and spin it off or sell it」「expire unused」）；測一須回原始協議（8-K 2025-08 附件）或法說原文 | https://mindsetonline.com/trump-administrations-deal-aims-to-retain-intels-foundry-unit-despite-financial-challenges/ |
| 14A 外部客戶進度（評估中、無簽約；PDK 秋季；確定承諾 2H26–1H27） | https://aiweekly.co/alerts/intel-promises-apple-and-terafab-a-14a-pdk-milestone-this-fall |

不宣稱董事會欲分拆、不宣稱權證將被行使、不宣稱市場以分部加總定價。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 量級小：以 95 美元粗算，懸崖約占市值個位數百分比；分拆價值差若大於此，懸崖不改決策 | Intel 8-K 2026-08-12 股數與價格；10-K 權證股數 | 誘因不足以改變結構決策 |
| R2 | 規避：「at least 51%」只限多數股權；以 ≤ 49% 引資、合資或預付（如 Altera 先例之反向）可取得大部分分拆價值而不觸發 | Intel FY25 10-K Warrant Condition 原文 | 選擇權仍在，只是型態受限 |
| R3 | 管理層明言不分拆、權證「expire unused」；市場本未給分拆選擇權價值，無錯價 | 10-K「neither currently nor expected to become exercisable」；CFO 轉述 | 已定價為零 |
| R4 | 到期：權證約 5 年（2030 前後），在剩餘實驗期內自然失效，懸崖有時限 | 二手轉述（測一須核原協議） | 窗內效果遞減 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) 原協議或 10-K 明定「indirectly own」含合資／少數股權引資之計算，使 ≤ 49% 引資即可取得分拆主要價值且不觸發（R2 成立）。
- (2) 以公開股數與近期股價粗算之 `C_split` 低於市值之一個量級門檻（測一自行界定並寫明），且無任一具名分析或公司文件把權證列為分拆障礙（R1）。
- (3) 公開層（法說、10-K、具名賣方）已明示把權證成本納入分拆評估，或公司已正式排除分拆——落差已被揭露或選擇權已被放棄（R3）。
- (4) 本卡只能以 L3-I#1 之預付取用權、L3-A#2 之補助淨額法、或 L2-I 之法定取用權重述（重疊判讀）。
- (5) 權證到期或條件失效落在 < 12 個月內，或 14A 外部客戶決策在窗內不可見，使效果不可辨（R4）。

複查觸發器（若日後殺）：Intel 或 DOC 修改權證條件或到期日；Intel 公告代工引資、合資或出售且揭露持股比例；具名賣方或公司文件將權證納入代工分拆估值。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：權證列永久權益、排除於稀釋 EPS；觸發時之稀釋入股數，不入損益——可觀測只有股數與條件。
2. 可交易工具：發行人普通股與選擇權；分拆事件為離散跳躍，表達須先界定事件與股價路徑之相關。
3. 半衰期：權證約至 2030；14A 承諾窗 2H26–1H27；觸發事件（引資公告）時點不可排程。

## 7. 本輪寫入

本卡；QUEUE 新列（ANALYST 測一）；ARCH_matrix L3-I 格標「已生成 #2」；FUNNEL §3 未測格計數。不改 L3-I#1／L3-A#1／L3-A#2／L3-P#1／L3-P#2／L2-I。
