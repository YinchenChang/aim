# L15-I#2 生成卡｜基礎設施軟體與資料：誘因（雲端商共同出資之中立相容開源引擎——授權防線與託管定價權）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/FILEIDS.tsv；archive/drive/USED_20261007_L15-I_generate_GK.md；archive/drive/USED_20261007_L15-I_test1_GK.md；archive/drive/USED_20261002_L11-I_generate_GK.md；archive/drive/USED_20261001_L10-I_generate_GK.md | EMITS: work/20261014_L15-I#2_generate_CL.md -->
**日期：** 2026-10-14　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3→4／6）　**格：** L15-I　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 全表已測（L15-A#2 本日測一，Q-0042 done）。非已殺／刻意排除、無 #2 之格只剩 L15-I（最後測一 2026-10-07T11:25Z，`archive/FILEIDS.tsv`）；同上一輪 SCOUT 對 L15-A 之選法 → **L15-I**，#2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `open source license`、`OpenSearch`、`Valkey`、`DocumentDB`，命中 0 筆。
- 比對（本卡須異型）：
  - **L15-I#1**（測一不通過，`archive/drive/USED_20261007_L15-I_test1_GK.md`）：遙測出站費使取用權為結構性；死因＝出站費率與保留期與權利型態句不可同頁並列。本卡不涉資料出站，主體為**軟體授權**與**雲端商之託管替代品定價**。
  - **L5-I**（已測｜不進 T）：雲層出站／切換費之法定上限。本卡非法規、非雲層切換費。
  - **L15-P#2**（市集抵扣）、**L15-A#1**（使用量×單價）、**L15-A#2**（遞延收入浮存）：本卡不拆營收、不涉承諾池與開票。
  - **L12-I#2**（IP 補償＝零保費賣權）：法律責任，非授權選擇。**L10-I**（預設份額義務）：分發層法定義務，非開源授權。**L11-I**（代理議價取用權）：注意力層。**L7-P#2**（資料存量授權）：訓練資料，非軟體。
  - 已殺 L8-P／L9-P／L11-P、C-A1–C-A5、C-I1–C-I5：不涉。
- §7-10 領域最近公開：ESTC 10-Q 1Q FY27（2026-07-31 季）；MDB 10-K FY26（2026-01-31）；LF DocumentDB 公告 2025-08-25；AWS ElastiCache Valkey 公告 2024-10-08。

## 1. 落差一句

種子主張：雲端商（AWS、Google、Microsoft）之誘因不是逐案分叉，而是**共同出資中立基金會下之相容引擎**（Valkey 2024-03、OpenSearch 基金會、DocumentDB 2025-08 入 LF，MIT），並以低價託管（ElastiCache Serverless for Valkey「priced 33% lower」）把相容層變成預設；ISV 之授權回應（Elastic 2024-08 加 AGPL、MongoDB 守 SSPL）防不住 API 相容之替代，託管定價權之上界由雲端商之相容品報價決定。錯價只在把授權回歸開源當成護城河修復。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因**：雲端商選擇「自建相容引擎＋中立治理」之成本 < 向 ISV 分潤；ISV 選擇授權（SSPL／ELv2／AGPL）以阻擋第三方託管。相容品成立後，ISV 託管服務之價差上界 ≈ 雲端商相容品折讓 |
| 量綱 | 價差（%，無量綱）；ISV 託管營收占比（%）；月付雲（隨需）vs 年約雲成長差（百分點） |
| 選擇變數 | 雲端商：是否出資相容引擎、託管定價；ISV：授權條款；客戶：引擎選擇 |
| 可見端 | ESTC 10-Q 營收分類（Annual／Monthly Elastic Cloud 分列）；ESTC／MDB 10-K 授權與競爭風險段；AWS 定價公告；LF 公告之參與者名單 |
| 指名不可見端 | 客戶由 ISV 託管轉相容引擎之流失額；雲端商相容品營收 |
| 表達工具型態（只指名） | 美股可交易之開源起家資料基礎設施 ISV。不選券 |

