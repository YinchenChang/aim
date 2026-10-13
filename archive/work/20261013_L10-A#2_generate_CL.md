# L10-A#2 生成卡｜分發與中介：會計恆等（商戶模式預收浮存：FCF ≡ 營業盈餘現金＋Δ預收商戶訂單（DMB）−資本支出；DMB ≈ 商戶模式預訂額 × 預收至付供應商之平均天數／365）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；archive/FILEIDS.tsv；archive/drive/USED_20261001_L10-A_generate_GK.md；archive/drive/USED_20261001_L10-A_test1_GK.md；work/20261013_L10-P#2_test1_CL.md | EMITS: work/20261013_L10-A#2_generate_CL.md -->
**日期：** 2026-10-13　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 4→5／6）　**格：** L10-A　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L10-P#2 測一 2026-10-13，Q-0029 done）。非已殺／刻意排除之格中最後測試日最舊者：`archive/FILEIDS.tsv` old 時戳 L10-A 測一 2026-10-01T06:36Z，早於 L10-I（07:39Z）與 L11-A（08:11Z）→ **L10-A**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `deferred merchant bookings float`（0 筆）、`agentic checkout merchant of record`（10 筆，皆推論硬體／吞吐，無關）；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L10-A#1**（測一不通過，`archive/drive/USED_20261001_L10-A_test1_GK.md`）：中介收入＝轉介量 × 每次分潤率（TAC 側，損益表）；死因＝兩因子不可並列，只剩混成 rate。本卡為**資產負債表／現金流量表**恆等式，兩側（DMB 餘額、ΔDMB、OCF、capex）皆為同檔申報行，不含分潤率。
  - **L10-P#2**（測一不通過，`work/20261013_L10-P#2_test1_CL.md`）：通道守恆與行銷費用率；死因＝SEO／AI 歸因不居首。本卡不論通道、不論行銷費用。
  - **L10-P#1**（端側能量）、**L10-I**（預設槽位）、**L11-P**（死 #3）、**L11-A**（曝光 × 價）、**C-A5**（API 單價）：皆不涉。不恢復 L11-P。
- §7-10 領域最近公開：Expedia 2Q26 10-Q（2026-08-06）、Booking 2Q26 10-Q（2026-08-04）。下一檢查點＝兩者 3Q26 10-Q（2026-10 下旬至 11 月初；3Q 為 DMB 季節性釋出季）、FY26 10-K（2027-02）。

## 1. 落差一句

市場以自由現金流（FCF）估值並由其支應回購之 OTA，其 FCF 含一塊**營運資金浮存**：商戶模式下旅客訂房即付款、OTA 於入住後才付供應商，ΔDMB 直接進入營業現金流；種子主張此項為「商戶模式預訂額成長 × 預收天數」之函數而非盈餘，成長放緩、預收天數縮短或商戶模式份額回落時即反轉——錯價只在把 ΔDMB 讀成可持續之現金盈餘。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等**：\(FCF = OCF - capex\)；\(OCF = NI + \text{非現金} + \Delta DMB + \Delta AP_{merchant} - \Delta AR + \dots\)；\(DMB_t \approx GB^{merch}_t \cdot d/365\) ⇒ \(\Delta DMB \approx \Delta GB^{merch}\cdot d/365 + GB^{merch}\cdot \Delta d/365\) |
| 選擇者 | 商戶 vs 代理模式份額（Booking.com 代理→商戶轉移；Vrbo／B2B 結構）；預收天數 \(d\)（訂房提前期、付供應商週期）；AI 介面 checkout 之 merchant of record 歸屬 |
| 可見端 | 10-Q／10-K 資產負債表「Deferred merchant bookings」；現金流量表 ΔDMB 行；OCF、capex；商戶 vs 代理收入分列 |
| 指名不可見端 | 平均預收天數 \(d\)（未揭露，僅可由 DMB ÷ 商戶預訂額 `[D]` 推估）；Booking 現金流量表 ΔDMB 與「other current liabilities」合併一行 |
| 表達工具型態（只指名，不選券） | 美股可交易、採商戶模式且於 10-Q 分列 DMB 之 OTA 主體。不選券 |

