# L4-I#2 生成卡｜運算硬體系統：誘因（加速器商以或有負債代替降價：雲端容量回租承諾、租約擔保、客戶認股權證＝賣出 GPU 租價賣權）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260926_L4-I_generate_GK.md；archive/drive/USED_20260926_L4-I_test1_GK.md；work/20261011_L4-A#2_test1_CL.md | EMITS: work/20261011_L4-I#2_generate_CL.md -->
**日期：** 2026-10-11　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain）　**格：** L4-I　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L4-A#2 已於本日測一）。最後測試日最舊＝2026-09-26 一批尚無 #2 者：L4-I、L5-A、L5-I；依表序取 **L4-I**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py "customer warrant" "contra revenue" "cloud service agreements"`，命中 **0** 筆；本卡載體由 `sec.py` 原文取得。
- 比對之舊檔與死因型態，本卡須異型：
  - **L4-I#1**（`archive/drive/USED_20260926_L4-I_generate_GK.md`；測一 `archive/drive/USED_20260926_L4-I_test1_GK.md`）：開放參考設計＝商品化互補品；所需量 `s_sys(t)`（系統 vs 元件美元時序）**不在申報層**，死於 (1)。本卡換為加速器商**自身資產負債表外之或有承諾**：所需量（回租承諾總額、擔保最大曝險、認股權證股數與歸屬條件）**為 10-Q 附註原文數字且 ≥ 2 期**。
  - **C-I3′**（生態鎖定；分部毛利由非機制項解釋）：本卡不用分部毛利。
  - **L13-I**（應收總額／載具評等；帳齡不可並列）、**L6-I**（backlog 變厚≠對手方變好）：兩者看**雲端／融資載具之信用**；本卡看**賣方讓渡之選擇權價值**（雲端在租價高時轉售第三方、租價低時回租給賣方），信用違約只是其中一支（擔保）。重疊列為否決 (4)。
  - **T-15 CoreWeave 空方**：委託資本外，非殺；本卡表達端為加速器商，非雲端。
  - **L3-I#2**（DOC 認股權證／分拆或有稀釋）：同為權證，但彼為政府持有、觸發為股權結構；本卡為**客戶**持有、歸屬綁定採購量＝價格讓渡。型態不同。
  - **L4-A#2**（整機商營運資本）：構成不同。
- §7-10 領域最近公開：NVIDIA Q2 FY27 10-Q（期末 2026-07-26，申報 2026-08-26）；AMD Q2 2026 10-Q（期末 2026-06-27，申報 2026-08-05）；WSJ 轉述之計畫暫停報導（2026-08-28）。下一檢查點＝AMD Q3 10-Q（約 2026-11 初）、NVIDIA Q3 FY27 10-Q（約 2026-11 下旬）。

## 1. 落差一句

加速器商在出貨時認列全額營收，但同時把部分價格讓渡寫成或有承諾：NVIDIA「AI clouds procure our data center infrastructure products and we commit to cloud service agreements, which the AI clouds can unilaterally stop providing to us and sell to third-party customers at more advantageous rates」——即雲端持有**免費選擇權**（租價高時賣給第三方、租價低時回租給 NVIDIA），NVIDIA 等於**賣出 GPU 租價賣權**；另有租約擔保（換取權證或獨家）與客戶認股權證（AMD 對 OpenAI、Meta 各 160M 股 @ $0.01，按 GPU 採購里程碑與股價目標歸屬）。這些讓渡於報表上「fair value not significant」或「no impact」。**落差＝市場以資料中心營收讀終端需求與售價，而有效售價＝營收 − 讓渡選擇權之現值；該現值在 GPU 租價下跌時才實現，且其行使可由回租承諾之「未被第三方用掉」比例事前觀測。**

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因（賣方以或有負債換取需求／獨家；選擇權讓渡）；非會計恆等、非守恆 |
| 選擇者 | 加速器商（承諾規模、擔保、權證）；AI 雲端與模型商（行使：轉售第三方 vs 回租賣方；違約） |
| 可見端 | NVIDIA Q2 FY27 10-Q：AI cloud agreements 承諾 36B（「typically six years」「decrease as capacity is used by third-party customers」）；Cloud service agreements 29B（另列，R&D 用）；land, power, and shell guarantees 3.5B（換權證；夥伴託管 712M）；SB Energy 擔保上限 105B（代 OpenAI 關係企業，換取「exclusively host NVIDIA AI infrastructure」，首期 FY2029）；公開公司權證名目 4.8B。前期：雲端服務承諾 27B（2026-01-25）→ 30B（2026-04-26）。AMD Q2 10-Q：OpenAI／Meta 權證各 160M 股；商業夥伴資料中心租約擔保最大曝險 4.1B（「may be issued in exchange for warrants」）；無條件承諾 30.3B（含多年期 CSP 雲端容量，「may be reduced, terminated or sold to others by the CSPs」） |
| 指名不可見端 | 回租承諾之已用／被第三方用掉之比例（季序列）；回租單價 vs 市場 GPU 時租；權證歸屬時之收入抵減（ASC 606 對客戶之對價）時點與金額 |
| 主張 | 讓渡選擇權價值與 GPU 租價負相關；租價下跌時：回租承諾不被第三方消化 → 賣方承擔租金（費用）或認列損失；擔保曝險上升；權證歸屬（若同時達採購量）→ 收入抵減。翻轉點＝市場 GPU 時租跌破回租單價 |
| 表達工具型態（只指名，不選券） | 美股可交易之加速器商（NVIDIA、AMD）。不選券 |
| 重疊 | L13-I／L6-I（對手方信用）；T-15；L3-I#2（權證）。重疊不構成丟棄 |

