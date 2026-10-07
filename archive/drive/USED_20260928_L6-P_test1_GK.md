<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1mnY_jhKf-Cut2n6rS46vI0iHHkpRS7KP；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi；1MLSGbk8FqWE0tjVvOZzlWnh6WuFLQtNY；1fNjiUcUe9YH12iXl1bWbffhbmEmp3iIr；10aH5MscncgySFaJadvJsX3z0OXviAie_；1Pm249SbDe6OUmA3RXYdqt-O_PrC9pj_z | EMITS: PENDING_UPLOAD -->
# L6-P 測一｜B 端實讀（公開叢集論文／訓練後記並列 N × 作業 MTTF 或 ETTR；次為 10-Q 同檔計費 GPU-h × 有效訓練時數）

**角色：** ANALYST@GK　**日期：** 2026-09-28　**格：** L6-P（雲端與基礎設施服務：單卡故障率×N → 有效訓練時數／掛牌時數單調下降）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先公開叢集論文／訓練後記中可並列 N 與作業 MTTF 或 ETTR 之**原表／原定義**；次為 10-Q 若同檔出現計費 GPU-h 與有效訓練時數。**禁止**只重讀實例 SLA 百分比、卡置換率、C-P1 checkpoint 儲存、L13-P 熱循環、或 T-15 空方材料。不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T、不入 §1。不改測 L6-A／L6-I。不恢復 C-P1。不生成、不改測 L13-P。不選券。
**原陳述（生成卡 `1mnY_jhKf-Cut2n6rS46vI0iHHkpRS7KP`；種子 3h §3.29）：** 同步訓練作業在任一卡停則整份停，作業 MTTF ≈ 單卡 MTTF／N；N 上升使有效訓練時數÷掛牌時數單調下降。錯價只在把單卡可靠度或實例 SLA 讀成大 N 作業的有效時數。
**對照式（生成用，非正式載入）：** `λ_job(N) ≈ N × λ_card`；`MTTF_job(N) ≈ 1/λ_job(N)`；`ETTR(N) ≈ MTTF_job/(MTTF_job+T_recover)`。種子：`∂ETTR/∂N < 0`（`T_recover` 不隨 N 同比下降時）。本輪不把單卡年故障率當作業可靠度，不把實例 SLA 當 ETTR，不把卡置換率當作業中斷率，不寫 H1。
**否決觸發（生成卡寫給本輪）：** (1) 實讀後無法並列 N 與作業 MTTF 或 ETTR，只剩實例 SLA 百分比與「叢集會壞」一句；或 (2) 可運作對照只能寫成 checkpoint 讀取占復原／儲存分列（滑回 C-P1）；或 (3) 只能寫成熱循環次數或會計年限（滑向 L13-P）；或 (4) 只能寫成該主體空方或委託資本外論點（滑向 T-15）；或 (5) 公開層已穩定可拒絕「N 上升而 ETTR 下降仍未被復原／超配吸收」。
**領域最近公開（§7-10）：** Kokolis et al. HPCA 2025／arXiv `2410.21680`（html v2 仍在；11 個月、>1.5×10⁸ A100 GPU-h）；Cui et al. arXiv `2503.11901` v4（2025-12-10）；Llama 3 405B 快照（arXiv `2407.21783`）；Epoch AI 2024-11-22。下一官方檢查點＝任一美股可交易雲端／HPC 租賃主體於 10-K／10-Q／20-F **同檔**分列（i）掛牌或計費 GPU-h 與（ii）有效訓練時數或 job-level MTTF／ETTR，且至少標明或可反解 N；或同檔把實現可用率與合約 SLA 對同一訓練作業窗並列。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：僅 `20260928_L6-P_generate_GK.md` `1mnY_jhKf-Cut2n6rS46vI0iHHkpRS7KP`（13944 B，2026-09-28T13:07:52Z）。無其他進行中 work 檔。
- query/：ARCH_dead `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`；ARCH_matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`（L6［P］＝已生成）；CHARTER_HIST `1DKg3HUr-zOWw20OmNe1aDpWT_izDwdiT`；INDEX `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`；MECH `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-09-28T13:15:40Z role SCOUT）
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-09-28；§1 無 L6-P；§3 L6［P］＝已生成；L6［A］＝測一部分通過｜不進 T；L6［I］＝測一通過｜不進 T）
- 本輪上傳前 work/ exact_name `20260928_L6-P_test1_GK.md` 空；無內容相近測一
- work 主動維護：L6-P 生成卡未吸收進 FUNNEL／matrix（待本測一後由 SCOUT 對齊狀態欄）。本輪不建 `DONE_`。生成卡標頭仍寫 `EMITS: PENDING_UPLOAD`（實際 fileId＝`1mnY_jhKf-Cut2n6rS46vI0iHHkpRS7KP`）；與既有測一卡慣例相同，不另發 HEALTH、不改原檔。

