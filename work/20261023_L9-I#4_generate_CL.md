# L9-I#4 生成卡｜受規管 HITL：誘因（環境式 AI 病歷之編碼強度——醫師簽署作合規掩護、提供者升碼、付款方自動降碼之軍備競賽）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260922_L9-I_generate_GK.md；archive/drive/USED_20260922_L9-I_test1_GK.md；archive/work/20261008_L9-I#2_generate_CL.md；work/20261008_L9-I#2_test1_CL.md；archive/work/20261015_L9-I#3_generate_CL.md；work/20261015_L9-I#3_test1_CL.md；work/20261023_L9-A#4_test1_CL.md | EMITS: work/20261023_L9-I#4_generate_CL.md -->
**日期：** 2026-10-23　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 6／6）　**格：** L9-I　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L9-A#4 本日測一不通過）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-15 兩格（L9-I#3、L12-P#3）；依佇列序取最早者 L9-I（Q-0050）；既有生成 3 份 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `ambient scribe`／`coding intensity`／`E/M`，命中 0 筆；未使用。內部數字（§12）未取用。
- 比對（本卡須異型）：
  - **L9-I#1**（`archive/drive/USED_20260922_L9-I_generate_GK.md`；測一同目錄 test1）：SaaS 賣方把 AI 成本折進 SKU；死於 SKU 改版不在申報層。本卡不涉 SaaS、不涉 AI 成本列。
  - **L9-I#2**（`work/20261008_L9-I#2_test1_CL.md`）：付款方初判拒付之不申訴留存率；死於 (2) AI 連結只剩 L9-P 型載體。本卡選擇者為**提供者**（升碼），付款方之回應為**按級降碼**（付款額調整，非拒付／申訴）；載體為理賠層編碼分布，非 AI 建議核可率。
  - **L9-I#3**（`work/20261015_L9-I#3_test1_CL.md`）：PFS 每碼 RVU 內嵌時間（單價租）；死於 (1)(3)。本卡為**碼別組合**（同一就診被編為較高級 E/M 或較高嚴重度 DRG），單價不變、組合上移；涉商業保險，不限 Medicare FFS。
  - **L9-A#3**（MA RAF 編碼存量）：本卡**排除** MA 風險調整（RAF／HCC）；限商業與 FFS 之 E/M 級別及住院嚴重度。若測一發現唯一可量化之 AI 編碼效果在 RAF，即依否決 (2) 併入 L9-A#3 型。
  - **L9-P**（ARCH_dead #1）：不量 HITL 工時或核可率；量的是已簽署病歷所生之碼別分布。C-A1（#6）、C-I5（#18）、C-A2（#9）：不涉。
- §7-10 領域最近公開：ELV 10-Q 3Q26（2026-10-21）；HCA 10-Q 2Q26（2026-07-28）；CI 10-Q 2Q26（2026-07-30）；Becker's 2026-07-01（UHC CEO）；Digital Health Insights 2026-07-13（PwC 2027 趨勢、UCSF 研究）；hccbuddy 2026-07-08（BHI 2026-03、Trilliant 2026-03）；ACDIS 2026-04-23；Parker Poe 2026-06-10（OIG MA ICPG 2026-02）。下一檢查點＝各家 3Q26 10-Q／電話會（2026-10 下旬–11 初）、PwC／Milliman 2027 定價季、Cigna R49 滿一年（2026-10-01 後）。

## 1. 落差一句

環境式 AI 病歷（ambient scribe）把就診內容完整轉錄並結構化，醫師簽署後即為計費依據——**醫師簽署是 HITL 合規門，也是法律掩護**：碼別上移以「文件更完整」為正當理由，提供者（醫院體系、醫師團體）有誘因採用並不回調。可讀事實：Trilliant（六大體系，2018–2024）新病人高強度 E/M 占比上升 12–20 個百分點；BHI 估 2023–2024 快增醫院每人住院成本 +9% 中約 20% 來自編碼強度；UCSF（JAMA Netw Open）AI 病歷使用者每週多計 1.81 RVU、拒付未升。付款方回應已成形：Cigna R49（2025-10-01 起）對 99204–05／99214–15／99244–45 自動降一級；ELV、CNC 以 AI 付款稽核追趕；UHC CEO 稱此推升趨勢但「不會持續」（飽和論）。**種子主張**：市場把付款方醫療成本率上升主要讀成利用率／罹病度，把提供者單位收入（如 HCA 每約當住院收入 +6.0%）讀成價格與組合；其中一段是由 AI 簽署病歷驅動、規則上合法、可被付款方演算法逆轉之**編碼強度租**。**方向未定**：(a) 一次性階升，付款方以 1–2 年定價滯後吸收、提供者保有；或 (b) 付款方降碼／稽核擴散，租金回吐、提供者單位收入成長放緩。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：選擇者＝提供者（採用 ambient AI、編碼政策）、簽署醫師（HITL 合規門）；對手＝付款方（自動降碼、付款稽核、定價）；規則端＝CMS／OIG（E/M 文件要件、稽核）、州保險監理（降碼政策是否受限） |
| 恆等（僅定義） | 專業／住院收入＝件數 × Σ(碼別占比 × 單價)；碼別占比上移 → 單位收入 ↑，件數與單價不變 |
| 已讀事實 | 見 §1；HCA 10-Q 2Q26：「6.0% increase in revenue per equivalent admission」，並註明受 FL 州指定支付影響；「coding」「acuity」「intensity」皆 0 筆。ELV 10-Q 3Q26：醫療成本趨勢歸因「utilization … unit cost」「higher population acuity」，「coding」0 筆；營收增「premium rate increases … in recognition of medical cost trends」。CI 10-Q 2Q26：「coding」0 筆，AI 只見風險因子。MSMS：R49 以 12 個月理賠比對同儕「consistent pattern of coding at a higher E/M level」。PwC（經 DHI 轉述）：近 70% 受訪精算師把 AI 文件／編碼工具列前三大成本驅動。OIG MA ICPG（2026-02）警示 AI 提示補碼（MA 範圍，屬 L9-A#3 側）。 |
| 未證之連結 | 申報層把編碼強度與醫療成本率或單位收入連結之句或量；理賠層 E/M 分布按 AI 採用與否可分之公開序列（CMS Part B PUF 是否足以區分）；降碼回吐之量 |
| 量綱 | 高級 E/M 占比（百分點）；編碼強度歸因成本 ÷ 付款方醫療成本（%）；提供者單位收入成長中之組合貢獻（百分點） |
| 選擇變數 | 提供者：採用範圍、編碼稽核；付款方：降碼門檻、稽核、定價假設；監理：E/M 文件要件、降碼政策之限制（醫學會反對） |
| 半衰期 | 商業定價 1 年；Cigna R49 以 12 個月同儕比對；飽和論下 2–3 年 |

