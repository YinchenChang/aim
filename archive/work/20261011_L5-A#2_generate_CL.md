# L5-A#2 生成卡｜儲存與 IO：會計恆等（HDD 營收 ≡ 台數 × 每台 TB × 每 TB 價；台數封頂時營收成長 ≡ 面密度成長 × 價）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260926_L5-A_generate_GK.md；archive/drive/USED_20260926_L5-A_test1_GK.md；archive/drive/USED_20260929_L5-P_T_GK.md | EMITS: work/20261011_L5-A#2_generate_CL.md -->
**日期：** 2026-10-11　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain）　**格：** L5-A　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L4-I#2 已於本日測一）。最後測試日最舊＝2026-09-26 一批尚無 #2 者：L5-A、L5-I；依表序取 **L5-A**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py exabyte "hard disk" nearline`，命中 **0** 筆；載體由 `sec.py` 原文取得。
- 比對之舊檔與死因型態，本卡須異型：
  - **L5-A#1**（`archive/drive/USED_20260926_L5-A_generate_GK.md`；測一 `archive/drive/USED_20260926_L5-A_test1_GK.md`）：`C_io = V_KV × P_bit`；死於 (1)＝所需量（雲端儲存 vs 運算美元行、KV 位元×單價）**不在申報層**。本卡換為**儲存媒體製造商自身之出貨恆等**：營收、EB 出貨（分 nearline／non-nearline）、每 EB 均價變動率為 **10-K 原文數字且 ≥ 2 期**。
  - **L5-P**（T 已寫｜不進 L；`archive/drive/USED_20260929_L5-P_T_GK.md`）：HBM 頻寬守恆、decode 上界。本卡不涉 HBM、不涉推論吞吐。
  - **C-P1**（ARCH_dead #11，L5）：訓練 checkpoint／復原。本卡不以工作負載歸因，只用供給端恆等。重疊列為否決 (5)。
  - **L5-I#1**（出站費／資料重力）：雲端定價誘因，非本卡。
  - **L3-P#2**（HBM 堆疊良率）、**L4-A#2**（整機商營運資本）：層與構成不同。
- §7-10 領域最近公開：Seagate FY26 10-K（期末 2026-07-03，申報 2026-08-04）；Western Digital FY26 10-K（期末 2026-07-03，申報 2026-08-14）。下一檢查點＝兩家 FQ1'27 10-Q／財報 8-K（約 2026-10 下旬）。

## 1. 落差一句

HDD 營收恆等於 `Units × (TB/unit) × ($/TB)`。若台數受磁頭／碟片產能封頂（業者不擴台數產能、以面密度供給 EB），則 EB 成長 ≡ 每台 TB 成長（HAMR／ePMR 換代節奏），營收成長 ≡ 面密度成長 ×（1＋每 TB 價變動）。**落差＝市場以資料量需求（AI 資料湖、IDC 資料圈 ~27% CAGR）外推 HDD 營收，而恆等式使前瞻營收之上界由面密度路線圖與每 TB 價決定，非由需求決定；兩家同年 EB 與 $/TB 之拆分已分歧**（Seagate FY26：EB 595→789、營收 9,097→12,195 百萬，混合 $/TB 近持平；WDC FY26：EB +25%、每 EB 均價 +8%「improved pricing environment」）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（營收之乘積分解）＋供給封頂；非誘因 |
| 選擇者 | HDD 製造商（台數產能、換代節奏、長約定價）；雲端買方（容量點選擇） |
| 可見端 | Seagate 10-K：EB 分 nearline 695／497、non-nearline 94／98；營收；Data Center 營收占比 80%／75%。WDC 10-K：營收 12,919／9,520／6,317；「25% increase in exabytes sold and an 8% increase in ASPs per exabyte」；Cloud 占 89%，EB +27%、ASP/EB +8% |
| 指名不可見端 | 台數或平均每台 TB 之季序列（申報層是否揭露未知；財報簡報可能有）；同容量點之單價（like-for-like $/TB） vs 容量點組合效應；台數產能上限之原文 |
| 主張 | 台數封頂下 `g_Rev ≈ g_TB/unit + g_$/TB`；面密度換代延遲 → EB 成長斷檔，非需求斷檔；$/TB 由組合（大容量點每 TB 較便宜）與同容量點漲價兩股相反力組成，合併數掩蓋後者 |
| 表達工具型態（只指名，不選券） | 美股可交易 HDD 製造商（Seagate、Western Digital）。不選券 |
| 重疊 | C-P1（儲存需求歸因）；NAND／eSSD 替代週期；L5-I。重疊不構成丟棄 |