**不主張方向、不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Elastic 10-Q 1Q FY27 https://www.sec.gov/Archives/edgar/data/1707753/000170775326000054/estc-20260731.htm （sec.py 實讀）：「Annual Elastic Cloud $ 185,003 39 % $ 145,912 35 % Monthly Elastic Cloud 50,202 10 % 49,862 12 %」（千美元；本季 vs 去年同季）——月付雲持平、年約雲 +27%。
2. Elastic 10-K FY26 https://www.sec.gov/Archives/edgar/data/1707753/000170775326000018/estc-20260430.htm ：「we develop the majority of our software in public repositories under an open source GNU Affero General Public License v3 (“AGPL”)」；grep `OpenSearch` 0 筆（檢索失敗，非不存在）。
3. MongoDB 10-K FY26 https://www.sec.gov/Archives/edgar/data/1441816/000162828026016799/mdb-20260131.htm ：「Our decision to offer Community Server under the Server Side Public License (“SSPL”) may harm the adoption」；競爭段「bundle competing products with … their cloud computing」；grep `DocumentDB` 0 筆。
4. Linux Foundation 2025-08-25 https://www.linuxfoundation.org/press/linux-foundation-welcomes-documentdb-to-advance-open-developer-first-nosql-innovation ：MIT；「compatible with the popular open source MongoDB drivers」；參與者含 AWS、Google、Microsoft、Snowflake 等。
5. AWS Database Blog 2024-10-08 https://aws.amazon.com/blogs/database/amazon-elasticache-and-amazon-memorydb-announce-support-for-valkey/ ：「ElastiCache Serverless for Valkey is priced 33% lower than ElastiCache Serverless for Redis OSS」；「node-based ElastiCache for Valkey is priced 20% lower」。
6. Elastic AGPL 公告 2024-08-29 https://www.businesswire.com/news/home/20240829537786/en （未實讀，只指名）。

缺段（§7-2）：未取 ≥ 4 期 Monthly／Annual Elastic Cloud 序列；未取 OpenSearch／DocumentDB 託管價目與 ESTC／MDB 託管價目同口徑；未取任何 ISV 申報或電話會將流失歸因於相容引擎之原文；Redis 私有（不可交易）。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 年約雲 +27% 顯示企業客戶不因相容品流失；月付雲持平可由 Elastic 自身推年約／市集轉換解釋 | ESTC 10-Q（§3-1） | 可分離性 |
| R2 | 相容僅及 API 子集；ISV 之向量檢索、AI 功能不在相容層，價差不封頂 | 待測一指名 | 機制不成立 |
| R3 | OpenSearch／Valkey 分叉已逾 2–5 年，市場已定價 | 待測一指名賣方 | 已定價 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法就 ≥ 1 家美股上市 ISV 取得 ≥ 4 期託管營收分類（如 ESTC Annual／Monthly Elastic Cloud）並列，且無法就 ≥ 1 組（ISV 託管 vs 雲端商相容品）取得同口徑價目原文；或
(2) 可運作對照只能寫成出站／保留期（L15-I#1）、雲層切換費（L5-I）、使用量×單價（L15-A#1）、市集抵扣（L15-P#2）或 IP 補償（L12-I#2）；或
(3) 具名賣方已量化相容引擎對 ESTC／MDB 託管價差或流失之影響並為市場所引用（已定價）；或
(4) `[D]` 量綱不可連接：相容品可替代之營收占 ISV 營收 < 10%，或 R1 成立（申報層無法把月付雲變化歸因於相容替代）；或
(5) 12 個月內無可觀測驅動：無授權變更、無相容引擎新版／新託管、無雲端商定價變動。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：託管雲營收分類、NRR、毛利率。2. 可交易工具：開源起家資料 ISV（不選）。3. 半衰期：年約續約週期與相容引擎發版週期。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L15［I］格加「#2 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0043。不改 L15-I#1、L15-A#1／#2、L15-P#1／#2、L5-I、L12-I#2、L10-I、L11-I、L7-P#2 結論。
