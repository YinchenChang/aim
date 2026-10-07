<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1PsNSkEHuldFtcV13l-etxUODxHhMwW_E；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h | EMITS: （本檔；Drive work/ 上傳後填 fileId） -->
# L4-P 測一｜B 端實讀（CEI／機櫃幾何對帳；禁 CPO 營收列）

**角色：** ANALYST@GK　**日期：** 2026-09-26　**格：** L4-P（運算硬體系統：SerDes 通道損耗封頂銅纜可達距離）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先通道規格之距離／IL 預算與機櫃幾何能否對帳。**禁止只重讀 CPO 營收列與路線圖一句。** 不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T。
**原陳述（生成卡 `1PsNSkEHuldFtcV13l-etxUODxHhMwW_E`）：** 被動銅通道可達距離由 SerDes 插入損耗在 Nyquist 的預算封頂；CEI-LR 目標距離已由 3 m→2 m→1 m 單調縮。機櫃／跨櫃幾何一旦大於該距離，域必須切段、加 retimer／ACC／AEC，或改光。錯價只在把「域可以任意加大」或「光學進入 scale-up＝一般 TAM」當成與距離無關的敘事。
**守恆（生成用）：** `R_cu(f_N, IL_budget) < D_domain ⇒ 域不能由被動銅單層覆蓋`。本輪不估參數、不寫 H1。
**否決觸發（生成卡寫給本輪）：** (1) 對 OIF／IEEE／機櫃公開機械圖實讀後，`R_cu` 與 `D_domain` 皆無法形成可對帳區間，只剩 SKU 名稱與論壇一句；或 (2) 可運作對照只能寫成 CPO／光學營收分列（滑回 N-02）；或 (3) 公開層已出現穩定可拒絕之「域半徑 ≤ 銅可達」或「域放大不觸發介質切換」。
**領域最近公開（§7-10）：** OIF CEI-224G Framework（2022-02-07）；OIF CEI Rolling Deck（檔案約 2026-03）；OIF OFC 2026 CEI-448G（2026-03-17／框架 2025-11-04）；Ethernet Alliance／OIF TEF（2025-12-02–03）；Molex 448G 通道分析（頁面 2026-09-23）；NVIDIA NVLink 文（2026-07-20）；FY26 10-K（期 2026-01-25）；Lenovo GB300-NVL72 機械規格；Ciena／HI2026 轉述（2026-08-20）。下一官方檢查點＝OIF 448G-LR 目標距離定稿，或任一加速器／交換／連接器主體 10-K／10-Q 首次把 scale-up 域內銅／光分列且可與 CEI／IEEE 距離對帳。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260926_L4-P_generate_GK.md` `1PsNSkEHuldFtcV13l-etxUODxHhMwW_E`（10725 B，2026-09-26T09:27:28Z）；`20260923_HEALTH_CL.md` `1_urT6I7RovcM73D3IBTKGIk6RY1z9nC0`；`20260923_HEALTH_GK.md` `1byQGbjCmIT1orLv51moyAH5xnABFO95e`
- query/：`ARCH_dead.md` `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`；`ARCH_matrix.md` `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`；`CHARTER_HIST.md` `1DKg3HUr-zOWw20OmNe1aDpWT_izDwdiT`；`INDEX.json` `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`；`MECH.md` `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-09-26T09:23:25Z role SCOUT）
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-09-24；§1 無 L4；§3 L4［P］＝已生成）
- matrix L4［P］＝已生成。INDEX `L4` 指向 matrix，無獨立 L4-P 測一 fileId
- 本輪上傳前 work/ 無同名 `20260926_L4-P_test1_GK.md`
- 生成卡所列 Converge Digest 長鏈本輪 404；改以同文短鏈實讀（見 URL）。此為鏈位漂移，不把舊鏈不命中寫成「HI2026 不存在」。

---

## 終態

