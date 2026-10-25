# L4-A#4 生成卡｜運算硬體系統：會計恆等（EMS 代工之主理人／代理人淨額認列：報告營收＝總吞吐 − 淨額零組件；營運資本吸收不入營收之零組件）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260926_L4-A_generate_GK.md；archive/work/20261011_L4-A#2_generate_CL.md；archive/work/20261017_L4-A#3_generate_CL.md | EMITS: work/20261025_L4-A#4_generate_CL.md -->
**日期：** 2026-10-25　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L4-A　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L12-I#4 本日已測一）。最後測試日最舊＝2026-10-17（L4-A#3、L4-I#3、L5-P#3、L5-A#3）；依表序取 **L4-A**；非已殺、非刻意排除。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py consigned consignment "net basis" ODM`，命中 0 筆。
- 比對之舊檔與死因型態，本卡須異型：
  - **L4-A#1**（`archive/drive/USED_20260926_L4-A_generate_GK.md`）：BOM 份額恆等；死於 BOM 不在申報層。本卡所需量（淨額零組件餘額、分部營收）為申報附註項。
  - **L4-A#2**（`archive/work/20261011_L4-A#2_generate_CL.md`）：整機商 CCC 恆等（OCF＝NI−ΔWC）。本卡物件為**營收計量口徑**（ASC 606-10-55-36～40 主理人／代理人），營運資本只作副產可見端；且主體為 EMS 代工，非 Dell／SMCI 整機商。重疊（同在營運資本科目）照記，不構成丟棄。
  - **L4-A#3**（`archive/work/20261017_L4-A#3_generate_CL.md`）：客戶權證收入減項；本卡無權證、無股價反身性。
  - **L13-A#2**（客戶預付入 OCF）、**L3-A#4**（NCI 歸屬）、**L13-A#3**（EPS 分母）、**C-A3／C-A4**（折舊年限）、**C-I3′**、**N-01**、**N-02**：構成不同。
- §7-10 領域最近公開：Jabil 10-K FY2026（期末 2026-08-31，申報 2026-10-23）。下一檢查點＝Jabil 1Q FY27 10-Q（期末 2026-11-30，約 2026-12 下旬）。

## 1. 落差一句

Jabil FY2026 10-K Note（Revenue）：「If the Company does not obtain control of these components before they are transferred to the customer, the Company accounts for revenue and cost of revenue associated with such components on a net basis」，且「$ 3.4 billion and $ 1.1 billion … of components included in prepaid expenses and other current assets … expected to be accounted for on a net basis once transferred」（3Q FY26 10-Q：2.8B）；MD&A 將預付增加歸因於 Intelligent Infrastructure 分部之「customer-controlled consignment components」。故 **報告營收 ≈ 總吞吐 − 淨額零組件**，且淨額零組件**佔用營運資本卻不產生營收**。落差＝市場若以報告營收成長、毛利率（9.2%）、營收倍數或「營收／投入資本」橫比 EMS 同業（Celestica、Flex 等，其 10-K 檢得 0 筆 "net basis"），則 AI 機櫃代工之實際吞吐、毛利率可比性與資本報酬可能被系統性誤讀；方向未定（淨額化使營收成長低估而毛利率高估；營運資本佔用使 ROIC 高估或低估取決於分母口徑）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（營收計量）：`Rev_reported = Throughput − C_net`；`GM% = GP / Rev_reported`；`ΔPrepaid_net` 入 OCF 而不入 Rev。非守恆、非誘因 |
| 量綱 | `C_net`［$］＝淨額零組件轉交金額；比值 `C_net / Rev`、`Prepaid_net / Rev`、`GM%_gross-up = GP/(Rev+C_net)` 皆無量綱 |
| 可見端（實讀） | Jabil 10-K FY26：淨營收 35,954（+20.6%）、Intelligent Infrastructure +45%（雲端與資料中心既有客戶 +33 pp）、毛利率 9.2%（8.9%）、預付及其他流動資產 4,559（2,010）、現金流量表預付 −2,538、AP 等 +7,984、最大客戶 20%；淨額零組件餘額 3.4B（1.1B）；3Q FY26 10-Q 2.8B |
| 指名不可見端 | 當期**轉交**之淨額零組件金額（流量，非餘額）；淨額化之客戶與產品別；若改總額認列之營收；同業是否同型處理（Celestica 10-K FY25 僅「consignment model … for particular components」、未見 net basis 字樣） |
| 主張 | 報告營收與毛利率對「客戶自控關鍵零組件（GPU／加速器等）比重」有機械性依存；比重上升時報告營收成長低於吞吐成長、毛利率上升而非定價改善 |
| 外部參照物（測一查證） | EMS 業之寄售／淨額處理前例（如 PC／手機代工客戶自購料）；僅作會計路徑先例，非量級 |
| 表達工具型態（只指名，不選券） | 美股上市 EMS／伺服器代工普通股與上市選擇權。不選券 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| Jabil 10-K FY2026（Revenue 附註、MD&A、現金流量表） | https://www.sec.gov/Archives/edgar/data/898293/000162828026067038/jbl-20260831.htm |
| Jabil 10-Q 3Q FY2026（淨額零組件 2.8B） | https://www.sec.gov/Archives/edgar/data/898293/000162828026046138/jbl-20260531.htm |
| Celestica 10-K FY2025、10-Q 2Q26（對照：consignment 一句、無 net basis） | https://www.sec.gov/Archives/edgar/data/1030894/000103089426000011/cls-20251231.htm ；https://www.sec.gov/Archives/edgar/data/1030894/000103089426000044/cls-20260630.htm |
| Flex 10-K FY2026（對照：0 筆） | https://www.sec.gov/Archives/edgar/data/866374/000086637426000012/flex-20260331.htm |
| Jabil FY26 業績稿／法說、具名賣方模型 | 測一取得（初搜未檢得淨額口徑討論，例 https://beancount.io/blog/2026/10/03/jabil-fy2026-earnings-analysis 待讀） |

