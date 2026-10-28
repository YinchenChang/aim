# L13-I#4 生成卡｜資本與融資結構：誘因（買方監理資本計提誘因：資料中心 SPV／租約支撐債之邊際買方若為 RBC 受限之壽險，其選擇依「利差 ÷ NAIC 指定等級所對應之資本計提」最大化，而非依利差所含風險——評等帶內之利差溢價是監理資本套利之價格，NAIC 指定制度變動即改變邊際買方）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261002_L13-I_generate_GK.md；archive/drive/USED_20261002_L13-I_test1_GK.md；archive/work/20261013_L13-I#2_generate_CL.md；work/20261013_L13-I#2_test1_CL.md；archive/work/20261020_L13-I#3_generate_CL.md；work/20261020_L13-I#3_test1_CL.md；archive/work/20261028_L13-P#4_generate_CL.md；archive/work/20261026_L13-A#4_generate_CL.md；archive/work/20261011_L4-I#2_generate_CL.md | EMITS: work/20261028_L13-I#4_generate_CL.md -->
**日期：** 2026-10-28　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 3→4／6）　**格：** L13-I　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L13-P#4 本日測一，Q-0119 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-20（L13-I#3、L14-P#3）；依表序取 **L13-I**。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `insurer`、`private credit`、`SPV`、`Hyperion`＝0 筆；未用。載體全由本輪 WebSearch／WebFetch 實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L13-I#1**（供應商兼股東／債權人之私有資訊 → 公開信評**資訊含量**；死因＝應收帳齡與股權餘額不可並列）：本卡不論評等是否準確；評等只作**買方資本計提之輸入**，選擇者為買方投資長。
  - **L13-I#2**（擔保人兼股東之違約分支選擇；死因＝終止費 F 遮蔽）：本卡不涉擔保人分支。
  - **L13-I#3**（發行人依機構債務含量選工具；死因＝公司已事前公告組合）：#3 之選擇者為**發行人**、約束為機構槓桿觸發線；本卡選擇者為**買方**、約束為 NAIC 指定等級 → RBC 因子。
  - **L13-A#1**（表外義務上界／RVG）：本卡不估 RVG 是否足額，RVG 只作評等之來源；**L13-A#4**（可轉債全成本）、**L4-I#2**（客戶認股權證）：不涉。
  - **L13-P#4**（OpenAI 跨供應商現金守恆）：本卡不涉對手方預算。
  - **C-A4／C-A3**（ARCH_dead #4–5，表達窗／折舊樞紐）：不以殘值、年限、`k` 為樞紐；不重開。**L11-P**：不恢復。不寫 T-15。
- §7-10 領域最近公開：NAIC 2026 Summer National Meeting（Willkie 2026-08-25 摘要）；NAIC 私信評報告 2026-09-23（Forbes 轉述）；Moody's 壽險 AI 曝險報告（Bloomberg 經 Royal Gazette 2026-10-25）；Hyperion 債價 94.4（Protos 2026-09-23）。下一檢查點＝NAIC Fall National Meeting（2026-11）、上市壽險 3Q26 10-Q、年底 2026 法定報表新揭露（2027 初）。

## 1. 落差一句