**不通過。不進 T。** 機制（插入損耗預算封頂被動銅距離；距離隨 Nyquist 上升而縮）未被否證。失敗在可對帳性——CEI-LR **目標距離**有世代表至 224G（448G-LR＝TBD）；NVL72 機櫃包絡有 OEM 毫米數；兩端不在同一官方表、NVLink 通道公尺不在 10-K、主動銅把牆鐘從被動目標拉開。可見端已被 SKU 名稱＋訪談「72／144＝銅維、1152＝跨櫃光」用盡。

| 測試項 | 結果 |
|---|---|
| B 端已實讀（非指名；非只讀 CPO 營收／路線圖一句） | **通過**　OIF Framework／Rolling Deck／OFC 2026／TEF；Molex；Lenovo 機械圖；NVLink 文；FY26 10-K Networking 段；Shainer 訪談；Ciena ACC 轉述 |
| `R_cu` 可寫成官方距離區間 | **部分**　CEI-56G-LR＝3 m／112G-LR＝2 m／224G-LR＝1 m（Framework＋TEF 同表）；448G-LR＝**TBD**；IL 224G＝40 dB @ 56 GHz bump（Rolling Deck 演示），448G IL＝TBD |
| `D_domain` 可寫成公開機櫃區間 | **部分**　GB300-NVL72 機櫃 600×1,068×2,236 mm（Lenovo）；地板對角 ≈1.225 m；高度 2.236 m。**無**跨櫃／NVL144／NVL576／NVL1152 官方機械圖本輪對帳 |
| `R_cu` × `D_domain` 同表對帳（可拒絕「域任意放大」） | **不通過**　標準目標 ≠ NVLink 實測可達；SKU 文無公尺 |
| 域內銅鏈／光鏈為申報科目 | **不通過**　FY26 10-K Networking 一桶（NVLink＋IB＋Ethernet＋cable solutions incl. optical modules）；無 CPO 列（N-02 死因仍在） |
| 穩定可拒絕之「域半徑 ≤ 銅可達」 | **不存在**　訪談質性句不是可拒絕區間 |
| 否決觸發 (1) | **觸發**　可對帳的是「標準目標表」與「單機櫃包絡」各自動；乘積無官方分母 |
| 否決觸發 (2) | **未觸發**　本輪拒絕把對照寫成 CPO 營收分列 |
| 否決觸發 (3) | **未觸發**　無穩定可拒絕數值界 |
| 升格 T | **否** |

失效歸因（§7-2）：不是檢索失敗。失敗在量綱——所需量（具名域 SKU 之被動銅可運作公尺 × 可對帳機櫃／跨櫃幾何）不是所讀之量（CEI 目標距離、OEM 單機櫃毫米、Networking 合計營收）。現況檔名＝上列 work／query。複查觸發器＝生成卡原文（見下）。停。

本格不入 §1。不改正本（對齊屬 SCOUT）。

---

## 已實讀載體

### A. OIF CEI 距離／IL（第一因子 `R_cu`）

**OIF-FD-CEI-224G-01.0（2022-02-07）Table 1 歷史 CEI-LR：**
- CEI-25G-LR＝5 m 銅纜；CEI-56G-LR＝3 m；CEI-112G-LR＝2 m；CEI-224G-LR＝**1 m**。
- IL：25G＝25 dB @ 12.5 GHz；56G＝30 dB @ 14 GHz；112G＝28 dB @ 28 GHz；**224G＝TBD**（當時）。

**OIF CEI Rolling Deck（實讀 PDF；224G 專案頁）：**
- CEI-224G-LR＝Backplane or Passive Copper Cable；**1000 mm host and daughter cards**；**2 connectors**；FEC 允許 1e-15。
- 同頁演示句把 LR 寫成 Passive **／ Active** Copper Cable；die-to-die **40 dB @ 56 GHz**、通道損耗「over 25 dB」。主動銅已在標準演示矩陣內，不是後加敘事。
- CEI-448G：Deck 開頭「Initiated two new OIF CEI-448G projects in Q1 2026」——本 Deck **無** 448G-LR 凍結距離。

