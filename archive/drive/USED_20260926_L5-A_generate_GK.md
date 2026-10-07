# L5-A 生成卡｜儲存與 IO：長脈絡使每 token IO 成本可分離
<!-- BY: SCOUT@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；15yX80fTMKfnqFzswGor_CvH2zVAc87M3 | EMITS: PENDING_UPLOAD -->
**日期：** 2026-09-26　**角色：** SCOUT@GK　**格：** L5-A　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 本輪只產生成卡。不測。不改正本狀態欄（FUNNEL §3／matrix L5［A］仍＝已生成）。不入 §1。

---

## 0. 本輪範圍

- 種子＝ARCH_3h §3.29 L5-A（`1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj`）：**每 token 之 IO 成本＝KV cache 讀寫量×每位元傳輸／儲存單價；長脈絡使該項由可忽略升為可分離**。B 端載體（3h 僅指名、未實讀）：雲端業者儲存營收分列。
- 生成序註：3h 填格為 A→I→P。同層 L5-I（出站費／資料重力）、L5-P（HBM 頻寬×時間守恆）本輪不生成。L1–L4、L8、L9、L12 已測或已殺；其餘已生成格依序本格為首。
- 已死相鄰、機制不同、不得合併：
  - **C-P1**（`ARCH_dead` #11，層標 L5）：方向翻負／價格不可分離；複查＝checkpoint 讀取占復原 >50%、儲存分列訓練／推論。種子是**推論態 KV／脈絡**之每位元單價，不是訓練 checkpoint 復原。
  - **C-A5**（#13）：前沿 API 單價於上市主體未分列。屬 L7 售價側，不是 IO 恆等。
  - **C-A1**（#6）：consumption／席次毛利不可分列。屬 L9 交付成本，不是 KV 位元。
- 3h 重疊標「新」。與 L5-P／L7-A 相鄰但不構成丟棄（3h 第 5 條）。
- CHARTER §7-3：不執行終端篩選。§7-4 三題只標「轉入個股層時必問」。§7-10：領域最近公開＝Gemini Developer API pricing（頁面日 2026-09-24，含 context caching 讀價＋每小時儲存價）；USENIX OSDI 2026 DirectKV 議程頁（2026-09-24）；NVIDIA Dynamo KVBM 文件；NVIDIA CES 2026 Context Memory Storage／CMX（2026-01，BlueField-4 預期 2026 H2）。下一官方檢查點＝任一雲端分部 10-K／10-Q 首次分列儲存 vs 運算、或分列推論脈絡／KV 類營收；或 API 商損益首次把 cached-token／context-storage 列為可對帳美元行。

---

## 1. 落差一句（生成物 → 候選陳述）

市場把推論成本讀成「每百萬 token 的 FLOP 價」（L7-A 側）。種子主張：長脈絡下，每新增 token 必須讀寫既有 KV；該 IO 量隨脈絡長度近似線性，乘上每位元傳輸或儲存單價後，可由短脈絡的可忽略項變成可分離項。錯價只在把「token 成本＝計算」當成完整恆等，或把雲端「儲存營收」當成該 IO 項的代理。C-P1 已在訓練 checkpoint／復原方向上死；本格 B 端不是那一列。

---

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計可分離項（IO 成本由可忽略升為可分列）；不是純物理上界、不是誘因 |
| 選擇者 | 服務端定價（cached-read／context-storage SKU）＋架構（每 token KV 位元數） |
| 可見端 | API 價目之 cached input／context storage 列；加速器商「context memory」產品名；雲端分部總營收 |
| 指名不可見端 | 雲端儲存營收中屬推論 KV／脈絡之份額；每 token 實際搬移位元×單價之美元時序 |
| 主張 | 脈絡長度上升 ⇒ KV 讀寫量上升 ⇒ IO 項相對 FLOP 項之權重上升；短脈絡可忽略不蘊含長脈絡仍可忽略 |
| 表達工具型態（只指名，不選券） | 已上市、美股可交易之雲端分部或儲存系統主體；API 價目為公開表。不選券 |
| 重疊 | C-P1 訓練儲存分列；L5-P HBM 頻寬守恆；L5-I 出站費；L7-A token 毛利。重疊不構成丟棄 |

