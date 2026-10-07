# L13-I 測一｜資本與融資結構：股權餘額對同一客戶應收帳齡

<!-- BY: ANALYST@GK | MODEL: Grok 4.7【自報】 | CHARTER: AIM-C1.1 | NOTE: 測一不通過｜不進 T。不改 L13-P／L13-A。不重開 C-A4／C-A3。不寫 T。不改正本 | CONSUMES: 1UCgKVL5OOLSXUCamuHAIo83RMZtajlDv；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1xdEw0NdnY1nsv_LKFiFNAZgPoyxv3oKx；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi | EMITS: SELF -->

**日期：** 2026-10-02　**角色：** ANALYST@GK　**格：** L13-I　**上限：** 測一，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 本輪只測生成卡。不寫 T。不改正本狀態欄。

---

## 0. 本輪範圍

- 被測＝生成卡 `20261002_L13-I_generate_GK.md` fileId `1UCgKVL5OOLSXUCamuHAIo83RMZtajlDv`（12561 B，全文已讀，未截斷）。種子＝ARCH_3h §3.29 L13-I（`1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj`）：供應商同時為股東與債權人時，其對客戶信用之私有資訊不外顯 → 公開信評對該類客戶之資訊含量下降。B 端載體＝股權投資餘額 vs 應收帳款帳齡。重疊標＝新。快照 `1xdEw0NdnY1nsv_LKFiFNAZgPoyxv3oKx` 本輪未改。
- 並列對＝同一供應方 10-K／10-Q 的兩欄：（i）對具名客戶之股權投資餘額（或同檔可對帳之 as-converted 持股）；（ii）該同一客戶之應收帳齡或信用損失分桶。缺一則不可並列。公開信評是否引用該分桶是第三欄，不是帳齡之替代。
- 不改 L13-P（測一不通過｜不進 T，測一 `1RxfWgMnBAudanpfl8be15Ttvmk7kOULk`）。不改 L13-A（T 已寫｜不進 L，`1K-v28HccclcvzFzOy9zpCy994PkiERqX`；測一 `1ux-Zbnu5k-4Dc1TUOEUHucf4I3iimlju` 自判不進 T 未改成通過）。不重開 C-A4／C-A3。不改 L6-I。不恢復 L11-P。不把本格改寫成未開始租／RVG／JV、熱循環、backlog／RPO，或表達窗 k。
- session 列 `work/` `1CEprzXwFF4FA0HRHDe9prm2cIYRLB12z` 僅本生成卡；`inbox_GK` `1ZbILrSDyO71BiAS8yV_Ccx9W_WUKDm-S` 空；`query/` `1OPi79EP1MtU8dfSGJhzA8et8Grliaf8w` 5 筆（ARCH_dead、matrix、CHARTER_HIST、INDEX、MECH）。MECH `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h` last_sync_utc 2026-10-02T07:33:17Z role SCOUT。正本 FUNNEL `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI` 日期 2026-10-02，§1 無 L13-I，§3 仍列 L13-I 已生成未測。本輪不改正本。

---

## 1. 實讀（URL；B 端）

1. Microsoft 10-K，期 2026-06-30，acc `0001193125-26-323660`，簽名日 2026-07-29。https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm  
   關聯方段原文：股權法，as-converted 約 25%；OpenAI 為 ASC 850 關聯方；FY2026 商業安排收入（含分潤）$24.1 billion；2026-06-30 應收 $6.0 billion；投資資金承諾 $13.0 billion，已撥付 $11.9 billion。同段無帳齡、無該客戶信用損失分桶。全文詞界「aging／past due」無敘事命中。資產負債表應收淨額之備抵是全公司 $1,040 million（應收 $80,876 million），政策句是已知問題戶、歷史經驗與其他可得證據，不是具名客戶分桶。
2. NVIDIA 10-Q，期 2026-07-26，acc `0001045810-26-000075`，簽名日 2026-08-26。https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm  
   Note 6：非上市股權以成本減減損、按可觀察價格調整；期末帳面 $47,898 million。股權法投資於基礎設施融資方 $3.3 billion。承諾段：對 AI 模型商、基礎設施融資方與其他私人公司之股權投資承諾，未具名。MD&A：股權投資 $99 billion、承諾 $25 billion（2026-07-26）。應收集中：五名直接客戶佔 22%、14%、13%、11%、10%，未具名；投資級客戶付款條件可至 90 日至一年。OpenAI 只出現在對其關係企業之租賃信用支持保證，不是股權餘額對帳齡。全文無 CoreWeave、無 related party、無帳齡表。
3. CoreWeave 10-Q，期 2026-06-30，acc `0001769628-26-000366`（索引封面 Date 2026-08-11）。https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm  
   應收淨額 $2,541 million。2026-01 與 NVIDIA 之私募：約 23 million 股 Class A，$87.20，總額 $2.0 billion。此為本體發行所得，不是供應方帳面股權對本體應收帳齡。關聯方段是 Magnetar（2025-03 起不再符合 ASC 850）。股權法是一筆 JV（帳面 $44 million），不是供應方對本體之帳齡對照。無應收帳齡。
4. 同主體 Exhibit 99.1，acc 路徑 `0001769628-26-000357`，日期 2026-08-10。https://www.sec.gov/Archives/edgar/data/1769628/000176962826000357/ex991pr.htm  
   DDTL 5.5 獲 Moody’s Ba2、Fitch BB+，「reflecting the strength of the collateral and structural protections supporting the transaction.」未提供應方私有資訊、應收帳齡，或供應方持股。載具評等，不是發行人信評已吸收帳齡。
