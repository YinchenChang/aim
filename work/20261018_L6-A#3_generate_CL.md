# L6-A#3 生成卡｜雲端與基礎設施服務：會計恆等（在建工程之折舊管線：`ΔD ≥ Σ CIP_j ÷ L_j` 於轉入使用時入損益）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260927_L6-A_generate_GK.md；archive/drive/USED_20260927_L6-A_test1_GK.md；archive/work/20261011_L6-A#2_generate_CL.md；work/20261011_L6-A#2_test1_CL.md | EMITS: work/20261018_L6-A#3_generate_CL.md -->
**日期：** 2026-10-18　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3／6）　**格：** L6-A　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L6-P#3 本日測一，Q-0066 done）。最後測試日最舊＝2026-10-11（L6-A#2、L6-I#2、L13-A#2）；依表序取 **L6-A**；非已殺、非刻意排除。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py construction in progress depreciation`，回多筆，皆為硬體規格／機架功率（SRC_HW_*），相關 0；本卡未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L6-A#1**（`archive/drive/USED_20260927_L6-A_generate_GK.md`／test1）：已簽約未交付÷已交付之**營收**領先比。本卡為**成本端**：已資本化未轉入使用之資產尚未提折舊；載體為 PP&E 附註，非 RPO／backlog。
  - **L6-A#2**（`archive/work/20261011_L6-A#2_generate_CL.md`）：電費轉嫁份額 θ。不同型。
  - **C-A3**（ARCH_dead #5）：折舊**年限**離散。本卡年限 `L_j` 取申報值不動，動的是**折舊起點**（在建→使用）。
  - **L13-A**（未開始租約、RVG）：租賃義務未入表。本卡為自有資產、已入表、未提折舊。**L2-A#2**（利息資本化）：在建期利息資本化墊高 AFFO；本卡不涉利息，只涉轉入後之折舊步升。**L3-A#2**：折舊基數扣補助。不同型。
  - 重疊列為否決 (4)。
- §7-10 領域最近公開：Oracle FQ1 FY27 10-Q（期末 2026-08-31）；CoreWeave 10-Q（期末 2026-06-30）；Microsoft FY26 10-K（期末 2026-06-30）。下一檢查點＝CoreWeave Q3 10-Q（約 2026-11）、Oracle FQ2 FY27（約 2026-12）。

## 1. 落差一句

