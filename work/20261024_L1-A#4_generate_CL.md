# L1-A#4 生成卡｜能源與電力：會計恆等（大負載客戶預付款之損益路徑——受管電業淨利 ≡ 費率基報酬 ＋ 客戶預付款攤銷收入 ＋ 稅負墊高攤銷 − 預付款持有成本）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260926_L1-A_generate_GK.md；archive/work/20261008_L1-A#2_generate_CL.md；archive/work/20261016_L1-A#3_generate_CL.md；work/20261016_L1-A#3_test1_CL.md；archive/work/20261009_L1-I#2_generate_CL.md | EMITS: work/20261024_L1-A#4_generate_CL.md -->
**日期：** 2026-10-24　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1→2／6）　**格：** L1-A　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。非「已殺／刻意排除」格中最後測一最舊＝2026-10-16（L1-A#3、L1-I#3、L3-P#3、L3-A#3、L12-A#3、L12-I#3；10-15 批已於 10-23 依表序補 #4）→ 依表序取 **L1-A**（L1-P＝刻意排除 T-11 不取）；既有生成 3 份 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `contribution in aid of construction`／`CIAC`／`rate base`／`utility`，命中 0 筆。內部數字（§12）：未取用。
- 比對（本卡須異型）：
  - **L1-A#1**（GK）：PPA 鎖定價 − 現貨＝存量；死於鎖定價與現貨無法同主體分離。本卡不談電價。
  - **L1-A#2**：Bloom 產品／服務營收認列時差。主體與恆等不同。
  - **L1-A#3**（`work/20261016_L1-A#3_test1_CL.md`）：AFUDC 權益——電業**自有資本**之在建報酬資本化（非現金、待入費率基）。本卡為**客戶資金**：大負載客戶預付款（customer advances／customer advances for construction）在建期即以**營業收入**（「return on construction work in progress」）及**其他收入**（稅負墊高攤銷）認列，並伴隨利息費用（預付款持有成本）；且預付款支應之資本支出**排除於資本計畫**、不入費率基。AFUDC 為 NI_cash 以外之非現金項；本卡之項目有現金對應但**依附單一合約、隨建設完成而終止**。測一須判二者是否於同一電業同季重疊計算，不得合併。
  - **L1-I#2**：大負載最低需量只及新約、未覆蓋部分落於其他費率類別（誘因／分攤）。本卡不談擱淺分攤，談已收預付款在損益表之認列路徑。
  - ARCH_dead：C-A3（折舊年限樞紐）、C-I3′／N-02（利益未分列）——本卡之項目**已分列**於 MD&A 變動表與附註，型態不同。T-11 不碰。
- §7-10 領域最近公開：Entergy 10-Q 2Q26（2026-07-31，acc `0000065984-26-000283`）；Entergy 10-K FY25（2026-02-19，acc `0000065984-26-000174`）。下一檢查點＝Entergy 3Q26 10-Q／業績（約 2026-10 底～11 初）；LPSC 就 Hyperion 擴建 ESA（Pelican Policy 2026-04-10 報導之約 7.5 GW、20 年 ESA）之程序。

## 1. 落差一句

受管電業淨利 ≡ 核定 ROE × 費率基 ＋ 客戶預付款攤銷之「在建報酬」收入 ＋ 預付款稅負墊高（tax gross-up）攤銷 − 預付款持有成本（carrying costs，入利息費用）＋ …。Entergy 2Q26：營收變動表單列「Return on construction work in progress for certain utility plant investments」+40M（1H +70M；Entergy Louisiana +25.7M／1H +43.2M），其他收入「amortization of tax gross-up on customer advances」+31M（季額 40.4M vs 9.1M；FY25 已 +65M），利息費用「carrying costs on customer advances」+18M；同季歸屬 Entergy 淨利約 482.6M。種子主張：市場以費率基成長外推電業 EPS 成長，未把**依附個別大負載合約、於建設期間認列、建成後即止**之預付款損益項自費率基報酬中分離——此等項目之持續期與規模由合約之預付款時程決定，而非由費率基決定。**方向未定**：可為建設期 EPS 之暫時抬升（建成後斷崖），亦可為被低估之無風險合約收入（客戶出資、股東不承擔資本）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：NI ＝ ROE×E×RB ＋ R_cwip（預付款攤銷收入，依成本發生認列）＋ A_gu（稅負墊高攤銷，其他收入）− I_adv（預付款持有成本）＋ 其他；預付款支應之 capex 不入 RB（10-Q：「The planned construction and capital investments amounts above exclude investments expected to be funded with customer advances for construction」） |
| 已讀事實 | Entergy 10-Q 2Q26（sec.py 全文）：「The return on construction work in progress … represents the revenue related to the amortization of certain customer advances designed to provide a return on investment in construction work in progress for certain utility plant investments, which is recognized as the related costs are incurred」；資產負債表 Customer advances（流動）1,470,056 vs 632,850、（非流動）170,298 vs 35,000、Customer advances for construction 2,086,359 vs 1,615,455（千美元，2026-06-30 vs 2025-12-31）；1H26 財務活動 Customer advances received for construction 885,867、used (436,221)；營業現金流增加「$700 million in receipts of advance payments related to customer agreements, including $599 million in customer advances and $101 million in tax gross-up」；稅負墊高攤銷 1H26 63.2M（ELL 42.5M）vs 24.6M。10-K FY25：大負載資料中心合約「contribute significant funds, through contributions in aid of construction or through minimum bill revenues … customer advances for construction, and credit and collateral requirements」。 |
| 未證之連結 | 各預付款對應之合約／客戶（Meta Hyperion 等）與攤銷時程；R_cwip 與 A_gu 之未來序列（建成日）；A_gu 是否與所得稅費用對沖（淨效果）；公司調整後 EPS 是否含此等項目；指引 EPS 成長率中之占比；他電業（AEP、SO、XEL、D）有無同型科目 |
| 量綱 | (R_cwip ＋ A_gu − I_adv)×(1−t) ÷ NI（%）；該淨額對 EPS 年增量之貢獻（% of ΔEPS）；預付款餘額 ÷ 費率基（%）；預付款支應 capex ÷ 總 capex |
| 半衰期 | 依合約建設期（年級）；季度可觀測 |

