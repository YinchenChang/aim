# L1-I#4 生成卡｜能源與電力：誘因（大負載之「表後淨額」誘因——以自有／共址發電沖減計費負載以避開輸電與容量費；監理改寫此誘因後，表後供電需求中屬費率套利之部分不可見）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260926_L1-I_generate_GK.md；archive/work/20261009_L1-I#2_generate_CL.md；archive/work/20261016_L1-I#3_generate_CL.md；work/20261016_L1-I#3_test1_CL.md；archive/work/20261024_L1-A#4_generate_CL.md | EMITS: work/20261024_L1-I#4_generate_CL.md -->
**日期：** 2026-10-24　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 2→3／6）　**格：** L1-I　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L1-A#4 已於本日測一）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-16（L1-I#3、L3-P#3、L3-A#3、L12-A#3、L12-I#3；L1-A 已於 10-24 補 #4）→ 依表序取 **L1-I**（L1-P＝刻意排除 T-11 不取）；既有生成 3 份 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `co-location`／`behind the meter`／`network integration`／`transmission service`，命中 0 筆。內部數字（§12）：未取用。
- 比對（本卡須異型）：
  - **L1-I#1**（GK）：發電開發商之佇列佔位誘因 → 公開佇列高估；死於承諾 MW 不可分離。本卡選擇者＝**大負載（資料中心）**，誘因＝**沖減計費負載以避開輸電／容量費**，非佔位。
  - **L1-I#2**：受管電業以費率基報酬為誘因擴建、最低需量覆蓋不足；損失落於其他費率類別。本卡之損益承擔者**不經費率分攤**：為表後／共址供電之**非受管供應方**（燃料電池、燃氣機組、共址 IPP）與資料中心開發商。輸電費轉嫁至其他費率類別一節屬 L1-I#2 型，本卡不以之為落差。
  - **L1-I#3**：買方減碳宣稱誘因 → 核電長約屬性溢價（Scope 2 規則依存）。本卡為**費率結構套利**（輸電／容量計費基礎），非環境屬性。
  - **L1-A#1–#4**（PPA 鎖價存量、Bloom 收入認列時序、AFUDC、客戶預付款損益路徑）：會計恆等型。L1-A#2 與本卡共用 Bloom 為可能載體，但 #2 談收入認列時差，本卡談需求來源中之監理套利成分；不得合併。
  - ARCH_dead：C-I3′／N-02（利益未分列）——本卡測一 (1) 即為同類可分離性題；主體與機制不同，非已殺同型。T-11 不碰。
- §7-10 領域最近公開：FERC 2026-06-18 令（195 FERC ¶ 61,209，Docket EL25-49-002 et al.）接受 PJM 50 MW 表後淨額門檻（改以單一電氣位置可淨額之**負載**計）、三年過渡（至 2028-12-18）及既有合約保留；同日對 PJM／MISO／CAISO／ISO-NE／NYISO／SPP 六份 show cause（含「behind the meter generation and co-located loads」）；PJM 60 日內再遵循（約 2026-08-17）；新輸電服務費率之 paper hearing 未結。ERCOT：PUCT 2026-07-24 Docket 59220 首件 SB 6 淨額安排核准附條件。Bloom 10-Q 3Q26（2026-10-22）。下一檢查點＝FERC 就 PJM 2026-08 再遵循之裁定、paper hearing 費率結論、六 RTO show cause 回覆之裁定；Bloom／Talen／GEV 4Q26 申報。

## 1. 落差一句

