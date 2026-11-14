# L11-I#6 生成卡｜人類注意力：誘因（同意選擇架構由被監理者自行設計：歐盟「較少個人化廣告」（LPA）選項上線後，可變現注意力 ≡ k·m_P ＋ (1−k)·m_LPA；同意率 k 由平台以選項呈現、摩擦與 LPA 檔之廣告中斷設計左右，且從未揭露；DMA 監理以「uptake」證據改寫設計權）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261002_L11-I_generate_GK.md；archive/work/20261013_L11-I#2_generate_CL.md；archive/work/20261020_L11-I#3_generate_CL.md；archive/work/20261028_L11-I#4_generate_CL.md；archive/work/20261103_L11-I#5_generate_CL.md；work/20261103_L11-I#5_test1_CL.md | EMITS: work/20261114_L11-I#6_generate_CL.md -->
**日期：** 2026-11-14　**角色：** SCOUT@CL（排程 SCOUT-GEN，pick 配額 1→2／6）　**格：** L11-I　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L11-A#6 於 2026-11-13 測一，Q-0198 done）。非已殺／刻意排除格中最後測試日最舊＝2026-11-03（L11-I、L13-A）；依表序取 **L11-I**（與 #3–#5 同一平手規則；淺 clone 無法以 commit 時間細分）。既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `tokenomics_leads.py Meta advertising Europe consent`，6 筆皆硬體／模型訓練列，相關命中 0；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L11-I#1**（代理議價使注意力存量轉為合約權利）：本卡不涉代理或權利型態。
  - **L11-I#2**（pro-rata 版稅池占比）：本卡非池內分配。
  - **L11-I#3**（創作者兌現率按付費者年齡分級，供給側定價）：本卡之選擇變數在**使用者側同意**，非對創作者之兌現率。
  - **L11-I#4**（賣方兼執法者之違規廣告主門檻 e）：本卡無違規收入、無執法門檻；監理者改寫的是**選項設計**而非平台自訂之執法強度。
  - **L11-I#5**（推薦位以版稅折讓出售）：本卡不涉供給側讓利換曝光。
  - **反覆死因（#2–#5）＝不可分離／無可界定上下界。** 本卡之 k 亦未揭露，故測一須**先驗 (2)**：分部或地理揭露（Europe 廣告營收、每則廣告價格之地區拆分）能否把 k 之作用界定到可拒絕之區間。
  - **L12 系列**（訴訟／罰款或有負債）：本卡不賭罰款額或上訴勝負。**L10-I 系列**（預設槽位、佣金路由）：本卡非分發槽位。**L11-A#1**（曝光 × 單價）：價量只作讀數。**L11-P**（ARCH_dead #3）：不恢復。
- §7-10 領域最近公開：Meta 10-Q 期末 2026-09-30（EDGAR 路徑見 §3 #1）；Q3 2026 法說報導 2026-10-22；歐盟執委會 2025-12-08 公告 LPA 新選項 2026-01 呈現、上線後「seek feedback and evidence … on the impact and uptake」。本輪未見其後之執委會決定（檢索失敗不是存在性主張，§7-2）。
- SEC：`tools/sec.py` 本輪被宿主隱私外掛拒絕（腳本內含聯絡 email）；10-Q 原文未讀，僅記 EDGAR URL 作載體錨；測一須實讀或記「無法判定（失敗歸因：宿主）」。

## 1. 落差一句

