# L5-I#4 生成卡｜儲存與 IO：誘因（超大規模買方之「裝機回收」外部選項：退役伺服器 DDR4 經 CXL 擴充器再部署 → 新 DRAM 價格愈高、回收誘因愈強 → 伺服器 DRAM 有效需求彈性高於以新購位元建模者）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260926_L5-I_generate_GK.md；archive/work/20261011_L5-I#2_generate_CL.md；archive/work/20261018_L5-I#3_generate_CL.md；work/20261018_L5-I#3_test1_CL.md | EMITS: work/20261026_L5-I#4_generate_CL.md -->
**日期：** 2026-10-26　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L5-I　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L5-A#4 2026-10-25 測一，Q-0105 done）。最後測試日最舊＝2026-10-18（L5-I#3、L6-P#3、L6-A#3）；依表序取 **L5-I**；非已殺、非刻意排除。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py CXL DRAM memory DDR4`，回 1 筆（SRC_HW_052 GB300 NVL72 BOM），**相關 0 筆**；載體全由 WebSearch／WebFetch 原文取得。
- 比對之舊檔與死因型態，本卡須異型：
  - **L5-I#1**（雲端出站費＝取用權；量綱失敗）：選擇者＝雲端業者對其客戶。本卡選擇者＝超大規模業者作為**記憶體買方**，物件＝退役記憶體之報廢 vs 再部署。
  - **L5-I#2**（供給者 JV 資本紀律；(1)(2) 觸發）：供給側擴產誘因。本卡為需求側之**存量供給**（裝機回收），不主張晶圓擴產與否。
  - **L5-I#3**（長約誘因相容；(5)(6) 觸發，下限不可觀測、結果多為重議）：買方對**合約**之違約選擇。本卡不涉長約履約；選擇變數為退役 DIMM 之再用率 `s`，可拒絕事件為控制器出貨與再用量揭露。
  - **L5-P#4**（HDD 裝機退役世代 → 替換需求，守恆型）：同用「退役」存量，但為 HDD 替換之機械守恆；本卡為 DRAM 買方之價格誘因選擇。
  - **L4-I#3**（自研替代品之外部選項）：替代物為新設計產品；本卡替代物為買方**已付費之折舊存量**，邊際成本＝控制器＋良率篩選，非研發。重疊列為否決 (4)。
  - **C-P1**（ARCH_dead #11，checkpoint 需求歸因）：本卡不做需求歸因。
- §7-10 領域最近公開：Meta Vistara 論文（ISCA 2026 Industry Session，2026-06-29）；Google／UIUC／Stanford IEEE CAL 2026-03-23；Astera Labs 2Q26 法說（2026-08-04）；TrendForce DDR4 1Q26 漲價報導（2026-01-19）。下一檢查點＝Astera Labs 3Q26 財報（約 2026-11 上旬）、Micron FQ1'27 10-Q（約 2026-12 下旬）、Marvell 3Q FY27（約 2026-12 上旬）。

## 1. 落差一句

伺服器 DRAM 需求慣以「新伺服器出貨 × 每台新購容量」建模；退役伺服器之 DIMM 視為報廢。**種子主張：DDR5／DRAM 合約價大幅上漲後，超大規模業者取得一條以自身折舊存量對抗新購之外部選項——退役 DDR4 經 CXL 2.0 擴充器（Meta 自研 Vistara、Marvell Structera X、Astera Leo）再部署，邊際成本僅控制器與篩選；選擇式為「再用若 `P_new(GB) × 有效容量增益 > C_ctrl(GB) + 延遲成本`」，故新 DRAM 價格愈高，再用率 `s` 愈高。** 落差＝若 `s × R_retired`（再部署 GB）對年度伺服器 DRAM 新增位元需求為非可忽略份額，則短缺期之需求彈性被低估、價格高峰之半衰期短於以新購位元建模者；反之，若 `s` 由技術（延遲容忍工作負載占比）而非價格決定，則本卡不成立。

## 2. 機制型態

