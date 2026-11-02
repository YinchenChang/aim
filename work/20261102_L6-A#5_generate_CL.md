# L6-A#5 生成卡｜雲端與基礎設施服務：會計恆等（分部損益之未分攤項：`OI_合併 ≡ Σ OI_分部 ＋ OI_未分攤`；前沿模型開發成本列「Alphabet-level activities」而不入 Google Cloud 分部，分部利潤率不含其所售模型之開發成本）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260927_L6-A_generate_GK.md；archive/work/20261011_L6-A#2_generate_CL.md；archive/work/20261018_L6-A#3_generate_CL.md；archive/work/20261026_L6-A#4_generate_CL.md；archive/work/20261018_L6-P#3_generate_CL.md；archive/work/20261013_L7-A#2_generate_CL.md | EMITS: work/20261102_L6-A#5_generate_CL.md -->
**日期：** 2026-11-02　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3／6）　**格：** L6-A　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L6-P#5 本日測一，Q-0148 done）。各格最後測試日最舊＝2026-10-26（L6-A#4、L6-I#4、L13-A#4）；依表序取 **L6-A**；非已殺、非刻意排除。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py segment allocation "Alphabet-level"`，**命中 0 筆**；未使用。內部數字（§12）未取用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L6-A#1**（GK；RPO 營收領先比）：營收時序。本卡不涉營收時點，涉**成本歸屬於哪一報告分部**。
  - **L6-A#2**（電費轉嫁 θ，ASC 606 總額／淨額）：營收組成。不同型。
  - **L6-A#3**（CIP 折舊起點）／**C-A3**（折舊年限）：折舊時點與量。本卡不改任何成本之時點或量，只改其**分部歸屬**（ASC 280）；合併損益不變。
  - **L6-A#4**（ASC 230 capex 現金流分類）：現金流節別。不同型。
  - **L6-P#3**（機群容量守恆 `K_ext + K_1P + K_RD`）：實體容量分配之守恆。本卡為**報告層**成本歸屬，容量是否互換不入式。
  - **L7-A#2**（實驗室持股計量 → 營業外損益）：營業外。本卡全在營業利益之內。**L8-A#4**（衡量替代法持股帳面）：資產負債表。不同型。
  - 重疊列為否決 (5)。
- §7-10 領域最近公開：Alphabet 10-Q 期 2026-09-30（2026-10-29）；Microsoft 10-Q 期 2026-09-30（2026-10-28；FY27 起分部改組並重編）；Amazon 10-Q 期 2026-09-30（2026-10-30）；Oracle FQ1 FY27 10-Q（2026-09-11）。下一檢查點＝Alphabet FY26 10-K（約 2027-02）、Oracle FQ2 FY27（約 2026-12）。

## 1. 落差一句

