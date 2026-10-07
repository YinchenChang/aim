<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 12v3tRscJICwIQocFgyUaiMxF6Wa746JT；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h | EMITS: （本檔；Drive work/ 上傳後填 fileId） -->
# L3-P 測一｜B 端實讀（賣方出貨／認列原文與條件化 WPH；客戶側產出能否對同一機時）

**角色：** ANALYST@GK　**日期：** 2026-09-26　**格：** L3-P（半導體製造測試：曝光機 WPH×機台＝產能上界）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先賣方出貨／認列原文與 WPH 之劑量／視場條件。**禁止只重讀「EUV 出貨成長」與論壇機隊一句。** 不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T。
**原陳述（生成卡 `12v3tRscJICwIQocFgyUaiMxF6Wa746JT`）：** 市場把「EUV 機台出貨／認列台數」或規格書 WPH 讀成先進節點產能的充分統計。可曝光晶圓上界＝規格 WPH × 在線機台 × 可用率，再除以每片每層所需曝光次數；High-NA 半視場使大晶粒每層曝光次數上升。錯價只在把「出貨台數／標稱 WPH」當成已交付之層曝光產能。
**守恆式（生成用）：** `C_upper ≤ WPH_spec(dose, field) × N_up × A_avail / E_layer`。`E_layer ≥ 1`；半視場＋晶粒 > 半場 ⇒ `E_layer` 上升。本輪不估參數、不寫 H1。
**否決觸發（生成卡寫給本輪）：** (1) 對 20-F／年報／季報實讀後，出貨台數與條件化 WPH 皆無法對到客戶側層曝光產能，只剩認列台數與規格一句；或 (2) 公開規格已把半視場補償寫進標稱 WPH，且大晶粒拼接佔比無法從公開項分離，上界與可見定價不可辨；或 (3) 公開層已出現穩定可拒絕之「WPH×N vs 產出」對帳，方向翻負或與 1:1 不可辨。
**領域最近公開（§7-10）：** ASML Q2 2026 新聞稿／法說稿／IR 簡報（2026-07-15）；ASML Q4 FY2025 記者會簡報（2026-01-28）；ASML 2025 年報 US GAAP／SEC 年報頁（約 2026-02-25）；NXE:3800E 產品頁；Investor Day 2024 EUV ATP（2024-11-14）；ASML×Intel High-NA 里程碑稿（2026-07-15）與後續合作稿（2026-09-08）。下一官方檢查點＝ASML Q3 2026（約 2026-10 中）或任一 20-F／10-K／年報把「已安裝 EUV 機時 × 層曝光次數」與晶圓產出對帳。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260926_L3-P_generate_GK.md` `12v3tRscJICwIQocFgyUaiMxF6Wa746JT`（10492 B，2026-09-26T10:55:47Z）；`20260923_HEALTH_CL.md` `1_urT6I7RovcM73D3IBTKGIk6RY1z9nC0`；`20260923_HEALTH_GK.md` `1byQGbjCmIT1orLv51moyAH5xnABFO95e`
- query/：`ARCH_dead.md` `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`；`ARCH_matrix.md` `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`；`CHARTER_HIST.md` `1DKg3HUr-zOWw20OmNe1aDpWT_izDwdiT`；`INDEX.json` `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`；`MECH.md` `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-09-26T10:53:06Z role SCOUT）
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-09-26；§1 無 L3；§3 L3［P］＝已生成）
- matrix L3［P］＝已生成（台股禁／複委託費率未取＝表達約束，不改已生成）。INDEX 無獨立 L3-P 測一 fileId
- 3h 快照 `1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj` L3-P B 端僅指名「機台出貨量；WPH 規格」
- 本輪上傳前 work/ 無同名 `20260926_L3-P_test1_GK.md`
- work 主動維護：三檔皆未吸收進現行 FUNNEL／CHARTER；HEALTH 兩份非本輪標的；生成卡待測一後由 SCOUT 對齊。本輪不建 `DONE_`。

---

## 終態

**不通過。不進 T。** 機制（曝光次數 × 單次時間 ≤ 日曆小時）未被否證。失敗在可觀測性——賣方給的是認列台數（年報可拆 NXE／EXE）＋條件化標稱 WPH＋High-NA「出貨 vs 在運」分列；缺客戶側 `N_up × A_avail` 與 `E_layer`（層數 × 每層場次 × 拼接），故 `C_upper` 不能與公開晶圓產出對帳。規格端已把半視場的額外場次寫進 EXE 標稱 WPH（更高加速度／不同劑量基準），大晶粒拼接佔比不是科目。

