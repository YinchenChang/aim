# L1-A 生成卡｜能源與電力：已鎖定電價恆等式（PPA−現貨＝存量）
<!-- BY: SCOUT@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；1MDu2Yqt62b6QEwchjqI77YrMs1HBKsbv | EMITS: 待上傳回填 -->
**日期：** 2026-09-26　**角色：** SCOUT@GK　**格：** L1-A　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 本輪只產生成卡。不測。不改正本狀態欄（FUNNEL §3／matrix L1［A］仍＝已生成＝3h 快照）。B 端僅指名。不入 §1。

---

## 0. 本輪範圍

- 種子＝ARCH_3h §3.29 L1-A（`1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj`）：**已鎖定電價恆等式：電費＝容量 MW×負載率×每 MWh×8760；PPA 鎖定價與現貨價之差為一個存量**。B 端載體（3h 僅指名、未實讀；本輪維持僅指名）：公用事業 PPA 揭露；業者能源成本分列。重疊＝T-11（方向為負），重疊度未判。
- 生成序註：3h 填格為 A→I→P。matrix 由上而下、格內 A→I→P，略過已測／已殺／刻意排除後，本輪下一格＝L1-A（L1-P＝刻意排除維持 T-11，不在本輪）。`work/` 巡查：無 `20260926_L1-A_generate_GK.md` 或內容相近檔；`work/` 現況僅 `20260923_HEALTH_CL.md`（`1_urT6I7RovcM73D3IBTKGIk6RY1z9nC0`）、`20260923_HEALTH_GK.md`（`1byQGbjCmIT1orLv51moyAH5xnABFO95e`），與本格無關、本輪不標記。
- 已死／相鄰、機制不同、不得合併：
  - **T-11**（`ARCH_1` 台帳；L1-P 刻意排除）：電力層第一原理落差，**成立但方向為負**；原標的台達電／奇鋐＝台股禁、本即不表達。構成＝物理／設備層落差，不是「鎖定價−現貨＝存量」之會計恆等。同層家族、型態不同，不得併死、不得借其標的。
  - **C-P4**（`ARCH_dead` #19）：水耗非損益科目。屬 L2 水約束，不是電價存量。
  - **L2-A**：每 MW 建置成本＝(土建+機電+冷卻)÷可用 MW；已測｜不進 T。構成＝capex 恆等，不是電費流／鎖定差存量。
  - **L2-I**：併網／水權撤回與損失歸屬；部分通過｜不進 T。構成＝誘因／法定取用權，不是電價科目。
- CHARTER §7-3：不執行終端篩選。§7-4 三題只標「轉入個股層時必問」。§7-10：領域最近公開＝Equinix Q2 2026 10-Q（截止 2026-06-30，acc `0001101239-26-000147`）；Digital Realty FY2025 10-K（截止 2025-12-31，約 2026-02-14 申報）與 Q2 2026 10-Q（約 2026-08-01）；Vistra Q2 2026 10-Q（約 2026-08-08）；Constellation Q2 2026 10-Q（約 2026-08-07）；New Era／Luminant 20 年 PPA 8-K（2026-09-21）。下一官方檢查點＝EQIX／DLR（或同等美股營運商）或 CEG／VST（或同等美股發電商）10-K／10-Q 首次把「已鎖定 PPA 成交單價」與「殘差現貨／關稅單價」分列成可畫存量之美元或 $/MWh 列。

---

## 1. 落差一句（生成物 → 候選陳述）

市場把資料中心電費讀成隨現貨或零售關稅重定價的**流量**（缺電 → 單價升 → 營運商成本升）。種子主張：電費恆等式 `C = MW × LF × p × 8760` 在 `p` 已由 PPA（或同等長期合約）鎖定之後，`(p_PPA − p_spot)` 乘上剩餘約定量是一個**存量**——該差在合約壽命內已決定，不是每季重估的流量。錯價只在把「電力緊張」譯成營運商損益的可變電費，而不是已鎖定差的存量與未鎖定殘差。B 端指名之對照＝公用事業／發電商 PPA 揭露，以及營運商能源成本分列——若分列只能看到「utilities」總額或轉嫁給租戶的 reimbursements，存量不可畫。

