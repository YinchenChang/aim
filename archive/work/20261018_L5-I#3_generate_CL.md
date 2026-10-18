# L5-I#3 生成卡｜儲存與 IO：誘因（記憶體長約之誘因相容：買方於現貨跌破約價時之違約／重議誘因 vs 押金＋擔保＋價格帶之約束 → 「去週期化」是否成立）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；query/INDEX.json；archive/drive/USED_20260926_L5-I_generate_GK.md；archive/work/20261011_L5-I#2_generate_CL.md；archive/work/20261017_L5-A#3_generate_CL.md | EMITS: work/20261018_L5-I#3_generate_CL.md -->
**日期：** 2026-10-18　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L5-I　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L5-A#3 2026-10-17 測一，Q-0064 done）。最後測試日最舊＝2026-10-11（L5-I、L6-P／A／I、L13-A）；依表序取 **L5-I**；非已殺、非刻意排除。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py lead time HDD SSD allocation`，回 7 筆，**相關 0 筆**（PUE、METR、Anthropic 營收列）；載體全由 `sec.py` 與 WebSearch／WebFetch 原文取得。
- 比對之舊檔與死因型態，本卡須異型：
  - **L5-I#1**（`archive/drive/USED_20260926_L5-I_generate_GK.md`）：雲端出站費＝結構性取用權；失敗在量綱（價目列名非連續量）。本卡選擇者＝記憶體**買方**（超大規模／OEM），物件＝長約之履約或違約選擇；所需量為申報層連續量（RPO、合約負債、退款負債、擔保），非價目表。
  - **L5-I#2**（`archive/work/20261011_L5-I#2_generate_CL.md`；(1)(2) 觸發）：**供給者**資本配置誘因（晶圓不擴），死於新潔淨室公告與 TrendForce 共識。本卡不主張供給側擴產與否，只主張**需求側合約之誘因相容**；選擇者、選擇變數、可拒絕事件皆不同。
  - **L5-A#3**（Everpure 權利金混合恆等）、**L5-P#3**（HDD IO 守恆）、**L5-A#2**（HDD 量價恆等）：不同型。
  - **C-P1**（ARCH_dead，L5，checkpoint 需求歸因）、**L13-I**（供應方對客戶股權＋應收帳齡）：本卡不做需求歸因；與 L13-I 共享「客戶信用」維度，但本卡物件為長約之價差違約誘因，非股權循環。重疊列為否決 (6)。
- §7-10 領域最近公開：Sandisk FY26 10-K（期末 2026-07-03，申報 2026-08-17）；Micron FY26 10-K（期末 2026-09-03，申報 2026-10）；JPMorgan（Jay Kwon）LTA 報告之報導 2026-05-18；Citron 空方 2026-02-24。下一檢查點＝Sandisk FQ1'27 10-Q（約 2026-11 上旬）、Micron FQ1'27 10-Q（約 2026-12 下旬）。

## 1. 落差一句

