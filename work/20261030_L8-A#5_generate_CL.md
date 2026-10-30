# L8-A#5 生成卡｜標註／驗證：會計恆等（匯兌損益之科目歸屬恆等——同一離岸人力匯兌效果，INOD 入直接營運成本、TASK 移出營業線並自 Adjusted EBITDA 排除）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260918_L8-A_generate_GK.md；archive/work/20261007_L8-A#2_generate_CL.md；archive/work/20261015_L8-A#3_generate_CL.md；archive/work/20261023_L8-A#4_generate_CL.md；work/20261023_L8-A#4_test1_CL.md；archive/work/20261007_L8-I#2_generate_CL.md；archive/work/20261015_L8-I#3_generate_CL.md；archive/work/20261023_L8-I#4_generate_CL.md | EMITS: work/20261030_L8-A#5_generate_CL.md -->
**日期：** 2026-10-30　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 2→3／6）　**格：** L8-A　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。非「已殺／刻意排除」格中最後測一最舊＝2026-10-23（L8-A#4、L8-I#4、L9-A#4、L9-I#4、L12-P#4）→ 依表序取 **L8-A**（L8-P 已殺不取）；既有生成 4 份 → #5。附記：上一輪 L1-A#5 生成卡 §0 以 2026-10-24 為最舊，與 ARCH_matrix 所載 10-23 批不符；本卡不改該卡，僅依現表選格。
- Tokenomics 線索（CLAUDE.md §11）：已查 `TaskUs`／`Innodata`／`foreign currency`，命中 0 筆。內部數字（§12）：未取用。
- 比對（本卡須異型）：
  - **L8-A#1**（GK）：支出 ÷ 有效條數（產出單位分母）；死於分母不可得。本卡不用產出單位。
  - **L8-A#2**：賣方未開票收入（認列時點）。本卡不涉收入認列。（TASK 應收含未開票 127.4 百萬——屬 #2 型，本卡不用。）
  - **L8-A#3**：INOD 客戶預付之轉付成本（營運資本）。本卡不涉營運資本。
  - **L8-A#4**：買方（META）持有 Scale 股權之衡量替代法帳面。本卡不涉投資帳面。
  - **L8-I#2／#3／#4**（買方持股轉單、勞動分類或有負債、可終止合約 × 客戶集中）：誘因型；本卡不以客戶集中或終止權為落差（TASK Client A 26%→20%、Client B 11% 僅作背景，不入機制）。
  - **C-I2**（專家單價歸因）：本卡不涉單價；TASK 管理層之「operating shift to higher cost geographies」歸因不作本卡機制。
  - ARCH_dead 其餘（C-A3 折舊年限、C-A4／C-A1 可分離性等）：不涉。
- §7-10 領域最近公開：TASK 10-Q 2Q26（申報 2026-08-06，acc `0001829864-26-000149`）與 8-K 業績稿（acc `0001829864-26-000147`）；INOD 10-Q 2Q26（申報 2026-08-06，acc `0001104659-26-092021`）。下一檢查點＝兩家 3Q26 10-Q（約 2026-11 上旬）。

## 1. 落差一句

美股兩家可交易之標註／驗證人力供應商，成本基礎同為菲律賓、印度等離岸人力，但**同一經濟項目（離岸成本之匯兌效果）落在不同科目**：INOD 之菲、印、斯里蘭卡子公司功能貨幣＝美元，「realized (gain) loss on forward contracts, foreign currency revaluation (gain) loss」與未指定避險之公允值變動**全入直接營運成本**（即入毛利率 46%、Adjusted Gross Margin 49%，2Q26）；TASK 子公司以當地幣換算（2Q26 外幣換算調整 −3,050 千入 OCI），指定避險之重分類入 Cost of services（2Q26 931 千損失），但未指定避險之公允值變動與美元帳戶重衡量入營業線以下之「Other income, net」（2Q26 −5,033 千、1H26 −12,359 千），且於 Adjusted EBITDA 調節中列「Foreign currency losses (gains)」**排除**（2Q26 −3,854 千、1H26 −9,457 千；1H26 Adjusted EBITDA 116,229 千）。恆等：**經濟離岸人力成本（美元）≡ 帳列營業成本 ± 指定避險重分類 ± 未指定避險與重衡量損益**；後一項在 INOD 進毛利、在 TASK 出營業線並出 Adjusted EBITDA。種子主張：同層兩主體之毛利率／Adjusted EBITDA 率與其比較，含一項**科目歸屬而非營運**之成分；1H26 TASK 之排除額約為其 Adjusted EBITDA 之 8% `[D]`（9,457 ÷ 116,229）。**方向未定**：匯率反轉時 TASK 之排除項轉為損失（Adjusted 指標高於 GAAP），INOD 則直接壓毛利。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：功能貨幣選擇（ASC 830）× 避險指定（ASC 815）× 非 GAAP 排除項 → 同一匯兌效果之科目路由 |
| 已讀事實 | TASK 10-Q 2Q26：遠期合約「maturities of generally 12 months or less」，避險 PHP／INR／MXN／COP／EUR 之預期成本；未結指定避險名目 301,449 千（PHP 163,622）；AOCL 預計 12 個月內重分類淨損 0.7 百萬；「Other income, net — Changes are driven by our exposure to foreign currency exchange risk … primarily the Philippines, including economic hedges」。8-K 業績稿註 (3)：「Realized and unrealized foreign currency losses and gains include the effect of fair market value changes of forward contracts not designated as hedging instruments and remeasurement of U.S. dollar-denominated accounts to foreign currency」。INOD 10-Q 2Q26：子公司功能貨幣＝美元；「For derivative instruments that are not designated as hedges, any change in fair value is recorded directly in earnings as part of direct operating costs」；指定避險名目 34.9 百萬（2025 末 19.7）。 |
| 未證之連結 | INOD 直接營運成本內匯兌項之金額（10-Q 未見單列）；TASK 排除項中屬「預期成本之經濟避險」與「美元帳戶重衡量」之拆分；賣方是否以 Adjusted EBITDA 率比較兩家；PHP／INR 對美元之期間走勢。此即測一第一關。 |
| 量綱 | 排除額 ÷ Adjusted EBITDA（%）；匯兌項 ÷ 直接營運成本（%）；兩家毛利率差中科目歸屬成分（pp） |
| 選擇變數 | 管理層：功能貨幣判定、避險指定與否、非 GAAP 排除項定義 |
| 半衰期 | 每季重報；遠期合約 ≤ 12 個月滾動 |

