# L4-A#6 生成卡｜運算硬體系統：會計恆等（產品保固準備之滾存恆等：報告毛利率＝組合毛利率 −（新提列＋既存估計變動）／營收；準備餘額＝期初＋提列＋估計變動 − 實際耗用。同售機櫃級 AI 系統之三家整機商提列強度相差一個數量級）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；AIM_FUNNEL.md；archive/drive/USED_20260926_L4-A_generate_GK.md；archive/drive/USED_20260926_L4-A_test1_GK.md；archive/work/20261011_L4-A#2_generate_CL.md；archive/work/20261017_L4-A#3_generate_CL.md；archive/work/20261025_L4-A#4_generate_CL.md；archive/work/20261031_L4-A#5_generate_CL.md；work/20261011_L4-A#2_test1_CL.md；work/20261017_L4-A#3_test1_CL.md；work/20261025_L4-A#4_test1_CL.md；work/20261031_L4-A#5_test1_CL.md | EMITS: work/20261108_L4-A#6_generate_CL.md -->
**日期：** 2026-11-08　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L4-A　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L4-P#6 本日已測一）。最後測試日最舊＝2026-10-31（L4-A#5）；非已殺、非刻意排除。既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py warranty "liquid cooling" "failure rate"`，命中 **1** 筆（SRC_DC_016：Supermicro 保固頁之標準保固年限，人工 3 年／零件 1 年），只作「去哪找」，未作證據；本卡載體全由 `sec.py` 原文取得。內部研究數字（§12）未取用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L4-A#1**（BOM 份額恆等；死於 BOM 不在申報層）：本卡所需量（保固準備滾存表四列）為申報附註項。
  - **L4-A#2**（整機商 CCC／OCF 恆等；死於符號差異先於 AI、已被公開解讀）：本卡為**損益表成本中之或有負債估計**（ASC 460-10 保固），非營運資本時序。
  - **L4-A#3**（客戶權證收入減項；死於 ASC 606-10-32-25A 切斷反身性）：本卡在成本端，無權證。
  - **L4-A#4**（EMS 主理人／代理人淨額；死於 (2) 毛利金額不變）：本卡之提列與估計變動**直接改變毛利金額與 EPS**。
  - **L4-A#5**（晶片設計商確定採購承諾損失，ASC 330；死於 (4) 不可撤銷比例不可觀測）：本卡為**售後義務**（ASC 460），主體為整機商；關鍵量（期初、提列、估計變動、耗用、期末）四列皆在 10-Q／10-K 揭露，不需不可見之合約比例。重疊（同為 COGS 內之估計提列）照記。
  - **L3-A#6**（Intel LCNRV 回補）：存貨端、晶圓廠；構成不同。**C-I3′**（分部毛利由非機制項解釋）：本卡之機制項本身即申報列，非殘差。**N-01**、**N-02**、**L2-I#3**：構成不同。
- §7-10 領域最近公開：Super Micro 10-Q 1Q FY27（期末 2026-09-30，申報 2026-11-06）；Dell 10-Q FQ2 FY27（期末 2026-07-31，申報 2026-09-08）；HPE 10-Q 3Q FY26（期末 2026-07-31，申報 2026-09-03）。下一檢查點＝Dell FQ3 FY27 10-Q（期末約 2026-10-30，約 2026-12）、HPE 10-K FY26（期末 2026-10-31，約 2026-12）。

## 1. 落差一句

