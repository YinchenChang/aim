# L5-A#5 生成卡｜儲存與 IO：會計恆等（股權報酬之授予日成本 vs 既得日成本：GAAP SBC ≡ Σ 股數 × P_grant ÷ 服務期，而淨額交割之現金代扣稅 ≡ 既得股數 × P_vest × 代扣率，列於融資活動、不入任何公司口徑 FCF；股價十倍級重定價後兩者之比 κ 為可觀測之盈餘／現金流品質缺口）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/work/20261025_L5-A#4_generate_CL.md；work/20261025_L5-A#4_test1_CL.md；archive/work/20261101_L5-P#5_generate_CL.md | EMITS: work/20261101_L5-A#5_generate_CL.md -->
**日期：** 2026-11-01　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L5-A　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L5-P#5 本日測一，Q-0143 done）。最後測試日最舊＝2026-10-25（L5-A#4、L12-A#4、L12-I#4）；依表序取 **L5-A**；非已殺、非刻意排除。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `yen`、`Sandisk`，**命中 0 筆**。內部數字（§12）未取用。載體全由 `sec.py` 實讀。
- 本輪先試兩個方向後放棄（記錄以免重生）：① Sandisk 日圓成本／避險遞延——10-Q 1Q FY27 Note 7 只有 non-designated hedges（無現金流量避險遞延），且銷貨成本僅占營收 15%，FX 槓桿量級不足；② 供給者存貨消化（出貨 ≡ 生產 − ΔI）——Sandisk 本季存貨 2,698→3,016 上升，無消化。
- 比對之舊檔與死因型態，本卡須異型：
  - **L5-A#1**（KV IO 成本，雲端儲存美元行不在申報層）、**L5-A#2**（HDD 營收量價分解，共識）、**L5-A#3**（Everpure 毛利混合）、**L5-A#4**（Sandisk 合資表外 capex，R 已在 OCF）：皆非股權報酬；本卡不涉營收分解、毛利混合、FV 撥款或租賃保證。
  - **L5-I#3**（長約保障比）、**L13-A#2**（客戶預付入 OCF）：本卡不以 NBM 預付為落差（Sandisk Adjusted FCF 已扣 NBM 預付，見 §3-2）。
  - **L7-I#2**（Meta SBC 集中化之誘因）：彼為人才誘因；本卡為會計計量之授予日／既得日缺口，主體為儲存。
  - **L13-P#3**（Alphabet／Meta 母公司現金守恆、ATM 用於代扣稅）：彼為現金守恆與回購零下界；本卡為恆等式之計量缺口且主體股價十倍級重定價，不主張現金不足。
  - **L12-A#3**（OBBBA 現金稅 vs 帳面稅）：本卡之稅只涉代扣與 windfall，不涉遞延稅時序。
  - **C-A1／C-A3／C-A4／C-P1**（ARCH_dead）：不同型。
- §7-10 領域最近公開：Sandisk 10-Q 1Q FY27（2026-10-30）與 8-K 99.1（2026-10-29；宣布 8 比 1 股票分割）；WDC 10-Q 1Q FY27（2026-10-23）；Seagate 10-Q 1Q FY27（2026-10-29）；Micron 10-K FY26（2026-10-09）。下一檢查點＝Micron 1Q FY27 10-Q（約 2026-12／2027-01）、Sandisk 2Q FY27（約 2027-01 下旬；公司公告日前不作 `[V]`）。

## 1. 落差一句

恆等：`SBC_GAAP,t ≡ Σ_g n_g · FV_g(P_grant) / τ_g`（授予日公允價值，攤銷後不重估）；淨額交割之代扣現金 `W_t ≡ n_vest,t · P_vest,t · θ`（θ＝代扣率），列融資活動；經濟成本（既得日價值）`E_t ≡ n_vest,t · P_vest,t`。定義 `κ_t ≡ W_t / SBC_GAAP,t`。可見值（1Q FY27，皆 `[V]` 申報原文）：

| 主體 | GAAP SBC | 既得代扣稅（融資） | κ `[D]` | 其他 |
|---|---|---|---|---|
| Sandisk | $91M | $755M（前年同期 $15M） | ≈ 8.3 | 未攤銷 $1,350M／2.48 年；稀釋股 154 vs 基本 146；Adjusted FCF $5,696M 未扣代扣稅（代扣 ≈ 13.3%） |
| WDC | $79M | $317M（前年 $55M） | ≈ 4.0 | windfall 稅益 $98M |
| Seagate | $63M | $17M（前年 $50M） | ≈ 0.3（季節性） | 離散稅益 ≈ $83M 主要為 SBC 超額稅益 |
| Micron FY26 | $1,333M（CF） | $1,127M（權益表 withholdings） | ≈ 0.85 | — |

