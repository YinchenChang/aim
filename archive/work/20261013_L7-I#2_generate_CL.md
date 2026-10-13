# L7-I#2 生成卡｜模型層：誘因（未上市實驗室股權之流動化設定研究人才之外部選擇權 → 上市主體股權報酬集中化，股東→稀缺研究者之租金轉移）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/FILEIDS.tsv；archive/drive/USED_20260930_L7-I_generate_GK.md；archive/drive/USED_20260930_L7-I_test1_GK.md；work/20261013_L7-P#2_test1_CL.md | EMITS: work/20261013_L7-I#2_generate_CL.md -->
**日期：** 2026-10-13　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1→2／6）　**格：** L7-I　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L7-P#2 測一 2026-10-13，Q-0026 done）。非已殺／刻意排除之格中，最後測試日最舊者：依 `archive/FILEIDS.tsv` 之 `archive_work` USED_ 時戳（與 L7-P#2 選格同源），L7-I 測一 2026-09-30T09:30:46Z 早於 L7-A 09:30:52Z、L10-P 09:47Z → **L7-I**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py talent compensation researcher SBC`，命中 1 筆（SRC_MOD_045，Moonshot 非同步 RL），**與本格無關**；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L7-I#1**（測一不通過）：評測集取用權為合約性、分數與取用不可分離。本卡不論評測、不論分數；誘因作用在**人才報酬**，B 端為上市主體股權報酬科目。
  - **C-I1**（死 #10）：估值歸因權重能力。本卡不主張實驗室估值歸因於權重；實驗室估值只作研究者外部選擇權之**價格輸入**，不作能力證據。
  - **C-A5**／**C-P3**（死 #13／#16）：API 單價／權重更新支出。本卡不論售價與訓練支出。
  - **L7-P#1／L7-P#2**、**L7-A**：能量下界、資料存量、token 毛利。無關。
  - **L6-I#2**（測一不通過）：高管獎金指標（bookings）設計之誘因。本卡為**研究者人才市場**之外部選擇權與股權授予量，非績效指標設計；不得滑回指標設計。
  - **L13-I**（測一不通過）：供應方對客戶股權投資 × 應收帳齡。本卡不論供應方持股。
  - **C-I2**／**L8-P**：標註專家單價／工時。本卡為前沿研究者，非標註勞務。
- §7-10 領域最近公開：Meta 2Q26 10-Q（2026-07-30）、Alphabet 2Q26 10-Q；OpenAI 員工股份出售（CNBC 2026-08-10，經 Dealroom）。下一檢查點＝Meta／Alphabet 3Q26 10-Q（約 2026-10 下旬）及 2027 DEF 14A。

## 1. 落差一句

市場把上市平台股權報酬之跳升讀成一次性「AI 搶人潮」並以回購抵銷稀釋；種子主張：只要未上市前沿實驗室持續以二級出售／回購讓員工股權在高估值下流動化，研究者之外部選擇權即被持續標價，上市主體須以集中、遠期、高履約價之股權報酬匹配，使股權報酬對人數脫鉤（人數降、報酬升）成為結構性、而非暫時性之股東→研究者租金轉移。錯價只在把未認列報酬餘額與每人報酬跳升當成會回落之一次性項。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因／外部選擇權**：研究者保留報酬 \(w^{*} \approx\) 未上市實驗室股權之可實現價值（二級出售頻率 × 估值 × 授予量）；上市主體授予 \(G_t \ge w^{*}\)；股東承擔 \(G_t\) 之稀釋與費用 |
| 選擇者 | 實驗室二級出售是否持續（IPO 後外部選擇權轉為公開市價、流動化溢酬消失）；研究者是否以使命／文化而非價格選擇（Amodei／Su 論點）；上市主體能否以裁員抵銷 |
| 可見端 | 上市主體 10-Q 股權報酬按科目（R&D）、未認列股權報酬餘額與攤銷期、RSU 授予日公允價值、期末人數、特殊選擇權授予（履約價、市場條件）；風險因子中「AI research talent」句；實驗室二級出售之日期／規模／估值（報導） |
| 指名不可見端 | 研究者個人授予額；R&D 股權報酬中 AI 研究者之占比；實驗室授予量 |
| 表達工具型態（只指名，不選券） | 美股可交易、股權報酬於 10-Q 按科目分列且揭露未認列餘額與人數之大型平台。不選券 |

