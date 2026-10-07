<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1LVQtOU8-JAtppOh1vHt2HJk6SLh9CKDa；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；1iECgyKYkah8xQF4UB-g8fOnAApI3pLVx；1-umn-OoxhkuP4f6K0dni2jzzz7rnec02 | EMITS: （本檔；Drive work/ 上傳後填 fileId） -->
# L4-I 測一｜B 端實讀（加速器商系統／元件分列能否成時序）

**角色：** ANALYST@GK　**日期：** 2026-09-26　**格：** L4-I（運算硬體系統：開放機櫃＝commoditize-the-complement）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先加速器商系統／元件分列能否畫出 `s_sys(t)`。**禁止只重讀參考設計一句、分部毛利率、或 L4-A 之 BOM 表。** 不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T、不入 §1。
**原陳述（生成卡 `1LVQtOU8-JAtppOh1vHt2HJk6SLh9CKDa`）：** 市場把加速器商公開機櫃／基板參考設計讀成對整機商讓利或生態中立。種子主張：開放的是互補品（機櫃組裝），目的是讓整機商彼此可替換、利潤被壓向組裝工價，稀缺租金留在加速器。錯價只在把「參考設計開放」讀成整機商毛利池被分享，而不是被商品化。B 端對照＝加速器商自己營收裡「系統」比重的時序——若開放後系統比重上升，互補品可能被賣方收回，不是被商品化。
**對照式（生成用）：** `s_sys(t) = Rev_sys(t) / Rev_accel_total(t)`。開放後 `s_sys` 下降且整機商可替換性上升 → 與種子同向；`s_sys` 上升 → 賣方收回系統。本輪不估參數、不寫 H1。
**否決觸發（生成卡寫給本輪）：** (1) 對 10-K／10-Q／20-F 實讀後，`s_sys(t)` 無法從公開項分離，只剩 DC／C&N／參考設計名稱；或 (2) 可見時序只能寫成加速器商自有系統／Networking 成長（即開放未商品化互補品，只是多一條自營系統），且與整機商利潤無獨立對照；或 (3) 公開層已出現穩定可拒絕之 `s_sys(t)`，方向與「開放以壓整機商」不可辨，或只能用 C-I3′ 已死的分部毛利率翻號解釋。
**領域最近公開（§7-10）：** NVIDIA Q2 FY27 10-Q（截止 2026-07-26，申報約 2026-08-27，acc `0001045810-26-000075`）；NVIDIA Q2 FY27 CFO Commentary（2026-08-26）；NVIDIA FY26 10-K／R25（截止 2026-01-25，acc `0001045810-26-000021`）；NVIDIA Q1 FY27 CFO Commentary（2026-05-20／21；「previous sub-markets」最後一次給 DC compute／networking 美元）；AMD 10-Q（截止 2026-06-27，申報 2026-08-05，acc `0000002488-26-000123`）＋Q2 8-K／exhibit 99.1。下一官方檢查點＝NVIDIA Q3 FY27（約 2026-11）或任一美股可交易加速器商 10-K／10-Q／20-F 首次把「系統／機櫃／參考設計授權」與「加速器元件」分列成可畫至少兩期之美元列。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260926_L4-I_generate_GK.md` `1LVQtOU8-JAtppOh1vHt2HJk6SLh9CKDa`（11298 B，2026-09-26T12:04:10Z）；`20260926_L4-A_generate_GK.md` `1-umn-OoxhkuP4f6K0dni2jzzz7rnec02`＋`DONE_` `17x4DkXNYNHuXn-mRiMCqa05VFNaksA2C`；`20260926_L4-A_test1_GK.md` `1iECgyKYkah8xQF4UB-g8fOnAApI3pLVx`＋`DONE_` `1MQPU326KJfRtohmE0eG3nb_IYYnHiJhr`；`20260923_HEALTH_CL.md` `1_urT6I7RovcM73D3IBTKGIk6RY1z9nC0`；`20260923_HEALTH_GK.md` `1byQGbjCmIT1orLv51moyAH5xnABFO95e`
- L4-P 生成／測一已 `USED_`（`1PsNSkEHuldFtcV13l-etxUODxHhMwW_E`／`18EssPf0uT4BUyR44fEkRKMKyP-iW3jx0`），不在 work/ 現況清單
- query/：`ARCH_dead.md` `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`；`ARCH_matrix.md` `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`（L4［I］＝已生成）；`CHARTER_HIST.md` `1DKg3HUr-zOWw20OmNe1aDpWT_izDwdiT`；`INDEX.json` `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`（L4 註＝P 已測、A/I 已生成；無 L4-A／L4-I 測一鍵）；`MECH.md` `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-09-26T11:29:51Z role SCOUT）
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-09-26；§1 無 L4-I；§3 L4［I］＝已生成）
- 3h 快照 `1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj` L4-I B 端僅指名「加速器商營收中『系統』比重之時序」
- 本輪上傳前 work/ 無同名 `20260926_L4-I_test1_GK.md`、無內容相近測一
- work 主動維護：L4-I 生成卡未吸收進 FUNNEL／matrix（待本測一後由 SCOUT 對齊）。L4-A 兩檔已有 `DONE_`、正本仍在 work/＝中繼態，本輪不另標。HEALTH 兩份非本輪標的。本輪不建 `DONE_`。

