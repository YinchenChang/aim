# L6-A#2 生成卡｜雲端與基礎設施服務：會計恆等（電力轉嫁份額 θ：營收 ≡ 租金＋θ·電費；電價衝擊在「總額法認列之轉嫁」下膨脹營收、壓低毛利率而不改租金經濟）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260927_L6-A_generate_GK.md；archive/drive/USED_20260927_L6-A_test1_GK.md；archive/drive/USED_20260928_L6-P_generate_GK.md；archive/drive/USED_20260928_L6-I_generate_GK.md；archive/drive/USED_20260928_L13-A_generate_GK.md；archive/work/20261007_L2-A#2_generate_CL.md | EMITS: work/20261011_L6-A#2_generate_CL.md -->
**日期：** 2026-10-11　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L6-A　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L5-I#2 已於本日測一，Q-0020 done）。尚無 #2 且非已殺／刻意排除之格中，最後測試日最舊＝**L6-A**（測一 2026-09-27；L5-P 測一同日但 T 2026-09-29 較新）。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py colocation pass-through reimbursement PJM`，**命中 0 筆**；載體由 `sec.py` 與 WebSearch／WebFetch 原文取得。
- 比對之舊檔與死因型態，本卡須異型：
  - **L6-A#1**（`archive/drive/USED_20260927_L6-A_generate_GK.md`；測一 `archive/drive/USED_20260927_L6-A_test1_GK.md`，部分通過｜不進 T）：時序存量比 `已簽未交付 MW／已交付 MW` 領先營收；失敗在跨主體單位不可加與極性不定。本卡**換恆等式與變數**：營收之**組成**（租金 vs 電費轉嫁），變數＝轉嫁份額 θ 與電價，非交付時序、非 RPO。
  - **C-A3**（ARCH_dead #5，L6）：折舊年限。本卡不涉折舊。
  - **L6-I**（長約逆選擇／backlog 品質）、**L6-P**（單卡故障率×N）：不同型態。
  - **L13-A**（未開始租＋RVG＋專案槓桿）、**L2-A#2**（利息資本化與在建轉營運）：資產負債表與費用時點，非營收組成。
  - **L1-A#2／L1-I#2**（能源層）：本卡只用電價為外生輸入，不主張電價方向；重疊列為否決 (5)。
  - **T-15**：委託資本外；不得改寫成空方。
- §7-10 領域最近公開：DLR 10-Q 期 2026-06-30（acc `0001104659-26-089296`，2026-07-31）；EQIX 10-Q 期 2026-06-30（acc `0001101239-26-000147`）；PJM 2027/28 BRA 結果 2025-12-17。下一檢查點＝兩家 Q3 2026 10-Q（約 2026-10 下旬至 11 上旬）；PJM 2028/29 BRA。

## 1. 落差一句

