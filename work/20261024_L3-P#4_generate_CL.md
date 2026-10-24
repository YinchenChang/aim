# L3-P#4 生成卡｜半導體製造測試：守恆（中介層面積守恆：每片 12 吋晶圓可切之 CoWoS 中介層數隨中介層尺寸非線性下降——「萬片／月」產能不等於封裝顆數產能）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260926_L3-P_generate_GK.md；archive/work/20261009_L3-P#2_generate_CL.md；archive/work/20261016_L3-P#3_generate_CL.md；archive/work/20261016_L3-A#3_generate_CL.md；archive/drive/USED_20260924_L3-A_generate_GK.md；archive/work/20261017_L4-I#3_generate_CL.md | EMITS: work/20261024_L3-P#4_generate_CL.md -->
**日期：** 2026-10-24　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3→4／6）　**格：** L3-P　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L1-I#4 已於本日測一）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-16（L3-P#3、L3-A#3、L12-A#3、L12-I#3）→ 依表序取 **L3-P**；既有生成 3 份 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `CoWoS`／`interposer`／`advanced packaging`，命中 0 筆。內部數字（§12）：未取用。
- 比對（本卡須異型）：
  - **L3-P#1**（GK）：曝光機**機時守恆**（WPH × 機台 ÷ 每層曝光次數）；死於可觀測性。本卡為**幾何面積守恆**（圓形晶圓上可排之矩形中介層數），非機時；選擇者為封裝產能方與 GPU／ASIC 設計方，非曝光機賣方。
  - **L3-P#2**：HBM 堆疊**良率乘積**（記憶體廠晶圓投入比）；方向已被揭露／定價。本卡不談良率乘積，談**良率 100% 時亦成立**之每片切數上界；良率只作乘數輸入。
  - **L3-P#3**：探針卡**觸壓壽命守恆**（耗材流量）。物件、選擇者與載體皆異。
  - **L3-A#1**（有效晶粒單價恆等，含 CoWoS 良率一句）、**L3-A#3**（封測代收材料轉嫁、毛利率分母）：會計恆等型；本卡不談收入認列或單價口徑，談**實體產能單位換算**。
  - **L4-I#3** R2 提及「CoWoS／HBM 受限」為反方約束，非本機制；不改其結論。
  - ARCH_dead：C-I3′／N-02（利益未分列）——本卡測一 (1) 即為同類可分離性題（封裝顆數未揭露）；主體與機制不同，非已殺同型。N-01（機隊世代組成非科目）不同物件。
- §7-10 領域最近公開：TSMC 3Q26 新聞稿（2026-10-15，6-K acc `0001046179-26-000726`）；TSMC 北美技術論壇相關報導（2026-05-14：現行 5.5 倍光罩、2028 年 14 倍光罩／20 HBM、2029 年 > 14 倍／24 HBM）；CoPoS 試產線 2026-02 主要設備安裝完成、量產 2028–2029（TrendForce 2026-04-16）；優分析 2026-09-15（CoWoS 月產能 2026 年底約 12 萬片、2027 年約 18 萬片）。下一檢查點＝TSMC 3Q26 法說逐字稿（2026-10-15）之 CoWoS 句、Amkor 3Q26 10-Q（約 2026-10 下旬）、NVIDIA FQ3'27 財報（約 2026-11 下旬）、TSMC 4Q26 法說（約 2027-01 中）。

## 1. 落差一句

