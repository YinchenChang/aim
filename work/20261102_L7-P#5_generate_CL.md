# L7-P#5 生成卡｜模型層：守恆（MoE 權重駐留守恆：每個 decode 步須讀取之權重位元組 ∝ 被觸及之專家數，而非活躍參數；每 token 權重成本 ＝ 觸及位元組 ÷ 批量 → 稀疏模型之「每 token 成本 ∝ 活躍參數」只在高並發成立，服務端存在最小有效規模）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；AIM_FUNNEL.md；archive/drive/USED_20260930_L7-P_generate_GK.md；archive/work/20261013_L7-P#2_generate_CL.md；archive/work/20261020_L7-P#3_generate_CL.md；archive/work/20261027_L7-P#4_generate_CL.md；archive/work/20261102_L6-P#5_generate_CL.md | EMITS: work/20261102_L7-P#5_generate_CL.md -->
**日期：** 2026-11-02　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 4→5／6）　**格：** L7-P　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額配置、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L6-I#5 本日已測一，Q-0150 done）。非已殺／刻意排除格中，最後測試日最舊＝2026-10-27 一組（L7-P/A/I#4、L10-P/A/I#4、L11-A#4）；同日依表序（沿前輪規則）取 **L7-P**。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py MoE "mixture of experts" "active parameters" "total parameters"`，**命中 0 筆**。載體全由 WebSearch／web-fetch 子代理原文取得。內部數字（§12）本輪未取用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L7-P#1**（測一通過｜不進 T）：FLOP/token × J/FLOP＝每 token **能量**下界（算力綁定）。本卡約束量為**權重位元組讀取**（頻寬綁定），且隨批量變動，非常數下界。
  - **L7-P#2**（部分通過）：訓練資料存量。本卡不論訓練。
  - **L7-P#3**（不通過；(1)(2)(5)）：容量 GW → token → 營收**總量上界**。本卡不經 GW、不論總營收；物件為**單一服務者**之每 token 成本對其流量（並發）之彈性。
  - **L7-P#4**（部分通過）：KV 快取位元組·秒 vs 按 token 計價（**每請求**、隨上下文長）。本卡之位元組為**權重**（跨請求共享、由批量攤提），與上下文長無關；同屬 decode 記憶體綁定，重疊列否決 (4)。
  - **L4-P#3**（HBM 位元守恆，硬體出貨側）：本卡不論 HBM 供給，只論模型架構對服務成本之批量依存。
  - **L7-I#4**（照付不議 → 降價填充）、**L7-A**（token 毛利恆等）：本卡之落差在成本曲線形狀，不在誘因或認列；重疊列否決 (4)。
  - **C-A5**（死 #13，API 已實現單價不可分離）、**C-P3**（#16）、**C-I1**（#10）：本卡不主張實驗室售價可分離；B 端落在**同一開放權重模型之多服務者報價**與公開服務系統揭露，非 L7 未上市主體科目。
- §7-10 領域最近公開：RuntimeWire（2026-10-25，OpenRouter 公開 API 抓取）；arXiv 2606.11690（2026-06-10）。下一檢查點＝OpenRouter 端點價格（可隨時重抓）、SemiAnalysis InferenceX 更新、新雲（Nebius Token Factory 等）3Q26 申報。

## 1. 落差一句

公開敘事以**活躍參數**估稀疏（MoE）模型之推論成本，並以開放權重 MoE 之低價推論「推論商品化、任何 GPU 持有者皆可平價供給」（Spheron「why active parameters set your GPU bill」為此口徑之例）。**種子主張：每個 decode 步，服務者須自 HBM 讀取被批內 token 觸及之全部專家權重；批量小時觸及專家數 ≈ `B·k`，批量大時趨近全體 `E`，故每 token 權重讀取 `W_tok ≈ (P_shared + P_expert·min(E, B·k)) ÷ B`。小批量下每 token 成本跟隨總參數，只有在 `B` 高到觸及全體專家且進入算力綁定區（Epoch：H100 臨界批量約 300）時才收斂至活躍參數。** 推論：同一開放權重 MoE 之每 token 成本對服務者流量具陡峭規模經濟——能以跨節點專家並行聚集高並發者（模型實驗室自營、極少數大型託管者）與其餘服務者之成本差可達數倍至一個數量級；可觀測之鏡像＝同一模型多端點報價離散（RuntimeWire：DeepSeek 單一模型 41 端點、33 家、輸出價差 13.3 倍）。落差＝若市場把「開放權重 MoE 低價」讀為推論供給之完全競爭，則低估流量集中度之價值（方向：成本優勢歸於流量聚合者，非歸於 GPU 持有者）。

