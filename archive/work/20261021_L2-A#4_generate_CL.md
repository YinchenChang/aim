# L2-A#4 生成卡｜資料中心實體：會計恆等（出租方之租期－耐用年限錯配：租期末帳面殘值恆等式 BV_T ≡ C·(1 − T/L)，AI 專用設施於首租期結束時仍有大比例未折舊成本）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260913_L2-A_test2_cost-index_GK.md；archive/work/20261007_L2-A#2_generate_CL.md；archive/work/20261014_L2-A#3_generate_CL.md；work/20261018_L6-A#3_test1_CL.md | EMITS: work/20261021_L2-A#4_generate_CL.md -->
**日期：** 2026-10-21　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 2→3／6）　**格：** L2-A　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L2-P#4 本日測一，Q-0082 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-14 之五格（L2-A#3、L14-I#2、L15-P／A／I#2），依表序取第一 → **L2-A**。既有 #1–#3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `data center useful life depreciation lease term`，回 19 筆，無一涉耐用年限或租期（多為 GPU 單價、PUE、模型算力）；未用。
- 比對（須異型）：
  - **L2-A**（`archive/drive/USED_20260913_L2-A_test2_cost-index_GK.md`）：建置成本指數。本卡不涉成本水準。
  - **L2-A#2**：利息資本化墊高 AFFO（資本化時點）。本卡為**完工後**折舊年限 vs 租期。
  - **L2-A#3**：電力轉嫁總額認列（營收分子）。不涉。
  - **L6-A#3**（`work/20261018_L6-A#3_test1_CL.md`）：CIP 轉入之折舊管線**時點**。本卡為年限**長度**與租期錯配之期末殘值。
  - **C-A3**（ARCH_dead #5）：GPU 折舊年限（雲端層、伺服器）。本卡限出租方之建物／機電，非伺服器。
  - **L13-A**（承租方未開始租／RVG）：承租方負債側；本卡為出租方資產側。Moody's 2026-02 報告（承租方揭露）為鄰接，不構成重疊。
- §7-10 領域最近公開：APLD 10-K FY26（期 2026-05-31）；DLR 10-Q 2Q26（期 2026-06-30）。下一檢查點＝APLD 10-Q FQ1 FY27（2026-10）、DLR 10-Q 3Q26（2026-11）。

## 1. 落差一句

出租方（AI 專用資料中心開發商）以 ~15 年租約出租，但建物、機電以 15–39 年直線折舊；恆等式 \(BV_T = C\,(1 - T/L)\) 使首租期結束時帳上仍留大比例成本，租期內 GAAP 折舊低於「租期內回收」折舊 \(C/T\)，報表 EBIT／EBITDA 與租約收益率隱含對續租或殘值之假設。可拒絕之主張＝≥ 2 家出租方之 \(\sum_j C_j(1 - T/L_j)/\sum_j C_j\) ≥ 30%（`[D]`）且附註／MD&A／賣方未揭露或未調整續租假設。若出租方已以租期折舊專用資產、或租約含殘值保證／買回、或賣方已以租期回收計價，本卡死。不主張任何主體價值方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **會計恆等（A）**：(i) \(D_t = \sum_j C_j/L_j\)；(ii) \(BV_T = \sum_j C_j(1 - T/L_j)\)；(iii) 租期內回收缺口 \(G = \sum_j C_j/T - D_t\)（年）；(iv) 殘值比 \(\rho \equiv BV_T/\sum C_j\) |
| 選擇者 | 出租方管理層（年限估計，ASC 360）；承租方（續租選擇權，非出租方可控） |
| 可見端 | 10-K PP&E 附註之類別×年限×成本；租約附註之租期、續租選擇權、終止權、殘值保證；出租方 MD&A 之收益率／「stabilized yield」口徑 |
| 指名不可見端 | 續租機率；AI 專用機電（液冷、高密度配電）之經濟壽命；租約到期時之再出租價格 |
| 量綱 | 年；\(\rho\) 無因次；\(G\)＝美元／年（只作比例，不寫金額） |
| 外部參照物（測一查證） | DLR 建物「5 - 39 years」、in-place lease「weighted-average of 13 years」（同檔可並列年限與租期） |
| 表達工具型態（只指名，不選券） | 美股、以長租 AI 設施為主之出租方普通股；不選券 |
| 重疊 | C-A3（折舊年限，資產不同）；L13-A（租約，側不同）；L6-A#3（折舊，時點 vs 長度） |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Applied Digital 10-K FY26（sec.py）https://www.sec.gov/Archives/edgar/data/1144879/000114487926000048/apld-20260531.htm ：PP&E 附註「Mechanical infrastructure 20 years 71,939」「Electrical infrastructure 15 years 104,491」「Electric generation and transformers 15 years - 30 years 188,110」「Building 39 years 279,308」「Building improvements 15 years - 25 years 682,348」「Construction in progress 2,776,232」（千美元）；租約「approximately 15-year lease (with three five-year renewal options)」。`[D]` 示意：39 年建物於 15 年租期末 \(1-15/39\)＝62% 未折舊；15 年機電＝0%。
2. Digital Realty 10-Q 2Q26（sec.py）https://www.sec.gov/Archives/edgar/data/1297996/000110465926089296/dlr-20260630x10q.htm ：「Buildings are depreciated on a straight-line basis over an estimated remaining useful life of 5 - 39 years」；「remaining non-cancelable lease terms (weighted-average of 13 years …」（收購 PPA 段）。
3. 待測一補：Galaxy（Helios，15 年 CoreWeave 租約）、Cipher（Black Pearl 15 年）、TeraWulf 10-K PP&E 年限表（本輪 sec.py 10-Q grep「useful li」GLXY 無 PP&E 年限、CIFR 只見礦機 3 年與租賃改良「lesser of」）。
4. 鄰接（承租方側，非本卡證據）：Moody's 2026-02（DCD 報導 https://www.datacenterdynamics.com/en/news/moodys-hyperscalers-understating-risks-of-short-term-ai-dc-lease-agreements-leaving-investors-in-the-dark/ ）：租期趨短、「toward the life of compute hardware」；RVG 不入承租方負債。

