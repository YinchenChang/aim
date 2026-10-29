# L2-A#5 生成卡｜資料中心實體：會計恆等（出租方租金收入之直線化與預收租金攤轉：GAAP 租賃收入 ≡ 當期現金租金 ＋ Δ應計租金應收 ＋ 預收租金攤轉；遞增租約前段之收入／EBITDA 恆高於現金）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260913_L2-A_test2_cost-index_GK.md；archive/work/20261007_L2-A#2_generate_CL.md；archive/work/20261014_L2-A#3_generate_CL.md；archive/work/20261021_L2-A#4_generate_CL.md；work/20261007_L2-A#2_test1_CL.md；work/20261021_L2-A#4_test1_CL.md；work/20261018_L6-A#3_test1_CL.md | EMITS: work/20261029_L2-A#5_generate_CL.md -->
**日期：** 2026-10-29　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 5→6／6）　**格：** L2-A　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L2-P#5 本日測一，Q-0127 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-21 之 **L2-A**（#4；L2-P 已於本日 #5 更新）。既有 #1–#4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `straight-line rent lease escalator`，5 筆（SRC_DC_014 每 IT MW 資本支出；SRC_CAP_008–011 模型指數），無一涉租金認列或遞增條款；未用。
- 比對（須異型）：
  - **L2-A**（`archive/drive/USED_20260913_L2-A_test2_cost-index_GK.md`）：建置成本指數。不涉。
  - **L2-A#2**（`archive/work/20261007_L2-A#2_generate_CL.md`；測一通過｜量級不足）：利息資本化（費用側、在建期）。本卡為**營收側、營運期**。
  - **L2-A#3**（`archive/work/20261014_L2-A#3_generate_CL.md`）：電力轉嫁之總額／淨額認列（變動租金之分子歸屬）。本卡只論**固定租金**之時間分配，變動租金除外。
  - **L2-A#4**（`archive/work/20261021_L2-A#4_generate_CL.md`；測一 `work/20261021_L2-A#4_test1_CL.md` 否決 (3)：賣方以 EV／EBITDA 定價，折舊不入分子）：本卡之差額**正位於 EBITDA 之內**（直線化收入與預收攤轉皆入營收、不被 D&A 加回），故 #4 之死因反成本卡之市場端前提；此點由測一驗證，不由本卡斷言。
  - **L6-A#3**（`work/20261018_L6-A#3_test1_CL.md`）：CIP 轉折舊管線時點。不涉。
  - **ARCH_dead C-A3**（GPU 折舊年限）、**L13-A**（承租方 RVG）：資產／側別不同。承租方以認股權換取信用支撐（Google 對 WULF／Fluidstack）之攤銷屬本卡 R3 之鄰接項，不作樞紐。
- §7-10 領域最近公開：WULF 10-Q 2Q26（2026-08-05 申報）；GLXY 10-Q 2Q26（2026-08-10）；APLD 10-Q 1Q FY27（2026-10-07）。下一檢查點＝WULF／CIFR／GLXY 3Q26 10-Q（約 2026-11 上旬）。

## 1. 落差一句