| 測試項 | 結果 |
|---|---|
| B 端已實讀（非指名；非只讀「EUV 出貨成長」／論壇機隊一句） | **通過**　Q2 2026 新聞稿＋官方法說稿＋IR 簡報；Q4 FY2025 記者會簡報；2025 年報／SEC 年報頁；NXE:3800E 產品頁；Investor Day 2024 ATP；ASML×Intel 2026-07-15／2026-09-08 稿；TSMC 20-F 2025（客戶側對照） |
| 出貨台數＝在線機時 | **不通過**　FY2025 High-NA：出貨 8、在運 6；認列＝SAT 後；季表「New lithography systems sold」含 DUV |
| 條件化 WPH 可對客戶有效 WPH | **不通過**　ATP／年報 WPH 綁定劑量與視場；產品頁數字動態渲染缺失；廠內可用率／劑量不是科目 |
| 半視場乘數可從標稱 WPH 分離 | **不通過**　ATP 已給 EXE 獨立 WpH；大晶粒拼接佔比無公開項 |
| 客戶側產出可對同一機時 | **不通過**　TSMC 20-F＝合計 12 吋約當出貨；無已安裝 EUV 機時、無每層曝光次數。Intel／ASML 稿＝累計晶圓張數（含認證／研發），不是 `WPH×N×A / E` |
| 「WPH×N vs 產出」可拒絕 1:1 | **不存在**　兩邊皆無官方時序 |
| 否決觸發 (1) | **觸發** |
| 否決觸發 (2) | **觸發** |
| 否決觸發 (3) | **未觸發**　對帳序列不存在，方向未翻負 |
| 升格 T | **否** |

失效歸因（§7-2）：不是檢索失敗。失敗在量綱——所需量（在線機時、可用率、每層場次／拼接佔比、與同期晶圓產出同表）不是所讀之量（認列台數、條件化規格 WPH、累計 High-NA 晶圓張數）。現況檔名＝上列 work／query。複查觸發器＝生成卡原文（見下）。停。

本格不入 §1。不改正本（對齊屬 SCOUT）。

---

## 已實讀載體

### A. 賣方季報｜ASML Q2 2026（2026-07-15）

新聞稿表：Q2 新微影系統售出 **86** 台（Q1＝67）；舊機 5 台；Installed Base Management €2,762M。CEO：「2026 low NA EUV capacity of around **65**」；規劃 2027 再加約 30%，並評估 2028 再加約 30%。**無**當季 EUV 台數、**無** WPH、**無**半視場。

官方法說稿（CFO）：淨系統銷售 €6.6B，其中 EUV 系統 €3.8B「**including sales of 1 High NA system**」，非 EUV €2.8B；Logic 51%／Memory 49%。「We now expect to **ship around 65 Low NA EUV systems this year**」。Installed Base 超導因升級。IR 簡報同構；系統銷售單位列「Sale of lithography systems」Q2＝91（含舊機），註：不含量測／檢測。

H1 2026 6-K 質性句：系統銷售增加「driven by higher sales volumes for **EXE and NXE** systems」——平台有量，無台數分列。

R1 在本季已成立：可見端是「全微影售出台數＋EUV 銷售額＋1 套 High-NA 認列＋Low-NA 年產能約 65」。不是在線機時。

### B. 賣方年報／記者會｜FY2025 認列 vs 出貨 vs 在運

Q4 FY2025 記者會簡報（2026-01-28）：

- EUV 系統銷售 €11.6B（+39%），「**recognized revenue on 48 EUV systems (NXE & EXE)**」；含「first EXE:5200B … after completion of **Site Acceptance Test**」。
- High-NA：「We **shipped** a total of **eight** High NA systems … and **six are in operation** including our first second-generation … EXE:5200B which meets full specs at a customer site」。
- NXE:3800E「achieving **record NXE throughput of 230** wafers per hour」（示範峰值，不是 ATP 列）。

2025 年報／SEC 年報頁：

