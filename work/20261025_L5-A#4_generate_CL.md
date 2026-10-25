# L5-A#4 生成卡｜儲存與 IO：會計恆等（合資表外資本支出恆等：Sandisk 經濟資本支出 ≡ 自有 PP&E＋FV 票據／股權淨撥款＋租賃融資份額＋FV 自身營運現金流再投資；FCF 只扣前兩項）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260926_L5-A_generate_GK.md；archive/drive/USED_20260926_L5-A_test1_GK.md；archive/work/20261011_L5-A#2_generate_CL.md；work/20261011_L5-A#2_test1_CL.md；archive/work/20261017_L5-A#3_generate_CL.md；work/20261017_L5-A#3_test1_CL.md；work/20261011_L5-I#2_test1_CL.md；query/ARCH_live.md 列 L3-A#4、L5-I#3 | EMITS: work/20261025_L5-A#4_generate_CL.md -->
**日期：** 2026-10-25　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L5-A　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L5-P#4 本日測一，Q-0104 done）。各非殺、非排除格之最後測試日最舊＝**L5-A**（#3，2026-10-17）；既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `Sandisk`、`Flash Ventures`、`Kioxia`，**命中 0 筆**。載體全由 `sec.py` 與下列 fetch 取得。內部數字（§12）未取用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L5-A#1**（GK；(1) 觸發）：`C_io = V_KV × P_bit`，雲端儲存美元行不在申報層。本卡不涉 KV、雲端。
  - **L5-A#2**（(2)(4) 觸發）：HDD 營收量價分解，死於共識與同容量點價不可拆。本卡非營收分解。
  - **L5-A#3**（(3)(6) 觸發）：Everpure 毛利混合恆等，死於權利金占比 minimal 與毛利為政策變數。本卡非毛利混合，主體換 NAND 製造商，恆等式在**現金流／資本支出之表內外分界**。
  - **L5-I#2**（JV 雙邊同意之供給誘因；(1)(2) 觸發）：本卡不主張供給擴或不擴、不主張 NAND 價方向；只問同一筆已公布之投資在 Sandisk 報表落在哪一科目。
  - **L5-I#3**（長約保障比；客戶預付／擔保）：本卡不以客戶 NBM 預付為落差（亦排除 L13-A#2 客戶預付入 OCF 型）。
  - **L3-A#4**（Intel 合資晶圓廠 NCI）：同為「合資」但彼為**合併**主體之少數股權歸屬；本卡為**未合併**權益法主體之表外融資，且不以 NCI 為落差。
  - **C-A3／C-A4**（帳面折舊年限）、**C-P1**：不同型；本卡不主張折舊年限。重疊列為否決 (5)。
- §7-10 領域最近公開：Sandisk FY26 10-K（期末 2026-07-03，申報 2026-08-17）；FY26 Q4 財報 8-K（2026-08-05）；Kioxia／Sandisk ¥5 兆投資公告（2026-08-28）。下一檢查點＝Sandisk 1Q FY27 財報與 10-Q（約 2026-11 上旬；公司未公告日期前不作 `[V]`）。

## 1. 落差一句

