# L14-P#4 生成卡｜企業終端需求：守恆（企業端點裝機量之存量—流量守恆：`IB_{t+1} = IB_t + S_t − R_t`，裝機量 IB 受員工數約束近乎固定時，替換出貨之跨期總和 ≈ IB × T ÷ L——AI 驅動之記憶體成本上升所壓下之出貨，若平均壽命 L 不永久延長，即以「機齡」形式累積為遞延替換存量 D_t，而非消失之需求）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；query/INDEX.json；archive/drive/USED_20261005_L14-P_generate_GK.md；archive/drive/USED_20261005_L14-P_test1_GK.md；archive/work/20261013_L14-P#2_generate_CL.md；work/20261013_L14-P#2_test1_CL.md；archive/work/20261020_L14-P#3_generate_CL.md；work/20261020_L14-P#3_test1_CL.md | EMITS: work/20261028_L14-P#4_generate_CL.md -->
**日期：** 2026-10-28　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 4→5／6）　**格：** L14-P　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L13-I#4 本日測一，Q-0120 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-20（L14-P#3）；L14-A／L14-I／L15-P／L15-A＝10-21、L15-I＝10-22，其餘格 #4 皆 ≥ 10-23 → **L14-P**。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：本輪未查（格已定；載體以 SEC 與調查機構原報導直讀）。命中 0。
- 比對之舊檔與死因型態，本卡須異型：
  - **L14-P#1**（席次 ≤ 員工數；死因＝同一 10-K 付費席次水準與期末員工數不可並列）：本卡之 IB 雖以員工數為錨，但守恆量是**實體裝置之跨期替換流量**（存量—流量—壽命），樞紐是壽命 L 之彈性與遞延存量 D，不是單期上界。
  - **L14-P#2**（預付容量承諾池；死因＝滾存條款不可得）：不涉承諾池、RPO、credit。
  - **L14-P#3**（客服人工處理量 H ≡ V(1−a)）：不涉互動量或 AI 自助率；本卡之 AI 只作外生成本衝擊（記憶體價格），不作替代人工之機制。
  - **L14-A**（IT 支出比重）、**L14-A#2／#3**、**L14-I**／**#2／#3**（採購誘因、裁員歸因）：本卡不以支出比重、會計分流或揭露誘因為樞紐。
  - **C-A2**（ARCH_dead，企業預算單位經濟）：不主張每單位毛利。
  - **L5-*／L3-***（記憶體／半導體供給層）：本卡不主張記憶體價格方向；記憶體價格只作 B 端外生輸入，守恆發生在需求端裝機量。
  - **L11-P／L8-P／L9-P**（已殺）：不涉。
- §7-10 領域最近公開：HP 10-Q 期末 2026-07-31（FY26 Q3）；HP 8-K／SEC 申報 2026-09-21（2027 出貨假設）；IDC 3Q26 初估 2026-10-09。下一檢查點＝HP FY26 10-K（約 2026-12）、IDC／Gartner 4Q26 初估（約 2027-01）。

## 1. 落差一句

市場（HP、Omdia、IDC 之 2026–2027 口徑）把記憶體成本推高下之 PC 出貨下滑讀成**需求流失**（HP 規劃 2027 產業出貨「mid-single digits」下滑；Omdia 2027 −7%），同時把 ASP 上升讀成營收韌性；種子主張企業端點為受員工數約束之近固定裝機量 IB，跨期替換總和由 `Σ S ≈ IB × T ÷ L` 鎖定：若 L 之延長是成本驅動之暫時延後而非永久結構，被壓下之出貨以機齡形式累積為遞延替換存量 `D_t = Σ (IB/L₀ − S_t)`，於記憶體成本回落時回補；若 L 永久延長（Gartner：企業 PC 平均壽命約 +15%），則出貨為永久下移、本卡之「遞延」主張死。可拒絕之主張＝成本衝擊期間 D_t 為正且在 ≥ 12 個月窗內以出貨回補之形式釋放；若企業平均機齡未升（出貨下滑全為通路去庫存）、或壽命延長被證為永久，本卡死。本卡不主張任何公司營收或股價方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆（P）**：`IB_{t+1} = IB_t + S_t − R_t`；穩態 `R ≈ IB/L`；`D_t ≡ Σ_{τ≤t}(IB/L₀ − S_τ)`；機齡 `Ā_t` 隨 D_t 上升。另：出貨 S＝終端銷售 − Δ通路庫存（IDC 歸因 3Q26 下滑於上半年囤貨，須先剝離） |
| 選擇者 | 企業買方（替換時點、壽命政策）；OEM／通路（庫存） |
| 可見端 | HP 10-Q 之 Commercial PS 營收、ASP 與單位量變動百分比（MD&A）；IDC／Gartner／Omdia 季出貨與年預測；Gartner 壽命延長百分比；OEM 對 Windows 換機之敘述 |
| 指名不可見端 | 企業裝機量 IB 與平均機齡 Ā 之逐期值；終端銷售（sell-out）vs 出貨（sell-in）；企業壽命政策之可逆性 |
| 量綱 | 台、台／季、年（L、Ā）、無因次比例（ASP、單位量年比） |
| 外部參照物（測一查證） | 2011–2012 泰國洪水 HDD 漲價後之 PC 出貨與回補；2020–2022 疫情前拉與 2023 低谷（「被拉前之出貨」是否於後期以負值出現——守恆之反向案例） |
| 表達工具型態（只指名，不選券） | 美股 PC OEM 普通股、記憶體上游（只作對照，非主體）；不選券 |
| 重疊 | L14-P#1（員工數錨）、L5（記憶體供給）；重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. HP 10-Q FY26 Q3（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/0000047217/000004721726000051/hpq-20260731.htm ：Net revenue「Commercial PS $ 8,579 $ 7,036 $ 23,575 $ 20,467」（百萬美元；三個月／九個月，2026 vs 2025）；「The net revenue increase was primarily due to a 19.8% increase in ASPs, partially offset by a 4.2% decrease in PC unit volume. The decrease in PC unit volume was driven by an increasing commodity cost environment, partially offset by the Windows-based PC operating system refresh.」；「Commercial PS net revenue increased 15.2% primarily due to a 20.2% increase in ASPs, partially offset by a 3.7% decrease in PC unit volume」；「we experienced higher inflationary pressure in memory and storage costs and supply constraints in our Personal Systems business, which we anticipate will continue」。
2. Dow Jones via iTiger（HP 2026-09-21 SEC 申報）https://www.itiger.com/news/2669157775 ：「HP said it is planning for industry-wide personal computer unit volumes to fall by roughly mid-single digits next year」；「preliminary assumption is for a decline in PC unit sales in calendar year 2027」（轉述，測一須以 sec.py 取原申報）。
3. The Register（2026-10-09，IDC 3Q26 初估）https://www.theregister.com/a/5302264 ：出貨 −20.1% 至 62.7M 台；IDC Jitesh Ubrani「What we're seeing is the result of the strong first half pull-in」「Vendors and channels loaded up on inventory early in the year to get ahead of price hikes」；2027 −7% 歸 Omdia。無商用／消費分項、無機齡。
4. ChannelWeb（Gartner，Ranjit Atwal）https://www.channelweb.co.uk/news/2026/gartner-warns-memory-crunch-will-slash-pc-shipments-as-vendors-raise-prices ：2026 出貨 −10.4%；DRAM＋SSD「could rise around 130 per cent by the end of this year」；「average PC lifespan will increase by about 15 per cent for enterprise buyers and 20 per cent for consumers」（文中無發布日期，測一須取 Gartner 原新聞稿）。
5. 待讀：Dell 10-Q（CSG Commercial 營收與單位敘述）；Lenovo 業績公告（IDG）；Microsoft 10-Q 之 Windows OEM／Commercial 敘述；IDC／Gartner 原新聞稿之商用分項；任何機齡或裝機量調查（Gartner／IDC／Omdia、端點管理商遙測）。

