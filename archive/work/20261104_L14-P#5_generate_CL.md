# L14-P#5 生成卡｜企業終端需求：守恆（企業 AI 推論工作量之放置守恆：`W_ent ≡ W_pub + W_priv`——同一份企業推論工作量在公有雲／API 與私有雲／自建 AI 伺服器之間分配；「回遷」使私有端之 AI 伺服器出貨與公有端之企業推論營收互為替代，兩端之企業 AI 需求成長不可相加）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/RETRIG_5.md；archive/work/20261104_L13-I#5_generate_CL.md；archive/work/20261013_L14-P#2_generate_CL.md；archive/work/20261020_L14-P#3_generate_CL.md；archive/work/20261028_L14-P#4_generate_CL.md；work/20261028_L14-P#4_test1_CL.md | EMITS: work/20261104_L14-P#5_generate_CL.md -->
**日期：** 2026-11-04　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 3→4／6）　**格：** L14-P　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L13-I#5 本日測一，Q-0161 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-28（L14-P#4、L14-A#4、L14-I#4；L13-I#4 已於本日以 #5 更新）；依表序取 **L14-P**。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `repatriation on-prem enterprise inference`，命中 11 筆皆 GPU TCO／吞吐列（SRC_DC_012、SRC_PERF_*），與企業放置無關，相關命中 0；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L14-P#1**（席次 ≤ 員工數；死因＝同一 10-K 付費席次與員工數不可並列）：不涉席次、員工數。
  - **L14-P#2**（預付容量承諾池，美元／credit；死因＝滾存條款 ≥ 2 家不可得）：本卡守恆量為**工作量**（推論 token／GPU 時），不是合約美元池；RPO 只作公有端之旁證。
  - **L14-P#3**（客服人工處理量 H ≡ V(1−a)）：不涉人工時；AI 不作替代人工之機制。
  - **L14-P#4**（企業端點裝機量存量—流量；死因＝否決 (2)，D_t 為負／前拉）：本卡不是跨期替換，是**同期跨場所之分配**；不以壽命、機齡為樞紐。
  - **L14-A／#2–#4**（支出比重、會計分流）、**L14-I／#2–#4**（採購、揭露誘因）：本卡不以預算比重或誘因為樞紐；放置選擇之成因（成本、主權、治理）只作外生輸入。
  - **L6-P／#2–#5**（雲端層守恆，含 RPO 之電力-時間預算 ρ）：本卡之選擇者為企業買方、守恆在需求端工作量之分配，不在雲端供給之電力-時間；重疊不構成丟棄。
  - **C-A2**（ARCH_dead，企業預算單位經濟）：不主張每單位毛利。**L11-P／L8-P／L9-P**：不恢復。不寫 T。
- §7-10 領域最近公開：Dell 10-Q 期末 2026-07-31（2026-09-08）；Microsoft 10-Q 期末 2026-09-30（2026-10-28）；Cloudera／Wakefield 調查 2026-08-11；Broadcom Private Cloud Outlook 2026-06-09。下一檢查點＝Dell 3Q FY27 10-Q（約 2026-12）、HPE FY26 10-K（約 2026-12）、各雲 4Q26 財報（2027-01／02）。

## 1. 落差一句

市場同時把 OEM 之 AI 伺服器出貨（Dell AI-optimized servers 季收 164 億美元、年增約 1 倍）中之「企業」部分與超大規模雲／模型 API 之企業推論營收讀成**兩條各自成長之企業 AI 需求**；種子主張：企業推論工作量 `W_ent` 於任一期只能放在一處，`W_ent ≡ W_pub + W_priv`——當企業「回遷」（Cloudera 調查 66% 稱過去 12 個月曾把 AI 工作量移回私有／本地；Broadcom 調查 56% 正或計畫於私有雲跑生產推論）時，私有端出貨之增量有一部分是公有端企業推論之**替代**，非新增。可拒絕之主張＝(i) 兩端之企業份額可分別量到 ≥ 2 期；(ii) 私有端份額上升時公有端之企業推論成長同期放緩（替代彈性 ≠ 0）；若兩端同時加速且無份額轉移，或私有端成長全來自新工作量（W_ent 擴張主導），本卡死。本卡不主張任何公司營收或股價方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **守恆（P）**：`W_ent,t = W_pub,t + W_priv,t`；`s_t ≡ W_priv/W_ent`；`ΔW_priv = s·ΔW_ent + W_ent·Δs`——第二項為自公有端之轉移（零和）。工作量單位＝推論 token 或 GPU 時；私有端由已部署 AI 伺服器之可用 GPU 時 × 利用率上界 |
| 選擇者 | 企業買方（放置決策：成本、資料治理、主權、延遲） |
| 驅動（因果層，§7-5） | 公有端單位推論價格 vs 自建 TCO；資料治理要求；GPU 供給排程（OEM 交期） |
| 量綱 | token／期、GPU 時／期；無因次份額 s；美元只作代理（營收 ÷ 單價） |
| 可見端 | OEM 10-Q AI 伺服器營收與 backlog（Dell、HPE）；企業／主權／neocloud 客群揭露（若有）；雲端 10-Q Azure 等成長率、RPO；調查機構之放置份額（Cloudera、Broadcom、IDC） |
| 指名不可見端 | `W_ent` 之絕對值；OEM 出貨之企業 vs neocloud／主權拆分；私有 AI 伺服器之利用率；公有端營收中企業推論 vs 訓練／消費者之拆分 |
| 外部參照物（測一查證） | 2010s 中後期「cloud repatriation」（Dropbox 2016–2017 自建，S-1 揭露基礎設施成本變化）——工作量自公有遷出而總量不變之具名前例；反向：2015–2020 企業伺服器出貨停滯而 AWS 高成長（公有端吸收工作量） |
| 表達工具型態（只指名，不選券） | 美股伺服器 OEM 普通股、雲端平台普通股；不選券 |
| 重疊 | L6-P（雲端供給守恆）、L4（運算硬體）、L14-P#2（企業承諾）；重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Dell 10-Q FQ2'27（期末 2026-07-31）https://www.sec.gov/Archives/edgar/data/1571996/000157199626000046/dell-20260731.htm （`sec.py doc --grep` 實讀）：「AI-optimized servers $ 16,401 $ 8,208」（三個月，百萬美元）；「Traditional servers and networking 10,531 4,736」；「resulting in a significant increase in backlog as we exited the quarter」；「there is inherent non-linearity in the timing of demand」；「customers modernize and consolidate their data centers」。10-Q 未分企業／雲客群（`enterprise customers` 0 筆）。
2. Futurum（2026-09-09）https://futurumgroup.com/?p=95253 ：「booked $60.9 billion in AI server orders during Q2 FY 2027 and exited the quarter with $95 billion in AI server backlog」；客戶點名 CoreWeave、Nscale、「corporate clients」、主要 AI 供應商——企業占比未量化。
3. Microsoft 10-Q 1Q FY27（期末 2026-09-30）https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm ：「Commercial remaining performance obligation increased 73% to $677 billion」；「Azure revenue increased 48%」——公有端成長，未分企業推論。
4. VirtualizationReview（2026-08-12；Cloudera／Wakefield，2026-06-05–22，n＝1,500）https://virtualizationreview.com/articles/2026/08/12/cloudera-survey-66-percent-repatriated-ai-workloads-from-public-cloud.aspx ：66%「moved AI workloads from public cloud back to on-premises or private cloud environments during the previous 12 months」；推論放置「Hybrid … 31 percent」。（Campus Technology 2026-08-18 為同一調查，不另計）
5. Broadcom（2026-06-09；Radius Tech，2026-02–03，n＝1,800）https://investors.broadcom.com/news-releases/news-release-details/broadcoms-private-cloud-outlook-2026-reveals-ai-tipping-point ：「56% of enterprises are running or planning to run production AI inferencing on private cloud」vs「41% on public cloud」。（利害方：私有雲供應商）

