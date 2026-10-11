# L4-P#2 生成卡｜運算硬體系統：守恆（封裝供電電流守恆：I＝P／V 與 I²R，橫向供電之電流密度上界迫使垂直供電，轉換時點為可算門檻而非供應商選擇）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/INDEX.json；query/RETRIG_3.md；archive/drive/USED_20260926_L4-P_generate_GK.md；archive/drive/USED_20260926_L4-P_test1_GK.md；archive/drive/USED_20260926_L4-A_generate_GK.md；archive/drive/USED_20260926_L4-I_generate_GK.md | EMITS: work/20261011_L4-P#2_generate_CL.md -->
**日期：** 2026-10-11　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L4-P　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。最後測試日最舊＝2026-09-26 一批中尚無 #2 者：L4-P／L4-A／L4-I、L5-A／L5-I（L3-P／L3-I 已於 10-09 重測）；依表序取 **L4-P**（非已殺、非刻意排除）。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py "power delivery" "vertical power" "800 VDC"`，命中 **0** 筆；本卡載體全由原文檢索取得。
- 比對之舊檔與死因型態，本卡須異型：
  - **L4-P#1**（`archive/drive/USED_20260926_L4-P_generate_GK.md`；測一 `archive/drive/USED_20260926_L4-P_test1_GK.md`）：**訊號**通道損耗封頂被動銅距離（`R_cu < D_domain`）；死於否決 (1)——CEI 目標距離與機櫃毫米不在同一官方表、公尺不在 10-K、Networking 一桶。本卡換為**供電電流**守恆（功率／電壓／電阻，非訊號頻寬／距離）；B 端換為**已在申報層分列之科目**（Vicor 損益表 Royalty revenue 行與 Advanced／Brick 產品線；MPS Enterprise Data 終端市場行），不依賴標準距離表。
  - **N-02**（`query/ARCH_dead.md` #15；L4-P#1 註為「熱／電密度閘門」）：死於 (a) CPO 營收於上市主體未分列（RETRIG R-15 2026-10-09 仍未觸發）。本卡表達點不是光學／CPO 營收，而是供電元件與供電專利授權之已分列行。重疊於「密度閘門」之概念層；表達點不同，不併、不復活 N-02。
  - **C-I3′**（#14，UL 型／分部毛利由非機制項解釋）：本卡須在測一自證載體行之變動可由機制項（電流密度門檻）而非一次性項（授權新約、和解金）解釋——列為否決觸發 (2)。
  - **N-01**（#17，機隊世代組成非科目）：不同物件。
  - **L4-A**（系統 BOM 恆等）、**L4-I**（開放機櫃 commoditize-the-complement）：會計／誘因，構成不同。
  - **L2-P#2**（資料中心實體守恆）與機架層 800 VDC：本卡邊界限於**封裝／主機板層**（處理器 VR 至晶粒），不及機架母線與設施配電，以免滑入 L2。
- §7-10 領域最近公開：Vicor 2Q26 10-Q（期末 2026-06-30）與 2Q26 法說（2026-07-21）；MPS 2Q26 10-Q（期末 2026-06-30）；Google「Towards 10kAmp AI Chip」（IEEE T-CPMT 2026）；Infineon TDM2454xx VPD 模組發表（2026）。下一檢查點＝Vicor／MPS 3Q26 10-Q（約 2026-10 下旬至 11 月初）；Vicor 第二件 ITC 案終局裁定（法說稱 2027）。

## 1. 落差一句

