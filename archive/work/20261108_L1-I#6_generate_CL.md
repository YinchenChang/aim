# L1-I#6 生成卡｜能源與電力：誘因（既有機組業主之「申報停役」選項——停役通知換取 RMR 成本服務費或 DOE 202(c) 成本回收；公開之「退役風險 MW」高估實際退出，容量稀缺之供給側被誤讀）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260926_L1-I_generate_GK.md；archive/work/20261009_L1-I#2_generate_CL.md；archive/work/20261016_L1-I#3_generate_CL.md；archive/work/20261024_L1-I#4_generate_CL.md；archive/work/20261031_L1-I#5_generate_CL.md；work/20261031_L1-I#5_test1_CL.md；archive/work/20261105_L1-A#6_generate_CL.md | EMITS: work/20261108_L1-I#6_generate_CL.md -->
**日期：** 2026-11-08　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1→2／6）　**格：** L1-I　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L12-P#6 已於本日測一）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-31（L1-I#5、L3-P#5、L3-A#5、L3-I#5、L4-P#5、L4-A#5；各測一檔 git 新增時間同為 2026-11-05T19:17:39Z，不能再分）→ 依表序取 **L1-I**（L1-P＝刻意排除 T-11 不取）；既有生成 5 份 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `deactivation`／`RMR`／`retirement`／`202(c)`，命中 0 筆。內部數字（§12）：未取用。
- 比對（本卡須異型）：
  - **L1-I#1**（GK）：**新進**開發商佇列佔位 → 公開佇列高估新增供給。本卡選擇者＝**既有機組業主**，標的＝**退出**側之公開數字（停役通知），誘因＝留用補償，非佔位成本。
  - **L1-I#2**：受管電業費率基誘因、最低需量覆蓋率。本卡 RMR／202(c) 費用由費率人承擔一節**不作落差**（屬 #2 型轉嫁）；落差只在供給側 MW 之讀法。
  - **L1-I#3**（Scope 2 屬性溢價）、**L1-I#4**（表後淨額）、**L1-I#5**（負載韌性 vs 可中斷，需求側容量定義）：皆需求側或屬性；本卡為**供給側退出**。
  - **L1-A#6**（GEV 保位預付之營運資金）、**L1-A#1–#5**：會計恆等型，主體為設備商／PPA。不同。
  - **T-11**（電網容量／機組交期，物理供給不足）：本卡不以「新機組交期」為機制；測一若落差只能以交期表述 → 否決 (6)。
  - ARCH_dead：C-I3′／N-02（利益未分列）——測一 (1) 為同類可分離性題；主體不同，非已殺同型。全表無退役／RMR 型死因（`grep` work／archive 無同型生成卡）。
- §7-10 領域最近公開：FERC 2026-08 核准 Brandon Shores／Wagner RMR 延長兩年（Sierra Club 新聞稿 2026-08-28）；DOE 對 J.H. Campbell 第五次 202(c) 延長至 2026-11-14（Michigan Public 2026-08-14）；POWER 202(c) 紀錄（2026-04-02，43 令、≥ 4.4 GW 煤機）；Environment+Energy Leader（2026-06-15，更新 2026-11-06）。下一檢查點＝Campbell 令 2026-11-14 屆期是否再延；PJM 2029/30 BRA（2026-12）之規劃參數與 RMR 處理；TLN 10-Q 3Q26。

## 1. 落差一句

PJM 停役程序下，業主遞停役通知後若 PJM 判定可靠度違規，可要求續運並以 RMR 成本服務費補償（Brandon Shores 1.3 GW 煤、Wagner 774 MW 油；首份 RMR 每年約 $180M 固定費至 2029-05，延長案至 2031-05〔E+E Leader〕）；DOE 另以 FPA 202(c) 令強制續運（≥ 43 令、≥ 4.4 GW 煤機〔POWER〕；Campbell 第五次延長，費用約 $180M 至 2026-03 由客戶承擔〔Michigan Public／密州 AG〕）。故**停役通知是帶留用選擇權之選項**：在高容量價環境，遞停役取得成本服務保障可能優於留在市場。種子主張：市場與容量稀缺論述把「已申報／風險中退役 MW」讀成確定退出之供給，但其中一部分以 RMR／202(c) 形式留在系統；若留用機組被計為容量供給（PJM 曾就 2026/27、2027/28 BRA 申請計入 RMR 機組，ER25-682，未讀原文），或其 MW 抵減需新建量，則以退役數推出之稀缺租與新建需求被高估；反之若不計入供給而實際運轉，則出清價高於實體稀缺。**錯價方向依計入規則而定**，本卡不定號。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：既有業主之退出選擇 ＝ f（市場淨收入、RMR 成本服務費率、202(c) 成本回收、環保合規成本、可靠度違規判定）；監理（PJM、FERC、DOE）決定留用選項之存在與報酬 |
| 選擇者 | 既有機組業主（IPP、受管電業之發電部門）；PJM（可靠度判定）；DOE（202(c)）；FERC（RMR 費率核准） |
| 已讀事實 | Sierra Club 2026-08-28（FERC 核准 Brandon Shores／Wagner RMR 延長兩年）；E+E Leader 2026-06-15／11-06（1.3 GW＋774 MW；原訂 2025-05 退役；$180M／年至 2029-05；延長至 2031-05；2026/27 BRA $329/MW-day；人民律師 Lapp：「data center growth, almost entirely outside the state」）；Michigan Public 2026-08-14（Campbell 第五次延長至 2026-11-14；客戶負擔約 $180M 至 2026-03）；POWER 2026-04-02（43 令、≥ 4.4 GW）；POWER 2024-01-10（PJM：Wagner 3、4「will be needed to operate under a Reliability-Must-Run」） |
| 未證之連結 | 停役通知 MW 中後續 RMR／202(c)／撤回之比例（PJM 停役清單逐列狀態）；RMR／202(c) 機組於 2028/29 以後 BRA 是否計為供給；業主遞停役之策略性（RMR 報酬 vs 市場淨收入）是否可由申報看出；賣方／ISO 退役預測（如 PJM「Energy Transition in PJM」退役風險 GW）是否已扣留用 |
| 量綱 | 留用 MW ÷ 停役通知 MW（%）；RMR 年費 ÷ 機組 MW（$/MW-day，對照 BRA 出清價）；計入／不計入供給之 VRR 出清價差（$/MW-day） |
| 半衰期 | 年（RMR 期 2–6 年；202(c) 每 90 日；BRA 年度；2029/30 BRA 2026-12） |