Sandisk 全部晶圓來自未合併之 Flash Ventures（FV，持股 49.9%，權益法），FV 之設備投資由四源支應：Sandisk／Kioxia 之票據與股權撥款（入 Sandisk 投資活動）、**售後租回之租賃融資**（Sandisk 保證 50%，不入 Sandisk 現金流量表）、FV 自身營運現金流（來自晶圓「cost plus a small markup」之價款，即經 Sandisk 銷貨成本）、日本政府補助。恆等：
`I_SNDK ≡ PPE_own ＋ (N_out − N_in ＋ E) ＋ Λ ＋ R`，其中 `Λ`＝新增租賃融資之 Sandisk 份額，`R`＝FV 營運現金流再投資之 Sandisk 份額。公司 FCF＝OCF − `PPE_own`；Adjusted FCF 再加「Activity related to Flash Ventures, net」（即 `N`、`E`）；**`Λ` 與 `R` 均不在任何 FCF 口徑中扣除**。10-K 原文：「Funding commitments assume no additional operating lease guarantees. Additional operating lease guarantees can reduce funding commitments.」——即租賃保證可替代現金撥款。種子主張：¥5 兆（2032 前）擴產期內，`Λ` 之占比決定「Adjusted FCF」與「扣除全部經濟資本支出後之 FCF」之差；此差可由 10-K／10-Q 之保證餘額增量（`ΔG`＋當期本金攤還）近似觀測，而市場以 Adjusted FCF 口徑外推。本卡不定方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（資本支出之表內外分界）；非守恆、非誘因、非量價或毛利混合 |
| 選擇者 | FV 之融資組合由 Sandisk 與 Kioxia 共同決定（租賃可得性受「investor capacity and risk allocation policies」限制，10-K 原文），非 Sandisk 單方 |
| 可見端（`[V]`，A1／A2） | FY26：`PPE_own` 177（百萬美元）；票據撥出 462、收回 187；FV 淨活動 −275；FCF 11,494；Adjusted FCF 8,743；營收 20,248。資產負債表「Notes receivable and investments in Flash Ventures」678（FY25 654）。租賃保證餘額 ¥149.0B／923（本金攤還 565＋期末購買選擇權 358；FY27 到期 378）。最大可估損失 2,897（票據 577、股權 102、租賃保證 923、存貨與預付 1,295）。Flash Ventures related commitments 6,559（1 年內 2,627），註：含「depreciation reimbursement and lease payments on owned and committed equipment, funding commitments for loans and equity investments」 |
| 可見端（二手） | CFO（FY26 Q4 法說，二手 A4）：「CapEx dollars increasing year-over-year」「capital intensity will decline to approximately 6% of revenue」。`[D]` FY26 `PPE_own` ÷ 營收 ≈ 0.9%；(`PPE_own`＋FV 淨撥款) ÷ 營收 ≈ 2.2%——與「≈ 6%」之差即公司口徑之「gross capex」含表外份額之跡象（口徑待測一以逐字稿原文確認） |
| 指名不可見端 | FV 當期總資本支出及其融資組合（租賃／撥款／自身 OCF／補助）；`Λ` 之季序列；公司「capital intensity」之精確定義；¥5 兆中 Sandisk 份額（B&F 稱產出約 60／40，與 10-K「generally equals 50% each」不一致，待測一釐清） |
| 主張 | 恆等式於公開層可給 `Λ＋R` 之區間（gross capex 口徑 − 現金流量表口徑）；若 FCF 共識未扣該區間，構成可測落差；可被公司以 gross／net capex 並列揭露或具名賣方已以 gross 口徑建模拒絕 |
| 表達工具型態（只指名，不選券） | 美股 NAND 製造商（Sandisk）。不選券 |
| 重疊 | L5-I#2（同主體同 JV，誘因型）、L3-A#4（合資，NCI 型）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. A1 Sandisk FY26 10-K（Note 10 Related Parties／Flash Ventures；Liquidity 之 Material Cash Requirements；Off-Balance Sheet）。https://www.sec.gov/Archives/edgar/data/2023554/000162828026057406/sndk-20260703.htm
2. A2 Sandisk FY26 Q4 財報 8-K ex99.1（FCF／Adjusted FCF 定義與調節）。https://www.sec.gov/Archives/edgar/data/2023554/000162828026053346/sndkq4-26ex991xpressrelease.htm
3. A3 Sandisk FY26 Q3 10-Q（保證餘額前期值）。https://www.sec.gov/Archives/edgar/data/0002023554/000162828026029401/sndk-20260403.htm
4. A4 FY26 Q4 法說摘要（二手，GuruFocus 2026-08-05）。https://www.gurufocus.com/news/9009608/sandisk-corp-sndk-q4-2026-earnings-call-highlights-record-revenue-and-eps-driven-by-ai-data-center-surge
5. A5 ¥5 兆投資（二手，Blocks & Files 2026-08-28）：「more than $31 billion (¥5 trillion) to increase NAND output」「contingent upon continuing Japanese government support」；Fab3 FY2029、約 ¥1.8 兆。https://www.blocksandfiles.com/flash/2026/08/28/sandisk-and-kioxia-have-yen-for-new-nand-fabs/5293245
6. A6 TIKR 2026-08-31（二手）：投資「largely channeled through their joint venture」、Sandisk 份額「flows as contributions and equipment rather than a separate check」。https://www.tikr.com/es/blog/sandisks-record-japan-bet-runs-into-its-own-capital-efficiency-story
7. 測一須另取：FY26 Q4 法說逐字稿原文（capital intensity／gross capex 定義）；FY25 10-K 與 FY26 各 10-Q 之保證餘額（¥）序列；Kioxia 有價證券報告書或決算說明之 FV 設備投資額與租賃融資額（若可得）；WDC 時期 gross vs net capex 口徑之歷史原文；具名賣方 FCF 模型是否扣 FV 份額；1Q FY27 10-Q（sec.py）。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 公司自設 Adjusted FCF 已納入 FV 淨活動，且管理層以「capital intensity ≈ 6%」公開 gross 口徑 | A2；A4 CFO | 已揭露，落差即共識 |
| R2 | 租賃付款與折舊經晶圓價格入 Sandisk 銷貨成本（「depreciation reimbursement and lease payments」，A1），`Λ` 只是時序遞延，終入損益 | A1 | 無經濟落差，只有時序 |
| R3 | 租賃可得性受限（「not guaranteed」，A1），`Λ` 占比可能下降，表外份額自然收斂 | A1 | 落差無持續性 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 公司原文（逐字稿或申報）已定義並量化 gross capex（含 FV 份額，分列租賃融資部分），且與現金流量表口徑之差逐季可對帳（落差即揭露）。
(2) 具名賣方或評等機構已以 gross 口徑（含 FV 租賃份額）計 FCF 或以之定價（落差即共識）。
(3) 保證餘額（¥）序列 ≥ 4 期顯示 `ΔG`＋本金攤還 相對 Adjusted FCF 低於 2%（`Λ` 量級不足以改變任何 FCF 口徑判讀）。
(4) 申報層無可近似 `Λ` 或 `R` 之科目（保證表、承諾表、最大損失表皆不可推增量），且無替代科目可拒絕（§7-4 財報科目題不可答）。
(5) 可運作對照只能寫成 JV 供給誘因（L5-I#2）、合資 NCI 歸屬（L3-A#4）、客戶預付入 OCF（L13-A#2／L5-I#3）或折舊年限（C-A3／C-A4）。
(6) R2 成立且時序遞延 ≤ 1 個財年（租賃付款於當期或次期即入銷貨成本），使表內外分界無半衰期可捕捉。

複查觸發器（若日後殺）：Sandisk 首次於 10-Q／10-K 或財報 8-K 分列 FV 總資本支出與其租賃融資份額；或保證餘額（¥）較前期增加逾一倍；或公司改變 FCF／Adjusted FCF 定義納入租賃保證增量。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：現金流量表 PP&E 與 FV 票據行；Note 10 保證表、承諾表、最大可估損失表；Adjusted FCF 調節。
2. 可交易工具：Sandisk 美股（不選券）。
3. 半衰期：¥5 兆擴產窗（至 2032；Fab3 FY2029）vs 租賃攤還（現有保證 2027–2031）。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0105；`query/ARCH_matrix.md` L5［A］標「#4 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 兩筆（Sandisk FY26 Datacenter 營收；Kioxia／Sandisk ¥5 兆投資）。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L5-A#1–#3、L5-P#1–#4、L5-I#1–#3、L3-A#4、C-P1 結論。
