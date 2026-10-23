# L2-I#4 生成卡｜資料中心實體：誘因（併網排隊下之速度溢價——表後專屬發電之買方續約權以電網到位為條件）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260917_L2-I_generate_GK.md；archive/work/20261007_L2-I#2_generate_CL.md；archive/work/20261015_L2-I#3_generate_CL.md；work/20261015_L2-I#3_test1_CL.md；work/20261021_L2-A#4_test1_CL.md；work/20261008_L1-A#2_test1_CL.md；work/20261009_L1-I#2_test1_CL.md；query/QUEUE.md | EMITS: work/20261023_L2-I#4_generate_CL.md -->
**日期：** 2026-10-23　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 2／6）　**格：** L2-I　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L15-I#3 於 2026-10-22 測一）。非「已殺／刻意排除」格中最後測一最舊者為 2026-10-15 批（L2-I#3／L8-A#3／L8-I#3／L9-A#3／L9-I#3／L12-P#3）；同日依 QUEUE 序次（Q-0046 最先）取 **L2-I**；既有生成 3 份 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `bridge power behind-the-meter onsite`，命中 3 筆，皆為需求端 OpenAI 支出／搜尋量，與本格無關 → 實用命中 0。
- 比對（本卡須異型）：
  - **L2-I#1**（許可／併網可撤回 × 損失歸屬錯配）：該卡是取用權被**撤回**；本卡是電網接入**到位**後，買方對專屬發電之需求消失——方向相反之同一變數。
  - **L2-I#2**（開發 JV 之 GP 兼買方 promote）：關係人定價；不涉。
  - **L2-I#3**（`work/20261015_L2-I#3_test1_CL.md`；設備訂單保位選擇權、可取消 backlog）：該卡為交貨前取消權；本卡為已投產資產之**期末續約權**，取消代價不存在（主約期滿自然到期）。
  - **L2-A#4**（`work/20261021_L2-A#4_test1_CL.md`；AI 出租方租期－耐用年限之 ρ）：該卡為會計恆等（折舊 vs 租期）；本卡之因果驅動層為**買方續約決策 ＝ f(電網接入時點, 表後 vs 電網單價)**，殘值由外生之電網建設決定，非由折舊政策決定。
  - **L1-I#2**（受管電業大負載成本轉嫁其他費率類別）：損失落在費率基；本卡之資產在電網外、損失落在表後發電商（及其 JV 投資人）。
  - **L1-A#2**（Bloom 堆更換認列時點）：會計時點；不涉。
  - ARCH_dead C-A3（續約單價）：該死因為雲 GPU 續約單價；本卡為發電容量，續約與否由電網替代品決定。C-P4（水）不涉。
- §7-10 領域最近公開：WMB 10-Q 2Q26（2026-08-03 申報）；WMB Q2 2026 電話會（2026-07 底至 08 初）；SEI 10-Q 2Q26；BE 10-Q 3Q26（2026-10-22 申報）；BNEF 2026-07-29。下一檢查點＝WMB 3Q26 10-Q（約 2026-11 初）。

## 1. 落差一句

大負載併網排隊長於資料中心建設週期時，買方（超大規模業者）願為「速度」付溢價：向中游／發電商簽專屬表後（behind-the-meter）燃氣發電 PPA，主約 10–12.5 年、**續約選擇權在買方**。買方之續約意願＝電網到位後表後單價相對電網單價之函數；電網接入一旦到位，速度溢價歸零，續約權成為買方之免費選擇權。發電資產經濟年限長於主約，期末殘值由**電網建設進度**（外生、可觀測）決定，風險落在資產持有人。種子主張：以專案報酬或已簽約 EBITDA 外推者，若對主約後現金流套用管線型永續倍數，讀到的部分是**排隊期之速度租**而非永續需求。**方向未定**（電網持續落後、或表後轉為電網支援／混合資產、或買方主動延長 → 落差收窄）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：買方以短於資產年限之主約＋單方續約權購買「時間」；續約決策以電網替代品為條件 |
| 已讀事實 | WMB 10-Q 2Q26 分部描述：「power innovation projects under development that will deliver speed-to-market solutions in power grid-constrained markets」。Socrates：「expected 556 MW of capacity. Socrates South was placed into service in late July 2026 … supported by a 10‑year, primarily fixed‑price power purchase agreement, with an option for the customer to extend the term of the agreement」。另四案：「backed by primarily fixed-price power purchase agreements, with options for the customer to extend」；Apollo（OH）12.5 年／490 MW、Aquila（UT）12.5 年／520 MW、Socrates the Younger（OH）10 年／340 MW、Neo（OH）12.5 年／682 MW。長交期設備「backed by reimbursement from the customer if the equipment order is canceled」。2026-07 出售五案 49% 予投資人換 5.34B 承諾資本。CFO（Q2 2026 電話會）以「total cash flow Williams will see from these five projects」比投入資本、僅計主約期；JV 買回權 2033 起。CEO：「you will continue to see contract terms extend in duration」；「hybrid projects that would … support grid expansion」。SEI 10-Q 2Q26 風險因子：「increased grid capacity that could reduce the demand for our products and services」；Stateline VIE「off-grid power generation pursuant to a long-term equipment lease arrangement」。BNEF 2026-07-29：表後燃氣「often seen as a temporary bridge」，開發商在評估「once permanent grid connections become available」後之角色。Cleanview（次級）：Socrates 兩廠「Neither … will be connected to the electric grid」，並推測期滿後 Meta 將併網（推測，非一手）。 |
| `[D]` 待算 | 主約期 ÷ 資產經濟（折舊）年限；主約期內累計現金流 ÷ 投入資本（是否 ≥ 1，即期內回收）；表後容量占供給方分部 EBITDA 比；該站址公用事業併網預定日 vs 主約到期日之差 |
| 量綱 | 年（主約、年限、併網時點差）；無因次（期內回收倍數、殘值比、分部占比）；$/MWh（表後 vs 電網單價） |
| 選擇變數 | 買方：主約長度、續約與否、併網申請時點；供給方：主約定價（是否期內回收）、續約權定價、資產可遷移性（模組化燃機 vs 固定電廠） |
| 半衰期 | 該區大負載併網排隊消化（數年；與 PJM／AEP Ohio 大負載程序同步） |

