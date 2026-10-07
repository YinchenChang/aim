# L4-P 生成卡｜運算硬體系統：SerDes 通道損耗封頂銅纜可達距離
<!-- BY: SCOUT@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；1IIpN9tt1L4JP_ZstWVAV3ad3ntqTq_9c | EMITS: PENDING_UPLOAD -->
**日期：** 2026-09-26　**角色：** SCOUT@GK　**格：** L4-P　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 本輪只產生成卡。不測。不改正本狀態欄（FUNNEL §3／matrix L4［P］仍＝已生成）。不入 §1。

---

## 0. 本輪範圍

- 種子＝ARCH_3h §3.29 L4-P（`1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj`）：**機櫃內銅纜可達距離受 SerDes 通道損耗封頂 → scale-up 網域規模有距離型上界**。B 端載體（3h 僅指名、未實讀）：通道損耗規格；機櫃尺寸。
- 生成序註：3h 填格為 A→I→P。同層 L4-A（系統 BOM）、L4-I（開放機櫃／commoditize-the-complement）本輪不生成。上一 session 排隊本格；L3-I／L3-P 仍＝已生成、無本輪生成卡。
- 已死相鄰、機制不同、不得合併：
  - **N-02**（`ARCH_dead` #15）：不通過(a)，CPO 營收於上市主體未分列；複查＝同利益分列。種子是距離上界，不是光學營收佔比。
  - **C-I3′**（#14）：不通過(a)，UL 型／分部毛利由非機制項解釋。屬 L4-I 生態鎖定側。
  - **N-01**（#17）：機隊世代組成非科目。不是通道物理。
- 3h 重疊標「N-02（熱／電密度閘門）為另一獨立閘門，重疊度未判」。重疊不構成丟棄（3h 第 5 條）。
- CHARTER §7-3：不執行終端篩選。§7-4 三題只標「轉入個股層時必問」。§7-10：領域最近公開＝OIF CEI-448G／OFC 2026（2026-04）；OIF CEI Rolling Deck（約 2026-03）；NVIDIA NVLink 技術文（2026-07-20）；Hot Interconnects 2026／Shainer（2026-08）；Molex 448G 通道分析（2026-09-23）；GTC Taipei 2026 網路面板（頁面日含 2026-09-26）。下一官方檢查點＝OIF 448G-LR 目標距離定稿或任一加速器商 10-K／10-Q 首次把 scale-up 域內銅／光分列。

---

## 1. 落差一句（生成物 → 候選陳述）

市場把 scale-up 網域顆數讀成架構選擇（SKU 命名、交換器 radix、軟體域）。種子主張：被動銅通道的可達距離由 **SerDes 通道插入損耗在 Nyquist 的預算**封頂；每翻一倍每通道速率，OIF CEI-LR 的銅纜目標距離已由 3 m→2 m→1 m 單調縮。機櫃／跨櫃幾何一旦大於該距離，域必須切段、加 retimer／ACC／AEC，或改光。錯價只在把「域可以任意加大」或「光學進入 scale-up＝一般 TAM」當成與距離無關的敘事。N-02 已在「CPO 營收分列」上死於 (a)；本格 B 端不是那一列。

---

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆／純物理距離上界（通道損耗 vs 幾何；非會計恆等、非誘因） |
| 選擇者 | 通道標準起草者＋機櫃幾何（相對 L4-A 之 BOM 池、L4-I 之參考設計開放） |
| 可見端 | 域 SKU 名稱（NVL72／144／576／1152）、CPO／光學路線圖一句、交換器總頻寬 |
| 指名不可見端 | 被動銅在該代 SerDes 的可運作距離區間；該距離與機櫃對角線／跨櫃間距之差；域內銅鏈 vs 光鏈之公開拆分 |
| 主張 | 域半徑 > 銅可達距離 ⇒ 銅不能單獨覆蓋該域；光學／主動銅是距離閘門後的替代，不是平行的偏好 |
| 表達工具型態（只指名，不選券） | 已上市、美股可交易之加速器／交換／連接器主體；通道規格為公開標準／論壇。不選券 |
| 重疊 | N-02 光學利益分列；L4-A BOM；L4-I 系統營收比重；L5-P HBM 頻寬守恆。重疊不構成丟棄 |

