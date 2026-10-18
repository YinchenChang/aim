# L6-I#3 生成卡｜雲端與基礎設施服務：誘因（融資可貸性讓價：只有投資級對手方之合約可抵押借款 → 供給方以單價換可貸性）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260928_L6-I_generate_GK.md；archive/drive/USED_20260928_L6-I_test1_GK.md；archive/drive/USED_20260929_L6-I_T_GK.md；archive/work/20261011_L6-I#2_generate_CL.md；work/20261011_L6-I#2_test1_CL.md | EMITS: work/20261018_L6-I#3_generate_CL.md -->
**日期：** 2026-10-18　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 4／6）　**格：** L6-I　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L6-A#3 本日測一，Q-0067 done）。最後測試日最舊＝2026-10-11（L6-I#2、L13-A#2）；依表序取 **L6-I**；非已殺、非刻意排除。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py GPU rental price contract spot H100`，回多筆；相關 1（SRC_DC_012 SemiAnalysis 每 GPU 小時 TCO，2026-05，作測一找原文之線索）；本卡未作證據。
- 比對之舊檔與死因型態，本卡須異型：
  - **L6-I#1**（`archive/drive/USED_20260928_L6-I_generate_GK.md`／test1／T）：逆選擇——最願簽長約者替代選項最少，backlog 品質不隨規模改善。本卡方向相反：誘因來自**供給方之債權人**，供給方主動追逐**高信用**對手方並以單價讓渡換可貸性；問的是單價／毛利，不是對手方違約。
  - **L6-I#2**（`archive/work/20261011_L6-I#2_generate_CL.md`）：賣方代理人 bookings 計酬。不同型（本卡之代理人為公司整體，約束來自貸款合約，非計酬）。
  - **C-A4**（ARCH_dead #4）：續約單價比 `k`。本卡為**首約**單價與即時價之差，且歸因於融資約束，不涉續約。
  - **L13-I／#2**（擔保人權證、recognition agreement）、**L13-A#2**（客戶預付入 OCF）、**L4-I#2**（加速器商回租承諾）：皆融資或對手方結構；本卡為融資約束 → 定價之傳導，載體為 DDTL 條款與合約單價，非擔保／預付／回租。
  - 重疊列為否決 (4)。
- §7-10 領域最近公開：CoreWeave 10-Q（期末 2026-06-30）；Contrary Research「Why 20% of neoclouds won't survive」更新 2026-06-24。下一檢查點＝CoreWeave、Nebius Q3（約 2026-11）。

## 1. 落差一句

誘因：專案型 GPU 雲之債務（DDTL／ABS）以「contributed contracts」之合約現金流為擔保，且限於投資級對手方；可借成數與利率取決於對手方信用而非單價。故供給方之最適選擇為**以首約單價讓渡換取可貸性**（低單價 × 高成數 × 低利率），使「合約 backlog 規模」與「每單位容量之經濟毛利」脫鉤。種子主張：市場以混合毛利率與 backlog 規模外推，未分離 `Δp ≡ p_spot − p_IG-contract` 之讓價；`Δp` 與融資條件可拒絕。本卡不定方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因（債權人約束 → 定價選擇）；非守恆、非會計恆等 |
| 可見端 | CoreWeave 10-Q 2026-06-30 原文：DDTL「collateralized with the assets underlying the contributed contracts and the pledged contractual cash flows, generally from investment grade counterparties」，DDTL 1.0／2.0／2.1／3.0／5.0 有效利率 15%／11%／9%／9%／9%；客戶集中度附註；公開首約總額（Nebius–Microsoft、Nebius–Meta、CoreWeave–OpenAI／Meta）÷ 容量 |
| 指名不可見端 | 合約單價（每 GPU 小時或每 MW）；IG 與非 IG 合約之毛利拆分；可借成數 |
| 對照式（生成用） | 首約隱含單價 `p_c`（合約總額 ÷ 合約 GPU 小時）vs 同期即時／公開價 `p_s`；`Δp/p_s` 與 DDTL 有效利率之下降同向。可拒絕：`Δp` ≈ 0 或與期限溢價（一般利率期限結構）不可分 |
| 表達工具型態（只指名，不選券） | 美股 GPU 雲（CoreWeave、Nebius 等）。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. CoreWeave 10-Q（期末 2026-06-30）https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm （附註 10 Debt；MD&A Debt Financing 段）
2. CoreWeave DDTL 信貸協議（8-K 附件；測一以 `sec.py filings CRWV --form 8-K` 取）——「eligible contract」、對手方評等門檻、借款基數公式。
3. Contrary Research（Claire Burch、Bernie Margulies，更新 2026-06-24）https://research.contrary.com/report/why-20-of-neoclouds-wont-survive-the-ai-boom ——「instead focus on the offtake contracts as collateral」「creditworthy buyers flow to large providers who can finance against their credit cheaply」。
4. 即時價指數：https://www.spheron.network/blog/h100-price-per-hour-2026/ ；https://aimultiple.com/gpu-index （二手，未實讀）。
5. 測一須另取：Nebius 20-F／6-K 之 Microsoft／Meta 合約總額與容量；CoreWeave ≥ 4 季 DDTL 利率與客戶集中度；SemiAnalysis TCO 原文（線索：Tokenomics SRC_DC_012）；具名賣方是否已以「可貸性讓價」建模單價或毛利。**不宣稱已錯價。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 信用分層定價已是公開框架：大供給方以低融資成本服務高信用買方，小供給方高價服務低信用買方 | Contrary Research 2026-06-24（#3） | 落差為共識 |
| R2 | `Δp` 只是期限溢價（長約 vs 即時），與融資約束無關 | 一般期限結構；待原文 | 不可分離 |
| R3 | 讓價由低利率與高成數完全補償，股權報酬不受損（MM 型） | 待原文 | 誘因無淨效果 |
| R4 | 管理層已揭露合約毛利／單價分層 | 待法說原文 | 無資訊增量 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 首約單價 `p_c` 於 ≥ 2 主體不可由申報或公告總額 ÷ 容量推得，或 `p_s` 無可比之同代 GPU 公開序列（可觀測性失敗）。
(2) 具名賣方或研究機構原文已以融資約束／對手方信用解釋首約單價或毛利（R1 共識）。
(3) 信貸協議原文不以對手方評等為借款資格（「generally」僅描述，非條款），使誘因鏈斷開。
(4) 可運作對照只能寫成對手方違約／集中（L6-I#1）、計酬（L6-I#2）、續約單價 `k`（C-A4）、擔保／預付／回租（L13-I、L13-A#2、L4-I#2）。
(5) `Δp` 與期限溢價或交付時點不可分（R2），或管理層原文已揭露分層單價／毛利（R4）。
(6) 只有 ≤ 1 家上市 L6 主體以合約現金流專案融資，使表達只剩單一主體。

複查觸發器（若日後殺）：任一 GPU 雲主體首次分列 IG vs 非 IG 合約之營收或毛利；信貸協議全文揭露對手方評等門檻與成數；公開首約單價序列出現（每 GPU 小時或每 MW）。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：DDTL 附註、客戶集中度、RPO、毛利率／調整後營業利益率、利息費用。
2. 可交易工具：CoreWeave、Nebius 等美股與選擇權。
3. 半衰期：首約期限（約 5–7 年）；融資條件季度變動；`[V]` 不寫。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L6［I］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L6-I#1／#2、L6-A#1–#3、L6-P#1–#3、L13-A／#2、L13-I／#2、L4-I#2、C-A4 結論。