---

## 終態

**不通過。不進 T。** 機制（開放參考設計＝商品化互補品；`s_sys` 下降＝租金留在加速器、整機商被壓向組裝工價）未被否證。失敗在可觀測性——加速器商給的是 C&N／Data Center 平台營收；年頻可再拆 DC Compute vs Networking；文內有「system shipments」「HGX systems → full-scale datacenter solutions」質性句。**無**系統／DGX／機櫃／參考設計授權對 GPU／加速器元件之美元分列，故**無**可畫之 `s_sys(t)`。第二家美股加速器商（AMD）Data Center 把 Instinct／EPYC／NIC／FPGA 捆在同一列；Helios 為授權給客戶與代工之機架架構，且 10-Q 明文「不製造、不出售完成之 Helios 機架」——仍無系統美元列。

| 測試項 | 結果 |
|---|---|
| B 端已實讀（非指名；非只讀參考設計一句／分部毛利率／L4-A BOM） | **通過**　NVIDIA Q2 FY27 10-Q＋CFO Commentary＋FY26 10-K／R25＋Q1 FY27 CFO Commentary；AMD 10-Q＋Q2 8-K／99.1 |
| `s_sys(t)`＝系統／機櫃美元 ÷ 加速器商總營收可成時序 | **不通過**　無系統／機櫃／DGX／參考設計授權美元列。至少兩期之比重序列不存在 |
| 年頻 DC Compute vs Networking 可否代替 `s_sys` | **否**　Networking＝互連／交換平台，不是機櫃組裝；Compute＝加速計算平台，不是 GPU 元件。兩者皆含「systems」質性詞 |
| 參考設計授權收入獨立分列 | **不通過**　NVIDIA 無 MGX／HGX 授權列。AMD Helios＝授權給客戶／代工，無授權收入列 |
| 開放後 `s_sys` 下降且整機商可替換性上升 | **不可檢**　無 `s_sys`。可見質性句指向賣方把系統收進自有平台（NVIDIA）或授權但不入帳（AMD） |
| 否決觸發 (1) | **觸發** |
| 否決觸發 (2) | **觸發（質性端）**　可見殘差＝NVIDIA Networking／「full-scale datacenter solutions」／「system shipments」；無獨立整機商利潤對照列可與 `s_sys` 同窗。本輪不重讀整機商 GM（那是 L4-A／R3） |
| 否決觸發 (3) | **未觸發**　`s_sys` 序列不存在，方向未翻、未用 C-I3′ 毛利率翻號 |
| 升格 T | **否** |

失效歸因（§7-2）：不是檢索失敗。失敗在量綱——所需量（系統 vs 元件美元時序、參考設計授權列）不是所讀之量（C&N／DC、年頻 Compute vs Networking、Data Center 分部、Helios 產品句）。現況檔名＝上列 work／query。複查觸發器＝生成卡原文（見下）。停。

本格不入 §1。不改正本（對齊屬 SCOUT）。

---

