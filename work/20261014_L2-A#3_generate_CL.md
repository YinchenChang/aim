# L2-A#3 生成卡｜資料中心實體：會計恆等（電力轉嫁總額認列——收入＝租金＋公用事業轉嫁，零毛利成分混入營收成長與每 MW 收入）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260913_L2-A_test2_cost-index_GK.md；archive/work/20261007_L2-A#2_generate_CL.md；work/20261007_L2-A#2_test1_CL.md；work/20261014_L2-P#3_test1_CL.md；query/QUEUE.md | EMITS: work/20261014_L2-A#3_generate_CL.md -->
**日期：** 2026-10-14　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain，配額 6／6）　**格：** L2-A　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L2-P#3 本日測一，Q-0044 done）。最後測一最舊者仍為 2026-10-07 批（L2-A#2／L2-I#2／L8-A#2／L8-I#2／L9-A#2）；L2-P 已於本日測過，依 QUEUE 序次取 Q-0002 → **L2-A**，#3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `utility reimbursement pass-through power`，命中 1 筆（ChatGPT 搜尋次數，無關，未用）。
- 比對（本卡須異型）：
  - **L2-A#1**（每 MW 建置成本 × 冷卻佔比；`archive/drive/USED_20260913_L2-A_test2_cost-index_GK.md`）：資本支出分母；本卡為**損益表收入之組成**，不涉建置成本。
  - **L2-A#2**（利息資本化；`work/20261007_L2-A#2_test1_CL.md`）：利息在損益與資產間分配；本卡不涉利息。
  - **L2-P#3**（`work/20261014_L2-P#3_test1_CL.md`）：功率擺盪物理；本卡不涉時域。
  - **L1-I#2**（大負載最低需量／擔保費率）：公用事業對營運商之費率；本卡為營運商對租戶之轉嫁**認列方式**（總額 vs 淨額），不主張費率高低。
  - **L13-A**（入表租賃 ≠ 義務上界）、**L6-A**（已簽未交付 MW）、C-A3／C-A4（折舊年限／續約單價）、C-P4（水）：不涉。
- §7-10 領域最近公開：DLR 10-Q 2Q26（簽署 2026-07-31）；EQIX 10-Q 2Q26。

## 1. 落差一句

會計恆等：`租賃收入 ＝ 基本租金 ＋ 轉嫁收入`；DLR 自述對轉嫁為主要義務人（「primary obligor」），故公用事業費用以**總額**入收入、同額入營業費用，毛利近零。AI 高密度合約每 MW 用電與電價同時上升時，報告營收成長、每 MW 收入、同店收入成長中混入零毛利成分，而 EBITDA 利潤率被機械性稀釋；淨額轉嫁（租戶直購電力）之營運商不受影響。種子主張：以營收或利潤率比較營運商、或以營收成長外推者，讀到的是轉嫁組成之差而非定價力之差。**方向未定**（可高估成長、亦可低估利潤率品質）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：ASC 606 主理人／代理人判斷 → 總額認列；收入與費用同額膨脹 |
| 量綱 | 轉嫁收入／租賃收入（%）；公用事業費用同比（%）；轉嫁對營收成長之貢獻（百分點）；EBITDA 利潤率稀釋（百分點） |
| 選擇變數 | 營運商：租約型態（Turn-Key 計量轉嫁 vs 租戶直購 powered shell）、主理人判斷；租戶：自購電力與否 |
| 可見端 | DLR 10-Q 公用事業費用分列（穩定／非穩定）、轉嫁認列政策句、營收變動歸因句 |
| 指名不可見端 | 轉嫁收入金額本身（DLR 未單列收入側）；EQIX 電力是否內含於單價 |
| 表達工具型態（只指名） | 美股上市資料中心 REIT／營運商。不選券 |

**不主張方向、不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. DLR 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1297996/000110465926089296/dlr-20260630x10q.htm （`sec.py doc --grep` 實讀）：
   - 「Reimbursements are recognized in rental and other services revenue in the condensed consolidated income statements as we are the primary obligor」。
   - 「in some cases we are not entitled to reimbursement of property operating expenses, other than utility expense, and real estate taxes under our leases for Turn-Key Flex® facilities」。
   - 穩定收入增加「primarily due to increases in new leasing and renewals and higher utilities reimbursements across all regions」。
   - Total Utilities 2Q26 396,454 vs 2Q25 339,288（+16.8%）；Rental and other services 1,674,633 vs 1,457,360（千美元）。`[D]` 公用事業費用／租賃收入 ≈ 23.7%；費用增額 57,166 ÷ 租賃收入增額 217,273 ≈ 26%（轉嫁比例未知，為上界）。
   - 非穩定公用事業增加「due to higher utility consumption in a growing portfolio of recently completed development sites」。
2. EQIX 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1101239/000110123926000147/eqix-20260630.htm ：成本端「utility costs including electricity」；「$26 million of higher utilities expense, driven by increases in power costs and higher utility usage」；轉嫁認列方式未見（`pass-through`／`metered` 待測一實讀）。
3. 次級：DLR／EQIX 季度 supplemental（EX-99）是否單列 utility reimbursement revenue；租戶直購電力之超大規模租約（powered shell）比重。

缺段（§7-2）：收入側轉嫁金額未單列；EQIX 轉嫁口徑未讀；具名賣方是否已剔除轉嫁未查。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 轉嫁為行業常識，賣方以 NOI／AFFO／每股 FFO 估值，總額認列不影響此等指標 | DLR 自身以 FFO／AFFO 為主要指標（10-Q FFO 段） | 已定價／無落點 |
| R2 | 超大規模 AI 租約多為租戶直購電力（淨額），AI 增量反而**降低**轉嫁占比 | 待測一以租約型態原文核實 | 方向與機制相反 |
| R3 | 電價變動為外生，與 AI 定價力無關，屬雜訊 | DLR 歸因「higher power pricing … mainly in EMEA and APAC」 | 可分離性 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後 ≥ 2 家美股上市資料中心營運商之 10-Q／10-K 或 supplemental 無法取得 ≥ 4 期轉嫁收入或公用事業費用之同口徑序列，且無轉嫁認列政策（總額／淨額）原文；或
(2) 可運作對照只能寫成每 MW 建置成本（L2-A#1）、利息資本化（L2-A#2）、費率最低需量（L1-I#2）或功率擺盪（L2-P#3）；或
(3) 具名賣方或公司指引已以剔除轉嫁之口徑報告營收成長或利潤率並為市場所引用（已定價）；或
(4) `[D]` 量級：轉嫁對營收成長之貢獻 < 5 個百分點，或對 EBITDA 利潤率稀釋 < 1 個百分點，或 R2 成立（AI 增量以淨額為主）；或
(5) 12 個月內無可觀測驅動：無電價變動、無租約型態轉換揭露、無主理人判斷變更。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：租賃及其他服務收入、公用事業費用、EBITDA。2. 可交易工具：資料中心 REIT／營運商（不選）。3. 半衰期：電價週期與租約期（數年）。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L2［A］格加「#3 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0045。不改 L2-A#1／#2、L2-P#1／#2／#3、L2-I／#2、L1-I#2、C-P4 結論。