守恆式（生成用，非正式載入）：

`R_cu(f_N, IL_budget) < D_domain  ⇒  域不能由被動銅單層覆蓋`。

`R_cu` 隨 `f_N` 上升而下降（CEI-LR 目標距離時序）。本輪不估參數、不寫 H1。

---

## 3. 已 fetch 之公開錨（URL；非完整 B 端實讀）

1. OIF CEI-224G Framework（2022-02-07）：CEI-LR 歷史目標距離 CEI-56G-LR＝3 m銅纜／CEI-112G-LR＝2 m／CEI-224G-LR＝1 m。插入損耗欄 224G 當時 TBD。https://www.oiforum.com/wp-content/uploads/OIF-FD-CEI-224G-01.0.pdf
2. OIF CEI Rolling Deck（檔案日約 2026-03）：CEI-224G-LR＝背板或被動銅纜；1000 mm host＋daughter、2 connectors；演示 die-to-die 約 40 dB @ 56 GHz。https://www.oiforum.com/wp-content/uploads/CEI-Rolling-Deck.pdf
3. OIF OFC 2026 CEI-448G（2026-04）：「AI Scale-up is Dominated by Copper」；CEI-448G-LR 目標距離 **TBD**；被動銅約 ~1.5 m、重定時可換距離但耗能。https://www.oiforum.com/wp-content/uploads/60317a-OIF-OFC2026_CEI-448G_Fast-and-Furious-Signaling-Developments-1.pdf
4. Ethernet Alliance／OIF TEF 面板（2025-12）：同表 448G-LR 距離 TBD；明文「Achieving comparable reach to 224G at 448G is exceptionally challenging」。https://ethernetalliance.org/wp-content/uploads/2025/12/OIF_TEF_Panel2_2512.pdf
5. Molex 448G 通道分析（頁面日 2026-09-23）：共封裝銅相對 PCB 降損；~80 GHz 附近非線性滾降截斷頻寬；既有 224G-PAM4 合格通道不保證 448G PAM-6／8。https://www.molex.com/en-us/industries-applications/servers-storage/performance-analysis-of-various-modulation-techniques-over-448gbps-channels-in-data-centers
6. NVIDIA Technical Blog（2026-07-20）：NVLink 6／Vera Rubin NVL72＝72 GPU、3.6 TB/s／GPU、機櫃 260 TB/s；路線圖域至 1152 GPU「with future co-packaged optics」。**文內無銅纜公尺數。** https://developer.nvidia.com/blog/nvidia-nvlink-the-scale-up-network-for-ai-factories/
7. GTC 2026 轉述＋Shainer（SDxCentral 2026-03-19）：「If you can use copper, use copper」；NVL72／144「fits copper dimensions」；1152「beyond copper… multiple racks」；速率升則銅可達距離縮。**訪談／二手，非 10-K 科目。** https://www.sdxcentral.com/news/nvidia-backs-copper-in-next-gen-interconnects-amid-push-into-co-packaged-optics/
8. Hot Interconnects 2026 轉述（2026-08-21）：Ciena ACC 把約 1 m DAC 級通道延伸到約 3–4 m（200G/lane 線性 redriver）；光學「move inward」進 scale-up。仍非申報距離科目。https://convergedigest.com/hot-interconnects-ciena-bilal-riaz-on-cpo-448g-and-the-post-dac-ai-network/
9. 供應鏈二手（DIGITIMES 2026-06-25）：Rubin Ultra NVL576 機櫃間 CPO；Feynman NVL1152 以 CPO 為跨櫃。**不是 10-K。** https://www.digitimes.com.tw/tech/dt/n/shwnws.asp?id=0000759844_08U9SAN53BG34P5NKUE88

以上為生成錨。**不宣稱 `R_cu` 已成可重算官方時序，不宣稱域內銅／光鏈已分列，不宣稱距離上界已被市場錯價。** 測試一之 B 端須實際 fetch 標準／規格書或可反解之機櫃幾何，禁止只疊路線圖一句與 N-02 已死的 CPO 營收列。

