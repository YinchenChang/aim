# L4-P#3 生成卡｜運算硬體系統：守恆（HBM 位元守恆：Σ 加速器出貨 × 每顆 HBM 容量 ≤ HBM 位元供給 → 單位數與每顆容量互為代價）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260926_L4-P_generate_GK.md；archive/drive/USED_20260926_L4-P_test1_GK.md；archive/work/20261011_L4-P#2_generate_CL.md；work/20261011_L4-P#2_test1_CL.md；work/20261009_L3-P#2_test1_CL.md；work/20261016_L3-P#3_test1_CL.md | EMITS: work/20261017_L4-P#3_generate_CL.md -->
**日期：** 2026-10-17　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L4-P　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。最後測試日最舊＝2026-10-11（L4-P／A／I、L5-P／A／I、L6-P／A／I、L13-A），同日取表序第一格 L4-P；非已殺、非刻意排除。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py HBM "bit shipment" "HBM content" accelerator units`，命中 19 筆，皆為各世代 HBM 容量／頻寬規格（SRC_HW_020–070，多為「模型內建知識」）與 MS 機櫃 BOM 二手；**未採用**為證據，僅提示測一須回 NVIDIA／AMD 產品頁實讀每顆容量。
- 比對之舊檔與死因型態，本卡須異型：
  - L4-P#1（`archive/drive/USED_20260926_L4-P_generate_GK.md`）：SerDes 通道損耗封頂銅纜距離（訊號物理）。本卡無距離、無互連。
  - L4-P#2（`archive/work/20261011_L4-P#2_generate_CL.md`）：封裝供電 I²R → VPD（電流守恆）。本卡無供電。
  - L3-P#2（`work/20261009_L3-P#2_test1_CL.md`）：HBM 堆疊良率 → 每好位元晶圓投入（供給端製造）。本卡取**位元供給為給定**，主張其在**需求端之分配守恆**（單位數 × 每顆容量），不涉晶圓投入比。
  - L3-P#3（探針卡觸壓）、L5-P（decode 吞吐上界 BW／V_byte，頻寬非容量）、L5-I#2（NAND 資本配置）：物件不同。
  - ARCH_dead：N-01（機隊世代組成非科目）、N-02（CPO 分列）、C-I3′（UL 型）、C-P1（checkpoint）。無「位元分配守恆」型。不併。
- §7-10 領域最近公開：Micron FY26 10-K（2026-10-09）；Micron FQ4'26 法說（2026-09-30）；NVIDIA 2Q FY27 10-Q（2026-08-26）；TrendForce 2026-08-04 新聞稿。下一檢查點＝NVIDIA 3Q FY27 10-Q／法說（約 2026-11 下旬）；SK hynix 3Q26 業績（約 2026-10 下旬）；Rubin Ultra HBM 規格定案。

## 1. 落差一句

HBM 位元在短窗內近乎固定（TrendForce 2026-08-04：「HBM bit shipments are projected to grow by 50–60% YoY in 2027」且仍落後需求；Micron FQ4'26：已就「the vast majority of its calendar 2027 HBM bit supply」完成協議），故 **Σ_i 出貨_i × GB_i ≤ 位元供給 × 分配份額** 是硬約束。**落差＝每顆容量上修與出貨顆數上修無法同時成立**：若市場（加速器商指引、賣方顆數模型）同時採用世代容量躍升（如每封裝 HBM 由 288 GB 級升至 TB 級）與顆數高成長，兩者之乘積可超出位元供給，必有一方讓步——TrendForce 已報導 NVIDIA 評估將 Rubin Ultra 由 12-Hi HBM4e 降為 8-Hi 或 HBM4，並稱「the number of DRAM stack layers determines the trade-off between HBM capacity per GPU」與出貨量。**方向未定**：讓步可落在每顆容量（性能／定價權）、顆數（營收）、或加速器商以承諾鎖定較大份額（NVIDIA 10-Q 供應承諾 119B → 279B，「primarily memory」）而由他家加速器（ASIC、AMD）承擔缺口。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（位元總量分配）：`Σ_i U_i × C_i ≤ B × s`（`U` 顆數、`C` 每顆 GB、`B` 產業 HBM 位元供給、`s` 分配份額，`s` 由長約／承諾決定） |
| 量綱 | `U`［顆／年］×`C`［GB／顆］＝［GB／年］；`B`［GB／年］由記憶體廠位元成長率 × 基期推得；不以美元代位元 |
| 可見端 | TrendForce 2027 HBM 位元 +50–60%、Rubin Ultra 降配評估；Micron 10-K「HBM3E 12-high represented the majority of our HBM shipments」「HBM4 36GB 12-high」「HBM4 48GB 16-high」樣品；Micron 法說 2027 位元多數已簽、FY27–28「much tighter」；NVIDIA 10-Q「increasing supply commitments from $119 billion last quarter to $279 billion … primarily memory」 |
| 指名不可見端 | 各加速器商之 HBM 位元分配份額 `s_i`；賣方顆數模型是否以位元守恆校驗；加速器商顆數本身（NVIDIA 不揭顆數）；HBM 位元基期之絕對量（僅成長率公開） |
| 主張 | 顆數 × 每顆容量受位元守恆約束；市場對兩者之上修若未經此式校驗即可能不一致，且缺口之落點（容量／顆數／他家）決定受影響之主體 |
| 表達工具型態（只指名，不選券） | 美股上市加速器商與記憶體廠普通股及上市選擇權。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| TrendForce 新聞稿（2026-08-04，Rubin Ultra 降配、2027 位元 +50–60%） | https://trendforce.com/presscenter/news/20260804-13166.html ；轉載 https://iconnect007.com/article/151071/dram-supply-to-remain-tight-in-2027-prompting-nvidia-to-lower-hbm-configurations-for-rubin-ultra/151068/pcb |
| Micron FY26 10-K（HBM 產品組成、HBM4 規格） | https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm |
| Micron FQ4'26 法說摘要（2027 HBM 位元多數已簽、供給受限） | https://www.marketbeat.com/instant-alerts/transcript-micron-technology-q4-earnings-call-highlights-2026-09-30/ |
| NVIDIA 2Q FY27 10-Q（供應承諾 119B → 279B，「primarily memory」） | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm |
| NVIDIA／AMD 產品規格頁（每顆 HBM 容量；測一實讀） | 測一以 WebSearch 取得原頁 |
| SK hynix IR（3Q26 業績；HBM 位元成長與 2027 協議；韓國申報，非 SEC） | 測一以 WebSearch 取得 |

