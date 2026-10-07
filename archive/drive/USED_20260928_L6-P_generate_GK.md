# L6-P 生成卡｜雲端與基礎設施服務：單卡故障率×N → 有效訓練時數／掛牌時數單調下降
<!-- BY: SCOUT@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | NOTE: 3h L6-P 種子正式生成；不改測 L6-A／L6-I；不重開 C-P1／C-A3／C-A4；不寫 T-15；不改測 L13-P | CONSUMES: 1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi；10aH5MscncgySFaJadvJsX3z0OXviAie_；1Pm249SbDe6OUmA3RXYdqt-O_PrC9pj_z；1MLSGbk8FqWE0tjVvOZzlWnh6WuFLQtNY；1fNjiUcUe9YH12iXl1bWbffhbmEmp3iIr | EMITS: PENDING_UPLOAD -->
**日期：** 2026-09-28　**角色：** SCOUT@GK　**格：** L6-P　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 本輪只產生成卡。不測。不改正本狀態欄（FUNNEL §3／matrix L6［P］仍＝已生成）。不入 §1。B 端只指名可重算欄，不宣稱可分離、不寫 H1。

---

## 0. 本輪範圍

- 種子＝ARCH_3h §3.29 L6-P（`1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj`）：**單卡年故障率×N 決定平均無故障作業時間；N 上升使「有效訓練時數÷掛牌時數」單調下降**。B 端載體（3h 僅指名、未實讀）：業者可用率 SLA；故障率白皮書。
- 生成序：3h 填格為 A→I→P。同層 L6-A 測一部分通過｜不進 T（生成 `10aH5MscncgySFaJadvJsX3z0OXviAie_`；測一 `1Pm249SbDe6OUmA3RXYdqt-O_PrC9pj_z`；指名 RPO 附註≠所需量）。同層 L6-I 測一通過｜不進 T（生成 `1MLSGbk8FqWE0tjVvOZzlWnh6WuFLQtNY`；測一 `1fNjiUcUe9YH12iXl1bWbffhbmEmp3iIr`；可觀測／可並列）。本輪不改測該兩格。
- 3h 重疊標：「~~C-P1~~ 已封存，重疊度未判（恢復前須先給）」。CHARTER §7-3：終端篩選不得在生成階段執行。重疊不構成丟棄；恢復 C-P1 之前須先給重疊度，本輪不恢復。
- 已死／相鄰、機制不同、不得合併、不得重開：
  - **C-P1**（ARCH_dead #11，層標 L5）：死因＝方向翻負／價格不可分離；複查＝營運商揭露 checkpoint 讀取占復原 >50%、儲存分列訓練／推論且訓練側成長不低於 GPU、或非同步 checkpoint 三年採用 <50%。本格是**作業窗內故障事件隨 N 的守恆加總**與 ETTR，不是 checkpoint I/O 的儲存產品價格。
  - **C-A3**（#5，L6）：折舊年限／減損。本格不是會計年限。
  - **C-A4**（#4，L13）：`k`／窗。本格不是續約單價。
  - **T-15 CoreWeave 空方**：FUNNEL §2／INDEX 標 **委託資本外**，非殺。本格可把該主體白皮書／SLA／10-Q 當揭露載體指名；**不得改寫成空方論點，不得選券。**
  - **L6-A**：`R＝已簽約未交付／已交付` 領先營收。本格不是交付落差比。
  - **L6-I**：backlog **品質**（集中度、替代選項）。本格不是對手方信用。
  - **L13-P**（3h 原文）：GPU 實體壽命受**熱循環次數**封頂，與會計年限無關。本格是**作業窗 MTTF／ETTR**，不是資產報廢壽命。本輪不生成、不改測 L13-P。