- 「We recognized **four EXE and 44 NXE** systems in sales in 2025 compared to **two EXE and 42 NXE** in 2024。」合計 48，與記者會一致；EXE／NXE 年頻可拆，季頻不可拆。
- 0.55 NA：「recognized revenue for four systems that were shipped to customers’ **R&D facilities**」。
- 年末客戶在 High-NA 上「run more than **400,000 wafers**」。
- NXE:3800E 出貨「at full specification, which includes **220 wafers-per-hour**」相對 NXE:3600D 160 wph（約 +37%）。EXE:5200B「**175 wafers per hour**」「60% higher … compared to … EXE:5000」。
- CEO 訪談另寫 NXE:3800E「from 160 … to **230**」——與記者會紀錄峰值並列表述，與 ATP／產品規格 220 並存。本輪把 220 當規格錨、230 當示範句，不混成廠內有效 WPH。

認列 ≠ 出貨 ≠ 在運。SAT 把「台數→產能」打斷。R1 用盡可見端。

### C. WPH 規格｜產品頁＋Investor Day 2024 ATP

NXE:3800E 產品頁（本輪 fetch）：劑量條件「At dose: **30 mJ/cm²**」；WPH 數字為**動態渲染、本輪缺失**。生成卡已預告；改讀 ATP／年報，不把空位當「無規格」。

Investor Day 2024《EUV products and business opportunity》（2024-11-14）ATP：

| 平台 | 條件 | 標稱吞吐 |
|---|---|---|
| NXE:3600D | 30 mJ/cm² | 160 WpH |
| NXE:3800E | 30 mJ/cm² | **220 WpH** |
| NXE:4000F | 30 mJ/cm² | ≥250 WpH |
| EXE:5000 | 0.55 NA；表列 50 mJ/cm² | **110 WpH** |
| EXE:5200B | 同族 | **175 WpH** |
| EXE:5200C | 同族 | ≥185 WpH |

同簡報專頁「**High NA half field exposure requires stitching for large die**」：小晶粒可落半場、同罩多次、**不必拼接**；大晶粒「Image is split between two masks; stitching … may be needed」。另頁把 High-NA 對特定 DRAM／Logic 層的劑量下降寫成單次曝光 WPH 對照（例：DRAM contact 0.33 NA 148 mJ／22 wph vs 0.55 NA 44 mJ／155 wph）——這是層製程替換敘事，不是廠內 `E_layer` 時序。

R2：EXE 標稱 WPH 已是半場平台自己的數，且劑量基準與 NXE 不同（30 vs 50 mJ）。把「半視場使次數加倍」直接乘在 220 上，與賣方公開 ATP 不一致。補償是否「剛好抵銷加倍」本輪無公開項可拒絕。

### D. 客戶側｜產出能否對同一機時

TSMC 20-F 2025（L3-A 測一已實讀、本輪覆核用途）：12 吋約當出貨 2025＝**15,022** 千片；節點表＝佔**晶圓營收**％；**無**已安裝 EUV 台數、**無**機時、**無**每層曝光次數。2025 年報微影段：提升 EUV scanner 應用效率、開始發展 High-NA「to support … advanced process」——質性，無對帳列。

ASML×Intel 2026-07-15 稿：Intel Foundry 於 18A 對 Core Ultra Series 3（Panther Lake）**特定層**進 High-NA 量產；與 NXE 平台良率對齊；雙資格。2026-09-08 稿：High-NA「more than **one million wafers** processed to date」＝早期認證＋研發＋特定層量產之**累計張數**；「Customers can realize the benefits … current mask format, either by floor-planning within the 6-inch mask or by utilizing … stitching」。同日另有 TSMC×ASML 大尺寸光罩倡議（標題已核；本輪不把倡議當產能對帳）。

累計晶圓張數 ≠ `WPH_spec × N_up × A_avail / E_layer`。R3：加倍作用域被官方寫成「大晶粒才拼接／可切小落半場」。R4：客戶側可見產出仍是合計晶圓或平台營收，瓶頸可在封裝／測試／非曝光（L3-A 法說已有封裝緊句），本格無法用賣方台數拒絕。

論壇／SEMICON 機隊句本輪**不採**為 B 端參數（生成卡禁令）。

### E. 可寫但不可當對帳的上界試算（明示＝非官方）

只為展示缺項，不寫 H1、不寫彈性。

