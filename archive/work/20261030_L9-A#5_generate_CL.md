# L9-A#5 生成卡｜受規管 HITL：會計恆等（執業醫師之「友善 PC」合併邊界——VIE 主要受益人判定 × 總額認列 vs 州 CPOM 收緊）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260921_L9-A_generate_GK.md；archive/work/20261007_L9-A#2_generate_CL.md；archive/work/20261015_L9-A#3_generate_CL.md；archive/work/20261023_L9-A#4_generate_CL.md；work/20261023_L9-A#4_test1_CL.md | EMITS: work/20261030_L9-A#5_generate_CL.md -->
**日期：** 2026-10-30　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 5／6）　**格：** L9-A　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。單位：百萬 US$。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。非「已殺／刻意排除」格中最後測一最舊者＝2026-10-23 批：L8-A#4、L8-I#4（本日已處理）、**L9-A#4**、L9-I#4、L12-P#4；依表序取 **L9-A**；既有生成 4 份 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `telehealth`、`corporate practice`，命中 0 筆。內部數字（§12）未取用。
- 比對（本卡須異型）：
  - **L9-A#1**（`archive/drive/USED_20260921_L9-A_generate_GK.md`）：席次定價之每席交付成本 vs 合併毛利率。本卡不涉毛利率。
  - **L9-A#2**（`archive/work/20261007_L9-A#2_generate_CL.md`）：PSAV 毛節省計費 vs IDR 回吐（變動對價）。本卡不涉付款方節省。
  - **L9-A#3**（`archive/work/20261015_L9-A#3_generate_CL.md`）：風險調整收入之 RAF 變動對價 vs RADV。本卡不涉 MA 給付。
  - **L9-A#4**（`archive/work/20261023_L9-A#4_generate_CL.md`；測一 `work/20261023_L9-A#4_test1_CL.md`）：ULAE 準備 paid-to-paid 比率。本卡不涉準備。
  - 本卡為**合併邊界恆等**（ASC 810 VIE 主要受益人 → 合併 → ASC 606 主理人總額認列）；人審環節＝持照醫師開立處方之法定 HITL。
  - ARCH_dead（L9-P 表達層、C-A1 可分離性、C-A2 無可交易主體、C-I5 cohort 無）：無合併邊界型死因；重疊不構成丟棄。
- §7-10 領域最近公開：HIMS 10-Q 2Q26（2026-08-10）；LFMD 10-Q 2Q26（2026-08-05）；CA AG Carbon Health 和解報導 2026-08-17；CA 上訴案 amicus 2026-03-30。下一檢查點＝兩家 3Q26 10-Q（約 2026-11 上旬）。

## 1. 落差一句

直面消費者遠距醫療平台（HIMS、LFMD）以「友善 PC」結構運作：醫師擁有之專業法人（Affiliated Medical Groups／LifeMD PC）與平台無共同股東，平台經管理服務協議（MSA）＋股權移轉限制（continuity）協議取得「主導對經濟績效最重大活動之能力」，據此判定為 VIE 主要受益人而**全額合併**，再以「平台決定由哪個 PC 與醫師提供諮詢」為由按**主理人**認列全部諮詢收入。恆等式：**合併收入＝平台自身收入＋PC 對病患收入 − 公司間抵銷**；合併與總額認列兩個判斷共同依賴「控制」。州 CPOM 收緊（Oregon SB 951：MSO 不得握有雇用、定價、帳務、付款方契約之最終決定權，股權移轉協議只限窄情境；California SB 351 2026-01-01 生效；CA AG 於上訴案主張 continuity 協議本身即可違反 CPOM；Carbon Health 和解要求 MSO 放棄對 PC 之定價／雇用控制）正好拆的是**權力條件**之證據。種子主張：若控制條款須改寫，會計上可能 (a) 去合併、諮詢收入改按代理人淨額（平台費）認列，或 (b) 經濟不變而僅改呈現；讀者把「訂閱收入」讀成平台自身可持續之收入時，部分讀到的是一個以可被州法否定之控制為前提的合併選擇。**方向未定**：Oregon 對無州內實體診所之遠距醫療豁免；2029 前既存結構不適用；去合併未必改變現金流。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：合併邊界（ASC 810 VIE）× 主理人／代理人（ASC 606）；外生變數＝州 CPOM 對 MSO 控制條款之限制 |
| 已讀事實 | HIMS 10-Q 2Q26 Note 11：「the variable interest entities (“VIEs”) are the Affiliated Medical Groups … primary beneficiary … because it has the ability to direct the activities that most significantly affect the entities’ economic performance and has the obligation to absorb the losses」；「There is no noncontrolling interest」；VIE 流動及總資產 7.8（FY25 末 6.9）、負債 7.9（6.0）；「the VIEs charged $ 26.9 million and $ 96.6 million」（2Q26 vs 2Q25）、上半年 55.3 vs 224.0；VIE 淨損 2.9（5.8）；XeCare 於 2025-11 改為全資、Apostrophe 2025-04 全資。收入政策：「accounts for the Affiliated Medical Groups service revenue … as a principal … because (i) the Company determines which Affiliated Medical Group and Provider provides the consultation」。風險因子：「corporate practice of medicine doctrine … has been the subject of a recent increase in focus and action by a number of state legislatures」；違反則「we would need to restructure the arrangements … or terminate」。總收入 753.2（544.8）。LFMD 10-Q 2Q26 Note：「LifeMD PC is a VIE and subject to consolidation. LifeMD PC and the Company do not have any stockholders in common … managed service agreement … provide all non-clinical services」；「Total assets and liabilities for the LifeMD PC were not material」；Telehealth subscription revenue 29.3（62%）、product 18.0（38%），總 47.3。 |
| `[D]` | HIMS VIE 收費 ÷ 總收入：2Q26 ≈ 3.6%、2Q25 ≈ 17.7%（降幅來源未讀：XeCare 改全資？定價／包裹改制？）；LFMD 訂閱收入 ÷ 總收入 ≈ 62% |
| 未證之連結 | (i) 兩家 MSA／continuity 協議實際條款是否落入 SB 951／SB 351 禁區；(ii) 失去權力條件後，主理人判斷（i）–（iii）是否仍成立——即去合併是否必然改淨額；(iii) HIMS VIE 收費驟降之原因；(iv) 兩家醫師所在州與 Oregon 遠距豁免之適用；(v) 公司是否已揭露重組計畫或審計師關鍵查核事項（CAM）提及 VIE。此即測一第一關。 |
| 量綱 | 可能改淨額之收入 ÷ 總收入（%）；去合併對營收與毛利率之 pp 變動；無純量 H1 |
| 半衰期 | 州法：CA 2026-01-01 已生效、OR 新設 2026-01-01／既存 2029-01-01；CA 上訴判決時點 `[A]` 2026–2027，待測 |

