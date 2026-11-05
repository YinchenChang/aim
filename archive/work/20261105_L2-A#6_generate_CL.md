# L2-A#6 生成卡｜資料中心實體：會計恆等（出租方以股權工具支付第三方信用支撐之對價：遞延費用資產 \(A_0\) 依租期直線攤銷，其損益表落點決定 Adjusted EBITDA／每 MW 收益是否含此成本）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/work/20261007_L2-A#2_generate_CL.md；archive/work/20261014_L2-A#3_generate_CL.md；archive/work/20261021_L2-A#4_generate_CL.md；archive/work/20261029_L2-A#5_generate_CL.md；work/20261029_L2-A#5_test1_CL.md；query/ARCH_live.md（L13-A#4、L13-A#5、L12-A#5 列） | EMITS: work/20261105_L2-A#6_generate_CL.md -->
**日期：** 2026-11-05　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 4→5／6）　**格：** L2-A　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L2-P#6 本日測一，Q-0168 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-29：L2-A（#5，Q-0128）與 L2-I（#5，Q-0129）同日；取佇列序在前之 **L2-A**。既有 #1–#5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `backstop warrant lease guarantee`，命中 6 筆（SRC_DC_014、SRC_DC_016、SRC_CAP_008–011），無一涉信用支撐或認股權；未用。內部研究數字未用。
- 比對（須異型）：
  - **L2-A**（`archive/drive/USED_20260913_L2-A_test2_cost-index_GK.md`）：建置成本指數。不涉。
  - **L2-A#2**：利息資本化（費用側、在建期）。本卡為**營運期、非現金之第三方對價攤銷**，不經利息科目。
  - **L2-A#3**：電力轉嫁總額認列（變動租金）。不涉。
  - **L2-A#4**：建物折舊年限 vs 租期之殘值比。本卡之資產為**無形遞延費用**（信用支撐權益），年限即租期，無年限錯配；樞紐是**科目落點**而非年限。
  - **L2-A#5**（測一 `work/20261029_L2-A#5_test1_CL.md`）：固定租金直線化＋預收攤轉，全期守恆、只移時點。本卡之成本**全期不守恆**（\(A_0\) 為一次性股權轉移，非租金重分配）；L2-A#5 生成卡 R3 已把「認股權攤銷」列為鄰接項、不作樞紐，測一 A 段明記「攤銷之損益表科目本檔未載明，留待 3Q26 10-Q」——本卡即以該未決點為樞紐。
  - **L13-A#4**（可轉債全成本）、**L13-A#5**（子公司 PIK 優先）：融資工具之成本未入利息；本卡之工具由**非融資人、非承租人之第三方擔保者**取得，成本以租約資產（非負債）攤銷。若測一判定其實質為融資成本，則落 (4) 否決。
  - **ARCH_dead C-A3**（GPU 折舊年限）、**C-P4**（水耗）：不涉。
- §7-10 領域最近公開：CIFR 10-Q 3Q26（2026-11-02 申報）；HUT 10-Q 3Q26（2026-11-04）；WULF 10-Q 2Q26（2026-08-05）、8-K 2026-11-04（Justified Google Backstop）。下一檢查點＝WULF 3Q26 10-Q（預期 2026-11 上中旬）。

## 1. 落差一句

