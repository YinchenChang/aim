# L14-A#5 生成卡｜企業終端需求：會計恆等（IT 經銷商之總額／淨額認列恆等：交易總額 G ≡ R_principal ＋ R_agent ÷ τ；淨銷售 NS ≡ R_principal ＋ R_agent——AI 軟體／雲端訂閱以代理人淨額認列被壓縮至抽成 τ，而硬體〔含 AI 帶動之記憶體價格轉嫁〕以本人總額認列被放大；經銷商「AI 帶動成長」之淨銷售讀數混合兩種量綱）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261005_L14-A_generate_GK.md；archive/drive/USED_20261005_L14-A_test1_GK.md；archive/work/20261013_L14-A#2_generate_CL.md；archive/work/20261021_L14-A#3_generate_CL.md；archive/work/20261028_L14-A#4_generate_CL.md；work/20261013_L14-A#2_test1_CL.md；work/20261021_L14-A#3_test1_CL.md；work/20261028_L14-A#4_test1_CL.md；archive/work/20261013_L14-P#2_generate_CL.md；archive/work/20261028_L14-I#4_generate_CL.md | EMITS: work/20261104_L14-A#5_generate_CL.md -->
**日期：** 2026-11-04　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 4→5／6）　**格：** L14-A　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L14-P#5 測一 2026-11-04，Q-0162 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-28（L14-A、L14-I；均 #4）；表序在前者＝**L14-A** → #5。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `reseller memory price CDW`，命中 2 筆（SRC_HW_052 機架 BOM、SRC_PRC_046 API 批次價），與本格無關，未用。內部數字（§12）未取。
- 比對之舊檔與死因型態，本卡須異型：
  - **L14-A#1**（買方 IT 支出 ÷ 營收；死因＝同一申報無法並列 IT 支出與 AI 行）：本卡不用買方支出，樞紐為**中介（經銷商）之認列口徑**。
  - **L14-A#2**（費用化／資本化；分列僅 1 家）：不涉買方資本化。
  - **L14-A#3**（重組排除項橋接）：不涉成本端。
  - **L14-A#4**（SI 之 AI 專項簽約滾存 U ≡ U₋₁＋B−R；死因＝同口徑並列僅 Accenture 1 家）：彼為存量／流量轉換；本卡為同一期內**總額 vs 淨額**之呈報量綱，不涉簽約、不涉 AI 專項 KPI 停揭。
  - **L14-P#2**（預付容量承諾池內替代）、**L14-I#3**（MACC 退抵路由）：彼為雲端消耗之池內再分配；本卡不主張替代，只主張同一筆企業支出在經銷商帳上依認列角色呈現為 G 或 G·τ。
  - **L14-I#4**（AI 名義套件牌價階梯＋續約鎖價）：彼為軟體賣方牌價之誘因；本卡之價格項為**本人認列硬體之元件成本轉嫁**（記憶體），且不判讀任何誘因。
  - **L14-P#5**（企業 AI 伺服器回遷）、**L14-P#1/#3/#4**（席次、人工處理量、PC 汰換）：不涉。
  - **C-A2**（ARCH_dead，單位經濟／無可交易主體）：不主張單位經濟。
- §7-10 領域最近公開：CDW 10-Q 2Q26（申報 2026-08-05）、Insight 10-Q 2Q26（2026-08-06）與 8-K 新聞稿（2026-08-06）。下一檢查點＝兩家 3Q26 10-Q（約 2026-11 上旬，測一應先查是否已申報）。

## 1. 落差一句

