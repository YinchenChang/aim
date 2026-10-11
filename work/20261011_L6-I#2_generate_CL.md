# L6-I#2 生成卡｜雲端與基礎設施服務：誘因（代理人誘因：bookings 計酬不定價交付時程與合約結構 → RPO 增速 ≠ 可交付之經濟價值增速）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260928_L6-I_generate_GK.md；archive/drive/USED_20260928_L6-I_test1_GK.md；archive/drive/USED_20260929_L6-I_T_GK.md；archive/work/20261011_L6-P#2_generate_CL.md；work/20261011_L6-P#2_test1_CL.md；work/20261011_L6-A#2_test1_CL.md；work/20261011_L4-I#2_test1_CL.md | EMITS: work/20261011_L6-I#2_generate_CL.md -->
**日期：** 2026-10-11　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 4→5／6）　**格：** L6-I　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L6-P#2 已於本日測一，Q-0023 done）。尚無 #2 且非已殺／刻意排除之格中，最後測試日最舊者並列 2026-09-29（L6-I、L13-A 之 T；L6-P 已有 #2）；以列序（層序）→ **L6-I**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py bookings compensation incentive RPO`，**命中 0 筆**。
- 比對之舊檔與死因型態，本卡須異型：
  - **L6-I#1**（T `archive/drive/USED_20260929_L6-I_T_GK.md`）：backlog 變厚≠對手方變好——**選擇者＝對手方**（逆選擇）。本卡**換選擇者**：賣方內部代理人（計酬對象），誘因來自計酬指標設計，不論對手方品質。
  - **L6-P#2**（本日測一不通過）：MW·h 交付守恆、ρ 不可界定。本卡不換算 MW，不需 ρ。
  - **L6-A#2**：電費轉嫁之營收會計。本卡不論電費。
  - **L4-I#2**：加速器商之表外回租／擔保讓渡價格（供給端誘因）。本卡為雲業者之內部計酬，不論供應商承諾。
  - **L13-A／L13-I**：租賃義務上界、融資載具比例。本卡不估義務、不論融資。
  - **T-15**（CoreWeave 空方，委託資本外）：不寫；CoreWeave 2026 DEF 14A「bookings」「backlog」0 筆，本卡亦不以其為載體。
- §7-10 領域最近公開：Oracle 2026 DEF 14A（申報 2026-09-25，涵蓋 FY26）；Oracle FQ1 FY27 10-Q 附件 10.07（FY27 獎金計畫，申報 2026-09）。下一檢查點＝Oracle FY27 DEF 14A（約 2027-09）、各季 10-Q RPO 分段。

## 1. 落差一句

