# L4-I#5 生成卡｜運算硬體系統：誘因（配貨稀缺作為搭售貨幣：加速器緊缺時，買方以接受同供應商 scale-out 網路／NIC 換取配貨優先；搭售品份額為主產品稀缺度之函數，緊缺解除即回歸）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260926_L4-I_generate_GK.md；archive/work/20261011_L4-I#2_generate_CL.md；archive/work/20261017_L4-I#3_generate_CL.md；archive/work/20261025_L4-I#4_generate_CL.md；archive/work/20261024_L4-P#4_generate_CL.md | EMITS: work/20261101_L4-I#5_generate_CL.md -->
**日期：** 2026-11-01　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L4-I　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L4-A#5 於 2026-10-31 已測一）。最後測試日最舊＝2026-10-25（L4-I#4、L5-P#4、L5-A#4、L12-A#4、L12-I#4 同日）；依表序取 **L4-I**；非已殺、非刻意排除。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py networking Spectrum-X InfiniBand attach`，命中 2 筆（SRC_HW_060 InfiniBand 單埠頻寬；SRC_DC_014 IREN 向 Dell 採購 GB300 含 InfiniBand 之總額）；皆非本卡機制之證據，未作引用，不回讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L4-I#1**（開放參考設計＝商品化互補品；死於系統比重不在申報層）：彼為加速器商**開放**互補品以壓整機商；本卡為加速器商以**稀缺配貨**把互補品（scale-out 網路）**綁入**，方向相反。
  - **L4-I#2**（回租承諾／擔保／權證代降價）：讓價形式；本卡不讓價，反以配貨權**收取**搭售品份額。
  - **L4-I#3**（外部選項＝自研加速器壓價上限）：本卡之外部選項為**同一買方之第三方網路**（商用 Ethernet 交換器／NIC），非加速器替代品；但 TPU／MI 系外部選項會降低稀缺度，屬本卡之解除路徑，重疊照記。
  - **L4-I#4**（買方延後選擇權）：時點選擇權；本卡為**品項綁定**。
  - **C-I3′**（生態鎖定；死於分部毛利由非機制項解釋）：彼為軟體／生態之**持久**鎖定；本卡主張**狀態依存**（隨配貨稀缺度變動）之搭售，可由稀缺解除而逆轉。最接近之重疊，ANALYST 以 (5) 判。
  - **N-02**（CPO 營收未分列）、**L4-P#4**（Clos 埠數守恆、每 GPU 收發器數）：物理／光學量；本卡看網路**供應商份額**之誘因來源。
  - **L4-A#3**（客戶權證收入減項）、**N-01**：構成不同。
- §7-10 領域最近公開：NVIDIA 10-Q 2Q FY27（期末 2026-07-26，申報 2026-08-26）；NVIDIA 10-K FY26（申報 2026-02-25）；Arista 2Q26 法說（2026-08-04）。下一檢查點＝Arista 3Q26（約 2026-11 上旬）、NVIDIA 3Q FY27（約 2026-11 下旬）。

## 1. 落差一句

NVIDIA 10-K FY26：「Revenue from Data Center networking grew 142% driven by the introduction and continued ramp of NVLink compute fabric for GB200 and GB300 systems and the growth of Ethernet and InfiniBand platforms」，同期 Data Center computing +59%；二手（Global Data Center Hub 2026-05-25）報 1Q FY27 networking 14.8B（+199% YoY）、compute 60.4B。而 2Q FY27 10-Q 與 8-K 新聞稿改以市場平台（Hyperscale 48,710／ACIE 40,313 百萬美元）呈現，`sec.py doc --grep "etworking"` 於 8-K 新聞稿 0 筆、10-Q 無 compute／networking 金額分列。另：DOJ 2024-08 調查（The Information 首報；Tom's Hardware 轉述）焦點為「forcing its customers to buy products in bundles」「pressured cloud service providers into purchasing multiple products together, such as A100 or H100 GPUs along with Mellanox-branded networking gear」及對採購 AMD／Intel 晶片者「higher prices on networking equipment」；歐盟 2024-12 問卷問「whether the contracts require them to buy networking equipment with GPU」。落差＝市場若把 networking 份額成長全數讀為產品優勢（持久），則其中**依存於加速器配貨稀缺之搭售部分**（稀缺解除、外部加速器選項變多或監理介入時可逆）之比例與時點可能被誤估；方向未定（亦可能搭售部分極小，或 NVLink 為技術必然而非搭售）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因（市場力移轉／tying）：主產品配貨稀缺 → 買方以接受互補品換配貨 → 互補品份額 `s_net = f(稀缺度 σ)`；非守恆、非會計恆等 |
| 量綱 | `s_net`（NVIDIA 於 AI scale-out 網路之份額，無量綱）；`net/DC`（網路 ÷ 資料中心營收，無量綱）；σ 以交期（週）或配貨比代理 |
| 須拆分 | NVLink scale-up（技術上屬機櫃不可分，非搭售）vs scale-out（InfiniBand／Spectrum-X 交換器、ConnectX／SuperNIC，可由第三方替代）——只後者適用本機制 |
| 可見端（實讀） | 10-K FY26 networking +142% vs computing +59%（原文上）；10-Q 2Q FY27 Data Center 89,023 百萬美元、市場平台新口徑；10-Q 風險因子：中國監理 2025-09-15 初步認定違反 Mellanox 併購承諾，可能導致「restrictions or other orders regarding our networking business」；Arista 2Q26：Etherlink AI fabrics「more than 100 cumulative customers」（MarketBeat 自動摘要） |
| 指名不可見端 | scale-out 網路與 NVLink 之營收拆分；買方別網路供應商組合；配貨與網路採購是否於合約掛鉤；DOJ／EU 程序現況 |
| 主張 | 稀缺期 `s_net` 之上升有一部分可由 σ 解釋，且於 σ 下降（GPU 交期縮短、MI4xx／TPU 外部供給增加）時以 1–4 季落後回落；`net/DC` 之歸因若不拆此部分即失真 |
| 外部參照物（測一查證） | 前例：搭售／配貨綁定之反壟斷前例（如歐盟 Microsoft／Google Android 搭售案之份額回落）；只作路徑先例 |
| 表達工具型態（只指名，不選券） | 美股上市加速器商、商用 Ethernet 交換器／NIC 商之普通股與上市選擇權。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| NVIDIA 10-K FY26（networking vs computing 成長原文） | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm |
| NVIDIA 10-Q 2Q FY27（市場平台新口徑、Mellanox 風險因子） | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm |
| NVIDIA 8-K 2Q FY27 新聞稿 | https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm |
| DOJ 調查報導（2024-08-02） | https://tomshardware.com/tech-industry/artificial-intelligence/us-doj-launches-nvidia-antitrust-investigation-investigating-potential-strong-arm-tactics-related-to-ai-gpu-supply |
| 歐盟搭售問卷報導（2024-12-06，Reuters 轉載） | https://www.business-standard.com/world-news/eu-probes-nvidia-over-potential-bundling-practices-in-ai-chip-market-124120601064_1.html |
| 1Q FY27 compute／networking 二手數字 | https://www.globaldatacenterhub.com/p/nvidia-posts-816-billion-quarter |
| Arista 2Q26 法說摘要 | https://www.marketbeat.com/instant-alerts/arista-networks-q2-earnings-call-highlights-2026-08-04/ |
| NVIDIA 2Q／3Q FY27 CFO commentary 與法說逐字稿；Arista、Broadcom、Celestica 10-Q；Dell'Oro／650 Group AI 後端網路份額；DOJ／EC／SAMR 程序文件 | 測一取得 |

