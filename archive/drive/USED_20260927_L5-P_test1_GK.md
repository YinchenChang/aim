<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1YfrqbYR3Gsfnhia_F_Qb5aoGdbl5eGFM；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi；1VaVhI3eGdH_h6rT9Cso3BwUHiz4wVoOm | EMITS: PENDING_UPLOAD -->
# L5-P 測一｜B 端實讀（JEDEC／廠商 HBM BW 單位 × 可反解參數量模型卡 → `BW／V_byte` vs ridge）

**角色：** ANALYST@GK　**日期：** 2026-09-27　**格：** L5-P（儲存與 IO：HBM 頻寬×時間＝可搬移位元；推論 arithmetic intensity 下界使頻寬成守恆瓶頸）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先 JEDEC／廠商 HBM BW 單位與至少一個可反解參數量之公開模型卡，對帳成 `BW／V_byte` vs `ridge＝PeakFLOP／BW`。**禁止只重讀 C-P1 訓練列、L5-A 雲端總額、「HBM 短缺」評論。** 不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T、不入 §1。
**原陳述（生成卡 `1YfrqbYR3Gsfnhia_F_Qb5aoGdbl5eGFM`；種子 3h §3.29）：** 單位時間可從 HBM 搬出的位元＝頻寬×時間，是守恆量；decode／低 batch 的 AI 有下界；一旦低於裝置 ridge，吞吐上界是頻寬不是算力。
**對照式（生成用）：** `Bits(t)＝BW_HBM×t`；`AI＝FLOP／byte`；`ridge＝PeakFLOP／BW`；`AI < ridge ⇒ throughput ≤ BW／V_byte`。本輪不估參數、不寫 H1。
**否決觸發（生成卡寫給本輪）：** (1) 實讀後 `BW` 與 `V_byte` 皆無法形成同一單位可對帳區間，只剩產品句與參數個數；或 (2) 可運作對照只能寫成訓練 checkpoint／雲端儲存分列／HBM 產能 ASP；或 (3) 公開層已出現穩定可拒絕之「decode AI 已高於該代 ridge」或「吞吐不隨 BW 移動」。
**領域最近公開（§7-10）：** JESD270-4 新聞稿 2025-04-16；JESD270-4A 目錄 2025-12；Samsung HBM4 商用出貨 2026-02-12；Micron HBM4 量產 2026-03-16；SK hynix HBM4 產品頁（本輪實讀）；NVIDIA H200 官網 141 GB／4.8 TB/s（本輪實讀）。下一官方檢查點＝生成卡原文：JEDEC HBM4E 正式出版之 pin／堆疊頻寬下界，或任一美股加速器／HBM 商 10-K／10-Q 首次把裝置級記憶體頻寬（或 HBM 代際×堆疊數之可對帳 BW）與運算吞吐分列且可與公開規格對帳。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260927_L5-P_generate_GK.md` `1YfrqbYR3Gsfnhia_F_Qb5aoGdbl5eGFM`（12418 B，2026-09-27T00:28:12Z）；`20260923_HEALTH_CL.md` `1_urT6I7RovcM73D3IBTKGIk6RY1z9nC0`；`20260923_HEALTH_GK.md` `1byQGbjCmIT1orLv51moyAH5xnABFO95e`；`DUP_PLACEHOLDER_L1-I_test1_do_not_use.md` `1lci-pu8ekOI7T-za2Sl93q-j1GUoNAjl`
- query/：`ARCH_dead.md` `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`；`ARCH_matrix.md` `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`（L5［P］＝已生成）；`CHARTER_HIST.md` `1DKg3HUr-zOWw20OmNe1aDpWT_izDwdiT`；`INDEX.json` `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`；`MECH.md` `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-09-26T15:01:36Z role SCOUT）
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-09-26；§1 無 L5-P；§3 L5［P］＝已生成）
- L5-A 測一 `1VaVhI3eGdH_h6rT9Cso3BwUHiz4wVoOm`、L5-I 測一 `1RgdzJlhJ-JluyxMLRTg8T-vsK-0XpSMJ` 已 `USED_`，不在 work/；本輪只引用 L5-A fileId 作「禁止重讀雲端總額」邊界
- 本輪上傳前 work/ exact_name `20260927_L5-P_test1_GK.md` 空；無內容相近測一
- work 主動維護：L5-P 生成卡未吸收進 FUNNEL／matrix（待本測一後由 SCOUT 對齊）。HEALTH 兩份與 DUP_ 占位非本輪標的。本輪不建 `DONE_`。

