<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1a1H-GCf5gLXusmySde1tJkm-qEmXlJVS；1zTFfvQVcvJr4jZmz_mZzznOsnZucfR3y；1jTOPPqrGjFJjVjpMlVNaWf-eMM46enKh；1cDBz8987NXrbhf4DGliGPCJGQyXX7JRW；1Kc4TQJPVQUq6DzkKlGVognxR5DXhuUEJ；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h | EMITS: （本檔；Drive work/ 上傳後填 fileId） -->
# L9-I 測一｜B 端實讀（SKU／edition 重組頻率 vs 未分列＝誘因）

**角色：** ANALYST@GK　**日期：** 2026-09-22　**格：** L9-I（受規管 HITL：誘因）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不開 T。不併殺 L9-P／L9-A／C-A1／C-I5。
**原陳述（生成卡 `1a1H-GCf5gLXusmySde1tJkm-qEmXlJVS`）：** 應用層賣方把推論與支援成本折進既有席次／版本 SKU，使合併毛利率看起來穩定；「AI 未分列」是揭露選擇而非資訊缺失。B 端＝SKU 重組／改版公告頻率（對照是否同期出現獨立 AI 成本或可拒絕 AI SKU 營收）。
**否決觸發（生成卡寫給本輪）：** (1) SKU 重組／改版在已上市應用層 10-K／10-Q 或可對齊之官方價目檔不形成可點算時序，只剩單次產品文；或 (2) 可觀測之「未分列」只能沿 C-A1／L9-A 已走路徑（合併毛利額／`k`）解釋，無法把「揭露選擇」寫成獨立診斷項；或 (3) 公開層已出現穩定、可拒絕之獨立 AI 成本／SKU 列，使「未分列＝誘因輸出」方向翻負。
**領域最近公開（§7-10）：** CRM 版本簡化文 2026-09-03＋價目頁當日快照；CRM Q2 FY27 PR／Ex.99.1 2026-08-26／27；NOW 官方 ITSM Foundation 產品頁＋Community 2026-05-28；NOW Q2 2026 2026-07-22；VEEV FY26 10-K 2026-03-20、產品頁 Vault AI。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260922_L9-I_generate_GK.md` `1a1H-GCf5gLXusmySde1tJkm-qEmXlJVS`（9315 B）；`20260921_HEALTH_GK.md` `1RAClJHocNj0EobBYlD7Rp9dbDwkdEaRw`；`push_l9a_align.py` `1OeD0rkMsMufb-x8hr9bo07A1b7jqm1qs`
- inbox_GK／inbox_CL：空
- query 五檔在；MECH last_sync_utc 2026-09-22T06:35:13Z role ANALYST
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`；matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`（§3 L9［I］仍【未生成】，本輪不改）
- L9-A 測一已 USED_ `1zTFfvQVcvJr4jZmz_mZzznOsnZucfR3y`

---

## 終態

**不通過。不進 T。** 機制（賣方有誘因把 AI 折進席次 SKU）未被否證。失敗在可觀測性——可見的是單次產品文／現行價目快照／營收重分類附註，不是 10-K／10-Q 或可對齊官方價目檔上的可點算改版時序；「未分列」仍落在 C-A1／L9-A 的合併桶。

| 測試項 | 結果 |
|---|---|
| B 端已實讀（非指名） | **通過**　CRM 新聞室＋官方價目＋Q2 FY27 PR／Ex.99.1／FY26 10-K 附註；NOW 官方產品頁＋Community＋Q2 2026 PR；VEEV FY26 10-K＋Vault AI 產品頁 |
| 10-K／10-Q 出現「SKU／edition 重組次數」序列 | **不通過**　三家皆無此科目 |
| 官方價目檔形成可對齊之歷史時序（非當日快照） | **不通過**　CRM 有現行價目頁；NOW／VEEV 無公開價目 |
| 手拼事件曆可數（新聞室／社群） | **弱通過（非申報層）**　CRM 約 2–3 次官方事件／12 個月；NOW 一次 2026-04 重包；VEEV 0 |
| 「未分列」可寫成獨立於毛利額／`k` 的診斷 | **不通過**　缺的仍是 AI 成本列 |
| 穩定可拒絕之獨立 AI **成本**列 | **不存在**　消費計價 SKU 存在（R5），不構成成本列 |
| 否決觸發 (1) | **觸發** |
| 否決觸發 (2) | **觸發** |
| 否決觸發 (3) | **未完整觸發**　有獨立消費 SKU／AI ARR 敘事，無獨立 AI 成本列；方向未翻負 |
| 升格 T | **否** |

失效歸因（§7-2）：不是檢索失敗。失敗在量綱——3h 分母「SKU 重組／改版公告頻率」在申報層不存在；官方價目不是檔案化時序。現況檔名＝上列 work／query。複查觸發器＝生成卡原文（見下）。停。

本格不入 §1。不改正本（對齊屬 SCOUT）。

---

## 已實讀載體

### A. CRM｜官方產品文＋價目＋申報

**事件（官方，非頻率表）：**
- 2026-09-03 新聞室：Enterprise／Unlimited／Agentforce 1 → Core／Advanced／Max（US$195／395／550 每席每月）。原文「consolidating what previously required piecing together multiple SKUs」；Max＝Agentforce 1 同價、「nearly 60% more value」；既有客戶舊版價不變。Core／Advanced／Max 各含 50 萬／100 萬／275 萬 Flex Credits／org／年。
- FY26 10-K 附註：FY26 第三季把服務品項**改名**為 Agentforce；「There were no changes in the allocation of revenue between these service offerings as a result of this change。」改名 ≠ 重組次數。
- FY27 Q1 起訂閱營收重分類為 Agentforce Apps vs Data 360, Headless Platform, and Other（管理視角，不是 SKU 計數、不是成本列）。Q2 FY27：Agentforce Apps US$7,193M；Data 360… US$3,618M。
- Q2 FY27 PR：Agentforce ARR 逾 US$1.5B（Q2 起含 AI offerings、Slackbot、Headless 360）；「Bookings from Agentforce One Edition and Agentforce for Apps, premium SKUs… more than doubled Q/Q」——SKU **名稱**入新聞稿，不是改版頻率。

**現行價目快照（2026-09-22 讀）：**
- https://www.salesforce.com/sales/pricing/ 列 Free／Starter／Pro／Core／Advanced／Max。Core 起含 Flex Credits。同頁仍標部分 Agentforce 能力「available for purchase」——與 09-03「打進每一層」文案並非同一檔案版本，價目頁是活頁不是歸檔時序。
- https://www.salesforce.com/agentforce/pricing/ 仍列獨立消費層：Flex Credits US$500／10 萬；Conversations US$2；add-on 約 US$125／席／月；Agentforce User License US$5。**席次層可折、消費層仍獨立（R5）。**

**申報層沒有的：** edition 重組次數、價目樹版本號、獨立 AI 成本列。Agentforce ARR／AWU＝契約／產出敘事，L9-A 已用過，本格不得再當頻率分母。

### B. NOW｜官方產品頁＋Community＋業績（無價目檔）

- 官方產品頁存在 ITSM Foundation（以及 Advanced／Prime 敘事）：AI 導向進線／草稿寫進 Foundation 賣點，無公開美元價。
- Community 2026-05-28（Giga Sage，**非 10-K、非法務價目**）：April 2026 起 ITSM＝Foundation／Advanced／Prime；「AI is bundled into every tier with an Assist allocation」；Prime 才可建 net-new custom AI skills。另有 CSM／ITOM 同期改包之社群文，同屬貢獻者文。
- 夥伴轉述（The Cloud People 2026-06-26 等）：五層→三層、舊 SKU EOS 2026-07-01。EOS 日期**未**在本輪所讀之 Community 主文出現；不得把轉述當申報層。
- Q2 2026 PR：訂閱毛利 GAAP US$2,847M；AI ACV 跨 US$1B。無 Now Assist 獨立 SKU 營收、無改版次數、無 Assist 池餘額時序。
- **無**官方可下載之歷史價目檔。可點算者＝2026-04 一次重包事件簇。

### C. VEEV｜FY26 10-K＋產品頁

- 10-K（期 2026-01-31，2026-03-20）：Veeva AI／Vault AI Agents「integrated」於應用。訂閱成本＝第三方運算基礎設施（AWS **與** Salesforce）＋託管／支援人員＋資料取得＋設備軟體＋分攤。LLM 使用成本在敘事上落入研發，不是訂閱成本分列、不是 AI SKU 營收。
- 無 SKU、無 edition 梯、無改版次數。產品頁稱標準 Agents 一年三釋，是發版節奏不是商業 SKU 重組。
- 第三方估價與「early adopter 免費／GA 價未定」不進本格分母。

### D. 事件曆（手拼；明示＝非申報時序）

| 主體 | 可指日之官方／準官方事件 | 同期獨立 AI 成本列 | 同期獨立 AI 營收／消費 SKU |
|---|---|---|---|
| CRM | 2026-09-03 三版重包；FY26 Q3 改名（分配不變）；FY27 Q1 營收重分類 | 無 | 有：Flex Credits／Conversations／add-on；Agentforce ARR |
| NOW | 2026-04 三層重包（產品頁＋Community） | 無 | 有敘事：Assist 池；AI ACV（非 SKU 營收列） |
| VEEV | 無商業 edition 重包 | 無（LLM∈R&D 敘事） | 無獨立 AI 營收列 |

兩家同年可點算「重組次數 × 是否出現獨立 AI **成本**列」＝次數可手拼、成本列三家皆無。生成卡要求的對照（ii）在成本端全空，只剩 ARR／ACV／消費計價——生成卡已禁止把該敘事當本格分母翻版。

---

## 對種子與反方

| 主張 | B 端讀後 |
|---|---|
| 未分列是選擇不是遺漏 | 可陳述。選擇的可見輸出是產品文與現行目錄，不是申報頻率 |
| 改版頻率可作指名載體 | **不成立於申報／價目檔**　只成立於手拼新聞室事件 |
| R1 簡化＝降搜尋成本／讓利 | **成立於文案**　CRM「more value at no additional cost」；不能由此否證藏成本，也不能由此得到時序 |
| R2 分母在 10-K／10-Q 不存在 | **成立**　觸發 (1) |
| R3 未分列已被 C-A1／L9-A 走完 | **成立於診斷項**　本輪新看到的是包裝事件，不是新的未分列量綱；觸發 (2) |
| R4 不得載入 C-I5 買方 NRR | **遵守** |
| R5 消費計價仍獨立 | **成立**　CRM Flex Credits／Conversations／add-on 仍在價目頁；NOW Assist 池仍是消費層。故「藏進既有 SKU」不是全稱；觸發 (3) 未完整觸發 |

---

## 不開 T／§7-4

進 T 需把 H1 寫成財富倍數窗。本輪可寫入的只有「兩家有單次重包文、一家無；三家無改版頻率序列、無 AI 成本列」。不夠把揭露選擇寫成可載入參數。

§7-4 三題本輪不答（生成卡：轉入個股層時必問；本格不轉、不進 T）。

**複查觸發器（沿用生成卡，不改寫）：** 任兩家美股上市應用層主體於同一年之 10-K／10-Q 或與其同期之官方價目／版本公告，可點算（i）SKU／edition 重組次數或範圍與（ii）是否同期出現獨立 AI 交付成本或可拒絕之 AI SKU 營收，且該序列不是 Agentforce ARR／AI ACV 敘事之翻版。

---

## URL

1. https://www.salesforce.com/news/stories/salesforce-simplifies-editions-2026/
2. https://www.salesforce.com/sales/pricing/
3. https://www.salesforce.com/agentforce/pricing/
4. https://www.salesforce.com/news/press-releases/2026/08/26/fy27-q2-earnings/
5. https://www.sec.gov/Archives/edgar/data/1108524/000110852426000187/crm-q2fy27xexhibit991.htm
6. https://www.sec.gov/Archives/edgar/data/1108524/000110852426000060/crm-20260131.htm
7. https://www.sec.gov/Archives/edgar/data/1108524/000110852426000127/crm-20260430.htm
8. https://www.servicenow.com/products/itsm/foundation.html
9. https://www.servicenow.com/community/itsm-articles/itsm-licensing-in-april-2026-foundation-advanced-and-prime-in/ta-p/3544380
10. https://www.morningstar.com/news/business-wire/20260722644148/servicenow-reports-second-quarter-2026-financial-results
11. https://www.sec.gov/Archives/edgar/data/1393052/000139305226000014/veev-20260131.htm
12. https://www.veeva.com/products/vault-ai/

**（完）**
