# L9-A#4 生成卡｜受規管 HITL：會計恆等（理賠自動化下之未分配理賠費用準備——paid-to-paid 比率沿用歷史人工理賠成本 vs 「否決須由合格人員決定」之監理底線）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260921_L9-A_generate_GK.md；archive/drive/USED_20260922_L9-A_test1_GK.md；archive/work/20261007_L9-A#2_generate_CL.md；work/20261007_L9-A#2_test1_CL.md；archive/work/20261015_L9-A#3_generate_CL.md；work/20261015_L9-A#3_test1_CL.md | EMITS: work/20261023_L9-A#4_generate_CL.md -->
**日期：** 2026-10-23　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 5／6）　**格：** L9-A　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L8-I#4 本日測一不通過）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-15 三格（L9-A#3、L9-I#3、L12-P#3）；依佇列序取最早者 L9-A（Q-0049）；既有生成 3 份 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `claims automation`／`loss adjustment`／`insurance`，命中 0 筆；未使用。內部數字（§12）未取用。
- 比對（本卡須異型）：
  - **L9-A#1**（`archive/drive/USED_20260921_L9-A_generate_GK.md`；測一 `archive/drive/USED_20260922_L9-A_test1_GK.md`）：SaaS 每席次交付成本；死於席次與成本不同表。本卡不涉席次、不涉 AI COGS。
  - **L9-A#2**（`work/20261007_L9-A#2_test1_CL.md`）：Claritev 節省分成收入 vs IDR 回吐；死於收入不分列。本卡在**負債側**（準備金估計），非收入認列。
  - **L9-A#3**（`work/20261015_L9-A#3_test1_CL.md`）：MA 風險調整變動對價；死於診斷來源不分列、量級 < 1%。本卡之分解變數（DCC／A&O，即 ALAE 與 ULAE）在法定報表 Schedule P 為**強制分欄**，非公司自願揭露。
  - C-A1（#6，AI COGS 不可分列）、C-I5（#18）、L9-P（#1，核可率／HITL 工時）：不涉；本卡不以 HITL 工時為量，而以準備金估計方法之輸入為量。L9-I 系屬誘因格，不比。
- §7-10 領域最近公開：LMND 10-Q 2Q26（2026-08-04）；FL HB 527（2026 會期 House 108-0 通過、2026-03-13 Senate Rules 未審而死）；AZ HB 2175（2026-07-01 生效，健康險否決須醫療主任親簽）；NAIC AI Model Bulletin（2023-12，> 24 州採用）；actuary.info 2026-08（LMND LAE 5%）。下一檢查點＝各家 3Q26 10-Q（約 2026-11）、FY26 法定年報 Schedule P（2027-03-01）、FL 2027 會期。

## 1. 落差一句

產險之理賠費用準備分兩段：ALAE（DCC，逐案法律／鑑定費）與 ULAE（A&O，理賠部門自身之人事與營運成本，不歸屬逐案）。ULAE 準備普遍以 paid-to-paid 法估計：`ULAE 準備 ≈ (歷史已付 ULAE ÷ 歷史已付損失) × (c × 個案準備 + IBNR)`。若 AI 理賠（如 LMND「roughly 55% of our claims were automated」、無人工之首報與結案）壓低每件理賠之人工成本，則：(a) 以歷史比率沿用之 ULAE 準備對新事故年**系統性高估**，未來以有利前期發展釋放；或 (b) 反向——監理把「否決／減額須由合格人員決定」立為底線（FL HB 527 已一院通過、AZ 已生效於健康險、NAIC 公告要求人為監督），使複雜件（否決、傷害、第三人）之人工成本無法壓縮，自動化只吃掉易件 → 剩餘未決件之單件 ULAE **上升**，歷史比率**低估**。恆等式本身為真；讀者把當期 LAE 比率下降讀成永久經營成果時，部分讀到的是 (i) 易件先結之組合效果、(ii) ULAE 估計比率之滯後。**方向未定**：(a) 與 (b) 何者主導取決於監理底線是否落地與未決件組合。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：LAE 準備＝DCC 準備＋A&O 準備；A&O 準備＝比率 × 加權未決損失；當期 LAE 比率＝(已付＋Δ準備) ÷ 已賺保費 |
| 已讀事實 | LMND 10-K FY25（2026-02-25）：AI Jim「will take the first notice of loss … without human intervention (and with zero claims overhead, known as loss adjustment expense, or “LAE”). As of December 31, 2025, roughly 55% of our claims were automated」；「AI Jim triages and assigns claims he is not authorized to settle … to human claims experts」；「unallocated loss adjustment」0 筆。LMND 10-Q 2Q26：淨未決損失及 LAE 期末 190.9（百萬美元）；1H26 前期發展（16.4）有利；ALAE／ULAE 不分列。actuary.info（2026-08）：LMND 2Q26 LAE 比率 5%（自報）、車險 7%，未拆 ALAE／ULAE；有利發展來自自動化過半前之事故期。FL HB 527 摘要：「prohibits use of artificial intelligence or machine learning systems as sole basis」否決或減額；「decisions to deny claim … be made by qualified human professionals」。Enlyte：AZ HB 2175 2026-07-01 生效；NAIC 公告 > 24 州。ROOT 10-Q 2Q26：「loss adjustment expense ratio」「unallocated」0 筆。 |
| 未證之連結 | 法定報表 Schedule P Part 1 之 A&O 已付與準備按事故年序列（是否隨自動化率下降）；公司是否改變 ULAE 估計比率；監理底線對否決件人工成本之量 |
| 量綱 | A&O 已付 ÷ 損失已付（無因次，按曆年）；A&O 準備 ÷ 未決損失（無因次）；A&O 前期發展 ÷ 已賺保費（%）；自動化結案占比（%） |
| 選擇變數 | 公司：自動化範圍、ULAE 比率假設；監理：人審底線之範圍（否決／減額／全部）；精算師：方法選擇（paid-to-paid、Kittel、按件計） |
| 半衰期 | ULAE 準備對應未決件，短尾險（屋主／租屋）≤ 1–2 年釋放；車險傷害件較長；法定年報每年 03-01 |

