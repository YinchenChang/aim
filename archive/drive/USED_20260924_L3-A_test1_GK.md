<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 14hDQC4MhQGMVZfXJn6GdDjTOOyQ5UZQo；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h | EMITS: （本檔；Drive work/ 上傳後填 fileId） -->
# L3-A 測一｜B 端實讀（節點 ASP／層別良率能否從申報反解）

**角色：** ANALYST@GK　**日期：** 2026-09-24　**格：** L3-A（半導體製造測試：有效晶粒單價恆等）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先 20-F／季報／法說能否反解節點 ASP 或層別良率。**禁止只重讀二手價帶與論壇良率一句。** 不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T。
**原陳述（生成卡 `14hDQC4MhQGMVZfXJn6GdDjTOOyQ5UZQo`）：** 有效晶粒單價＝每片晶圓價÷(前端良率×封裝層良率×每片晶粒數)。市場把代工報價／節點營收佔比所隱含之晶圓 ASP 讀成先進製程單位成本的充分統計。錯價只在把「晶圓 ASP／節點 mix」當成有效晶粒單價的代理。
**恆等（生成用）：** `P_eff = P_waf / (Y_fe × Y_pkg × N_die)`。本輪不估參數、不寫 H1。
**否決觸發（生成卡寫給本輪）：** (1) 對 20-F／10-Q／法說實讀後，節點 ASP 與層別良率皆無法從公開項反解或分離，只剩營收％與二手價帶；或 (2) 封裝層公開良率穩定近 1，且前端良率對面積的敏感度無法從公開項寫成與晶圓報價可對照的彈性區間；或 (3) 公開層已出現穩定可拒絕之 `P_eff` 對 `P_waf` 彈性，方向翻負或與 1 不可辨。
**領域最近公開（§7-10）：** TSMC 2Q26 新聞稿／管理報告／簡報（2026-07-16）；2Q26 法說逐字稿頁面日 2026-08-28；20-F 2025（約 2026-04-16）；2025 年報英文（約 2026-05）；TrendForce CoWoS-L（2026-09-18）；技術論壇／OCP APAC 引述（2026-05-14 起）。下一官方檢查點＝3Q26 季報（約 2026-10 中）。GFS FY25 10-K（2026-02）。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260924_L3-A_generate_GK.md` `14hDQC4MhQGMVZfXJn6GdDjTOOyQ5UZQo`（10578 B，2026-09-24T05:50:09Z）；`20260923_HEALTH_CL.md` `1_urT6I7RovcM73D3IBTKGIk6RY1z9nC0`；`20260923_HEALTH_GK.md` `1byQGbjCmIT1orLv51moyAH5xnABFO95e`
- query/：`ARCH_dead.md` `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`；`ARCH_matrix.md` `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`；`CHARTER_HIST.md` `1DKg3HUr-zOWw20OmNe1aDpWT_izDwdiT`；`INDEX.json` `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`；`MECH.md` `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-09-24T06:00:06Z role ANALYST）
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-09-23；§1 無 L3；§3 L3［A］＝已生成）
- matrix L3［A］＝已生成。INDEX `L3` 指向 matrix，無獨立 L3-A 測一 fileId
- 本輪上傳前 work/ 無同名 `20260924_L3-A_test1_GK.md`

---

## 終態

**不通過。不進 T。** 機制（單價＝總價÷有效產出；良率為乘積）未被否證。失敗在可觀測性——申報層給的是節點佔**晶圓營收**％＋**合計**出貨；缺節點出貨則節點 ASP 反解停；層別良率不是科目；Others／先進封裝與測試、光罩捆綁。

| 測試項 | 結果 |
|---|---|
| B 端已實讀（非指名；非只讀二手價帶／論壇一句） | **通過**　20-F 2025；2Q26 新聞稿 PDF＋管理報告＋簡報＋官方法說稿；2025 年報；GFS FY25 10-K ASP 段；TrendForce 2026-09-18（只作封裝結構，不作價） |
| 節點 ASP 可從晶圓營收％＋出貨反解 | **不通過**　出貨不分節點 |
| 層別良率（Y_fe／Y_pkg／CoW／中介層）為申報科目 | **不通過**　20-F／季報無列 |
| Others 能拒絕測試／光罩／非 CoWoS | **不通過**　20-F 原文捆綁；CapEx 同捆 10–20% |
| 混合「每片營收」≠節點 ASP | **已核**　可重算，但被 mix 用盡（R3） |
| `P_eff` 對 `P_waf` 彈性可拒絕 1 | **不存在**　兩端皆無官方時序 |
| 否決觸發 (1) | **觸發** |
| 否決觸發 (2) | **觸發**　論壇／OCP 封裝良率近 1（非 10-Q）；前端面積彈性無公開項可寫 |
| 否決觸發 (3) | **未觸發**　彈性序列不存在，方向未翻負 |
| 升格 T | **否** |