- CHARTER §7-10：領域最近公開＝Kokolis et al. HPCA 2025／arXiv `2410.21680`（11 個月、>1.5×10⁸ A100 GPU-h；html v2 2026-08 仍在）；Cui et al. Delta「Story of Two GPUs」arXiv `2503.11901` v4（2025-12-10；1,056 張 A100／H100、2.5 年、1.17×10⁷ GPU-h）；Llama 3 405B 54 日快照（16,384 H100；419 次非預期中斷）；Epoch AI「Hardware failures won’t limit AI scaling」（對該快照反解約 50,000 GPU-h／中斷）；Cedana 二次摘 2026-08-21；Data Gravity 二次摘 2026-09-21（置換率≠中斷率）；CoreWeave 可靠度文 2026-05-21；SemiAnalysis ClusterMAX 3.0 2026-09-23；AWS Compute SLA（EC2 單實例 99.5%／多 AZ 99.99%）。下一官方檢查點＝任一美股可交易雲端／HPC 租賃主體於 10-K／10-Q／20-F **同檔**分列（i）掛牌或計費 GPU-h 與（ii）有效訓練時數或 job-level MTTF／ETTR，且至少標明作業規模 N 或可反解 N；或同檔把實現可用率與合約 SLA 對同一訓練作業窗並列。

---

## 1. 落差一句（生成物）

市場把雲端／基礎設施服務可靠度讀成「單卡年故障率低」或「合約 SLA 三個九」。種子主張：同步訓練作業在任一卡停則整份停，作業 MTTF ≈ 單卡 MTTF／N；N 上升使有效訓練時數÷掛牌時數單調下降。錯價只在把單卡可靠度或實例 SLA 讀成大 N 作業的有效時數。L6-A／L6-I 已在交付比與 backlog 品質上測完不進 T；本格 B 端不是那兩列。C-P1 不恢復。T-15 不進本格。

---

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆型故障加總（獨立假設下 MTTF ∝ 1／N）＋作業有效時數比；不是交付時序恆等、不是逆選擇、不是熱循環壽命 |
| 選擇者 | 作業跨卡數 N；同步集體通訊是否把單點故障升級為整份重啟；復原／checkpoint 時長 |
| 可見端 | 公開叢集論文之 MTTF／ETTR×N；業者 SLA（實例／區域可用率）；故障率白皮書或訓練後記之中斷次數 |
| 指名不可見端 | 單一可單位化連續參數把「ETTR(N)」寫成 H1 倍數窗；10-Q 把計費 GPU-h 與有效訓練時數同檔分列 |
| 主張 | N 上升 ⇒ 作業 MTTF 下降 ⇒ ETTR＝有效訓練時數／掛牌時數單調下降（復原時間不隨 N 等比縮短時） |
| 表達工具型態（只指名，不選券） | 已上市、美股可交易、有公開 SLA 或訓練可靠度揭露之雲端／HPC 租賃主體。不選券 |
| 重疊 | C-P1 checkpoint 儲存；L13-P 熱循環壽命；L6-A 交付比；L6-I backlog 品質。重疊不構成丟棄 |

恆等式（生成用，非正式載入）：

`λ_job(N) ≈ N × λ_card`　（獨立假設；相關故障只會使 λ_job 更大）

`MTTF_job(N) ≈ 1 / λ_job(N)`

`ETTR(N) = T_effective / T_billed ≈ MTTF_job / (MTTF_job + T_recover)`

種子：`∂ETTR/∂N < 0`（`T_recover` 不隨 N 同比下降時）。**不把單卡年故障率當成作業可靠度。不把實例 SLA 可用率當成 ETTR。不把卡置換率當成作業中斷率。**

---

## 3. 已 fetch 之公開錨（URL；非完整 B 端實讀）

以下只證明「指名載體存在且近期仍更新、可並列 N 與 MTTF／中斷次數或 SLA」。**不宣稱已完成測試一，不宣稱可單位化，不宣稱市場錯價。** 數字多為論文／二次摘，測試一須對原論文表與原 SLA 定義實讀。

