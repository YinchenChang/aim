# L15-A#4 生成卡｜基礎設施軟體與資料：會計恆等（取得合約成本資本化之營業利益時差恆等：銷售佣金之「資本化—攤銷」使損益表佣金費用 ≠ 當期現金佣金，差額恆等於遞延佣金餘額變動 −ΔD；AI 驅動之大額多年容量合約使資本化跳增時，當期營業利益率被墊高、其後攤銷爬升回吐）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261007_L15-A_generate_GK.md；archive/work/20261014_L15-A#2_generate_CL.md；archive/work/20261021_L15-A#3_generate_CL.md；archive/work/20261029_L15-P#4_generate_CL.md；archive/work/20261013_L14-P#2_generate_CL.md；archive/work/20261021_L14-A#3_generate_CL.md；archive/work/20261026_L13-A#4_generate_CL.md；archive/work/20261020_L13-A#3_generate_CL.md | EMITS: work/20261029_L15-A#4_generate_CL.md -->
**日期：** 2026-10-29　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 2→3／6）　**格：** L15-A　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L15-P#4 已測，Q-0124 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-21（L2-P#4、L2-A#4、L15-A#3 同日）；L15-A 為本輪序（第 4 輪 L15-P#4 之後）且 L15-A#4 未生成，取 **L15-A**。既有 #1–#3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `commission`、`sales compensation`、`deferred contract`，0 筆；未用。內部數字（§12）未用。
- 比對（須異型）：
  - **L15-A#1**（`archive/drive/USED_20261007_L15-A_generate_GK.md`）：消費營收＝使用量×有效單價。本卡不分解營收，標的是**費用端時差**。
  - **L15-A#2**（`archive/work/20261014_L15-A#2_generate_CL.md`）：OCF 中 Δ合約負債（預收浮存）。本卡標的為資產端 **Δ遞延佣金**，且作用於營業利益（損益表），非 OCF；FCF 已含現金佣金，故本卡落差不在 FCF。
  - **L15-A#3**：託管成本轉嫁之產品毛利。本卡不涉 COGS／毛利。
  - **L14-P#2**（容量承諾池互抵、rollover）：本卡不主張承諾池內替代或未用容量；容量合約只作資本化之觸發事件。
  - **L14-A#3**（AI 重組排除項之 GAAP／調整後橋接）：本卡之 ΔD 不在任何排除項內，GAAP 與非 GAAP 同受影響。
  - **L13-A#3**（EPS 分母股數）、**L13-A#4**（可轉債全成本）：不涉股數與融資。
  - 已殺 C-A1–C-A5、L8-P／L9-P／L11-P：不涉。
- §7-10 領域最近公開：SNOW 10-Q 2Q FY27（期 2026-07-31）；MDB 10-Q 2Q FY27（期 2026-07-31，2026-09-01 申報）。下一檢查點＝SNOW／MDB 3Q FY27 10-Q（約 2026-12）。

## 1. 落差一句

種子主張：ASC 340-40 下，賣方之銷售佣金分兩路——依消耗計之佣金當期費用化（E），依合約簽訂／擴張計之佣金資本化（C）後於約 5 年攤銷（A）；故 **S&M 佣金費用 ≡ E＋A，現金佣金 ≡ E＋C，兩者差 ≡ C − A ≡ ΔD**（D＝遞延佣金餘額）。AI 帶動之大額多年容量合約使 C 跳增時，當期營業利益率（GAAP 與非 GAAP 皆然）被墊高 ΔD/R，其後 A 以時滯爬升回吐。市場若把同期營業利益率擴張讀為營運槓桿或 AI 效率，則把會計時差當經常性改善。SNOW 已見樣態：FY26 Δ遞延佣金（現金流量表）−$305.1M、攤銷 $140.4M（FY25 $93.1M），營收約 $4.7B；1H FY27 攤銷 $117.5M vs 上年同期 $59.0M。反例 MDB：2024 年改佣金制淡化預付多年承諾後，1H FY27「amortization exceeding current-period capitalization」，D 下降，方向相反。可拒絕之主張＝ΔD/R 與攤銷增量占營業利益率變動之比可由申報重算且非可忽略，而賣方與公司指引未作此分解。不主張任何主體價值方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等（A）**：\(D_t \equiv D_{t-1} + C_t - A_t\)；\(\text{S\&M}^{佣金}_t \equiv E_t + A_t\)；\(\text{現金佣金}_t \equiv E_t + C_t\)；營業利益率之時差成分 \(\equiv \Delta D_t / R_t\)；\(A_t \approx \sum_{k} C_{t-k}/L\)（L＝攤銷期，SNOW、MDB 皆約 5 年，SNOW 續約部分按合約期） |
| 量綱 | 美元／期；\(\Delta D/R\)、\(A/R\) 無因次（pp） |
| 選擇者 | 賣方（佣金制度：消耗計 vs 簽約計；攤銷期估計）；客戶（多年容量 vs 隨需）；會計判斷（「commensurate with renewal」之分界） |
| 可見端 | 10-K／10-Q 資產負債表遞延佣金（流動／非流動）、現金流量表「Amortization of deferred commissions」與「Deferred commissions」變動、收入附註「Costs Capitalized to Obtain Contracts」、MD&A S&M 增量歸因句、政策附註攤銷期 |
| 指名不可見端 | E 與 C 之分列（多數只揭露 A 與 ΔD，C 須推算）；AI 相關合約所占 C 之份額 |
| 表達工具型態（只指名，不選券） | 美股消費制基礎設施軟體商；不選券 |
| 重疊 | L15-A#2（營運資金時差，但在負債端／OCF）；L14-P#2（容量合約） |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Snowflake 10-K FY26（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm ：「A portion of the sales commissions paid to the sales force is earned based on the level of the customers’ consumption of our platform, and a portion … is earned upon the origination, expansion, or renewal of customer contracts. Sales commissions tied to customers’ consumption are expensed in the same period as they are earned. Sales commissions and referral fees earned upon the origination or expansion of customer contracts that are not commensurate with those earned upon the renewal of contracts are capitalized and then amortized over a period of benefit that we determined to be five years」；現金流量表「Amortization of deferred commissions 140,415 93,128 74,787」、「Deferred commissions ( 305,063 ) ( 101,569 ) ( 134,787 )」（千美元，FY26／25／24）；資產負債表遞延佣金流動 214,058／97,662、非流動 241,759／183,967；MD&A「a $305.1 million increase in deferred commissions earned primarily by our sales force upon the origination, expansion, or renewal of customer contracts」；「total revenue for the year ended January 31, 2026 was $4.7 billion」。
2. Snowflake 10-Q 2Q FY27（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1640147/000164014726000037/snow-20260731.htm ：六個月「Amortization of deferred commissions 117,473 58,954」、「Deferred commissions ( 106,320 ) ( 84,864 )」；非流動遞延佣金 222,581（2026-07-31）vs 241,759。
3. MongoDB 10-K FY26（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1441816/000162828026016799/mdb-20260131.htm ：「Deferred commissions were $ 373.2 million and $ 363.4 million as of January 31, 2026 and 2025」；「Amortization expense … was $ 136.8 million, $ 112.6 million and $ 99.5 million」；攤銷期「generally five years」；現金流量表 Deferred commissions「( 9,791 ) ( 69,127 ) ( 41,830 )」。
4. MongoDB 10-Q 2Q FY27（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1441816/000162828026059830/mdb-20260731.htm ：「a decrease of $10.1 million in deferred commissions primarily due to amortization exceeding current-period capitalization」；遞延佣金 $363.0M（2026-07-31）；六個月攤銷 $71.0M vs $68.0M。
5. MDB 佣金制變更之二手：Motley Fool（2024-04-04）https://www.fool.com/investing/2024/04/04/why-mongodb-stock-tumbled-199-in-march ：「the company has changed its sales incentives to de-emphasize upfront commitments」（二手；一手電話會議原文未取）。