種子只主張恆等式使 FCF 對商戶預訂額成長率與 \(d\) 有可計算之敏感度；**不主張 FCF 方向、不主張浮存必然反轉之時點，不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Expedia 10-K FY25 https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm ：「Deferred merchant bookings 1,858 794 572 Net cash provided by operating activities 3,880 3,085 2,690」；「Capital expenditures … ( 770 ) ( 756 )」；「net cash provided by operating activities increased by $795 million primarily due to increased benefits from working capital changes, including growth in deferred merchant bookings」。`[D]` FY25 ΔDMB ÷ (OCF − capex) ≈ 60%。
2. Expedia 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1324424/000132442426000053/expe-20260630.htm ：「Deferred merchant bookings 15,426 10,428」；6M「Deferred merchant bookings 4,998 4,898 Net cash provided by operating activities 5,409 4,073」；「Under the merchant model, we receive cash from travelers at the time of booking」。
3. Booking 10-K FY25 https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm ：「Deferred merchant bookings and other current liabilities 796 1,361 2,742 … Net cash provided by operating activities 9,409 8,323 7,344」；「Additions to property and equipment ( 322 ) ( 429 )」。`[D]` FY25 該合併行 ÷ (OCF − capex) ≈ 9%（合併行，非純 DMB）。
4. Booking 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1075531/000107553126000037/bkng-20260630.htm ：「Deferred merchant bookings 10,121 5,270」；6M「Deferred merchant bookings and other current liabilities 4,207 3,796」；「ongoing shift from agency to merchant revenues at Booking.com」。
5. PPC Land（2025-10-03）https://ppc.land/openai-launches-instant-checkout-for-chatgpt-with-stripe-partnership/ ：ChatGPT Instant Checkout「merchant control preservation as the merchant of record」——AI 介面 checkout 現行不移轉 MoR。

缺段（§7-2）：≥ 4 季單季 ΔDMB 序列（各 10-Q 年初至今差分 `[D]`）；商戶模式預訂額之同檔分列（Expedia 未分列商戶 GB）；Booking 純 DMB 變動；第三家主體（Airbnb「funds payable」口徑不同）之同口徑對照。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | 公司已在 MD&A 自行將 OCF 增加歸因於 DMB 成長 | Expedia FY25 10-K（§3-1） | 浮存成分已公開揭露，可能已定價 |
| R2 | AI 介面 checkout 保留商家為 MoR | OpenAI／PPC Land（§3-5） | AI 不改變誰收預付款，\(d\) 與商戶份額不受 AI 衝擊 |
| R3 | 只要商戶預訂額持續成長，ΔDMB 持續為正，浮存「永續」 | 恆等式本身（成長型浮存） | 反轉需成長放緩，觸發非結構性 |
| R4 | Booking 合併行占比僅約 9% | Booking FY25 10-K（§3-3） | 單一主體量級不足 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法就 ≥ 2 家上市主體取得 ≥ 4 季可歸屬之 ΔDMB（純 DMB，非合併行）與 OCF、capex 同檔申報行；或
(2) 可運作對照只能寫成轉介量 × 分潤率（滑回 L10-A#1）、通道份額或行銷費用率（L10-P#2）、預設槽位（L10-I）、或曝光 × 價（L11-A）；或
(3) 公司指引或具名賣方原文已把 FCF 拆為「扣除營運資金／DMB 之 FCF」並以之估值或指引（已定價）；或
(4) TTM ΔDMB 占 FCF 之比於 ≥ 2 家主體皆 < 10%（量級不足）；或
(5) 12 個月內無任何可觀測之 \(d\) 或商戶份額變動驅動（無支付時點政策、商戶／代理模式轉換或 MoR 移轉之一手揭露），致恆等式只隨成長率被動變動。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：ΔDMB 能否與 other current liabilities 分離（Booking 否、Expedia 是）。2. 可交易工具：OTA 美股可交易，但浮存是否已由公司或賣方剔除。3. 半衰期：DMB 季節性（1H 累積、2H 釋出）使單季讀數雜訊大，TTM 判讀需 ≥ 4 季。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L10［A］格加「#2 已生成」；`AIM_FUNNEL.md` §3 一句；`query/QUEUE.md` 新列 Q-0030。不寫：ARCH_live／INDEX／ARCH_dead。不改 L10-A#1、L10-P#2、L10-P#1、L10-I、L11-P／L11-A、C-A5。
