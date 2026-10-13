# L13-P#2 生成卡｜資本與融資結構：守恆（同一併網 MW 只能挖礦或 HPC：MW_mine + MW_HPC,gross ≤ MW_site；HPC 現金流由子公司層有擔保票據之超額現金流掃款先取，母公司層之可支配現金隨 MW 移轉而一對一流失挖礦端）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/FILEIDS.tsv；archive/drive/USED_20261002_L13-P_generate_GK.md；archive/drive/USED_20261002_L13-P_test1_GK.md；archive/drive/USED_20261002_L13-I_generate_GK.md；archive/work/20261011_L13-A#2_generate_CL.md；work/20261011_L6-P#2_test1_CL.md | EMITS: work/20261013_L13-P#2_generate_CL.md -->
**日期：** 2026-10-13　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 2→3／6）　**格：** L13-P　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L11-I#2 測一 2026-10-13，Q-0035 done）。非已殺／刻意排除且無 #2 之格中最後測試日最舊者：`archive/FILEIDS.tsv` L13-P 測一 2026-10-02T07:31Z，早於 L13-I（08:00Z）、L14-*／L15-*（10-05 起）→ **L13-P**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `bitcoin miner`、`HPC lease`、`interconnect`、`hashrate`，3 筆（機架功率、每日字數），皆與本格無關；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L13-P#1**（測一不通過，`archive/drive/USED_20261002_L13-P_test1_GK.md`）：GPU 熱循環計數封頂實體壽命 vs 伺服器會計年限；死因＝否決 (1)：現場熱循環計數無任何申報分列，與會計年限不可並列。本卡之守恆量為**併網 MW**，兩側（挖礦 MW／HPC MW、hashrate）皆已在同一 10-Q 分列；不涉折舊年限或元件壽命。
  - **L13-A#1**（入表租賃≠義務上界）、**L13-A#2**（客戶預付之重大融資成分，`archive/work/20261011_L13-A#2_generate_CL.md`）：本卡不涉租賃義務或預付；論的是出租方之**資本結構隔離**。
  - **L13-I#1**（供應商兼股東兼債權人時之信評資訊含量）：本卡不涉信評。
  - **C-A4／C-A3**（ARCH_dead #4–5：重定價窗／折舊樞紐）：本卡不以年限或續約單價比 `k` 為樞紐；不重開。
  - **L6-P#2**（RPO 交付之電力-時間預算，`work/20261011_L6-P#2_test1_CL.md`；死因＝ρ 每 MW 營收不可界定）：該卡守恆在**承租／雲端**側之營收上界；本卡在**出租方**同一站址之挖礦／HPC MW 互斥與債權層級，不需 ρ。**L1-I#2**（公用事業費率基礎）、**L2-P#2**（散熱封頂每櫃功率）：不涉。
- §7-10 領域最近公開：TeraWulf 10-Q 期末 2026-06-30（2026-08-05 申報）；Cipher 10-Q 期末 2026-06-30（2026-08-04）；TeraWulf 8-K 2026-10-05（Muskie 擴建、循環信用額度擴增）。下一檢查點＝兩家 3Q26 10-Q（2026-11 初）。

## 1. 落差一句

市場以「挖礦現金流＋HPC 租約價值」之加總讀改轉 HPC 之礦企，並把母公司層可轉債視為兩者共同支撐；種子主張同一站址併網 MW 守恆（MW 從挖礦移到 HPC，hashrate 一對一下降），而 HPC 端現金流先經子公司層有擔保票據之利息、攤還與**超額現金流強制回購要約**，母公司層可支配現金在轉換期內由「挖礦 MW 剩餘量 × 每 MW 挖礦毛利」＋「子公司掃款後可分配額」構成——錯價只在把移出之 MW 同時算在兩邊，或把子公司現金流視為母公司可支配。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆**：\(MW_{mine}(t) + MW_{HPC,gross}(t) \le MW_{site}\)（併網上限）；\(H(t) \approx MW_{mine}(t)/\eta\)（\(\eta\)＝j/th）；母公司可支配現金 \(\approx g_{mine}\cdot MW_{mine}(t) + D_{sub}(t)\)，\(D_{sub}\)＝子公司於有擔保票據付息、攤還、超額現金流回購要約後之可分配額 |
| 可見端 | 同一 10-Q：站址挖礦 MW、HPC critical IT MW、營運 hashrate、j/th；有擔保票據之發行主體（子公司）、擔保人、首順位留置、超額現金流回購條款；受限現金（專款專用、償債準備帳戶） |
| 指名不可見端 | 子公司對母公司之分配限制條款全文（indenture restricted payments 定義）；每 MW 挖礦毛利之申報分列；gross MW 與 critical IT MW 換算係數 |
| 表達工具型態（只指名，不選券） | 美股可交易、同站址由挖礦轉 HPC 且於子公司層發行有擔保票據之主體（股權或母公司可轉債）。不選券 |