| 欄 | 內容 |
|---|---|
| 型態 | **[I] 誘因**：買方於「新購 vs 再用折舊存量」之選擇，選擇變數 `s`（再用率）隨 `P_new` 上升 |
| 選擇者 | 超大規模業者（Meta 已部署；Google 論文；Astera 稱兩家美系超大規模 2027 量產出貨） |
| 第一原理量 | `R_retired`（年退役伺服器 DRAM GB）、`s`、每控制器容量（Vistara 256 GB／Structera X 1.5 TB 實體、壓縮 1.8–2x）、`C_ctrl` ÷ GB、`P_new` ÷ GB |
| 判定量 `[D]` | `g = s × R_retired × 壓縮增益 ÷ ΔD_new`（ΔD_new＝年度伺服器 DRAM 新增位元需求） |
| 可拒絕事件 | 控制器業者揭露 CXL 記憶體控制器營收或出貨；超大規模業者揭露再用量；DRAM 供給者法說就 CXL 再用對需求之原文 |
| 表達工具型態（只指名，不選券） | 美股可交易 DRAM 供給者（Micron）；CXL 控制器業者（Astera Labs、Marvell）。不選券 |
| 重疊 | L4-I#3（外部選項）、L5-P#4（退役存量）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Meta Vistara：「custom CXL 2.0 memory expander ASIC」、部署於「millions of production servers」、每 MemServer 768 GB DDR5＋256 GB CXL DDR4；約 40% 機隊不能擴容（HWBusters 2026-06-30 轉述）。https://hwbusters.com/news/meta-reuses-old-ddr4-memory-in-new-servers-to-cut-costs/ ；論文出處 ISCA 2026 Industry Session（Blocks & Files 2026-06-26）。https://www.blocksandfiles.com/architecture/2026/06/26/panmnesia-boosts-cxl-scale-with-fabric-switching-meta-repurposes-old-dram-with-cxl/5263151
2. Park, Ayers, Morris, Levis, Kim，「Capacity-Latency Tradeoffs in CXL Memory Expander at Hyperscale」，IEEE CAL 25(1)，2026-03-23：「DRAM now dominates the total cost of ownership (TCO) of datacenter servers」；再用「older, slower legacy DRAM modules from retired servers」；Zstd 4 KiB 有效容量 +35.8%。https://sing.stanford.edu/site/assets/publications/park26.pdf
3. Marvell Structera X 2404：四通道 DDR4、12 DIMM、1.5 TB 實體（TechRadar 2025-12-10）。https://www.techradar.com/pro/this-tiny-chip-could-singlehandedly-solve-the-ram-shortage-by-allowing-hyperscalers-to-reuse-old-ddr4-memory-via-cxl-and-it-even-comes-with-an-extraordinary-feature
4. Astera Labs 2Q26 法說（MarketBeat 2026-08-04 轉述）：「renewed interest in memory expansion」；Leo 新設計案；「volume shipments of standard and custom Leo CXL memory controllers to two U.S. hyperscalers in 2027」。https://www.marketbeat.com/instant-alerts/astera-labs-q2-earnings-call-highlights-2026-08-04/
5. TrendForce（引 Commercial Times，2026-01-19）：DDR4 1Q26 漲幅「up to 50%」，多家供給者 2026 退出 DDR4——再用之機會成本（退役 DDR4 轉售價）同步上升。https://www.trendforce.com/news/2026/01/19/news-ddr4-reportedly-leads-legacy-memory-rally-with-q1-prices-up-to-50-ddr3-in-tight-supply/
6. 測一須另取：Vistara 論文原文（aisystemcodesign.github.io）之部署 GB、再用占比、TCO 原文；ALAB、MRVL 10-K／10-Q（sec.py）CXL 分列或描述；Micron FY26 10-K 與 FQ1'27 法說（sec.py）就 CXL／再用之原文；Microsoft（Pond 論文系列）、Google、Amazon 有無同型部署一手；具名賣方或 TrendForce 是否把 CXL 再用納入 DRAM 位元需求；伺服器退役年齡與 DIMM 壽命一手。**不宣稱已錯價。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 超大規模業者已以長約鎖價，「pricing is contractually capped」，其邊際價非現貨，再用誘因弱 | Mobius Materials 2026-08-19 https://www.mobiusmaterials.com/post/inside-the-memory-supercycle-second-act | 誘因量級／選擇者錯置 |
| R2 | 再用只開給延遲容忍工作負載（擴充記憶體對不容忍者停用），`s` 由技術封頂、不隨價格 | SDxCentral 2026-07-06 轉述 Vistara 作者 https://www.sdxcentral.com/news/meta-recycling-memory-is-magic-solution-to-ram-supply-misery/ | 型態失敗（非誘因） |
| R3 | DDR4 本身漲價且停產，退役 DIMM 轉售價上升，再用之機會成本同升 | TrendForce #5 | 價差被抵銷 |
| R4 | 控制器量產在 2027（Astera），2026 短缺期內量級可忽略 | Astera #4 | 時序／量級 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 再用量（GB 或占比）於 ≥ 2 家超大規模業者或控制器業者皆不可取得，且 CXL 控制器營收於 ALAB／MRVL 申報層不可分列，使 `g` 無任何可觀測分量（量綱失敗）。
(2) 公開層（具名賣方或研究機構原文，非報導轉述）已把 CXL／退役 DRAM 再用納入伺服器 DRAM 位元需求或價格情境，使落差為共識。
(3) `[D]` `g` 於測一可得之最寬假設下 < 3%（再部署有效 GB ÷ 年度伺服器 DRAM 新增位元需求），量級不足。門檻於本卡凍結，測一不得改。
(4) 可運作對照只能寫成長約履約（L5-I#3）、供給者擴產（L5-I#2）、HDD 退役替換（L5-P#4）或自研替代品（L4-I#3）。
(5) 原文顯示再用決策早於本輪漲價（設計立項與部署節奏不隨 `P_new` 變動），或 `s` 由延遲容忍占比封頂（R2 成立），使 `s` 對價格無彈性——非誘因型。
(6) 超大規模業者之 DRAM 取得價經原文確認為長約封頂（R1 成立），且再用僅發生於長約買方，使誘因與現貨價脫鉤。

複查觸發器（若日後殺）：ALAB 或 MRVL 於 10-K／10-Q／8-K 分列 CXL 記憶體控制器營收或客戶；任一超大規模業者揭露再用 DRAM 量；Micron 法說或申報就 CXL 再用對需求之原文；具名研究機構將再用納入位元需求模型。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：控制器業者之產品別營收（CXL 是否分列）；DRAM 供給者之伺服器 DRAM 位元出貨與 ASP；超大規模業者伺服器耐用年限與資產處分。
2. 可交易工具：Micron、Astera Labs、Marvell 美股；Samsung／SK hynix 非美股主上市；Meta 為使用者非供給者。
3. 半衰期：控制器量產 2027（Astera 原文）；檢驗事件為 ALAB 3Q26 財報（約 2026-11）與 Micron FQ1'27（約 2026-12）；`[V]` 日期不寫。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L5［I］標「#4 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 線索 2 筆。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L5-I#1–#3、L5-A#1–#4、L5-P#1–#4、L4-I#3、C-P1 結論。