1. Kokolis et al., *Revisiting Reliability in Large-Scale Machine Learning Research Clusters*，HPCA 2025／arXiv `2410.21680`：兩座多租戶研究叢集、11 個月、約 400 萬份作業、>1.5×10⁸ A100 GPU-h。實測 8-GPU 作業 MTTF 47.7 日、1,024-GPU 作業 MTTF 7.9 時；擬合投影 16,384-GPU 1.8 時、131,072-GPU 0.23 時。文內定義／估計 ETTR。https://arxiv.org/html/2410.21680v2　https://ai.meta.com/research/publications/revisiting-reliability-in-large-scale-machine-learning-research-clusters/
2. Llama 3 405B 預訓練快照（至多 16,384 H100、54 日）：466 次作業中斷、419 次非預期；GPU／HBM3 合計過半；團隊稱有效訓練時間 >90%；多數由自動化處理。https://ai.meta.com/research/publications/the-llama-3-herd-of-models/
3. Epoch AI 對該快照反解：約每 50,000 GPU-h 一次中斷；外推 100,000 GPU 叢集約每 30 分一次。結論寫「checkpoint 不會限制近中期規模」——是種子單調命題的具名反方，不是本格通過。https://epoch.ai/blog/hardware-failures-wont-limit-ai-scaling
4. Cui et al., *Story of Two GPUs*，arXiv `2503.11901` v4（2025-12-10）：Delta 1,056 張 A100／H100、2.5 年、1.17×10⁷ GPU-h。H100 不可校正記憶體錯誤之每卡 MTBE 劣於 A100 約 3.2×；節點可用率約 A100 99.4%、H100 99.3%；投影維持 99.9% 作業可用率需約 5% 超配。https://arxiv.org/abs/2503.11901
5. CoreWeave 部落格 2026-05-21 引用同一 MTTF 表（1,024 → 7.9 時；16,384 → 1.8 時）；另文稱內部 1,024-GPU 測得 MTTF 3.66 日、ETTR 97.5%（行銷測，非 10-Q）。https://www.coreweave.com/blog/why-distributed-training-fails-at-scale
6. AWS Compute SLA：單 EC2 實例月可用率承諾 99.5%；跨至少兩 AZ 之區域級 99.99%。定義是實例／區域「Unavailable」，不是訓練作業 ETTR，也不是 MTTF(N)。https://aws.amazon.com/compute/sla/
7. CoreWeave 公開 SLA 頁目前可見者為物件儲存月可用率 ≥99.9% 與 Observe SLO；**未在本輪找到**與訓練作業 ETTR 或按 N 分列之計算 SLA 正文。https://docs.coreweave.com/policies/terms-of-service/coreweave-ai-object-storage-policy
8. 二次對帳（不得代替原表）：Cedana 2026-08-21 重排 Kokolis 表；Data Gravity 2026-09-21 指出 Llama 3「9%/年」常被誤讀——該文把 NCSA Delta **實體置換**標成 A100 約 0.36%/年、H100 約 0.82%/年，與作業中斷率不是同一量。https://cedana.com/blog/gpu-failure-rate-fleet-size/　https://www.datagravity.dev/p/how-long-does-a-gpu-last

缺段（CHARTER §7-2）：任一美股雲／HPC 主體 10-Q 之 ETTR 或「有效訓練時數／計費時數」表；CRWV／AMZN／MSFT／GOOGL 訓練作業 SLA 原定義是否含 N；Kokolis／Delta 原論文之完整誤差條與故障分類表。測試一不得把部落格 MTTF 或實例 SLA 當成已從申報附註重算。

---

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | 3h 指名 B 端是「SLA＋故障率白皮書」；公開 SLA 是實例／區域可用率，**不是** ETTR(N)。白皮書／論文不是 10-Q 科目 | AWS Compute SLA；CRWV 儲存 SLA；Kokolis 為研究叢集論文 | 測試一可能停在 (a)：所需量不是所讀之量（比照 L6-A「指名 RPO ≠ 所需量」） |
| R2 | Epoch AI：復原／checkpoint 足夠快則硬體故障**不限制**規模；ETTR 下降可被 `T_recover` 壓住，單調命題不自動變成可捕捉落差 | Epoch AI 2024 文；Llama 3 >90% 有效訓練時間 | 機制成立 ≠ 未定價且可捕捉（§7-4） |
| R3 | 作業中斷 ≠ 卡故障 ≠ 卡置換。Llama 3 419 次含軟體／網路；Delta 置換率遠低於中斷率 | Llama 3 表；Data Gravity 2026-09-21；Delta 論文 | `λ_card` 量綱未釘則 `N×λ` 不可重算 |
| R4 | 相關故障（機架供電、同一批 HBM）使獨立假設失效；方向仍可能下降，但係數不是 N | Factryze MTBF Math；mlsysbook 附錄 | 無單一可單位化連續參數 |
| R5 | 滑向 checkpoint 儲存營收＝恢復 C-P1；滑向熱循環壽命＝改測 L13-P；滑向空方選券＝違反 T-15 | ARCH_dead #11；3h L13-P；FUNNEL §2 | 表達點選錯＝換格，不是本格通過 |
| R6 | 超配 5%、熱備、checkpointless 把 ETTR 缺口內化成業者成本，不出現在公開 SLA 或毛利分列 | Delta 5% 超配投影；AWS HyperPod／SemiAnalysis 復原時延對照 | 可見端停在工程論文，申報層無對照 |