三家同售 GB200／GB300 級機櫃系統之整機商，保固準備滾存走向相反：**Dell** 保固負債 450 → 1,035 → 1,207（百萬美元；FY26 末 → FQ1 → FQ2 FY27），FQ1 提列＋估計變動 819（前年同季 211），六個月 1,202（前年 460），而附註明言「warranty liability process does not differentiate between estimates made for pre-existing warranties and those made for new warranty obligations」；**Super Micro** 1Q FY27 營收 19,945.8 百萬美元、毛利率 12.7%，保固提列 37.5（÷營收 0.19%；FY24／FY25／FY26 為 0.35%／0.27%／0.35% `[D]`），耗用 41.5 > 提列，期末準備 26.4，約為 FY26 年耗用 128.2 之 0.2 年 `[D]`，而其政策稱保固期 15–39 個月；**HPE** 九個月準備 284 → 277 持平。故 **報告毛利率 ＝ 組合毛利率 −（新提列＋既存估計變動）／營收**，**期末準備 ＝ 期初 ＋ 提列 ＋ 估計變動 − 耗用**；若同型產品之真實保固成本率相近，則提列率差一個數量級之一方須以日後「既存估計變動」補提（毛利下修）或回轉（毛利上修）。落差＝市場以報告毛利率比較整機商時，未必區分其中保固提列強度之差。**方向未定**（可能為 SMCI 少提，亦可能 Dell 一次性多提或含 CSG 個人電腦組合）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（成本計量／或有負債滾存）：`GM% = GM%_mix − (Accr + ΔEst)/Rev`；`W_end = W_beg + Accr + ΔEst − Util`（ASC 460-10-25-5／-30：銷貨時估計並提列，估計變動入當期）。非守恆、非誘因 |
| 量綱 | `a = Accr/Rev`（無量綱，季／年）；覆蓋期 `c = W_end / Util_年`（年）；保固期 `τ_w`（月，15–39）；敏感度 `s = Δa × Rev_4Q / GP_4Q`（無量綱，毛利占比）|
| 可見端（實讀） | 見 §1 數字。SMCI 10-K FY26 政策：「limited warranty to end-users ranging from 15 to 39 months … Warranty accruals are based on estimates that are updated on an ongoing basis taking into consideration inputs such as new product introductions」。Dell AI-optimized servers 營收 FQ1／FQ2 FY27：16,132 `[D]`／16,401 |
| 指名不可見端 | 各家保固成本按產品線（AI 機櫃 vs 傳統伺服器 vs PC）分列；對上游（GPU／板卡商）之背對背保固轉嫁比例；Dell 新提列與既存估計變動之拆分；液冷機櫃之現場故障率 |
| 主張 | 提列率 `a` 與覆蓋期 `c` 之跨公司差異，若非產品組合或轉嫁所致，則為日後毛利之機械性修正項；營收急增時，同一 `Δa` 對毛利金額之衝擊等比放大（SMCI 毛利率 12.7%，`Δa` 每 0.5pp ≈ 毛利 4%）|
| 外部參照物（測一查證） | 公開報導 GB200 機櫃液冷漏液／過熱與重設計（Tom's Hardware、DCD，2025）；僅作「新產品導入增加保固不確定性」之先例，非量級 |
| 表達工具型態（只指名，不選券） | 美股上市伺服器整機商普通股與上市選擇權。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| Super Micro 10-Q 1Q FY27（Note 6 Product Warranties、MD&A 毛利率段、遞延收入之延長保固） | https://www.sec.gov/Archives/edgar/data/1375365/000137536526000027/smci-20260930.htm |
| Super Micro 10-K FY26（保固政策、三年滾存表） | https://www.sec.gov/Archives/edgar/data/1375365/000137536526000022/smci-20260630.htm |
| Dell 10-Q FQ2 FY27／FQ1 FY27（Warranty Liability 表、分部營收、MD&A） | https://www.sec.gov/Archives/edgar/data/1571996/000157199626000046/dell-20260731.htm ；https://www.sec.gov/Archives/edgar/data/1571996/000157199626000030/dell-20260501.htm |
| HPE 10-Q 3Q FY26（Warranties 表） | https://www.sec.gov/Archives/edgar/data/1645590/000164559026000080/hpe-20260731.htm |
| GB200 機櫃故障／漏液報導（二手） | https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-gb200-production-ramps-up-after-suppliers-tackle-ai-server-overheating-and-liquid-cooling-leaks ；https://www.datacenterdynamics.com/en/news/nvidia-server-makers-solve-blackwell-technical-issues-ramp-up-shipments-of-gb200-racks-report/ |
| Supermicro 保固頁（線索：Tokenomics SRC_DC_016；測一回原文實讀） | https://www.supermicro.com/en/support/warranty |
| 法說逐字稿（Dell FQ1／FQ2 FY27、SMCI 1Q FY27）、具名賣方 | 測一取得 |