資料中心選擇表後／共址供電，誘因至少有二：**上線速度**（避開併網與網路升級等待）與**計費負載淨額**（以表後發電沖減 NITS 輸電費與容量費之計費基礎）。監理已開始拆掉後者：FERC 2025-12-18 令判 PJM 費率不合理、2026-06-18 令接受 50 MW 淨額上限（三年過渡、既有合約保留），新共址負載須擇 Interim NITS／Firm／Non-Firm Contract Demand，並按總需量付 regulation／black start、按 NITS 總需量或契約需量付容量費；ERCOT 依 SB 6 對既有發電之淨額安排逐案審查、附全斷電義務。種子主張：市場把表後／共址供電需求（燃料電池、燃氣機組、共址 IPP 長約）讀成**結構性**（速度與電網稀缺），未拆出依存於**淨額計費規則**之套利成分；規則收緊後，新約之經濟性重定價、或改為表前（如 Talen–AWS 於 2026-04 轉為「front-of-the-meter」）。**方向未定**：若速度誘因獨占，淨額規則改變不影響需求，落差不存在；亦可能 Non-Firm Contract Demand 免容量費使表後更有利。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：大負載之供電型態選擇 ＝ f（上線速度、淨額可避之輸電／容量費、可靠度、排放許可）；監理改寫「可避費用」項 |
| 選擇者 | 資料中心開發商／雲業者（表後 vs 共址 vs 電網）；FERC／PJM／PUCT（淨額門檻、新服務費率、過渡與保留）；表後供應方（以何合約型態承接） |
| 已讀事實 | Mayer Brown 2026-01-13（12-18 令：三種新服務、按總需量計 regulation／black start、容量費依 NITS 總需量或 Firm 契約需量、Non-Firm 免容量費、PJM 須提淨額 MW 門檻、既有三年過渡）；CES 2026-03／DCF 2026-03-12（PJM 2026-02-23 提 50 MW、過渡至 2028-12-18）；Willkie 2026-07-02（06-18 令接受 50 MW 但改以負載計、六份 show cause、實施日 PJM 提 2029-06-01 須補證）；White & Case 2026-08-05（PUCT Docket 59220：265.5 MW 既有風場＋260 MW AI 資料中心、輸電緊急時全斷、不得參與需量反應）；Talen 10-Q 2Q26：AWS 1,920 MW「front-of-the-meter」至 2042、2026-04 轉換完成；Bloom 10-Q 3Q26：大型資料中心部署驅動產品需求、Oracle「on-site solid state power for AI data centers」，**全文無 behind-the-meter／transmission charge／FERC 字樣** |
| 未證之連結 | 淨額可避費用（$/MWh 或 $/kW-年）占表後供電總經濟性之比；各上市供應方之訂單中屬 PJM 淨額 > 50 MW 情境者之比例；既有合約保留範圍；Non-Firm 服務實施日與費率；他 RTO show cause 結果 |
| 量綱 | 可避輸電＋容量費 ÷ 表後全成本（%）；受影響之表後 MW ÷ 供應方在手訂單 MW（%）；規則情境下之訂單／合約重定價（$/kW） |
| 半衰期 | 年（過渡至 2028-12-18；PJM 實施日爭議至 2029；合約 10–20 年） |

## 3. B 端可觀測載體（只指名）

1. FERC 2026-06-18 令與 PJM 遵循（Willkie 摘要）https://www.willkie.com/publications/2026/07/ferc-greenlights-pjm-co-located-load-framework-in-part-calls-for-further-tariff-updates ；12-18 令摘要 https://www.mayerbrown.com/en/insights/publications/2026/01/ferc-directs-pjm-to-facilitate-co-location-arrangements ；PJM 遵循 ER26-1479 https://www.pjm.com/pjmfiles/directory/etariff/FercDockets/9461/20260223-er26-1479-000.pdf （未讀）
2. PJM 50 MW 提案報導 https://ces-ltd.com/pjm-responds-to-fercs-december-order-on-co-located-load/ ；https://www.datacenterfrontier.com/energy/article/55362901/pjm-moves-to-redefine-behind-the-meter-power-for-ai-data-centers
3. PUCT Docket 59220 https://www.whitecase.com/insight-alert/puct-affirms-curtailment-authority-over-co-located-data-centers-first-net-metering
4. Talen 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm ；Bloom 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/1664703/000162828026066931/be-20260930.htm
5. 離網趨勢評論（無數字）Utility Dive 2026-03-17 https://www.utilitydive.com/news/as-data-centers-go-off-grid-utilities-face-new-cost-and-planning-risks/811944/
6. 未讀：GEV、CAT、VST、CEG 10-Q 有無表後／共址合約之淨額依存揭露；PJM 表後淨額現存 MW 統計；paper hearing 費率主張；具名賣方或顧問（如 Enverus）就表後經濟性拆分可避輸電費之原文。

## 4. 不寫

H1／H5、表達工具選擇、方向判斷。

## 5. 否決觸發（測一逐條實讀）

1. **可分離性：** 任一上市表後／共址供應方或其客戶之申報、電話會或具名來源均無法分離「淨額可避費用」對訂單或合約經濟性之貢獻（金額、比例或受影響 MW 皆無）→ 否決（C-I3′／N-02 型）。
2. **誘因不存在或不重要：** 具名一手或分析顯示表後選擇幾乎全由上線速度驅動、可避費用占比可忽略（例如 < 10% 全成本），或 > 50 MW 新案本就不享淨額 → 否決。
3. **已被定價／已揭露：** 具名賣方或評等機構已就淨額規則變動量化上市供應方之訂單／盈餘敏感度 → 否決（無錯價）。
4. **保留覆蓋：** 既有合約保留與三年過渡覆蓋上市供應方絕大部分在手訂單，且 12 個月內無新約受影響 → 否決（重定價窗 < 12 個月或不存在）。
5. **方向抵銷：** Non-Firm Contract Demand 免容量費或六 RTO show cause 結果使表後／共址經濟性淨改善 → 不否決但標方向反轉，不得合併為同向落差。
6. **主體錯置：** 規則變動之損益主要落於受管電業費率分攤（L1-I#2 型）而非非受管供應方 → 否決本卡、不得改寫為 L1-I#2。