## 已實讀載體

### A. 加速器商季報｜NVIDIA Q2 FY27 10-Q（截止 2026-07-26；acc `0001045810-26-000075`）

可報告分部（百萬美元）：

| | 三個月迄 Jul 26, 2026 | 三個月迄 Jul 27, 2025 | 六個月迄 Jul 26, 2026 |
|---|---|---|---|
| Compute & Networking | 88,299 | 41,331 | 162,850 |
| Graphics | 7,922 | 5,412 | 14,987 |
| Total | 96,221 | 46,743 | 177,837 |

市場平台：Data Center **89,023**（同比 +117%；環比 +18%）；其下 Hyperscale 48,710／ACIE 40,313。**本季 10-Q 無 DC Compute vs Networking 美元拆。** C&N 定義＝「Data Center accelerated computing and networking platforms and AI solutions and software」。

MD&A 原句：「**Blackwell continued to account for the majority of our system shipments.**」「We will be shipping both Blackwell and Rubin **systems**.」Vera Rubin「began production shipments in the third quarter of fiscal year 2027」。產品句把 processors、interconnects、software、**systems** 寫在同一平台裡。

R1 在本季已成立：可見端是 C&N／DC 平台營收＋「system shipments」質性句。**不是**系統 vs 元件美元。C&N ≠ 系統營收；DC ≠ 加速器元件；「system shipments」無金額。

### B. 加速器商年報｜NVIDIA FY26 10-K／R25（截止 2026-01-25；acc `0001045810-26-000021`）

可報告分部：C&N FY26 **193,479**／FY25 116,193／FY24 47,405。Graphics FY26 22,459。

終端市場 Data Center FY26 **193,737**，其下：

| | FY26 | FY25 | FY24 |
|---|---|---|---|
| DC Compute | 162,361 | 102,196 | 38,950 |
| DC Networking | 31,376 | 12,990 | 8,575 |

Networking FY26 +142%。MD&A：DC computing「driven by demand for our Blackwell computing platform」；DC networking「driven by the introduction and continued ramp of **NVLink compute fabric for GB200 and GB300 systems** and the growth of Ethernet and InfiniBand platforms」。

質性句（對本格打擊大於數字）：「Gross margin decreased to 71.1% in fiscal year 2026 from 75.0% … **as our business model transitioned from offering Hopper HGX systems to Blackwell full-scale datacenter solutions**」。「Our Data Center infrastructure **systems** include supercomputing platforms and servers, bringing together … GPUs, CPUs, interconnects …」。

年頻 Compute vs Networking **存在**，系統 vs 元件 **仍不存在**。Networking 31.4B 是加速器商自己收走的互連平台，不是機櫃組裝被商品化後的殘差，也不是 `Rev_sys`。R2 用盡可見端：開放參考設計與自營系統敘述並行，公開層只能寫成賣方把系統收進平台。

R25 與 10-K 本文皆無 HGX／MGX／DGX／reference design 授權收入列。客戶類型句列 AIB／ODM／OEM／CSP／system integrators，**無**授權費科目。

### C. Q2 評論稿未續列；Q1 為「previous sub-markets」最後一次美元拆

Q2 FY27 CFO Commentary：C&N 88,299；DC 89,023。**無** Compute vs Networking 美元。與 10-Q 一致。

Q1 FY27 CFO Commentary（2026-05-20／21）：「**Under the previous sub-markets**, Data Center compute revenue was a record $60.4 billion … Data Center networking revenue was a record $14.8 billion」。此後官方改以 Hyperscale／ACIE 報 DC 子市場。即使把 Q1 的 60.4／14.8 與 FY26 年頻 162.4／31.4 串成序列，得到的仍是 **平台組合**（compute platform vs networking platform），不是系統 vs 元件。禁止把 Networking／DC 佔比寫成 `s_sys(t)`。

### D. 第二家加速器商｜AMD 10-Q（截止 2026-06-27；acc `0000002488-26-000123`）＋Q2 8-K／99.1

Data Center 分部三個月 **6,718**／六個月 12,493（百萬美元）。分部定義同時含 AI accelerators、server CPUs、GPUs、APUs、DPUs、AI NICs、FPGAs——**Instinct 與 EPYC 不拆，系統與元件不拆**。

