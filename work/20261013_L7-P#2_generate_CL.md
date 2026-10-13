# L7-P#2 生成卡｜模型層：守恆（公開人類文本存量有限 × 預訓練 token 需求 → 新鮮人類生成內容之取用權由「可爬取」轉「須授權」）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260930_L7-P_generate_GK.md；archive/drive/USED_20260930_L7-P_test1_GK.md；archive/drive/USED_20261002_L11-I_generate_GK.md；archive/drive/USED_20261001_L10-A_test1_GK.md | EMITS: work/20261013_L7-P#2_generate_CL.md -->
**日期：** 2026-10-13　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 0→1／6）　**格：** L7-P　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（最後一筆 L13-A#2 測一 2026-10-11，Q-0025 done）。非已殺／刻意排除之格中，最後測試日最舊者＝**L7-P**（測一 2026-09-30T09:28Z，`archive/drive/USED_20260930_L7-P_test1_GK.md`；依 `archive/FILEIDS.tsv` 時戳，早於 L7-I 09:30、L7-A 09:30、L10-P 09:47）。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py 資料 data licensing token stock`，命中 30 筆，**與本格相關 2 筆**：SRC_MOD_029／030（DeepSeek V4-Flash／V4-Pro 預訓練 token，出處 arXiv `2606.19348`）。本輪回原文實讀失敗（WebFetch 權限逾時，失敗歸因＝無人值守之逐網域核准；非存在性主張）。只作「預訓練 token 量」之載體指名，不作證據。
- 比對之舊檔與死因型態，本卡須異型：
  - **L7-P#1**（測一通過｜不進 T）：FLOP × 每 FLOP 焦耳＝推論**能量**下界；守恆量＝物理能量。本卡守恆量換為**訓練資料存量**（公開人類文本 token 數），作用在**預訓練**端，不論推論能量、不論 TOPS/W。
  - **C-P3**（死 #16）：權重更新支出非獨立科目。本卡不論權重更新成本；B 端落在**資料供給方**之申報科目，不落在 L7 未上市主體。
  - **C-A5**（死 #13）：API 已實現單價不可分離。本卡不論模型售價。
  - **C-I1**（死 #10）：估值歸因權重能力。本卡不主張權重能力定價。
  - **C-I2**（死 #12，L8）：人類回饋**專家單價**（新產出之標註勞務）。本卡為**既存**人類生成內容之存量取用權，非標註勞務；不得滑回專家單價。
  - **L8-P**（死 #2）：每條交付人工分鐘數。本卡不論標註工時。
  - **L11-I**（測一不通過）：代理代表使用者議價，注意力存量轉合約性（agent API 條款）。本卡為**訓練用**內容取用，非代理流量／注意力；B 端為授權收入科目而非條款頁。
  - **L10-A**（測一不通過）：TAC／轉介分潤。本卡不論流量分潤。
  - **L5-P#2**、**L5-P**：KV／HBM 頻寬。無關。
- §7-10 領域最近公開：Epoch AI「Will we run out of data?」（Villalobos 等；頁面未載更新日，本輪讀取 2026-10-13）；Reddit 10-Q 期 2026-06-30（申報 2026-07-31）。下一檢查點＝Reddit 3Q26 10-Q（約 2026-10 下旬至 11 月初）。

## 1. 落差一句

市場把預訓練資料視為可無限爬取、邊際成本趨零之投入；種子主張：公開人類文本存量近似固定（守恆型存量），在現行過度訓練與多輪重複下近窗即被用盡，故新鮮、可驗證為人類生成之內容取用權由「結構性免費」轉為「合約性付費」，該轉換在少數資料持有方之申報科目上可觀測。錯價只在把既往授權收入當成一次性、非經常項。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆型存量耗竭**：\(S_{\mathrm{human}}\)（有效公開人類文本 token）近似固定；需求 \(D_t = N_t \times r_t\)（參數 × token/參數，含過度訓練倍數）÷ 可重複輪數 \(e\)。\(D_t/e \to S_{\mathrm{human}}\) 時邊際人類 token 之影子價格由 0 轉正 |
| 選擇者 | 合成資料／RL 自生資料能否替代人類 token 而不劣化（model collapse 與否）；重複輪數 \(e\) 之上限；授權是否可被未授權爬取繞過 |
| 可見端 | Epoch 存量與耗竭年份區間；資料持有方 10-Q 收入分列（Other revenue）、RPO 之「content licensing」組成、客戶集中度與續約風險句 |
| 指名不可見端 | 每 token 授權單價；授權方實際被用於預訓練之 token 數；前沿實驗室預訓練語料之人類／合成比例 |
| 表達工具型態（只指名，不選券） | 已上市、美股可交易、於申報中分列內容授權收入或 RPO 之內容持有方。不選券 |

