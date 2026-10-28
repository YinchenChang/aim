# L11-I#4 生成卡｜人類注意力：誘因（賣方兼執法者：平台自定違規廣告主之執法門檻 e，違規收入 R_v 以「懲罰性出價」留在拍賣內；外部強制（州 AG 訴訟、監理）把 e 由內生改為外生）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261002_L11-I_generate_GK.md；archive/drive/USED_20261002_L11-I_test1_GK.md；archive/work/20261013_L11-I#2_generate_CL.md；work/20261013_L11-I#2_test1_CL.md；archive/work/20261020_L11-I#3_generate_CL.md；work/20261020_L11-I#3_test1_CL.md；archive/work/20261027_L11-A#4_generate_CL.md | EMITS: work/20261028_L11-I#4_generate_CL.md -->
**日期：** 2026-10-28　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 1→2／6）　**格：** L11-I　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L11-A#4 測一 2026-10-27，Q-0117 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-20（L11-I、L13-P、L13-I、L14-P）；依表序取 **L11-I**。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `tokenomics_leads.py Meta advertising scam`＝2 筆（SRC_MOD_047／048，Llama RL 後訓練），相關命中 0；未用。載體全由本輪 sec.py／WebSearch／WebFetch 實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L11-I#1**（代理議價使注意力存量轉為合約權利；死因＝同一條款頁兩句不可並列）：本卡不涉代理或權利型態。
  - **L11-I#2**（pro-rata 版稅池；死因＝AI 占比無水準序列、可分配殘量 < 1%）：本卡非池分配。
  - **L11-I#3**（DevEx 兌現率分級；死因＝選擇變數不可分離、基期污染）：本卡選擇變數為**平台對違規廣告主之執法門檻**（確定度門檻、收入護欄），非對供給側之價格分級。測一須先驗 (2) 可分離性——此為本格反覆死因。
  - **L11-A#1**（曝光 × 單價）：本卡不以價量恆等為主張；價量只作讀數。**L11-A#4**（存量池轉換）：不涉。
  - **L12 系列**（法案成立與否、或有負債）：本卡不賭訴訟勝負或罰款額；主張為執法門檻外生化後之**收入組成**變動。**L10-I#4**（代理失誤之買家保障成本）：不同主體與機制。**L11-P**（ARCH_dead #3）：不恢復。
- §7-10 領域最近公開：Meta 3Q26 10-Q（申報 2026-10-22）與法說（2026-10-21）；Rhode Island AG 訴狀（Providence Superior Court，報導 2026-10-23）。

## 1. 落差一句

