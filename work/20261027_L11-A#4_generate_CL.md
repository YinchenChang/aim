# L11-A#4 生成卡｜人類注意力：會計恆等（累積內容存量之貨幣化池耗竭：儲存訂閱數 S_t ≡ 既有超額存量池 N₀ 之累計轉換 ＋ 新增超額流量；有限池一次性轉換使 Other Revenue 成長在池耗竭／週年後機械收斂）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261001_L11-A_generate_GK.md；archive/drive/USED_20261001_L11-A_test1_GK.md；archive/work/20261013_L11-A#2_generate_CL.md；work/20261013_L11-A#2_test1_CL.md；archive/work/20261020_L11-A#3_generate_CL.md；work/20261020_L11-A#3_test1_CL.md；archive/drive/USED_20261001_L10-A_generate_GK.md | EMITS: work/20261027_L11-A#4_generate_CL.md -->
**日期：** 2026-10-27　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 0→1／6）　**格：** L11-A　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。非已殺／刻意排除格中最後測試日最舊＝2026-10-20（L11-A、L11-I、L13-P、L13-I、L14-P）；依表序取 **L11-A**。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `tokenomics_leads.py Snap infrastructure DAU`＝命中 0；未用。載體全由本輪 sec.py／WebSearch／WebFetch 實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L11-A#1**（曝光 × 單價，流量恆等；死因＝兩因子水準不可並列）：本卡非價量拆解，為**有限存量池之轉換恆等**。
  - **L11-A#2**（內容資產攤銷估計；死因＝驅動無可觀測證據）：本卡無會計估計。
  - **L11-A#3**（訂閱預收遞延滯後；死因＝公司指引已自供收斂、滯後 ≤ 4 季 < 12 個月窗）：本卡不主張認列滯後；主張池耗竭與寬限期到期之**兩段**事件（2026-09 起寬限到期、2027-2H 週年），窗口跨 ≥ 12 個月。測一須驗此差異是否實質，否則依 (4) 殺。
  - **L11-I#1–#3**（條款權利、版稅池、兌現率分級）：不涉。**L11-P**（ARCH_dead #3）：不恢復。
  - **L10-A#1**（轉介量 × 分潤率）、**L10-I#2**（App Store 佣金路由）：不同恆等；交易處理費只作成本項，不為落差。
  - **L15-A#2**（遞延收入開票條件）、**L5 系列**（儲存硬體需求）：本卡之「儲存」為消費者付費存量，非硬體位元需求；重疊不構成丟棄。
- §7-10 領域最近公開：Snap 2Q26 10-Q（申報 2026-08-04）與 8-K 2Q26 prepared remarks（2026-08-03）。下一檢查點＝3Q26 10-Q／法說（約 2026-11 初，日期待測一確認）。

## 1. 落差一句

