# L15-P 測一｜基礎設施軟體與資料：同一序列或同一 10-K／10-Q 之分析師人數與每人每日秒數

<!-- BY: ANALYST@GK | MODEL: Grok 4.7【自報】 | CHARTER: AIM-C1.1 | NOTE: 測一不通過｜不進 T。不改已入 §1 之 L14-P／L14-A／L14-I。不生成 L15-A／L15-I。不恢復 L11-P／L8-P／L9-P。不寫 T。不改正本 | CONSUMES: 1XVlmFvYT70DGOizIj3CZzqE0SoKzON9E；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h | EMITS: SELF -->

**日期：** 2026-10-05　**角色：** ANALYST@GK　**格：** L15-P　**上限：** 測一，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 本輪只測生成卡。不寫 T。不改正本狀態欄。

---

## 0. 本輪範圍

- 被測＝生成卡 `20261005_L15-P_generate_GK.md` fileId `1XVlmFvYT70DGOizIj3CZzqE0SoKzON9E`（12547 B，全文已讀，未截斷）。種子＝ARCH_3h §3.29 L15-P（`1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj`，本輪讀到該列）：分析師注意力存量（每人每日秒數×人數）。B 端指名＝資安人力統計公開。重疊＝S-P-1，待議 25。本輪只測生成卡否決第一觸發：同一官方序列或同一 10-K／10-Q 能否並列界定母體之分析師人數與每人每日警報作業秒數，且 on-call 是否在秒數內已標明。
- 並列對＝同一檔的兩欄：（i）界定母體之人數；（ii）該母體每人每日警報作業秒數或工時。缺一則不可並列。就業人數、職缺數、每日警報條數、每則調查分鐘，都不是該乘積。警報條數×每則分鐘是負荷，不是存量。BLS 全職敘事、調查自陳、業績稿或部落格配比，不併成秒×人。
- 不改已入 §1 之 L14-P／L14-A／L14-I。不生成 L15-A／L15-I。不恢復 L11-P／L8-P／L9-P。不把本格改寫成清醒秒數、標註分鐘、核可工時、使用量×單價、出站取用權，或席次與期末員工數。
- session 列 `work/` `1CEprzXwFF4FA0HRHDe9prm2cIYRLB12z` 僅生成卡；`inbox_GK` `1ZbILrSDyO71BiAS8yV_Ccx9W_WUKDm-S` 空；`query/` `1OPi79EP1MtU8dfSGJhzA8et8Grliaf8w` 5 筆（ARCH_dead、matrix、CHARTER_HIST、INDEX、MECH）。MECH `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h` last_sync_utc 2026-10-05T14:21:12Z role SCOUT。正本 FUNNEL `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI` 日期 2026-10-05，7957 B，§1 已含 L14 三格＝測一不通過｜不進 T，§3 仍列 L15-P／A／I 已生成未測。本輪不改正本。

---

## 1. 實讀（URL；B 端）

1. BLS Occupational Outlook Handbook，Information Security Analysts，SOC 15-1212，頁面 last modified 2026-08-27。https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm  
   就業 2025＝192,900；展望 2035＝233,400（變動 +40,600）；年均職缺約 14,100。工時句：「Most information security analysts work full time, and some work more than 40 hours per week.」「Information security analysts sometimes have to be on call outside of normal business hours in case of an emergency.」無每人每日警報作業秒數，無 SOC 分析師子集，on-call 未折成秒數。此頁是官方序列，兩因子不同檔。
2. Optiv 新聞稿 2026-09-22（Ponemon Institute；Optiv 與 Palo Alto Networks）。https://www.optiv.com/company/press-releases/nearly-half-organizations-say-their-socs-cant-keep-pace-modern-threats  
   574 名有 SOC 之 IT／資安受訪者。SOC 自評有效或非常有效 51%。不足 staffing 46%。「SOCs managing an average of 2,566 alerts and incidents each day.」36% 仍以人工流程調查。無分析師人數×每人秒數同表。