## 3. B 端可觀測載體（只指名）

1. LMND 10-K FY25 https://www.sec.gov/Archives/edgar/data/1691421/000169142126000016/lmnd-20251231.htm ；10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1691421/000169142126000055/lmnd-20260630.htm
2. ROOT 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1788882/000178888226000061/root-20260630.htm ；HIPO 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1828105/000182810526000043/hippo-20260630.htm
3. FL HB 527（2026）https://www.flsenate.gov/Session/Bill/2026/527 ；分析 https://www.flsenate.gov/Session/Bill/2026/527/Analyses/h0527a.IBS.PDF
4. Enlyte 2026 https://www.enlyte.com/insights/article/compliance/ai-claims-handling-compliance-2026
5. actuary.info 2026-08 https://actuary.info/insights/lemonade-lae-ratio-ai-claims-loss-reserving-2026
6. 未讀：各子公司 NAIC 法定年報 Schedule P Part 1（A&O 欄）及精算意見書（SAO）；大型已上市產險（PGR、ALL、TRV）10-K 之 LAE 分列與自動化揭露；CAS 就 ULAE 方法於自動化下之論文。

缺段（§7-2）：A&O 事故年序列、ULAE 比率假設之變更；本輪只讀上列；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | ULAE 準備量級小（LAE 總比率 5% 且多為當期已付），前期釋放 ÷ 保費遠 < 1% | 載體 1、5 | 量級小 |
| R2 | 公司不拆 ALAE／ULAE，10-Q 層不可分列（同 L9-A#2／#3 死因） | 載體 1、2；載體 5「does not split」 | 表達層 |
| R3 | FL HB 527 已死；監理底線未落地於產險，(b) 無驅動 | 載體 3 | 驅動缺 |
| R4 | 有利發展來自自動化過半前之事故期，與本機制無關 | 載體 5 | 歸因錯置 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) ≥ 2 家上市 AI 理賠主體之 10-K／10-Q／法定 Schedule P（或可取之摘要）皆無法分列 A&O（ULAE）已付或準備，亦無 ULAE 估計比率或方法之揭露；或
(2) 可運作對照只能寫成 L9-A#2／#3（收入或變動對價不分列）或 L9-P（HITL 工時／核可率）而無準備金分欄結構；或
(3) `[D]` 量級：A&O 準備 ÷ 已賺保費，或可得最佳之 A&O 前期發展 ÷ 已賺保費 < 1%；或
(4) 12 個月內無可觀測驅動：無州法／監理要求於產險落地人審底線、且無公司揭露自動化率或 ULAE 假設變更；或
(5) 公司或具名賣方／評等機構（AM Best 等）已量化 ULAE 準備對自動化之敏感度（已定價）。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：未決損失及 LAE、前期發展、法定 Schedule P A&O 欄。2. 可交易工具：上市產險（不選）。3. 半衰期：短尾險 1–2 年；法定年報 03-01。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L9［A］格加「#4 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0091。不改 L9-A#1–#3、L9-I／#2／#3、L9-P、C-A1、C-I5 結論。
