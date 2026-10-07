<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | NOTE: 只做 L10-P 測一。不改測 L10-A／L10-I。不恢復 L11-P。不改正本 | CONSUMES: 1VEC5j3IyGocvJNgEDSm6VI3lowXPB0bh；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi；1xdEw0NdnY1nsv_LKFiFNAZgPoyxv3oKx | EMITS: SELF -->
# L10-P 測一｜B 端實讀（端側能量或殼溫門檻 × 留端 vs 回雲之功能類；次為 10-K／10-Q 同檔分列）

**角色：** ANALYST@GK　**日期：** 2026-09-30　**格：** L10-P（分發與中介：端側能量預算決定哪些中介功能留在端、哪些必回雲）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先同一公開來源並列「端側能量或殼溫／降頻門檻」與「因此留在端側 vs 回雲之功能類或請求占比」；次為 10-K／10-Q／20-F 同檔分列該兩項，且標明裝置類與是否含無線電。**禁止**把 tokens/J 改善或模型大小口號當成已實現留端占比；禁止把對照寫成分潤率、選擇畫面、注意力秒數、資料中心 FLOP/J 或 PUE。不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T、不入 §1。不改測 L10-A／L10-I。不恢復 L11-P（ARCH_dead #3）。不選券。
**原陳述（生成卡 `1VEC5j3IyGocvJNgEDSm6VI3lowXPB0bh`；種子 ARCH_3h §3.29 L10-P，`1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj`）：** 端側能量預算（電池與散熱上限）決定哪些中介功能可在端側完成、哪些必回雲。B 端載體甲-21 之兩項缺輸入，3h 已歸 (a)。錯價只在把端側覆蓋率讀成與能量預算無關的產品選擇。
**對照式（生成用，非正式載入）：** \(E_{\mathrm{on}} \le E_{\mathrm{budget}}\)（電池可撥焦耳，且殼溫路徑 \(\le T_{\mathrm{cap}}\)）。功能 \(f\) 留端僅當 \(E(f)+E_{\mathrm{radio,avoided}}\) 落在預算內；否則必回雲。本輪不把論文 tokens/J 改善當成已實現留端占比，不把機器人機載 GPU 排水當成手機中介，不把資料中心 FLOP/J 底板改寫成端側預算。不寫 H1。
**否決觸發（生成卡寫給本輪）：** (1) 實讀後無法並列端側能量或殼溫門檻與留端 vs 回雲之功能類，只剩 tokens/J 或模型大小口號；或 (2) 可運作對照只能寫成分潤率或選擇畫面（滑回 L10-A／L10-I）；或 (3) 可運作對照只能寫成注意力秒數、資料中心 FLOP/J 或 PUE（滑向 L11-P／L7-P／L2-P）；或 (4) 公開層已穩定可拒絕「能量預算綁定留端／回雲」——例如同來源顯示分流由能力或隱私決定、能量項不改功能類。
**領域最近公開（§7-10）：** Zou 等，EnerInfer，arXiv `2606.23001`（v1 2026-06-22；v2 摘要 2026-06-24，仍為端側頻率／熱切換，本輪全文讀 v1 HTML）；Saad-Falcon 等，*Intelligence per Watt*，arXiv `2511.07885`（HTML 檢索 2026-09-30；生成卡頁面日期 2026-09-09）；Microsoft Research 卸載推論網誌（生成卡檢索頁面日期 2026-09-24）。下一官方檢查點＝任一美股可交易、出貨端側裝置或中介客戶端之主體於 10-K／10-Q／20-F **同檔**分列（i）端側推論之能量或殼溫／降頻門檻與（ii）因此留在端側 vs 回雲之功能類或請求占比，且標明裝置類與是否含無線電。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/ `1CEprzXwFF4FA0HRHDe9prm2cIYRLB12z`：1 筆、無前綴、無 `DONE_`。L10-P 生成 `1VEC5j3IyGocvJNgEDSm6VI3lowXPB0bh`（11955 B，2026-09-30T09:36:21Z）。本輪上傳前 exact_name `20260930_L10-P_test1_GK.md` 空；檔名檢索無 `L10-P_test1`。
- query/ `1OPi79EP1MtU8dfSGJhzA8et8Grliaf8w`：ARCH_dead `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`；ARCH_matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`（3543 B，2026-09-30T09:18:30Z；L10［P］＝已生成；L10［A］＝已生成；L10［I］＝已生成；L11［P］＝已殺）；INDEX `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`（11603 B，同日）；MECH `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-09-30T09:30:55Z role SCOUT；synced CHARTER `12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi`；synced FUNNEL `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`）。
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-09-30；§1 無 L10-P；§3 L10［P］仍＝已生成）。
- work 主動維護：work 僅此 1 筆，未吸收（未入 §1、測一未做），不建 `DONE_`。生成卡標頭 `EMITS: SELF`，與慣例相符，不發 HEALTH。無疑似重複。

---

## 終態

**測一不通過（殼溫門檻與端側／卸載功率可觀測；留端 vs 回雲之功能類不可並列）｜不進 T。** 否決 (1) 觸發。指名 B 端在公開論文**未成立**：EnerInfer v1 HTML 同一來源有殼溫例示上界 \(42^\circ\mathrm{C}\)（峰值頻率下 100 s 超 \(42^\circ\mathrm{C}\)、200 s 超 \(45^\circ\mathrm{C}\)）與預設端側功率對雲卸載功率 >138%（Huawei Mate 70 Pro、文字潤色；多出功率在 NPU 與記憶體；無線電未標），但控制只在端側切 NPU／DDR 頻率，雲卸載是功率基線、不是運行時路由。無功能類或請求占比表。arXiv `2511.07885` 有本地／雲路由與能量降幅（WildChat 表 8、NaturalReasoning 表 9），分流鍵是模型大小／精度以匹配雲端 SOTA，不是電池焦耳或殼溫；無線電未含。機制（能量預算綁定留端／回雲）未被本輪實讀寫成可重算對照。

