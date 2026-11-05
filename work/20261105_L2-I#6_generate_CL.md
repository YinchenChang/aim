# L2-I#6 生成卡｜資料中心實體：誘因（開發方之非約束承租意向書公告 × 同窗股本發行——承租方零成本之排他選擇權，價差由新股認購人承擔）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md（L2-I#5、L2-P#4、L2-A#6、L13-I#3、L4-I#4 列）；archive/drive/USED_20260917_L2-I_generate_GK.md；archive/work/20261007_L2-I#2_generate_CL.md；archive/work/20261015_L2-I#3_generate_CL.md；archive/work/20261023_L2-I#4_generate_CL.md；archive/work/20261029_L2-I#5_generate_CL.md；work/20261105_L2-A#6_generate_CL.md | EMITS: work/20261105_L2-I#6_generate_CL.md -->
**日期：** 2026-11-05　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 5→6／6）　**格：** L2-I　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L2-A#6 本日測一，Q-0169 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-29：L2-I（#5，Q-0129）——同日之 L2-A 已於本日生成 #6。既有 #1–#5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `LOI "letter of intent" ATM hyperscaler`，命中 0 筆。內部研究數字未用。
- 比對（須異型）：
  - **L2-I#1**（許可／併網可撤回 × 損失歸屬錯配）：法定取用權；本卡為私人非約束意向書，無撤回主體。
  - **L2-I#2**（開發 JV 之 GP 兼買方 promote）：關係人定價；本卡無關係人交易，損失方為**公開市場新股認購人**。
  - **L2-I#3**（設備訂單保位、可取消 backlog）：**買方**對供應商之取消權、已計入供應商 backlog；本卡之選擇權持有人為承租方，但驅動層是**開發方之揭露與融資時點選擇**——意向書未計入任何合約科目，只進新聞稿、IPO 招股書與「pipeline／contract potential MW」頭條。
  - **L2-I#4**（表後發電期末續約權）、**L2-I#5**（MEP 合約型態）：不涉。
  - **L2-P#4**（MW 口徑 gross vs critical IT）：分母定義；本卡為**簽約狀態**（非約束 vs 定約）之混同，不涉 MW 口徑。
  - **L2-A#6**（第三方信用支撐對價攤銷）：已定約之成本認列；本卡在定約之前。
  - **L13-I#3**（評等線附近依債務含量排序工具）：投資級發行人之工具排序；本卡為無營收開發方之**股本發行時點 × 非約束公告**，評等不涉。
  - **L4-I#4**（世代切換延後選擇權）：不涉。ARCH_dead C-A3／C-A4／C-P4：不涉。
- §7-10 領域最近公開：FRMI 10-Q 2Q26（2026-08-14）、8-K 2026-11-04；APLD 10-Q 1Q FY27（2026-10-07）；RIOT 8-K 3Q26（2026-11-04）。下一檢查點＝FRMI 10-Q 3Q26（預期 2026-11 中旬）；Lupia v. Fermi 動議裁定。

## 1. 落差一句

無營收之 AI 資料中心開發方，於股本發行窗內公告與「不具名投資級承租方」之**非約束**意向書（LOI）／排他期；承租方取得零成本之排他選擇權（不付訂金或所附墊款可隨時終止），開發方取得以「投資級承租」敘事定價之股本。恆等式（誘因）：發行窗內新股認購之定價隱含 \(\pi\)（LOI→同一對手方定約之機率）× 投資級信用溢價；實際 \(\pi\) 由承租方決定且無對價。可拒絕之主張＝≥ 2 家開發方之「公告 LOI→12 個月內同一對手方定約」轉換率 < 50%，且其股本發行（IPO／ATM／SEPA／增發）落於 LOI 公告至排他期屆滿之窗內，且市場端（具名賣方或股價事件）把 LOI 容量計入估值而未按 \(\pi\) 折算。`[D]`（初讀，待測一）：APLD 2024 年 400 MW LOI 0／1 轉換（同園區 2025 年改租 CoreWeave，非投資級超大規模商）；FRMI 2025-09 LOI 0／1 轉換（首份定約 2026-08-09 為 TensorWave）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因（I）**：(i) 開發方選擇公告與否、措辭（「investment grade」「exclusivity」「advanced discussions」）及時點；(ii) 承租方持有排他期內之免費選擇權；(iii) 股本發行窗與 LOI 窗重疊；(iv) 排他期屆滿／墊款終止以 8-K 揭露，常落於發行完成後 |
| 選擇者 | 開發方（公告、發行時點、pipeline 口徑）；承租方（是否定約、是否撥付墊款） |
| 可見端 | 8-K Item 8.01（LOI、排他延長、屆滿、AICA 終止）；10-K／10-Q 股本附註（ATM 銷售量與所得、IPO 所得）；招股書與證券集體訴訟起訴狀；投資人簡報之「Contract Potential」「pipeline MW」 |
| 指名不可見端 | 承租方身分；LOI 條款（價格、MW、終止權）；股本銷售之逐日分布 |
| 量綱 | 無因次（轉換率 \(\pi\)；窗內發行所得 ÷ 同期總股本發行）；月（排他期） |
| 外部參照物（測一查證） | Lupia v. Fermi Inc.（S.D.N.Y. 1:26-cv-00050）起訴主張即本機制（「tenant demand and funding arrangements … risk of termination of a prospective tenant's funding commitment」）；反例：RIOT 3Q26 定約即公告且自述不預期增發 |
| 表達工具型態（只指名，不選券） | 美股、無營收或轉型中之 AI 資料中心開發方普通股；不選券 |
| 重疊 | L2-I#3（選擇權家族，持有人與驅動層不同）；L13-I#3（發行時點，主體與觸發不同） |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論；SEC 皆經 `tools/sec.py` 全文實讀）

