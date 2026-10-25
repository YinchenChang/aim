# L12-A#4 生成卡｜監理與法制：會計恆等（地方營業動產稅：稅額 ≡ 稅率 × Σ 原始成本 × 法定評估係數(年齡)——GPU 伺服器之非所得稅負擔以「原始成本」而非經濟價值計）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260922_L12-A_generate_GK.md；archive/drive/USED_20260922_L12-A_test1_GK.md；archive/work/20261008_L12-A#2_generate_CL.md；work/20261008_L12-A#2_test1_CL.md；archive/work/20261016_L12-A#3_generate_CL.md；work/20261016_L12-A#3_test1_CL.md；archive/work/20261016_L12-I#3_generate_CL.md | EMITS: work/20261025_L12-A#4_generate_CL.md -->
**日期：** 2026-10-25　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 2／6）　**格：** L12-A　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。非「已殺／刻意排除」格中最後測一最舊＝**2026-10-16（L12-A#3、L12-I#3）**；10-24 之 L4-P#4 生成卡 §0 記「最舊＝10-17」漏列此二格（L1-A#4、L3-P#4 卡皆已列之），本輪依表序補取 **L12-A**；既有生成 3 份 → #4。L12-I 留下一輪。
- Tokenomics 線索（CLAUDE.md §11）：已查 `"property tax" "personal property"`、`tax Virginia`，各 0 筆；未使用。
- 比對（本卡須異型）：
  - **L12-A#1**（TIC 法定／自願營收權重；死於申報層無兩欄）：本卡不用營收拆分。
  - **L12-A#2**（著作權或有負債 N×s vs ASC 450；死於一次性、量級、N 不可重算）：本卡為**經常性**成本，參數（稅率、係數表）由法令公告直接給出，不需重算件數。
  - **L12-A#3**（OBBBA 所得稅時序 ASC 740；死於 (3) 量級 < 5% OCF）：本卡為**非所得稅**（從價動產稅），不涉遞延稅、不涉聯邦稅法；且主體選擇以**資本密集、低毛利之 GPU 雲**為主（量級題留給測一，見否決 (3)）。
  - **L12-I#3**（§232 半導體關稅抵銷配額之在建誘因）：不涉關稅。
  - 鄰型：C-A3／C-A4（帳面折舊年限、離散減損）——本卡之係數表為**稅法評估**，與帳面年限無關，且恰相反：法定係數不隨 GPU 經濟價值下跌而調整。C-P4（水耗非損益科目）：本卡死因若出現亦屬 C-P4 型「非分列科目」，見否決 (6)。L2-*（資料中心實體）未有稅制型。
- §7-10 領域最近公開：Loudoun COR 新評估表（公告 2025-11-07／11-20，**2026-01-01 生效**）；Loudoun FY2027 Adopted Budget 一般基金收入表；Virginia FY27–28 預算協議（VPM 2026-06-20：銷售稅豁免保留至 2035、兩年期資料中心能源稅約 1.2B）；NTU／Walczak 動產稅研究（2026-10-13）。下一檢查點：Loudoun FY2028 預算提案（約 2027-02）、2027 年 Virginia 議會（能源稅於 2028-06-30 屆期）、各 GPU 雲 3Q26 10-Q。

## 1. 落差一句

