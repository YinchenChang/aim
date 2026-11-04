# L13-P#5 生成卡｜資本與融資結構：守恆（信用市場出清守恆：每一元超大雲公司債券發行必被某持有者買下——超大雲淨發行 ≡ Σ_h 持有者淨買入；指數中性需求（指數權重 × 基準型資金淨流入）之外之剩餘，只能以新發讓價／利差擴大吸引非基準型邊際買家，或溢出至非美元、私募信貸與表外結構）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261002_L13-P_generate_GK.md；archive/work/20261013_L13-P#2_generate_CL.md；archive/work/20261020_L13-P#3_generate_CL.md；work/20261020_L13-P#3_test1_CL.md；archive/work/20261028_L13-P#4_generate_CL.md；work/20261028_L13-P#4_test1_CL.md | EMITS: work/20261104_L13-P#5_generate_CL.md -->
**日期：** 2026-11-04　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 1→2／6）　**格：** L13-P　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L11-I#5 測一 2026-11-03，Q-0159 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-28（L13-P、L13-I、L14-P、L14-A、L14-I）；依表序取 **L13-P**。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `tokenomics_leads.py bond issuance spread`＝0 筆；未用。載體全由本輪 sec.py／WebSearch／WebFetch 實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L13-P#1**（GPU 熱循環計數 vs 會計年限；死因＝現場計數無申報）：不涉硬體壽命。
  - **L13-P#2**（礦企站址 MW 挖礦／HPC 互斥＋子公司掃款；死因＝雙計一側無可觀測量）：不涉單一發行人站址。
  - **L13-P#3**（超大雲**發行人自身**來源＝用途按季封閉；死因＝表外量級 ≥ 表內外部融資、僅總額揭露）：#3 問「缺口由哪種融資填」；本卡問「已選定之債券融資由**誰買、以何價出清**」——守恆量為**持有者側之吸收容量**，加總維度為持有者類別，不是發行人現金流量表各列。表外結構在本卡為溢出項（否決 (6)），不是封閉式主體。
  - **L13-P#4**（單一對手方 OpenAI 現金跨供應商封閉；死因＝不等式不綁定、對手方已公開融資計畫）：#4 在需求方預算；本卡在**信用市場出清**，與任何單一客戶無關。
  - **L13-A#1–#5**（租賃／預付／EPS 分母等會計恆等）、**L13-I#1–#4**（信評資訊含量、擔保等誘因型）：本卡不以評等或會計認列為樞紐；評等型對照列為否決 (5) 之崩塌方向。
  - **C-A4／C-A3**（ARCH_dead #4–5，重定價窗／折舊樞紐）：不涉；不重開。**T-15**（CoreWeave，委託資本外）：不涉、不用為載體。
- §7-10 領域最近公開：Meta 10-Q 期末 2026-09-30（2026-10-22 申報）；Reuters／LSEG 分析 2026-07-29；Vanguard／Bloomberg 資料至 2026-07-31（ai-cio 2026-09-24）；Bloomberg／ICE 指數權重至 2026-08（ai-cio 2026-10-01）。Fed Z.1 2Q26 版、NAIC 持有統計之最新日期留給測一確認。

## 1. 落差一句