Oracle 現場業務負責人之年度獎金以 bookings 為主要權重（原文：「Total Non-GPU Infrastructure Bookings, weighted 30% • GPU Bookings, weighted 10% • Total SaaS Bookings Growth, weighted 10% • Non-GAAP Software Revenue Growth, weighted 20% • Non-GAAP Total Operating Income Growth, weighted 30%」），FY26 bookings 類達成「150 %」、營收類「92 %」、營業利益類「95 %」（DEF 14A）。bookings 指標於原文不區分合約期限、認列時程、預付或客供 GPU 結構；同期 RPO 增量「Most … were large scale AI contracts where the customer prepaid Oracle for the purchase of the GPUs, or the customer bought and supplied the GPUs to Oracle」（8-K Ex.99.1）。種子主張：若計酬對 bookings 之邊際報酬不隨期限與毛利遞減，則代理人偏好長期、遠端認列、低單位毛利之大單，RPO 增速系統性高於可交付經濟價值增速；市場若以 RPO 增速計量成長，即錯置。本卡不定方向與量級，只立可拒絕之誘因鏈。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因（委託－代理；計酬指標之選擇性）；非守恆、非會計恆等、非逆選擇 |
| 選擇者 | 賣方代理人（NEO 及其下之業務組織）；薪酬委員會設計指標 |
| 可見端 | DEF 14A 指標權重與達成率；FY27 獎金計畫附件之指標選單（原文含「(b) bookings」「(d) contract value」「(g) data center openings or closings」）；10-Q／10-K RPO 認列分段（FY26 末 12%／34%／34%→FQ1 FY27 13%／37%／34%）；客戶預付遞延收入科目 |
| 指名不可見端 | bookings 之內部定義（是否折現、是否含客供硬體價值）；業務層（非 NEO）計酬；單筆合約之期限與毛利 |
| 主張 | bookings 權重高且不分期限 → RPO 結構往遠端與低毛利偏移；可由 RPO 分段之遠端占比、毛利率指引、或 bookings 定義原文拒絕 |
| 表達工具型態（只指名，不選券） | 美股上市雲供給者（Oracle 為唯一已見載體；其他業者以 DEF 14A 指標比對） |
| 重疊 | L6-I#1（同格不同選擇者）、L6-A#2（毛利）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Oracle 2026 DEF 14A https://www.sec.gov/Archives/edgar/data/1341439/000119312526402816/orcl-20260925.htm （Hura 五項權重與達成率；CEO 級為「Non-GAAP operating income growth」；長期激勵「achievement of long-term total revenue goals」——`sec.py` 本輪實讀）
2. Oracle FQ1 FY27 10-Q Ex.10.07 https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-ex10_07.htm （FY27 獎金計畫指標選單）
3. Oracle FY26 Q4 8-K Ex.99.1 https://www.sec.gov/Archives/edgar/data/0001341439/000119312526265848/orcl-ex99_1.htm （預付／客供 GPU 句；「$75 billion」）
4. Oracle FQ1 FY27 10-Q https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm （RPO 分段）；FY26 10-K https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm
5. 對照：CoreWeave 2026 DEF 14A https://www.sec.gov/Archives/edgar/data/1769628/000176962826000191/crwv-20260422.htm （「bookings」「backlog」「performance metric」0 筆）；IREN 2025 DEF 14A https://www.sec.gov/Archives/edgar/data/1878848/000114036125037383/ny20053824x2_def14a.htm （PRSU 以 TSR／股價門檻）
6. 測一須另取：Oracle bookings 之定義原文（法說或 10-K）；Microsoft／Amazon／Alphabet 最近 DEF 14A 之雲業務指標；具名賣方或治理研究對 Oracle bookings 計酬之評論。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | CEO 級與多數 NEO 只以非 GAAP 營業利益成長計酬；長期激勵綁「long-term total revenue goals」——高層誘因錨在交付後之營收／利潤 | DEF 14A（#1） | 誘因非主導 |
| R2 | 委員會已將 GPU bookings（10%）與 non-GPU（30%）分權，顯示已區分低毛利結構 | DEF 14A（#1） | 已部分定價結構 |
| R3 | 大型 AI 合約由共同 CEO／董事會層級議定，非現場業務驅動 | ERP Today（Tarsilla Moura，2026-06-11）https://erp.today/oracle-q4-2026-earnings-ai-cloud-backlog-funding/ 引 Magouyrk「bring-your-own-hardware or prepaid customer structures」 | 選擇者錯置 |
| R4 | 管理層已公開指引毛利下行「because of data center ramp timing and mix」——市場已知低毛利結構 | 同上（Maxson） | 已定價 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) Oracle bookings 之定義原文顯示已按期限折現、扣除客供硬體或以毛利加權（誘因鏈斷）。
(2) bookings 權重只及單一 NEO 且其下業務層無 bookings 計酬原文可得，而 R3 有原文（大單由 CEO／董事會議定）——選擇者不成立。
(3) RPO 分段之遠端占比（37–60 月＋其後）於 bookings 高達成期間未上升，或毛利率指引已明文歸因於合約結構（R4 成立，無錯置）。
(4) 具名賣方或治理研究已公開以 bookings 計酬解釋 RPO 結構（已定價）。
(5) 可運作對照只能寫成 L6-I#1 對手方逆選擇、L6-A#2 毛利會計、L4-I#2 供應商回租或 T-15。

複查觸發器（若日後殺）：任一美股雲供給者 DEF 14A 首次以 bookings／RPO／contract value 為高權重指標且揭露定義；或 Oracle 於申報層揭露 bookings 定義或 RPO 按毛利／期限分桶。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：RPO 與分段；客戶預付遞延收入；毛利率（OCI）；DEF 14A 指標。
2. 可交易工具：Oracle 美股（不選券）。
3. 半衰期：DEF 14A 年度一次；RPO 分段季度一次；遠端段認列落在 2029 後，長於 12 個月窗。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L6［I］標「#2 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L6-I#1 之 T、L6-P#2、L6-A#2、L4-I#2、L13-A、L13-I 結論；不寫 T-15。
