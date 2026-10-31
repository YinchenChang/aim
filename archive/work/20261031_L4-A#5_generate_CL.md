# L4-A#5 生成卡｜運算硬體系統：會計恆等（確定採購承諾之損失預提：報告毛利率＝組合毛利率 −（提列 − 回轉）／營收；表外供應承諾為未來提列之上界）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260926_L4-A_generate_GK.md；archive/work/20261011_L4-A#2_generate_CL.md；archive/work/20261017_L4-A#3_generate_CL.md；archive/work/20261025_L4-A#4_generate_CL.md；work/20261025_L4-A#4_test1_CL.md | EMITS: work/20261031_L4-A#5_generate_CL.md -->
**日期：** 2026-10-31　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L4-A　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L4-P#5 本日已測一）。最後測試日最舊＝2026-10-25（L4-A#4、L4-I#4、L5-P#4、L5-A#4、L12-A#4、L12-I#4）；依表序取 **L4-A**；非已殺、非刻意排除。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py "inventory provision" "purchase obligation" "supply commitment"`，命中 **0** 筆。內部研究數字（§12）未取用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L4-A#1**（`archive/drive/USED_20260926_L4-A_generate_GK.md`）：BOM 份額恆等；死於 BOM 不在申報層。本卡所需量（提列、回轉、承諾分年表）皆為申報附註項。
  - **L4-A#2**（`archive/work/20261011_L4-A#2_generate_CL.md`）：整機商 CCC／OCF 恆等。本卡物件為**損益表營業成本中之損失預提**（ASC 330-10-35 存貨跌價與確定採購承諾損失），非現金時序；主體為晶片設計商，非整機商。
  - **L4-A#3**（`archive/work/20261017_L4-A#3_generate_CL.md`）：客戶權證收入減項（營收端）。本卡在成本端，無權證、無股價反身性。
  - **L4-A#4**（`archive/work/20261025_L4-A#4_generate_CL.md`；測一死於 (2)：淨額法只同額縮減營收與成本，毛利**金額**、core EPS、FCF 不變）。本卡之提列**直接改變毛利金額與 EPS**，不受該死因約束。
  - **N-01**（機隊世代組成非科目）：本卡之世代轉換只經由已揭露之提列科目作用，不需世代組成。**L2-I#3**（backlog 取消誘因）：彼為供應商端合約負債，本卡為買方（晶片商）對其上游之承諾損失。**C-I3′**、**N-02**、**L13-A#2**：構成不同。
- §7-10 領域最近公開：NVIDIA 10-Q 2Q FY27（期末 2026-07-26，申報 2026-08-26）；AMD 10-Q 2Q26（申報 2026-08-05）。下一檢查點＝NVIDIA 3Q FY27 10-Q（期末 2026-10-25，約 2026-11 下旬）。

## 1. 落差一句

NVIDIA 2Q FY27 10-Q Note 10：供應與產能承諾「from $119 billion last quarter to $279 billion」，分年 FY27 餘 92／FY28 87／FY29 88／FY30 6（十億美元），「for our data center infrastructure systems, primarily memory and manufacturing facilities … across current and future product architectures」，且僅「in certain instances … may be cancelable, rescheduled, or adjustable」；同期 MD&A：存貨與超額採購義務提列 985M、回轉 177M，對毛利率淨影響 −0.8pp（毛利率 75.0%），資產負債表「Excess inventory purchase obligations」2,138M。前例：FY26 1Q H20 一次 4.5B 提列使上半年毛利率淨影響 −5.9pp；AMD MI308 同型。故 **報告毛利率 ＝ 組合毛利率 −（提列 − 回轉）／營收**，而提列之上界由**不可撤銷承諾 ×（架構或需求錯配之損失率）** 決定，承諾規模約為單季營收（96.2B）之 2.9 倍。落差＝市場若以 mid-70s 毛利率指引為結構值，則承諾在 FY28–FY29 之集中（175B）意味一次架構／需求／記憶體價格錯配即可在單季轉為數個百分點之毛利率衝擊；反之若需求持續，歷史提列之回轉可推高毛利率。**方向未定**。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（成本計量）：`GM% = GM%_mix − (Prov − Rel) / Rev`；`Prov ≤ Inv + Commit_noncancel − NRV`（ASC 330-10-35-17/18 確定採購承諾損失須於預期時認列）。非守恆、非誘因 |
| 量綱 | `Commit`［$］；`Commit / Rev_q`（季）；`(Prov − Rel)/Rev`（pp）；敏感度 `s = Commit_noncancel × ℓ / Rev_4Q`，`ℓ`＝損失率（無量綱） |
| 可見端（實讀） | NVIDIA 2Q FY27：營收 96,221M；毛利率 75.0%；存貨 31,575M（原料 11,341）；超額採購義務負債 2,138M（FY26 末 2026-01-25：2,739）；存貨提列 784M（2Q）；提列＋義務 985M、回轉 177M；承諾表如上；客戶預付 2.8B。AMD 2Q26：無條件承諾 30.3B（2026 餘 17.4B）；毛利率 54%（前年 40%，MI308 存貨相關費用不再）|
| 指名不可見端 | 承諾中不可撤銷之比例；承諾按架構（Blackwell Ultra／Rubin／後續）與品項（HBM、晶圓、封裝）之分布；固定價 vs 指數價；供應商取消費率 |
| 主張 | 報告毛利率對「承諾之架構特定性 × 需求錯配」有機械性依存；承諾 ÷ 營收上升時，同一損失率對毛利率之衝擊等比放大 |
| 外部參照物（測一查證） | NVIDIA H20（FY26 1Q 4.5B）、H200（FY27 上半年 0.4B）、AMD MI308；僅作會計路徑先例，非量級 |
| 表達工具型態（只指名，不選券） | 美股上市 AI 加速器設計商普通股與上市選擇權。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| NVIDIA 10-Q 2Q FY27（Note 4 存貨、應計負債、Note 10 承諾、MD&A 毛利率段、風險因子） | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm |
| NVIDIA 10-K FY26（承諾、提列政策、H20 費用） | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm |
| AMD 10-Q 2Q26（無條件承諾、MI308 存貨相關費用、預付安排風險因子） | https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm |
| 公開討論承諾規模之二手（測一核原文與是否及於提列機制） | https://www.barchart.com/story/news/4406785/michael-burry-called-nvidias-95-billion-in-purchase-obligations-troubling-in-february-six-months-later-the-filings-show-that-number-ballooned-to-279-billion ；https://www.nasdaq.com/articles/nvidias-supply-commitments-more-doubled-279-billion-heres-what-it-does-stock ；https://www.tikr.com/blog/nvidias-1-1-billion-kyec-deal-is-the-small-number-in-a-279-billion-supply-bet |
| NVIDIA 2Q／3Q FY27 法說逐字稿、具名賣方模型 | 測一取得 |

