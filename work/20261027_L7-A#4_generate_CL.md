# L7-A#4 生成卡｜模型層：會計恆等（可互換之承諾算力按工作負載分攤：功能別毛利率 vs 性質別算力率之口徑恆等）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；query/QUEUE.md；archive/work/20261020_L7-A#3_generate_CL.md；archive/work/20261027_L7-P#4_generate_CL.md；work/20261027_L7-P#4_test1_CL.md；work/20261020_L7-A#3_test1_CL.md；work/20261013_L7-A#2_test1_CL.md；export/LEADS_算力收支.md | EMITS: work/20261027_L7-A#4_generate_CL.md -->
**日期：** 2026-10-27　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1→2／6）　**格：** L7-A　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額配置、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L7-P#4 已測一，Q-0111 done）。非已殺／刻意排除格中，最後測試日最舊＝2026-10-20 一組（L7-A/I#3、L10-P/A/I#3、L11-A/I#3、L13-P/I#3、L14-P#3）；同日以 QUEUE 序決勝（沿 L13-A#4／L7-P#4 卡之規則），最早＝**L7-A#3**（Q-0071）。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py "gross margin" "inference cost" "training compute" Anthropic`，命中 16 筆；相關 2 筆：SRC_DEM_004／005（The Information〈Why OpenAI, Anthropic Missed Their Own Gross Margin Forecasts〉，付費牆未讀；OpenAI 非付費用戶推論支出）。只作指名，不作證據；本卡數點全取自公開 S-1 原文（sec.py 實讀）。
- 比對之舊檔與死因型態，本卡須異型：
  - **L7-A#1**（測一不通過）：列表價 vs FLOP／單位成本不可並列。本卡不論單價或 FLOP，只論**同一筆總算力費用在功能科目間之分攤**。
  - **L7-A#2**（部分通過）：持股方公允價值計量。本卡在實驗室本身之費用分類。
  - **L7-A#3**（部分通過）：市集總額認列 × 分潤列 S&M（營收側口徑）。本卡為**成本側**口徑（cost of revenue vs R&D vs S&M 之算力分攤），不論 gross／net。
  - **L7-P#4**（部分通過）：KV 占用 × 平價計價之 1/L 斜率（物理守恆）。本卡不論上下文，只論會計分攤；其測一 B 段 `[D]` 功能別毛利率序列為本卡之起點數點，不改其結論。
  - **L7-P#3**（不通過）：GW→營收總量上界。本卡不經容量。
  - **C-A3／C-A4**（折舊年限）、**L6-A#3**（折舊起點）、**L6-A#4**（capex 繞道）：本卡不論資本化或折舊，S-1 之 compute and infrastructure 已含租賃與折舊，分攤問題與其正交。
  - **C-A5**（死 #13，API 單價不可分離／L7 未上市）、**C-P3**（死 #16，權重更新支出非獨立科目）：S-1 已公開 Note 8 功能別表，C-P3 所稱「非獨立科目」之一部已可觀測（R&D 含模型開發算力）；C-A5／C-P3 複查觸發器屬 SCOUT-WATCH，本卡不代判。
  - **T-15**：無關，不寫。
- §7-10 領域最近公開：Anthropic 公開 S-1（EDGAR，2026-10-26）；Zitron（2026-05-21）、Augment（Paul Smalera，2026-06-04）、Futurum（Nick Patience，2026-06-02）均為 S-1 公開前。下一檢查點＝S-1/A、SEC 意見函（CORRESP）、上市後首份 10-Q。

## 1. 落差一句