---

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | 距離上界是標準與訪談，不是損益科目；域 SKU 顆數可見，公尺數不可見 | NVLink 文無公尺；20-F／10-K 無「被動銅覆蓋半徑」列 | 測試一可能停在 (a)：所需量不是所讀之量（與 N-02 同型風險，量不同） |
| R2 | ACC／AEC／CPC／retiming 把牆鐘距離從 1 m 拉到數米，守恆在被動通道不在系統產出 | Ciena HI2026；Marvell 224G CPC 2.5 m 演示 | 上界被主動銅移動，落差不在「必須改光」 |
| R3 | 448G-LR 距離仍 TBD；「單調縮」在下一代尚未凍結，不能當已實現閘門 | OIF OFC 2026 表 | 主張的單調性停在 224G，跨代外推是敘事 |
| R4 | 賣方已公開把 1152 標成光學域、72／144 標成銅域；市場若已按尺寸定價，則無錯價 | Shainer；NVIDIA 文「future CPO」 | 機制真、價已反映，升格失敗在「未定價且可捕捉」 |
| R5 | 把本格做成「買光學／CPO」會滑回 N-02 已死的 (a) | `ARCH_dead` #15 | 表達點選錯＝換格，不是本格通過 |

種子仍可能在「CEI-LR（或等價 IEEE）目標距離 × 公開機櫃／跨櫃幾何，對齊已上市主體之域 SKU 世代」上寫成可重算對照。乘積是否存在、上界是否可拒絕「域任意放大」，是測試一的題。

---

## 5. SCOUT 裁決

**留。** 不進 T。下一動作＝ANALYST@GK 對本格做測試一（B 端須實際 fetch 並列 URL；優先通道規格之距離／IL 預算與機櫃幾何能否對帳，禁止只重讀 CPO 營收列與路線圖一句）。

理由（只到殺／留）：
- 守恆本身可陳述，與 L4-A／L4-I、已死 N-02／C-I3′／N-01 不同構成。
- 3h B 端未實讀；本輪只把指名載體寫成可派工之規格項。R1–R4 足夠強，預設風險＝公尺數不在科目、主動銅移動上界、448G 距離未凍結、市場已按尺寸定價；不是機制已被否證。
- 終端三題本階段不答（§7-3）。

否決觸發（寫給 ANALYST，不是本輪執行）：
- 對 OIF／IEEE／機櫃公開機械圖實讀後，`R_cu` 與 `D_domain` 皆無法形成可對帳區間，只剩 SKU 名稱與論壇一句；或
- 可運作對照只能寫成 CPO／光學營收分列（即滑回 N-02 已死表達點）；或
- 公開層已出現穩定可拒絕之「域半徑 ≤ 銅可達」或「域放大不觸發介質切換」，使距離上界與可見定價不可辨。

複查觸發器（若日後殺）：任一美股可交易加速器、交換或連接器主體於 10-K／10-Q／20-F，分列 scale-up 域內銅鏈與光鏈（或等價：具名域 SKU 之介質與可對帳機櫃幾何），且可與同期 CEI／IEEE 距離目標對帳。

---

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：域內銅／光或「距離閘門後的替代鏈」能否從 Networking／Compute 再拆；能否拒絕一般光模組／scale-out。
2. 可交易工具：恆等落在美股可交易揭露主體，而非僅私有連接器或無申報之機櫃 OEM。
3. 半衰期：448G-LR 目標距離一旦定稿或 ACC 把牆鐘拉過跨櫃間距，≥12 個月窗內上界是否被工程抵銷。

---

## 7. 本輪寫入／不寫入

寫入：本生成卡入 Drive `work/`（fileId 見標頭 EMITS，上傳後回填）。
不寫入：FUNNEL 正本 `1FcrhXNs53jWu_8fFlezc86uZvd3EqXI`（§3 L4 仍＝已生成；不入 §1）；matrix 正本 `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`；§2／§4／§5；INDEX.json；ARCH_dead。禁止新建同名正本。狀態欄對齊屬測試一之後 session。