缺段（§7-2）：IB 與 Ā 之逐期序列；sell-out 與 sell-in 之分離；壽命延長之可逆性證據。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 企業 PC 平均壽命約 +15%——壽命延長即永久吸收，D 不回補 | #4 Gartner Atwal | 守恆成立但 L 內生上移，遞延存量為零 |
| R2 | 3Q26 下滑為上半年囤貨之通路去化，非終端延後 | #3 IDC Ubrani | Δ通路庫存解釋，D 未必形成 |
| R3 | Windows 10 終止支援（2025-10）已把替換前拉至 2025–1H26，2027 低谷為前拉之反面，非遞延 | #1 HP「Windows-based PC operating system refresh」 | 守恆方向相反：D 為負（已預支） |
| R4 | HP／Omdia 已公開 2027 下滑假設，市場已讀入量之下移 | #2、#3 | 已定價（量端） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 無法就 ≥ 2 家 OEM 或 ≥ 1 家調查機構取得 ≥ 4 期同口徑之商用（企業）單位量或可重算之等價量（營收 ÷ ASP 變動、出貨分項）；或企業機齡／裝機量無任何具名公開數值（≥ 2 個時點），使 D 之正負不可 `[D]` 重算。
(2) 前拉（R3：Windows 10 終止支援）與囤貨（R2）合計之量 ≥ 成本衝擊期間之出貨缺口，使 D ≤ 0（以 `[D]` 粗算：2025–1H26 超額出貨 vs 2H26–2027 缺口；門檻＝D 為正須 ≥ 商用年出貨之 5%，本卡凍結）。
(3) 公司或具名賣方已就「出貨缺口 ＝ 永久壽命延長 ＋ 遞延回補」量化分解並給回補時點（已定價）。
(4) 壽命延長有具名證據顯示為永久（企業政策改寫、租賃／DaaS 合約年期延長、Gartner 原稿明言結構性），或回補時點落在 > 剩餘實驗期。
(5) 可運作對照只能寫成席次 ≤ 員工數（L14-P#1）、承諾池（L14-P#2）、人工處理量（L14-P#3）、IT 支出比重（L14-A）、單位經濟（C-A2）或記憶體供給價格方向（L5 型）。
(6) 重定價窗（≥ 12 個月）內無檢驗事件（OEM 10-Q／10-K、IDC／Gartner 季出貨、記憶體合約價公告）。

複查觸發器（若日後殺）：任一 OEM 或調查機構首次公布企業平均機齡或裝機量序列；OEM 申報首次分列 sell-out 與 sell-in；Gartner／IDC 撤回或改寫壽命延長假設；記憶體合約價連續兩季回落而商用出貨年比轉正。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：OEM 商用 PC 營收、ASP 與單位量變動、通路庫存、遞延收入（服務）；記憶體成本敘述。
2. 可交易工具：PC OEM 普通股；不選券。
3. 半衰期：季度 10-Q；調查機構季初估。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0121；`query/ARCH_matrix.md` L14［P］標「#4 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live、export/LEADS（本輪實讀事實屬 PC 終端，非算力收支範圍）。不改 L14-P#1–#3、L14-A／#2／#3、L14-I／#2／#3、C-A2 結論；不恢復 L11-P／L8-P／L9-P；不寫 T。
