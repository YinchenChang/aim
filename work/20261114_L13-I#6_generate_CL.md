# L13-I#6 生成卡｜資本與融資結構：誘因（主權出資者之非財務報酬：海灣主權資本對美國資料中心權益之出價含「晶片取得」之影子價值 λ；2026-07-10 美國把 UAE 升入 Country Group A:5、改為免個別許可後，λ 之邊際部分消失——若主權為私有資料中心收購之邊際出價者，其要求報酬率回升即改變私有標的之清算價）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261002_L13-I_generate_GK.md；archive/work/20261013_L13-I#2_generate_CL.md；archive/work/20261020_L13-I#3_generate_CL.md；archive/work/20261028_L13-I#4_generate_CL.md；archive/work/20261104_L13-I#5_generate_CL.md；work/20261114_L13-P#6_test1_CL.md；work/20261114_L13-A#6_test1_CL.md；archive/work/20261110_L6-P#6_generate_CL.md；archive/work/20261102_L6-I#5_generate_CL.md | EMITS: work/20261114_L13-I#6_generate_CL.md -->
**日期：** 2026-11-14　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 4→5／6）　**格：** L13-I　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L13-P#6 本日測一，Q-0201 done）。非已殺／刻意排除格中最後測試日最舊＝2026-11-04（L13-I#5、L14-P#5、L14-A#5、L14-I#5、L15-P#5）；依表序取 **L13-I**。既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `sovereign MGX UAE`，2 筆（皆為 NVIDIA「MGX」機架命名，非本題），相關命中 0；未用。內部數字（§12）未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L13-I#1**（私有資訊 → 公開信評資訊含量）：不涉評等。
  - **L13-I#2**（擔保人兼股東之違約分支；死因＝終止費遮蔽）：不涉擔保。
  - **L13-I#3**（發行人依機構債務含量選工具）：選擇者非發行人。
  - **L13-I#4**（壽險買方之 RBC 資本計提；死因＝持有人結構不可得）：#4 之非報酬項為**監理資本**；本卡之非報酬項為**出口管制下之晶片取得**，出資者為主權投資體，資產為私有資料中心權益。
  - **L13-I#5**（非交易型載具之贖回閘門與顧問估值）：本卡不涉贖回、不涉 NAV 估值。
  - **L13-P#6**（ATM 實現容量）、**L13-A#6**（預募現金之利息收入）：不涉。
  - **L6-P#6**（管轄區合格容量分區守恆）、**L6-I#5**（買方自建／外購排序；否決 (4) 提及主權買方）：兩卡之主權為**算力需求方**；本卡之主權為**美國資產之資本供給方**，樞紐為其要求報酬率。
  - **C-A3／C-A4**（折舊樞紐／表達窗）：不以殘值、年限為樞紐；不重開。**L11-P／L8-P／L9-P**：不恢復。不寫 T-15。
- §7-10 領域最近公開：BIS 將 UAE 升入 A:5（2026-07-10，二手轉述）；Aligned 收購完成（2026-07-21，一手新聞稿）；US–UAE 會談重申 1.4 tn 承諾（2026-03-26，二手）；Semafor 2026-09-28「MGX looks for data center assets in the Asia-Pacific」（robots 拒讀，僅標題）。下一檢查點＝AIP 第二筆交易或募資進度、CFIUS／BIS 對 UAE 之後續、MGX／ADIA／Mubadala 美國資料中心新交易。

## 1. 落差一句