恆等式（生成用，非正式載入）：\(D_t^{\mathrm{eff}} = N_t \cdot r_t / e \;\le\; S_{\mathrm{human}} + S_{\mathrm{syn}}^{\mathrm{usable}}\)。種子綁定條件＝\(S_{\mathrm{syn}}^{\mathrm{usable}}\) 對前沿品質不可完全替代。**不把 Epoch 之耗竭年份當成市場未定價之證據；不把授權收入成長當成存量耗竭之證據（可能為搜尋／顯示用途）；不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Epoch AI，*Will we run out of data? Limits of LLM scaling based on human-generated data*：有效公開人類文本存量「on the order of 300 trillion tokens」，90% CI 100T–1000T；80% CI 於 2026–2032 年間被完全使用；過度訓練 5× 則約 2027、100× 則約 2025；多輪訓練使有效存量擴 2–5×；Llama 3-70B 過度訓練約 10×。https://epoch.ai/blog/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data
2. Reddit, Inc. Form 10-Q，季末 2026-06-30，acc `0001713445-26-000100`（`python tools/sec.py doc` 全文 grep）：Note 3 收入分列「Other revenue 43,280／34,842（千美元，2Q26／2Q25）；六個月 82,021／68,573」；「remaining performance obligations in contracts with an original expected duration exceeding one year was $ 92.1 million. This amount consists primarily of long-term content licensing contracts」，2026 餘 62.0M、2027 30.1M；收入認列「right to access content … generally ratably over the license period」；風險句「substantially all of the contract value associated with our licensing revenue is derived from two of our partners … may not be renewed, or … renewed based on less favorable terms」及「the value of content for AI training purposes may be reduced over time」。https://www.sec.gov/Archives/edgar/data/1713445/000171344526000100/rddt-20260630.htm
3. WSJ 經 Crypto Briefing 轉述（2026-07-22）：Reddit 與 Google 之 AI 資料授權續約談判「hit turbulence」，管理層考慮限制 Google 取用；轉述 Google 約年 60M、OpenAI 估年 70M（二手，非申報）。https://cryptobriefing.com/reddit-stock-google-ai-deal-non-renewal/
4. 線索：Tokenomics SRC_MOD_029／030 → arXiv `2606.19348`（DeepSeek V4 預訓練 token；本輪未讀成）。

缺段（§7-2）：Reddit FY25 10-K 收入分列與 ≥ 4 季 Other revenue 序列；其他內容持有方（新聞、圖庫、論壇、程式碼平台）之申報層授權科目；Epoch 頁更新日期；前沿實驗室合成資料占比原文。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | 合成資料與推理模型自生資料可替代人類 token（OpenAI 以 Strawberry 生成 Orion 訓練資料之報導） | Boulton，The Next Platform，2025-01-16（Dell 委託內容） | \(S_{\mathrm{syn}}\) 可用則存量不綁定；機制成立 ≠ 未定價（§7-4） |
| R2 | 多輪重複擴有效存量 2–5×，且過度訓練政策可調；耗竭區間 2026–2032 寬 | Epoch（同 §3-1） | 綁定時點不可釘，重定價窗可能 > 實驗期或已過 |
| R3 | 申報方自陳：AI 訓練用內容價值「may be reduced over time」；兩大客戶集中、續約可能降價 | Reddit 10-Q 2Q26 風險因子 | 授權收入可為非經常、可被買方議價壓低；方向不定 |
| R4 | 未授權使用：「some companies … use such content without license」 | Reddit 10-Q 2Q26 | 取用權未必轉合約性；存量守恆不保證付費 |
| R5 | 授權用途混合（machine learning、business analysis、display、training）；Other revenue 非純訓練授權 | Reddit 10-Q 2Q26 | 申報科目與機制量不可分離（C-A5／C-P1 型風險） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後申報層無任何可與「訓練用內容授權」對應之收入或 RPO 分列（只有 Other revenue 混合項且無 RPO 組成句），且無第二家上市內容持有方可對照；或
(2) 可運作對照只能寫成標註／人類回饋專家單價或工時（滑回 C-I2／L8-P）、代理流量條款（滑向 L11-I）或流量分潤（滑向 L10-A）；或
(3) 前沿實驗室或具名研究原文已穩定顯示預訓練人類 token 需求不再成長（合成／RL 資料已為主且無劣化），使存量不綁定；或
(4) Epoch 存量或耗竭區間之最新更新已推遲至實驗期（2036）之後；或
(5) 授權收入序列 ≥ 4 季內呈下降或續約降價之申報證據，與「轉合約性付費」方向相反。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：訓練用授權能否自 Other revenue／RPO 拆出。2. 可交易工具：持有方為美股可交易且授權占比足以影響損益。3. 半衰期：合成資料若在 ≥ 12 個月窗內替代人類 token，取用權之合約性是否消失。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L7［P］格加「#2 已生成」；`AIM_FUNNEL.md` §3 一句；`query/QUEUE.md` 新列。不寫：ARCH_live／INDEX／ARCH_dead（狀態對齊屬測一之後）。不改 L7-P#1、L7-A、L7-I 及任何已殺格。
