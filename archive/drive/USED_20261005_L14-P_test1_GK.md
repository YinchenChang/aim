# L14-P 測一｜企業終端需求：同一 10-K／10-Q 之付費席次與期末員工數

<!-- BY: ANALYST@GK | MODEL: Grok 4.7【自報】 | CHARTER: AIM-C1.1 | NOTE: 測一不通過｜不進 T。不改 L14-A／L14-I。不重開 C-A2。不恢復 L11-P／L8-P／L9-P。不寫 T。不改正本 | CONSUMES: 1HuYarX0X4lu2GcG8C0drV94kns8PZbHQ；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h | EMITS: SELF -->

**日期：** 2026-10-05　**角色：** ANALYST@GK　**格：** L14-P　**上限：** 測一，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 本輪只測生成卡。不寫 T。不改正本狀態欄。

---

## 0. 本輪範圍

- 被測＝生成卡 `20261005_L14-P_generate_GK.md` fileId `1HuYarX0X4lu2GcG8C0drV94kns8PZbHQ`（11884 B，全文已讀，未截斷）。種子＝ARCH_3h §3.29 L14-P（`1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj`，本輪未重讀）：席次數 ≤ 員工數；每人每年工時上限；導入人力與被取代人力競爭同一存量。本輪只測生成卡否決第一觸發：同一 10-K／10-Q 能否並列付費席次與期末員工數。
- 並列對＝同一申報正文的兩欄：（i）付費席次水準（期末存量，不是成長率）；（ii）同一母體之期末員工數。缺一則不可並列。賣方自有員工數不是客戶席次的上界母體。BLS 週工時、二手員工數摘、業績稿不在 10-K／10-Q 正文者，不作席次對帳。
- 不改 L14-A／L14-I（FUNNEL §3 仍＝已生成未測，無獨立檔）。不重開 C-A2。不恢復 L11-P／L8-P／L9-P。不把本格改寫成 IT 支出÷營收、預算回流、單位經濟、清醒秒、標註分鐘或核可率。
- session 列 `work/` `1CEprzXwFF4FA0HRHDe9prm2cIYRLB12z` 僅本生成卡；`inbox_GK` `1ZbILrSDyO71BiAS8yV_Ccx9W_WUKDm-S` 空；`query/` `1OPi79EP1MtU8dfSGJhzA8et8Grliaf8w` 5 筆（ARCH_dead、matrix、CHARTER_HIST、INDEX、MECH）。MECH `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h` last_sync_utc 2026-10-05T13:27:09Z role SCOUT。正本 FUNNEL `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI` 日期 2026-10-02，§1 無 L14-P，§3 仍列 L14-P 已生成未測。本輪不改正本。

---

## 1. 實讀（URL；B 端）

1. Microsoft 10-K，期 2026-06-30，acc `0001193125-26-323660`，申報日 2026-07-29。https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm  
   Human Capital 原文：「As of June 30, 2026, we employed approximately 223,000 people on a full-time basis, 121,000 in the U.S. and 102,000 internationally.」職能分列 89,000／77,000／43,000／14,000。此數本輪從該 10-K 正文讀到，不用二手摘。  
   MD&A 定義：「Microsoft 365 Commercial seat growth: The number of Microsoft 365 Commercial seats at end of period where seats are paid users covered by a Microsoft 365 Commercial subscription.」同段結果句：「Microsoft 365 Commercial seats grew 6% driven by small and medium businesses and frontline worker offerings.」消費者側是 subscriber growth 7%，不是商業席次水準。全文抽取未見付費席次期末存量（無「million seats」水準句）。10-K 索引附件為 EX-19／21／23／31／32／97，無 EX-99.1。https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm
2. Microsoft 10-Q，期 2026-03-31，acc `0001193125-26-191507`。https://www.sec.gov/Archives/edgar/data/789019/000119312526191507/msft-20260331.htm  
   同定義；「Microsoft 365 Commercial seats grew 6%」。九個月比較句只寫 continued seat growth。員工句是「Total company headcount declined year-over-year」，無期末存量。無 Copilot 席次水準。
3. Microsoft 業績稿 EX-99.1，日期 2026-07-29，acc `0001193125-26-323632`（與 10-K 不同 accession）。https://www.sec.gov/Archives/edgar/data/789019/000119312526323632/msft-ex99_1.htm  
   「Microsoft 365 Copilot reached over 30 million paid seats」。無期末員工數。此檔不是 10-K／10-Q 正文，不併入第 1 項對帳。
4. ServiceNow 10-K，期 2025-12-31，acc `0001373715-26-000007`，申報日 2026-01-29。https://www.sec.gov/Archives/edgar/data/1373715/000137371526000007/now-20251231.htm  
   「As of December 31, 2025, we employed: 29,187 EMPLOYEES on a full-time basis」。客戶：「approximately 8,700 customers」。ACV > $5 million 客戶 603。抽取未見付費席次或 licensed users 水準。客戶數不是席次。