市場把海灣主權資本（MGX 直持 Aligned 35%、為 AIP 最大出資者；UAE 對美 1.4 tn／10 年承諾）對美國私有資料中心之出資讀成「長期、價格不敏感之耐心資本」，並以此支撐私有收購估值（Aligned EV 約 40 bn、6.4 GW）與上市資料中心股之私有市場參照；種子主張：此出資之目標函數含**非財務報酬** λ——對美投資是取得美國晶片出口許可之對價（Bloomberg 2025-10-09：「match its investment … on a dollar-for-dollar basis」；許可節奏「depend in part on how the UAE's specific investment plans unfold」）——故主權要求報酬率 \(r_s = r_{mkt} − λ/K\)。2026-07-10 UAE 升入 A:5、核准實體免個別許可後，λ 之**邊際**部分歸零（承諾仍在、但不再逐批換許可），主權之邊際出價應向 \(r_{mkt}\) 回升；若主權曾是私有資料中心收購之邊際出價者，此變化在私有交易之資本化率／EV 倍數與主權交易流量上可見，而市場仍以「耐心資本」外推。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因（I）**：主權出資者 s 對美國資產 i 之出價 \(P_i^s = CF_i / (r_{mkt} − g − λ_t/K_i)\)；λ_t＝每美元美國投資換得之出口許可影子價值。許可制下 λ_t > 0；A:5 免許可制下邊際 λ_t → 0（剩餘＝政治承諾之履約價值，非邊際） |
| 選擇者 | 主權投資體（MGX、Mubadala、ADIA；對照 Saudi PIF／Humain，未升 A:5）；其交易對手（私有資料中心賣方：基礎設施基金） |
| 驅動（因果層，§7-5） | 美國出口管制制度（個別許可 vs A:5／Supplement 8 核准實體）；雙邊投資對等條款；CFIUS 審查 |
| 量綱 | 要求報酬率／資本化率［%］；λ／K［%／年］；主權參與交易之 EV／EBITDA 或 EV／MW［x、$／MW］；主權參與份額［% 交易權益］ |
| 可見端 | 主權參與之美國資料中心交易（價值、持股比、日期）；BIS／Commerce 許可公告與國家分組變動；雙邊聯合聲明之投資承諾；上市資料中心 REIT 與私有交易之隱含倍數差；CFIUS 年報 |
| 指名不可見端 | 主權之內部門檻報酬率；許可與投資之逐筆對應（Commerce 官方稿只寫安全與申報條件）；AIP 其他出資人比例 |
| 外部參照物（測一查證） | 非財務目的主權出資改變私有資產清算價之具名一手前例（如 2000s 中東主權對歐美地標不動產、或日本 1980s 美國不動產之戰略性出價與其後回落）；自然對照：Saudi（未升 A:5、仍屬許可制）vs UAE（A:5）之 2026H2 美國交易流量 |
| 表達工具型態（只指名，不選券） | 上市資料中心 REIT／開發商普通股（以私有交易為估值參照者）；上市另類資管（GIP 母公司）；不選券 |
| 重疊 | L13-I#4（買方之非報酬約束，但約束型態與出資者皆異）；L6-P#6（主權需求側）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Aligned 新聞稿（2026-07-21）https://aligneddc.com/press-release/aip-mgx-and-blackrocks-gip-close-acquisition-of-aligned-data-centers/ ：「Aligned's enterprise value of approximately $40 billion」；「51 campuses and more than 6.4GW of operational and planned capacity」；AIP「initial target of mobilizing and deploying $30 billion of equity capital」；「an additional $5 billion of growth capital」。〔一手、利害方〕
2. Tiger Brokers 轉載 Deep News（2025-12-11）https://www.itiger.com/news/1173986703 ：「MGX will directly acquire 35% of Aligned, BlackRock 20%, and AIP the remaining 45%」；「$21B equity consideration」（代理轉述）；MGX 亦投資 Vantage；「The deals may trigger CFIUS review」。〔二手〕
3. Data Center Knowledge 轉載 Bloomberg（2025-10-09）https://www.datacenterknowledge.com/data-center-chips/us-approves-some-nvidia-uae-sales-in-trump-ai-diplomacy-step ：「the UAE made concrete plans for a reciprocal amount of investment on American soil」；「will match its investment with what it receives in chip shipments on a dollar-for-dollar basis」；「It's unclear when additional licenses may be issued … depend in part on how the UAE's specific investment plans unfold」。〔二手，匿名官員〕
4. Commerce 聲明（2025-11-19，GlobalSecurity 轉載）https://www.globalsecurity.org/military/library/news/2025/11/mil-251119-commerce01.htm ：「The approvals are conditioned on both companies meeting rigorous security and reporting requirements」；G42、Humain 各「up to 35,000 Nvidia Blackwell chips (GB300s)」。〔一手；**未**寫投資條件——與 #3 相左，測一須處理〕
5. Middle East AI News（2026-07-11）https://www.middleeastainews.com/p/usa-eases-ai-chip-exports-to-uae ：「upgraded the United Arab Emirates to its highest export control tier, Country Group A:5」；「without individual export licences」。FAF（2026-07-15）https://www.faf.ae/home/2026/7/15/silicon-sovereignty-how-washingtons-elevation-of-the-uae-to-trusted-chip-status-is-redrawing-the-geopolitical-map-of-artificial-intelligence ：「On July 10, 2026, the United States Department of Commerce announced sweeping changes」。〔二手；BIS 原稿測一須實讀〕
6. Middle East AI News（2026-04-06）https://www.middleeastainews.com/p/us-affirms-ironclad-ai-commitments ：「the UAE reaffirmed its $1.4 trillion US investment commitment」。vision2030.ai（2026-07-31）https://vision2030.ai/geopolitics/us-chip-export-controls-saudi-uae-divergence/ ：Saudi「“Almost $1 trillion”, 18 November 2025」；Supplement No. 8 核准美商名單。〔二手〕

