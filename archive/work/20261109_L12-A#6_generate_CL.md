# L12-A#6 生成卡｜監理與法制：會計恆等（公司最低稅 CAMT：現金稅 ≥ 15% × AFSI − 抵減；AI 實驗室持股之未實現公允價值利得入 AFSI，而一般應稅所得被 100% 紅利折舊與研發費用化壓低 → 帳面利得轉為現金稅之法定路徑）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260922_L12-A_generate_GK.md；archive/work/20261008_L12-A#2_generate_CL.md；archive/work/20261016_L12-A#3_generate_CL.md；archive/work/20261025_L12-A#4_generate_CL.md；archive/work/20261101_L12-A#5_generate_CL.md；work/20261101_L12-A#5_test1_CL.md；archive/work/20261109_L5-A#6_generate_CL.md（ARCH_live 摘要） | EMITS: work/20261109_L12-A#6_generate_CL.md -->
**日期：** 2026-11-09　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 6／6）　**格：** L12-A　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。非「已殺／刻意排除」格中最後測一最舊＝**2026-11-01（L12-A#5、L12-I#5）**；依表序取 **L12-A**；既有生成 5 份 → #6。L12-I 留下一輪。前一輪 SCOUT（鎖 2026-11-09 08:21 UTC）未留產出即逾時，本輪鎖已逾 90 分之殘鎖重取。
- Tokenomics 線索（CLAUDE.md §11）：已查 `minimum tax`、`Anthropic`，命中 14 筆皆為 Anthropic 定價／token 類 SRC，相關 0 筆；未使用。內部研究數字（§12）未取用。
- 比對（本卡須異型）：
  - **L12-A#1**（TIC 法定／自願營收權重）：不用營收拆分。
  - **L12-A#2**（著作權或有負債 N×s vs ASC 450）：本卡非或有負債，為法定稅基恆等。
  - **L12-A#3**（OBBBA 研發費用化／紅利折舊之**所得稅時序**，ASC 740 遞延；死於量級 < OCF 5%）：#3 問「扣除提前→現金稅一次性下降」；本卡問**最低稅底板**——同一組扣除使一般稅下降時，帳面非現金利得經 AFSI 抬高 15% 底板，現金稅由底板決定。驅動變數為**未實現投資利得**，非折舊／研發時點。CAMT 抵減結轉之「可回收性」使本卡部分具時序性，重疊判讀見否決 (5)。
  - **L12-A#4**（地方動產稅）、**L12-A#5**（REIT 身分門檻）：非從價稅、非稅務身分。
  - **L5-A#6**（Micron 新加坡 QDMTT／Pillar Two 補充稅）：外國補充稅、稅基為低稅率獎勵所得；本卡為美國 §55／§56A 國內最低稅、稅基為帳面所得含公允價值利得。
  - **L12-I#3／L3-I#6／L3-A#2**（§48D）：無關。ARCH_dead：無稅基型死因；C-P4（非損益科目）型表達層風險見否決 (6)。
- **§7-10 領域最近公開：** CAMT 暫行指引 Notice 2025-27、2025-46（2025-09-30）、2025-49（2025-10，「options for taxpayers to disregard certain unrealized gains and losses for items measured at fair value」，Thomson Reuters 2026-02-20 轉述，**未讀原文：是否涵蓋非加密資產之 ASC 321 權益證券未定**）；Notice 2026-7（2026-02-18，修正 2025-49，2026-02-18 後開始之課稅年度適用修正版）。AMZN 10-Q 3Q26（2026-10-30）、GOOGL 10-Q 3Q26（2026-10-29）。

## 1. 落差一句

