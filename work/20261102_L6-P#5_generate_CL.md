# L6-P#5 生成卡｜雲端與基礎設施服務：守恆（已承諾 GPU 時之再售守恆：`H_phys = H_com + H_od`、`H_com = H_use + H_resold + H_idle`；現貨／按需市場之供給＝`H_od + H_resold`，在承諾占比 ≈ 98% 時，買方閒置之微小變動對現貨供給有約 `λ = H_com ÷ H_od` 倍之槓桿）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/work/20261026_L6-P#4_generate_CL.md；archive/drive/USED_20260928_L6-P_generate_GK.md；archive/drive/USED_20260929_L6-P_T_GK.md | EMITS: work/20261102_L6-P#5_generate_CL.md -->
**日期：** 2026-11-02　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 2／6）　**格：** L6-P　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L5-I#5 於 2026-11-01 測一，Q-0147 done）。最後測試日最舊＝2026-10-26（L6-P#4、L6-A#4、L6-I#4、L13-A#4 同日）；依表序取 **L6-P**；非已殺、非刻意排除。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py GPU resale secondary market rental index`，回 22 筆，**相關 0 筆**（皆硬體規格、折舊年限、TCO；無轉售或現貨供給）。載體全由 WebSearch／web-fetch 子代理／sec.py 原文取得。
- 比對之舊檔與死因型態，本卡須異型：
  - **L6-P#1**（T，同步作業 MTTF∝1/N）：可靠度守恆。本卡守恆量＝**GPU 時在合約層間之分配**（使用／轉售／閒置）。
  - **L6-P#2**（RPO 交付之 MW·h 上界；(1) ρ 不可界定）：供給方交付上界。本卡不換算營收、不需 ρ；守恆在**買方側**之已購 GPU 時。
  - **L6-P#3**（供給方容量用途分割；(2) 賣方已以份額建模）：供給方之 `K_ext/K_1P/K_RD`。本卡為買方已承諾容量之閒置如何回流現貨市場。
  - **L6-P#4**（冷卻型態存量；(1) 不可觀測）：實體機房。本卡不涉機房型態。
  - **L6-I#4**（買方交付終止權）：契約退出選擇權。本卡不需終止；買方保有合約、只轉售時段。
  - **L7-I#4**（模型層照付不議 → 降價填充 token）：輸出為 token 價格。本卡輸出為 **GPU 時現貨供給與租價指數**；重疊列否決 (4)。
  - **C-A3／C-A4**（折舊年限）、Compute Exchange 二手硬體市場：實體殘值。本卡為服務時段，非硬體所有權；重疊列否決 (4)。
- §7-10 領域最近公開：SF Compute「The average customer now saves 25%」（Evan Conrad，2026-09-09）；packet.ai（2026-10-23）；CoreWeave 10-Q（期末 2026-06-30）。下一檢查點＝CoreWeave 3Q26 10-Q（約 2026-11 中旬）、Nebius 3Q26、Silicon Data／Ornn 月度指數。

## 1. 落差一句

公開敘事以 GPU 租價指數（Silicon Data H100 Hyperscaler Index、SemiAnalysis H100 一年合約指數、Ornn）作為算力**實體稀缺**之讀數（packet.ai 2026-10-23 轉述 SemiAnalysis：H100 一年合約指數 2025-10 低點後至 2026-03 升近 40%）。**種子主張：GPU 雲收入 ≈ 98% 來自照付不議之承諾合約（CoreWeave 10-Q 2Q26），現貨／按需只是 ≈ 2% 之殘差；而承諾容量之買方閒置可經轉售回流現貨（SF Compute 訂單簿：「Sell unused compute time」；平台平均實現折扣 25%），且供給方本身「has the right to resell」承諾容量並以之入 RPO 變動對價（CoreWeave 10-Q 營收附註）。故守恆式 `H_spot_supply = H_od + H_resold`，`H_resold ≤ H_com − H_use`；在 `λ = H_com ÷ H_od ≈ 49` 時，買方使用率 1 pp 之下滑可使現貨供給增約 49%——無需新建一 MW。** 落差＝若市場把現貨／短約指數讀為實體稀缺，則指數對買方使用率（而非建置速度）之槓桿被誤估（方向不定：使用率高時指數超調向上；任一大買方閒置時，指數可在無新供給下斷崖，並經「right to resell」之變動對價回傳至 GPU 雲之 RPO 估計）。

## 2. 機制型態