若誤把「2026 Low-NA 產能約 65 × 220 WpH × 24 × 365」當年晶圓上界，得到的是**單次曝光、100% 可用、全視場、無層數**的規格小時，不是任何一家代工的成品晶圓。分母 `E_layer` 與 `A_avail` 缺一則不可與 TSMC 15.0M 或 Intel 累計 High-NA 張數對帳。本輪到此停。

---

## 對種子與反方

| 主張 | B 端讀後 |
|---|---|
| 守恆式可寫 | 可寫。缺 `N_up`／`A_avail`／`E_layer` 則不可重算 `C_upper` |
| 錯價＝把出貨台數／標稱 WPH 當已交付層曝光產能 | 可見端已被「認列台數＋條件化 WPH＋升級／IBM」用盡。錯價句無官方對照錨 |
| R1 台數≠機時（安裝／SAT／可用率） | **成立**　8 shipped vs 6 in operation；認列待 SAT；季「sold」含 DUV |
| R2 標稱 WPH 已內含半場補償 | **在規格層成立**　EXE 獨立 WpH＋不同劑量；半場專頁存在。補償幅度不可分離 |
| R3 加倍只打大晶粒；可切小／不拼接 | **成立於官方稿**　ATP 拼接頁＋2026-09-08「floor-planning within the 6-inch mask or … stitching」 |
| R4 瓶頸可在相鄰層 | **未被否證**　客戶產出無曝光機時分列 |
| R5 N-05 舊種子換編碼 | **本輪不判死**　3h 記「證據削弱、未入 dead」；本格仍缺新的可觀測項，但不把相鄰當已殺 |

「WPH×N vs 產出」在本輪兩邊都沒有官方序列，故既不能接受也不能拒絕 1:1。

---

## 不開 T／§7-4

進 T 需數值窗與可拒絕之 H1 倍數。本輪可寫入的只有「年報認列 44 NXE＋4 EXE、High-NA 出貨／在運分列、ATP 條件化 WPH、客戶側無層曝光機時」。不夠把 `C_upper` 寫成財富倍數窗。

§7-4 三題本輪不答（生成卡：轉入個股層時必問；本格不轉、不進 T）。題目本身已由本輪讀數預示方向（認列台數拒絕不了服務／升級；美股可交易主體是賣方但產能消耗在代工；大尺寸光罩／切小可把半場乘數打近 1），但不在本輪作答。

**複查觸發器（沿用生成卡，不改寫）：** 任一美股可交易曝光機或代工／IDM 主體於 20-F／10-K／10-Q，分列已安裝 EUV 機時或每層曝光次數，且可與同期晶圓產出對帳。

---

## URL

1. https://www.asml.com/en/news/press-releases/2026/q2-2026-financial-results
2. https://ourbrand.asml.com/asset/1fd3908a-0381-47b5-9b69-a3094f656651/2026_07_15-ASML-Transcript-investor-call-Q2-2026.pdf
3. https://ourbrand.asml.com/asset/9078cf4d-91fd-4dd9-a5d5-d1caab6dc046/2026_07_15_Presentation-Investor-Relations-Q2-2026.pdf
4. https://ourbrand.asml.com/m/1a5a2a9d0491701c/original/2026_01_28-Presentation-ASML-Press-Conference-Q4FY2025_FINAL.pdf
5. https://www.asml.com/en/products/euv-lithography-systems/twinscan-nxe-3800e
6. https://edge.sitecorecloud.io/asmlnetherlaaea-asmlcom-prd-5369/media/project/asmlcom/asmlcom/asml/files/investors/investor-days/2024/04_euv-products-and-business-opportunity---peter-vanoppen.pdf
7. https://ourbrand.asml.com/m/8ab959d4926657b/original/asml-2025-annual-report-strategic-report-section.pdf
8. https://www.sec.gov/Archives/edgar/data/937966/000162828026011377/asml-2025xannualxreportx.htm
9. https://www.asml.com/news/press-releases/2026/high-na-euv-reaches-new-readiness-milestone
10. https://www.asml.com/en/news/press-releases/2026/intel-foundry-and-asml-collaborate-to-accelerate-industry-readiness-for-high-na-euv
11. https://investor.tsmc.com/sites/ir/sec-filings/2025_20F%20Report.pdf
12. https://investor.tsmc.com/sites/ir/annual-report/2025/2025%20TSMC%20Annual%20Report.E.pdf

**（完）**
