# L13-P#4 生成卡｜資本與融資結構：守恆（單一對手方之跨供應商承諾守恆：同一對手方 OpenAI 之現金只能付一次——Σ_v 雲端供應商可歸 OpenAI 之 RPO 於年 t 之認列 ≡ OpenAI 年 t 算力現金支出 ≤ OpenAI 營收 ＋ 淨外部融資 ＋ Δ現金；各供應商 backlog 轉換率受同一預算約束而聯動）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261002_L13-P_generate_GK.md；archive/drive/USED_20261002_L13-P_test1_GK.md；archive/work/20261013_L13-P#2_generate_CL.md；work/20261013_L13-P#2_test1_CL.md；archive/work/20261020_L13-P#3_generate_CL.md；work/20261020_L13-P#3_test1_CL.md；archive/work/20261011_L6-P#2_generate_CL.md；archive/work/20261011_L6-I#2_generate_CL.md；archive/work/20261018_L6-P#3_generate_CL.md；archive/work/20261018_L6-I#3_generate_CL.md；archive/work/20261028_L11-I#4_generate_CL.md | EMITS: work/20261028_L13-P#4_generate_CL.md -->
**日期：** 2026-10-28　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 2→3／6）　**格：** L13-P　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L11-I#4 測一 2026-10-28，Q-0118 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-20（L13-P、L13-I、L14-P）；依表序取 **L13-P**。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `tokenomics_leads.py OpenAI commitments RPO`＝20 筆（輸出速度、牌價、推論支出列），相關命中 0；未用。載體全由本輪 sec.py／WebSearch／WebFetch 實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L13-P#1**（熱循環計數 vs 會計年限；死因＝現場循環數與會計年限不可並列）：本卡不涉硬體壽命。
  - **L13-P#2**（礦企 MW 挖礦／HPC 守恆＋子公司掃款；死因＝雙計一側無可觀測量、母公司償付不受約束）：本卡守恆量為**一個對手方之現金**，橫跨多個上市供應商，不是單一發行人之站址 MW。
  - **L13-P#3**（超大雲母公司現金來源＝用途按季封閉；死因＝表外量級 ≥ 表內外部融資、僅總額揭露）：#3 為**供給方自身**之封閉式；本卡為**需求方**之封閉式，加總維度為跨供應商之應收承諾。測一須先驗 (2)——對手方別揭露是否存在（本格 #3 死因為只有總額）。
  - **L6-P#2**（RPO 交付之電力-時間預算）：約束在供給側之 MW；本卡約束在需求側之現金。**L6-I#2**（bookings 計酬誘因）、**L6-I#3**（投資級對手方可貸性）：誘因型，非守恆。**L6-P#3**（機群容量分割）：供給側。
  - **L13-I#2**（租約擔保人兼股東）、**L13-I#3**（評等觸發線工具選擇）、**L13-A#2–#4**：不涉跨供應商加總。
  - **C-A4**（ARCH_dead #4，表達窗）、**C-A3**（折舊樞紐）：不重開。**L11-P**：不恢復。**T-15 CoreWeave 空方**（委託資本外）：本卡不寫 T-15；CoreWeave 只作加總之一項讀數，不作主體。
- §7-10 領域最近公開：Oracle 10-Q（期末 2026-08-31，申報 2026-09-11）；Microsoft 10-K FY26（期末 2026-06-30，申報 2026-07-29），FY27 Q1 10-Q 未出（本輪 sec.py 最新 10-Q 期末 2026-03-31）；AMD 10-Q（期末 2026-06-27）；CoreWeave 10-Q（期末 2026-06-30）；OpenAI 收入 run-rate 報導 2026-10-08（FT、Reuters 等，二手）。OpenAI S-1 為機密送件，本輪未見公開版。

## 1. 落差一句