**種子主張：** 儲存主體股價於 2025–26 十倍級重定價後，GAAP SBC 仍以低價授予日計（Sandisk 分拆時期授予），而經濟成本與代扣現金以既得日高價計；公司 FCF／Adjusted FCF 口徑與非 GAAP EPS 皆不含此項；未來 2–3 年舊授予攤畢、新授予以高價計後，GAAP SBC 將機械性上移（未攤銷餘額可算）。市場若以公司口徑 FCF 殖利率外推，則漏計 `W` 或等價之稀釋。反之，若 `W`／市值 < 0.5%／年或賣方已普遍以「FCF − 代扣稅」口徑，則無落差。本卡不定方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（ASC 718 授予日計量 vs 既得日現金／稀釋；現金流量表分類）；非守恆、非誘因 |
| 計量者 | 公司（GAAP 與非 GAAP 口徑之定義者）；賣方模型是否扣 `W` |
| 可見端 | 10-Q 現金流量表「Taxes paid on vested stock awards」、權益表 withholding 行、SBC 附註未攤銷成本與加權服務期、稀釋股數、windfall 稅益 |
| 指名不可見端 | 各期既得股數 × 既得日價格（只部分可反解）；新授予之股數與公允價值（年度 10-K／proxy 才揭）；賣方模型是否以 `FCF − W` 或全稀釋股估值 |
| 主張 | `κ` 與 `W ÷ 公司口徑 FCF` 可逐季觀測；GAAP SBC 之上移路徑可由未攤銷餘額＋新授予推出；可被量級過小、共識已計、或回購完全抵銷稀釋所拒絕 |
| 表達工具型態（只指名，不選券） | 美股可交易之 Sandisk、Western Digital、Seagate、Micron。不選券 |
| 重疊 | L5-A#4（同 Sandisk、同 FCF 口徑議題但不同科目）、L13-P#3（代扣稅現金）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Sandisk 10-Q 1Q FY27（現金流量表、Note 12 股東權益、Note 14 所得稅）：https://www.sec.gov/Archives/edgar/data/2023554/000162828026068601/sndk-20261002.htm
2. Sandisk 8-K Ex 99.1（FCF／Adjusted FCF 定義與調節；8 比 1 分割）：https://www.sec.gov/Archives/edgar/data/2023554/000162828026068243/sndkq1-27ex991xpressrelease.htm
3. WDC 10-Q 1Q FY27：https://www.sec.gov/Archives/edgar/data/106040/000162828026066933/wdc-20261002.htm
4. Seagate 10-Q 1Q FY27：https://www.sec.gov/Archives/edgar/data/1137789/000113778926000309/stx-20261002.htm
5. Micron 10-K FY26：https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm
6. 一般性 SBC 反方論述（Mauboussin 訪談，CFA Society Toronto）：https://cfatoronto.ca/?p=5446
7. 測一須另取：Sandisk 10-K FY26 之授予股數與授予日公允價值、PSU 最大倍數（10-Q：1M 授予可至 4M 股）；proxy 之 FY27 授予；四家最近 4 季 `W` 時序；回購股數 vs 既得發行股數（淨股數變動）；具名賣方或財經媒體是否以 `FCF − W` 或 SBC 既得日成本評論儲存股；8 比 1 分割前後之授予政策。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | SBC 為真實費用、應自 FCF 扣除之論點早已公開且普及（Mauboussin 等） | #6 | 方法層已入共識（否決 (2)） |
| R2 | 代扣稅實為以既得日價買回股份，等價於回購；Sandisk 同季回購 $5,000M，淨股數由回購主導 | #1 | `W` 只是回購之一部分，股東層面無遺漏 |
| R3 | 量級：Sandisk `W` ≈ Adjusted FCF 13%，但相對市值可能 < 1%／年 | 測一須以市值核算 | 對 `H1` ≥ 5 之重定價不構成驅動（否決 (3)） |
| R4 | 季節性與一次性：分拆換股之加速既得、PSU 達標集中於一季（Seagate κ 0.3 vs Sandisk 8.3） | #1、#4 | `κ` 非穩態，不可外推 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 四家最近 4 季 `W` 加總 ÷ 同期公司口徑 FCF < 5%，或 `W` 年化 ÷ 市值 < 0.5%（門檻於此凍結）——量級不足。
(2) 具名賣方、評等機構或主流財經媒體已明文以 `FCF − W`、既得日 SBC 成本或全稀釋口徑評估任一家儲存主體（R1；已入共識）。
(3) 同期回購股數 ≥ 既得發行股數 × 3，且公司已以淨股數變動為主要揭露（R2；稀釋已被完全抵銷且可見）。
(4) `κ` 高值只來自分拆換股加速既得或一次性 PSU（R4），剔除後最近 4 季 `κ` < 2。
(5) 可運作對照只能寫成 L5-A#4（FCF 口徑之 FV 撥款）、L13-P#3（母公司現金守恆）或 L7-I#2（人才誘因）。
(6) 12 個月內無可檢驗事件（10-K 授予揭露、proxy、季報 `W`、分割後授予政策）可使本機制被拒絕。

複查觸發器（若日後殺）：任一儲存主體改變 FCF 定義納入或排除代扣稅；或單季 `W` ÷ 公司口徑 FCF > 15% 連續 2 季；或 GAAP SBC 年增 > 100%（新高價授予開始攤銷）。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：現金流量表代扣稅行、SBC 附註、稀釋股數、windfall 稅益——皆可拒絕之科目。
2. 可交易工具：Sandisk、WDC、Seagate、Micron 美股（不選券）。
3. 半衰期：舊授予攤畢約 2.5 年（Sandisk 加權服務期 2.48 年）；與 12 個月窗之相容性測一須查。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0144；`query/ARCH_matrix.md` L5［A］標「#5 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 一筆（Sandisk 1Q FY27 營收）。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L5-A#1–#4、L5-P#1–#5、L5-I#1–#4、L7-I#2、L13-P#3、C-P1 結論。