---

## 終態

**測一通過｜不進 T。** 機制（`Bits(t)＝BW×t`；decode／低 batch 之 AI 可低於 ridge，使每秒 token 上界 ≤ `BW／V_byte`）未被否證。B 端指名兩欄均已實讀，且可寫成同一單位對照：

1. **BW 欄可單位化。** JEDEC 新聞稿給堆疊地板：2048-bit × 8 Gb/s → **2 TB/s／堆疊**。廠商產品頁／出貨稿給出貨針速與堆疊 BW：Micron **>11 Gb/s、>2.8 TB/s／堆疊**；Samsung **11.7 Gb/s（至 13 Gb/s）、至 3.3 TB/s／堆疊**；SK hynix **>2.8 TB/s、2K I/O**。加速器官網給裝置合計 BW：H200 **141 GB HBM3e、4.8 TB/s**。單位皆為 B/s（或等價 TB/s）。**不把 JEDEC 地板當成出貨針速，不把廠商堆疊 BW 乘未在官網出現的堆疊數當成 H200 裝置 BW。**
2. **V_byte 欄可反解。** Meta Llama 3.1 官方卡標 **70B**＋GQA＋128k；公開 `config`（hidden 8192、layers 80、heads 64、kv_heads 8、vocab 128256、intermediate 28672、dtype BF16）可還原權重位元與每 token KV 位元。HF 模型頁列 71B params／BF16；架構還原 N≈70.6×10^9。`V_byte` 以 byte／token 計。
3. **ridge 對帳可寫。** H200 官網 Peak FP16／BF16 Tensor＝1979 TFLOPS（註²；頁面本輪未寫 sparsity）、BW＝4.8 TB/s → `ridge`∈約 **206–412 FLOP/byte**（視 1979 是否含 2:4）。decode batch＝1、BF16 權重主項之 AI≈**1 FLOP/byte**（FP8 權重≈2），低於該區間。吞吐上界 BF16≈**34 token/s／卡**（100% BW、只計權重）。
4. **否決未觸發。** (1) 單位可對帳，不是只剩產品句。(2) 對照不是 checkpoint／雲端總額／ASP。(3) 公開層未出現「decode AI 已高於該代 ridge」；H200 官網反將記憶體頻寬寫成 LLM／HPC 瓶頸句，但那是行銷句，不是「吞吐不隨 BW 移動」的拒絕項。

不進 T：R1（10-K 無「被頻寬閘住的推論營收」列）未解；R2（batch／快取／卸載可把 AI 推近 ridge）使下界非常數；R3（賣方已按 BW 敘事賣卡）使錯價未證；§7-4 三題本輪不答。無 H1。

---

## A. HBM／裝置 BW（實讀）

| 源 | URL | 本輪讀到的 BW 單位 |
|---|---|---|
| JEDEC JESD270-4 新聞稿 2025-04-16 | https://www.jedec.org/news/pressreleases/jedec%C2%AE-and-industry-leaders-collaborate-release-jesd270-4-hbm4-standard-advancing | 2048-bit；32 ch×2 pseudo；**至 8 Gb/s**；**至 2 TB/s／堆疊**；4／8／12／16-hi；24 Gb 或 32 Gb die；最高立方 **64 GB**（32 Gb×16-hi） |
| JEDEC 標準目錄 JESD270-4／4A | https://www.jedec.org/standards-documents/docs/jesd270-4 | 標題 High Bandwidth Memory (HBM4) DRAM。4A＝Version 1.1、目錄日 Dec 2025。摘要：每 ch **64-bit DDR**。**正文須註冊**；針速／2 TB/s **不在無登入摘要**，本輪地板數字來自新聞稿，不偽稱已讀標準全文 |
| Micron HBM4 產品頁 | https://www.micron.com/products/memory/hbm/hbm4 | 12H **36 GB**、16H **48 GB**；**>11.0 Gbps**；**>2.8 TB/s／堆疊**；2048-bit |
| Micron 量產稿 2026-03-16 | https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin | HBM4 36GB 12H 已量產出貨；**>2.8 TB/s**；**>11 Gb/s**；為 NVIDIA Vera Rubin 設計。另 16H 48 GB 送樣 |
| Samsung 出貨稿 2026-02-12 | https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing ；半導體站同文 https://semiconductor.samsung.com/news-events/news/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/ | 商用出貨。穩定 **11.7 Gbps**、至 **13 Gbps**；對 JEDEC 8 Gbps 約 +46%；單堆疊至 **3.3 TB/s**（稱較 HBM3E ×2.7）；12-hi 24–36 GB、16-hi 至 48 GB |
| SK hynix HBM4 產品頁 | https://product.skhynix.com/products/dram/hbm/hbm4.go | **over 2.8TB/s**；**IO 2K**；**至 16-high**。本輪頁面未吐針速／容量格 |
| NVIDIA H200 官網 | https://www.nvidia.com/en-us/data-center/h200/ | **141 GB HBM3e**；**4.8 TB/s**（SXM 與 NVL 同）。FP16／BF16 Tensor **1,979 TFLOPS**（SXM；註²）；FP8 Tensor **3,958 TFLOPS**。Llama2 70B 推論對 H100 稱 1.9×（H200 BS32 vs H100 BS8，ISL 2K／OSL 128） |