---

## 終態

**測一通過（可觀測／可並列）｜不進 T。** 指名 B 端在公開叢集論文／訓練後記**成立**：Kokolis et al. HPCA 2025／arXiv `2410.21680` 原文並列作業規模 N 與作業 MTTF（實測 8-GPU 47.7 日、1,024-GPU 7.9 時；擬合投影 16,384-GPU 1.8 時、131,072-GPU 0.23 時），並定義 ETTR＝生產性 runtime／作業牆鐘。Llama 3 405B 原文 Table 5 並列 N＝16,384 H100、54 日快照、466／419 次作業中斷、有效訓練時間 >90%。機制（同步作業 MTTF 隨 N 下降、可重算）未被否證。否決 (1)–(4) 未觸發。否決 (5) 未觸發：MTTF 隨 N 下降被原文寫成與 `∝ 1/N` 相符，但同來源 ETTR 在已觀測窗仍高（Kokolis 最大優先作業約 0.85–0.9；Llama 3 >90%），不能穩定拒絕「下降已被復原吸收」，也不能把單調 ETTR 命題寫成已定價可捕捉落差。

不進 T：10-Q 次級路徑**未成立**——CRWV 10-Q 期 2026-06-30 acc `0001769628-26-000366` 同檔檢索 MTTF／ETTR／GPU-hour／effective training／billed hours 皆缺；無可把計費 GPU-h 與有效訓練時數寫進申報科目。ETTR(N) 不是單一可單位化連續參數可寫 H1 倍數窗：`T_recover`、checkpoint 間隔、超配把缺口內化（R2／R6）。無 H1。§7-4 三題本輪不答。

與相鄰格：對照不是 checkpoint I/O 佔復原或儲存分列（C-P1 未恢復）；不是熱循環次數或會計年限（L13-P 未改測）；不是交付比（L6-A 未改測）；不是 backlog 品質（L6-I 未改測）。CRWV／論文叢集只作揭露載體，不寫空方（T-15 地位未動）。Delta 置換率與節點可用率**不進通過條件**（置換 ≠ 作業中斷）。實例 SLA 百分比**不進通過條件**。

---

## A. 指名 B 端：論文／訓練後記並列 N × 作業 MTTF 或 ETTR（實讀）

| 源 | URL | 本輪讀到的量 |
|---|---|---|
| Kokolis et al., *Revisiting Reliability in Large-Scale Machine Learning Research Clusters*，HPCA 2025 pp.1259–1274／arXiv `2410.21680` html v2 | https://arxiv.org/html/2410.21680v2　https://arxiv.org/pdf/2410.21680　https://ai.meta.com/research/publications/revisiting-reliability-in-large-scale-machine-learning-research-clusters/ | **範圍：** 兩座多租戶研究叢集 RSC-1≈16k GPU、RSC-2≈8k GPU；11 個月；約 400 萬份作業；>1.5×10⁸ A100 GPU-h。**定義（原文）：** MTTF＝量測系統時間÷故障次數；ETTR＝一 job run 之生產性 runtime ÷ 可用牆鐘（含排隊與非生產 runtime；刻意忽略 userspace 故障以聚焦叢集穩定）。**Fig.7／正文：** 8-GPU 作業 MTTF **47.7 日**；1,024-GPU 作業 MTTF **7.9 時**（約低兩個數量級）。「Empirically, hardware reliability shrinks inversely proportional to the number of GPUs, with more consistent trends starting at 32 GPUs。」理論 `MTTF ∝ 1/N_gpus`，`MTTF=(N_nodes r_f)^{-1}`；`r_f` 用 >128-GPU 作業之故障與 node-days。RSC-1 `r_f≈6.50`／千 node-day；RSC-2 `≈2.34`。**投影（非實測）：** 16,384-GPU **1.8 時**；131,072-GPU **0.23 時**。Observation 8：4k 規模 MTTF 已約 10 時。相關故障存在（3–5% 硬體故障共現；PCIe 與 XID 79 高共現）但不推翻方向。ETTR：最大優先長作業估計約 0.85–0.9；12k-GPU 投影視 checkpoint 寫入開銷與重啟開銷而變 |
| Llama 3 405B 預訓練快照，*The Llama 3 Herd of Models*，arXiv `2407.21783` | https://arxiv.org/html/2407.21783　https://arxiv.org/pdf/2407.21783　https://ai.meta.com/research/publications/the-llama-3-herd-of-models/ | **N＝16,384** H100 80GB。54 日快照：作業中斷 **466**＝計畫 **47**＋非預期 **419**。原文：「the synchronous nature of training makes it less fault-tolerant—a single GPU failure may require a restart of the entire job。」有效訓練時間＝有用訓練時間／經過時間，**>90%**；需大幅人工介入僅 3 次。Table 5（非預期根因，原文計數）：Faulty GPU 148（30.1%）；GPU HBM3 72（17.2%）；Software Bug 54（12.9%）；Network Switch/Cable 35（8.4%）；Host Maintenance 32（7.6%）；GPU SRAM 19（4.5%）；GPU System Processor 17（4.1%）；其餘 <2%。GPU 類合計原文稱 **58.7%**；約 78% 為確認或疑似硬體。平均非預期中斷間隔＝54×24／419 ≈ **3.1 時／次**（作業層，不是單卡年故障率） |