不進 T：10-K 次級路徑**未成立**——AAPL 10-K 期 2025-09-27 acc `0000320193-25-000079`（可見層申報日 2025-10-31）本輪可見層無 joule／殼溫／降頻門檻與留端占比同檔分列；不把「可見層未見」寫成全檔不存在。\(E_{\mathrm{on}}\le E_{\mathrm{budget}}\) 不是單一可單位化連續參數可寫 H1 倍數窗：殼溫是舒適例示不是守恆底板，降頻可把功能留在端（R2／R3），甲-21 兩項缺輸入本輪未補。無 H1。§7-4 三題本輪不答。

與相鄰格：對照不是分潤恆等（L10-A 未改測）、不是選擇畫面（L10-I 未改測）、不是注意力秒數（L11-P 未恢復）、不是資料中心每 FLOP 焦耳（L7-P 未改寫）、不是設施 PUE（L2-P 未改寫）。裝置與論文係數只作揭露載體，不選券。tokens/J 改善 38% **不進通過條件**。MSR 機器人電池排水 **不進通過條件**。

---

## A. 指名 B 端：同一公開來源並列殼溫／能量門檻 × 留端 vs 回雲功能類（實讀）

| 源 | URL | 本輪讀到的量 | 並列？ |
|---|---|---|---|
| EnerInfer v1 HTML | https://arxiv.org/html/2606.23001v1 | 殼溫例示 < \(42^\circ\mathrm{C}\)；峰值 100 s／200 s 超 \(42^\circ\mathrm{C}\)／\(45^\circ\mathrm{C}\)。預設端側功率 > 雲卸載 138%，多出在 NPU＋Mem。降頻後 NPU＋Mem 功率 −44%、吞吐仍 >10 token/s、tokens/J +38%。控制＝端側頻率切換與熱預測（MAE \(0.16^\circ\mathrm{C}\)）。作者自標無穩定排序、商用裝置常無元件級功率感測、殼溫依請求到達與熱歷史 | **否**。雲是功率基線，不是「必回雲」功能類。無留端／回雲占比 |
| arXiv `2511.07885` HTML | https://arxiv.org/html/2511.07885 | 表 8 WildChat 能量降幅隨大小門檻約 63.5%（≤4B）至 90.7%（≤120B）；表 9 NaturalReasoning 約 46.3% 至 85.9%。正文混合路由相對批次雲基線能量可降 60–80%。裝置含 M4 Max、iPhone 16 Pro／A18 Pro NPU、雲 GPU。能量＝加速器抽功，不含無線電。殼溫與電池預算缺席 | **否**。分流鍵＝大小／精度匹配雲端 SOTA，能量是後果不是決策項 |
| MSR 卸載推論網誌 | https://www.microsoft.com/en-us/research/blog/offloaded-inference-for-real-world-physical-ai-robotics/ | Jetson Thor 對機器人電池排水至多 160%（或數小時）；圖標 Stretch-3。取捨含網路延遲、頻寬與可用 GPU | **不作 B 端**。機器人操作，不是手機中介功能類 |

缺段（CHARTER §7-2）：甲-21 原文（3h 已標兩項缺輸入、歸 (a)，本輪未取到該檔）；EnerInfer v2 全文（只讀 v2 摘要，摘要仍為端側頻率／熱切換，不把「摘要未寫路由」寫成 v2 全文無路由）；`2511.07885` 表 8–9 以外之附錄功率原始列；AAPL 10-K 可見層以外之附註全文。

---

## B. 次級路徑：10-K 同檔分列

AAPL Form 10-K，財政年度止 2025-09-27，acc `0000320193-25-000079`，https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm 。本輪可見層無 joule、watt、thermal、throttl、殼溫、on-device、Private Cloud Compute、推論能量、請求占比。不把可見層未見寫成全檔不存在。未另讀 20-F。次級路徑未成立，不因此改判通過。

---

## C. 否決檢核

| # | 結果 |
|---|---|
| (1) | **觸發。** 殼溫門檻與端側／卸載功率可觀測；留端 vs 回雲之功能類不可並列。剩 tokens/J 與模型大小門檻 |
| (2) | 未觸發。對照不是分潤率或選擇畫面。不改測 L10-A／L10-I |
| (3) | 未觸發。對照不是注意力秒數、資料中心 FLOP/J 或 PUE。不恢復 L11-P，不改寫 L7-P／L2-P。MSR 排水不進通過條件 |
| (4) | 未觸發為穩定拒絕。`2511.07885` 分流由能力（大小／精度）決定、能量項不改功能類，但是該文未檢驗能量預算綁定後予以拒絕；EnerInfer 能量項只改端側頻率。缺並列 ≠ 機制已被公開層穩定拒絕 |

---

## D. 本輪寫入／不寫入

寫入：本測一入 Drive `work/`（fileId 見上傳回傳；標頭 EMITS＝SELF）。
不寫入：FUNNEL 正本（§3 L10［P］仍＝已生成；不入 §1；不改 L10-A／L10-I）；matrix；INDEX.json；ARCH_dead；ARCH_3h；GRID 快照 `1xdEw0NdnY1nsv_LKFiFNAZgPoyxv3oKx`。禁止新建同名正本。狀態欄對齊屬下一 session。
