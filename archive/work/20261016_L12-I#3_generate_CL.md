# L12-I#3 生成卡｜監理與法制：誘因（§232 半導體關稅抵銷配額：在建期 2.5× vs 完工後 1.5× ＋ §48D 2026-12-31 開工期限 → 「保持在建」之誘因）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260922_L12-I_generate_GK.md；archive/drive/USED_20260922_L12-I_test1_GK.md；archive/work/20261008_L12-I#2_generate_CL.md；work/20261008_L12-I#2_test1_CL.md；archive/work/20261008_L3-A#2_generate_CL.md；work/20261008_L3-A#2_test1_CL.md；work/20261009_L3-I#2_test1_CL.md；work/20261015_L12-P#3_test1_CL.md | EMITS: work/20261016_L12-I#3_generate_CL.md -->
**日期：** 2026-10-16　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain，配額 2／6）　**格：** L12-I　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L12-A#3 已於本日測一）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-08（L12-I#2、L3-A#2、L1-A#2）；同日依 QUEUE 先後（Q-0010 早於 Q-0011／Q-0012）取 L12-I。既有生成 2 份 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tariff`／`Section 232`／`48D`／`fab`，命中 5 筆（皆模型定價／評測，與本格無關）；未使用。
- 比對（本卡須異型）：
  - **L12-I#1**（GK）：法規合規成本落部署者、租金歸模型商；死於部署者 SG&A 無分列。本卡非合規成本，為**貿易救濟之配額設計**誘因；載體為公告文本與建廠里程碑。
  - **L12-I#2**：IP 補償＝賣方零保費賣權；死於觸發事件 0 件。本卡誘因已由法令文字確定（配額倍數），不待第三方求償。
  - **L3-A#2**（補助淨額法沖減 PP&E，會計呈現）：本卡不談補助入帳，談**行為**——配額倍數與開工期限如何改變「何時宣告完工」。§48D 在 L3-A#2 只作補助延續之反方 R4；本卡用其**開工期限**而非抵減入帳。
  - **L3-I#2**（DOC 認股權證之分拆選擇權）、**L12-P#3**（出口管制質量平衡）、**L1-I#2**（電業大負載擔保）：主體與規則皆不同。L12-P#3 之 H200 25% 關稅只作背景，本卡不測轉運。
  - ARCH_dead：無關稅／配額型死因。C-A4／C-A3（帳面折舊年限）、C-P4 無關。
- §7-10 領域最近公開：Proclamation 11002（2026-01-14，01-15 生效）；美台協議（2026-01-15）；TSMC 20-F FY25（2026-04）；Lutnick 2026-09-02 談話；Phase 2 報告已完成未公開（截至 2026-08-30）；Crapo／Wyden 2026-08-05 支持 §48D 延長，未立法（截至 2026-09-03）。下一檢查點＝Phase 2 公告；§48D 延長立法或 2026-12-31 屆期；TSMC 3Q26／4Q26 法說與 20-F FY26。

## 1. 落差一句

§232 半導體關稅之抵銷設計以**美國產能**換免稅進口額度：美台協議規定在建期可免稅進口「計畫產能」之 **2.5 倍**，完工後降為 **1.5 倍**（Global Policy Watch 2026-02；Tech Times 2026-09-03 對 TSMC 同述）；同時 §48D 35% 抵減只給 **2026-12-31 前開工**者。兩條規則合成之誘因：**盡早「開工」、盡量久「在建」、以計畫產能（非已建產能）換額度**——完工即失去 1.0× 額度。種子主張：市場以宣告產能（TSMC Arizona 265B 承諾）推算美國產能上線時程與設備需求，未把「在建期額度大於完工後」之反向誘因折入完工日期與分階段宣告。**方向未定**：Phase 2 稅率與名單未公告，配額可能永不生效；TSMC 自述「including any offsets, are still unclear」。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：規則端（Commerce／USTR、總統公告、協議）給「在建」優於「完工」之報酬；行為端（建廠者）選擇開工時點、分期與完工宣告 |
| 誘因式（僅定義） | 免稅額度 Q＝m(狀態) × 產能基數；m(在建)＝2.5、m(完工)＝1.5；完工之邊際額度損失＝1.0 × 基數 × Phase 2 稅率 × 進口單價；與延後完工之成本（折舊未起、營收延後、§48D 置於服務條件）相比 |
| 已讀事實 | Proclamation 11002：25% 只及窄類 AI 晶片且限非美國使用（White & Case 2026-01）；「may consider imposing significant tariffs」並附「offset program to enable companies investing in United States semiconductor production」。TSMC 20-F FY25：「grants preferential Section 232 treatment for Taiwanese semiconductor producers investing in U.S. manufacturing capacity. However, details … including any offsets, are still unclear」。Lutnick 2026-09-02：在美建廠者無關稅；未給稅率／時程。§48D：須 2026-12-31 前開工（Tech Times 2026-08-31）。 |
| 未證之連結 | 「計畫產能」與「在建期」由誰認證、上限期間多長；§48D 開工認定（實體工作／5% 安全港與持續性要求）是否限制「久在建」；Phase 2 是否實施 |
| 量綱 | 完工前後額度差所避關稅（美元／年）÷ 建廠者營收或營業利益（%）；完工日期延後（月） |
| 半衰期 | Phase 2 公告（不定期）；§48D 期限 2026-12-31；在建期長度（年級） |

