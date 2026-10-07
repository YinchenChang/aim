<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1vbroLuAzR1ayP0SuO23VN-5nhr8p5AV8；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；15yX80fTMKfnqFzswGor_CvH2zVAc87M3；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h | EMITS: （本檔；Drive work/ 上傳後填 fileId） -->
# L5-A 測一｜B 端實讀（儲存分列／cached 美元行，或價目反解 `V_KV × P_bit`）

**角色：** ANALYST@GK　**日期：** 2026-09-26　**格：** L5-A（儲存與 IO：長脈絡使每 token IO 成本可分離）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先 10-K／10-Q／20-F 儲存 vs 運算分列，或 API 商損益之 cached-token／context-storage 已實現美元行；次為可把官方價目反解成 `V_KV × P_bit` 的規格。**禁止只疊訓練 checkpoint 列與「AI storage workload」評論。** 不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T、不入 §1。
**原陳述（生成卡 `1vbroLuAzR1ayP0SuO23VN-5nhr8p5AV8`；種子 3h §3.29）：** 每 token 之 IO 成本＝KV cache 讀寫量×每位元傳輸／儲存單價；長脈絡使該項由可忽略升為可分離。市場把推論成本讀成每百萬 token 的 FLOP 價。B 端指名＝雲端業者儲存營收分列。
**對照式（生成用）：** `C_io(token) = V_KV(token, L, arch) × P_bit`。`L` 大到使 `C_io` 相對 `C_flop` 不再可折進「其他」⇒ 可分離。本輪不估參數、不寫 H1。
**否決觸發（生成卡寫給本輪）：** (1) 對 10-K／10-Q／20-F 與官方價目實讀後，`V_KV` 與 `P_bit` 皆無法形成可對帳區間，只剩雲端總額與評論一句；或 (2) 可運作對照只能寫成訓練 checkpoint／復原佔比（滑回 C-P1）；或 (3) 公開層已出現穩定可拒絕之「長脈絡 IO 仍折進計算單價且不可分離」，使可分離主張與可見定價不可辨。
**領域最近公開（§7-10）：** Gemini Developer API pricing（頁面日 2026-09-24）；Gemini context caching（頁面日 2026-09-02／explicit 段仍有效）；Anthropic prompt caching 官方頁；OpenAI prompt caching 官方頁；AMZN FY2025 10-K acc `0001018724-26-000004`（截止 2025-12-31）；GOOGL FY2025 10-K acc `0001652044-26-000018` 與 Q2 2026 10-Q acc `0001652044-26-000071`（截止 2026-06-30）；NVIDIA CMX 產品頁（讀取 2026-09-24）＋ BlueField-4 新聞 2026-01-05；Dynamo KVBM 官方文件；USENIX OSDI 2026 DirectKV 議程頁。下一官方檢查點＝生成卡原文（見下）。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260926_L5-A_generate_GK.md` `1vbroLuAzR1ayP0SuO23VN-5nhr8p5AV8`（11042 B，2026-09-26T13:59:20Z）；`20260923_HEALTH_CL.md` `1_urT6I7RovcM73D3IBTKGIk6RY1z9nC0`；`20260923_HEALTH_GK.md` `1byQGbjCmIT1orLv51moyAH5xnABFO95e`；`DUP_PLACEHOLDER_L1-I_test1_do_not_use.md` `1lci-pu8ekOI7T-za2Sl93q-j1GUoNAjl`
- query/：`ARCH_dead.md` `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`（#11 C-P1）；`ARCH_matrix.md` `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`（L5［A］＝已生成）；`CHARTER_HIST.md` `1DKg3HUr-zOWw20OmNe1aDpWT_izDwdiT`；`INDEX.json` `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`（無 L5-A 測一鍵）；`MECH.md` `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-09-26T13:55:50Z role SCOUT）
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-09-26；§1 無 L5-A；§3 由 matrix 代理，L5［A］＝已生成＝3h 快照）
- 3h 快照 `1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj` L5-A B 端僅指名「雲端業者儲存營收分列」
- C-P1 原檔 `15yX80fTMKfnqFzswGor_CvH2zVAc87M3`（ARCH_4e §4.25：叢集可靠性稅；方向翻負／價格不可分離；複查＝checkpoint 讀取占復原＞50%）
- 本輪上傳前 work/ 無同名 `20260926_L5-A_test1_GK.md`（Drive exact_name 空）
- work 主動維護：L5-A 生成卡未吸收進 FUNNEL／matrix（待本測一後由 SCOUT 對齊）。HEALTH 兩份與 DUP_ 占位非本輪標的。本輪不建 `DONE_`。

---

## 終態