不宣稱提列風險已入或未入共識、不宣稱方向。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 承諾規模已為公開議題（Michael Burry 2026-02 稱 95B 採購義務「troubling」；279B 經多家媒體報導），市場已折價 | Barchart、Nasdaq 轉載（上表） | 落差已揭露（須查是否及於提列 → 毛利率之映射，或僅規模） |
| R2 | 管理層指引與賣方模型以 non-GAAP 毛利率為主，大型一次性提列被排除或被視為一次性 | 測一查 NVIDIA non-GAAP 調節（H20 費用之處理） | 落差不影響定價（L4-A#4 型死因之變體；須查實際口徑） |
| R3 | 承諾主要為記憶體與產能保留，可跨架構挪用；架構錯配不構成損失，只剩價格風險 | Note 10 原文「primarily memory and manufacturing facilities … current and future product architectures」 | 損失率 `ℓ` 近 0，機制弱化 |
| R4 | 承諾多可撤銷／重排（10-Q 原文），不可撤銷部分小 | Note 10 原文 | 上界不可計算或過小 |
| R5 | 需求遠超供給（客戶預付 2.8B、供給受限敘述），損失需需求斷崖，12 個月內機率低 | 10-Q 風險因子與 MD&A | 機制真、窗內不發生 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) NVIDIA 申報／法說或 ≥ 1 位具名賣方已將承諾規模映射為提列或毛利率敏感度（不只報導規模）（R1）。
- (2) 主要估值與指引口徑排除承諾損失提列，且公開層無以 GAAP 毛利率或 GAAP EPS 定價之具名證據（R2）。
- (3) `[D]` 量級（凍結）：`s = (FY28＋FY29 承諾) × 5% ÷ 最近 4 季營收` **< 2%** 即否決；不可撤銷比例若可得，以之替代全額。
- (4) 一手原文顯示承諾主要為可跨架構挪用之記憶體／產能且價格非固定（R3），或不可撤銷部分無法自公開層界定亦無代理量（R4）。
- (5) 本卡只能以 L4-A#2（CCC）、L2-I#3（backlog 取消）、N-01（世代組成）或 L4-A#4（營收淨額口徑）重述。
- (6) 12 個月內無檢驗事件（NVIDIA 3Q FY27 10-Q 約 2026-11、FY27 10-K 約 2027-03、架構轉換時程公告、HBM 合約價格公告）。

複查觸發器（若日後殺）：NVIDIA 或 AMD 首次揭露承諾之不可撤銷比例或按架構分列；單季提列 ÷ 營收 ≥ 2%；具名賣方首次以承諾 × 損失率建模毛利率。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：營業成本中之存貨與採購義務提列、提列回轉、應計負債「Excess inventory purchase obligations」、Note 10 承諾表、non-GAAP 毛利率調節。
2. 可交易工具：美股上市 AI 加速器設計商普通股與上市選擇權（不選）。
3. 半衰期：季（10-Q 逐季揭露提列與承諾；架構轉換約 12 個月一代）。

## 7. 本輪寫入

本卡；QUEUE Q-0141（ANALYST 測一）；ARCH_matrix L4［A］格標「#5 已生成」；FUNNEL §3 未測格；`export/LEADS_算力收支.md` 追加 3 列（NVIDIA 10-Q 2Q FY27 ×2、AMD 10-Q 2Q26）。不改 L4-A#1–#4、L4-P#1–#5、L4-I#1–#4、L2-I#3、C-I3′、N-01、N-02。
