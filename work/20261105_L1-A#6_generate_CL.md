# L1-A#6 生成卡｜能源與電力：會計恆等（發電設備商之客戶預付浮存——CFO ≡ 營運盈餘 ＋ Δ合約負債；Δ合約負債 ≡ 新簽預付（訂單＋保位協議）− 交機認列 → FCF 為訂單「加速度」之函數，非盈利水準）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260926_L1-A_generate_GK.md；archive/work/20261008_L1-A#2_generate_CL.md；archive/work/20261016_L1-A#3_generate_CL.md；archive/work/20261024_L1-A#4_generate_CL.md；archive/work/20261030_L1-A#5_generate_CL.md；work/20261030_L1-A#5_test1_CL.md；archive/work/20261015_L2-I#3_generate_CL.md | EMITS: work/20261105_L1-A#6_generate_CL.md -->
**日期：** 2026-11-05　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 0→1／6）　**格：** L1-A　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L2-P#6／A#6／I#6 已於本日測一）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-30（L1-A#5、L8-A#5、L8-I#5、L9-A#5、L9-I#5、L12-P#5）→ 依表序取 **L1-A**（L1-P＝刻意排除 T-11 不取）；既有生成 5 份 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `long-term service`／`LTSA`／`gas turbine`／`GE Vernova`，命中 0 筆。內部數字（§12）：未取用。
- 比對（本卡須異型）：
  - **L1-A#1**（GK）：PPA 鎖定價 − 現貨存量。本卡不談電價。
  - **L1-A#2**：Bloom 產品毛利於驗收一次認列、壽命期成本落服務合約（**毛利**跨期配比）。本卡不動毛利認列，動的是**現金與盈餘之差**（資產負債表浮存）。
  - **L1-A#3**：AFUDC 權益（非現金盈餘）。本卡方向相反：現金 ＞ 盈餘。
  - **L1-A#4**：受管電業大負載客戶預付款之損益攤銷（費率基外）。本卡主體為**設備供應商**、項目為營運資金而非損益。
  - **L1-A#5**：核能 PTC 分段收入。主體、恆等皆不同。
  - **L2-I#3**（`archive/work/20261015_L2-I#3_generate_CL.md`）：買方保位之**取消／延後選擇權**（backlog 品質，誘因型）。本卡不問訂單可否取消，問**已收預付現金**於交機時之反轉時序（會計恆等）；測一不得以 backlog 可取消性為落差。
  - **L15-A#2**（合約負債浮存，軟體訂閱）：訂閱浮存隨續約滾動、穩態不反轉。本卡之浮存綁定**一次性產能稀缺週期**之保位與交機排程（2026–2030），穩態假設不成立與否即測點；型態為「Δ合約負債之二階依存」，非浮存存在本身。
  - ARCH_dead：C-A3（折舊年限）、C-I3′／N-02（利益未分列）——本卡項目**已分列**（10-Q 現金流量 MD&A 逐項歸因）。T-11 不碰。
- §7-10 領域最近公開：GEV 10-Q 3Q26（2026-10-28，acc `0001996810-26-000163`）；GEV 8-K 3Q26 業績稿（2026-10-28，acc `0001996810-26-000162`）；XBRL companyfacts 至 2026-09-30。下一檢查點＝GEV 10-K FY26（約 2027-01 下旬）。

## 1. 落差一句

發電設備商之營業現金流 ≡ 調整後盈餘 ＋ Δ營運資金，其中 Δ合約負債 ≡ 新簽預付（訂單頭期款＋**保位協議 slot reservation agreements** 之預付）− 交機時之合約負債轉收入；故 FCF 對**訂單增速（加速度）**敏感，而非對盈利水準。GEV（sec.py 實讀）：9M26 CFO **16,737M**（9M25 2,508M），其中「a $17.0 billion inflow from changes in working capital」、「contract liabilities and current deferred income of $19.5 billion, driven by down payments on orders and slot reservation agreements at Power」；FCF 9M26 **15,307M** vs 9M25 1,902M；合約負債（XBRL `ContractWithCustomerLiability`）20,304M（2025-09-30）→ 25,950M（2025-12-31）→ 31,949M → 40,037M → **45,747M**（2026-09-30）；同期營收 9M26 33,084M、歸屬淨利 9M26 6,704M（含 1Q26 4,745M 之非經常項，待測一拆）。業績稿：2026 FCF 指引 **$16–17B**（前值 $11.5–12.5B）；3Q26 Gas Power「Signed 11 GW … including 8 GW of slot reservation agreements and 3 GW of orders. Converted 13 GW … to orders and shipped 5 GW … slot reservation agreements from 63 to 58 GW」；回購授權增至 $20B。種子主張：市場以 FCF（及其支撐之回購）作為盈利能力代理，未把「營運資金以外之 CFO ≈ 0」與「預付浮存於交機高峰（訂單增速趨緩、交機量上升時）轉負」自 FCF 中分離。**方向未定**：若保位／訂單持續加速、浮存穩態化（R3），FCF 可維持；若訂單平台化而交機量升，Δ合約負債轉負、FCF < 盈餘，且已用於回購之現金不可回收。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：CFO_t ≡ (NI_t ＋ 非現金項_t) ＋ ΔCL_t ＋ ΔWC其他_t；ΔCL_t ≡ d_o·Orders_t ＋ d_s·SRA_t − Σ(交機_t × 累計預付比)。FCF 之「預付成分」＝ΔCL_t；交機高峰期 ΔCL_t < 0 為恆等必然，非預測 |
| 已讀事實 | 上述 10-Q 3Q26 現金流 MD&A 原文、業績稿 3Q26 GW 拆分與指引、XBRL 合約負債 9 期序列與 CFO／NI／營收序列；10-Q RPO 196,721M（Equipment RPO 104,054M，33%／60%／97% 分年認列句，截斷待全讀）；10-Q grep `refundable` 0 筆（§7-2：非不存在） |
| 未證之連結 | 保位協議是否計入 RPO、預付比例 d_s 與可退還性；交機排程（GW／年）與保位轉單之時序；併購（Prolec GE）帶入之合約負債與有機 ΔCL 之分離（現金流量表已排除併購，資產負債表未排除）；1Q26 淨利之非經常項；同業（CAT Energy & Transportation customer advances、Siemens Energy、Mitsubishi Power——後二者非 SEC 申報）是否同型；具名賣方是否以「ex-down-payment FCF」估值 |
| 量綱 | 有機 ΔCL ÷ FCF（%，滾動 4 季）；CL ÷ TTM 營收（倍）；交機 GW ÷ 新簽 GW（比）；預付反轉期之 ΔCL ÷ 調整後 EBITDA（%） |
| 半衰期 | 保位協議交機期（推定 2028–2030，待證）；季度可觀測 |