主機代管／批發資料中心之電費轉嫁若以總額法（principal）認列為營收，則 `Rev ≡ Rent + θ·C_power`，`Margin ≡ (Rent − OpEx_x − (1−θ)·C_power) / (Rent + θ·C_power)`。電價上漲（PJM 2027/28 容量價觸頂、資料中心負載為主因）在高 θ 主體**膨脹營收成長、機械性壓低毛利率／EBITDA 率而不改租金經濟**；在低 θ 主體（電費含於固定月租）則**直接吃掉利潤**。種子主張：若市場以單一「營收成長＋利潤率」框架比較兩類主體，則同一電價衝擊被讀成相反之營運訊號；落差＝θ 未被分開定價。本卡不定方向之大小，只立可拒絕之恆等式。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（營收組成＋總額法認列）；非誘因、非物理上界、非時序存量比 |
| 選擇者 | 無（恆等）；θ 由合約型態決定（批發／Turn-Key 多為轉嫁；零售 colocation 多為含電月租或計量電） |
| 可見端 | DLR 10-Q：「Reimbursements are recognized in rental and other services revenue … as we are the primary obligor」；Stabilized 租金營收增加「primarily due to increases in new leasing and renewals and higher utilities reimbursements」；「cost of electric power and other utilities is a significant component of operating expenses」。EQIX 10-Q：成本「utility costs including electricity」；Americas 成本「$26 million of higher utilities expense, driven by increases in power costs」；RPO 排除「metered power」 |
| 指名不可見端 | 轉嫁營收之美元額（DLR 未分列）；θ 之主體別數值；各主體電價避險比例 |
| 主張 | 同一電價衝擊 ΔC：高 θ 主體 ΔRev ≈ θ·ΔC、ΔMargin < 0（分母膨脹）、Δ租金利潤 ≈ 0；低 θ 主體 ΔRev ≈ 0、Δ利潤 ≈ −(1−θ)·ΔC |
| 表達工具型態（只指名，不選券） | 美股可交易之資料中心 REIT／主機代管／HPC 租賃主體（DLR、EQIX 等）。不選券 |
| 重疊 | L6-A#1（同主體不同恆等）；L1（電價外生）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. DLR 10-Q 期 2026-06-30（收入認列政策、Stabilized／Non-stabilized 營收拆解、營業費用段）。https://www.sec.gov/Archives/edgar/data/1297996/000110465926089296/dlr-20260630x10q.htm
2. EQIX 10-Q 期 2026-06-30（成本結構、區域成本變動之 utilities 句、RPO 排除計量電）。https://www.sec.gov/Archives/edgar/data/1101239/000110123926000147/eqix-20260630.htm
3. PJM 2027/28 BRA 結果新聞稿 2025-12-17：「$333.44/MW-day (UCAP)」、「came in at the FERC-approved cap」、短缺 6,623 MW、「Nearly 5,100 MW … attributable to data center demand」。https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2025-releases/20251217-pjm-auction-procures-134479-mw-of-generation-resources.pdf
4. 測一須另取：DLR／EQIX 10-K 之電力合約型態與避險揭露；DLR 補充包是否分列 utility reimbursements；具名賣方是否以「剔除轉嫁之營收／利潤率」比較主體；CoreWeave／Core Scientific 等 HPC 租約之電費歸屬條款。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | REIT 以 NOI／AFFO 定價，轉嫁在 NOI 層互抵，營收膨脹不影響估值 | DLR 10-Q 自報 Same-Capital cash NOI 與 Stabilized 拆解（上列 #1） | 無落差 |
| R2 | EQIX 管理層 EBITDA 率目標之槓桿為定價、成本改善、SG&A，未列電價——電價已由避險與月租調價吸收 | EQIX Q2 2026 法說摘要 https://vectorshift.ai/research/companies/equinix/earnings/2026-q2 | 低 θ 主體亦無利潤衝擊 |
| R3 | 營收成長主因新租與續約，轉嫁為次要項 | DLR 10-Q 原句「primarily due to increases in new leasing and renewals and higher utilities reimbursements」（同列） | 量級不足 |
| R4 | 電價為能源層（L1）機制，本卡只是轉述 | L1-A#2／L1-I#2 | 不可分離 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 申報層（10-K／10-Q／補充包）無法取得轉嫁營收美元額或 θ 之任何區間，只剩定性句（恆等之變數不可觀測）。
(2) 公開層（業者原文或具名賣方）已明文以「剔除電費轉嫁之營收成長／利潤率」報告或比較主體，使 θ 已被分開定價（R1 成立）。
(3) 轉嫁營收占營收比例之可得區間 × 合理電價變動 < 營收或利潤率之一般季波動（量級不足，R3 成立）。
(4) 主要主體電價避險或固定價購電覆蓋 ≥ 窗期，使 ΔC 於 12 個月以上窗內近零。
(5) 可運作對照只能寫成電價方向（L1）、交付時序（L6-A#1）、折舊（C-A3）或融資槓桿（L13-A）。

複查觸發器（若日後殺）：任一美股可交易資料中心主體於 10-K／10-Q 或補充包首次分列 utility reimbursements／power pass-through 營收；或 PJM／其他 ISO 容量價再創上限且主體揭露電價對利潤率之量化影響。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Rental and other services（含轉嫁）、utilities expense、Stabilized 營收拆解、EBITDA 率。
2. 可交易工具：DLR、EQIX 美股（不選券）。
3. 半衰期：PJM 容量價逐年拍賣、轉嫁按期認列——電價傳導至營收為當期，落差半衰期或短於 12 個月窗。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L6［A］標「#2 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L6-A#1／L6-P／L6-I／C-A3／L13-A／L2-A#2／L1 結論。
