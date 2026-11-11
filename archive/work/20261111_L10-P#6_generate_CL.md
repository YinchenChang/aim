# L10-P#6 生成卡｜分發與中介：守恆（行動接取網之空口時槽守恆：同頻段同地區之 TDD 業者須同步，DL＋UL＋保護時槽＝1 且框架比例於釋照前由監理定案，單一業者不能移動；AI 上行需求（眼鏡、多模態助理）之增量只能由 FDD 低頻／上行接收分集／站點密度承接——上行升級若發生，其受益面落在 FDD 與站點，而非中頻 TDD Massive MIMO）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260930_L10-P_generate_GK.md；archive/work/20261013_L10-P#2_generate_CL.md；archive/work/20261020_L10-P#3_generate_CL.md；archive/work/20261027_L10-P#4_generate_CL.md；archive/work/20261103_L10-P#5_generate_CL.md | EMITS: work/20261111_L10-P#6_generate_CL.md -->
**日期：** 2026-11-11　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3→4／6）　**格：** L10-P　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L7-I#6 本日測一，Q-0194 done）。非已殺／刻意排除格中最後測試日最舊＝2026-11-03（L10-P#5、L10-A#5、L10-I#5、L11-A#5、L11-I#5、L13-A#5 同日）；依表序取 **L10-P**。既有生成數 5 → #6。
- 格界：L10「分發與中介」含把 AI 服務送達終端之接取通路（#4 已收 CDN 交付）；本卡取行動無線接取之**空口**。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py uplink TDD Ericsson mobile`，命中 0。內部數字（§12）未取。載體全由本輪 WebSearch／web-fetch 子代理實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L10-P#1**（不通過）：端側能量／殼溫決定功能留端或回雲；死因＝功能類不可並列。本卡不論端側運算能量；UE 發射功率只作上行覆蓋邊界之旁證，守恆量為**時槽占比**。
  - **L10-P#2**（不通過）：需求通道守恆 → 行銷費用率。本卡不論通道份額或獲客成本。
  - **L10-P#3**（部分通過）：自駕車隊實體容量上界。本卡非車隊。
  - **L10-P#4**（不通過）：CDN 計費位元組 ≡ 請求 × 每請求位元組。本卡不論流量計費或營收量綱，論**容量供給端之方向配額**；若實讀後只能寫成「AI 流量位元組占比小」即滑回 #4（否決 (4)）。
  - **L10-P#5**（測一部分通過）：域名世代存活。無關。
  - **L4-P 系列／L2-P 系列**：伺服器與資料中心實體上界；本卡在接取網，不在資料中心。**L11-P（已殺）**：不論注意力；不恢復。
- §7-10 領域最近公開：Ericsson Mobility Report 2026-06（上行專文，2026-06-16）；Light Reading／RCR 2026-10-07／08（DT 準 CFO 表態）；Nandlall 評論 2026-07-29；Ookla 轉述 2026-07-07。下一檢查點＝Ericsson Mobility Report 2026-11 版（若已出，測一先讀）與 Ericsson／Nokia 4Q26 財報（約 2027-01）。

## 1. 落差一句