先進封裝產能以「**CoWoS 萬片晶圓／月**」流通（2026 年底約 11.5–14 萬片、2027 年約 17–18 萬片，皆法人估），市場常以片數成長外推加速器顆數成長。但每片 300 mm 晶圓（≈ 70,686 mm²）上可排之矩形中介層數 `N ≈ πd²/(4A) − πd/√(2A)`（`A`＝中介層面積；光罩 ≈ 26 × 33 ＝ 858 mm²），隨 `A` 由 3.3 倍→5.5 倍→9.5 倍→14 倍光罩**超線性**下降（邊緣損失項隨 `√A` 惡化）；公開層僅有「12 吋晶圓可置 29 顆 H100 vs 16 顆 B200」之二手一句。種子主張：**封裝顆數產能 ＝ 片數 × N(A) × 良率**；若中介層尺寸路線（Rubin／Rubin Ultra 及大型 ASIC 往 9.5–14 倍光罩）推進快於片數擴產，則 2027 年**加速器封裝顆數**成長顯著低於片數成長，而**每顆所含運算晶粒與 HBM 堆疊數**上升——片數口徑同時高估顆數、低估每顆含量。**方向未定**：對以顆計價之下游（基板、測試插槽、伺服器組裝）偏負，對以面積／晶圓計價之上游（TSMC 每片 ASP、HBM 堆疊數）可能偏正；CoPoS（方形面板，面積利用率高）量產若提前，則落差縮小。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [P] 守恆：幾何面積守恆（晶圓面積 ≥ Σ 中介層面積 ＋ 邊緣與切割損失）；`N(A)` 為上界，與良率相乘 |
| 選擇者 | GPU／ASIC 設計方（中介層尺寸、HBM 堆疊數、CoWoS-S／-L／-R）；TSMC 與 OSAT（片數擴產、CoPoS 時程）；HBM 廠（每顆堆疊數） |
| 已讀事實 | TrendForce 2026-05-14（引 Commercial Times）：現行最大 5.5 倍光罩、良率約 98%；2028 年 14 倍光罩、20 HBM；2029 年 > 14 倍、24 HBM；SoW > 40 倍光罩。TrendForce 2026-04-16：CoWoS 月產能 2026 年底約 11.5–14 萬片、2027 年約 17 萬片（法人）；CoPoS 試產線 2026-02 主要設備安裝完成，量產 2028–2029。TrendForce 2026-04-28：CoWoS 單片 ASP 約 1 萬美元；先進封裝約占 2025 年營收 10%；「capacity will reach about 1.3 million units in 2026 and could rise to 2 million in 2027」（units 未定義）。優分析 2026-09-15：「封裝面積越大，同一片晶圓可支撐的有效封裝數量就越少」，CoWoS-L 朝約 5.5 倍光罩；2026 年底約 12 萬片、2027 年約 18 萬片。all-about-industries 2025-06-19：「only 16 B200 … compared to 29 H100 or H200」每片。TSMC 3Q26 新聞稿（sec.py 實讀，3,823 字）：無 packaging／CoWoS 字樣，只有節點別晶圓營收占比。Amkor 10-Q 2Q26（sec.py）：Computing 終端市場占 22%；全文無「interposer」「2.5D」字樣 |
| 未證之連結 | 2026–2027 各世代中介層實際面積與出貨組合；片數 ↔ 顆數之官方或具名換算；市場共識是否以片數直接外推顆數（具名反方或賣方模型原文）；CoWoS-L（RDL＋LSI 橋接）是否改變可排版幾何（非整片矽中介層） |
| 量綱 | 顆／片 ＝ N(A) × Y；顆數成長 ＝ 片數成長 × [N(A₂)／N(A₁)] × [Y₂／Y₁]；每顆 HBM 堆疊數 × 顆數 ＝ HBM 堆疊需求 |
| 半衰期 | 季到年（世代切換 12–18 個月；CoPoS 量產 2028–2029） |

## 3. B 端可觀測載體（只指名）

1. TSMC 3Q26 6-K 新聞稿 https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm ；3Q26 法說逐字稿（未讀）
2. TSMC 路線（報導）https://www.trendforce.com/news/2026/05/14/news-tsmc-sees-ai-wafer-demand-rising-11x-from-2022-2026-targets-cowos-with-24-hbm-stacks-in-2029/ ；產能與 CoPoS https://www.trendforce.com/news/?p=56168 ；ASP https://www.trendforce.com/news/2026/04/28/news-tsmc-cowos-wafer-asp-reportedly-nears-7nm-levels-advanced-packaging-poised-to-become-a-key-profit-driver/
3. 片數 vs 面積評論 https://uanalyze.com.tw/index.php/articles/9531755299 ；每片顆數二手 https://www.all-about-industries.com/panel-level-packaging-at-tsmc-first-copos-pilot-line-2026-mass-production-from-2029-a-46222908685203d0c28cea97fcf7557c/
4. Amkor 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1047127/000104712726000046/amkr-20260630.htm
5. 未讀：NVIDIA 10-Q／電話會之出貨顆數或「units」口徑；ASE（ASX 20-F）先進封裝分列；Ibiden／Unimicron ABF 基板顆數或面積口徑；TSMC 20-F 先進封裝產能單位；具名賣方以「片 × 每片顆數」建模之原文。

## 4. 不寫

H1／H5、表達工具選擇、方向判斷。

## 5. 否決觸發（測一逐條實讀）

1. **可分離性：** 任一上市主體（TSMC、NVIDIA、Amkor、ASE、基板商）之申報、電話會或具名來源均無法把 CoWoS 片數換成封裝顆數或面積（每片顆數、平均中介層面積、顆數產能皆無）→ 否決（C-I3′／N-02 型）。
2. **已被定價／已揭露：** 具名賣方、TrendForce 或 TSMC 已以顆數（或片數 × 每片顆數）公開量化 2026–2027 加速器封裝供給，且市場流通數即為顆數口徑 → 否決（無錯價）。
3. **幾何不綁定：** CoWoS-L 之 RDL／LSI 架構或混排（大小中介層同片）使 `N(A)` 損失可忽略（< 10%），或世代組合 12 個月內不往 ≥ 9 倍光罩移動 → 否決。
4. **替代路徑提前：** CoPoS 或 SoW 於 12 個月內量產並承接主要大尺寸封裝 → 否決（重定價窗 < 12 個月）。
5. **方向抵銷：** 每顆 HBM 堆疊數與運算晶粒數上升，使以面積或堆疊計之需求與片數同步、只有以顆計之下游受影響 → 不否決但標方向分歧，不得合併為同向落差。
6. **主體錯置：** 落差主要落於非上市主體或台股（台股禁、複委託停用，CHARTER §2-8）而無美股可交易對應 → 標表達約束（§7-4 三題），不在生成階段否決。
