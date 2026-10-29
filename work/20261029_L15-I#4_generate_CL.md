# L15-I#4 生成卡｜基礎設施軟體與資料：誘因（集中型 AI 原生買方之雙源門檻——單一客戶觀測支出越過自建／第二供應商之門檻時，買方以雙源壓量於續約重設承諾；門檻屬性使同一誘因依規模序列傳遞至其他高支出 AI 原生客戶，非單一客戶特例）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261007_L15-I_generate_GK.md；archive/work/20261014_L15-I#2_generate_CL.md；archive/work/20261022_L15-I#3_generate_CL.md；archive/work/20261029_L15-A#4_generate_CL.md；query/QUEUE.md（Q-0113 L7-I#4 邊界、Q-0123 L14-I#4 邊界、Q-0124 L15-P#4 邊界） | EMITS: work/20261029_L15-I#4_generate_CL.md -->
**日期：** 2026-10-29　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 3→4／6）　**格：** L15-I　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L15-A#4 已測，Q-0125 done）。第 4 輪序中唯一未生成 #4 之非已殺／刻意排除格＝L15-I（最後測試 2026-10-22，#3）；L2-P／L2-A（#4 測於 2026-10-21）已有 #4，依前輪（L15-A#4 卡 §0）之輪序慣例先補齊本輪，取 **L15-I**。既有 #1–#3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `observability`、`insourcing`、`AI-native`，0 筆；未用。內部數字（§12）未用。
- 比對（須異型）：
  - **L15-I#1**（`archive/drive/USED_20261007_L15-I_generate_GK.md`）：遙測出站費／保留期使取用權結構性鎖定（賣方鎖定誘因）。本卡反向：**買方**之脫鎖誘因，標的為續約承諾量重設，不涉出站費率或保留期；載體同為 DDOG 但量綱不同（承諾／用量 vs 出站單價）。
  - **L15-I#2**：雲端商共同出資相容開源引擎封頂託管價。本卡之第二供應商為商業閉源（Chronosphere，現屬 PANW），觸發者為單一大買方之支出門檻，非雲端商之相容層。
  - **L15-I#3**：收購方收割俘虜裝機基、前置認列。本卡賣方為讓步方（續約換量），非收割方；無前置認列。
  - **L7-I#3**（模型層客戶集中／換供應）、**L7-I#4**（照付不議承諾過剩）：本卡層＝基礎設施軟體，機制為支出門檻觸發之雙源，不主張換供應或承諾過剩；買方仍續約。
  - **L14-I#4**（牌價世代）、**L15-A#4**（佣金資本化）、**L15-P#4**（儲存占比）、**L14-P#2**（承諾池互抵）、**L15-A#1**（量×價）：不涉。
  - 已殺 C-A1–C-A5、L8-P／L9-P／L11-P：不涉。
- §7-10 領域最近公開：DDOG 10-Q 2Q26（期 2026-06-30，2026-08-06 申報）。下一檢查點＝DDOG 3Q26 業績 **2026-11-04**（盤前，finviz 轉載公司公告）。

## 1. 落差一句

種子主張：市場把 DDOG 2Q26「largest customer … usage reduction」讀成單一客戶（報導指為 OpenAI，公司未證實）之特例，並接受管理層「back out a large customer … pretty much the same growth rate」之框架；種子主張此為**門檻型買方誘因**：觀測支出隨 AI 原生客戶之 GPU／推論規模超線性增長，越過門檻後買方之最適反應是引入第二供應商（或自建）並在續約時以雙源壓低承諾量——賣方為保留 logo 接受「renewed … nine-figure」而用量下降。門檻屬性意味同一誘因將依規模序列傳遞至其他高支出 AI 原生客戶（2Q26：年支出 > $1M 者 31 家、> $10M 者 8 家），AI 原生群之成長於各自續約點分段下台階。可拒絕之主張＝第 2–n 大 AI 原生客戶之續約可觀測地呈現（或不呈現）同型用量重設，而公司與賣方以「除最大客戶外」口徑外推。不主張任何主體價值方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因（I）**：買方 \(i\) 之觀測支出 \(S_i \propto V_i^{\beta}\)（\(V\)＝遙測量，隨運算規模增長）；雙源／自建之固定成本 \(F\)；當 \(S_i \cdot \delta > F\)（\(\delta\)＝雙源可壓之價量比例）時，買方於續約點採雙源，續約後 \(S_i\) 下修；賣方續約之最適為接受低承諾保 logo |
| 量綱 | 美元／年（支出、承諾）；\(\delta\) 無因次；門檻以年支出帶（$1M／$10M）代理 |
| 選擇者 | 買方（AI 原生大客戶之工程／採購）；賣方（續約讓步幅度）；第二供應商（PANW 收購後之 Chronosphere 定價） |
| 可見端 | DDOG 10-Q MD&A 營收增量歸因句、NRR 敘述、RPO；電話會議 AI 客戶數與支出帶、「excluding largest customer」指引口徑；PANW 申報之 Chronosphere 客戶與 ARR 揭露 |
| 指名不可見端 | 個別客戶續約日、承諾額；AI 原生群營收占比（2025-Q4 起停揭：「have not put it in there」） |
| 表達工具型態（只指名，不選券） | 美股觀測／基礎設施軟體商；不選券 |
| 重疊 | L15-I#1（同載體 DDOG，反向誘因）；L7-I#3（集中度） |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. DDOG 10-Q 2Q26（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1561550/000162828026054458/ddog-20260630.htm ：「Revenue $ 1,121,454 $ 826,760 … 36 %」；「We saw a reduction in usage from our largest customer starting in the third quarter of 2026, which may cause a deceleration in reven…」；NRR「low-120%'s」（2025-06-30 約 120%）；RPO $3,471.4M vs $3,461.2M（2025-12-31）。
2. DDOG 2Q26 電話會議逐字稿（第三方轉錄）https://transcripts.platformaeronaut.com/transcripts/DDOG-2Q26-transcript ：CFO「Regarding our largest customer, we have seen a usage reduction, which is incorporated in our Q3 and full year 2026 guidance」「this customer has recently renewed with us」；「31 customers spending more than $1 million annually … eight customers spent more than $10 million annually」；CEO「if you back out a large customer from our growth, you get pretty much the same growth rate」。
3. DDOG 4Q25 電話會議（Motley Fool 轉錄）https://www.fool.com/earnings/call-transcripts/2026/02/10/datadog-ddog-q4-2025-earnings-call-transcript ：指引「our business, excluding our largest customer, grows at least 20%」；AI 原生占比「have not put it in there」；約 650 家 AI 原生、19 家 ≥ $1M。
4. DDOG 10-K FY25（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1561550/000162828026008819/ddog-20251231.htm ：grep「AI-native」「largest customers」「small number of customers」0 筆——集中度未於申報層量化。
5. PANW 8-K Ex.99.1（2026-01-29，sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1327567/000119312526029489/d884183dex991.htm ：「completed its acquisition of Chronosphere」——第二供應商已併入大型平台。
6. 二手：TIKR（2026-08-21）https://www.tikr.com/blog/datadog-fell-19-on-a-q2-beat-is-the-selloff-a-buying-opportunity-or-a-warning ：當日收跌 19.03%；「Analysts and press reports identified the account as OpenAI」；續約「nine figures but committed to consuming less」（二手）。GuruFocus 轉 UBS（TradingView）https://pl.tradingview.com/news/gurufocus%3Ac9e252306094b%3A0-datadog-versus-chronosphere-inside-openai ：「OpenAI now runs Datadog … and privately held Chronosphere side by side」；自建「seems unlikely」（二手，無日期）。
7. 檢驗事件：DDOG 3Q26 業績 2026-11-04（finviz 轉載）https://finviz.com/news/402639/datadog-announces-date-of-third-quarter-fiscal-year-2026-earnings-call 。