1. **Applied Digital 8-K ex99.1**（2024-04-11）https://www.sec.gov/Archives/edgar/data/1144879/000114487924000077/apld3q24earningsrelease.htm ：「Entered into exclusivity and executed a letter of intent (the "LOI") with a US-based hyperscaler for a 400 MW capacity lease」；「In advanced discussions for project-level financing for this investment-grade tenant」；同稿「The exclusive negotiation period with the initial HPC anchor tenant identified for our Ellendale campus expired at the end of March」（前一排他亦未轉換）。
2. **Applied Digital 8-K**（2024-07-26）https://www.sec.gov/Archives/edgar/data/1144879/000114487924000194/apld-20240726.htm ：「entered into an agreement extending the exclusivity period … no assurance can be given that the parties will actually consummate the lease documentation」。
3. **Applied Digital 10-K FY24**（2024-08-30）https://www.sec.gov/Archives/edgar/data/1144879/000114487924000216/apld-20240531.htm ：「We have primarily financed our strategic growth through our at-the-market ("ATM") offerings」；2024-07-09 新 ATM（上限 125.0 百萬美元）。**10-Q 1Q FY25**（2024-10-09）https://www.sec.gov/Archives/edgar/data/1144879/000114487924000253/apld-20240831.htm ：「We continue the negotiations (although exclusivity has recently expired) with a US-based hyperscaler」；窗內 ATM 所得 14.6＋16.4 百萬美元（兩方案）。**10-Q 2Q FY25** https://www.sec.gov/Archives/edgar/data/1144879/000114487925000006/apld-20241130.htm ：2024-08-28 SEPA（YA Fund）、2024-10-30 終止 ATM。後續：Ellendale（Polaris Forge 1）2025-06 租予 CoreWeave（公司稿 https://ir.applieddigital.com/news-events/press-releases/detail/123/ ，測一回原文）。
4. **Fermi 8-K**（2025-12-12）https://www.sec.gov/Archives/edgar/data/2071778/000121390025120940/ea0269377-8k_fermi.htm ：「non-binding letter of intent, dated September 19, 2025, with an investment grade-rated tenant」；AICA「advance up to $150 million … No funds have been drawn」；「exclusivity period … expired at midnight on December 9, 2025」；「On December 11, 2025, the First Tenant notified the Company that it is terminating the AICA」。
5. **Fermi 10-K FY25**（2026-03-30）https://www.sec.gov/Archives/edgar/data/2071778/000207177826000010/frmi-20251231.htm ：IPO 2025-10-02、每股 21.00、總所得淨額 745.6 百萬美元（LOI 後 13 天）；「we have entered into a single letter of intent … and have largely only received expressions of interest」；Lupia v. Fermi 類別期間 2025-10-01 至 2025-12-11。**10-Q 2Q26** https://www.sec.gov/Archives/edgar/data/2071778/000207177826000051/frmi-20260630.htm ：首份定約＝TensorWave（2026-08-09，15 年、222 MW）；TTU 地租之開工通知以「a lease with a Phase 1 tenant for not less than 200 MW」為條件、期限 2026-12-31。
6. **Riot 8-K ex99.1／ex99.2**（2026-11-04）https://www.sec.gov/Archives/edgar/data/0001167419/000110465926122368/riot-ex99d1.htm ：Corsicana 910 IT MW、15 年 triple-net、約 28 bn 合約總額，「we do not currently anticipate issuing equity」（反例：定約後公告、無發行）；ex99.2 https://www.sec.gov/Archives/edgar/data/0001167419/000110465926122368/riot-ex99d2.htm 「1,301 IT MW Contract Potential」含「AMD Expansion Capacity 150 IT MW」（選擇權容量與已簽並列）。

