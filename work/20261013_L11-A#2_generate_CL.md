# L11-A#2 生成卡｜人類注意力：會計恆等（內容資產按「預估觀看型態」攤銷：未攤銷餘額 ≡ Σ 成本 ×（1 − 預估累積觀看占比）；實際觀看衰減快於預估 ⇒ 估計變更、攤銷前移）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/FILEIDS.tsv；archive/drive/USED_20261001_L11-A_generate_GK.md；archive/drive/USED_20261001_L11-A_test1_GK.md；archive/work/20261013_L10-A#2_generate_CL.md | EMITS: work/20261013_L11-A#2_generate_CL.md -->
**日期：** 2026-10-13　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 0→1／6）　**格：** L11-A　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L10-I#2 測一 2026-10-13，Q-0031 done）。非已殺／刻意排除且無 #2 之格中最後測試日最舊者：`archive/FILEIDS.tsv` L11-A 測一 2026-10-01T08:11Z，早於 L11-I（10-02）、L13-P／L13-I（10-02）、L14-*（10-05 起）、L15-*（10-05 起）→ **L11-A**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `content amortization`、`streaming engagement hours`，0 筆；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L11-A#1**（測一不通過，`archive/drive/USED_20261001_L11-A_test1_GK.md`）：損益流量恆等 廣告收入＝曝光數 × 每次曝光價；死因＝否決 (1)：只有年比、曝光數水準與每次曝光價水準不可並列。本卡為**資產負債表存量／會計估計**恆等式，兩側（內容資產各類餘額、按類攤銷、未來三年預期攤銷、公司自報總觀看時數）皆有**水準**，不含曝光或單價。
  - **L11-P**（ARCH_dead #3，結構性不可表達）：每人每日清醒秒數。本卡不論清醒時間總量。不恢復 L11-P。
  - **L11-I**（測一不通過）：代理議價／權利型態。本卡不涉條款。
  - **L7-P#2**（內容授權收入／RPO）：資料授權賣方側。本卡為內容買方之攤銷估計，不涉授權給 AI 實驗室。
  - **L10-A#1／#2、L10-P#2、L10-I#2**：轉介分潤、預收浮存、通道行銷費用、應用商店佣金。皆不涉。**C-A5**：不以 API 單價重開。
- §7-10 領域最近公開：Netflix 10-Q 季期 2026-06-30（申報 2026-07-17）；Netflix「What We Watched」H1 2026（2026-07 中）；Nielsen The Gauge 2026-05（MediaPost 2026-07-28）。下一檢查點＝Netflix 3Q26 10-Q（2026-10 下旬）、FY26 10-K（2027-01）；觀看報告 2027 起改為年報（每年 Q1）。

## 1. 落差一句

市場以 Netflix 營業利益率擴張讀其注意力份額，攤銷被當作已由過往現金支出鎖定之可預測費用（公司指引 2026 攤銷 ~+10%、現金／攤銷 ~1.1x）；種子主張攤銷**時序**是由「預估觀看型態」決定之會計估計，若注意力移往 YouTube／創作者／生成式影音使片庫觀看衰減快於預估，恆等式要求估計變更、攤銷前移，此敏感度在指引中不可見——錯價只在把攤銷讀成與觀看型態無關之機械排程。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等（估計）**：\(CA^{rel}_t = \sum_i C_i\,(1 - F_i(t))\)，\(F_i\)＝依「歷史及預估觀看型態」之累積攤銷占比（加速法；>90% 於首播後 4 年內）；\(Amort_t = \sum_i C_i\,\Delta F_i(t)\)。實際觀看 \(h_i\) 偏離預估 ⇒ \(F_i\) 改寫（ASC 250 推延適用）⇒ 當期攤銷上升 |
| 選擇者 | 管理層對各片之預估觀看曲線；稽核（EY 關鍵查核事項）以「歷史與預測觀看時數」比對 |
| 可見端 | 10-K／10-Q：授權／自製（已上線、製作中、開發中）內容資產餘額；按類攤銷；未來三年預期攤銷（10-K）；現金流量表內容增加與攤銷；公司自報總觀看時數（水準，半年→年） |
| 指名不可見端 | 各片預估 vs 實際觀看曲線；估計變更之金額（僅於變更時揭露）；新片 vs 片庫觀看占比 |
| 表達工具型態（只指名，不選券） | 美股可交易、以觀看型態攤銷內容資產且自報觀看水準之串流主體。不選券 |

