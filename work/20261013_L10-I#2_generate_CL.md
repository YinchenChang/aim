# L10-I#2 生成卡｜分發與中介：誘因（App Store 導出購買佣金由 27% 被法院壓為 0 → 開發者把付費者由應用商店內購導向替代支付；支付管道佣金差驅動路由份額）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；archive/FILEIDS.tsv；archive/drive/USED_20261001_L10-I_generate_GK.md；archive/drive/USED_20261001_L10-I_test1_GK.md；work/20261013_L10-A#2_test1_CL.md；work/20261013_L10-P#2_test1_CL.md | EMITS: work/20261013_L10-I#2_generate_CL.md -->
**日期：** 2026-10-13　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 5→6／6）　**格：** L10-I　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L10-A#2 測一 2026-10-13，Q-0030 done）。非已殺／刻意排除之格中最後測試日最舊者：`archive/FILEIDS.tsv` old 時戳 L10-I 測一 2026-10-01T07:39Z，早於 L11-A（08:11Z）、L11-I（10-02）、L13-P／L13-I（10-02）、L14／L15（10-05 起）→ **L10-I**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `app store commission`、`anti-steering`，0 筆；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L10-I#1**（測一不通過，`archive/drive/USED_20261001_L10-I_test1_GK.md`）：預設槽位由結構性轉為法定（DMA 選擇畫面）；死因＝轉換前結構性預設份額與轉換後選擇次數不可並列，公開層只有上線日與參與者季報承諾。本卡不論預設槽位、不論選擇畫面；載體為**開發者自身申報之成本行與歸因句**，第三人可逐季讀。
  - **L10-A#1**（轉介量 × 分潤率，只剩混成 rate）、**L10-A#2**（DMB 浮存，部分通過）：本卡不寫成量 × 率之會計恆等；主張為**佣金差 → 路由選擇**之誘因反應。
  - **L10-P#2**（需求通道守恆、行銷費用率）、**L10-P#1**（端側能量）、**L11-A**（曝光 × 價）、**L11-P**（死 #3）、**C-A5**（API 單價）：皆不涉。不恢復 L11-P。ARCH_dead／ARCH_live 無 app store／anti-steering 前例（grep 0 筆）。
- §7-10 領域最近公開：Match Group 2Q26 10-Q（2026-08）、Bumble 2Q26 10-Q（2026-08）；Courthouse News 2026-08-11（地院重定佣金程序）。下一檢查點＝兩者 3Q26 10-Q（2026-11 上旬）；最高法院 2026 年 10 月庭期之 Epic v. Apple 藐視案言詞辯論。

## 1. 落差一句

美國法院禁止 Apple 對 App Store 導出（link-out）購買收佣後，訂閱型開發者之「應用商店內購 ↔ 替代支付」路由由佣金差（App Store 內購費 vs 替代支付之卡費）決定；種子主張此路由份額為誘因反應、可由開發者成本行逐季讀出，且其持續性懸於**尚未裁定之佣金率**（地院重定、最高法院已受理）——錯價只在把節省之內購費讀成永續毛利，而非一個待裁定之制度參數。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因（I）**：開發者路由選擇 \(s\)（付費者走替代支付之份額）＝ f（App Store 佣金 \(c_{IAP}\) − 導出佣金 \(c_{link}\) − 卡費、轉換摩擦）；\(c_{link}\) 由法院設定（2025-04-30 地院＝0；2025-12-11 第九巡迴維持藐視、發回佣金率；地院重定中） |
| 選擇者 | 開發者（導出按鈕、網頁定價折扣）；付費者（是否離開 app 付款）；法院（\(c_{link}\)） |
| 可見端 | 開發者 10-Q／10-K「Cost of revenue」及其歸因句（內購費減少「due to Payers shifting from app store payments to alternate payment methods」）；占收入比 |
| 指名不可見端 | 路由份額 \(s\) 本身（開發者未揭露付費者經替代支付之比例）；Apple 端導出交易量（未分列） |
| 表達工具型態（只指名，不選券） | 美股可交易、以 iOS 訂閱為主且於 10-Q 分列內購費歸因之開發者主體；或平台方。不選券 |