失效歸因（§7-2）：不是檢索失敗。失敗在量綱——所需量（節點 ASP、層別良率、`N_die` 的申報對帳）不是所讀之量。現況檔名＝上列 work／query。複查觸發器＝生成卡原文（見下）。停。

本格不入 §1。不改正本（對齊屬 SCOUT）。

生成卡所列 `pr.tsmc.com/english/news/3278` 本輪開啟為 **December 2025 Revenue Report**，不是 2Q26 新聞稿。2Q26 改以官網 PDF／管理報告／簡報／逐字稿實讀（URL 見末）。此為鏈位漂移，不把舊鏈不命中寫成「2Q26 不存在」。

---

## 已實讀載體

### A. TSMC 20-F 2025（申報層；約 2026-04-16）

- 晶圓製造：「The principal source of our revenue is wafer fabrication, which accounted for approximately **86%** of our net revenue in 2025. The rest of our net revenue was mainly derived from **packaging and testing services, mask making, design, and royalty income**.」——非晶圓腿是捆綁餘項，不是 CoWoS 營收列，不是層別良率。
- 節點表＝佔**晶圓營收**％（註 (1) 原文），不是佔合併營收、不是出貨％：

| 解析度 | 2023 | 2024 | 2025 |
|---|---|---|---|
| 3nm | 6% | 18% | 24% |
| 5nm | 33% | 34% | 36% |
| 7nm | 19% | 17% | 14% |
| 16nm | 10% | 8% | 7% |
| 28nm | 10% | 7% | 7% |
| 其餘 | … | … | … |
| 合計 | 100% | 100% | 100% |

- 先進（≤7nm）佔晶圓營收 74%（2024＝69%）。
- 12 吋約當出貨（千片）：2023＝12,002；2024＝12,910；2025＝**15,022**。無節點分列。
- ASP 驅動原文：「mainly attributed to an increase in ASP due to a **higher proportion of advanced technology (7-nanometer and below) revenue and an increase in wafer shipments**」。官方已把可見的「每片變貴」歸因於 mix＋量。R3 用盡可見端。
- 服務菜單含 mask／3DFabric／SoIC／CoWoS／測試，皆無金額、無良率科目。
- **無**節點 ASP 列、**無**節點出貨、**無** Y_fe／Y_pkg／缺陷密度時序。

反解停在：`隱含節點 ASP = (晶圓營收 × 節點％) ÷ 該節點出貨`；分母不存在。

### B. TSMC 2Q26（2026-07-16 發布；逐字稿頁面 2026-08-28）

新聞稿 PDF＋Management Report＋簡報＋官方法說稿一致：

- 合併營收 NT$1,270.38B／US$40.20B；毛利率 67.7%；12 吋約當出貨 **4,336** 千片（1Q26 4,174；2Q25 3,718）。
- 佔晶圓營收：2nm 3%；3nm 30%；5nm 33%；7nm 11%；≤7nm＝77%。**仍無節點出貨。**
- 平台（佔**淨營收**）：HPC 66%；Smartphone 22%。平台切 ≠ 節點切 ≠ 封裝切。
- CapEx 2026 升至 US$60–64B：「About 70% to 80% … advanced process technologies, about 10% … specialty technologies, and about **10% to 20% … advanced packaging, testing, mask making and others**.」
- 法說 Goldman 問為何不把先進封裝從該 10–20% 桶拆出。C.C. Wei：前後端彈性調度，長期後端約 10–20% 大區間；產品吃測試機比預期多。**公司拒絕把封裝從測試／光罩分離。**
- 2nm 爬坡預期稀釋 2H26 毛利率約 3–4 個百分點——節點對集團毛利率的敘事，不是節點 ASP、不是 Y_fe。
- 產品載具句：內部 product-like vehicle「close to 90% … 256 megabits SRAM yield」＝研發演示，不是前端量產良率時序，不能代入 `Y_fe`。
- 「packaging capacity is so tight that now it limits my customers' growth」＝產能敘事（鄰近 L3-P），不是層別良率。

### C. TSMC 2025 年報（英文）

- 3nm 佔 2025 晶圓營收 24%；2nm 於 4Q25 進入量產「**good yield**」（無數字）；先進＝7nm 及更先進；出貨 15.0 million 12-inch-equiv.。與 20-F 同構，無新增 ASP／良率科目。

### D. 美股可交易對照｜GFS FY25 10-K

- 淨營收 US$6,791M；晶圓製造約 89%；出貨 2.3 million 300mm-equiv.（+10.4%）；公司層 ASP **−10.4%**（特定終端降價＋長期約不足額使用付款減少）。
- 承認「wafer price varies significantly across technology platforms」且受 yield／defect density 影響——**質性**。無節點 ASP 表、無層別良率。
- 含義：美股代工主體可有**公司層** ASP 變動句；L3-A 要的是節點 ASP 與乘積良率，GFS 同樣不給。

