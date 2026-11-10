# L6-P#6 生成卡｜雲端與基礎設施服務：守恆（管轄區合格容量之分區守恆：受駐留／主權約束之需求 `D_r^bound` 只能由「位於 r 且營運者合格」之已通電容量 `K_r^elig` 滿足；全球加總平衡 `ΣK_r` vs `ΣD_r` 不等於分區平衡，受約束區之影子價格由 `K_r^elig` 決定，而非全球供需）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260928_L6-P_generate_GK.md；archive/work/20261011_L6-P#2_generate_CL.md；archive/work/20261018_L6-P#3_generate_CL.md；archive/work/20261026_L6-P#4_generate_CL.md；archive/work/20261102_L6-P#5_generate_CL.md；archive/work/20261105_L2-P#6_generate_CL.md；archive/work/20261104_L14-P#5_generate_CL.md；archive/work/20261102_L6-I#5_generate_CL.md | EMITS: work/20261110_L6-P#6_generate_CL.md -->
**日期：** 2026-11-10　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 1→2／6）　**格：** L6-P　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額配置、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L12-I#6 本日測一，Q-0188 done）。非已殺／刻意排除格中最後測試日最舊＝2026-11-02（L6-P#5、L6-A#5、L6-I#5、L7-P#5、L7-A#5 同日）；依表序取第一 → **L6-P**。既有生成 #1–#5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `tokenomics_leads.py sovereign Europe region residency`，**0 筆**；載體全由 WebSearch／web-fetch 子代理／sec.py 原文取得。內部數字（§12）未用。
- 比對（須異型）：
  - **L6-P#1**（T，同步作業 MTTF∝1/N）：可靠度守恆。本卡守恆於**管轄區**間，不涉故障。
  - **L6-P#2**（RPO ≤ ∫ 通電 MW × ρ；(1) ρ 不可界定）：營收上界。本卡不用 RPO、不需 ρ。
  - **L6-P#3**（同一機群於用途間分割）：用途分割、容量可互換。本卡之樞紐為容量**跨區不可互換**（法律＋營運者資格），不論用途。
  - **L6-P#4**（冷卻型態存量）、**L2-P#6**（已出貨未上電存量）：實體／時間差。本卡容量皆已通電，差在**位置與營運者資格**。
  - **L6-P#5**（承諾 GPU 時之轉售槓桿）：合約層。本卡之現貨可在全球轉售，唯受約束需求不能買他區時段。
  - **L14-P#5**（企業工作量公有／私有放置守恆）：放置於部署型態間；本卡於**地理／管轄**間，公有雲內部即可成立。
  - **L12-P#3**（出口管制下出貨地 vs 落地之轉運差額）：硬體流向；本卡為**工作量**不可移出，硬體可自由流入。
  - **L13-P#4**（同一買方跨供應商承諾）、**L6-I#5**（自建／外購排序）：買方側；本卡為需求之法定可服務集合。
  - 重疊列為否決 (5)。
- §7-10 領域最近公開：Silicon Data「H100 Rental Prices by Region (Q3 2026)」（2026-07-31）；歐盟 Cloud and AI Development Act 提案（COM(2026) 502，2026-06；理事會文件 ST-10104-2026）；AWS ESC G6 上線（2026-05-07）。下一檢查點＝Silicon Data Q4 2026 分區報告、CADA 理事會／議會立場、Nebius 3Q26 業績 6-K。

## 1. 落差一句

公開敘事以全球 GW 供需與單一 GPU 租價指數讀算力稀缺或過剩（如 SemiAnalysis 2028 末容量過剩之二手轉述，見 L2-P#6 測一）。**種子主張：受資料駐留／主權約束之工作量只能落在「位於該管轄區且營運者合格」之容量上；`K_r^elig` 是全球容量之小子集（AWS ESC 2026-01 上線時「GPU-based instances are missing entirely」，2026-05 僅 L4 級 G6），故受約束區之價格由區內合格容量決定，全球過剩不傳導、全球短缺則放大。** Silicon Data 已記錄分區價差（Q3 2026 hyperscaler／非 hyperscaler 倍數「roughly 1.6x in the Nordics to roughly 3x in US West」）並明言「workloads with them are, in effect, paying a regional premium」。落差＝市場若以全球平衡外推，將誤估 (i) 合格容量持有者之價格持續性，與 (ii) 合格性定義（如 CADA 主權準則是否把美系「主權雲」計為合格）變動時之斷崖——方向不定。

## 2. 機制型態

