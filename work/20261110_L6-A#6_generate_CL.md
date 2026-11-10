# L6-A#6 生成卡｜雲端與基礎設施服務：會計恆等（長期資產減損之可回收性門檻：`BV_t ≡ C − 累計折舊_t − 累計減損_t`；減損只在「資產群組未折現現金流 < 帳面」時認列，認列額＝帳面 − 公允價值；故 `未認列經濟損失 H ≡ max(0, BV − FV) − 已認列減損` 可在 FV 遠低於 BV 時恆為正而帳上為零）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260927_L6-A_generate_GK.md；archive/work/20261011_L6-A#2_generate_CL.md；archive/work/20261018_L6-A#3_generate_CL.md；archive/work/20261026_L6-A#4_generate_CL.md；archive/work/20261102_L6-A#5_generate_CL.md；work/20261102_L6-A#5_test1_CL.md；archive/work/20261021_L2-A#4_generate_CL.md；archive/work/20261108_L3-A#6_generate_CL.md；archive/work/20261103_L11-A#5_generate_CL.md；archive/work/20261031_L4-A#5_generate_CL.md | EMITS: work/20261110_L6-A#6_generate_CL.md -->
**日期：** 2026-11-10　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 2→3／6）　**格：** L6-A　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額配置、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L6-P#6 本日測一，Q-0189 done）。非已殺／刻意排除格中最後測試日最舊＝2026-11-02（L6-A#5、L6-I#5、L7-P#5、L7-A#5 同日；L6-P 已於本日取 #6）；依表序取第一 → **L6-A**。既有生成 #1–#5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `tokenomics_leads.py impairment GPU depreciation "useful life" residual`，30 筆，相關 2 筆（SRC_DC_007 CoreWeave 折舊年限、SRC_DC_008 Nebius 折舊年限；線索：Tokenomics SRC_DC_007）→ 回 CoreWeave 10-K 原文實讀（下 §3-1）。內部數字（§12）未用。
- 比對（須異型）：
  - **L6-A#1**（RPO 已簽未交付領先營收）：營收時序；本卡為資產帳面之衡量門檻。
  - **L6-A#2**（電力轉嫁總額）、**L6-A#4**（capex 現金流分類）、**L6-A#5**（分部未分攤）：列報／分類；本卡為**認列與否**之門檻。
  - **L6-A#3**（CIP 轉入後之折舊管線 `ΔD ≥ ΣCIP/L`）：折舊流量。本卡不以耐用年限或折舊起點為落差（L6-A#5 測一邊界已排除「折舊起點／年限」）；年限辯論（Meta 4→5.5 年、Amazon 部分縮回 5 年）列為**反方共識**，非本卡機制。
  - **L2-A#4**（出租方租期末殘值 `BV_T ≡ C·(1−T/L)`）：租期－年限錯配之存量；本卡為**期中**觸發門檻與資產群組界定，不需租期屆滿。
  - **L3-A#6**（存貨 LCNRV，逐項、以淨變現價值即時認列）：對照組——存貨規則無未折現門檻；本卡之樞紐正是 PP&E 有此門檻而存貨沒有。
  - **L11-A#5**（商譽減損之市值調節）：報告單位層、以公允價值測；本卡為 ASC 360 長期資產之**未折現**第一步。
  - **L4-A#5**（確定採購承諾損失預提）：表外承諾；本卡為已入帳之 PP&E。
  - 重疊列為否決 (5)。
- §7-10 領域最近公開：CoreWeave 10-Q 2Q26（2026-08-12）；Silicon Data「H100 Rental Prices by Region (Q3 2026)」（2026-07-31）；ASC 360-10-35 無 2025–26 修訂（測一須核 FASB 最新 ASU 清單）。下一檢查點＝CoreWeave 10-Q 3Q26（應已於 2026-11 初申報，測一以 sec.py 取）、Nebius 3Q26 6-K、Silicon Data Q4 2026。

## 1. 落差一句