ASC 280 之加總恆等：`OI_合併 ≡ OI_Services ＋ OI_Cloud ＋ OI_OtherBets ＋ OI_ALA`。Alphabet 原文：未分攤至分部者主要為「certain AI-focused shared research and development activities, including employee compensation expenses and technical infrastructure usage costs associated with the development of our general AI models」（Note 15）；MD&A：「Alphabet-level activities primarily reflect expenses related to our shared AI research and development」。Google Cloud 對外出售以這些通用模型為核心之服務（Gemini／Vertex）與 TPU 系統，但其分部營業利益**不承擔模型開發成本**。定義無量綱 `χ ≡ |OI_ALA| ÷ OI_Cloud` 與「依營收比分攤後之分部利潤率差」`Δm ≡ s_Cloud·|OI_ALA| ÷ Rev_Cloud`（`s_Cloud`＝Cloud 營收 ÷ (Services＋Cloud) 營收，一種可替換之分攤鍵）。`[D]` 本輪初算（皆 `[V]` 一手申報 10-Q 期 2026-09-30，單位百萬美元；`[D]` 自算）：
- 3Q26：Cloud 營收 30,709、OI 11,121（分部利潤率 36.2%）；ALA −7,655 → `χ` ≈ 0.69；`s_Cloud` ≈ 24.2% → 分攤 ≈ 1,851 → `Δm` ≈ 6.0 pp（調整後 ≈ 30.2%）。
- 3Q25：Cloud 營收 15,157、OI 3,594（23.7%）；ALA −4,467 → `χ` ≈ 1.24；`s_Cloud` ≈ 14.8% → `Δm` ≈ 4.4 pp。
- 9M26：Cloud 營收 75,505、OI 26,533（35.1%）；ALA −18,835（9M25 −10,866，＋73%）→ `χ` ≈ 0.71。
種子主張：若市場與賣方以「Google Cloud 分部利潤率」與 AWS（Amazon 原文：基礎設施成本「allocated to the AWS segment based on usage」，無未分攤 AI 研發列）或 Azure 比較、或以分部 OI × 倍數作 SOTP，則 Cloud 之利潤率擴張有一部分為**歸屬邊界**而非單位經濟；ALA 增速（＋71% YoY 於 3Q）高於合併 OI 增速（＋30%），使邊界效應隨模型開發投入擴大。本卡不定方向與量級是否足以定價；分攤鍵（營收、使用量、推論 token 比）之選擇本身為測一對象，不由本卡凍結。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等（ASC 280 分部報告；CODM 口徑之未分攤項）；非守恆、非誘因 |
| 選擇者 | 申報主體（CODM 報告結構）；恆等式本身無選擇 |
| 可見端 | Alphabet 10-Q Note 15 分部營收／OI／ALA 與分部費用補充（Cloud「Employee compensation」7,081／「Other costs and expenses」12,507，3Q26）；MD&A 分部獲利段；Cloud MD&A 新增「inventory and related costs associated with the sale of TPU systems」 |
| 指名不可見端 | ALA 內模型開發 vs 公司層費用（法務、慈善、資遣）之拆分；模型開發之基礎設施使用成本金額；推論成本 vs 訓練成本歸屬；Microsoft FY27 起「Agents and Infra」分部合併應用、多模型系統與 Azure 基礎設施（重編），Azure 單獨利潤不可見；Amazon 模型（Nova 等）開發成本落於哪一分部未明文 |
| 對照式（生成用） | `m_Cloud,adj ≡ (OI_Cloud − k·|OI_ALA|) ÷ Rev_Cloud`，`k`＝分攤鍵。可拒絕：若在任一合理 `k`（營收比、算力使用比）下 `Δm` ＜ 3 pp，或 ALA 中模型開發占比經原文確認為小 |
| 表達工具型態（只指名，不選券） | 美股雲端／AI 平台主體（Alphabet；比較組 Amazon、Microsoft、Oracle）。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Alphabet 10-Q 期 2026-09-30（Note 15 分部、MD&A 分部獲利）。https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm
2. Alphabet 8-K Ex 99.1 4Q24 新聞稿（ALA 歷史口徑；Gemini app 團隊成本仍列 Services 之原文）。https://www.sec.gov/Archives/edgar/data/1652044/000165204425000010/googexhibit991q42024.htm
3. Amazon 10-Q 期 2026-09-30（Note 8：Technology and infrastructure 依使用量分攤至 AWS；無未分攤列）。https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm
4. Microsoft 10-Q 期 2026-09-30（「Recast of Certain Prior Period Information」；Agents and Infra 分部）。https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm
5. Oracle FQ1 FY27 10-Q（分部 margin 僅「direct controllable costs」，研發全不分攤；比較組口徑差異）。https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm
6. 二手：MBI Deep Dives「Alphabet 2Q'26: Google Cloud is On Cloud Nine」（2026-07-23；引 2Q24 申報「prospectively beginning in the second quarter of 2024」AI 模型團隊移入 ALA；建議看合併利潤率）https://www.mbi-deepdives.com/goog2q26/ （前段實讀，後段付費牆）
7. 測一須另取：Alphabet 2Q24 8-K／10-Q 之 ALA 移列原文與是否重編；≥ 6 季 ALA 與 Cloud OI 序列；具名賣方 SOTP 是否扣 ALA 或以合併計價；法說中管理層就 Cloud 利潤率與模型成本歸屬之原文；Amazon、Microsoft 模型開發成本歸屬原文。**不宣稱已錯價。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 分部利潤率之邊界問題已是公開敘事；分析者已建議改看合併利潤率 | MBI Deep Dives 2026-07-23（#6） | 落差消失（已知） |
| R2 | Alphabet 以合併 EPS／FCF 定價，Cloud 未上市、無獨立價格，分部利潤率不是定價變數 | §7-4 可交易工具題 | 不可表達 |
| R3 | 比較組亦各有口徑差（Oracle 研發全不分攤；Microsoft 已合併 Azure 與應用），「Cloud 利潤率」本無可比基準，市場不以之跨主體比較 | 載體 #4、#5 | 無判別力 |
| R4 | ALA 主要服務 Services（搜尋、Gemini app），Cloud 合理分攤份額低 | 分攤鍵未知；Gemini app 成本仍列 Services（#2） | 量級不足 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) Alphabet 原文或測一實讀確認 ALA 中通用模型開發占比不可估，或任一合理分攤鍵下 3Q26 `Δm` ＜ 3 pp（量級不足）。
(2) ≥ 2 家具名賣方或主要媒體之 Alphabet SOTP／Cloud 估值已扣 ALA 或明確以合併利潤率計價（R1 成立）。
(3) Alphabet 於 12 個月內預告或執行將模型開發成本分攤至分部之重編（落差半衰期 ＜ 12 個月窗）。
(4) 比較組（Amazon、Microsoft）原文顯示其模型開發成本同樣不入雲端分部，使 Google Cloud 與 AWS／Azure 之邊界差為零（R3 成立）。
(5) 可運作對照只能寫成 RPO 時序（L6-A#1）、電費總額法（L6-A#2）、折舊起點或年限（L6-A#3／C-A3）、capex 現金流分類（L6-A#4）、容量分割（L6-P#3）或持股計量（L7-A#2／L8-A#4）。
(6) 無任一可交易工具之定價可證以 Cloud 分部利潤率為輸入（R2 成立，§7-4 不可表達）。

複查觸發器（若日後殺）：Alphabet 首次單列 ALA 中模型開發之美元數或重編分部；或 Google Cloud 以任何形式分拆、追蹤股或單獨融資。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Note 15 分部 OI、ALA、分部費用補充；MD&A 分部獲利。
2. 可交易工具：Alphabet 美股與選擇權（比較組 Amazon、Microsoft、Oracle）。不選券。
3. 半衰期：分部結構季內可改（Microsoft FY27 即重編）；`[V]` 不寫。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L6［A］標「#5 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md`（ALA 3Q26 一筆；Cloud 3Q26 營收已有 2026-10-31 列，不重複）。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L6-A#1–#4、L6-P#1–#5、L6-I#1–#4、L7-A#2、L8-A#4、C-A3 已測或已殺結論。不寫 T、不寫 H1。