`[D]` 可重算對照（公開申報數，非測一結論）：TeraWulf Lake Mariner 挖礦 245 MW → 145 MW（2025-12-31 → 2026-06-30，×0.59）；同期營運 hashrate 9.3 → 5.6 EH/s（×0.60）；HPC critical IT 18 → 81 MW。守恆之一側在申報層近乎一對一。**不主張挖礦毛利方向、不主張可分配額大小、不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. TeraWulf 10-K FY25 https://www.sec.gov/Archives/edgar/data/1083301/000108330126000031/wulf-20251231.htm ：「the Lake Mariner Data Campus operated 245 MW of legacy bitcoin mining capacity and had 18 MW of critical IT HPC capacity」；「through its wholly owned subsidiary Wulf Compute LLC (“Wulf Compute”), completed a private offering of $ 3,200.0 million aggregate principal amount of 7.75 % Senior Secured Notes due 2030」；「required to make an offer to holders to repurchase the 2030 Secured Notes based on excess cash flows」；「secured by first-priority liens」；「Customer backstop arrangements … are only effective following the commencement of the relevant lease」；母公司層另有 2030／2031／2032 Convertible Notes（公允價值表同段）。hashrate 表：9.3 EH/s（2025-12-31）。
2. TeraWulf 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1083301/000108330126000166/wulf-20260630.htm ：「operated 145 MW of legacy bitcoin mining capacity and had 81 MW of critical IT HPC capacity」；「TeraWulf operational hashrate (EH/s) 5.6 12.2」（2026-06-30 vs 2025-06-30）；超額現金流回購句同上。
3. Cipher 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1819989/000181998926000041/cifr-20260630.htm ：「Black Pearl Facility … that was previously used for bitcoin mining. The Company is in the process of retrofitting the Black Pearl Facility for an HPC tenant」；「we currently operate approximately 207 MW of capacity at one bitcoin mining data center in Texas」；「Restricted cash primarily relates to proceeds from various senior secured notes offerings which the Company is restricted from using for general corporate purposes outside of financing specific site developments」；「cash required to be held in debt service accounts related to various senior secured notes」；Barber Lake 由子公司 Cipher Barber Lake LLC 出租，預計 2026-09 交付。
4. TeraWulf 8-K 2026-10-05 https://www.sec.gov/Archives/edgar/data/1083301/000162828026064757/wulf-20261001.htm ：子公司 DB Long Hunts Data LLC 輸電與能源服務協議修訂；循環信用額度擴增「subject to customary closing conditions」。

缺段（§7-2）：indenture 全文（restricted payments、excess cash flow 定義）未取；Cipher 10-Q 未見 EH/s 字串（hashrate 單位或表名待測一確認）；每 MW 挖礦毛利無申報分列。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | 市場本以 MW 為單位估值，並明示 MW 由挖礦「allocate」至 AI/HPC（「allocate 20% of their current and target power capacity to AI/HPC」；「~$4.5M per megawatt (MW) of installed capacity」），即已計守恆 | VanEck, Matthew Sigel, 2024-08-16 https://www.vaneck.com/us/en/insights/blogs/digital-assets/matthew-sigel-bitcoin-miners-ai-arbitrage-play-to-boost-revenue/ | 雙計可能不存在（已定價） |
| R2 | 公司自述轉型「HPC hosting as its primary business」，收入組合移出挖礦為公開指引 | TeraWulf 10-K（§3-1） | 挖礦端流失已被申報預告 |
| R3 | 挖礦毛利占母公司現金流可能已微小，MW 移轉之母公司影響量級不足 | TeraWulf 10-K 營運現金流為負（同檔） | 量級可能不足 |
| R4 | 超額現金流掃款只在初期建設完成後啟動，且 Google backstop 只在租約起算後生效；轉換期之時序可能與 ≥ 12 個月窗不合 | TeraWulf 10-K（§3-1） | 窗與時序風險 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法就同一主體取得 ≥ 4 期同口徑之站址挖礦 MW、HPC MW 與營運 hashrate **水準**，或無法取得子公司有擔保票據之分配限制／超額現金流掃款條款原文（indenture 或 10-K／10-Q 附註），致母公司可支配現金不可界定；或
(2) 可運作對照只能寫成熱循環 vs 會計年限（L13-P#1）、租賃義務上界（L13-A#1）、預付融資成分（L13-A#2）、信評（L13-I#1）、RPO 每 MW 營收 ρ（L6-P#2）或折舊樞紐／重定價窗（C-A3／C-A4）；或
(3) 具名賣方、信評機構或公司原文已就母公司層可轉債之償付來源，分列挖礦 MW 剩餘量與子公司可分配額（已定價）；或
(4) `[D]` 轉換期內挖礦 MW 減少所致母公司層現金變動 < 母公司層年度利息支出之 10%（量級不足）；或
(5) 12 個月內無可觀測驅動：無新增站址由挖礦轉 HPC、無子公司層新票據、且 MW／hashrate 序列不再變動。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：母公司可支配現金不入單一申報行，須由 MW、hashrate、受限現金、子公司票據條款拼合。2. 可交易工具：股權與母公司可轉債對本機制方向可能不同。3. 半衰期：轉換完成後挖礦 MW → 0，守恆一側消失；窗限於轉換期。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L13［P］格加「#2 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列。不改 L13-P#1、L13-A／L13-A#2、L13-I、C-A3／C-A4、L6-P#2 結論。