---

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（鎖定單價與現貨之差為存量；非物理上界、非誘因） |
| 選擇者 | 營運商／租戶對發電商或公用事業：鎖定 PPA vs 留在現貨／關稅 |
| 可見端 | PPA 公告之 MW、年期、交貨年；營運商 utilities／能源成本列；租戶 utilities reimbursements |
| 指名不可見端 | 已鎖定成交 `$/MWh`；殘差現貨／關稅 `$/MWh`；兩者差 × 剩餘約定量之存量時序；轉嫁後存量落在營運商或租戶 |
| 主張 | `p` 鎖定後，`(p_PPA − p_spot)` 是存量；把電費當流量重定價，會把已鎖定量誤讀成可交易之季頻成本衝擊 |
| 表達工具型態（只指名，不選券） | 已上市、美股可交易之資料中心營運商或發電商揭露主體。不選券。台股禁（T-11 原標的不復活） |
| 重疊 | T-11（方向負、物理層）；L2-A capex；C-P4 水。重疊不構成丟棄 |

對照式（生成用，非正式載入）：

`C(t) = MW(t) × LF(t) × p(t) × 8760`

`S_lock(t) = (p_PPA − p_spot(t)) × Q_remain(t)`

`p(t)` 可拆 `ω_lock · p_PPA + (1 − ω_lock) · p_spot`。`ω_lock → 1` 時，流量衝擊縮成殘差，`S_lock` 才是種子要的量。本輪不估參數、不寫 H1。

---

## 3. B 端指名（3h 原欄；本輪不實讀、不宣稱可分離）

3h 原文兩欄：**公用事業 PPA 揭露**；**業者能源成本分列**。本輪只把指名寫成可派工之載體，禁止把下列 URL 當成測試一已完成。

| 指名欄 | 載體（只指名） | 公開入口（錨，非實讀結論） |
|---|---|---|
| 公用事業／發電商 PPA 揭露 | Vistra：AWS Comanche Peak 1,200 MW／20 年；Meta PJM 核電 2,609 MW／20 年。Constellation：Microsoft Crane（TMI-1 重啟）20 年 PPA；2026 另簽 920 MW 長約。New Era／Luminant（Vistra 關係企業）20 年、200–207 MW（8-K 2026-09-21） | VST Q2 2026 10-Q（約 2026-08-08）；CEG Q2 2026 10-Q（約 2026-08-07，https://investors.constellationenergy.com/static-files/ffe5acb1-a976-4963-85f7-28551efd3929 ）；NUAI 8-K 2026-09-21（https://www.sec.gov/Archives/edgar/data/2028336/000121390026101642/0001213900-26-101642.txt ）。可見 MW／年期／交貨窗；**未見**可用之成交 `$/MWh`。第三方盤點（MLQ.ai 2026-07-17）：62 件協議可用公開單價＝0 |
| 業者能源成本分列 | Equinix：CoR 含 utilities／electricity；IR 簡報有 utilities cost as % of revenues；年報質性：29 件 PPA、合約 >1,400 MW、2025 營運 PPA 854 MW | Q2 2026 10-Q acc `0001101239-26-000147`（https://investor.equinix.com/sec-filings/all-sec-filings/content/0001101239-26-000147/0001101239-26-000147.pdf ）；FY2025 年報質性 PPA 句。**無**鎖定單價 vs 現貨單價分列，故**無**可畫之 `S_lock` |
| 業者能源成本分列 | Digital Realty：Total Utilities（stabilized／non-stabilized）；Tenant reimbursements — Utilities；「power agreement charges」為變動句之一 | FY2025 10-K（約 2026-02-14，https://www.sec.gov/Archives/edgar/data/1494877/000110465926015365/dlr-20251231x10k.htm ）：2025 Total Utilities $1,426M vs 2024 $1,333M。Q1／Q2 2026 營運報表另列 utilities 與 tenant reimbursements。**無** `$/MWh` 鎖定／現貨拆 |
| 轉嫁結構（非 3h 主欄，防滑到租戶側） | 營運商合約：metered power／utilities reimbursement／all-in 含電 | EQIX／DLR 10-K／10-Q 之 pass-through 句。若電費幾乎全數轉嫁，`S_lock` 不在營運商損益。不得把 reimbursements 當成 `p_PPA` |

以上為指名錨。**不宣稱 utilities 總額已等於 `C = MW×LF×p×8760`，不宣稱 PPA 公告已給出 `p_PPA`，不宣稱 `S_lock` 已存在，不宣稱鎖定差已在營運商或發電商損益中可分離。** 測試一之 B 端須實際 fetch 鎖定單價與現貨／關稅單價能否同表對帳，禁止只疊「已簽 PPA、MW 上升」或 utilities 總額 YoY。

