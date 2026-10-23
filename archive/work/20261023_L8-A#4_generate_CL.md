# L8-A#4 生成卡｜標註／驗證：會計恆等（買方持有供應商股權之帳面——衡量替代法下以成本承載之最大標註商）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260918_L8-A_generate_GK.md；archive/work/20261007_L8-A#2_generate_CL.md；archive/work/20261015_L8-A#3_generate_CL.md；work/20261015_L8-A#3_test1_CL.md | EMITS: work/20261023_L8-A#4_generate_CL.md -->
**日期：** 2026-10-23　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3／6）　**格：** L8-A　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L2-I#4 本日測一）。非「已殺／刻意排除」格中最後測一最舊者＝2026-10-15 批：L8-A#3、L8-I#3、L9-A#3、L9-I#3、L12-P#3（L2-I#3 同日，已於 L2-I#4 輪處理）；依 QUEUE 序次（Q-0047 最先）取 **L8-A**；既有生成 3 份 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `Scale annotation Meta`，命中 6 筆，皆硬體／模型訓練指標，與本格無關，未採用。
- 比對（本卡須異型）：
  - **L8-A#1**（`archive/drive/USED_20260918_L8-A_generate_GK.md`）：支出 ÷ 有效條數；死於分母不可得。本卡不用產出單位。
  - **L8-A#2**（`archive/work/20261007_L8-A#2_generate_CL.md`）：賣方未開票收入（認列時點）。本卡不在賣方損益。
  - **L8-A#3**（`archive/work/20261015_L8-A#3_generate_CL.md`；測一 `work/20261015_L8-A#3_test1_CL.md`）：賣方客戶預付之轉付成本（營運資本）。本卡不在賣方營運資本。
  - **L8-I#2**（買方 Meta 持股 Scale → 他買方轉單、TaskUs 客戶量轉移；誘因）：本卡同一持股事實，但問的是**買方資產負債表上該股權之帳面恆等**（衡量替代法：帳面＝成本＋可觀察向上調整－減損／向下調整），不問客戶流向。
  - **L13-I**（供應方持有客戶股權 vs 應收帳齡）：方向相反（本卡為客戶持有供應商）、科目異（非應收）。
  - L8-P（分鐘／條）、C-I2（專家單價）：不涉。重疊不構成丟棄。
- §7-10 領域最近公開：META 10-Q 3Q26（期 2026-09-30，申報 2026-10-22）。下一檢查點＝META FY2026 10-K（約 2027-01 底）。

## 1. 落差一句

Meta 以約 14.3（US$十億）取得 Scale AI 49% 無表決權股，FY2025 10-K 揭露該投資以**衡量替代法**承載 13.80、「do not have significant influence」；衡量替代法下帳面＝成本＋同發行人可觀察交易之調整－減損，而 Scale 自交割後**無新定價輪或次級交易**（次級彙編 2026-10-21），故帳面停在成本——Meta 非上市股權之累計減損／向下調整 FY2024 末、FY2025 末、2Q26、3Q26 皆為 624（百萬）未動。同期 Scale 自報營收 2024 約 0.87、2025「just shy of 1」、2026 預期「top 1」（十億，未經審計），交割後失 OpenAI 等客戶、裁員 14%。種子主張：最大標註商之估值在申報層只以「成本」形式存在；成本 ÷ 營收隱含倍數（約 29 倍投後 ÷ 約 1）與已上市同層主體不可比對，且減損測試只由定性指標觸發——**錯價可能在任一方向**：(i) 若出現向下之可觀察價格（新輪、次級、IPO）或減損指標，Meta 須於損益認列；(ii) 若同層私有估值上行（Mercor 約 10），向上調整亦入損益。**方向未定**；本格只主張「該帳面為成本凍結值、非公允值」之恆等可被重算。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：衡量替代法帳面＝初始成本＋累計向上調整－累計減損／向下調整；損益只在可觀察交易或減損觸發時變動 |
| 已讀事實 | META 10-K FY2025 Note 5：初始成本 20,271（6,342）；累計向上 429（300）；累計減損／向下（624）（（624））；衡量替代法 20,076（6,018）；權益法 7,448（52）（百萬，2025-12-31（2024-12-31））。「mostly consist of our minority investments in Scale AI for $ 13.80 billion … and our investment in Jio Platforms Limited of $ 5.82 billion」「We do not have significant influence over these investees' operations.」關鍵會計估計：減損測試「performed at each reporting date to determine whether there are triggering events」，定性因子含「the investee's financial condition and business outlook; industry and sector performance」。META 10-Q 2Q26：初始成本 20,816；向上 559；減損（624）；衡量替代法 20,751。META 10-Q 3Q26：初始成本 21,119；向上 582；減損（624）；衡量替代法 21,077；權益法 11,547；全文「Scale AI」0 筆、「Jio」0 筆（10-Q 不再逐名）。 |
| 未證之連結 | Scale 是否已有任何同發行人可觀察交易（員工回購、次級、債務附認股權）；Meta 是否於任何申報或電話會評論該持股之減損評估；Scale 營收中 Meta 自身採購占比（投資人兼客戶之循環）。此即測一第一關。 |
| 量綱 | 帳面 ÷ 被投資方營收（倍數，無因次）；同層上市主體 EV ÷ 營收（無因次）；帳面 ÷ Meta 總資產（%）；可觀察價格 ÷ 入股價格（無因次） |
| 選擇變數 | Meta：減損指標判斷；Scale：是否定價新輪／次級（定價即迫使 Meta 調整） |
| 半衰期 | 每季重報；只在可觀察交易或減損觸發時解消 |