缺段（§7-2）：OEM AI 伺服器之企業客群營收或出貨占比（一手）；公有端企業推論營收拆分；以工作量（非受訪者比例）計之放置份額 s_t 時間序列；HPE／Supermicro 同期客群揭露（測一以 `sec.py` 實讀）。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | OEM AI 伺服器 backlog 以 neocloud／主權／模型商為主，企業僅小部分；私有端之企業增量相對公有端過小，替代不可量 | #2 | 非邊際 |
| R2 | 調查之「回遷」為受訪者比例（曾移動任一工作量），非工作量份額；利害方調查（Broadcom、Cloudera 皆售私有方案） | #4、#5 | 可觀測性／偏誤 |
| R3 | `W_ent` 擴張遠快於份額轉移（Azure +48%、RPO +73% 與 Dell AI +100% 同時成立）——兩端同時成長，守恆不約束 | #1、#3 | 量級 |
| R4 | 公有端與私有端之替代已為市場共識（「hybrid AI」敘事普遍），已定價 | #4、#5 | 已定價 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後 < 2 家 OEM 或雲平台能於同一申報或具名機構數中分出**企業客群**之 AI 伺服器／AI 推論量（或營收）≥ 2 期——份額 s_t 不可量。
(2) 可得之最佳數據下，`W_ent·Δs` 之轉移項占私有端企業增量 < 20%，或 s_t 於 2025Q4–2026Q3 不升（無回遷）——替代不存在或可忽略（R3）。
(3) 私有端企業份額上升之同期，公有端企業推論成長無放緩（不同期或同向加速），且無一手證據把兩者連結——替代彈性不可辨。
(4) 放置證據只有受訪者比例型調查且全為利害方（R2），無一手申報或第三方工作量數據。
(5) 具名賣方或研究機構已量化「企業回遷 → OEM 企業 AI 伺服器 vs 雲端企業推論營收之替代」並公開——已定價（R4）。只點名「hybrid／repatriation 趨勢」不算。
(6) 重定價窗（≥ 12 個月）內無可觀測檢驗事件（Dell／HPE 季報客群揭露、雲端季報、IDC 企業 AI 伺服器追蹤），或已全部於窗前公告。
(7) 可運作對照只能寫成雲端供給之電力-時間守恆（L6-P 型）、承諾池（L14-P#2 型）、跨期替換（L14-P#4 型）或支出比重（L14-A 型），而非企業推論工作量之跨場所分配。

複查觸發器（若日後殺）：任一 OEM 於 10-K／10-Q 分列企業客群 AI 伺服器營收；任一雲平台揭露企業推論量或營收；第三方（非私有雲供應商）發布以工作量計之企業推論放置份額。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：OEM ISG 之 AI-optimized servers 營收與 backlog 之客群拆分；雲端之 AI 服務營收／RPO 之企業部分。
2. 可交易工具：伺服器 OEM、雲端平台普通股。不選券。
3. 半衰期：季報；OEM 交期（backlog 轉營收約 1–3 季）；年度調查。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0162；`query/ARCH_matrix.md` L14［P］標「#5 已生成」；`export/LEADS_算力收支.md` 追加 2 筆（Dell AI-optimized servers 季營收〔一手〕、Dell AI 伺服器訂單／backlog〔二手〕）。Microsoft RPO／Azure 已在線索檔，不重寫。不寫入：FUNNEL（留給測一）、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L14-P#1–#4、L14-A、L14-I、L6-P 結論；不寫 T。
