# L13-P#3 生成卡｜資本與融資結構：守恆（母公司現金按季封閉：OCF＋外部融資＋Δ現金 ≡ capex＋融資租賃本金＋股利＋RSU 代扣稅＋回購＋併購；回購已觸零下界後，capex 超過 OCF 之每一元只能由債、普通股、強制可轉特別股或表外承擔，流通股數由年減轉年增）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20261002_L13-P_generate_GK.md；archive/work/20261013_L13-P#2_generate_CL.md；work/20261013_L13-P#2_test1_CL.md；work/20261020_L13-A#3_test1_CL.md | EMITS: work/20261020_L13-P#3_generate_CL.md -->
**日期：** 2026-10-20　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 3→4／6）　**格：** L13-P　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L11-I#3 本日測一，Q-0077 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-13（L13-P、L13-I、L14-P、L14-A）；依表序取 **L13-P**。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `capex buyback free cash flow hyperscaler`，3 筆皆 ChatGPT 需求／OpenAI 成本列，相關命中 0；未用。載體全由本輪 sec.py／WebSearch／WebFetch 實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L13-P#1**（`archive/drive/USED_20261002_L13-P_generate_GK.md`）：GPU 熱循環計數 vs 會計年限；死因＝現場計數無申報。本卡守恆量為**現金流量表各列**，全部於 10-Q 逐季分列。
  - **L13-P#2**（`work/20261013_L13-P#2_test1_CL.md`）：同站址 MW 互斥＋子公司有擔保票據限制性支付閘（礦商出租方）。本卡在**承租方／買方母公司**層，無結構隔離、無 indenture 閘；樞紐為回購之零下界（不能為負）。
  - **L13-A#1**（入表租賃≠義務上界：未開始租／RVG／JV）：本卡**不估表外義務**，只把表外融資（如 JV、未開始之租約）當作封閉式之洩漏項，列為否決 (3)。
  - **L13-A#2**（客戶預付入 OCF，Oracle）：本卡不用 Oracle、不論 OCF 之組成。
  - **L13-A#3**（EPS 分母恆等：ATM 加權時滯＋if-converted，Oracle；死因＝公司 ATM 後直接給 EPS 指引）：本卡之股數只是守恆之下游讀數；載體公司（Alphabet、Meta）不給 EPS 指引；主張為**現金缺口之來源組合**，非加權時滯。
  - **L13-I#1／#2**（信評資訊含量；擔保人認股權）、**C-A4／C-A3**（ARCH_dead #4–5，重定價窗／折舊樞紐）：不涉；不重開。**T-15**（CoreWeave，委託資本外）：不涉。
- §7-10 領域最近公開：Alphabet 10-Q 2Q26（2026-07-23）、Meta 10-Q 2Q26（2026-07-30）與 8-K Ex.99.1（2026-07-29）。下一檢查點＝3Q26 10-Q／財報（約 2026-10 下旬至 11 初）；2027 capex 首次指引（4Q26 財報，約 2027-01／02）。

## 1. 落差一句

