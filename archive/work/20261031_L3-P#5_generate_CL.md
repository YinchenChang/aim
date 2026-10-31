# L3-P#5 生成卡｜半導體製造測試：守恆（老化測試熱能守恆：每腔可移除熱量 Q_ch 為上界，AI 加速器老化之有效顆數產能 ＝ min(插槽數, Q_ch ÷ P_dev) × 稼動時數 ÷ t_BI——「系統台數／插槽數」不等於老化顆數產能）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/INDEX.json；archive/drive/USED_20260926_L3-P_generate_GK.md（經 L3-P#4 §0 摘）；archive/work/20261009_L3-P#2_generate_CL.md；archive/work/20261016_L3-P#3_generate_CL.md；archive/work/20261024_L3-P#4_generate_CL.md；work/20261024_L3-P#4_test1_CL.md；archive/work/20261016_L3-I#3_generate_CL.md（標題） | EMITS: work/20261031_L3-P#5_generate_CL.md -->
**日期：** 2026-10-31　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 2→3／6）　**格：** L3-P　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L1-I#5 已於本日測一）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-24（L3-P#4、L3-A#4、L3-I#4、L4-P#4）→ 依表序取 **L3-P**；既有生成 4 份 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `burn-in`／`Aehr`／`system-level test`，命中 0 筆。內部數字（§12）：未取用。
- 比對（本卡須異型）：
  - **L3-P#1**（GK）：曝光機**機時守恆**；死於可觀測性。本卡守恆量為**熱量（kW）**，約束在老化腔散熱與供電，非前段機時。
  - **L3-P#2**：HBM 堆疊**良率乘積**；方向已揭露／定價。本卡良率只作輸入（早夭率決定是否需老化），不作落差。
  - **L3-P#3**：探針卡**觸壓壽命**（耗材流量）。本卡為資本設備之**熱容量上界**，非耗材；WLBI 之 WaferPak 只作載體。
  - **L3-P#4**：中介層**面積幾何**；死於 (2) 已定價（每片顆數公開層已逐點引用）。本卡不談晶圓面積。
  - **L3-I#3**：測試機「指定者≠付款者」誘因型；本卡不談誰出資本支出。
  - **公開層已存在之相鄰敘事（反方）：** Wing VC 2026-05「The Chip Testing Bottleneck」已以 ATE **機時**（每顆 20+ 分鐘 vs 手機 SoC 30–60 秒）量化「order-of-magnitude shift in machine-hours per shipped unit」，並稱 Advantest／Teradyne 為 chokepoint。本卡須與之區分：機時敘事以**時間**為約束、以 ATE 為主體；本卡以**功率×時間（熱量）**為約束、以**老化腔**（封裝級與晶圓級）為主體——若測一發現兩者在公開層已被同一模型合併，觸發否決 (2)。
  - ARCH_dead：C-I3′／N-02（利益未分列）——本卡否決 (1) 同屬可分離性題；主體與機制不同，非已殺同型。
- §7-10 領域最近公開：Aehr 10-K FY26（2026-07-27 申報，期末 2026-05-29）；Aehr 新聞稿 2026-08-12；Semiconductor Engineering 2026-09-10；Electronic Design（Advantest 撰）2026-08-28；Teradyne 10-Q 3Q26（2026-10-30）；Cohu 10-Q 3Q26（2026-10-29）。Aehr FQ1'27 10-Q（期末約 2026-08-28）**未見於 sec.py filings 最新列**（最新 10-Q＝2026-04-08）——下一檢查點。

## 1. 落差一句

