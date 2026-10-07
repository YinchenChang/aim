<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1H1eZlmYlDa8Gd_TV6-y9G331Oqz5RMOL；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h | EMITS: PENDING_UPLOAD -->
# L3-I 測一｜B 端實讀（賣方暫收款／保留費 vs 設計商預付／承諾；同一標的與同一下修規則）

**角色：** ANALYST@GK　**日期：** 2026-09-26　**格：** L3-I（半導體製造測試：產能預付款為合約性取用權）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先賣方暫收款／保留費附註與設計商預付／承諾附註能否對同一標的與同一下修規則。**禁止只重讀產能法說與 NVDA 承諾總額。** 不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T。
**原陳述（生成卡 `1H1eZlmYlDa8Gd_TV6-y9G331Oqz5RMOL`）：** 預付買到的是合約性排序／保留權，不是產能物權；需求下修時預付方承擔沒入、短少費、或無法按原排序取片的損失；賣方側可見的是合約負債／暫收款。錯價只在把「預付餘額＝已持有產能」或「承諾美元＝可分離之晶圓取用權」當成充分統計。
**契約式（生成用）：** `預付 → 保留權／排序，不 → 產能所有權`；`需求下修 ⇒ 損失 ∈ 預付方（沒入／短少費／排序失效）`。本輪不估參數、不寫 H1。
**否決觸發（生成卡寫給本輪）：** (1) 對 20-F／10-K／10-Q 實讀後，暫收款／預付／承諾皆無法對到「排序權 vs 物權」或「下修損失歸屬」，只剩合併餘額與法說一句；或 (2) 公開契約規則穩定為可退／可抵，使「預付方承擔全部損失」無法寫成可拒絕區間；或 (3) 公開層已出現穩定可拒絕之兩側對帳（保留權已被科目定價），落差與可見定價不可辨。
**領域最近公開（§7-10）：** TSMC 2Q26 合併財報（2026-08-14）；TSMC 2Q26 法說逐字稿（頁面日 2026-08-28）；NVIDIA FY2027 Q2 10-Q（截至 2026-07-26）；NVIDIA FY26 10-K（期 2026-01-25）；Micron FY2026 Q3 10-Q（截至 2026-05-28）；GFS 20-F 2025（約 2026-02-27）；CRUS FY26 10-K（截至 2026-03-28）；AMD 10-Q（截至 2026-03-28）。下一官方檢查點＝TSMC 3Q26 季報（約 2026-10 中）或任一美股可交易主體首次把「產能保留預付」與一般存貨預付／記憶體長約分列，並寫明需求下修時之退款／抵帳／沒入規則，且可與對手方同期科目對帳。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260926_L3-I_generate_GK.md` `1H1eZlmYlDa8Gd_TV6-y9G331Oqz5RMOL`（12138 B，2026-09-26T10:16:33Z）；`20260923_HEALTH_CL.md` `1_urT6I7RovcM73D3IBTKGIk6RY1z9nC0`；`20260923_HEALTH_GK.md` `1byQGbjCmIT1orLv51moyAH5xnABFO95e`
- query/：`ARCH_dead.md` `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`；`ARCH_matrix.md` `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`；`CHARTER_HIST.md` `1DKg3HUr-zOWw20OmNe1aDpWT_izDwdiT`；`INDEX.json` `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`；`MECH.md` `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-09-26T10:13:13Z role SCOUT）
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-09-26；§1 無 L3；§3 L3［I］＝已生成）
- matrix L3［I］＝已生成。INDEX 無獨立 L3-I 測一 fileId
- 本輪上傳前 work/ 無同名 `20260926_L3-I_test1_GK.md`
- work 主動維護：三檔皆未吸收進現行 FUNNEL／CHARTER；HEALTH 兩份非本輪標的；生成卡待測一後由 SCOUT 對齊。本輪不建 `DONE_`。

---

## 終態

**不通過。不進 T。** 機制（預付換保留／排序、不是晶圓物權）未被否證——TSMC 原文即「to retain the Company’s capacity」，結算是退款或抵應收。失敗在可對帳性：先進邏輯主市場的賣方暫收款與設計商承諾**不能對同一標的、也不能對同一下修規則**；唯一兩側可對的是 GFS↔CRUS 成熟節點單一協議，且該協議已把「非退還保留費」與「可抵貨預付晶圓」分列（R3）。種子「需求下修 ⇒ 全部損失 ∈ 預付方」被 TSMC 可退／可抵句與 GFS underutilization／LTA 重談打開（R1、R4）。

