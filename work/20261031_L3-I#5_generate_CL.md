# L3-I#5 生成卡｜半導體製造測試：誘因（配給賽局之重複下單：先進封裝短缺時，客戶「多報、多處訂」之邊際成本近零，OSAT 依非約束性預訂擴產；預付款為篩選裝置）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md（經 FUNNEL §2）；archive/drive/USED_20260926_L3-I_generate_GK.md；archive/work/20261009_L3-I#2_generate_CL.md；archive/work/20261017_L3-I#3_generate_CL.md；archive/work/20261024_L3-I#4_generate_CL.md；work/20261024_L3-I#4_test1_CL.md；archive/work/20261031_L3-A#5_generate_CL.md（格式） | EMITS: work/20261031_L3-I#5_generate_CL.md -->
**日期：** 2026-10-31　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 4→5／6）　**格：** L3-I　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L3-A#5 已於本日測一）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-24（L3-I#4、L4-P#4）→ 依表序取 **L3-I**；既有生成 4 份 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `48D`／`investment tax credit`／`begin construction`（初擬方向），命中 0 筆；改選本機制後未再查。內部數字（§12）：未取用。
- 初擬棄用：§48D 開工期限之提前開工誘因——與 L12-I#3（§48D 開工期限＋10 年連續性安全港）同規則，型態過近，棄。TSMC 毛利率目標驅動 CoW 外包——TrendForce 2026-04-28 標題稱 CoWoS 晶圓 ASP 近 7 nm、將為利潤驅動（只見標題），前提（封裝低於公司均毛利）不成立，且 08-05 報導稱外包「not being led by TSMC」而由晶片商提出，棄。
- 比對（本卡須異型）：
  - **L3-I#1**（GK）：產能預付款＝合約性排序權而非物權。本卡**不以預付款之法律性質為落差**；預付款在此只作**篩選裝置**（否決 (1)：預付覆蓋擴產則重複下單不成立）。物件為**非約束性預訂之總量**是否超過終端需求。
  - **L3-I#2**（DOC 認股權證）、**L3-I#3**（指定者≠付款者）：主體與機制不同。
  - **L3-I#4**（第二供應源＝買方議價選擇權，約束 TSMC 定價）：本卡不談定價約束；談**配給下之數量誇報**（Lee–Padmanabhan–Whang 型 shortage gaming）。多源只作誇報之管道，不作議價工具；否決 (5) 檢兩者能否分離。
  - **L3-P#3／#4／#5**（探針卡、中介層面積、老化熱容量）：守恆型；本卡不涉物理容量上限。
  - ARCH_dead：C-I3′／N-02（利益未分列）——OSAT 申報有 Advanced products 與 Computing 分列，但 CoWoS／LEAP 單列僅見 ASE 口頭目標，否決 (2) 檢之。
- §7-10 領域最近公開：Amkor 10-Q 3Q26（2026-10-27）；ASE 6-K 3Q26 業績（2026-10-29，acc `0000950103-26-016323`／`-016324`）；TrendForce 2026-08-05（CoWoS 產能與 CoW 外包，二手）；TrendForce 2026-07-31（ASE 2Q26 法說，二手）。

## 1. 落差一句