出租方將含年遞增條款之固定租金依 ASC 842 直線認列，並將預收租金於租期內攤轉為收入：恆等式 \(Rev^{fix}_t \equiv Cash_t + \Delta AR^{SL}_t + \Delta DRL^{-}_t\)（應計租金應收之增加、預收／遞延租金負債之減少）。遞增率 g、租期 T 下，首年直線收入／現金租金 \(= \frac{(1+g)^T-1}{gT}\)（`[D]` g＝3%：T＝15 → 1.24；T＝20 → 1.34），第 k 年比值 \(\frac{(1+g)^T-1}{gT(1+g)^{k-1}}\)（T＝20、k＝5 → 1.19）。非 REIT 之 AI 出租方（前礦企）之 Adjusted EBITDA 不扣直線化與預收攤轉（REIT 之 AFFO 則扣），而賣方以 EV／EBITDA 或「平均年收益／MW」定價。可拒絕之主張＝≥ 2 家上市 AI 出租方之 \((Rev^{fix}-Cash)/Rev^{fix}\) 於其賣方定價年度 ≥ 10%（`[D]`），且其 Adjusted EBITDA 定義未扣除、具名賣方以該 EBITDA 或平均收益定價。若租約無遞增或遞增極低、Adjusted EBITDA 已扣直線化、或賣方以現金 NOI／AFFO 定價，本卡死。本卡不主張任何主體價值方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等（A）**：(i) \(Rev^{SL}=\frac{1}{T}\sum_{k=1}^{T}Cash_k\)；(ii) \(\sum_{k}(Rev^{SL}-Cash_k)=0\)（全期守恆，只移時點）；(iii) 預收 \(P\) 於收訖期入現金、於起租後每期 \(P/T\) 或依抵扣進度入收入；(iv) 前段超額 \(X_t \equiv Rev^{fix}_t - Cash_t>0\)，後段 \(X_t<0\) |
| 選擇者 | 出租方（Adjusted EBITDA 調整項之定義；租約之遞增率、預收結構）；賣方（倍數之分母口徑） |
| 可見端 | 10-Q 租賃附註「straight-line basis over the noncancellable term」「deferred rent liability or accrued rent receivable」；現金流量表「(Decrease) increase in deferred rent liability」；未來最低租賃收入到期表（逐年遞增率）；MD&A 之 Adjusted EBITDA 定義與調節表 |
| 指名不可見端 | 各租約遞增率原文（多未揭露，僅能由到期表反推）；賣方模型中收入是否直線化 |
| 量綱 | 無因次比值（\(X_t/Rev_t\)）；年（T、k）；遞增率 %／年 |
| 外部參照物（測一查證） | REIT 慣例：DLR AFFO 調節列「直線租金收／支」（`work/20261007_L2-A#2_test1_CL.md` A1 已讀）——同一經濟事項於 REIT 被扣除、於非 REIT 出租方是否被扣除即為落差之對照組 |
| 表達工具型態（只指名，不選券） | 美股、以長租 AI 設施為主之非 REIT 出租方普通股；不選券 |
| 重疊 | L2-A#3（同為營收側；變動 vs 固定租金）；L2-A#4（同一定價分母，方向相反） |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. TeraWulf 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1083301/000108330126000166/wulf-20260630.htm ：「recognizes the total combined fixed payments under the agreements on a straight-line basis over the noncancellable term. The Company recognizes the difference between straight-line revenue recognized during the period and the lease payments due … as deferred rent liability or accrued rent receivable」；「The Core42 HPC Leases provide for certain prepaid rent amounts (“Prepaid Rent”) representing the first 12 months base rent under each lease for a total of $ 90.0 million which shall be applied towards 50 % of each month’s base rent」；現金流量表「(Decrease) increase in deferred rent liability ( 30,843 ) 90,000」（六個月，千美元）；「Lease income relating to lease payments … 44,485」（六個月）。`[D]` 示意：同期遞延租金負債減少額約當固定租金收入之 69%（含直線化抵銷，僅上界示意）。Adjusted EBITDA 定義 (i)–(vi) 與調節表**無**直線化或預收攤轉調整列。另「Google Warrants … recorded an asset of $ 515.5 million … will amortize this asset over the life of the Fluidstack HPC Leases on a straight-line basis」（攤銷之報表科目待測一確認）。
2. Galaxy 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1859392/000185939226000091/glxy-20260630.htm ：「Lease income is recognized on a straight-line basis over the lease term」；「Deferred lease revenue … Beginning balance $ 150,000 … Prepaid rent … Ending Balance $ 150,000」；未來最低租賃收入「2027 259,079 2028 266,851 2029 274,857 Thereafter 3,820,130 Total … 4,747,792」（千美元；`[D]` 年增約 3.0%）。
3. Bernstein（The Block 2026-07-07）https://www.theblock.co/post/407429/bernstein-maintains-36-terawulf-target-after-19-billion-20-year-anthropic-lease ：「21 times one-year forward EV/EBITDA on its CY30 steady-state estimate」；Anthropic 20 年租約「average annual yield of $2.4 million per IT megawatt」——以**平均**（即直線化口徑）收益建模。
4. Applied Digital 10-Q 1Q FY27（sec.py）https://www.sec.gov/Archives/edgar/data/1144879/000114487926000059/apld-20260831.htm ：「Short term lease incentive 8,543」；「deferred revenue primarily related to advance billings for tenant fit-out services and the delivery of power」（直線化字樣 0 筆；測一須讀 10-K FY26 租賃政策段）。
5. Cipher（DCD 2026-03-25）https://datacenterdynamics.com/en/news/cipher-digital-secures-hyperscale-tenant-under-15-year-lease/ ：15 年 hyperscale 租約，未述遞增與預收；CIFR 10-Q 2Q26 直線化字樣只見債務成本與礦機（測一須讀租賃附註／8-K）。

