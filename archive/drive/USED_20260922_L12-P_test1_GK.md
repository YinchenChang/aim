<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1BrfvvlzGeI8k-6U34_VwQG_JUj9_69J9；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h | EMITS: （本檔；Drive work/ 上傳後填 fileId） -->
# L12-P 測一｜B 端實讀（標準規定時長 × 公開證書庫發證數）

**角色：** ANALYST@GK　**日期：** 2026-09-22　**格：** L12-P（監理與法制：物理測試時長底板）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。強制一問＝具名標準時長 `[V]` × UL／BV（或同等）公開證書庫發證數 → 物理測試小時存量。**禁止只讀 TAT。** 不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不開 T。不併殺 L12-A／L12-I。
**原陳述（生成卡 `1BrfvvlzGeI8k-6U34_VwQG_JUj9_69J9`）：** 有一截 TIC 營收被標準寫死的物理暴露時長閘制；錯價只在把行政 TAT／文件週期縮短讀成物理底板也在縮。前次 4f 測一把 TAT 當底板，量錯。
**否決觸發（生成卡寫給本輪）：** (1) UL／BV（或同等）公開證書庫＋具名標準時長表實讀後，仍無法形成可點算之「標準時長 × 發證數」時序或存量，只剩單張證書查詢；或 (2) 乘積無法對齊任一已上市 TIC 之公開營收／毛利科目，使「受物理時長閘制之營收佔比」寫不成區間；或 (3) 公開層已出現穩定、可拒絕之物理閘制佔比，且其水準使「市場隱含 AI 可壓縮比例 − 該佔比」方向翻負或差距不可辨。
**領域最近公開（§7-10）：** IEC 60068-2-78:2025（2025-08-06）；JESD22-A101D.01（2021-01）；UL 3115 Issue 2（2026-03-27）；ULS FY2025 10-K（2026-02）；ULS Q2 2026（2026-08-04）；IECEE 2025 年證量（IEC facts as-of 2025-12-31；Nemko 轉述 2026-06-02）；BV Italia 登記更新 2026-07-31；BV H1 2026 Certification（2026-08）。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260922_L12-P_generate_GK.md` `1BrfvvlzGeI8k-6U34_VwQG_JUj9_69J9`（10378 B）；`push_l9a_align.py` `1OeD0rkMsMufb-x8hr9bo07A1b7jqm1qs`
- inbox_GK／inbox_CL：空
- query 五檔在；MECH last_sync_utc 2026-09-22T07:10:31Z role SCOUT
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`；matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`（L12［P］＝【未研究】，本輪不改）
- archive_work 已含 L9-I 測一 USED_ `1pRrXaIalc3S3aVwV0WK-6ltplb1SyWZ5`、生成 USED_ `1a1H-GCf5gLXusmySde1tJkm-qEmXlJVS`

---

## 終態

**不通過。不進 T。** 機制（標準寫死之暴露時長不可被模型縮短）未被否證。失敗在可觀測性——時長參數在方法標準層存在；公開證書庫給得出單張查詢與（IECEE）全方案年證量，給不出「該標準強制時長 × 該庫發證數」可加總時序／存量，也對不齊已上市 TIC 的營收列。

| 測試項 | 結果 |
|---|---|
| B 端已實讀（非指名；非 TAT 行銷頁） | **通過**　IEC／JEDEC 時長錨；UL Product iQ／BV Italia／LCIE／Intertek／SGS 庫介面；IECEE 年證量；ULS 10-K／Q2 服務類 |
| 具名標準時長表公開可讀 | **部分通過**　JESD22-A101 時長公開；60068-2-78 時長是參數，2025 偏好表付費牆；UL 3115 無物理暴露時長表 |
| 「時長 × 發證數」時序或存量 | **不通過**　各 TIC 庫＝單張查詢；IECEE 年證量不是按時長標準、也不是單一上市主體 |
| 乘積對齊已上市 TIC 營收／毛利科目 | **不通過**　最近列＝ULS Certification Testing（FY2025 US$851M／約 28%），科目過寬 |
| 穩定可拒絕之物理閘制佔比 | **不存在** |
| 否決觸發 (1) | **觸發** |
| 否決觸發 (2) | **觸發** |
| 否決觸發 (3) | **未觸發**　佔比不存在，方向未翻負 |
| 升格 T | **否** |

失效歸因（§7-2）：不是檢索失敗。失敗在量綱——16(a) 乘積的第二因子（按標準可點算之發證數）在 UL／BV／Intertek／SGS 公開層不存在；IECEE 總量不能代換成「物理小時存量」。現況檔名＝上列 work／query。複查觸發器＝生成卡原文（見下）。停。

本格不入 §1。不改正本（對齊屬 SCOUT）。

---

## 已實讀載體

### A. 標準時長表（第一因子；非 TAT）

**IEC 60068-2-78:2025 Test Cab（2025-08-06，Ed. 3.0）**
- 方法標準：嚴重度＝溫度 × 相對濕度 × **總測試時長**。時長是標準參數，不是實驗室收件／排程／出報告週期。
- IEC webstore 公開層只有摘要；2025 版偏好時長表**付費牆**，本輪不得把生成卡轉述的 12 h／16 h／24 h／2／4／10／21／56 日當成 2025 已核對表（該列來自 2001 公開預覽）。
- 產品標準疊加例：EN IEC 61800-5-1 修正草案把 Test Cab of 60068-2-78:2025 寫成暴露 **≥ 96 h**——這是產品族下限，不是方法標準全表，也不是發證數。

**JESD22-A101D.01（2021-01）**
- 85 °C／85 %RH，時長 **1000 +168/−24 h**。此即種子「1,000 h」公開來源之一。JEDEC 分類頁存在；全文需註冊下載。時長參數成立。
- 公開層**沒有**「依 A101 發證／完成件數」時序。

**UL 3115 Issue 2（2026-03-27）**
- Outline of Investigation：AI 產品安全（資料／演算法／治理／偏誤等準則）。CEO 訪談：約 200 項準則；「不是進黑箱」。無公開 1,000 h 類暴露時長表。首發證書敘事（Qcells 等）不構成本格分母。

本輪**未**把任何 TIC 服務線 TAT／連網實驗室牆鐘讀成底板。

### B. 公開證書庫（第二因子）

| 庫 | 能做什麼 | 不能做什麼 |
|---|---|---|
| UL Product iQ（需免費帳） | 按 CCN／檔號／關鍵字查單張 Listing | 無按標準之公開合計、無發證年序、無時長欄 |
| BV Italia 登記（更新至 2026-07-31） | 證號或公司名查有效性；每搜最多 50 筆 | 無按標準合計；無物理時長欄；系統／產品／能力證混庫 |
| LCIE 產品庫 | 查有效日與真偽；欄位含方案／標準 | 明示查核用；排除 ISO 9001／IECQ／IECEx／ATEX／ETICS |
| Intertek 多個 Mark 目錄 | 按公司／型號查 Listing | 無按標準合計、無時長欄 |
| SGS Certified Client／Components | 證號或公司名查狀態 | 管理系統與產品混；無時長×件數 |
| IECEE CB 公開庫 | 單張 CB 證摘錄；年報總量 | 2025 年發證 133,918（IEC facts as-of 2025-12-31；Nemko 轉述 134,403）。分類＝HOUS／ITAV／MED 等產品族，**不是** 60068-2-78／A101。94–95 家 NCB，不能記成 ULS 或 BV 一<家的發證數 |

結論：第二因子在指名庫上＝單張查詢。IECEE 總量不可代入乘積（錯主體、錯分類、無時長）。

### C. 已上市 TIC 科目（對齊題）

**ULS FY2025 10-K（期 2025-12-31）：** Certification Testing US$851M（約 28%）；Ongoing US$1,006M（33%）；Non-certification Testing US$911M（30%）；Software US$285M（9%）；合計 US$3,053M。Q2 2026 Certification Testing US$237M。
- 10-K 原文：Certification Testing「include testing to global or regional standards, **engineering evaluation and project review and functional safety testing of embedded software**」。28% **≠** 物理閘制佔比（R3 成立）。
- 核數師關鍵事項：認證測試收入按「各專案階段已過時間／該階段**預估時長**」認列——這是專案包絡，不是標準暴露時長。不得把認列時長讀回本格分母。

**BV Certification H1 2026：** 收入 EUR 285.7M，有機 +1.9%。構成偏 QHSE 方案（約 53%）與永續／數位（約 35%）。不是物理小時存量，也不是 ULS 式 Testing 列。

無「受標準規定暴露時長閘制」之測試營收列。佔比寫不成區間。

### D. 乘積試算（明示＝不可做）

可寫：A101 單次暴露中位 1,000 h。不可寫：`1,000 h × N_A101`，因公開層無 `N_A101`（亦無 `N_60068-2-78` 按庫、按年）。用 IECEE 13.4 萬張／年去乘任一小時數＝量綱錯配，本輪不做。

---

## 對種子與反方

| 主張 | B 端讀後 |
|---|---|
| 時長守恆、AI 不觸及暴露段 | **機制未否證**　方法標準仍把時長當參數 |
| 小時存量＝時長 × 公開發證數 | **表達點不成立於公開層**　缺第二因子 |
| R1 並行／艙位壓縮牆鐘 | 本輪未讀產能；即使成立也不補發證數 |
| R2 庫給得出單張、給不出強制時長可加總時序 | **成立**　觸發 (1) |
| R3 Certification Testing 28% 過寬 | **成立**　觸發 (2) |
| R4 UL 3115／AI 營收落在無物理底板腿 | **成立於 3115 本身**　3115 無暴露時長表 |
| R5 不得把簽署工時加進分母 | **遵守**　本輪未載入人時 |

---

## 不開 T／§7-4

進 T 需把 H1 寫成財富倍數窗。本輪可寫入的只有「時長參數存在、發證數按標準不可加總、Testing 列過寬」。不夠把閘制佔比寫成區間。

§7-4 三題本輪不答（生成卡：轉入個股層時必問；本格不轉、不進 T）。

**複查觸發器（沿用生成卡，不改寫）：** 任一家美股或主要歐股上市 TIC 於 10-K／20-F／半年報，分列「受標準規定暴露時長閘制」之測試營收（或等價：具名標準族之 Certification Testing 與時長參數可對齊），且可與同期公開證書庫存量對帳。

---

## URL

1. https://webstore.iec.ch/en/publication/82357
2. https://webstore.ansi.org/preview-pages/IEC/preview_iec60068-2-78%7Bed3.0%7Den.pdf
3. https://www.jedec.org/taxonomy/term/3413
4. https://www.ul.com/PiQ
5. https://productiq.ulprospector.com/en
6. https://www.ul.com/software/product-sourcing-and-certifications-database
7. https://www.bureauveritas.it/certificate-register
8. https://www.lcie.fr/en/certified-product-database/
9. https://www.intertek.com/directories/
10. https://www.sgs.com/certifiedclients
11. https://www.iecee.org/certification/cb-test-certificates
12. https://iec.ch/what-we-do/facts-figures
13. https://www.nemko.com/blog/the-cb-scheme-statistics-for-2025-now-available
14. https://www.sec.gov/Archives/edgar/data/1901440/000190144026000005/uls-20251231.htm
15. https://www.sec.gov/Archives/edgar/data/1901440/000190144026000005/R13.htm
16. https://www.morningstar.com/news/business-wire/20260804813387/ul-solutions-inc-reports-strong-second-quarter-2026-results
17. https://www.ul.com/services/ul-3115-ai-safety-certification-services-ai-enabled-products
18. https://www.ul.com/news/ul-solutions-launches-landmark-artificial-intelligence-safety-certification-services

**（完）**
