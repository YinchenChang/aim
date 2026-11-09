# L5-A#6 生成卡｜儲存與 IO：會計恆等（Pillar Two 補充稅之「帳面已計、現金遞延」：現金稅 ≡ 帳面稅 − Δ應付所得稅（含非流動）；新加坡 DTT 過渡年申報期 18 個月＋1 個月繳納，使 FY26 補充稅以非流動應付稅留在資產負債表，OCF／Adjusted FCF 同額虛增，並於可推算之日一次流出）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/work/20261011_L5-A#2_generate_CL.md；archive/work/20261017_L5-A#3_generate_CL.md；archive/work/20261025_L5-A#4_generate_CL.md；archive/work/20261101_L5-A#5_generate_CL.md；archive/work/*L12-A#3_generate_CL.md | EMITS: work/20261109_L5-A#6_generate_CL.md -->
**日期：** 2026-11-09　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L5-A　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L5-P#6 本日測一，Q-0184 done）。最後測試日最舊＝2026-11-01（L5-A#5、L5-I#5、L12-A#5、L12-I#5）；依表序取 **L5-A**；非已殺、非刻意排除。既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tax`、`Pillar`、`Seagate`、`Micron`，**命中 0 筆**。內部數字（§12）未取用。載體全由 `sec.py` 實讀與 IRAS 原文。
- 比對之舊檔與死因型態，本卡須異型：
  - **L5-A#1**（KV IO 成本）、**L5-A#2**（HDD 營收量價恆等，共識）、**L5-A#3**（毛利混合／權利金 `s`）、**L5-A#4**（Sandisk 合資表外 capex）、**L5-A#5**（SBC 授予日 vs 既得日代扣稅）：皆非所得稅；本卡不涉營收分解、毛利混合、FV 撥款、代扣稅。
  - **L12-A#3**（OBBBA：§174A／紅利折舊造成之**遞延稅**時序，成長即不回轉）：彼為暫時性差異（遞延稅負債）；本卡為**當期稅已確定、僅繳納日遞延**之應付所得稅（非流動），金額已入損益、繳納日由法定申報期決定、必然一次回轉，非成長可延續之時序。
  - **L13-A#2**（客戶預付入 OCF）、**L5-I#3**（長約保障比）：本卡不以客戶存款為落差（Micron 10-K 亦列 customer deposits，測一須拆開）。
  - **L3-I#6**（§48D 期限誘因）：彼為投資抵減之期限誘因；本卡不涉 §48D。
  - **C-A1／C-A3／C-A4／C-P1**（ARCH_dead）：不同型。
- §7-10 領域最近公開：Micron 10-K FY26（2026-10-09）；IRAS e-Tax Guide MTT／DTT 第三版（2026-10-30）與 Module 9（2026-05）；Seagate 10-K FY26（2026-08-04）；WDC、Sandisk 10-K FY26（2026-08）。下一檢查點＝Micron 1Q FY27 10-Q（約 2026-12／2027-01）。

## 1. 落差一句

恆等：`CashTax_t ≡ TaxProvision_t − ΔDTL_t − ΔTaxPayable_cur,t − ΔTaxPayable_noncur,t`；`OCF_t` 經由 ΔTaxPayable 吸收未繳稅；`Adj.FCF_t ≡ OCF_t − 淨資本支出`。新加坡 DTT（QDMTT）適用 FY 起於 2025-01-01 以後；過渡年申報期為 FYE 後 18 個月、繳納期再 1 個月（IRAS Module 9 slides 26、33）。

可見值（皆 `[V]` 申報原文；比值 `[D]`）：

| 主體 | FY26 帳面稅 | QDMTT／補充稅 | 現金稅 | 非流動應付所得稅 | 其他 |
|---|---|---|---|---|---|
| Micron（FYE 2026-09-03） | $14,761M（ETR 14.8%，前年 11.6%） | $9.03B（抵銷新加坡獎勵 $11.22B 之大部分） | $1,254M（新加坡 $481M） | $9.82B（前年 $648M） | OCF $89,675M；4Q Adj. FCF $33,199M 為回購授權增額之基礎 |
| Seagate（FYE 2026-07-03） | $506M（ETR 13.73%，前年 2.91%） | $422M（11.44 個百分點） | 測一取 | 測一取 | 獎勵淨效益 $197M（前年 $285M），獎勵至 FY2034 |
| WDC／Sandisk | 10-K 言 Pillar Two 已計入（WDC：馬來西亞、泰國） | 測一取 | 測一取 | 測一取 | — |

`[D]` Micron：Δ非流動應付所得稅 ≈ 9.82 − 0.648 ≈ $9.17B ≈ FY26 OCF 之 10.2%；帳面稅 − 現金稅 ≈ $13.5B ≈ OCF 之 15%。依 IRAS 期限，Micron FY26 為過渡年 → DTT 申報約 2028-03、繳納約 2028-04；FY27 為非過渡年 → 約 2028-12 申報、2029-01 繳納，**2028 曆年內可能兩年度補充稅集中流出**。