**不通過。不進 T。** 機制（長脈絡下每新增 token 必須讀寫既有 KV；該 IO 量×每位元單價可由短脈絡的可忽略項變成可分離項）未被否證。失敗在可觀測性——3h 指名之 B 端（雲端儲存營收分列）在 AMZN／GOOGL／MSFT 公開分部是雲端總額，無儲存 vs 運算美元行，更無 KV／脈絡行；API 商損益無 cached-token／context-storage 已實現美元行。公開價目上，**僅 Gemini explicit caching 同時列 cached-read 與每小時儲存價**（單位＝`$ / 1M tok / hr`，不是 `$ / bit`）；Anthropic／OpenAI 是寫入溢價＋讀取折扣，無儲存時長列。`V_KV`（每 token KV 位元）無與上述價目同主體之官方規格可反解成可對帳區間。乘積 `V_KV × P_bit` 對不齊任一美股可交易主體之可分列營收。未滑回 C-P1。

| 測試項 | 結果 |
|---|---|
| B 端已實讀（非指名；非只疊 checkpoint／「AI storage」評論） | **通過**　AMZN FY2025 10-K；GOOGL FY2025 10-K＋Q2 2026 10-Q；MSFT Intelligent Cloud／Azure 公開段；Gemini pricing＋caching；Anthropic prompt caching＋API 價目；OpenAI prompt caching＋API 價目；NVIDIA Dynamo KVBM；NVIDIA CMX 產品頁＋2026-01-05 新聞；OSDI 2026 DirectKV 議程 |
| 雲端 10-K／10-Q 分列儲存 vs 運算，或分列推論脈絡／KV 營收 | **不通過**　AWS／Google Cloud／Azure 皆為雲端總額或消費平台總額 |
| API 商損益出現 cached-token／context-storage 已實現美元行 | **不通過**　Alphabet 不拆 Gemini cache；OpenAI／Anthropic 非申報主體、無該列 |
| 官方價目可反解 `V_KV × P_bit` 且對齊已上市主體可分列營收 | **不通過**　Gemini 有 `$ / tok / hr` 儲存列，缺官方 `V_KV`（bit／token）與申報美元對帳端 |
| 可運作對照是否只能寫成訓練 checkpoint／復原（C-P1） | **否**　本輪載體皆推論態 KV／脈絡；未用 checkpoint 佔比 |
| 公開層是否已穩定拒絕「IO 可從計算單價分離」 | **未穩定拒絕**　Gemini 已把儲存時長列成獨立價目；另兩家折進計算倍率。行業層不統一 |
| 否決觸發 (1) | **觸發**　可對帳區間不存在；所讀＝雲端總額＋價目列＋產品名 |
| 否決觸發 (2) | **未觸發** |
| 否決觸發 (3) | **未觸發**　Gemini 儲存列使「一律折進計算單價」不可作為行業穩定拒絕句 |
| 升格 T | **否** |

失效歸因（§7-2）：不是檢索失敗。失敗在量綱——所需量（同窗可對帳之 `V_KV` 與 `P_bit`，或申報層 KV／脈絡／cached 美元行）不是所讀之量（AWS／GCP／Azure 總額、API `$ / 1M tok` 折扣、`$ / 1M tok / hr` 儲存價目、CMX 產品名、KVBM GB 環境變數、論文加速比）。現況檔名＝上列 work／query。複查觸發器＝生成卡原文（見下）。停。

本格不入 §1。不改正本（對齊屬 SCOUT）。

---

## 已實讀載體

### A. 雲端分部｜Amazon FY2025 10-K（截止 2025-12-31；acc `0001018724-26-000004`）

分部三行：North America／International／AWS。AWS FY2025 net sales **$128,725 million**（FY2024 107,556）；operating income **$45,606 million**。原文：「The AWS segment consists of amounts earned from global sales of **compute, storage, database, and other services**.」列名存在於描述句，**美元行只有 AWS 總額**。無 S3／EBS／EFS 分列，無推論脈絡／KV／context-cache 行。收入認列按使用量，不把 storage 從 compute 拆成可畫兩期之差。

R1 在本檔已成立：3h 指名之「雲端業者儲存營收分列」＝所需量不是所讀之量。

### B. 雲端分部｜Alphabet FY2025 10-K acc `0001652044-26-000018`＋Q2 2026 10-Q acc `0001652044-26-000071`

FY2025 Google Cloud 營收 **$58,705 million**（FY2024 43,229）；operating income **$13,910 million**。Q2 2026 Google Cloud **$24,768 million**（Q2 2025 13,624）。原文定義：GCP consumption／subscription＋Workspace＋「sale of TPU systems」。質性句出現「AI-optimized storage offerings」，**不是美元行**。無儲存 vs 運算 vs 脈絡快取分列。Pichai 公開 token 吞吐（第三方轉述：每分鐘 API token）不連到 cache 營收科目——本輪不把 token 吞吐寫成 `C_io`。