對照式（生成用，非正式載入）：`Rev ≡ U × c × p`，`c = TB/unit`，`p = $/TB`；`ΔlnRev = ΔlnU + Δlnc + Δlnp`；封頂 ⇒ `ΔlnU ≈ 0`。本輪不估參數、不寫 H1。

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Seagate FY26 10-K（MD&A「HDD Exabytes Shipped」表、Overview「789 exabytes」、areal density／Mozaic HAMR 段）。https://www.sec.gov/Archives/edgar/data/1137789/000113778926000159/stx-20260703.htm
2. Seagate FQ2／FQ3 FY26 10-Q（季 EB 序列）。https://www.sec.gov/Archives/edgar/data/1137789/000113778926000026/stx-20260102.htm ；https://www.sec.gov/Archives/edgar/data/1137789/000113778926000088/stx-20260403.htm
3. Western Digital FY26 10-K（Net Revenue 段 EB 與 ASP/EB 變動率；HAMR／ePMR 路線圖；long-term agreements）。https://www.sec.gov/Archives/edgar/data/106040/000162828026057139/wdc-20260703.htm
4. Western Digital FQ3 FY26 10-Q。https://www.sec.gov/Archives/edgar/data/106040/000162828026029054/wdc-20260403.htm
5. 兩家財報 8-K 附件／簡報（平均每台容量、台數、資本支出指引；測一須以 `sec.py filings --form 8-K` 定位，本輪未讀）。

測一須另取：台數或平均每台 TB ≥ 4 季；資本支出與「不增台數產能」之原文；同容量點價格之任何原文（LTA 定價條款）；具名賣方或媒體是否已以「面密度 × 價」建模營收。**不宣稱已錯價，不宣稱封頂成立。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 業者自己已把營收拆成 EB × ASP/EB 並公開「產能紀律、以面密度成長」，落差為共識 | WDC 10-K Net Revenue 段；兩家法說 | 共識 |
| R2 | 台數未封頂：業者可擴磁頭／碟片產能或延長舊平台壽命 | 兩家資本支出指引 | 恆等不綁 |
| R3 | $/TB 變動主要為容量點組合，與同容量點價格不可分 | 混合均價定義 | 拆分不可辨 |
| R4 | 需求端由 NAND／QLC eSSD 替代主導，HDD 營收是替代比問題非面密度問題 | 儲存產業評論 | 機制換層 |
| R5 | 長約（LTA）鎖量鎖價，前瞻 12 個月營收已大致可見 | WDC「long-term agreements with certain customers」 | 半衰期／無落差 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 兩家 ≥ 4 季申報與財報 8-K 均不揭露台數或平均每台 TB，只剩 EB 與營收（`U` 與 `c` 不可分）。
(2) 公開層（業者原文或具名賣方／媒體）已明文以「EB ＝台數 × 每台容量、台數持平」或「營收 ≈ 面密度 × 價」建模並量化，使落差為共識。
(3) 任一家申報或指引原文顯示擴充台數產能（資本支出階躍、新磁頭／碟片產線），台數不封頂。
(4) $/TB 之變動於申報層無法區分組合效應與同容量點價格（只有混合 ASP/EB），且無其他原文可拆。
(5) 可運作對照只能寫成工作負載歸因（訓練 checkpoint＝C-P1）、雲端出站費（L5-I）或 NAND 週期。

複查觸發器（若日後殺）：任一美股可交易 HDD 製造商於 10-K／10-Q 或財報 8-K 揭露台數與平均每台容量 ≥ 4 季，或揭露同容量點價格／LTA 定價變動，或宣布台數產能擴充／縮減。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：營收、EB（10-K 表）、ASP/EB 變動率（WDC 敘述）；台數與每台 TB 是否在申報層。
2. 可交易工具：Seagate、Western Digital 皆美股可交易；產業集中（兩家＋Toshiba 非美股）。
3. 半衰期：面密度換代（HAMR 量產爬坡）之時點是否落在 ≥ 12 個月窗；LTA 期限。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L5［A］標「#2 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L5-A#1／L5-P／L5-I／C-P1／L3-P#2／L4-A#2 結論。