**種子主張：** 帳面 EPS 已含 15% 最低稅（ETR 跳升已公開），但現金面 FY26–27 之 OCF／Adj. FCF 含約一年份以上未繳補充稅；若市場以近期 FCF 殖利率、或以 Adj. FCF 為基礎之回購授權外推，則高估可持續現金流，並於 2028 年出現可預告之一次性現金流出。反之，若公司或賣方已明示「現金稅率」路徑，或該款項相對市值／年 OCF 量級不足，則無落差。本卡不定方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（ASC 740 當期稅於帳面認列，繳納依申報期；應付稅分流動／非流動；現金流量表間接法）；非守恆、非誘因 |
| 計量者 | 公司（OCF、Adj. FCF 定義與回購授權公式）；賣方模型之現金稅率假設 |
| 可見端 | 10-K／10-Q 稅附註（獎勵、QDMTT、現金稅 ASU 2023-09 表）、其他非流動負債中之應付所得稅、MD&A 之 OCF 歸因句、Adj. FCF 調節表 |
| 指名不可見端 | 各季 QDMTT 應計之流動／非流動分類變動；IRAS 是否給予延長（「or such extended time」）或分期（e-Tax Guide Annex A Q9，未經逐字核實）；賣方模型是否把非流動應付稅視為類負債 |
| 主張 | 「帳面稅 − 現金稅」與 Δ非流動應付稅可逐季觀測；流出日可由法定期限推算；可被量級不足、共識已計、或公司已以現金稅口徑揭露所拒絕 |
| 表達工具型態（只指名，不選券） | 美股可交易之 Micron、Seagate、Western Digital、Sandisk。不選券 |
| 重疊 | L12-A#3（帳面 vs 現金稅，但為遞延稅、US）、L5-A#5（FCF 口徑缺漏，但為代扣稅）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Micron 10-K FY26（稅附註、其他非流動負債、現金流量表、Adj. FCF 與回購授權調節）：https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm
2. Seagate 10-K FY26（ETR 調節表 QDMTT 行、獎勵淨效益）：https://www.sec.gov/Archives/edgar/data/1137789/000113778926000159/stx-20260703.htm
3. WDC 10-K FY26（GMT：馬來西亞、泰國）：https://www.sec.gov/Archives/edgar/data/106040/000162828026057139/wdc-20260703.htm
4. Sandisk 10-K FY26（Pillar Two 已計入、CAMT FY27）：https://www.sec.gov/Archives/edgar/data/2023554/000162828026057406/sndk-20260703.htm
5. IRAS Module 9（DTT 申報 15／18 個月、繳納 1 個月）：https://www.iras.gov.sg/docs/default-source/uploadedfiles/pdf/module-9---globe-and-dtt-related-compliance-obligations.pdf
6. IRAS e-Tax Guide MTT 與 DTT 第三版（§4.1 適用 FY 起於 2025-01-01 以後）：https://www.iras.gov.sg/docs/default-source/e-tax/e-tax-guide-mtt-and-dtt.pdf?sfvrsn=e95bc2a9_16
7. 測一須另取：Micron 1Q FY27 10-Q（非流動應付稅續增額、現金稅）；Micron 4Q FY26 電話會官方逐字稿與 1Q FY27 指引之稅率／現金稅句；Seagate、WDC、Sandisk 10-Q 1Q FY27 之現金稅與應付稅；具名賣方是否以現金稅口徑建 FCF；IRAS 是否有分期或延長規定之原文。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | Micron 已於 MD&A 明文把 OCF 增加歸因於「noncurrent income taxes payable related to the implementation of Pillar Two」，並於附註揭露 $9.82B | #1 | 已揭露 → 落差即揭露（否決 (2)） |
| R2 | 補充稅已入 EPS；以本益比或 EV／EBITDA 定價者不受現金時點影響 | #1、#2 | 時點效應不改價值，只改 FCF 期間分配 |
| R3 | 量級：$9B 相對 Micron 市值或多年 OCF 可能為個位數 % | 測一以市值核算 | 對 `H1` ≥ 5 之重定價不構成驅動（否決 (1)） |
| R4 | 回購授權公式可能已扣除稅款或以 net of 調整項計 | #1 調節表後段 | 機械連結不成立 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 四家 Δ非流動（及遞延繳納之流動）補充稅應付合計 ÷ 同期 OCF < 5%，或 2028 年預估集中流出 ÷ 該主體市值 < 1%（門檻於此凍結）——量級不足。
(2) 公司於業績稿／電話會／指引明示現金稅率路徑或 2028 年繳納時點，或具名賣方、評等機構、主流財經媒體已明文以扣除補充稅應付之 FCF 評估任一家（R1；已入共識）。
(3) Micron 回購授權之 Adj. FCF 調節已扣除補充稅應付或其增額（R4）。
(4) IRAS 原文允許分期或延長使流出平均分攤於 ≥ 3 年，使任一年流出 ÷ 該年 OCF < 3%。
(5) 可運作對照只能寫成 L12-A#3（遞延稅時序）、L5-A#5（代扣稅 FCF 口徑）或 L13-A#2（客戶預付入 OCF）。
(6) 12 個月內無可檢驗事件（Micron 1Q／2Q FY27 10-Q 應付稅變動、指引稅率句、Seagate／WDC／Sandisk 10-Q 現金稅）可使本機制被拒絕。

複查觸發器（若日後殺）：任一儲存主體單季「帳面稅 − 現金稅」÷ OCF > 15% 連續 2 季；或公司首次揭露 DTT 繳納日／金額；或新加坡修法改變 DTT 申報期或獎勵型態（如 QRTC 取代免稅）。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：稅附註（獎勵、QDMTT、現金稅表）、其他非流動負債之應付所得稅、現金流量表——皆可拒絕之科目。
2. 可交易工具：Micron、Seagate、WDC、Sandisk 美股（不選券）。
3. 半衰期：過渡年流出約 2028-04（Micron），距今約 17 個月；與 ≥ 12 個月重定價窗之相容性測一須查。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0185；`query/ARCH_matrix.md` L5［A］標「#6 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 一筆（Micron FY26 OCF）。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L5-A#1–#5、L5-P#1–#6、L5-I#1–#5、L12-A#3、L13-A#2、C-P1 結論。