種子只主張「佣金差 → 路由份額」為可觀測之誘因反應，且 \(c_{link}\) 為待裁定之制度參數；**不主張毛利方向、不主張裁定結果，不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Match Group 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/891103/000089110326000130/mtch-20260630.htm ：「Cost of revenue $ 204,262 $ (37,676) (16)% $ 241,938 Percentage of revenue 24% 28%」；「Cost of revenue decreased across all segments primarily due to Payers shifting from app store payments to alternate payment methods, resulting in $38.0 million lower in-app purchase fees and an increase of $4.6 million in credit card processing fees」；風險因子「our ability to realize reductions in in-app purchase fees」；「On February 22, 2026, Apple removed the Azar app from the Apple App Store following a February 6, 2026 update to Apple’s App Review Guidelines」。
2. Bumble 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1830043/000183004326000104/bmbl-20260630.htm ：「Cost of revenue consists primarily of in-app purchase fees due on payments processed through the Apple App Store and Google Play Store」；「As a percentage of revenue, cost of revenue decreased … primarily due to the reduction in fees as a result of alternate payment methods offered to iPhone operating system members in the United States」。
3. Digital Policy Alert（Epic Games v. Apple，No. 25-2935）https://digitalpolicyalert.org/event/39719-us-court-of-appeals-for-the-ninth-circuit-affirmed-contempt-finding-and-remanded-on-commission-rate-in-epic-games-v-apple ：2025-12-11 第九巡迴「affirmed the district court's civil contempt finding against Apple」，就導出購買佣金率發回；2026-05-06 最高法院駁回 Apple 暫緩 mandate 之聲請。
4. Courthouse News（Nairn，2026-08-11）https://www.courthousenews.com/apples-fight-over-commissions-for-linked-out-app-store-purchases-continues-in-district-court/ ：Gonzalez Rogers「The court is to determine an appropriate commission, that is a factual issue」；Apple 曾尋求導出銷售 27%；最高法院 6 月 30 日同意審查藐視認定，預期 10 月起之庭期審理。

缺段（§7-2）：≥ 4 季內購費歸因序列（Match 1Q26／4Q25／3Q25 10-Q、Bumble 同期）；路由份額 \(s\) 或替代支付付費者占比之任何數值揭露；第三家開發者（非約會類，如 Spotify 20-F／6-K、Duolingo 10-Q）之同型歸因；平台方 10-Q 對導出交易之揭露。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | 佣金率為待裁定事實問題，Apple 求 27% | Courthouse News（§3-4） | \(c_{link}\) 可能回升，誘因差收斂，節省非永續——但此即種子主張之不確定性來源 |
| R2 | 最高法院已受理藐視案 | 同上 | 可能整體推翻 0 佣金，機制半衰期短於 12 個月 |
| R3 | 開發者已在申報行自行量化節省（Match $38.0M） | Match 10-Q（§3-1） | 節省已公開，可能已定價 |
| R4 | Apple 2026-02-06 審核指引更新使 Azar 下架 | Match 10-Q（§3-1） | 平台以審核規則反制，路由份額受非價格手段壓制 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法就 ≥ 2 家上市開發者取得 ≥ 4 季之「Cost of revenue（或內購費）占收入比＋歸因於替代支付／導出之原文句」；或
(2) 可運作對照只能寫成轉介量 × 分潤率（滑回 L10-A#1）、預設槽位（L10-I#1）、通道份額或行銷費用率（L10-P#2）、曝光 × 價（L11-A）；或
(3) 公司指引或具名賣方原文已將內購費節省量化並以「佣金裁定情境」分列（已定價為情境，而非讀成永續）；或
(4) ≥ 2 家主體之 TTM 內購費節省 ÷ 收入皆 < 2%（量級不足）；或
(5) 12 個月內無可觀測之 \(c_{link}\) 裁定事件（地院佣金裁定、最高法院判決）或平台規則變更之一手文件，致誘因差不變、只隨採用率被動移動。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：內購費能否自 Cost of revenue 分離（Match 給金額、Bumble 只給定性）。2. 可交易工具：開發者與平台方皆美股可交易，惟節省已見於申報行。3. 半衰期：由地院佣金裁定與最高法院判決日界定，可能 < 12 個月。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L10［I］格加「#2 已生成」；`AIM_FUNNEL.md` §3 一句；`query/QUEUE.md` 新列 Q-0031。不寫：ARCH_live／INDEX／ARCH_dead。不改 L10-I#1、L10-A#1／#2、L10-P#1／#2、L11-P／L11-A、C-A5。
