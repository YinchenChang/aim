<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1-umn-OoxhkuP4f6K0dni2jzzz7rnec02；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h | EMITS: （本檔；Drive work/ 上傳後填 fileId） -->
# L4-A 測一｜B 端實讀（加速器商系統／元件分列；整機商 COGS／毛利附註）

**角色：** ANALYST@GK　**日期：** 2026-09-26　**格：** L4-A（運算硬體系統：系統 BOM＝加速器+HBM+網路+機電）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先加速器商系統／元件分列與整機商 COGS／毛利附註。**禁止只重讀「GPU 出貨成長」與券商 BOM 一句。** 不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T、不入 §1。
**原陳述（生成卡 `1-umn-OoxhkuP4f6K0dni2jzzz7rnec02`）：** 市場把加速器出貨顆數（或加速器商 Data Center／Compute 營收）讀成整機價值的充分統計。可觀測系統售價對應四項 BOM——加速器＋HBM＋網路＋機電；加速器佔 BOM 比重下降時，殘差落入整機商（或 HBM／網通／機電賣方）毛利池，而不是等比例落入加速器顆數。錯價只在把「GPU 出貨量／加速器營收」當成已交付之整機價值。
**守恆式（生成用）：** `P_sys = P_accel + P_hbm + P_net + P_mech + π_oem`；`s_accel = P_accel / (P_sys − π_oem)`。本輪不估參數、不寫 H1。
**否決觸發（生成卡寫給本輪）：** (1) 對 10-K／10-Q／20-F 實讀後，系統 vs 元件與四項 BOM 皆無法從公開項分離，只剩 DC／C&N／AI Server 營收與二手拆解；或 (2) 可見殘差只能寫成加速器商自有 Networking／系統銷售（即接收端不是整機商），且整機商毛利變動由非 BOM 項解釋；或 (3) 公開層已出現穩定可拒絕之 `s_accel` 時序，方向翻負或與「GPU 顆數代理系統價值」不可辨。
**領域最近公開（§7-10）：** NVIDIA Q2 FY27 10-Q（截止 2026-07-26，申報約 2026-08-27）；NVIDIA FY26 10-K／分部表（截止 2026-01-25，acc `0001045810-26-000021`）；NVIDIA Q2 FY27 CFO Commentary（2026-08-26）；SMCI FY26 10-K（截止 2026-06-30，申報 2026-08-31／頁面 2026-09-01）；Dell Q2 FY27 8-K／簡報（2026-09-01／頁面約 2026-09-02）；Dell Q2 FY27 10-Q（截止 2026-07-31，申報 2026-09-08）。下一官方檢查點＝NVIDIA Q3 FY27（約 2026-11）或任一加速器商／整機商 10-K／10-Q／20-F 首次把「系統／機櫃營收」與「加速器元件營收」分列，或把 GPU 轉售成本從整機毛利拆出。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260926_L4-A_generate_GK.md` `1-umn-OoxhkuP4f6K0dni2jzzz7rnec02`（11106 B，2026-09-26T11:32:39Z）；`20260923_HEALTH_CL.md` `1_urT6I7RovcM73D3IBTKGIk6RY1z9nC0`；`20260923_HEALTH_GK.md` `1byQGbjCmIT1orLv51moyAH5xnABFO95e`
- query/：`ARCH_dead.md` `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`；`ARCH_matrix.md` `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`；`CHARTER_HIST.md` `1DKg3HUr-zOWw20OmNe1aDpWT_izDwdiT`；`INDEX.json` `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`；`MECH.md` `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-09-26T11:29:51Z role SCOUT）
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-09-26；§1 無 L4-A；§3 L4［A］＝已生成）
- matrix L4［A］＝已生成（3h 快照；L4［P］＝已測｜不進 T，測一 `18EssPf0uT4BUyR44fEkRKMKyP-iW3jx0`）。INDEX L4 註＝P 已測、A/I 已生成；無獨立 L4-A 測一 fileId
- 3h 快照 `1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj` L4-A B 端僅指名「整機商 BOM 拆解；加速器商系統營收比重」
- 本輪上傳前 work/ 無同名 `20260926_L4-A_test1_GK.md`
- work 主動維護：三檔皆未吸收進現行 FUNNEL／CHARTER（生成卡待測一後由 SCOUT 對齊；HEALTH 兩份非本輪標的）。本輪不建 `DONE_`。