種子仍可能在「同一公開來源並列 N 與 MTTF 或 ETTR、且定義釘死為作業中斷而非置換」上寫成可重算對照。實例 SLA 百分比本身不夠。

---

## 5. SCOUT 裁決

**生成 L6-P 並留。** 不進 T。不改測 L6-A／L6-I。不恢復 C-P1。不重開 C-A3／C-A4。不把 T-15 改寫成空方。不生成、不改測 L13-P。下一動作＝ANALYST@GK 對本格做測試一。

理由（只到殺／留／生成）：
- 楔可陳述，層正確（雲端與基礎設施服務／物理守恆），與 L6-A 交付比、L6-I 逆選擇、L13-P 熱循環壽命、C-P1 checkpoint 儲存不同構。
- 3h 已警告與已封存 C-P1 重疊未判；生成階段不得以重疊丟棄，也不得未給重疊度就恢復。
- R1–R4 足夠強，預設風險＝SLA≠ETTR、中斷≠置換、復原把單調下降壓沒、論文不可進 10-Q；不是機制已被否證。
- 終端三題本階段不答（§7-3）。

否決觸發（寫給 ANALYST，不是本輪執行）：
- 實讀後無法並列「N」與「作業 MTTF 或 ETTR」，只剩實例 SLA 百分比與「叢集會壞」一句；或
- 可運作對照只能寫成 checkpoint 讀取占復原／儲存分列（滑回 C-P1）；或
- 可運作對照只能寫成熱循環次數或會計年限（滑向 L13-P）；或
- 可運作對照只能寫成該主體空方或委託資本外論點（滑向 T-15）；或
- 公開層已穩定可拒絕「N 上升而 ETTR 下降仍未被復原／超配吸收」——例如同來源顯示 ETTR 在相關 N 區間不降或上升。

複查觸發器（若日後殺）：任一美股可交易雲端／HPC 租賃主體於 10-K／10-Q／20-F 同檔分列計費或掛牌 GPU-h 與有效訓練時數或 job-level MTTF／ETTR，且標明或可反解作業規模 N；或同檔把實現可用率與合約 SLA 對同一訓練作業窗並列。

---

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：ETTR 或超配／熱備成本能否從 SLA 學分與「可用率」敘事再拆；跨論文加總能否拒絕重複計算同一叢集。
2. 可交易工具：恆等落在美股可交易雲／HPC 主體揭露，而非僅私有實驗室論文或無申報之內部 MTTF。
3. 半衰期：checkpointless／機內容錯一旦把 `T_recover` 壓到作業步長以下，≥12 個月窗內「ETTR 隨 N 下降」是否消失。

---

## 7. 本輪寫入／不寫入

寫入：本生成卡入 Drive `work/`（fileId 見上傳回傳；標頭 EMITS 於上傳前為 PENDING）。
不寫入：FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（§3 L6［P］仍＝已生成；不入 §1；不改 L6-A／L6-I 狀態）；matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`；INDEX.json（8 KB 滿）；ARCH_dead；ARCH_3h（快照不可更新）。禁止新建同名正本。狀態欄對齊屬測試一之後 session。
L6-A／L6-I 測檔本輪不改。