## 3. B 端可觀測載體（只指名）

1. HIMS 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1773751/000177375126000163/hims-20260630.htm （Note 11 VIE、收入政策主理人段、CPOM 風險因子）；HIMS 10-K FY25 https://www.sec.gov/Archives/edgar/data/1773751/000177375126000022/hims-20251231.htm
2. LFMD 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/948320/000149315226036200/form10-q.htm （VIE 段、收入分列）
3. Oregon SB 951 解析（Foley，2025-06-17）https://www.foley.com/insights/publications/2025/06/oregons-new-corporate-practice-of-medicine-restrictions-five-takeaways-for-digi/
4. CA AG amicus 與 SB 351／AB 1415（Faegre Drinker，2026-05-15）https://www.faegredrinker.com/zh/insights/publications/2026/5/mso-pc-structures-in-the-crosshairs-california-ag-takes-aim-at-continuity-agreements
5. CA AG Carbon Health 和解（Digital Health Insights，2026-08-17）https://dhinsights.org/news/how-californias-carbon-health-ruling-impacts-msos-tech-companies
6. 待測一指名讀：兩家 10-K 之 CAM 段與 MSA 附件（EX-10）；HIMS 2Q25→2Q26 VIE 收費降幅之一手說明；*Art Center Holdings v. WCE CA Art*（B338625）判決；第三家以上友善 PC 上市主體（如 TDOC、TALK、AMWL）之 VIE 揭露；SB 351 法條原文。

缺段（§7-2）：協議條款、CAM、上訴判決；本輪只讀上列；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | HIMS VIE 資產僅 7.8、收費占總收入 ≈ 3.6%；產品經全資藥局出貨，不受 PC 邊界影響 | 載體 1 | 量級不足 |
| R2 | Oregon SB 951 明文豁免「無州內實體診所之遠距醫療」，既存結構至 2029 才適用 | 載體 3 | 外生變數對樣本主體不咬合 |
| R3 | 主理人判斷以平台決定配置與負責履約為據，與是否合併 PC 可分離；去合併仍可總額 | 載體 1 收入政策 | 恆等差不傳導至收入 |
| R4 | Carbon Health 報導稱 SB 351／AB 1415「don't expressly prohibit MSO/PC structures」 | 載體 5 | 監理只改條款、不改結構 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後找不到樣本主體之控制條款（MSA／continuity）落入 SB 951、SB 351 或 CA AG 主張範圍之一手原文或具名法律分析（只剩推論）；或
(2) 可運作對照只能寫成一般「監理風險」而無「權力條件 → 合併 → 總額」之特有恆等鏈（即主理人判斷可與合併完全分離，R3 成立）；或
(3) 公司、審計師（CAM）或具名賣方已量化去合併或改淨額對營收之影響（已定價）；或
(4) `[D]` 樣本主體可能改淨額之收入 ÷ 總收入 < 5%（最近 4 季均值），且第二家以上主體亦 < 5%——量級不足；或
(5) 12 個月內無可觀測驅動：無州法生效日、上訴判決、AG 執法或公司重組揭露可指名。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：營業收入（總額／淨額）、VIE 附註、毛利率。2. 可交易工具：HIMS／LFMD 普通股、選擇權（不選）。3. 半衰期：州法生效日與判決 vs ≥ 12 個月窗。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L9［A］格加「#5 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0133。線索檔（§12 D）：本輪事實非算力收支類，未寫。不改 L9-A#1–#4、L9-I#1–#4、L9-P、C-A1、C-A2、C-I5 結論。