## 3. B 端可觀測載體（只指名）

1. TASK 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1829864/000182986426000149/task-20260630.htm （Note 4 Forward Contracts、AOCL 附註、MD&A Other income、Item 3 市場風險）
2. TASK 8-K 2Q26 業績稿 https://www.sec.gov/Archives/edgar/data/0001829864/000182986426000147/earningsreleaseex991q22026.htm （Adjusted EBITDA 調節表與註 (3)；全年指引 Adjusted EBITDA margin ~19%）
3. INOD 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/903651/000110465926092021/inod-20260630x10q.htm （功能貨幣政策、衍生工具政策、直接營運成本定義、AOCL 表、Adjusted Gross Profit 調節）
4. 待測一指名讀：TASK 與 INOD 3Q26 10-Q；TASK FY2025 10-K 功能貨幣政策原文；INOD FY2025 10-K 匯兌損益金額（若單列）；兩家業績電話會原文就匯率對毛利／EBITDA 之量化；具名賣方之同層比較表。

缺段（§7-2）：INOD 匯兌項金額、TASK 排除項之拆分、賣方原文；本輪只讀上列；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 兩家皆依 GAAP 揭露，政策段原文可讀，屬已揭露之會計選擇，不是錯價 | 載體 1、3 政策段 | 恆等無資訊落差 |
| R2 | TASK 指定避險重分類已入 Cost of services，12 個月內待重分類僅 0.7 百萬；營業線之匯兌效果已大致鎖定，排除項主要為資產負債重衡量，非人力成本 | 載體 1 | 經濟成本已在營業線 |
| R3 | 兩家主營組成不同（TASK 以 CX／Trust & Safety 為主、AI Services 為成長線；INOD 以 AI 資料工程為主），毛利率比較本即不可直接對照 | 載體 2、3 | 比較基礎不存在 |
| R4 | 量級：9,457 千 ÷ 1H26 營收 615,121 千 `[D]` 約 1.5%；對估值影響有限 `[A]` | 載體 2 | 終端條件，本輪不篩（§7-3），僅列 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法自兩家申報確認匯兌項之科目路由差異（INOD 入直接營運成本、TASK 未指定避險入 Other income 並自 Adjusted EBITDA 排除），或任一方於最近申報已改變政策；或
(2) 可運作對照只能寫成一般「非 GAAP 排除項」或任何跨國服務業之匯兌揭露，而無標註層特有之結構（同層兩家可交易主體、離岸人力成本為主要成本、毛利／EBITDA 率為同層比較口徑）；或
(3) 具名賣方、評等機構或兩家管理層已公開量化匯兌對毛利／Adjusted EBITDA 之影響並據以調整同層比較（已定價）；或
(4) `[D]` 量級：最近 4 季內，TASK 排除額 ÷ Adjusted EBITDA 之絕對值 < 3%，且 INOD 直接營運成本內匯兌項 ÷ 毛利 < 3%（若 INOD 金額不可得，以 TASK 單邊判）；或
(5) 12 個月內無可觀測驅動：無 3Q26／4Q26／FY2026 10-K 之可指名申報日，或 PHP／INR 期間波動不足以使排除項改號。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Other income, net、Cost of services／Direct operating costs、AOCL、Adjusted EBITDA 調節。2. 可交易工具：TASK、INOD（不選）。3. 半衰期：季度重報 vs ≥ 12 個月窗。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L8［A］格加「#5 已生成」；`AIM_FUNNEL.md` 日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0131。不改 L8-A#1–#4、L8-I／#2／#3／#4、L8-P、C-I2 結論。
