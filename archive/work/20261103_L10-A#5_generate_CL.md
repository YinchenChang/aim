# L10-A#5 生成卡｜分發與中介：會計恆等（分發收入方之毛利組合恆等：Services GP ≡ L·m_L ＋ (S − L)·m_o；預設搜尋授權收入 L 近零成本（m_L ≈ 1），其權重在毛利遠高於營收，L 之變動對 Services 毛利率之傳導為 (m_L − m_o)·ΔL／S）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；AIM_FUNNEL.md；archive/drive/USED_20261001_L10-A_generate_GK.md；archive/work/20261013_L10-A#2_generate_CL.md；archive/work/20261020_L10-A#3_generate_CL.md；archive/work/20261027_L10-A#4_generate_CL.md；work/20261013_L10-A#2_test1_CL.md；work/20261020_L10-A#3_test1_CL.md；work/20261027_L10-A#4_test1_CL.md；archive/work/20261013_L10-I#2_generate_CL.md | EMITS: work/20261103_L10-A#5_generate_CL.md -->
**日期：** 2026-11-03　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3→4／6）　**格：** L10-A　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L10-P#5 本日測一，Q-0155 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-27（L10-A#4、L10-I#4、L11-A#4）；依表序取 **L10-A**。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py Apple licensing services margin`，命中 2 筆（OpenAI 推論支出，無關）＝相關命中 0。載體全由本輪 sec.py／WebSearch／WebFetch 實讀。內部數字（§12）未取。§12 線索輸出：本輪事實非 AI 算力收支一手數值（Gemini–Siri 付款僅二手報導），未寫 LEADS。
- 比對之舊檔與死因型態，本卡須異型：
  - **L10-A#1**（測一不通過）：**付款方** TAC＝轉介量 × 每次分潤率；死因＝量與率不可並列，只剩混成 rate。本卡在**收款方**，可拒絕之主張落在**毛利組合**（m_L 與 m_o 之差使 L 之毛利權重 ≫ 營收權重），不需拆量與率；若實讀後只剩「Safari 查詢量 × 36%」即滑回 #1 型（否決 (3)）。
  - **L10-A#2**（部分通過）：商戶預收浮存，現金時序。本卡不涉現金時序。
  - **L10-A#3**（不通過）：主事人／代理人列報切換。本卡不論列報口徑（授權收入淨額列報無爭議）。
  - **L10-A#4**（測一已做）：自保準備之精算估計。本卡不涉估計。
  - **L10-I#1**（預設槽位／選擇畫面）、**L10-I#2**（App Store 佣金路由）：誘因型；本卡不主張任何一方之行為選擇，只主張恆等式之傳導係數。
  - **L12 系列**：驅動含 DOJ v. Google 救濟，但主張落在毛利組合；若只剩「上訴勝敗」即 L12（否決 (4)）。
  - **L11-P**（死 #3）不恢復；C-A5 不重開；不寫 T-15。
- §7-10 領域最近公開：Apple 8-K Ex.99.1 FQ4 FY2026（2026-11-02）；Apple 10-K FY2025（2025-10-31）；Google D.C. Circuit 上訴書（2026-05-22，9to5Mac 報導）；DOJ 案卷所載 final judgment 2025-12-05、上訴簡報 2026-07-28（MacMyths 2026-09-23 轉述）。下一檢查點＝Apple 10-K FY2026（預期 2026-11 上旬）、FQ1 FY2027 10-Q（約 2027-01 底）、D.C. Circuit 言詞辯論／判決。

## 1. 落差一句