5. S&P 頁「CoreWeave Outlook Revised To Positive, 'B+' Rating Affirmed」，頁面標 2026-04-09。https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/3543328  
   可見：展望調為正向、B+ 維持；NVIDIA 2026-01 之 $2 billion 股權投資；最大客戶 backlog 集中度由 85% 降至約 35%。該頁抽取未見應收帳齡、逾期、信用損失或供應方私有資訊句。不把 backlog 集中度寫成帳齡。

缺段：任一供應方同檔之具名客戶應收帳齡或信用損失分桶；NVIDIA 附註具名被投客戶與該客戶應收之對照；評等行動引用該分桶。`site:sec.gov` 以帳齡或逾期加股權法加 OpenAI／Anthropic／CoreWeave 檢索，命中為 CoreWeave 應收淨額與較早 RPO 附註，不是帳齡表。檢索未見 ≠ 不存在（CHARTER §7-2）。

---

## 2. 可觀測／可並列

| 欄 | 判定 | 讀到什麼 |
|---|---|---|
| 股權法比例與關聯方身分 | 可觀測 | MSFT：as-converted 約 25%；ASC 850 |
| 同一客戶應收總額 | 可觀測 | MSFT：2026-06-30 應收 $6.0 billion；同段商業安排收入 $24.1 billion |
| 資金承諾與已撥付 | 可觀測 | MSFT：$13.0 billion 承諾，$11.9 billion 已撥付 |
| 全公司備抵 | 可觀測 | MSFT：$1,040 million。不是該客戶分桶 |
| 未具名應收集中與付款條件 | 可觀測 | NVDA：五名直接客戶百分比；90 日至一年。無帳齡 |
| 客戶側之供應方入股 | 可觀測 | CRWV：NVIDIA 私募約 23 million 股、$87.20、$2.0 billion。不是供應方帳面對帳齡 |
| 載具評等 | 可觀測 | Exhibit 99.1：Ba2／BB+，理由是擔保與結構 |
| 發行人評等標題與 backlog 句 | 可觀測 | S&P 2026-04-09：B+ 維持；backlog 集中度。不是帳齡 |
| （ii）同一客戶應收帳齡或信用損失分桶 | 不可並列 | 已讀三份 10-K／10-Q 無此欄 |
| （i）與（ii）同檔並列 | 不可並列 | 股權比例與應收總額在，帳齡不在。應收總額不是帳齡 |

可運作對照只剩：關聯方總額、未具名集中度、客戶側發行所得、載具擔保評等、backlog 集中度。這五類不是「股權餘額 vs 同一客戶帳齡」的兩側。

---

## 3. 否決

生成卡寫給本輪之觸發，本輪執行：

- **(1) 觸發。** 實讀後無法在同一供應方 10-K／10-Q 並列股權投資餘額與同一客戶應收帳齡或信用損失分桶。剩下的是應收總額（MSFT 關聯方段）與通話式集中度（NVDA）。
- **(2) 同向。** 公開信用句是載具擔保（Exhibit 99.1）與 backlog 集中度（S&P）。無替代申報把帳齡與信評引用放在同一檔。不把 backlog 寫成通過。
- (3) 未改格。不把對照寫成未開始租／RVG／JV。CRWV 之 JV 股權法不採。不改 L13-A。
- (4) 未改格。不把對照寫成熱循環或會計年限。不改 L13-P。不重開 C-A4／C-A3。
- (5) 未改格。S&P 之 backlog 集中度不採為本格對照。不改 L6-I。不恢復 L11-P。
- (6) 未觸發「公開層已穩定拒絕私有資訊不外顯」。同檔沒有帳齡，也沒有信評引用該分桶。關聯方段把比例、收入與應收總額寫出，只說明身份已外顯，不說明帳齡已外顯。

終端三題本輪不答（CHARTER §7-3；生成卡 §6 本階段不答）。

---

## 4. 次級路徑

上市供應方＝Microsoft。FY2026 10-K（acc `0001193125-26-323660`，簽名 2026-07-29）已開：關聯方段有股權法比例與應收總額，無帳齡。NVIDIA 10-Q（acc `0001045810-26-000075`，簽名 2026-08-26）已開：股權與應收分列，對手方未具名，無帳齡。CoreWeave 10-Q（acc `0001769628-26-000366`）已開：應收淨額與 NVIDIA 入股所得，無帳齡。**10-K／10-Q 次級路徑未成立。**

失敗歸因：三份原檔已取。S&P 頁可開，抽取未見帳齡句，不把未逐段存檔之正文寫成已重算。關鍵字檢索未帶回同檔並列，不以此作不存在主張。

複查觸發器（沿生成卡）：任一已上市供應方於 10-K／10-Q 同檔分列對具名客戶之股權投資餘額與該客戶應收帳齡或信用損失分桶，且該客戶之公開信評行動可對照是否引用該分桶。

---

## 5. 終態

**測一不通過（股權法比例、應收總額與載具評等可觀測；同一客戶應收帳齡或信用損失分桶與股權餘額不可並列）｜不進 T。**

不改 L13-P。不改 L13-A。不重開 C-A4／C-A3。不改 L6-I。不恢復 L11-P。不寫 T。不改正本 FUNNEL／matrix／INDEX。

---

## 6. 本輪寫入／不寫入

寫入：本測一入 Drive `work/`（fileId 見上傳回傳；標頭 EMITS＝SELF）。
不寫入：FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`；matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`；INDEX.json `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`；ARCH_dead；ARCH_3h。禁止新建同名正本。狀態欄對齊屬下一 session。生成卡尚未入 §1，本輪不建 `DONE_`。

**（L13-I 測一結束。）**