缺段（§7-2）：C 與 E 之分列未取（多數申報不揭露 E）；SNOW 管理層對 FY26 資本化跳增之來源（AI／大型多年合約）未取一手歸因；具名賣方是否以 ΔD/R 調整營業利益率未取；DDOG、Confluent、Elastic 等第二家同向樣本未取。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | FCF 已含現金佣金，市場以 FCF 定價，ΔD 只影響營業利益，無錯價 | SNOW 10-K 現金流量表 | 已定價（→(3)） |
| R2 | 攤銷期 5 年使 A 平滑，ΔD/R 量級小於營業利益率變動之雜訊 | MDB 10-K（ΔD/R 小） | 量級不足（→(2)） |
| R3 | 資本化跳增只是合約結構（多年）之一次性，已於 RPO 與指引反映 | SNOW 10-K RPO | 已入指引（→(3)） |
| R4 | 本質為預收／營運資金時差（L15-A#2 型） | — | 歸他型（→(4)） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 任一主體之 \(C_t\)（＝ΔD＋A）與 \(A_t\) 無法由 ≥ 3 期申報重算，或 ≥ 2 家消費制主體之 ΔD/R 皆不顯著偏離 0；或
(2) `[D]` 時差成分 |ΔD/R| 及攤銷增量 ΔA/R 於 ≥ 1 主體之任一財年 < 1.5 pp 營收，或 < 該主體同期營業利益率變動之 25%（門檻凍結於此）；或
(3) 公司指引原文或具名賣方已就遞延佣金資本化／攤銷對營業利益率之影響作量化或明示調整（含 SNOW FY27 指引、電話會議）；或
(4) 可運作對照只能寫成 L15-A#2（合約負債／OCF 浮存）、L14-P#2（容量承諾池）或 L14-A#3（排除項橋接）；或
(5) 12 個月內無檢驗事件（SNOW／MDB 3Q FY27 10-Q 約 2026-12、FY27 10-K 約 2027-03）；或
(6) 資本化跳增之來源原文顯示與 AI／多年容量合約無關且屬佣金制度單次調整（如計提方式更正），使恆等不具持續性。

複查觸發器（若日後殺）：任一消費制基礎設施軟體商首次分列 E／C 或改變攤銷期；佣金制度由簽約計轉為消耗計（或反向）之一手公告；遞延佣金單年變動 ≥ 營收 5%。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：遞延佣金（流動／非流動）、攤銷、S&M、非 GAAP 營業利益率。2. 可交易工具：基礎設施軟體商普通股（不選）。3. 半衰期：攤銷期約 5 年；資本化跳增後 A 爬升約 1–5 年。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0125；`query/ARCH_matrix.md` L15［A］加「#4 已生成」；`AIM_FUNNEL.md` §3 一句與日期行。LEADS：本輪事實（佣金會計）非 AI 算力收支，未寫。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L15-A#1–#3、L15-P#1–#4、L15-I#1–#3、L14-P#2、L14-A#3、L13-A#3–#4；不碰 L1-P；不寫 T。
