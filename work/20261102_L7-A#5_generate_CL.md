# L7-A#5 生成卡｜模型層：會計恆等（直租算力之融資租賃利息移出營業利益：同一算力經雲託管採購時全額入「compute and infrastructure」，經自租（融資租賃）時只有 ROU 攤銷入營業費用、利息入營業外——採購組合位移即改寫營業利益率）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；query/QUEUE.md；archive/work/20261027_L7-A#4_generate_CL.md；work/20261027_L7-A#4_test1_CL.md；archive/work/20261026_L6-A#4_generate_CL.md；work/20261026_L6-A#4_test1_CL.md；archive/work/20261026_L13-A#4_generate_CL.md；archive/work/20261102_L6-I#5_generate_CL.md | EMITS: work/20261102_L7-A#5_generate_CL.md -->
**日期：** 2026-11-02　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 5→6／6）　**格：** L7-A　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額配置、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L7-P#5 已測一，Q-0151 done）。非已殺／刻意排除格中，最後測試日最舊＝2026-10-27 一組（L7-A#4、L7-I#4、L10-P/A/I#4、L11-A#4）；同日以 QUEUE 序決勝（沿 L7-A#4 卡規則），最早＝**L7-A#4**（Q-0112）。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py "finance lease" lease Anthropic`，命中 14 筆，相關 0 筆（皆定價、能力指標、客戶數）。本卡數點全取自 S-1 原文（sec.py 實讀）。內部數字（§12）未取用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L7-A#1**（不通過）：列表價 vs FLOP。本卡不論單價。
  - **L7-A#2**（部分通過）：持股方公允價值。本卡不論任何公允價值（發行方轉債公允值變動亦不納入）。
  - **L7-A#3**（部分通過）：市集總額／淨額（營收側）。本卡為成本側行次。
  - **L7-A#4**（部分通過）：同一筆性質別算力在**功能科目間**之分攤（COR／R&D／S&M）。本卡不論功能別；論**同一經濟成本在營業線上下之切分**（營業費用 vs 營業外利息），由採購型態（服務 vs 融資租賃）決定，非管理層分攤判斷。
  - **L6-A#4**（部分通過）：融資租賃／供應商融資之**現金流**分類（還款列籌資、不入 capex）。本卡**不論現金流量表**，只論損益表之營業利益行次；不以 OCF／FCF 為落差。
  - **L13-A#4**（不通過）：可轉換票據全成本。本卡不論 Broadcom NPA 轉債之成本或稀釋。
  - **L6-I#5**（不通過）：買方尚未起租租約之自建／外購排序誘因。本卡非誘因，且主體為實驗室本身。
  - **C-A3／C-A4／L6-A#3**（折舊年限／起點）：本卡取 S-1 所載租期（5 年）為攤銷期，不論年限假設。
  - **C-A5／C-P3**（死 #13／#16，L7 未上市）：觸發器屬 SCOUT-WATCH，本卡不代判；Anthropic 公開 S-1 已在 L7-A#4 測一記錄。
  - **T-15**：無關，不寫。
- §7-10 領域最近公開：Anthropic S-1（EDGAR，2026-10-26）；DRS/A 最近 2026-10-09。下一檢查點＝S-1/A、CORRESP、上市後首份 10-Q。

## 1. 落差一句

