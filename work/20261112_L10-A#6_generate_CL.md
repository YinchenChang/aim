# L10-A#6 生成卡｜分發與中介：會計恆等（平台自由現金流定義之邊界：FCF ≡ OCF − 購置 PP&E；自駕車隊資本經非市場股權、貸款應收、融資租賃與 ROU 等不入 FCF 定義之列流出，FCF 讀數與經濟資本支出之差 Δ ≡ E_eq + E_loan + E_lease + E_ROU 隨自駕部署放大）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；AIM_FUNNEL.md；query/ARCH_live.md；archive/drive/USED_20261001_L10-A_generate_GK.md；archive/work/20261013_L10-A#2_generate_CL.md；archive/work/20261020_L10-A#3_generate_CL.md；archive/work/20261027_L10-A#4_generate_CL.md；archive/work/20261103_L10-A#5_generate_CL.md | EMITS: work/20261112_L10-A#6_generate_CL.md -->
**日期：** 2026-11-12　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 0→1／6）　**格：** L10-A　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（Q-0195 done）。非已殺／刻意排除格中最後測試日最舊＝2026-11-03（L10-A#5、L10-I#5、L11-A#5、L11-I#5、L13-A#5）；依表序取 **L10-A**。既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py Uber autonomous fleet`，命中 0。載體全由本輪 sec.py／WebSearch／WebFetch 實讀。內部數字（§12）未取。§12 線索輸出：寫 1 筆（Uber 雲端最低支出承諾，10-Q 一手）。
- 比對之舊檔與死因型態，本卡須異型：
  - **L10-A#1**（不通過）：付款方 TAC 量 × 率。本卡不涉分潤。
  - **L10-A#2**（部分通過）：商戶預收浮存（OCF 內之時序）。本卡在 **OCF 之外**：資本流出之列報位置使其不入 FCF 定義；不論 OCF 內任何營運資金項。
  - **L10-A#3**（不通過）：主事人／代理人列報（損益表收入口徑）。本卡為現金流量表分類，不論營收。
  - **L10-A#4**（不通過）：自保準備精算估計。本卡不涉估計；Uber 保險準備之 ΔR 浮存不得作本卡證據。
  - **L10-A#5**（不通過）：收款方毛利組合。本卡不涉毛利。
  - **L10-P#3**（部分通過）：自駕車隊容量守恆（行程上界）。本卡不主張行程或容量，只主張資本流出之列報位置；若實讀後只剩「部署車數 × 單車行程」即滑回 L10-P#3（否決 (4)）。
  - **L13-A#1**（T 已寫）：入表租賃 ≠ 義務上界（未開始租／RVG／JV）＝**表外義務存量**。本卡不主張表外義務，主張**已發生之現金流出**落於 FCF 定義之外；若可拒絕之主張只剩「或有 offtake 承諾未入表」即 L13-A#1 型（否決 (4)）。
  - **L13-A#2**：客戶預付入 OCF。異型（本卡不涉 OCF 內項）。
  - **L2-A#4**（租期末殘值）、**L6-A#6**（GPU 減損）：本卡不以車輛殘值或減損為落差；CEO 雖稱殘值未建立，測一不得以殘值估計作為主張。
  - **L7-A#2**（持股方公允價值）：本卡不論 Lucid／Aurora 等持股之公允價值損益，只論取得持股之現金流出。
  - L11-P（死 #3）不恢復；C-A5 不重開；不寫 T-15。
- §7-10 領域最近公開：Uber 10-Q 期 2026-09-30（2026-11-04 申報）；Uber Q3 2026 法說逐字稿（2026-11-04）。下一檢查點＝Uber 10-K FY2026（約 2027-02）、Q4 2026 法說、公司預告之「infrastructure financing」與「vehicle financing」公告。

## 1. 落差一句

