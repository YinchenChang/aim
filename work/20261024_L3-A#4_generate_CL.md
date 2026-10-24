# L3-A#4 生成卡｜半導體製造測試：會計恆等（合資晶圓廠少數股權：合併毛利／營業利益含 100% 合資廠經濟，夥伴 49% 報酬只見於 NCI 線；NCI 買回溢價直入 APIC、永不經損益）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260924_L3-A_generate_GK.md；archive/work/20261008_L3-A#2_generate_CL.md；archive/work/20261016_L3-A#3_generate_CL.md；work/20261016_L3-A#3_test1_CL.md；archive/work/20261009_L3-I#2_generate_CL.md；archive/work/20261017_L4-A#3_generate_CL.md；archive/work/20261024_L3-P#4_generate_CL.md | EMITS: work/20261024_L3-A#4_generate_CL.md -->
**日期：** 2026-10-24　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 4→5／6）　**格：** L3-A　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L3-P#4 已於本日測一）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-16（L3-A#3、L12-A#3、L12-I#3；L3-P 已取）→ 依表序取 **L3-A**；既有生成 3 份 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `SCIP`／`Brookfield`／`Intel`／`non-controlling`，命中 12 筆，皆為「Intelligence」字串誤中之模型評測列，無關，0 筆採用。內部數字（§12）：未取用。
- 比對（本卡須異型）：
  - **L3-A#1**（GK）：有效晶粒單價（晶圓價 ÷ 良率 × 顆數），死於層別良率不可由申報反解。本卡不涉單價、良率。
  - **L3-A#2**：補助淨額法沖減 PP&E → 折舊基數，死於量級。本卡不涉補助；折舊基數不變，動的是**損益歸屬**（合併 vs 歸屬母公司）。
  - **L3-A#3**：封測材料轉嫁之毛利率分母，死於已揭露（(5)(6) 觸發）。本卡分母不變，動的是**毛利以下之少數股權扣除與權益交易繞過損益**。
  - **L3-I#2**：DOC 認股權證之分拆或有稀釋（Intel，≤ 49% 引資不觸發）。同一主體但機制為權證觸發條件（誘因），本卡為合併會計恆等；不改其結論。
  - **L4-A#3**：客戶權證收入減項。物件不同。
  - ARCH_dead：C-A3（折舊年限離散）不同物件；C-I3′／N-02（利益未分列）——本卡 NCI 按主體逐列分列於附註，非未分列型，但否決 (1) 檢其季別可分性。
- §7-10 領域最近公開：Intel 10-Q 2Q26（2026-07-24，acc `0000050863-26-000157`）；2Q26 業績稿 8-K（2026-07-23）；10-K FY25（2026-01-23）；Intel 3Q26 財報定於 **2026-10-29** 盤後（intc.com 2026-10-06 公告）＝下一檢查點，其後 3Q26 10-Q。

## 1. 落差一句

Intel 以 VIE 合併 Arizona SCIP（Brookfield 49%，Fab 52／62，18A）：Intel 有權購買 100% 晶圓產出，生產合約自 1Q26 起算，Intel 須維持最低產量，否則付 volume-related damages 予 SCIP。合併層面晶圓購價與違約金皆**內部消除**，故 **合併毛利率／營業利益 ≡ 100% 合資廠經濟，且與生產合約價格無關**；Brookfield 之 49% 只在 `NI_Intel ≡ NI_合併 − Σ s_k·NI_k` 之 NCI 線扣除（1H26 Arizona SCIP 歸屬 NCI 359M；10-K 明言 NCI「continue to increase in 2026 … increase significantly in 2027」）。另，Ireland SCIP 之 Apollo 49% 於 2026-04-08 以 14.2B 買回，**13.5B 超額直接減 APIC**，不經損益、不攤銷；此後 Fab 34 盈餘 100% 歸屬 Intel、NCI 扣除消失。種子主張：市場與公司指引以（非 GAAP）毛利率、營業利益率讀 Intel 晶圓廠經濟，而 (a) 夥伴報酬（及低稼動違約金之 49% 移轉）落在 NCI 線、隨 18A 量產遞增；(b) NCI 買回之成本永不進入 EPS 或 ROIC 之損益分子，買回後歸屬 EPS 機械性上升。**方向未定**：(a) 對歸屬盈餘偏負；(b) 對歸屬 EPS 偏正而經濟為融資置換；若 Brookfield 部分亦被買回，(a) 轉為 (b)。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：`GM_合併 = f(D_SCIP, 營運成本)`，與 `P_contract`、違約金無關（消除）；`NCI_k = s_k × (P_contract·Q + 違約金 − D_SCIP − 其他)`；`NI_Intel = NI_合併 − Σ NCI_k`。NCI 買回（ASC 810-10-45-23）：`ΔAPIC = −(對價 − NCI 帳面)`，損益表不認列 |
| 選擇者 | Intel（生產合約定價、最低產量條款、是否買回夥伴權益、非 GAAP 口徑）；Brookfield／Apollo（出資與退出）；分析師（以毛利率／EBITDA 或歸屬 EPS 估值，EV 是否加 NCI） |
| 已讀事實 | 10-Q 2Q26（sec.py `--out` 全文；`--grep` 回 0 筆屬工具與 iXBRL 標籤交錯，改以全文自行檢索）：NCI 表 1H26 Arizona SCIP 期初 9,106、partner contributions 4,082、distributions (119)、歸屬 NCI 淨利 359、期末 13,428；Ireland SCIP 歸屬 NCI 135、期末 0；總 NCI 15,601。Arizona SCIP PP&E 已投入服務 13.8B、在建 6.0B。「On April 8, 2026, we reacquired Apollo's 49 % minority ownership interest in Ireland SCIP for aggregate cash consideration of $ 14.2 billion … recognized the residual consideration of $ 13.5 billion as a reduction to our capital in excess of par value」。2Q26 合併 NI (10,848)、歸屬 NCI 185、歸屬 Intel (11,033)。業績稿 8-K 2Q26：非 GAAP 毛利率 41.8%、非 GAAP EPS 0.42；Adjusted FCF 定義扣「net SCIP partner contributions」，2Q26「Partner contributions, net (12,216)」（買回已入 FCF）。3Q26 指引非 GAAP 毛利率 42.0%、EPS 0.38。10-K FY25：NCI 淨利 2025 年 293M，「anticipate … continue to increase in 2026 … increase significantly in 2027 following … Fab 34」；風險因子：SCIP「penalties should key metrics not be attained」、14A 停止可致「substantial additional payments to our SCIP partners」；Arizona 未出資承諾 5.2B |
| 未證之連結 | 生產合約定價公式（成本加成？固定報酬？）未揭露；季別 Arizona NCI（附註僅累計期）；非 GAAP 毛利率／營業利益是否已含 NCI 調整（目前看非 GAAP EPS 為「attributable」口徑，已扣 NCI）；具名賣方 EV 是否加 NCI；Ireland 買回後 NCI 消失對 3Q26 起歸屬 EPS 之貢獻；違約金是否已發生 |
| 量綱 | NCI 歸屬淨利 ÷ 非 GAAP 歸屬淨利（%）；APIC 減項 ÷ 歸屬權益（%）；Arizona NCI 帳面 ÷ 企業價值（%）；每季 NCI 增量 ÷ 18A 晶圓量 |
| 半衰期 | 季到年（Arizona 分批投入服務 2025–2027；Fab 34 已全資；Brookfield 退出時點未知） |