Q3 2026 Meta 歐洲廣告營收 YoY +18% vs 美加 +33%（newsmediahouse 2026-10-22 報導；歐洲前兩季約 40% → 24%），CFO 2026-07 法說：「We're seeing the impact of less personalized ads offering in Europe now that it's fully rolled out, and that may be an additional headwind」；而 10-K FY2025 與 10-Q Q1／Q2 2026 之風險段同句（「less relevant and effective than our premium ad offerings」），**不揭露選擇 LPA 之使用者比例 k、亦無收入效果**（cittago 2026-09 逐檔比對）。可變現注意力由平台自設之同意架構決定，監理者以 uptake 證據改寫該架構；種子主張：若市場把歐洲減速讀為一次性基期或宏觀，則錯價只在「k 之水準與其被監理改寫之方向」。本卡不主張方向與量級，只立可拒絕之「k 之作用可界定，且 12 個月內有外生改寫事件」。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因（I）**：平台同時為同意介面設計者與廣告收入受益者。歐洲廣告營收 ≡ 注意力 × [k·m_P ＋ (1−k)·m_LPA]，m_P > m_LPA；設計者之邊際誘因＝以呈現順序、摩擦、LPA 檔之不可略過廣告中斷等把 k 推高；監理者（DMA 守門人義務）之誘因相反 |
| 驅動（因果層，§7-5） | 選項設計權之歸屬（平台自定 vs 執委會依 uptake 證據強制修改）；使用者對 LPA 檔體驗之反應；廣告主在 LPA 庫存之轉換率（m_LPA 隨模型改進而變，CFO「a lot of runway」） |
| 量綱 | 歐洲廣告營收［$／季］；YoY 成長率［%］；k［比率］；m_P／m_LPA［每千曝光收入比］；每則廣告價格地區拆分［%］ |
| 可見端 | 10-Q／10-K 地理分部營收（依使用者地理位置之廣告營收）、每則廣告價格與曝光數地區成長；法說 CFO 歸因句；執委會 DMA 新聞稿 |
| 指名不可見端 | k 之現值與序列；m_LPA／m_P；LPA 檔廣告中斷頻率之設計參數；執委會 uptake 證據內容 |
| 外部參照物（測一查證） | 同意選擇架構被監理改寫之具名一手前例（例：Google 搜尋選擇畫面、Apple ATT 提示之歐盟國家級裁罰）及其前後之同意率／收入揭露 |
| 表達工具型態（只指名，不選券） | 美股上市社群廣告平台普通股；不選券 |
| 重疊 | L12（DMA 罰款）、L11-A#1（價量）、L11-I#4（自設門檻）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Meta 10-Q（期末 2026-09-30）https://www.sec.gov/Archives/edgar/data/0001326801/000162828026066773/meta-20260930.htm ；Q1 2026 10-Q https://www.sec.gov/Archives/edgar/data/0001326801/000162828026028526/meta-20260331.htm ；10-K FY2025 https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm ——地理營收、每則廣告價格／曝光地區成長、LPA 風險段。本輪未實讀（§0）。
2. newsmediahouse 2026-10-22 https://www.newsmediahouse.com/article/meta-s-ad-sales-are-suffering-now-that-europeans-can-pick-less-personalization/ ：歐洲 +18%、美加 +33%；「Meta does not disclose how many people have picked each option」；Rothschild & Co Redburn（Dominic Ball，經 WIRED）：「the EU's free, personalized advertising option is contributing to the European slowdown」；LPA「uses 90 percent less data」。二手。
3. cittago 2026-09-06（更新 09-23）https://cittago.com/blog/meta-less-personalised-ads-eu-filings-2026/ ：10-K FY2025、10-Q Q1／Q2 2026 風險段逐字相同，無使用者比例、無收入效果。二手。
4. PYMNTS 2025-12-08 https://www.pymnts.com/meta/2025/meta-agrees-to-give-eu-users-more-personalized-ad-choice/ ：執委會「Meta will present these new options to users in the EU in January 2026」；上線後收集 uptake 證據；2025-04 €200M DMA 罰款。
5. AdExchanger 2025-10-29 https://www.adexchanger.com/platforms/metas-q3-was-a-net-win-disguised-as-a-loss/ ：CFO「We cannot rule out the commission imposing further changes to that offering」，可能「significant negative impact on our European revenue」。
6. mezha.net 同題報導——本輪讀取失敗（client_error；非存在性主張）。

缺段（§7-2）：k 之任何一手數值；10-Q 原文（宿主阻）；執委會 2026 年任何 uptake 評估或新程序之一手；具名賣方是否把 LPA 分列入歐洲模型；Q3 2026 法說官方逐字稿。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 歐洲減速主要為基期（前兩季高成長）與匯率，非 LPA；Meta Q3 未直接歸因 | #2 | 不可分離 |
| R2 | 10-Q 自 FY2025 10-K 起即揭露風險，賣方（Redburn）已點名，市場已知 | #2、#3 | 已定價 |
| R3 | m_LPA 隨模型改進收斂（CFO「a lot of runway」），k 不再重要 | #2 | 機制自消 |
| R4 | 執委會僅「收集證據」，無排定決定日 | #4 | 窗內無檢驗事件 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 公司或具名賣方已量化 LPA 對歐洲廣告營收或 k，且入 2026／2027 指引或共識——已定價（R2）。
(2) 實讀後地理揭露（歐洲營收、每則廣告價格地區拆分）無法把 LPA 效果與基期／匯率／宏觀分開，使 `[D]` LPA 對歐洲廣告營收年成長之影響區間寬於 [0, 20 pp] 之一半以上、或上界 × 歐洲營收占比 < 1% 合併營收——不可分離或不重大（R1）。**先驗本條。**
(3) 重定價窗（≥ 12 個月）內無可觀測之外生改寫事件（執委會對 LPA 之 uptake 評估、新不遵循程序或決定、歐盟法院對 €200M 罰款上訴之判決、他司法區（英國 ICO／CMA）同類同意設計之行動），或其已於窗前全部公告（R4）。
(4) 可運作對照只能寫成罰款或有負債（L12 型）、曝光 × 單價（L11-A#1 型）或平台自設執法門檻（L11-I#4 型）。
(5) 一手證據顯示 m_LPA ≈ m_P（LPA 庫存每則價格與個人化庫存差 < 10%），使 k 無經濟作用（R3）。
(6) 申報顯示 LPA 選項僅適用極小使用者群（例：只限未登入或新註冊）而非全體歐盟使用者，使機制非主體。

複查觸發器（若日後殺）：Meta 首次揭露 k 或 LPA 收入效果；執委會發布 LPA uptake 評估或新決定；歐盟法院就 Meta DMA 罰款上訴判決；英國或他司法區強制修改同意選擇架構。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：依使用者地理之廣告營收（Europe）、每則廣告價格與曝光數之地區成長、DMA 相關風險段。
2. 可交易工具：社群廣告平台普通股。不選券。
3. 半衰期：執委會程序不定期；法院上訴以年計；季報讀數按季。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0199；`query/ARCH_matrix.md` L11［I］標「#6 已生成」；`AIM_FUNNEL.md` §3「已生成未測」。不寫入：INDEX.json、ARCH_dead、RETRIG、ARCH_live、LEADS（本輪無 AI 算力收支類新數值）。不改 L11-I#1–#5、L11-A#1–#6、L11-P、L12 系列、L10-I 系列結論；不寫 T-15。