缺段（§7-2）：最大客戶之身分、占比、續約額之一手均未取（公司未揭露）；第 2–8 大 AI 原生客戶之續約時點未取；UBS 原報告未取；PANW 10-Q 對 Chronosphere 之客戶揭露未讀；具名賣方是否建模 AI 原生群之續約重設未取。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 單一客戶特例：除最大客戶外成長率不變且加速 | DDOG CEO 2Q26 電話會議 | 不可傳遞（→(2)） |
| R2 | 市場已定價：2Q26 當日 −19%，指引「fully de-risk」 | TIKR；DDOG CFO | 已定價（→(3)） |
| R3 | 自建不可能、雙源只施壓價格不減量 | UBS（GuruFocus 轉述） | 機制不成立（→(4)） |
| R4 | 其他 AI 原生大客戶支出帶低一級，未達門檻 | DDOG 支出帶揭露 | 量級不足（→(4)） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法就 DDOG 取得 ≥ 4 期（季）之 AI 客戶支出帶（≥ $1M／≥ $10M 家數）或「除最大客戶外」成長口徑並列，且無法就最大客戶以外之任何 AI 原生客戶取得續約或用量變動之一手或具名報導；或
(2) 3Q26（2026-11-04）與其後一期揭露顯示 ≥ $10M AI 原生客戶家數續增且公司明示無第二家用量重設（R1 成立，誘因不傳遞）；或
(3) 具名賣方或研究機構已以 AI 原生群之續約時點 × 用量重設建模 DDOG 2027 營收並為市場引用（已定價）；或
(4) 可運作對照只能寫成出站／保留期鎖定（L15-I#1）、相容開源封頂（L15-I#2）、收購方收割（L15-I#3）、模型層換供應（L7-I#3）或量×價（L15-A#1）；或 `[D]` 第 2–8 大 AI 原生客戶合計支出 < 營收 3%（門檻凍結於此），使傳遞無量綱；或
(5) 12 個月內無檢驗事件（3Q26 2026-11-04、4Q26 約 2027-02、FY26 10-K）；或
(6) 最大客戶用量下降之一手歸因為工作負載遷移或一次性優化（非雙源／自建），使門檻誘因不成立。

複查觸發器（若日後殺）：DDOG 或同業首次揭露第二家大客戶續約降量；AI 原生群占比恢復揭露；PANW 揭露 Chronosphere 自 AI 原生客戶之大額取代案。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：營收增量歸因、NRR、RPO、AI 客戶支出帶。2. 可交易工具：觀測軟體商普通股（不選）。3. 半衰期：年約續約週期（約 12 個月）；門檻傳遞依客戶規模序列 1–3 年。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0126；`query/ARCH_matrix.md` L15［I］加「#4 已生成」；`AIM_FUNNEL.md` §3 一句與日期行。LEADS：本輪事實（觀測軟體營收／客戶）非 AI 算力投入、收入、硬體、雲端合約或資料中心之直接事實，未寫。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L15-I#1–#3、L15-A#1–#4、L15-P#1–#4、L7-I#3–#4、L14-I#4；不碰 L1-P；不寫 T。