會計恆等：資產於「placed in service」時才開始提折舊；故當期折舊 `D_t` 只反映在用資產，而資產負債表上之在建工程（CIP）已鎖定一個**下限之折舊步升** `ΔD ≥ Σ_j CIP_j ÷ L_j`（j＝伺服器／建物；忽略報廢與減損）。管線比 `π ≡ (Σ CIP_j ÷ L_j) ÷ D_t^{年化}` 為申報層可算之無量綱量。`[D]` 本輪初算（伺服器年限 6 年、CIP 全視為伺服器，故為上界側）：Oracle 2026-08-31 CIP 48,546M／PP&E 總額 153,596M（31.6%；前季 32.6%），季折舊 3,156M → `π` ≈ 0.64；CoreWeave 2026-06-30 CIP 11,918M／52,622M（22.6%；前期 27.6%），季 D&A 1.4B → `π` ≈ 0.35。種子主張：毛利率指引與賣方模型若以「資本支出 ÷ 年限」平滑攤提，會錯置折舊步升之**時點**（集中於轉入季）；`π` 為其可拒絕之量。本卡不定方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（折舊起點規則；ASC 360 placed-in-service）；非守恆、非誘因 |
| 可見端 | PP&E 附註之「Construction in progress」列（Oracle 註(2)「servers, networking equipment and leasehold improvements to be deployed」；CoreWeave；Meta 亦列 80,345M，但非 L6）；各類資產年限（Oracle 伺服器 6 年）；季折舊（現金流量表） |
| 指名不可見端 | Microsoft 10-K 無 CIP 列（「Construction」6 筆皆風險因子；只揭建物承諾 34.6B 與應付設備款 26.7B）；Alphabet、Amazon 10-Q 無 CIP 列（`sec.py` 0 筆；10-K 待查）；CIP 內伺服器 vs 建物拆分；轉入時點 |
| 對照式（生成用） | `D_{t+k} − D_t ≥ Σ_j CIP_{j,t} ÷ L_j − 報廢`。可拒絕：若 CIP 大幅下降之季（轉入使用）折舊未出現對應步升，或 CIP 主要為建物（L ≈ 40 年）使 `π` 小到不具量級 |
| 表達工具型態（只指名，不選券） | 美股雲端／AI 基礎設施服務商（Oracle、CoreWeave；次為揭露 CIP 之他者）。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Oracle FQ1 FY27 10-Q（期末 2026-08-31）。https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm （PP&E 附註 3；現金流量表折舊）
2. CoreWeave 10-Q（期末 2026-06-30）。https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm （附註 5）
3. Microsoft FY26 10-K。https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm （PP&E 表無 CIP；為不可見端之證據）
4. 二手（共識候選）：Trefis「The Bill For Oracle's AI Build Arrived Before The Revenue」（2026-08-31）https://www.trefis.com/articles/613728/the-bill-for-oracles-ai-build-arrived-before-the-revenue/2026-08-31 （未實讀）
5. 測一須另取：Oracle ≥ 4 季 CIP、各類資產與折舊序列（含 FY26 10-K）；CoreWeave ≥ 4 季同列；Amazon／Alphabet 10-K 是否列 CIP；管理層原文是否已給折舊步升之時點指引；具名賣方是否以 CIP 轉入建模折舊。**不宣稱已錯價。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 「成本先於營收」已是公開敘事，市場已讀 CIP | Trefis 2026-08-31（#4）；CoreWeave 折舊評論多 | 落差消失 |
| R2 | 管理層已逐季指引毛利率與折舊，步升時點已內含於指引 | 待原文（Oracle、CoreWeave 法說） | 被指引吸收 |
| R3 | CIP 轉入與營收起算同季（租約／合約以交付觸發），步升與營收配對，對毛利率中性 | L6-A#1 之交付機制 | 量級抵銷 |
| R4 | CIP 多為建物（長年限），伺服器到貨即轉入，`π` 實際遠小於上界側初算 | 待附註拆分 | 量級不足 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) CIP 與折舊於 ≥ 4 季不可並列，或 CIP 內伺服器／建物不可拆、使 `π` 區間寬到無判別力（可觀測性失敗）。
(2) 具名賣方或研究機構原文已以 CIP 轉入時點建模折舊步升或毛利率（共識）。
(3) 管理層原文已給折舊步升之時點與量級指引（R2），使恆等式無資訊增量。
(4) 可運作對照只能寫成已簽約未交付營收比（L6-A#1）、未開始租約（L13-A）、利息資本化（L2-A#2）或折舊年限（C-A3）。
(5) 轉入使用與營收起算經原文確認同步（R3），使 `π` 對毛利率之淨效果不可分離。
(6) 只有 ≤ 1 家 L6 主體揭露 CIP 列（Microsoft／Amazon／Alphabet 皆無），使表達只剩單一主體。

複查觸發器（若日後殺）：Microsoft、Amazon 或 Alphabet 於 10-K／10-Q 首次分列 CIP；任一 L6 主體分列 CIP 內伺服器 vs 建物；管理層首次給出轉入時點指引。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：PP&E 附註 CIP 列、折舊（現金流量表）、雲端分部毛利率、資本支出、應付設備款。
2. 可交易工具：Oracle、CoreWeave 等美股與選擇權。
3. 半衰期：CIP 轉入週期（伺服器數季、建物 1–3 年）；`[V]` 不寫。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L6［A］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L6-A#1／#2、L6-P#1–#3、L6-I#1／#2、L13-A／#2、L2-A#2、L3-A#2、C-A3／C-A4 結論。
