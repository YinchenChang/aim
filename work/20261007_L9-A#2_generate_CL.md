# L9-A#2 生成卡｜受規管 HITL：會計恆等（毛節省計費 vs 聯邦仲裁回吐——PSAV 收入基數未扣 IDR 逆轉）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/INDEX.json；archive/drive/USED_20260921_L9-A_generate_GK.md；archive/drive/USED_20260922_L9-A_test1_GK.md | EMITS: work/20261007_L9-A#2_generate_CL.md -->
**日期：** 2026-10-07　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain）　**格：** L9-A　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格依據（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L8-I#2 本日測一不通過）。非「已殺／刻意排除」格中最後測試最舊＝2026-09-22（L9-A、L9-I、L12-P、L12-A、L12-I 同日）；同日依表序取 L9、再依 [P][A][I] 序取 L9-A（L9-P 已殺）。既有生成數 1 → 本卡 #2。
- 比對過之舊檔與死因型態，本卡須異型：
  - L9-A#1（`archive/drive/USED_20260921_L9-A_generate_GK.md`；測一 `archive/drive/USED_20260922_L9-A_test1_GK.md`）——應用層 SaaS 每席次交付成本（推論＋支援）÷席次；死於席次與推論＋支援不同表、毛利額離散度＝規模。本卡**不涉席次、不涉 AI COGS、不涉 SaaS**。
  - C-A1（ARCH_dead #6，consumption／Agentforce 毛利不可分列）、C-I5（#18，AI 採用 cohort NRR）、L9-P（#1，AI 建議人工核可率／HITL 工時）——本卡之「人」為聯邦認證之獨立仲裁實體（IDRE），量綱為美元節省與仲裁裁決，不是工時、核可率或留存。
  - L2-A#2（利息資本化墊高 AFFO）為他層「調節項墊高指標」型；本卡為「收入基數用毛額、逆轉落在客戶端」，非資本化。重疊不構成丟棄。
- §7-10 領域最近公開更新：Claritev Q2 2026 10-Q（期 2026-06-30）；Georgetown CHIR／Health Affairs IDR 2025 全年資料（Fierce 2026-08-26 報導）。下一檢查點＝Claritev Q3 2026 10-Q（約 2026-11）；CMS IDR 公開資料下一批。

## 1. 落差一句

聯邦 No Surprises Act 下，付款方對網外帳單之出價（多由第三方定價商以 QPA 法算出）可被醫療提供者送交 IDR 由人類仲裁者裁決；Claritev 之 PSAV（節省百分比）收入以定價當下之**毛節省**為基數，而 2025 年提供者勝率約 85–88%、爭議量年增 77%、Claritev 客戶出價被採納率僅 20–24%。恆等式：**付款方實現節省＝定價節省 − IDR 裁決超額 − IDR 費用**；若 PSAV 費不隨 IDR 敗訴回吐，Claritev 之收入基數與客戶實現價值之差隨爭議量擴大。市場把「PSAV 收入四年新高」與「NSA 業務帶動成長」讀成兩個正面訊號；若兩者同源於爭議量上升，則同一驅動同時侵蝕客戶淨節省。**方向未定**：若合約已含敗訴回吐（10-Q 所稱「credits」），差距已在收入認列之變動對價限制內處理。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：收入基數（毛節省）≠ 客戶實現節省（扣 IDR 逆轉） |
| 已讀事實 | Claritev Q2'26 10-Q：Claims Intelligence 營收 178.465（Q2'25 156.966，US$百萬）；Network 50.333（54.125）；PRI 28.680（30.479）；PSAV 占營收 85.8%（82.6%）。資產負債表「Unbilled Independent Dispute Resolution fees, net」17.995（12-31-25 10.563）。收入認列：「Significant judgment is required to estimate constrained variable consideration」；PSAV 收入「may be returned or credited in subsequent periods」，因「payers not utilizing the discounts that were initially calculated」。 |
| 外部參照 | Georgetown CHIR（Hoadley 等，2026-03）：2025 上半年 120 萬件爭議、提供者勝 88%；Fierce 2026-08-26：2025 年 260 萬件（+77%）、IDR 總成本 22.4B、急診中位裁決 315% QPA。Claritev 2026-07-30 新聞：處理約 27 萬件仲裁、客戶出價採納率 2025 年 20%（業界 12%）、Q4 24%。 |
| 未證之連結 | ① PSAV 合約是否於 IDR 敗訴時回吐節省費（「credits」之定義是否涵蓋）；② NSA 相關節省占 PSAV 收入之比重；③ 未開票 IDR 費之性質（代墊實體費 vs 服務費應收）與敗訴時之回收對象 |
| 量綱 | 美元節省（毛／淨）；IDR 敗訴率（無因次）；PSAV 收入（US$）；未開票 IDR 費（US$） |
| 半衰期 | 每季 10-Q；NSA 規則（IDR 費率、批次規則）每年 CMS 更新；客戶合約多年 |
| 重疊 | L9-A#1（同格異機制）；L2-A#2（他層，調節墊高型）；L9-P（同層「人類裁決」但量綱為工時）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；本輪未判可分離）