2026 上半年 Alphabet 與 Meta 回購皆為 0（2025 同期 28.31／22.92 bn），capex 已逼近或超過 OCF（Alphabet 2Q26 capex 44.93 vs OCF 39.07 `[D]`；Meta 2Q26 FCF 0.78 bn），Alphabet 已發行普通股 30.50＋強制可轉特別股 19.06＋債 56.23 bn，稀釋後加權股數 12,198M（2Q25）→ 12,309M（2Q26）。種子主張：回購觸零後，股東回饋不再是吸收 capex 波動之緩衝，capex 指引之每一增量依守恆式**一對一**轉為外部融資，其股本部分直接進流通股數；可拒絕之主張＝自 2Q26 起，季度「capex＋股利＋代扣稅＋併購 − OCF」與「淨外部融資＋Δ現金」逐季封閉（差 ≤ 少量），且股本融資占外部融資之比例與股數年增率可由下一季 10-Q 讀出。本卡不主張方向與量級，不主張股價。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆（P）**：現金流量表按季封閉；回購 B ≥ 0 為硬下界；股利 Dv 與 RSU 代扣稅 W 為黏性項（後者可改 sell-to-cover 轉成稀釋）。B 觸零後：Δ外部融資 ≡ Δcapex − ΔOCF＋ΔDv＋ΔW＋Δ併購 − Δ(Δ現金) |
| 守恆量 | 季度現金（美元／季）；下游計數＝流通股數（股） |
| 選擇者 | 公司財務長（債／股／可轉／表外／動用現金之組合）；capex 由 AI 基建計畫決定 |
| 可見端 | 10-Q 現金流量表：OCF、Purchases of PP&E、融資租賃本金、Repurchases、Dividends、Net payments related to stock-based award activities、Proceeds from issuance of common stock／mandatory convertible preferred／debt、Repayments；股東權益表；稀釋加權股數；8-K capex 指引 |
| 指名不可見端 | 季內 ATM 實際使用量（至 10-Q 方見）；表外 JV 之出資與未開始租約之未來現金；賣方模型之股數假設 |
| 量綱 | 美元／季；股；比例（股本融資 ÷ 外部融資）無因次 |
| 外部參照物（測一查證） | 資本密集期回購暫停之前例（如 2000 年代電信、2010 年代能源業 capex 高峰期之回饋—融資替代）；公司自身 2024–2025 回購序列 |
| 表達工具型態（只指名，不選券） | 美股大型平台普通股、其強制可轉特別股、投資級公司債；不選券 |
| 重疊 | L13-A#3（股數）、L13-A#1（表外）、L6 系列（capex 側）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Alphabet 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm ：6M26 vs 6M25 Repurchases of stock 0／28,306；Dividend payments 5,231／4,977；Net payments related to stock-based award activities 12,056／5,731；Proceeds from issuance of common stock 30,499／0；mandatory convertible preferred 19,063／0；debt 56,226／31,378；Repayments 5,253／18,397；Acquisitions 33,697／353；「In the three and six months ended June 30, 2026, there were no repurchases」；授權餘額 $69.5 bn。XBRL：OCF 6M 84.86 bn、PP&E 6M 80.60 bn。
2. Meta 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm ：「We did not repurchase any shares of Class A common stock during the six months ended June 30, 2026」；授權餘額 $25.03 bn；6M 代扣稅 8.70 bn、股利 2.70 bn；May 2026 Notes；票據本金 84.00 bn。XBRL：OCF 6M 64.09、PP&E 6M 49.11、債 6M 24.91 bn。
3. Meta 8-K Ex.99.1 2Q26 https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm ：「Capital expenditures, including principal payments on finance leases, were $31.08 billion」；「free cash flow was $784 million」；FY26 capex「$130-145 billion」；現金及有價證券 90.26 bn。
4. XBRL 稀釋加權股數（sec.py facts）：Alphabet 12,495（2Q24）…12,198（2Q25）／12,203（3Q25）／12,238（1Q26）／12,309（2Q26）；Meta 2,610…2,570（2Q25）／2,564（1Q26）／2,566（2Q26）。
5. 市場讀數（線索）：247 Wall St.（Alex Sirois，2026-08-12）https://247wallst.com/investing/2026/08/12/ai-race-based-dilution-why-meta-is-more-dangerous-than-alphabet/ ：Alphabet「closed a $49.6B equity raise, opened an ATM program of up to $40B」、capex「$195B to $205B with more to come in 2027」、Meta 股權授予將「directly expand the net share count」；無股數或缺口量化。

缺段（§7-2）：具名賣方對 2027 股數或外部融資組合之量化；ATM 季內使用量；表外 JV 出資序列。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 回購暫停、股本融資與稀釋已被公開討論 | #5 247 Wall St. | 已定價 |
| R2 | 現金餘額（Meta 90.26 bn）與 OCF 成長可吸收缺口，守恆式不綁定 | #3 | 鬆弛項過大 |
| R3 | 表外（JV、未開始租約）可承擔增量，使表內封閉無資訊 | L13-A#1 型 | 洩漏 |
| R4 | 封閉式為會計恆真，無預測內容 | — | 同義反覆 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 封閉式各項無 ≥ 4 季同口徑序列（含回購觸零前後），或股本融資與債務融資不可分列。
(2) 具名賣方或公司已量化 2027 外部融資組合或股數路徑且與本卡可拒絕主張一致——已定價。
(3) 表外融資（JV 出資、未開始租約）之量級 ≥ 表內外部融資之同量級且未揭露——洩漏使封閉失去約束。
(4) 現金及有價證券 ÷ 預期年缺口 `[D]` ≥ 4 年——鬆弛項使回購零下界不綁定。
(5) 可運作對照只能寫成 EPS 分母時滯（L13-A#3）、表外義務上界（L13-A#1）或結構隔離之限制性支付（L13-P#2）。
(6) 重定價窗（≥ 12 個月）內無檢驗事件（3Q26／4Q26 10-Q、2027 capex 指引），或回購已於窗前宣布恢復。

複查觸發器（若日後殺）：任一載體宣布恢復回購或取消股利；首次揭露 ATM 使用量或表外 JV 出資序列；2027 capex 指引首次發布；具名賣方發布股數／外部融資組合模型。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：現金流量表融資段各列、Purchases of PP&E、融資租賃本金；稀釋加權股數。
2. 可交易工具：大型平台普通股、強制可轉特別股、投資級公司債。不選券。
3. 半衰期：季度 10-Q；年度 capex 指引。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0078；`query/ARCH_matrix.md` L13［P］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L13-P#1／#2、L13-A#1–#3、L13-I#1／#2、C-A3／C-A4 結論；不寫 T-15。
