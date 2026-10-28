# L14-I#4 生成卡｜企業終端需求：誘因（AI 名義之牌價階梯＋續約鎖價：賣方以「已內含 AI」為由調升套件牌價，新價只在下次續約生效；買方有誘因於生效日前提前續約鎖舊價 → 簽約量前移、牌價增量按續約世代分 1–3 年滲入 ARPU，報表以「Copilot／E5／E7 加購」歸因 ARPU 成長）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261005_L14-I_generate_GK.md；archive/work/20261014_L14-I#2_generate_CL.md；archive/work/20261021_L14-I#3_generate_CL.md；work/20261021_L14-I#3_test1_CL.md；archive/work/20261022_L15-I#3_generate_CL.md；archive/work/20261028_L14-A#4_generate_CL.md | EMITS: work/20261028_L14-I#4_generate_CL.md -->
**日期：** 2026-10-28　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 0→1／6）　**格：** L14-I　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L14-A#4 測一 2026-10-28，Q-0122 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-21（L14-I#3、L15-P#3、L15-A#3）；依表序取第一 → **L14-I**，既有 #1–#3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `price increase`、`ARPU`、`Microsoft 365`，0 筆；未用。內部數字（§12）未取。
- 比對之舊檔與死因型態，本卡須異型：
  - **L14-I#1**（`archive/drive/USED_20261005_L14-I_generate_GK.md`）：人力節省是否回流採購預算。本卡不涉節省去向。
  - **L14-I#2**（`archive/work/20261014_L14-I#2_generate_CL.md`）：裁員理由措辭。本卡不涉人力。
  - **L14-I#3**（`work/20261021_L14-I#3_test1_CL.md`，否決 (6)：市集代理人費率使退抵 φ 上界 < 5%）：承諾退抵之採購路由。本卡無市集、無承諾退抵；選擇變數是**續約時點**（買方）與**牌價歸因口徑**（賣方）。
  - **L15-I#3**（`archive/work/20261022_L15-I#3_generate_CL.md`）：收購方對俘虜裝機基調價、不可終止多年約前置認列。本卡主體為在位套件商之**全面牌價階梯**，增量方向相反（多年約延後而非前置調價之認列），且主張之落差為「牌價 vs AI 加購」之 ARPU 歸因。
  - **L14-A#4**（AI 專項簽約滾存）、**L14-A#1–#3**、**L14-P#1–#4**（席次 ≤ 員工數、承諾池、人工處理量、PC 汰換）：不涉。
  - **C-A1**（ARCH_dead #6，AI 營收不可分列）：本卡不主張 AI 營收額，只主張 ARPU 成長之**牌價世代成分**可由公開牌價表與合約期 `[D]` 上下界化。**C-A2**、**C-I5**：不涉。
- §7-10 領域最近公開：MSFT 10-Q 1Q FY27（期 2026-09-30，申報 2026-10-28）；MSFT 4Q FY26 電話會議（2026-07-29）；MSFT 授權 FAQ（2026 M365 Packaging & Pricing Updates）。下一檢查點＝MSFT 2Q FY27（約 2027-01 下旬）。

## 1. 落差一句

