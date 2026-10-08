# L1-A#2 生成卡｜能源與電力：會計恆等（現場發電設備：產品毛利於驗收時一次認列，壽命期堆疊更換成本落在可逐年解約之服務合約 → 申報毛利前置）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260926_L1-A_generate_GK.md；archive/drive/USED_20260926_L1-A_test1_GK.md | EMITS: work/20261008_L1-A#2_generate_CL.md -->
**日期：** 2026-10-08　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain）　**格：** L1-A　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L3-A#2 已於本日測畢）。其餘格最後測試日最舊＝2026-09-26 一批（L1-A、L1-I、L3-P、L3-I、L4-P／A／I、L5-A／I）；同日依表序取 **L1-A**（L1-P 刻意排除 T-11）。既有生成數 1 → #2。
- 比對之舊檔與死因型態，本卡須異型：
  - L1-A#1（`archive/drive/USED_20260926_L1-A_generate_GK.md`；測一 `archive/drive/USED_20260926_L1-A_test1_GK.md`）：**價格鎖定存量** `S_lock = (p_PPA − p_spot)×Q_remain`，死於 `p_PPA` 與 `p_spot` 不可由公開項分離。本卡不涉電價、不涉 PPA；載體為**設備供應商之收入認列時序**（產品 vs 服務分部毛利、保固準備、服務合約條款），皆為申報科目。
  - ARCH_dead #5 C-A3（折舊年限離散）、L13-P（GPU 年限）：皆為**資產年限**假設。本卡不動年限；動的是**成本認列時點**（壽命期成本是否在產品認列時預提）。
  - L6-I（backlog 變厚 ≠ 對手方變好）、L13-A：backlog 型。本卡 backlog 只作可見端，不以其為落差。
  - L2-A#2（利息資本化墊高 AFFO）：成本資本化型、L2。本卡為收入／成本跨期配比，L1。
- §7-10 領域最近公開：Bloom Energy 2Q26 10-Q（至 2026-06-30，acc `0001628280-26-050247`）；Bloom FY25 10-K（acc `0001628280-26-006516`）；GE Vernova 2Q26 10-Q（至 2026-06-30，acc `0001996810-26-000148`）。下一檢查點＝Bloom 3Q26 10-Q（約 2026-10 底／11 初）。

## 1. 落差一句

現場燃料電池／燃氣發電設備之**產品**毛利於驗收時一次認列，而壽命期內之週期性燃料電池堆更換由**服務合約**承擔——服務合約「subject to termination for convenience on an annual basis」，故 ASC 606 下不構成多年期履約義務、亦不預提壽命期虧損；**落差＝市場把產品段毛利（Bloom 2Q26 約 36.5%）讀成整機壽命期毛利，而 2026 年產品出貨約三倍成長所生之堆更換潮將在數年後經服務段毛利實現**。**方向未定**：服務段毛利已由 FY23 約 −20.7% 轉為 2Q26 約 18.7%，可能已將更換成本定價入服務費。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：`GM_life = GM_prod·R_prod + Σ_t (R_svc,t − C_svc,t)/(1+r)^t`；`C_svc,t` 含堆更換 `C_stack × N_fleet(t−τ)`（τ＝堆壽命）。申報 `GM_t = (GP_prod,t + GP_svc,t)/R_t`；`R_prod` 成長期 `GP_prod` 主導，更換潮在 t+τ 落入 `GP_svc` |
| 選擇者 | 公司（服務合約年度可解約條款、保固期長短、是否列 onerous／loss 準備）；客戶／融資方（是否續約服務） |
| 可見端 | 分部收入與毛利（product／installation／service／electricity）；accrued warranty；服務合約年期（5–20 年）與年度可解約句；backlog 之 product／service 拆分；RPO（不含可解約服務） |
| 指名不可見端 | 堆壽命 τ 之實際分布；每次更換單位成本；服務費是否逐年覆蓋更換；服務 backlog 中可解約部分之續約率 |
| 已讀錨 | Bloom 2Q26 10-Q（https://www.sec.gov/Archives/edgar/data/0001664703/000162828026050247/be-20260630.htm）：2Q26 產品收入 935.4M（2Q25 296.6M），產品毛利率約 36.5%；服務收入 69.0M、毛利率約 18.7%；安裝毛利為負；accrued warranty（流動）77.8M（2025-12-31 為 20.0M）；6M26 單一非關係人客戶約 73% 營收。Bloom FY25 10-K（https://www.sec.gov/Archives/edgar/data/1664703/000162828026006516/be-20251231.htm）：O&M「range from 5 to 20 years」、「subject to termination for convenience on an annual basis」、服務含「periodic fuel cell replacements」；營收隨驗收時點波動。sec-api.io 分析（https://sec-api.io/insights/financial-analysis-of-bloom-energy-q2-2026-filings-and-scenarios-to-2029，2026-10-01）：服務毛利率 FY23 −20.7%、FY24 −0.7%、FY25 10.0%；FY25 末 backlog 約 20B（product 約 6B、service 約 14B）；6/30 產品＋安裝 RPO 442.4M；Brookfield 至多 5B 融資框架、Oracle 認股權、AEP 至多 1GW。GE Vernova 2Q26 10-Q（https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000148/gev-20260630.htm）：流動合約資產 9,522M（2025 末 9,294M），LTSA 附註 9 未讀到 |
| 量綱 | 毛利率：百分點；堆更換：美元／MW／次；τ：年；**accrued warranty 為短期保固，≠ 壽命期堆更換負債**，不可直接相加 |
| 未證之連結 | ① 堆更換是否確在服務合約而非產品保固內預提；② 服務費定價是否已覆蓋（服務毛利轉正為反證方向）；③ 量級：更換潮對整體毛利是否非邊際 |
| 半衰期 | 年（τ 約數年；2026 出貨批之更換約落在 2030 前後） |

