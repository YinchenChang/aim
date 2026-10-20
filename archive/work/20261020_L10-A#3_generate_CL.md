# L10-A#3 生成卡｜分發與中介：會計恆等（主事人／代理人列報恆等：營收 ≡ Σ 市場 GB × 混成 take rate；監理驅動之列報切換改營收不改 GB／EBITDA，稅負與雇傭成本才改經濟）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；work/20261013_L10-A#2_test1_CL.md；archive/work/20261013_L10-A#2_generate_CL.md | EMITS: work/20261020_L10-A#3_generate_CL.md -->
**日期：** 2026-10-20　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 5→6／6）　**格：** L10-A　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L10-P#3 本日測一，Q-0073 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-13（L10-A、L10-I、L11-A、L11-I、L13-P、L13-I、L14-P、L14-A）；依表序取 **L10-A**。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py principal agent gross revenue take rate`，命中 15 筆皆 AI 硬體／模型需求列，與本格無關＝相關命中 0。載體全由本輪 sec.py／WebSearch／WebFetch 實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L10-A#1**（測一不通過）：TAC＝轉介量 × 每次分潤率，量與率不可並列。本卡不論轉介分潤；恆等兩側（營收、GB、司機支付）皆於同一 10-Q 逐季申報。
  - **L10-A#2**（測一部分通過）：商戶預收浮存（ΔDMB 入 FCF）。本卡不論現金時序，只論損益表列報口徑。
  - **L10-P#2／#3**：通道守恆、車隊容量守恆；本卡非守恆。**L10-I／#2**：預設與佣金路由；本卡非誘因。
  - **L12 系列**（監理與法制）：本卡之驅動為監理，但可拒絕之主張落在會計恆等（列報 vs 經濟之分離）；若實讀後只能寫成「法規通過與否」即滑入 L12（否決 (4)）。
  - **L11-P**（死 #3）：不論注意力。不恢復。C-A5 不重開。
- §7-10 領域最近公開：Uber 2Q26 10-Q（2026-08-05）；Littler 論 EU 平台工作指令（2026-08-20）；英國 VAT 改制（2026-01 生效）。下一檢查點＝Uber 3Q26 10-Q（約 2026-11 初）、EU 指令轉置期限 2026-12-02。

## 1. 落差一句