CAMT 為法定恆等：**`Tax_US = max(T_regular, 15% × AFSI − CAMT_FTC) `**，超出部分形成 CAMT 抵減結轉，僅於日後 `T_regular > 15% × AFSI` 時可回收；AFSI 以帳面稅前所得為起點，§168 財產以稅務折舊取代帳面折舊，但**未實現投資利得原則上留在 AFSI**（除非暫行指引之選擇性調整涵蓋）。2026 年 Amazon 與 Alphabet 之稅前所得有相當部分來自對 Anthropic 等私人 AI 公司持股之公允價值上調（非現金），同時 OBBBA 之 100% 紅利折舊與國內研發即時費用化壓低一般應稅所得。**落差＝若上述利得入 AFSI 且底板綁定，帳面 AI 持股利得將以 15% 轉為窗內現金稅（並以遞延 CAMT 抵減資產掛帳），而兩家 10-K FY25 未提 CAMT、3Q26 10-Q 稅附註只談 Pillar Two；市場以「非現金、非營運」剔除該利得時，可能同時剔除了其現金稅後果。** 方向（是否綁定、是否已選擇排除）未定。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（法定最低稅）：`CashTax_US = max(T_reg, 0.15·AFSI − FTC_CAMT)`；`AFSI = PTI_book − D_book + D_tax(§168) ± 指引選擇性調整（含未實現公允價值利得）`；`ΔCAMT credit = max(0, 0.15·AFSI − FTC − T_reg)` |
| 量綱 | 所得［美元／年］；稅率 15%、21%［無因次］。輸出：`[D]`（CAMT − T_reg）÷ OCF［%］；未實現利得 ÷ 稅前所得［%］ |
| 可見端 | AMZN 10-Q 3Q26：Anthropic 優先股「observable changes in prices」上調 9M26 **62.9B**、可供出售債券（Anthropic 可轉債轉換部分）利得 9M26 **4.5B**；稅前所得 9M26 **147,560M**；所得稅費用 33,939M；遞延所得稅（現金流量表）35,522M；「Cash paid for income taxes, net of refunds」9M26 **5,293M**（9M25 6,774M）。AMZN 10-K FY25：「U.S. taxable income is reduced by accelerated depreciation deductions … reduced by tax credits」，OBBBA 恢復 100% 紅利折舊、國內研發即時費用化。GOOGL 10-Q 3Q26：「Loss (gain) on debt and equity securities, net」9M26 **(126,755)M**；稅前所得 248,520M、所得稅 47,281M、遞延所得稅 33,077M；非流通證券 135,230M（2025-12-31：68,687M）；稅附註只談 Pillar Two「Side-by-Side Safe Harbor」。兩家 10-K FY25 檢索「alternative minimum」0 命中 |
| 指名不可見端 | 各家 AFSI 估算與 CAMT 是否綁定；是否已選擇 Notice 2025-49／2026-7 之未實現利得排除；應付 CAMT 之估計稅款時點；CAMT 抵減結轉餘額 |
| 主張 | 恆等由法條＋公開申報（稅前所得、利得、遞延稅、現金稅、稅務折舊之遞延稅負債變動）可部分重算；指引是否排除 ASC 321 權益證券利得為二元開關 |
| 表達工具型態（只指名，不選券） | 持有大額私人 AI 公司股權並以公允價值（或衡量替代法可觀察價格）認列利得之美股大型科技公司普通股及上市選擇權。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| AMZN 10-Q 3Q26（Anthropic 利得、稅前、遞延稅、現金稅） | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm |
| AMZN 10-K FY25（稅附註、OBBBA 句） | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm |
| GOOGL 10-Q 3Q26（證券利得、稅附註） | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm |
| GOOGL 10-K FY25 | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm |
| CAMT 指引轉述（Notice 2025-49 未實現利得選擇性調整；Notice 2026-7） | https://tax.thomsonreuters.com/news/additional-interim-camt-guidance-tweaks-afsi-calculations/ |
| Notice 2025-46 摘要（KPMG） | https://kpmg.com/us/en/taxnewsflash/news/2025/09/notice-2025-46-interim-guidance-camt-domestic-corps-troubled-companies-tax-consolidated-groups.html |
| 未實現利得排除限於加密資產之報導（Vedder；本輪 302 後讀取逾時，未讀） | https://www.vedderprice.com/irs-provides-interim-guidance-with-respect-to-portions-of-proposed-camt-regulations-to-be-withdrawn-interim-guidance-provides-that-unrealized-cyptocurrency-gains-not-subject-to-camt |
| IRB 2025-44（Notice 2025-49 原文所在） | https://www.irs.gov/irb/2025-44_IRB |
| 市場敘事：利得占淨利比（Fortune 2026-04-30；AMZN 1Q26 Anthropic 稅前利得 16.8B；文內無稅務討論） | https://fortune.com/2026/04/30/google-amazon-ai-profits-anthropic-stake-bubble-earnings-2026/ |
| 對照：NVDA、MSFT（OpenAI 權益法）、CRM 等之非流通股權利得與稅附註 | 測一以 `sec.py` 取得 |

不宣稱缺口已存在、不宣稱市場未計入、不宣稱淨方向。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | Notice 2025-49（經 2026-7 修正）已給予「disregard certain unrealized gains and losses for items measured at fair value」之選擇，若涵蓋 ASC 321 權益證券，利得不入 AFSI | Thomson Reuters 2026-02-20 轉述；原文待讀 | 機制開關歸零 |
| R2 | 稅務折舊替代帳面折舊之 AFSI 調整，使 AFSI 本已被紅利折舊壓低；兩家實際有效稅率 18–24%，一般稅可能已高於 15% 底板 | AMZN／GOOGL 10-Q 稅附註 | 不綁定 |
| R3 | CAMT 超額形成抵減結轉，可於日後回收 → 只是時序，現值損失小；即 L12-A#3 型 | §53(e) | 量級／重疊 |
| R4 | 兩家未揭露 CAMT 即代表管理層判斷不重大（10-K 重大性） | 10-K FY25 0 命中 | 已知且不重大 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) Notice 2025-49／2026-7 原文（IRB）明文允許於 AFSI 排除**非數位資產**之權益證券未實現公允價值利得（含 ASC 321 衡量替代法之可觀察價格調整），或已發布之最終規則同效（R1）。
- (2) `[D]` 以申報可得值估 AFSI（稅前所得 − 帳面折舊 + 稅務折舊之近似，以遞延稅負債中折舊項變動推得）後，AMZN 與 GOOGL 於 2026 課稅年度 `0.15·AFSI ≤ T_reg + 一般稅抵減`，即底板兩家皆不綁定（R2）。
- (3) `[D]` 量級：（0.15·AFSI − T_reg）÷ 最近 4 季 OCF < **3%**（兩家皆然），或應繳時點全落在 12 個月重定價窗外。
- (4) 任一家已於申報、法說官方逐字稿或稅務附註揭露 CAMT 負擔／抵減結轉，或 ≥ 1 家具名賣方已以 CAMT 口徑建模其現金稅（R4 反面：已公開）。
- (5) 本卡經重疊判讀只能以 L12-A#3（扣除時序、遞延稅）或 L5-A#6（最低稅補充稅）重述：CAMT 抵減結轉可於 ≤ 3 年內回收之 `[D]` 估計成立，致現金效果純為時序（R3）。
- (6) 除 AMZN、GOOGL 外無第三家上市主體適用，且兩家價格於窗內主要由 AI 持股估值本身與資本支出敘事解釋（不可分離），或稅後果只落非損益科目（C-P4 型）。
- (7) 12 個月內無檢驗事件（10-K FY26 稅附註約 2027-02、1Q27 10-Q、IRS CAMT 最終規則或新 Notice）可解析綁定與否。

## 6. 不寫

不寫 H1／H5；不選券；不主張價值方向；不寫 T。