10-Q 風險因素原句：「**Although we supply certain products used in Helios-based system, we do not manufacture or sell the completed Helios rack systems.**」「the introduction of system-level architectures, such as our “Helios” rack-scale platforms, **which we develop and license for implementation by customers and their manufacturing partners**」。Helios 是本格「開放／授權參考設計」在第二家主體上的可見名稱，但授權收入**未分列**，完成機架**不入 AMD 營收**。故 AMD 也不能產 `s_sys(t)`——不是「系統比重下降」，是「完成系統不在本體帳上」。

8-K／99.1：Data Center 成長歸因 EPYC＋Instinct MI350；Helios 為產品發表句，無美元。

### E. 明示不採

- 參考設計產品頁／論壇上線日（生成卡：可見端名稱，不是 3h B 端）。
- L4-A 已讀之四項 BOM、整機商 GM％、券商機架表。本格 B 端不是整機商毛利池。
- C-I3′ 已死分部毛利率（`ARCH_dead` #14）。本輪不用該列翻號證明「開放」。
- 把 DC Networking／DC 總額當 `s_sys` 的試算：分母與分子皆非 `Rev_sys`，明示＝非官方，本輪到此停。

---

## 對種子與反方

| 主張 | B 端讀後 |
|---|---|
| 開放互補品以壓整機商 | 機制可陳述。缺 `s_sys(t)` 則不可拒絕「開放＝讓利」也不可接受「開放＝商品化」 |
| 錯價＝把參考設計開放讀成整機商毛利被分享 | 可見端已被 C&N／DC／Compute vs Networking／Helios 授權句用盡。錯價句無官方對照錨 |
| R1 所需量不是所讀之量 | **成立**　系統／元件與授權收入皆非科目 |
| R2 殘差已被自營系統／Networking 收走 | **在可見端成立**　FY26 Networking +142%；「HGX systems → full-scale datacenter solutions」；Q2「system shipments」是加速器商自己的出貨句。AMD 則把完成機架排除在本體營收外 |
| R3 整機商 GM 不可譯 | **本輪不採該列**（屬 L4-A）。不把 SMCI／Dell GM 寫進本格通過條件 |
| R4 翻轉 C-I3′ 已死毛利率 | **本輪不用該列**。C-I3′ 構成＝鎖定／UL 毛利率；本格構成＝開放互補品／系統比重 |
| R5 滑到「買加速器／賣整機」或 L4-A BOM | **本輪不選券、不開 T、不重讀 BOM** |

「開放後系統比重下降」在本輪兩邊都沒有官方序列，故既不能接受也不能拒絕。NVIDIA 質性句方向與種子相反（系統被收進自有平台）；AMD 質性句是授權但不入帳——兩者都不是可單位化之 `s_sys(t)`。

---

## 不開 T／§7-4

進 T 需數值窗與可拒絕之 H1 倍數。本輪可寫入的只有「C&N／DC 平台營收、年頻 Compute vs Networking、Q1 一次 previous-sub-market 拆、AMD Data Center 捆綁列、Helios 授權但不出售完成機架」。不夠把 `s_sys` 寫成財富倍數窗。

§7-4 三題本輪不答（生成卡：轉入個股層時必問；本格不轉、不進 T）。題目本身已由本輪讀數預示方向（C&N／DC／Data Center 再拆不出系統 vs 元件或授權列；美股可交易主體存在但誘因落在未分列科目；加速器商把機櫃收進自有系統銷售或改以授權不入帳，已在質性句出現），但不在本輪作答。

**複查觸發器（沿用生成卡，不改寫）：** 任一美股可交易加速器商於 10-K／10-Q／20-F，分列系統／機櫃營收與加速器元件營收並可畫至少兩個報告期之比重，或分列參考設計／系統授權收入。

---

## URL

1. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
2. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm
3. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
4. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/R25.htm
5. https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q127/Q1FY27-CFO-Commentary.pdf
6. https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm
7. https://www.sec.gov/Archives/edgar/data/2488/000000248826000121/q22026991.htm
8. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