缺段（§7-2）：未取出租方任一家按資產類別之成本分配至 AI 專用 vs 通用；未取賣方以租期或續租假設計價之原文；GLXY／CIFR／WULF 10-K 年限表未讀。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 殼、電力接入、土地之經濟壽命遠長於 GPU，「everything under the GPU lasts longer」；長年限合理 | electroneconomics（https://electroneconomics.substack.com/p/everything-under-the-gpu-lasts-longer ，搜尋得，未讀） | 機制反向 |
| R2 | 租約含續租選擇權（APLD 三次五年），續租機率高 | APLD 10-K 原文 | \(T\) 應含續租 |
| R3 | 賣方以 NAV／EV／MW 或重置成本估值，不用 GAAP 折舊 | 待測一 | 不進定價 |
| R4 | 減損測試（ASC 360 未折現現金流）在到期前觸發即揭露 | APLD 10-K 減損段 | 落差有揭露機制 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀 ≥ 3 家長租 AI 出租方 10-K，\(\rho\) ≥ 30% 者 < 2 家（或年限 ≤ 租期為常態）；或
(2) 出租方已就 AI 專用資產以租期折舊、或租約含殘值保證／承租方買回條款，使 \(\rho\) 由承租方承擔；或
(3) 具名賣方、評等機構原文已以租期回收或續租機率調整出租方盈餘／估值（已定價）；或未能取得任何以 GAAP 折舊盈餘或 AFFO 定價之具名原文（落差無市場端）；或
(4) 可運作對照只能寫成 GPU 年限（C-A3）、CIP 時點（L6-A#3）、承租方負債（L13-A）或利息資本化（L2-A#2）；或
(5) 12 個月內無檢驗事件（年限估計變更、減損、續租／終止公告、首租約到期）；或
(6) 首批 AI 租約到期在 2036-10-15 實驗期之後，且 12 個月內無任何能使 \(\rho\) 重定價之中間事件（重定價窗 > 剩餘期，§1）。

複查觸發器（若日後殺）：任一出租方變更機電年限估計；首件 AI 長租提前終止或不續租公告；評等機構發布出租方殘值方法論。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：PP&E 年限表、折舊費用、租約附註。2. 可交易工具：長租出租方普通股（不選）。3. 半衰期：年限估計變更或減損為事件型；租期末為 ~15 年。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0083；`query/ARCH_matrix.md` L2［A］加「#4 已生成」；`AIM_FUNNEL.md` §3 一句與日期行。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L2-A／#2／#3、L2-P#1–#4、L2-I／#2／#3、L6-A#3、L13-A、C-A3；不碰 L1-P；不寫 T。
