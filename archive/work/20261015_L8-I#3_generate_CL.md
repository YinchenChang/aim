# L8-I#3 生成卡｜標註／驗證：誘因（勞動分類套利——供應商以承攬人／平台接案者取代受僱者之或有負債）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260918_L8-I_generate_GK.md；archive/drive/USED_20260918_L8-I_test1_GK.md；archive/work/20261007_L8-I#2_generate_CL.md；work/20261007_L8-I#2_test1_CL.md | EMITS: work/20261015_L8-I#3_generate_CL.md -->
**日期：** 2026-10-15　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain，配額 3／6）　**格：** L8-I　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L8-A#3 本日測一）。非「已殺／刻意排除」格中最後測一最舊者＝2026-10-07 批之 L8-I#2、L9-A#2；依 QUEUE 序次（Q-0005 先於 Q-0006）取 **L8-I**；既有生成 2 份 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `annotator contractor misclassification`，命中 0 筆。
- 比對（本卡須異型）：
  - **L8-I#1**（`archive/drive/USED_20260918_L8-I_generate_GK.md`；測一 `archive/drive/USED_20260918_L8-I_test1_GK.md`）：品質不可契約（誰驗證驗證者）；死於爭議／重工率申報層不存在。本卡不涉品質。
  - **L8-I#2**（`work/20261007_L8-I#2_test1_CL.md`）：買方持股競爭供應商 → 量轉移；死於不分服務線、反向證據。本卡不涉買方、不涉量。
  - **C-I2**（ARCH_dead #12）：專家勞動逆選擇、單價由相鄰機制驅動。本卡主張不在單價，而在**供應商對勞動之法律分類選擇**所遞延之成本（工資工時、社保、追溯稅）。
  - L8-P（分鐘／條）、L8-A#1–#3（條數分母、未開票、客戶預付轉付）：不涉。
- §7-10 領域最近公開：Bloomberg Law 2026-09-29（AI 訓練員分類訴訟 ≥ 5 件加州、1 件德州）；McKinney v. Scale AI 和解最終核准聽證 2026-10-30；TaskUs 10-Q 2Q26、INOD 10-Q 2Q26（2026-08）。下一檢查點＝2026-10-30 聽證、兩家 3Q26 10-Q（約 2026-11）。

## 1. 落差一句

標註／RLHF 供應商有誘因以承攬人或平台接案者（而非受僱者）提供人力，以壓低直接營運成本並保有量的彈性；分類風險之成本（追溯工資、加班、社保、罰則）在 ASC 450「很有可能且可估計」前不入帳，故毛利中含有一筆未計提之或有勞動負債。加州 ABC 測試推定受僱；私有主體已有實例（McKinney v. Scale AI，CGC-24-620481，和解基金 US$12.5M，類別期 2020-12-10 至 2026-02-28；Surge AI、Mercor、Handshake AI 另案待決）。種子主張：上市供應商之毛利擴張若部分來自平台化／承攬化人力，則讀者把毛利讀成經營槓桿時，讀到的部分是遞延勞動成本。**方向未定**：上市主體之承攬比重可能很小（TaskUs 自稱「a small number of individuals」），則落差不存在。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：供應商之勞動分類選擇 → 成本遞延至訴訟／監理時點；買方（實驗室）不承擔 |
| 已讀事實 | TaskUs 10-K FY25：「There may be adverse tax and employment law consequences if the independent contractor status of some of our personnel … is successfully challenged. In several countries, a small number of individuals provide services to us as independent contractors. In addition, we have now seen over 1,100,000 account registrations on TaskVerse … Freelancers who perform projects on the TaskVerse are not employees of TaskUs.」「we could incur significant costs, including for prior periods」。TaskUs 10-Q 2Q26：「TaskVerse」0 筆；法律程序為概括句（不重大）。INOD 10-K FY25：「independent contractor」「freelance」「misclassif」皆 0 筆；INOD 10-Q 2Q26 MD&A：直接營運成本增量含「third-party delivery resources」（未量化）。Bloomberg Law 2026-09-29：被告含 Mercor、Handshake AI、Meta 所購之 Assured Robot Intelligence；原告以「algorithmic monitoring」作為控制之證據。 |
| 未證之連結 | 上市主體之承攬／第三方人力占直接成本之比重；是否已有針對上市主體之同型訴訟或計提 |
| 量綱 | 承攬／第三方人力成本 ÷ 直接營運成本（無因次）；類比和解額 ÷ 涉案期間該人力成本（無因次）；計提額 ÷ 毛利（%） |
| 選擇變數 | 供應商：受僱或承攬、交付地（加州／海外）；監理：ABC 測試適用範圍；買方：是否於合約要求分類合規 |
| 半衰期 | 訴訟 2–5 年；計提於「很有可能」時一次認列 |