**OIF OFC 2026 CEI-448G（2026-03-17；引用框架 OIF-FD-CEI-448G-01.0，2025-11-04）：**
- 句：「AI Scale-up is Dominated by Copper」。
- 世代表：CEI-224G-LR＝PAM4、40 dB @ 56 GHz（Bump）、1 m copper cable；**CEI-448G-LR＝TBD／TBD／TBD**（調變、IL、距離皆 TBD）。
- 應用桶：PCBA to PCBA across a chassis **~1 m**＝LR（Electrical or Optical）。
- 能效／可達表另列 Passive Copper **~1.5 m**。此為應用／能效桶，**不是**已凍結之 448G-LR 目標。
- Retimer／redriver／optical「when longer distances … within or between racks」。

**Ethernet Alliance／OIF TEF Panel 2（2025-12-02–03）：**
- 同歷史表：56G-LR 3 m／112G-LR 2 m／224G-LR 1 m／**448G-LR TBD**。
- 原文：「Achieving comparable reach to 224G at 448G is exceptionally challenging」。
- 投影：LR distance 1000 mm；425 Gbps PAM4 模擬 1200 mm cable IL < 40 dB——模擬，不是定稿。

**Molex 448G 通道分析（頁面日 2026-09-23）：**
- 448G PAM-6 需約 90 GHz、PAM-8 約 75 GHz 通道頻寬；~80 GHz 非線性滾降截斷。
- 已合格之 224G-PAM4 通道**不保證** 448G PAM-6／8。CPC 相對 PCB 降損、拉長可達，但連接器成為頻寬瓶頸。
- **無**公尺數目標；不能代替 CEI-LR 表。

結論：`R_cu` 作為 **CEI-LR 目標距離**可寫到 224G（單調 3→2→1 m）。跨到 448G 與跨到 NVLink 實測可達＝未凍結。R3 成立。

### B. 機櫃幾何（第二因子 `D_domain`）

**Lenovo GB300-NVL72 機械規格（官方 OEM）：**
- Rack solution：**Width 600 mm；Depth 1,068 mm**（延伸框至 1,200 mm）；**Height 2,236 mm**。
- 地板對角 √(0.600²+1.068²) ≈ **1.225 m**。高度 **2.236 m**。
- 此為單機櫃包絡，不是「域半徑」科目，也不是跨櫃間距。

**NVIDIA Technical Blog（2026-07-20）：**
- Vera Rubin NVL72：NVLink 6＝3.6 TB/s／GPU、機櫃 260 TB/s、72-GPU 域。
- 路線圖域至 **1152 GPU**「with future co-packaged optics」。
- 「NVLink Switch trays and NVLink spine of 5,000 cables」——**文內無銅纜公尺數。**

對帳試算（明示＝不可當官方乘積）：若把 CEI-224G-LR 目標 1.0 m 對 Lenovo 高度 2.236 m，高度 > 目標；對地板對角 1.225 m，對角 ≈ 目標上沿。中置交換托盤是工程上把路徑壓回銅可達的設計選擇（Register／OCP 敘事），**不是** 10-K 可拒絕區間。NVL144／576／1152 本輪無對等機械圖，跨櫃 `D_domain` 寫不成區間。

### C. 申報層（拒滑回 N-02）

**NVIDIA FY26 10-K**（`nvda-20260125.htm`，期 2026-01-25）：
- Networking offerings＝NVLink interconnects and switches ＋ InfiniBand／Ethernet 平台（adapters、cables、DPUs、switch chips and systems）。
- cable solutions「including optical modules」＝產品菜單一句，**不是** scale-up 域內銅／光分列。
- 本輪檢索：**無** CPO／co-packaged 列、**無** NVLink 公尺、**無** 域 SKU 介質表。
- FY26 Networking 營收 US$31,376M（Compute US$162,361M）＝平台桶。把此桶讀成「距離閘門後的光學 TAM」＝N-02 已死表達點。本輪不採用。

R1 成立於申報層。觸發 (2) 未走：對照沒有改寫成 CPO 營收。

### D. 訪談／ACC（明示非申報；只核反方）