---

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | 所需量是 `p_PPA` 與 `p_spot` 之差；可見端是 MW、年期、utilities 美元總額。單價不是科目 | MLQ.ai 2026-07-17：62／62 無可用公開 `$/MWh`；EQIX／DLR／VST／CEG 10-Q 有容量與年期、無成交單價 | 測試一可能停在 (a)：所需量不是所讀之量 |
| R2 | 多數租約把電費轉嫁（reimbursements／metered power）。存量若存在，落在租戶，不在營運商 | DLR tenant reimbursements — utilities；EQIX metered power／CoR utilities 句 | 表達點選在營運商＝量落錯主體 |
| R3 | 發電商長約把 `p_PPA` 鎖在賣方營收；公開層只見 RPO／剩餘履約義務美元，不是 `$/MWh` 差 | CEG 剩餘履約義務表；VST／CEG PPA 新聞稿 | 把發電商 RPO 當成 `S_lock`＝換量 |
| R4 | T-11 已判電力層第一原理落差方向為負；本格若用同一「缺電」敘事證明鎖定差可交易，只是把符號從設備層翻到會計層 | `ARCH_1` T-11；matrix L1-P 刻意排除 | 表達點選錯＝沿用已排除方向，不是本格通過 |
| R5 | 把本格做成「買發電商／賣營運商」或滑到台股電源設備，會滑到尺碼或台股禁 | CHARTER §2-8 台股禁；T-11 原標的 | 表達點選錯＝換格 |

種子仍可能在「若公開層出現可對帳之 `p_PPA` 與殘差現貨，且未轉嫁部分可畫 `S_lock` 時序」上寫成可拒絕的會計對照。缺單價對，反解停。是否存在、轉嫁後殘差是否仍在美股可交易主體，是測試一的題。

---

## 5. SCOUT 裁決

**留。** 不進 T。下一動作＝ANALYST@GK 對本格做測試一（B 端須實際 fetch 並列 URL；優先鎖定 `$/MWh` 與現貨／關稅 `$/MWh` 能否同主體、同窗對帳，禁止只重讀 PPA MW 公告或 utilities 總額）。本輪不測。

理由（只到殺／留）：
- 會計恆等可陳述，與已排除 L1-P／T-11（物理層、方向負）、已測 L2-A（capex）、已死 C-P4（水）不同構成。
- 3h B 端未實讀；本輪維持僅指名。R1–R4 足夠強，預設風險＝單價不是科目、轉嫁把存量移出租戶外之可交易主體、RPO 不可譯成 `$/MWh` 差、翻轉 T-11 已排除方向；不是機制已被否證。
- 終端三題本階段不答（§7-3）。

否決觸發（寫給 ANALYST，不是本輪執行）：
- 對 10-K／10-Q／20-F／關稅或 PPA 附註實讀後，`p_PPA` 與 `p_spot` 無法從公開項分離，只剩 MW、年期、utilities 總額；或
- 可見電費幾乎全數轉嫁，未鎖定殘差無法在美股可交易主體上寫成獨立存量；或
- 公開層已出現穩定可拒絕之 `S_lock`，方向與「鎖定差為存量、非流量衝擊」不可辨，或只能用 T-11 已排除之設備／物理敘事翻號解釋。

複查觸發器（若日後殺）：任一美股可交易資料中心營運商或發電商於 10-K／10-Q／20-F，分列已鎖定 PPA 成交單價與殘差現貨／關稅單價，並可畫至少兩個報告期之差或剩餘約定量美元。

---

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：`p_PPA` 與 `p_spot` 能否從 utilities／燃料與購電／PPA 附註再拆；能否拒絕轉嫁、REC／屬性憑證與容量費交換。
2. 可交易工具：存量落在美股可交易營運商或發電商揭露主體，而非僅私有租戶、未申報之 behind-the-meter 專案或台股設備商。
3. 半衰期：提前解約、重議價、或下一代負載改走 on-site 發電，是否在 ≥12 個月窗內把「已鎖定差＝存量」打成重新打開的流量。

---

## 7. 本輪寫入／不寫入

寫入：本生成卡入 Drive `work/`（fileId 見標頭 EMITS，上傳後回填）。
不寫入：FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（§3 L1［A］仍＝已生成＝3h 快照；不入 §1）；matrix 正本 `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`；§2／§4／§5；INDEX.json；ARCH_dead。禁止新建同名正本。狀態欄對齊屬測試一之後 session。
