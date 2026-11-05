# L15-A#5 生成卡｜基礎設施軟體與資料：會計恆等（供應商最低承諾地板恆等：消費制 ISV 對雲端與前沿模型供應商之逐約年最低支出為固定地板 F_y，而其對客戶之收入為消費制、隨需部分無最低；差額付款 ≡ max(0, F_y − S_y)，使 AI 推論成本之量風險落在 ISV 端）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md（L15／L14／L6 列）；archive/drive/USED_20261007_L15-A_generate_GK.md；archive/work/20261014_L15-A#2_generate_CL.md；archive/work/20261021_L15-A#3_generate_CL.md；archive/work/20261029_L15-A#4_generate_CL.md；work/20261029_L15-A#4_test1_CL.md | EMITS: work/20261105_L15-A#5_generate_CL.md -->
**日期：** 2026-11-05　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 1→2／6）　**格：** L15-A　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L15-P#5 已測，Q-0165 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-29（L2-P/A/I#5、L15-A#4、L15-I#4 同日）；同日以佇列序取最早者 Q-0125＝**L15-A**。既有 #1–#4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `purchase commitment`、`take-or-pay`、`Snowflake`，0 筆；未用。內部數字（§12）未用。
- 比對（須異型）：
  - **L15-A#1**（`archive/drive/USED_20261007_L15-A_generate_GK.md`）：營收＝使用量×有效單價。本卡不分解營收，標的是**供應端合約地板**。
  - **L15-A#2**（`archive/work/20261014_L15-A#2_generate_CL.md`）：客戶端合約負債（預收浮存）／OCF。本卡為**表外**供應商承諾，不在資產負債表與 OCF。
  - **L15-A#3**（`archive/work/20261021_L15-A#3_generate_CL.md`）：已實現託管成本轉嫁 GM≡1−H/R（流量）。本卡標的是**未實現之承諾存量與差額付款**，GM 本身不是落差；H 高於 F 時本卡恆等不作用。
  - **L15-A#4**（`archive/work/20261029_L15-A#4_generate_CL.md`）：佣金資本化—攤銷時差。不涉資本化。
  - **L14-P#2**（買方容量承諾池互抵／rollover）、**L15-P#2**（客戶雲端承諾之市集抵扣）：皆為 ISV 之**客戶**端承諾；本卡為 ISV 作為**買方**對供應商之承諾，方向相反。
  - **L6-A#4**（capex 現金流分類）、**L13-A#4**（可轉債全成本）：不涉 capex 與融資。
  - 已殺 C-A1（AI COGS 不可分列）：本卡不需分列 AI COGS，只需地板 F_y 與合約年；C-A5／C-P3（L7 未上市）：本卡主體為已上市 ISV。L8-P／L9-P／L11-P 不涉。
- §7-10 領域最近公開：SNOW 10-Q 2Q FY27（期 2026-07-31）；DDOG 10-Q 3Q26（期 2026-09-30，2026-11-04 申報）。下一檢查點＝SNOW 3Q FY27 10-Q（約 2026-12）；AI 供應商合約首年屆滿約 2026-11／12。

## 1. 落差一句

ISV 對供應商之承諾：\(U_t \equiv U_{t-1} + N_t - S_t\)（U＝剩餘最低承諾，N＝新簽／修約，S＝已實現合格支出），每約年差額付款 \(\equiv \max(0, F_y - S_y)\)。SNOW 2Q FY27 10-Q 揭露：與一家「third-party AI service provider」三年約（2025-12 起）修約後首約年加承 $190M，三年最低 $390M，剩餘 $270M，**逐約年**未達即付差額；同期雲端約改為五年 $6.0B、每約年最低 $0.9–1.25B。對客戶端，RPO「excludes … on-demand arrangements as there are no minimum purchase commitments」，且收入「dependent upon customers’ future consumption」。故 AI 推論之量風險不對稱地落在 ISV：客戶 AI 消費低於地板時，差額以成本或損失認列而無對應收入。市場若把模型商合作（公告「$200M partnership」）讀為 AI 收入容量，而非成本地板，則錯讀方向。可拒絕之主張＝F_AI,y 相對 AI 歸因收入或產品營收非可忽略、且首約年實現支出與地板之差可由申報重算，而公司指引與賣方未作此分解。不主張任何主體價值方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等（A）**：\(U_t \equiv U_{t-1}+N_t-S_t\)；差額 \(\Delta_y \equiv \max(0,F_y-S_y)\)；覆蓋比 \(\phi_y \equiv F_y / \text{產品 COGS}_y\)（雲端）、\(\phi^{AI}_y \equiv F^{AI}_y / R^{AI}_y\)（模型商） |
| 量綱 | 美元／約年；\(\phi\) 無因次；差額占產品營收（pp） |
| 選擇者 | ISV（承諾規模換單價折扣）；供應商（最低承諾條款、跨雲抵用）；客戶（隨需 vs 容量約、AI 功能採用） |
| 可見端 | 10-K／10-Q「Other Contractual Commitments」與 MD&A 義務段之逐約年地板、剩餘額、約期；產品 COGS；RPO 與 12 個月認列比；風險因子「pay the difference」句 |
| 指名不可見端 | 合約年內已實現 S_y（多數只揭露剩餘 U）；AI 歸因收入 R^AI（非 GAAP 敘事，須另取）；跨雲抵用條款之實際比例 |
| 表達工具型態（只指名，不選券） | 美股消費制基礎設施軟體商；不選券 |
| 重疊 | L15-A#3（成本流量）；L15-P#2／L14-P#2（承諾池，方向相反） |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Snowflake 10-Q 2Q FY27（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1640147/000164014726000037/snow-20260731.htm ：「amended an existing three-year agreement with a third-party AI service provider that began in December 2025 … committed to spend an additional $ 190 million for the first contract year, increasing the total minimum purchase commitment over the three-year contract term ending November 2028 to $ 390 million. As of July 31, 2026, the total remaining minimum purchase commitment was $ 270 million. Services accessed through certain public cloud providers may be applied toward the Company’s contractual spend commitments … required to pay the difference if it fails to meet the minimum spend for any contract year」；「committed to a cumulative minimum spend of $6.0 billion over a five-year contract term ending March 31, 2031 with minimum spend for each contract year ranging from $900.0 million to $1.25 billion」；風險因子「services provided by these public cloud providers and frontier AI model providers such as Anthropic and OpenAI … If we fail to meet any minimum commitments … pay the difference」；RPO $9.0B、54% 於 12 個月；產品 COGS 2Q $434.4M（上年 $302.3M）。
2. Snowflake 10-K FY26（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm ：非可取消購買承諾表 FY27 $656.3M／FY28 $796.7M／FY29 $660.8M／FY30 $50.0M／其後 $518.0M，合計 $2,681.9M；註 (1) $1.0B（2023-06 至 2028-05，「no minimum purchase commitment during any year」）、註 (2) $530.0M（2025-11 至 2030-10）；FY26 產品 COGS $1,260.3M；RPO「excludes performance obligations from on-demand arrangements as there are no minimum purchase commitments」。
3. 公告（二手／公司稿）：Snowflake–Anthropic $200M（2025-12）https://snowflake.com/en/news/press-releases/snowflake-and-anthropic-announce-200-million-partnership-to-bring-agentic-ai-to-global-enterprises/ ；Snowflake–OpenAI $200M（2026-02）https://www.snowflake.com/en/news/press-releases/snowflake-and-openAI-forge-200-million-partnership-to-bring-enterprise-ready-ai-to-the-worlds-most-trusted-data-platform ——10-Q 之「AI service provider」是否即其一，本輪未對應（未讀公告正文）。
4. 對照 Datadog 10-Q 3Q26（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1561550/000162828026070292/ddog-20260930.htm ：「Purchase commitments for business operations are primarily related to cloud hosting and other software-based services」；九個月「no other material changes … to the Company’s contractual obligations」——未見 AI 模型商地板揭露。

