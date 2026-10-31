# L3-A#5 生成卡｜半導體製造測試：會計恆等（利息資本化：利息發生額 ≡ 損益表利息費用＋資本化利息；在建工程未轉固前，晶圓廠建置期之利息不經損益，轉固後改經折舊入銷貨成本，停工則停止資本化）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md（經 FUNNEL §2）；archive/work/20261008_L3-A#2_generate_CL.md；archive/work/20261016_L3-A#3_generate_CL.md；archive/work/20261024_L3-A#4_generate_CL.md；work/20261024_L3-A#4_test1_CL.md；archive/work/20261031_L3-P#5_generate_CL.md（格式） | EMITS: work/20261031_L3-A#5_generate_CL.md -->
**日期：** 2026-10-31　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3→4／6）　**格：** L3-A　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L3-P#5 已於本日測一）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-24（L3-A#4、L3-I#4、L4-P#4；L3-P 已取）→ 依表序取 **L3-A**；既有生成 4 份 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `capitalized interest`／`construction in progress`／`Intel`，命中 12 筆，皆為「Intelligence」字串誤中之模型評測列，0 筆採用。內部數字（§12）：未取用。
- 比對（本卡須異型）：
  - **L3-A#1**（GK）：有效晶粒單價（晶圓價 ÷ 良率 × 顆數），死於層別良率不可由申報反解。本卡不涉單價、良率。
  - **L3-A#2**：政府補助淨額法沖減 PP&E → 折舊基數，死於量級。本卡不涉補助（Intel 10-Q 之「capital-related government incentives」不作載體）；動的是**融資成本之認列時點與科目**（利息費用 vs 資產成本）。
  - **L3-A#3**：封測材料轉嫁之毛利率分母，死於已揭露。本卡不涉營收口徑。
  - **L3-A#4**：Intel 合資廠 NCI 歸屬與 APIC 繞道。同一主體，但機制為合併邊界；本卡為**資本化恆等**，不改其結論（Arizona SCIP 之 CIP／已轉固數只作 CIP 結構之讀數）。
  - ARCH_dead：C-A3（折舊年限離散）——本卡年限不動；L13-P（GPU 年限 vs 熱循環）不同物件；C-I3′／N-02（利益未分列）——本卡資本化利息逐期分列於附註，非未分列型，但否決 (1) 檢其可歸屬性（按廠／按節點）。
- §7-10 領域最近公開：Intel 10-Q 3Q26（2026-10-30，acc `0000050863-26-000191`）；Intel 10-K FY25（2026-01-23）；Micron 10-K FY26（2026-10-09，期末 2026-09-03）；TXN 10-Q 3Q26（2026-10-23，XBRL）；ASC 835-20（利息資本化）未見 2026 修訂（測一核）。

## 1. 落差一句

依 ASC 835-20，**利息發生額 ≡ 損益表利息費用＋資本化利息**；資本化部分計入在建工程（CIP），**轉固後隨折舊入銷貨成本**，若建置活動「實質全部暫停」則停止資本化。晶圓廠擴建期之資本化比例極高：Intel 3Q26 利息費用 3.24 億美元、資本化 2.64 億美元 → 發生額 5.88 億、資本化比 ≈ 45% `[D]`（FY24 ≈ 59%、FY25 ≈ 52%、9M26 ≈ 47% `[D]`）；Micron FY26 利息費用 1.06 億、資本化 3.83 億 → 資本化比 ≈ 78% `[D]`，且 FQ3、FQ4 利息費用為 **0**。種子主張：**以申報利息費用估算之融資成本與以申報毛利率估算之晶圓廠成本結構，均未含建置期之資本化利息；當 CIP 大量轉固（Intel 18A／14A、Arizona SCIP、Micron Idaho／New York），(a) 損益表利息費用在債務不變下機械性上升，(b) 已資本化利息經折舊進入 Intel Foundry／Micron 銷貨成本；若 Ohio 等專案轉為實質停工或終止，資本化即停止且累積資本化利息隨資產減損**。**方向未定**：量級對 Micron 可能可忽略（資本化利息 ÷ 營業利益 ≈ 0.4% `[D]`），對 Intel 較大（3Q26 ≈ 10.5% `[D]`）；14A 加速擴建亦可能使資本化比上升而非下降。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：`I_inc ≡ I_exp + I_cap`；`I_cap ≤ I_inc`，且 `I_cap ≈ r_w × 平均合格支出（CIP）`；轉固後 `ΔDep = Σ I_cap,累積 ÷ 耐用年限` |
| 選擇者 | 公司（合格資產之認定、加權資本化率、暫停／恢復建置之判斷、轉固時點）；審計師（ASC 835-20-25-5「substantially all activities suspended」之適用） |
| 已讀事實 | Intel 10-Q 3Q26（sec.py 實讀）：「Interest expense is net of $ 264 million of interest capitalized in the third quarter of 2026 and $ 806 million in the first nine months of 2026 ($ 284 million in the third quarter of 2025 and $ 964 million in the first nine months of 2025)」；同表利息費用 324／282（3Q26／3Q25）、908／808（9M）；營業利益 3Q26 2,522（Intel Foundry −1,853）；Arizona SCIP「construction in progress assets of $ 5.9 billion ($ 5.6 billion as of December 27, 2025) and assets that have been placed into service of $ 14.7 billion ($ 12.2 billion …)」；「During Q2 2026, we committed to completing development of Intel 14A … We have also accelerated various manufacturing expansion projects」；總債務 50,134。Intel 10-K FY25（sec.py 實讀）：「We also capitalize interest on borrowings related to eligible capital expenditures. Capitalized interest is added to the cost of qualified assets and depreciated over the estimated useful life」；「Interest expense is net of $ 1.2 billion of interest capitalized in 2025 ($ 1.5 billion in 2024 and 2023)」；CIP 34,543（2025-12-27）vs 50,418（2024-12-28），「decreased in 2025 as Arizona SCIP placed the first tranche … into service」；「As these construction-in-progress assets are placed into service, we expect to incur depreciation expense that impacts future production costs」；Ohio：「slowed the pace of construction」「further slowed down the construction」，若無 14A 外部客戶「we would likely discontinue the new leading-edge fabrication facilities we are building in Ohio」。Micron 10-K FY26（sec.py 實讀）：「We capitalize interest on borrowings during the period of time we carry out the activities necessary to bring assets to the condition of their intended use … weighted-average capitalization rate … based on our consolidated debt portfolio」；FY25 利息費用下降「as a result of increased capitalized interest driven by higher levels of building construction」；CIP 11,424 vs 5,518；未轉固設備 61.2 億 vs 40.5 億；營業利益 99,340、利息費用 (106)。XBRL `InterestCostsCapitalized`（sec.py facts）：MU FY24／25／26＝225／321／383 百萬；TXN 2026 季別約 3 百萬（量級極小） |
| 未證之連結 | 資本化利息按廠／節點之分配（Ohio vs Arizona vs Oregon）；Ohio 是否已達「實質全部暫停」之會計門檻（公司稱 slowed，非 suspended）；累積資本化利息存量（非申報科目，須由逐年流量加總 `[D]`）；具名賣方是否以利息發生額而非利息費用建模；TSMC（20-F）、GFS（20-F）、Samsung 同口徑 |
| 量綱 | 美元／期；資本化比 ＝ I_cap ÷ (I_exp + I_cap)；損益影響 ＝ ΔI_exp（停止資本化）＋ ΔDep（轉固後折舊）；相對量 ＝ ÷ 營業利益或 ÷ 分部營業損益 |
| 半衰期 | 季到數年（轉固以季計；累積資本化利息隨 5 年級耐用年限攤提） |