老化（burn-in）產能在公開層以「**系統台數、插槽數、訂單美元**」流通（Aehr：FOX-XP 每台 9 片 300 mm 晶圓同測；Sonoma 標準型每腔 88 顆；backlog 2026-05-29 為 8,060 萬美元 vs 前年 1,520 萬美元），但每腔可移除之熱量 `Q_ch` 為硬上界：有效同測顆數 ＝ `min(n_slot, Q_ch ÷ P_stress)`，年產出顆數 ＝ 有效同測顆數 × `8760·U ÷ t_BI`。AI 加速器之老化應力功率 `P_stress` 由 700 W 級→1,000 W→「1600 W 以上」（Aehr 10-K）乃至「multi-kilowatt」（Advantest 撰文），而 `t_BI` 為「minutes to hours」（Aehr 10-K）、SLT「30 分鐘至兩小時以上」（Electronic Design）。種子主張：**若 P_stress × t_BI（每顆熱量）之成長快於腔熱容量之成長，則以台數或插槽外推之老化顆數產能被高估，老化設備需求（以 kW·h 計）高於以顆數成長外推之量**；反之若客戶縮短 `t_BI`、改以晶圓級低應力或機櫃級現場老化替代，則需求低於外推。**方向未定**：對老化設備商可正可負；對以顆計之加速器出貨，若老化成約束則為產出上限之一。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [P] 守恆：能量守恆（腔內供入電能 ＝ 移除熱量；`Σ P_stress ≤ Q_ch`）；與時間相乘得每顆熱量 `E_dev ＝ P_stress × t_BI` |
| 選擇者 | GPU／ASIC 設計方（是否老化、應力電壓／溫度、`t_BI`、晶圓級 vs 封裝級）；OSAT／代工（腔數、液冷與廠務電力）；老化設備商（每腔 kW、液冷架構） |
| 已讀事實 | Aehr 10-K FY26（sec.py 實讀）：「Lower power devices being tested up to 20-50 watts per device are placed on BIBs」；Sonoma「devices that can reach levels of power as high as 1600 or more watts … supports up to 88 devices with independent test resources per chamber」；「thermal control is liquid cooled」；「burn-in times can range anywhere from minutes to hours or even days」；FOX-XP「can test and burn-in up to 18 wafers at a time」；全晶圓接觸產品線占營收約 63%／66%／98%（FY26／25／24）；backlog 8,060 萬美元（2026-05-29）vs 1,520 萬美元。Aehr 新聞稿 2026-08-12：領先 AI 處理器客戶 2,200 萬美元追加訂單，「Each FOX-XP system is configured to test and burn in nine 300 mm wafers simultaneously」，出貨至台灣量產夥伴。Wing VC 2026-05：加速器「draw 700–1,200W」、測試成本占 ASP 由 <2% 往 5–7%（未附出處）。Semiconductor Engineering 2026-09-10：「At these power levels, the test hardware becomes part of the experiment」；接觸電阻不均→EOS。Electronic Design 2026-08-28（Advantest VP 撰，利害方）：「approaching multi-kilowatt operating envelopes」；SLT「30 minutes to more than two hours per device」；假例 100 萬顆 × 45 分鐘需 > 100 個平行測站。Teradyne 10-Q 3Q26（sec.py）：SLT 併入 Semiconductor Test 分部，全文無「burn」字樣。Cohu 10-Q 3Q26（sec.py）：無「burn」「thermal」「watt」字樣 |
| 未證之連結 | 每腔 kW 之實值（Sonoma 88 顆 × 1600 W ≈ 141 kW 為上限推算 `[D]`，非申報值）；AI 加速器實際老化應力功率與 `t_BI`；老化是否為 AI 加速器之全量篩選或抽樣；機櫃級現場老化（hyperscaler 端）是否替代封裝級；市場共識是否以台數／插槽外推（具名賣方模型原文） |
| 量綱 | 顆／年 ＝ min(n_slot, Q_ch／P_stress) × 8760·U ／ t_BI；需求 kW·h ＝ 顆數 × P_stress × t_BI；設備需求（腔數）＝ kW·h ÷ (Q_ch × 8760·U) |
| 半衰期 | 季到年（加速器世代 12–18 個月；腔交期約一至兩季，Aehr 稱六個月內出貨） |

## 3. B 端可觀測載體（只指名）

1. Aehr 10-K FY26 https://www.sec.gov/Archives/edgar/data/1040470/000165495426006919/aehr_10k.htm ；10-Q FQ3'26 https://www.sec.gov/Archives/edgar/data/1040470/000165495426003348/aehr_10q.htm ；FQ1'27 10-Q（未見）
2. Aehr 新聞稿 https://www.aehr.com/2026/08/aehr-receives-22-million-follow-on-order-for-ai-processor-wafer-level-burn-in-systems/ ；2025-08 hyperscaler 封裝級訂單 https://www.aehr.com/2025/08/major-hyperscaler-expands-ai-processor-production-capacity-with-additional-aehr-test-package-level-test-and-burn-in-systems/
3. 產業評論：https://wing.vc/content/the-chip-testing-bottleneck ；https://semiengineering.com/validation-gets-tested-at-1kw/ ；https://www.electronicdesign.com/technologies/test-measurement/article/55401601/advantest-system-level-test-for-next-gen-ai-and-hpc-devices
4. Teradyne 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/97210/000119312526441091/ter-20260927.htm ；Cohu 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/21535/000143774926033843/cohu20260926_10q.htm
5. 未讀：Advantest（6857.T／ADR）SLT 與老化分列；KES Systems、AEM Holdings（新加坡）老化產品；TestConX 2026 keynote PDF；NVIDIA／AMD 10-Q 之測試或老化敘述；Aehr 電話會原文之 AI 客戶每腔功率或 `t_BI`；具名賣方以 kW 或插槽建模之原文。

## 4. 不寫

H1／H5、表達工具選擇、方向判斷。

## 5. 否決觸發（測一逐條實讀）

1. **可分離性：** 任一上市主體（Aehr、Advantest、Teradyne、Cohu、AEM、NVIDIA、AMD）之申報、電話會或具名來源均無法給出每腔 kW、AI 加速器老化應力功率或 `t_BI` 之任二者 → 否決（C-I3′／N-02 型）。
2. **已被定價／已揭露：** 具名賣方或公司已以熱量（kW·h、每腔功率）或「功率 × 時間」量化 AI 老化需求；或 Wing VC 型 ATE 機時敘事已將老化熱容量納入同一模型 → 否決（無錯價）。
3. **熱不綁定：** 腔散熱上限高於 `n_slot × P_stress`（插槽數而非熱量為綁定約束），或 AI 加速器老化之 `t_BI` < 15 分鐘使熱量項可忽略 → 否決。
4. **替代路徑：** 12 個月內主要 AI 加速器改以機櫃級現場老化或省略封裝級老化（具名一手證據） → 否決（落差翻向且窗 < 12 個月）。
5. **方向抵銷：** 晶圓級老化（低應力功率、多晶粒同測）之擴張抵銷封裝級每顆熱量上升，使 kW·h 需求與顆數同步 → 不否決但標方向分歧。
6. **主體錯置：** 落差主要落於非上市主體（KES）或非美股（Advantest 東證、AEM 新加坡）而美股可交易對應僅小型股（流動性） → 標表達約束（§7-4 三題），不在生成階段否決。