3. Information Security Buzz 2026-09-14 轉 Prophet Security。https://informationsecuritybuzz.com/prophet-security-research-finds-ai-is-cutting-soc-investigation-times/  
   250 名 IT／資安受訪者。中位組織每日約 100 則警報，較大端平均近 1,000；74% 至少 50 則，27% 至少 500 則。徹底調查平均約 75 分鐘、中位 45 分鐘。未調查占比平均 28%、中位 22%。已用 AI 者中，54% 稱調查時間降 25–50%，另 18% 降幅過半。57% 預期兩年內角色改變但不減人數。無每人每日秒數，無與警報同表之分析師人數。
4. ISC2「2025 Cybersecurity Workforce Study」頁 https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study ：本輪直讀正文未取出（頁面只回標題與 Loading component；CHARTER §7-2）。發行人新聞稿 2025-12-04 已開：https://www.prnewswire.com/news-releases/isc2-study-finds-cybersecurity-budget-constraints-remain-but-do-not-worsen-while-skill-needs-grow-302632487.html 樣本 16,029；33% 稱無資源足額配置；29% 稱請不起所需技能；95% 至少一項技能需求；59% 稱關鍵或顯著技能需求。該稿無 workforce gap 數字，無秒×人。檢索摘錄稱本年未列 gap、34% 稱 staffing 剛好；摘錄不是實讀，不採用。次級頁之 4.8 million 不採。
5. CrowdStrike 10-K，期 2026-01-31，acc `0001535527-26-000010`，申報日 2026-03-05。https://www.sec.gov/Archives/edgar/data/1535527/000153552726000010/crwd-20260131.htm  
   「As of January 31, 2026, we had 10,698 full-time employees.」抽取未見 SOC 分析師人數、每人每日警報作業秒數，或人數×秒數。此數是賣方全體全職，不是警報作業母體。
6. Palo Alto Networks 10-K，期 2026-07-31，acc `0001327567-26-000023`。https://www.sec.gov/Archives/edgar/data/1327567/000132756726000023/panw-20260731.htm  
   「With a global workforce of 21,921 as of July 31, 2026」。同檔：「from the end of fiscal 2025 to the end of fiscal 2026, our headcount increased from 16,068 to 21,921 employees, including approximately 4,223 additional headcount as a result of the CyberArk acquisition.」簽名日抽取見 2026-09-10。抽取未見分析師秒數或 on-call 折秒。全體員工含收購，不是 SOC 分析師母體。
7. SentinelOne 10-K，期 2026-01-31，acc `0001583708-26-000020`，申報日 2026-03-19。https://www.sec.gov/Archives/edgar/data/1583708/000158370826000020/s-20260131.htm  
   「As of January 31, 2026, we had over 2,900 full-time employees worldwide.」同檔：「our headcount grew from over 2,800 employees as of January 31, 2025, to over 2,900 employees as of January 31, 2026.」抽取未見分析師人數×每人秒數。

缺段：任一官方序列或任一 10-K／10-Q 同檔之界定母體分析師人數與每人每日警報作業秒數，且 on-call 是否計入已標明。Vectra 2023 之次級彙編本輪不取、不混成。檢索未見同檔並列 ≠ 不存在（CHARTER §7-2）。

---

## 2. 可觀測／可並列

| 欄 | 判定 | 讀到什麼 |
|---|---|---|
| 職類就業人數 | 可觀測 | BLS OOH 2026-08-27：SOC 15-1212，2025＝192,900；2035＝233,400 |
| 全職／on-call 敘事 | 可觀測 | 多數全職；部分每週超過 40 小時；緊急時 on-call。敘事不是秒數 |
| 賣方期末員工數 | 可觀測 | CRWD 10-K：2026-01-31 共 10,698 全職。PANW：2026-07-31 共 21,921。S：2026-01-31 超過 2,900 |
| 每日警報條數 | 可觀測，不同調查 | Optiv／Ponemon：平均 2,566。Prophet 轉述：中位約 100、較大端平均近 1,000。分母不同 |
| 每則調查分鐘 | 可觀測，不同調查 | Prophet 轉述：平均約 75、中位 45。無同表人數 |
| 技能優先於增員 | 可觀測，發行人稿 | ISC2 稿 2025-12-04：技能需求句在；gap 數字不在該稿。研究頁正文未取出 |
| （i）界定母體之分析師人數 | 不可並列 | 已讀官方序列與三份 10-K 只給職類就業或賣方全體員工 |
| （ii）與（i）同檔之每人每日秒數 | 不可並列 | 秒數不在上述任一檔。on-call 未標是否在秒數內 |