加速器封裝電流 `I_core = P_pkg ÷ V_core`；`P_pkg` 每代上升而 `V_core` 已近 ~0.7–0.8 V 下限，故 `I_core` 已越過千安級、朝 10,000 A（Google，T-CPMT 2026）；橫向供電損耗 `∝ I_core² × R_lateral`、且可用電流密度受封裝周邊面積封頂，**當 `I_core ÷ A_shadow` 超過橫向可達之 A/mm² 時，垂直供電（VPD）是被迫而非選項**——公開層把 VPD 讀成供應商之間的設計勝負與「下一代產品」敘事（Vicor：3 A/mm² 基線、明年 5 A/mm²、量產「明年第三季末／第四季」；Infineon：2 A/mm²），而**轉換門檻本身（每代加速器之 `I_core` 與 `A_shadow`）未被公開對帳**；落差＝若門檻可由公開 TDP／電壓／封裝尺寸反算，則 VPD 採用時點與受影響之已分列科目（供電元件營收、供電專利權利金）可事前排序，而非事後歸因於「需求改善」。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆／物理：電荷守恆＋焦耳損耗（`P = V·I`；`P_loss = I²R`）；電流密度上界 `J_max`（A/mm²）× 可用面積 ≥ `I_core`；非會計恆等、非誘因 |
| 選擇者 | 加速器商（TDP、核心電壓、封裝尺寸）；供電元件商（模組電流密度）；主機板／ODM（橫向或垂直佈局） |
| 可見端 | Vicor 10-Q：Royalty revenue 行（2Q26 30,426 vs 2Q25 10,353，千美元）、Advanced Products 行；MD&A 稱增幅「primarily due to higher royalty revenue due to a new license agreement」。MPS 10-Q：Enterprise Data 終端市場（2Q26 380,561，佔 38.8%；2Q25 143,964），增幅「primarily due to higher sales of power management solutions for artificial intelligence」。模組規格：Vicor 650 A 連續／1200 A 峰值（48 V 直供）、GCM 目標 2 A/mm²；Infineon 280 A／四相、2 A/mm² |
| 指名不可見端 | 每代加速器之 `I_core`、`V_core`、封裝下方可用面積 `A_shadow`；橫向可達 `J_lat_max`；VPD vs 橫向之出貨拆分；權利金之計費基礎（單位、架構或一次性總包） |
| 主張 | `I_core ÷ A_shadow > J_lat_max ⇒` 橫向供電不可行，VPD 成為必要；門檻穿越時點由加速器路線圖決定，可事前算 |
| 表達工具型態（只指名，不選券） | 已上市、美股可交易之供電元件或供電專利授權揭露主體（Vicor、MPS；Infineon 為 OTC ADR，僅作反方載體）。不選券 |
| 重疊 | N-02（密度閘門概念；表達點不同）；L4-A（BOM 中機電項）；L2-P#2（設施層，本卡不及）。重疊不構成丟棄 |

守恆式（生成用，非正式載入）：`I_core = P_pkg / V_core`；橫向可行 ⇔ `I_core ≤ J_lat_max × A_lat`。本輪不估參數、不寫 H1。

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Vicor 2Q26 10-Q（Royalty revenue／Product revenue 損益行；Note 6 依產品線×收入類別：Advanced Products 之 Royalties 30,426、NRE 1,932；Brick 無權利金）。https://www.sec.gov/Archives/edgar/data/0000751978/000119312526322462/vicr-20260630.htm
2. Vicor 2Q26 法說（2026-07-21；CEO：3 A/mm² 基線已完成；VP Sales：明年 5 A/mm²、量產「late third quarter, fourth quarter of next year」；CFO：新授權約 Q2 認列 15、Q3 5、此後每季 10（百萬美元，兩年合計 60）；第二件 ITC 終局 2027；「one hyperscaler」授權）。https://www.fool.com/earnings/call-transcripts/2026/07/21/vicor-vicr-q2-2026-earnings-call-transcript/
3. MPS 2Q26 10-Q（MD&A 終端市場表 Enterprise Data；單一報導分部）。https://www.sec.gov/Archives/edgar/data/0001280452/000162828026053275/mpwr-20260630.htm
4. Google，「Towards 10kAmp AI Chip: A System Perspective from Lateral to Vertical Power Delivery」，IEEE T-CPMT 2026（摘要：電流需求「rapidly exceeding the 10,000 A threshold」；LPD 之「fundamental physical limitations」）。https://research.google/pubs/towards-10kamp-ai-chip-a-system-perspective-from-lateral-to-vertical-power-delivery-2/
5. Vicor 1200A ChiP-set 新聞稿（650 A 連續／1200 A 峰值，48 V 直供；GCM 目標 2 A/mm²、「eliminating PDN losses」）。https://www.vicorpower.com/press-room/hydra-ii
6. Infineon TDM2454xx VPD 模組（280 A／四相；2 A/mm²；橫向沿晶圓表面佈線增阻）。https://newelectronics.co.uk/content/product-launches/infineon-unveils-high-density-power-modules-for-vpd-in-ai-data-centres