恆等骨架：`Rev ≡ Σ_m GB_m · τ_m + Σ_{m∈principal} GB_m · d_m`（`τ`＝平台費率；`d`＝司機／外送員支付占 GB 比；代理人市場司機支付沖減營收，主事人市場列成本）；`GB`、`Rev − 司機支付`（貢獻）於切換前後不變，只有稅基（主事人按全票價課 VAT）與雇傭成本改經濟。已見數點：Uber 2Q26「Mobility business model changes in the UK … negatively impacted revenue by $1.1 billion」，營收 +12% vs GB +24%；營收／GB 27.1% → 24.5%［D］。英國改制：倫敦外改代理人（司機負 VAT），倫敦因 TfL 執照仍為主事人、全票價課 20% VAT（TaxiPoint 2026-01-02）。EU 平台工作指令 2026-12-02 轉置期限、可反駁之僱傭推定（Littler 2026-08-20），可反向推動「平台成為僱主／主事人」之列報。種子主張：市場以營收成長與營收倍數讀聚合平台，而監理驅動之列報切換（英國朝代理人、EU 可能朝主事人）使營收與經濟脫鉤；以恆等式分離「列報量」與「經濟量（VAT 稅基、雇傭成本）」後，兩者方向可相反。本卡不定方向與量級，只立可拒絕之分離。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（ASC 606 主事人／代理人判斷 × 市場別列報） |
| 量綱 | GB、營收、司機支付［美元／季］；take rate、d［無量綱］ |
| 可見端 | Uber 10-Q：GB、營收、「business model changes」影響額（逐季）、成本科目定義；DoorDash、Lyft 10-Q 之 EU 指令風險段 |
| 指名不可見端 | 各市場主事人／代理人之 GB 份額；EU 各國轉置後之列報判斷 |
| 主張 | 列報切換之營收影響 ≠ 經濟影響；可由「公司已逐季量化且賣方已調整」或「市場只看 GB／EBITDA」拒絕 |
| 外部參照物（測一查證） | 過往列報切換前例（如 Uber 2022–2023 英國倫敦改主事人致營收跳升、ASC 606 導入時之重編） |
| 表達工具型態（只指名，不選券） | 美股上市聚合平台普通股；不選券 |
| 重疊 | L12（監理）、L10-A#1（take rate）、L13（資本結構無）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Uber 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1543151/000154315126000032/uber-20260630.htm ：「Effective January 2, 2026, we implemented a business model change in certain UK markets, primarily driven by regulatory and tax considerations … payments to drivers are recorded as a reduction of revenue instead of cost of revenue」；「negatively impacted revenue by $1.1 billion」；成本定義「where we are primarily responsible for Mobility and Delivery services」；「Platform Work」0 筆。
2. TaxiPoint（Perry Richardson，2026-01-02）https://www.taxi-point.co.uk/post/principal-to-agency-uber-restructures-driver-contracts-to-sidestep-vat-hit-from-rachel-reeves-minic ：倫敦外「agent rather than the supplier」；主事人須就「the passenger's fare」課 20% VAT，取代 TOMS；財部估年增逾 £700m；倫敦仍為主事人。
3. Littler（Raoul Parekh、Alison Bell，2026-08-20）https://www.littler.com/news-analysis/asap/eu-platform-work-directive-uncertainty-ahead-implementation-deadline ：「until December 2, 2026」；「rebuttable legal presumption of employment status」；多國未公布草案。
4. DoorDash 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1792789/000179278926000050/dash-20260630.htm ：「EU's Platform Work Directive … may impact the classification of Dashers」；「as a principal」0。
5. Lyft 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1759509/000162828026054499/lyft-20260630.htm ：EU 指令風險「especially following our recent acquisitions」。
6. 測一須另取：Uber 3Q26 10-Q 是否揭露其他市場列報切換；賣方是否以「ex-business model change」口徑建模；英國改制之 VAT 經濟影響（倫敦全票價）是否已揭露；EU 主要市場（西班牙 Ley Rider 前例）之列報判斷；過往切換時股價／共識反應之具名分析。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 公司逐季量化切換影響額，並以 GB、EBITDA 為指引口徑 | #1 | 已定價／列報無資訊 |
| R2 | 切換對 EBITDA、FCF 為零，營收倍數非主要定價口徑 | #1［D］ | 不重大 |
| R3 | EU 指令轉置滯後、各國不一，窗內無可觀測切換 | #3 | 不可並列（窗內） |
| R4 | 真正經濟量為稅與雇傭成本，屬 L12 監理論點 | #2、#3 | 滑入他格 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 具名賣方／研究機構已以「排除列報切換」之營收或 take rate 口徑建模並公開（或公司指引已改此口徑）——已定價（R1）。
(2) 切換對 EBITDA／FCF 無影響，且可得證據顯示市場定價以 GB／EBITDA 為主——列報落差不重大（R2）。
(3) 至重定價窗（≥ 12 個月）內無任何市場之可觀測列報切換或經濟稅負揭露——不可並列（R3）。
(4) 可運作對照只能寫成 L12 系列（法規成立與否）、L10-A#1（take rate）或 L10-P#2。
(5) 英國改制之 VAT 經濟成本已由公司量化並透過票價轉嫁（具名證據）——經濟腿已消化。

複查觸發器（若日後殺）：Uber／Lyft／DoorDash 10-Q 揭露新市場之 business model change 及其營收影響；任一 EU 主要市場完成轉置並由平台改僱傭制；賣方首次以「ex-business model change」口徑出報告。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：營收、GB、成本（司機支付）、「business model changes」影響額附註。
2. 可交易工具：聚合平台普通股。不選券。
3. 半衰期：季度 10-Q 揭露 → EU 轉置（2026-12-02）後首份 10-K。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L10［A］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L10-A#1／#2、L10-P#1–#3、L10-I／#2、L11-P、L12 系列、C-A5 結論；不寫 T-15。
