# L7-A#3 生成卡｜模型層：會計恆等（雲市集總額認列與分潤科目歸屬：營收與毛利率之口徑恆等）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260930_L7-A_generate_GK.md；archive/drive/USED_20260930_L7-A_test1_GK.md；archive/work/20261013_L7-A#2_generate_CL.md；work/20261013_L7-A#2_test1_CL.md；work/20261020_L7-P#3_test1_CL.md | EMITS: work/20261020_L7-A#3_generate_CL.md -->
**日期：** 2026-10-20　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 2→3／6）　**格：** L7-A　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L7-P#3 本日已測一，Q-0070 done）。非已殺／刻意排除格中，最後測試日最舊＝2026-10-13（L7-A、L7-I、L10-P／A／I、L11-A／I、L13-P、L13-I、L14-P、L14-A）；依表序取 **L7-A**。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py Anthropic marketplace gross net Bedrock "revenue share"`，命中 22 筆；相關 4 筆：SRC_DEM_034／036／037（Reuters 讀機密 S-1：市集占比、分潤）、SRC_DEM_062（Axios OpenAI 淨額口徑）。本輪回原文實讀 Reuters（經 Global Banking & Finance）與 Axios；只作載體指名，不作證據。
- 比對之舊檔與死因型態，本卡須異型：
  - **L7-A#1**（測一不通過）：列表價 vs FLOP／成本不可並列（單位成本）。本卡不論單位成本或 FLOP。
  - **L7-A#2**（部分通過）：**持股方**之公允價值計量（NI ≡ OI＋s·ΔV）。本卡在**實驗室本身**之營收認列（主理人／代理人）與費用科目歸屬。
  - **C-A5**（死 #13，API 已實現單價不可分離）：本卡不需單價，只需市集營收占比與分潤總額兩數。
  - **L10-A**（TAC 分潤，分發層）、**L15-P#2**（雲承諾池市集抵扣，ISV 端）、**L2-A#3／L6-A#2**（電力轉嫁總額法）：同屬「總額 vs 淨額」族，但主體與科目不同；重疊照記，測一須查 L10-A 死因（轉介量 × 分潤率不可並列）是否同樣適用。
  - **L7-P#3**（本日測一不通過）：容量守恆；本卡不涉容量。
  - **T-15**：無關，不寫。
- §7-10 領域最近公開：Reuters（Echo Wang、Krystal Hu，2026-09-29）讀機密 S-1；Axios（Madison Mills，2026-09-03）；OpenAI CRO 備忘錄（Implicator，2026-04-13）。下一檢查點＝公開 S-1 及 SEC 意見往來函（CORRESP，上市前公開）。

## 1. 落差一句

