# L13-A#3 生成卡｜資本與融資結構：會計恆等（股權融資資本支出之 EPS 分母恆等：加權平均股數時滯＋強制可轉換特別股之 if-converted 切換與價格帶股數）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260928_L13-A_generate_GK.md；archive/drive/USED_20260929_L13-A_T_GK.md；archive/work/20261011_L13-A#2_generate_CL.md；work/20261011_L13-A#2_test1_CL.md；archive/work/20261017_L4-A#3_generate_CL.md；work/20261017_L4-A#3_test1_CL.md；work/20261013_L13-I#2_test1_CL.md | EMITS: work/20261020_L13-A#3_generate_CL.md -->
**日期：** 2026-10-20　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 0→1／6）　**格：** L13-A　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L6-I#3 2026-10-19 已測一，Q-0068 done）。非已殺／刻意排除格中，最後測試日最舊＝**L13-A**（#2 測一 2026-10-11，`work/20261011_L13-A#2_test1_CL.md`）；其餘格最後測試日 ≥ 2026-10-13。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py "mandatory convertible" "at-the-market" Oracle equity`，**命中 0 筆**。
- 比對之舊檔與死因型態，本卡須異型：
  - **L13-A#1**（T 不進 L）：入表租賃負債≠義務上界——負債端量測時點。本卡在**權益端**（普通股與特別股），不涉租賃。
  - **L13-A#2**（測一不通過，(1) 已定價）：客戶預付之現金流分類與融資增額。本卡不涉 OCF 分類；但同載體（Oracle），重疊照記。
  - **L4-A#3**（測一不通過）：客戶權證收入減項，死於 ASU 2019-08 授予日計量切斷股價→收入反身性。本卡物件＝**發行人自身籌資**之 EPS 分母（ASC 260 加權平均與 if-converted），非應付客戶對價；股價→股數之連動由合約條款（轉換率價格帶、ATM 按市價發行）直接給定，不經 ASC 606。
  - **L13-I#2**：出租方對擔保人發 $0.01 認股權（誘因／違約路徑）。本卡不論擔保。
  - **L12-A#3**（稅時序）、**L2-A#2**（利息資本化）、**L6-A#3**（CIP 折舊管線）、**C-A3／C-A4**（年限／重定價窗）：本卡不涉損益分子之時序，只涉分母。
  - **T-15**（委託資本外）：不寫；不以 CoreWeave 為主載體。
- §7-10 領域最近公開：Oracle FQ1 FY27 10-Q（期末 2026-08-31，申報 2026-09-11）。下一檢查點＝FQ2 FY27 10-Q（約 2026-12）——首個含 ATM 股數全期加權之季。

## 1. 落差一句

