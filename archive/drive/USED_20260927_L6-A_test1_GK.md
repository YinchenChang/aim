<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 10aH5MscncgySFaJadvJsX3z0OXviAie_；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi | EMITS: PENDING_UPLOAD -->
# L6-A 測一｜B 端實讀（10-Q／10-K 已簽約未交付 vs 已交付／已計費；RPO 附註須對原檔）

**角色：** ANALYST@GK　**日期：** 2026-09-27　**格：** L6-A（雲端與基礎設施服務：已簽約未交付／已交付 領先營收）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先 10-Q／10-K 同表或可對帳附註中的已簽約未交付 vs 已交付／已計費；次為補充包 KPI **僅當**能指回同一報告期之申報數字。**禁止只重讀 RPO 總額、折舊年限、或 T-15 空方材料。** 不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T、不入 §1。T-15 主體 10-Q 只作揭露載體，不得改寫成空方。
**原陳述（生成卡 `10aH5MscncgySFaJadvJsX3z0OXviAie_`；種子 3h §3.29）：** 租賃收入＝已交付 MW×每 MW 月租×使用率；「已簽約未交付÷已交付」為既有揭露且領先營收。錯價只在把 RPO 美元總額當成已可認列營收。
**對照式（生成用）：** `Rev_t = MW_deliv_t × P_MW,t × u_t`；`R_t = MW_signed_undeliv_t / MW_deliv_t`（美元代理：signed-not-commenced 年化租金／在營年化租金）。**不把 RPO 總額當作分子。** 本輪不估參數、不寫 H1。
**否決觸發（生成卡寫給本輪）：** (1) 實讀後無法形成「已簽約未交付／已交付」可對帳區間，只剩 RPO 總額與「backlog 創新高」一句；或 (2) 可運作對照只能寫成折舊年限／減損假設（滑回 C-A3）；或 (3) 可運作對照只能寫成單一委託資本外主體之空方（滑向 T-15）；或 (4) 公開層已出現穩定可拒絕之「該比值只是剩餘合約年期、不領先新交付營收」。
**領域最近公開（§7-10）：** EQIX 10-Q 期 2026-06-30 acc `0001101239-26-000147`；DLR 8-K／supplemental 2026-07-23 與 10-Q acc `0001104659-26-089296`（2026-07-31）；CRWV 10-Q 期 2026-06-30（2026-08-12 入檔）；APLD FY2026 10-K 期 2026-05-31 acc `0001144879-26-000048`；CORZ 10-Q 期 2026-06-30 acc `0001839341-26-000014`。下一官方檢查點＝生成卡原文：任一美股可交易雲端／主機代管／HPC 租賃主體於 10-K／10-Q，同表分列已簽約未交付 MW（或 signed-not-commenced 年化租金）與已交付／已計費 MW（或在營年化租金），且可畫至少兩期之比值——本輪 CORZ 已滿足後段；EQIX／CRWV 之 RPO 附註未滿足前段。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260927_L6-A_generate_GK.md` `10aH5MscncgySFaJadvJsX3z0OXviAie_`（12606 B，2026-09-27T01:56:26Z）；`20260923_HEALTH_CL.md` `1_urT6I7RovcM73D3IBTKGIk6RY1z9nC0`；`20260923_HEALTH_GK.md` `1byQGbjCmIT1orLv51moyAH5xnABFO95e`；`DONE_20260923_HEALTH_GK.md` `1vOqAWh9feQK65EJAau9vBfA2bB47Nsys`；`DUP_PLACEHOLDER_L1-I_test1_do_not_use.md` `1lci-pu8ekOI7T-za2Sl93q-j1GUoNAjl`
- query/：`ARCH_dead.md` `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`；`ARCH_matrix.md` `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`（L6［A］＝已生成）；`CHARTER_HIST.md` `1DKg3HUr-zOWw20OmNe1aDpWT_izDwdiT`；`INDEX.json` `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`；`MECH.md` `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-09-27T01:52:42Z role SCOUT）
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-09-27；§1 無 L6-A；§3 其餘層依 matrix）
- 本輪上傳前 work/ exact_name `20260927_L6-A_test1_GK.md` 空；無內容相近測一
- work 主動維護：L6-A 生成卡未吸收進 FUNNEL／matrix（待本測一後由 SCOUT 對齊）。HEALTH 兩份與 DUP_ 占位非本輪標的。本輪不建 `DONE_`。

---

## 終態