## 3. B 端可觀測載體（只指名）

1. Trilliant／BHI 經 ACDIS 2026-04-23 https://acdis.org/node/70256 ；hccbuddy 2026-07-08 https://hccbuddy.com/news/ai-documentation-coding-intensity-payer-downcoding-2026
2. DHI 2026-07-13 https://dhinsights.org/news/ambient-ai-scribes-are-boosting-provider-revenue-insurers-are-already-clawing-it-back ；UCSF 研究 https://pmc.ncbi.nlm.nih.gov/articles/PMC12738533 （本輪 reCAPTCHA 擋，未讀原文）
3. Becker's 2026-07-01 https://www.beckerspayer.com/payer/unitedhealthcare-ceo-ai-driven-cost-inflation-not-going-to-be-persistent/ ；HFMA 2025-07-29 https://www.hfma.org/revenue-cycle/reeling-payers-plan-to-increase-scrutiny-of-providers-coding-practices/
4. Cigna R49：MSMS https://www.msms.org/news/despite-physician-pushback-cignas-new-downcoding-policy-went-effect-oct-1-act-now ；AAFP https://www.aafp.org/pubs/fpm/blogs/gettingpaid/entry/cigna-downcoding-em.html
5. ELV 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/1156039/000115603926000071/elv-20260930.htm ；CI 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1739940/000173994026000065/ci-20260630.htm ；HCA 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/860730/000119312526321077/hca-20260630.htm
6. OIG：Parker Poe 2026-06-10 https://www.parkerpoe.com/news/2026/06/oig-guidance-warns-physician-practices-of-compliance-risks
7. 未讀：UNH／CNC／CVS／HUM 3Q26 10-Q 與電話會原文；THC／UHS／CYH 10-Q 之單位收入組合；CMS Part B 利用 PUF 之 E/M 級別序列；Milliman「code shift decade」；PwC Behind the Numbers 2027 原文；Cigna R49 政策原文。

缺段（§7-2）：申報層 0 筆僅限上列三份 10-Q 與 `sec.py --grep` 字面詞；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 飽和、非持續：AI 驅動之成本壓力是一時現象 | UHC CEO Tim Noel（載體 3） | 窗短 |
| R2 | 已定價：付款方已以「premium rate increases in recognition of medical cost trends」重訂價；PwC 2027 趨勢 9% 已含 | ELV 10-Q（載體 5）、PwC（載體 2） | 已定價 |
| R3 | 量級小：UCSF 每次就診僅 +0.04 RVU；勞力、用品、利用率貢獻大於 AI 工具 | 載體 2 | 量級小 |
| R4 | 文件更完整＝正確編碼，非升碼；歸因不可分 | UCSF 作者（載體 2）、ELV 稱支持改善文件之 AI（載體 3） | 歸因 |
| R5 | 申報層不分列（同 L9-A#2／#3、L9-I#3 死因） | 載體 5 之 0 筆 | 表達層 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) ≥ 2 家上市付款方或提供者之 10-K／10-Q 皆無句或量把編碼強度連至醫療成本率或單位收入，**且**無 ≥ 2 期可公開取得、可區分 AI 採用之理賠層 E/M 級別或嚴重度序列；或
(2) 可量化之 AI 編碼效果只存在於 MA RAF（L9-A#3 型）、拒付／申訴（L9-I#2 型）或 HITL 工時／核可率（L9-P 型）；或
(3) `[D]` 量級：編碼強度歸因成本 ÷ 付款方醫療成本，或提供者單位收入成長中可歸因組合上移者 < 1%；或
(4) 已定價：付款方已明示於定價中量化編碼強度，或具名賣方／評等機構／精算顧問已逐家量化其對 MBR 或提供者收入之影響；或
(5) 12 個月內無可觀測驅動：無付款方新增或擴大降碼／稽核政策、無州法或 CMS／OIG 就 AI 文件之 E/M 要件動作、亦無提供者揭露降碼回吐。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：付款方醫療成本率、前期理賠準備發展；提供者每約當住院收入、付款方組合。2. 可交易工具：上市付款方／醫院（不選）。3. 半衰期：商業定價 1 年；R49 同儕窗 12 個月。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L9［I］格加「#4 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0092；`export/LEADS_算力收支.md` 追加 1 列。不改 L9-I#1–#3、L9-A#1–#4、L9-P、C-A1、C-I5 結論。
