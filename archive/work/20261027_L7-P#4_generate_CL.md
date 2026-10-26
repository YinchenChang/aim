# L7-P#4 生成卡｜模型層：守恆（KV 快取記憶體占用守恆：長上下文／代理工作負載之 HBM 位元組·秒 vs 按 token 計價）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/work/20261020_L7-P#3_generate_CL.md；archive/work/20261013_L7-P#2_generate_CL.md；export/LEADS_算力收支.md | EMITS: work/20261027_L7-P#4_generate_CL.md -->
**日期：** 2026-10-27（台北；UTC 2026-10-26）　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 0→1／6）　**格：** L7-P　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額配置、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L13-A#4 已測一，Q-0110 done）。非已殺／刻意排除格中，最後測試日最舊＝2026-10-20 一組（L7-P/A/I#3、L10-P/A/I#3、L11-A/I#3、L13-P/I#3、L14-P#3）；同日以 QUEUE 序決勝（沿 L13-A#4 卡之規則），最早＝**L7-P#3**（Q-0070）。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py "KV cache" "long context" "context caching" HBM`，命中 18 筆，全為 SRC_HW HBM 規格與 SRC_PERF_074（vLLM GB200 decode）；與本卡之計價／占用恆等無直接關係，未作載體。
- 比對之舊檔與死因型態，本卡須異型：
  - **L7-P#1**（測一通過｜不進 T）：FLOP/token × J/FLOP＝**每 token 能量下界**（算力綁定）。本卡之約束量為**記憶體占用**（位元組·秒），與 FLOP 無關；長上下文 decode 為記憶體容量／頻寬綁定。
  - **L7-P#2**（部分通過）：訓練資料存量。本卡不論資料。
  - **L7-P#3**（測一不通過，(1)(2)(5)）：容量（GW）→ token → 營收**總量上界**，死因「已以每 MW 營收建模」。本卡不經 GW、不論總營收，物件為**單請求**之計價單位（token）與占用單位（KV 位元組 × 上下文長 × 駐留時間）之錯配，及其隨上下文分布移動之毛利斜率。
  - **L5-I#4**（DRAM 再用誘因）、**L5-P／L5 系列**（儲存守恆）：本卡不論記憶體供給或位元需求，只論模型商計價恆等；HBM／DRAM 需求外溢只記重疊。
  - **L7-A#3**（雲市集分潤）：本卡不論認列。**C-A5**（死 #13：API 單價不可分離／L7 未上市）、**C-P3**（死 #16）：本卡須單價或毛利按上下文分列，可否觀測列為否決 (3)(5)；C-A5 複查觸發器屬 SCOUT-WATCH，不代判。
  - **T-15**：無關，不寫。
- §7-10 領域最近公開：Anthropic 公開 S-1（EDGAR，`export/LEADS_算力收支.md` 2026-10-26 列，`anthropicpbc-sx1.htm`）；Google Gemini API 價目頁（本輪實讀 2026-10-26，無更新日）；Anthropic 1M 上下文 GA 公告 2026-03-13。下一檢查點＝S-1 修正版／首份 10-Q 之毛利與計價揭露；Gemini 3.8 Flash 2027-01-01 調價生效。

## 1. 落差一句