---

## 終態

**不通過。不進 T。** 機制（系統售價＝四項 BOM＋整機商毛利；`s_accel` 移動改寫誰拿殘差）未被否證。失敗在可觀測性——加速器商給的是 C&N／Data Center 平台營收，年頻可再拆 DC Compute vs Networking，文內有「system shipments」一句；**無**系統／DGX／機櫃對 GPU 元件之美元分列。整機商給的是 AI Server／GPU & Super Racks 營收＋合併（或分部營業）毛利率／營業利益率；COGS 承認 GPU 為成本大宗，**無** GPU 轉售成本列、**無**四項 BOM。券商四代機架表本輪不採為參數。

| 測試項 | 結果 |
|---|---|
| B 端已實讀（非指名；非只讀 GPU 出貨成長／券商 BOM 一句） | **通過**　NVIDIA Q2 FY27 10-Q＋CFO Commentary＋FY26 10-K／R25 分部表；SMCI FY26 10-K；Dell Q2 FY27 8-K／IR 簡報＋10-Q |
| 加速器商系統 vs 元件美元可分列 | **不通過**　可見端＝C&N／DC；年頻 DC Compute vs Networking。無系統／機櫃 vs GPU 元件列 |
| 四項 BOM 可從公開項分離 | **不通過**　無官方加速器／HBM／網路／機電時序。HBM 在加速器 ASP 內或在記憶體賣方，兩邊皆無本格分母 |
| 整機商 COGS 可拆 GPU 轉售 vs 非 GPU | **不通過**　SMCI：GPU「increasing portion of cost of sales」＋GPU servers／HPC／rack-scale 帶動 COGS 年增；無轉售成本列。Dell：AI-optimized servers 營收分列，COGS 不分列 |
| `s_accel` 下降進入整機商可見毛利池 | **不可檢**　無 `s_accel` 官方時序。整機商 ％ 與美元池不可互譯；可見殘差可寫進加速器商自有 Networking／「full-scale datacenter solutions」 |
| 「GPU 顆數 vs 系統價值」可拒絕 1:1 | **不存在**　兩邊皆無官方對照錨 |
| 否決觸發 (1) | **觸發** |
| 否決觸發 (2) | **觸發**　Networking／系統銷售在加速器商側；整機商毛利變動由 mix／定價／製造費用解釋 |
| 否決觸發 (3) | **未觸發**　`s_accel` 序列不存在，方向未翻負 |
| 升格 T | **否** |

失效歸因（§7-2）：不是檢索失敗。失敗在量綱——所需量（系統 vs 元件美元、四項 BOM、GPU 轉售成本、與同期機櫃 ASP 對帳）不是所讀之量（C&N／DC、AI Server 營收、合併 GM％、ISG 營業利益率）。現況檔名＝上列 work／query。複查觸發器＝生成卡原文（見下）。停。

本格不入 §1。不改正本（對齊屬 SCOUT）。

---

## 已實讀載體

### A. 加速器商季報｜NVIDIA Q2 FY27（截止 2026-07-26；10-Q acc `0001045810-26-000075`）

Note 13 可報告分部（百萬美元）：

| | 三個月迄 Jul 26, 2026 | 三個月迄 Jul 27, 2025 | 六個月迄 Jul 26, 2026 |
|---|---|---|---|
| Compute & Networking | 88,299 | 41,331 | 162,850 |
| Graphics | 7,922 | 5,412 | 14,987 |
| Total | 96,221 | 46,743 | 177,837 |

市場平台：Data Center **89,023**（同比 +117%）；其下 Hyperscale 48,710／ACIE 40,313。**本季 10-Q 無 DC Compute vs Networking 美元拆。**（Q1 FY27 評論稿仍有 DC compute 60.4B／networking 14.8B；Q2 評論稿與 10-Q 皆未續列。）

MD&A 原句：「**Blackwell continued to account for the majority of our system shipments.**」「Vera Rubin, began production shipments in the third quarter of fiscal year 2027。」「We will be shipping both Blackwell and Rubin **systems**.」C&N 定義＝「Data Center accelerated computing and **networking platforms** and AI solutions and software」。產品句把 processors、interconnects、software、**systems** 寫在同一平台裡。