不宣稱缺口已存在、不宣稱市場未校驗、不宣稱讓步落點。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 守恆已被具名公開：容量 vs 出貨之取捨與降配評估已由 TrendForce 發布 | TrendForce 2026-08-04 | 落差已揭露 |
| R2 | 位元基期與分配份額不可得，守恆式無法對帳（量綱成立而量級不可觀測） | 記憶體廠只揭成長率；NVIDIA 不揭顆數 | 不可證偽 |
| R3 | 長約與 279B 承諾已鎖定主要加速器商之位元，缺口只落在邊際買方，對主要主體無錯價 | NVIDIA 10-Q；Micron 法說 | 錯價主體非流動上市 |
| R4 | 每顆容量可由 LPDDR／CXL 等替代記憶體分擔（容量非剛性），守恆不硬 | 測一查證（如 Vera CPU LPDDR5X、MS BOM） | 約束鬆 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) ≥ 1 位具名賣方或產業研究機構已以「位元供給 ÷ 每顆容量」校驗加速器顆數，或加速器商／記憶體廠法說已明言此取捨（R1 成立且有量化）。
- (2) 位元供給基期、分配份額或加速器顆數三者中 ≥ 2 項無公開量級，使 `Σ U × C` 與 `B × s` 無法在 `[D]` 層對帳（R2）。
- (3) 主要加速器商之 2027 位元已由長約／承諾鎖定且公開，缺口只落在非上市或非本池可交易主體（R3）。
- (4) 每顆容量之替代（LPDDR、CXL、降配）使約束在 12 個月窗內不綁定（R4）。
- (5) 本卡只能以 L3-P#2（每好位元晶圓投入）、L5-P（頻寬上界）、N-01（機隊組成）或 L4-I#2（表外承諾）重述（重疊判讀）。
- (6) `[D]` 量級：測一自定並寫明門檻（如以公開成長率推得之「顆數成長 × 每顆容量成長」對「位元成長」之超額比），低於門檻即否決。

複查觸發器（若日後殺）：記憶體廠揭露 HBM 位元絕對量或分客戶份額；加速器商揭露顆數或 HBM 承諾分列；Rubin Ultra／MI 系列 HBM 規格定案與原計畫相異；賣方公開位元守恆校驗模型。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：加速器商供應承諾（10-Q Note）、毛利率中記憶體成本；記憶體廠 HBM 營收（多不分列）與位元成長敘述。
2. 可交易工具：美股上市加速器商、記憶體廠普通股與選擇權；SK hynix、Samsung 為韓國上市，非本池可交易範圍。
3. 半衰期：年度（記憶體長約以曆年簽訂；加速器世代約年度）。

## 7. 本輪寫入

本卡；QUEUE 新列（ANALYST 測一）；ARCH_matrix L4-P 格標「已生成 #3」；FUNNEL §3 未測格計數。不改 L4-P#1／#2、L4-A#1／#2、L4-I#1／#2、L3-P#1–#3、L5-P、N-01、N-02、C-I3′。