## 2. 機制型態

| 欄 | 內容 |
|---|---|
| 型態 | **[P] 守恆**：每 decode 步之權重位元組讀取量為物理量；同一位元組被批內所有 token 共享，攤提量 ＝ 讀取量 ÷ 批量 |
| 守恆式 | `W_step = b·(P_shared + P_expert·n_touched(B))`，`n_touched(B) ≈ E·(1 − (1 − k/E)^B)`；`W_tok = W_step ÷ B`；頻寬綁定區 `t_step ≥ W_step ÷ BW_HBM` |
| 第一原理量 | 總參數／活躍參數比 `s = P_total ÷ P_active`；專家數 `E`、每 token 選 `k`；臨界批量 `B* ≈ FLOP/s ÷ BW`（Epoch：H100 ≈ 300） |
| 判定量 `[D]` | 規模經濟比 `ρ ＝ C_tok(B_low) ÷ C_tok(B*)`；同模型報價離散 `q ＝ p_max ÷ p_min`（須扣量化精度、上下文上限、延遲 SLA 之差異） |
| 可拒絕事件 | 同模型報價離散主要由量化／SLA 解釋（非流量）；小型服務者以同等成本供給高 `s` 模型；`s` 趨勢反轉（新模型改回稠密或低稀疏） |
| 表達工具型態（只指名，不選券） | 推論託管與新雲（上市者如 Nebius、CoreWeave；Cloudflare Workers AI）；開放權重實驗室多未上市。不選券 |
| 重疊 | L7-P#4（KV 位元組）、L4-P#3（HBM 位元）、L7-I#4、L7-A。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Epoch AI，Ege Erdil，「How do mixture-of-experts models compare to dense models in inference?」（2024-12-20）：「MoEs are more efficient at inference than dense models of the same total parameter count, but less efficient than dense models with the same active parameter count」；「an 8-way sparse model has the same short-context decoding economics as a dense model half its size」；H100 臨界批量「around 300」。舊硬體數字，測一須更新。https://epoch.ai/gradient-updates/moe-vs-dense-models-inference
2. SemiAnalysis InferenceX 詞彙「Active parameters」（無日期）：「every expert must sit in HBM ready to be selected, so capacity requirements and parallelism plans follow total parameters even though arithmetic follows active ones」。https://inferencex.semianalysis.com/glossary/active-parameters
3. Chitral Patil，arXiv 2606.11690（2026-06-10，未經同儕審查；PDF 只實讀約前 39k 字）：「At small batch sizes or in prefill-dominated regimes, total parameters drive memory bandwidth cost and the active-vs-total distinction narrows」；2×H100 NVL 單節點、1–10 rps 下「effective cost spans $0.21 to $15.25 per million output tokens—an underutilization penalty of 2.5–24×」。小模型（≤ 47B 總參數）單節點，不含跨節點專家並行。https://arxiv.org/abs/2606.11690
4. RuntimeWire，Morgan Laning（2026-10-25）：OpenRouter 公開 API 抓取，DeepSeek 單一模型「output prices … run from $0.18 to $2.40 per million tokens」「a 13.3x spread across 41 endpoints from 33 providers」；「OpenRouter's default routing favors the cheapest providers」。未拆量化／SLA。https://runtimewire.com/article/one-deepseek-model-41-endpoints-a-13x-price-gap-on-openroute-b239fa
5. DeepSeek open-infra-index Day 6「DeepSeek-V3/R1 Inference System Overview」（2025-03）：跨節點專家並行與「theoretical cost-profit ratio 545%」之原始揭露。**本輪 WebFetch 權限逾時（無人值守之逐網域核准），未實讀；非存在性主張。** 媒體轉述見 SCMP（僅搜尋結果標題，未實讀）。https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md ；https://www.scmp.com/tech/big-tech/article/3300734/deepseek-shows-power-v3-r1-models-theoretical-545-profit-margin
6. 測一須另取：OpenRouter 端點 API 原始（價格、量化、上下文、吞吐）以拆 `q`；主要開放 MoE 之 `E`、`k`、`s`（DeepSeek V3/V4、Kimi K2、Qwen3 模型卡）；SemiAnalysis InferenceX 之吞吐 vs 互動性曲線；上市推論託管者（Nebius、CoreWeave、Cloudflare）申報之推論服務利用率或 token 量；具名賣方是否以流量／並發建模開放權重推論毛利。**不宣稱已錯價。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 服務成本以總參數決定容量、以活躍參數決定算力，已是業界常識，吞吐 vs 互動性曲線已公開 | SemiAnalysis #2；Epoch #1 | 共識（否決 (2)） |
| R2 | 實測顯示活躍參數仍為飽和經濟之主要預測量 | arXiv 2606.11690 #3 | 規模經濟只在低負載，主流服務者皆在飽和區 |
| R3 | 報價離散源自量化、SLA、地區與行銷補貼，非成本曲線 | RuntimeWire #4 未拆解 | `q` 不能歸因於 `B` |
| R4 | 低價路由使流量自動集中至最低價者，規模經濟已被聚合平台抹平 | RuntimeWire #4（OpenRouter 預設路由） | 優勢歸於路由層而非服務者 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 同一開放權重 MoE 之多服務者報價無法取得量化精度、上下文上限或延遲之分列，或主要開放 MoE 之 `E`、`k`、`P_shared` 不可得，使 `q` 無法歸因、`n_touched(B)` 無法計算（量綱失敗）。
(2) 具名賣方或研究機構原文（非報導轉述）已以並發／批量建模開放權重推論之每 token 成本與服務者規模經濟（SemiAnalysis InferenceX 若已直接給出 MoE 每百萬 token 成本 vs 並發曲線且被賣方引用，即觸發），使落差為共識。
(3) `[D]` 於最寬假設下 `ρ` < 3（低負載對臨界批量之每 token 成本比），或扣除量化／SLA 後之同模型報價離散 `q` < 3。門檻於本卡凍結，測一不得改。
(4) 可運作對照只能寫成每 token 能量下界（L7-P#1）、KV 快取占用（L7-P#4）、HBM 供給（L4-P#3）、照付不議降價（L7-I#4）或 token 毛利恆等（L7-A）。
(5) 可交易表達不存在：受益之流量聚合者皆未上市（開放權重實驗室、私有託管商），上市推論託管者之推論營收不分列（§7-4 可分離性）。
(6) 12 個月內無可觀測之檢驗事件（新 MoE 發布之 `s` 揭露、端點報價重抓、上市託管者申報推論 token 量或利用率）。

複查觸發器（若日後殺）：任一上市推論託管者分列推論營收與 token 量；具名賣方以並發建模開放權重推論毛利；同模型報價離散在量化分組後仍 > 5 倍。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：推論服務營收與 token 量、利用率是否分列。
2. 可交易工具：上市新雲／邊緣推論者；開放權重實驗室不可交易。
3. 半衰期：端點報價可隨時重抓；新模型發布與季報為檢驗事件；`[V]` 日期不寫。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L7［P］標「已生成 #5」；`export/LEADS_算力收支.md` 線索 1 筆。不寫入：AIM_FUNNEL.md（§3 沿前輪慣例由測一輪對齊）、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L7-P#1–#4、L7-A#1–#4、L7-I#1–#4、L4-P#3、C-A5、C-P3、C-I1 結論。
