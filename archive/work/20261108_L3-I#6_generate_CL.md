# L3-I#6 生成卡｜半導體製造測試：誘因（§48D 開工期限之選擇權誘因：2026-12-31 前「開工」即鎖定 35% 投資抵減且以連續性安全港延至 2036 年投產 → 2026 下半年美國廠案開工／5% 成本安全港付款叢集於期限前，其後新案開工斷崖；開工≠依需求擴產）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md（經 FUNNEL §2）；archive/drive/USED_20260926_L3-I_generate_GK.md；archive/work/20261009_L3-I#2_generate_CL.md；archive/work/20261017_L3-I#3_generate_CL.md；archive/work/20261024_L3-I#4_generate_CL.md；archive/work/20261031_L3-I#5_generate_CL.md；archive/work/20261008_L3-A#2_generate_CL.md（補助淨額法，相鄰）；archive/work/20261108_L3-A#6_generate_CL.md（格式） | EMITS: work/20261108_L3-I#6_generate_CL.md -->
**日期：** 2026-11-08　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 4→5／6）　**格：** L3-I　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L3-A#6 已於本日測一）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-31（L3-I#5、L4-A#5、L4-P#5）→ 依表序取 **L3-I**；既有生成 5 份 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `48D`／`半導體`／`fab`，命中 5 筆，皆為模型定價／評測（SRC_PRC_012–014、SRC_CAP_002、SRC_HAR_014），與本格無關，未用。內部數字（§12）：未取用。
- 比對（本卡須異型）：
  - **L3-I#1**（GK）：產能預付款＝排序權。本卡物件非客戶預付，而是**政府稅制期限**對供給方之開工誘因。
  - **L3-I#2**：DOC 認股權證之或有稀釋（分拆選擇權成本）。本卡不涉股權結構。
  - **L3-I#3**：ATE 指定客戶 vs 採購客戶。本卡不涉客戶結構。
  - **L3-I#4**：14A 擴產以外部承諾需求為閘門（需求→開工）。本卡為反向：**稅制期限→開工**，與需求解耦；不改其結論。
  - **L3-I#5**：非約束預訂之重複下單（需求端誇報）。本卡為供給端時點誘因。
  - **L3-A#2**：補助以淨額法沖減 PP&E（會計呈現、死於量級）。本卡不論入帳方式；物件為**開工時點之叢集與其後斷崖**（行為），非折舊基數。
  - ARCH_dead：C-I3′／N-02（利益未分列）→ 否決 (2)；L12 系（監理）之落差為審查／許可閘門，本卡為稅抵期限，不碰 L12-P#1–#6。
- §7-10 領域最近公開：Holland & Knight 2026-10-05「Section 48D Deadline Is Near」（現行法仍為 2026-12-31，「Unless the U.S. Congress takes action」）；H.R. 6055（SEMI Investment Act，2025-11-17 提出，擬改為 2031-12-31；後續動作未核）；26 CFR 1.48D-5（T.D. 10009，2024-10-23）；Micron 10-K FY26（2026-10-09）；TI 10-Q 3Q26（2026-10-23）。

## 1. 落差一句