1. Claritev 10-Q（期 2026-06-30）https://www.sec.gov/Archives/edgar/data/0001793229/000179322926000067/ctev-20260630.htm ——收入認列（PSAV、變動對價限制、credits）；服務線營收；合約類型占比；未開票 IDR 費。MD&A 本輪未取得（擷取未回傳），非不存在。
2. Claritev 10-Q（期 2026-03-31）https://www.sec.gov/Archives/edgar/data/0001793229/000179322926000046/ctev-20260331.htm ——同上之前一季。
3. Claritev FY2025 10-K（本輪未讀）——PSAV 合約條款、IDR 服務收費結構、客戶集中。
4. Claritev Q2'26 電話會摘要（MarketBeat／Nasdaq 2026-08-07）https://www.nasdaq.com/articles/claritev-q2-earnings-call-highlights ——「growth was led by … No Surprises Act business」；NSA 增幅「primarily tied to one client」；PSAV 220（近四年新高）；「arbitration outcomes outperform the industry by approximately eight percentage points」。
5. Claritev 2026-07-30 新聞（iTiger 轉載）https://www.itiger.com/news/1100115469 ——27 萬件仲裁、出價採納率 20%／24%。
6. Georgetown CHIR https://chir.georgetown.edu/the-no-surprises-act-idr-process-an-early-look-at-2025-data/ ；Fierce Healthcare 2026-08-26 https://www.fiercehealthcare.com/regulatory/costs-tied-no-surprises-acts-idr-process-hit-22b-2025-study-finds ——全市場勝率、量、成本。

缺段（§7-2）：PSAV 合約對 IDR 敗訴之回吐條款；NSA 節省占 PSAV 比；credits 之歷史金額。失敗歸因＝本輪只讀 10-Q 前段與二手摘要；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 10-Q 已明列 PSAV 收入可回吐並以變動對價限制估計；IDR 敗訴若屬「payers not utilizing the discounts」，收入已淨額化 | 載體 1 | 恆等差已在認列內，無落差 |
| R2 | 爭議量上升反使 Claritev 之 IDR 服務需求上升（管理層：NSA 業務帶動成長、仲裁結果優於業界 8pp）；客戶之替代方案更差，價值主張未受損 | 載體 4、5 | 淨效果可能為正 |
| R3 | 多數網外理賠不進 IDR（2.6M 件 vs 理賠總量），敗訴逆轉之美元占 PSAV 基數可能很小 | 載體 6 量級；本輪未算 | 量級不足 |
| R4 | NSA 增幅集中於單一客戶——屬客戶集中與合約時點，非恆等差 | 載體 4 | 競爭解釋 |

## 5. SCOUT 裁決

**生成 L9-A#2 並留。** 不進 T。下一動作＝ANALYST 測一。

否決觸發（寫給 ANALYST，逐條實讀）：
1. 10-K／10-Q 實讀後，PSAV 合約明示 IDR 敗訴（或任何節省未實現）即回吐費用，且 credits 已計入變動對價限制 → 收入已以淨節省為基數，否決。
2. NSA／IDR 相關之節省或收入無法於 10-K／10-Q／財報稿與其他 PSAV 分離，且無同檔代理（如未開票 IDR 費、NSA 營收描述之量化）→ 不可觀測，否決。
3. 以申報或公開資料粗估，IDR 敗訴逆轉之美元占 Claims Intelligence 營收基數之量級 < 數個百分點且無擴大序列 → 量級不足，否決。
4. 可運作對照只能寫成 L9-A#1（席次／AI COGS）、C-A1、C-I5、L9-P（工時／核可率）或 L2-A#2（資本化墊高）→ 換格或重開已死，否決。
5. 具名賣方或公司已公開量化 IDR 敗訴對 PSAV 收入或客戶淨節省之影響 → 已定價，非落差。

複查觸發器（若日後殺）：Claritev 或任一上市定價／支付完整性主體於 10-K／10-Q 揭露 IDR 敗訴導致之收入回吐金額；或 CMS 公開按定價商分列之 IDR 結果。

## 6. 轉入個股層時必問（§7-4；本輪不答）
1. 財報科目：PSAV 收入、變動對價限制、credits／退款負債、未開票 IDR 費、服務線營收。
2. 可交易工具：Claritev（NYSE:CTEV）；IDR 實體與多數支付完整性同業未上市。
3. 半衰期：NSA 規則年更；IDR 批次與費率規則（2026 IDR 運作規則）；合約多年期 vs ≥ 12 個月窗。
