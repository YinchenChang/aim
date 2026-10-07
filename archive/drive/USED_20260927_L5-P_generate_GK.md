# L5-P 生成卡｜儲存與 IO：HBM 頻寬×時間＝可搬移位元；推論 arithmetic intensity 下界使頻寬成守恆瓶頸
<!-- BY: SCOUT@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；1vbroLuAzR1ayP0SuO23VN-5nhr8p5AV8；1VaVhI3eGdH_h6rT9Cso3BwUHiz4wVoOm；1RaVhNa9EEeMUq6dssdfGjQTIdwex7osx；1RgdzJlhJ-JluyxMLRTg8T-vsK-0XpSMJ | EMITS: PENDING_UPLOAD -->
**日期：** 2026-09-27　**角色：** SCOUT@GK　**格：** L5-P　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 本輪只產生成卡。不測。不改正本狀態欄（FUNNEL §3／matrix L5［P］仍＝已生成＝3h 快照）。B 端僅指名。不入 §1。L5-A＝已測｜不進 T（測一 `1VaVhI3eGdH_h6rT9Cso3BwUHiz4wVoOm`；生成 `1vbroLuAzR1ayP0SuO23VN-5nhr8p5AV8`）。L5-I＝已測｜不進 T（測一 `1RgdzJlhJ-JluyxMLRTg8T-vsK-0XpSMJ`；生成 `1RaVhNa9EEeMUq6dssdfGjQTIdwex7osx`；matrix 註「部分通過」不入 §1）。

---

## 0. 本輪範圍

- 種子＝ARCH_3h §3.29 L5-P（`1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj`）：**HBM 頻寬×時間＝可搬移位元數；推論之 arithmetic intensity 下界使記憶體頻寬成為守恆型瓶頸**。B 端載體（3h 僅指名、未實讀；本輪維持僅指名）：HBM 規格；模型參數量。重疊標「~~C-P1~~ 已封存（叢集可靠性），機制不同」。
- 生成序註：3h 填格為 A→I→P。同層 L5-A／L5-I 已有生成卡＋測一（皆不入 §1）。`work/` 巡查：無 `L5-P` 檔、無同名／內容相近待推檔。進行中僅 `20260923_HEALTH_CL.md`、`20260923_HEALTH_GK.md`、`DUP_PLACEHOLDER_L1-I_test1_do_not_use.md`（已 DUP_ 前綴，本輪不另標）。
- 已死相鄰、機制不同、不得合併：
  - **C-P1**（`ARCH_dead` #11，層標 L5）：死因＝P1 方向翻負／價格不可分離（T-12 型）；複查＝checkpoint 讀取占復原 >50%、儲存分列訓練／推論。3h 重疊欄寫「叢集可靠性」——與 dead 原文死因不同；本格用 dead 原文，不沿用 3h 的叢集標籤當死因。種子是**裝置級可搬移位元上界**，不是訓練 checkpoint／復原佔比。
  - **L5-A**：長脈絡使每 token IO 成本可分離（會計項）。已測｜不進 T。不是物理頻寬上界。
  - **L5-I**：出站費取用權型態轉換。已測｜不進 T。不是 HBM 通道。
  - **L4-P**：SerDes 通道損耗封頂銅纜距離。已測｜不進 T。是機櫃互連距離，不是封裝內 HBM 匯流排。
  - **L7-A／C-A5**：token 售價−FLOP 成本；前沿 API 單價未分列。屬售價側，不是頻寬守恆。
- CHARTER §7-3：不執行終端篩選。§7-4 三題只標「轉入個股層時必問」。§7-10：領域最近公開＝JEDEC JESD270-4（2025-04-16）／JESD270-4A（2025-12）／SPHBM4 JESD330-4（2026-06）＋附則（2026-08）；Samsung HBM4 商用出貨（2026-02-12）與產品頁 HBM4／HBM4E；Micron HBM4 量產公告（2026-03-16，Vera Rubin）與產品頁；SK hynix HBM4 產品頁＋Hot Chips 2026（約 2026-08，12H 量產）；NVIDIA H200 官方頁 141 GB／4.8 TB/s；GTC 2026 SK hynix S81977（頁面日含 2026-09-26）；TrendForce 推論記憶體階層（2026-09-11）；BOOST 論文（2026-09-21）。下一官方檢查點＝JEDEC HBM4E 正式出版之 pin／堆疊頻寬下界，或任一美股加速器／HBM 商 10-K／10-Q 首次把裝置級記憶體頻寬（或等價：HBM 代際 × 堆疊數之可對帳 BW）與運算吞吐分列且可與公開規格對帳。

---

## 1. 落差一句（生成物 → 候選陳述）