**單位核對（公開乘法，非正式載入）：**  
`BW_stack ≈ (interface_bits × pin_Gb/s)／8`。2048×8／8＝**2.048 GB/s×1000 → 2.048 TB/s**（JEDEC「至 2 TB/s」）。2048×11／8＝**2.816 TB/s**（Micron／SK「>2.8」）。2048×13／8＝**3.328 TB/s**（Samsung「3.3」）。出貨針速 ≥ 標準地板；二者不可互換。

H200 官網**未**給堆疊數。裝置 BW 用 **4.8 TB/s** 一列，不用第三方「6×24 GB」反推。H200 是 HBM3e 裝置，與 HBM4 堆疊規格不同代，只作「可見裝置 BW＋可見 PeakFLOP」的 ridge 分母／分子。

---

## B. 模型卡／`V_byte`（實讀）

| 源 | URL | 本輪讀到的可反解量 |
|---|---|---|
| Meta Llama 3.1 官方卡 | https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md | 8B／**70B**／405B；GQA＝Yes；context **128k**。**未列精確參數整數** |
| HF 官方模型頁（gated） | https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct | 頁面 **71B params**、tensor **BF16** |
| 公開 config 鏡（非 gated） | https://huggingface.co/d-matrix/Llama-3.1-70B/blob/main/config.json | `hidden_size` 8192；`num_hidden_layers` 80；`num_attention_heads` 64；`num_key_value_heads` 8；`intermediate_size` 28672；`vocab_size` 128256；`max_position_embeddings` 131072；`torch_dtype` bfloat16 |
| HF 釋出說明 KV 表 | https://huggingface.co/blog/llama31 | FP16 KV：70B 於 1k／16k／128k token＝**0.313／4.88／39.06 GB** |

**還原（生成用；N 取區間）：**  
`head_dim＝8192／64＝128`。  
`N_label＝70×10^9`（官方卡）；架構還原 N≈70.6×10^9；HF 頁 71×10^9。本輪 `N∈[70,71]×10^9`。  
權重位元：`W_BF16＝N×2` → **140–142 GB**；`W_FP8＝N×1` → **70–71 GB**。  
每新 token 之 KV（BF16）：`2 × n_kv_heads × head_dim × n_layers × 2 B＝2×8×128×80×2＝327,680 B/token`。  
HF 表 0.313 GB／1k token＝313,000 B/token（差約 4.5%；本輪主用 config 公式，表作核對）。

`V_byte(token) ≈ W／batch ＋ L×KV_byte`（decode；略啟動與寫入）。  
batch＝1、L≪W／KV 時，`V_byte ≈ W`。

---

## C. `BW／V_byte` vs ridge（同一單位）

裝置錨＝H200 SXM 官網：`BW＝4.8×10^12 B/s`。  
`Peak_FP16_page＝1.979×10^15 FLOP/s`（註²）。若該列含 2:4，dense ≈ 0.989×10^15。  
`ridge＝Peak／BW` → **412 FLOP/byte**（頁面數字）或 **206 FLOP/byte**（dense 半值）。區間寫 **[206, 412] FLOP/byte**。

