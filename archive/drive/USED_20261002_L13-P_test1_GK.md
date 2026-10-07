# L13-P 測一｜資本與融資結構：熱循環計數對會計年限

<!-- BY: ANALYST@GK | MODEL: Grok 4.7【自報】 | CHARTER: AIM-C1.1 | NOTE: 測一不通過｜不進 T。不改 L13-A。不生成 L13-I。不重開 C-A4。不改正本 | CONSUMES: 1fetXqQLkwaBdFmihRvzoebokE_kYZCsa；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi | EMITS: SELF -->

**日期：** 2026-10-02　**角色：** ANALYST@GK　**格：** L13-P　**上限：** 測一，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 本輪只測生成卡。不寫 T。不改正本狀態欄。

---

## 0. 本輪範圍

- 被測＝生成卡 `20261002_L13-P_generate_GK.md` fileId `1fetXqQLkwaBdFmihRvzoebokE_kYZCsa`（11933 B，全文已讀，未截斷）。種子＝ARCH_3h §3.29 L13-P（`1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj`，14804 B，L13 列已讀）：GPU 之實體壽命受熱循環次數封頂（熱應力累積為守恆型計數），與會計年限無關。B 端＝45 格中唯一指名失敗者，先歸 (a) 未檢索，不得記為 (b) 結構性不可分離。重疊標＝新。
- 並列對＝同一 10-K／10-Q 的兩欄：（i）現場熱循環次數或等效熱應力計數，且標明為現場 duty cycle 而非實驗室鑑定循環；（ii）該主體伺服器會計年限。缺一則不可並列。
- 不改 L13-A（T 已寫｜不進 L，`1K-v28HccclcvzFzOy9zpCy994PkiERqX`；測一 `1ux-Zbnu5k-4Dc1TUOEUHucf4I3iimlju` 自判不進 T 未改成通過）。不生成 L13-I。不重開 C-A4／C-A3。不改 L6-P。不恢復 L11-P。不把本格改寫成租賃義務、信評、叢集 MTTF、注意力秒數，或折舊表達窗。
- session 列 `work/` `1CEprzXwFF4FA0HRHDe9prm2cIYRLB12z` 僅本生成卡；`inbox_GK` `1ZbILrSDyO71BiAS8yV_Ccx9W_WUKDm-S` 空；`query/` `1OPi79EP1MtU8dfSGJhzA8et8Grliaf8w` 5 筆（ARCH_dead、matrix、CHARTER_HIST、INDEX、MECH）。MECH `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h` last_sync_utc 2026-10-02T07:06:49Z role SCOUT。正本 FUNNEL `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI` 日期 2026-10-02，§1 無 L13-P，§3 仍列 L13-P／I 已生成未測。matrix 本輪未讀正文（5038 B，2026-10-02T07:02:23Z）。本輪不改正本。

---

## 1. 實讀（URL；B 端）

1. JEDEC Temperature Cycling，JESD22-A104F.01，頁面標 Published Apr 2023。https://www.jedec.org/standards-documents/docs/jesd-22-a104e  
   範圍句：單室、雙室、三室、空氣或其他氣態介質之溫度循環，涵蓋元件與焊點互連測試。頁上無條件表、無循環數、無現場 duty cycle。全文標 Free download，須註冊。官方頁不是現場剩餘計數。
2. 第三方 PDF 標 JEDEC Standard No. 22-A104F.01、Temperature Cycling、April 2023。https://file.globalso.com/file_manage/3034/20250321/jedec-jesd22-a104f-01-2023-temperature-cycling-1.pdf  
   可見實驗溫度條件表與每小時循環率（鑑定剖面），不是現場剩餘計數。警戒句：所選條件之高溫可能超過部分封裝材料玻璃轉移溫度，誘發設計應用之現場條件通常見不到的失效機制。不把該表之等級循環數寫成 JEDEC 官方頁原文，亦不寫成申報已列之現場計數。
3. Amazon 物業設備表，期間 2025-12-31，Exhibit R26，acc `000101872426000004`。https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/R26.htm  
   Servers and networking equipment 估計耐用年限五至六年。註 (1)：2024-01-01 起伺服器由五年改六年；2025-01-01 起一部分伺服器與網路設備由六年改五年。表內無 GPU 分列、無熱循環次數、無熱應力計數。同主檔 Note 3：https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm 同列，仍是年數。
4. Amazon 會計政策，期間截至 2025-06-30，Exhibit R8，acc `000101872425000086`。https://www.sec.gov/Archives/edgar/data/1018724/000101872425000086/R8.htm  
   2025-01-01 起該子集由六年改五年。理由：技術發展加快，尤其人工智慧與機器學習。仍是年數估計，不是循環計數。
5. NVIDIA 博客，2026-10-01。https://blogs.nvidia.com/blog/productive-durable-fungible-ai-factories/  
   A100（2020 出貨）六年後仍在商用。會計年限被寫成實體壽命之保守代理；Microsoft V100 相對六年帳面跑了 8.4 年。全文無熱循環次數、無焊點疲勞計數。賣方敘事，方向與「帳面已高估實體壽命」相反。賣方不折舊其售出之 GPU。

