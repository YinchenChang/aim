# L7-P#6 生成卡｜模型層：守恆（端側權重駐留守恆：端側模型權重位元組＋KV ≤ 裝置 DRAM 扣系統保留之 AI 可用額；DRAM 價格衝擊使每機容量停滯時，端側可承載參數上限停滯 → 能力需求超出部分只能路由至雲端，「端側 AI 省雲端推論」之敘事受記憶體守恆約束）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；AIM_FUNNEL.md；archive/drive/USED_20260930_L7-P_generate_GK.md；archive/work/20261013_L7-P#2_generate_CL.md；archive/work/20261020_L7-P#3_generate_CL.md；archive/work/20261027_L7-P#4_generate_CL.md；archive/work/20261102_L7-P#5_generate_CL.md；archive/work/20261102_L7-P#5_test1_CL.md | EMITS: work/20261111_L7-P#6_generate_CL.md -->
**日期：** 2026-11-11　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 0→1／6）　**格：** L7-P　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額配置、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L6-I#6 已測一，Q-0191 done）。非已殺／刻意排除格中，最後測試日最舊＝2026-11-02（L7-P#5、L7-A#5）；同日依表序取 **L7-P**。既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py on-device DRAM smartphone "edge inference"`，**命中 0 筆**。內部數字（§12）本輪未取用。載體由 WebSearch 與 web-fetch 子代理原文取得。
- 比對之舊檔與死因型態，本卡須異型：
  - **L7-P#1**（通過｜不進 T）：每 token 能量下界（算力綁定，資料中心）。本卡約束量為**端點裝置記憶體容量**，非能量。
  - **L7-P#2**（部分通過）：訓練資料存量。本卡不論訓練。
  - **L7-P#3**（不通過）：容量 GW → 營收總量上界。本卡不經 GW、不論營收上界。
  - **L7-P#4**（部分通過）：資料中心 KV 位元組·秒 vs 按 token 計價。本卡之 KV 只作端側容量之一項，物件為**端／雲工作量分割**。
  - **L7-P#5**（不通過；(2)(3)(5)）：MoE 權重讀取對批量之規模經濟（服務端）。本卡無批量攤提；端側為單用戶（B＝1），約束為**駐留容量**而非頻寬攤提。死因 (2) 共識、(5) 不分列——本卡同列否決 (2)(5)，B 端改落在上市之手機 OEM／SoC／雲端授權方。
  - **L14-P#5**（企業推論公有／私有放置守恆）：本卡為**消費端裝置 vs 雲**，驅動為 DRAM 容量而非企業治理。**L15-P#5**（AI 建置吸收伺服器元件供給）：本卡取 DRAM 價格為外生輸入，不論伺服器交付。**L4-P#3**（HBM 位元守恆）：本卡不論 HBM 供給。
  - **C-A5**（死 #13）、**C-P3**（#16）、**C-I1**（#10）：不主張實驗室單價可分離。
- §7-10 領域最近公開：TrendForce 2Q26 行動 DRAM 報告（2026-05-15 轉載）；Apple–Google 聯合聲明（2026-01-12，MacRumors 報導；本輪僅搜尋結果標題，未實讀）。下一檢查點＝TrendForce 4Q26／1Q27 行動 DRAM 報告、Apple 10-K FY26（已出，測一以 sec.py 讀）、WWDC 2027 端側模型揭露。

## 1. 落差一句