| 測試項 | 結果 |
|---|---|
| B 端已實讀（非指名；非只讀產能法說／NVDA 承諾總額） | **通過**　TSMC 2Q26 合併財報 Note 20.c；TSMC 2Q26 法說稿；NVDA FY27 Q2 10-Q Note 10＋CFO commentary；NVDA FY26 10-K 製造／風險段；MU FY26 Q3 10-Q Note 14＋流動性段；GFS 20-F 2025 LTA／風險段；CRUS FY26 10-K Note 13；AMD 10-Q（截至 2026-03-28）承諾／風險段 |
| 賣方暫收款／保留費寫出下修規則 | **部分**　TSMC＝條件滿足後退款或抵應收、由雙方同意；GFS＝LTA 含預付／保留費＋未達量 underutilization＋2025 已重談量價期；CRUS 所見之賣方側規則＝非退還保留費＋短少費＋預付抵貨 |
| 設計商預付／承諾寫出下修規則 | **部分**　NVDA＝下定單前可取消／改期／調整、「may result in additional costs」；承諾美元主要記憶體＋製造設施混列。AMD＝超額庫存／生產成本；預付供給協議有現金流句、無對手方分列。MU＝反向（IDM 收客戶存款） |
| 兩側對**同一標的**（節點／期間／對手方） | **不通過**　TSMC 暫收款無對手方、無節點。NVDA US$279B ≠ TSMC NT$234,225,146 千，且 CFO 寫「primarily related to the procurement of memory」。唯一具名對手方對＝GFS↔CRUS |
| 兩側對**同一下修規則**（退款／抵帳／沒入） | **不通過**　TSMC 規則＝或然退／抵；NVDA 規則＝可改期＋額外成本（非沒入表）；CRUS 規則已分列但只覆蓋成熟節點單一協議 |
| 「預付方承擔全部損失」可寫成可拒絕區間 | **不通過**　TSMC 原文已把「全部」打開 |
| 穩定可拒絕之兩側對帳（保留權已被科目定價） | **僅 CRUS 單協議存在**　非先進邏輯市場合計 |
| 否決觸發 (1) | **觸發**　先進邏輯兩側停在合併餘額／混列承諾 |
| 否決觸發 (2) | **觸發**　TSMC 穩定句＝可退或可抵、雙方同意 |
| 否決觸發 (3) | **未觸發於目標市場**　CRUS 分列不外推為 TSMC／NVDA 已定價 |
| 升格 T | **否** |

失效歸因（§7-2）：不是檢索失敗。失敗在量綱——所需量（同一契約之節點／期間／對手方 × 同一退款／抵帳／沒入句）不是所讀之量（賣方合計暫收款、設計商記憶體＋製造混列承諾、成熟節點單客戶分列）。現況檔名＝上列 work／query。複查觸發器＝生成卡原文（見下）。停。

本格不入 §1。不改正本（對齊屬 SCOUT）。

---

## 已實讀載體

### A. 賣方｜TSMC 2Q26 合併財報 Note 20.c（2026-08-14）

**Temporary receipts from customers（NT$ 千）：**

| | 2026-06-30 | 2025-12-31 | 2025-06-30 |
|---|---|---|---|
| 流動（列於 accrued expenses and other current liabilities） | 141,853,142 | 146,559,275 | 155,973,239 |
| 非流動（列於 other noncurrent liabilities） | 92,372,004 | 43,298,936 | 65,942,034 |
| 合計 | **234,225,146** | **189,858,211** | **221,915,273** |

原文：「payments made by customers to the Company **to retain the Company’s capacity**. When the terms and conditions set forth in the agreements are subsequently satisfied, the treatment of temporary receipts, **either by refund or by accounts receivable offsetting, will be determined by mutual consent**.」

同附註分開列 **contract liabilities**（2026-06-30 NT$55,852,048 千；2025-12-31 NT$49,954,384 千；2025-06-30 NT$56,799,375 千）。暫收款 ≠ 合約負債 ≠ 已交付晶圓。

