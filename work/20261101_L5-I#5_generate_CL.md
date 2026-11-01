# L5-I#5 生成卡｜儲存與 IO：誘因（訂閱式儲存之逆選擇：元件成本暴漲期，企業買方由「買斷（已漲價）」轉向「固定 $/TiB 之 STaaS 長約」並拉長期限、加大預留——供給者等於對買方賣出一張 NAND 成本買權）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；AIM_FUNNEL.md §2（ARCH_dead 摘）；archive/drive/USED_20260926_L5-I_generate_GK.md；archive/work/20261011_L5-I#2_generate_CL.md；archive/work/20261018_L5-I#3_generate_CL.md；archive/work/20261026_L5-I#4_generate_CL.md；work/20261026_L5-I#4_test1_CL.md；archive/work/20261031_L3-I#5_generate_CL.md；archive/work/20261015_L2-I#3_generate_CL.md | EMITS: work/20261101_L5-I#5_generate_CL.md -->
**日期：** 2026-11-01　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 0→1／6）　**格：** L5-I　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L5-P#5、L5-A#5、L12-A#5、L12-I#5 皆本日測一，Q-0143–0146 done）。最後測試日最舊＝2026-10-26（L5-I#4、L6-P#4、L6-A#4、L6-I#4、L13-A#4）；依表序取 **L5-I**；非已殺、非刻意排除。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py storage subscription Evergreen NAND`，回 2 筆（SRC_DEM_038／039 OpenAI 訂閱占比），**相關 0 筆**；載體全由 `sec.py` 與 WebSearch／WebFetch 原文取得。內部數字（§12）未取用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L5-I#1**（雲端出站費＝取用權；量綱失敗）：選擇者＝雲端業者對客戶之價目。本卡選擇者＝**企業買方**在「買斷 vs 固定費率訂閱」間之選擇；所需量為申報層連續量（RPO、訂閱 ARR、訂閱毛利、Evergreen//One 資本支出），非價目列名。
  - **L5-I#2**（NAND 供給者 JV 資本紀律；(1)(2) 觸發）：供給側擴產。本卡不主張擴產與否。
  - **L5-I#3**（記憶體長約誘因相容；(5)(6) 觸發）：**現貨跌破約價時買方違約／重議**，對手為記憶體原廠。本卡方向相反（現貨**上漲**時買方**行使**合約內嵌選擇權）、對手為陣列供給者、合約為消費式 STaaS。重疊（「固定價合約 vs 現貨」結構）列為否決 (6)。
  - **L5-I#4**（DDR4 經 CXL 再用；(5) 觸發：驅動為壽命錯配非價格）：本卡之價格連結須有一手原文（否決 (3)）；不以存量再用為機制。
  - **L5-A#3**（Everpure 權利金混合恆等）、**L5-A#5**（SBC 代扣稅）：同公司、不同型；本卡不以產品毛利混合或權利金為落差。
  - **L3-I#5／L2-I#3**（配給賽局重複下單／可取消訂單）：短缺期之訂單誇報。本卡物件為**不可取消** TCV（10-Q：「non-cancelable Total Contract Value」），不主張誇報。
  - **C-P1**（ARCH_dead #11，L5 checkpoint 需求歸因）：本卡不做需求歸因。
- §7-10 領域最近公開：Everpure 10-Q 2Q FY27（期末 2026-08-02）；Everpure 執行長致客戶信（2026-04-23，經 Akave 2026-05-28 轉述，未實讀原信）；NetApp 部落格 2026-01-20。下一檢查點＝Everpure 3Q FY27 財報與 10-Q（約 2026-11 下旬）、NetApp 2Q FY27 10-Q（約 2026-11 下旬）。

## 1. 落差一句

儲存陣列供給者之毛利慣以「元件成本 vs 產品售價」建模，訂閱收入視為穩定、低波動之年金。**種子主張：元件成本暴漲期（Everpure 10-Q：「The cost of our components increased significantly during fiscal 2026 and the first half of fiscal 2027」；「we raised our prices during the first half of fiscal year 2027」），若 Evergreen//One 等 STaaS 之 $/TiB 費率於長約內固定（供給者行銷原文：「flat $/TiB subscription model with no hidden fees or surprise price increases—even if market conditions or hardware costs change」），則買方之最適選擇為：由買斷轉向 STaaS、拉長期限、加大預留承諾。** 供給者等於在高點賣出一張「以已鎖定費率取得未來新增容量」之買權；其成本（為履約而部署之硬體）於期內以折舊與零件替換進入訂閱成本。落差＝若此逆選擇之量級足以使訂閱毛利於 TCV 期內落後下滑，則「訂閱＝穩定年金」之建模低估了元件成本之遞延傳導；反之，若合約允許期內調價、或新約費率已同步上調，則本卡不成立。

## 2. 機制型態