市場把資料中心 SPV／租約支撐債（Meta Hyperion「Beignet」27.3 bn、A+、T+225bp、Meta 自身 AA-／Aa3）相對發行人自身曲線之利差溢價讀成「結構複雜與流動性之補償」，並把美國壽險持有之數位基礎設施債（Moody's：2026-06 末 39.5 bn，半年 +34%）讀成對 AI 信用之看法；種子主張：對 RBC 受限之壽險，資產選擇之目標函數是**利差 ÷ 指定等級資本計提**，同一評等帶（NAIC 1.x）內利差最高者即最適——故此類債之利差溢價在評等帶內由「壽險資本套利需求」定價，而非由違約／回收差定價。可拒絕之主張＝(i) 此類交易之壽險（含資管母公司之保險帳）持有占比足以成為邊際買方；(ii) NAIC 指定制度之變動（SVO 對 filing-exempt 評等之裁量 2026-01-01 生效、已運作；SSAP No. 26 對 ABS 結構之債券分類修訂 2026-10-02 截止意見；年底 2026 新揭露）會改變邊際買方，從而改變表外資料中心融資之成本。本卡不主張利差方向、不主張任何評等錯誤。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因（I）**：壽險 i 選資產 a，max \((s_a − EL_a)/(c(d_a)\cdot κ)\)；\(d_a\)＝NAIC 指定等級（由 CRP 評等 filing-exempt 或 SVO 決定），\(c(d)\)＝RBC 因子，κ＝目標 RBC 比。同一 \(d\) 下 \(s\) 高者勝；若 \(d\) 被 SVO 下調或分類改為非債券，\(c\) 跳升，需求轉移 |
| 選擇者 | 壽險投資長（及其資管母公司：Apollo／Athene、KKR／Global Atlantic、Brookfield 等之保險帳） |
| 驅動（因果層，§7-5） | NAIC 指定制度（filing-exempt、SVO 裁量、SSAP 26 債券定義、RBC 因子）；壽險負債端成長（年金）所需之利差資產量 |
| 量綱 | 利差［bp］；RBC 因子［% 面額］；持有額［美元］；持有占比［比率］ |
| 可見端 | 交易定價利差與評等（IFR 等）；Moody's／NAIC 之壽險曝險統計；上市壽險 10-K／10-Q 與投資組合簡冊（Athene Asset Compendium）；NAIC 會議紀錄與 SAPWG／VOSTF 議案 |
| 指名不可見端 | 各交易之持有人分布（144A 私募，無公開登記）；私信評（PLR）之內容；壽險對單一交易之 NAIC 指定等級（年底法定報表 Schedule D 可逐券查，測一驗可得性） |
| 外部參照物（測一查證） | NAIC 指定套利已被監理處置而致利差重估之具名前例（如 CLO 夾層／組合票據 2023–2024 SVO 與 RBC 修訂、私信評 2024 Discretion Amendment 前後之利差變化） |
| 表達工具型態（只指名，不選券） | 美股上市另類資管（有保險帳者）與壽險普通股；超大雲母公司普通股；不選券 |
| 重疊 | L13-I#1（評等，但角色不同）、L13-I#3（評等約束，但選擇者不同）、L13-A#1（RVG）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. IFR（2025-12-17）https://www.ifre.com/ifr-awards/2327933/financing-package-blue-owl-capitalbeignet-investors-us27.3bn-23.6-year-bond ：Beignet 27.3 bn、10-16 定價「Treasuries plus 225bp」、S&P A+（「one notch below Meta's Aa3/AA–」）、「low double-digit number of investors」、Pimco 為主錨。
2. IFR（2025-12-17）https://www.ifre.com/ifr-awards/2340435/the-metablue-owl-deal-broken-down-off-balance-sheet-gymnastics-24-years-after-enron ：RVG 16 年、最後四年以終止費覆蓋；租約四年不可撤銷、選擇權至約 20 年；投資人得「spread pickup to Meta's own long bonds」（未給 bp）。
3. Protos（2026-09-23）https://protos.com/metas-ai-bond-just-hit-a-record-low-as-its-stock-soared/ ：票息 6.581%、2049 到期；價 94.4（高點約 110）；Pimco 約 18 bn、BlackRock 逾 3 bn。
4. Royal Gazette／Bloomberg 轉述 Moody's（2026-10-25）https://www.royalgazette.com/reinsurance/business/article/20261025/life-insurers-investment-exposure-to-ai-spikes-24/ ：壽險 AI 相關投資 85.2 bn（+24%）；hyperscaler 債 32.2 bn（約占其流通債 6.6%）；數位基礎設施債 39.5 bn（+34%）；非投資級占比 4.7%→6.1%。
5. Forbes（2026-10-08）https://www.forbes.com/sites/daraabasiita/2026/10/08/ai-debt-is-flowing-into-assets-insurance-regulators-struggle-to-track/ ：NAIC 2026-09-23 報告——私信評債約 512 bn（2025 末）；Athene 2025 末資料中心貸款 1.4 bn／商用抵押 42 bn、ABS 54 bn 中資料中心約 1%、私信評資產約 13%；NAIC 新揭露首見於年底 2026 法定報表。
6. Willkie（2026-08）https://www.willkie.com/publications/2026/08/naic-report-2026-summer-national-meeting ：「While the amendment was effective January 1, 2026, its implementation depended on developing technology enhancements … now complete, and the process is operational」；SSAP No. 26 擬排除含重大內嵌 ALM 風險之 ABS 結構於債券分類（意見截止 2026-10-02）；CLO RBC 因子年底 2026 生效。
7. KBRA（2026-06）https://www.kbra.com/publications/NqqwYmxw ：2024-08 Discretion Amendment 授權 SVO 挑戰評等；原定 2026-01 實施「has been delayed」（與 #6 之「operational」時序不一，測一以 NAIC 一手對齊）。