## 3. B 端可觀測載體（只指名）

1. Intel 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/50863/000005086326000157/intc-20260627.htm （Note 3 Non-Controlling Interests；流動性段 Repurchase of NCI in Ireland SCIP）
2. Intel 2Q26 業績稿 https://www.sec.gov/Archives/edgar/data/0000050863/000005086326000155/q226earningsrelease.htm （非 GAAP 調節、Adjusted FCF 定義）
3. Intel 10-K FY25 https://www.sec.gov/Archives/edgar/data/50863/000005086326000011/intc-20251227.htm （Note 4、MD&A NCI 展望、SCIP 風險因子）
4. Intel 3Q26 財報日公告 https://www.intc.com/news-events/press-releases/detail/1782/intel-to-report-third-quarter-2026-financial-results （2026-10-29）
5. 未讀：3Q26 業績稿與 10-Q；電話會就 SCIP／NCI／Brookfield 之原文；Brookfield（BAM／BN）申報中 Intel 合資之報酬口徑；具名賣方模型 EV 是否計 NCI、EPS 是否剔除 NCI 變動；同型他例（TSMC 子公司少數股權、GlobalFoundries 等）。

## 4. 不寫

H1／H5、表達工具選擇、方向判斷。

## 5. 否決觸發（測一逐條實讀）

1. **可分離性：** Arizona SCIP 歸屬 NCI 無法取得 ≥ 4 個單季（或可推之累計期差）序列，且生產合約價與違約金無任何量化揭露 → 否決（C-I3′／N-02 型）。
2. **已揭露／已被定價：** 公司於業績稿或電話會逐季量化 NCI 對歸屬 EPS 之影響（含 Ireland 買回後增益），且具名賣方模型以歸屬口徑（EPS、EV 含 NCI）估值 → 否決（無錯價）。
3. **量級：** 1H26–3Q26 Arizona NCI 年化 ÷ 非 GAAP 歸屬淨利 < 5%，且 Ireland 買回後 NCI 消除之年化增益 ÷ 同分母 < 5% → 否決（量級不足，L3-A#2 型）。
4. **口徑已對齊：** 公司主要指引指標（非 GAAP EPS 等）本即「attributable」且市場流通數為該口徑，毛利率不作估值錨 → 否決（落差只存在於不被使用之指標）。
5. **APIC 繞道不具經濟意義：** 若 Ireland 買回對價 ≈ 夥伴未來應得現金流之公允值，且市場已以融資成本（債務增量 6.5B 票據之利息）計入 → 不否決 (a)，但 (b) 標「融資置換、非錯價」，不得與 (a) 合併為同向落差。
6. **重定價窗：** Brookfield 權益於 12 個月內被買回或結構終止，使 (a) 機制消失 → 否決 (a)；(b) 保留待測。

## 6. 複查觸發器（若測一不進 T）
Intel 宣布買回 Brookfield 於 Arizona SCIP 之權益；或 10-Q 首次揭露生產合約定價／違約金金額；或 NCI 歸屬淨利單季 ≥ 非 GAAP 歸屬淨利 10%。
