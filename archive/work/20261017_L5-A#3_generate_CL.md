# L5-A#3 生成卡｜儲存與 IO：會計恆等（全快閃陣列商產品毛利混合恆等：GM_prod ≡ (1−s)·GM_hw + s·GM_roy，零件漲價下 GM 持平 ⇒ 隱含權利金占比 s 可反解）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260926_L5-A_generate_GK.md；archive/drive/USED_20260926_L5-A_test1_GK.md；archive/work/20261011_L5-A#2_generate_CL.md；work/20261011_L5-A#2_test1_CL.md；work/20261017_L5-P#3_test1_CL.md | EMITS: work/20261017_L5-A#3_generate_CL.md -->
**日期：** 2026-10-17　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain）　**格：** L5-A　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L5-P#3 本日測一，Q-0063 done）。最後測試日最舊＝2026-10-11（L5-A、L5-I、L6-P／A／I、L13-A）；依表序取 **L5-A**；非已殺、非刻意排除。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `Everpure hyperscale DirectFlash license`，**命中 0 筆**；載體全由 `sec.py` 與下列 fetch 取得。
- 比對之舊檔與死因型態，本卡須異型：
  - **L5-A#1**（`archive/drive/USED_20260926_L5-A_generate_GK.md`；測一 (1) 觸發）：`C_io = V_KV × P_bit`，雲端儲存 vs 運算美元行不在申報層。本卡不涉 KV、不涉雲端分部。
  - **L5-A#2**（`work/20261011_L5-A#2_test1_CL.md`；(2)(4) 觸發）：HDD 營收 ≡ 台數 × 每台 TB × 每 TB 價，死於共識與同容量點價格不可拆。本卡換**主體**（全快閃陣列商，非媒體製造商）與**恆等式**（毛利混合恆等，非營收量價分解）；主張落在申報層已有之毛利率與管理層歸因句可否反解一個未揭露分量。
  - **L5-P#3**（本日測一不通過）：HDD IO 密度守恆；Everpure 設計勝出理由原文為營運成本／電力／機櫃，非 IO 密度。本卡不主張替代方向。
  - **L5-I#2**（NAND 供給者誘因）、**C-P1**（ARCH_dead #11，訓練 checkpoint）：不同型。重疊列為否決 (5)。
- §7-10 領域最近公開：Everpure 2Q FY27 10-Q（期末 2026-08-02，申報 2026-09-04）；2Q FY27 財報 8-K（2026-08-26）。下一檢查點＝3Q FY27 財報（約 2026-11 下旬，公司未公告日期前不作 `[V]`）。

## 1. 落差一句