## 3. B 端可觀測載體（只指名）

1. PJM 停役清單與通知／撤回函 https://www.pjm.com/planning/services-requests/gen-deactivations （頁未讀；搜尋見通知／撤回 PDF，如 zion-ct1-ct2-ct3-withdrawal.pdf、rockford-withdrawal.pdf、forked-river-unit-2-deactivation-notice.pdf）；TEAC 停役更新 https://www.pjm.com/-/media/DotCom/committees-groups/committees/teac/2025/20250506/20250506-item-02---generation-deactivation-notification-update.pdf （未讀）
2. RMR：https://www.sierraclub.org/maryland/blog/2026/08/press-release-ferc-approves-brandon-shores-and-wagner-plant-s-rmr-extension ；https://environmentenergyleader.com/stories/maryland-coal-plant-extension-to-2031-tied-to-data-center-load,129806 ；https://www.powermag.com/pjm-urges-delayed-retirement-of-840-mw-fossil-fuel-power-plant-citing-reliability-impacts/ （已讀）；FERC 令原文（未讀）
3. 202(c)：https://www.powermag.com/doe-has-issued-more-than-40-section-202c-emergency-orders-since-may-2025-heres-an-updated-log ；https://www.michiganpublic.org/politics-government/2026-08-15/michigan-coal-power-plant-set-to-close-more-than-a-year-ago-is-again-ordered-to-keep-running （已讀）；DOE 202(c) 令原文（未讀）
4. RMR 是否計入 BRA：PJM ER25-682 FERC 令 https://www.pjm.com/pjmfiles/directory/etariff/FercOrders/8045/20250214-er25-682-000.pdf ；PJM 拒絕將 RMR 納入未來拍賣之報導 https://www.power-eng.com/business/policy-and-regulation/pjm-rejects-calls-to-include-reliability-must-run-resources-in-future-capacity-auctions/ ；Maryland OPC 致 PJM 董事會函（2024-08-30）（皆未讀）
5. 未讀：TLN 10-Q 3Q26／10-K FY25（sec.py）之 RMR 收入與停役政策；VST／NRG／CEG 10-Q 之停役與 202(c) 段；CMS（Consumers）10-Q 之 Campbell 成本回收；MISO／SPP／ERCOT 同型程序（MISO Attachment Y SSR）；具名賣方或 IMM（Monitoring Analytics）是否量化留用 MW 對出清價。

## 4. 不寫

H1／H5、表達工具選擇、方向判斷。

## 5. 否決觸發（測一逐條實讀）

1. **可分離性：** PJM 停役清單、IMM 報告或上市業主申報均無法給出「停役通知 MW 中留用（RMR／202(c)／撤回）MW」之量化 → 否決（C-I3′／N-02 型）。
2. **誘因不存在或不重要：** `[D]` 留用 MW ÷ 近 3 年停役通知 MW < 10%，或留用 MW ÷ 同期 PJM 可靠度需求 < 0.5% → 否決（門檻本卡凍結）。
3. **已被定價／已揭露：** 具名賣方、IMM 或 PJM 規劃參數已就 RMR／202(c) 留用 MW 量化對 BRA 出清價或新建需求之影響 → 否決（無錯價）。
4. **規則中性：** RMR／202(c) 機組在現行與下一 BRA 之處理已使退役讀法與實體一致（計入供給且退役預測已扣除，或不計入且不運轉）→ 否決。
5. **窗不足：** 未來 12 個月內無 RMR 到期／延長、202(c) 屆期、BRA 規則變動之檢驗事件 → 否決（重定價窗 < 12 個月或不存在）。
6. **主體錯置：** 落差只能以新機組交期（T-11）、費率人成本轉嫁（L1-I#2 型）或需求側容量定義（L1-I#5 型）表述 → 否決本卡、不得改寫為他卡。
7. **方向不定：** 計入／不計入之兩向效果無法由一手規則定號 → 不否決但標方向不定，不得合併為同向落差。