恆等式（生成用，非正式載入）：

`C_io(token) = V_KV(token, L, arch) × P_bit`

`L` 大到使 `C_io` 相對 `C_flop` 不再可折進「其他」⇒ 可分離。本輪不估參數、不寫 H1。

---

## 3. 已 fetch 之公開錨（URL；非完整 B 端實讀）

1. Gemini Developer API pricing（頁面日 2026-09-24）：explicit context caching 同時列 **cached-token 讀價**與 **每百萬 token 每小時儲存價**（例：部分 Pro 檔 $4.50／1M tok／hr；多數 Flash／2.5 檔 $0.50–$1.00／1M tok／hr，2027-01-01 部分調升）。此為公開價目上「脈絡以儲存計價」的現成列，不是 10-K 營收列。https://ai.google.dev/gemini-api/docs/pricing
2. Gemini context caching 說明：計費因子＝快取 token 數＋TTL 儲存時長；預設 TTL 1 小時。https://ai.google.dev/gemini-api/docs/caching
3. Anthropic prompt caching（文件族，2026 價目轉述一致）：cache write 1.25×（5 min TTL）／2×（1 h TTL），cache read 0.1× 基價。是「再計算折扣＋寫入溢價」，**不是**按小時儲存列。生成錨，測試一須對官方價目頁實讀。https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
4. OpenAI prompt caching 文件族：自動前綴快取；較新型號 cached input 可至約 0.1×。TTL／是否收儲存費依型號，頁面須實讀。https://platform.openai.com/docs/guides/prompt-caching
5. NVIDIA Dynamo KVBM（官方文件）：KV block 可自 GPU 卸到 CPU／Disk 分層（`DYN_KVBM_CPU_CACHE_GB`／`DYN_KVBM_DISK_CACHE_GB`）。證實「脈絡態」有獨立記憶階層，不是只活在 HBM。https://docs.nvidia.com/dynamo/latest/user-guides/kv-cache-offloading.html
6. NVIDIA CES 2026 Inference Context Memory Storage／CMX（BlueField-4；二手架構文 2026-01-11）：機櫃級脈絡儲存與 Dynamo 配對；約 4×150 TB／器具之公開轉述。**不是 10-K 科目。** https://www.chiplog.io/p/analysis-of-nvidias-bluefield-4-dpu
7. USENIX OSDI 2026 DirectKV 議程頁（2026-09-24）：長脈絡 KV 卸到 CPU 記憶體；相對既有卸除方案之傳輸／容量數字為論文主張，非申報。https://www.usenix.org/conference/osdi26/presentation/luo
8. Amazon 10-K 收入認列：AWS 安排含 compute、storage、database 等，按使用量認列；**分部只報 AWS 總額，不把 storage 從 compute 拆成美元行。** 例：https://www.sec.gov/Archives/edgar/data/1018724/000101872425000004/R24.htm
9. Alphabet 收入拆分：Google Cloud 為單一雲端行，無儲存 vs 運算 vs 脈絡快取。https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
10. 產業二手（Wing 2026-08／09；非申報）：128K／70B 約 40 GB KV vs ~140 GB 權重；MLA vs 標準注意力每 token KV 可差數倍。只作量級線索。https://www.wing.vc/content/the-ai-memory-stack

以上為生成錨。**不宣稱雲端儲存營收已分列 KV，不宣稱 `C_io` 已成可重算官方時序，不宣稱長脈絡 IO 已被市場錯價。** 測試一之 B 端須實際 fetch 價目或 10-K／10-Q 附註，禁止只疊「AI 是儲存負載」評論與 C-P1 已死的訓練 checkpoint 列。