短缺期之配給以「預訂量」為分配基準時，客戶之最適策略是**誇報並多處下單**（重複下單之邊際成本≈ 0，若預訂無約束、可取消）；供給方據此擴產，短缺解除時預訂同步蒸發。Amkor 10-Q 3Q26 原文：「customers do not commit to purchase any significant amount of packaging or test services or provide us with binding forecasts … in any material amount. In addition, we sometimes experience double booking by customers」；同期 TrendForce 轉述 TSMC 月 CoWoS 產能 7 萬 → 13–14 萬片（2025 → 2026 年底）、供需缺口仍約 20%，且 ASE／SPIL 以 2026 資本支出自建 CoW 線、由**晶片商**提出「全流程」繞過 TSMC 瓶頸；ASE 2026 資本支出上調至 105 億美元（二手）並稱已取得「客戶 2027 需求與產能要求之能見度」。種子主張：**AI 先進封裝之 2027 產能規劃（TSMC＋OSAT 合計）以短缺期之多處預訂為輸入，若同一終端需求同時預訂於 TSMC CoWoS 與 OSAT 全流程線，合計預訂 > 終端加速器需求所需之封裝量；OSAT 之擴產與毛利率擴張（ASE ATM 3Q26 毛利率 30.6%、4Q26 指引再升 1–2 pp）對此誇報之敏感度未被定價**。**方向未定且反證已在手**：Amkor 預期未來 12 個月收取客戶預付款約 19 億美元、2026-10 另簽一筆 2027 年約 13 億美元，對比 9M26 資本支出 12.37 億 `[D]`——預付規模與擴產同量級，正是抑制重複下單之約束，可能使本落差不成立。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：配給賽局。客戶 i 之預訂 `b_i = d_i × g(短缺度, 取消成本)`，`g > 1` 當取消成本 ≈ 0；`Σ b_i（跨 TSMC＋OSAT） − D_pkg` ＝誇報量；預付、take-or-pay、不可取消條款使 `g → 1` |
| 選擇者 | 晶片商（NVIDIA、AMD、ASIC 設計商與其雲端客戶）：預訂量與分散下單；OSAT／TSMC：是否要求預付或約束性預測、擴產節奏 |
| 已讀事實 | **Amkor 10-Q 3Q26**（sec.py 實讀）：上引「binding forecasts」「double booking」兩句；風險因子「the absence of backlog, the short-term nature of our customers' commitments, double bookings by customers」；「we expect to receive approximately $1.9 billion of customer advance payments in the next 12 months … In October 2026, we entered into an advance payment agreement with a customer pursuant to which we expect to receive approximately $1.3 billion in 2027」；合約負債 547.6 vs 390.8 百萬（2026-09-30 vs 2025-12-31）；Advanced products 3Q26 1,631.6 vs 1,683.5 百萬；Computing 占營收 26%（3Q25 19%）；資本支出 3Q26 548.4、9M26 1,236.8 百萬。**ASE 6-K 3Q26**（sec.py 實讀）：ATM 營收 NT$151.5B、毛利率 30.6%（2Q26 27.3%）；封裝營收 122,945 百萬（YoY +53%）、測試 26,302（+43%）；ATM 設備資本支出 3Q26 US$2,104M（封裝 991M）；4Q26 指引 ATM 營收 QoQ +11–13%、毛利率 +100–200 bp。**TrendForce 2026-08-05**（二手，轉述 ETNews／Mydrivers）：「expand outsourcing of CoW … to OSAT companies including ASE」「Unlike its previous practice of primarily outsourcing WoS」；NVIDIA 預訂 2026 年約 80–85 萬片 CoWoS、逾半；缺口約 20%；Mirror Daily：ASE／SPIL 自建 CoW 線「not being led by TSMC, but instead reflects a new approach proposed by major chipmakers」。**TrendForce 2026-07-31**（二手）：ASE 2026 capex 85 → 105 億美元；LEAP 2026 已逾 35 億目標、2027 目標 55 → ≥ 75 億美元；「secured visibility into customers' 2027 demand and capacity requirements」 |
| 未證之連結 | 同一終端需求是否實際**同時**預訂於 TSMC 與 OSAT（客戶別預訂不公開）；ASE LEAP 合約之取消條款與預付比例（ASE 6-K 未見）；Amkor 預付款對應之產品（是否為 AI 先進封裝或 Arizona 廠）；合計封裝預訂 vs 加速器出貨所需封裝量之 `[D]` 換算（每片 CoWoS 晶圓可封顆數隨中介層面積而變，見 L3-P#4 之結論，不重用其落差） |
| 量綱 | 片／月（CoWoS 等效晶圓）；誇報率 ＝ Σ 預訂 ÷ 終端所需 − 1；OSAT 曝險 ＝ AI 先進封裝營收 ÷ 總營收；約束度 ＝ 預付款 ÷ 對應擴產資本支出 |
| 半衰期 | 2–6 季（短缺解除至預訂修正之滯後；歷史 2021–2023 OSAT 循環為參照，測一須實讀） |

