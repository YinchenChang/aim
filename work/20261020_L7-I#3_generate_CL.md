# L7-I#3 生成卡｜模型層：誘因（直營產品與 API 大客戶之通路衝突：實驗室垂直整合誘因 → 集中客戶之自建／換供應商誘因）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260930_L7-I_generate_GK.md；archive/drive/USED_20260930_L7-I_test1_GK.md；archive/work/20261013_L7-I#2_generate_CL.md；work/20261013_L7-I#2_test1_CL.md；work/20261020_L7-A#3_test1_CL.md | EMITS: work/20261020_L7-I#3_generate_CL.md -->
**日期：** 2026-10-20　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3→4／6）　**格：** L7-I　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L7-A#3 本日已測一，Q-0071 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-13（L7-I、L10-P／A／I、L11-A／I、L13-P、L13-I、L14-P、L14-A）；依表序取 **L7-I**。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py "Long-Term Benefit Trust" governance PBC "dual-class" board`（治理方向之初探），命中 0；本卡改題後未再查。載體全由本輪 WebSearch／WebFetch 實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L7-I#1**（測一不通過）：評測集取用權合約性、分數與取用不可分離。本卡不論評測。
  - **L7-I#2**（部分通過）：研究人才外部選擇權 × 股權報酬。本卡不論人才、不論 SBC。
  - **C-I1**（死 #10）：估值歸因權重能力。本卡不主張估值歸因。
  - **L10-I**（測一不通過）：分發層「預設份額與選擇次數不可並列」。本卡**不需**預設份額或選擇次數：B 端為實驗室申報之客戶集中度（前二大客戶占營收）與營收拆分（訂閱／用量／市集）之序列，以及具名客戶之自建模型／方案改版之公告日——測一須查 L10-I 死因是否同樣適用。
  - **L10-I#2**（導出佣金 → 開發者路由）、**L14-I／#2**（企業採購／裁員歸因）：主體不同。
  - **L7-A#3**（本日部分通過）：同一 S-1 轉述資料源（Reuters），但本卡用其客戶集中段而非市集認列段；重疊照記。
  - 治理（LTBT／超級表決權）：初探後放棄——TechTimes（2026-08-19）、Yahoo Finance 已公開廣泛討論，預期 (1) 即觸發；不寫。
- §7-10 領域最近公開：Cursor 新方案含 Grok、不含 Claude 用量（2026-10-12 上線；Schmalbach 2026-10-13）；Clarity（2026-09-06，引 Ramp）；TradingKey 讀 Reuters S-1 轉述（2026-09-30）。下一檢查點＝公開 S-1 之客戶集中與營收拆分附註。

## 1. 落差一句

