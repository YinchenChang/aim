<!-- BY: ANALYST@GK | MODEL: Grok 4.7【自報】 | CHARTER: AIM-C1.1 | NOTE: 只做 L15-I 測一。不改已入 §1 之 L15-A／L15-P／L14-P／L14-A／L14-I。不恢復 L11-P／L8-P／L9-P。不寫 T。τ／s 不得用本卡補定義。不改正本 | CONSUMES: 10CY4GNXIPHgLJCQrqX82WW_4zhU_jc-M；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h | EMITS: SELF -->
# L15-I 測一｜B 端實讀（出站費率 × 保留期；權利型態句）

**角色：** ANALYST@GK　**日期：** 2026-10-07　**格：** L15-I（基礎設施軟體與資料：遙測出站取用權）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先同一條款頁或同一 10-K／10-Q 並列出站費率與保留期，並標明取用權是結構性計價還是可行使之合約權利。**禁止**把所有權條款、方案保留天數、BYOC 報導或 Data Act 日期當成型態已判定；禁止把對照寫成使用量×有效單價、分析師人數×每人每日秒數、雲層出站／切換貸項，或清醒秒數／標註分鐘／核可工時；禁止用本卡補 τ 或 `s` 的定義。不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T、不入 §1。不改已入 §1 之 L15-A／L15-P／L14-P／L14-A／L14-I。不恢復 L11-P／L8-P／L9-P。不選券。
**原陳述（生成卡 `10CY4GNXIPHgLJCQrqX82WW_4zhU_jc-M`；種子 ARCH_3h §3.29 L15-I，`1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj`）：** 遙測資料由客戶產生、由供應商儲存，出站成本使取用權為結構性而非合約性。B 端載體僅指名：出站費率；資料保留期條款。重疊＝種子（法定驅動型需求），型態不同。本輪種子原文已讀到該列。
**對照式（生成用，非正式載入）：** 權利型態（結構性／合約性）。結構性＝離開供應商索引或自訂目的地要再付一筆隨位元組變動的出站或掃描費，且該費不因所有權條款而消失。合約性＝同一頁寫明客戶可不付該計量費而取回或轉出。只公布所有權，或只公布保留天數，都判不出型態。不寫 H1。τ／`s` 不在本式補定義。
**否決觸發（生成卡寫給本輪）：** (1) 實讀後無法在同一條款頁或同一 10-K／10-Q 並列出站費率與保留期，只剩所有權條款、方案天數或 BYOC 報導；或 (2) 可運作對照只能寫成使用量×有效單價（滑回 L15-A）；或 (3) 可運作對照只能寫成分析師人數×每人每日秒數（滑回 L15-P）；或 (4) 可運作對照只能寫成雲層出站／切換貸項或 Data Act 切換費（滑入 L5-I 或法定種子）；或 (5) 可運作對照只能寫成清醒秒數／標註分鐘／核可工時（重開 L11-P／L8-P／L9-P）；或 (6) 公開層已穩定可拒絕「出站成本使取用權為結構性」——同頁寫明客戶可不付計量出站而取回，且該句不依賴方案外之再水合或自訂目的地費。
**領域最近公開（§7-10）：** Datadog 日誌價目頁（無 as-of；自訂目的地轉送起價 \\( \\$0.25 \\)／GB outbound；轉 S3／GCS／Azure 含在 \\( \\$0.10 \\)／GB 擷取；再水合掃描 \\( \\$0.10 \\)／壓縮 GB）。保留期文件無更新日期。EULA PDF 檔名 `Datadog_EULA_08072023`（正文抽取未見獨立日期行）。DASH BYOC 報導 2026-06-11。Snowflake OpenTelemetry 博客 2026-09-29。Data Act 第 29 條次級閱讀（Springlex；官方 HTML 本輪 503）：2027-01-12 起不得收切換費。Datadog 10-K 期 2025-12-31，acc `0001628280-26-008819`，申報 2026-02-18。10-Q 期 2026-06-30，acc `0001628280-26-054458`，申報 2026-08-06；htm 直讀被拒。下一官方檢查點＝任一已上市基礎設施軟體主體之條款頁或 10-K／10-Q，同頁並列客戶遙測之出站費率與保留期，並標明取用權是結構性計價還是可行使之合約權利。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/ `1CEprzXwFF4FA0HRHDe9prm2cIYRLB12z`：1 筆、無前綴、無 `DONE_`。L15-I 生成 `10CY4GNXIPHgLJCQrqX82WW_4zhU_jc-M`（13992 B，2026-10-07T10:57:10Z）。本輪上傳前 exact_name `20261007_L15-I_test1_GK.md` 空。
- inbox_GK `1ZbILrSDyO71BiAS8yV_Ccx9W_WUKDm-S`：空。
- query/ `1OPi79EP1MtU8dfSGJhzA8et8Grliaf8w`：5 筆。ARCH_dead `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`；ARCH_matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`（7310 B，2026-10-07T10:52:25Z；本輪未讀全文）；INDEX `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`（18616 B，同日；本輪未讀全文）；CHARTER_HIST `1DKg3HUr-zOWw20OmNe1aDpWT_izDwdiT`；MECH `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-10-07T10:58:46Z role SCOUT；synced CHARTER `12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi`；synced FUNNEL `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`）。
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-10-07，8327 B）：§1 已含 L15-A＝測一不通過｜不進 T、L15-P＝測一不通過｜不進 T、L14-P／L14-A／L14-I＝測一不通過｜不進 T。§3：已生成未測 1 格＝L15-I。
- work 主動維護：work 僅此 1 筆，未吸收（未入 §1、測一未做），不建 `DONE_`。生成卡標頭 `EMITS: SELF`，與慣例相符，不發 HEALTH。無疑似重複。

