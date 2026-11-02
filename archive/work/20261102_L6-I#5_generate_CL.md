# L6-I#5 生成卡｜雲端與基礎設施服務：誘因（買方之自建／外購排序：同時握有自建與外購選項之超大規模買方，把**耐久需求留給自建**、把**最不確定／過渡之切片外購給新雲**——新雲之超大規模合約流量是買方「自建缺口」之函數，而非總 AI 需求之函數）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260928_L6-I_generate_GK.md；archive/work/20261011_L6-I#2_generate_CL.md；archive/work/20261018_L6-I#3_generate_CL.md；archive/work/20261026_L6-I#4_generate_CL.md；archive/work/20261102_L6-P#5_generate_CL.md；archive/work/20261102_L6-A#5_generate_CL.md；archive/work/20261021_L14-I#3_generate_CL.md；archive/work/20261028_L13-P#4_generate_CL.md；archive/work/20261020_L13-I#3_generate_CL.md；archive/work/20261011_L4-I#2_generate_CL.md；archive/work/20261101_L4-I#5_generate_CL.md | EMITS: work/20261102_L6-I#5_generate_CL.md -->
**日期：** 2026-11-02　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3→4／6）　**格：** L6-I　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L6-A#5 本日測一，Q-0149 done）。非已殺、非刻意排除之格中，最後測試日最舊＝2026-10-26（L6-I#4、L13-A#4 並列）；依表序取 **L6-I**。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py neocloud Microsoft third-party capacity lease`，命中 11 筆；相關 1（SRC_DC_014 IREN／Microsoft 每 MW 設備 capex，新聞稿）——與自建／外購排序無關，**未使用**。其餘為模型能力／OpenAI 支出類，未使用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L6-I#1**（GK；逆選擇＝對手方信用）：本卡對手方為投資級買方，風險不在信用，而在**被外購之需求切片**本身被選擇（切片逆選擇，非對手方逆選擇）。
  - **L6-I#2**（賣方代理人 bookings 計酬）：選擇者為賣方內部；本卡選擇者為買方。
  - **L6-I#3**（債權人驅動之首約讓價 `Δp`）：本卡不涉單價。
  - **L6-I#4**（已簽批次之交付終止權）：本卡不問已簽合約是否被退出，而問**新合約流量**由何決定；合約全數履行亦可成立。若測一只能以「終止／減量事例」證明，即退化為 L6-I#4（否決 (5)）。
  - **C-A4**（續約單價比 `k`）：本卡不涉續約價格；續約與否只作觀測事件，不定價。
  - **L6-P#3**（供給方容量之用途分割）、**L6-P#5**（承諾再售）、**L6-A#5**（分部未分攤項）、**L6-A#4**（capex 現金流分類）：不涉。L6-A#4 之融資租賃入帳問題只作載體（新雲容量是否列融資租賃），非落差。
  - **L14-I#3**（企業以市集消化 MACC）、**L13-P#4**（單一對手方 OpenAI 現金守恆）、**L13-I#3**（評等觸發線之工具選擇）：買方、量與動機均不同。
  - **L4-I#2**（加速器商兜底回租）、**L4-I#5**（配貨搭售）：選擇者為加速器商；本卡為雲買方。
  - 重疊列為否決 (5)。
- §7-10 領域最近公開：Microsoft 10-Q 期 2026-09-30（2026-10-28 申報）；Microsoft FQ1 FY27 法說 2026-10-28；Nadella 言論報導 2026-10-30。下一檢查點＝CoreWeave、Nebius、IREN 3Q26 申報（約 2026-11）；Microsoft 10-Q FQ2 FY27（約 2027-01 底）。

## 1. 落差一句

超大規模業者同時握有「自建」與「向新雲外購」兩個選項；其最適排序是把**可預期、跨世代可再用、客戶分散**之需求留給自建，而把**時點錯配（自建來不及）、單一世代、單一客戶**之切片外購（Nadella：「I didn't want to get stuck with massive scale of one generation」、「We didn't want to just be a hoster for one company」；Guthrie：「We've made the decision that we don't want to be constrained in terms of capacity」；Bloomberg：外購「letting Microsoft free up its own server farms」）。故新雲之超大規模合約流量 ≈ 買方之**自建缺口**（需求 − 自建可交付），在自建追上時會先於總 AI 需求轉弱而停止，即使總需求仍「exceeds supply」。種子主張：市場以「投資級買方之新雲合約」為**總 AI 需求**之證據並外推新雲之新約流量；而若排序誘因成立，新雲新約流量之一階驅動為買方自建時程，與總需求之相關低於所見。觀測量 `g ≡ 買方外購容量 ÷（自建＋外購）`之季變動、`τ ≡ 新雲合約期 ÷ 設備經濟年限`（只作排序證據）。本卡不定方向與量級。