公開敘事把端側 AI 讀為兩件同時成立之事：「端側推論替用戶與 OEM 省下雲端推論成本」與「端側 AI 推升每機 DRAM 內容」。**種子主張：端側可承載之模型受 `b·P_dev + KV ≤ M_AI = M_phone − M_OS/app` 約束；Apple 端側模型約 3B 參數、2-bit 量化感知訓練（已壓到極限位寬），故 `P_dev` 只能隨 `M_AI` 成長。2026 年行動 DRAM 合約價單季大漲（TrendForce：LPDDR5X 2Q26 季增 78–83%），OEM 降規格（高階 12GB 成主流、16GB 採用下降；低階回 4GB），`M_AI` 於可安裝基數上停滯。能力需求持續上升而 `P_dev` 停滯時，超出部分只能路由雲端（Apple：PCC 上 PT-MoE 伺服器模型；報導中之 1.2T 參數客製 Gemini）。** 推論：DRAM 衝擊不是端側 AI 之「延後」，而是把助理推論工作量**移往雲**之守恆轉移；落差＝若市場同時定價「端側省雲端成本」與「DRAM 內容升級」，兩者在價格衝擊期互斥（方向：端／雲分割移向雲，受益與受損按誰承擔雲端推論成本分配，本卡不主張方向）。

## 2. 機制型態

