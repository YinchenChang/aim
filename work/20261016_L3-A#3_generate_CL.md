# L3-A#3 生成卡｜半導體製造測試：會計恆等（封測代收材料：淨銷售 ≡ 加工附加值＋材料轉嫁 → 毛利率分母含轉嫁項）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260924_L3-A_generate_GK.md；archive/drive/USED_20260924_L3-A_test1_GK.md；archive/work/20261008_L3-A#2_generate_CL.md；work/20261008_L3-A#2_test1_CL.md；archive/work/20261009_L3-I#2_generate_CL.md；archive/work/20261009_L3-P#2_generate_CL.md | EMITS: work/20261016_L3-A#3_generate_CL.md -->
**日期：** 2026-10-16　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain，配額 3／6）　**格：** L3-A　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L12-I#3 已於本日測一）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-08（L3-A#2、L1-A#2；L12-I 已取）；依 QUEUE 先後（Q-0011 早於 Q-0012）取 L3-A。既有生成 2 份 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `consigned`／`OSAT`／`packaging`／`Amkor`，命中 0 筆。
- 比對（本卡須異型）：
  - **L3-A#1**（GK）：有效晶粒單價＝晶圓價 ÷（多層良率 × 顆數）；死於節點 ASP／層別良率不可由申報反解。本卡不談良率與單價，談**營收認列口徑**（材料自購轉嫁 vs 客戶寄售）。
  - **L3-A#2**：補助淨額法沖減 PP&E，死於量級（≤ 1.9% 毛利）。本卡不涉補助與折舊。
  - **L3-I#2**（預付款取用權）、**L3-P#2**：主體與恆等不同。
  - ARCH_dead：C-I3′／N-02（L4 分部毛利由非機制項解釋、未分列）為「利益未分列」型；本卡之材料成本**已分列**（ASU 2023-07 重大分部費用），型態不同。
- §7-10 領域最近公開：Amkor 10-Q 2Q26（2026-07-28）；Amkor 10-K FY25（2026-02-20）；ASE 20-F FY25（2026-04-01）；Amkor 3Q26 財報預計 2026-10 下旬（下一檢查點）。

## 1. 落差一句

封測廠淨銷售 ≡ 加工附加值 ＋ 自購材料轉嫁（基板、IC、被動元件等；晶圓多為客戶寄售、不入營收）。Amkor 2Q26 材料成本占淨銷售 52.6%（1H26 53.0%），毛利率 16.8%；管理層自述「advanced packaging, which tends to have higher material costs」。故**毛利率 ≡ 毛利 ÷（附加值＋轉嫁）**：先進封裝 mix 上升（或基板漲價轉嫁）機械地拉低毛利率，即使附加值毛利率（毛利 ÷〔淨銷售 − 材料〕）上升；反之客戶改寄售基板／HBM 則營收縮、毛利率升而經濟不變。種子主張：市場與指引以毛利率（「mid-to-high-teens」）讀封測定價力與稼動率，未以附加值口徑折算材料轉嫁比之變動。**方向未定**。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：GM% ＝ GP ÷ S；S ＝ VA ＋ M（M＝材料轉嫁）；附加值毛利率 ＝ GP ÷ (S − M)；ΔGM% 可拆為附加值毛利率變動 × (1 − m) 與材料比 m 變動兩項 |
| 已讀事實 | Amkor 10-Q 2Q26 分部表「Net sales $ 1,897,965 … Less: Materials cost of sales 997,510」（千美元；2Q25 1,511,392／799,020）；比率表「Materials 52.6 % 52.9 %」「Gross margin 16.8 % 12.0 %」。10-K FY25「The silicon wafer is generally consigned from our customer. We generally do not take ownership of the customer consigned wafer」。 |
| 未證之連結 | 材料是否以近成本轉嫁（無加成）；寄售範圍（基板／HBM／IC）是否逐期變動、是否揭露；同業（ASE、Intel Foundry 封裝、TSMC CoWoS）口徑可比性 |
| 量綱 | 附加值毛利率（%）vs 報告毛利率（%）；兩者變動之差（百分點／季） |
| 半衰期 | 季（每季分部表即更新） |

## 3. B 端可觀測載體（只指名）

1. Amkor 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1047127/000104712726000046/amkr-20260630.htm （分部重大費用：材料／人工／折舊／其他；比率表；材料成本敘述）。
2. Amkor 10-K FY25 https://www.sec.gov/Archives/edgar/data/1047127/000104712726000014/amkr-20251231.htm （寄售晶圓、材料採購責任條款）。歷期 10-Q 供 ≥ 4 季材料序列。
3. ASE Technology 20-F FY25 https://www.sec.gov/Archives/edgar/data/1122411/000119312526135585/d50802d20f.htm （封測／EMS 分部、原物料成本、寄售；本輪未讀）。
4. TSMC 20-F／6-K（先進封裝營收之寄售 HBM 口徑；本輪未讀）。
5. Amkor 法說與新聞稿（毛利率指引、材料轉嫁、價格調整）；Hudson Labs 2026-07-08 https://www.hudson-labs.com/research/amkr-q2-2026-earnings （「mid-to-high-teens gross margins」、「tripling of advanced packaging revenue in 2026」、客戶接受漲價以抵成本）。
6. 具名賣方是否以附加值口徑建模（未讀）。

缺段（§7-2）：材料加成與寄售範圍變動之原文；本輪未讀；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 材料成本逐季於分部表公開，任何讀者可自算附加值毛利率；已定價 | 載體 1 | 落差 |
| R2 | 材料比 m 長期穩定（52.9%→52.6%），口徑效果 < 1 個百分點，毛利率變動主由稼動率解釋 | 載體 1、5（稼動 50s→low 70s） | 量級 |
| R3 | 材料含加成，非純轉嫁；附加值口徑高估 | 未讀 | 機制 |
| R4 | 封測為小型層；可交易主體少、台股禁（§2-8） | CHARTER §2-8 | 表達 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) ≥ 2 家上市封測／先進封裝主體無法提供 ≥ 4 期材料成本（或原物料）與淨銷售之同口徑序列；或
(2) `[D]` 量級：4 期以上報告毛利率與附加值毛利率之變動差，最大值 < 1 個百分點（口徑效果可忽略）；或
(3) 公司原文明示材料含實質加成或與加工一併定價，使「轉嫁」分解不成立；或
(4) 寄售範圍（晶圓以外）無任何揭露或已觀測之變動，且先進封裝 mix 上升未伴隨材料比上升；或
(5) 公司或具名賣方已以附加值／材料除外口徑揭露或建模（已定價）；或
(6) 已觀測之毛利率變動，公司原文歸因於稼動率、價格或匯率，且材料比變動之貢獻可由恆等式算出 < 其三分之一。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：分部材料成本、存貨（客戶承擔之未用材料）、寄售揭露。2. 可交易工具：美股上市封測主體（不選）。3. 半衰期：季。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L3［A］格加「#3 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0054。不改 L3-A#1／#2、L3-P#1／#2、L3-I#1／#2、C-I3′、N-02、L12-I#3 結論。
