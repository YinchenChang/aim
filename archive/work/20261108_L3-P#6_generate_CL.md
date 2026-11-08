# L3-P#6 生成卡｜半導體製造測試：守恆（在製品流量守恆／Little 定律：WIP ＝ 產出率 × 週期時間——HBM 占比上升使週期時間拉長，同一晶圓投片產能之「期內可出貨量」下降，擴產先以在製品存貨出現、後以出貨出現）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md（經 FUNNEL §2）；archive/drive/USED_20260926_L3-P_generate_GK.md；archive/work/20261009_L3-P#2_generate_CL.md；archive/work/20261016_L3-P#3_generate_CL.md；archive/work/20261024_L3-P#4_generate_CL.md；archive/work/20261031_L3-P#5_generate_CL.md；work/20261031_L3-P#5_test1_CL.md；work/20261024_L3-P#4_test1_CL.md（grep） | EMITS: work/20261108_L3-P#6_generate_CL.md -->
**日期：** 2026-11-08　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 2→3／6）　**格：** L3-P　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L1-I#6 已於本日測一）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-31（L3-P#5、L3-A#5、L3-I#5、L4-P#5、L4-A#5）→ 依表序取 **L3-P**；既有生成 5 份 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `T-glass`／`substrate`／`glass cloth`／`ABF`，命中 0 筆（候選題材之一，見下，未採）。內部數字（§12）：未取用。
- 捨棄之候選題材：T-glass／載板面積守恆——公開層已有 Counterpoint「From T Glass Crisis to Capacity Erosion」與 Tom's Hardware 報導（Nittobo 擴產），且與 L3-P#4（面積幾何，死於已定價）同型，不生成。
- 比對（本卡須異型）：
  - **L3-P#1**（GK）：曝光機**機時守恆**（WPH × 機台 ÷ 曝光次數）——產能**速率**上界。本卡不談速率上界，談**存量＝速率 × 時間**之流量守恆：速率不變時，週期時間拉長即需更大在製品存量，且擴產對出貨之時滯＝週期時間。
  - **L3-P#2**：HBM 堆疊**良率乘積**（每好位元之晶圓投入，trade ratio）；方向已揭露／定價。本卡在**良率 100%** 時亦成立；trade ratio 只作輸入。
  - **L3-P#3**（觸壓壽命，耗材流量）、**L3-P#4**（中介層面積幾何）、**L3-P#5**（老化腔熱量，死於插槽綁定）：物件與守恆量皆異。
  - **L3-A 系**（單價恆等、補助淨額、材料轉嫁…）：會計恆等型。本卡以存貨科目為**可觀測載體**，但落差為實體流量（片／天），非認列口徑；若測一發現 WIP 天數變動主要來自成本口徑（每位元成本、跌價） → 否決 (3)。
  - **公開層相鄰敘事（反方）：** SEMI（Sungho Yoon，2025-08-21，semiengineering.com 贊助部落格）已稱「since 2020, fab cycle times have grown at a compound annual growth rate of 14.8%」，以週期時間為**產出速率之減速**，並以 HBM 滲透率、位元成長、稼動率、週期時間建模投片需求（「wafer input would need to increase by 23.9% annually」）；**未用 Little 定律、未以 WIP 存量或時滯建模、未給天數**。本卡須與之區分：彼為速率；本卡為存量與時滯。若測一發現具名賣方已以 WIP 天數／時滯量化記憶體供給回應 → 否決 (2)。
  - ARCH_dead：C-I3′／N-02（利益未分列）——本卡否決 (1) 為同類可分離性題（HBM 之 WIP 未分列）。主體與機制不同，非已殺同型。
- §7-10 領域最近公開：Micron 10-K FY26（2026-10-09 申報，期末 2026-09-03）；Micron 10-Q 3Q26（2026-06-25，期末 2026-05-28）；TSMC 20-F FY25（2026-04-16）；SEMI 部落格 2025-08-21。下一檢查點＝Micron 1Q27 10-Q（期末約 2026-12 初，申報約 2027-01）；SK hynix 4Q26 法說（約 2027-01 下旬）。

## 1. 落差一句

Little 定律（穩態流量守恆）：`WIP ＝ λ × CT`（WIP 片數、λ 投片／產出率、CT 週期時間）。記憶體供給在公開層以**投片產能（片／月）× 位元密度 ÷ trade ratio** 換算為**同期**位元供給；但 Micron 10-K FY26 自承「Manufacturing system-level solutions, such as SSDs, managed NAND, and HBM, typically results in higher per-unit manufacturing costs and **longer cycle time** as compared to other products」。若 HBM（TSV、堆疊、測試、老化）使加權 CT 拉長，則 ① 擴產／轉產之出貨回應落後 ΔCT；② 同一 λ 須綁住更多在製品，產能爬坡期之可出貨量低於同期換算；③ 需求反轉時，管線內在製品（以 CT 計之存量）於反轉後仍持續流出——供給尾巴長於以月產能外推者。**種子主張：以同期位元換算之供給回應模型，系統性低估「緊缺期之時滯」與「反轉期之殘餘流出」**。方向未定：緊缺延長（對記憶體廠正）與反轉期過剩（負）並存。

