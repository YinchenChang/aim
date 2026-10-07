# L14-A 測一｜企業終端需求：同一 10-K／10-Q 之 IT 支出與總營收

<!-- BY: ANALYST@GK | MODEL: Grok 4.7【自報】 | CHARTER: AIM-C1.1 | NOTE: 測一不通過｜不進 T。不改 L14-I。不重開 C-A2。不改已測 L14-P。不恢復 L11-P／L8-P／L9-P。不寫 T。不改正本 | CONSUMES: 11Xmuy56BEXLYfqiRm4WWsmg4A0Lug2xc；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h | EMITS: SELF -->

**日期：** 2026-10-05　**角色：** ANALYST@GK　**格：** L14-A　**上限：** 測一，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 本輪只測生成卡。不寫 T。不改正本狀態欄。下列數字是申報科目，不是部位。

---

## 0. 本輪範圍

- 被測＝生成卡 `20261005_L14-A_generate_GK.md` fileId `11Xmuy56BEXLYfqiRm4WWsmg4A0Lug2xc`（11290 B，全文已讀，未截斷）。種子＝ARCH_3h §3.29 L14-A（`1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj`）：比重＝IT 支出÷總營收；比重是否上升直接判定新增或排擠。B 端載體僅指名 SG&A 分列＋產業總量。本輪只測生成卡否決第一觸發：同一 10-K／10-Q 能否並列 IT 支出與總營收。
- 並列對＝同一申報正文三欄：（i）IT 支出（不是 SG&A 合計，不是通訊＋設備＋租賃折舊混列）；（ii）同一主體、同一期間之總營收；（iii）IT 內 AI 行 vs 非 AI 行，或 IT 外 AI 行，並標明是否含資本支出、是否含 IT 部門以外支出。缺（i）或（iii）則比重不能判定新增或排擠。產業總量與調查比重不作公司對帳。
- 不改 L14-I（仍＝已生成，無獨立檔）。不重開 C-A2。不改已測 L14-P（測一 `142j3vdUU9F1QD4bq6FevLyOQSP1WIoR3`）。不恢復 L11-P／L8-P／L9-P。不把本格改寫成席次與員工數、預算回流或單位經濟。
- session 列 `work/` `1CEprzXwFF4FA0HRHDe9prm2cIYRLB12z` 僅本生成卡；`inbox_GK` `1ZbILrSDyO71BiAS8yV_Ccx9W_WUKDm-S` 空；`query/` `1OPi79EP1MtU8dfSGJhzA8et8Grliaf8w` 5 筆（ARCH_dead、matrix、CHARTER_HIST、INDEX、MECH）。MECH `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h` last_sync_utc 2026-10-05T13:40:35Z role SCOUT。正本 FUNNEL `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI` 日期 2026-10-05，§1 有 L14-P、無 L14-A，§3 仍列 L14-A 已生成未測。本輪不改正本。

---

## 1. 實讀（URL；B 端）

1. JPMorgan Chase 10-K，期 2025-12-31，acc `0001628280-26-008131`，申報日 2026-02-13。https://www.sec.gov/Archives/edgar/data/19617/000162828026008131/jpm-20251231.htm  
   總淨營收：「Total net revenue $ 182,447 $ 177,556 (g) $ 158,104」（2025／2024／2023，百萬）。非利息費用合計 95,640／91,797／87,172。  
   非薪酬分列：「Technology, communications and equipment (a) 11,029 9,831 9,246」。註 (a)：「Includes depreciation expense associated with auto operating lease assets.」薪酬另列 54,487／51,357／46,465，技術人員薪酬不在該行。MD&A：「higher investments in technology across the LOBs and Corporate and in marketing in CCB」——技術與行銷同一句，無金額。全文未見 AI 支出行、AI／非 AI 分列，或「比重上升＝新增」。
2. JPMorgan Chase 10-Q，期 2026-03-31，acc `0001628280-26-029344`。https://www.sec.gov/Archives/edgar/data/19617/000162828026029344/jpm-20260331.htm  
   總淨營收 1Q26 $ 49,836；1Q25 $ 45,310。同行：「Technology, communications and equipment (a) 3,021 2,578」。抽取未見 AI 支出分列。
3. Bank of America 10-K，期 2025-12-31，acc `0000070858-26-000157`。https://www.sec.gov/Archives/edgar/data/70858/000007085826000157/bac-20251231.htm  
   「Total revenue, net of interest expense 113,097 105,856」。非利息費用：「Information processing and communications 7,453 7,231」「Occupancy and equipment 7,448 7,289」「Total noninterest expense $ 69,727 $ 66,812」。無 IT 支出行。AI 句是監理義務（「Artificial intelligence-related (AI) LRRs」），不是支出分列。「Technology hardware and equipment」出現在產業曝險表，不是本公司 IT 支出。
4. Walmart 10-K，期 2026-01-31，acc `0000104169-26-000055`，申報日 2026-03-14。https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm  
   淨銷售 $ 706,413／$ 674,538。總營收 713,163／680,985。「Operating, selling, general and administrative expenses 147,943 139,884 130,971」。全文未見 information technology expense／Technology expense／AI spend。資本支出桶：「Supply chain, customer-facing initiatives, technology and other $ 16,468 $ 14,603」——供應鏈、客端、技術與其他混列，不是費用比重的分子。
