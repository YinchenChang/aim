# L14-A#2 生成卡｜企業終端需求：會計恆等（買方 AI 支出之費用化／資本化分流：AI 現金支出 ＝ 當期費用 ＋ 資本化增量；報表營業費用 ＝ 當期費用 ＋ 既往資本化之攤銷——AI「省下之營業費用」可部分為分類與時序，而非淨節省）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/FILEIDS.tsv；archive/drive/USED_20261005_L14-A_generate_GK.md；archive/drive/USED_20261005_L14-A_test1_GK.md；archive/work/20261013_L14-P#2_generate_CL.md；work/20261013_L14-P#2_test1_CL.md | EMITS: work/20261013_L14-A#2_generate_CL.md -->
**日期：** 2026-10-13　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 5→6／6；chain 觸發）　**格：** L14-A　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L14-P#2 測一 2026-10-13，Q-0038 done）。非已殺／刻意排除且無 #2 之格＝L14-A／I、L15-P／A／I；`archive/FILEIDS.tsv` 測一時間最舊者＝L14-A（2026-10-05T13:59Z；L14-I 14:19Z、L15-P 14:38Z、L15-A／I 10-07）→ **L14-A**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `capitalized software`、`internal-use software`、`ASU 2025-06`，0 筆；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L14-A#1**（測一不通過，`archive/drive/USED_20261005_L14-A_test1_GK.md`）：IT 支出 ÷ 總營收之**比重水準**；死因＝同一 10-K／10-Q 無法並列 IT 支出、總營收與 AI 行（JPM「Technology, communications and equipment」含汽車租賃折舊）。本卡不以 IT 比重為樞紐；守恆量是**同一筆 AI 支出在現金流量表與損益表之分流**（費用化 vs 資本化／預付資產），可見端是現金流量表資本化軟體行與資產附註之攤銷，不需 IT 支出總額。
  - **L14-P#1**（席次 ≤ 員工數）、**L14-P#2**（預付容量承諾池；死因＝滾存條款僅 1 家）、**L14-I**（預算回流）：不涉。
  - **C-A2**（已殺，ARCH_dead #9，企業 AI 預算單位經濟）：不主張每單位毛利或 ROI。**C-A1**（席次 vs token 不可分列）、**L15-A**（使用量 vs 單價）：不涉賣方定價。
  - **L11-P／L8-P／L9-P**（已殺）：不涉。
- §7-10 領域最近公開：FASB ASU 2025-06（2025-09 發布；年度期間始於 2027-12-15 後生效，得提前採用）；Hershey 10-Q 2Q26（2026-08）、JPM 10-Q 2Q26（2026-08-06）均稱「evaluating」。下一檢查點＝各公司 FY26 10-K（2027-02／03）之採用日與影響揭露。

## 1. 落差一句

市場把企業報表上「AI 導入後營業費用率下降」讀成 AI 帶來之淨節省；種子主張 AI 支出在 GAAP 下分流——訂閱費當期費用化，但雲端安排實作成本（ASC 350-40，記為預付資產、按託管期攤銷）與內部開發人力（應用開發期）可資本化——故導入期報表營業費用低估 AI 現金支出、攤銷期再回到費用；且 ASU 2025-06 改變資本化起點（FASB 預期雲端實作成本資本化**減少**），採用時點會造成營業費用之一次性台階。錯價只在把分類與時序效果讀成淨節省。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等**：\(C^{AI}_t = E^{AI}_t + \Delta K^{AI}_t\)；\(OpEx^{AI}_t = E^{AI}_t + A_t\)，\(A_t=\sum_{s<t} K_s/\tau\)。\(OpEx_t - C_t = A_t - \Delta K_t\)：導入加速期 < 0（報表低估），攤銷期 > 0 |
| 選擇者 | 買方管理層（資本化政策、ASU 2025-06 採用時點與過渡法：prospective／retrospective／modified） |
| 可見端 | 現金流量表「capitalized software／internal-use software」或「purchases of software」行；資產附註之資本化軟體毛額、累計攤銷、攤銷費用；ASC 350-40 雲端實作成本預付資產餘額與攤銷；ASU 2025-06 採用揭露；管理層之 AI 效率敘述 |
| 指名不可見端 | 資本化中 AI 所占比例；費用化 AI 訂閱額；攤銷年限 \(\tau\) 對 AI 項之適用 |
| 表達工具型態（只指名，不選券） | 美股可交易、宣稱 AI 帶動營業費用率改善、且資本化軟體行重大之非科技企業。不選券 |