## 3. B 端可觀測載體（只指名）

1. Intel 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/50863/000005086326000191/intc-20260926.htm ；10-K FY25 https://www.sec.gov/Archives/edgar/data/50863/000005086326000011/intc-20251227.htm
2. Micron 10-K FY26 https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm ；10-Q FQ3'26 https://www.sec.gov/Archives/edgar/data/723125/000072312526000015/mu-20260528.htm
3. XBRL `us-gaap:InterestCostsCapitalized`（data.sec.gov companyfacts，經 sec.py facts）：INTC、MU、TXN
4. GlobalFoundries 20-F FY25 https://www.sec.gov/Archives/edgar/data/1709048/000170904826000022/gfs-20251231.htm （未讀）
5. Ohio 進度報導（只見標題，未實讀）：https://www.tomshardware.com/tech-industry/semiconductors/intels-fab-roadmap-examined ；https://www.datacenterdynamics.com/en/news/intel-further-delays-28bn-ohio-chip-fabs-by-half-a-decade ；https://cwcolumbus.com/news/local/construction-at-intels-ohio-one-site-may-rely-on-securing-new-manufacturing-customers
6. 未讀：TSMC 20-F／季報之資本化利息；Intel 電話會原文就利息費用指引；具名賣方模型原文；ASC 835-20-25-4／-5 原文。

## 4. 不寫

H1／H5、表達工具選擇、方向判斷。

## 5. 否決觸發（測一逐條實讀）

1. **可分離性：** 資本化利息無法歸屬至可辨識之廠或節點（Ohio／Arizona／Oregon；Idaho／New York），且公司亦不揭露 CIP 按專案之分布 → 否決（C-I3′／N-02 型）。
2. **已被定價／已揭露：** 公司已給出利息費用或折舊之前瞻指引且明列資本化利息之轉換效應；或具名賣方已以利息發生額（gross interest）建模 → 否決（無錯價）。
3. **量級：** 最近 4 季資本化利息 ÷ 最近 4 季營業利益絕對值 < 5% `[D]`（門檻本卡凍結），且累積資本化利息轉固後之年折舊增量 ÷ 年銷貨成本 < 1% `[D]` → 否決（L3-A#2 型量級死）。
4. **不轉固／不停工：** 12 個月內無可辨識之大額轉固事件，亦無專案由 slowed 轉為 suspended／discontinued 之一手證據（10-Q／8-K） → 否決（窗 < 12 個月之檢驗事件缺）。
5. **方向抵銷：** 14A 加速擴建使合格支出上升，資本化比不降反升，抵銷轉固效應 → 不否決但標方向分歧。
6. **主體錯置：** 落差主要落於非美股（TSMC 已為 ADR；Samsung 非可交易）或量級僅在小型股 → 標表達約束（§7-4 三題），不在生成階段否決。