**已讀事實 `[D]`（Micron，sec.py 實讀；成本口徑，非片數）：** WIP 餘額 6,401（2025-08-28）→ 6,960（2026-05-28）→ 8,252（2026-09-03）百萬美元。WIP ÷ 當季 COGS × 當季天數：4Q25 ≈ 93 天（6,401 ÷ 6,261 × 91）；3Q26 ≈ 99 天（6,960 ÷ 6,400 × 91）；4Q26 ≈ 113 天（8,252 ÷ 7,182 × 98；4Q26 為 14 週）。季 COGS 由年度／九個月相減（FY26 25,684 − 18,502；FY25 22,505 − 16,244）。**此為成本加權之 WIP 天數，不是實體 CT**：每位元成本下降、產品組合（HBM 單位成本高）與跌價迴轉均會扭曲。TSMC 20-F FY25：WIP NT$181,198.8 百萬（2024-12-31）→ NT$188,014.4 百萬（2025-12-31）；年報以「shorter cycle time」為競爭要素，未揭露 CT 天數。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [P] 守恆：流量守恆（Little 定律 `L ＝ λW`；穩態下在製品存量 ＝ 產出率 × 停留時間）；擴產之出貨時滯 ＝ CT |
| 選擇者 | 記憶體廠（HBM 轉產比例、前段／後段 CT、是否以成品或晶圓庫存緩衝）；GPU／ASIC 客戶（HBM 世代與堆疊高度 → 後段步驟數）；設備／封測（TSV、TC bonder、測試站數決定後段排隊） |
| 已讀事實 | 見 §1。Micron 10-K FY26：「In 2026, HBM3E 12-high represented the majority of our HBM shipments. In 2026, we began volume production of our HBM4 36GB 12-high」；「delivered samples of HBM4 48GB 16-high」。SEMI 2025-08-21：CT 年複合 +14.8%（2020 起）；「HBM wafers consume over three times more wafer area per bit」；「semi-finished wafers to accumulate as inventory」 |
| 未證之連結 | 實體 CT（天）之一手值（前段 DRAM、HBM 後段）；WIP 天數變動中 CT vs 成本口徑之拆分；HBM 之 WIP 是否可分列；市場共識是否以同期換算（具名賣方模型原文）；SK hynix／Samsung（非 SEC 申報）同型序列 |
| 量綱 | 片 ＝ 片／天 × 天；位元供給(t) ＝ λ(t − CT) × 位元／片 ÷ trade ratio；時滯 ＝ ΔCT（天）；`[D]` 載體＝WIP 金額 ÷ 日 COGS（天，成本口徑） |
| 半衰期 | 季（CT 以週至月計；HBM 世代 12–18 個月） |

## 3. B 端可觀測載體（只指名）

1. Micron 10-K FY26 https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm （Note 6 存貨；風險因子 cycle time 句；損益表）
2. Micron 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/723125/000072312526000015/mu-20260528.htm ；1Q26／2Q26 10-Q 與 FY24／FY25 10-K（WIP 天數序列 ≥ 8 季）
3. TSMC 20-F FY25 https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm （Note 13 存貨；cycle time 句）；TSMC 6-K 季報
4. SEMI／Semiconductor Engineering 2025-08-21 https://semiengineering.com/from-latency-to-reaction-simulating-the-next-wafer-demand-inflection/
5. 未讀：Micron 電話會原文之 HBM cycle time／lead time 句；SK hynix、Samsung 法說之 HBM 生產週期；SanDisk／WDC 10-Q（NAND 對照）；NVIDIA 10-Q 之 supply／purchase obligations 與 lead time 句；具名賣方位元供給模型是否含時滯；TrendForce 位元供給預估方法。

## 4. 不寫

H1／H5、表達工具選擇、方向判斷。

## 5. 否決觸發（測一逐條實讀）

1. **可分離性：** Micron（或任一上市記憶體／代工主體）之申報、電話會或具名一手來源均無 CT 天數、HBM 生產週期或 HBM 在製品之任一可量化值，且 `[D]` WIP 天數無法以 ≥ 8 季序列計得 → 否決（C-I3′／N-02 型）。
2. **已被定價／已揭露：** 具名賣方或公司已以 WIP 天數、生產週期時滯或 Little 定律型存量量化記憶體／HBM 供給回應；或 SEMI 型 CT 敘事已含時滯／存量項 → 否決（無錯價）。
3. **口徑主導：** `[D]` WIP 天數之變動 ≥ 50% 可由每位元成本變動、產品組合單位成本或存貨跌價／迴轉解釋（10-K／10-Q 原文或可重算拆分）→ 否決（載體不代表 CT）。
4. **時滯不重要：** HBM 加權 CT 相對 DRAM 之增量 < 2 週（一手），或記憶體廠以成品／晶圓庫存（die bank）緩衝使出貨不受 CT 約束（一手原文）→ 否決。
5. **方向抵銷：** 前段 CT 縮短（Micron 稱 centers of excellence「quicker cycle times」）抵銷後段 HBM CT 增加，使加權 CT 持平 → 不否決但標方向分歧。
6. **主體錯置：** 落差主要落於 SK hynix／Samsung（非美股）而美股對應僅 Micron → 標表達約束（§7-4 三題），不在生成階段否決。

## 6. 測一入口

依 §5 (1)–(6) 逐條實讀；SEC 一律 `tools/sec.py`；`[D]` WIP 天數序列 ≥ 8 季並列算式；12 個月內檢驗事件：Micron 1Q27／2Q27 10-Q、SK hynix 4Q26 法說、HBM4E 量產。