**不主張方向、不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. WMB 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/107263/000010726326000026/wmb-20260630.htm （分部描述、Socrates 與四案主約年限、續約權、JV、取消補償）
2. WMB Q2 2026 電話會（次級彙編）https://earningswhispers.com/transcript/WMB/Q22026 ——主約期現金流／投入資本句、JV 2033 買回、合約延長句。
3. SEI 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1697500/000162828026054349/sei-20260630.htm （電網容量風險句、Stateline 租約；租期與終止補償待測一讀）
4. BE 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/1664703/000162828026066931/be-20260930.htm （本輪以「bridge」「grid connection」grep 0 筆；需以他詞複核資料中心 PPA／租約期）
5. BNEF 2026-07-29 https://about.bnef.com/insights/data-centers/gas-is-letting-data-centers-grow-beyond-the-grid/ （「temporary bridge」框架）
6. Cleanview Meta New Albany https://cleanview.co/reports/behind-the-meter-data-centers/full-report/meta-new-albany （站址不併網；OPSB 核准日；次級）
7. 待測一指名讀：AEP Ohio／PUCO 大負載併網排程（New Albany 站址）；WMB 10-K FY2025 物業廠房耐用年限附註；其他表後供給方（如 VST、GEV 航改機租賃、CAT 發電分部）之資料中心合約年限。

缺段（§7-2）：資產經濟年限 0 筆（本輪未讀 10-K 附註）；主約期內回收倍數未揭露（CFO 只給相對改善）；站址併網預定日 0 筆；具名賣方就主約後殘值之量化 0 筆（WebSearch 1 輪，命中為 Simply Wall St／Webull 敘事，未讀）。失敗歸因＝本輪只讀上列；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 定價已在主約期內回收資本，期末殘值為紅利 | WMB CFO：報酬以主約期現金流計（載體 2） | 殘值風險不入估值 → 無落差 |
| R2 | 合約年限持續延長、轉為核心基礎設施 | WMB CEO 句（載體 2） | 續約權價值轉向供給方 |
| R3 | 站址設計為永不併網（off-grid），電網替代品不存在 | Cleanview（載體 6）；SEI「off-grid」 | 驅動變數失效 |
| R4 | 電網排隊與燃機交期皆 > 主約期，買方期滿仍無替代 | BNEF 194 GW 2035 需求預測（載體 5） | 落差只是時點 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後 ≥ 2 家美股上市表後供給方（WMB／SEI／BE 或他者）10-Q／10-K 無主約年限、續約權歸屬或終止補償之原文；或
(2) 可運作對照只能寫成租期－年限之折舊恆等（L2-A#4）、交貨前取消權（L2-I#3）、費率基轉嫁（L1-I#2）或許可撤回（L2-I#1）——即續約決策無法以電網替代品為條件寫出；或
(3) 具名賣方／評等機構／公司已公開量化主約後殘值或以主約期內回收定價並為市場所引用（已定價）；或
(4) `[D]` 量級：主約期 ≥ 資產經濟年限 80%，或主約期內累計現金流 ÷ 投入資本 ≥ 1 有一手揭露，或表後容量占供給方分部 EBITDA < 10%；或該等站址於主約期內無任何公用事業併網路徑（R3／R4 成立）；或
(5) 12 個月內無可觀測驅動：無新簽表後 PPA 年限揭露、無大負載併網程序裁定、無 JV／續約權條款變更。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：分部 EBITDA、PP&E 耐用年限、非控制權益（JV）。2. 可交易工具：表後供給方（不選）。3. 半衰期：區域大負載併網排隊消化。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L2［I］格加「#4 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0088、本卡生成無佇列列可消化（SCOUT-GEN 配額）。不改 L2-I#1–#3、L2-A#1–#4、L2-P#1–#4、L1-I#2、L1-A#2、C-A3、C-P4 結論。