缺段（§7-2）：未取任一份 Adjusted EBITDA 扣除直線化之 AI 出租方（反例搜尋未做）；未取具名賣方模型之收入口徑原文（Bernstein 僅見轉述）；CIFR、APLD、IREN 之遞增率未取；WULF 認股權攤銷之科目（營收抵減或費用）未確認。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | REIT 慣例（AFFO 扣直線租金）已為市場所熟知；賣方對前礦企亦以「contracted revenue／annualized NOI per MW」或 NAV 估值，直線化差額已被看穿 | DLR AFFO 調節（§2 外部參照物）；Bernstein 以 CY30 穩態（§3-3） | 已定價 |
| R2 | 量級：g＝3% 時穩態年（k≈5）之超額約 10–19%，且全期守恆；對終值倍數之影響為一次性 | 本卡 §1 `[D]` | 量級不足 |
| R3 | 預收租金為已收現金（WULF 2025 年已入帳），攤轉只是 IFRS／GAAP 對已實現現金之時間分配，信用風險為零；與認股權攤銷（降低收入）方向相反可部分抵銷 | WULF 10-Q（§3-1） | 不構成誤讀 |
| R4 | 遞增條款可能低於 3% 或為 CPI 連動上限，使 \(X_t\) 接近 0 | 待測一（各家到期表反推） | 恆等式不咬合 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀 ≥ 3 家非 REIT AI 出租方（WULF、GLXY、CIFR、APLD、IREN 擇取）10-Q／10-K，可由同檔取得「直線化政策＋到期表或遞增率＋Adjusted EBITDA 定義」三項者 < 2 家（不可觀測）；或
(2) `[D]` 樣本之 \((Rev^{fix}-Cash)/Rev^{fix}\) 於其賣方定價年度皆 < 10%（門檻凍結於此；含預收攤轉）；或
(3) 樣本之 Adjusted EBITDA 已扣直線化／預收攤轉，或具名賣方原文以現金租金、現金 NOI 或 AFFO 定價（R1 已定價）；或未能取得任何以 GAAP 收入口徑之 EBITDA 或平均收益定價之具名原文（落差無市場端）；或
(4) 可運作對照只能寫成利息資本化（L2-A#2）、電力轉嫁總額（L2-A#3）、折舊年限（L2-A#4／C-A3）或承租方 RVG（L13-A）；或
(5) 12 個月內無檢驗事件（3Q26／4Q26 10-Q／10-K 之遞延租金負債與應計租金應收序列、Adjusted EBITDA 定義變更、賣方報告口徑）；或
(6) 直線化差額與預收攤轉不改變任何被定價之財報科目（§7-4），例如賣方模型直接使用合約現金表。

複查觸發器（若日後殺）：任一樣本主體於 Adjusted EBITDA 新增或刪除直線租金調整列；SEC 意見函就非 GAAP 衡量之直線化／預收處理提問；具名賣方首次揭露以 GAAP 平均收益 vs 現金收益之差異下修 EBITDA。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：租賃收入（固定部分）、應計租金應收、遞延租金負債、Adjusted EBITDA 調節表。2. 可交易工具：非 REIT AI 出租方普通股（不選）。3. 半衰期：每季 10-Q 現金流量表即揭露一部分；全期守恆，前段超額於租期中點後反轉。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0128；`query/ARCH_matrix.md` L2［A］加「#5 已生成」；`AIM_FUNNEL.md` 日期行；`export/LEADS_算力收支.md` 追加 5 列（WULF 上半年 HPC 租賃收入、Core42 預收租金、GLXY 預收租金、GLXY 未來最低租賃收入、Bernstein 平均年收益／MW）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L2-A／#2–#4、L2-P／#2–#5、L2-I／#2–#4、L6-A#3、L13-A、C-A3；不寫 T。
