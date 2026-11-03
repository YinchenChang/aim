# L7-I#5 生成卡｜模型層：誘因（自我預先承諾之能力門檻（RSP）→ 能力進展最快處觸發延後／限縮之內生減速器）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；AIM_FUNNEL.md；archive/drive/USED_20260930_L7-I_generate_GK.md；archive/work/20261013_L7-I#2_generate_CL.md；archive/work/20261020_L7-I#3_generate_CL.md；archive/work/20261027_L7-I#4_generate_CL.md；work/20261027_L7-I#4_test1_CL.md | EMITS: work/20261103_L7-I#5_generate_CL.md -->
**日期：** 2026-11-03　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1→2／6）　**格：** L7-I　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L13-A#5 本日測一，Q-0153 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-27（L7-I#4、L10-P／A／I#4、L11-A#4）；依表序取 **L7-I**。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py AGI "revenue share" Microsoft OpenAI`（初選題：OpenAI–Microsoft AGI 條款），相關命中 0；初選題因 2026-04-27 合約改訂（分潤付至 2030「independent of OpenAI's technology progress」，PYMNTS 2026-04-27 實讀）已失去 AGI 觸發，放棄。改題後未再查。內部數字（§12）未取用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L7-I#1**（不通過）：評測取用權合約性。本卡不論評測取用。
  - **L7-I#2**（部分通過）：人才外部選擇權 × SBC。不論人才。
  - **L7-I#3**（部分通過）：通路衝突／客戶換供應；其 §0 曾初探「治理（LTBT／超級表決權）」並放棄（已廣泛討論）。**本卡不以 LTBT 選董權、雙層股權或 PBC 身分本身為落差**；只論**事前登記之能力門檻（RSP）被觸及時對開發／發布時程之約束**——一個以能力量測為輸入、以延後／限縮為輸出之規則。
  - **L7-I#4**（部分通過；(6) 觸發）：照付不議承諾 → 降價填充。本卡不論承諾容量或定價；兩卡可同時成立（承諾付款不因延後而停）但落差不同。
  - **L7-A#3／#4／#5、L7-P#1–#5**：會計口徑與物理守恆；本卡不以分潤、分攤、租賃利息、KV／MoE 吞吐為落差。
  - **L12（監理與法制）各卡**：本卡**不以政府出口管制**（S-1/A：2026-06 商務部對 Fable 5／Mythos 5 之全球出口限制）為機制；政府限制只作對照（可分離性見否決 (5)）。
  - **C-I1／C-A5／C-P3**（死 #10／#13／#16）：估值歸因權重／API 單價不可分離／權重支出非科目。C-A5 複查觸發器「任一前沿 API 商 IPO」：S-1/A 已申報、未掛牌；本卡不代判。
- §7-10 領域最近公開：Anthropic S-1/A 第 1 號修正（2026-11-02，acc 0001628280-26-068676，sec.py 全文 1,592,879 字實讀）；Johnsen（2026-11-03）、Soon（2026-11-03）、Thakker（2026-11-02）評論。下一檢查點＝RSP 對 AI R&D 門檻之指定報告、掛牌後首份 10-Q。

## 1. 落差一句