近旁、不進並列：2008 NVIDIA 8-K（acc 路徑 `000119312508145974`）把系統熱管理與使用型態列為筆記型 MCP／GPU 現場故障之貢獻因子，不是循環次數，也不是伺服器會計年限。2026-09-19 契約附件（acc 路徑 `000119312526395475`，ex10.23）有 GPU Failure Rate，百分比經遮罩，是故障比例契約，不是熱循環計數，且不在物業附註。檢索 `site:sec.gov`「thermal cycle／temperature cycling」加伺服器耐用年限，命中為年限變更、技術過時風險、上述 8-K、熱架構行銷、以及要求揭露年限敏感度之請願。檢索未見同檔並列。檢索未見 ≠ 不存在（CHARTER §7-2）。

缺段：JESD22-A104F.01 官方全文未取（註冊牆）。第三方 PDF 只用於確認方法本體是鑑定剖面。Meta／Microsoft 之年限變更本輪未逐份實讀 10-K，不拿來補並列。

---

## 2. 可觀測／可並列

| 欄 | 判定 | 讀到什麼 |
|---|---|---|
| 伺服器會計年限 | 可觀測 | Amazon R26：Servers and networking equipment 五至六年；2024-01-01 五年改六年；2025-01-01 子集六年改五年 |
| 年限變更之理由 | 可觀測 | R8：技術發展加快，尤其人工智慧與機器學習。仍是年數 |
| 實驗室溫度循環標準 | 可觀測 | JESD22-A104F.01，Apr 2023：元件與焊點互連之溫度循環。官方頁無循環數 |
| 鑑定剖面 ≠ 現場 duty cycle | 可觀測 | 第三方 PDF 之條件表是實驗溫度與每小時循環率；警戒句指向現場通常見不到的機制 |
| 賣方「帳面短於仍在役」 | 可觀測 | NVIDIA 博客 2026-10-01：會計年限＝實體壽命之保守代理；無循環次數 |
| （i）現場熱循環次數或等效計數 | 不可並列 | 已讀 10-K／10-Q 無此欄。鑑定循環不是此數 |
| （ii）與該主體伺服器會計年限同檔並列 | 不可並列 | 年限在，計數不在。無替代申報把兩欄放在同一附註 |

可運作對照只剩：帳上年數、年限估計之變更、實驗室鑑定標準、賣方服役敘事。這四類不是「現場計數 vs 會計年限」的兩側。

---

## 3. 否決

生成卡寫給本輪之觸發，本輪執行：

- **(1) 觸發。** 實讀後無法在同一申報並列「現場熱循環次數或等效計數」與「伺服器會計年限」。剩下的是鑑定標準（JESD22-A104F.01）與年數估計（Amazon R26／R8）。
- **(2) 同向。** NVIDIA 博客 2026-10-01 把帳面寫成實體壽命之保守代理（A100 六年後仍在商用；V100 8.4 年對六年帳面）。無替代申報分列現場計數。
- (3) 未改格。不把對照寫成租賃義務、信評、叢集 MTTF 或注意力秒數。不改 L13-A。不生成 L13-I。不改 L6-P。不恢復 L11-P。
- (4) 未改格。年限估計變更不是本格計數。不重開 C-A4／C-A3。

終端三題本輪不答（CHARTER §7-3；生成卡 §6 本階段不答）。3h 之 (a) 未改記為 (b)。

---

## 4. 次級路徑

上市持有人＝Amazon。FY2025 10-K（acc `000101872426000004`，期間 2025-12-31，主檔 `amzn-20251231.htm` 與 R26）已開：物業表有伺服器與網路設備年限，無熱循環欄。2025 年第二季政策（acc `000101872425000086`，R8，期間止 2025-06-30）已開：子集六年改五年，理由是技術步伐，不是循環計數。**10-K／10-Q 次級路徑未成立。**

失敗歸因：官方 JEDEC 全文在註冊牆後；已取 PDF 仍是鑑定剖面。SEC 關鍵字檢索未帶回同檔並列，不以此作不存在主張。

複查觸發器（沿生成卡）：任一已上市、持有 GPU 之主體於 10-K／10-Q 同檔分列現場熱循環次數或等效熱應力計數，且與該主體伺服器會計年限並列，並標明計數是否為現場 duty cycle 而非實驗室鑑定循環。

---

## 5. 終態

**測一不通過（伺服器會計年限與實驗室溫度循環標準可觀測；現場熱循環次數與會計年限不可並列）｜不進 T。**

不改 L13-A。不生成 L13-I。不重開 C-A4／C-A3。不改 L6-P。不恢復 L11-P。不寫 T。不改正本 FUNNEL／matrix／INDEX。

---

## 6. 本輪寫入／不寫入

寫入：本測一入 Drive `work/`（fileId 見上傳回傳；標頭 EMITS＝SELF）。
不寫入：FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`；matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`；INDEX.json `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`；ARCH_dead；ARCH_3h。禁止新建同名正本。狀態欄對齊屬下一 session。生成卡尚未入 §1，本輪不建 `DONE_`。