恆等：`R_gross ≡ R_direct + G_mkt`；`R_net ≡ R_gross − F`，`F ≡ s·G_mkt`（分潤）。若 `F` 列營業費用（非營收減項、非 cost of revenue），則申報毛利率 `GM_rep ≡ 1 − C/R_gross`，而淨額等效毛利率 `GM_net ≡ 1 − C/(R_gross − F)` 且營業費用率同步差 `F/R_gross`。已見數點：Reuters 讀機密 S-1——2025 市集銷售約 $2.16B、占營收 47%、「books the full value of marketplace contracts」（主理人）、付平台約 $351M、「within the "sales, marketing, and partnerships" operating expense line item」、約每元 16 分；Axios：改淨額使營收減約 6–10%。種子主張：市場已辯論**營收水準**（gross vs net，Axios／OpenAI CRO），但**毛利率與費用率**之口徑差（分潤落在 S&M 而非營收減項或 cost of revenue）及其隨市集占比 `G_mkt/R_gross` 變動之時間路徑，可能未被比較口徑（同業淨額、SaaS 毛利倍數）吸收；公開 S-1 與 CORRESP 為首個可驗證點。本卡不定方向與量級，只立可拒絕之恆等。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（ASC 606 主理人／代理人判定 × 費用科目歸屬 → 營收、毛利率、營業費用率三者口徑恆等） |
| 量綱 | $／yr；占比 `G_mkt/R`、`s`［無量綱］；毛利率差 pp |
| 可見端 | 公開 S-1 之營收拆分（直接／訂閱／市集）、收入認列政策附註、S&M 科目附註；SEC CORRESP（主理人判定之理由）；同業（OpenAI）口徑報導；雲端商 10-Q 之市集認列政策 |
| 指名不可見端 | 季度 `G_mkt` 序列；`s` 是否隨合約更新（AWS 擴約、Microsoft Foundry 新增）變動；市集抵扣承諾（客戶以雲承諾購買 Claude）之占比 |
| 主張 | 毛利率口徑差 ≈ `F/R` 量級之 pp，且隨市集占比變動；若市場以申報毛利率與淨額同業並比即錯置。可由「具名賣方已以淨額重算毛利率」或「S-1 將分潤列營收減項」拒絕 |
| 外部參照物（測一查證） | 平台型公司總額／淨額改列前例（例：SEC 意見函要求改淨額之公開 CORRESP）——僅作路徑先例 |
| 表達工具型態（只指名，不選券） | 模型實驗室普通股（上市後）；不選券 |
| 重疊 | L10-A（分潤）、L15-P#2（市集抵扣）、C-A5（L7 上市性）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Reuters 讀機密 S-1（轉載）https://www.globalbankingandfinance.com/exclusive-anthropic-ipo-prospectus-lays-bare-deep-dependence/ （本輪實讀：47%、$2.16B、$351M、S&M 科目、主理人）
2. Axios（Madison Mills，2026-09-03）https://axios.com/2026/09/03/anthropic-and-openais-revenue-chasm-explained （本輪實讀：淨額化減 6–10%；CORRESP 將於上市前公開）
3. Implicator（Marcus Schuler，2026-04-13）https://www.implicator.ai/openai-cro-tells-staff-anthropic-inflates-run-rate-by-8-billion/ （本輪實讀：OpenAI CRO Denise Dresser 稱高估約 $8B；兩法皆合 GAAP；Anthropic 答「principal」）
4. 測一須另取：EDGAR 公開 S-1 及 CORRESP（`sec.py`）；具名賣方是否已以淨額重算毛利率或營業費用率；Amazon／Alphabet／Microsoft 10-Q 之第三方模型市集認列政策（總額或淨額）；OpenAI 口徑原文（Axios 2026-10-08）；SEC 要求平台改淨額之前例。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 總額／淨額已成公開辯論且量化（6–10%、$8B） | Axios（#2）、Implicator（#3） | 已定價 |
| R2 | 分潤占總營收僅約 7.6%［D］，毛利率口徑差量級小於估值區間誤差 | Reuters（#1）之 $351M ÷ $4.6B | 不重大 |
| R3 | 兩法皆合 GAAP，S-1 由審計與 SEC 核可後口徑即定，無後續重述路徑 | Implicator（#3） | 無觸發事件 |
| R4 | 公開上市未發生或延後，L7 無可交易主體 | `work/20261020_L7-P#3_test1_CL.md` A1 | 表達失敗（同 C-A5 死因） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 具名賣方／研究機構已以淨額重算實驗室毛利率或營業費用率，或已明言分潤列 S&M 之毛利效果——已定價（R1）。
(2) 公開 S-1 將分潤列營收減項或 cost of revenue（口徑差消失），或 `F/R` < 3% 且無上升路徑——不重大（R2）。
(3) 主理人判定無可觀測之再審路徑（CORRESP 已結案、無改列前例）且市集占比無季度序列——不可觀測（R3）。
(4) 可運作對照只能寫成 L10-A 分潤、L15-P#2 市集抵扣、L2-A#3／L6-A#2 轉嫁總額法或 C-A5。
(5) 至測一日 EDGAR 無公開 S-1，且無已上市主體能分離實驗室營收口徑——表達不可行（R4）。

複查觸發器（若日後殺）：EDGAR 出現模型實驗室公開 S-1 或 CORRESP；任一實驗室改列淨額或分潤科目；雲端商 10-Q 首次揭露第三方模型市集之總額／淨額政策。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：S-1 收入認列政策附註、營收拆分、S&M 科目（分潤）、cost of revenue。
2. 可交易工具：模型實驗室普通股（上市後）。不選券。
3. 半衰期：公開 S-1（報導最早 2026-10-23）→ CORRESP 公開 → 首份 10-Q。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L7［A］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L7-A#1／#2、L7-P#1–#3、L7-I／#2、L10-A、L15-P#2、C-A5、C-P3、C-I1 結論；不寫 T-15。
