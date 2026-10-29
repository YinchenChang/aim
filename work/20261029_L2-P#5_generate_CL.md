# L2-P#5 生成卡｜資料中心實體：守恆（施工存量－交付流量之連續方程——未來 τ 內可交付之 MW ≤ 今日在建且已過最短工期者；公司「ready for service」指引之 MW 若超出自身申報在建存量所能流出者，滑期為恆等式之必然）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/work/20261007_L2-P#2_generate_CL.md；archive/work/20261014_L2-P#3_generate_CL.md；archive/work/20261021_L2-P#4_generate_CL.md；work/20261021_L2-P#4_test1_CL.md；archive/work/20261015_L2-I#3_generate_CL.md；archive/work/20261023_L2-I#4_generate_CL.md | EMITS: work/20261029_L2-P#5_generate_CL.md -->
**日期：** 2026-10-29　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 4→5／6）　**格：** L2-P　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L15-I#4 測一本日，Q-0126 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-21 之 L2-P（#4）與 L2-A（#4）；依表序取第一 → **L2-P**。既有生成 #1–#4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `under construction MW`，3 筆（SRC_HW_011／012 機架功率、SRC_DC_014 每 IT MW 資本支出），無一涉施工存量或交付時序；未用。
- 比對（本卡須異型）：
  - **L2-P#1**（PUE 受濕球封頂）：熱力學水準上界。不涉。
  - **L2-P#2**（`archive/work/20261007_L2-P#2_generate_CL.md`）：每櫃 kW 受散熱介質封頂（空間密度）。不涉。
  - **L2-P#3**（`archive/work/20261014_L2-P#3_generate_CL.md`）：訓練負載功率之時域擺盪（電氣動態）。不涉。
  - **L2-P#4**（`archive/work/20261021_L2-P#4_generate_CL.md`；測一 `work/20261021_L2-P#4_test1_CL.md` 否決 (3)）：MW **口徑**（接入 vs critical IT）。本卡一律以同一主體同口徑之 MW 自比（在建 vs 指引），不跨主體加總、不涉口徑換算；死因 R1（賣方已換算）不適用於本卡樞紐，但同型反方（市場端已有逐站追蹤）列為 R1 由測一檢驗。
  - **L2-I#3**（可取消設備訂單）：誘因、backlog 計入。本卡不論訂單選擇權。**L2-I#4**（併網排隊之速度溢價）：誘因。本卡不論電網排隊價格，只論工期下界之存量流量。**L2-A#2**（利息資本化）：會計。不涉。
  - **ARCH_dead #19 C-P4**（水）、**L1-P**（刻意排除 T-11）：不涉發電、燃料或水。
- §7-10 領域最近公開：CBRE North America Data Center Trends 2026 上半年（新聞稿 2026-08-27）；APLD 10-Q 1Q FY27（2026-08-31 期，2026-10-07 申報）。下一檢查點＝CBRE 2026 下半年版（約 2027-02）；各主體 2026-09-30／11-30 季 10-Q。

## 1. 落差一句