**Shainer／SDxCentral（GTC 2026 訪談）：**
- 「If you can use copper, use copper。」
- NVL72／144「fits copper dimensions」；1152「beyond copper… multiple racks」→ CPO。
- 「If you continue to increase speeds, then the copper reach will go shorter。」
- **無公尺。** 此即 R4 的可見端：賣方已把 72／144 標成銅維、1152 標成光學域。質性句，不是可拒絕數值界。觸發 (3) 未走。

**Ciena／Hot Interconnects 2026 轉述（Converge Digest 2026-08-20；生成卡長鏈 404，本輪改短鏈）：**
- Nitro 2004 線性 redriver：200G／lane ACC；演示把約 **1 m DAC 級通道**延到約 **3 m**，目標約 **4 m**；~1.5 pJ/bit；非全重定時。
- 定位＝被動 DAC 與光學 scale-up 之間的橋。R2 在供應商演示層成立：牆鐘距離可被主動銅移動。不是 CEI-LR 目標，不是 10-K。

---

## 對種子與反方

| 主張 | B 端讀後 |
|---|---|
| 守恆可寫（IL 預算封頂被動銅距離） | 可寫。CEI-LR 目標至 224G 單調縮；448G-LR 未凍結 |
| 錯價＝把域放大當成與距離無關 | 可見端已被 SKU 名稱＋「銅維／光維」訪談用盡。錯價句無官方公尺對照錨 |
| R1 公尺不在科目 | **成立** |
| R2 ACC／AEC 移動被動牆 | **在演示／訪談層成立**；Rolling Deck 已把 Active Copper 寫進 LR 演示 |
| R3 448G-LR 距離 TBD，「單調縮」跨代外推 | **成立** |
| R4 72／144 銅、1152 光已被公開標定 | **在訪談層成立**；申報層連公尺都沒有 |
| R5 做成「買 CPO」＝滑回 N-02 | **遵守**　本輪未載入 CPO 營收列 |

`R_cu < D_domain` 的「當且僅當」在本輪兩邊沒有可同表的官方序列，故既不能接受也不能拒絕「域任意放大已被距離閘門定價」。

---

## 不開 T／§7-4

進 T 需數值窗與可拒絕之 H1 倍數。本輪可寫入的只有「CEI-LR 目標至 224G 為 1 m、448G-LR TBD、NVL72 機櫃包絡毫米存在、NVLink 公尺與域內介質不是科目」。不夠把距離上界寫成財富倍數窗。

§7-4 三題本輪不答（生成卡：轉入個股層時必問；本格不轉、不進 T）。題目本身已由本輪讀數預示方向（科目分不出銅／光、美股主體 Networking 過寬、448G 定稿或 ACC 拉過跨櫃會壓縮窗），但不在本輪作答。

**複查觸發器（沿用生成卡，不改寫）：** 任一美股可交易加速器、交換或連接器主體於 10-K／10-Q／20-F，分列 scale-up 域內銅鏈與光鏈（或等價：具名域 SKU 之介質與可對帳機櫃幾何），且可與同期 CEI／IEEE 距離目標對帳。

---

## URL

1. https://www.oiforum.com/wp-content/uploads/OIF-FD-CEI-224G-01.0.pdf
2. https://www.oiforum.com/wp-content/uploads/CEI-Rolling-Deck.pdf
3. https://www.oiforum.com/wp-content/uploads/60317a-OIF-OFC2026_CEI-448G_Fast-and-Furious-Signaling-Developments-1.pdf
4. https://ethernetalliance.org/wp-content/uploads/2025/12/OIF_TEF_Panel2_2512.pdf
5. https://www.molex.com/en-us/industries-applications/servers-storage/performance-analysis-of-various-modulation-techniques-over-448gbps-channels-in-data-centers
6. https://developer.nvidia.com/blog/nvidia-nvlink-the-scale-up-network-for-ai-factories/
7. https://pubs.lenovo.com/gb300-nvl72/server_specifications_mechanical
8. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
9. https://www.sdxcentral.com/news/nvidia-backs-copper-in-next-gen-interconnects-amid-push-into-co-packaged-optics/
10. https://convergedigest.com/hot-interconnects-ciena-bilal-riaz-cpo-448g-post-dac-ai-network/

**（完）**