Meta 3Q26 每則廣告均價 +14%、曝光 +10%，管理層歸因「ad performance gains」；同期 Reuters（2025-11-06）所引內部文件稱 2024 年約 10%（約 $16B）收入來自詐騙與禁售品廣告，且以「penalty bid」對疑似詐騙者**加價而非封鎖**、封鎖須 95% 確定度、審查團隊 2025 上半年行動成本護欄 0.15% 收入。若 e 由平台內生設定，違規收入以高單價留在拍賣，則一部分單價增長＝違規需求之租；外部強制（USVI 2025-12、Rhode Island 2026-10、Santa Clara County 2026-05、參議員請 FTC／SEC 調查）把 e 外生化時，R_v 與其對均價之貢獻同步退出。種子主張：若市場把單價增長全讀為 AI 投放效率，錯價只在 R_v 份額。本卡不主張方向與量級，只立可拒絕之「R_v 份額可界定，且 12 個月內有外生化事件」。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因（I）**：平台同時為注意力賣方、拍賣設計者與執法者。R ≡ R_clean ＋ R_v·(1 − e)；e＝f(確定度門檻 θ, 收入護欄 g)；penalty bid 使違規廣告主之實現單價 > 一般 → 均價含違規溢價 |
| 驅動（因果層，§7-5） | 平台對 θ、g 之自定權；外部強制（州消費者保護訴訟、FTC／SEC、EU DSA、UK 詐騙廣告義務）改寫 θ 之成本；生成式廣告工具降低違規廣告主之進入成本 |
| 量綱 | 廣告收入［美元／季］；均價變動［%］；R_v／R［比率］；θ［確定度］；g［收入比率］ |
| 可見端 | 10-Q 均價／曝光年比與歸因句、「enhance enforcement … may be material」風險句、訴訟附註；訴狀與 Reuters 所引內部文件；Meta 移除數量 |
| 指名不可見端 | R_v 現值（Meta 稱 10.1% 為「rough and overly-inclusive」、真值較低、不給更新數）；penalty bid 之溢價幅度與適用量；θ、g 現值 |
| 外部參照物（測一查證） | 平台加強廣告執法後收入受損之具名前例（如 Google 對違規廣告主之執法年報、TikTok／Meta 過往品類禁令後之揭露） |
| 表達工具型態（只指名，不選券） | 美股上市廣告平台普通股；不選券 |
| 重疊 | L11-A#1（價量）、L12（訴訟）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Meta 10-Q 3Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm ：「Ad impressions delivered across our Family of Apps in the third quarter of 2026 increased 10% year-over-year, and our average price per ad … increased 14%」；「Our ongoing efforts to enhance enforcement against ads and marketers which violate our advertising policies adversely affect our revenue, and we expect that the continued enhancement of such efforts will have an impact on our revenue in the future, which may be material」；訴訟附註：「litigation and government inquiries … relating to … fraud, deceptive activity or advertising, financial scams」；DZ Reserve（潛在受眾估計灌水集體訴訟）仍待第九巡迴上訴。
2. 同一風險句已見於 10-Q 2Q25 https://www.sec.gov/Archives/edgar/data/1326801/000162828025036791/meta-20250630.htm 、10-Q 3Q25 https://www.sec.gov/Archives/edgar/data/1326801/000162828025047240/meta-20250930.htm 、10-K FY25 https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm ——措辭未變、從未量化。
3. Meta 3Q26 法說（2026-10-21）https://www.fool.com/earnings/call-transcripts/2026/10/21/meta-meta-q3-2026-earnings-call-transcript/ ：均價「increased 14% year over year driven by ad performance gains」；Q4 收入指引 $73–76B；scam／fraud／integrity 0 處（WebFetch 摘要，測一應以 IR 逐字稿 PDF 複核：https://s21.q4cdn.com/399680738/files/content_files/META-Q3-2026-Earnings-Call-Transcript.pdf ）。
4. Reuters 內部文件報導（2025-11-06）之轉述：PPC Land https://ppc.land/meta-charged-suspected-fraudsters-premium-rates-while-earning-billions-from-scam-ads/ ——約 10%／$16B、每半年 $3.5B 高法律風險部分、penalty bid、95% 門檻、0.15% 護欄；Meta 發言人稱護欄為「a revenue projection rather than a ceiling」。二手，測一須取 Reuters 原文。
5. 參議員 Blumenthal、Hawley 請 FTC／SEC 調查（2025-11-25）https://san.com/cc/senators-want-ftc-sec-investigation-into-meta-making-billions-on-scam-ads/ 。
6. USVI AG 訴訟（St. Croix 高等法院，報導 2025-12-30）https://interestingengineering.com/culture/virgin-islands-sues-meta-scam-ads ；Rhode Island AG 訴訟（Providence Superior Court，報導 2026-10-23；求民事罰款、返還、不當得利吐出、禁制令；提及 Santa Clara County 2026-05 類似訴訟）https://www.insurancejournal.com/news/east/2026/10/23/890093.htm 。

缺段（§7-2）：Reuters 原文；R_v 任何 2025–2026 更新值；penalty bid 溢價幅度；FTC／SEC 是否立案；具名賣方是否把違規收入份額納入模型；訴狀全文（RI、USVI、Santa Clara）。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | Meta：10.1% 為「rough and overly-inclusive」，真值較低；用戶詐騙回報已下降 | #4、#6 | 份額小到不重大 |
| R2 | 違規收入不分列，均價增長無法拆出違規溢價 | #1、#3 | 不可分離（L11-I#3 型死因） |
| R3 | 「enhance enforcement」風險句自 2025 年起即在申報，市場已知 | #2 | 已定價 |
| R4 | 被封鎖之違規預算轉為合規廣告主填補拍賣，均價不降 | 拍賣機制 | 恆等外有替代 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 公司或具名賣方／評等機構已量化違規收入份額或執法對收入之影響，且已入 2027 指引或共識——已定價（R3）。
(2) 實讀後 R_v／R 無可界定上下界（唯一數值仍為 2024 內部估計且公司否認），使 `[D]` 份額區間寬於 [0, 10%] 之一半以上、或上界 < 2%——不可分離或不重大（R1、R2）。
(3) 重定價窗（≥ 12 個月）內無可觀測之外生化事件（FTC／SEC 立案、訴訟裁定或和解附執法條款、EU／UK 執法決定），或其已於窗前全部公告。
(4) 可運作對照只能寫成曝光 × 單價（L11-A#1 型）、訴訟或有負債（L12 型）或兌現率分級（L11-I#3 型）。
(5) 拍賣替代（R4）有具名一手證據：既往大規模違規廣告主下架後均價未降。

複查觸發器（若日後殺）：Meta 首次量化執法對收入之影響；FTC 或 SEC 公開立案；任一州 AG 案和解附 θ／護欄條款；具名賣方以違規收入份額建模。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Advertising revenue、均價／曝光年比、Legal and related（訴訟附註、accrued legal）。
2. 可交易工具：廣告平台普通股。不選券。
3. 半衰期：訴訟程序以年計；監理立案不定期；季報讀數按季。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0118；`query/ARCH_matrix.md` L11［I］標「#4 已生成」。不寫入：FUNNEL（載入量 29,905 B，留給測一）、INDEX.json、ARCH_dead、RETRIG、ARCH_live、LEADS（本輪無 AI 算力收支類新數值）。不改 L11-I#1–#3、L11-A#1–#4、L11-P、L12 系列、L10-I#4 結論；不寫 T-15。