恆等：`C ≡ C_serve + C_free + C_dev`（性質別 compute and infrastructure ＝ 功能別 cost of revenue 內算力 ＋ S&M 內免費存取算力 ＋ R&D 內模型開發／研究／內部使用算力）。功能別毛利率 `GM_f ≡ 1 − (C_serve + X)/R`（X＝COR 內人員與分攤），性質別算力率 `GM_c ≡ 1 − C/R`；兩者差 `(C_free + C_dev − X)/R`，且 `α ≡ C_serve/C` 之決定為管理層對**同一批可互換之多年承諾算力**按工作負載之分攤判斷，非外部價格。
已見數點（本輪 sec.py 實讀公開 S-1，M$）：
- 性質別損益表：營收 2025 4,585、1H25 1,163、1H26 16,286；compute and infrastructure 2025 7,326、1H25 2,334、1H26 8,945（「driven by the delivery of committed compute … under our CSP arrangements」）。
- Note 8 功能別：cost of revenue 2025 2,773、1H25 1,019、1H26 2,380（「Substantially all … compute and infrastructure costs associated with customer-serving workloads」）；R&D 6,338／1,850／9,741（「model development, research, and internal usage workloads」）；S&M 911／239／3,808（含「compute and infrastructure costs associated with providing free access」）。
- 呈現變更：「During the year ended December 31, 2025, the Company changed its presentation … from a functional classification under which cost of revenue, gross profit (loss) … to a classification based on the nature of expenses」——毛利行自損益表面移除，功能別只留附註。
- `[D]`：`GM_f` 1H25 12.4%→1H26 85.4%；`GM_c` −100.7%→45.1%；`α` 上界（COR ÷ C）43.7%→26.6%（2025 37.9%）；口徑差 113→40 pp。營收 ×14 期間服務分攤占比上界下降約 17pp。
- 風險因素原文：承諾算力「procured well in advance based on projected demand across all workloads」、「the composition of our available compute may not optimally match our needs」。
種子主張：市場以「毛利率」比較 AI 實驗室與 SaaS（Augment：「Gross margin is the single number that most separates the bull and bear readings」），但 `GM_f` 對分攤鍵 `α` 之敏感度（每 1pp `α` ≈ C/R ≈ 0.55pp 毛利率，1H26 `[D]`）與 `α` 隨訓練週期／免費用量之時間路徑，可能未被比較口徑吸收；S-1 之公開化為首個可驗證點。本卡不定方向與量級，只立可拒絕之恆等。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（費用性質別 ↔ 功能別之調節；共用資產之分攤鍵） |
| 量綱 | $／期；`α`、`C/R`［無量綱］；毛利率差 pp |
| 可見端 | S-1 損益表（性質別）、Note 8 功能別表與註腳、MD&A compute 敘述、風險因素；上市後 10-Q 同表；SEC CORRESP（分攤方法之問答） |
| 指名不可見端 | 分攤鍵（GPU-小時？請求量？叢集歸屬？）；同一叢集日夜在服務與訓練間切換時之計量；閒置／預留容量之歸屬；內部使用（員工 Claude）與免費存取之算力量 |
| 主張 | `GM_f` 為分攤判斷之函數；若比較基準（同業、SaaS 倍數、賣方模型）採 `GM_f` 而不調節至 `GM_c`，即錯置。可由「具名賣方／評等機構已以 `GM_c` 或含訓練算力之口徑建模」或「S-1 揭露客觀分攤鍵且 `α` 隨服務量同向」拒絕 |
| 外部參照物（測一查證） | 共用資產分攤之 SEC 意見函前例（雲端商 cost of revenue 分攤、遊戲／串流內容攤銷科目歸屬）；OpenAI 推論支出（The Information，付費牆）——僅作路徑先例 |
| 表達工具型態（只指名，不選券） | 模型實驗室普通股（上市後）；不選券 |
| 重疊 | L7-A#3（S&M 科目同時承接分潤與免費算力）、L7-P#4（毛利率序列）、C-P3（權重更新支出）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Anthropic 公開 S-1（本輪 sec.py 實讀，上列原文）：https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm
2. Ed Zitron〈Anthropic's "Profitability" Swindle〉（2026-05-21；本輪實讀：引 The Information「missed on its gross margin projections」、推論成本超預期 23%、WSJ「unclear what accounting methods Anthropic has used to book revenue and costs」）：https://wheresyoured.at/anthropics-profitability-swindle
3. Augment〈Anthropic's S-1: Reconstructed From the Record〉（Paul Smalera，2026-06-04；列「Cost of revenue, and where compute sits in it」為待答題，並轉述 Zitron「favorable accounting around compute costs」）：https://augment.market/pulse/anthropics-s-1-reconstructed-from-the-record
4. Futurum（Nick Patience，2026-06-02；轉述內部資料毛利「roughly 50% today toward 77%」）：https://futurumgroup.com/insights/anthropic-files-for-ipo-looking-to-beat-openai-to-the-punch/
5. Epoch〈compute makes up more than 50% of the cost of running an AI company〉（未讀，測一實讀）：https://epoch.ai/data-insights/company-spending-breakdown
6. The Information〈Why OpenAI, Anthropic Missed Their Own Gross Margin Forecasts〉（線索：Tokenomics SRC_DEM_004；付費牆，測一另尋轉述原文）