市場把 Microsoft 365 商業雲之 ARPU 加速讀為企業 AI 付費意願（公司口徑：1Q FY27 10-Q「Microsoft 365 commercial cloud revenue increased 17% driven by higher revenue per user, reflecting continued upsell to premium seat offerings, including Microsoft 365 Copilot, E5, and E7」，席次 +5%）；種子主張：2026-07-01 生效之全面牌價階梯（以 Copilot Chat 等「AI 進展」為由；M365 E3 $36→$39、O365 E3 $23→$26、F1 $2.25→$3、F3 $8→$10、Business Basic $6→$7、Business Standard $12.50→$14）**只在下次續約生效**，買方因而有誘因於 6-30 前提前續約鎖舊價（IDC 公開建議），致 (a) 簽約量前移至 4Q FY26（「Commercial bookings grew 18% when excluding … OpenAI, driven by strong execution in our core annuity sales motions」），(b) 牌價增量依 1–3 年續約世代逐季滲入 ARPU，於 FY27–FY29 呈現為平滑之「ARPU 成長」，而公司歸因句只列 Copilot／E5／E7 加購、不列牌價。可拒絕之主張＝`[D]` 牌價世代成分占 ARPU 成長之比例不可忽略且未被具名賣方拆出。本卡不主張任何主體營收或股價方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因（I）**：買方於生效日 τ 前之續約選擇：提前續約成本＝提前之現金時間價值與鎖定期內之彈性損失；收益＝ΔP × 席次 × 鎖定期剩餘年數。賣方之歸因選擇：把 ARPU 增量歸於 AI 加購（敘事）而非牌價（可比性）。ARPU 成長 ≈ \(g_{mix} + \sum_c w_c \cdot \Delta P_c/P_c \cdot r_{c,t}\)（\(w_c\)＝SKU 席次權重，\(r_{c,t}\)＝至 t 已續約世代占比，受提前續約壓低） |
| 選擇者 | 企業買方之採購（續約時點、SKU 降階、席次縮減）；賣方管理層（牌價、套件內含、MD&A 歸因句） |
| 可見端 | 牌價表與生效規則（授權 FAQ）；MD&A ARPU 歸因句與席次成長；商業 bookings 增速與「expiry base」敘述；未賺收入 roll-forward；同業先例（Google Workspace 2025-03-17 起續約生效之 Gemini 名義調價；Salesforce 2025-08-01 均價 +6%，理由未提 AI） |
| 指名不可見端 | 各 SKU 席次權重 \(w_c\)、EA 續約日分佈、提前續約量、實際折扣後淨價變動 |
| 量綱 | 百分點（ARPU 成長之成分）；\(r_{c,t}\) 無因次；不寫金額 |
| 外部參照物（測一查證） | Microsoft 2022-03-01 前次 M365 商業調價（E3 $32→$36）後之 Office 365 商業 ARPU 序列及當時歸因句；Google Workspace 2025 調價後之 Google Cloud 敘述 |
| 表達工具型態（只指名，不選券） | 美股、以席次套件為主之在位生產力軟體商普通股；不選券 |
| 重疊 | L15-I#3（俘虜基調價）、C-A1（AI 營收不可分列）；本卡只用牌價、續約世代與歸因句 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. MSFT 10-Q 1Q FY27（sec.py 全文 grep）https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm ：上引 ARPU 歸因句；「Microsoft 365 commercial seats grew 5% driven by installed base expansion … primarily small and medium business and frontline worker offerings」；「Commercial remaining performance obligation increased 73% to $677 billion」；全文 `ARPU` 0 筆、`price increase` 0 筆（`price` 45 筆皆為公允價值／移轉訂價／風險因子語境）。
2. Microsoft 授權 FAQ https://www.microsoft.com/en-us/licensing/news/2026-M365-Packaging-Pricing-Updates-FAQ ：「Pricing updates will be effective July 1, 2026」；理由「major advancements in AI (ex. Copilot Chat, Copilot Chat Analytics)」；「Customers on existing multi-year agreements will continue at their current pricing until renewal」；6-30 前續約可鎖舊價至下次續約。
3. IDC 2025-12-11 https://www.idc.com/resource-center/blog/microsoft-365-price-increase-announcement-december-2025/ ：SKU 牌價表（上引）；「Customers may consider renewing their current agreement early, prior to 1st July 2026, to maximize price protection」；未給營收影響。
4. MSFT 4Q FY26 電話會議（Motley Fool 轉錄，二手）https://www.fool.com/earnings/call-transcripts/2026/08/07/microsoft-msft-q4-2026-earnings-call-transcript/ ：bookings 句（上引）；「Premium offerings, including Copilot, E5, and early traction in E7 drove ARPU growth」；「we expect to see acceleration in M365 Commercial cloud revenue growth through this fiscal year」；全文未見「early renewal」，商用牌價調整未被列為成長驅動（僅消費者雲「lapped the benefit from last year's price increase」）。
5. 同業：Google Workspace https://9to5google.com/2025/01/15/google-workspace-price-increase-2025/ （Business Standard 年約 $12→$14，「no sooner than March 17, 2025」，年約於下次續約生效，「With Gemini now included」）；Salesforce https://www.salesforce.com/uk/news/stories/pricing-update-2025/ （2025-08-01 Enterprise／Unlimited 均價 +6%，理由「innovation and customer value」，未提 AI）。
6. CIO Dive 2025-12-05 https://ciodive.com/news/microsoft-365-ai-tools-higher-price/807189 ：IDC 分析師具名評論，無營收量化。