`[D]` 可重算對照（申報與自報水準，非測一結論）：每觀看小時攤銷＝H1 2026 攤銷 8,529,209 千 ÷ ~97B 小時 ≈ \$0.088；H1 2025 7,655,186 千 ÷（97B／1.02）≈ \$0.080，**約 +9%**——攤銷 +11.4% 而觀看 +2%。**不主張攤銷方向、不主張估計變更必然發生或其時點，不寫 H1。** 本機制只移動時序，總成本不變（見 R2）。

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Netflix 10-K FY25 https://www.sec.gov/Archives/edgar/data/1065280/000106528026000034/nflx-20251231.htm ：「we estimate the content amortization pattern … based upon various factors including historical and estimated viewing patterns. If actual viewing patterns differ from these estimates, the pattern and/or period of amortization would be changed … could result in greater in-period expenses」；「On average, over 90% of a licensed or produced content asset is expected to be amortized within four years」；「approximately $ 6,381 million, $ 2,280 million, and $ 1,469 million of the $ 12,139 million unamortized cost of the licensed content is expected to be amortized in each of the next three years」；produced released「$ 4,309 million, $ 2,784 million, and $ 1,840 million of the $ 10,687 million」；攤銷 FY25／24／23「16,422,166 15,301,517 14,197,437」、內容增加「( 17,096,617 ) ( 16,223,617 ) ( 12,554,703 )」；CAM：「historical and forecasted viewing hour consumption」；風險因子：「new technological developments, including the development and use of generative AI」。
2. Netflix 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1065280/000106528026000212/nflx-20260630.htm ：「Content assets, net $ 33,837,573 $ 32,778,392」；「Licensed content, net $ 12,229,733 … Released, less amortization 10,487,502 … In production 10,313,433」；6M 攤銷「8,529,209 7,655,186」、6M 內容增加「( 9,774,440 ) ( 7,385,470 )」。
3. Netflix 2Q26 股東信（8-K Ex.99.1）https://www.sec.gov/Archives/edgar/data/0001065280/000106528026000211/ex991_q226.htm ：「our members watched more than 97 billion hours, up 2% year over year」；「View hours grew +2% in H1’26 vs. +1.5% growth in 2025」；「content amortization to grow slower in the second half of the year and to increase ~10% for 2026」；「annual cash content spend to amortization ratio of ~1.1x」；「GenAI workflows have been used in roughly 300 of our titles」；「we will shift to publishing this report annually in the first quarter, beginning in 2027」。
4. MediaPost（2026-07-28，Nielsen The Gauge 2026-05）https://www.mediapost.com/publications/article/416872/ ：「YouTube grew another 13% year-over-year to a 13.8% share」；Netflix「adding 9% year-over-year to total an 8.0% share」。
5. Audit Analytics（2015-10-19）https://blog.auditanalytics.com/netflix-change-in-amortization-estimate ：Q3 2015 10-Q「changed the amortization method of certain content given changes in estimated viewing patterns」；「a $12.8 million decrease in operating income」。
6. TheWrap（2026-07-17）https://thewrap.com/media-platforms/tv/netflix-viewership-report-2026-takeaways ：Third Bridge John Conca「we do not see the lift to reported view hours per member」。

未取：Netflix about 頁 H1 2026 觀看報告原頁（WebFetch 權限逾時，非存在性主張；數值經 8-K 股東信取）。缺段（§7-2）：≥ 4 期同口徑攤銷／觀看時數序列（觀看報告半年制 2023H1 起，可取）；新片 vs 片庫觀看占比；第二家主體（Disney／WBD 採個別／群組貨幣化法，口徑不同）；10-K 揭露之 WBD 合併協議若成交，購買法重估將打斷序列可比性（本卡不查成交狀態）。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | Netflix 觀看時數仍成長、Gauge 份額年增 9%；注意力未自 Netflix 流出 | 股東信 2Q26（§3-3）；Nielsen（§3-4） | 驅動不存在則恆等式靜止 |
| R2 | 估計變更只移動時序，總成本與現金不變；FCF 不受影響 | 恆等式本身；現金／攤銷 ~1.1x 指引 | 可捕捉之價差可能僅為短期 EPS 噪音 |
| R3 | 唯一可查之前例影響極小（營業利益 −\$12.8M） | Audit Analytics（§3-5） | 量級不足 |
| R4 | 加速法已把 >50% 片庫成本置於首年；尾部餘額小 | 10-K 三年預期攤銷（§3-1） | 片庫衰減加快之增量攤銷受限 |
| R5 | 觀看報告 2027 起改年報 | 股東信（§3-3） | 可觀測頻率下降 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法就 ≥ 4 期取得同口徑之內容資產分類餘額、按類攤銷與公司自報總觀看時數**水準**（以致每觀看小時攤銷 `[D]` 不可重算）；或
(2) 可運作對照只能寫成曝光數 × 單價（L11-A#1）、清醒秒數（L11-P）、權利型態（L11-I）、授權收入（L7-P#2）或轉介／浮存／佣金（L10 系列）；或
(3) 公司或具名賣方原文已將攤銷估計對觀看型態之敏感度量化或以每觀看小時成本建模（已定價）；或 10-K／10-Q 自 2015 以來之估計變更揭露皆不重大且稽核敏感度分析無異常；或
(4) `[D]` 以 10-K 三年預期攤銷表推算：次年預期攤銷占比上移 5 個百分點之增量攤銷 < 最近年度營業利益 3%（量級不足）；或
(5) 12 個月內無可觀測驅動：公司總觀看時數與 Nielsen Gauge 份額皆持續年增，且無每會員觀看下降之一手揭露。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：估計變更金額只在發生時揭露；平時只能以每觀看小時攤銷 `[D]` 旁證。2. 可交易工具：美股可交易，但 WBD 合併之購買法會計可能主導未來攤銷序列。3. 半衰期：加速法下片庫尾部 ≤ 4 年，錯價窗須 ≥ 12 個月方合准入。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L11［A］格加「#2 已生成」；`AIM_FUNNEL.md` §3 一句；`query/QUEUE.md` 新列 Q-0034。不寫：ARCH_live／INDEX／ARCH_dead。不改 L11-A#1、L11-I、L11-P、L7-P#2、L10 系列、C-A5。