**指名不可見：** 節點／封裝層／期間；具名對手方；沒入 vs 退款的觸發表；與出貨對帳。R1 成立於賣方主科目本身。R5（時點用盡可見端）未被本輪否證：合計由 2025-06 NT$221.9B → 2025-12 NT$189.9B → 2026-06 NT$234.2B，無對手方拆解則變動可被出貨時點／新客戶／匯率解釋。

### B. 賣方法說｜TSMC 2Q26 逐字稿（頁面日 2026-08-28）

產能與客戶「well in advance」規劃；2026 CapEx 約 USD60–64B。**無**暫收款拆解、**無**下修條款、**無**退款／沒入句。本輪不把此句當 B 端參數（生成卡禁令）。

### C. 設計商｜NVIDIA FY27 Q2 10-Q Note 10（截至 2026-07-26）＋ CFO commentary

- Supply and capacity commitments：**USD279B**（上季 USD119B）。到期拆：FY27 餘 USD92B／2028 USD87B／2029 USD88B／其後小尾。
- 原文：「data center infrastructure systems, **primarily memory and manufacturing facilities**」。CFO commentary 再收窄：「**primarily related to the procurement of memory**」。
- 「in certain instances, these agreements may be **cancelable, rescheduled, or adjustable** for our business needs **prior to placing firm orders**. Changes to these agreements **may result in additional costs**.」
- 同表另列 cloud service agreements、未開始之 data center leases、股權承諾、CapEx——不是代工暫收款。
- 本輪 10-Q 本文**無** TSMC 具名、**無** prepaid wafers 科目對 TSMC Note 20.c、**無**節點保留權分列。

FY26 10-K（期 2026-01-25）風險／製造段：為鎖定供給與產能「paid premiums, provided deposits, and entered into long-term supply agreements and capacity commitments」；「prepaid manufacturing and capacity agreements」。此為質性菜單，**不是**可與 TSMC 暫收款對帳的餘額時序。

對帳試算（明示＝不可當官方乘積）：TSMC 暫收款合計約 NT$234B（約 USD7B 量級，視匯率）vs NVDA 承諾 USD279B。數量級差一到兩個數量級，且後者主述記憶體。R2 成立。

### D. 反向／記憶體｜Micron FY26 Q3 10-Q（截至 2026-05-28）

- Note 14：新簽 strategic customer agreements 為 **take-or-pay**、多年代量；RPO 約 USD5B，其中合約負債 USD422M「primarily consisted of **customer deposits**」。
- 流動性段：已締結協議預期「cash deposits and related financial commitments of **$22 billion**」；「Approximately **$18 billion** … in the form of cash deposits」。
- 方向＝**IDM 對戰略客戶收存款**，不是代工對設計商之排序權。記憶體長約，不能代入 L3-I 的代工暫收款對帳。

### E. 賣方對照｜GFS 20-F 2025（約 2026-02-27）

- LTA「include **customer advanced payments and capacity reservation fees** in order to secure future supply」。截至 2025-12-31 LTA 剩餘營收承諾約 **USD11B**。
- 「From time to time our wafer revenue consists of restructuring or **underutilization payments** from customers unable to meet their volume commitments。」
- 風險段：2025 已重談若干 LTA——拉長承諾期、降低價格或量。賣方可能因無法履約而付現金罰則；客戶違約則廠能空置。
- R4 成立：下修損失可契約化轉回（underutilization）或經重談攤開，不是「全部 ∈ 預付方」的單向沒入。

### F. 唯一兩側可對｜CRUS FY26 10-K Note 13（截至 2026-03-28）↔ GFS

2021-07-28 Capacity Reservation and Wafer Supply Commitment Agreement（GFS Singapore；Commitment Period 2022–2026；2025-02-18 修季出貨分佈）：

- **非退還**產能保留費原 USD60M，攤銷後餘額 **USD6.7M**（Other current assets）。
- 預付晶圓原 USD195M，自 FY24 Q2 起抵貨價；餘額 **USD14.7M**（科目「**Prepaid wafers**」）。
- 短少則付 **shortfall payments**。
- 估剩餘採購義務約 **USD180M**。

