# L4-P#4 生成卡｜運算硬體系統：守恆（Clos 埠數守恆：交換器 ASIC 頻寬 C＝埠數 R × 每埠速率 s 為常數 → 層數 L＝⌈log 端點數／log(R/2)⌉ 為階梯函數，每 GPU 光模組數由 L 決定而非固定比）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260926_L4-P_generate_GK.md；archive/work/20261011_L4-P#2_generate_CL.md；archive/work/20261017_L4-P#3_generate_CL.md；work/20261011_L4-P#2_test1_CL.md；work/20261017_L4-P#3_test1_CL.md；work/20261017_L4-A#3_test1_CL.md；work/20261017_L4-I#3_test1_CL.md | EMITS: work/20261024_L4-P#4_generate_CL.md -->
**日期：** 2026-10-24　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L4-P　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。最後測試日最舊＝2026-10-17（L4-P／A／I、L5-P／A），同日取表序第一格 L4-P；非已殺、非刻意排除。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py transceiver optics "per GPU" radix fat-tree`（0 筆）與 `800G 1.6T switch network optical`（7 筆，皆 VR200 機架功率／峰值算力／牌價，與本機制無關）。**未採用**。
- 比對之舊檔與死因型態，本卡須異型：
  - L4-P#1（`archive/drive/USED_20260926_L4-P_generate_GK.md`）：SerDes 通道損耗封頂銅纜距離——決定**每條鏈路之介質**（銅／光）。本卡取介質為給定，主張**鏈路條數**由拓撲層數決定。
  - L4-P#2（`archive/work/20261011_L4-P#2_generate_CL.md`）：封裝供電 I²R → VPD。無供電。
  - L4-P#3（`archive/work/20261017_L4-P#3_generate_CL.md`；測一 (1) 觸發：取捨已被 TrendForce／SemiAnalysis 量化）：位元總量之需求端分配（`Σ U×C ≤ B×s`）。本卡非供給分配，是**單一叢集內之拓撲組合守恆**（每台交換器上行＝下行），量為整數階梯。
  - L4-A（系統 BOM 加總）：會計加總，非拓撲。L4-I#3（外部選項）、L4-A#3（權證）：物件不同。
  - L3-P#4（中介層面積）、L5-P（HBM 頻寬上界）、L2-P#2（散熱封頂每櫃功率）：物件不同。
  - ARCH_dead：N-02（CPO 營收未分列；本卡不主張 CPO 份額，CPO 僅改每條鏈路之封裝型態，不改條數）、N-01（機隊世代組成）、C-I3′（UL 型）。無「拓撲層數守恆」型。不併。
- §7-10 領域最近公開：Meta OCP 2026（DCD 2026-10-13，Flattened Planar Fabric 三層→二層、8 平面）；OpenAI／Microsoft／AMD／Broadcom／NVIDIA 論文 arXiv:2605.04333（2026-05-05）；Broadcom Tomahawk 6 量產出貨稿（2026-03-12）；Lumentum FY26 10-K（2026-08-17）；Arista 2Q26 10-Q（2026-08-05）。下一檢查點：Arista 3Q26（約 2026-11 初）、Coherent／Fabrinet／Credo 下一季申報、NVIDIA 3Q FY27（約 2026-11 下旬）。

## 1. 落差一句

交換器 ASIC 總頻寬固定（Tomahawk 6：「512 200G or 1024 100G SerDes on a single chip」），**埠數 R 與每埠速率 s 互為代價**；非阻塞折疊 Clos 之端點上限 ≈ 2(R/2)^L，故層數 L 為端點數之**階梯函數**，每 GPU 之光鏈路數約隨 L 線性（FS 2023 舉例：三層 1:6、二層 1:2.5）。**落差＝以「每 GPU 光模組固定比 × GPU 出貨」或「每計算單元模組數」外推之單位數，與拓撲扁平化（多平面、高 radix）可同時成立否**：OpenAI 等五方論文稱 8 個 100G 平面使 131,072 GPU 為二層，「for full bisection bandwidth we require 2/3 of the optics and 3/5 the number of switches compared to a 3-tier network」；Meta 2026-10 宣布三層→二層；而 Goldman Sachs（轉載 2026-05-22）以每計算單元 1.6T 等效模組 216（GB300 NVL72）→ 2.5k（Rubin Ultra NVL576）建模。**方向未定**：叢集跨越 (R/2)^L 門檻（百萬 GPU）則 L 上跳、比值上升；radix 倍增或多平面則 L 下降、比值下降；兩者之淨效果與落點（光模組商、交換器商、銅／AEC）為測一題目。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（埠／頻寬）：`R × s = C_ASIC`；非阻塞 Clos 每台交換器上行頻寬＝下行頻寬 → `N_max(L) = 2·(R/2)^L`；鏈路數／端點 ≈ `L`（每層邊界一條），光收發器／端點 ≈ `2L − 1`（端點至葉層若為銅則再減） |
| 量綱 | `R`［埠］×`s`［Gb/s／埠］＝`C`［Gb/s］；`N`［端點］；`L`［層，整數］；光模組／GPU［個／GPU］；1.6T 等效＝個 × s／1.6T。不以美元代條數 |
| 可見端 | Broadcom TH6 稿（512×200G、LightCounting「128K-XPU network using only two switch tiers」、Dell'Oro「fewer switch tiers and reduced optical complexity」）；arXiv:2605.04333（二層 131,072 GPU、2/3 光學、3/5 交換器）；Meta OCP 2026（三層→二層、8 平面）；GS 每計算單元模組數；Lumentum 10-K「cloud transceiver product lines which increased by more than 173% due to an increase in shipment volume, partially offset by lower average selling prices」 |
| 指名不可見端 | 各超大規模業者之叢集端點數與層數分布；多平面採用率；光模組商出貨之單位數（多只揭營收）；賣方模型之每 GPU 比是否隨 L 變動 |
| 主張 | 每 GPU 光模組數非常數，受 `L(N, R)` 階梯約束；若市場單位數外推未經此式校驗，扁平化（或叢集再擴）會使單位數與外推不一致 |
| 表達工具型態（只指名，不選券） | 美股上市光模組／元件商、交換器 ASIC 與系統商、銅纜／AEC 商普通股及上市選擇權。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| Broadcom TH6 量產出貨稿（2026-03-12） | https://investors.broadcom.com/news-releases/news-release-details/broadcom-now-shipping-worlds-first-1024-tbps-switch-production |
| OpenAI／MSFT／AMD／AVGO／NVDA 多平面論文（2026-05-05） | https://arxiv.org/pdf/2605.04333 |
| Meta OCP 2026 FPF（DCD 2026-10-13） | https://www.datacenterdynamics.com/en/news/meta-details-next-gen-ai-infra-custom-multi-terabit-switches-unified-fabrics/ |
| Goldman Sachs 光網路報告轉載（2026-05-22；每計算單元模組數） | https://techblog.comsoc.org/2026/05/22/goldman-sachs-report-optical-networking-is-the-next-mega-trend-in-ai-infrastructure/ |
| FS 層數與 GPU：模組比（2023-12-22，舊世代基準） | https://community.fs.com/article/analyzing-gpu-to-optical-module-ratios-and-demand-in-ai-networks.html |
| SemiAnalysis「Nvidia's Optical Boogeyman」（每 GPU 光模組比之具名估計） | https://newsletter.semianalysis.com/p/nvidias-optical-boogeyman-nvl72-infiniband |
| Lumentum FY26 10-K（雲端收發器出貨量 +173%） | https://www.sec.gov/Archives/edgar/data/1633978/000162828026057358/lite-20260627.htm |
| Arista 2Q26 10-Q（AI 網路敘述；`sec.py --grep` 測一以大小寫變體重試） | https://www.sec.gov/Archives/edgar/data/1596532/000159653226000175/anet-20260630.htm |
| Coherent、Fabrinet、Credo 最近 10-K／10-Q；LightCounting／Dell'Oro 單位數預測 | 測一以 `sec.py filings` 與 WebSearch 取得 |