26 U.S.C. §48D(e)：抵減不適用於「construction of which begins after December 31, 2026」之財產；OBBBA 將 2025-12-31 後投產者之抵減率 25%→35%。1.48D-5：開工＝「physical work of a significant nature」（例：基礎開挖、澆置基礎）**或** 已支付／發生總成本 5%；連續性安全港：2026 年開工、2036-12-31 前投產者視為連續（H&K）。**故開工是一張低履約成本、十年期之 35% 抵減選擇權**：理性業者於 2026 下半年把所有「或許會蓋」之美國廠案先開工／先付 5%，**實際設備投入則仍依需求於 2027–2036 分期**；2027 起新案開工斷崖。公開層若以 2H26 開工／動土／設備訂金叢集讀作需求驅動之產能承諾（或以 2027 新案斷崖讀作需求轉弱），兩者皆把**稅制期限效應**誤當**需求訊號**。
**已讀事實 `[V]`：**
- Micron 10-K FY26（sec.py）：「we receive a 35% investment tax credit on qualified investments in U.S. semiconductor manufacturing under the CHIPS Act」；FY26 PP&E 支出 30.71B、政府補助抵減資本支出收款 3.32B；風險因子：「we have discretion in the timing of use of certain of these incentives」。
- TI 10-Q 3Q26（sec.py）：9M26「Investment tax credit (ITC) used to reduce income taxes payable $380」（百萬）；「We expect to continue benefiting from the CHIPS Act. This includes the 35% ITC」；「Beyond 2026, capital expenditures will be dependent on revenue and growth expectations」。
- ManufacturingMag 2026-06-16（標 AI 輔助、作線索）：「The 48D Cliff: Why Chipmakers Are Racing to Pour Concrete Before Dec. 31, 2026」——未具名任何為期限動土之公司。
**種子主張：** 2H26 美國半導體廠案開工與 5% 安全港付款叢集之一部分為稅抵選擇權之行使，不代表等量設備需求；開工後之設備投入（WFE）節奏仍由需求決定，且 35% 抵減延續至 2036，使**後段設備需求之價格彈性高於開工數所示**。方向未定；H.R. 6055 若通過則機制消失（否決 (1)）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：期限 T＝2026-12-31；開工成本 c（實體工作或 5% 成本）≪ 抵減現值 0.35·PV(合格投入)；選擇權到期 2036 → 最適策略＝期限前對所有正機率廠案開工，延後實投 |
| 選擇者 | 業者（開工與否、以實體工作或 5% 路徑）；國會（延長與否）；Treasury（連續性與「integral」解釋）；設備商（5% 安全港之訂金合約） |
| 已讀事實 | 見 §1 |
| 未證之連結 | 2H26 實際開工／5% 付款之案數與資本支出規模；業者是否於申報揭露「開工以保抵減」之意圖；開工後實投節奏；具名賣方是否已拆出期限效應；H.R. 6055 現況 |
| 量綱 | 案數；美元（合格投入 × 35%）；時間（開工→投產年數 ≤ 10） |
| 半衰期 | 期限前 1–2 季（叢集）；其後 2027–2028 新案斷崖可觀測 |

## 3. B 端可觀測載體（只指名）

1. Micron 10-K FY26 https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm （Note 15 Government Incentives；購置義務 4.18B；1Q27 資本支出指引）
2. TI 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/97476/000009747626000169/txn-20260930.htm （ITC 現金效益；2026 後資本支出口徑）
3. Holland & Knight 2026-10-05 https://www.hklaw.com/en/insights/publications/2026/10/section-48d-deadline-is-near
4. 26 CFR 1.48D-5 https://www.law.cornell.edu/cfr/text/26/1.48D-5 ；H.R. 6055 https://www.govinfo.gov/content/pkg/BILLS-119hr6055ih/pdf/BILLS-119hr6055ih.pdf
5. 未讀：26 U.S.C. §48D 原文（LII 讀取逾時，非存在性主張）；congress.gov H.R. 6055 動作；Intel、GlobalFoundries、Samsung Austin/Taylor、TSMC Arizona（20-F／6-K）、SK hynix Indiana、Amkor Arizona 之 2H26 開工公告；AMAT／LRCX／KLAC 美國區訂單與客戶訂金；SEMI World Fab Forecast 美國新案數。

## 4. 不寫

H1／H5、表達工具選擇、方向判斷、受益或受損標的。

## 5. 否決觸發（測一逐條實讀）

1. **期限消失：** H.R. 6055 或其他立法於 2026-12-31 前延長／取消 §48D(e) 期限，或 Treasury 放寬至以投產日認定 → 否決（誘因不存在）。
2. **可分離性：** 申報與公告無法區分「期限驅動開工」與「需求驅動開工」（無開工日、無 5% 安全港揭露、無逐案合格投入）→ 否決（C-I3′／N-02 型）。
3. **無叢集：** `[D]` 2H26 美國半導體廠案開工（含 5% 路徑）案數 ÷ 2024–1H26 半年均值 < 1.5，或 2H26 開工案之合格投入 ÷ 同期美國半導體資本支出 < 10% → 否決（量級；門檻凍結於此）。
4. **已定價／已揭露：** 公司或具名賣方已明言開工係為保抵減且實投依需求分期，並據以調整 WFE／產能預測 → 否決（無錯價）。
5. **連續性綁定：** 1.48D-5 連續性要求（或 2026 新指引）實質迫使開工後依原時程投入（安全港不足以延後實投）→ 否決（開工≈實投，無選擇權）。
6. **口徑：** 叢集主要來自已核 CHIPS 直接補助之里程碑（獎助協議時程）而非 §48D 期限 → 標方向分歧，拆分後再判。

## 6. 測一入口

依 §5 (1)–(6) 逐條實讀；SEC 一律 `tools/sec.py`；§48D 原文改以 govinfo／uscode.house.gov 實讀；開工案數 `[D]` 須列每案出處；12 個月內檢驗事件：2026-12-31 期限本身、H.R. 6055 動作、Micron 1Q27／2Q27 10-Q、TI 10-K FY26、設備商 4Q26／1Q27 美國區訂單揭露。