## 3. B 端可觀測載體（只指名）

1. TaskUs 10-K FY25 https://www.sec.gov/Archives/edgar/data/1829864/000182986426000012/task-20251231.htm （承攬人／TaskVerse 風險段）
2. TaskUs 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/0001829864/000182986426000149/task-20260630.htm （Note 9 承諾與或有）
3. INOD 10-K FY25 https://www.sec.gov/Archives/edgar/data/903651/000110465926020655/inod-20251231x10k.htm ；INOD 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/903651/000110465926092021/inod-20260630x10q.htm （「third-party delivery resources」）
4. Bloomberg Law 2026-09-29 https://news.bloomberglaw.com/daily-labor-report/ai-data-trainers-suits-open-new-misclassification-fight-frontier
5. McKinney v. Scale AI 和解頁 https://www.claimdepot.com/settlements/mckinney-scaleai-settlement ；原告律所 2024-12-06 https://clarksonlawfirm.com/scale-ai-misclassifies-workers/
6. Surge AI 訴訟（Bloomberg Law）https://news.bloomberglaw.com/financial-accounting/ai-training-firm-surge-ai-hit-with-worker-misclassification-suit （本輪未讀）

缺段（§7-2）：上市主體承攬比重、INOD 第三方交付之法律型態、Appen（ASX，非可交易範圍）之對照；本輪只讀上列；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 上市主體以受僱者為主（TaskUs 菲律賓受僱、承攬「small number」）；承攬化集中於私有平台（Scale、Surge、Mercor） | 載體 1、4 | 表達層：無上市曝險 |
| R2 | 唯一已知和解 US$12.5M 對一家估值數百億之主體為小額，且無前瞻性改分類條款 | 載體 5 | 量級小 |
| R3 | 若和解成為行業定價，成本轉嫁於買方單價，供應商毛利不變 | — | 機制被轉嫁抵銷 |
| R4 | 私有平台之分類成本上升反使受僱型上市供應商相對受益（方向反轉） | 推論，待具名 | 方向未定 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 上市標註供應商（TaskUs、INOD 等）之申報與財報稿無法量化或代理承攬／第三方人力占直接成本之比重，亦無同型訴訟或計提；或
(2) 可運作對照只能寫成 C-I2（專家單價）、L8-I#1（品質）或 L8-I#2（量轉移）而無勞動分類特有之遞延成本結構；或
(3) `[D]` 量級：可得之最佳類比（和解額 ÷ 類別期該主體人力成本或營收）< 1%，且無前瞻性改分類條款；或
(4) 12 個月內無可觀測驅動：無上市主體成為被告、無監理行動（如美國勞工部規則、加州執法）點名 AI 訓練員；或
(5) 具名賣方或公司已把分類風險量化入毛利預測（已定價）。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：直接營運成本中之承攬／第三方人力、或有負債附註、法律程序。2. 可交易工具：標註／AI 資料服務商（不選）。3. 半衰期：訴訟至計提。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L8［I］格加「#3 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0048。不改 L8-I#1／#2、L8-A#1–#3、L8-P、C-I2 結論。