---

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | 3h 指名之 B 端是「雲端業者儲存營收分列」；AWS／Azure／GCP 公開分部是雲端總額，S3／Blob／GCS 無獨立美元行，更無 KV 行 | AMZN／GOOGL 10-K 拆分 | 測試一可能停在 (a)：所需量不是所讀之量（與 C-P1／N-02 同型風險，量不同） |
| R2 | API 價目的 cached-read 是計算折扣，不一定是「每位元儲存／傳輸」；Anthropic／OpenAI 無 Gemini 那種 hourly storage 列 | Anthropic／OpenAI 價目結構 | 恆等式右端 `P_bit` 在多數可見價目上不存在 |
| R3 | 架構（MLA、offload、前綴快取）把 `V_KV` 壓下去，可分離項可再變回可忽略 | DeepSeek-V3 MLA；Dynamo KVBM；Moonshot 轉述 | 長脈絡不保證 IO 權重單調上升 |
| R4 | 賣方已把 cached token 與 context memory 做成公開 SKU／產品名；若價已按脈絡定，則無錯價 | Gemini storage 列；NVIDIA CMX 品類 | 機制真、價已反映，升格失敗在「未定價且可捕捉」 |
| R5 | 把本格做成「買 NAND／企業 SSD／雲端儲存股」會滑向一般儲存週期或滑回 C-P1 訓練儲存 | `ARCH_dead` #11；Sandisk／NAND 敘事 | 表達點選錯＝換格，不是本格通過 |

種子仍可能在「公開價目之脈絡儲存／cached-token 列 × 可反解之每 token KV 位元，對齊已上市主體之可分列營收」上寫成可重算對照。乘積是否存在、IO 項是否真能從雲端／API 總額拆出，是測試一的題。

---

## 5. SCOUT 裁決

**留。** 不進 T。下一動作＝ANALYST@GK 對本格做測試一（B 端須實際 fetch 並列 URL；優先 10-K／10-Q 儲存分列或 API 商損益之 cached／context-storage 美元行，次為可把價目列反解成 `V_KV × P_bit` 的官方規格；禁止只重讀訓練 checkpoint 列與「AI storage workload」評論）。

理由（只到殺／留）：
- 恆等本身可陳述，與 L5-I／L5-P、已死 C-P1／C-A5／C-A1 不同構成。
- 3h B 端未實讀；本輪只把指名載體寫成可派工之規格項。R1–R4 足夠強，預設風險＝雲端不拆儲存、多數 API 無 `P_bit`、架構壓低 `V_KV`、SKU 已定價；不是機制已被否證。
- 終端三題本階段不答（§7-3）。

否決觸發（寫給 ANALYST，不是本輪執行）：
- 對 10-K／10-Q／20-F 與官方價目實讀後，`V_KV` 與 `P_bit` 皆無法形成可對帳區間，只剩雲端總額與評論一句；或
- 可運作對照只能寫成訓練 checkpoint／復原佔比（即滑回 C-P1）；或
- 公開層已出現穩定可拒絕之「長脈絡 IO 仍折進計算單價且不可分離」，使可分離主張與可見定價不可辨。

複查觸發器（若日後殺）：任一美股可交易雲端分部或 API／儲存系統主體於 10-K／10-Q／20-F，分列儲存 vs 運算、或分列推論脈絡／KV／context-cache 營收（或等價：cached-token／context-storage 之已實現美元行），且可與同期公開價目之 `P_bit` 對帳。

---

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：KV／脈絡 IO 能否從雲端或「AI 基礎設施」再拆；能否拒絕一般物件儲存／訓練資料湖／checkpoint。
2. 可交易工具：恆等落在美股可交易揭露主體，而非僅私有 API 商或無申報之快取中介。
3. 半衰期：MLA／offload／CMX 量產一旦把 `V_KV` 或有效 `P_bit` 壓回可忽略，≥12 個月窗內可分離項是否消失。

---

## 7. 本輪寫入／不寫入

寫入：本生成卡入 Drive `work/`（fileId 見標頭 EMITS，上傳後回填）。
不寫入：FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（§3 L5 仍＝已生成；不入 §1）；matrix 正本 `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`；§2／§4／§5；INDEX.json；ARCH_dead。禁止新建同名正本。狀態欄對齊屬測試一之後 session。
