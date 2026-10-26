# L6-P#4 生成卡｜雲端與基礎設施服務：守恆（已通電機房之冷卻型態存量守恆：`K_air,t = K_air,0 − R_t`；舊世代 GPU 之供給與壽命由氣冷 MW 存量及其改造速率決定，而非折舊年限、電費或產品曆）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260928_L6-P_generate_GK.md；archive/drive/USED_20260929_L6-P_T_GK.md；archive/work/20261011_L6-P#2_generate_CL.md；work/20261011_L6-P#2_test1_CL.md；archive/work/20261018_L6-P#3_generate_CL.md；work/20261018_L6-P#3_test1_CL.md | EMITS: work/20261026_L6-P#4_generate_CL.md -->
**日期：** 2026-10-26　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3／6）　**格：** L6-P　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L5-I#4 本日測一，Q-0106 done）。最後測試日最舊＝2026-10-18（L6-P#3、L6-A#3）；依表序取 **L6-P**；非已殺、非刻意排除。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py H100 rental price vintage fleet`，回 14 筆，**相關 0 筆**（皆規格／BOM，無租價或機房冷卻型態）；載體全由 WebSearch／WebFetch／sec.py 原文取得。
- 比對之舊檔與死因型態，本卡須異型：
  - **L6-P#1**（T，同步作業 MTTF∝1/N）：可靠度守恆。本卡守恆量＝**已通電機房 MW 依冷卻型態之存量**。
  - **L6-P#2**（RPO 交付之 MW·h 上界；(1) ρ 不可界定）：以每 MW 營收換算交付上界。本卡不換算營收、不需 ρ；只用「每 MW 只能容納一種世代」與「氣冷 MW 不能容納機架級液冷世代」。
  - **L6-P#3**（可互換機群之用途分割；(2) 賣方已以份額建模）：守恆於**用途**間。本卡守恆於**世代 × 機房型態**間，選擇變數為改造速率 `R_t`，非分配份額。
  - **C-A3／C-A4**（ARCH_dead #5，折舊年限）：帳面耐用年限。本卡不論帳面，論舊世代之**實體供給上界**與退場觸發；重疊列為否決 (4)。
  - **L2-P#2**（kW／櫃封頂）、**L2-P#4**（MW 申報口徑）：資料中心層之密度與口徑。本卡為雲端層之**世代壽命與舊世代可售 GPU 時**；重疊列為否決 (4)。
  - **L4-I#4**（OEM 世代切換延後選擇權）：買方對新貨之延後。本卡為已裝機舊貨之退場。
- §7-10 領域最近公開：CoreWeave 10-Q（期末 2026-06-30，申報 2026-08-12）與 2Q26 法說（2026-08-12 報導）；Silicon Data H100 Hyperscaler Index 月報（2026-04-27）；Global Data Center Hub（2026-09-11）。下一檢查點＝CoreWeave 3Q26 10-Q 與法說（約 2026-11 中旬）、Nebius 3Q26（約 2026-11）、Silicon Data 月度指數。

## 1. 落差一句

公開敘事以兩種方式決定舊世代 GPU 之壽命與價格：帳面折舊年限（C-A3 型），或「每代每度電做更多事、電費使退役更划算」「退役時程由供應商產品曆決定」（Global Data Center Hub 2026-09-11）。**種子主張：在電力為約束之期間，舊世代之真實退場條件是 MW 槽位之機會成本，而 MW 並非跨世代可互換——機架級液冷世代（GB200／GB300 NVL72，報導稱 120–140 kW／櫃）無法進入為約 20 kW／櫃建造之氣冷機房（Tom's Hardware 2026-08-12：「The energized, air-cooled capacity holding them has no higher-value use」）。故守恆式 `K_air,t = K_air,0 − R_t`（`R_t`＝氣冷 MW 改造為液冷之累計量）給出舊世代可售 GPU 時之上界 `≈ K_air,t ÷ kW_old`；只要需求 > 供給且 `R_t` 慢，舊世代租價與合約期由氣冷存量支撐（CoreWeave：A100 合約至 2029、「pricing for prior generation SKUs is at or above where it was years ago」）；`R_t` 加速之時點才是舊世代退場波之觸發。** 落差＝若市場以折舊年限或電費模型估舊世代殘值／退場，而實際退場由改造速率決定，則舊世代收入之期限結構被誤估（方向不定：改造慢 → 長於預期；改造快且新世代供給充足 → 斷崖式短於預期）。