**不主張方向、不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. FASB 規則文本（經公司申報轉錄）：Hershey 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/0000047111/000162828026050900/hsy-20260628.htm ：「ASU No. 2025-06 … removing all references to software development project stages … costs are capitalized when management has authorized and committed funding and it is probable the project will be completed … effective for annual reporting periods beginning after December 15, 2027 … Early adoption is permitted … prospective, retrospective or modified transition approach」；「currently evaluating」。
2. JPMorgan Chase 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/19617/000162828026054343/jpm-20260630.htm ：ASU 2025-06「The Firm is evaluating the potential impact … as well as the Firm's planned date of adoption」；費用行「Technology, communications and equipment」3,107 vs 2,704（百萬，三個月）含汽車租賃折舊（L14-A#1 死因之同一行，本卡不用其水準）。資本化軟體行待查。
3. 會計師事務所解讀：Crowe「How to account for AI spend under US GAAP」https://www.crowe.com/insights/how-to-account-for-ai-spend-under-us-gaap ：「the recurring subscription fee is recorded as a period expense」；實作成本「must be recognized as a prepaid asset … expensed on a straight-line basis over the term of the hosting arrangement」；合格者含「Loaded payroll costs of AI engineers, data scientists, and machine learning infrastructure engineers」；「the revised standard could result in a decrease in CCA implementation cost capitalization」。
4. 第二解讀（未實讀）：CLA https://www.claconnect.com/en/resources/articles/26/internal-use-software ；CFGI https://www.cfgi.com/asu-2025-06-targeted-improvements-to-the-accounting-for-internal-use-software/

缺段（§7-2）：未取任何非科技企業 ≥ 4 期資本化軟體序列；未找到市場以「AI 淨節省」讀費用率之具名錨；提前採用 ASU 2025-06 之企業名單未查（EDGAR FTS 不可用，WebSearch 候選須 sec.py 實讀）。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 訂閱型 AI（主流採購形態）一律當期費用化，資本化空間小 | Crowe（§3-3） | 分流量級可能不足 |
| R2 | ASU 2025-06 預期**減少**雲端實作成本資本化 → 採用後分類效果反向且縮小 | Crowe（§3-3） | 落差於 2028 前後自行收斂 |
| R3 | 資本化軟體與攤銷每期揭露於現金流量表與附註，分析師慣於加回 | — | 可能已定價 |
| R4 | 非科技企業之資本化軟體行多合併於「capital expenditures」，無法分出軟體 | JPM 10-Q（§3-2）待查 | 可見端可能不存在 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後 ≥ 2 家宣稱 AI 效率之非科技企業，無法於同一 10-K／10-Q 取得 ≥ 4 期之資本化軟體（或雲端實作成本預付資產）增量與攤銷費用之同口徑分列；或
(2) 可運作對照只能寫成 IT 支出 ÷ 營收（L14-A#1）、席次 ≤ 員工數（L14-P#1）、預付容量池（L14-P#2）、預算回流（L14-I）、單位經濟（C-A2）、單價（L15-A）或 AI COGS 分列（C-A1）；或
(3) 具名賣方／公司原文已就「AI 效率」中之資本化與攤銷效果分列量化（已定價）；或
(4) `[D]` 資本化軟體增量相對營業費用變動 < 10%，或 \(A_t - \Delta K_t\) 於樣本期近零（分流量級不足）；或
(5) 12 個月內無可觀測驅動：無 ASU 2025-06 提前採用揭露、無資本化政策變更、無 AI 效率之管理層量化敘述。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：現金流量表資本化軟體行、資產附註攤銷、營業費用。2. 可交易工具：宣稱 AI 效率之企業股權（不選）。3. 半衰期：攤銷年限（常見 3–5 年）與 ASU 2025-06 生效（年度期間始於 2027-12-15 後）。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L14［A］格加「#2 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列。不改 L14-A#1、L14-P#1／#2、L14-I、C-A2、C-A1、L15-A 結論。