## 3. B 端可觀測載體（只指名）

1. Proclamation 11002 https://www.whitehouse.gov/presidential-actions/2026/01/adjusting-imports-of-semiconductors-semiconductor-manufacturing-equipment-and-their-derivative-products-into-the-united-states/ （抵銷方案條文；本輪未讀原文，經 White & Case 摘要 https://www.whitecase.com/insight-alert/president-trump-orders-narrowly-targeted-25-section-232-tariff-certain-advanced ）。
2. 美台協議與配額倍數：Global Policy Watch 2026-02 https://www.globalpolicywatch.com/2026/02/a-month-in-semiconductor-policy-section-232-measures-bis-rule-and-taiwan-deal-signal-strategic-push/ ；USTR／Commerce 原文未讀。
3. TSMC 20-F FY25 https://www.sec.gov/Archives/edgar/data/1046179/000162828026025362/tsm-20251231.htm （Section 232 段、Arizona 分期與量產時程）；6-K 季報與法說（Arizona 各期開工／量產日）。
4. Micron、Intel、GlobalFoundries、Texas Instruments 10-K／10-Q：美國廠在建工程（CIP）、置於服務日、§48D 認列、關稅段（本輪未讀）。
5. 設備商 AMAT／LRCX／KLAC 10-K 美國地區營收序列（需求時點代理；本輪未讀）。
6. Tech Times 2026-08-31 https://www.techtimes.com/articles/325977/20260831/chip-tariff-phase-2-lands-fab-tax-credit-deadline-leaves-industry-frozen.htm ；2026-09-03 https://www.techtimes.com/articles/326474/20260903/chip-tariff-phase-two-confirmed-build-america-pay-lutnick-announces.htm （Phase 2 狀態、§48D 期限、TSMC 1.5× 約覆蓋 45% 產出之估計）。
7. TariffLens 2026-05-27 https://www.tarifflens.ai/blog/section-232-semiconductor-tariff-july-2026-phase-2-guide （Phase 2 未實施、抵銷方案未見條文）。
8. 未讀：Treasury §48D 開工認定指引原文；Commerce Phase 2 報告；具名賣方對 TSMC Arizona 完工時程之模型。

缺段（§7-2）：配額認證規則與在建期上限；本輪未讀；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | Phase 2 未公告、稅率／名單未定；配額只存在於協議與談話，可能永不具拘束力 | TariffLens 2026-05-27；Tech Times 2026-09-03；TSMC 20-F「still unclear」 | 誘因不存在 |
| R2 | 建廠延後之成本（AI 晶片需求、客戶要求美國產地、營收延後）遠大於額度差；TSMC 有加速 Arizona 之客戶誘因 | 載體 3、6 | 方向 |
| R3 | §48D 開工認定含持續施工要求，「開工後久拖」可能喪失抵減，兩規則互相抵消 | Treasury 指引（未讀） | 機制 |
| R4 | 額度差之量級：1.5× 已約覆蓋 TSMC 45% 產出（Tech Times），邊際 1.0× 之價值可能小 | 載體 6 | 量級 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 規則端：12 個月內無 Phase 2 公告或抵銷方案法律文本，且在建 vs 完工倍數差只見於新聞稿／談話（誘因無拘束力）；或
(2) ≥ 2 家美國建廠上市主體（如 TSM、MU、INTC、GFS、TXN）之 20-F／10-K／10-Q 無法提供 ≥ 4 期之分廠或分期開工／置於服務／量產日期或 CIP 序列，誘因之行為端不可觀測；或
(3) 規則互斥：§48D 或配額規則本身要求持續施工或設在建期上限，使「久在建」不可行；或
(4) `[D]` 量級：完工前後額度差所避關稅之可得最佳估計 < 該主體年營業利益 2%；或
(5) 公司或具名賣方已明示完工時程不受配額影響、或已將配額倍數納入時程模型（已定價）；或
(6) 已觀測之延後（如有）由非誘因項（人力、成本、需求、設備交期）解釋，且公司原文如此歸因。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：CIP、置於服務、§48D 應收／抵減、關稅成本段。2. 可交易工具：美國建廠者與設備商（不選）。3. 半衰期：Phase 2 公告不定期；§48D 2026-12-31；在建期年級。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L12［I］格加「#3 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0053。不改 L12-I#1／#2、L12-A#1–#3、L12-P#1–#3、L3-A#2、L3-I#2、L1-I#2、C-A3、C-A4 結論。