不宣稱淨額效應已入或未入共識、不宣稱方向。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 管理層已於法說量化淨額化對營收／毛利率之影響，賣方據此建模 | 測一查 Jabil FY26 4Q 法說逐字稿 | 落差已揭露 |
| R2 | 市場以 core EPS／FCF 定價，營收口徑無關 | Jabil 非 GAAP 主指標為 core operating income／core EPS（10-K 調節表） | 落差不影響定價 |
| R3 | 淨額零組件為過路帳、短期回轉，餘額變動只是時序 | MD&A「timing of shipments」 | 機制弱化為 L4-A#2 型 |
| R4 | 同業實際同型處理（僅用語不同），橫比無偏 | 測一查 CLS／FLEX 附註 | 落差不存在 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) Jabil 申報或法說已量化淨額化對營收／毛利率之影響，或 ≥ 1 位具名賣方以總吞吐或淨額調整口徑建模（R1）。
- (2) 主要估值與指引口徑（core EPS、FCF）與營收口徑無關，且公開層無以營收倍數或營收成長定價 Jabil 之具名證據（R2）。
- (3) 淨額零組件之轉交流量無法自公開層推得（只有餘額），且無代理量可界定 `C_net / Rev` 量級。
- (4) `[D]` 量級：測一自定門檻（如 `C_net / Rev` 或毛利率還原差），低於門檻即否決。
- (5) Celestica／Flex 等同業附註顯示同型淨額處理（R4），或本卡只能以 L4-A#2（CCC）／L13-A#2（預付入 OCF）重述。
- (6) 12 個月內無檢驗事件（淨額比重變動之揭露、口徑變更、客戶自購料政策公告）。

複查觸發器（若日後殺）：Jabil 首次揭露淨額零組件轉交金額或總額口徑營收；同業首次揭露淨額處理；主要客戶公告改為直接採購或改回代工採購關鍵零組件。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：淨營收、毛利率、預付及其他流動資產、OCF 營運資本變動、core operating income 調節表。
2. 可交易工具：美股上市 EMS／伺服器代工普通股與上市選擇權（不選）。
3. 半衰期：季（10-Q 餘額逐季揭露；淨額比重隨客戶專案切換）。

## 7. 本輪寫入

本卡；QUEUE 新列（ANALYST 測一）；ARCH_matrix L4［A］格標「#4 已生成」；FUNNEL §3 未測格計數；`export/LEADS_算力收支.md` 追加 2 列（Jabil 10-K FY26）。不改 L4-A#1–#3、L4-P#1–#4、L4-I#1–#3、L13-A#2、C-I3′、N-01、N-02。