恆等式（生成用，非正式載入）：\(\mathrm{SBC}_t / \mathrm{Headcount}_t\) 上升且 \(\mathrm{Headcount}_t\) 下降 ⇔ 報酬集中於少數人；未認列餘額 \(U_t\) 為已承諾之未來費用。種子綁定條件＝外部選擇權（實驗室流動化）持續。**不把實驗室估值當成能力證據；不把股權報酬上升當成錯價證據（可能已定價）；不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Meta 10-Q，季末 2026-06-30（`python tools/sec.py doc` 全文）https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm ：股權報酬「Share-based compensation — 7,658 … 4,834」（2Q26／2Q25，百萬美元）；按科目「Research and development 6,760 4,080」；「unrecognized share-based compensation expense for RSU awards was $ 79.79 billion … approximately three years」；「issued nonstatutory stock options to purchase an aggregate of 20 million shares … weighted-average exercise price of $ 2,788 per share … service and market conditions」；MD&A「The higher employee compensation was mainly from increases in share-based compensation expense and severance expenses」；「Headcount was 75,472 as of June 30, 2026, a decrease of 1% year-over-year」「May 2026 headcount reduction of approximately 8,000 employees」；風險「significant challenges in hiring specialized technical personnel, particularly senior engineering and AI research talent … From time to time we issue significant equity to attract additional employees or to retain our existing employees」。
2. Alphabet 10-Q，季末 2026-06-30 https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm ：「Stock-based compensation expense 11,514 14,708」（6M 2025／2026）；RSU 授予加權公允價值「Granted 114 $ 292.21」；「$ 59.1 billion of unrecognized compensation cost related to unvested RSUs and PSUs … 2.7 years」；未分配項含「certain AI-focused shared research and development activities, including employee compensation expenses」；「fluctuations in employee compensation expenses may not directly correlate with changes in headcount」。
3. Dealroom（2026-08-11，轉述 CNBC 2026-08-10）https://dealroom.co/news/144253-openai-closes-7b-share-sale-at-852b-valuation-ahead-of-ipo/ ：約 7B 二級出售，現任與前任員工得「cash out … at the company's $852 billion valuation」；2026-06 已秘密遞交招股書、未定上市時程。
4. Implicator.ai（Schuler，2025-08-21，轉述 WSJ／Morgan Stanley）https://www.implicator.ai/meta-hits-pause-on-ai-hiring-as-reorgs-and-costs-bite ：Morgan Stanley 警示 Meta 與 Google 股權報酬上升壓縮回購空間；單一研究者報價「as high as $1.5 billion」；簽約金近 100M（報導，二手）。

缺段（§7-2）：Meta FY25 10-K 與 ≥ 4 季股權報酬按科目序列；Microsoft／Amazon 同口徑；Anthropic 員工流動化事件之一手來源；具名賣方對「SBC 結構性 vs 一次性」之原文；DEF 14A 中 2026 選擇權授予對象與市場條件細節。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | 股權報酬上升已被賣方點名並納入回購／EPS 預期 | Morgan Stanley（經 §3-4） | 已定價（§7-4） |
| R2 | 研究者選擇取決於使命與文化，非價格匹配 | Amodei、Su（經 §3-4） | \(w^{*}\) 非價格綁定，機制弱化 |
| R3 | 實驗室 IPO 後外部選擇權轉公開市價、流動化溢酬消失 | Dealroom §3-3（已遞交招股書） | 綁定條件可在窗內解除，半衰期短 |
| R4 | 裁員抵銷：人數降 1%、遣散一次性；總員工報酬占營收可持平 | Meta 10-Q §3-1 | 對股東之淨轉移量級可能小 |
| R5 | 高履約價選擇權（市場條件）使報酬與股東報酬對齊，非租金轉移 | Meta 10-Q §3-1 | 方向不定：若未達條件則費用不實現 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後申報層無法並列「股權報酬（按科目或未認列餘額）」與「期末人數」之 ≥ 4 季序列，或只剩風險因子句；或
(2) 可運作對照只能寫成績效指標設計（滑回 L6-I#2）、實驗室估值歸因權重能力（滑回 C-I1）、或標註勞務單價（滑回 C-I2）；或
(3) 具名賣方或公司指引原文已把股權報酬上升明列為持續性費用並納入長期利潤率指引（已定價）；或
(4) 未上市前沿實驗室之員工流動化於 12 個月內轉為公開市價（IPO 完成）且上市主體授予隨即回落；或
(5) ≥ 4 季內股權報酬／人數比回落至跳升前水準，或股權報酬增幅主要來自一次性加速歸屬／遣散。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：AI 研究者之股權報酬能否自 R&D SBC 或未分配項拆出。2. 可交易工具：平台美股可交易，但股權報酬占營業利益之比是否足以影響重定價。3. 半衰期：實驗室 IPO 時點決定外部選擇權之流動化溢酬何時消失。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L7［I］格加「#2 已生成」；`AIM_FUNNEL.md` §3 一句；`query/QUEUE.md` 新列。不寫：ARCH_live／INDEX／ARCH_dead。不改 L7-I#1、L7-P#2、L7-A 及任何已殺格。
