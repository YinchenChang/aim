# L10-P#2 生成卡｜分發與中介：守恆（需求來源通道守恆：預訂量 ≡ 直接＋付費＋自然搜尋＋B2B＋AI 介面；自然搜尋通道萎縮之量須由他通道承接，承接價格進入行銷費用率）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/FILEIDS.tsv；archive/drive/USED_20260930_L10-P_generate_GK.md；archive/drive/USED_20260930_L10-P_test1_GK.md | EMITS: work/20261013_L10-P#2_generate_CL.md -->
**日期：** 2026-10-13　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3→4／6）　**格：** L10-P　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L7-A#2 測一 2026-10-13，Q-0028 done）。非已殺／刻意排除之格中最後測試日最舊者：`archive/FILEIDS.tsv` archive_work 時戳 L10-P 測一 2026-09-30T09:47:02Z，早於 L10-A 2026-10-01T06:38Z → **L10-P**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py booking travel agent referral traffic`（5 筆）、`agentic commerce checkout`（2 筆），皆為推論效能／agent 評測成本，與本卡無關；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L10-P#1**（測一不通過，`archive/drive/USED_20260930_L10-P_test1_GK.md`）：端側能量／殼溫上界分流功能留端或回雲；死因＝留端 vs 回雲之功能類不可並列。本卡不論裝置、能量、殼溫；守恆量是**需求側之預訂單位**（room nights），兩側皆為申報行。
  - **L10-A**（測一不通過）：中介收入＝轉介量 × 每次分潤率（搜尋商 TAC 側）；死因＝轉介量與分潤率不可並列。本卡站在**目的地側**，守恆量為預訂量非收入；若實讀後只能寫成 CPC × 點擊，即滑回 L10-A（否決 (2)）。
  - **L10-I**（測一不通過）：預設槽位／選擇畫面義務。本卡不論預設槽位。
  - **L11-P**（死 #3，結構性不可表達：注意力秒數）、**L11-A**（曝光數 × 每次曝光價）：本卡不論注意力或曝光。不恢復 L11-P。
  - **C-A5**（死 #13）：API 單價。無關。
- §7-10 領域最近公開：Booking 2Q26 10-Q（2026-08-04）、Expedia 2Q26 10-Q（2026-08-06）、Tripadvisor 2Q26 10-Q（2026-08-06）。下一檢查點＝三者 3Q26 10-Q（約 2026-10 下旬至 11 月初）、FY26 10-K（2027-02）。

## 1. 落差一句

市場把「AI 回答介面取代點擊」讀成 OTA 之需求或品牌問題；種子主張：預訂量在通道間守恆（直接＋付費搜尋／metasearch／affiliate＋自然搜尋＋B2B＋AI 介面＝總量），自然搜尋通道被 AI 摘要吃掉之量不消失而須由他通道承接，承接之邊際價格（付費 CPC、AI 介面分潤）進入「行銷費用 ÷ 總預訂額」——錯價只在把行銷費用率之上升讀成週期性 ROI 雜訊，而非通道守恆下之結構性轉移。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆**：\(Q = Q_{dir} + Q_{paid} + Q_{SEO} + Q_{B2B} + Q_{AI}\)；\(\Delta Q_{SEO} < 0\) 且 \(Q\) 由旅遊需求外生決定 ⇒ \(\sum_{其他}\Delta Q = -\Delta Q_{SEO}\)；行銷費用率 \(m = (c_{paid}Q_{paid} + c_{AI}Q_{AI} + \text{brand})/GB\) |
| 選擇者 | 承接通道（直接 vs 付費 vs AI 介面）；AI 介面是否收取分潤或改為導流至 OTA 應用（Bernstein Clarke 之反方）；付費通道 CPC |
| 可見端 | 10-Q 季度 room nights；行銷費用與「% of Total gross bookings」；直接通道占比（TTM，粗粒度「mid-fifties」）；管理層對 SEO 下降之歸因句 |
| 指名不可見端 | 各通道之精確 room nights 份額（只有直接通道 TTM 區間）；AI 介面通道之量與單價；SEO 通道絕對量 |
| 表達工具型態（只指名，不選券） | 美股可交易、於 10-Q 分列行銷費用率與通道組成之大型 OTA／metasearch 主體。不選券 |

