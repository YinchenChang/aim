<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 15rl3xgklpe7vm_DHZN831Rx0IurPhgIb；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；1S8FeDY2MXqTCc20IKToblDC5HFJIFb5U | EMITS: （本檔；Drive work/ 上傳後填 fileId） -->
# L1-I 測一｜B 端實讀（ISO／RTO 互聯原檔能否把 Q_pub 與 Q_commit 同窗對帳；申請成本是否仍近零）

**角色：** ANALYST@GK　**日期：** 2026-09-26　**格：** L1-I（能源與電力：併網佇列序位＝法定／監理性取用權；佔位申請成本近零 → 公開申請量高估真實擬建）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先 ISO／RTO **發電**互聯佇列原檔能否把 `Q_pub` 與 `Q_commit` 同窗對帳，並核對申請成本是否仍近零。**禁止只重讀 LBNL 完成率、撤回總 GW、或大負載資料中心佇列。** 不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T、不入 §1。
**原陳述（生成卡 `15rl3xgklpe7vm_DHZN831Rx0IurPhgIb`）：** 市場把 RTO／ISO 公開之「已申請互聯容量」讀成即將到來的供給。種子主張：佇列序位是法定／監理性取用權；佔位申請成本近零 → 灌水佔位，故 `Q_pub = Q_commit + Q_spec`，公開申請量高估真實擬建。錯價只在把佇列總 GW 譯成可交付供給／需求，而不是把 `δ = Q_pub − Q_commit` 當高估項。
**對照式（生成用）：** `Q_pub(t) = Q_commit(t) + Q_spec(t)`；`δ(t) = Q_pub(t) − Q_commit(t)`。`Q_commit`＝已繳保證金／已證明場址控制／已簽 IA 且未撤回。撤回 MW **不是** `δ` 的替代。本輪不估參數、不寫 H1。
**否決觸發（生成卡寫給本輪）：** (1) 對 ISO／RTO 互聯佇列公開檔實讀後，`Q_commit` 無法從公開項分離，只剩總申請、狀態桶、撤回 MW；或 (2) 可見時序只能寫成叢集／保證金改革後的清場撤回，近零申請成本前提不再成立，且無獨立之高估差；或 (3) 公開層已出現穩定可拒絕之 `δ`，方向與「公開申請高估真實擬建」不可辨，或只能用 L2-I 已測之撤回／歸屬或 T-11 已排除之物理敘事翻號解釋。
**領域最近公開（§7-10）：** PJM Interconnection Queue Update State-Level Statistics（截至 2026-08-03）；PJM Cycle 1 新聞稿 2026-04-29（811／220 GW）與 2026-08-03（715／201.5 GW）；PJM Cycle 1 Application Requirements（IPS 2026-01-26）；ERCOT Senate 說明 2026-07-29（窗 2026-06-30）；ERCOT Capacity-Changes-by-Fuel August 2026（發布 2026-09-08）；ERCOT Planning Guide 2026-07-01＋Fee Schedule（檔名 060125）；MISO GI 頁 D1／M2（D1 自 2026-06-10＝$7,600；M2＝$8,000/MW）。LBNL Queued Up 2026 只作入口圖、**不作本輪通過條件**。下一官方檢查點＝任一 ISO／RTO 互聯佇列公開檔首次把「已繳保證金／已證明場址控制／財務承諾 MW」與「裸申請 MW」分列成可畫至少兩期之差。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/ `1CEprzXwFF4FA0HRHDe9prm2cIYRLB12z`：`20260926_L1-I_generate_GK.md` `15rl3xgklpe7vm_DHZN831Rx0IurPhgIb`（13449 B，2026-09-26T13:02:32Z）；`20260923_HEALTH_CL.md` `1_urT6I7RovcM73D3IBTKGIk6RY1z9nC0`；`20260923_HEALTH_GK.md` `1byQGbjCmIT1orLv51moyAH5xnABFO95e`。exact_name `20260926_L1-I_test1_GK.md` 空。
- query/：`ARCH_dead.md` `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`；`ARCH_matrix.md` `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`（L1［I］＝已生成）；`CHARTER_HIST.md` `1DKg3HUr-zOWw20OmNe1aDpWT_izDwdiT`；`INDEX.json` `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`（無 L1-I 鍵）；`MECH.md` `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-09-26T12:59:15Z role SCOUT）
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-09-26；§1 無 L1-I；§3 L1［I］＝已生成＝3h 快照）
- 3h 快照 `1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj` L1-I B 端僅指名「RTO／ISO 之互聯佇列公開檔」
- work 主動維護：L1-I 生成卡未吸收進 FUNNEL／matrix（待本測一後由 SCOUT 對齊）。HEALTH 兩份非本輪標的。本輪不建 `DONE_`。

---

## 終態

**不通過。不進 T。** 機制（佇列序位＝法定取用權；近零申請成本 → 公開申請高估真實擬建）未被否證。失敗在可觀測性與前提老化——ISO／RTO 原檔給的是總申請、狀態桶（研究中／協議／商轉／撤回）與（ERCOT 規劃月表上）IA 日期＋Financial Security 是／否。**無**與 `Q_pub` 同一宇宙、可加總之「已繳保證金／已證明場址控制／財務承諾 MW」列，故**無**可畫之 `δ(t)`。撤回 GW 與「已簽 IA」存量都不是 `Q_commit`。申請成本：PJM Cycle 1 與 MISO DPP 已不是近零（讀iness $4,000/MW＋研究保證金；M2 $8,000/MW）；ERCOT **發電**入場費仍是千美元級（Fee Schedule：$3,000 FIS 新機／$14,000 ≥10 MW GIM），近零前提在 ERCOT 入場端未死、在 FERC 轄區新循環已改寫。

| 測試項 | 結果 |
|---|---|
| B 端已實讀（非指名；非只讀 LBNL 完成率／撤回總 GW／大負載佇列） | **通過**　PJM 州統計 PDF＋Cycle 1 兩則新聞稿＋Cycle 1 申請要件 PDF；ERCOT Senate PDF＋August 2026 Capacity-Changes xlsx＋Planning Guide＋Fee Schedule；MISO GI 頁 D1／M2 |
| `Q_pub` 與 `Q_commit` 同窗、同宇宙可對帳 | **不通過**　PJM 州統計無保證金／場址／承諾 MW 列。ERCOT Senate 給活躍 462.8 GW，無承諾分列。ERCOT 月表 FS Yes＝71.4 GW 落在 115.1 GW 規劃子集，不是 462.8 GW 的分母 |
| `δ(t)`＝差可成至少兩期時序 | **不通過**　分子定義在公開層不存在。至少兩期之差序列不存在 |
| 撤回 MW 或已簽 IA 存量可否代替 `δ` | **否**　量綱不同。撤回＝結果項；已簽 IA＝比 `Q_commit` 更窄的後段桶 |
| 申請成本是否仍近零 | **分域**　PJM Cycle 1／MISO＝否。ERCOT 發電入場費＝仍近零（千美元）；TSP 財務擔保出現在 IA 之後，不是申請成本 |
| 否決觸發 (1) | **觸發** |
| 否決觸發 (2) | **部分觸發**　PJM／MISO 近零前提已被規則改寫；ERCOT 入場費未改寫。兩邊都無獨立 `δ` |
| 否決觸發 (3) | **未觸發**　`δ` 序列不存在，方向未翻、未用 L2-I 撤回／歸屬或 T-11 物理敘事翻號 |
| 升格 T | **否** |

失效歸因（§7-2）：不是檢索失敗。失敗在量綱——所需量（同窗同宇宙之 `Q_pub` 與 `Q_commit`，外加申請成本檔次時序）不是所讀之量（狀態桶、撤回、已簽協議存量、規劃子集上的 FS 是／否、改革後入場保證金規則）。現況檔名＝上列 work／query。複查觸發器＝生成卡原文（見下）。停。

本格不入 §1。不改正本（對齊屬 SCOUT）。

---

## 已實讀載體

### A. PJM 州統計原檔｜Interconnection Queue Update State-Level Statistics（截至 2026-08-03）

公開總量（自 2020）：申請約 **544 GW**；撤回 **194 GW**；待研究 **231 GW**；Studies Completed & Agreement Tendered **119 GW**（其內撤回 16 GW）；Completed Interconnection Agreement Phase **103 GW**；已商轉 **25 GW**；在建 44 GW；暫停 7 GW；Agreements 27 GW。

燃料表（PJM Total）：Agreements **51.1 GW**／466 件；Studies **231.2 GW**／985 件。州表同結構（燃料 × Agreements／Studies × GW）。

**無**保證金美元／MW、場址控制、Readiness、財務承諾 MW 欄。Agreements／已簽協議階段 ≠ 生成卡定義之 `Q_commit`（保證金＋場址＋已簽 IA 且未撤回之聯集）。禁止用 544−103 或 544−25 造 `δ`。

### B. PJM Cycle 1 原檔｜新聞稿 2026-04-29 與 2026-08-03＋IPS 申請要件 2026-01-26

| 窗 | 件 | 名牌 GW | 條件 |
|---|---|---|---|
| 申請窗關 2026-04-27（04-29 稿） | 811 | 220（新聞稿整數；IPS 2026-06-26 表 Generator Interconnection 220,227 MWE） | 申請＋研究協議、Study Deposit、Readiness Deposit、100% 場址控制 |
| 申請審查完 2026-08-03 | 715 | 201.5 | 「vets … technical information and financial deposits」；first-ready, first-served |

燃料（08-03 稿，進入研究）：氣 99.8 GW／147；儲能 60.0／314；核 17.3／24；光 11.8／117；光＋儲 7.5／37；風 3.9／61。第三方 RTO Insider 記申請審查階段撤回 **26.7 GW**——這是改革清場，不是 `δ`。

入場成本（IPS 原表，非近零）：

| 規模 | Study Deposit |
|---|---|
| 0–20 MW | $75,000 |
| >20–50 | $200,000 |
| >50–100 | $250,000 |
| >100–250 | $300,000 |
| >250–750 | $350,000 |
| >750 | $400,000 |

Study Deposit 單次／Cycle；**10% 不可退**。Readiness Deposit ＝ **$4,000／MW**（取能源 MW 與容量 MW 較大者；200 MW＝$800,000）。場址控制 100%（光 5 acre／MW、風 30 acre／MW、儲能 1 acre／100 MWh 等）。後段：RD2＝網升本 10%−RD1；RD3＝20%−(RD1+RD2)；DP1 關閉後 RD1 全額在險。

08-03 稿另給存量：「Since 2020 … more than 300 GW … over 100 GW worth of projects with signed interconnection agreements」；「currently has **51 GW** of generation with signed agreements」。51 GW 已簽 ≠ Cycle 1 的 201.5 GW（Cycle 1 研究 2026-09 起、最終協議談判至 2028-05）。兩組數字不能減。

R2 在 PJM 新循環成立：近零入場成本前提已被規則改寫。R1 仍成立：公開統計仍無 `Q_commit` 列。

### C. ERCOT 發電互聯｜Senate 2026-07-29（窗 2026-06-30）

活躍發電互聯：**1,949 件／462,785 MW**。燃料：光 161,554 MW（34.9%）；風 47,991（10.4%）；氣 77,607（16.8%）；儲能 170,945 MW／410 GWh（36.9%）；其他 5 GW。這是本格 `Q_pub` 的官方一句。**無**保證金／場址／承諾 MW 分列。

同份簡報另列大負載約 474 GW（資料中心約 90.2%／420,812 MW）。**明示不採**——物件是負荷側，屬 L2-I，不是 3h B 端之發電互聯檔。

### D. ERCOT 規劃月表原檔｜Capacity-Changes-by-Fuel August 2026（xlsx，2026-09-08）

五張燃料表欄位含 INR、Projected COD、**IA Signed**、Capacity (MW)、**Financial Security**（Yes／No）。本輪加總（非官方匯總列）：

| 燃料表 | 件 | MW | FS Yes MW | FS No MW |
|---|---|---|---|---|
| Wind | 46 | 14,416.5 | 10,660.1 | 3,756.3 |
| Solar | 198 | 50,919.5 | 35,536.4 | 15,383.1 |
| Battery | 209 | 34,584.3 | 19,497.2 | 15,087.1 |
| Gas-CC | 8 | 7,761.5 | 2,609.2 | 5,152.2 |
| Gas-Other | 12 | 7,390.1 | 3,050.1 | 4,340.0 |
| **合計** | **473** | **115,071.9** | **71,353.1** | **43,718.8** |

幾乎列列有 IA 日期（472／473）。這不是活躍佇列 1,949／462.8 GW 的分列——是已進入規劃月表、帶預計 COD 的子集。FS Yes 71.4 GW **不能**從 462.8 GW 減出 `δ`。IA 日期也不是「已繳保證金＋場址控制」的聯集定義。R1 在 ERCOT 官方總表成立；月表只證明「規劃子集上存在 FS 二元欄」，不證明同窗對帳。

GIS 產品頁 PG7-200-ER 標 Public／EWS，本輪讀到的可下載原檔是上列月表與 Senate 簡報，不是需市場合約帳號的完整 GIS 逐列庫。

### E. 申請成本原檔｜ERCOT Fee Schedule ＋ Planning Guide 2026-07-01；MISO GI 頁

ERCOT Fee Schedule（檔名 060125；Planning Guide §5.2.2 指向 Protocols Fee Schedule；費用不可退，除非 Protocols 另定）：

- FIS Application：新機 **$3,000**；既有修改 **$2,700**
- GIM：SODG $2,300；＜10 MW $8,000；**≥10 MW $14,000**（修改同檔次）

相對 GW 級專案，這仍是近零入場價。Planning Guide 另要 FIS 場址控制；TSP 財務擔保出現在協議／施工端（月表 FS 欄），不是申請表上的 $/MW 佔位費。PUCT 16 TAC 25.195 自 2026-01-01 把超津貼互聯設施成本（138 kV 及以下津貼基期 $14M、更高電壓 $20M）轉給發電商——這是施工分攤，不是申請成本。PUCT 2026-09-18 大負載 $50,000/MW 擔保 **明示不採**。

MISO 官方 GI 頁（對照 FERC 轄區，非本格唯一錨）：D1 非退還申請費自 2026-06-10 ＝ **$7,600**；M2 milestone ＝ **$8,000／MW**（現金或 LC），申請時繳。200 MW＝$1.6M 里程碑。近零前提在 MISO 亦不成立。

FERC Order 2023 範本（只作規則背景，非本輪 `δ`）：$5,000 不可退申請費＋規模分檔研究保證金（$35,000+$1,000/MW 至 $250,000）＋場址控制（或 $10,000/MW 替代擔保）。DC Circuit 2026-07-31 維持 Order 2023。PJM／MISO 已落地的 $/MW 數字高於範本下限。

### F. 明示不採

- LBNL Queued Up 2026：活躍約 8,200 件、發電 1,312 GW＋儲能 749 GW；2000–2020 cohort 商轉 13%／撤回 75%；已有 draft 或 executed IA 但未商轉 549 GW。彙編不是 3h「RTO／ISO 檔」。13%／75%／549 GW **不**完成本格測量，也不是 `δ`。
- 只疊「佇列 544／463／220 GW」或「撤回 194 GW／26.7 GW／>750 GW」。撤回 ≠ `Q_spec`。
- ERCOT／PJM 大負載或 Large Load Registry。滑格＝L2-I。
- L2-I 已測之未既得權撤回／歸屬（`1S8FeDY2MXqTCc20IKToblDC5HFJIFb5U`）。本格物件是發電互聯申請 vs 承諾，不是許可撤回損失歸屬。
- T-11／L1-P 設備／物理層、L1-A 鎖定電價存量。本輪不借。
- 第三方儀表板（Kardashev／Lumion／interconnection.fyi）總 GW。不是 ISO 原檔。

---

## 對種子與反方

| 主張 | B 端讀後 |
|---|---|
| 公開申請高估真實擬建；錯價＝把總 GW 當可交付供給 | 機制可陳述。缺同宇宙 `Q_commit` 則不可拒絕「佇列＝即將供給」也不可接受「δ 即高估」 |
| R1 所需量不是所讀之量 | **成立**　承諾／保證金／場址 MW 不是 PJM 州統計或 ERCOT Senate 總表的科目。ERCOT 月表 FS 欄在錯誤的分母上 |
| R2 申請成本已不是近零；2025 撤回更像改革清場 | **在 PJM Cycle 1 與 MISO 成立**。ERCOT 發電入場費仍近零，故「全域近零已死」不成立；「FERC 新循環近零已死」成立。兩邊都無獨立 `δ` |
| R3 換成大負載／資料中心申請 GW | **本輪不採該列** |
| R4 用 L2-I 已測撤回證明本格高估 | **本輪不用該列**。L2-I 構成＝撤回／歸屬；本格構成＝申請成本近零 → 灌水 |
| R5 翻轉 T-11 已排除方向 | **本輪不用該列** |
| R6 把佇列總量當可交易供給預測 | **本輪不選券、不開 T** |

「公開申請 − 財務承諾」在本輪沒有官方同窗序列，故既不能接受也不能拒絕種子。可見端能確定的只有：(i) 狀態桶與已簽 IA 存量存在；(ii) 新循環入場保證金在 PJM／MISO 已是 $/MW 級；(iii) ERCOT 入場費仍是千美元、FS 只在規劃子集上可見。

---

## 不開 T／§7-4

進 T 需數值窗與可拒絕之 H1 倍數。本輪可寫入的只有「申請／研究／協議／商轉 GW、Cycle 1 811→715、Study Deposit 檔次、$4,000/MW、$8,000/MW、$3,000／$14,000 入場費、規劃子集 FS Yes 71.4／115.1 GW」。不夠把 `δ / Q_pub` 寫成財富倍數窗。

§7-4 三題本輪不答（生成卡：轉入個股層時必問；本格不轉、不進 T）。題目本身已由本輪讀數預示方向（公開佇列再拆不出保證金 MW 列；美股可交易主體若以佇列總 GW 作敘事，錯價落在未分列之高估項；PJM／MISO 決策點保證金已在 ≥12 個月窗內改寫近零前提），但不在本輪作答。

**複查觸發器（沿用生成卡，不改寫）：** 任一 ISO／RTO 互聯佇列公開檔或 LBNL 年報，分列已繳保證金／已證明場址控制／財務承諾 MW 與裸申請 MW，並可畫至少兩個報告期之差。

---

## URL

1. https://www.pjm.com/-/media/DotCom/planning/services-requests/interconnection-state-level-statistics.pdf
2. https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2026-releases/20260429-over-800-new-generation-projects-seek-to-connect-under-pjms-reformed-process.pdf
3. https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2026-releases/20260803-over-700-new-generation-projects-accepted-into-first-cycle-of-reformed-interconnection-process.pdf
4. https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/ips/2026/20260126/20260126-item-05---cycle-1-application-requirements-and-nextgen-process.pdf
5. https://www.pjm.com/-/media/DotCom/committees-groups/subcommittees/ips/2026/20260626/20260626-item-03---cycle-schedule-update.pdf
6. https://www.ercot.com/gridinfo/resource
7. https://www.ercot.com/files/docs/2026/07/29/ERCOT-Senate-July-29-Panel-1-Assessing-The-Grid.pdf
8. https://www.ercot.com/files/docs/2026/09/08/Capacity-Changes-by-Fuel-Type-Charts_August_2026.xlsx
9. https://www.ercot.com/files/docs/2026/06/18/July-1-2026-Planning-Guide.pdf
10. https://www.ercot.com/files/docs/2023/03/31/ERCOT-Fee-Schedule-060125.docx
11. https://www.ercot.com/mp/data-products/data-product-details?id=PG7-200-ER
12. https://www.misoenergy.org/planning/resource-utilization/generator-interconnection/