AI 出租方（前礦企）為取得資料中心租約之信用評等支撐，向非承租之第三方（Google）發行近零行權價認股權；出租方把發行日公允值 \(A_0\) 記為遞延費用資產，並「over the life of the lease on a straight-line basis」攤銷。恆等式：\(\text{淨租約經濟}_t \equiv Rent_t - A_0/T\)；若攤銷落於 D&A 或「其他」而非營收抵減或營業費用，則 \(\text{Adj. EBITDA}_t = \text{Adj. EBITDA}^{淨}_t + A_0/T\)，且認股權負債之公允值變動另被 Adj. EBITDA 排除——兩條路徑使此股權對價**永不進入** EBITDA 與「每 MW 年收益」口徑。對照：Plug Power 對**客戶** Amazon 之認股權依 ASC 606 直接抵減營收（2020 年 −399.7 百萬美元、全年合併營收轉負）；Google 非承租人，故 606 不直接適用，科目屬管理層判斷。`[D]`（輸入待測一實讀）：CIFR \(A_0\)＝544.5、T＝10 → 54.5／年，對照公告合約約 3,000／10 年 → 約 18%（若攤銷年限延至 20 年合約期則約 9%）；WULF \(A_0\)＝515.5、T＝10 → 51.6／年，對照首批公告約 3,700／10 年 → 約 14%（擴約後更低）。可拒絕之主張＝≥ 2 家出租方之 \((A_0/T)/Rent\) ≥ 5%，且攤銷不在營收抵減或 Adj. EBITDA 內，且具名賣方以 EBITDA 或每 MW 收益定價而未扣除。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等（A）**：(i) \(A_0\)＝發行日認股權公允值（Black-Scholes，Level 3）；(ii) 攤銷 \(a=A_0/T\) 自租約起租起；(iii) 認股權負債後續 \(\Delta FV\) 入損益、被 Adj. EBITDA 排除；(iv) 補足條款（CIFR：行權期前股份價值 < 435.0 百萬美元則增發或付現）使對價下限為合約固定 |
| 選擇者 | 出租方（攤銷科目、Adj. EBITDA 定義、攤銷年限＝初始租期或含後續承租人之合約期）；Google（擔保終止條件：WULF Justified 案於 Anthropic 取得投資級評等滿三個月即終止） |
| 可見端 | 10-Q 附註「Warrants」「Other noncurrent assets／Deferred charges」之 \(A_0\) 與攤銷政策句；Adj. EBITDA 調節表各列；認股權公允值變動列；EPS 稀釋股數 |
| 指名不可見端 | 攤銷起始後之損益表科目（截至 CIFR 3Q26、WULF 2Q26 均未見攤銷列：CIFR 544.5 兩期不變；WULF 515.5 兩期不變）；賣方模型是否扣除 |
| 量綱 | 無因次 \((A_0/T)/Rent\)；年（T）；股數（稀釋） |
| 外部參照物（測一查證） | Plug Power 10-K FY2020（ASC 606 客戶認股權→營收抵減，原文已讀，§3-4）；對照組 HUT（Google 對 River Bend 租約提供 financial backstop，3Q26 10-Q 全文「Google」僅 1 次、未見股權對價揭露） |
| 表達工具型態（只指名，不選券） | 美股、以第三方信用支撐之長租 AI 設施為主之非 REIT 出租方普通股；不選券 |
| 重疊 | L2-A#5 R3（鄰接，已讓出樞紐）；L13-A#4／#5（融資成本未入利息之同族，側別不同） |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論；SEC 皆經 `tools/sec.py` 全文實讀）

1. **Cipher Digital 10-Q 3Q26**（2026-11-02）https://www.sec.gov/Archives/edgar/data/1819989/000181998926000050/cifr-20260930.htm ：Note 16「as consideration for Google agreeing to backstop certain obligations of Fluidstack … issued to Google a warrant to purchase 24,178,576 shares … exercise price of $ 0.01」；「if … the value of the Warrant Shares does not equal or exceed $ 435.0 million, the Company shall be obligated to issue additional Warrant Shares and/or make a cash payment」；「recorded an asset of $ 544.5 million in Other noncurrent assets … will amortize this asset over the life of the lease on a straight-line basis」；Note 12 Fluidstack 租約「10-year term」，2026-09 修約移除兩次五年續租選擇權並與「a leading AI lab」簽 10 年接續租約（「aggregate 20-year contracted term」），出租方自擔超支前 359.3 百萬美元；Adj. EBITDA 調節表含「Change in fair value of warrant liability (127,180)」（3Q26）、無攤銷列；認股權負債 525,160 → 504,880（千美元）。
2. **TeraWulf 10-Q 2Q26**（2026-08-05）https://www.sec.gov/Archives/edgar/data/1083301/000108330126000166/wulf-20260630.htm ：Google Warrants 73,580,000 股、$0.01；「recorded an asset of $ 515.5 million … in deferred charges … will amortize this asset over the life of the Fluidstack HPC Leases on a straight-line basis」；Fluidstack「initial 10-year term and two five-year renewal options」、一案已部分起租；Adj. EBITDA 定義排除「change in fair value of warrant liabilities」；1H26「Change in fair value of warrants」損失 971,992（千美元）。
3. **TeraWulf 8-K**（2026-11-04）https://www.sec.gov/Archives/edgar/data/1083301/000162828026069810/wulf-20261104.htm ：Justified 三案 Google Credit Support Agreements（Anthropic 20 年、約 401 MW）；對價型態改為「upon payment of such termination fee, Google would be entitled to acquire an equity interest in Raylan」；擔保於 Anthropic 取得投資級評等滿三個月即終止——第二型對價（或有子公司股權），測一須判定是否另有 \(A_0\)。
4. **Plug Power 10-K FY2020** https://www.sec.gov/Archives/edgar/data/1093691/000155837021007147/plug-20201231x10k.htm ：「waived the remaining vesting conditions under the warrant … issued to Amazon … which resulted in a reduction to revenue of $399.7 million, resulting in negative consolidated revenue of $93.2 million」（外部參照物：客戶側之同型股權對價入營收抵減）。
5. **Hut 8 10-Q 3Q26**（2026-11-04）https://www.sec.gov/Archives/edgar/data/1964789/000119312526446146/hut-20260930.htm ：River Bend「lease agreement is supported by a financial backstop provided by Google LLC」；未見認股權或遞延費用（對照組）。
6. 合約總額錨（利害方二手，測一須回 8-K 原文）：Blockworks「Cipher Mining inks $3B AI hosting deal with Fluidstack」https://www.blockworks.co/news/cipher-mining-inks-3b-ai-hosting-deal-with-fluidstack ；The Block「$3.7 billion 10-year AI compute deal」https://www.theblock.co/amp/post/366959/bitcoin-miner-terawulf-shares-jump-50-after-google-secures-8-stake-as-part-of-3-7-billion-10-year-ai-compute-deal 。

