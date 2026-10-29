# L2-I#5 生成卡｜資料中心實體：誘因（MEP 承包商之合約型態選擇——AI 資料中心轉向 GMP／成本加成與 CM 角色，風險由業主承接）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260917_L2-I_generate_GK.md；archive/work/20261007_L2-I#2_generate_CL.md；archive/work/20261015_L2-I#3_generate_CL.md；archive/work/20261023_L2-I#4_generate_CL.md；work/20261029_L2-P#5_test1_CL.md；work/20261029_L2-A#5_test1_CL.md；query/QUEUE.md | EMITS: work/20261029_L2-I#5_generate_CL.md -->
**日期：** 2026-10-29　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1／6）　**格：** L2-I　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L2-A#5 於 2026-10-29 測一）。非「已殺／刻意排除」格中最後測一最舊者為 2026-10-23 批（L2-I#4／L8-A#4／L8-I#4／L9-A#4／L9-I#4／L12-P#4）；同日依 QUEUE 序次（Q-0088 最先）取 **L2-I**；既有生成 4 份 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `data center construction contractor`，命中 15 筆，皆為硬體單價／PUE／模型算力／需求端，與建造合約型態無關 → 實用命中 0。
- 比對（本卡須異型）：
  - **L2-I#1**（許可／併網可撤回 × 損失歸屬錯配）：法定取用權；本卡為私人建造合約之成本超支風險歸屬。
  - **L2-I#2**（開發 JV 之 GP 兼買方 promote）：關係人定價；不涉。
  - **L2-I#3**（設備訂單保位、可取消 backlog）：買方對**設備供應商**之取消選擇權；本卡為**施工承包商**之計價型態（固定價 vs GMP／成本加成），不涉取消。
  - **L2-I#4**（表後發電續約權以電網到位為條件）：期末續約；本卡為施工期內之超支風險分配。
  - **L2-A#1–#5**（每 MW capex、利息資本化、電力轉嫁總額、租期－年限 ρ、直線化租金）：出租方會計；本卡主體為承包商、因果驅動層為**稀缺技工下之合約型態選擇**。L2-A#3 為電力轉嫁總額認列（營運期）；本卡之「轉嫁」為施工期材料／設備／分包成本在 CM／prime 角色下之低加成。
  - **L2-P#1–#5**（櫃密度、功率擺盪、MW 口徑、時程延誤 E＝G−UC）：守恆；不涉合約計價。
  - ARCH_dead C-A3（續約單價）、C-P4（水）：不涉。L3-A#4 生成卡提及之「生產合約定價公式（成本加成？）」屬晶圓代工 NCI，非本層。
- §7-10 領域最近公開：EME 10-Q 3Q26（2026-10-29 申報）；FIX 10-Q 3Q26（2026-10-22 申報）；STRL 10-Q 3Q26（2026-10-29 申報）；EME Q2 2026 電話會（2026-07-30）。下一檢查點＝EME／FIX Q3 2026 電話會逐字稿與 FY2026 10-K（約 2027-02）。

## 1. 落差一句

AI 資料中心 MEP（機電）技工稀缺時，業主（超大規模業者／開發商）為鎖定交期改以 GMP（成本＋固定費，設上限）或成本加成發包、並讓承包商擔任 CM／prime（材料、設備、分包以低加成流過）；承包商之**毛利率**因此被**合約型態組成**拉低、而**風險承擔**同步下降，業主承接超支風險。種子主張：以分部營業利益率讀承包商定價力或執行力者，讀到的部分是合約型態組成（風險移轉）而非價格；反向亦然——固定價占比高之同業，穩定毛利率內含未被分列之超支風險溢價。**方向未定**（GMP 上限實際綁住承包商 → 風險未移轉；或業主側超支已入 capex 指引 → 無落差）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：稀缺要素（技工產能）之租不以單價、而以合約型態（風險歸屬）收取；業主以承擔超支換取交期確定 |
| 已讀事實 | EME 10-Q 3Q26（三、九月）：某營建分部營業利益率 12.1%／11.9% vs 前年 12.9%／12.8%，歸因「a greater percentage of revenues generated from projects for which we are acting as either the construction manager or prime contractor and that carry lower than average gross profit margins due to a higher proportion of materials, equipment, and subcontractor costs, and (b) an increase in the number of guaranteed maximum price and cost-plus contracts, particularly in newer geographies or on projects where design or scope is still evolving」；同分部最大增量來自「network and communications … data center construction projects」。EME Q2 2026 電話會（Motley Fool 逐字稿，2026-07-30）：CEO Guzzi 答 Stifel「probably shift to mechanical 9% to 10%」「the shift is really coming into the AI data centers」「That's prudent both from the end customer, the owner, and … from us」；CFO Nalbandian 將 Mechanical 12.5%（−110 bp）歸因 CM／prime 與 GMP／cost-plus，另答 Oppenheimer 稱「water and wastewater … food processing」「more of mix and project based」（**口徑矛盾**：同季兩說）。FIX 10-Q 3Q26 MD&A：「Given the fixed price nature of much of our project work … significant losses on fixed price project work」；cost-plus／T&M「sometimes subject to a guaranteed maximum cost. These margins are frequently less than fixed-price contract margins because there is less risk of unrecoverable cost overruns」；毛利率 3Q26 24.8%（934,482／3,766,302 千美元）vs 3Q25 24.8%（607,871／2,450,969）`[D]`；「particularly for data centers」。STRL 10-Q 3Q26：E-Infrastructure 以資料中心為驅動；合約型態詞 grep 0 筆。 |
| `[D]` 待算 | 承包商按合約型態之營收占比（固定價／GMP／成本加成）≥ 2 時點；分部毛利率變動拆解：型態組成效果 vs 同型態內價格效果；GMP 上限觸發（超支吸收）之揭露筆數；業主側：資料中心每 MW 建造成本指引上修中可歸因於成本加成超支之份額 |
| 量綱 | 無因次（營收占比、毛利率 pp、組成效果占變動比）；$/MW（業主側） |
| 選擇變數 | 業主：發包型態、上限水準、是否直接採購長交期設備（owner-furnished）；承包商：投標型態、是否承接 CM／prime、GMP 共享節餘條款 |
| 半衰期 | MEP 技工供給追上 AI 資料中心開工量之時長（數年；與學徒培訓、移地擴張同步） |