Snap 2Q26 Other Revenue $316M（+85%），公司歸因「Snapchat+, Memories Storage, and Lens+」，1Q26 10-Q 明言「partially attributable to Memories Storage Plans」；Memories Storage 於 2025-09-26 對既有 >5GB 存量開徵，並給「12 months of temporary Memories storage」。若此段成長部分來自**一次性轉換十年累積之超額存量池 N₀**（加寬限到期之第二波），則 S_t ≡ ΣΔconv(N₀) ＋ new-overcap flow 要求其增量於池耗竭後退回至新增超額流量之速率；種子主張：若市場或公開模型把 Other Revenue 成長外推為 AI 創作工具帶動之持續訂閱，錯價只在把存量轉換讀成流量。本卡不主張方向與量級，只立可拒絕之「Other Revenue 增量中 Memories 存量轉換份額可界定，且於 2027 收斂」。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等（A）**：\(S^{mem}_t ≡ c_t·N_0 + Σ f_τ\)（\(c_t\)＝既有池累計轉換率，上界 1；\(f\)＝新增超額使用者流量）；Other Rev ≡ Σ_產品 訂閱數 × 實現單價（按比例認列）；成本側 infra 含儲存，未付費者刪除／匯出則儲存成本降 |
| 驅動（因果層，§7-5） | 使用者對累積注意力產物（照片／影片 Memories）之保存付費意願；寬限期到期時之付費 vs 刪除選擇；AI 創作工具（Lens+）為競爭解釋 |
| 量綱 | Other Revenue［美元／季］；訂閱者數［人］；Memories 儲存量［GB／人］；infra 成本［美元／季］ |
| 可見端 | 10-Q／10-K Other Revenue、MD&A 增量歸因句、CODM 分部費用表 Infrastructure costs；prepared remarks 訂閱者數、run-rate；newsroom 方案條款 |
| 指名不可見端 | 各訂閱產品收入拆分、Memories 方案訂閱者數、>5GB 使用者數 N₀、寬限到期後之轉換／刪除率 |
| 外部參照物（測一查證） | Google Photos 2021-06 終止免費無限儲存、iCloud／Google One 之存量轉換訂閱曲線（具名一手或研究） |
| 表達工具型態（只指名，不選券） | 美股上市社群平台普通股；不選券 |
| 重疊 | L11-A#3（訂閱）、L10-I#2（應用商店費）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Snap 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1564408/000156440826000052/snap-20260630.htm ：「a $145.1 million and $278.1 million increase in other revenue … due to higher subscription revenue from growth in the number of subscribers, attributable to new subscription products」；「Other revenue primarily consists of revenue from subscriptions, which include Snapchat+, Lens+, and Snapchat Platinum … We also generate subscription revenue from Memories Storage Plans」；分部表 Revenue 1,598,993 vs 1,344,930、Infrastructure costs 403,464 vs 393,257、Content and developer partner costs 115,112 vs 152,432（千美元）；DAU 493M（+5%）、ARPU $3.25 vs $2.87。
2. Snap 10-Q 1Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1564408/000156440826000027/snap-20260331.htm ：「a $133.0 million increase in other revenue … due to higher subscription revenue from growth in the number of subscribers, partially attributable to Memories Storage Plans」。
3. Snap 8-K 2Q26 prepared remarks（sec.py）https://www.sec.gov/Archives/edgar/data/1564408/000156440826000047/q22026preparedremarks.htm ：「Snapchat+, Memories Storage, and Lens+ helped drive 85% year-over-year growth in Other Revenue to $316 million in Q2. Less than 3% of our monthly active users are paying subscribers」；FY infra 指引 $1.65–1.70B（前 $1.60–1.65B），「additional investment in the AI and machine learning infrastructure needed to support revenue growth」。
4. Snap newsroom（2025-09-26）https://newsroom.snap.com/snap-memory-storage ：5GB 門檻；「100GB, 250GB with Snapchat+, or 5TB with Snapchat Platinum」；「We'll provide 12 months of temporary Memories storage for any Memories that exceed the 5GB storage limit」；到期後處置未載。
5. Snap newsroom（2026-02-18）https://newsroom.snap.com/snap-1b-direct-revenue-25m-subscription ：訂閱者「surpassed 25 million」、直接收入「exceeded a $1B annualized revenue run rate」。
6. Subscription Insider（2026-08-04）https://www.subscriptioninsider.com/blog/snap-s-other-revenue-jumps-85-as-it-adds-more-ways-for-users-to-pay-news ：無 Memories 分列、無分析師可持續性評論——二手，只作線索。

缺段（§7-2）：Memories 方案訂閱者或收入分列；N₀；寬限到期處置之一手條款；具名賣方 Other Revenue 2027 模型與其驅動假設；3Q26 實際值。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 公司未分列 Memories；Other Revenue 由 Snapchat+／Lens+ 主導，存量轉換份額小到不改總量 | #1、#3 | 不可分離／不重大 |
| R2 | 儲存為持續性需求（照片每年新增），轉換後留存＝經常性，非一次性 | #4 | 恆等驅動錯置 |
| R3 | 賣方已以訂閱者數 × ARPU 建模並預期成長放緩 | 待測一具名 | 已定價 |
| R4 | 寬限期到期多數使用者刪除或匯出而非付費，第二波不存在 | #4 未載處置 | 事件不成立 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 公司或具名賣方已明示 Memories 轉換為一次性／已量化其份額，且 2027 Other Revenue 指引或共識已反映收斂——已定價（R3）。
(2) 實讀 1Q25–3Q26 申報後，Memories 份額無任何可界定上下界（無分列、無訂閱者數、無方案價），使 `[D]` 份額區間寬於 [0, 1] 之一半——不可分離（R1；C-A1 型死因）。
(3) 重定價窗（≥ 12 個月）內無可觀測之收斂事件（寬限到期之處置、週年 YoY），或其已於窗前全部公告。
(4) 可運作對照只能寫成訂閱者 × 單價（L11-A#1 型）、認列滯後（L11-A#3 型）或應用商店費路由（L10-I#2 型）。
(5) 公司原文把 Other Revenue 增量主因歸於 AI 創作工具（Lens+）或 Snapchat+ 新功能並量化，使驅動層不在存量池。

複查觸發器（若日後殺）：Snap 首次分列 Memories 訂閱者或收入；寬限期處置條款公布；任一具名賣方以存量池耗竭建模 Other Revenue。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Other revenue、MD&A 增量歸因句、Infrastructure costs、Deferred revenue。
2. 可交易工具：社群平台普通股。不選券。
3. 半衰期：寬限到期約 2026-09 起；週年對比 2026-4Q 起至 2027-3Q。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0117；`query/ARCH_matrix.md` L11［A］標「#4 已生成」；`export/LEADS_算力收支.md` 一筆（Snap infra 指引）。不寫入：FUNNEL（載入量 29,831 B，留給測一）、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L11-A#1–#3、L11-I#1–#3、L11-P、L10-A、L10-I#2、L15-A#2 結論；不寫 T-15。