對照式（生成用，非正式載入）：`P_eff = Rev − PV(put on GPU-hour rate; strike = 回租單價, notional = 回租承諾) − PV(擔保) − FV(權證歸屬)`。本輪不估參數、不寫 H1。

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. NVIDIA Q2 FY27 10-Q（Note 8 衍生工具名目、Note 13 承諾與擔保、MD&A AI cloud 段）。https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
2. NVIDIA Q1 FY27 10-Q 與 FY26 10-K（前期承諾與擔保）。https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm ；https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
3. AMD Q2 2026 10-Q（權證、擔保、Note 10 承諾）與 Q1 2026／Q3 2025 10-Q（序列）。https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm ；https://www.sec.gov/Archives/edgar/data/2488/000000248826000076/amd-20260328.htm ；https://www.sec.gov/Archives/edgar/data/2488/000000248825000166/amd-20250927.htm
4. 計畫暫停報導（CloudNews.Tech 轉述 WSJ，2026-08-28）：「NVIDIA has paused part of its newly launched program for financial support and revenue sharing with AI cloud providers」；NVIDIA 發言人「the model unveiled in July still exists and continues to evolve」。https://cloudnews.tech/nvidia-pauses-its-new-model-for-financing-ai-clouds-over-antitrust-concerns/
5. 市場 GPU 時租序列（測一須定位具名、可回溯之公開指數或報價；本輪未讀）。

測一須另取：回租承諾之已用比例或「decrease」之季額；回租單價或其與市場時租之關係之任何原文；權證歸屬條件之採購量門檻原文（8-K 附件）；管理層對承諾之會計處理（費用 vs 收入抵減）。**不宣稱讓渡價值已可估，不宣稱已錯價。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 回租承諾為賣方自身 R&D 真實需求（Nemotron、Cosmos、GR00T），非需求支撐 | NVIDIA 10-Q「Cloud service agreements – … support our research and development of our open models」 | 變動由非機制項解釋（C-I3′ 型）；但 AI cloud agreements 36B 另列且明文可轉售第三方，須分開判 |
| R2 | 曝險相對營收小（擔保 3.5B、AMD 4.1B；SB Energy 105B 首期 FY2029），讓渡現值不足以改變有效售價 | 兩家 10-Q | 機制真、量級不足（可能落 §1 門檻外；測一不判 H1，但須記） |
| R3 | 「循環融資」已是公開議題，市場已折價 | WSJ／CloudNews 2026-08-28；大量評論 | 落差為共識 |
| R4 | 讓渡只在雲端違約時實現＝信用問題，落入 L13-I／L6-I | 擔保條款「triggered upon certain tenant defaults」 | 機制換層 |
| R5 | 計畫已部分暫停（反壟斷顧慮），前瞻窗不足 12 個月 | 同 4 | 半衰期不足 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 兩家 ≥ 2 期申報均不揭露回租承諾之已用／被第三方消化比例或回租單價，只剩總額（選擇權行使不可觀測）。
(2) AI cloud agreements 之變動可完全由賣方自身 R&D 使用或單一合約事件解釋，並有管理層原文佐證（C-I3′ 型）。
(3) 公開層（10-Q／法說／具名賣方或媒體）已明文量化讓渡選擇權或回租承諾之損益影響，使落差為共識。
(4) 讓渡之唯一實現路徑為對手方違約（擔保），租價路徑不存在或被條款排除——即機制落入 L13-I／L6-I。
(5) 計畫終止或承諾於 ≥ 2 期內歸零，前瞻窗 < 12 個月。

複查觸發器（若日後殺）：任一美股可交易加速器商於 10-K／10-Q 揭露回租承諾之使用率、回租單價，或因承諾／擔保／客戶權證認列損失或收入抵減 ≥ 1 期。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：讓渡落於費用、其他收益（衍生工具公允價值）或收入抵減？是否可與 R&D 雲端支出分離。
2. 可交易工具：NVIDIA、AMD 皆美股可交易；讓渡相對其市值之量級。
3. 半衰期：GPU 租價跌破回租單價之時點、權證歸屬時點是否落在 ≥ 12 個月窗內。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L4［I］標「#2 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L4-I#1／L4-A／L4-A#2／L4-P／L4-P#2／C-I3′／L13-I／L6-I／L3-I#2 結論。