恆等：融資租賃之經濟成本 `K_FL ≡ A + I`（ROU 攤銷＋租賃負債利息）；性質別損益表中 `A` 入「compute and infrastructure」（營業費用），`I` 入「other income (expense), net」（營業外）。同一算力若經 CSP 託管（購買承諾／服務合約）取得，供應方之資本成本已含於價格、全額入營業費用。故營業利益率 `OM ≡ 1 − (C_csp + A_direct + O)/R`，在經濟成本不變下，採購組合由 CSP 移向自租，`OM` 機械上升約 `s × (I/K_FL) × (K/R)`。定義 `δ ≡ I_FL ÷ (C + I_FL)`＝總算力經濟成本落在營業線下之比。
已見數點（本輪 sec.py 實讀 S-1，M$ 或原文）：
- 「five-year master equipment leases with Broadcom … These Lease Arrangements are accounted for as finance leases. Our rent payments over the life of these leases are equal to an aggregate of approximately $161.2 billion excluding interest」；「TPU-based compute capacity, a portion of which began to come online in 2026, with additional capacity expected to come online starting in 2027」。
- 會計政策：finance lease ROU「amortized … recognized within operating expenses based on the nature of the leased asset. The interest component of a finance lease … is presented separately」；MD&A：Other income (expense), net 含「interest expense from finance leases」。
- Note 7：1H26 finance lease cost＝攤銷 13＋利息 5；加權折現率（融資租賃）7.1%、剩餘期 4.9 年；「Leases Not Yet Commenced」2025-12-31 約 $50.2B → 2026-06-30 約 $321.4B（未折現，2026–2028 起租，期 < 1–20 年）。
- 業務節：「Anthropic Direct … leasing chips directly and hosting them in dedicated facilities … A significant portion of this total committed spend relates to Anthropic Direct, and we expect it to represent a growing share of our compute investments over time」。
- 損益：1H26 營收 16,286、compute and infrastructure 8,945；2Q26 營業利益率 8%、Adjusted Operating Margin 19%（Adjusted 只加回 SBC、非現金捐贈、Bartz 和解；不涉租賃利息）。
- `[D]`（只作量綱，不作預測）：$161.2B ÷ 5 年 ≈ 每年攤銷 32.2B；以 7.1% × 平均餘額（≈ 80.6B，等額本金近似）≈ 每年利息 5.7B → `I/K_FL` ≈ 15%；首年若全額起租 ≈ 11.4B（161.2 × 7.1%）。相對 1H26 年化營收（32.6B）≈ 17pp、相對 1H26 年化 compute（17.9B）≈ 32%。1H26 實際 `δ` ≈ 0.06%（5 ÷ 8,950）——機制屬前瞻，於起租後之 10-Q 才可量。
種子主張：上市後市場以 `OM`／Adjusted Operating Margin 之改善讀「規模效率」，但其中一部分可能只是採購型態由服務轉融資租賃、把約 15% 之直租算力經濟成本移到營業線下；比較基準（同業、SaaS、自身歷史）若不調節 `I_FL`，即錯置。本卡不定方向與量級，只立可拒絕之恆等。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（ASC 842 融資租賃損益行次：攤銷 vs 利息；服務合約 vs 租賃之採購型態） |
| 量綱 | $／期；`δ`、`I/K_FL`、`s`［無量綱］；營業利益率 pp |
| 可見端 | S-1／10-Q Note 7 租賃費用組成（攤銷、利息）、Leases Not Yet Commenced、性質別損益表、Other income (expense) 組成、非 GAAP 調節、MD&A compute 敘述 |
| 指名不可見端 | 起租時點與批次；CSP 託管單價中隱含之資本成本；直租 vs 託管之每單位算力經濟成本差（管理層稱「long-term economic advantages」，未量化） |
| 主張 | `OM` 隨直租占比上升而機械改善之部分，若未被市場或發行人調節，即比較錯置。可由「具名分析／評等機構已以含租賃利息之算力成本或 EBITDA／租賃調整口徑讀 Anthropic」或「發行人非 GAAP／MD&A 已並列或內含 `I_FL`」拒絕 |
| 外部參照物（測一查證） | ASC 842 前航空與零售之 EBITDAR、Moody's／S&P 租賃資本化調整（行次搬移之標準先例）；超大規模雲之融資租賃利息呈現（同為營業外）——僅作路徑先例 |
| 表達工具型態（只指名，不選券） | 模型實驗室普通股（上市後）；不選券 |
| 重疊 | L7-A#4（同一 compute 行之另一切法）、L6-A#4（同一融資租賃之現金流側）、L13-A#4（同一 Broadcom 結構之轉債側）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Anthropic S-1（本輪 sec.py 實讀，上列原文）：https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm
2. MarketBeat（Leo Miller，2026-09-30）〈Broadcom's AI Growth Story Faces a $161 Billion Anthropic Test〉——本輪經代理實讀：引 adjusted operating profit「$559 million, or a 5.1% margin」、「cannot pay for its commitments based on its current operating profits」；未論融資／營業租賃或利息行次：https://www.marketbeat.com/articles/broadcoms-ai-growth-story-faces-a-161-billion-anthropic-test/
3. Forkast（2026-08-07）〈Anthropic SPVs Stack $71 Billion in Chip-Lease Debt in 60 days〉——實讀：稱「off-balance-sheet leasing」「This is not corporate debt」，與 S-1「accounted for as finance leases」相左（作者為 AI 署名，可信度低）：https://forkast.news/anthropic-spvs-stack-71-billion-in-chip-lease-debt-in-60-days/
4. Digitech Bytes（2026-10-27）〈Broadcom's $63 Billion Financing Machine〉——實讀：轉述 $161.2B「excluding interest」與 9% PIK；未論損益行次：https://digitechbytes.com/finance-operations/broadcom-s-63-billion-financing-machine-who-pays-for-anthropic-s-chips/
5. Augment〈Anthropic's S-1: Reconstructed From the Record〉（未就本題重讀，測一實讀）：https://augment.market/pulse/anthropics-s-1-reconstructed-from-the-record
6. Epoch〈Will financing bottleneck AI compute〉（未讀，測一實讀）：https://epoch.ai/gradient-updates/will-financing-bottleneck-ai-compute
7. Chiltern Capital、Tunguz、Clouded Judgement 之 S-1 讀數（L7-A#4 測一 A3／A6／A7 已列；測一查其是否處理租賃利息）

