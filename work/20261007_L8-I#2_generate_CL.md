# L8-I#2 生成卡｜標註／驗證：誘因（買方持股競爭供應商——最大客戶之量向自家關係企業轉移）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260918_L8-I_generate_GK.md；archive/drive/USED_20260918_L8-I_test1_GK.md；work/20261007_L8-A#2_test1_CL.md | EMITS: work/20261007_L8-I#2_generate_CL.md -->
**日期：** 2026-10-07　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain）　**格：** L8-I　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格依據（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L8-A#2 本日測一不通過）。非「已殺／刻意排除」格中最後測試最舊者＝L8-I（測一 2026-09-18）。既有生成數 1 → 本卡 #2。
- 比對過之舊檔與死因型態，本卡須異型：
  - L8-I#1（`archive/drive/USED_20260918_L8-I_generate_GK.md`；測一 `archive/drive/USED_20260918_L8-I_test1_GK.md`）——品質不可契約（誰驗證驗證者）；不通過，死於爭議／退件／重工率申報層不存在、毛利變動與 C-I2 路徑不可分。本卡**不涉品質、不涉毛利**，只涉買方股權誘因下之量分配。
  - C-I2（ARCH_dead #12；專家單價由相鄰機制驅動）——本卡不涉單價。
  - L8-A#1／L8-A#2（條數分母；未開票）、L8-P（分鐘／條）——本卡不用產出單位、不用應收科目。
  - L13-I（供應方持有客戶股權 vs 應收帳齡，不通過）——方向相反：本卡為**客戶**持有**供應方之競爭者**股權；不同層、不同主體關係。重疊不構成丟棄。
- §7-10 領域最近公開更新：TaskUs Q2 2026 10-Q（期 2026-06-30）與財報稿（2026-08）；Innodata Q2 2026 10-Q（期 2026-06-30）。下一檢查點＝兩者 Q3 2026 10-Q（約 2026-11）。

## 1. 落差一句

買方持有某一標註供應商股權時，其誘因是把委外量導向該關係企業、並由中立供應商撤出；Meta 於 2025-06 以 US$14.3B 取得 Scale AI 49%，而 Meta 為 TaskUs 最大客戶（FY25 占服務營收 26%）。TaskUs Customer A 營收占比 Q2'25 26% → Q1'26 24% → Q2'26 20%；以占比×服務營收推得 Customer A 年減約 19%、其餘客戶年增約 13.5% `[D]`（與管理層「mid-teens growth from clients other than our largest client」一致）。管理層與市場把此讀成「分散化」；若實為最大客戶之結構性移轉，則屬單向、不可逆之量流失。**方向未定**：競爭解釋為 Meta 之 Trust & Safety 工作被自動化（與 AI 服務線無關）；另一面，Scale 之其他買方（Google、OpenAI）撤出可使中立供應商（TaskUs、Innodata）受益，兩效果可抵銷。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：買方股權 → 委外量向關係企業傾斜；對手買方因中立性疑慮撤出該關係企業 |
| 已讀事實 | Meta 投資 Scale AI US$14.3B、49%，約 2025-06-13；OpenAI 逐步停用、Google 據報計畫切斷（Fortune 2025-06-19）。TaskUs FY25 10-K：Meta 占 2025 營收 26%；10-Q Customer A：Q2'24 20%、Q2'25 26%、Q3'25 27%、Q1'26 24%、Q2'26 20%（應收占比 Q2'26 12%）。Innodata Q2 2026 營收 92.1（Q2'25 58.4，US$百萬），+58%。 |
| 時序 | Customer A 占比於交易前上升（20%→26%），交易後三季內回落至 20%——時序與誘因一致，但未排除他因 |
| 未證之連結 | ① Customer A 於 10-Q 是否即 Meta（10-K 具名，10-Q 匿名）；② Customer A 之下滑在哪一服務線（T&S 自動化 vs AI 服務改道）；③ Meta 是否確實增加對 Scale 之委外（若 Meta 亦減用 Scale，誘因主張翻負） |
| 量綱 | 客戶營收年增率（無因次）；客戶占比變動（百分點）；服務線營收年增率差 |
| 半衰期 | 每季 10-Q 重報；股權關係存續期內持續 |
| 重疊 | L13-I（反向股權，異層）；L8-I#1（同格，異機制）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；本輪未判可分離）