不宣稱保固差異已入或未入共識、不宣稱方向。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 提列率差由產品組合解釋：Dell 數字含 CSG 個人電腦與傳統伺服器（PC 保固率高），SMCI 幾乎全為伺服器 | Dell 10-Q 分部營收表；附註未按分部列保固 | `Δa` 非同型產品之差，量級失真 |
| R2 | GPU／板卡故障由上游（NVIDIA 等）背對背保固承擔，整機商只擔自製件與人工；SMCI 低提列合理 | 線索：Tokenomics SRC_DC_016（Supermicro 保固頁，本輪未實讀）；測一實讀保固頁與 10-K 供應商保固條款 | 真實成本率本即低，`Δa` 無補提含意 |
| R3 | 大型雲／neocloud 客戶自行維運或另購延長保固（入遞延收入，非保固準備），標準保固責任小 | SMCI 10-Q：「deferred revenue primarily results from customer payments received upfront for extended warranties and on-site services」 | 成本在服務收入對應之成本，非準備；恆等式範圍錯置 |
| R4 | Dell FQ1 跳增為已知單一議題之一次性提列，已於法說說明並被視為一次性 | 測一查 Dell FQ1 FY27 法說與 8-K | 落差已揭露／不影響定價 |
| R5 | 量級：保固提列占營收 < 1%，對估值無足輕重 | §1 數字 | `s` 過小 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) Dell、SMCI 或 HPE 之申報／法說，或 ≥ 1 位具名賣方，已公開解釋 Dell 保固負債跳增之原因，**或**已比較整機商間保固提列強度（R4）。
- (2) 一手原文顯示提列率差主要由產品組合（PC vs 伺服器）解釋，且無法以分部或代理量（如 ISG 占比加權）界定伺服器端提列率（R1）。
- (3) `[D]` 量級（凍結）：`s = (Dell 最近 2 季 Accr 合計 ÷ 同期營收 − SMCI 最近 4 季提列 ÷ 同期營收) × SMCI 最近 4 季營收 ÷ SMCI 最近 4 季毛利`；`|s|` **< 3%** 即否決。若 (2) 可得伺服器端代理率，以之替代 Dell 全公司率。
- (4) 一手原文（10-K 供應商條款、保固政策、法說）顯示 GPU／主要元件故障成本由上游背對背承擔，或標準保固實質由延長保固服務合約承擔（R2／R3），使跨公司 `a` 不可比。
- (5) 本卡只能以 L4-A#5（採購承諾損失）、L4-A#2（CCC）、L4-A#4（淨額口徑）、C-I3′（分部毛利殘差）或 N-01（機隊世代）重述。
- (6) 12 個月內無檢驗事件（Dell FQ3 FY27 10-Q 約 2026-12、HPE 10-K FY26 約 2026-12、SMCI 2Q FY27 10-Q 約 2027-02、Dell 10-K FY27 約 2027-03；任一家首次分列既存估計變動）。

複查觸發器（若日後殺）：任一整機商首次按產品線分列保固成本或拆分既存估計變動；單季「既存估計變動」÷營收 ≥ 0.5%；具名賣方首次以保固提列率比較整機商毛利率。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：營業成本中之保固提列與既存估計變動、保固準備滾存表（流動／非流動）、遞延收入中之延長保固、供應商保固回收（若有）。
2. 可交易工具：美股上市伺服器整機商普通股與上市選擇權（不選）。
3. 半衰期：季（10-Q 逐季揭露滾存表；保固期 15–39 個月決定估計變動之兌現期）。

## 7. 本輪寫入

本卡；QUEUE Q-0182（ANALYST 測一）；ARCH_matrix L4［A］格標「#6 已生成」；`export/LEADS_算力收支.md` 追加 2 列（SMCI 10-Q 1Q FY27 營收、Dell FQ1 FY27 AI-optimized servers `[D]`）。不改 L4-A#1–#5、L4-P#1–#6、L4-I#1–#5、L3-A#6、C-I3′、N-01、N-02。