**測一部分通過｜不進 T。** 機制（當期租賃收入只認已交付容量；已簽約未交付對已交付的比值是可觀測存量比）未被否證。3h 指名之 B 端「10-Q RPO 附註」**不是**所需量（R1 成立）。另有申報層對照可寫成同一單位區間：

1. **RPO 總額 ≠ `MW_signed_undeliv`。** EQIX 10-Q：$15.0B 未履行履約義務，初約 1–5 年、約 65% 兩年內認列；**含**已在服務中合約之剩餘年期與 lessor 安排；**不含**計量電、xScale 或有費、多數可無罰金終止之互聯。CRWV 10-Q：未履行 RPO $103.7B（41%／24 個月、39%／25–48 月）；定義為「not delivered, or partially undelivered」之交易價格，仍是美元義務而非未通電 MW。Earnings 之 Revenue Backlog＝RPO＋其他已承諾待交付估計（$104.2B），不是 10-Q 同表之 MW 比。
2. **所需量在別張申報表上存在。** CORZ 10-Q **同一張 KPI 表、三個報告日**：Leased Customer Power vs Billable Customer Power＝590／395（2026-06-30）、590／225（2026-03-31）、590／120（2025-12-31）。定義釘在同檔：Leased＝已簽約不論是否已開始服務；Billable＝已開始服務且在計費。APLD FY2026 10-K **同一檔**：合約 critical IT 1,410 MW vs 期末 operating／revenue-generating 約 100 MW（Polaris Forge 1 首棟；期後 2026-06-30 再交 75 MW＝175 MW，屬 8-K／通話，不併入 10-K 期末比）。
3. **補充包美元代理（次優先，已指回同期 8-K）。** DLR 2026-07-23 Ex.99.1／Q2 supplemental：signed-but-not-commenced backlog $1.9B（100% share）／$1.4B（DLR share），稱約當在營資料中心租金之 30%；Q2 新簽至 commence 加權落後約 9 個月；roll-forward 列 1Q→2Q 之 Signed／Commenced。此 KPI **不在** 10-Q 附註主文；10-Q 同期（acc `0001104659-26-089296`）給 Occupied MW／IT Load MW（2,799／3,102 @ 2026-06-30），那是已建成占用，不是已簽未開租。
4. **否決未全觸發。** (1) 不是「只剩 RPO 總額」——CORZ／APLD 可對帳；但 3h 指名載體本身失敗，故只部分通過。(2) 對照不是折舊年限（C-A3 未滑回）。(3) 對照不是單一 T-15 空方；CRWV 只作 RPO 定義對照，MW 比用 CORZ／APLD。(4) 公開層可拒絕的是「RPO＝剩餘年期」（EQIX 附註自己寫初約+續約），不是「leased−billable 只是剩餘年期」。

不進 T：R1（指名 B 端不是所需量）未解；R3（跨主體 KPI 不可加、單位 MW vs 年化租金 vs RPO 美元）使無單一可單位化連續參數；R4（`R` 下降可為交付跟上或預售定義改成 90 日內認列）極性不定。無 H1。§7-4 三題本輪不答。

---

## A. 指名 B 端：10-Q／10-K RPO 附註（實讀）