## 3. B 端可觀測載體（只指名）

1. GEV 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/1996810/000199681026000163/gev-20260930.htm （Note 9 合約資產／負債、RPO、現金流量 MD&A）
2. GEV 8-K 3Q26 業績稿 https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000162/gevpressrelease3q26.htm （GW 拆分、FCF 指引、回購授權）
3. GEV XBRL companyfacts（`python tools/sec.py facts GEV --concept ContractWithCustomerLiability`；`NetCashProvidedByUsedInOperatingActivities`；`NetIncomeLoss`；`RevenueFromContractWithCustomerExcludingAssessedTax`）
4. GEV 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000148/gev2q2026form10-q.pdf ；1Q26 https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000064/gev1q2026form10-q.pdf （未讀）
5. 二手（未讀，只作線索）：FourWeekMBA「Down Payments Gave GE Vernova $19.5B of Cash in Nine Months」https://fourweekmba.com/ai-down-payments-gave-ge-vernova-19-5b-of-cash-in-nine-months/ ；Turbomachinery「GE Vernova Q3 2026 gas power backlog 122 GW」https://www.turbomachinerymag.com/view/ge-vernova-q3-2026-gas-power-backlog-122-gw-trench-acquisition
6. 未讀：GEV 10-K FY25 保位協議會計政策與 RPO 排除句；3Q26 電話會議官方逐字稿之 FCF 正常化／「down payments」句；CAT 10-Q customer advances；具名賣方原文。

缺段（§7-2）：具名賣方以剔除預付之 FCF 估值之原文本輪未見；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 管理層已於 10-Q 逐項歸因 CFO 至預付，資訊公開、市場已見 | 載體 1 | 已定價 |
| R2 | 二手媒體已以標題量化預付對現金之貢獻 | 載體 5 FourWeekMBA | 已定價 |
| R3 | 產能稀缺延續、保位持續滾動（業績稿預期 YE26 ≥ 130 GW），浮存穩態化，反轉延後至窗外 | 載體 2 | 時序 |
| R4 | 預付若不可退還，訂單取消時轉為收益，下行反而受保護 | 未證（10-Q grep 0） | 方向 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 有機 ΔCL（現金流量表口徑）不足 4 季可對齊序列，或無法與併購帶入額分離；或
(2) `[D]` 量級：滾動 4 季有機 ΔCL ÷ FCF < 40%，或 CL ÷ TTM 營收於最近 4 季未上升（門檻凍結於此）；或
(3) 一手文件確認保位／訂單預付對交機前之營運成本（存貨採購）全額對應支出（即浮存已被同步消耗，淨營運資金效果 < 20% 之 ΔCL）；或
(4) 具名賣方或評等機構已以剔除預付之 FCF（或「normalized FCF」）估值或評等（已定價）；或
(5) 與 L2-I#3（可取消訂單選擇權）或 L15-A#2（訂閱浮存）為同一金額之重述——即本卡之反轉時序無法與取消率或續約率分離；或
(6) 12 個月內無可觀測驅動：無季報 ΔCL 符號變化、無保位轉單／交機 GW 揭露、無 FCF 指引更新。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：合約負債及流動遞延收入、現金流量表營運資金項、RPO。2. 可交易工具：（不選）。3. 半衰期：保位交機期；季度。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L1［A］格加「#6 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0171。`export/LEADS_算力收支.md`：本輪事實（燃氣發電設備預付與 FCF）非 AI 算力投入／收入／硬體／雲端合約／資料中心之直接事實（業績稿未分列資料中心客戶額），不寫。不改 L1-A#1–#5、L1-I#1–#5、L1-P（T-11）、L2-I#3、L15-A#2、C-A3、N-02 結論。