| 欄 | 內容 |
|---|---|
| 型態 | **[P] 守恆**：實體 GPU 時在合約層間之存量－流量；每一 GPU 時僅能被使用、轉售或閒置其一 |
| 守恆式 | `H_phys = H_com + H_od`；`H_com = H_use + H_resold + H_idle`；`H_spot_supply = H_od + H_resold` |
| 第一原理量 | 承諾占比 `c = H_com ÷ H_phys`（以營收占比代理，須於測一釘死口徑）；買方使用率 `u = H_use ÷ H_com`；轉售可達率 `r`（合約允許轉售之承諾占比） |
| 判定量 `[D]` | `λ = c ÷ (1 − c)`；`∂H_spot_supply/H_od ≈ λ · r · Δ(1 − u)`；SF Compute 實現折扣 25% 推 `H_resold/H_com` 之區間（須扣價差與費用） |
| 可拒絕事件 | GPU 雲揭露轉售權之變動對價金額或承諾／按需容量分列；租價指數單季斷崖而同期無新供給公告；大買方（實驗室）公開轉售或轉讓承諾容量 |
| 表達工具型態（只指名，不選券） | 美股 GPU 雲（CoreWeave、Nebius）；超大規模雲。不選券 |
| 重疊 | L7-I#4（承諾 → 降價）、L6-I#4（終止權）、L6-P#3（用途分割）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. CoreWeave 10-Q（2026-06-30 期，acc 0001769628-26-000366；sec.py `--grep committed` 18 筆）：「committed contracts, which are take-or-pay, or on-demand, which are pay-as-you-go」；「committed contracts accounted for 98% of our revenue」；RPO 變動對價含「estimates of committed cloud computing capacity that the Company has the right to resell」；RPO 103.7 bn，41% 於 24 個月內。`resell|resale|sublicens|secondary market` 原文大小寫檢索 0（僅 `right to resell` 句經 `committed` 檢索帶出）。https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm
2. SF Compute，「The average customer now saves 25% with SFC」（Evan Conrad，2026-09-09）：「receive an average 25% realized discount off their compute price, via resale」。無平台總轉售量。https://sfcompute.com/news/realized-discount
3. SF Compute 文件「Sell unused compute time」：「You receive credits only when a buyer buys the time」；「Low use of graphics processing units (GPUs) alone does not mean the time is spare」。https://docs.sfcompute.com/preview/guides/reselling-introduction
4. packet.ai（2026-10-23，利害方）：「Resale exists but is narrow」；AWS 僅 Standard RI、12% 費；「Google Cloud and Azure document no resale route for commitments」；轉述 SemiAnalysis H100 一年合約指數。https://packet.ai/blog/oversubscribed-gpu-capacity
5. DCD（SF Compute 募資）：「enables buyers of GPU capacity to resell their unused capacity」「help combat the risk of overbuilding」；管理逾 1 億美元硬體。https://www.datacenterdynamics.com/en/news/sf-compute-raises-40m-for-ai-compute-marketplace-offering/
6. SiliconANGLE（Duncan Riley，2026-07-17）：Compute Exchange（預留容量採購場，逾 100 供應商）；Silicon Data 指數由同一人主導——指數提供者與交易場同源，測一須釘指數樣本是否含轉售時段。https://siliconangle.com/2026/07/17/compute-exchange-opens-secondary-market-used-nvidia-h100-a100-gpus/
7. 測一須另取：Nebius、IREN、Lambda（若有申報）之承諾／按需分列與轉售條款（sec.py）；Silicon Data、Ornn、SemiAnalysis 指數方法論（樣本是否含轉售／短約）；Microsoft、OpenAI、Anthropic 一手是否揭露承諾容量轉讓或轉售；具名賣方是否以買方使用率或轉售量建模租價。**不宣稱已錯價。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 轉售管道狹窄：大雲無承諾轉售途徑，AWS 有費率與條件；殘差市場與承諾市場分割，買方閒置不流入現貨 | packet.ai #4 | `r` ≈ 0 → 機制斷路 |
| R2 | 「閒置」難定義：低使用率不等於時段可售 | SF Compute 文件 #3 | `H_idle` 不可觀測 |
| R3 | 現況為全面短缺，買方使用率趨近 1；槓桿只在需求轉弱時發作 | Apollo 2026-06（L6-P#4 卡 #4 已錨） | 12 個月內無事件 |
| R4 | 供給方轉售權已入 RPO 變動對價，風險已在申報層定價 | CoreWeave 10-Q #1 | 共識／已揭露（否決 (2)） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 承諾／按需容量（或營收）分列、轉售量或轉售權變動對價金額，於 ≥ 2 家 GPU 雲或交易場之申報、法說或一手揭露皆不可取得，且無具名指數方法論說明樣本是否含轉售時段，使 `c` 與 `H_resold` 皆不可觀測（量綱失敗）。
(2) 具名賣方或研究機構原文（非報導轉述）已以買方使用率、承諾殘差或轉售供給建模 GPU 租價指數，或 GPU 雲已量化揭露轉售權變動對價，使落差為共識。
(3) `[D]` 可得之最寬假設下 `λ` ≤ 5（即按需占比 ≥ 約 17%），或可轉售承諾占比 `r` < 10%，量級不足。門檻於本卡凍結，測一不得改。
(4) 可運作對照只能寫成供給方用途分割（L6-P#3）、買方終止權（L6-I#4）、token 降價誘因（L7-I#4）、RPO 交付上界（L6-P#2）或硬體殘值／折舊年限（C-A3／C-A4）。
(5) 原文顯示主要承諾合約禁止或實質排除買方轉售，且供給方「right to resell」之收益不入現貨指數樣本（R1 成立），使買方閒置與指數無傳導路徑。
(6) 12 個月內無可觀測之檢驗事件（指數方法變更、轉售量揭露、大買方轉讓承諾、GPU 雲變動對價附註變動）。

複查觸發器（若日後殺）：任一 GPU 雲於 10-K／10-Q 量化轉售權變動對價或承諾／按需容量分列；租價指數單季跌幅 > 25% 而同期無新供給公告；具名賣方以買方使用率建模租價。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：RPO 變動對價（轉售權、可用性抵減、交付延遲）分列；按需營收占比。
2. 可交易工具：CoreWeave、Nebius 美股；超大規模雲之雲端分部不可分離。
3. 半衰期：以指數月度發布與 GPU 雲季報為檢驗事件；CoreWeave 3Q26（約 2026-11）；`[V]` 日期不寫。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L6［P］標「已生成 #5」；`export/LEADS_算力收支.md` 線索 3 筆。不寫入：AIM_FUNNEL.md（§3 沿前輪慣例由測一輪對齊）、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L6-P#1–#4、L6-A#1–#4、L6-I#1–#4、L7-I#4、C-A3、C-A4 結論。
