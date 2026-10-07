# L2-A#2 生成卡｜資料中心實體：會計恆等（利息資本化率與在建轉營運之費用翻轉）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/INDEX.json；archive/drive/USED_20260913_L2-A_test2_cost-index_GK.md；archive/drive/USED_20260917_L2-I_generate_GK.md；work/20261007_L2-P#2_test1_CL.md | EMITS: work/20261007_L2-A#2_generate_CL.md -->
**日期：** 2026-10-07　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain）　**格：** L2-A　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格依據（SCOUT.md §C-2）：ARCH_matrix 已無【未生成】／已生成未測格（L2-P#2 本日測一不通過）。非「已殺／刻意排除」格中最後測試最舊者＝L2-A（測二 `archive/drive/USED_20260913_L2-A_test2_cost-index_GK.md`，2026-09-13）；次舊 L2-I 測一 2026-09-17。L2-A 既有生成數計 1（每 MW 建置成本 × 冷卻佔比非線性；HUB 時期，無獨立 repo 檔）→ 本卡 #2。
- 比對過之舊檔與死因型態，本卡須異型：
  - L2-A#1（每 MW 建置成本＝(土建＋機電＋冷卻)／MW；測二部分通過、失敗在量綱）——本卡不是建置成本，是**利息成本在損益與資產負債表之間的分配**。
  - L2-P#2（`work/20261007_L2-P#2_test1_CL.md`；死於申報層無介質分列）——本卡載體為 GAAP 必揭科目（ASC 835-20 資本化利息），不依賴自願分列。
  - L2-I（許可／併網）、C-P4（水；ARCH_dead #19）、L2-P#1（PUE）——不涉。
  - C-A3／C-A4（ARCH_dead #4–5；GPU 折舊年限／續約單價）——本卡不涉折舊年限假設，涉利息資本化之起訖。
  - L6-A（已簽未交付 MW vs 已交付；測一部分通過）——本卡不以 backlog 為對照；重疊點＝交付時點。若只能寫成 L6-A → 否決 (4)。
  - L13-A（入表租賃 ≠ 義務上界）——同屬融資面，但本卡是已入表債務之利息去向，不是表外義務。
  - Hindenburg 對 EQIX 之 AFFO／維護性 capex 分類指控（2024-03）——同屬「會計品質」型，但對象是 capex 分類，不是利息資本化；其結局列為反方 R1。
- §7-10 領域最近公開更新：EQIX 10-Q（Q1 2026，申報 2026-04-29；Q2 2026 10-Q 已申報，見 `work/20261007_L2-P#2_test1_CL.md` A2）；DLR 10-K FY2025（申報 2026-02-13）；DLR Q2 2026 supplemental（2026-07-23；~1.4 GW 在建）。

## 1. 落差一句

會計恆等：`利息發生額 ＝ 費用化利息 ＋ 資本化利息`，資本化利息 ≈ 加權借款利率 × 合格在建資產餘額，於資產可供使用時停止並轉為折舊之一部分。資料中心開發商在建規模擴張時，資本化比率上升，使當期 FFO／AFFO 之利息負擔低於現金利息發生額；在建轉營運之季，費用化利息與折舊同時上升。種子主張：市場以每股 AFFO 成長率定價，若外推未分離「資本化率上升」之暫時貢獻，則交付集中期之 AFFO 路徑被誤讀。**方向未定**：起租現金流可能同季完全抵銷（無落差），或交付延遲使資本化期延長（落差加深）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：利息成本於資本化／費用化之分配，加總恆等於發生額 |
| 量綱 | 資本化比率＝資本化利息 ÷（資本化＋費用化利息），無因次；在建餘額（US$）；停止資本化時點（季） |
| 已讀數值（XBRL `InterestCostsCapitalized`，10-K 原值） | EQIX：2023 US$26.0M、2024 US$36.0M、2025 US$79.0M；Q1 2026 US$32M。費用化 `InterestExpenseNonoperating`：2024 US$457M、2025 US$527M、Q1 2026 US$148M → 資本化比率約 7%（2024）、13%（2025）、18%（Q1 2026）`[A]` 分析者算術。DLR：2023 US$116.8M、2024 US$118.9M、2025 US$127.2M（費用化值本輪未取得：DLR 該 XBRL 標籤 404） |
| 兩側 | 損益側＝費用化利息（入 FFO）；資產側＝在建餘額（含資本化利息）→ 日後折舊（FFO 加回，AFFO 不加回維護外者） |
| 半衰期 | 由交付排程決定；DLR backlog 起租分 2026／2027／2028+（supplemental 2026-07-23） |
| 重疊 | L6-A（交付時點）、L13-A（融資面）、Hindenburg 型會計品質指控。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；本輪未判可分離）