1. TaskUs 10-Q（期 2026-06-30）https://www.sec.gov/Archives/edgar/data/0001829864/000182986426000149/task-20260630.htm ——客戶集中（營收／應收）；服務線營收。
2. TaskUs 10-Q（期 2026-03-31）https://www.sec.gov/Archives/edgar/data/0001829864/000182986426000113/task-20260331.htm ——Customer A 24%／應收 11%（本卡 SCOUT 已讀於 L8-A#2 測一）。
3. TaskUs FY2025 10-K https://www.sec.gov/Archives/edgar/data/1829864/000182986426000012/task-20251231.htm ——「Meta accounted for 26%」；客戶風險因素。
4. TaskUs Q2'26 財報稿 https://www.sec.gov/Archives/edgar/data/0001829864/000182986426000147/earningsreleaseex991q22026.htm ——「mid-teens growth from clients other than our largest client」。
5. Innodata 10-Q（期 2026-06-30）https://www.sec.gov/Archives/edgar/data/0000903651/000110465926092021/inod-20260630x10q.htm ——客戶集中段本輪未取得（擷取止於附註前段），非不存在。
6. Fortune 2025-06-19 https://www.fortune.com/2025/06/19/openai-is-phasing-out-scale-ai-work-following-startups-meta-deal ——Meta–Scale 交易條件與對手買方撤出。

缺段（§7-2）：Customer A 依服務線之分列；Meta 對 Scale 之委外量；Innodata 客戶集中。失敗歸因＝本輪只讀上列前段；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | Meta 之 TaskUs 量以 Trust & Safety（內容審核）為主，下滑為 LLM 自動化審核所致，與 Scale 股權無關 | TELUS Q2 2026 MD&A：hyperscale 舊服務「automated faster than anticipated」，點名 content moderation（L8-A#1 測一已讀，`archive/drive/USED_20260918_L8-A_test1_GK.md`） | 若下滑集中於 T&S，誘因機制不成立 |
| R2 | Meta 實際未把量導向 Scale（研究員對 Scale 品質之負評見 HeroHunt 轉述，L8-I#1 生成卡 §3-5） | 非申報，本輪未實讀 | 若 Meta 亦減用 Scale，主張翻負 |
| R3 | 中立性紅利：Google／OpenAI 撤出 Scale，量流向中立供應商；TaskUs 其餘客戶 +13.5%、Innodata +58% | 載體 4、5、6 | 淨效果可能為正，非單向流失 |
| R4 | 管理層已公開拆出「最大客戶以外」成長率，市場已見集中度下降 | 載體 4 | 可能已定價 |

## 5. SCOUT 裁決

**生成 L8-I#2 並留。** 不進 T。下一動作＝ANALYST 測一。

否決觸發（寫給 ANALYST，逐條實讀）：
1. 10-Q／10-K／財報稿實讀後，Customer A 之營收無法依服務線分離，且無同檔代理（如 T&S 年增率與 Customer A 年增率之對照）→ R1 不可排除，否決。
2. 公開可得證據顯示 Meta 於 2025-06 後並未增加對 Scale 之委外（或明示減少）→ 誘因主張翻負，否決。
3. Customer A 占比之下滑始於 2025-06 之前，或 ≥ 4 季序列顯示其下滑與交易時點無關 → 時序不支持，否決。
4. 可運作對照只能寫成 L8-I#1（品質／爭議率）、C-I2（專家單價）、L8-A#1／#2（條數分母／未開票）、或 L13-I（供應方持股客戶 vs 應收）→ 換格或重開已死，否決。
5. 具名賣方或公司已公開以「Meta 移轉至 Scale」解釋 Customer A 下滑 → 已定價，非落差。

複查觸發器（若日後殺）：任一美股上市標註／驗證主體於 10-K／10-Q 依服務線揭露最大客戶營收，或具名揭露客戶對競爭供應商之股權關係對其量之影響；或 Meta 公開其資料委外之供應商分配。

## 6. 轉入個股層時必問（§7-4；本輪不答）
1. 財報科目：客戶集中（營收／應收占比）、服務線營收、客戶合約之便利終止條款。
2. 可交易工具：TaskUs（NASDAQ:TASK；私有化案 2025-10 終止）、Innodata（NASDAQ:INOD）；Scale AI 未上市。
3. 半衰期：股權關係存續期 vs ≥ 12 個月窗；合約 1–3 年、多可便利終止。