存量－流量守恆：\(D(t,t+\tau) \le UC_{\ge}(t) \equiv \sum_{i\in UC(t)} MW_i \cdot \mathbb{1}[a_i(t) \ge T_{min} - \tau]\)——未來 τ 期間可交付（ready for service）之 MW，不能超過今日已在建、且已施工時長 \(a_i\) 加上 τ 不短於最短工期 \(T_{min}\)（長交期電氣設備約 2.5 年為下界之一）之存量。上市開發商／新雲主體於 10-Q 逐案揭露「在建 MW」與「initial／full ready for service」日期；若其 12 個月內指引交付之 MW 大於自身申報在建存量中可流出者，則滑期非風險而是恆等式之必然，且滑期會依序延後租約起租、收入與利息資本化終止點。可拒絕之主張＝樣本中 ≥ 2 家上市主體之「12 個月內 RFS 指引 MW」> 其同檔可流出在建 MW（以開工日推算），且具名賣方原文以公司指引日期建模起租。若指引皆落在存量可流出範圍內、或賣方／追蹤機構已逐站以施工進度改寫時程，本卡死。本卡不主張任何主體價值方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆（P）**：(i) \(UC(t+1) = UC(t) + S_t - D_t\)（開工 S、交付 D）；(ii) \(D(t,t+\tau) \le UC_{\ge}(t)\)；(iii) 指引超額 \(E \equiv G(t,t+\tau) - UC_{\ge}(t)\)，\(E>0\) ⇒ 必然滑期量 ≥ E |
| 選擇者 | 發行人（指引日期與分期定義：「initial」vs「full」RFS）；賣方（是否以指引建模起租） |
| 可見端 | 10-Q／10-K MD&A 逐案「currently under construction」「anticipate reaching initial ready for service in …」；破土公告日（\(a_i\) 之起點）；歷次申報之同案日期序列（滑期史） |
| 指名不可見端 | 逐案施工進度（衛星／許可文件，私有追蹤者有）；長交期設備到貨；各案 \(T_{min}\) |
| 量綱 | MW（同主體同口徑）；月（a、τ、\(T_{min}\)）；E 為 MW |
| 外部參照物（測一查證） | Sightline（2026-02-24）：2026 預定上線約 16GW，在建約 5GW、約 11GW 無可見施工；2025 年 26% 預期容量滑期（[currence.ai](https://www.currence.ai/blog/data-center-outlook)）。Wood Mackenzie（2025-10-15）：大型電力變壓器平均交期 128 週、GSU 143 週、開關設備 44 週（[woodmac](https://www.woodmac.com/news/opinion/mind-the-gap-tackling-supply-chain-challenges-in-the-electric-td-sector/)） |
| 表達工具型態（只指名，不選券） | 美股、以逐案 RFS 日期驅動近期收入之資料中心開發／轉型主體普通股；不選券 |
| 重疊 | L2-I#4（電網到位為條件）；L2-P#4（MW 為單位） |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. APLD 10-Q 1Q FY27（sec.py）https://www.sec.gov/Archives/edgar/data/1144879/000114487926000059/apld-20260831.htm ：「Our two buildings at our Polaris Forge 2 campus, with an aggregate 300MW of capacity, are currently under construction. We anticipate reaching initial ready for service in the second half of calendar year 2026 and full capacity in early calendar year 2027」；同段 Polaris Forge 1 第三棟 150MW、Polaris Forge 3 300MW、Delta Forge 1 300MW、Delta Forge 2 210 MW 皆「under construction」。
2. APLD 10-K FY26（sec.py）https://www.sec.gov/Archives/edgar/data/1144879/000114487926000048/apld-20260531.htm ：「On August 18, 2025, we also announced that we would be breaking ground on our Polaris Forge 2 campus with an initial 200 MW … anticipate reaching initial capacity in the calendar year 2026」——開工日（\(a_i\) 起點）與前期指引措辭可比。
3. CBRE（2026-08-27）https://www.cbre.com/press-releases/north-american-data-center-demand-continues-to-outpace-supply-despite-record-construction-activity ：「The 7,481 megawatts (MW) under construction in H1 2026」；「power constraints are extending completion timelines」。產業總量，口徑未述。
4. SynMax Vulcan（2026-06-12）https://blog.synmax.com/vulcan/datacenter-delays-are-a-3-billion-earnings-problem-and-most-of-it-hasnt-hit-yet-1 ：以衛星進度對照「the online date committed in earnings guidance」；約 4.5 GW 遞延至 2027 年底；逐公司矩陣在付費平台。
5. SemiAnalysis（2026-06-18）https://newsletter.semianalysis.com/p/stop-saying-half-of-2026-us-datacenter ：反駁 Sightline 分母（「hugely flawed denominator, off by multiples」）；逐站時程（Nebius NJ 約 25 MW 已通電 vs 年底 100 MW 承諾；Core Scientific Denton 250 MW 年底 2025 指引判為未達；CoreWeave 年底 2026 1.7 GW active power 與指引相符）。

缺段（§7-2）：未取 IREN、CIFR、WULF、GLXY、CRWV、NBIS 之逐案在建 MW 與 RFS 日期；未取具名賣方以指引日期建模起租之原文；APLD 逐案開工日僅 Polaris Forge 2 有原文。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 市場端已有逐站施工追蹤（衛星＋許可），並以指引日期 vs 實際進度量化遞延 | SynMax 2026-06-12；SemiAnalysis 2026-06-18（§3-4、§3-5） | 已定價 |
| R2 | 產業層「半數滑期」說法分母錯誤；多數遞延集中於未開工之公告案，在建案之時程穩定（hyperscaler 自建 YE2026 預測 6 個月僅動 ~1%、colo < 5%） | SemiAnalysis（§3-5） | 在建存量內 E ≈ 0 |
| R3 | 「initial RFS」可由一棟中的部分資料廳交付，\(T_{min}\) 對分期交付不具約束；指引本已以分期措辭吸收 | APLD 措辭（§3-1） | 恆等式不咬合 |
| R4 | 預租 > 80%，承租方容忍滑期、租約多以交付日起租，滑期只移動時點不改總額；對長期估值量級小 | CBRE（§3-3） | 量級不足／半衰期短 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀樣本（APLD 加 ≥ 3 家：IREN、CIFR、WULF、GLXY、CRWV、NBIS 擇取）中，同檔可得「在建 MW＋開工日＋12 個月內 RFS 指引 MW」三項者 < 2 家（不可觀測）；或
(2) `[D]` 各家 \(E = G - UC_{\ge}\) 皆 ≤ 0（以 \(T_{min}\) 取 18 個月為寬鬆下界、指引取「initial」口徑），或 E 合計 < 該主體在建 MW 之 10%（門檻凍結於此）；或
(3) 具名賣方、評等機構或追蹤者原文已以施工進度改寫上述主體之逐案時程（R1；含 SynMax／SemiAnalysis 公開段落點名該主體）；或未能取得任何以公司指引日期建模起租之具名賣方原文（落差無市場端）；或
(4) 可運作對照只能寫成 MW 口徑（L2-P#4）、PUE 水準（L2-P#1）、密度（L2-P#2）、功率擺盪（L2-P#3）、電網排隊溢價（L2-I#4）或可取消訂單（L2-I#3）；或
(5) 12 個月內無檢驗事件（逐季 10-Q 之同案 RFS 日期更新、起租公告、CBRE 2026 下半年版）；或
(6) 起租／收入認列不以 RFS 為條件（租約以簽約或固定日起租），使滑期不進任何財報科目（R4、§7-4）。

複查觸發器（若日後殺）：任一樣本主體於 10-Q 首次將同案 RFS 日期延後 ≥ 2 季；具名賣方發布以施工進度下修起租時程之原文；SEC 意見函就 RFS 指引依據提問。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：租金收入起認日、在建工程轉固定資產、利息資本化終止點、合約收入 backlog 之時程表。2. 可交易工具：以逐案 RFS 驅動近期收入之主體普通股（不選）。3. 半衰期：一季（每份 10-Q 更新日期即解析一部分）。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0127；`query/ARCH_matrix.md` L2［P］加「#5 已生成」；`AIM_FUNNEL.md` §3 一句與日期行；`export/LEADS_算力收支.md` 追加 5 列（CBRE 在建 MW、預租比、Sightline 2026 預定上線、APLD Delta Forge 2 合約收入、SynMax 遞延 GW）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L2-P#1–#4、L2-A／#2–#4、L2-I／#2–#4、C-P4；不碰 L1-P（刻意排除）；不寫 T。