恆等骨架：`GP_S ≡ L·m_L + (S − L)·m_o`；`GM%_S ≡ m_o + (m_L − m_o)·L／S`；`∂GM%_S／∂L ≈ (m_L − m_o)／S`。已見數點：Apple Services 營收 109,158 → 123,301、成本 26,844 → 29,358（百萬美元，FY25 → FY26，8-K Ex.99.1）；GM% 75.4% → 76.2% `[D]`。外部報導 L ≈ 20B（2022，法庭文件；36% 分潤）。以 L＝20B、m_L＝1 為 `[A]`：L／S＝18.3%（FY25）／16.2%（FY26）；L／GP_S＝24.3%／21.3%；L／公司總 GP＝10.2%／8.6%；扣 L 後 m_o＝69.9%／71.6% `[D]`。市場若把 Services 毛利率擴張讀作 App Store／訂閱組合之結構性改善，而其中一塊為**以 12 個月為期、受上訴與 AI 搜尋分流兩面壓力之近零成本授權**，則錯價在於把 L 之毛利權重當作營收權重（差 ≈ 1／m_o 倍）。**不主張 L 之方向或時點，不寫 H1。**

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（分部毛利組合；收款方淨額列報之授權收入） |
| 量綱 | S、L、GP［美元／年或季］；m_L、m_o、GM%［無量綱］；L／S 與 L／GP 之比［無量綱］ |
| 選擇者 | Google 續約條件（救濟：非獨占、預設條件 ≤ 1 年）；Safari 查詢量（Cue 2025-05 證詞：首次下降）；Apple 是否加入 AI 搜尋供應者與其分潤條款；Apple 對 Google 之 Gemini 付款（若列 Services 成本則同時壓 m_o） |
| 可見端 | 10-K／10-Q Services 營收與成本、GM%；10-K 風險因素明文「licensing arrangements with Google」；MD&A「different mix of services」 |
| 指名不可見端 | L 本身（Apple 不分列；只有法庭文件 2022 一點）；m_L（是否有可歸屬成本）；Gemini 付款之會計位置 |
| 主張 | L 之毛利權重未被市場分離；可由「公司或賣方已分離」或「L 占比小／穩」拒絕 |
| 外部參照物（測一查證） | 前例：2025-05-07 Cue 證詞當日 GOOGL 與 AAPL 股價反應；JPMorgan 2025-07 情境（最壞 12.5B、約 15% EPS） |
| 表達工具型態（只指名，不選券） | 美股上市、收取預設搜尋授權之分發平台普通股。不選券 |
| 重疊 | L10-A#1（量 × 率）、L10-I#1（預設槽位）、L12（反壟斷）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Apple 8-K Ex.99.1 FQ4 FY2026（sec.py）https://www.sec.gov/Archives/edgar/data/320193/000032019326000024/a8-kex991q4202609262026.htm ：「Services 31,573 28,750 123,301 109,158」；「Cost of sales: … Services 7,593 7,106 29,358 26,844」；「Services reaching an all-time high」。
2. Apple 10-K FY2025（sec.py）https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm ：「the Company earns revenue from licensing arrangements with Google LLC (“Google”) and other companies to offer their search services on the Company’s platforms」；「on September 2, 2025, the … D.C. District Court … ordered certain remedies」；「remedies initially proposed by the DOJ, such as those prohibiting Google from offering the Company commercial terms for search distribution」；「Services gross margin percentage increased … primarily due to a different mix of services」；Services GM 82,314／71,050／60,345（2025／24／23）。廣告服務含「third-party licensing arrangements」。
3. 9to5Mac（Marcus Mendes，2026-05-22）https://9to5mac.com/2026/05/22/google-defends-its-safari-deal-with-apple-in-antitrust-ruling-appeal/ ：「Google paid Apple around $20 billion in 2022 alone」；「36% of the search advertising revenue generated through Safari」；「Google can no longer make the Safari agreement exclusive」；「12-month default limit」；D.C. Circuit 上訴書。
4. MacMyths（2026-09-23）https://macmyths.com/googles-antitrust-ruling-preserved-its-apple-search-deal-but-changed-the-rules/ ：final judgment「dated December 5, 2025」；「appellate briefing filed July 28, 2026」；L 「a reported estimate, not an undisputed figure Apple publishes」。
5. Fortune／Yahoo（Beatrice Nolan，2025-07-30）https://finance.yahoo.com/news/apple-risks-12-5-billion-152458330.html ：JPMorgan「could cost Apple $12.5 billion annually, about 15% of Apple's earnings per share, as a worst-case scenario」（具名賣方已做 EPS 情境 → 否決 (1) 候選）。
6. iPhone in Canada（Nehal Malik，2025-05-08）https://www.iphoneincanada.ca/2025/05/08/apple-google-search-declining ：Cue「searches on its Safari web browser declined for the first time last month」；Google「We continue to see overall query growth in Search」。
7. Xataka（Javier Lacort，2025-06-18）https://www.xataka.com/empresas-y-economia/quinta-parte-beneficio-anual-apple-esta-riesgo-desaparecer-noche-a-manana ：「supone también en torno a un 20% del beneficio neto anual de Apple」（作者自算、無出處）。
8. AppleInsider（2025-11-05）https://appleinsider.com/articles/25/11/05/apple-considers-paying-1b-per-year-to-use-google-gemini-in-siri ：Apple 考慮每年約 1B 付 Google 用 Gemini（二手，轉述 Bloomberg）。
9. 測一須另取：Apple 10-K FY2026（sec.py）是否新增 L 之量化或 Services 成本中 AI 付款敘述；Alphabet 10-Q 3Q26（sec.py）TAC 與 Distribution partners 分列；具名賣方（Morgan Stanley、Bernstein、JPMorgan 等）是否以「ex-Google 授權」口徑呈現 Services GM 或 GP；D.C. Circuit 時程；續約條件是否已重談（2026 年續約公開與否）。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 賣方已以 EPS 情境量化 L 之最壞損失（JPMorgan 12.5B／≈15% EPS） | #5 | 已定價 |
| R2 | 救濟已確定允許付款續行，只改獨占與期限；L 之存續風險已降 | #3、#4 | 機制只剩期限，ΔL 小 |
| R3 | Google 稱整體查詢仍成長；Safari 單月下降不構成趨勢 | #6 | ΔL 無可觀測驅動 |
| R4 | Services GM% 擴張可由 App Store、雲端、廣告成長解釋，L／S 逐年下降，權重自然稀釋 | #1、#2 | 恆等式成立但不重大 |
| R5 | 可拒絕之事件是上訴判決，屬 L12 | #3、#4 | 滑入他格 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 具名賣方或公司已公開以**毛利或 GP 口徑**（非僅營收或 EPS 情境）分離 L，或以「ex-Google 授權」口徑呈現 Services GM——已定價（R1）。僅營收／EPS 情境不觸發本條，但測一須記錄。
(2) `[D]` L／GP_S（以測一可得之最佳 L 估計，區間給出）< 15%，或窗內（≥ 12 個月）無任何可觀測之 ΔL 驅動（續約重談、上訴判決、Safari 查詢量揭露、AI 搜尋供應者分潤協議）——落差不重大（R2、R3、R4）。門檻 15% 於本卡凍結。
(3) 實讀後可拒絕之主張只剩「Safari 查詢量 × 分潤率」——L10-A#1 型。
(4) 可運作對照只能寫成 L12 系列（上訴勝敗）、L10-I#1（預設槽位選擇）或 L10-A#3（列報）。
(5) 一手證據顯示 m_L 顯著 < 1（授權有可歸屬之分潤回付或成本），或 Gemini 等 AI 付款列於 Services 成本且與 L 同約綁定，使 L 之淨毛利貢獻與營收權重相近。

複查觸發器（若日後殺）：Apple 10-K／10-Q 首次分列授權收入或其占比；D.C. Circuit 判決改變付款條件；Apple 公布 AI 搜尋供應者分潤協議；Google 10-Q 揭露 Distribution TAC 對單一夥伴之變動。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Services net sales、Services cost of sales、Services GM%；風險因素授權句。
2. 可交易工具：分發平台普通股。不選券。
3. 半衰期：季度（10-Q）；續約期 ≤ 12 個月。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L10［A］標「#5 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live、LEADS。不改 L10-A#1–#4、L10-P#1–#5、L10-I#1–#4、L12 系列、C-A5 結論；不寫 T-15。