| 源 | URL | 本輪讀到的量 |
|---|---|---|
| EQIX 10-Q 期 2026-06-30 acc `0001101239-26-000147` | https://investor.equinix.com/sec-filings/all-sec-filings/content/0001101239-26-000147/0001101239-26-000147.pdf | RPO **約 $15.0B**（含 deferred installation）。初約 1–5 年、其後一年續約；約 **65%** 未來兩年認列。**排除**計量電、xScale 視未來事件之服務費、多數可無重大罰金終止之互聯。**包含**被視為 lessor 之安排。無「已簽約未交付 MW／已交付 MW」同表。未開始之**房東側**租約承諾另列約 $708M（2026–2029 開始），不是客戶容量比 |
| EQIX 10-Q MD&A（同檔；StreetInsider 轉全文） | https://www.streetinsider.com/SEC+Filings/Form+10-Q+EQUINIX+INC+For%3A+Jun+30/26835342.html | Annualized Gross Bookings Q2 **$424M**／H1 **$802M**；定義**只計預期 90 日內開始產生收入**之約。Cabinet utilization **約 78%**（2026-06-30 與 2025-06-30）。無 sold-not-installed 數列表 |
| EQIX Q2 2026 業績稿 | https://d1io3yog0oux5.cloudfront.net/_dffbc0672baa862647cc7f6d882d9ba9/equinix/db/2183/27054/earnings_release/Equinix+Q2+2026+Earnings+Press+Release+and+Financials.pdf | 年度化新簽創高、record backlog；預售／執行語言。**不是** 10-Q 同表之 MW 比 |
| EQIX Q2 簡報定義頁 | https://d1io3yog0oux5.cloudfront.net/_dffbc0672baa862647cc7f6d882d9ba9/equinix/db/2183/27054/earnings_presentation/Equinix+Q2+26+Earnings+Presentation+Final.pdf | Annualized Gross Bookings：新簽 ≥12 月 MRR 年化，**只含預期 90 日內開始認列**。通話稱 cabinets sold but not yet installed 紀錄、剩餘 2026 零售擴容約 30% 已預售——補充語言 |
| CRWV 10-Q 期 2026-06-30（Stock Titan 摘附註） | https://www.stocktitan.net/sec-filings/CRWV/10-q-core-weave-inc-quarterly-earnings-report-d3b596a1f167.html | 「As of June 30, 2026, the Company had **$103.7 billion** of unsatisfied RPO」；41% 至 2028-06-30、39% 第 25–48 月、餘第 49–78 月。定義：交易價格淨估計變動對價，配置於 **not delivered, or partially undelivered** 之義務；含已開立／未開立對價。遞延收入合計約 **$9.7B** |
| CRWV Q2 2026 業績稿 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000362/coreweave2q26earningspress.htm | Revenue backlog **約 $104B**（2026-06-30）；定義＝RPO＋其他已承諾但待交付／待可用之估計，**須滿足交付與服務可用**。Active power 擴至 **1.5 GW**；total contracted power 季末約 **3.7 GW**（通話日後簡報約 4.2 GW）。MW 對照在業績／簡報，**不在**上列 10-Q RPO 段 |
| CRWV 簡報 backlog 對帳 | 業績簡報（8-K 族，2026-08-12） | 2026-06-30：RPO $103.7B ＋ other $0.5B ＝ backlog $104.2B；2025-06-30 RPO $30.1B。此為美元義務時序，不是 `R` |

**單位核對：** EQIX／CRWV 之 RPO 分母若用當期營收，得到的是「剩餘合約年期＋未履約」倍數，不是未交付／已交付容量比。EQIX Bookings 還把 >90 日才開始的約排除在外，與種子分子方向相反。

---

## B. 所需量：已簽約未交付 vs 已交付／已計費（實讀）

| 源 | URL | 本輪讀到的可對帳量 |
|---|---|---|
| CORZ 10-Q 期 2026-06-30 acc `0001839341-26-000014` | https://www.sec.gov/Archives/edgar/data/1839341/000183934126000014/core-20260630.htm | **同表三期（MW）：** Gross utility 2,115／1,860／1,426；Leasable 1,275／1,275／920；**Leased 590／590／590**；Unleased 685／685／330；**Billable 395／225／120**（2026-06-30／2026-03-31／2025-12-31）。敘事：395 vs 590，差 195 MW 在建／試車。定義：Leased＝已簽約不論是否已開始服務；Billable＝已開始服務且在計費。Billable 為 Colocation 段收入主驅動 |
| APLD FY2026 10-K 期 2026-05-31 acc `0001144879-26-000048` | https://ir.applieddigital.com/sec-filings/all-sec-filings/content/0001144879-26-000048/0001144879-26-000048.pdf | 合約組合表：五校園 **1,410 MW** contracted critical IT、基期約 **$36.2B**。同檔：「contracted and operating or under construction…of which approximately **100 MW** was operating and revenue-generating」。Polaris Forge 1 首棟 100 MW 於 2025-10／11 營運。**無**第二個 10-K 期末 live 列，兩期 `R` 不能只靠本檔 |
| APLD FY2026 8-K／業績（期後） | https://www.stocktitan.net/sec-filings/APLD/8-k-applied-digital-corp-reports-material-event-f47682e4a62b.html | 2026-06-30 再交 Building 2 Phase 1 **75 MW**，校園 live **175 MW**。期後數字，不與 10-K 期末 100 MW 混成「同一張 10-K 的兩期」 |
| DLR Ex.99.1 2026-07-23（Q2 supplemental／8-K） | https://www.sec.gov/Archives/edgar/data/1297996/000110465926086270/dlr-20260723xex99d1.htm ；IR 包 https://investor.digitalrealty.com/static-files/678a7e32-514a-41c8-aebc-9492d513bf61 | signed-but-not-commenced：**$1.9B**（100% share）／**$1.4B**（DLR share）；「約當在營資料中心租金之 **30%**」。Q2 新簽 $307M（100%）／$208M（DLR）；加權落後 **9 個月**。Occupied MW **2,799** vs IT Load **3,102**（100% share，五期序列）。後者是建成占用，不是 signed-not-commenced |
| DLR 10-Q 期 2026-06-30 acc `0001104659-26-089296` | https://www.sec.gov/Archives/edgar/data/1494877/000110465926089296/0001104659-26-089296-index.htm | 同期 10-Q 存在。本輪對 10-Q 主文未讀到把 signed-not-commenced 與在營租金寫成可畫兩期比值之附註；該對照留在 8-K／supplemental |