| 欄 | 內容 |
|---|---|
| 型態 | **[I] 誘因**：買方於「買斷（已漲價）vs 固定費率 STaaS」之選擇；選擇變數＝STaaS 占新購比 `σ`、合約期限 `τ`、預留／按需比 `ρ`；誘因式：`σ` 隨 `(P_capex 漲幅 − P_staas 漲幅)` 上升 |
| 選擇者 | 企業儲存買方（Everpure、NetApp Keystone、HPE GreenLake 客戶）；對手方＝陣列供給者 |
| 第一原理量 | 新約 TCV 與 RPO 增速 vs 產品營收增速；STaaS 部署資本支出；訂閱毛利；元件成本漲幅；STaaS 新約費率是否調整 |
| 判定量 `[D]` | `x = (高點期簽訂之 TCV 中硬體交付成本 × 元件成本漲幅) ÷ 該 TCV 期內訂閱毛利`；`Δσ`＝漲價期 RPO 增速 − 產品營收增速之變化（相對 FY26 前段） |
| 可拒絕事件 | 合約條款允許期內依元件成本調價；新約 $/TiB 與產品同幅上調；RPO／TCV 增速未相對加速；訂閱毛利未落後下滑 |
| 表達工具型態（只指名，不選券） | 美股可交易陣列／STaaS 供給者（Everpure、NetApp、HPE）。不選券 |
| 重疊 | L5-I#3（固定價合約結構）、L5-A#3（同公司毛利）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Everpure 10-Q 2Q FY27（acc 0001474432-26-000088）https://www.sec.gov/Archives/edgar/data/0001474432/000147443226000088/pstg-20260802.htm （sec.py 實讀 2026-11-01）：RPO「$4.1 billion」、「primarily includes non-cancelable Total Contract Value (TCV) sales for our storage-as-a-service offerings, including Evergreen//One」；RPO 年增「44%」（FY26 末 40%）；「approximately 42% of total RPO over the next 12 months」；Subscription ARR「$2,133,684」千、年增 20%；訂閱毛利 74%→73%（2Q），下滑歸因「higher part replacements cost, depreciation of assets supporting the growth of our Evergreen//One offering」；產品毛利下滑「primarily due to increase in component pricing」；「we raised our prices during the first half of fiscal year 2027」；資本支出「equipment supporting deployments of our Evergreen//One offering」。
2. Everpure 部落格「How Evergreen//One Storage Subscriptions Protect Your IT Budget from Tariffs and Price Spikes」（2025-04-17，修訂 2025-11-18）https://blog.everpuredata.com/perspectives/evergreen-one-subscriptions/ ：「committed not to increase prices on Evergreen//One services due to tariffs」；「flat $/TiB … even if market conditions or hardware costs change」；「long-term contracts and SLAs that lock in pricing」（行銷語，未附條款）。
3. Evergreen//One Product Guide（合約條款正本）https://www.everpuredata.com/legal/evergreen-one-product-guide.html ——本輪 WebFetch 權限逾時未讀（失敗歸因：PROVENANCE_REQUIRED；非不存在）；舊版 PDF 錨：https://www.purestorage.com/content/dam/pdf/en/legal/evergreen-one-product-guide-mar-18-2025-aug-17-2025.docx.pdf
4. Akave 2026-05-28（二手、利害方行銷）https://akave.com/blog/the-storage-squeeze-why-wasabi-backblaze-and-everpure-are-all-raising-prices-in-2026 ：轉述 Everpure 2026-04-23 致客戶信「customer prices have risen approximately 70% since the beginning of the year」；Wasabi Reserved Capacity「Existing RCS contracts continue at their prior rate through the original term」（同型：既有預留約維持舊價之直接例）。
5. NetApp 部落格 2026-01-20 https://www.netapp.com/blog/rising-nand-flash-costs-6-strategies-to-optimize-it-spend/ ：推 Keystone「eliminating the need to prepurchase storage during peak pricing cycles」（供給者主動以 STaaS 承接漲價期需求之原文）。
6. 待讀：Everpure 2026-04-23 致客戶信原文；Everpure 3Q FY27 10-Q／法說之 Evergreen//One TCV 與新約費率；NetApp 10-Q（Keystone）、HPE 10-Q（GreenLake 儲存）；具名賣方或媒體是否已以「STaaS 固定費率 × 元件成本」建模。

## 4. 競爭解釋（測一須逐條排除）

| # | 競爭解釋 | 若成立 |
|---|---|---|
| R1 | 合約允許期內依元件成本或「market conditions」調價，或費率只鎖至續約 | 無買權，本卡不成立 |
| R2 | 新約 $/TiB 已與產品同幅上調；只有既有約受保護 | 無新增選擇誘因；只剩既有存量之一次性遞延 |
| R3 | RPO 增速來自續約與 Portworx／雲端訂閱，非 Evergreen//One 新約 | `Δσ` 不可歸因 |
| R4 | 供給者以既有存貨／長約鎖價元件履約，硬體成本漲幅不傳導 | `x` 趨近 0 |
| R5 | 訂閱毛利下滑由軟體攤銷與人事解釋（10-Q 已並列） | 機制不可分離 |

## 5. 否決觸發（任一成立即不進 T；門檻本卡凍結）

(1) Product Guide 或 10-K／10-Q 原文明載 Evergreen//One 費率可於期內依元件成本、通膨或市場條件調整（R1）。
(2) 原文顯示 2026 漲價期之 Evergreen//One 新約 $/TiB 上調幅度 ≥ 產品漲幅之 70%（R2）。
(3) 漲價期（FY27 1H–2H）RPO 年增 − 產品營收年增，較 FY26 同期**未擴大 ≥ 10 個百分點**；或無一手原文將 STaaS 需求變化連結至元件漲價（R3）。
(4) `[D]` `x` < 10%：以 10-Q 之 Evergreen//One 部署資本支出 × 元件成本漲幅 ÷ 未來 12 個月訂閱毛利粗算，不足 10%（R4）。
(5) 訂閱毛利變動經管理層歸因主要為軟體攤銷／人事，零件替換與 Evergreen//One 折舊非主因，且 12 個月內無可檢驗事件（R5）。
(6) 測一所得之唯一可觀測量為「固定價合約 vs 現貨」之重議結果（L5-I#3 型），或產品毛利之元件成本（L5-A#3 型），而無 `σ`／`τ`／`ρ` 之選擇證據。

## 6. 不寫

不寫 H1／H5、不寫 T、不選券、不主張價值方向。邊界：不改 L5-I#1–#4、L5-A#1–#5、L5-P#1–#5、L3-I#5、L2-I#3、C-P1 已測或已殺結論。