Oracle RPO $664B（2026-08-31，年前 $455B，增量「primarily attributable to certain significant cloud contracts」）、Microsoft commercial RPO $678B（FY26 末）且 FY26 Q2 投影片稱約 45% 由 OpenAI 驅動、AWS $38B／7 年、CoreWeave「up to approximately $6.5 billion」等 OpenAI 承諾，各自以供應商之 backlog 被讀；種子主張：同一對手方之現金只能付一次——Σ_v（可歸 OpenAI 之 RPO 於年 t 之認列排程）≡ OpenAI 年 t 算力現金支出 ≤ 營收_t ＋ 淨外部融資_t ＋ Δ現金_t。OpenAI 2025 營收約 $13B、對投資人稱 2030 前算力支出約 $600B（與先前「$1.4T／30 GW」口徑不同）、資本缺口報導約 $207B。若各供應商 backlog 轉換率被獨立外推，則加總排程可超過對手方預算；超過部分只能以延後、重議或改由他客戶承接之形式在供應商間分配——錯價只在**加總與分配**，不在任何單一供應商之 RPO 數字。本卡不主張方向與量級，只立可拒絕之「跨供應商可歸 OpenAI 之年度認列排程可加總，且與 OpenAI 可得資金來源可並列」。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆（P）**：對手方現金預算之封閉。Σ_v S_v,t ≡ C_t ≤ Rev_t ＋ F_t ＋ ΔCash_t；S_v,t＝供應商 v 之可歸 OpenAI RPO 於年 t 之認列額。層級分離：雲端供應商（Oracle、Microsoft、AWS、CoreWeave、Google）為同層，晶片協議（AMD 6 GW＋認股權證、Nvidia、Broadcom）多經雲端供應商採購，跨層相加即雙計（`$1.4T` 口徑之疑點，測一查） |
| 驅動（因果層，§7-5） | OpenAI 營收成長率、外部融資可得性（私募輪、IPO、債）、算力單價；供應商端無驅動力——約束完全在對手方之來源側 |
| 量綱 | RPO 與認列排程［美元／年］；OpenAI 營收、融資［美元／年］；份額［比率］ |
| 可見端 | Oracle RPO 與 12／13–36／37–60 月認列比例；Microsoft RPO 與 OpenAI 份額口頭／投影片；CoreWeave 客戶集中度與 OpenAI 合約額；AMD 認股權證歸屬條件；OpenAI 營收與融資報導 |
| 指名不可見端 | 各供應商 RPO 中 OpenAI 之逐年排程（Oracle 不點名）；合約之取消、延後、容量條件條款；OpenAI 自身之未來最低支付表（S-1 公開前不可得） |
| 外部參照物（測一查證） | 單一大客戶跨多供應商承諾超過其資金來源而致多家供應商同時下修 backlog 之具名前例（如電信泡沫期光纖 IRU／容量交換、太陽能多晶矽長約） |
| 表達工具型態（只指名，不選券） | 美股上市雲端供應商與加速器商普通股；不選券 |
| 重疊 | L6-P#2（供給側時間預算）、L13-P#3（供給側封閉式）、L4-I#2（加速器商或有承諾）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Oracle 10-Q 期末 2026-08-31（sec.py）https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm ：「Remaining performance obligations were $ 664 billion as of August 31, 2026 , of which we expect to recognize approximately 13 % as revenues over the next twelve months , 37 % over the subsequent month 13 to month 36 , 34 % over the subsequent month 37 to month 60」；MD&A：「$664 billion and $455 billion as of August 31, 2026 and 2025 … primarily attributable to certain significant cloud contracts」；全文 grep `OpenAI` 0 處、`limited number of` 0 處——**不點名**。
2. Microsoft 10-K FY26（sec.py）https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm ：「Commercial remaining performance obligation increased 84% to $678 billion」；RPO 估計「can involve significant judgments, including … potential renegotiation of commitments」；OpenAI 以權益法投資列示（FY26 淨利益 $6.5B，主為 Recapitalization 稀釋利益）。10-K 本文未見 OpenAI 占 RPO 之比例句（測一複核）。
3. Microsoft FY26 Q2 投影片（轉述）Cloud Wars 2026-01-29 https://cloudwars.com/cloud/microsoft-q2-rpo-soars-110-led-by-openai-commitment-of-281-billion/ ：「Roughly 45% of the commercial RPO balance is driven by commitments from OpenAI」（$625B 之 45% ≈ $281B）。二手，測一取一手投影片或逐字稿。
4. CoreWeave 10-Q 期末 2026-06-30（sec.py）https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm ：「OpenAI committed to pay us up to approximately $6.5 billion through May 31, 2031」；「Other significant customers include Microsoft and OpenAI … risks of non-payment and non-performance」。只作加總一項，不作主體（T-15 邊界）。
5. AMD 10-Q 期末 2026-06-27（sec.py）https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm ：OpenAI 認股權證「up to 160 million shares … vest in tranches based on specified AMD Instinct GPU purchase milestones by OpenAI … or indirectly through authorized third-parties」——晶片採購可經第三方（雲端）完成，跨層雙計之一手依據。
6. Reuters（經 Business Standard，2026-02-21）https://www.business-standard.com/world-news/openai-expects-600-bn-in-compute-spending-through-2030-ahead-of-ipo-126022100286_1.html ：「roughly $600 billion in total compute spending through 2030」；Altman「$1.4 trillion to develop 30 gigawatts」；2025 營收 $13B；2030 營收「more than $280 billion」（CNBC）。
7. Capacity（2026）https://capacityglobal.com/news/openais-ipo-is-the-largest-compute-procurement-vehicle-in-corporate-history/ ：Oracle「$60 billion per year for five years (2027–2031)」、AWS $38B／7 年、CoreWeave $22.4B、AMD 6 GW；資本缺口約 $207B；S-1 機密送件。二手。
8. Luminix 彙整 https://www.useluminix.com/reports/company-overviews/oracle-ai-debt-openai-contract/source/1 ：S&P 2026-07-09 將 Oracle 降至 BBB-、稱 OpenAI 為關鍵信用風險、估 OpenAI 約占當時 $638B RPO 之半；FT 2026-10-08 報 OpenAI 9 月 run-rate 約 $50B（低於先前約 $70B）。二手，測一取 S&P 原文與 FT 原文。

