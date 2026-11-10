# L6-I#6 生成卡｜雲端與基礎設施服務：誘因（供給方兼股東之總報酬誘因：雲供給方同時持有買方實驗室之股權並提供「隨交付里程碑解鎖」之融資額度，其最適化對象為「分部利潤＋持股增值」而非分部利潤——故被投資實驗室之 backlog／營收中有一段由供給方自資，且其單價、配給與條件非公平交易）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260928_L6-I_generate_GK.md；archive/work/20261011_L6-I#2_generate_CL.md；archive/work/20261018_L6-I#3_generate_CL.md；archive/work/20261026_L6-I#4_generate_CL.md；archive/work/20261102_L6-I#5_generate_CL.md；archive/work/20261102_L6-I#5_test1_CL.md；archive/work/20261028_L13-P#4_generate_CL.md；archive/work/20261013_L7-A#2_generate_CL.md；archive/work/20261011_L4-I#2_generate_CL.md；archive/work/20261013_L13-I#2_generate_CL.md；archive/work/20261020_L13-I#3_generate_CL.md；archive/work/20261110_L6-A#6_generate_CL.md；archive/work/20261110_L6-P#6_generate_CL.md | EMITS: work/20261110_L6-I#6_generate_CL.md -->
**日期：** 2026-11-10　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3→4／6）　**格：** L6-I　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L6-A#6 本日測一，Q-0190 done）。非已殺、非刻意排除之格中最後測試日最舊＝2026-11-02（L6-I#5、L7-P#5、L7-A#5 並列）；依表序取 **L6-I**。既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py Anthropic investment AWS commitment Google Cloud`，命中約 25 筆；相關 3（SRC_DEM_034／036／037：Reuters 讀 Anthropic 機密 S-1 之雲市集營收與分潤，二手）——作測一找原文之線索，**本卡未作證據**。
- 比對之舊檔與死因型態，本卡須異型：
  - **L6-I#1**（GK；逆選擇＝對手方信用）：本卡不論對手方信用；買方信用可為最佳，機制仍成立。
  - **L6-I#2**（賣方內部代理人 bookings 計酬）：本卡之代理人為公司整體，誘因來自**持股**，非計酬。
  - **L6-I#3**（債權人驅動之首約讓價 `Δp`）：約束來源為 DDTL 債權人；本卡讓渡之受益者為**供給方自己持股之買方**，報酬回流於股權線，非可貸性。
  - **L6-I#4**（買方之交付終止權）、**L6-I#5**（買方自建／外購排序）：選擇者為買方；本卡選擇者為供給方。
  - **L13-P#4**（OpenAI 跨供應商現金守恆，[P]）：本卡不論買方預算上界；論供給方自資比例與定價誘因。若測一只能以「買方付不起」立論，即退化為 L13-P#4（否決 (5)）。
  - **L7-A#2**（上市主體持有實驗室股權之計量制度，[A]）：本卡不論持股如何入帳；入帳只作可見端（利得與分部利潤分屬兩科目）。
  - **L4-I#2**（加速器商以或有負債代替降價）、**L13-I#2**（租約擔保人兼股東）：選擇者為加速器商／擔保人；本卡為**雲服務供給方**對其**服務買方**。
  - **L6-A#6**（減損門檻）、**L6-P#6**（分區合格容量）：不涉。
  - 重疊列為否決 (5)。
- §7-10 領域最近公開：Amazon 10-Q 期 2026-09-30（2026-10-30 申報）；Alphabet 10-Q 期 2026-09-30（2026-10-29）；Anthropic 機密 S-1 報導（Reuters 2026-09-29、WSJ 2026-10-20／21，二手）。下一檢查點＝Anthropic 公開 S-1（若轉公開）、Microsoft 10-Q FQ2 FY27（約 2027-01 底）、Amazon／Alphabet 10-K FY26（約 2027-02）。

## 1. 落差一句