| 欄 | 內容 |
|---|---|
| 型態 | **[P] 守恆**：每一受約束 GPU 時只能由 r 區合格容量供給；`D_r^bound ≤ K_r^elig`，超額只能由價格配給或延後，不能由他區補 |
| 守恆式 | `K = Σ_r (K_r^elig + K_r^inelig)`；`D = Σ_r (D_r^bound + D_r^free)`；`D^free` 可跨區套利，`D_r^bound` 不可 |
| 第一原理量 | 約束需求占比 `b_r = D_r^bound ÷ D_r`；合格容量占比 `e_r = K_r^elig ÷ K_r`；合格性規則（位置／營運者總部／員工國籍／法律管轄） |
| 判定量 `[D]` | 緊度比 `θ_r = D_r^bound ÷ K_r^elig`；分區溢價 `π_r = p_r^elig ÷ p_global − 1`（同等級 GPU、同期限）；當全球利用率下滑時 `π_r` 是否不降 |
| 可拒絕事件 | 分區指數顯示受約束區溢價隨全球價同步收斂；合格性規則放寬（美系主權雲被認定合格）；歐盟區合格 GPU 容量大幅上線後溢價未變 |
| 表達工具型態（只指名，不選券） | 美股上市之歐洲區 GPU 雲（Nebius）；超大規模雲之主權區（不可分離）。不選券 |
| 重疊 | L6-P#3（用途分割）、L14-P#5（放置）、L12-P#3（出口轉運）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Silicon Data（Yang Gao，2026-07-31）分區 H100 租價：「Hyperscaler H100 rates fell 26 to 54% by region since Q1 2025」；「Workloads without data-residency constraints can arbitrage that spread」；北歐段「consistent with regional capacity tightness on the non-hyperscaler side」。https://www.silicondata.com/blog/h100-rental-prices-by-region-q3-2026
2. Silicon Data（Carmen Li，2026-01-02）：歐洲國別價差「France $3.00/hr vs Germany $6.22/hr and Sweden $6.39/hr.」（同頁北美、歐洲均記 $4.12，內部不一致，測一須核）。https://www.silicondata.com/blog/geography-of-gpu-pricing-a100-vs-h100
3. tecRacer（AWS 夥伴，2026-01-15）：ESC「No GPU instances (yet)」「GPU-based instances are missing entirely」；ESC 對 eu-central-1「roughly a 15% price increase」。https://www.tecracer.com/blog/2026/01/aws-european-sovereign-cloud-esc-launch-pricing-and-whats-next.html
4. AWS What's New（2026-05-07）：「G6 instances powered by NVIDIA L4 GPUs are available in AWS European Sovereign Cloud (Germany)」——合格區之 GPU 等級落後全球區。https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-ec2-g6-aws-european-sovereign-cloud/
5. ITdaily（Michaël Aussems，2026-06-09）論 CADA：「Data center capacity within the EU must at least triple within five to seven years.」；主權準則「will then serve as the basis for (public) procurement」；「this proposal is far from binding」。https://itdaily.com/blogs/cloud/eu-aims-to-triple-data-center-capacity-by-2033-but-is-the-plan-enough/
6. 反向載體：ICLE 系評論（約 2026-05）轉述 SemiAnalysis「on-demand GPU rental capacity is sold out across both Hopper and Blackwell」——全球短缺時分區約束不顯。https://barczentewiczcom.pages.dev/post/build-don-t-block-what-the-compute-market-says-about-eu-ai-sovereignty/
7. 測一須另取：CADA 提案原文（COM(2026) 502；理事會 ST-10104-2026 https://data.consilium.europa.eu/doc/document/ST-10104-2026-INIT/en/pdf）之合格性與公共採購條款；Nebius 6-K／20-F 之分區容量與價格（sec.py；2026-10-22 6-K 檢索 `sovereign|Europe|Finland|region|price` 0 筆）；Nebius 2026-09 調價（dutchitchannel 原頁 4xx，需另找來源）；Microsoft／Google 主權雲之 GPU 機型；具名賣方是否以分區合格容量建模。**不宣稱已錯價。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 分區溢價已被指數商量化並公開——共識 | Silicon Data #1 | 否決 (2) |
| R2 | 約束需求占比小：多數 AI 訓練／推論無駐留約束，可跨區套利；`b_r` 微小則 `θ_r` 無意義 | Silicon Data #1 之「without constraints can arbitrage」 | 量級（否決 (3)） |
| R3 | 主權規則未定且非約束性；美系主權雲（AWS ESC）可能被認定合格，`K_r^elig` 隨之擴大 | ITdaily #5、AWS #4 | 規則反轉 |
| R4 | 全球皆售罄，分區約束只在需求轉弱時顯現；12 個月內不可見 | SemiAnalysis 轉述 #6 | 否決 (6) |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 同等級 GPU、同期限之分區價格（受約束合格區 vs 全球／美國）於 ≥ 2 個獨立來源（指數商、供應商牌價、申報）皆不可取得，或合格性無可操作定義（位置／營運者），使 `π_r` 與 `K_r^elig` 皆不可觀測（量綱失敗）。
(2) 具名賣方或研究機構原文（非報導轉述）已以「駐留約束需求 ÷ 合格容量」或等價分區平衡建模 GPU 價格或特定 GPU 雲營收，使落差為共識（Silicon Data 之描述性價差不自動構成建模；測一須判其是否含合格性分割）。
(3) `[D]` 最寬假設下歐盟區約束需求占比 `b_EU` < 15%，或 `π_EU`（非 hyperscaler 層、合格區 vs 全球同等級）< 20%，量級不足。門檻於本卡凍結，測一不得改。
(4) 原文顯示分區溢價過去 4 季與全球價同步收斂（`π_r` 隨全球價下滑而下滑），即約束不形成分割。
(5) 可運作對照只能寫成用途分割（L6-P#3）、公有／私有放置（L14-P#5）、出口轉運（L12-P#3）、未上電存量（L2-P#6）或轉售槓桿（L6-P#5）。
(6) 12 個月內無可觀測檢驗事件（CADA 立場／採購準則定案、Silicon Data 分區季報、合格區新 GPU 世代上線、Nebius 分區揭露）。

複查觸發器（若日後殺）：CADA 或成員國公共採購規則把營運者總部／管轄列為強制合格條件；分區指數顯示受約束區溢價於全球價下跌季擴大；GPU 雲於申報分列主權區營收或容量。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：分區營收／容量；主權區合約之期限與價格條款。
2. 可交易工具：Nebius 美股；超大規模雲主權區不可分離。
3. 半衰期：以分區指數季報、CADA 立法進程為檢驗事件；`[V]` 日期不寫。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L6［P］標「已生成 #6」；`AIM_FUNNEL.md` §3「已生成未測」；`export/LEADS_算力收支.md` 線索 1 筆。不寫入：INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L6-P#1–#5、L6-A#1–#5、L6-I#1–#5、L14-P#5、L12-P#3、L2-P#6 結論。