可運作對照只剩：職類就業人數、賣方全體員工數、不同調查的警報條數與每則分鐘。這三類不是「同一母體秒×人」。警報×分鐘是負荷，不能代替存量。

---

## 3. 否決

生成卡寫給本輪之觸發，本輪執行：

- **(1) 觸發。** 實讀後無法在同一官方序列或同一 10-K／10-Q 並列分析師人數與每人每日秒數。剩下的是 BLS 就業人數、三份 10-K 的全體員工數，以及 Optiv／Prophet 的警報調查。
- **(2) 同向。** 可運算的一對是警報條數×每則分鐘，且兩調查分母不同。不把負荷寫成存量。不把 BLS 192,900 乘上任一調查的分鐘。
- (3) 未改格。不把對照寫成清醒秒數、標註分鐘或核可工時。不恢復 L11-P／L8-P／L9-P。
- (4) 未改格。不把對照寫成使用量×有效單價或出站取用權。不生成 L15-A／L15-I。
- (5) 未改格。不把對照寫成席次與期末員工數。不改已測 L14-P／L14-A／L14-I。
- (6) 未觸發「公開層已穩定拒絕秒×人是綁定存量」。同檔沒有乘積，無從與警報需求比剩餘。秒／則下降的自陳（Prophet 轉述）不是同母體存量已可重算。

終端三題本輪不答（CHARTER §7-3；生成卡 §6 本階段不答）。待議 25 不在本輪裁決。

---

## 4. 次級路徑

上市賣方＝CrowdStrike、Palo Alto Networks、SentinelOne。CRWD FY2026 10-K（acc `0001535527-26-000010`，申報 2026-03-05）已開：全體員工數在，分析師秒數不在。PANW FY2026 10-K（acc `0001327567-26-000023`，期 2026-07-31）已開：全體員工數與收購併入人數在，秒數不在。S FY2026 10-K（acc `0001583708-26-000020`，申報 2026-03-19）已開：全體員工數在，秒數不在。官方序列 BLS OOH（2026-08-27）已開：職類就業與全職敘事在，秒數不在。**10-K／10-Q 次級路徑未成立。**

失敗歸因：三份 10-K 與 BLS 頁已取。ISC2 研究頁正文未取出，不以該失敗主張 gap 不存在或秒×人不存在。調查負荷在另一類出版，不是「注意力存量不存在」。買方或 SOC 營運主體同檔並列未在本輪檢索命中，不以此作不存在主張。

複查觸發器（沿生成卡）：任一官方統計序列，或已上市資安軟體／SOC 營運主體之 10-K／10-Q，同檔分列界定母體之分析師人數與每人每日警報作業秒數或工時，使乘積可重算，並標明 on-call 是否在秒數內。

---

## 5. 終態

**測一不通過（職類就業人數、賣方期末員工數與警報調查可觀測；同一官方序列或同一 10-K／10-Q 之分析師人數與每人每日秒數不可並列）｜不進 T。** 否決 (1) 觸發，(2) 同向。10-K／10-Q 次級路徑未成立。不改已入 §1 之 L14-P／L14-A／L14-I。不生成 L15-A／L15-I。不恢復 L11-P／L8-P／L9-P。不寫 T。不改正本 FUNNEL／matrix／INDEX。未建 DONE_。

**（L15-P 測一結束。）**
