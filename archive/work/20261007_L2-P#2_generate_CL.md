# L2-P#2 生成卡｜資料中心實體：守恆（散熱介質封頂之每櫃功率）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/INDEX.json；archive/drive/USED_20260929_GRID_snapshot_GK.md；archive/drive/USED_20260917_L2-I_generate_GK.md；archive/drive/USED_20260913_L2-A_test2_cost-index_GK.md；archive/drive/USED_20260926_L4-P_generate_GK.md；archive/drive/USED_20260930_L7-P_generate_GK.md | EMITS: work/20261007_L2-P#2_generate_CL.md -->
**日期：** 2026-10-07　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L2-P　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格依據（SCOUT.md §C-2）：ARCH_matrix 45 格皆已測；非「已殺／刻意排除」之格中，L2-P 之最後測試最舊——matrix＝「已測」、INDEX 無獨立檔（fileId＝GRID 快照 `archive/drive/USED_20260929_GRID_snapshot_GK.md`），其內容於他卡引用為「PUE 受濕球溫度封頂」，同層之 C-P4（水約束）於 ARCH_dead #19 標 4b §4.15（早於 2026-09-16）。其餘最舊者 L2-A 測二為 2026-09-13。L2-P 既有生成數計 1（PUE／濕球 種子）→ 本卡 #2。
- 比對過之舊檔與死因型態，本卡須異型：
  - L2-P#1（PUE 受濕球封頂；設施能效比）——本卡量綱為**每櫃 kW 與散熱介質**，不是 PUE。
  - C-P4（ARCH_dead #19；死因＝不通過(a)：水耗非損益科目、VRT 分部為地理別）——本卡不經水、不經冷卻商分部。
  - L2-A（`archive/drive/USED_20260913_L2-A_test2_cost-index_GK.md`；液冷相對空冷總成本 +7–10%）——會計恆等之每 MW 建置成本；本卡不是建置成本。
  - L2-I（`archive/drive/USED_20260917_L2-I_generate_GK.md`）——許可／併網取用權；本卡不涉許可。
  - L4-P（`archive/drive/USED_20260926_L4-P_generate_GK.md`）——銅通道插損封頂域大小；本卡是熱、不是訊號。
  - L7-P——每 FLOP 焦耳；本卡在設施層、不在晶片層。
  - ARCH_dead #1–#19 其餘：無以「散熱介質×設計密度」為機制者。
- §7-10 領域最近公開更新：Uptime Institute 2026 年度調查（2026-07-28）；DCK 密度上限報導（2026-08-28）；DLR 2026 Q2 法說（2026-07-23）。

## 1. 落差一句

能量守恆：機櫃電功率全數成為須排出之熱；空氣顯熱 `Q[BTU/h] = 1.08 × CFM × ΔT[°F]` 使每 kW 於 ΔT 20°F 需約 158 CFM，故風冷廳之可交付每櫃功率被介質封頂（實務約 40–50 kW/櫃），而 AI 機櫃（GB200 NVL72 近 140 kW）在其上。市場與申報以「MW」為單一可替代單位計容量、續租價與 backlog；種子主張 MW 依散熱介質與設計密度分裂為**兩種不可互換之財貨**，錯價只在把舊風冷 MW 與液冷就緒 MW 以同一單價（或同一續租價差）讀。方向未定：可能是舊 MW 被高估（擱淺），也可能是市場已過度折價而稀缺使舊 MW 重定價上行。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [P] 守恆：熱流＝電功率；介質熱容封頂每櫃密度 |
| 量綱 | kW/櫃（功率／佔地）× 介質（空氣／液體）；不是 $/MW、不是 PUE、不是水量 |
| 兩側 | 供給側＝依年份／設計密度之已建 MW；需求側＝以 kW/櫃 規格下單之租戶。兩側皆以 MW 加總時，差異消失於總數 |
| 改造路徑 | 風冷→液冷改造約 US$2–3M/MW（GDCH，二手，單一來源）；後門換熱器為中間解。改造速度決定半衰期 |
| 重疊 | L2-A（建置成本）、L2-P#1（PUE）、C-P4（水）、L4-P（櫃內幾何）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；本輪未判可分離）