缺段（§7-2）：各供應商 OpenAI 之逐年認列排程；合約取消／延後條款原文；OpenAI 自身最低支付表（S-1 公開版）；Google Cloud 對 OpenAI 承諾額；Microsoft FY27 Q1 10-Q（約 2026-10 末）之 OpenAI 份額更新。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | S&P 已降評並點名 OpenAI 為關鍵信用風險；Microsoft 已口頭揭露 45% 份額——集中度市場已知 | #3、#8 | 已定價 |
| R2 | 合約有容量交付條件與重議空間（Microsoft 10-K「potential renegotiation of commitments」），OpenAI 承諾為上限（「up to」）而非照付 | #2、#4 | 守恆式之左邊非剛性，延後即自動封閉 |
| R3 | 被釋出之容量由 Meta、Anthropic、Jane Street 等他客戶承接（CoreWeave 2026 新增 Meta、Jane Street 合約） | #4 | 恆等外有替代，供應商端不受損 |
| R4 | OpenAI 以 IPO（報導估值 $850B–$1T）補足缺口；來源側可擴張 | #7 | 不等式不綁定 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法取得 **≥ 3 家**供應商之可歸 OpenAI 承諾額與期間（一手或公司口頭），使 Σ_v S_v,t 不可加總（L13-P#3 型「只有總額」死因）。
(2) 跨供應商加總之窗內（2027–2030）年度排程 `[D]` 不超過 OpenAI 已報導之來源上界（營收報導值 ＋ 已宣布融資）——不等式不綁定（R4）。門檻：Σ_v S_v,t ÷（Rev_t ＋ F_t）之區間下端 < 1 即觸發。
(3) 具名賣方、評等機構或供應商本身已以「對手方預算約束下之跨供應商分配」建模 backlog 轉換或 2027 指引——已定價（R1）。只點名集中度不算。
(4) 重定價窗（≥ 12 個月）內無可觀測之檢驗事件（OpenAI S-1 公開版或首份 10-Q 揭露未來最低支付表；任一供應商 RPO 下修或重議揭露；OpenAI 融資輪結果），或其已全部於窗前公告。
(5) 可運作對照只能寫成供給側 MW 時間預算（L6-P#2 型）、供給方自身來源用途封閉（L13-P#3 型）或對手方信用利差（評等型），而非需求方現金之跨供應商封閉。

複查觸發器（若日後殺）：OpenAI S-1 公開或首份定期報告揭露最低支付表；Oracle 或 Microsoft 首次點名 OpenAI 之逐年 RPO；任一供應商揭露 OpenAI 合約延後或重議；具名賣方以對手方預算約束建模。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：RPO 與認列期間分桶、客戶集中度附註、權益法投資（Microsoft）、認股權證（AMD）。
2. 可交易工具：雲端供應商與加速器商普通股。不選券。
3. 半衰期：RPO 按季更新；OpenAI 融資與 IPO 事件不定期；合約期 5–7 年。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0119；`query/ARCH_matrix.md` L13［P］標「#4 已生成」；`export/LEADS_算力收支.md` 追加 2 筆（Oracle RPO、Microsoft commercial RPO；一手 10-Q／10-K）。不寫入：FUNNEL（載入量 29,973 B，留給測一）、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L13-P#1–#3、L13-A#1–#4、L13-I#1–#3、L6 系列、C-A3／C-A4 結論；不寫 T-15。