decode batch＝1、只計權重：  
`FLOP/token ≈ 2N ≈ 1.41×10^11`。  
`AI_BF16 ≈ 2N／(2N)＝1 FLOP/byte`；`AI_FP8 ≈ 2`。  
兩者皆 **≪ ridge**。守恆上界：  
`tok/s ≤ BW／W_BF16 ≈ 4.8e12／1.41e11 ≈ 34`；FP8 ≈ **68**。  
L＝4096 時 KV 讀≈1.34 GB，相對 140 GB 權重為次項，不翻轉 AI≪ridge。

**batch 使 AI 上升（R2，本輪承認、不否證守恆）：** 權重項攤銷後 `AI≈batch`（BF16、略 KV）。要接近 ridge 下沿 206，約需 batch∼200（忽略 KV／效率）。低 batch／互動 decode 仍在頻寬側。本輪**不**主張所有推論都 memory-bound。

加大 PeakFLOP、BW 不變 → ridge 上移、`BW／V_byte` **不動**。這是種子可拒絕項，可用上表重算。本輪不讀已實現 serving 是否貼上界（生成卡「指名不可見端」）。

---

## D. 本輪明確不讀、不引用為通過條件

- C-P1 訓練 checkpoint／復原佔比；`ARCH_dead` #11 死因不是本格 B 端。
- L5-A 測一 `1VaVhI3eGdH_h6rT9Cso3BwUHiz4wVoOm` 之雲端分部總額。所需量不是儲存 vs 運算美元行。
- 「HBM 短缺」產能／ASP 評論。所需量是 B/s 與 byte／token，不是顆數週期。
- 10-K「裝置 BW vs 運算吞吐」分列：本輪不開。複查觸發器保留給該列首次出現。
- 閉源 frontier 模型卡（R6）：本輪改用開源 Llama 3.1 70B，不把不可反解的 frontier 名當成 `V_byte`。
- H200 堆疊數之第三方拆解；HBM4E／cHBM／HBF／host 併讀把守恆式作廢之主張（未讀到可拒絕的官方 BW 重定義）。

---

## 對 R1–R6 之測一處分（不寫 H1）

| # | 反方 | 本輪 |
|---|---|---|
| R1 | 規格是 TB/s 與參數個數；損益無頻寬閘住營收列 | **成立為表達層風險，不是本測一否決。** BW 與 `V_byte` 已可對帳。科目分列屬 §7-4 #1／複查觸發器 |
| R2 | batch／快取／MLA／卸載把 AI 推過 ridge | **半成立。** GQA 已折進 KV 公式，低 batch 仍 AI≪ridge；高 batch 可移走閘門。下界非常數。守恆式仍真 |
| R3 | 賣方已把 decode＝memory-bound 寫進產品頁 | **半成立。** H200 官網寫記憶體頻寬對 LLM／HPC 關鍵，並給對 H100 之推論倍率（且比較改變了 batch）。機制可見≠錯價成立 |
| R4 | 瓶頸是容量 GB 不是 TB/s | **未把本格做成買 GB。** 容量進入 `W` 是否裝得下；吞吐上界用的是 BW。二者同頁分列（141 GB vs 4.8 TB/s） |
| R5 | 做成買 HBM 商因短缺＝換格 | **未觸發。** 不選券、不寫表達點 |
| R6 | 閉源參數不可反解 | **本輪避開。** 指定 Llama 3.1 70B。閉源主體的已實現吞吐仍可能空 |

---

## 轉入個股層時必問（§7-4，本輪仍不答）

1. 財報科目：頻寬閘門後的利益能否從「HBM 營收」或「資料中心 GPU」再拆；能否拒絕一般 DRAM／NAND／訓練產能。
2. 可交易工具：守恆落在美股可交易揭露主體，而非僅私有加速器或無申報之客製 base die。
3. 半衰期：HBM4E／cHBM／PIM／host 併讀一旦把有效 BW 或 AI 移過 ridge，≥12 個月窗內上界是否被工程抵銷。

---

## 本輪寫入／不寫入

寫入：本測一入 Drive `work/`（fileId 見標頭 EMITS，上傳後回填）。
不寫入：FUNNEL 正本、matrix、INDEX、ARCH_dead、CHARTER。禁止新建同名正本。狀態欄對齊屬下一 SCOUT session。