5. 產業與調查（不作公司對帳）。Gartner 新聞稿 2026-07-27：全球 IT 支出 2026 年 6,369（十億）、增 14.2%；分資料中心系統、裝置、軟體、服務、IaaS、通訊服務。無公司 IT÷營收。https://www.gartner.com/en/newsroom/press-releases/2026-07-27-gartner-forecasts-worldwide-it-spending-to-grow-14-point-2-percent-in-2026-totaling-6-point-37-trillion  
   CIO 2026-09-23 引 Lovelock：2024–2025 有淨新增，「now more of their spending is about rebranding than diversion」。分析師陳述。https://www.cio.com/article/4225785/ai-spend-will-jump-49-5-in-2026-says-gartner.html  
   CIO Dive 2026-09-30 轉 BCG（>1,300）：AI 支出占營收自 2025 年末 1.7% 至 3.3%，八成在 IT 預算外。調查自陳。https://www.ciodive.com/news/ai-spending-spreading-beyond-it/831823/

缺段：任一 10-K／10-Q 同檔之 IT 支出（不含通訊、設備、汽車營運租賃折舊；含或不含之口徑已標明）與總營收，以及 AI 行與非 AI 行。檢索未見 ≠ 不存在（CHARTER §7-2）。

---

## 2. 可觀測／可並列

| 欄 | 判定 | 讀到什麼 |
|---|---|---|
| 總營收 | 可觀測 | JPM 10-K 總淨營收 182,447／177,556。JPM 10-Q 49,836／45,310。BAC 113,097／105,856。WMT 淨銷售 706,413／674,538 |
| SG&A 或非利息費用合計 | 可觀測 | JPM 非利息費用 95,640。BAC 69,727。WMT 營業、銷售、總務及管理 147,943。合計不是 IT |
| 技術相關費用行 | 可觀測，不是 IT | JPM：「Technology, communications and equipment」11,029／9,831，註 (a) 含汽車營運租賃折舊。BAC：「Information processing and communications」7,453，設備在另一行。薪酬不在行內 |
| 資本支出中的技術 | 可觀測，不可分離 | WMT 桶「supply chain, customer-facing initiatives, technology and other」16,468。不是費用比重分子 |
| 產業 IT 總量 | 可觀測，不是公司比重 | Gartner 2026-07-27：6,369、增 14.2%。無公司營收分母 |
| 調查所稱 AI 占營收 | 可觀測，不是 10-K | BCG 轉述 1.7%→3.3%，八成在 IT 外。不是申報科目 |
| （i）IT 支出 | 不可並列 | 已讀兩份 10-K、一份 10-Q、一份零售 10-K。命名行是混列或通訊處理，不是 IT |
| （ii）與（i）同檔總營收 | 分母在，分子不在 | 營收與混列行同頁，不能當成 IT÷營收 |
| （iii）AI 行 vs 非 AI 行 | 不可並列 | 四份申報無此欄。改標句在 CIO 轉述，不在 10-K |

可運作對照只剩：總營收、SG&A／非利息費用合計、混列技術行、混列資本支出桶、產業總量、調查比重。這六類不是「同一主體 IT 支出÷總營收，且能拒絕排擠」。

---

## 3. 否決

生成卡寫給本輪之觸發，本輪執行：

- **(1) 觸發。** 實讀後無法在同一 10-K／10-Q 並列 IT 支出與總營收。剩下的是 SG&A／非利息費用合計、混列技術行（JPM 含汽車租賃折舊；BAC 為資訊處理及通訊）、產業總量。不把混列行寫成 IT 分子。
- (2) 未改格。不把對照寫成席次與員工數。不改 L14-P。
- (3) 未改格。不把對照寫成採購預算不回流。不改 L14-I。
- (4) 未改格。不重開 C-A2。不恢復 L11-P／L8-P／L9-P。
- (5) 未觸發「公開層已穩定拒絕比重上升＝新增」。同檔沒有 AI 行，無從把比重上升歸因於營收下降或重分類。分析師「改標」與調查「八成在 IT 外」是敘事，不是同檔兩列。

終端三題本輪不答（CHARTER §7-3；生成卡 §6 本階段不答）。

---

## 4. 次級路徑

上市買方＝JPMorgan Chase、Bank of America、Walmart。JPM FY2025 10-K 與 FY2026 Q1 10-Q 已開：總營收與混列技術行在，IT 支出與 AI／非 AI 分列不在。BAC FY2025 10-K 已開：總營收與資訊處理及通訊在，IT 支出不在。WMT FY2026 10-K 已開：總營收與 SG&A 在，IT 費用行不在，資本支出技術與其他混列。**10-K／10-Q 次級路徑未成立。**

失敗歸因：四份申報正文已取。混列技術行存在，不是「技術科目不存在」。產業總量與調查比重不是公司比重已可重算。未在本輪命中的買方同檔三欄，不以此作不存在主張。

複查觸發器（沿生成卡）：任一已上市買方於 10-K／10-Q 同檔分列 IT 支出與總營收，且 AI 行與非 AI 行同檔可對帳，並標明是否含資本支出與 IT 部門以外支出。

---

## 5. 終態

**測一不通過（總營收與技術相關費用行可觀測；同一 10-K／10-Q 之 IT 支出與總營收不可並列）｜不進 T。** 否決 (1) 觸發。10-K／10-Q 次級路徑未成立。不改 L14-I。不重開 C-A2。不改已測 L14-P。不恢復 L11-P／L8-P／L9-P。不寫 T。不改正本 FUNNEL／matrix／INDEX。未建 DONE_。

**（L14-A 測一結束。）**