毛利率 75.0%（Q2／H1 FY27）；YoY 改善歸因 Blackwell Ultra mix。COGS「consists primarily of the cost of semiconductors … board and device costs … **memory and component costs**」——記憶體在加速器商自己的成本裡，不是整機商四項 BOM 的獨立官方列。

R1 在本季已成立：可見端是 C&N／DC 平台營收＋「system shipments」質性句。**不是**系統 vs 元件美元。C&N ≠ 系統營收；DC ≠ 加速器元件；Compute vs Networking（即便年頻存在）≠ 加速器 vs 非加速器 BOM。

### B. 加速器商年報｜NVIDIA FY26 10-K（截止 2026-01-25；R25／本文）

可報告分部：C&N FY26 **193,479**／FY25 116,193／FY24 47,405。Graphics FY26 22,459。

終端市場 Data Center FY26 **193,737**，其下：

| | FY26 | FY25 | FY24 |
|---|---|---|---|
| DC Compute | 162,361 | 102,196 | 38,950 |
| DC Networking | 31,376 | 12,990 | 8,575 |

Networking FY26 +142%。MD&A：DC computing「driven by demand for our Blackwell computing platform」；DC networking「driven by the introduction and continued ramp of **NVLink compute fabric for GB200 and GB300 systems** and the growth of Ethernet and InfiniBand platforms」。

質性句（對本格打擊大於數字）：「Gross margin decreased to 71.1% in fiscal year 2026 from 75.0% … **as our business model transitioned from offering Hopper HGX systems to Blackwell full-scale datacenter solutions**」（另含 H20 存貨／承諾 4.5B）。「Our Data Center infrastructure **systems** include supercomputing platforms and servers, bringing together … GPUs, CPUs, interconnects …」「Data Center systems are extreme co-designed with the GPU, CPU, NVLink switch, DPU, NIC, and scale-out networking」。

年頻 Compute vs Networking **存在**，系統 vs 元件 **仍不存在**。Networking 31.4B 是加速器商自己收走的可見殘差，不是整機商毛利池。R2 用盡可見端。

### C. 整機商年報｜SMCI FY26 10-K（截止 2026-06-30；申報頁 2026-08-31）

單一營運分部。淨銷 **39,063.1**（千美元計為 39,063,072）；毛利 4,227.3；**GM 10.8%**（FY25 11.1%；FY24 13.8%）。毛利額年增約 1,797，％ 下降。官方解釋：「**primarily due to our strategy to offer competitive pricing to gain market share, change in product and customer mix, and higher manufacturing related expenses.**」——三項皆非 `s_accel`。

產品句：Server and Storage Systems 年增主項＝「Hyper Servers, **GPU & Super Racks of $15,261.5 million or 83.4%** compared to prior year … primarily related to our GB200, and GB300 systems」。這是產品線出貨／開立帳單成長額，**不是** GPU 轉售成本、**不是**四項佔比。

COGS：年增 15,293.7（+78.3%），「primarily driven by an increase of $14,699.8 million or 73.3% in certain products including **GPU servers, HPC systems, and rack-scale solutions**」。風險因素：「**GPUs have represented an increasing portion of our cost of sales.**」有方向、無金額、無「轉售 vs 自製／機電／網路」拆。DCBBS 文案把「individual GPUs and networking switches to complete racks」寫成產品範圍，不是科目。

存貨 12,896（成品 10,276／在製 1,678／原料 942）。一供應商佔進貨 63.1%。一客戶佔銷售 28.1%。皆不能還原 `s_accel`。

R3：GM％ 走低與「佔比下降則整機商池上升」同向或反向都無法拒絕——％ 壓縮時美元池仍升。錯價句無官方對照錨。

### D. 整機商季報｜Dell Q2 FY27（8-K 2026-09-01；簡報頁約 2026-09-02；10-Q 截止 2026-07-31）

ISG 淨銷 Q2 **31,782**：AI-Optimized Servers **16,401**（+100%）；Traditional Servers and Networking 10,531（+122%）；Storage 4,850（+26%）。YTD ISG 60,791，AI Server YTD 32,533。訂單 60.9B、期末 backlog 95.0B。FY27 AI Server 指引上修至 74B。

ISG 營業利益 Q2 **4,781**（佔 ISG 淨銷 **15.0%**，同比 8.8%）；YTD 7,836（12.9%）。10-Q：YTD 公司產品毛利率升、但「**partially offset by shift in mix towards AI-optimized servers**」；YTD ISG 營業利益率升，因費用率下降「**outpacing decline in gross margin rate from mix shift to AI-optimized servers**」。Q2 單季產品毛利率升主因「disciplined pricing」，**無** AI Server 單獨 GM。