雲供給方（Amazon 對 Anthropic 與 OpenAI；Alphabet 對 Anthropic；Microsoft 對 OpenAI 與 Anthropic）同時是買方實驗室之股東與融資者，其最適化對象為「雲分部利潤＋持股增值」；故對被投資實驗室之單價讓渡、配給優先與自資付款，在分部線上表現為「外部 AI 需求帶動之營收與 backlog」，而回報則落在營業外持股利得。種子主張：市場以被投資實驗室之 backlog 與營收增量作**公平交易外部需求**外推雲分部，而若總報酬誘因成立，其中 `s ≡ 供給方對該買方之同期新增融資／股權撥款 ÷ 該買方對供給方之同期付款` 之一段為自資，且該段之單價／毛利低於公平交易；此段在買方上市（流動性事件）後之誘因改變——持股可變現、額度到期——而先於總需求轉弱。觀測量 `s`（季別）、被投資買方占分部 backlog 比例 `b`。本卡不定方向與量級。

已見事例（一手，sec.py 實讀 Amazon 10-Q 期 2026-09-30）：「we entered into a financing arrangement to make available to Anthropic an aggregate facility not to exceed $ 20.0 billion that will expire 30 months after an Anthropic liquidity event, including an initial public offering (“IPO”). At inception, there is no amount available to be drawn against and as we reach certain delivery milestones of compute capacity under the amended commercial arrangement, amounts under this facility are made available for Anthropic to draw upon at its discretion.」——融資額度與**供給方自身之交付里程碑**掛鉤，為本卡誘因之直接載體。同檔：「In Q2 2026, AWS and Anthropic announced an expansion of the strategic collaboration and existing multi-year commitment by more than $ 100.0 billion over 10.0 years」；「During the nine months ended September 30, 2026, we invested $50.0 billion in OpenAI’s Series C Preferred Stock … and $10.0 billion in Anthropic nonvoting preferred stock」；「In Q1 2026, AWS and OpenAI … announced an expansion of the existing $ 38.0 billion multi-year commitment … by $ 100.0 billion over 8.0 years」；持股向上調整「$ 62.8 billion for the nine months ended September 30, 2026」入「Other income (expense), net」。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因（供給方兼股東之總報酬最適化；以分部毛利讓渡換持股增值、以自身融資額度支撐買方付款）；非守恆、非會計恆等 |
| 選擇者 | 雲服務供給方兼買方股東（Amazon／AWS；Alphabet／Google Cloud；Microsoft／Azure） |
| 可見端 | 供給方 10-Q／10-K：對買方之股權投資、可轉債、融資額度及其解鎖條件；營業外持股利得；分部 backlog／RPO 與「commitment expansion」敘述；買方（Anthropic）公開 S-1（若出）之供應商承諾、單價、關係人交易 |
| 指名不可見端 | 被投資買方合約之單價與公平交易價之差；分部 backlog 中被投資買方之占比（Alphabet 10-Q 只給 Google Cloud backlog 合計 $560.8B，不分客戶）；額度實際提領與付款之時間對應 |
| 對照式（生成用） | 可拒絕：(a) 被投資買方之單價／條件與非關係人同級客戶相同（無讓渡）；或 (b) `s` 於各季均小（自資段量級不足）；或 (c) 賣方／市場已以剔除自資段之「外部需求」口徑估雲分部 |
| 表達工具型態（只指名，不選券） | 美股可交易之供給方（AMZN、GOOGL、MSFT）及其選擇權；次為被投資買方若上市。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Amazon 10-Q 期 2026-09-30（Anthropic 29 筆；融資額度、承諾擴大、OpenAI Series C、持股利得、VIE 句「Certain of our investments, including our investments in Anthropic and OpenAI, represent a variable interest in entities that we do not consolidate」）。https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm （sec.py 實讀）
2. Alphabet 10-Q 期 2026-09-30：Google Cloud revenue backlog $560.8B，「just over 55 %」於 24 個月內認列；Anthropic 未具名於投資或客戶段（grep 1 筆，非相關段）。https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm （sec.py 實讀）
3. PitchBook（Jacob Robbins）經 Morningstar Australia 2026-05-08：「The same hyperscalers writing the equity checks are also the vendors collecting the compute bills.」；「When revenue misses, the hyperscaler doesn't absorb the pain alongside you; they get paid first.」；列 Alphabet 對 Anthropic 投資與 TPU 協議、Microsoft／Nvidia 對 Anthropic 與 Azure 承諾。https://www.morningstar.com.au/stocks/ahead-ipos-ai-giants-keep-making-circular-deals-heres-why-thats-risk-clone （二手，web-fetch 實讀）
4. Anthropic 對 Google Cloud 承諾報導（2026-05-06）：https://www.computing.co.uk/news-analysis/2026/anthropic-commits-200bn-to-google-cloud （二手；搜尋結果，未實讀；測一取一手）
5. Amazon／Anthropic 擴大投資報導：https://www.implicator.ai/amazon-adds-up-to-25-billion-to-anthropic-stake-locks-in-100-billion-aws-spend/ （二手；搜尋結果，未實讀）；fourweekmba「Amazon’s Anthropic Loop」頁 WebFetch client_error（失敗歸因：站方拒絕，非不存在）。
6. 測一須另取：Microsoft 10-Q 期 2026-09-30 之 OpenAI／Anthropic 投資與 Azure 承諾句；Amazon 10-K FY25 與 Alphabet 10-K FY25 之關係人／集中度揭露；Anthropic S-1（公開版若出）之供應商單價、關係人交易；具名賣方是否剔除自資段估雲分部；Q3 2026 額度實際提領額。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 買方付款為真現金，來源多元（自有營收＋第三方募資），供給方投資占買方募資比例小；「循環」不改變需求之真實性 | 一般性反論；PitchBook 文未給反方（測一須取具名反方） | 對照 (b) |
| R2 | 循環交易已是市場熱門題材，供給方股價已反映 | PitchBook／Morningstar 2026-05-08；多家媒體「circular financing」報導 | 已定價 |
| R3 | 供給方對被投資方之定價須符合關係人與反壟斷審查，讓渡受限 | 待測一取具名出處 | 對照 (a) |
| R4 | 持股利得遠大於任何單價讓渡，供給方對分部毛利之讓渡在總報酬上可忽略，市場以總報酬估值 | 本卡自設；Amazon 9M26 持股利得已列營業外（10-Q） | 量級／已定價 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 被投資買方之單價、配給或付款來源在供給方與買方兩端申報（10-Q／10-K／S-1）及管理層原文中均不可分列，且無 ≥ 2 個獨立出處可界定 `s` 或 `b`，使落差不可觀測。
(2) 一手原文顯示被投資買方合約之單價／條件與非關係人同級客戶相同，或融資額度實際提領為零且無提領計畫——讓渡與自資前提不成立。
(3) 具名賣方或供給方管理層已以剔除自資段（或分列被投資買方）之口徑估雲分部成長／毛利，且 R2 之市場反應反覆可見——已定價。
(4) `[D]` 以可得一手數字估 `s` 或 `b` 均 < 10%（門檻本卡凍結），量級不足。
(5) 可運作對照只能寫成：對手方信用（L6-I#1）、計酬（L6-I#2）、債權人讓價（L6-I#3）、買方終止權（L6-I#4）、自建／外購排序（L6-I#5）、買方預算守恆（L13-P#4）、持股入帳制度（L7-A#2）、加速器商或擔保人選擇權（L4-I#2、L13-I#2）。
(6) 12 個月內（至 2027-11）無可檢驗事件：買方未上市、未公開 S-1、供給方未揭露額度提領或客戶集中度。

複查觸發器（若日後殺）：任一雲供給方於 10-Q／10-K 首次分列被投資買方之營收或 backlog 占比；或被投資買方公開 S-1 揭露對各供應商之單價／關係人交易條款；或 Amazon 對 Anthropic 額度首次披露實際提領額。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：供給方——分部營收、分部營業利益、RPO／backlog、非流通權益證券利得、可轉債 AFS、融資額度；買方——關係人交易、供應商承諾。
2. 可交易工具：AMZN、GOOGL、MSFT 現股與選擇權（不選券）。
3. 半衰期：至買方流動性事件後 30 個月（Amazon 額度到期條款）；`[V]` 不寫。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L6［I］標「#6 已生成」；`AIM_FUNNEL.md` §3 一句。`export/LEADS_算力收支.md`：本輪實讀之 Amazon 額度、承諾擴大、OpenAI Series C、Google Cloud backlog 均已在檔（第 18、135、149、150 列），**未新增**。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L6-I#1–#5、L6-A#1–#6、L6-P#1–#6、L13-P#4、L7-A#2、L4-I#2、L13-I#2、L13-I#3 結論。