**生成用比值（非正式載入；只證明可重算）：**  
CORZ `R = (Leased − Billable) / Billable` → 2025-12-31 **470／120＝3.92**；2026-03-31 **365／225＝1.62**；2026-06-30 **195／395＝0.49**。Leased 三期不變、Billable 上升，`R` 下降＝交付跟上，不是 RPO 膨脹。  
APLD 期末（2026-05-31）`(1410 − 100) / 100＝13.1`（合約 MW／在營 MW）。美元 $36.2B／在營租金本檔未給，不偽稱已有美元 `R`。  
DLR 美元代理 `1.4 / 在營 ≈ 0.30`（公司自報）； Occupied／IT Load＝2,799／3,102＝**90.2%**，與 0.30 的 backlog／在營租金不是同一分數。

---

## C. 本輪明確不讀、不引用為通過條件

- C-A3 折舊年限／減損假設（`ARCH_dead` #5）。所需量不是資產壽命。
- C-A4 融資／續約單價 `k`。
- T-15 空方論點、CRWV 部位或尺碼。CRWV 10-Q 只核對 RPO 定義。
- 二手「四家雲 RPO 加總／ORCL AI MW 落差」評論（生成卡錨 #8）。
- EQIX 通話「record backlog of cabinets」無櫃數／MW 之 10-Q 同表。
- DLR Occupied MW／IT Load 當作種子 `R`（建成占用 ≠ 已簽未開租）。
- APLD 期後 175 MW 與 10-K 期末 100 MW 混成兩期官方時序。

---

## 對 R1–R5 之測一處分（不寫 H1）

| # | 反方 | 本輪 |
|---|---|---|
| R1 | 10-Q RPO 是未履行義務之交易價格，含已在服務中之剩餘年期，不是尚未交付 MW | **成立。** EQIX／CRWV 附註已實讀。測一在指名載體上停在「所需量不是所讀之量」。通過條件改走 CORZ／APLD 申報 KPI，故只部分通過 |
| R2 | RPO 排除變動對價、可終止約、JV 或有費，RPO／營收比系統性偏離 `R` | **成立為 RPO 路徑。** 不把 EQIX $15.0B／季營收或 CRWV $103.7B／季營收寫成 `R` |
| R3 | 補充包 KPI 跨主體不可加、跨期定義會改 | **成立為單位化風險。** CORZ＝MW；DLR＝年化 GAAP 租金；EQIX bookings＝90 日內 MRR；APLD＝合約 MW vs 在營 MW。無單一連續參數 |
| R4 | 交付跟上則 `R` 下降；高 `R` 可為執行落後或預售成功，極性不明 | **半成立。** CORZ 三期 `R` 3.92→0.49 與「交付跟上」同向；EQIX 把 >90 日開始之約排除在 Bookings 外，預售成功不進該 KPI。領先主張未獲穩定極性，寫不成 H1 窗 |
| R5 | 做成買／空某家 GPU 雲或 REIT＝換格 | **未觸發。** 不選券。T-15 材料未當通過條件 |

---

## 轉入個股層時必問（§7-4，本輪仍不答）

1. 財報科目：未交付／已交付能否從 RPO 總額再拆；能否拒絕剩餘合約年期、計量電、可終止互聯、JV 或有費。CORZ 已用非 RPO 的 leased／billable；該列是否進損益主表仍未答。
2. 可交易工具：恆等落在美股可交易揭露主體，而非僅私有主機商或無申報之預售意向書。
3. 半衰期：通電一旦把 `R` 壓回常態、或預售定義改成「90 日內開始認列」，≥12 個月窗內領先項是否消失。

---

## 本輪寫入／不寫入

寫入：本測一入 Drive `work/`（fileId 見標頭 EMITS，上傳後回填）。
不寫入：FUNNEL 正本、matrix、INDEX、ARCH_dead、CHARTER。禁止新建同名正本。狀態欄對齊屬下一 SCOUT session。