市場把推論吞吐讀成「卡的 TFLOPS／token 單價」（L7-A 側）或「卡的 GB 容量」。種子主張：單位時間可從 HBM 搬出的位元＝頻寬×時間，是守恆量；decode／低 batch 的 arithmetic intensity 有下界（每產出一 token 須重讀權重＋既有 KV 的位元，FLOP／byte 不隨模型變大而等比例上升），一旦低於裝置 ridge（峰值 FLOP÷BW），吞吐上界是頻寬不是算力。錯價只在把「下一代算力翻倍＝推論吞吐翻倍」或把「容量 GB」當成頻寬瓶頸的代理。C-P1 已在訓練 checkpoint／復原方向上死；L5-A 已在雲端儲存／KV 美元分列上停；本格 B 端不是那兩列。

---

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆／純物理位元流上界（BW×t；roofline：AI 下界 vs ridge）；非會計恆等、非誘因 |
| 選擇者 | 裝置規格（每堆疊 BW×堆疊數）＋模型／批次決定之每 token 搬移位元 |
| 可見端 | JEDEC／廠商 HBM 每堆疊 BW；加速器官網合計 HBM BW；公開模型參數量 |
| 指名不可見端 | 已實現推論吞吐是否被該 BW 上界閘住（vs 被算力、互連、軟體閘住）；10-K 是否把 BW 代際當可對帳美元行 |
| 主張 | `AI_decode` 低於 `PeakFLOP／BW` ⇒ 每秒 token 上界 ≤ `BW／V_byte(token)`；加大 FLOP 而不加大 BW 不移動該上界 |
| 表達工具型態（只指名，不選券） | 已上市、美股可交易之 HBM 商或加速器主體；規格為公開標準／產品頁。不選券 |
| 重疊 | C-P1 訓練儲存；L5-A KV IO 會計可分離；L5-I 出站；L4-P 銅距離；L7-A token 毛利。重疊不構成丟棄 |

守恆式（生成用，非正式載入）：

`Bits(t) = BW_HBM × t`

`AI = FLOP／byte`；`ridge = PeakFLOP／BW`；`AI < ridge  ⇒  throughput ≤ BW／V_byte`

`V_byte` 由權重位元＋KV 位元（參數量、精度、脈絡、batch）決定。本輪不估參數、不寫 H1。

---

## 3. B 端指名（3h 原欄；本輪不實讀、不宣稱可分離）

3h 原文兩欄：**HBM 規格；模型參數量**。本輪只把指名寫成可派工之載體，禁止把下列 URL 當成測試一已完成。同層 L5-A 測一已實讀雲端總額——本格要的量是**堆疊／裝置 BW 規格 × 可反解之每 token 位元**，不是儲存 vs 運算美元行，不得把 L5-A 的分部總額重貼成本格通過。

| 指名欄 | 載體（只指名） | 公開入口（錨，非實讀結論） |
|---|---|---|
| HBM 規格 | JEDEC HBM4：2048-bit、32 ch、標稱至 8 Gb/s、堆疊頻寬至 2 TB/s；4／8／12／16-hi；24 Gb／32 Gb die | JESD270-4 出版 2025-04-16；JESD270-4A 2025-12。正文付費／註冊。新聞稿可讀標稱。https://www.jedec.org/standards-documents/docs/jesd270-4 ；https://www.jedec.org/news/pressreleases/jedec%C2%AE-and-industry-leaders-collaborate-release-jesd270-4-hbm4-standard-advancing |
| HBM 規格 | 廠商堆疊 BW（高於 JEDEC 地板）：Micron HBM4 12H 36 GB、>11 Gb/s、>2.8 TB/s／堆疊；Samsung 商用 HBM4 至 13 Gb/s、至 3.3 TB/s／堆疊；SK hynix 產品頁 >2.8 TB/s、2K I/O | https://www.micron.com/products/memory/hbm/hbm4 ；https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin ；https://semiconductor.samsung.com/news-events/news/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/ ；https://semiconductor.samsung.com/dram/hbm/ ；https://product.skhynix.com/products/dram/hbm/hbm4.go |
| HBM 規格 | 加速器合計 BW（堆疊數×每堆疊，官網）：H200 141 GB HBM3e、4.8 TB/s | https://www.nvidia.com/en-us/data-center/h200/ |
| 模型參數量 | 公開權重規模（例：Llama 類 8B／70B／405B；廠商 frontier 卡常只給「模型名」不給可對帳參數×精度位元） | 開源模型卡／技術報告為錨，不是 10-K 科目。測試一須指定一組可反解 `V_byte` 的公開模型，禁止只用「大模型」一句 |

以上為指名錨。**不宣稱 JEDEC 地板＝出貨 BW，不宣稱廠商 TB/s 已在 10-K 分列，不宣稱 decode 必低於該代 ridge，不宣稱容量 GB＝頻寬上界，不宣稱 HBM4E／cHBM／HBF／host 併讀已把守恆式作廢。** 測試一之 B 端須實際 fetch 標準／產品頁之 BW 單位與至少一個可反解參數量之模型卡，禁止只疊「HBM 短缺」評論、C-P1 訓練儲存列、或 L5-A 雲端總額。