恆等（Little 定律之記憶體占用守恆）：每加速器組 `Σ_i b × L_i × T_i ≤ (M_HBM − W) × Δt`，其中 `b`＝每 token KV 位元組［B／token］、`L`＝請求上下文長［token］、`T`＝駐留時間［s］（≈ 輸出 token 數 `o` ÷ decode 速率）、`M_HBM − W`＝扣權重後可用 HBM。按 token 計價之營收 `p_in·L + p_out·o`；故**輸出營收 ÷ 占用 ∝ p_out ／ (b·L)**——在單價不隨上下文調整時，每位元組·秒之輸出營收與平均上下文長成反比；快取讀取（約 0.1× 輸入價）而保留期不另計費者，保留之位元組·秒無對應營收。
已見數點（本輪實讀）：
- KV 每 token 位元組（公式 `2 × layers × kv_heads × head_dim × bytes`）：Llama-3.1-70B 320 KiB、405B 504 KiB、gpt-oss-120b 72 KiB（滑動窗）；70B 於 128K 上下文每 session 40 GiB（MinIO MemKV 文件）。
- Yao Fu（Edinburgh，arXiv 2405.08944）：Yi-34B 於 2×A100-80G「about 100+ users concurrency of 4K context, but only 5 users of 100K context」（理論峰值）。
- SemiAnalysis（經 2026-05-22 推文彙整，二手）：432k 筆實際 coding-agent 請求「96k-token median input」；另一推文「~50% of requests already exceed 128k tokens」。
- 計價分歧：Anthropic 2026-03-13「無長上下文附加、無乘數」（Opus 4.6 5／25、Sonnet 4.6 3／15 $/MTok，1M 窗）；Google Gemini 3.1 Pro 輸入 $2.00（≤200k）／$4.00（>200k）、輸出 $12／$18、快取儲存「$4.50 / 1,000,000 tokens per hour」；Gemini 3.8 Flash 輸入／輸出 $0.75／$3.75「through December 31, 2026」→ $1.50／$7.50「starting January 1, 2027」，儲存 $0.50→$1.00（ai.google.dev/pricing）。另 Z.AI 中期公告稱 2026 上半年平均 API 售價約 +101%（LEADS 既有列）。
種子主張：以每 token 成本（FLOP／能量）或每 GW 營收衡量模型商單位經濟者，漏掉「上下文分布右移 × 平價計價」對每加速器營收之 1/L 斜率；可由已公開之價目結構差異與上下文分布事前界定方向，量級待測一。本卡不定方向與量級，只立可拒絕之恆等。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（HBM 位元組·秒占用守恆；Little 定律：並發 = 到達率 × 駐留） |
| 量綱 | B／token；token；s；B·s；$／token；$／(GB·s)［D］ |
| 可見端 | 官方價目頁（上下文分層、快取寫／讀／儲存費）；模型組態（layers、kv_heads、head_dim、注意力型態）；上下文長分布（SemiAnalysis、OpenRouter）；公開 S-1／10-Q 毛利與 cost of revenue |
| 指名不可見端 | 閉源前沿模型之 `b`（MLA、滑動窗、KV 量化、卸載至 DRAM／SSD 後之有效值）；實際 `T` 與批次；按上下文分列之毛利 |
| 主張 | 平價長上下文 × 上下文右移 → 每加速器輸出營收下降，除非 `b` 下降同速；可由「`b` 壓縮已抵銷」或「已有具名模型」拒絕 |
| 外部參照物（測一查證） | Google 對 >200k 輸入加倍與按小時儲存計費之定價前例；Gemini 3.8 Flash 2027 調價；Z.AI API 售價 +101%——僅作路徑先例，非因果、非量級 |
| 表達工具型態（只指名，不選券） | 模型實驗室普通股（上市後）；持股方／雲端模型商普通股為間接。不選券 |
| 重疊 | L7-P#1（單位成本底板，算力維）、L7-P#3（容量→營收）、L5-I#4／L5 系列（記憶體需求外溢）、C-A5（單價可分離性）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Google Gemini API 價目頁：https://ai.google.dev/pricing
2. Anthropic 1M 上下文 GA 公告（2026-03-13）：https://claude.com/fr-fr/blog/1m-context-ga ；Anthropic 價目文件 https://docs.claude.com/en/docs/about-claude/pricing（本輪 WebFetch 302 轉 platform.claude.com，權限逾時未讀）
3. Anthropic 公開 S-1（LEADS 既有列；本輪未讀，測一以 sec.py 實讀）：https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm
4. KV 尺寸公式與例：https://docs.min.io/memkv/operate/kv-cache-sizing/
5. Yao Fu, arXiv 2405.08944：https://arxiv.org/html/2405.08944v1
6. SemiAnalysis coding-agent 上下文分布（二手彙整）：https://backlist.sdan.io/d/2026-05-22 ——測一須回 SemiAnalysis 原文
7. 記憶體階層與 NVIDIA ICMS／KV 卸載：https://www.theregister.com/2026/01/28/how_agentic_ai_strains_modern_memory_heirarchies/
8. Gemini 3.8 Flash 2027 調價（二手）：https://www.techplained.com/gemini-3-8-flash