---

## 終態

**測一不通過（所有權條款、方案保留天數、價目分軌與 BYOC 報導可觀測；同一條款頁或同一 10-K／10-Q 之出站費率與保留期，以及權利型態句，不可並列）｜不進 T。** 否決 (1) 觸發。指名 B 端在條款頁與申報層**未成立**：EULA 有客戶擁有 Customer Data，以及終止後至多 30 日、受方案保留期制約之下載，無出站費率。保留期文件有方案天數，無出站費。價目頁有分軌費率與 15 日索引保留，但是列表價、無 as-of、無型態句，不是條款頁，也不是 10-K／10-Q。10-K 有「易於取用、完整粒度、較長期間」之保留敘事與按產品而異之單位計量，無出站費率並列。機制（出站成本使取用權為結構性而非合約性）未被本輪實讀寫成同頁可判定之型態。

不進 T：10-K 摘要層已開、未成立；10-Q 索引已開，htm 直讀被拒，摘要層未見兩欄。不把「同頁未分列」寫成出站成本不存在。權利型態不是單一可單位化連續參數可寫 H1 倍數窗。無 H1。§7-4 三題本輪不答。τ 的數值與 `s` 的定義本輪不補；`ARCH_3c` 未讀。

與相鄰格：對照不是使用量×有效單價（L15-A 未改測）、不是分析師人數×每人每日秒數（L15-P 未改測）、不是席次／員工數、IT÷營收或採購 KPI（L14 未改測）、不是雲層切換費（不滑入 L5-I，不把 2027-01-12 寫成已翻轉）、不是清醒秒數／標註分鐘／核可工時（L11-P／L8-P／L9-P 未恢復）。

---

## A. 指名 B 端：同一公開來源並列出站費率與保留期（實讀）

| 源 | URL | 本輪讀到的量 | 並列？ |
|---|---|---|---|
| Datadog 日誌價目（無 as-of） | https://www.datadoghq.com/pricing/?product=log-management | 擷取起價 \\( \\$0.10 \\)／GB（未壓縮；年約，或隨需同價）。標準索引 15 日保留 \\( \\$1.70 \\)／百萬事件／月（隨需 \\( \\$2.55 \\)）。自訂目的地轉送起價 \\( \\$0.25 \\)／GB outbound、每目的地（未壓縮）。FAQ：轉 S3／GCS／Azure 含在 \\( \\$0.10 \\)／GB 擷取，不另計；其他目的地（外部 SIEM／BI）起價 \\( \\$0.25 \\)／GB outbound。再水合：掃描壓縮日誌 \\( \\$0.10 \\)／壓縮 GB，命中事件再按所選保留期之索引費。Flex：每百萬事件最低 30 日或最低 \\( \\$0.05 \\) | **否（對通過條件）。** 費率與 15 日保留在同一列表價頁，但無型態句、無所有權條款、無 as-of。檔案層轉存含在擷取、自訂目的地另計、再水合是掃描費，一句「出站＝結構性」蓋不住分軌。不是條款頁，不是 10-K／10-Q |
| Datadog 保留期文件（無更新日期） | https://docs.datadoghq.com/data_security/data_retention_periods/ | 日誌保留依方案。APM 索引 span 15 或 30 日、依方案。指標 tags／values 15 個月 | **否。** 天數在，出站費、再水合、轉送、所有權都不在 |
| Datadog EULA，PDF 檔名 `08072023`；正文抽取未見獨立日期行 | https://s3.amazonaws.com/EULA/Datadog_EULA_08072023.pdf | §1.4：雙方之間，客戶擁有 Customer’s Environment 與 Customer Data 之全部權利。§11.5：已付清者，受較短 Service Plan 保留期制約，終止生效日起至多 30 日，得下載終止前已可經服務取用之 Customer Data；此外之終止後使用依價目頁計價；終止後資料於一般作業刪除，且不得留過適用之 Service Plan 保留期 | **否。** 所有權與終止後下載窗在同一份 EULA，出站費率不在。30 日下載不是「可不付計量出站而取回」；該句仍受保留期制約，且其他使用指向價目頁 |
| TechTarget 2026-06-11 | https://www.techtarget.com/it-infrastructure/news/366644272/Datadog-observability-breaks-away-from-SaaS-with-BYOC | DASH 起支援把指標、日誌、追蹤留在客戶控管雲（BYOC）。Omdia／Torsten Volk：自有 OpenTelemetry 發行版使上游收集器只有基本功能，進階功能要 Datadog agent | **否。** 位置轉換≠權利已變合約性。無出站費率、無保留期、無免費取回句。不是條款頁，不是 10-K |
| Snowflake 工程博客 2026-09-29，Deepti Bhutani | https://www.snowflake.com/en/blog/opentelemetry-enterprise-data-asset/ | 遙測不必只住在作業平台；可留成客戶治理的開放資料集 | **否。** 廠商敘事。無出站費率、無保留期、無合約性取回句，不是 10-K |
| EU Data Act 第 29 條（次級；Springlex。官方 HTML 本輪 503，不把次級當條文已核） | https://www.springlex.eu/en/packages/data-act/data-act-regulation/article-29/ | 2024-01-11 至 2027-01-12 得收不超過直接切換成本之減免費；2027-01-12 起資料處理服務提供者不得對切換過程收取切換費 | **不採。** 法定、雲層。3h 已標型態不同。不併入本格，不把日期寫成已翻轉 |