5. Atlassian 10-K，期 2025-06-30，acc `0001650372-25-000036`，簽名日 2025-08-15。https://www.sec.gov/Archives/edgar/data/1650372/000165037225000036/team-20250630.htm  
   「As of June 30, 2025, we had 13,813 full-time employees.」「powers more than 300,000 customers worldwide.」風險句：「reductions in paid seats from existing customers.」抽取未見付費席次期末存量。股東信（acc `0001650372-25-000064`，EX 不是本 10-K）只寫 paid seat expansion 與 AI MAU > 3.5 million，無席次水準對員工數。https://www.sec.gov/Archives/edgar/data/1650372/000165037225000064/teamq12026shareholderlet.htm

缺段：任一 10-K／10-Q 同檔之付費席次期末存量與同一母體期末員工數；導入工時與被稱取代職類工時（本輪不測第二恆等，生成卡第一觸發已足）。BLS 週工時本輪不取、不作對帳。檢索未見買方同檔並列 ≠ 不存在（CHARTER §7-2）。

---

## 2. 可觀測／可並列

| 欄 | 判定 | 讀到什麼 |
|---|---|---|
| 賣方期末員工數 | 可觀測 | MSFT 10-K：2026-06-30 約 223,000 全職。NOW：29,187。TEAM：13,813 |
| 席次定義 | 可觀測 | MSFT 10-K／10-Q：期末付費使用者，涵於 Commercial 訂閱。定義不是水準 |
| 席次成長率 | 可觀測 | MSFT 10-K 與 10-Q：Commercial seats grew 6%。成長率不是存量 |
| 賣方員工數方向 | 可觀測 | MSFT 10-Q：headcount declined year-over-year。無存量 |
| 客戶數 | 可觀測 | NOW 約 8,700；TEAM > 300,000。不是席次 |
| Copilot 付費席次水準 | 可觀測，但不同檔 | 8-K EX-99.1：over 30 million。該檔無員工數。acc 與 10-K 不同 |
| （i）付費席次期末存量 | 不可並列 | 已讀三份 10-K 與一份 10-Q 無此欄 |
| （ii）與（i）同檔、同一母體 | 不可並列 | 員工數是賣方自有人力；席次成長率是客戶付費使用者。兩欄即使同頁也不是 `Seats ≤ N` 的兩側 |

可運作對照只剩：賣方員工存量、席次成長率、客戶數、另一 accession 的 Copilot 席次水準。這四類不是「同一母體付費席次 vs 期末員工數」。

---

## 3. 否決

生成卡寫給本輪之觸發，本輪執行：

- **(1) 觸發。** 實讀後無法在同一 10-K／10-Q 並列付費席次水準與期末員工數。剩下的是員工數（MSFT／NOW／TEAM 10-K）與席次成長率（MSFT 10-K／10-Q）。
- **(2) 同向。** 席次水準在另一份 8-K 業績稿，該稿無員工數。不把 8-K 併進 10-K 寫成通過。不把 6% 成長率寫成席次存量。
- (3) 未改格。不把對照寫成 IT 支出÷營收。不改 L14-A。
- (4) 未改格。不把對照寫成採購預算不回流。不改 L14-I。
- (5) 未改格。不重開 C-A2。不恢復 L11-P／L8-P／L9-P。
- (6) 未觸發「公開層已穩定拒絕席次 ≤ 員工數」。同檔沒有席次水準，無從與員工數比大小。賣方 223,000 對客戶席次不是該不等式的 `N`。

終端三題本輪不答（CHARTER §7-3；生成卡 §6 本階段不答）。BLS 34.4 週工時與二手 223,000 摘本輪不用。

---

## 4. 次級路徑

上市賣方＝Microsoft。FY2026 10-K（acc `0001193125-26-323660`，申報 2026-07-29）已開：員工數與席次成長率在，席次水準不在。FY2026 Q3 10-Q（acc `0001193125-26-191507`）已開：席次成長率與人力方向在，兩側存量都不在。ServiceNow 10-K（acc `0001373715-26-000007`）與 Atlassian 10-K（acc `0001650372-25-000036`）已開：員工數與客戶數在，席次水準不在。**10-K／10-Q 次級路徑未成立。**

失敗歸因：四份 10-K／10-Q 正文已取。席次水準在不同 accession 的 8-K 附件，不是「席次不存在」。買方同檔並列未在本輪檢索命中，不以此作不存在主張。

複查觸發器（沿生成卡）：任一已上市主體於 10-K／10-Q 同檔分列付費席次期末存量與同一母體期末員工數，且導入／部署工時與被稱取代之職類工時可對帳。

---

## 5. 終態

**測一不通過（賣方期末員工數與席次成長率可觀測；同一 10-K／10-Q 之付費席次水準與期末員工數不可並列）｜不進 T。** 否決 (1) 觸發，(2) 同向。10-K／10-Q 次級路徑未成立。不改 L14-A／L14-I。不重開 C-A2。不恢復 L11-P／L8-P／L9-P。不寫 T。不改正本 FUNNEL／matrix／INDEX。未建 DONE_。

**（L14-P 測一結束。）**