## 4. 最強反方（具名，測一驗）

- **已點名**：Zitron（2026-05）明言 compute 會計有利化；Augment 列為 S-1 待答題。若 S-1 公開後有具名賣方／評等機構已以 `GM_c`（或「含訓練之毛利」）建模並公開，即 R1。
- **分攤合理**：訓練與服務叢集若實體分離（不同加速器架構——S-1 稱「different AI accelerators have varying performance characteristics across workload types」），`α` 為客觀計量而非判斷；`α` 下降可完全由 1H26 前沿訓練擴張解釋。
- **營收主導**：`GM_f` +73pp 主要來自營收 ×14 而非 `α`；`α` 每 1pp 之毛利率影響（~0.55pp）相對營收效應可能過小。

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 具名賣方、評等機構或研究機構於 S-1 公開後已以性質別算力率（`GM_c`）或含 R&D 算力之調整毛利建模或並列報導——已定價（R1）。
(2) S-1、S-1/A 或 CORRESP 原文揭露客觀分攤鍵（叢集實體歸屬或計量之 GPU-小時），且 `α` 與服務量指標（consumption-based 營收或 token 量）同向——分攤非判斷（R2）。
(3) `[D]` 以 S-1 已分列數字，`α` 於 1H25→1H26 之變動對 `GM_f` 之影響 < 5pp（`ΔGM_f` 中可歸因於 `α` 者；本門檻於生成時凍結）——量級不足（R3）。
(4) 可運作對照只能寫成 L7-A#1 單位成本、L7-A#3 總額／淨額、L7-P#4 上下文斜率或 C-A3／C-A4 折舊。
(5) 至測一日無已上市主體可表達（Anthropic 未掛牌），且上市後 12 個月內無功能別表之季度序列（10-Q 不續揭）——表達或可觀測不可行（R4）。
(6) OpenAI／xAI 等同業之公開口徑（xAI 經 SpaceX 申報）已採同一功能別分攤且市場並比無口徑差——比較錯置不成立（只削弱，不單獨否決）。

複查觸發器（若日後殺）：Anthropic 10-Q 或 S-1/A 首次揭露算力分攤方法或功能別算力分列；SEC CORRESP 就 cost of revenue 分類提問；具名賣方首次以性質別算力率估值或比較。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：損益表 compute and infrastructure；Note 8 cost of revenue、R&D、S&M 及其註腳；MD&A。
2. 可交易工具：模型實驗室普通股（上市後）；不選券。
3. 半衰期：上市後首份 10-Q（功能別表是否續揭）；S-1/A 與 CORRESP 公開。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列（Q-0112）；`query/ARCH_matrix.md` L7［A］標「#4 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L7-A#1–#3、L7-P#1–#4、L7-I#1–#3、C-A5、C-P3、C-I1 結論；不寫 T-15。線索輸出（§D）：S-1 性質別算力與功能別 cost of revenue 各一列。