## 2. 機制型態

| 欄 | 內容 |
|---|---|
| 型態 | **[P] 守恆**：已通電 MW 依冷卻型態分割之存量－流量；每 MW 只容一世代；氣冷 MW 不容機架級液冷世代 |
| 守恆式 | `K_t = K_air,t + K_liq,t`；`K_air,t = K_air,0 − R_t`；舊世代可售 GPU 數上界 `N_old ≤ K_air,t ÷ kW_old`（含 PUE 口徑須於測一釘死） |
| 第一原理量 | `K_air`、`K_liq`（MW）；`R_t`（MW／季）；每 GPU 全系統 kW（A100／H100 氣冷 vs NVL72）；改造時長與成本 vs 新建液冷時長 |
| 判定量 `[D]` | `φ = K_air ÷ K_t`（具名 GPU 雲之氣冷占比）與 `R_t ÷ K_air`（年改造率）；舊世代合約剩餘期 vs `K_air ÷ R_t` |
| 可拒絕事件 | GPU 雲揭露機房冷卻型態分列或改造計畫；舊世代合約到期後之再簽價（CoreWeave：一批 H100 以原價 95% 再簽，CNBC 轉述）；租價指數之舊世代斷崖 |
| 表達工具型態（只指名，不選券） | 美股 GPU 雲（CoreWeave、Nebius）；超大規模雲。不選券 |
| 重疊 | C-A3／C-A4（年限）、L2-P#2（密度）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Tom's Hardware（Luke James，2026-08-12）轉述 CoreWeave 2Q26 法說：A100 合約至 2029；Intrator「pricing for prior generation SKUs is at or above where it was years ago」；CFO「older-generation ASPs at or above levels from a year ago」；DGX A100 6.5 kW、舊機房約 20 kW／櫃 vs NVL72 120–140 kW；contracted 4.2 GW vs 1.5 GW online。https://www.tomshardware.com/tech-industry/coreweave-ceo-mike-intrator-says-it-has-signed-an-a100-contract-running-into-2029
2. CoreWeave 10-Q（2026-06-30 期，acc 0001769628-26-000366；sec.py 實讀，`cooling` 4 筆、`useful life` 2 筆）：「third-party data centers are required to undergo extensive retrofitting and improvement efforts」；「cycling out older components of our infrastructure and replacing them with the latest technology」。氣冷／液冷 MW 分列 0 筆（`air-cooled`、`liquid cool`、`retrofit` 字串檢索 0）。https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm
3. Silicon Data，「H100 Hyperscaler Index, April 2026」（Carmen Li，2026-04-27）：2026-03-01 至 04-20 區間 7.40–7.52 美元／時，CV 0.47%；「Supply is contracted, not spot」；同期 B200 +24%。https://www.silicondata.com/blog/h100-hyperscaler-index-april-2026
4. Apollo，「The Growing Compute Shortage」（2026-06）：「older-generation chips are seeing rental rates increase to levels not seen since 2024」（引 SemiAnalysis 2026-04）；「Even if silicon constraints ease, power infrastructure remains a critical limiting factor」。https://www.apollo.com/content/dam/apolloaem/documents/insights/the-growing-compute-shortage.pdf
5. Nadella（podcast，TechRadar 2025-11-05 轉述）：「a bunch of chips sitting in inventory that I can't plug in」「I don't have warm shells to plug into」——電力／機殼為約束之原文錨。https://www.techradar.com/pro/you-may-actually-have-a-bunch-of-chips-sitting-in-inventory-that-i-cant-plug-in-satya-nadella-admits-an-embarrassing-shortcoming-so-lets-hope-it-doesnt-set-the-company-back-in-the-ai-arms-race
6. 公開框架代表：Global Data Center Hub（2026-09-11）：「Each generation does more work for each dollar of electricity」「the electricity bill alone makes retirement the cheaper option」「set by a supplier's product calendar」——未提 MW 槽位或冷卻型態。https://www.globaldatacenterhub.com/p/how-long-does-an-ai-chip-last-and
7. 測一須另取：CoreWeave、Nebius、IREN、Applied Digital 最近 10-K／10-Q 與法說（sec.py）之冷卻型態分列、改造計畫、舊世代合約到期表；Microsoft／Amazon／Google 對氣冷機房改造之一手（Microsoft「Fairwater」、AWS IRHX 等）；具名賣方（SemiAnalysis、Morgan Stanley、Bernstein）是否以機房冷卻存量或 MW 機會成本建模舊世代殘值／租價；Uptime Institute 或 JLL 之氣冷／液冷 MW 存量與改造速率；CNBC 原文「95%」再簽句。**不宣稱已錯價。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 舊世代高價來自全面算力短缺（GPU、記憶體、TSMC），非機房型態；短缺解除即回落 | Apollo #4（「GPUs are scarce, memory prices are surging, TSMC capacity is effectively sold out」） | 型態錯置：主因為短缺而非守恆 |
| R2 | 守恆已被公開陳述——「The energized, air-cooled capacity holding them has no higher-value use」 | Tom's Hardware #1 | 共識風險（否決 (2)） |
| R3 | 改造（加 CDU／後門熱交換）時長短、成本低，`R_t` 可隨需而快，存量不綁 | 測一須取具名工程／營運商原文 | 量級：`K_air ÷ R_t` 短於舊世代合約期 |
| R4 | 主要舊世代合約為長期 take-or-pay，收入期限已由合約鎖定，機房存量不改收入 | Silicon Data #3「Supply is contracted, not spot」 | 可捕捉性：落差不進收入 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 氣冷／液冷 MW（或改造量）於 ≥ 2 家 GPU 雲或超大規模業者之申報、法說或一手揭露皆不可取得，且無具名第三方（Uptime、JLL、CBRE、SemiAnalysis）存量估計，使 `φ` 與 `R_t` 皆不可觀測（量綱失敗）。
(2) 具名賣方或研究機構原文（非報導轉述）已以機房冷卻型態存量或 MW 槽位機會成本建模舊世代租價、殘值或退場時程，使落差為共識。
(3) `[D]` 可得之最寬假設下，具名 GPU 雲之 `K_air ÷ R_t`（以年計）≤ 其舊世代合約加權剩餘期之 0.5，或 `φ` < 10%，量級不足。門檻於本卡凍結，測一不得改。
(4) 可運作對照只能寫成折舊年限（C-A3／C-A4）、kW／櫃密度封頂（L2-P#2）、MW 申報口徑（L2-P#4）、用途分割（L6-P#3）或 RPO 交付上界（L6-P#2）。
(5) 原文顯示舊世代租價／再簽價之變動可由整體短缺指標完全解釋（R1 成立），且舊世代亦部署於液冷機房並被保留（即槽位非綁定條件）。
(6) 舊世代收入於主要主體為長約鎖定至 2029 以後（R4 成立），使 12 個月內無可觀測之再簽或退場事件。

複查觸發器（若日後殺）：任一 GPU 雲或超大規模業者於 10-K／10-Q／法說分列氣冷 vs 液冷 MW 或改造計畫；舊世代租價指數單季跌幅 > 25% 且同期改造公告；具名賣方以冷卻存量建模舊世代殘值。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：GPU 雲之 RPO 依世代或到期分列（多數不分列）、PP&E 中 GPU 與機房設施分列、改造資本支出。
2. 可交易工具：CoreWeave、Nebius、IREN、Applied Digital 美股；超大規模雲之雲端分部不可分離。
3. 半衰期：以舊世代合約到期與改造公告為檢驗事件；CoreWeave 3Q26（約 2026-11）；`[V]` 日期不寫。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L6［P］標「#4 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 線索 2 筆。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L6-P#1–#3、L6-A#1–#3、L6-I#1–#3、L2-P#2、L2-P#4、L4-I#4、C-A3、C-A4 結論。