## 3. B 端可觀測載體（只指名）

1. Amkor 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/1047127/000104712726000052/amkr-20260930.htm ；8-K 3Q26 業績 https://www.sec.gov/Archives/edgar/data/1047127/000104712726000049/amkr-20261026.htm
2. ASE 6-K 3Q26 https://www.sec.gov/Archives/edgar/data/1122411/000095010326016323/dp255782_6k.htm 、https://www.sec.gov/Archives/edgar/data/1122411/000095010326016324/dp255760_6k.htm ；ASE 20-F FY25（未讀：取消條款、預付）
3. TrendForce https://www.trendforce.com/news/2026/08/05/news-tsmc-reportedly-expands-outsourcing-of-key-cowos-front-end-step-to-osats-amid-rising-nvidia-asic-demand/ ；https://www.trendforce.com/news/2026/07/31/news-ase-again-raises-2026-capex-to-record-us10-5b-eyes-2x-leading-edge-advanced-packaging-revenue-by-2027/
4. 只見標題、未實讀：TrendForce 2026-04-28 CoWoS ASP https://www.trendforce.com/news/2026/04/28/news-tsmc-cowos-wafer-asp-reportedly-nears-7nm-levels-advanced-packaging-poised-to-become-a-key-profit-driver/ ；Morgan Stanley CoWoS 需求 2027 倍增（轉述）https://www.kucoin.com/news/flash/morgan-stanley-report-cowos-demand-to-double-by-2027-amd-and-asics-drive-ai-chip-growth ；「CoWoS sells out to 2027」https://aiweekly.co/alerts/tsmc-pilots-copos-panel-packaging-as-cowos-sells-out-to-2027
5. 未讀：TSMC 3Q26 法說原文（CoWoS 產能、客戶預付或長約）；NVIDIA 10-Q 3QFY27 之供應承諾／預付（prepaid supply agreements、multi-year capacity）；AMD、Broadcom 同口徑；具名賣方是否量化重複下單。

## 4. 不寫

H1／H5、表達工具選擇、方向判斷。

## 5. 否決觸發（測一逐條實讀）

1. **約束已到位：** AI 先進封裝之預訂由預付款、take-or-pay 或不可取消條款支撐，且預付（或約束性承諾）÷ 對應擴產資本支出 ≥ 50% `[D]`（門檻本卡凍結；Amkor 19 億 vs 9M26 資本支出 12.37 億為首讀） → 否決（`g → 1`，誇報無成本優勢）。
2. **不可分離：** OSAT 不分列 AI／CoWoS 類先進封裝營收或產能（僅 Advanced products、Computing 等寬口徑），且晶片商申報亦無封裝承諾分列 → 否決（C-I3′／N-02 型）。
3. **已被定價／已揭露：** 具名賣方或公司已量化 CoWoS／先進封裝之重複下單或 2027 過剩風險（含 Amkor 之 double booking 句已被具名報告引為主論點） → 否決（無錯價）。
4. **無超額：** 以公開加速器出貨或預訂（NVIDIA、AMD、ASIC）換算之 2027 封裝需求 ≥ TSMC＋OSAT 規劃產能 `[D]`（即無合計誇報空間）；或 TSMC 與 OSAT 線之客戶集合可證不重疊 → 否決。
5. **與 L3-I#4 不可分離：** 多處下單之可觀測證據只能解讀為議價（壓 TSMC 價格）而非數量誇報 → 否決（型態重複）。
6. **無 12 個月內檢驗事件：** 未來 4 季無可辨識之預訂修正窗（OSAT 指引、TSMC CoWoS 產能更新、晶片商供應承諾變動）→ 否決（重定價窗 < 12 個月之檢驗缺）；主體僅 ADR（ASX）或美股（AMKR）以外 → 標表達約束（§7-4），不在生成階段否決。