不宣稱缺口已存在、不宣稱市場未校驗、不宣稱淨方向。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 扁平化之光學節省已由建造者本身量化公開（2/3 光學、3/5 交換器） | arXiv:2605.04333；LightCounting／Dell'Oro 於 TH6 稿 | 落差已揭露 |
| R2 | 多平面以 8 條 100G 取代 1 條 800G，**條數不降反升**（每 GPU 8 鏈路），故「層數降 → 模組降」不成立；1.6T 等效口徑下兩者可抵 | Meta FPF「eight 100G links to eight distinct switches」；arXiv 同篇 | 守恆式之方向不定，或量綱錯置（條數 vs 等效） |
| R3 | 單位成長主因為 scale-up 光學化（NVL576 等），scale-out 拓撲之效應相對可忽略 | GS「about 13x from scale-out to scale-up」 | 機制量級小 |
| R4 | 叢集規模擴張（≥ 百萬 XPU、跨園區）使 L 回升，扁平化只是一代之暫態 | Broadcom 稿「more than one million XPUs」 | 半衰期短於 12 個月窗或方向反轉 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) ≥ 1 位具名賣方或產業研究機構之光模組單位預測已明示以層數／radix／多平面校驗（非固定比），或光模組商法說已量化扁平化對其單位數之影響（R1 成立且及於單位預測）。
- (2) 在 1.6T 等效口徑下，多平面之「條數升、層數降」淨效果 ≤ 測一自定門檻（如每 GPU 等效模組變動 < 15%），使守恆式不產生可觀測差（R2）。
- (3) scale-out 光模組占光學可定址量之份額 < 測一自定門檻，或測一無法分離 scale-out 與 scale-up（R3）。
- (4) 叢集端點數分布、層數、多平面採用率三者中 ≥ 2 項無公開量級，使 `[D]` 無法對帳。
- (5) 本卡只能以 L4-P#1（介質距離）、L4-P#3（位元分配）、N-02（CPO 分列）或 L4-A（BOM 加總）重述（重疊判讀）。
- (6) 可交易主體之相關營收不分列（光模組商不揭 AI scale-out 單位或營收），使錯價主體不可指認（N-02 型表達層）。

複查觸發器（若日後殺）：光模組商揭露單位數或每 GPU 比；超大規模業者公布叢集層數／平面數；賣方公開以拓撲建模之單位預測；下一代 ASIC（≥ 204.8T）radix 規格發布。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：光模組商雲端／資料通訊營收、出貨量敘述與 ASP；交換器商 AI 網路營收；銅纜／AEC 商營收。
2. 可交易工具：美股上市光模組、元件、交換器、AEC 商普通股與選擇權；中國上市光模組商（中際旭創等）非本池可交易範圍。
3. 半衰期：交換器 ASIC 世代約 2 年；叢集架構以建案（年度）定。

## 7. 本輪寫入

本卡；QUEUE 新列（ANALYST 測一）；ARCH_matrix L4-P 格標「已生成 #4」；FUNNEL §3 未測格計數；`export/LEADS_算力收支.md` 追加 2 筆（Lumentum 10-K、arXiv:2605.04333）。不改 L4-P#1–#3、L4-A#1–#3、L4-I#1–#3、L3-P#1–#4、L5-P、L2-P#2、N-01、N-02、C-I3′。