**不主張方向、不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. EME 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/105634/000010563426000130/eme-20260930.htm （分部利益率歸因句、資料中心增量、RPO 句；分部名稱待測一確認）
2. FIX 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/1035983/000110465926118159/fix-20260930x10q.htm （固定價為主之風險句、cost-plus 毛利較低句、9,399 案平均 $3.8M）
3. STRL 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/874238/000087423826000125/strl-20260930.htm （E-Infrastructure；合約型態待 10-K 讀）
4. EME Q2 2026 電話會（次級逐字稿）https://www.fool.com/earnings/call-transcripts/2026/07/30/emcor-eme-q2-2026-earnings-call-transcript/
5. Earnings Whispers 預覽（2026-10-21；AI 生成、經編輯核）https://finviz.com/news/405649/emcor-must-prove-record-backlog-and-margins-can-outrun-its-sliding-stock ——「Further erosion would raise questions about whether that mix shift is a lasting drag」＝市場以利益率讀之證據（次級）。
6. Capacity 2026-05-08 https://capacityglobal.com/news/datacentre-contractor-concentration-problem-ai-infrastructure-risk/ （框架協議／優先供應商使工作集中；不涉合約型態）
7. 待測一指名讀：EME／FIX FY2025 10-K 合約型態政策與占比（若有）；IESC、LMB（Limbach，「owner direct」）、PRIM、MYRG 10-Q／10-K 同口徑；EME／FIX Q3 2026 電話會逐字稿；業主側（DLR、EQIX、CRWV、APLD）capex 指引上修之歸因句；具名賣方就型態組成之量化。

缺段（§7-2）：任何承包商按合約型態之營收占比數值 0 筆（本輪只讀 3 份 10-Q；FIX 只給定性「much of」）；GMP 上限觸發揭露 0 筆；業主側超支歸因 0 筆；具名賣方量化 0 筆（WebSearch 2 輪）。失敗歸因＝本輪只讀上列；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 公司已於 10-Q 明文分列型態組成效果，市場可讀 | EME 10-Q 3Q26 歸因句（載體 1） | 已揭露 → 無落差 |
| R2 | 型態轉換來自水務／食品加工，非資料中心 | EME CFO 答 Oppenheimer（載體 4） | 驅動變數非 AI |
| R3 | 利益率仍在 12／24 個月均值內，量級不足 | EME CFO（載體 4） | 量級 |
| R4 | GMP 有上限，超支仍由承包商吸收 → 風險未移轉 | FIX「subject to a guaranteed maximum cost」（載體 2） | 機制失效 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後 ≥ 2 家美股上市 MEP／資料中心承包商（EME／FIX／IESC／LMB／PRIM／MYRG／STRL 擇）10-Q／10-K／一手電話會無合約型態組成之原文（占比或歸因句）；或
(2) 可運作對照只能寫成時程延誤（L2-P#5）、可取消訂單（L2-I#3）、電力轉嫁總額（L2-A#3）或每 MW capex 恆等（L2-A#1）——即合約型態對風險歸屬之效果無法分列寫出；或
(3) 具名賣方或公司已公開量化型態組成對利益率之效果並為市場所引用（已定價）；或
(4) `[D]` 量級：型態組成效果 < 分部營業利益率年變動 50%，或 < 0.5 pp；或型態轉換之主來源非資料中心（R2 成立）；或 GMP 合約中超支由承包商吸收之揭露占多數（R4 成立）；或
(5) 12 個月內無可觀測驅動：無 FY2026 10-K 型態揭露、無季度歸因句更新、無業主側 capex 超支歸因。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：分部營業利益率、合約資產／負債、RPO、損失準備（loss contracts）。2. 可交易工具：MEP 承包商（不選）。3. 半衰期：MEP 技工供需平衡。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L2［I］格加「#5 已生成」；`AIM_FUNNEL.md` §3；`query/QUEUE.md` 新增 ANALYST 列 Q-0129。無線索列（本輪事實為建造合約型態，非算力投入／收入數值）。不改 L2-I#1–#4、L2-A#1–#5、L2-P#1–#5、C-A3、C-P4 結論。