恆等骨架：公司定義 `FCF ≡ OCF − Capex_PP&E`；經濟資本流出 `K ≡ Capex_PP&E + E_eq（非市場股權）+ E_loan（貸款應收）+ E_lease（融資租賃本金，入籌資）+ E_ROU（非現金取得之 ROU）`；`Δ ≡ K − Capex_PP&E`。9M26 vs 9M25（百萬美元，10-Q）：FCF 7,613／6,955；Capex 239／261；非市場股權 805／286；貸款應收 327／78；融資租賃本金 124／112；非現金 ROU 679／100。`[D]`（未歸因於自駕，上界）：(E_eq＋E_loan)÷FCF＝14.9%（9M26）vs 5.2%（9M25）；連 ROU 計 23.8% vs 6.7%。公司稱自駕承諾約 $10B（法說），早期車輛「on our balance sheet」，長期由第三方資本融資；未決定之融資結構決定流出落在 Capex（入 FCF）或他列（不入）。市場若以 FCF（含其回購能力）讀自駕轉型之資本密度，則錯價在於 **FCF 定義之邊界**而非 FCF 之數值。**不主張方向或時點，不寫 H1。**

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（現金流量表分類 × 非 GAAP FCF 定義邊界） |
| 量綱 | OCF、Capex、E_eq、E_loan、E_lease、E_ROU、Δ［美元／期］；Δ÷FCF［無量綱］ |
| 選擇者 | 公司之融資結構（自持購車入 Capex、經 VIE／車隊營運商之股權或貸款、融資租賃、第三方 SPV）；AV 夥伴之里程碑（承諾或有） |
| 可見端 | 10-Q 現金流量表各列；Note 12 VIE（未合併 VIE「primarily vehicle fleet operators」、最大損失暴露）；MD&A FCF 調節；法說 CFO／CEO 融資說明 |
| 指名不可見端 | 各列中自駕歸屬之占比；或有 offtake 承諾之額與時程；車隊 SPV 結構 |
| 主張 | Δ 之自駕歸屬部分於窗內 ≥ 門檻且市場未以 Δ 調整 FCF；可由「公司或賣方已以含 Δ 口徑呈現」或「Δ 歸屬小」或「流出改入 Capex」拒絕 |
| 外部參照物（測一查證） | 前例：平台轉重資產時賣方改用「FCF after investments／leases」口徑之具名先例（如 Amazon「FCF less principal repayments of finance leases」自揭口徑） |
| 表達工具型態（只指名，不選券） | 美股上市之乘車／外送分發平台普通股。不選券 |
| 重疊 | L10-P#3、L13-A#1、L7-A#2。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Uber 10-Q 期 2026-09-30（sec.py）https://www.sec.gov/Archives/edgar/data/1543151/000154315126000041/uber-20260930.htm ：現金流量表「Purchases of non-marketable equity securities (286) (805)」「Purchases of loan and notes receivable (78) (327)」「Principal payments on finance leases (112) (124)」「Right-of-use assets obtained in exchange for lease obligations 100 679」；FCF 調節「Net cash provided by operating activities $ 7,216 $ 7,852 … Purchases of property and equipment (261) (239) Free cash flow $ 6,955 $ 7,613」；承諾節「capital funding commitments and vehicle offtake commitments with various partners contingent upon the achievement of specified technical and operational milestones. We anticipate that part of these offtake commitments will transition to third-party financing structures over time.」；Note 12「Our unconsolidated VIEs consist of investments in privately held companies, primarily vehicle fleet operators」，總資產 1,329→1,176、最大損失暴露 1,509→1,260（含 Moove 定期貸款 384→449）；風險因素「we may need to incur additional debt to finance the purchase of autonomous vehicles or infrastructure to support autonomous vehicles」；PP&E 淨額 1,897→1,816。
2. Uber Q3 2026 法說逐字稿（2026-11-04）https://s23.q4cdn.com/407969754/files/doc_events/2026/Nov/04/Uber-Q3-Earnings-Call-Transcript.pdf ：Khosrowshahi「in the early days, we're going to take these vehicles on our balance sheet.」「the residual value of AV vehicles isn't established yet」「a $10 billion commitment based on certain deliverables」；Krishnamurthy「our long-run expectation is that this should be financed by third-party capital, not by Uber's balance sheet.」「we will have announcements to make both on infrastructure financing, but also on vehicle financing」；「approximately 700 fully driverless vehicles on Uber by year-end and more than 2,000 by the end of 2027」；Goldman（Sheridan）問「the balance sheet and incremental free cash flows」。
3. Dolphin Research（長橋，2026-08-05）https://longportapp.cn/news/294974721 ：「The $10bn AV commitment spans multiple years」；分兩桶「equity investments in AV software partners with milestones」與「selective balance sheet use for ground AV infrastructure, including fleet ops, real estate, and OEM take-or-pay commitments」；120k 車多年採購（二手轉述法說）。
4. MarketBeat（Chris Markoch，約 2026-06，日期未載）https://www.marketbeat.com/originals/ubers-av-pivot-growth-opportunity-or-margin-risk/ ：「signaling a major shift away from its asset-light model」；Stifel、Wells Fargo 調降目標價（未見口徑）。
5. Newsquawk 轉述 FT（2026-04-15）https://www.newsquawk.com/headlines/uber-uber-has-committed-more-than-usd-10bln-to-buying-thousands-of-autonomous-vehicles-and-taking-stakes-in-their-developers-according-to-ft ：「committed more than USD 10bln to buying thousands of autonomous vehicles and taking stakes in their developers」。
6. 測一須另取：Uber 10-K FY2025 承諾附註與 FY2026（若已出）；Note 2 非市場股權逐筆（自駕夥伴歸屬）；ROU 增額之資產性質（充電／車隊站場或辦公）；具名賣方（Goldman、Wolfe、Bernstein 等）FCF 是否扣除投資／租賃；FT 原文；Lyft 10-Q 同口徑對照。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 公司已明說 $10B 承諾與早期自持，市場已知 | #2、#5 | 已定價 |
| R2 | 9M26 之股權／貸款／ROU 增量主要屬 Delivery Hero、Moove 等非自駕項，自駕歸屬小 | #1 | Δ 不重大 |
| R3 | 早期自持車將入 Capex（PP&E），即在 FCF 內；長期轉第三方則不在 Uber 任一列 | #2 | 邊界無落差 |
| R4 | 700→2,000 輛之資本「fairly limited」（CFO） | #2 | 窗內量級小 |
| R5 | 本質是表外承諾（L13-A#1）或車隊容量（L10-P#3） | — | 滑入他格 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 公司或具名賣方已公開以含 E_eq／E_loan／E_lease 之口徑呈現 FCF（或「FCF after AV investments」），或明確扣除自駕投資——已定價（R1）。僅目標價調降或定性「資本密集」不觸發本條，但測一須記錄。
(2) `[D]` 自駕歸屬 Δ ÷ TTM FCF（以測一可得最佳歸屬，區間給出）< 10%，且窗內（≥ 12 個月）無可觀測之放大事件（車輛融資公告、首批自持車入表、offtake 里程碑達成）——落差不重大（R2、R4）。門檻 10% 於本卡凍結。
(3) 一手證據顯示自持自駕車購置全數列 Purchases of property and equipment（入 FCF），且第三方融資結構不經 Uber 之股權、貸款或擔保——邊界無落差（R3）。
(4) 實讀後可拒絕之主張只剩「或有承諾未入表」（L13-A#1 型）或「部署車數 × 單車行程」（L10-P#3 型）或持股公允價值（L7-A#2 型）。
(5) 自駕資本流出之主要列為 OCF 內項（如預付車隊營運費），使問題回到 L10-A#2 型時序。

複查觸發器（若日後殺）：Uber 公告車輛或基礎設施融資結構；10-K／10-Q 首次分列自駕投資或自駕 PP&E；具名賣方改 FCF 口徑；未合併 VIE 最大損失暴露跳增。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Purchases of PP&E、非市場股權、貸款應收、融資租賃本金、非現金 ROU；Note 12 VIE；承諾附註。
2. 可交易工具：分發平台普通股。不選券。
3. 半衰期：季度（10-Q）；融資結構公告為事件。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列（Q-0196）；`query/ARCH_matrix.md` L10［A］標「#6 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 1 筆。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L10-A#1–#5、L10-P#1–#6、L10-I#1–#5、L13-A 系列、C-A5 結論；不寫 T-15。