缺段（§7-2）：未取 APLD／FRMI 股價事件窗；未取具名賣方原文（是否計入 LOI 容量）；IREN、WULF、CIFR、HUT、GLXY、BTDR、CLSK、HIVE、dmg 之 LOI 公告與轉換未查；FRMI 起訴狀原文未讀（僅 10-K 轉述）；APLD 400 MW LOI 之對手方是否後續以他案定約未知。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 市場已懲罰：FRMI 公告終止當日股價大跌、APLD 改租 CoreWeave 後仍重估——LOI 風險於事件日即定價，無持續錯價 | BNN Bloomberg 2025-12-12「Fermi tumbles 40% after potential customer backs out」https://www.bnnbloomberg.ca/business/2025/12/12/data-center-reit-fermi-tumbles-40-after-potential-customer-backs-out-of-funding-deal/ （二手，測一回原價） | 已定價（事件後） |
| R2 | 定約者多以公告為後（RIOT、CIFR、WULF 皆公告定約租約），LOI 公告為少數；樣本 < 3 即不可推廣 | §3-6；L2-A#6 卡 §3 | 樣本不足 |
| R3 | 窗內發行規模小（APLD 窗內 ATM 合計約 31 百萬美元）；IPO 所得依 S-1 已含風險因素，損失歸屬於訴訟而非錯價 | §3-3、§3-5 | 量級不足／法律救濟已存在 |
| R4 | LOI→他方定約仍屬需求成立（APLD 改租 CoreWeave），開發方容量終被吸收；落差只在承租方信用，非容量 | §3-3 | 機制轉為信用（L6-I／L13-I 型） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀 ≥ 4 家 AI 資料中心開發方（APLD、FRMI 必讀；IREN、WULF、CIFR、HUT、GLXY、BTDR、CLSK 擇取）8-K／10-Q／10-K／招股書，可同時取得「LOI 或排他期公告日＋其後定約或屆滿之揭露＋同窗股本發行量」三項者 < 2 家（不可觀測）；或
(2) `[D]` 可觀測樣本之 LOI→12 個月內同一對手方定約轉換率 \(\pi\) ≥ 50%（門檻凍結於此），或窗內股本發行所得 ÷ 該公司 LOI 公告前後各 12 個月股本發行所得合計 < 20%（門檻凍結於此）；或
(3) 市場端：LOI 公告日與屆滿／終止日之異常報酬對稱（公告漲幅 ≤ 屆滿跌幅之絕對值，R1 成立）；或具名賣方原文明示以 \(\pi\) 折算或排除 LOI 容量；或未能取得任何把 LOI 容量計入估值之具名原文（落差無市場端）；或
(4) 可運作之對照只能寫成設備訂單取消權（L2-I#3）、MW 口徑（L2-P#4）、承租方信用／融資可貸性（L6-I#3）或投資級發行人工具排序（L13-I#3）；或
(5) 12 個月內無檢驗事件（FRMI 開工通知期限 2026-12-31、Lupia v. Fermi 駁回動議裁定、任一開發方新 LOI 公告或屆滿 8-K、APLD／FRMI 次一股本發行）；或
(6) 機制不改變任何被定價之財報科目或可交易工具（§7-4）——例如 LOI 容量從未進入任何公司指引、pipeline 頭條或賣方模型。

複查觸發器（若日後殺）：SEC 意見函或執法行動就非約束租約公告與同期發行提問；Lupia v. Fermi 進入證據開示或和解；新一批（≥ 2 家）開發方於股本發行窗內公告非約束 LOI。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：股本附註（ATM／IPO 所得、股數）、承諾與或有事項（訴訟）、8-K Item 8.01 序列。2. 可交易工具：AI 資料中心開發方普通股（不選）。3. 半衰期：LOI 排他期 2–6 個月；屆滿／終止 8-K 即解析。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0170；`query/ARCH_matrix.md` L2［I］加「#6 已生成」；`AIM_FUNNEL.md` 日期行與 §3；`export/LEADS_算力收支.md` 追加 2 列（RIOT Corsicana 合約總額、每 IT MW 資本成本）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L2-I／#2–#5、L2-A／#2–#6、L2-P／#2–#6、L13-I#3、L6-I#3、C-A3；不寫 T。