FY26 起才把 AI-optimized servers 從 servers and networking 拆出（營收列）。**仍無** GPU 轉售、**無**四項 BOM、**無** AI Server 毛利列。

Dell 可見端＝AI Server 營收＋ISG 營業利益率＋「AI mix 壓 GM％」。與 SMCI 同一量綱缺口。

### E. 明示不採

券商／產業四代機架 BOM（H100→Vera Rubin；生成卡已點名「GPU 佔比自約六成降至約五成」）**不是 10-K**。本輪不疊為 `s_accel`、不據以拒絕官方科目。論壇機隊句不採。

可寫但不可當對帳的佔比試算（明示＝非官方）：若誤把 NVIDIA DC Compute／DC 總額當 `s_accel`，得到的是加速器商平台組合，不是整機 BOM 佔比；分母缺 `P_hbm`／`P_mech`／`π_oem`，亦不能與 SMCI 10.8% 或 Dell ISG 15.0% 對帳。本輪到此停。

---

## 對種子與反方

| 主張 | B 端讀後 |
|---|---|
| 恆等式可寫 | 可寫。缺系統 vs 元件與四項官方列則不可重算 `s_accel` |
| 錯價＝把 GPU 出貨／加速器營收當已交付整機價值 | 可見端已被 C&N／DC／AI Server 營收＋合併 GM 用盡。錯價句無官方對照錨 |
| R1 所需量不是所讀之量 | **成立**　系統／元件與四項 BOM 皆非科目 |
| R2 殘差已被加速器商 Networking／系統銷售收走 | **在可見端成立**　FY26 Networking 31.4B（+142%）；「HGX systems → full-scale datacenter solutions」；Q2「system shipments」是加速器商自己的出貨句 |
| R3 ％ 與美元池不可互譯 | **成立**　SMCI GM％↓、毛利額↑；Dell AI mix 壓 GM％、ISG 營業利益額與％↑（費用槓桿）。官方歸因＝定價／mix／製造，不是 `s_accel` |
| R4 券商 BOM 把 HBM 從加速器拆出，但加速器 ASP 已含 HBM | **本輪不採二手表**；NVIDIA COGS 已列 memory and component costs，雙計風險在官方層已存在、無法校正 |
| R5 滑到「買整機／賣加速器」或 C-I3′ | **本輪不選券、不開 T**。C-I3′（`ARCH_dead` #14）構成不同，不合併 |

「GPU 顆數 vs 系統價值」在本輪兩邊都沒有官方序列，故既不能接受也不能拒絕 1:1。

---

## 不開 T／§7-4

進 T 需數值窗與可拒絕之 H1 倍數。本輪可寫入的只有「C&N／DC 平台營收、年頻 Compute vs Networking、AI Server／GPU & Super Racks 營收、合併 GM％、ISG 營業利益率」。不夠把 `s_accel` 或 `π_oem` 寫成財富倍數窗。

§7-4 三題本輪不答（生成卡：轉入個股層時必問；本格不轉、不進 T）。題目本身已由本輪讀數預示方向（C&N／ISG／Server and Storage 再拆不出系統 vs 元件或 GPU 轉售；美股可交易主體存在但恆等落在未分列科目；加速器商把機櫃收進自有系統銷售已在質性句出現），但不在本輪作答。

**複查觸發器（沿用生成卡，不改寫）：** 任一美股可交易加速器商或整機商於 10-K／10-Q／20-F，分列系統／機櫃營收與加速器元件營收，或分列 GPU 轉售成本與非 GPU COGS，且可與同期公開機櫃 ASP 對帳。

---

## URL

1. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
2. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm
3. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
4. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/R25.htm
5. https://www.sec.gov/Archives/edgar/data/1375365/000137536526000022/smci-20260630.htm
6. https://www.sec.gov/Archives/edgar/data/1571996/000157199626000039/exhibit991earnings8kq2fy27.htm
7. https://investors.delltechnologies.com/static-files/5d15be71-1d9a-45ec-8308-8987fb41084d
8. https://www.sec.gov/Archives/edgar/data/1571996/000157199626000046/dell-20260731.htm
9. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/0001045810-26-000051.txt