## 4. 最強反方（具名，測一驗）

- **經濟改善非呈現**：管理層稱 Anthropic Direct「will provide long-term economic advantages」；若直租每單位算力經濟成本（含利息）低於 CSP 託管價，`OM` 上升為真實改善，行次搬移只是其中一部分——須拆。
- **量級**：1H26 融資租賃利息僅 5M；若起租遞延或分批（2027 起），12 個月內 `δ` 可能 < 門檻。
- **已被讀出**：S-1 自身逐年揭露租賃費用組成，信用與賣方分析慣例上以 EBITDA 或租賃調整負債讀融資租賃；MarketBeat 已以「承諾 vs 營業利益」框架讀之。

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 具名賣方、評等機構或研究機構於 S-1 公開後已以含融資租賃利息之算力成本、EBITDA 或租賃調整口徑讀 Anthropic 營業利益率或比較同業——已定價（R1）。
(2) S-1、S-1/A、CORRESP 或首份 10-Q 之非 GAAP 調節或 MD&A 已把 `I_FL` 併入算力成本、或並列「含租賃利息之營業利益率」——發行人已中和（R2）。
(3) `[D]` 起租後首份含實質起租之 10-Q（或 12 個月內任一季），`δ` < 5%，或 `I_FL ÷ R` < 3pp（兩門檻於生成時凍結）——量級不足（R3）。
(4) 可運作對照只能寫成 L7-A#4 功能別分攤、L6-A#4 現金流分類、L13-A#4 轉債成本或 C-A3／C-A4 折舊年限。
(5) 至測一日無已上市主體可表達（Anthropic 未掛牌），且上市後 12 個月內無季度租賃費用組成（10-Q 不揭）——表達或可觀測不可行（R4）。
(6) 管理層或具名第三方量化直租 vs 託管之單位經濟成本差，且差額足以解釋 `OM` 改善之大部分——行次效應被經濟效應淹沒（只削弱，不單獨否決）。

複查觸發器（若日後殺）：Anthropic 首份 10-Q 之 Note 7 租賃利息首次 ≥ 營收 3%；發行人改變 Adjusted Operating Margin 定義（納入或排除租賃項）；具名賣方首次以未調節 `OM` 對 SaaS／同業比較而不提租賃利息（落差重現）。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：性質別損益表 compute and infrastructure；Other income (expense), net 之租賃利息；Note 7 租賃費用組成與 Leases Not Yet Commenced；非 GAAP 調節。
2. 可交易工具：模型實驗室普通股（上市後）；不選券。
3. 半衰期：起租批次（2026 部分、2027 起續上線）；上市後首份 10-Q。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列（Q-0152）；`query/ARCH_matrix.md` L7［A］標「#5 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 二列（Broadcom 融資租賃租金；尚未起租租約）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L7-A#1–#4、L7-P#1–#5、L7-I#1–#4、L6-A#4、L13-A#4、C-A3、C-A4、C-A5、C-P3、C-I1 結論；不寫 T-15。