缺段（§7-2）：SNOW AI 歸因收入 R^AI 一手口徑未取；首約年已實現 S^AI 未取（只有剩餘 $270M）；OpenAI 約是否另有地板未取；MDB、ESTC、DDOG 10-K 承諾表未取；具名賣方是否量化地板 vs 消費未取。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 地板遠低於實際支出，非約束（SNOW 產品 COGS 年化 ≈ $1.7B ≥ 雲端地板 $0.9–1.25B） | SNOW 10-Q 2Q FY27 | 量級不足（→(2)） |
| R2 | AI 約可經公有雲抵用（「Services accessed through certain public cloud providers may be applied」），地板可互換，差額實際不會發生 | 同上 | 可替代（→(6)） |
| R3 | 承諾已逐期揭露且公司稱可提前滿足（「may be satisfied earlier」），市場已知 | SNOW 10-K FY26 | 已定價（→(3)） |
| R4 | 本質為託管成本轉嫁（L15-A#3 型） | — | 歸他型（→(4)） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 任一主體之 AI 供應商地板 F^AI_y 與剩餘 U 無法由 ≥ 2 期申報（含本 10-Q 與 3Q FY27 10-Q 或 FY26 10-K）重算，或約年界線不可定；或
(2) `[D]` F^AI_y ÷ 同期產品營收 < 2%，**且**雲端地板 F_y ÷ 同約年產品 COGS 預估 < 70%（兩地板皆非約束；門檻凍結於此）；或
(3) 公司指引原文、電話會議或具名賣方已就最低承諾 vs AI 消費之差額風險作量化或明示（含「已超過地板」或「預期達成」之一手句）；或
(4) 可運作對照只能寫成 L15-A#3（已實現託管成本 GM）、L15-P#2／L14-P#2（客戶端承諾池）或 L15-A#2（合約負債）；或
(5) 12 個月內無檢驗事件（AI 約首約年屆滿約 2026-11／12、SNOW FY27 10-K 約 2027-03 之承諾表與差額付款／損失認列）；或
(6) 跨雲抵用或供應商互換條款原文顯示 AI 地板可由一般雲端支出滿足，使 F^AI 實質併入雲端地板而 R1 成立。

複查觸發器（若日後殺）：任一消費制 ISV 首次認列承諾差額付款或採購承諾損失；AI 模型商最低承諾額首次於 ≥ 2 家 ISV 申報出現；SNOW 揭露 AI 歸因收入之 GAAP 可對帳口徑。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：承諾附註、產品 COGS、差額付款認列科目（COGS 或其他費用）、RPO。2. 可交易工具：基礎設施軟體商普通股（不選）。3. 半衰期：約年 1 年（AI 約 2025-12—2028-11）；雲端約至 2031-03。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0166；`query/ARCH_matrix.md` L15［A］加「#5 已生成」；`AIM_FUNNEL.md` §3 一句與日期行；`export/LEADS_算力收支.md` 2 筆（SNOW AI 服務供應商最低承諾、雲端五年最低承諾）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L15-A#1–#4、L15-P#1–#5、L15-I#1–#4、L14-P#2、L15-P#2、L6-A#4；不碰 L1-P；不寫 T。