地方營業動產稅為法定恆等式：**`T_t = r × Σ_v C_v × f(t − v)`**（`C_v`＝v 年購入之原始成本、`f`＝法定評估係數、`r`＝每 100 美元稅率），與設備經濟價值無關。Loudoun 2026 起資料中心電腦設備係數由 50/40/30/20/10% 改為 **60/45/30/15/10/5%**（六年），稅率 **$4.15／$100**，故一台伺服器首年稅 ≈ 原始成本 2.49%（舊表 2.08%）、六年累計 ≈ 6.85% `[D]`；而 NTU（Walczak）指伺服器三年即近乎過時、多州以 40–56% 評估三年機。**落差＝GPU 雲／算力租賃之單位經濟（每 GPU 小時成本＝電力＋折舊＋利息）是否已計入此一「以原始成本計、隨 $／MW 而非 MW 縮放」之稅負**：AI 機櫃每 MW 設備成本數倍於 CPU 世代，動產稅每 MW 隨之放大，而電力類稅（Virginia 新能源稅）只隨 kWh；若租價下滑而法定係數不變，稅負 ÷ 租金收入於設備後期上升。**方向未定**：地方競相降稅（Fredericksburg $3.40→$1.25、與 Prince William 同級）與州銷售稅豁免保留，可使有效稅率遠低於 Loudoun。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（法定稅基）：`T_t = r·Σ_v C_v f(t−v)`；反解：`Σ_v C_v f(·) = T_t / r`（Loudoun FY2027 預算 $879.09M ÷ 4.15% ≈ **21.2B** 評估值 `[D]`） |
| 量綱 | `r`［$／$100 評估值］；`C`［美元原始成本］；`f`［無因次，%］；`T`［美元／年］。比值：`T / C`［%／年］、`T / 租金收入`［%］、`T / MW`［美元／MW·年］ |
| 可見端 | Loudoun COR 評估表（新舊兩版）；Loudoun FY2027 預算之「Computer Equipment Data Centers」收入序列：FY23 581.6M、FY24 684.8M（+17.8%）、FY25 699.8M（**+2.2%**）、FY26 adopted 794.8M、FY27 adopted 879.1M；Virginia 預算協議（能源稅、豁免保留）；NTU 各州三年機評估比 |
| 指名不可見端 | GPU 雲主體各管轄區之設備原始成本分布；地方協議（PILOT／降稅）條款；租約是否把動產稅轉嫁承租人；申報層之動產稅科目——CoreWeave FY25 10-K 全文以 `property tax`／`personal property` 檢索 **0 筆**（`sec.py doc --grep`） |
| 主張 | 動產稅負擔由法令參數與原始成本決定，可自公開參數重算；若 GPU 雲單位經濟未計或低估之，則法定係數變動（Loudoun 2026）、地方稅率競爭與州稅期滿將造成可觀測之成本差 |
| 表達工具型態（只指名，不選券） | 美股上市 GPU 雲／算力租賃商、資料中心 REIT（設備多屬承租人，故多半為間接）普通股及上市選擇權。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| Loudoun COR 評估表（2026 新表＋舊表） | https://www.loudoun.gov/6301/Business-Personal-Property-Tax-Assessment |
| Loudoun Now（2025-11-07；五年 50% → 六年 60%、PFM 標竿研究） | https://www.loudounnow.com/news/county-assessors-restructuring-personal-property-valuation-schedules/article_cd35dba4-037b-4117-b4f4-9bc320e976be.html |
| Blue Ridge Leader（2025-11-20；2026-01-01 生效） | https://blueridgeleader.com/?p=25905 |
| Loudoun FY2027 Adopted Budget 一般基金收入（資料中心電腦設備收入序列、4.150 稅率） | https://sheriff.loudoun.gov/DocumentCenter/View/221479/General-Fund-Revenue-PDF |
| Loudoun 資料中心稅收頁（$4.15／$100，TY2026–2027） | https://www.loudoun.gov/6409/Tax-Revenues-County-Budget |
| Fredericksburg 資料中心動產稅率 $1.25（原 $3.40；與 Prince William 同級） | https://news.fredericksburgva.com/?p=5030 |
| Virginia FY27–28 預算協議（VPM 2026-06-20） | https://www.vpm.org/generalassembly/2026-06-20/lucas-torian-scott-spanberger-fy2027-fy2028-budget-deal |
| Virginia 2026 常會未達成預算（Cardinal News 2026-03-14；豁免 FY25 為業界省近 2B） | https://cardinalnews.org/2026/03/14/the-2026-general-assembly-session-wraps-with-no-budget-special-session-on-the-horizon/ |
| NTU／Walczak 動產稅研究（2026-10-13） | https://www.ntu.org/publications/detail/new-research-shows-many-state-property-tax-laws-punish-fast-evolving-technology |
| CoreWeave FY25 10-K（動產稅檢索 0 筆；長期資產依地理分列） | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm |
| 其他 GPU 雲（Nebius、IREN、Applied Digital 等）10-K／10-Q；Prince William、Henrico、Texas、Georgia 等郡稅率與係數表 | 測一以 `sec.py` 與 WebSearch 取得 |