1. EQIX XBRL `InterestCostsCapitalized`：https://data.sec.gov/api/xbrl/companyconcept/CIK0001101239/us-gaap/InterestCostsCapitalized.json ；`InterestExpenseNonoperating`：https://data.sec.gov/api/xbrl/companyconcept/CIK0001101239/us-gaap/InterestExpenseNonoperating.json （10-K acc 0001101239-26-000032；10-Q acc 0001101239-26-000091）
2. DLR XBRL `InterestCostsCapitalized`：https://data.sec.gov/api/xbrl/companyconcept/CIK0001297996/us-gaap/InterestCostsCapitalized.json （10-K FY2025 acc 0001104659-26-015365）；10-K 原文 https://www.sec.gov/Archives/edgar/data/1297996/000110465926015365/dlr-20251231x10k.htm （本輪 fetch 截於 Item 1A，附註未讀）
3. DLR supplemental（在建 GW、backlog 起租年）：https://www.sec.gov/Archives/edgar/data/0001297996/000110465926086270/dlr-20260723xex99d2.htm
4. EQIX／DLR 之 AFFO 定義與調節表（是否扣資本化利息）——本輪未讀，留給 ANALYST。

缺段（§7-2）：DLR 費用化利息、兩家 AFFO 調節是否處理資本化利息、在建餘額季序列。失敗歸因＝本輪只讀 XBRL 單一標籤；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 會計品質型指控已被公開檢驗：EQIX 審計委員會（外部顧問）結論財報準確、無須重編 | DCD 2024-05-10 https://datacenterdynamics.com/en/news/equinix-audit-says-financial-reporting-accurate-despite-hindenburg-claims | 本型已有公開先例、市場已見過；落差需超出「合規」層，指向定價誤讀 |
| R2 | 利息資本化為 ASC 835-20 標準處理，金額每年必揭於 10-K；賣方模型普遍逐項建模 | ASC 835-20；載體 1–2 本身即公開 | 若已公開且已建模，非落差（同 L2-P#2 生成卡 R5 型） |
| R3 | 交付與起租同季：停止資本化之季即起租，現金流抵銷 | DLR backlog 起租表（載體 3） | 翻轉被抵銷，AFFO 路徑無斷點 |
| R4 | 量級小：EQIX 2025 資本化利息相對營收與 AFFO 為個位數百分比 `[A]` | 載體 1 | 即便誤讀，對 `H1` ≥ 5 無槓桿——終端條件，本輪不篩（§7-3），僅列 |

## 5. SCOUT 裁決

**生成 L2-A#2 並留。** 不進 T。下一動作＝ANALYST 測一。

否決觸發（寫給 ANALYST，逐條實讀）：
1. 實讀 EQIX、DLR 最近 10-K／10-Q 附註與 AFFO 調節表後，資本化利息、費用化利息、在建餘額三者**無法**於同一申報期並列（缺一即不可重算資本化比率）→ 不可觀測。
2. AFFO 調節已將資本化利息扣回（或公司另以「含資本化利息之 AFFO」揭露），使每股 AFFO 不受資本化率影響 → 無誤讀管道。
3. 交付季之費用化利息增量被同季起租現金完全抵銷（以 backlog 起租表與歷史交付季核對）→ 無翻轉痕跡（R3）。
4. 可運作對照只能寫成已簽未交付 MW（L6-A）、表外租賃（L13-A）、折舊年限（C-A3／C-A4）、建置成本（L2-A#1）或 capex 分類（Hindenburg 型）→ 換格或重開已死，否決。
5. 具名賣方或評級機構已公開以資本化比率調整 AFFO（即 R2 為真且已定價）→ 非落差。

複查觸發器（若日後殺）：任一美股上市資料中心主體之資本化比率單年變動 ≥ 2 倍且 AFFO 指引未說明；或 AFFO 定義變更涉及資本化利息。

## 6. 轉入個股層時必問（§7-4；本輪不答）
1. 財報科目：資本化利息（附註）、費用化利息（損益表）、在建餘額（資產負債表）、AFFO 調節。
2. 可交易工具：哪一上市主體之資本化比率變動最大。
3. 半衰期：交付排程 vs ≥ 12 個月窗。