記憶體歷史上之長約於下行期被放棄（JPMorgan 報導原文：2017 DRAM 短缺期之遠期採購協議「easily abandoned in subsequent downturns」；本輪 LTA 之「contractual integrity … remains untested」）。本輪長約新增押金、預付與第三方擔保。**誘因相容條件：** 買方於現貨跌破約價時之違約收益 ≈ (約價下限 − 現貨) × 剩餘承諾量；違約成本 ≈ 可沒收押金＋擔保＋（供應關係之重複賽局價值）。若 `G ÷ RPO`（可沒收保障 ÷ 剩餘履約義務）遠小於下行期之預期價差率，約束不足，「去週期化」只在上行期成立；若價格帶下限低（Micron：「minimum and maximum bands」）則違約誘因本身小，但去週期化之收益亦小。種子主張：市場對兩種情形之一定價，而申報層已可給出 `G ÷ RPO` 與價格機制型態，兩者合起來決定哪一種成立。本卡不定方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因（買方履約／違約選擇；參與約束 vs 違約收益）；非會計恆等、非守恆 |
| 選擇者 | 長約買方（超大規模、OEM；申報未具名）；次選擇者＝供給者是否於下行期主動重議以保關係 |
| 可見端 | **Sandisk FY26 10-K：** NBM「commit us to deliver, and our customers to purchase, a stated volume of products, mostly over multi-year periods」；「pricing mechanisms consisting of fixed and variable components and are supported by financial guarantees」；RPO「$59.8 billion」，約 19% 於 12 個月內認列，「entirely related to NBMs」；合約負債 1,242（前期 25）；退款負債（押金，期末退還）1,500（前期 126）；第三方擔保「not recognized … until a triggering event」；自述「reduce certain elements of industry cyclicality」。**Micron FY26 10-K：** RPO「approximately $134 billion」，其中 13 billion 為合約負債（主為客戶押金，「Nearly all of the deposits are scheduled to be repaid between 2029 and 2031」）；約四分之一 12 個月內認列；「Pricing for our contracts is either fixed or periodically negotiated, with the majority … subject to minimum and maximum bands」；RPO「based on … committed volumes and minimum pricing and are not expected to be indicative of future revenue」；部分合約要求信用狀 |
| 指名不可見端 | 價格帶上下限水準；違約時押金是否可沒收（Sandisk 押金屬「refundable … following their satisfaction of all performance conditions」）；第三方擔保金額；買方名稱與集中度；重議條款 |
| 對照式（生成用） | `[D]` 保障比 `g ≡ G ÷ RPO`：Sandisk ≈ (1,500＋1,242)／59,800 ≈ 4.6%（含預付，預付非違約罰金，屬上界）；Micron ≈ 13／134 ≈ 9.7%（未含信用狀）。誘因相容需 `g ≳ E[(P_floor − P_spot)⁺ ÷ P_contract]`。本輪不估右式、不寫 H1 |
| 主張 | 下行期之長約履約率由 `g` 與價格帶下限決定；申報層已有 `g` 之兩家區間與價格機制型態；可被重議／違約事件或價格帶揭露拒絕或支持 |
| 表達工具型態（只指名，不選券） | 美股可交易記憶體供給者（Sandisk、Micron）。不選券 |
| 重疊 | L5-I#2（同層同主體、供給側）；L13-I（客戶信用）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Sandisk FY26 10-K（風險因子 NBM 段、MD&A Long-Term Agreements、Note 4 Revenue RPO／合約負債／退款負債）。https://www.sec.gov/Archives/edgar/data/2023554/000162828026057406/sndk-20260703.htm
2. Micron FY26 10-K（Revenue 附註 RPO、價格帶、押金償還期、信用狀）。https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm
3. JPMorgan（Jay Kwon）LTA 報告之報導（2026-05-18）：「contractual integrity … remains untested」；2017 協議「easily abandoned」。https://www.itiger.com/news/1100518440
4. Citron 空方（2026-02-24）：「supply mirage that can vanish in a single earnings call」。https://fintool.com/news/citron-shorts-sandisk-nand-cycle-peak
5. 測一須另取：Sandisk FQ1–FQ3 FY26 10-Q 與 FQ1'27 10-Q 之 RPO／押金季序列；Micron 2026 年內 10-Q 同欄；Samsung／SK hynix／Kioxia LTA 條款原文（非美股，取 IR）；2017–2019 DRAM 長約放棄或重議之一手原文（公司法說或申報）；跨產業前例（太陽能多晶矽 take-or-pay 長約於 2011–2013 下行期之違約與訴訟，一手判決或申報）；具名賣方是否已以 `g` 或價格帶下限建模下行情境。**不宣稱已錯價。**

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 長約下行期照樣被放棄，週期未變 | JPMorgan 報導（#3）引 2017 前例 | 支持本卡方向之一側；若已為共識則落差消失 |
| R2 | 供給週期（Samsung 份額戰）主導，合約無關 | Citron（#4） | 機制被相鄰驅動 |
| R3 | 公司自述 NBM 降低週期性，市場已以 LTA 重估 | Sandisk 10-K（#1）；JPMorgan 上調目標價（#3） | 共識（反向） |
| R4 | 價格帶上下限使違約收益本來就小，`g` 無關 | Micron 10-K（#2）「minimum and maximum bands」 | 誘因量級不足 |
| R5 | RPO 為「not … indicative of future revenue」，分母不可用 | Micron 10-K（#2） | 量綱 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 申報層或公司原文已揭露價格帶下限水準、違約沒收條款與擔保金額，使誘因相容可直接判定（落差不在申報缺口）；或反之，`G` 與 RPO 任一於 ≥ 2 家不可並列（量綱失敗，同 L5-I#1 型）。
(2) 公開層（具名賣方或研究機構原文，非報導轉述）已以保障比或價格帶下限量化下行期長約履約，使落差為共識（R1 或 R3 之原文須實讀）。
(3) 價格帶下限經原文確認接近現貨可能低點，使違約收益 `(P_floor − P_spot)⁺` 近 0（R4 成立）。
(4) 可運作對照只能寫成供給者擴產（L5-I#2）、HDD 恆等（L5-A#2）、需求歸因（C-P1）或客戶股權循環（L13-I）。
(5) 2017–2019 DRAM 或多晶矽前例之一手原文顯示押金／擔保結構已存在且仍被放棄，或結構不可比，使前例不能界定 `g` 門檻。
(6) 長約買方集中且具名揭露後，違約主體之信用與供應關係價值使重複賽局成本主導，`g` 不是決定變數。

複查觸發器（若日後殺）：任一美股可交易記憶體供給者於 10-K／10-Q／8-K 揭露長約重議、量或價調整、押金沒收或擔保動用；或揭露價格帶下限水準；或具名研究機構以保障比建模下行情境。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：RPO、合約負債、退款負債（押金）、信用狀／擔保、12 個月認列比、營收。
2. 可交易工具：Sandisk、Micron 美股；Samsung／SK hynix／Kioxia 非美股主上市。
3. 半衰期：RPO 12 個月認列 19%（Sandisk）／約 25%（Micron），押金償還 2029–2031（Micron）；檢驗事件為首次現貨跌破約價，時點未知，`[V]` 不寫。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L5［I］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L5-I#1／#2、L5-A#1–#3、L5-P#1–#3、C-P1、L13-I 結論。