---

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | 規格是 TB/s 與參數個數；損益沒有「被頻寬閘住的推論營收」列；可見端是產能／ASP | HBM 商與加速器 10-K 慣例（L5-A 已示範分部總額不可拆） | 測試一可能停在 (a)：所需量不是所讀之量 |
| R2 | batch／前綴快取／MLA／權重卸載把 `AI` 或 `V_byte` 推過 ridge，瓶頸從 BW 移走 | 公開 serving 文獻；Dynamo KVBM（L5-A 錨）；BOOST 2026-09 host+HBM 併讀 | 下界不是常數；守恆式仍真，閘門不在 HBM |
| R3 | 賣方已把「decode 是 memory-bound、所以買下一代 HBM／更寬卡」寫進 GTC／產品頁；若價已按 BW 代際定，則無錯價 | SK hynix GTC 2026 S81977；Micron／Samsung 產品句 | 機制真、價已反映 |
| R4 | 容量（GB／脈絡）與頻寬是兩個量；TrendForce 2026-09 主張推論第二瓶頸是容量，HBF／CMX 補的是 GB 不是 TB/s | TrendForce 2026-09-11；L5-A 之 CMX／KV 卸除 | 把本格做成「買更多 GB」＝換格 |
| R5 | 做成「買 MU／加速器因 HBM 短缺」會滑到產能週期或滑回 C-P1 | `ARCH_dead` #11；一般 DRAM 敘事 | 表達點選錯＝換格，不是本格通過 |
| R6 | 參數量在閉源 frontier 不可反解；開源卡的 `V_byte` 推不到上市主體的已實現吞吐 | 閉源模型卡不公布參數×精度 | B 端第二欄在可交易主體上可能空 |

種子仍可能在「JEDEC／廠商每堆疊 BW × 公開堆疊數 ＝ 裝置 BW；開源模型卡給出 `V_byte`；ridge 與 decode AI 可畫在同一單位」上寫成可重算對照。乘積是否存在、上界是否可拒絕「只加 FLOP 即加吞吐」，是測試一的題。

---

## 5. SCOUT 裁決

**留。** 不進 T。下一動作＝ANALYST@GK 對本格做測試一（B 端須實際 fetch 並列 URL；優先 JEDEC／廠商 HBM 規格之 BW 單位與至少一個可反解參數量的公開模型卡能否對帳成 `BW／V_byte` vs ridge；禁止只重讀訓練 checkpoint 列、雲端總額、「HBM 短缺」評論）。本輪不測。

理由（只到殺／留）：
- 守恆本身可陳述，與已測 L5-A／L5-I、已測 L4-P、已死 C-P1／C-A5 不同構成。
- 3h B 端未實讀；本輪維持僅指名。R1–R6 足夠強，預設風險＝規格不是科目、AI 下界可被批次／架構移走、賣方已按 BW 敘事定價、容量被誤當成頻寬、閉源參數不可反解；不是機制已被否證。
- 終端三題本階段不答（§7-3）。

否決觸發（寫給 ANALYST，不是本輪執行）：
- 對規格與模型卡實讀後，`BW` 與 `V_byte` 皆無法形成同一單位的可對帳區間，只剩產品句與參數個數；或
- 可運作對照只能寫成訓練 checkpoint／雲端儲存分列／HBM 產能 ASP（即滑回 C-P1 或產能週期）；或
- 公開層已出現穩定可拒絕之「decode AI 已高於該代 ridge」或「吞吐不隨 BW 移動」，使頻寬上界與可見定價不可辨。

複查觸發器（若日後殺）：任一美股可交易加速器或 HBM 商於 10-K／10-Q／20-F，分列裝置級記憶體頻寬（或 HBM 代際×堆疊數之可對帳 BW）與運算吞吐，且可與同期 JEDEC／產品頁 BW 及一組公開模型之 `V_byte` 對帳。

---

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：頻寬閘門後的利益能否從「HBM 營收」或「資料中心 GPU」再拆；能否拒絕一般 DRAM／NAND／訓練產能。
2. 可交易工具：守恆落在美股可交易揭露主體，而非僅私有加速器或無申報之客製 base die。
3. 半衰期：HBM4E／cHBM／PIM／host 併讀一旦把有效 BW 或 `AI` 移過 ridge，≥12 個月窗內上界是否被工程抵銷。

---

## 7. 本輪寫入／不寫入

寫入：本生成卡入 Drive `work/`（fileId 見標頭 EMITS，上傳後回填）。
不寫入：FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（§3 L5［P］仍＝已生成；不入 §1）；matrix 正本 `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`；§2／§4／§5；INDEX.json；ARCH_dead。禁止新建同名正本。狀態欄對齊屬測試一之後 session。
