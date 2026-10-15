# L12-P#3 生成卡｜監理與法制：守恆（出口管制下之 AI 伺服器實體質量平衡——出貨地 vs 落地可吸收容量 vs 轉運差額）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260922_L12-P_generate_GK.md；archive/drive/USED_20260922_L12-P_test1_GK.md；archive/work/20261008_L12-P#2_generate_CL.md；work/20261008_L12-P#2_test1_CL.md；query/RETRIG_2.md（R-26） | EMITS: work/20261015_L12-P#3_generate_CL.md -->
**日期：** 2026-10-15　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain，配額 6／6）　**格：** L12-P　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L9-I#3 本日測一不通過）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-08（L12-P#2、L12-A#2、L12-I#2、L3-A#2、L1-A#2）；同日依測一先後（QUEUE Q-0008 最早）取 L12-P。既有生成 2 份 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `export smuggling Malaysia diversion`，命中 0 筆；未使用。
- 比對（本卡須異型）：
  - **L12-P#1**（`archive/drive/USED_20260922_L12-P_generate_GK.md`；測一 `archive/drive/USED_20260922_L12-P_test1_GK.md`）：受測產品端物理暴露時長底板；死於證書庫不可加總、對不齊 TIC 營收。本卡不涉 TIC、不涉測試時長。
  - **L12-P#2**（`work/20261008_L12-P#2_test1_CL.md`）：監理機關審查流量 L＝λW；死於 (2) 機關端 FDA 日持平、(3) AI 歸因只剩 L9-P 型工時。本卡守恆量為**實體貨品**（伺服器／GPU 單位、MW），不涉審查佇列、不涉工時。
  - L4 系（RETRIG R-26：SMCI 系統 vs 授權收入分列）、C-I3′／N-01／N-02（L4 科目不分列）：本卡不靠產品線分列，靠**出貨地（ship-to）地理列**對照落地容量。
  - L12-A#2（著作權 N×s）、L12-I#2（IP 補償賣權）：法律責任型，非實體守恆。
  - ARCH_dead 無出口管制／轉運型死因。
- §7-10 領域最近公開：SMCI 10-K FY26 2026-08-31（含 2026-03-19 SDNY 起訴書段）；NVDA 10-Q 2Q FY27（期末 2026-07-26）；DOJ／Earthmade 起訴 2026-09-29（報導 2026-10-03）；Bloomberg／NST 2026-05-10（OBON／Thailand）；ISEAS Fulcrum 2026-07-02；馬來西亞戰略貿易許可 2025-07-14。下一檢查點＝NVDA 3Q FY27 10-Q（約 2026-11）、SMCI 1Q FY27 10-Q（約 2026-11）、BIS 東南亞許可規則或 Chip Security Act（位置驗證）立法進度。

## 1. 落差一句

出口管制下，運往東南亞之 AI 伺服器須滿足質量守恆：**出貨單位＝當地上電安裝＋在庫＋再出口（含轉運入中國）**。執法（SDNY 起訴 SMCI 前董事等三人、指控至少約 2.5B 美元 AI 技術經台灣→東南亞→中國；Earthmade 案經新加坡／馬來西亞）與規則（馬來西亞許可、BIS 以母公司總部認定中國實體）若關閉轉運腿，則**以東南亞出貨地計之需求中、無對應當地上電容量之部分**將由賣方營收消失，除非由合法管道（許可出口）替代。種子主張：市場以出貨地營收外推之東南亞 AI 需求，未扣除實體上無處吸收之轉運差額；**方向未定**：差額可能已小（2025-07 起許可收緊）或已由北美需求吸收（SMCI Asia 占比 FY25 25.0% → FY26 15.5%）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [P] 守恆：實體單位質量平衡；規則端＝BIS（EAR、總部歸屬指引）、DOJ／SDNY 執法、馬來西亞 MITI 許可、Chip Security Act（若立法：位置驗證） |
| 恆等（僅定義） | 出貨（單位或 GPU 數）＝當地安裝（MW × 單位／MW）＋Δ在庫＋再出口；轉運差額＝出貨 − 安裝 − Δ在庫 − 合法再出口 |
| 已讀事實 | SMCI 10-K FY26：「International net sales are based on the country to which the products were shipped」；Asia 6,063,327／5,494,147／2,912,570（千元，FY26／25／24），總額 39,063,072／21,972,042／14,989,251；2026-03-19 SDNY「unsealed an indictment of three individuals … including Yih-Shyan (Wally) Liaw … alleged conspiracy to commit export control violations」；公司非被告、收 grand jury subpoena 及 DOJ、BIS OEE、「foreign authorities requesting documents and information relating to certain other customers」。NVDA 10-Q 2Q FY27：地理列依「headquarters of direct customers」，「The end customer and shipping location may be different」；China（含 HK）7,880 vs H200 許可出貨「less than 1% of Data Center revenue」；「We have provided and will continue to provide assistance to authorities regarding attempted diversion」。NST／Bloomberg 2026-05-10：「at least US$2.5 billion in US AI technology was moved」，含「more than US$500 million shipped between Apr 2025 and mid-May 2025」；中介 OBON（曼谷）。Earthmade 案：「more than $176 mn from two Malaysia-based shipping companies」（2024）。馬來西亞 2025-07-14：美國原產高效能 AI 晶片之出口、轉運、過境須許可。 |
| 未證之連結 | 東南亞 AI 資料中心上電容量（MW）之可得時序與單位換算；NVDA 出貨地口徑（只給總部地）；起訴金額與賣方各期出貨之對應 |
| 量綱 | 出貨地營收（美元／期）÷ 當地上電容量換算之可吸收額（美元／期）；轉運差額 ÷ 賣方總營收（%） |
| 半衰期 | 執法事件（起訴、和解）不定期；BIS 規則年度級；季報地理列每季 |