### E. 論壇／產業報（明示非申報層；只核生成卡反方，不當 B 端參數）

- 2026-05-14 技術論壇（袁立本；多家一手報導）：5.5 倍光罩 CoWoS 已量產，良率超過 98%。
- 後續 OCP APAC／二手彙編：HVM 98–99%。**不是 10-Q 科目。**
- TrendForce 2026-09-18：CoWoS-L 預期主流至 2028；CoWoS-S 約 2 SoC＋8 HBM；更大模組走 CoWoS-L。**無層別良率、無 ASP。**
- 二手晶圓價帶（Silicon Analysts 等）本輪**不採**為 B 端（生成卡禁令）。

### F. 可重算但不可當節點 ASP 的混合每片

只為展示 mix 用盡可見端，不寫成 `P_waf` 時序、不寫彈性。

- 2025：淨營收 NT$3,809,054M × 約 86% ≈ 晶圓營收 NT$3.28T；÷ 15,022 千片 ≈ **每片約 NT$218k**（約 US$7k，匯率依 20-F US$121,423M／NT$3,809,054M）。此為全節點加權，必低於先進節點二手報價。
- 2Q26：US$40.20B × 約 86% ÷ 4,336 千片 ≈ **每片約 US$8k** 量級，同樣是混合數。
- 官方已把 ASP 上升寫成先進佔比＋出貨。把混合每片的升幅讀成「有效單價彈性 > 1」＝把 mix 當彈性。R3 成立。

`N_die` 的公開錨在設計商／拆解（生成卡：H100 級約 814 mm²），**不在代工 20-F**。面積可進缺陷模型，但不能與官方 `P_waf` 同表對帳。

---

## 對種子與反方

| 主張 | B 端讀後 |
|---|---|
| 恆等式可寫 | 可寫。缺公開分母／層別良率則不可重算 `P_eff` |
| 錯價＝把晶圓 ASP／mix 當有效單價 | 申報層無節點 ASP 可讀；可見端已被 mix 句用盡。錯價句無官方對照錨 |
| R1 官方只給營收％＋總出貨；二手價帶不能當 B 端 | **成立** |
| R2 CoWoS 論壇良率近 1 →「＋先進封裝」子句錯層 | **在論壇層成立**；申報層連該數字都沒有。剩下的面積－缺陷是經典單層，不是新落差的可觀測項 |
| R3 混合每片上升可由 mix 單獨解釋 | **成立**　20-F 原文即如此歸因 |
| R4 Others／CapEx 與測試、光罩捆綁 | **成立**　20-F 86% 句＋法說 10–20% 桶＋CEO 拒拆 |
| R5 切小晶粒／冗餘抵銷面積敏感度 | **未測**　無官方 Y_fe(A) 可對；不當作本輪否證或證實 |

彈性 > 1 的「當且僅當」在本輪兩邊都沒有官方序列，故既不能接受也不能拒絕。

---

## 不開 T／§7-4

進 T 需數值窗與可拒絕之 H1 倍數。本輪可寫入的只有「申報層有節點營收％與合計出貨、無節點 ASP、無層別良率」。不夠把 `P_eff / P_waf` 寫成區間。

§7-4 三題本輪不答（生成卡：轉入個股層時必問；本格不轉、不進 T）。題目本身已由本輪讀數預示答案方向（科目分不出、美股主體同樣不分列、論壇封裝良率近 1 壓縮「多層乘積」窗），但不在本輪作答。

**複查觸發器（沿用生成卡，不改寫）：** 任一美股可交易代工或先進封裝主體於 20-F／10-K／10-Q／20-F 等價，分列節點（或節點族）晶圓 ASP，或分列先進封裝營收與層別良率／報廢，且可與公開晶粒面積對帳。

---

## URL

1. https://investor.tsmc.com/sites/ir/sec-filings/2025_20F%20Report.pdf
2. https://pr.tsmc.com/system/files/newspdf/attachment/e98d0838eea3c47083fb67dbc349c059d8457c25/2Q26%20%28E%29_with%20gudiance_final_wmn.pdf
3. https://investor.tsmc.com/schinese/encrypt/files/encrypt_file/reports/2026-07/6f49632674bd2d0fd48cb65aaf89ec6ab510b559/2Q26%20ManagementReport.pdf
4. https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/0e4d9625c9ef46521afd54002f835e45a9035043/2Q26%20Presentation%20%28E%29.pdf
5. https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
6. https://investor.tsmc.com/sites/ir/annual-report/2025/2025%20TSMC%20Annual%20Report.E.pdf
7. https://www.sec.gov/Archives/edgar/data/1709048/000170904826000022/gfs-20251231.htm
8. https://www.trendforce.com/presscenter/news/20260918-13241.html
9. https://www.chinatimes.com/realtimenews/20260514002305-260410
10. https://winbuzzer.com/2026/05/18/tsmc-cowos-yields-top-98-as-capacity-expands-xcxwbn/

**（完）**