1. DLR 季度 supplemental／10-Q：續租量與現金 mark-to-market 依產品（0–1MW、>1MW）分列；**未見**依冷卻介質或設計密度分列。法說摘要：2026 Q2 續租 >US$261M、整體現金價差 >25%；0–1MW +5.2%、>1MW +66.7%；全年展望 9–11%。https://www.marketbeat.com/instant-alerts/digital-realty-trust-q2-earnings-call-highlights-2026-07-23/ ；8-K 附件 https://www.sec.gov/Archives/edgar/data/0001297996/000110465926047702/dlr-20260423xex99d1.htm（本輪未開）
2. EQIX：>100 IBX、>45 都會區支援直接液冷（2023-12-12）——以「站數」揭露，不是 MW 或租金分列。https://www.datacenterdynamics.com/en/news/equinix-to-roll-out-support-for-direct-to-chip-liquid-cooling-at-100-data-centers
3. Uptime Institute 2026 年度調查（2026-07-28）：平均 modal 密度緩升；回報峰值 ≥30 kW 之營運商增加；舊基礎設施拖慢全域進展。無平均值。https://itweb.africa/article/uptime-institute-16th-annual-2026-global-data-center-survey-deployment-of-high-density-racks-rising-fast-operators-face-continued-recruiting-and-retention-pressures/Kjlyr7wBr1evk6am
4. 物理錨：DCF（2022-07-01）`BTU = CFM × 1.08 × ΔT`；ΔT 20°F 時 158 CFM/kW。https://datacenterfrontier.com/understanding-the-physics-of-airflow-in-high-density-environments ；DCK（2026-08-28）引 Uptime：約 50 kW/櫃以上風冷不實際。https://www.datacenterknowledge.com/ai-data-centers/ai-rack-density-s-real-limits-power-cooling-failure-risk
5. 擱淺敘事（二手）：GDCH 2026-06-12，風冷約 40 kW/櫃封頂、NVL72 近 140 kW、改造 US$2–3M/MW、未列反方。https://www.globaldatacenterhub.com/p/heat-is-the-new-bottleneck-why-ai

缺段（§7-2）：任一上市主體以冷卻介質或設計 kW/櫃分列 MW、租金或續租價差。失敗歸因＝本輪未讀 10-K／supplemental 原文，不是「分列不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 稀缺壓過介質：>1MW 續租現金價差 +66.7%，舊 MW 正被上調重定價 | DLR 2026 Q2 法說（2026-07-23） | 「舊風冷 MW 擱淺」方向與觀測相反；錯價若存在須反向陳述 |
| R2 | 多數企業與推論負載仍風冷，典型高密 AI 櫃約 12 kW | Joseph Wolff（eRacks）於 DCK 2026-08-28 | 封頂只綁訓練級櫃，需求側未必分裂 |
| R3 | 租約結構與租戶信用遮蔽過時風險；冷殼可轉用 | William Scott（CSC）、Doug Rowlands（Invesco），Investment Magazine 2025-11-04 | 損益層看不到介質效應 |
| R4 | 改造成本相對續租價差小，封頂可在 <12 個月內拆除 | GDCH 2026-06-12 改造成本 | 半衰期短於重定價窗（§1 ≥12 個月） |
| R5 | 液冷支援已以站數公開（EQIX >100 IBX） | DCD 2023-12-12 | 若已公開且已定價，非落差 |

## 5. SCOUT 裁決

**生成 L2-P#2 並留。** 不進 T。下一動作＝ANALYST 測一。

否決觸發（寫給 ANALYST，逐條實讀）：
1. 實讀 DLR、EQIX（及任一其他上市資料中心主體）最近 10-K／10-Q／supplemental 後，MW、租金、續租價差、backlog 或減損**皆無**依冷卻介質或設計 kW/櫃之分列或可對應之揭露，只剩總 MW → 不可觀測。
2. 介質效應在可得分列中與 R1 方向相反且無密度差異（舊 MW 與新 MW 同步上調），即「不可互換」無價格痕跡。
3. 改造成本與工期證據顯示封頂可於 12 個月內以小於續租價差之成本拆除（R4）→ 窗不足。
4. 可運作對照只能寫成 PUE／濕球（L2-P#1）、水美元（C-P4）、每 MW 建置成本（L2-A）、許可（L2-I）或櫃內銅距（L4-P）→ 換格／重開已死，否決。
5. 僅剩物理式與二手敘事，無申報層載體。

複查觸發器（若日後殺）：任一美股上市資料中心主體於 10-K／10-Q／supplemental 首次依冷卻介質或設計 kW/櫃分列 MW、租金或續租價差，或就風冷設施認列過時減損。

## 6. 轉入個股層時必問（§7-4；本輪不答）
1. 財報科目：介質／密度分列落在哪一行（續租價差、減損、capex 改造）。
2. 可交易工具：哪一上市主體之舊風冷 MW 占比可估。
3. 半衰期：改造週期 vs ≥12 個月窗。