## 3. B 端可觀測載體（只指名）

1. SMCI 10-K FY26 https://www.sec.gov/Archives/edgar/data/1375365/000137536526000022/smci-20260630.htm （出貨地地理列、起訴書段、subpoena 段）；10-Q 各期未讀。
2. NVDA 10-Q 2Q FY27 https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm ；10-K FY26 https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm （總部地地理列、diversion 風險段、H200 許可段）。
3. NST／Bloomberg 2026-05-10 https://www.nst.com.my/amp/business/corporate/2026/05/1436113/us-suspects-nvidia-chips-smuggled-alibaba-thailand
4. Earthmade／Lui 起訴報導 2026-10-03 https://beinsure.com/news/greg-lui-doj-charges-allege-300mn-nvidia-ai-server-smuggling/ （DOJ 新聞稿與起訴書原文未讀）
5. TrendForce 2025-07-15（馬來西亞許可；SMCI Johor 產能至 5,000 機櫃／月）https://www.trendforce.com/news/2025/07/15/news-malaysias-ai-chip-curbs-shake-server-supply-chains-may-hit-super-micro-and-taiwans-wiwynn/ ；TrendForce 2025-05-12（馬來西亞 4 月 GPU 進口）https://www.trendforce.com/news/2025/05/12/news-malaysias-april-nvidia-gpu-imports-hit-record-usd-2-74b-fueling-china-rerouting-fears/ （未讀）
6. ISEAS Fulcrum 2026-07-02 https://fulcrum.sg/article/commentaries/the-us-china-ai-chip-war-southeast-asias-compliance-dilemma/ （BIS 總部歸屬指引；無量）
7. 未讀：SDNY 起訴書原文（US v. Liaw et al.）；馬來西亞／泰國海關 HS 8471／8473 進口統計；台灣財政部對馬來西亞伺服器出口統計；東南亞 DC 容量（營運商申報、政府統計）；Dell／HPE 地理列；具名賣方量化。

缺段（§7-2）：東南亞上電容量之 MW 序列；本輪未讀；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | SMCI Asia 占比已由 25.0% 降至 15.5%，美國占 70.9%；差額縮小且已反映於公開財報 | 載體 1 | 已定價／量級 |
| R2 | NVDA 自述 diversion 報導「even when unsubstantiated and untrue」；地理列為總部地，非出貨地，質量平衡無法在 NVDA 層閉合 | 載體 2 | 不可觀測 |
| R3 | 起訴金額為多年累計之指控，未經判決；與單期營收不可對齊 | 載體 3、4 | 量綱 |
| R4 | 東南亞合法建置（Microsoft、Alibaba Cloud、Johor 園區）可吸收大部分出貨 | 載體 5 | 方向 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) ≥ 2 家上市伺服器／GPU 賣方（如 SMCI、NVDA、DELL、HPE）之 10-K／10-Q 無法提供東南亞（或其所在區）**出貨地**營收 ≥ 4 期序列；或
(2) 東南亞 AI 資料中心上電容量（MW 或可換算之單位）無公開可加總序列，質量平衡不可閉合（L12-P#1 型可觀測性死因）；或
(3) `[D]` 量級：可得最佳代理之轉運差額（起訴指控額或出貨 − 容量換算）< 賣方總營收 1%（以期間對齊後）；或
(4) 唯一可觀測量為不定期執法事件（起訴、和解），無週期性序列可作里程碑（L12-I#2 型潛伏）；或
(5) 公司或具名賣方已量化轉運占比或執法對營收之影響（已定價）；或
(6) 12 個月內無可觀測驅動：無新 BIS 東南亞規則、Chip Security Act 未進展、無新起訴或對公司之執法。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：出貨地 vs 總部地地理列、應收帳款集中度、在庫跌價、或有負債（DOJ／BIS）。2. 可交易工具：伺服器 OEM／GPU 賣方（不選）。3. 半衰期：季報地理列每季；執法事件不定期；規則年度級。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L12［P］格加「#3 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0051。不改 L12-P#1／#2、L12-A、L12-I、L4 系、C-I3′、N-01、N-02 結論。