恆等骨架：`R ≡ R_sub + R_use + R_mkt`；`R_use ⊇ R_top2`（前二大客戶）。誘因：實驗室直營產品（Claude Code／訂閱）每單位用量之毛利 `m_d` 高於 API 批發 `m_w` 時，實驗室有垂直整合誘因；中介（編碼工具）之毛利受實驗室批發價擠壓、且與實驗室直營品同場競爭，中介有自建（開源底模微調）或換供應商之誘因。已見數點：Reuters 讀 S-1——兩名未具名客戶各約 12% 營收、訂閱約 789M（< 20%）、用量約 3.8B；Ramp／Clarity：Cursor 與 GitHub Copilot 約 1.2B／5B（24%）；Cursor Composer 2（2026-03，Kimi K2.5 底模，列表價約為 Opus 4.6 之 1/10）；Cursor 2026-10-12 新方案納 Grok、Claude 改逐次加價。種子主張：市場以「前沿能力 → 用量」看 API 營收，而 **24% 集中營收之對手方本身有明確且已行動之換供應誘因**，其流失路徑（方案改版 → 用量轉移 → 申報集中度下降）在公開 S-1 與首份 10-Q 可驗；本卡不定方向與量級，只立可拒絕之誘因鏈。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因（通路衝突：上游垂直整合 × 下游自建／多源） |
| 量綱 | 前二大客戶占比［無量綱］；營收拆分 $／yr；批發 vs 直營列表價 $／M token |
| 可見端 | S-1 客戶集中揭露（ASC 280 ≥ 10% 客戶）、營收拆分；具名中介之方案頁與模型公告（日期）；Microsoft 10-Q／GitHub 模型選單 |
| 指名不可見端 | 各客戶季度用量；中介內部模型路由比例；批發折扣 |
| 主張 | 集中客戶之換供應事件（已發生：Composer 2、Cursor 方案改版）領先於申報集中度變化；可由「具名賣方已以客戶流失建模」或「S-1 揭露長約／最低承諾鎖定前二大客戶」拒絕 |
| 外部參照物（測一查證） | 上游供應商進入下游市場後失去大客戶之前例（僅作路徑先例，測一取具名案例） |
| 表達工具型態（只指名，不選券） | 模型實驗室普通股（上市後）；不選券 |
| 重疊 | L10-I（預設份額）、L7-A#3（同一 S-1 轉述）、C-A5（L7 上市性）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. TradingKey（Yulia Zeng，2026-09-30）https://www.tradingkey.com/analysis/stocks/us-stocks/262193114-anthropic-ipo-filing-reveals-revenue-breakdown-amazon-google-tradingkey （本輪實讀：兩客戶各約 12%、訂閱約 789M、用量約 3.8B）
2. Clarity（2026-09-06）https://theclarity.us/editions/2026-09-06/investor （本輪實讀：Cursor＋Copilot 約 1.2B／5B，引 Ramp）
3. The Decoder（Matthias Bastian，2026-03-19／21）https://the-decoder.com/?p=33391 （本輪實讀：Composer 2 定價、Kimi K2.5 底模、仍支援 Claude）
4. Schmalbach（2026-10-13）https://www.vincentschmalbach.com/did-anthropic-just-lose-its-biggest-customer/ （本輪實讀：Cursor 2026-10-12 新方案含 Grok、Claude 改逐次付費；無流量數字）
5. PYMNTS（2026）https://www.pymnts.com/news/artificial-intelligence/2026/openai-and-anthropic-get-80percent-of-revenue-from-1percent-of-customers/ （本輪未讀，指名）
6. 測一須另取：公開 S-1 客戶集中附註與合約期限；Microsoft 10-Q 之 GitHub Copilot 模型供應敘述（sec.py）；Cursor 官方方案頁原文；具名賣方是否已以 Cursor／Copilot 流失建模；上游進入下游失大客戶之前例。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 集中度與 Cursor 改版已廣泛報導（「Did Anthropic just lose its biggest customer?」） | #2、#4 | 已定價 |
| R2 | 中介仍支援 Claude、使用者可逐次付費；換供應只改預設，不改用量 | #3、#4 | 誘因不足以移轉用量（亦即 L10-I 死因：預設份額不可觀測） |
| R3 | 營收成長以企業直簽與 Claude Code 為主，前二大占比自然稀釋 | #1（訂閱 < 20% 之反面需測一查） | 不重大 |
| R4 | 公開上市未發生或延後，L7 無可交易主體 | `work/20261020_L7-A#3_test1_CL.md` (5) | 表達失敗（同 C-A5 死因） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 具名賣方／研究機構已以前二大客戶流失（Cursor／Copilot 換供應）建模實驗室營收——已定價（R1）。
(2) 公開 S-1 或可得資料顯示前二大客戶有多年最低承諾或排他條款，或其占比已降至 < 10%——鎖定或不重大（R2／R3）。
(3) 唯一可觀測端為中介之預設模型選擇，而客戶集中度無季度序列——同 L10-I 死因（R2）。
(4) 可運作對照只能寫成 L10-I、L10-I#2、L14-I／#2、L7-A#3 或 C-A5。
(5) 至測一日 EDGAR 無公開 S-1，且無已上市主體能分離實驗室之客戶集中——表達不可行（R4）。

複查觸發器（若日後殺）：EDGAR 出現模型實驗室公開 S-1 或首份 10-Q 揭露 ≥ 10% 客戶序列；具名中介公告停用或降級某實驗室模型；Microsoft 10-Q 首次揭露 Copilot 模型供應商結構。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：S-1 客戶集中（≥ 10% 客戶）附註、營收拆分、遞延收入／最低承諾。
2. 可交易工具：模型實驗室普通股（上市後）。不選券。
3. 半衰期：公開 S-1 → 首份 10-Q（客戶集中更新）。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L7［I］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L7-I#1／#2、L7-A#1–#3、L7-P#1–#3、L10-I／#2、L14-I／#2、C-A5、C-P3、C-I1 結論；不寫 T-15。