已見事例：Microsoft FQ1 FY27「Capital expenditures were $45.2 billion as some third-party capacity deliveries we expected in Q1 were delayed」（Hood，經 Stocktwits 轉述，二手）——顯示第三方容量入其 capex（含融資租賃）口徑，可作 `g` 分子之一手入口待測；同日新雲股下跌被讀為「slower capacity ramp」（二手）。2025 年 Microsoft 退出部分 CoreWeave 協議（FT 經 Capital Brief，二手），歸因交付問題——屬 L6-I#4 型，**不**作本卡證據。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因（買方之自建／外購排序；峰荷外包＝把需求波動之高階部分轉嫁供給方）；非守恆、非會計恆等 |
| 選擇者 | 同時自建之超大規模買方（Microsoft 為主；次為 Meta、Google、Amazon 對新雲之採購） |
| 可見端 | Microsoft 10-Q 租賃附註（尚未起租租約、當季以租賃換得使用權資產、融資租賃 vs 營業租賃）；capex「including finance leases」口徑與法說之第三方容量敘述；新雲申報之客戶集中度、合約期、批次交付；買方管理層對外購用途之原文（橋接、單一世代、單一客戶） |
| 指名不可見端 | 買方內部之自建／外購分配規則；新雲合約在買方帳上屬服務或租賃；各新雲合約所服務之終端工作負載（OpenAI／第一方／Azure 客戶） |
| 對照式（生成用） | 可拒絕：(a) 買方外購與自建同比例擴張（`g` 穩定），外購非切片而是平行；或 (b) 外購切片為**最耐久**者（長約、跨世代、可續），與排序相反；或 (c) 新雲新約流量已被賣方以買方自建時程建模 |
| 表達工具型態（只指名，不選券） | 美股可交易之新雲（CoreWeave、Nebius、IREN；次為 Applied Digital、Cipher、TeraWulf 之 HPC 合約）。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Microsoft 10-Q 期 2026-09-30，Note 12 Leases：「As of September 30, 2026, we had additional leases, primarily for datacenters, that had not yet commenced of $ 364.6 billion, with some arrangements subject to certain contractual conditions being met. These leases will commence between fiscal year 2027 and fiscal year 2034 with lease terms of 1 year to 20 years.」；當季以租賃換得之使用權資產：營業 6,523／融資 5,192（百萬美元）；風險因素：「we rely on third-party providers, including colocation facilities, leased datacenters, and cloud infrastructure providers」、「As we manage infrastructure capacity constraints and evolving customer demand, we may modify capacity allocations, deployment priorities, pricing, or other commercial arrangements.」https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm （sec.py 實讀）
2. Bloomberg（Brody Ford）經 Data Center Knowledge 2025-10-02：「Microsoft has inked more than $33 billion in commitments to such providers, including Nebius, CoreWeave, Nscale, and Lambda.」；外購理由「letting Microsoft free up its own server farms」、「more financial flexibility」。https://www.datacenterknowledge.com/cloud/microsoft-bets-33b-on-neoclouds-to-ease-ai-crunch （二手）
3. MBI Deep Dives 2025-11-13 摘錄 Nadella 訪談（單一世代、單一客戶、fungibility 原文）。https://www.mbi-deepdives.com/nadellas-truth/ （二手；原訪談待測一取一手）
4. 24/7 Wall St. 2026-10-30（FQ1 FY27 法說 Nadella：「like 4 customers who buy a lot of capacity from you … that's not a business」；「as long as the pricing is right, we may sell them some」）。https://247wallst.com/investing/2026/10/30/satya-nadella-just-took-a-shot-at-oracle-and-coreweave/ （二手；逐字稿待測一取一手）
5. Gotrade 2026-10-29（Hood 第三方容量交付延誤、新雲股反應）。https://www.heygotrade.com/en/news/microsoft-cloud-beat-backs-rebound-lower-capex-hits-coreweave-and-neocloud-stocks-msft-crwv/ （二手）
6. 新雲端合約期與批次：Nebius 6-K 2025-09-08 https://www.sec.gov/Archives/edgar/data/1513845/000110465925088312/tm2525580d1_6k.htm ；IREN 10-K 期 2026-06-30 https://www.sec.gov/Archives/edgar/data/1878848/000187884826000052/iren-20260630.htm ；CoreWeave 10-Q 期 2026-06-30 https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm （皆為 L6-I#4 已錨之申報；本卡取其合約期與客戶集中度，不取終止條款）
7. 測一須另取：Microsoft FQ1 FY27 法說逐字稿（第三方容量、自建時程）；Microsoft 10-K FY26 之租賃與購買承諾；新雲 3Q26 申報之 Microsoft 占比變動與新約來源；Meta／Google 對新雲採購之管理層原文；具名賣方是否以買方自建時程建模新雲新約。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 買方「demand exceeds supply」，外購與自建均受限於供給，排序不具約束力；只要總短缺持續，切片無差別 | Hood（FQ1 FY27，經 SiliconANGLE／Gotrade） | 窗內不可檢驗 |
| R2 | 外購為五年長約、與自建平行擴張，屬「land-grab」而非過渡切片 | Guthrie（Bloomberg 2025-10-02）；ARPU 2025-11-12「long-term (often five-year) contracts」 | 對照 (a)(b) |
| R3 | 新雲客戶已分散（Meta、OpenAI 等），單一超大規模買方之排序不再主導新約流量 | CoreWeave 與 Meta 合約報導（24/7 Wall St. 引 $21B） | 量級不足 |
| R4 | 市場已讀出排序：新雲股對 Microsoft capex 敘述即時反應 | Gotrade 2026-10-29 | 已定價 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 買方外購容量（新雲服務或融資租賃）與自建容量於 Microsoft 10-Q／10-K 或法說原文不可分列，且 ≥ 2 家新雲申報亦無法分出該買方之新約與既有批次，使 `g` 無判別力。
(2) 買方管理層原文明示外購切片為**長期、跨世代、與自建同質**（非橋接、非單一世代／客戶），且新雲合約期 ≥ 設備經濟年限（`τ` ≥ 1），排序假說之前提不成立。
(3) 具名賣方或新雲管理層已以買方自建時程（或 `g`）建模新雲新約流量，且新雲股對買方 capex／自建敘述之反應（R4）已反覆可見——已定價。
(4) 2025–2026 期間新雲新約之來源已以非超大規模買方（實驗室、企業、主權）為主，單一超大規模買方之排序對新約流量之占比 < 30%，量級不足。
(5) 可運作對照只能寫成：已簽批次之終止／減量（L6-I#4）、對手方信用（L6-I#1）、首約讓價（L6-I#3）、續約單價（C-A4）、承諾再售（L6-P#5）、市集承諾消化（L14-I#3）或單一對手方現金上界（L13-P#4）。
(6) 12 個月內（至 2027-10）無可檢驗事件：買方未公布自建時程、新雲未揭露新約來源，`g` 之季變動不可觀測。

複查觸發器（若日後殺）：Microsoft（或另一超大規模買方）於 10-Q／10-K／法說原文首次分列第三方／新雲容量支出或占比；或任一美股可交易新雲揭露主要超大規模客戶之新約歸零而總 AI 雲需求指標（買方雲營收增速）未降。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：新雲端——RPO 之客戶別新增、客戶集中度、合約期；買方端——融資租賃使用權資產、尚未起租租約、capex 含融資租賃。
2. 可交易工具：CoreWeave、Nebius、IREN 等美股與選擇權（不選券）。
3. 半衰期：自建缺口之閉合約 4–8 季；`[V]` 不寫。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L6［I］標「#5 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 3 筆（Microsoft 尚未起租租約、當季以租賃換得使用權資產、Bloomberg 新雲承諾合計）。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L6-I#1–#4、L6-A#1–#5、L6-P#1–#5、L14-I#3、L13-P#4、L4-I#2、C-A4 結論。