不宣稱缺口已存在、不宣稱市場未計入、不宣稱淨方向。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 有效稅率遠低於 Loudoun：地方競相降稅（Fredericksburg $1.25、Prince William 同級），新 AI 容量流向低稅管轄區；Loudoun FY25 收入僅 +2.2% 即一跡象 | Fredericksburg 稿；Loudoun FY2027 預算序列 | 機制量級小或已被選址吸收 |
| R2 | 稅負多由承租人（超大規模業者）承擔，對其營業現金流微不足道 | Loudoun 稅收頁（電腦設備屬設備所有人）；L12-A#3 測一之 OCF 量級口徑 | 重大性不足 |
| R3 | 稅制屬地方公開參數，GPU 雲之 TCO 模型與承租定價已含之 | 待測一找具名 TCO 模型（SemiAnalysis 等）原文 | 落差已定價 |
| R4 | 評估過高已成政策議題，係數表反向修正（縮短年限、降評估比）之可能 | NTU／Walczak 2026-10-13 | 方向反轉 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) ≥ 1 份具名 GPU 雲 TCO 或單位經濟模型（賣方、SemiAnalysis、公司投資人簡報）已明列地方動產稅或「property taxes」之每 GPU／每 MW 成本（R3 成立）。
- (2) 上市 GPU 雲主要設備所在管轄區之加權有效 `r × f(1)` < 測一自定門檻（如原始成本 1%／年），或主要容量位於動產稅豁免／協議減免轄區（R1）。
- (3) `[D]` 量級：最可得估計之年動產稅 ÷ 該主體最近年度營收 < 測一自定門檻（如 2%），或 ÷ 調整後 EBITDA < 5%（R2）。
- (4) 測一無法取得 ≥ 2 個管轄區之 `r` 與 `f` 原文，或無法取得任一上市主體之設備地理分布，使恆等不可對帳。
- (5) 本卡只能以 L12-A#3（所得稅時序）、C-A3／C-A4（帳面折舊年限）或 L12-I#3（關稅）重述（重疊判讀）。
- (6) 可交易主體之 10-K／10-Q 均不分列動產稅或「taxes other than income」，且無公司說明可替代（C-P4 型表達層）。

複查觸發器（若日後殺）：任一上市 GPU 雲或 DC REIT 分列動產稅科目或每 MW 稅負；Loudoun 等主要郡改係數表或稅率；Virginia 能源稅續期或銷售稅豁免提前終止；具名 TCO 模型首次納入地方動產稅。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：營業成本或 SG&A 內之 property／non-income taxes；長期資產地理分列；租約轉嫁條款。
2. 可交易工具：美股上市 GPU 雲、算力租賃商、DC REIT 普通股與選擇權。
3. 半衰期：係數表由郡每年公告；稅率每年預算定；州能源稅以兩年預算週期定。

## 7. 本輪寫入

本卡；QUEUE 新列（ANALYST 測一）；ARCH_matrix L12-A 格標「已生成 #4」；FUNNEL §3 未測格計數；`export/LEADS_算力收支.md` 追加 2 筆（Loudoun FY2027 資料中心電腦設備稅收、Virginia 兩年期資料中心能源稅）。不改 L12-A#1–#3、L12-I#1–#3、L12-P#1–#4、C-A3、C-A4、C-P4、L2-*。