不宣稱搭售部分已入或未入共識、不宣稱方向。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 網路份額來自技術整合（NVLink、Spectrum-X 擁塞控制、SuperNIC 協同），非配貨搭售；NVIDIA：「We support customer choice and compete on merit」 | EU 報導引 NVIDIA 聲明；10-K 歸因 NVLink | 機制不成立或可分離部分極小 |
| R2 | 最大買方（超大規模）普遍自選 Ethernet（Arista 100+ AI 客戶），搭售只及議價力弱之小買方 | Arista 法說 | 量級不足 |
| R3 | 賣方已以 attach rate 建模並討論隨供給正常化回落 | 測一查賣方 | 落差已揭露 |
| R4 | 本卡只是 C-I3′（生態鎖定）之重述 | ARCH_dead #14 | 型態重複 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) ≥ 1 位具名賣方或研究機構已將 NVIDIA scale-out 網路份額／attach 與 GPU 供給緊缺度連結並量化其回落（R3）。
- (2) 公開層無法分離 scale-out 網路（InfiniBand／Spectrum-X／NIC）與 NVLink，且 2Q FY27 起連 networking 總額亦不揭露，致 `s_net` 或 `net/DC` 無任何一手或具名二手代理（可觀測性）。
- (3) DOJ／EC 程序已結案且無任何搭售或配貨掛鉤之實證，且無買方原文（合約、法說、訴狀）指稱配貨與網路採購掛鉤（R1）。
- (4) `[D]` 量級：測一自定並凍結門檻（如 scale-out 網路 ÷ Data Center 營收 < 5%，或搭售可歸部分 ÷ 營業利益 < 2%），低於即否決（R2）。
- (5) 本卡只能以 C-I3′（持久生態鎖定）或 L4-I#3（外部選項）重述，無法區分狀態依存性（R4）。
- (6) 12 個月內無檢驗事件（GPU 交期顯著縮短、MI4xx／TPU 外售放量、DOJ／EC／SAMR 決定、NVIDIA 恢復或終止 networking 分列）。

複查觸發器（若日後殺）：NVIDIA 重新分列 scale-out 網路營收；任一監理機關公布搭售認定或承諾；超大規模買方原文指稱配貨與網路採購掛鉤；GPU 供給轉寬後首季 NVIDIA 網路份額變動之一手數字。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Data Center 營收（市場平台）、networking 分列（若恢復）、分部毛利；第三方 Ethernet 商之 AI 營收。
2. 可交易工具：美股上市加速器商與商用網路設備商普通股與上市選擇權（不選）。
3. 半衰期：數季（取決於配貨稀缺解除時點與監理時程）。

## 7. 本輪寫入

本卡；QUEUE 新列（ANALYST 測一）；ARCH_matrix L4［I］格標「#5 已生成」；FUNNEL §3 不變（仍無已生成未測以外之變動，見 QUEUE）；`export/LEADS_算力收支.md` 追加 2 列（NVIDIA 10-Q 2Q FY27 Data Center 營收、10-K FY26 networking 年增率）。不改 L4-I#1–#4、L4-A#1–#5、L4-P#1–#5、C-I3′、N-01、N-02。