缺段（CHARTER §7-2）：同一條款頁或同一 10-K／10-Q 之出站費率與保留期，以及該頁對「取用權為結構性或合約性」的句子。價目頁的分軌費率不補這個缺段。失敗歸因＝本輪未取得條款頁或申報層同頁兩欄與型態句，不是「出站成本不存在」。複查觸發器＝任一已上市基礎設施軟體主體於條款頁或 10-K／10-Q 同頁分列出站費率與資料保留期，並標明客戶遙測之取用權是結構性計價還是可行使之合約權利。τ／`s` 不由本缺段代替。`ARCH_3c` 未讀。

---

## B. 次級路徑：10-K／10-Q 同檔分列

次級路徑已開，未成立。

Datadog 10-K 期 2025-12-31，acc `0001628280-26-008819`，申報 2026-02-18，`ddog-20251231.htm` 可開。摘要層讀到：提供安全、易於取用、完整粒度、較長期間之資料保留；訂閱可為承諾用量按月攤提、承諾用量隨用隨交、或按月用量；usage 按每產品之單位計量，單位依所交付價值而異。未見出站費率、再水合、BYOC，亦未見與保留敘事並列之出站費率或型態句。

Datadog 10-Q 期 2026-06-30，acc `0001628280-26-054458`，申報 2026-08-06：索引頁已開（`ddog-20260630.htm`）。htm 直讀被拒（SEC 自動化攔截）。browse 摘要層未見 egress、outbound、retention、ownership、rehydration、forwarding。不把摘要層未見寫成全檔不存在。可見索引不足以並列兩欄。

不把可見層未分列寫成全檔不存在。次級路徑未成立，不因此改判通過。

---

## C. 否決檢核

| # | 結果 |
|---|---|
| (1) | **觸發。** 所有權條款、方案天數、價目分軌與 BYOC 報導可觀測；同一條款頁或同一 10-K／10-Q 之出站費率與保留期不可並列，型態句亦不在 |
| (2) | 未觸發。對照不是使用量×有效單價。不改測 L15-A |
| (3) | 未觸發。對照不是分析師人數×每人每日秒數。不改測 L15-P |
| (4) | 未觸發。對照不是雲層出站／切換貸項。Data Act 第 29 條只記相鄰，不採為本格對照。不改測 L5-I |
| (5) | 未觸發。對照不是清醒秒數／標註分鐘／核可工時。不恢復 L11-P／L8-P／L9-P。不改測 L14-P／L14-A／L14-I |
| (6) | 未觸發。沒有同頁寫明客戶可不付計量出站而取回、且該句不依賴再水合或自訂目的地費。EULA §11.5 的 30 日下載受保留期制約，其他終止後使用指向價目頁。檔案層轉存含在擷取價是分軌，不是該拒絕句 |

---

## D. 本輪寫入／不寫入

寫入：本測一入 Drive `work/`（fileId 見上傳回傳；標頭 EMITS＝SELF）。
不寫入：FUNNEL 正本（§3 L15-I 仍＝已生成未測；不入 §1；不改 L15-A／L15-P／L14-P／L14-A／L14-I）；matrix；INDEX.json；ARCH_dead；ARCH_3h；`ARCH_3c`；GRID 快照 `1xdEw0NdnY1nsv_LKFiFNAZgPoyxv3oKx`。禁止新建同名正本。狀態欄對齊屬下一 session。不建 `DONE_`。不寫 T。

**（L15-I 測一結束。）**