## 4. 最強反方（具名，測一驗）

- **KV 壓縮抵銷**：DeepSeek MLA、滑動窗（gpt-oss-120b 72 KiB vs 70B 稠密 320 KiB）、FP8／FP4 KV、NVIDIA ICMS／Dynamo 與 WEKA、VAST 之 KV 卸載——「reduce GPU memory usage by up to 87 percent」（The Register 轉述 arXiv）。若 `b` 之有效值下降快於 `L̄` 上升，守恆不約束。
- **已定價**：Google 已對 >200k 與儲存分別計價；SemiAnalysis 已公開量測上下文分布並推論「pressure on KV cache management」。若具名賣方已按上下文分布建模每 GPU 營收或毛利，即 R1。
- **輸入主導**：代理請求以輸入為主、快取命中高；若營收主體為輸入 token（`p_in·L`，與占用同比例），1/L 斜率只作用於輸出營收，量級可能不足。

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 公司原文、S-1 或具名賣方／研究機構已按上下文長（或 KV 占用）建模每加速器營收、毛利或定價——已定價（R1）。
(2) 具名一手顯示前沿商用模型之有效 `b`（含壓縮、卸載）自 2025 至測一日之下降倍數 ≥ 同期 `L̄`（或中位輸入）上升倍數——守恆不約束（R2）。
(3) 公開 S-1、10-Q 或任一已上市主體不分列可歸因於上下文分布之毛利、cost of revenue 或單價，且 `[D]` 輸出營收占比 × 1/L 斜率對毛利率之 12 個月影響 < 5 個百分點（本門檻於生成時凍結）——不可觀測或量級不足（R3）。
(4) 可運作對照只能寫成 L7-P#1 能量底板、L7-P#3 容量→營收、L5-I#4／L5 記憶體需求或 C-A5。
(5) 至測一日無已上市主體能分離模型 API 營收與其服務成本（含 S-1 之分部），表達不可行（R4）。
(6) 已見之調價（Gemini 3.8 Flash 2027、Z.AI +101%）經原文歸因為促銷到期、需求或競爭，而具名一手明言與上下文／記憶體成本無關，且無其他模型商出現按上下文或保留時間計價之改動——路徑先例不成立（只削弱，不單獨否決）。

複查觸發器（若日後殺）：任一模型商首次分列長上下文或快取保留之營收／成本；Anthropic 價目文件恢復長上下文乘數或新增快取儲存費；具名一手公布前沿閉源模型 KV 有效位元組。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：S-1／10-Q 之營收拆分（用量／訂閱）、cost of revenue、推論成本敘述、價目變更之風險因素。
2. 可交易工具：模型實驗室普通股（上市後）；雲端模型商（Alphabet）普通股為間接。不選券。
3. 半衰期：Gemini 3.8 Flash 調價 2027-01-01；Anthropic 上市後首份 10-Q。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列（Q-0111）；`query/ARCH_matrix.md` L7［P］標「#4 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L7-P#1–#3、L7-A#1–#3、L7-I#1–#3、L5-I#4、L6-P#3、C-A5、C-P3、C-I1 結論；不寫 T-15。線索輸出（§D）：Gemini 3.1 Pro／3.8 Flash 價目各一列。