缺段（§7-2）：Meta 同期長債利差（一手）；各資料中心 SPV 交易之壽險持有占比；NAIC 1.D／1.E 等 RBC 因子一手值；SVO 是否已挑戰任何資料中心交易之評等。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | Hyperion 之主錨為 Pimco 共同基金（GIS 基金按 94.5 計價）與 BlackRock，非 RBC 受限壽險；邊際買方不受 RBC 約束 | #1、#3 | 選擇者錯置 |
| R2 | 壽險數位基礎設施債僅占現金與投資資產約 1.4% 量級之一部分；需求面太小，不足以定價 | #4 | 量級不足 |
| R3 | 利差溢價可由結構解釋：RVG 不覆蓋最後四年、租約四年可不續、144A 流動性差、債價自 110 跌至 94 顯示市場已重估風險 | #2、#3 | 競爭假說（風險定價） |
| R4 | 監理已在處置（SVO 裁量、SSAP 26、年底新揭露），套利已為公開資訊 | #5、#6 | 已定價 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後 **< 2 筆**具名資料中心 SPV／租約支撐交易可同時取得：評等、定價利差、發行人（或承租方）同期可比曲線利差——評等帶內利差溢價不可量測。
(2) 壽險（含資管母公司保險帳）於此類交易之持有占比無任何一手或具名機構數，或可得之數 < 25%（R1 成立：邊際買方非 RBC 受限）。
(3) 具名賣方、評等機構、NAIC 或監理機構已量化「NAIC 指定 → RBC → 資料中心債利差」之鏈並公開——已定價（R4）。只點名「監理關注私募信用」不算。
(4) 重定價窗（≥ 12 個月）內無可觀測檢驗事件（NAIC Fall 2026 會議決議、SSAP 26 定案、SVO 首次挑戰資料中心評等、年底 2026 法定報表逐券指定等級、上市壽險 10-Q 資料中心持有揭露），或其已全部於窗前公告。
(5) 可運作對照只能寫成評等資訊含量（L13-I#1 型）、發行人工具選擇（L13-I#3 型）、RVG 表外上界（L13-A#1 型）或對手方信用利差，而非買方資本計提誘因。

複查觸發器（若日後殺）：NAIC 或 SVO 公開挑戰任一資料中心 SPV 評等或改其債券分類；上市壽險首次分列資料中心 SPV 持有與指定等級；具名機構量化壽險占此類交易之持有比。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：壽險投資組合按 NAIC 指定等級分布、Schedule D 逐券、RBC 比；另類資管之保險帳利差收益（spread related earnings）。
2. 可交易工具：上市另類資管與壽險普通股、超大雲母公司普通股。不選券。
3. 半衰期：NAIC 每年三次會議；法定報表年度；交易定價事件不定期。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0120、Q-0119 已 done；`query/ARCH_matrix.md` L13［I］標「#4 已生成」；`export/LEADS_算力收支.md` 追加 2 筆（Beignet 定價、Moody's 壽險數位基礎設施債；均二手）。不寫入：FUNNEL（留給測一）、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L13-I#1–#3、L13-P#1–#4、L13-A#1–#4、L4-I#2、C-A3／C-A4 結論；不寫 T-15。