發行人以事前公開之規則（Responsible Scaling Policy）把「能力門檻被觸及」綁定為「加強措施（延後、限縮、人類核可）」之輸入；S-1/A 自述以內部估計與對未來模型之預期「may imminently meet our Responsible Scaling Policy's definition of 'dramatically accelerated progress attributable to AI'」，且已有實例（Mythos 2026-04 只以 Project Glasswing 門控預覽；新前沿 base model 預訓練延後逾一個月）。誘因結構：營收階躍來自最高能力層（S-1/A「growth also depends on how quickly new capabilities reach customers」），而規則恰在能力進展最快時收緊 → 營收對能力之彈性在門檻處被截斷，截斷時點與長度由非股東目標之內部程序決定。種子主張：市場（IPO 定價、具名估值模型）以能力→營收外推，未以門檻觸發機率 × 延後長度建模（Johnsen 2026-11-03 自述「a timing risk that no revenue model captures」，但其模型亦未計入）。本卡不定方向與量級，只立可拒絕之誘因鏈。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因（自我預先承諾／內生減速器：能力量測 → 規則觸發 → 發布或開發延後；觸發機率隨能力進展上升） |
| 量綱 | `[D]` ℓ＝同一模型類別首次門控可得日 → 一般可得日之天數；g_q＝季營收環比；觸發事件計數 n_RSP（S-1/A 與 RSP 報告揭露之延後／限縮次數）；門控層營收占比 s_gate（若揭露） |
| 可見端 | S-1/A 風險因素與「Our Approach to Safety」段落；RSP 現行版文本與能力報告；模型發布日（Mythos Preview 2026-04、Fable 5 GA／Mythos 5 2026-06、Mythos 5.1／Fable 5.1 2026-09）；季營收 |
| 指名不可見端 | 內部能力估計；延後之機會成本；門控層營收分列（S-1/A grep「by model class」0 筆） |
| 主張 | 門檻觸及（指定報告發布）後之季度，前沿層發布延後或限縮，ℓ 拉長，營收環比較前期減速且發行人歸因於安全措施；可由「RSP 觸及門檻不附約束性措施」「同業同規則且含競爭者豁免」「歷史 ℓ 短且無營收痕跡」或「已被具名建模」拒絕 |
| 外部參照物（測一查證） | 自我約束規則之商業代價前例（例：醫藥 FDA REMS 限縮通路、核電自願停機、交易所熔斷）；測一取具名一手案例 |
| 表達工具型態（只指名，不選券） | 模型實驗室普通股（上市後）；不選券 |
| 重疊 | L7-I#3（同 S-1、治理初探）、L7-I#4（同主體、承諾不停付）、L12（政府限制）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. A1 Anthropic S-1/A 第 1 號修正（2026-11-02；sec.py 實讀）https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm ——「our internal estimates and our expectations regarding future models, rather than our current models, indicate that we may imminently meet our Responsible Scaling Policy's definition of 'dramatically accelerated progress attributable to AI.' We have not designated any of our current models as exceeding this threshold」；「we have in the past not identified, and may in the future not identify, a significant acceleration in our rate of development until after it has occurred」；「recently chose to delay pre-training a new frontier base model for more than a month to allow time to further enhance our security measures」；「considering additional measures, including updates to our Responsible Scaling Policy, to require human review and approval of certain decisions in our research and development processes」；「we have in the past delayed the release of new models … such as with Mythos through Project Glasswing, which may have had a negative impact on our short-term revenue」；「we do not release every model we develop for general use」；Fable「runs with our production safeguards, which block or limit performance on certain sensitive topics, including by routing requests to a less capable Claude model」；「Over 90% of the contributions to our codebase in September 2026 were written by Claude」；Q3 營收 YoY +1,127%、算力費用 +382%；Q3 交付短期承諾算力 5.0B。grep「keep humans in control」「pause a stage」0 筆（評論所引字句待測一於原文定位）。
2. A2 Johnsen〈Anthropic Q3 Update〉（2026-11-03，作者自述由 AI 起草）https://artificialdiligence.substack.com/p/anthropic-q3-update ——「A company that may soon hit a self-imposed brake … carries a timing risk that no revenue model captures」；其機率加權模型未計門檻。
3. A3 Soon〈The Day Governance Became a Balance Sheet〉（2026-11-03）https://genesishumanexperience.com/2026/11/03/the-day-governance-became-a-balance-sheet/ ——停機成本「borne mainly through the share price」；暫停情境標「illustrative, not a forecast」；轉述 WSJ：RSP v3.0「dropped the commitment to pause if a competitor has released a comparable model」（二手）。
4. A4 Thakker（explainx，2026-11-02）https://explainx.ai/blog/anthropic-s-1-amendment-dramatically-accelerated-progress-rsp-threshold-imminently-claimed-vs-verified-2026 ——作者未讀原文；轉述 RSP v3.1「remains free to pause development in any circumstance it deems appropriate, even if the RSP does not require it」與「affirmative case」要求（待原文）。
5. 指名未讀：FourWeekMBA（WebFetch client_error）https://fourweekmba.com/ai-anthropic-filing-it-may-imminently-hit-an-ai-r-d-threshold/ ；cellcog https://cellcog.ai/blog/anthropic-s1a-ai-acceleration/ ；Anthropic RSP 現行版本頁（anthropic.com）。
6. 測一須另取：RSP 現行版原文（AI R&D 門檻之定義與觸及後義務、競爭者條款）；OpenAI Preparedness Framework／Google Frontier Safety Framework 同類門檻與義務；具名賣方／承銷研究是否以門檻觸發建模；Mythos→Fable GA 之 ℓ 與 Q2 營收環比；S-1/A 是否有門控層營收或 Glasswing 收費。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 安全措施提升信任、為採購決定性條件，門控反增營收（S-1/A「rigorous safeguards … decisive criteria when selecting an AI partner」） | A1 | 方向反轉，非截斷 |
| R2 | RSP 觸及門檻只要求報告／affirmative case，無約束性延後；發行人「free to」自由裁量 | A4、A1 | 非預先承諾 |
| R3 | 門控只改發布型態（Fable GA＋路由），能力仍以 GA 版變現；Q2→Q3 營收環比 +47% 未見痕跡 | A1、A2、A3 | 無可觀測營收效果 |
| R4 | 同業同規則（或含競爭者豁免），誘因為產業層，非發行人特有 | A3 | 無相對錯價 |
| R5 | L7 未掛牌 | `work/20261027_L7-I#4_test1_CL.md` (6) | 表達失敗（C-A5 型） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 具名賣方／研究機構已以「RSP 門檻觸發機率 × 延後長度」建模實驗室營收、估值或 IPO 定價——已定價。（僅定性提及「timing risk」不算建模。）
(2) RSP 現行版原文顯示觸及 AI R&D 門檻之義務不含任何對開發或發布之約束（只報告／論證），或明文含競爭者已發布可比模型即放寬之條款——非預先承諾（R2、R4）。
(3) `[D]` 歷史門控痕跡：ℓ（Mythos Preview 2026-04 → Fable 5 GA 2026-06）≤ 90 日，且門控所在季（2026Q2）營收環比不低於前一季——門控無可觀測營收效果（R3）。門檻：ℓ ≤ 90 日且 g_Q2 ≥ g_Q1 即觸發，凍結於此。
(4) 唯一可觀測之門控後果為政府出口管制所致停用（L12 範圍）或與之不可分離——型態落入 L12。
(5) 可運作對照只能寫成 L7-I#1–#4、L12 各卡、C-I1 或 C-A5。
(6) 至測一日 Anthropic（或其他有約束性能力門檻之實驗室）未掛牌，且無已上市主體能分離門檻效果——表達不可行（R5）。

複查觸發器（若日後殺）：RSP 能力報告指定任一模型超過 AI R&D 門檻；發行人於申報將營收減速歸因於安全延後；RSP 改版新增約束性人類核可；具名賣方發布門檻觸發模型；Anthropic 掛牌。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：季營收、MD&A 增長歸因段、風險因素中延後實例清單、RSP 報告日期。
2. 可交易工具：模型實驗室普通股（上市後）。不選券。
3. 半衰期：S-1/A → 掛牌 → RSP 指定報告 → 首份 10-Q。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` Q-0154；`query/ARCH_matrix.md` L7［I］標「#5 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 1 列（Q3 短期承諾算力 5.0B）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L7-I#1–#4、L7-A#1–#5、L7-P#1–#5、L12 各卡、C-A5、C-P3、C-I1 結論；不寫 T-15。