| 欄 | 內容 |
|---|---|
| 型態 | **[P] 守恆**：端側駐留權重與 KV 之位元組 ≤ 裝置 DRAM 可分配額；助理工作量 `W ≡ W_dev + W_cloud` |
| 守恆式 | `b·P_dev + KV(ctx) ≤ M_AI`；`W_cloud = W · Pr[所需能力 > C(P_dev)]` |
| 第一原理量 | 每權重位元 `b`（已 2 bit）；`M_AI`（裝置 DRAM − 系統保留）；可安裝基數之 DRAM 分布（TrendForce 2026 平均 8.5GB） |
| 判定量 `[D]` | 端側容量成長倍數 `g = M_AI(t+24m) ÷ M_AI(t)`（AI 合格可安裝基數加權）；雲端分流比 `f = W_cloud ÷ W` 之變動 |
| 可拒絕事件 | OEM 維持或提高 AI 機型 DRAM；端側改以 flash 串流權重（LLM in a flash 型）繞過 DRAM；助理能力需求停滯 |
| 表達工具型態（只指名，不選券） | 手機 OEM（Apple 等）之雲端推論成本承擔；雲端授權方（Alphabet）；行動 SoC／記憶體商。不選券 |
| 重疊 | L14-P#5、L15-P#5、L4-P#3、L7-P#4/#5。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. TrendForce 新聞稿（2025-12-11）：「smartphone and notebook brands are compelled to increase their product prices and reduce specifications」；「In high-end and mid-range models, DRAM capacities are expected to hover near the minimum standards, slowing upgrade cycles」；低階「likely to return to 4GB in 2026」。https://www.trendforce.com/presscenter/news/20251211-12831.html
2. I-Connect007 轉載 TrendForce（2026-05-15）：LPDDR5X 2Q26「QoQ surge of 78-83%」；「In the high-end segment, 12GB is becoming the mainstream configuration while 16GB adoption declines」；但「Average smartphone DRAM capacity is still projected to increase to 8.5GB in 2026」（年增 10%）——**平均仍升，與種子主張張力，測一須拆 AI 合格機型 vs 整體**。https://iconnect007.com/article/150033/mobile-dram-contract-prices-continue-rising-in-2q26-pressuring-smartphone-productio/150030/ein
3. Apple Machine Learning Research，Apple Intelligence Foundation Language Models Tech Report 2025（2025-07）：「a ∼3B-parameter on-device model … KV-cache sharing」「2-bit quantization-aware training」；伺服器端「Parallel-Track Mixture-of-Experts (PT-MoE)」於「Private Cloud Compute」。**只實讀摘要**；全文 arXiv 2507.13575 未讀。https://machinelearning.apple.com/research/apple-foundation-models-tech-report-2025
4. Unite.AI 轉述 Bloomberg（Gurman，2025-11-05）：「approximately $1 billion annually for a custom Gemini AI model」「1.2 trillion parameters and would run on Apple's Private Cloud Compute servers」。二手、未經雙方確認；Bloomberg 原文未讀。https://www.unite.ai/apple-reportedly-nearing-1-billion-annual-deal-with-google-to-power-revamped-siri/
5. Apple／Google 2026-01-12 合作聲明（僅搜尋結果，未實讀）：https://www.macrumors.com/2026/01/12/google-gemini-next-generation-siri/
6. 測一須另取：Apple 10-K FY26／10-Q（sec.py）之 PCC、雲端服務、記憶體成本與毛利句；Alphabet 10-Q 是否分列 Apple 授權；Apple 2026 端側模型更新（WWDC26）之參數與位寬；iPhone 17／18 系列 DRAM 規格；Samsung／Qualcomm 端側模型與 DRAM 規格；TrendForce／Counterpoint AI 合格可安裝基數之 DRAM 分布；Neowin「smartphones to come with less RAM … thanks to AI」所引原報告（本輪 fetch 失敗：client_error，非存在性主張）。**不宣稱已錯價。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 平均 DRAM 仍年增 10%，端側容量未停滯 | TrendForce #2 | `g` 可能 > 門檻（否決 (3)） |
| R2 | Apple 已公開端／雲雙層架構，雲端分流為設計而非約束 | Apple #3；聯合聲明 #5 | 共識（否決 (2)） |
| R3 | 助理雲端成本相對超大雲 AI capex 量級極小（報導約 $1B／年） | Unite.AI #4 | 量級不足（否決 (3)） |
| R4 | 權重自 flash 串流、量化再降位寬可繞過 DRAM 約束 | 待測一取具名出處 | 守恆式可規避（否決 (4)） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) AI 合格可安裝基數之 DRAM 分布、端側模型參數與位寬、或端／雲請求分流比之任一不可得，且無具名估計可代，使 `g` 或 `f` 無法計算（量綱失敗）。
(2) 具名賣方或研究機構原文（非報導轉述）已以「DRAM 價格 → 端側模型容量 → 雲端分流」鏈建模 OEM 雲端推論成本或授權方收入，使落差為共識。
(3) `[D]` 於最寬假設下 `g` ≥ 1.5（24 個月 AI 合格基數加權 `M_AI` 成長），或助理雲端分流之年化推論成本 ÷ 對應承擔方營業費用 < 1%。門檻於本卡凍結，測一不得改。
(4) 可運作對照只能寫成資料中心 KV 占用（L7-P#4）、MoE 批量攤提（L7-P#5）、企業放置（L14-P#5）、伺服器元件配給（L15-P#5）或 HBM 供給（L4-P#3）；或具名一手證據顯示 flash 串流／再降位寬已於量產端側助理採用，使 DRAM 非綁定約束。
(5) 可交易表達不存在：OEM 之雲端推論成本與授權方之對應收入皆不分列（§7-4 可分離性；同 L7-P#5 死因 (5) 型），且無替代科目（如 Apple 服務毛利附註、Alphabet 授權段）可承載。
(6) 12 個月內無可觀測之檢驗事件（TrendForce 季報、新機 DRAM 規格、WWDC 端側模型揭露、10-K／10-Q 雲端成本句）。

複查觸發器（若日後殺）：OEM 申報分列 AI 雲端推論成本或授權費；授權方分列 OEM 助理收入；TrendForce 首次發布 AI 合格機型 DRAM 分布。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：OEM 之 PCC／授權成本落於哪一科目；授權方是否分列。
2. 可交易工具：OEM、授權方、行動 SoC／記憶體商均上市；可分離性未知。
3. 半衰期：DRAM 合約價季更；新機規格年更；`[V]` 日期不寫。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L7［P］標「#6 已生成」；`export/LEADS_算力收支.md` 線索 2 筆（TrendForce 行動 DRAM 價格與平均容量）。不寫入：AIM_FUNNEL.md（§3 由測一輪對齊）、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L7-P#1–#5、L7-A#1–#5、L7-I#1–#5、L14-P#5、L15-P#5、L4-P#3、C-A5、C-P3、C-I1 結論。
