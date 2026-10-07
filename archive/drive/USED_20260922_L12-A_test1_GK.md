<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1xSd9OtwOXzBeJb_-kyX2UpeBPRzI3H7r；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；1D6RQ1288l4JpTt1xiqIhyDMcU_vJaAzk | EMITS: （本檔；Drive work/ 上傳後填 fileId） -->
# L12-A 測一｜B 端實讀甲-23（法定強制營收 vs 自願營收是否同表分列）

**角色：** ANALYST@GK　**日期：** 2026-09-22　**格：** L12-A（監理與法制：r 之法定／自願分解）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。強制一問＝甲-23：四家 TIC 中任一是否曾把**法定強制營收**與**自願營收**同表分列，且該切法能否對上集團 `r` 權重。**禁止只重讀 L12-P 的服務類表。** 不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不開 T。不併殺 L12-P／L12-I。
**原陳述（生成卡 `1xSd9OtwOXzBeJb_-kyX2UpeBPRzI3H7r`）：** `r_集團 = (w_法定 × r_法定) + (w_自願 × r_自願)`；種子寫 `r_法定≈1`、`r_自願≈0`，故集團 `r`＝權重。錯價只在把「自願腿可被壓縮」讀成「集團 `r` 可被壓縮」。甲-23 要的不是服務類名稱，是法定強制營收÷總營收是否在申報或投資人材料成列。
**否決觸發（生成卡寫給本輪）：** (1) 對 ULS／BV／SGS（Intertek 若仍在公開層）實讀後，申報層與主要投資人材料仍無「法定強制營收 vs 自願營收」同表分列，只剩服務類或事業部近義切；或 (2) 僅有單次、不可重算之簡報圖，無法把 `w_法定` 寫成區間；或 (3) 公開層已出現穩定權重，且其水準使「自願腿可壓 → 集團 `r` 可壓」方向翻負或差距不可辨。
**領域最近公開（§7-10）：** ULS FY2025 10-K（2026-02-20）；ULS Q2 2026（2026-08-04）；BV FY2025 結果簡報（2026-02-25）；BV 2025 URD 申報（2026-03-30）；BV H1 2026（2026-07-29）；BV CMD（2026-09-22）；SGS 2025 全年（2026-02-11）／Integrated Report；Intertek FY2025 ARA（2026-03）＋股東會通過方案（2026-08-06），生效預估 2026 Q4／2027 Q1。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260922_L12-A_generate_GK.md` `1xSd9OtwOXzBeJb_-kyX2UpeBPRzI3H7r`（9666 B，2026-09-22T09:02:30Z）；`push_l9a_align.py` `1OeD0rkMsMufb-x8hr9bo07A1b7jqm1qs`
- inbox_GK／inbox_CL：空
- query 五檔在；MECH last_sync_utc 2026-09-22T08:59:00Z role SCOUT
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`；matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`（L12［A］＝已生成＝3h 快照，本輪不改）
- L12-P 測一已 USED_／標記 `1D6RQ1288l4JpTt1xiqIhyDMcU_vJaAzk`（本輪不重讀其服務類表當甲-23 答案）

---

## 終態

**不通過。不進 T。** 機制（需求來源係數可寫成權重平均；法定腿≠自願腿）未被否證。失敗在可觀測性——甲-23 在四家公開層**沒有**可重算的「法定強制營收／自願營收」同表分列。唯一貼近種子用詞的載體是 BV 投資人簡報的標籤二分（Regulatory vs Risk mitigation／voluntary），屬非 IFRS、約數、且與同頁 Opex／Capex／Products 圖百分比相撞，不能當 `[V]` 權重。

| 測試項 | 結果 |
|---|---|
| B 端已實讀（非指名；非只讀 L12-P 服務類表） | **通過**　ULS 10-K／Q2 科目定義；BV FY2025 deck 附錄＋官網事業部表＋H1／CMD 敘事；SGS 2025 事業線表；Intertek ATIC／五事業＋要約現況 |
| 申報層同表分列法定強制 vs 自願營收 | **不通過**　四家皆無 10-K／20-F／URD／半年報附註兩欄 |
| 主要投資人材料同表分列且可重算 | **不通過**　僅 BV deck 有標籤；無歐元金額、標 c.、與另一切法同頁 |
| `w_法定` 可寫成區間 | **不通過**　觸發 (2) |
| 穩定權重使方向翻負 | **不存在** |
| 否決觸發 (1) | **觸發** |
| 否決觸發 (2) | **觸發** |
| 否決觸發 (3) | **未觸發**　權重不存在，方向未翻負 |
| 升格 T | **否** |

失效歸因（§7-2）：不是檢索失敗。失敗在量綱——種子權重因子在申報層不存在；BV 簡報標籤不能代換成附註列。現況檔名＝上列 work／query。複查觸發器＝生成卡原文（見下）。停。

本格不入 §1。不改正本（對齊屬 SCOUT）。

---

## 已實讀載體（甲-23；非 L12-P 時長×發證）

### A. ULS（美股；10-K 申報層）

**FY2025 10-K（期 2025-12-31，檔 2026-02-20）** 與 **Q2 2026** 補充表之「Major Service Category」＝Certification Testing／Ongoing Certification Services／Non-certification Testing and Other Services／Software。ASC 280 經營分部＝Industrial／Consumer／Software and Advisory。

甲-23 讀法（讀定義，不把佔比貼成 `w_法定`）：
- Certification Testing：「global or regional **regulatory requirements and other** design and performance specifications」——兩側寫進同一列（R1）。
- Ongoing：「maintain the right to use … marks」＋「meet **certain regulatory requirements**」＋「**mandatory** inspection and monitoring」——強制的是**持標方案內的巡廠**，不是「法定營收」欄。
- Non-certification：「**may not be required by any regulation** and may not result in a certification」——這是「可不被法規要求」的敘事，不是與上一列互為補集的自願欄。同一列還含 advisory／sustainability。

結論：10-K **有**法規用語，**無**法定／自願兩欄。本輪不引用 Testing／Ongoing／Software 金額當權重（R5／生成卡禁令）。

### B. Bureau Veritas（歐股；唯一貼近種子用詞之載體）

**官網 Key figures／事業部表（集團 EUR 6,466.4M，FY2025）：** Marine & Offshore 557.9；Agri-Food & Commodities 1,163.7；Industry 1,372.8；Buildings & Infrastructure 1,997.9；Certification 571.7；Consumer Products 802.4。這是事業部，不是甲-23。

**FY2025 Results Presentation 附錄「RESILIENT PORTFOLIO」同一頁兩張圖：**
- 標題一：RISK MITIGATION SERVICES VS. REGULATORY REVENUE IN PERCENTAGE OF GROUP REVENUE
- 標題二：REVENUE MIX BY TYPE OF SERVICES（Opex & Systems／Capex／Products）
- 腳註：(1) Voluntary revenue driven by enterprise programs or industry’s standards；(2) Regulatory revenue is driven by law or regulation
- 例示句：Certification is a **voluntary** business（industry or international schemes）；Marine & Offshore is a **regulatory** business by nature
- 同頁可見約數 c. 29%／c. 34%／c. 37%

甲-23 判定：
- 標籤存在，且定義對得上種子用詞（law or regulation vs voluntary／enterprise programs）。
- **不是同表分列的申報列**：無歐元、無附註編號、標 c.。公開擷取把兩圖百分比疊在一起（生成卡 R2）；本輪**不把 29／34／37 記成已核對 `w_法定`／`w_自願`**。
- H1 2025 中期簡報已出現同一對標題與同一組例示句（當時約數 28／35／37）——切法在投資人頁面重複，但仍無金額列，不能重算季頻時序。
- 用事業部名代權重會把符號用反（R3）：Certification FY2025＝571.7／6,466.4≈8.8%，deck 標成 **voluntary**；Marine＝557.9／6,466.4≈8.6%，deck 標成 **regulatory**。兩事業合計遠小於「集團權重」敘事，不能當 `w_法定`。
- 2025 URD PDF 本輪 fetch 失敗（§7-2：失敗≠不存在）。替代現況＝公司 Investor Key figures 與 FY／H1 新聞稿之公開表只有六事業部，無 Regulatory／Voluntary 兩欄。不得把 fetch 失敗寫成「URD 必無此列」。
- H1 2026（2026-07-29）與當日 CMD（2026-09-22）公開稿強調 AI-driven markets／services 2030 EUR 1B、事業部有機成長、Government Services 退出準備——敘事腿，不是 `w_法定` 列。

### C. SGS（瑞股）

2025-02-11 全年：Testing & Inspection CHF 6,165M；Certification／Business Assurance CHF 780M；集團 CHF 6,945M。事業線＝Industries & Environment／Natural Resources／Connectivity & Products／Health & Nutrition／Business Assurance。地域切與認列時點（point-in-time vs over time）存在。

Integrated Report 敘事：「Even as the United States reduced federal sustainability regulation, **voluntary demand** for trusted sustainability assurance continued to rise。」這是需求來源的句子，**不是**銷售兩欄。無 mandatory／voluntary 營收表。

### D. Intertek（英股；視窗內仍公開、預定下市）

FY2025 Strategic Report：ATIC＝Assurance 22%／Testing 45%／Inspection 24%／Certification 9%；五事業＝Consumer Products／Corporate Assurance／Health and Safety／Industry and Infrastructure／World of Energy。無法定／自願兩欄。「voluntary」在 ARA 主要出現於員工流失率，不是營收切法。

公開層現況（本輪）：Rule 2.7 全現金要約 2026-06-18；股東會／Court Meeting 通過 2026-08-06；方案生效預估 2026 Q4 或 2027 Q1，其後預定取消上市。截至 2026-09-22 仍為上市公司，但甲-23 視窗將縮。產業理由未改寫為法定／自願分列。

---

## 對種子與反方

| 主張 | B 端讀後 |
|---|---|
| `r_集團`＝權重平均；法定腿需求來源≈義務 | **機制未否證**　會計恆等仍可陳述；無人用申報列把它寫成數字 |
| 甲-23：至少一家同表分列法定／自願營收 | **不成立於申報層**　四家皆無兩欄 |
| BV deck 標籤可當 `[V]` 權重 | **不成立**　觸發 (2)；R2 成立 |
| R1 ULS「regulatory and other」不可分 | **成立** |
| R3 Certification＝voluntary，代換會翻號 | **成立於 BV 例示句**　本輪未用 Certification÷集團當 `w_法定` |
| R4 4b 三題四家不通過 | **不執行**（§7-3）；記存在，不開個股層 |
| R5 不得把 L12-P 服務類三列改貼成 `w_法定` | **遵守**　ULS 金額本輪不入權重 |

---

## 不開 T／§7-4

進 T 需把 H1 寫成財富倍數窗。本輪可寫入的只有「權重式可陳述、申報層無兩欄、BV 簡報標籤不可重算」。不夠把 `w_法定` 寫成區間，也就不能把「只壓自願腿不能改寫集團 `r`」寫成可拒絕之倍數差。

§7-4 三題本輪不答（生成卡：轉入個股層時必問；本格不轉、不進 T）。4b §4.17 四家三題不通過仍掛在「若有人要把本格帶進個股層，必問」。

**複查觸發器（沿用生成卡，不改寫）：** 任一家仍上市之 TIC 於 20-F／10-K／10-Q 或經審計附註分列 regulatory／mandatory 營收與 voluntary 營收，且該切法連續 ≥4 季。

---

## URL

1. https://www.sec.gov/Archives/edgar/data/1901440/000190144026000005/uls-20251231.htm
2. https://www.sec.gov/Archives/edgar/data/1901440/000119312526140051/d23202dars.pdf
3. https://ir.ul.com/sec-filings/quarterly-results/default.aspx
4. https://cdn3-group.bureauveritas.com/sites/g/files/zypfnx196/files/media/document/BureauVeritas_FY_2025_Results_Presentation.pdf
5. https://group.bureauveritas.com/investors/our-profile/key-figures
6. https://group.bureauveritas.com/investors/financial-information/financial-reports
7. https://cdn3-group.bureauveritas.com/sites/g/files/zypfnx196/files/media/document/Bureau-Veritas_Universal_Registration_Document_2025_17.9-Mo.pdf
8. https://www.businesswire.com/news/home/20260224846309/en/Bureau-Veritas-Sector-Leading-Organic-Revenue-Growth-of-6.5-in-FY-2025
9. https://www.businesswire.com/news/home/20260728246725/en
10. https://www.businesswire.com/news/home/20260921010375/en/
11. https://www.sgs.com/-/media/sgscorp/documents/corporate/reports-and-presentations/2020s/2026/sgs-2025-full-year-results-press-release-en.cdn.en.pdf
12. https://www.sgs.com/-/media/sgscorp/documents/corporate/reports-and-presentations/2020s/2026/sgs-2025-integrated-report-en.cdn.en-HU.pdf
13. https://www.intertek.com/siteassets/investors/2026/ara/intertek-strategic-report-2025.pdf
14. https://www.intertek.com/siteassets/investors/2026/ara/intertek-strategic-report-2025---our-business-model.pdf
15. https://www.intertek.com/siteassets/investors/2026/intertek-2025-full-year-results-announcement.pdf
16. https://www.investegate.co.uk/announcement/rns/intertek-group--itrk/recommended-final-cash-offer/9625392