此為本輪唯一「同一標的、同一契約、下修規則寫死、兩科目已分列」的公開對。R3 在此協議上成立：排序／保留 vs 抵貨預付已被科目說完。限制（生成卡已寫）：成熟節點／單一客戶，不是先進邏輯產能市場合計。GFS 20-F **不**把該 USD6.7M／14.7M 從 USD11B LTA 桶拆出對 CRUS。後續 CRUS 10-Q 另有 2026-06-30 新簽 2027–2028 協議——本輪不把未對帳之新約寫進通過條件。

### G. 設計商｜AMD 10-Q（截至 2026-03-28）

- 無條件承諾約 **USD25.7B**（FY26 餘 USD18.3B），捆晶圓／基板／元件／雲協議／授權。
- 營運現金流句：prepaid expenses 增 USD308M，「primarily by **prepayments of supply agreements**」——無對手方、無節點。
- 風險段：與 GF 之晶圓供應協議至 2026，未達年採購目標則超額庫存或單位成本上升；另有長期採購承諾與 prepayment arrangements；需求高估則超額庫存與生產成本上升。
- **無**與 TSMC 暫收款之對帳列。

---

## 對種子與反方

| 主張 | B 端讀後 |
|---|---|
| 預付 → 保留權，不 → 產能所有權 | **可寫於 TSMC 原文**（retain capacity；結算＝退／抵，不是交付物權）。不是已鎖定產出噸位 |
| 需求下修 ⇒ 全部損失 ∈ 預付方 | **過強**。TSMC＝或然退／抵＋雙方同意；GFS＝underutilization＋重談；CRUS＝保留費沒入但預付晶圓抵貨 |
| 錯價＝把餘額／承諾美元當晶圓取用權充分統計 | 先進邏輯兩側無同一標的可對。可見端已被合計暫收款＋混列承諾用盡 |
| R1 可退／可抵削弱「全部損失」 | **成立**　TSMC Note 20.c |
| R2 設計商承諾記憶體／製造／雲捆一列 | **成立**　NVDA Note 10＋CFO「primarily memory」；AMD USD25.7B 同捆 |
| R3 保留費 vs 預付晶圓可分列則無錯價 | **在 CRUS↔GFS 成立**；不外推先進邏輯 |
| R4 下修損失可落賣方或轉回 | **成立**　GFS underutilization；LTA 重談 |
| R5 暫收款變動被時點用盡 | **未被否證**　無對手方拆解 |

「同一標的 × 同一下修規則」在本輪只有成熟節點單協議成立，故既不能接受也不能拒絕「先進邏輯預付餘額被誤讀為物權」。

---

## 不開 T／§7-4

進 T 需數值窗與可拒絕之 H1 倍數。本輪可寫入的只有「TSMC 暫收款合計與可退／可抵句存在、NVDA 承諾混列記憶體、CRUS 已分列保留費與預付晶圓」。不夠把下修損失歸屬寫成財富倍數窗。

§7-4 三題本輪不答（生成卡：轉入個股層時必問；本格不轉、不進 T）。題目本身已由本輪讀數預示方向（先進邏輯科目對不上、美股設計商承諾過寬、CRUS 分列＋TSMC 可退句壓縮「全部損失 ∈ 預付方」窗），但不在本輪作答。

**複查觸發器（沿用生成卡，不改寫）：** 任一美股可交易代工、IDM 或設計商於 20-F／10-K／10-Q，把產能保留預付與一般存貨預付／記憶體長約分列，並寫明需求下修時之退款、抵帳或沒入，且可與對手方同期科目對帳。

---

## URL

1. https://investor.tsmc.com/sites/ir/financial-report/2026/TSMC%202026Q2%20Consolidated%20Financial%20Statements_E_2.pdf
2. https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
3. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
4. https://d18rn0p25nwr6d.cloudfront.net/CIK-0001045810/9498713c-0387-46ee-ba58-9412ca866dce.pdf
5. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm
6. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
7. https://www.sec.gov/Archives/edgar/data/723125/000072312526000015/mu-20260528.htm
8. https://www.sec.gov/Archives/edgar/data/1709048/000170904826000022/gfs-20251231.htm
9. https://d18rn0p25nwr6d.cloudfront.net/CIK-0000772406/5a2a184d-6b4f-422f-90b6-d4caf751c320.pdf
10. https://www.sec.gov/Archives/edgar/data/2488/000000248826000076/amd-20260328.htm

**（完）**