## 3. B 端可觀測載體（只指名）

1. Entergy 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/65984/000006598426000283/etr-20260630.htm （營收變動表、其他收入／利息變動、附註「Amortization of Tax Gross-up on Customer Advances」、資產負債表、現金流量表；子公司 ELL／EML 分列）
2. Entergy 10-K FY25 https://www.sec.gov/Archives/edgar/data/65984/000006598426000174/etr-20251231.htm （大負載合約安全條款段；FY25 其他收入 +65M 墊高攤銷；EML 預付款持有成本 12.4M）
3. Pelican Policy 2026-04-10（Hyperion 擴建 ESA 20 年、約 7.5 GW、「Meta will fund most of the incremental generation, transmission, and interconnection costs」、融資期長於 ESA）https://pelicanpolicy.org/energy/entergys-new-mega-deal/
4. Colorado Sun／HPPR 2026-04-07（Xcel 科羅拉多大負載費率：資料中心付新發電與輸電、最低月費、提前解約費）https://www.hppr.org/hppr-news/2026-04-07/xcel-proposes-new-rate-scale-for-data-centers-to-shield-consumers-from-added-power-costs
5. 未讀：Entergy 2Q26／3Q26 業績稿與電話會（調整後 EPS 是否含此等項目）；LPSC Hyperion 擴建 docket 原文；AEP、SO、XEL、D 10-Q 有無「customer advances for construction」或 CIAC 損益項；具名賣方就預付款收入之品質評論。

缺段（§7-2）：具名第三方對此等項目之量化本輪未見；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 墊高攤銷為稅之對沖項，與所得稅費用相抵，淨利影響近零 | 載體 1 附註結構（待測） | 量級 |
| R2 | 公司已於 MD&A 逐項分列並說明認列原則，賣方可直接剔除；已定價 | 載體 1、2 | 已定價 |
| R3 | 客戶出資降低股東資本與擱淺風險，屬收入品質之提升而非虛高 | 載體 2（10-K 安全條款段）、3 | 方向 |
| R4 | 規模相對 Entergy 淨利有限，且建成後轉為費率基或合約固定費，無斷崖 | 載體 1 | 量級／機制 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) R_cwip、A_gu、I_adv 任一無 ≥ 4 季可對齊序列（Entergy 10-Q／10-K 變動表與附註），或除 Entergy 外無任何他電業有同型科目而 Entergy 亦不足 4 季；或
(2) `[D]` 量級：(R_cwip ＋ A_gu − I_adv) 之稅後淨額 ÷ 淨利 < 3%，或對 EPS 年增量之貢獻 < 15%；或
(3) A_gu 經附註或公司說明確認與所得稅費用全額對沖（R1 成立），且 R_cwip 於合約中明定建成後由等額固定費或費率基報酬接續（R4 成立，無斷崖）；或
(4) 公司調整後 EPS 已剔除此等項目，或具名賣方／評等機構已以剔除口徑量化（已定價）；或
(5) 與 L1-A#3（AFUDC 權益）為同一金額之重述（預付款支應之 CWIP 亦計 AFUDC）而非可分離項；或
(6) 12 個月內無可觀測驅動：無新預付款合約、無建成日、季報該等項目無變化。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：營收「Other electric revenues」內之在建報酬、其他收入之墊高攤銷、利息之持有成本、預付款餘額。2. 可交易工具：電業（不選）。3. 半衰期：合約建設期；季報季度。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L1［A］格加「#4 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0094。`export/LEADS_算力收支.md`：本輪事實之出處未將預付款逐筆歸屬資料中心，不寫。不改 L1-A#1–#3、L1-I#1–#3、L1-P（T-11）、C-A3、N-02 結論。