種子只主張守恆約束使 \(m\) 之變動可部分歸因於 \(\Delta Q_{SEO}\)；**不主張 \(m\) 方向必然上升（AI 介面若成為低價通道，方向可反），不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Booking 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1075531/000107553126000037/bkng-20260630.htm ：「Room nights 325 309 5.3 %」；「Marketing expenses $ 2,371 $ 2,139 … % of Total gross bookings 4.7 % 4.6 %」；「slightly higher … driven primarily by declines in SEO, which remains a small component of our overall distribution mix, as well as changes in paid traffic mix」；「The mix of total room nights booked by consumers coming directly to our platforms was a mid-fifties percentage」；「we expect SEO traffic to decline in the short to medium term, which may lead to increased spend in paid marketing channels」。
2. Expedia 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1324424/000132442426000053/expe-20260630.htm ：「Selling and marketing - direct 2,119 1,920」（含「traffic generation costs from search engines」）；競爭段「AI powered digital planning and assistance」。
3. Tripadvisor 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1526520/000119312526336693/trip-20260630.htm ：「AI overviews displacing top ranked links, reduced click-through rates and a shift towards platform based non-traditional search」——SEO 依賴最高之主體，作 \(\Delta Q_{SEO}\) 上游對照。
4. Inside Retail／Reuters（Jain，2026-03-06）https://insideretail.us/openai-to-scale-back-plans-to-integrate-travel-bookings-in-chatgpt/ ：OpenAI 縮減 ChatGPT 內直接訂旅，改「checkouts inside specific third-party apps」；「OpenAI found ChatGPT users were researching products in the chatbot but not completing purchases through it」——\(Q_{AI}\) 之承接型態。

缺段（§7-2）：≥ 4 季行銷費用率序列（Booking、Expedia 各季 10-Q）；直接通道占比之季度或年度精確值；SEO／AI 通道量之任何數值揭露；Expedia 行銷費用之通道拆分。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | AI 平台改走第三方應用 checkout，OTA 仍能「get in front of consumers on AI platforms」 | Bernstein Richard Clarke（§3-4） | 承接通道成本可能不升，守恆成立但 \(m\) 不動 |
| R2 | LLM 無法處理取消／退款，供給與支付複雜度使 OTA 不可被繞過 | Booking CFO Steenbergen，Morgan Stanley TMT 2026-03-03（TIKR 轉述 https://www.tikr.com/blog/booking-holdings-stock-is-flat-for-a-year-while-eps-growth-hit-22-whats-next ） | \(Q_{AI}\) 不形成獨立通道 |
| R3 | SEO 為「small component」，量級不足以移動 \(m\) | Booking 10-Q（§3-1） | 機制成立、量級不足 |
| R4 | \(m\) 受 CPC、取消、外匯、中東衝突等多因子驅動，SEO 項不可分離 | Booking 10-Q 同段（因子清單） | 歸因不可分離（§7-4 第一題） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法就 ≥ 2 家上市主體取得 ≥ 4 季「行銷費用率」與「通道組成或 SEO 歸因」之同檔申報行；或
(2) 可運作對照只能寫成 CPC × 點擊或分潤率（滑回 L10-A）、預設槽位（L10-I）、注意力秒數／曝光價（L11-P／L11-A）、或端側能量（L10-P#1）；或
(3) 管理層或具名賣方原文已把 SEO 轉付費之成本上升量化並納入指引（已定價）；或
(4) ≥ 4 季內行銷費用率之變動，管理層歸因中 SEO／AI 通道從未居首（其他因子主導，量級不足）；或
(5) 總預訂量（room nights）同期非外生——即主體自述 AI 介面使總需求擴張或收縮，致守恆前提 \(Q\) 外生不成立。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：SEO／AI 通道之量或成本能否自行銷費用分離。2. 可交易工具：OTA 美股可交易，但通道成本是否已入指引。3. 半衰期：AI 介面 checkout 型態（直接 vs 第三方應用）之定案時點。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L10［P］格加「#2 已生成」；`AIM_FUNNEL.md` §3 一句；`query/QUEUE.md` 新列 Q-0029。不寫：ARCH_live／INDEX／ARCH_dead。不改 L10-P#1、L10-A、L10-I、L11-P／L11-A、C-A5。