公開辯論集中於 GPU **折舊年限**（流量）；**種子主張：即使年限正確，GPU 雲之 PP&E 帳面亦受 ASC 360 兩步測試保護——第一步以「資產群組」之**未折現**未來現金流比帳面，群組越大（全機群＋已簽長約）越難觸發；故 H100 世代之公允價值（以現貨租價或二手售價折現）可低於帳面而帳上零減損。** CoreWeave 10-K FY2025 原文：「The recoverability of the long-lived asset or asset group is assessed by comparing the undiscounted future cash flows … to its carrying value」且「For the years ended December 31, 2025, 2024, and 2023, no material impairment charges were recorded.」同期 Silicon Data 記 hyperscaler H100 租價「fell 26 to 54% by region since Q1 2025」。落差＝以「無減損／有形帳面」讀資產品質（含以設備為擔保之債務 LTV）者，與以 FV 讀者之間的 `H`；方向不定（可能是隱藏損失，也可能長約現金流使 FV 實際 ≥ BV）。

## 2. 機制型態

| 欄 | 內容 |
|---|---|
| 型態 | **[A] 會計恆等**：`BV ≡ C − AD − Imp`；`Imp = 1[UCF_g < BV_g]·(BV_g − FV_g)`；`H ≡ max(0, BV − FV) − Imp` |
| 樞紐參數 | 資產群組界定 `g`（逐叢集／逐合約／全機群）；未折現 vs 折現之差（長尾年數 × 無折現）；長約現金流是否計入群組 |
| 第一原理量 | 每 GPU 帳面 `BV_gpu`（技術設備淨額 ÷ 在役 GPU 數，按世代）；`FV_gpu` 代理＝(i) 二手成交價，或 (ii) 現貨租價指數 × 利用率 × 剩餘年限之現值 − 營運成本 |
| 判定量 `[D]` | `h ≡ H ÷ 技術設備淨額`（世代加權）；`h_E ≡ H ÷ 股東權益`；`κ ≡ UCF_g ÷ BV_g` 之最寬估計（> 1 即測試必過） |
| 可拒絕事件 | 任一 GPU 雲／超大規模雲對 Hopper 世代認列減損或縮短年限並揭露金額（門檻被觸發即落差消失）；二手 H100 價 ÷ 帳面 ≥ 1 |
| 表達工具型態（只指名，不選券） | 美股上市 GPU 雲（CoreWeave、Nebius 等）；以 GPU 擔保之 ABS／DDTL 債務；超大規模雲不可分離。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. CoreWeave 10-K FY2025（acc 0001769628-26-000104，sec.py 實讀）：ASC 360 政策句（asset group、undiscounted、「independent third-party appraisals」）與「no material impairment charges」三年。https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm
2. CoreWeave 10-Q 2Q26（acc 0001769628-26-000366，sec.py 實讀）：「Technology equipment $ 33,823」（2026-06-30，百萬美元）vs「$ 20,903」（2025-12-31）；累計折舊「( 5,886 )」；全文 `triggering` 0 筆、`impairment charge` 只見商譽。https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm
3. Silicon Data（2026-07-31）分區 H100 租價下滑 26–54%：https://www.silicondata.com/blog/h100-rental-prices-by-region-q3-2026
4. Shaping Tomorrow（2026-07-11）：年限辯論綜述；觀察指標「Secondary-market GPU rental rates (H100, Blackwell) fall below roughly $2 per hour」；轉述 Goldman「trailing-edge A100 and H100 rental prices have stayed high enough to imply five-to-six-year lives」（反方）；「a reset has not yet been forced」。https://decision-intel.shapingtomorrow.com/scans/ai-automation/2026-07-11-gpu-depreciation-reset/scan.html
5. 反方／共識載體：ElectronEconomics（2026-05-06，付費牆後未讀）「A fleet depreciated over six to eight years. The hardware economics may not stretch that far.」https://electroneconomics.substack.com/p/the-depreciation-clock-coreweaves ；Creative Strategies（Ben Bajarin，2026-06-02）「clearest mismatch between long data center leases, shorter customer contracts, and GPU depreciation」，全文報告列「GPU residual values」（未讀）。https://creativestrategies.com/research/neoclouds-the-backlog-quality-test/
6. 測一須另取：Nebius 20-F FY2025／6-K 之減損政策與資產群組；Oracle、Microsoft、Alphabet、Amazon、Meta 10-K 之 ASC 360 群組界定與 Hopper 相關任何減損／加速折舊（Amazon 加速折舊 $920M 為年限變更，非減損，須分開）；二手 H100（HGX 8-GPU）成交價之 ≥ 2 個獨立來源；GPU 擔保債務之評價條款（第三方鑑價、LTV 觸發）；具名賣方是否以 FV／NAV 口徑估 GPU 雲。**不宣稱已錯價。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | GPU 資產品質已被年限辯論充分定價——共識 | Shaping Tomorrow #4、ElectronEconomics #5、Bajarin #5 | 否決 (2) |
| R2 | 舊世代租價仍高，隱含 5–6 年壽命，FV ≈ BV | Goldman（經 #4 轉述） | 量級（否決 (3)） |
| R3 | 機群多被長約（take-or-pay）綁定，群組現金流確定，FV 以合約現金流計亦 ≥ BV | CoreWeave backlog（#5 引 US$66–88B） | 否決 (4) |
| R4 | 減損為非現金、不影響債務契約或現金流，市場不以帳面定價 | — （測一須找具名） | 機制相關性 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 同世代 GPU 之 `BV_gpu` 與 `FV_gpu` 於 ≥ 2 個獨立來源（申報、二手成交、租價指數）皆不可取得，或任一主體之資產群組界定不可由原文判定，使 `h` 不可觀測（量綱失敗）。
(2) 具名賣方或研究機構原文（非轉述）已以 FV／NAV 或「減損測試門檻」口徑估 GPU 雲資產並公開 `H` 或等價量；年限敏感度分析本身**不**構成本落差之共識（測一須判其是否含 FV 對帳面）。
(3) `[D]` 最寬假設下 `h` < 15%（世代加權技術設備淨額），或 `h_E` < 25%，量級不足。門檻於本卡凍結，測一不得改。
(4) 原文顯示主要 GPU 雲之 Hopper 機群 ≥ 70% 由剩餘期 ≥ 帳面剩餘年限之 take-or-pay 合約覆蓋（FV 由合約現金流支撐，`H` 結構上近零）。
(5) 可運作對照只能寫成折舊年限／起點（L6-A#3 型）、租期末殘值（L2-A#4 型）、存貨 LCNRV（L3-A#6 型）、商譽減損（L11-A#5 型）或採購承諾損失（L4-A#5 型）。
(6) 12 個月內無可觀測檢驗事件（10-K FY2026 減損／年限揭露、GPU 擔保債再融資鑑價、Silicon Data 季報、二手 H100 價格序列）。

複查觸發器（若日後殺）：任一上市 GPU 雲或超大規模雲揭露 Hopper 世代減損或觸發事件評估；GPU 擔保債務出現鑑價下修或 LTV 補繳；二手 HGX H100 成交價跌破申報每 GPU 帳面之 60%。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：技術設備淨額（按世代）、減損政策與群組、擔保債務鑑價條款。
2. 可交易工具：美股上市 GPU 雲；超大規模雲不可分離。
3. 半衰期：以年報減損揭露（FY2026 10-K，2027-02／03）與再融資鑑價為檢驗事件；`[V]` 日期不寫。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L6［A］標「已生成 #6」；`AIM_FUNNEL.md` §3「已生成未測」；`export/LEADS_算力收支.md` 線索 1 筆。不寫入：INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L6-A#1–#5、L6-P#1–#6、L6-I#1–#5、L2-A#4、L3-A#6、L11-A#5、L4-A#5 結論。