Everpure 產品營收含三源：自售陣列（含 NAND 零件成本轉嫁）、**超大規模業者出貨權利金**（第三方硬體、永久授權，依供應鏈出貨認列，近乎無銷貨成本）、Portworx 授權。恆等：`GM_prod ≡ (1−s)·GM_hw + s·GM_roy`，`GM_roy ≈ 1`。10-Q 明文「component pricing」上升壓低硬體毛利，而產品毛利 66%→65% 僅微降、「partially offset by royalties from hyperscaler shipments」——給定 GM_prod 與 GM_hw 之變動區間，`s` 可由恆等反解。種子主張：權利金占比 `s`（即超大規模 EB 部署之美元化速度）未分列，市場以產品營收 +54% 整體外推；恆等式可把「零件價轉嫁」與「權利金量」分離，兩者之半衰期相反（前者隨 NAND 價回落反轉，後者隨 EB 部署累積）。本卡不定方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（毛利混合）；非守恆、非誘因、非量價分解 |
| 選擇者 | 無；`s` 由超大規模出貨量 × 每 TB 權利金決定，`GM_hw` 由 NAND 價與轉嫁率決定 |
| 可見端 | 10-Q：產品營收 446,303→686,773（千美元，+54%）；產品毛利率 66%→65%；「increase in component pricing, partially offset by royalties from hyperscaler shipments」；營收增因「increased pricing with a mix shift to higher performance configurations with terabyte capacity up … and to a lesser extent, royalties from hyperscaler shipments」；權利金認列政策「recognized when the revenue is earned based upon shipments by our supply chain partners」。法說：「pricing, mix shift and capacity growth, offsetting lower system unit volumes」；「Only some of our growth acceleration can be attributed to price increases」；超大規模「order commitments … extend into calendar 2028」「10's of EB」 |
| 指名不可見端 | 權利金金額或占比、每 TB 權利金率、超大規模出貨 EB、硬體單獨毛利、轉嫁率；10-Q「per terabyte」「NAND」0 筆 |
| 主張 | 恆等式兩分量於公開層可給出 `s` 之區間；若 `s` 區間與市場以整體產品營收外推之隱含值不同，構成可測落差；可被分部或權利金金額揭露拒絕 |
| 表達工具型態（只指名，不選券） | 美股全快閃陣列商（Everpure）。不選券 |
| 重疊 | L5-A#2（同層會計恆等）、L5-P#3（同層替代敘事）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Everpure 2Q FY27 10-Q（acc 0001474432-26-000088）。https://www.sec.gov/Archives/edgar/data/1474432/000147443226000088/pstg-20260802.htm
2. Everpure 1Q FY27 10-Q。https://www.sec.gov/Archives/edgar/data/1474432/000147443226000061/pstg-20260503.htm ；FY26 10-K https://www.sec.gov/Archives/edgar/data/1474432/000147443226000027/pstg-20260201.htm
3. Everpure 2Q FY27 8-K ex99.1。https://www.sec.gov/Archives/edgar/data/0001474432/000147443226000084/everpure-ex991q2fy2027xpre.htm
4. 法說報導（二手）：Blocks & Files 2026-08-27。https://www.blocksandfiles.com/flash/2026/08/27/everpure-the-artist-formerly-known-as-pure-storage-ramps-up-growth-rate/5292871
5. 測一須另取：法說逐字稿原文（權利金、EB、轉嫁）；NAND 合約價季變動（TrendForce 等具名來源）以界定 `GM_hw`；≥ 4 季產品毛利率與歸因句。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 市場已以「定價回應」為焦點觀察 | William Blair（Ader）：「a full quarter of data showing how customers respond to materially higher pricing levels」（#4） | 已定價 |
| R2 | 管理層已定性拆分：權利金為「to a lesser extent」 | 10-Q（#1） | `s` 小，落差不顯著 |
| R3 | 公司刻意「operate at the lower end of our product gross margin range」 | Giancarlo（#4） | GM 為管理變數，恆等反解受政策污染 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) `GM_hw` 或轉嫁率無任何原文或具名第三方區間，恆等式只剩一式兩未知，`s` 不可解。
(2) 公司或具名賣方已量化權利金金額／占比，或已量化價格 vs 量對產品營收成長之貢獻（落差即共識）。
(3) ≥ 4 季產品毛利率與歸因句顯示權利金影響低於毛利率揭露精度（整數 %），`s` 區間含 0。
(4) 申報層無權利金、超大規模或 EB 之任何可對帳科目，且無替代科目可拒絕（§7-4 財報科目題不可答）。
(5) 可運作對照只能寫成 HDD 營收量價恆等（L5-A#2）、NAND 供給誘因（L5-I#2）或 IO 密度替代（L5-P#3）。
(6) 毛利率為公司自承之管理變數（R3）且無可分離之外生分量，使恆等式反解無識別。

複查觸發器（若日後殺）：Everpure 首次於 10-Q／10-K 分列權利金或超大規模營收；或首次揭露超大規模出貨 EB 之季數列。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：產品營收、產品毛利率、RPO、權利金認列政策句。
2. 可交易工具：Everpure 美股（不選券）。
3. 半衰期：NAND 價週期（轉嫁分量）vs 超大規模承諾至 CY2028（權利金分量）。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0064；`query/ARCH_matrix.md` L5［A］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L5-A#1／#2、L5-P#1–#3、L5-I#1／#2、C-P1 結論。