恆等骨架：同頻段 TDD 每框架 `α_DL + α_UL + α_G ≡ 1`；同地區業者須同步（GSMA：同區同頻段「have to be synchronised」；同頻隔離距離「up to 60km」），框架參數「defined and made public before awarding the spectrum」，GSMA 推 DDDSU 為 5G 共存最佳折衷 ⇒ 若特殊時槽採 10:2:2 符元，`α_UL ≈ (1 + 2/14)/5 ≈ 23%`、`α_DL ≈ 74%`［D，框架假設待測一以各國公告核］。上行容量 `C_UL ≈ Σ_band α_UL,b · W_b · η_UL,b · N_sites`，且邊緣使用者受 UE 發射功率限制（Nandlall：「A user behind two walls at the edge may not achieve 1 Mbps regardless of how empty the cell is」）。已見數點：Ericsson 2026-06：55 家中 43 家 2025 上行成長快於下行；AI 情境 2031 上行 3×（中）／5×（高）於 2025；眼鏡下載：上傳約 1:8。Nandlall：AI 會話約 26% 上行 vs 一般約 10%。Ookla 轉述：美國上行份額 5.1%、22 市場中 12 個上行配額持平或縮小，「operators cannot expand uplink windows without causing an identical reduction in download capacity」。種子主張：市場（廠商與部分賣方）把「AI 上行」讀成廣義 RAN 升級週期（Light Reading：「vendors like Ericsson and Nokia are eyeing a potential sales boost」），反方（DT、Nandlall）讀成不存在；時槽守恆指出第三種讀法——中頻 TDD 之上行配額為集體鎖定之常數，故即使上行需求兌現，增量容量只能來自 FDD 低頻（8RX、FDD MU-MIMO、上行 CA）與站點密度，受益組成與市場以「Massive MIMO 中頻換代」計之組成不同。本卡不定方向與量級，只立可拒絕之量綱鏈（§7-1）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（TDD 空口時槽 `α_DL + α_UL + α_G ≡ 1`；同區同步使 `α_UL` 為集體參數；上行容量由各頻段加總） |
| 量綱 | 時槽占比［無量綱］；頻寬［MHz］；頻譜效率［bit/s/Hz］；上行吞吐［Mbps］；上行流量［GB／月·用戶］；站點數［站］ |
| 可見端 | 各國 3.5 GHz／C-band 同步框架公告；Ericsson Mobility Report 上行統計與情境；Ookla 上行中位數；業者法說（T-Mobile 上行、AT&T 8RX 600 MHz）；Ericsson／Nokia 季報之地區與產品線句 |
| 指名不可見端 | 單一業者分頻段上行負載率；廠商 RAN 營收按 FDD／TDD、按低頻／中頻拆分；8RX 單元出貨量 |
| 主張 | AI 上行增量（若兌現）之容量承接與資本支出組成由時槽守恆決定，落在 FDD 低頻與站點；可由「監理已允許／業者已採非同步或上行加重框架」「具名者已以此組成建模」「上行需求不重大」拒絕 |
| 外部參照物（測一查證） | TD-LTE 時期框架定案（DSUDD 類）後，業者以 FDD 承擔上行之前例；固網 DOCSIS 上下行頻寬重分配（mid-split／high-split）為**可移動**對照 |
| 表達工具型態（只指名，不選券） | 美股可交易之 RAN 設備商 ADR、行動業者、鐵塔普通股；不選券 |
| 重疊 | L10-P#4（交付量綱）、L10-P#1（端側功率）、L4-P（硬體上界）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Ericsson Mobility Report 專文（2026-06-16）https://www.ericsson.com/en/reports-and-papers/mobility-report/articles/rising-uplink-demand-ai-driven-mobile-networks ：「43 out of 55 service providers experienced a higher uplink growth rate than downlink」；「uplink traffic being 3 times higher in 2031 than in 2025」；眼鏡「download-to-upload ratio is typically 1:8」；容量手段列 FDD 8RX、新 FDD 頻段、FDD MU-MIMO、站點與重耕；未論 TDD 框架。
2. Ericsson Mobility Report 專文（2025-11-20）https://www.ericsson.com/en/reports-and-papers/mobility-report/articles/ai-cloud-mobile-drive-uplink-growth ：眼鏡按需「about 1.4 Mbps in the uplink」；上行基線約 2 GB／月；以低頻 FDD 錨定上行、中頻 TDD 加強下行之 CA 範例。
3. GSMA《5G TDD Synchronisation Q&A》（2020）https://www.gsma.com/spectrum/wp-content/uploads/2021/03/5G-TDD-Synchronisation-QA.pdf ：同步義務、「up to 60km」、DDDSU、參數釋照前公告、「more uplink heavy applications are anticipated」。
4. Light Reading（2026-10-07）https://lightreading.com/ai-machine-learning/deutsche-telekom-dashes-vendor-hopes-for-big-mobile-uplink-spending ：DT 準 CFO 對 AI 推升資本密度「The short answer is no」；廠商「eyeing a potential sales boost」；T-Mobile CTO 7 月「improve the uplink performance」；AT&T 選 Ericsson 600 MHz「uplink-enhancing 8RX」；Signals Research 測 T-Mobile SA 上行影響「very modest」。
5. RCR Wireless（2026-10-08）https://rcrwireless.com/20261008/ai/deutsche-telekom-ai-traffic ：同上轉述；T-Mobile「isn't yet seeing meaningful AI-driven traffic pressure」。
6. Nandlall（RCR Analyst Angle，2026-07-29）https://www.rcrwireless.com/20260729/analyst-angle/6g-ai-uplink-panic-nandlall ：「TDD frames allocate uplink a minority of airtime」；AI 會話 26% 上行；「generative AI at 0.06 percent of network traffic」（引 Ericsson）；「I found no public operator disclosure attributing material uplink congestion to AI applications」。
7. Ookla 轉述（TechForge，2026-07-07）https://www.telecomstechnews.com/news/ookla-ai-workloads-strain-5g-infrastructure/ ：美國上行份額 5.1%；上行中位數 DT 24.57／T-Mobile 13.94／Verizon 13.43／AT&T 9 Mbps；時槽零和句。二手，測一須回 Ookla 原文。
8. Nokia 1Q26（Fierce，2026-04-23）https://www.fierce-network.com/broadband/nokia-machine-ai-will-drive-most-network-traffic ：「On the mobile side, Nokia is neither expecting nor chasing growth」；兩廠皆預期 2026 RAN 持平。
9. 測一須另取：美國 C-band／3.45 GHz 是否有強制同步框架（FCC 規則或業者協議）、歐洲各國 3.5 GHz 框架公告（如 ECC 決議）；Ericsson 20-F／6-K、Nokia 20-F（sec.py）之 RAN 產品線與上行相關句；AT&T／Verizon／T-Mobile 10-Q（sec.py）之上行或 8RX 資本支出句；具名賣方（如 Dell'Oro、Mobile Experts、投行）RAN 預測是否拆 FDD 低頻／上行。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | AI 上行需求不重大，無資本支出週期 | DT（#4、#5）、Nandlall（#6）、T-Mobile | 量級不足 |
| R2 | 上行增量本已規劃由 FDD 8RX／上行 CA 承接，業者與廠商公開如此說 | Ericsson（#1、#2）、AT&T（#4） | 已定價／非落差 |
| R3 | 動態 TDD、上行加重框架或 6G 上下行解耦可移動 `α_UL` | GSMA 半同步（#3）、Ericsson 6G 句（#1） | 守恆前提失效 |
| R4 | 上行瓶頸在信令／連線行為而非酬載 | Signals Research（#4、#6） | 量綱錯位 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 具名賣方／研究機構或廠商財報已將 AI 上行之容量承接**按 FDD 低頻／站點 vs 中頻 TDD 拆分**量化——已定價（R2）。
(2) 主要市場（美、歐至少一國）監理或業者已採或已核准上行加重／非同步 TDD 框架，或公告可於 2027 年前改框架——守恆前提不承重（R3）。
(3) `[D]` AI 增量上行流量占 2027–2028 行動上行總流量 < 10%，或主要業者上行負載率之一手揭露顯示現有 TDD 上行配額足以吸收 Ericsson 中情境至 2028——不重大（R1；門檻已凍結於本條）。
(4) 可運作對照只能寫成 L10-P#4（交付位元組／計費量綱）、L10-P#1（端側功率決定留端）或 L4-P 系列（硬體實體上界）。
(5) 各頻段上行容量或 RAN 支出之 FDD／TDD 拆分既無一手、亦無可替代第三方量測——不可並列（L10-P#1 死因型）。
(6) 市場、廠商與業者皆未以 AI 上行計價 RAN 支出（反方 R1 已成共識且無對向讀法），或 Ericsson／Nokia 4Q26 財報（約 2027-01）單季即全數解析——無可修正之錯價或重定價窗 < 12 個月。

複查觸發器（若日後殺）：任一主要市場監理公告 TDD 框架修訂；Ericsson／Nokia 揭露 FDD／低頻或 8RX 產品線成長；業者法說以 AI 上行列為資本支出理由。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：RAN 設備商之網路／行動網路營收（地區別）、產品線句；業者資本支出與頻譜支出；鐵塔租賃之新增設備租金（amendment）。
2. 可交易工具：RAN 設備商 ADR、行動業者、鐵塔普通股。不選券。
3. 半衰期：AI 眼鏡與多模態助理滲透（Ericsson 情境至 2031）→ 業者上行 KPI 惡化 → 頻譜／站點決策（年度預算）→ 廠商訂單；全數解析可能跨 2027–2029。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L10［P］標「#6 已生成」；`AIM_FUNNEL.md` §3 一句。未寫 `export/LEADS_算力收支.md`（本輪事實屬電信接取網流量與資本支出，非 AI 算力投入／收入／硬體／雲端合約／資料中心）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L10-P#1–#5、L10-A#1–#5、L10-I#1–#5、L4-P 系列、L11-P、C-A5 結論；不寫 T-15。