## 3. B 端可觀測載體（只指名，未實讀者標明）

1. Bloom 10-K FY25 Item 8：收入認列政策、product warranty 附註、服務合約之 loss／onerous 政策、performance guarantee 支付額（本輪截斷未讀）。
2. Bloom 10-Q 序列（≥ 6 季）：分部毛利、accrued warranty 變動、服務收入／裝機基數比。
3. Bloom 法說與投資人日：堆壽命、更換成本下降曲線之管理層陳述（未讀）。
4. GE Vernova 10-Q 附註 9：LTSA 合約資產與「changes in estimated profitability」累計調整（對照組：多年期不可解約、採成本比例法者會逐期修正估計；本輪未讀到）。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 服務毛利已轉正並擴大，更換成本已定價入服務費 | sec-api.io 2026-10-01（FY23 −20.7% → TTM 15.2%）；Bloom 2Q26 10-Q | 落差不存在 |
| R2 | 客戶（或融資方）承擔更換：可解約條款使不續約時成本轉回客戶 | Bloom FY25 10-K 年度可解約句 | 公司端無負債 |
| R3 | 堆壽命延長、單位成本下降，更換潮量級縮小 | 未讀（Bloom 管理層陳述待 ANALYST 取） | 量級不足 |
| R4 | 客戶集中（單一 73%）使服務續約與定價為逐案議價，市場已按逐案看待 | Bloom 2Q26 10-Q | 已定價／不可泛化 |

## 5. SCOUT 裁決

**留。** 不進 T。下一動作＝ANALYST 測一（實際 fetch 並列 URL）。終端三題（§7-4）只標「轉入個股層時必問」，本輪不執行。

否決觸發（寫給 ANALYST）：
- (1) 最近 10-K／10-Q 顯示堆更換成本已於產品認列時預提（保固或 loss 準備涵蓋壽命期），或已分列「服務合約預期損失」——前置不成立；
- (2) 服務段毛利連續 ≥ 4 季為正且隨裝機基數上升而不降，且管理層／附註陳述服務費覆蓋週期更換——R1 成立；
- (3) 可重算之壽命期更換成本（裝機 MW × 每 MW 更換成本 × 次數）< 對應產品毛利 10%（量級不足）；
- (4) 更換成本依合約由客戶／融資方承擔，或不續約時公司無義務（R2 成立，負擔不在上市主體）；
- (5) 管理層或賣方已公開以「含／不含壽命期服務」兩口徑揭露整機毛利或單位經濟（落差已被承認）。

複查觸發器（若日後殺）：服務段毛利單季轉負且管理層歸因於更換；或公司首次提列服務合約 loss 準備；或主要客戶不續約服務並揭露更換成本轉移；或 Bloom 揭露堆壽命／更換成本參數。