缺段（§7-2）：未取 MSFT 官方電話會議逐字稿（4Q FY26、1Q FY27）；未取具名賣方對 2026-07 調價之營收／ARPU 量化（Barchart／MarketBeat 頁抓取為空，失敗歸因＝頁面無內容回傳）；未取 EA 續約日分佈或提前續約量之任何一手；未查 2022-03 調價後之歸因句。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 賣方已以牌價調整建模 M365 ARPU（調價公告時即量化） | 待測一（具名賣方報告／新聞轉述） | 已定價 |
| R2 | E5／Copilot／E7 加購為真實 AI 付費，牌價成分小；大型 EA 客戶折扣抵銷牌價 | MSFT 4Q FY26「Premium offerings … drove ARPU growth」 | 量級不足 |
| R3 | 席次增長集中於低 ARPU 之 SMB／一線員工 SKU，恰為漲幅最大者（F1 +33%、F3 +25%），牌價效果已被管理層之「mitigated … by lower ARPU new seat adds」語句吸收 | §3-4 | 無方向性結論 |
| R4 | 牌價階梯屬一次性水準調整，市場以年增率讀即自動於 3 年後消失；無資訊落差 | 一般性 | 已知機制 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後 MSFT 申報或官方逐字稿已明文把 2026-07 牌價列為 M365 商業雲 ARPU／營收成長之驅動並給量級（公司已拆）；或
(2) `[D]` 以牌價表、合理 SKU 權重區間與 1–3 年續約世代，牌價成分於 FY27 任一季 < ARPU 成長之 15%（或 < 1.5 個百分點），量級不足；或
(3) 具名賣方、評等機構或公司原文已以牌價世代拆分 M365 ARPU（已定價）；或
(4) 可運作對照只能寫成：俘虜基調價前置認列（L15-I#3）、AI 營收額不可分列（C-A1）、承諾退抵路由（L14-I#3）、席次 ≤ 員工數（L14-P#1）或 AI 專項簽約滾存（L14-A#4）；或
(5) 12 個月內無檢驗事件（MSFT 2Q／3Q／4Q FY27 申報與電話會議、FY27 10-K 約 2027-07）；或
(6) 4Q FY26 bookings／未賺收入或 1Q FY27 未賺收入 roll-forward 顯示無提前續約痕跡（4Q FY26 商業 bookings 增速與「expiry base」敘述可由 expiry 結構完整解釋，且公司原文否認提前續約）。

複查觸發器（若日後殺）：MSFT 或同業於 MD&A 首次以「pricing」列 ARPU 驅動；新一輪套件牌價以 AI 名義公告；同業（Google、Salesforce、Adobe、Atlassian）揭露調價後續約世代或淨價實現。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：分部營收（M365 商業雲）、席次成長、未賺收入、商業 RPO。2. 可交易工具：在位套件商普通股（不選）。3. 半衰期：續約世代 1–3 年；揭露頻率每季。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0123；`query/ARCH_matrix.md` L14［I］加「#4 已生成」；`AIM_FUNNEL.md` §3 句與日期行；`export/LEADS_算力收支.md` 3 列（MSFT 1Q FY27 商業 RPO、Microsoft Cloud 營收、Azure 增速）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L14-I#1–#3、L14-A#1–#4、L14-P#1–#4、L15-I#3、C-A1、C-A2、C-I5 結論；不恢復 L11-P／L8-P／L9-P；不寫 T。
