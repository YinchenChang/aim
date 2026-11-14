# L13-P#6 生成卡｜資本與融資結構：守恆（次級市場股數吸收守恆：ATM 每賣出一股必由次級市場某買方於同日成交量內吸收——ATM 售股 ≡ 參與率 π × 成交量；故發行人可實現之股權融資額受 π × 美元日均成交額 × 交易日數封頂，而非受授權額度封頂）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20261002_L13-P_generate_GK.md；archive/work/20261013_L13-P#2_generate_CL.md；archive/work/20261020_L13-P#3_generate_CL.md；archive/work/20261028_L13-P#4_generate_CL.md；archive/work/20261104_L13-P#5_generate_CL.md；work/20261104_L13-P#5_test1_CL.md | EMITS: work/20261114_L13-P#6_generate_CL.md -->
**日期：** 2026-11-14　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 3→4／6）　**格：** L13-P　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L13-A#6 測一 2026-11-14，Q-0200 done）。非已殺／刻意排除格中最後測試日最舊＝2026-11-04（L13-P、L13-I、L14-P、L14-A、L14-I、L15-P）；依表序取 **L13-P**。既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `tokenomics_leads.py ATM equity issuance`＝0 筆；未用。
- SEC（CLAUDE.md §10）：本輪 `sec.py filings` 被宿主隱私外掛拒絕（UA 內建聯絡 email）＝**無法判定（失敗歸因：宿主）**；非存在性主張（§7-2）。本卡 B 端載體之申報層一律留給測一經 sec.py 實讀；本輪只用發行人新聞稿與二手報導。
- 比對之舊檔與死因型態，本卡須異型：
  - **L13-P#1**（GPU 熱循環 vs 會計年限）：不涉硬體。
  - **L13-P#2**（礦企站址 MW 互斥＋子公司限制性支付）：不涉站址或債約。
  - **L13-P#3**（超大雲發行人來源＝用途按季封閉；死因＝表外量級、僅總額）：#3 之封閉在發行人現金流量表；本卡之封閉在**次級市場成交量**（股數維度），守恆量為「當期可被吸收之新股數」，與發行人用途無關。
  - **L13-P#4**（單一對手方 OpenAI 跨供應商承諾）：不涉需求方。
  - **L13-P#5**（信用市場持有者出清；死因＝已定價、讓價利息 ÷ OCF 不可分離）：#5 在債券持有者類別、以利差出清；本卡在**股權次級市場、以參與率與時間出清**，出清變數為天數與價格衝擊，不是利差。
  - **L13-A#3**（Oracle ATM 之 EPS 分母加權時滯；會計恆等）：同一 ATM 事實，但 #3 問分母何時入帳；本卡問**授權額度能否於窗內被吸收**。不改其結論。
  - **L13-A#4**（可轉全成本）、**L13-A#6**（募後利息收入遞減）、**L13-I** 系列（評等、擔保、認股權）：本卡不以會計認列或評等為樞紐。
  - **C-A4／C-A3**：不涉；不重開。**T-15**（CoreWeave，委託資本外）：不涉、不用為載體。
- §7-10 領域最近公開：IREN Q1 FY27 新聞稿 2026-11-05；Oracle Q1 FY27 （期末 2026-08-31）第三方申報整理 2026-10-08；IFR 2026-02 月第 2619 期；rallies.ai 2026-04-16。IREN／Oracle 10-Q 原文日期留給測一以 sec.py 確認。

## 1. 落差一句