**單位核對（非正式載入；只證明可並列，不是 H1）：**

| 來源 | N（作業跨卡） | 作業層結果 | 實測／投影 | 與種子 |
|---|---|---|---|---|
| Kokolis Fig.7 | 8 | MTTF 47.7 日 | 實測 | 基準 |
| Kokolis Fig.7 | 1,024 | MTTF 7.9 時 | 實測 | 下降 |
| Kokolis 擬合 | 16,384 | MTTF 1.8 時 | 投影 | 下降 |
| Kokolis 擬合 | 131,072 | MTTF 0.23 時 | 投影 | 下降 |
| Llama 3 Table 5 | 16,384 | 419 非預期／54 日 ≈ 3.1 時／次；有效訓練時間 >90% | 實測快照 | MTTF 下降方向同；ETTR 仍高 |

Llama 3 的 3.1 時／次與 Kokolis 對 16k 的 1.8 時投影同數量級，定義不同（Llama＝全部非預期中斷含軟體／網路／維護；Kokolis MTTF 擬合自硬體／node 故障率），不得加總或視為同一係數。

---

## B. 次級路徑與相鄰源：不得改寫本格通過條件

| 源 | URL | 本輪讀到的量 | 本格用法 |
|---|---|---|---|
| CRWV 10-Q 期 2026-06-30 acc `0001769628-26-000366` | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/0001769628-26-000366.txt | 同檔全文檢索：**MTTF、ETTR、GPU-hour(s)、effective training、billed hours、job-level 皆 ABSENT**。有營收／RPO／集中度（屬 L6-I 已測量），無計費 GPU-h 與有效訓練時數並列 | 次級路徑不成立。不把 RPO 或 MW 當 ETTR |
| Epoch AI, *Hardware failures won’t limit AI scaling*，2024-11-22 | https://epoch.ai/blog/hardware-failures-wont-limit-ai-scaling　https://epoch.ai/publications/hardware-failures-wont-limit-ai-scaling | 對 Llama 快照反解：16,384×54 日 ≈ 880,000 GPU-day／419 ≈ **50,000 GPU-h／中斷**。結論：近中期 checkpoint **不限制**規模；估該次訓練 checkpoint＋復原約 **2.1%** 時間。100,000 GPU 叢集約每 30 分一次中斷（線性外推） | **具名反方（R2）**，不是通過條件。證明 `T_recover` 可把 MTTF 下降與 ETTR 缺口分開 |
| Cui et al., *Story of Two GPUs*，arXiv `2503.11901` v4（2025-12-10） | https://arxiv.org/abs/2503.11901　https://arxiv.org/html/2503.11901 | Delta：1,056 GPU（448 A100＋608 H100）；合計 1.17×10⁷ GPU-h。A100 不可校正記憶體每卡 MTBE 283,271 時 vs H100 88,768 時（約 3.2×）；節點可用率約 A100 99.4%、H100 99.3%；A100 置換 4／895 日、H100 置換 2／146 日；投影 99.9% 作業可用率約需 **5% 超配** | **不進通過條件。** 這是卡／節點 MTBE 與置換，不是作業 MTTF(N) 序列。置換率禁止當本格通過量（生成卡 R3） |