### C. 雲端分部｜Microsoft Intelligent Cloud／Azure（FY2026 公開段＋2026-09-02 分部改組 8-K 材料）

可見端＝Intelligent Cloud 總額與 Azure and other cloud services 成長率／（後續）Azure 消費營收列。原文列 Azure 為 compute、networking、storage、AI 之綜合平台。FY27 起改報 Agents and Infra／Devices and Consumer，Azure「更純」為消費平台——**仍不預告儲存 vs 運算 vs KV 分列**。本輪不把 Azure 成長率或 Intelligent Cloud 毛利率下滑寫成本格 IO 項。

### D. API 價目｜Gemini explicit context caching（頁面日 pricing 2026-09-24；caching 2026-09-02）

官方計費因子（caching 頁原文結構）：(i) cache token count，後續引用以折扣讀價；(ii) **storage duration（TTL）**，按 cached token count × 時長計；(iii) 非快取 input／output。預設 TTL **1 hour**。implicit caching：預設開啟、**無儲存費**；explicit：有儲存費。

Pricing 頁（Paid tier，摘可核對列；單位 USD／1M tokens）：

| 型號 | cached-token 讀價 | 儲存價（／hr） |
|---|---|---|
| Gemini 3.8／3.7／3.6 Flash | $0.075（至 2026-12-31）；$0.15（自 2027-01-01） | $0.50（至 2026-12-31）；$1.00（自 2027-01-01） |
| Gemini 2.5 Pro | $0.125（≤200k）／$0.25（>200k） | $4.50 標準／$8.10 large prompts |
| Gemini 2.5 Flash | $0.03（text／image／video） | $1.00（同模態）／$1.80 audio |

此為公開價目上「脈絡以儲存時長計價」的現成列。單位是 **`$ / 1M tok / hr`**，不是 `$ / bit`。缺官方每 token KV 位元，不能把該列寫成 `P_bit`。該列亦**不是** Alphabet 10-K 之已實現美元行。禁止用價目×假設用量造 Google Cloud 內之 KV 營收。

### E. API 價目｜Anthropic prompt caching（官方 docs＋API 價目頁）

結構：**cache write** 5-min TTL＝1.25× base input；1-hour TTL＝2× base input。**cache read** 多數型號 0.1×；Fable 5.1／Mythos 5.1＝0.025×；Opus 5.5＝0.05×。Fable 5.1 基價例：input $10／output $50／1M tok；Fable cache read＝$0.25／1M tok。TTL 綁在寫入溢價上。**無每小時儲存列。** 可見端＝計算折扣＋寫入溢價，不是每位元儲存／傳輸。R2 在 Anthropic 成立。

### F. API 價目｜OpenAI prompt caching（官方 guides＋API 價目）

官方句：快取保存的是可重用前綴之中間狀態（「key-value or KV states」）。GPT-5.6+：cache read **0.1×** uncached input；cache write **1.25×**；`ttl` 支援值 `"30m"`。更早型號用 `prompt_cache_retention`（in_memory／24h）。官方句：「Cache-write pricing is not an additive fee」。價目例（頁面所列）：GPT-6 Astra uncached input $10／cached $1；Sol $2／$0.20（／1M tok）。**無每小時儲存列。** R2 在 OpenAI 成立。私有主體無 10-K cached 美元行。

### G. 架構／產品名｜NVIDIA Dynamo KVBM（官方文件，現行路徑）

生成卡舊 URL `/user-guides/kv-cache-offloading.html` 本輪 **404**。現行官方頁確認同一機制：KVBM 將 KV block 自 GPU（G1）卸到 host／CPU（G2）、disk（G3）、object storage（G4）。環境變數 `DYN_KVBM_CPU_CACHE_GB`／`DYN_KVBM_DISK_CACHE_GB`。這證實「脈絡態」有獨立記憶階層，**不是** 10-K 科目，也不是 `$ / bit`。規格單位＝GB 容量，不是每 token 位元。

### H. 架構／產品名｜NVIDIA CMX（產品頁＋2026-01-05 新聞稿）

官方句：CMX 是「AI-native context tier」，「optimized for ephemeral key-value (KV) cache」，對照「general-purpose storage」。新聞稿（2026-01-05，CES）：BlueField-4 驅動 Inference Context Memory Storage Platform；相對傳統儲存宣稱至多 5× tokens/s 與功耗效率；BlueField-4／合作器具「available in the second half of 2026」。產品頁**無標價 SKU、無容量美元、無 10-K 行**。R4 的「賣方已做成產品名」成立於品類層，不成立於可對帳營收層。4×150 TB／器具屬二手轉述，本輪不以該數字作官方容量主張。

### I. 論文錨｜USENIX OSDI 2026 DirectKV 議程頁