AI 基建發行人之股權融資以 ATM 授權額度公告（Oracle US$20bn，2026-02；IREN 由 US$1.0bn「已用畢」擴為 US$6.0bn，2026-04），市場讀數以「授權額度＝可得資金」與「稀釋懸頂」兩分；但 ATM 為逐日於次級市場賣出（dribble out），每股必於當日成交量內被吸收，故**窗內可實現股權融資 ≤ π × 美元日均成交額 × 交易日數**（π＝發行人參與率，實務常引 5–15% ADV〔二手、待證〕）。種子主張：授權額度與可吸收額度之比 κ ＝ 授權 ÷ (π × $ADV × 窗日數) 若 > 1，則剩餘資金缺口須轉由債／預付／資產層融資補足，或以價格讓步（衝擊成本）出清；且 $ADV 與股價同向，股價下跌同時降低每股所得與可吸收股數之美元值（雙重壓縮）。本卡不主張方向與量級，只立可拒絕之「ATM 實現速度可由申報股數 ÷ 同期成交量量化，且與資本支出缺口可並列」。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆（P）**：股數存量封閉。ΔS_ATM,t ≡ 次級市場淨吸收股數；ΔS_ATM,t ＝ π_t × Vol_t；所得 ＝ Σ_t π_t × Vol_t × P_t（扣佣）；缺口 G ＝ capex − OCF − 債 − 預付；κ ＝ 授權 ÷ (π × $ADV × T) |
| 驅動（因果層，§7-5） | 資本支出排程與客戶預付比例（缺口上游）、股價與成交量（吸收端）、發行人與承銷代理之參與率上限（價格衝擊控制）、公開流通量 1/3 年度上限（S-3 baby shelf 不適用於大型發行人） |
| 量綱 | 股數［股／日］；參與率 π［比率］；美元成交額［美元／日］；授權與所得［美元］；κ［無量綱］ |
| 可見端 | 10-Q／10-K 股東權益變動表與期後事項之 ATM 售股數與淨所得；8-K 授權與完成公告；交易所日成交量；新聞稿資金來源表 |
| 指名不可見端 | 逐日 ATM 售股（多數發行人僅季揭露）；代理實際參與率上限；大宗配售與 ATM 之混合 |
| 外部參照物（測一查證） | 具名學術：Billett、Floros、Garfinkel〈At-the-Market Offerings〉JFQA 54(3), 2019——「Firms take down less than half of the announced ATM program allocation, on average」；takedown 與當季股價正相關。測一另找單一產業 ATM 授權遠超實現之一手前例（如 2021–22 礦企或 REIT） |
| 表達工具型態（只指名，不選券） | 美股上市 AI 基建發行人普通股（IREN、Oracle 及同型以 ATM 為主要股權來源之資料中心／礦轉 AI 主體）；不選券 |
| 重疊 | L13-A#3（同一 ATM 事實、會計時滯）、L13-P#3（發行人封閉）、L13-P#5（債市出清）、L2／L6 capex。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. IREN Q1 FY27 新聞稿（GlobeNewswire，2026-11-05）https://globenewswire.com/news-release/2026/11/05/3397020/0/en/iren-reports-q1-fy27-results.html ：「$15 billion remaining planned FY27 capex expected to be met by:」→「$9 billion of cash and committed GPU financing and prepayments」＋「$6 billion of target GPU financing, prepayments, data center financing and other corporate level sources」；現金及約當 3,522（2026-09-30）vs 5,896（2026-06-30）；現金流量表發行普通股所得 498（9 月季）vs 2,112（6 月季）〔讀取經摘要，測一以 10-Q 原文核〕。一手（利害方）。
2. rallies.ai（2026-04-16）https://rallies.ai/news/iren-slides-as-6-billion-at-the-market-share-sale-authorization-weighs-on-sentiment ：「up to $6.0 billion in ordinary shares」、取代「the prior $1.0 billion program, which it said had already been fully used」。二手；授權本身測一以 424B5／8-K 實讀。
3. blockspace.media（2026-03-05）https://blockspace.media/insight/iren-expands-gpu-fleet-to-150000-opens-6b-equity-offering ：「the largest ever for a bitcoin miner」；J.P. Morgan（2026-02）稱 IREN「a significant funding gap」。二手。
4. IFR 第 2619 期（2026-02-07–13）https://www.ifre.com/equities/2379787/oracle-takes-bottom-up-approach-to-funding-2026-capex 與 https://prod.ifre.com/bonds/2381048/us50bn-funding-blitz-shows-oracles-market-access-and-its-vulnerability ：Oracle「as much as US$20bn of new shares over the coming weeks via an at-the-market programme」；「Each leg lower in its share price will bring additional dilution」。二手。
5. sec-api.io 整理（2026-10-08）https://sec-api.io/insights/oracle-corporation-orcl-financial-and-ratio-analysis-q1-fy2027-filings-cloud-backlog-debt-and-capital-spending-scenarios-to-fy2030 ：「sold 141m common shares for $19.9bn in Q1 FY2027」、程式「fully used」（引 10-Q 0001193125-26-389274 與 2026-09-10 8-K）。二手轉述申報；測一以 sec.py 實讀。**已實現之對照案**：Oracle 單季吸收 ≈ 141m 股（約 63 交易日 → 約 2.2m 股／日〔D，待成交量核〕）。
6. 參與率慣例（二手、待證）：ibinterviewquestions.com（2026-05-05）https://ibinterviewquestions.com/guides/equity-capital-markets/at-the-market-atm-programs-dribble-out-mechanics 經摘要稱「5 to 15% of average daily volume」——**未經逐字核**，測一不得直接採用；須以律所實務文件（Mayer Brown／Cleary 等）或發行人揭露之參與率核。
7. 缺段（§7-2；測一取）：IREN 10-Q 期 2026-09-30 之 ATM 售股數、均價、剩餘額度；同期 IREN／Oracle 日成交量（交易所或公開行情）；其他以 ATM 為主之 AI 基建發行人（CIFR、WULF、APLD、HUT、CORZ 等）授權 vs 實現。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 大型高流動性發行人單季即可吸收整個授權（Oracle US$20bn「fully used」於一季） | #5 | 不綁定 |
| R2 | 發行人資金表以 GPU 融資、客戶預付（「90% of the GPU capex prepaid by the customer」）為主，ATM 為邊際來源 | #1 | 機制成立但不可分離 |
| R3 | 稀釋懸頂已被即時定價（授權公告日股價下跌 4.7%） | #2 | 已定價 |
| R4 | Billett et al.：發行人平均只用不到一半授權，授權本就非承諾——市場不以授權額為可得資金 | 參照物 | 落差前提不成立 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無 **≥ 2 家** AI 基建發行人可同時取得季度 ATM 售股數（申報）與同期成交量，使 π 不可量化、κ 不可並列（L13-P#3 型「只有總額」死因）。
(2) 窗內 `[D]` κ ＝ 未用授權 ÷ (π × $ADV × 窗日數) 之區間上端 ≤ 1（π 取 5–15% 或申報反推值）——吸收不綁定（R1）。
(3) 發行人資金表中 ATM／普通股所得占剩餘 capex 缺口 < 10%，使吸收上限對資金缺口無可分離影響（R2）。
(4) 具名賣方或信評已**量化**發行人 ATM 實現速度 × 成交量之容量（不止定性「稀釋」語）——已定價（R3）。
(5) 重定價窗（≥ 12 個月）內無可觀測檢驗事件（季度 10-Q ATM 售股、授權擴大／完成 8-K、資金表更新），或其已全部於窗前公告。
(6) 外部參照物顯示授權額長期被市場以「上限、非承諾」讀取（R4 成立且有賣方模型以實現額而非授權額建模）——落差前提崩塌。

複查觸發器（若日後殺）：任一 AI 基建發行人於 10-Q 首次揭露逐月 ATM 售股或代理參與率；授權擴大後連兩季實現 < 授權 25%；發行人資金表首次將 ATM 由「cash」改列為「target」來源。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：股東權益變動表之發行股數與所得、期後事項、流動性段之資金來源表、加權股數。
2. 可交易工具：該發行人普通股；不選券。
3. 半衰期：ATM 按日；申報按季；授權按 8-K 不定期。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0201；`query/ARCH_matrix.md` L13［P］標「#6 已生成」；`export/LEADS_算力收支.md` 一筆（IREN FY27 剩餘計畫 capex，發行人新聞稿）。不寫入：FUNNEL、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L13-P#1–#5、L13-A#1–#6、L13-I#1–#5、C-A3／C-A4 結論；不寫 T-15。