---

## C. 本輪明確不讀、不引用為通過條件

- AWS Compute SLA 單實例 99.5%／多 AZ 99.99%，及任何實例／區域「Unavailable」百分比（所需量是作業 ETTR(N)，不是實例 SLA）。
- CoreWeave 物件儲存 SLA、Observe SLO、2026-05-21 部落格內部 1,024-GPU MTTF 3.66 日／ETTR 97.5%（行銷測，非原論文表、非 10-Q）。
- Cedana／Data Gravity 二次摘與「9%/年」誤讀；Delta 實體置換率（A100≈0.36%/年、H100≈0.82%/年量級）——置換 ≠ 作業中斷。
- Checkpoint 讀取佔復原、訓練／推論儲存分列（C-P1）。
- GPU 熱循環次數、會計折舊年限（L13-P／C-A3）。
- 已簽約未交付／已交付比（L6-A）；RPO×集中度（L6-I）。
- 把 CRWV 或任何雲／HPC 主體寫成空方或選券（T-15）。
- 把 Kokolis 投影與 Llama 3 快照加總成單一 `λ_card`。
- 把節點可用率 99.3–99.4% 讀成 ETTR。

---

## 對 R1–R6 之測一處分（不寫 H1）

| # | 反方 | 本輪 |
|---|---|---|
| R1 | 公開 SLA 是實例／區域可用率，不是 ETTR(N)；白皮書不是 10-Q | **部分成立、未否決可並列。** 通過條件改走論文原表，不走 SLA。10-Q 次級路徑確認缺科目。可觀測在論文層成立，申報層不成立 |
| R2 | Epoch：復原／checkpoint 足夠快則硬體故障不限制規模 | **成立為讀法衝突。** Llama 3 在 N＝16,384 仍 >90% 有效訓練時間；Epoch 估 2.1% 損失。MTTF 下降 ≠ ETTR 單調下降未被吸收。機制成立 ≠ 未定價且可捕捉（§7-4） |
| R3 | 作業中斷 ≠ 卡故障 ≠ 卡置換 | **遵守。** 通過條件只用作業 MTTF／作業中斷次數×N。Delta 置換與 MTBE 只標邊界 |
| R4 | 相關故障使獨立假設 `N×λ` 係數不是 N | **未推翻方向。** Kokolis 自報共現 3–5%，仍寫經驗 MTTF 自 32-GPU 起與 `1/N` 相符。係數不可釘成單一連續參數 |
| R5 | 滑向 C-P1／L13-P／T-15＝換格 | **未滑。** 通過條件只用 N×作業 MTTF／ETTR 定義。未寫儲存營收、未寫熱循環、未寫空方、未選券 |
| R6 | 超配／熱備／checkpointless 把缺口內化成業者成本 | **成立到單位化失敗。** Delta 5% 超配投影與 Kokolis ETTR 對 checkpoint 開銷的敏感度，說明缺口可被成本吸收且不出現在 10-Q 科目 |

否決 (1) 未觸發：Kokolis 原文＋Llama 3 Table 5 已並列 N 與作業層 MTTF／中斷／有效訓練時間，不是只剩 SLA。(2)(3)(4) 未觸發。(5) 未觸發：ETTR 在已觀測 N 未升、也未被證明「穩定不降」；同時高 ETTR 與 Epoch 反方使單調可捕捉命題不定。

複查觸發器（若日後殺，沿用生成卡）：任一美股可交易雲端／HPC 租賃主體於 10-K／10-Q／20-F 同檔分列計費或掛牌 GPU-h 與有效訓練時數或 job-level MTTF／ETTR，且標明或可反解作業規模 N；或同檔把實現可用率與合約 SLA 對同一訓練作業窗並列。

---

## 本輪寫入／不寫入

寫入：本測一卡入 Drive `work/`（fileId 見上傳回傳；標頭 EMITS 於上傳前為 PENDING）。
不寫入：FUNNEL 正本、matrix、INDEX、ARCH_dead、ARCH_3h、CHARTER。不建 `DONE_`。狀態欄對齊＝下一 session SCOUT@GK。
L6-A／L6-I 測一終態不改。C-P1 不恢復。L13-P 不改測。T-15 不寫。C-A3／C-A4 不重開。