超大雲公司債券發行占美國 IG 供給由 2023–24 年約 2% 升至 2026 年迄 7 月底約 11%（Vanguard 依 Bloomberg 資料；圖表年份對應為推定）；Goldman 預估五家 2026 約 $250B、2027 約 $400B；同期新發讓價中位數由 2025 之 2.25 bp 升至 2026 之 12 bp、Apollo 稱認購倍數由 2 月近 5 倍降至 7 月 < 2 倍（Reuters／LSEG）。種子主張：債券市場守恆——超大雲淨發行 ≡ Σ_h 持有者淨買入；基準型持有者（指數基金／ETF、基準化之壽險與退休金）只按指數權重 w 吸收其淨流入，故**指數中性吸收量** ≈ w × 基準型資金淨流入；超出部分必由非基準型邊際買家以價格（讓價、利差）吸收，或溢出至非美元債、私募信貸與表外 JV。若股市以發行人現金流（#3）讀取融資而不讀出清之剩餘，則邊際債務成本與融資組合之轉向（債 → 普通股／強制可轉／表外）被延遲辨識。本卡不主張方向與量級，只立可拒絕之「持有者側吸收容量可按季量化，且與超大雲淨發行可並列」。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆（P）**：市場出清之存量封閉。ΔD_hyp,t ≡ Σ_h ΔH_h,t；指數中性部分 N_t ≈ w_t × Σ_{h∈基準型} Flow_h,t；剩餘 R_t ＝ ΔD_hyp,t − N_t 須由非基準型買家吸收，價格 s_t（讓價、利差）為其出清變數 |
| 驅動（因果層，§7-5） | 超大雲 capex 與 OCF 之差（發行量之上游）、基準型資金淨流入（IG 基金／ETF、壽險保費、退休金去風險）、持有者之單一發行人／產業集中度上限；發行人端只控制量與幣別，不控制吸收 |
| 量綱 | 發行與持有［美元／季］；指數權重 w［比率］；讓價與利差［bp］；認購倍數［倍］ |
| 可見端 | 發行額（LSEG／Bloomberg／發行人 8-K 與 10-Q 債務附註）；Bloomberg US Corporate、ICE 指數之科技權重；新發讓價、認購倍數、次級利差（報導）；IG 基金／ETF 流量（ICI、EPFR 報導） |
| 指名不可見端 | 單一發行案之持有者分配（簿記資料不公開）；壽險與退休金之內部集中度上限；私募信貸／JV 承接量之即時數 |
| 外部參照物（測一查證） | 單一產業大量發債超出指數中性吸收而致該產業利差相對擴大之具名前例（如 1999–2001 電信發債潮、2010 年代能源 HY 占比上升） |
| 表達工具型態（只指名，不選券） | 美股上市超大雲普通股（融資組合轉向之股數／利息費用讀數）；債券本身不在可交易範圍（§2-8）；不選券 |
| 重疊 | L13-P#3（發行人封閉式）、L13-I 系列（評等）、L6 系列（雲端 capex）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Meta 10-Q 期末 2026-09-30（sec.py）https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm ：「As of September 30, 2026, we had $84.00 billion aggregate principal amount of Notes outstanding, of which $2.75 billion matures in August 2027, with the remainder maturing through 2066」；「future interest payments obligations as of September 30, 2026 were $4.40 billion and $84.51 billion」。一手；發行人存量端。
2. Reuters（經 WHBL，2026-07-29）https://whbl.com/2026/07/29/hyperscaler-debt-binge-pushes-yields-up-as-investor-demand-cools/ ：Amazon、Alphabet、Meta、Oracle 2026 迄 7-07 發債約 $194B（2025 全年約 $108B，LSEG）；Goldman：五家 2026 約 $250B、2027 約 $400B，capex 約 $750B vs OCF 約 $778B；讓價中位數 12 bp（2025：2.25 bp）；91 檔中 78 檔 7-28 殖利率高於發行；Apollo：認購倍數「from nearly five times in February to below two times in July」；Goldman：市場飽和與發行人集中度「likely to become more binding constraints」。二手（通訊社）。
3. ai-cio（2026-09-24，引 Vanguard「The AI Buildout Comes to the Bond Market」2026-08-19）https://www.ai-cio.com/news/by-the-numbers-how-ai-related-debt-is-changing-the-bond-market/ ：超大雲發債占美國 IG 供給逐年（2026 YTD 約 11%，圖表文字錯亂、年份對應推定）。二手；測一取 Vanguard 原文。
4. ai-cio（2026-10-01）https://www.ai-cio.com/news/ai-debt-issuance-taking-up-more-room-in-bond-indexes/ ：Bloomberg 之 Gendron：科技為 $7.5T Bloomberg U.S. Corporate Index 過去 18 個月成長最大產業，至 8 月淨流通量 $891B（+27.5%）；Amazon 占指數市值 1.4%、Oracle 1.3%；ICE 之 Peacock：科技約占 ICE BofA Global Corporate & HY Index 4.5%。文內科技市值 $805B 與 $1.65T 兩數互相矛盾，測一不得採用未調和之數。
5. 缺段（§7-2；測一取）：Fed Z.1 L.213（公司債持有者分部，季）；NAIC 壽險持有產業分布；ICI／EPFR IG 基金與 ETF 流量；非美元（EUR／GBP）超大雲發行額；私募信貸／JV（如 Meta Hyperion）承接額之一手來源。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 科技仍只占指數小份額，「far from levels that are going to make people fundamentally change how they look at corporate bond market investing」（ICE，Peacock） | #4 | 不綁定 |
| R2 | 吸收以 10–20 bp 之讓價完成，相對 capex 量級之利息成本不重要；發行人基本面「the best they've seen in their careers」（Vanguard，Venter） | #2、#4 | 機制成立但不可捕捉 |
| R3 | Goldman 已明言飽和與集中度約束將更綁定；市場已知 | #2 | 已定價 |
| R4 | 溢出至歐元債、私募信貸與 JV 結構，USD IG 守恆有洩漏 | #4（Amazon 美元／歐元分拆） | 封閉式不閉 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後持有者側分解（Z.1 持有者分部、基準型資金流量、壽險持有）無 **≥ 2 個**獨立來源達季頻，使 N_t 不可量化、R_t 不可與淨發行並列（L13-P#3 型「只有總額」死因）。
(2) 窗內 `[D]` 超大雲淨發行 ÷ 指數中性吸收量 N_t 之區間上端 ≤ 1（剩餘不存在）——不綁定（R1）。
(3) 具名賣方、評等機構或指數商已**量化**超大雲發行之持有者吸收容量或剩餘（不止定性「飽和」語）——已定價（R3）。
(4) 重定價窗（≥ 12 個月）內無可觀測檢驗事件（季度 Z.1、發行人季報債務附註、2027 發行計畫揭露），或其已全部於窗前公告。
(5) `[D]` 讓價／利差擴大之增量利息 ÷ 發行人 OCF < 1%，使剩餘對股權讀數無可分離影響；可運作對照崩塌為 L13-P#3 型發行人封閉式或評等型（R2）。
(6) 非美元債、私募信貸與表外 JV 合計承接超大雲 2026 債務融資 ≥ 30%，USD IG 出清封閉式洩漏（R4）。

複查觸發器（若日後殺）：Z.1 或 NAIC 首次顯示基準型持有者科技集中度觸及上限；超大雲讓價中位數 ≥ 25 bp 持續兩季；發行人首次於 10-Q 揭露以普通股或強制可轉取代計畫中之債券發行。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：長期債務附註（本金、到期、利率）、利息費用、股數、表外承諾。
2. 可交易工具：超大雲普通股；債券不在範圍。不選券。
3. 半衰期：發行按月；Z.1 按季；指數權重按月重平衡。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0160；`query/ARCH_matrix.md` L13［P］標「#5 已生成」。不寫入：FUNNEL、INDEX.json、ARCH_dead、RETRIG、ARCH_live、LEADS（本輪實讀事實屬債務融資，非 §12 列舉之算力投入／收入／硬體／雲端合約／資料中心；不寫）。不改 L13-P#1–#4、L13-A#1–#5、L13-I#1–#4、C-A3／C-A4 結論；不寫 T-15。