缺段（§7-2）：BIS 2026-07-10 原規則文本（Federal Register）；主權於美國資料中心權益交易之占比（無市場層數字）；Aligned 交易倍數（未揭露）；A:5 前後主權參與美國交易之時間序列；Semafor 2026-09-28（robots 拒讀，無法判定是否轉向亞太）。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | Commerce 官方只以安全與申報為條件，投資對等是雙邊框架之政治承諾而非許可對價；λ 從未逐批存在 | #4 | 機制前提不成立 |
| R2 | 1.4 tn 承諾仍「ironclad」重申；λ 之存量部分（政治履約）不因 A:5 消失，主權出資節奏不變 | #6 | 方向相反 |
| R3 | 主權參與者與 BlackRock／GIP 共同出資，價格由基礎設施基金之報酬要求定，主權非邊際 | #1、#2 | 非邊際 |
| R4 | 私有資料中心估值由 hyperscaler 長約現金流與利率主導，主權要求報酬率之變動（若有）量級小於利率噪音 | — | 量級不足 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無任何一手（Commerce／BIS／白宮／UAE 官方聯合聲明）文字把出口許可之發放與 UAE 對美投資之金額或節奏相連——λ 只有匿名二手來源（R1 成立）。
(2) 2024-01 至 2026-10 可識別之美國資料中心權益交易（≥ 1 bn）中，主權參與者（MGX、Mubadala、ADIA、PIF、QIA、KIA、GIC、Temasek）出資占比無一手或具名機構數可得，或可得之數 < 15%——非邊際（R3）。
(3) A:5 生效（2026-07-10）後至測一日，UAE 主權實體宣布之美國資料中心新權益交易之額度與件數，不低於生效前同長度窗口——無反應（R2 成立）。且無其他可觀測端（AIP 募資進度、MGX 宣示轉向非美）支持 λ 下降。
(4) 主權參與交易與非主權同型交易之倍數（EV／MW 或資本化率）差 `[D]` 無法於 ≥ 2 組可比交易計得，或差 < 1 個資本化率百分點之 1/4（25bp）——量級不足（R4）。
(5) 具名賣方、評等機構或政策研究機構已量化「出口許可對價 → 主權要求報酬率 → 美國資料中心私有估值」之鏈並公開——已定價。只點名「海灣資金湧入」不算。
(6) 重定價窗（≥ 12 個月）內無可觀測檢驗事件（AIP 下一筆交易或募資結案、MGX／Mubadala 美國資料中心交易或處分、BIS 對 Saudi 之 A:5 決定、CFIUS 年報），或其已全部於窗前公告。
(7) 可運作對照只能寫成買方監理資本（L13-I#4 型）、載具贖回（L13-I#5 型）、分區容量守恆（L6-P#6 型）或利率／資本化率本身，而非主權出資之非財務報酬誘因。

複查觸發器（若日後殺）：BIS 或白宮一手文件明示許可與投資對等之連結；Saudi 升入 A:5（第二個自然實驗）；MGX／AIP 宣布處分或暫停美國資料中心投資；具名機構公布主權占美國資料中心權益交易之比重。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：上市資料中心開發商／REIT 之私有合資出售價與減值測試所用資本化率；另類資管之基礎設施費用相關收益中主權 LP 占比。
2. 可交易工具：上市資料中心 REIT／開發商、上市另類資管普通股。不選券。
3. 半衰期：私有交易逐筆公告；BIS 規則變動；季度財報之合資估值。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0202；`query/ARCH_matrix.md` L13［I］標「#6 已生成」；`export/LEADS_算力收支.md` 追加 1 筆（Aligned 收購完成 EV 與容量〔一手〕）。不寫入：FUNNEL（留給測一）、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L13-I#1–#5、L13-P#1–#6、L13-A#1–#6、L6-P#6、L6-I#5、C-A3／C-A4 結論；不寫 T-15。