## 3. B 端可觀測載體（只指名）

1. META 10-K FY2025 https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm （Note 5、關鍵會計估計、市場風險段）
2. META 10-Q 3Q26 https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm （Note 5 表；Scale 不再逐名）
3. META 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm （季序列）
4. Scale 估值／營收彙編（Value Add VC，2026-08-11，更新 2026-10-21）https://valueaddvc.com/blog/scale-ai-valuation-what-the-data-labeling-company-is-worth-after-the-meta-deal ——「no new priced round or secondary has been reported since」；營收引 Forbes 2026-05-14。
5. 交割前次級價（Business Insider 經 Reuters，2025-03-28）https://www.marketscreener.com/quote/stock/META-PLATFORMS-INC-10547141/news/Scale-AI-seeking-valuation-as-high-as-25-billion-in-potential-tender-offer-Business-Insider-report-49470566/ ——「seeking a valuation as high as $25 billion in a potential tender offer」（未證成交）。
6. 交割後營運事件：TechRepublic（裁員）https://www.techrepublic.com/article/news-scale-ai-layoffs/ ；同層私有估值：Mercor 約 10（parsers.vc）https://parsers.vc/news/251028-ai-leader-mercor-reaches-10-billion/
7. 待測一指名讀：Forbes 2026-05 Scale 營收原文；Meta 電話會（3Q26，2026-10 下旬）就 Scale 之任何陳述；INOD／TaskUs 10-Q（同層上市倍數之分母）。

缺段（§7-2）：Scale 經審計財報（無）、Meta 自身對 Scale 之採購額、可觀察交易；本輪只讀上列；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 衡量替代法本即以成本承載；無可觀察交易且定性指標未觸發時不調整，屬 GAAP 正常，不是錯價 | 載體 1 關鍵會計估計 | 恆等無落差 |
| R2 | 同層私有估值上行（Mercor 約 10）、Scale 營收仍成長、多數實驗室回流（Forbes 2026-05 引 Droege），減損指標不成立 | 載體 4、6 | 方向若有亦偏上 |
| R3 | Meta 對 Scale 之投資含人才取得（Wang 入 Meta）之策略價值，市場不以財務帳面評價 | 載體 4 | 讀者本不讀此帳面 |
| R4 | 量級：13.80 ÷ Meta 總資產 478.8 `[D]` 約 2.9%；任何調整對 Meta 為非重大 `[A]` | 載體 2 | 終端條件，本輪不篩（§7-3），僅列 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法自 Meta 申報（10-K／10-Q／8-K／電話會原文）確認 Scale 持股之現行帳面仍在衡量替代法且未經任何調整（3Q26 不逐名，若 FY2026 10-K 前無其他原文可定）；或
(2) 可運作對照只能寫成 L8-I#2（客戶流向）、L13-I（股權 vs 應收）或一般之「非上市股權以成本承載」而無標註層特有之結構（投資人兼主要客戶、成本 ÷ 營收與同層上市主體之可比性）；或
(3) 具名賣方、評等機構或 Meta 已公開評估該持股之公允值或減損可能（已定價）；或
(4) `[D]` 量級：在最不利之可觀察價格情境（以交割前次級 25 為下緣或同層上市倍數重算）下，調整額 < Meta 年度稅前淨利 1%，且同層無其他上市主體承載同型持股；或
(5) 12 個月內無可觀測驅動：無新定價輪、次級、IPO 申報或減損評論之時點可指名。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：非上市股權（衡量替代法）、利息及其他收益（淨額）中之未實現損益、關聯交易揭露。2. 可交易工具：持股方或同層上市標註商（不選）。3. 半衰期：可觀察交易之到來時點 vs ≥ 12 個月窗。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L8［A］格加「#4 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0089。不改 L8-A#1–#3、L8-I／#2／#3、L8-P、C-I2、L13-I 結論。