測一須另取：加速器商（NVIDIA／AMD／Broadcom 客製）公開之 TDP 與封裝尺寸、核心電壓或可反解之 VR 規格；Vicor 10-K 授權／訴訟附註（Note 11）原文；MPS 10-K 產品線敘述。**不宣稱 `I_core` 已有官方時序，不宣稱權利金行由機制驅動，不宣稱已錯價。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 權利金行之躍升由**一次性授權新約**與訴訟和解驅動，非由電流門檻；兩年總包「all-inclusive」與單位無關 | Vicor 2Q26 10-Q MD&A；法說 CFO／CEO | 可見科目之變動可由非機制項解釋（C-I3′ 型） |
| R2 | MPS Enterprise Data 為「power management solutions for AI and server」一桶，不分 VPD／橫向、不分加速器／CPU | MPS 2Q26 10-Q | 科目過寬，量綱不對（L4-P#1 同型風險，量不同） |
| R3 | VPD 多家同時供貨（Vicor、Infineon、MPS 等），物理門檻真但利益被競爭分攤，門檻穿越不歸任一主體 | Infineon 2 A/mm² 模組；Vicor「Gen 1 competitive solutions」 | 機制成立 ≠ 可捕捉（§7-4） |
| R4 | `V_core` 與 `A_shadow` 可被設計移動（背面供電 BSPDN、提高中間匯流電壓、多晶粒分割），門檻被工程推遲 | Google T-CPMT 2026 列「input voltage choices」「module granularity」 | 門檻非固定常數，時點不可事前排序 |
| R5 | 市場已按「AI 供電」敘事定價（MPS Enterprise Data 年增 164%） | MPS 2Q26 10-Q | 機制真、價已反映 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 對加速器商公開規格與 OEM／ODM 資料實讀後，`I_core`（或 `P_pkg`＋`V_core`）與 `A_shadow` 無法形成可對帳區間，只剩模組 A/mm² 與路線圖一句（即重演 L4-P#1 否決 (1)）。
(2) Vicor Royalty revenue 之 ≥ 4 季序列之變動可完全由授權新約起訖、和解金與 ITC 事件解釋，而無與加速器世代對應之單位計費證據（C-I3′ 型）。
(3) MPS 10-K／10-Q 無任何低於 Enterprise Data 之供電架構拆分，且 MD&A 無 VPD 字樣（量綱不對）。
(4) 公開層已有穩定可拒絕之「現行與下一代加速器以橫向供電即可」或「VPD 已全面量產」之陳述，使門檻與可見定價不可辨。
(5) 可運作對照只能寫成機架 800 VDC／設施配電（滑入 L2）或 CPO／光學營收（滑回 N-02）。

複查觸發器（若日後殺）：任一美股可交易供電元件或授權主體於 10-K／10-Q 分列垂直供電（或等價：按加速器世代／電流級距）之營收或權利金計費基礎，且可與同期加速器公開 TDP／封裝尺寸對帳。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：VPD 收入或權利金能否自 Advanced Products／Enterprise Data 再拆；能否拒絕一般伺服器供電。
2. 可交易工具：恆等落在美股可交易揭露主體，而非僅 OTC ADR 或私有模組商。
3. 半衰期：BSPDN／中間電壓上調或多家 VPD 齊供時，≥ 12 個月窗內門檻利益是否被工程或競爭抵銷。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L4［P］標「#2 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG。不改 L4-P#1／L4-A／L4-I／N-02／C-I3′／N-01 結論。