IT 經銷商（CDW、Insight）以「AI 動能」解釋淨銷售與毛利成長；種子主張：淨銷售恆等於本人總額認列項（以硬體為主，含 AI 資料中心需求帶動之記憶體漲價轉嫁）加代理人淨額認列項（軟體訂閱、雲端消耗，AI 授權多屬此類），兩者量綱不同——同一美元之企業 AI 軟體／雲端支出在淨銷售中只以抽成 τ 出現，而元件漲價以全額出現。可拒絕之主張＝把經銷商淨銷售成長讀成企業 AI 終端需求量者，系統性高估價格項、低估代理人項；若 `[D]` 拆解後本人項中價格成分不可分離、或代理人項占毛利之比過小、或市場已以毛利（而非淨銷售）讀此類主體（R2），本卡死。本卡不主張任何主體營收或股價方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等（A）**：(i) \(NS_t \equiv R^{P}_t + R^{A}_t\)；(ii) \(G_t \equiv R^{P}_t + R^{A}_t/\tau_t\)（G＝向客戶開立之總額；應收／應付以總額掛帳）；(iii) \(R^{P}_t \equiv \sum_k Q_{k,t}\,P_{k,t}\)，\(\Delta R^{P} = \sum P\Delta Q + \sum Q\Delta P\)（ΔP 含記憶體成本轉嫁）；(iv) 毛利 \(GP_t \equiv R^{P}_t\,m^{P}_t + R^{A}_t\)（代理人項之淨額即毛利） |
| 選擇者 | ASC 606 本人／代理人判定（控制權測試）；經銷商管理層之敘事歸因 |
| 可見端 | Insight 10-Q 營收附註逐季分列「Gross revenue recognition (Principal)」與「Net revenue recognition (Agent)」；CDW 10-Q 分硬體／軟體／服務淨銷售並註明部分以淨額認列；兩家應收／應付（DSO、DPO 受總額掛帳影響） |
| 指名不可見端 | τ（代理人抽成率）；G；本人項之量 Q 與價 P 拆分；AI 相關之代理人項占比 |
| 量綱 | 美元／期（NS、R、G、GP）；τ、m 無因次；Q 為台／件 |
| 外部參照物（測一查證） | 雲端轉型期（約 2015–2020）經銷商淨額化對淨銷售成長之壓抑先例；記憶體價格指數（如 TrendForce 合約價）作 ΔP 之外部錨 |
| 表達工具型態（只指名，不選券） | 美股、同時有本人與代理人認列之 IT 經銷商普通股；不選券 |
| 重疊 | L14-I 型（敘事歸因之誘因）可能為下一型；本卡只用金額與恆等 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Insight 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/932696/000093269626000070/nsit-20260630.htm ：營收附註「by recognition on either a gross basis as a principal in the arrangement, or on a net basis as an agent」；2Q26「Gross revenue recognition (Principal) $ 2,157,625 … Net revenue recognition (Agent) 241,872」（千美元；2Q25 對應 1,900,431／191,051）；MD&A「increases in hardware and services net sales as well as continued net revenue recognition in instances where Insight is the agent, partially offset by a decrease in software net sales」；合約資產「the Company invoices clients for the gross amount of consideration … including amounts ultimately passed on to the third-party service providers」。
2. Insight 8-K 2Q26 新聞稿（sec.py）https://www.sec.gov/Archives/edgar/data/0000932696/000093269626000067/nsit-20260806xerx8kex991.htm ：標題「Strong quarter led by AI momentum driving growth in cloud, infrastructure and services」；CEO「strength in cloud, infrastructure, and services, driven by AI demand」。
3. CDW 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1402057/000140205726000065/cdw-20260630.htm ：「Certain software and services revenues are recorded on a net basis as the Company is acting as an agent in the transaction. As a result, the category percentage of net revenues is not representative of the category percentage of gross profits.」；「increased demand for memory-intensive products driven by the rapid adoption of artificial intelligence (“AI”) applications … may continue to … drive pricing pressures」；「Netted down revenue results in an increase to both DSO and DPO as the corresponding receivables and payables reflect the gross amounts」。
4. CDW 8-K 2Q26 新聞稿（sec.py）https://www.sec.gov/Archives/edgar/data/0001402057/000140205726000062/cdw-2026630earningsrelease.htm ：「customers advanced investments in infrastructure modernization, cloud, and AI-enabled technologies」；毛利率下降「partially offset by a higher contribution of netted down revenue」。
5. CDW 10-K FY25（sec.py）https://www.sec.gov/Archives/edgar/data/1402057/000140205726000011/cdw-20251231.htm ：「DSO and DPO both increased due to an increase in netted down revenue and multi-year transactions」。

缺段（§7-2）：未讀兩家 3Q26 10-Q（可能已申報，本輪未查）；CDW 未見代理人項金額分列（10-Q 僅文字），需測一查 10-K 附註；未取法說逐字稿之 AI 營收或 AI 相關代理人項量化；未取記憶體合約價指數；未找到賣方以淨銷售讀企業 AI 需求之具名原文。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 公司自承類別淨銷售占比不代表毛利占比；經銷商以毛利為核心 KPI | CDW 10-Q 2Q26（§3-3）；Insight CEO 以「gross profit growth of 18%」為首（§3-2） | 市場已讀毛利，淨銷售混合無資訊 |
| R2 | 賣方對經銷商估值以毛利／EPS 為主，淨額化效果已為通識 | 測一需具名賣方原文 | 已定價 |
| R3 | 本人項之價格成分無量化揭露，(iii) 不可 `[D]` 分離 | §3 缺段 | 恆等不可運作 |
| R4 | 量級：Insight 代理人項 ≈ 淨銷售 10%（§3-1 `[D]`）；AI 相關部分更小 | §3-1 | 不足以重定價 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後 < 2 家主體能於一手申報（10-Q／10-K／8-K）取得 ≥ 4 季本人／代理人（或總額／淨額）同口徑分列；或
(2) `[D]` 代理人項占毛利 < 15%，或本人項 ΔP 成分無法以任何一手或外部指數錨定至 ±5 個百分點內（R3）；或
(3) 公司原文或具名賣方已以毛利或總額（G）讀企業需求、且明示淨額化與元件漲價效果（已定價，R1／R2）；或
(4) 可運作對照只能寫成 IT 支出 ÷ 營收（L14-A#1）、費用化／資本化（L14-A#2）、重組排除項（L14-A#3）、AI 專項簽約滾存（L14-A#4）、承諾池或 MACC 路由（L14-P#2／L14-I#3）、牌價階梯（L14-I#4）、席次／人工處理量／PC 汰換／伺服器回遷（L14-P#1／#3／#4／#5）；或
(5) 12 個月內無檢驗事件（兩家 3Q26／4Q26 10-Q／10-K、記憶體合約價轉向、任一主體開始量化 AI 相關代理人項）；或
(6) 代理人項中無法辨識任何 AI 相關成分（AI 授權若多以本人認列，則恆等不分離 AI 量綱）。

複查觸發器（若日後殺）：任一經銷商於申報中量化 AI 相關淨額認列項或交易總額 G；記憶體價格轉向致本人項價格成分可由申報反推；SEC 意見函要求經銷商說明本人／代理人判定或 AI 歸因。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：營收附註本人／代理人分列、類別淨銷售、毛利、DSO／DPO。2. 可交易工具：IT 經銷商普通股（不選）。3. 半衰期：元件價格循環（季至年）；揭露頻率每季。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0163；`query/ARCH_matrix.md` L14［A］加「#5 已生成」。不寫入：AIM_FUNNEL.md（沿前例，由測一輪對齊）、§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live、LEADS（本輪實讀事實無 AI 算力數值，未寫）。不改 L14-A#1–#4、L14-I#1–#4、L14-P#1–#5、C-A2 結論；不恢復 L11-P／L8-P／L9-P；不寫 T。