缺段（§7-2）：未見任何樣本已開始攤銷之損益表列（核心未決點）；未取具名賣方模型原文（本輪搜尋 `Google backstop warrants … EBITDA analyst` 只得新聞與逐字稿索引，0 筆賣方口徑）；IREN、GLXY、APLD 是否有同型第三方擔保對價未查；WULF 擴約後之 Fluidstack 年租金未取。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 信用支撐之經濟實質為融資成本（Google 認股權質押予 2030 Secured Notes 貸款人、使專案債可發行），排除於 EBITDA 與排除利息一致；EV 已含稀釋股數，市場以完全稀釋市值定價即已計入 | WULF 10-Q 質押句（§3-2）；EPS 稀釋表（§3-1） | 已定價（稀釋路徑） |
| R2 | 攤銷若入「lease revenue」抵減（同 Plug／ASC 606 類比或 ASC 842 lease incentive 類比），則 EBITDA 已含成本，恆等式不咬合 | 待 WULF 3Q26 10-Q／CIFR 起租季 | 科目已內含 |
| R3 | 量級：`[D]` 9%–18% 為租期均攤之一次性對價；以 \(A_0\)÷市值計約為已發生之稀釋，非持續現金流出 | 本卡 §1 | 量級不足（同 L2-A#2／#5 型） |
| R4 | 擔保可提前終止（WULF Justified：承租人投資級即終止），然攤銷依合約期——若提前終止則 \(A_0\) 剩餘一次減損，揭露反而清楚 | WULF 8-K（§3-3） | 揭露機制存在 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀 ≥ 3 家 AI 出租方（CIFR、WULF 必讀；HUT、IREN、GLXY、APLD 擇取）10-Q／10-K／8-K，可由同檔或同期申報取得「第三方信用支撐對價 \(A_0\)＋攤銷政策＋Adj. EBITDA 定義」三項者 < 2 家（不可觀測）；或
(2) `[D]` \((A_0/T)/\text{年基本租金}\)（年租金取申報之未來最低租賃收入表或 8-K 合約總額÷租期；T 取公司自述攤銷期）於可觀測樣本皆 < 5%（門檻凍結於此）；或
(3) 任一已起租樣本之攤銷列入營收抵減或營業成本且未於 Adj. EBITDA 加回（R2 成立）；或具名賣方原文已扣除信用支撐成本或以完全稀釋 EV 明示處理（R1 已定價）；或未能取得任何以 EBITDA／每 MW 收益定價之具名原文（落差無市場端）；或
(4) 可運作之對照只能寫成利息資本化（L2-A#2）、直線化／預收攤轉（L2-A#5）、可轉債全成本（L13-A#4）或子公司 PIK（L13-A#5）——即測一判定 \(A_0\) 實質為融資成本、應以資本成本處理；或
(5) 12 個月內無檢驗事件（WULF 3Q26 10-Q、CIFR 4Q26 10-K（Barber Lake 起租季）之攤銷列；WULF Justified 案是否另記 \(A_0\)；Adj. EBITDA 定義變更）；或
(6) 攤銷不改變任何被定價之財報科目（§7-4），例如 \(A_0\) 於起租前即全額減損或重分類至權益。

複查觸發器（若日後殺）：任一樣本首次於損益表列示信用支撐資產攤銷並於 Adj. EBITDA 加回；SEC 意見函就第三方擔保對價之科目或非 GAAP 處理提問；新增第三方擔保之租約另發股權對價（≥ 2 家）。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Other noncurrent assets／Deferred charges（信用支撐資產）、其攤銷列、Warrant liability 與公允值變動、Adj. EBITDA 調節表。2. 可交易工具：受第三方擔保之 AI 出租方普通股（不選）。3. 半衰期：起租後首份 10-Q 即揭露攤銷科目；攤銷期 10–20 年。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0169；`query/ARCH_matrix.md` L2［A］加「#6 已生成」；`AIM_FUNNEL.md` 日期行與 §3；`export/LEADS_算力收支.md` 追加 3 列（CIFR 信用支撐資產、CIFR 自擔超支額、WULF 信用支撐資產）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L2-A／#2–#5、L2-P／#2–#6、L2-I／#2–#5、L13-A#4／#5、L12-A#5、C-A3；不寫 T。
