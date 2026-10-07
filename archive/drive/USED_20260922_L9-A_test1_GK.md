<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1jTOPPqrGjFJjVjpMlVNaWf-eMM46enKh；1cDBz8987NXrbhf4DGliGPCJGQyXX7JRW；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1Kc4TQJPVQUq6DzkKlGVognxR5DXhuUEJ；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70 | EMITS: （本檔；Drive work/ 上傳後填 fileId） -->
# L9-A 測一｜B 端實讀（訂閱毛利額橫斷面 vs 席次／推論+支援）

**角色：** ANALYST@GK　**日期：** 2026-09-22　**格：** L9-A（受規管 HITL：會計恆等）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不開 T。不併殺 L9-P／C-A1／C-I5；不生成 L9-I。
**原陳述（生成卡 `1jTOPPqrGjFJjVjpMlVNaWf-eMM46enKh`）：** 席次定價下，交付一席的現金成本是推論加支援，不是合併毛利率；C-A1 已證明 `k` 與毛利率百分點同量級而不可分列。改讀多家已分列之**毛利額**橫斷面離散度，要把同一恆等從「比率解析度不夠」換成「美元額可相比」。恆等式本身為真；錯價只在把合併毛利率（或未分列之訂閱毛利額）當成每席次交付成本。
**否決觸發（生成卡寫給本輪）：** (1) 可重算序列只能借用 C-A1 之 `k`／合併毛利率，或無法與購併攤銷／產品組合分離；或 (2) 「席次數」與「推論+支援」無法在同一張已申報表同時出現，離散度只剩公司規模敘事。
**領域最近公開（§7-10）：** CRM Q2 FY27 新聞稿 2026-08-26／Exhibit 99.1 2026-08-27；NOW Q2 2026 新聞稿 2026-07-22；VEEV FY26 10-K 2026-03-20、10-Q（期 2026-07-31）2026-08-28；WDAY FY26 業績 2026-02-24。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260921_L9-A_generate_GK.md` `1jTOPPqrGjFJjVjpMlVNaWf-eMM46enKh`；`20260921_HEALTH_GK.md` `1RAClJHocNj0EobBYlD7Rp9dbDwkdEaRw`（晨稿，對午後正本已 stale）
- inbox_GK／inbox_CL：空
- query 五檔在；MECH last_sync_utc 2026-09-21T05:53:45Z role ANALYST
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`；matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`（L9［A］＝已生成、不入 §1）

---

## 終態

**不通過。不進 T。** 機制（會計恆等：每席次交付成本＝推論+支援）未被否證。失敗在申報層解析度——可見的是合併訂閱毛利額，不是「推論+支援」與「席次」同表。

| 測試項 | 結果 |
|---|---|
| B 端已實讀（非指名） | **通過**　CRM Q2 FY27 PR＋Ex.99.1；NOW Q2 2026 PR／GAAP–non-GAAP 調回；VEEV FY26 10-K＋Q2 FY27 10-Q；WDAY FY26 業績作第四橫斷面 |
| 多家已分列「訂閱毛利額」季頻存在 | **通過（公司層）**　四家均可由訂閱營收−訂閱 COGS 算出美元額 |
| 毛利額按推論／支援／AI 交付分列 | **不通過**　無此科目 |
| 席次數（或席次等效，且非 AWU／ACV 翻版）同表 | **不通過**　CRM 有 AWU 無席次；NOW 有 AI ACV 無席次；VEEV／WDAY 無席次時序 |
| 離散度可與規模／mix／購併攤銷分離 | **不通過**　離散度＝公司規模；NOW GAAP vs non-GAAP 差在購置攤銷 |
| 否決觸發 (1) | **觸發**　可重算序列＝合併訂閱毛利額（C-A1 同桶換單位） |
| 否決觸發 (2) | **觸發**　席次與推論+支援不同表 |
| 升格 T | **否** |

失效歸因（§7-2）：不是檢索失敗。失敗在量綱——3h 分子（推論+支援）與分母（席次）在已上市應用層 10-Q／10-K／業績表不同時出現；改讀毛利額只把 C-A1 的比率換成美元，未產生新觀測。現況檔名＝上列 work／query。複查觸發器＝生成卡原文（見下）。停。

不把「未分列」偷渡為 L9-I（R5）。本格不入 §1。

---

## 已實讀載體

### A. CRM｜Q2 FY27（期 2026-07-31，發布 2026-08-26／27）

- 訂閱與支援營收 US$10,820M；訂閱與支援 COGS US$2,021M → **訂閱毛利額 US$8,799M**（自行相減；新聞稿不印毛利額）。
- 購置無形資產攤銷列入 COGS：三個月 US$234M（對照期 US$150M）。扣掉攤銷後仍是合併託管／支援／人員桶，不是推論 vs 支援。
- 營收拆開（非毛利額）：Agentforce Apps US$7,193M；Data 360, Headless Platform, and Other US$3,618M。FY27 Q1 起改分類，不是交付成本分列。
- Informatica 對訂閱與支援貢獻 US$440M；指引另含待完成 Contentful／Fin。mix／M&A 進入營收成長，不進入每席次成本。
- Agentforce ARR 逾 US$1.5B（Q2 起含 AI offerings、Slackbot、Headless 360）；Agentforce+Data 360 ARR 近 US$3.9B。ARR＝契約年化，不是毛利額、不是席次。
- AWU：累計 70 億、單季 32 億（+97% Q/Q）。**產出單位＝消費計次，明文不是席次。**
- 新聞稿／Ex.99.1：**無**席次數、**無** Agentforce 毛利額、**無**「推論+支援」分列。

### B. NOW｜Q2 2026（期 2026-06-30，發布 2026-07-22）

- 訂閱營收 US$3,877M；GAAP 訂閱毛利額 **US$2,847M**（73.5%）；non-GAAP **US$3,123M**（80.5%）。
- GAAP→non-GAAP 訂閱毛利調回：SBC US$96M＋購置無形攤銷 US$177M（對照期 US$23M）＋遣散 US$3M。GAAP 訂閱 COGS＝US$1,030M，其中攤銷同比跳升＝購併層，不是每席次推論。
- 指引原文把毛利率走勢寫成 hyperscaler 夥伴＋客戶 AI 採用——合併桶。
- ServiceNow AI ACV 跨過 US$1B。ACV≠席次、≠毛利額。
- **無**席次數、**無** Now Assist／推論／支援成本分列。

### C. VEEV｜FY26 10-K（2026-03-20）＋Q2 FY27 10-Q（期 2026-07-31，2026-08-28）

- FY26：訂閱營收 US$2,684.2M；訂閱成本 US$362.9M → **訂閱毛利額 US$2,321.3M**。產品拆開是 Commercial vs R&D/Quality **營收**，不是毛利額。
- Q2 FY27：訂閱 US$766.8M；訂閱成本 US$105.7M → **訂閱毛利額 US$661.1M**。
- 10-K 原文：訂閱成本＝第三方運算基礎設施（AWS **與** Salesforce）＋託管／支援人員（含 data stewards）＋資料取得＋設備軟體＋分攤。支援與基礎設施在同一科目；**無**推論項、**無**席次。

### D. WDAY｜FY26（期 2026-01-31，業績 2026-02-24；第四橫斷面）

- 訂閱營收 US$8,833M；訂閱成本 US$1,531M → **訂閱毛利額 US$7,302M**。
- 10-K 驅動句：訂閱由客戶數、各客戶 **workers**、訂閱應用、價格驅動。workers 是敘事驅動因子，年報未給可重算席次／worker 時序與訂閱成本同表。
- 無推論 vs 支援分列。Paradox／Sana 購併進入 backlog，同屬 mix／M&A。

### E. 橫斷面（同為「訂閱毛利額」，不同窗，只證明規模）

| 主體 | 窗 | 訂閱毛利額 | 同表席次 | 同表推論+支援 |
|---|---|---|---|---|
| CRM | Q2 FY27 | US$8,799M | 無（有 AWU） | 無 |
| WDAY | FY26 | US$7,302M | 無（有 workers 敘事） | 無 |
| NOW | Q2 2026 | US$2,847M GAAP | 無（有 AI ACV） | 無 |
| VEEV | Q2 FY27 | US$661M | 無 | 無（基礎設施+支援合一） |

離散度排序＝營收規模排序。扣 NOW／CRM 購置攤銷只縮小 GAAP–non-GAAP 缺口，不產生每席次序列。

---

## 對種子與反方

| 主張 | B 端讀後 |
|---|---|
| 恆等式可寫 | 可寫。缺公開分子與分母則不可重算每席次 |
| 改讀毛利額＝新解析度 | **不成立**　得到的是 C-A1 合併桶的美元形 |
| R1 單位換算不是新觀測 | **成立** |
| R2 離散度＝規模／mix／攤銷 | **成立** |
| R3 席次在申報層缺；AWU≠席次 | **成立**　CRM 自己把產出單位寫成 AWU |
| R4 不得從後門載入 `k`／核可率 | **遵守**　本輪不用 token／HITL 工時 |
| R5 未分列≠L9-I | **遵守**　停在本格可觀測性 |

---

## 不開 T／§7-4

進 T 需把 H1 寫成財富倍數窗。本輪可寫入的只有「四家有合併訂閱毛利額、無席次、無推論+支援」。不夠把離散度換成可載入參數。

§7-4 三題本輪不答（生成卡：轉入個股層時必問；本格不轉、不進 T）。

**複查觸發器（沿用生成卡，不改寫）：** 任兩家美股上市應用層主體於同一季之 10-Q／10-K 同期分列（i）推論或 AI 交付直接成本與支援成本之美元額、（ii）席次數或可對齊之席次等效單位，且該單位不是已殺 L9-P 之核可率／HITL 工時翻版。

---

## URL

1. https://www.salesforce.com/news/press-releases/2026/08/26/fy27-q2-earnings/
2. https://www.sec.gov/Archives/edgar/data/1108524/000110852426000187/crm-q2fy27xexhibit991.htm
3. https://investor.salesforce.com/financials/
4. https://www.sec.gov/Archives/edgar/data/1373715/000137371526000072/0001373715-26-000072.txt
5. https://s205.q4cdn.com/537566246/files/doc_news/ServiceNow-Reports-Second-Quarter-2026-Financial-Results-2026.pdf
6. https://www.sec.gov/Archives/edgar/data/1393052/000139305226000014/veev-20260131.htm
7. https://www.sec.gov/Archives/edgar/data/1393052/000139305226000036/0001393052-26-000036.txt
8. https://www.sec.gov/Archives/edgar/data/0001327811/000132781126000010/wday-01312026x991.htm

**（完）**