Oracle 依 2026-02-01 公告之「$45 to $50 billion」籌資計畫，半數以股權完成：(i) 6.50% Series D 強制可轉換特別股（帳面 4,954M；季配息 81M 自淨利扣除得「Net income available to common shareholders」）；(ii) $20B ATM，FQ1 FY27「fully utilized the ATM Program and issued 141 million shares … for net proceeds of $19.9 billion」（均價 ≈ $141）。恆等：
`EPS_t = (NI_t − PrefDiv_t) ÷ W_t`，`W_{t+1} − W_t ≈ Σ_j ΔN_j × (未在 t 期內之天數占比)`；FQ1 基本加權 2,966M vs 期末流通 3,024M → 即使淨利與他項不變，FQ2 基本分母機械性 ≥ +1.96%。特別股於 2029-01-15 強制轉換為每股「between 499.8126 and 624.7657」普通股（≈ 25.0–31.2M 股；價格帶 ≈ $160.06–$200.08），現行 if-converted 下列為「anti-dilutive」而排除於稀釋股數，但其股息已扣自分子；轉換時分子回加股息、分母加入 25–31M 股，且帶內股數與股價**反向**。種子主張：GAAP 稀釋 EPS 之序列在 FQ1→FQ2 與 2029 轉換時有可由條款事前算出之分母步升，若市場以 EPS（或指引之 adjusted EPS）趨勢外推而未逐期重算分母，即錯置。本卡不定方向與量級，只立可拒絕之恆等。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（ASC 260 每股盈餘分母：加權平均時滯＋if-converted 切換＋強制轉換價格帶）；非守恆、非誘因、非收入計量 |
| 量綱 | 股數［M 股］；ΔW／W 無量綱；PrefDiv［$］；轉換率［股／特別股］× 特別股數［M］＝［M 股］ |
| 可見端 | 10-Q 損益表與 Note 10（EPS 計算表、排除股數 64M 及其三類構成）；股東權益變動表「Common stock issued via at-the-market program 19,909」；現金流量表 ATM 行；Note（Stockholders' Equity）轉換率、強制轉換日、Final Averaging Period；8-K（2026-02）Certificate of Designations |
| 指名不可見端 | ATM 各日發行時點（只知季總數，故 FQ1 加權為推算）；共識 EPS 模型所用股數；adjusted EPS 是否以稀釋或基本股數計、是否加回特別股股息 |
| 主張 | 分母步升可由已申報之期末股數、條款事前計算；EPS 指引與共識若以舊股數為基即偏離。可由公司指引原文已含新股數、或具名賣方已逐期重算分母而拒絕 |
| 外部參照物（測一查證） | 前例：其他以 ATM／強制可轉換特別股為資本支出籌資之發行人（公用事業、REIT 慣用）之 EPS 指引是否內含稀釋——僅作會計路徑先例，非量級 |
| 表達工具型態（只指名，不選券） | 美股上市雲供給者普通股（Oracle 為主載體；Nebius、CoreWeave 之 ATM 為對照）。不選券 |
| 重疊 | L13-A#2（同載體不同科目）、L4-A#3（股價連動不同路徑）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Oracle FQ1 FY27 10-Q https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm （EPS 表、ATM 141M 股、期末 3,024M、排除 64M——`sec.py` 本輪實讀）
2. Oracle FQ3 FY26 10-Q https://www.sec.gov/Archives/edgar/data/1341439/000119312526101045/orcl-20260228.htm （轉換率 499.8126–624.7657、強制轉換日 2029-01-15、if-converted 排除——本輪實讀）
3. Oracle 8-K（特別股發行）https://www.sec.gov/Archives/edgar/data/1341439/000119312526039344/d63638d8k.htm （Final Averaging Period 定義——本輪實讀）
4. Oracle FWP（2026-02-01 籌資計畫）https://www.sec.gov/Archives/edgar/data/1341439/000119312526032650/d36096dfwp.htm （「approximately half of its 2026 funding through a combination of equity-linked and common equity issuances」——本輪實讀）
5. 對照：Nebius ATM 6-K https://www.sec.gov/Archives/edgar/data/1513845/000110465925109806/tm2530882d1_ex99-1.htm （未實讀，測一取）
6. 測一須另取：FQ1 FY27 法說逐字稿與新聞稿之 FY27 adjusted EPS 指引是否明言含 ATM 股數；FQ2 FY27 10-Q 加權股數（約 2026-12）；具名賣方 EPS 模型股數；FY26 10-K EPS 附註；CoreWeave／Nebius 同類 ATM 揭露。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 媒體已量化 ATM 稀釋並指出價格依存：「would now require issuing approximately 158 million shares, representing 5.5% of its outstanding shares」「compared to just 58 million shares (2.0%) at the peak price」 | StockTi（Daniel Marsh，2026-07-20）https://stockti.com/oracle-s-share-plunge-triples-dilution-from-20b-equity-plan | 已定價（稀釋已公開量化） |
| R2 | ATM 已於 FQ1 全數用畢、季總數已申報；分母步升為任何讀 10-Q 者可得之算術 | 10-Q 原文（#1） | 資訊已公開，無落差 |
| R3 | 特別股轉換 25–31M 股約占流通 0.8–1.0%，且 2029 落點遠於 12 個月窗之觀測 | 10-Q／8-K 條款（#2、#3） | 量級不足／窗不合 |
| R4 | 市場以 EV／EBITDA 或 FCF 估值，EPS 分母不入定價 | 測一須找具名來源 | 機制不入價格 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 公司 EPS 指引原文已明言以 ATM 後股數為基（或法說已量化分母影響），且具名賣方／研究機構已逐期重算股數——已定價（R1／R2 擴及主流口徑）。
(2) FQ2 FY27 基本加權股數相對 FQ1 之增幅 < 1%（例如回購抵銷），或特別股轉換股數 ÷ 流通股 < 1% 且 ATM 已無剩餘授權——量級不足。
(3) 共識 EPS 所用股數不可觀測，且公司不揭露 ATM 發行時點，致時滯量無法界定（不可觀測）。
(4) 可運作對照只能寫成 L13-A#2 現金流分類、L4-A#3 收入減項、L13-I#2 擔保認股權或 T-15。
(5) 主流估值口徑以 EV 基礎倍數為主、EPS 分母變動無價格反應之具名證據（R4 成立）。

複查觸發器（若日後殺）：Oracle 或任一雲供給者新授權 ATM ≥ 流通市值 5%；或公司發行第二檔強制可轉換特別股；或 adjusted EPS 定義改為排除特別股股息。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：EPS 附註（基本／稀釋加權、排除股數）；股東權益變動表 ATM 行；特別股股息；轉換條款。
2. 可交易工具：美股雲供給者普通股（不選券）。
3. 半衰期：ATM 時滯於下一季（FQ2 FY27，約 2026-12）全數入分母；特別股轉換 2029-01-15（Final Averaging Period 前 20 交易日）。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L13［A］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L13-A#1 之 T、L13-A#2、L13-I／#2、L13-P／#2、L4-A#3、C-A3／C-A4 結論；不寫 T-15。