Luo & Shen, *No Buffer, No Bottleneck: Efficient Zero-Copy KV Cache Offloading for Long-Context LLMs*。主張：相對既有卸除，傳輸量至多 −50%、GPU 記憶體 −43%、端到端至多 1.2×。會議 2026-07。**論文主張，非申報、非價目。**

### J. 明示不採

- 訓練 checkpoint／復原佔比、非同步 checkpoint 採用率（C-P1 複查句）。本輪不借。
- Wing.vc／產業部落格之「128K／70B ≈ 40 GB KV」量級。非官方規格，不得與 Gemini `$ / tok / hr` 相乘造 `C_io`。
- 把 CMX 合作名單（Dell／HPE／NetApp／Pure／WEKA 等）讀成已上市主體已分列 KV 營收。
- NAND／企業 SSD／一般物件儲存週期（生成卡 R5）。本輪不選券、不換格。
- C-A5 前沿 API 單價未分列、C-A1 席次毛利。層與量不同。
- 第三方「cache share」假設把價目加成實驗室損益（The AI Realist 2026-09-08）。評論，非申報。

---

## 對種子與反方

| 主張 | B 端讀後 |
|---|---|
| 長脈絡使 `C_io` 由可忽略升為可分離 | 機制可陳述。Gemini 價目已把儲存時長從計算單價拆出；申報層未拆。可分離在**價目結構**上部分可見，在**營收科目**上不可見 |
| 錯價＝把 token 成本當成純 FLOP | 可見端已被雲端總額、`$ / 1M tok` 折扣、`$ / tok / hr` 儲存價、CMX 品類名用盡。錯價句無官方乘積對照錨 |
| R1 雲端不拆儲存／KV | **成立** |
| R2 `P_bit` 在多數價目不存在 | **成立於 Anthropic／OpenAI**；Gemini 有時長列但仍非 `$ / bit` |
| R3 架構壓低 `V_KV`（MLA／offload／前綴快取） | 本輪不估。KVBM／DirectKV／CMX 證明卸除與分層存在，可把有效搬移壓回可忽略——這是半衰期題，不是本輪否證 |
| R4 SKU 已定價故無錯價 | 價目／品類已出現；申報美元未出現。升格失敗點在「未定價且可捕捉」之前：先缺可對帳乘積 |
| R5 滑到 NAND／C-P1 | **本輪不滑** |

「公開價目之脈絡儲存／cached-token 列 × 可反解之每 token KV 位元，對齊已上市主體之可分列營收」——左端列在 Gemini 存在、在另兩家不存在；中端官方 `V_KV` 不存在；右端申報美元不存在。三端不能同時寫成可重算對照。

---

## 不開 T／§7-4

進 T 需數值窗與可拒絕之 H1 倍數。本輪可寫入的只有「AWS／GCP／Azure 總額、Gemini `$ / tok / hr`、Anthropic／OpenAI 倍率、KVBM GB、CMX 品類、論文加速比」。不夠把 `C_io` 寫成財富倍數窗。

§7-4 三題本輪不答（生成卡：轉入個股層時必問；本格不轉、不進 T）。題目本身已由本輪讀數預示方向（雲端／AI 基礎設施再拆不出 KV；可見價目主體部分為未上市 API 商；MLA／offload／CMX 量產可把有效 `V_KV` 壓回可忽略），但不在本輪作答。

**複查觸發器（沿用生成卡，不改寫）：** 任一美股可交易雲端分部或 API／儲存系統主體於 10-K／10-Q／20-F，分列儲存 vs 運算、或分列推論脈絡／KV／context-cache 營收（或等價：cached-token／context-storage 之已實現美元行），且可與同期公開價目之 `P_bit` 對帳。

---

## URL

1. https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
2. https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/R19.htm
3. https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
4. https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/R25.htm
5. https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm
6. https://ai.google.dev/gemini-api/docs/pricing
7. https://ai.google.dev/gemini-api/docs/caching
8. https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview
9. https://platform.claude.com/docs/en/build-with-claude/prompt-caching
10. https://platform.claude.com/docs/en/about-claude/pricing
11. https://developers.openai.com/api/docs/guides/prompt-caching
12. https://openai.com/api/pricing/
13. https://docs.nvidia.com/dynamo/kubernetes/kv-cache-offloading/overview
14. https://docs.nvidia.com/dynamo/reference/components/kvbm-configuration
15. https://www.nvidia.com/en-us/data-center/ai-storage/cmx/
16. https://nvidianews.nvidia.com/news/nvidia-bluefield-4-powers-new-class-of-ai-native-storage-infrastructure-for-the-next-frontier-of-ai
17. https://www.usenix.org/conference/osdi26/presentation/luo
18. https://microsoft.gcs-web.com/static-files/6f77f14c-9bdd-49c1-bfa3-1dbe8d872424

**（檔結束。）**
