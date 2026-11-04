# L13-I#5 生成卡｜資本與融資結構：誘因（半流動永續載具之贖回選擇權：持有 AI 資料中心之非交易型 REIT／信託，其份額按「顧問自定折現率與資本化率」之估值 NAV 定期贖回、受季度比例閘門限制——持有人在 NAV 高於上市可比隱含值時有先贖誘因，顧問因費用按 NAV 計而有維持假設之誘因；此通道對資料中心之新增資本供給是條件性可逆，而非「永久資本」）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/work/20261013_L13-I#2_generate_CL.md；archive/work/20261020_L13-I#3_generate_CL.md；archive/work/20261028_L13-I#4_generate_CL.md；work/20261028_L13-I#4_test1_CL.md；archive/work/20261104_L13-P#5_generate_CL.md；archive/work/20261103_L13-A#5_generate_CL.md | EMITS: work/20261104_L13-I#5_generate_CL.md -->
**日期：** 2026-11-04　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 2→3／6）　**格：** L13-I　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L13-P#5 本日測一，Q-0160 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-28（L13-I#4、L14-P#4、L14-A#4、L14-I#4）；依表序取 **L13-I**。既有生成數 4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `non-traded`、`BREIT`、`QTS`、`Blue Owl`、`redemption`＝0 筆；未用。載體全由本輪 WebSearch／WebFetch／`sec.py` 實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L13-I#1**（私有資訊 → 公開信評資訊含量）：本卡不涉評等。
  - **L13-I#2**（擔保人兼股東違約分支；死因＝終止費遮蔽）：不涉擔保人。
  - **L13-I#3**（發行人依機構債務含量選工具；死因＝事前公告組合）：選擇者非發行人。
  - **L13-I#4**（壽險 RBC 資本計提之買方選擇；死因＝否決 (2)，持有人以共同基金／資管帳為主，壽險占比不可得）：#4 之約束為**監理資本**、資產為**債券**；本卡之約束為**載具合約之贖回權與閘門**、資產為**以估值 NAV 計價之資料中心權益**，選擇者為散戶／財富管理通路持有人與顧問。
  - **L13-P#5**（信用市場出清守恆）：本卡非出清恆等式，為個體選擇；**L13-A#5**（子公司可贖回優先）：不涉列報。
  - **C-A3**（折舊樞紐）、**C-A4**（表達窗）：不以殘值、年限為樞紐；不重開。**L11-P**／**L8-P**／**L9-P**：不恢復。不寫 T-15。
- §7-10 領域最近公開：ODIT 8-K（2026-09-30 NAV，申報於 2026-10）；ODIT 10-Q 2Q26；OCIC 2026-04 股東信（8-K Ex.99.1）；AltsWire 2026-05-12（BREIT 1Q26）。下一檢查點＝各載具 4Q26 季度回購結果（2027-01）、ODIT 10-Q 3Q26、BREIT／ODIT 月 NAV。

## 1. 落差一句

市場把非交易型永續載具（BREIT 之 QTS、Blue Owl Digital Infrastructure Trust 等）對 AI 資料中心之出資讀成「永久資本」，從而把該通道之資本供給與其顧問之費用收入視為穩定；種子主張：此類載具之份額按**顧問自定**之折現率與資本化率估值之 NAV 贖回，受季度比例閘門（ODIT 3%／季、OCIC 5%／季）限制——當上市可比（資料中心 REIT）隱含資本化率高於顧問假設，持有人有「按偏高 NAV 先贖」之誘因、比例閘門使其成為搶先賽局；顧問之管理費（NAV 之 1.25%）與績效分成按 NAV 計，則有不調假設之誘因。可拒絕之主張＝(i) 估值 NAV 與上市隱含值之落差在 2026 可量測且非零；(ii) 贖回請求對此落差有反應，且一旦超過閘門即同時壓低新認購，使該通道對資料中心之**新增**出資於 12 個月內可逆。本卡不主張任何資產價值方向、不主張估值錯誤。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因（I）**：持有人 j 於季 t 申請贖回若 \(NAV_t^{adv} − V_t^{mkt} > c_{early} + \text{期望按比例執行損失}\)；閘門 g（3–5%）下，請求 R > g 時按比例執行，先申請者無劣勢、遲申請者承擔後續 NAV 下修 → 策略互補（搶先）。顧問 a：費 \(f\cdot NAV\)，假設 \((r, k)\) 由 a 定、估值顧問僅「review」 |
| 選擇者 | 載具持有人（財富管理通路散戶、fund-of-funds）；顧問（決定 \(r,k\) 與是否行使「may choose to repurchase only some, or even none」裁量） |
| 驅動（因果層，§7-5） | 載具合約條款（閘門、早贖扣減、董事會暫停權）；顧問估值假設；上市資料中心資產之定價 |
| 量綱 | 資本化率／折現率［%］；NAV 敏感度［% / 25bp］；贖回請求／流通股［%］；閘門［% NAV／季］ |
| 可見端 | 載具月 NAV 與組成（8-K）；10-Q 估值假設與敏感度表；季度回購請求與執行比（8-K、股東信）；上市資料中心 REIT 隱含資本化率（賣方或自算） |
| 指名不可見端 | 各載具單一資產估值；持有人結構與通路集中度；顧問與估值顧問之往來 |
| 外部參照物（測一查證） | 2022-11 至 2024-02 BREIT 閘門期（請求峰 5.3 bn／月、按比例執行 15 個月）——公開 REIT 先跌、估值 NAV 後調之具名前例；2026Q1 非交易型 BDC 請求潮（OCIC 21.9%、OTIC 41%） |
| 表達工具型態（只指名，不選券） | 美股上市另類資管普通股（費用按 NAV 計）；上市資料中心 REIT；不選券 |
| 重疊 | L13-I#4（買方約束，但約束與資產皆異）、L13-P#5（邊際買方，但本卡為載具內選擇）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. ODIT 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/0002069692/000206969226000057/osnl-20260630.htm ：「Data Centers 7.7% 6.1%」（折現率／資本化率）、「These assumptions are determined by the Adviser and reviewed by our independent valuation advisor」；資本化率 −25bp → +2.4%、+25bp → (2.2)%；回購「limited to no more than 3 % of the Company’s aggregate NAV per calendar quarter」、未滿兩年「repurchased at 98 %」；「may choose to repurchase only some, or even none」；管理費「1.25 % of NAV」；2Q26 損益表列 Performance participation allocation。
2. ODIT 8-K（2026-09-30 NAV）https://www.sec.gov/Archives/edgar/data/0002069692/000206969226000066/osnl-20260930.htm ：Investments in real estate 4,568,550 千美元；Net Asset Value 2,234,045 千美元；Class I NAV/股 10.5958。
3. OCIC 2026-04 股東信（8-K Ex.99.1）https://www.sec.gov/Archives/edgar/data/1812554/000119312526139036/d127449dex991.htm ：「quarterly liquidity of up to 5% … at net asset value」；「repurchase request of 21.9% … will fulfill its tender offer of 5%, on a pro rata basis」；「1% of shareholders representing the majority of tenders」。（信用載具，非資料中心；作閘門動態之對照）
4. Bisnow（2026-04-03）https://www.bisnow.com/news/national/capital-markets/blue-owl-caps-redemptions-after-investors-sought-54b-across-two-funds-133973 ：OCIC 22%、OTIC 41% 請求；「only fulfill 5% of requests」；Stanger：2026Q1 業界請求 14 bn 僅兌現約半。
5. AltsWire（2026-05-12）https://altswire.com/breit-raises-1-2-billion-in-q1-2026-highest-in-three-years-as-repurchases-fall-41/ ：BREIT 1Q26 募 1.2 bn、回購請求年減 41%；QTS 開發投入逾 3.7 bn、管線 25 bn 全數預租 15–20 年；「Requests peaked at $5.3 billion in January 2023 … prorate payouts for 15 consecutive months」；NAV 約 54.9 bn。
6. CoStar（2026-03-09）https://www.costar.com/article/2145056359/as-private-credit-cools-reawakening-could-be-near-for-real-estate-funds ：BCRED 請求約 7.9% NAV、上限自 5% 提至 7% 並注資；HPS 9.3% 超 5% 上限；Blackstone 稱 BREIT 組合含 QTS。

缺段（§7-2）：上市資料中心 REIT 同期隱含資本化率（一手或具名）；BREIT 之 QTS 估值假設與占 NAV 比（BREIT 10-Q，測一以 sec.py 實讀）；ODIT 季度回購請求率；資料中心型載具於 AI 資料中心第三方出資中之占比。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 資料中心型載具之贖回壓力低：BREIT 1Q26 請求年減 41%、淨流入轉正；2026Q1 請求潮集中於軟體信用 BDC，主因 AI 對軟體借款人之顛覆，與資料中心估值無關 | #4、#5 | 方向相反／非本通道 |
| R2 | 預租 15–20 年三淨租約之現金流確定，估值對資本化率之敏感度有限（±25bp ≈ ±2.3%），NAV 與上市值之落差不足以覆蓋 2% 早贖扣減與按比例損失 | #1、#5 | 量級不足 |
| R3 | 載具規模相對 AI 資料中心資本支出極小（ODIT 不動產約 4.6 bn），即使閘門觸發也不改邊際出資者 | #2 | 非邊際 |
| R4 | 閘門與 BREIT 2022–24 前例已廣為人知，市場已對另類資管費用流折價 | #4 | 已定價 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後 **< 2 個**資料中心占比可確認之半流動載具能同時取得：顧問估值資本化率（或折現率）、季度回購請求率、閘門條款——落差與反應不可量測。
(2) 上市資料中心 REIT 隱含資本化率（具名或由申報自算 `[D]`）與載具顧問資本化率之差，於 2025Q4–2026Q3 任一季皆 < 50bp，或載具 NAV 對上市可比之滯後 < 1 季——無「偏高 NAV 贖回」選擇權。
(3) 資料中心型載具 2026 各季回購請求均 < 閘門且淨流入為正，且無一手證據顯示請求率對 (2) 之落差有反應（R1 成立）。
(4) 半流動載具（含 BREIT／QTS）於可識別之 AI 資料中心第三方權益出資中占比無任何一手或具名機構數，或可得之數 < 5%（R3 成立：非邊際）。
(5) 具名賣方、評等機構或監理機構已量化「估值 NAV 對上市隱含值落差 → 贖回 → 資料中心出資／顧問費用」之鏈並公開——已定價（R4）。只點名「非交易型基金贖回壓力」不算。
(6) 重定價窗（≥ 12 個月）內無可觀測檢驗事件（各載具 4Q26／1Q27 回購結果、ODIT／BREIT 10-K 估值假設更新、董事會修改或暫停回購計畫），或其已全部於窗前公告。
(7) 可運作對照只能寫成買方監理資本（L13-I#4 型）、市場出清（L13-P#5 型）、折舊／殘值樞紐（C-A3 型）或資產估值本身，而非持有人贖回與顧問估值之誘因。

複查觸發器（若日後殺）：任一資料中心型半流動載具請求超過閘門或董事會修改回購計畫；顧問上調資料中心資本化率 ≥ 25bp；具名機構量化資料中心 NAV 對上市隱含值之落差。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：另類資管之費用相關收益（按 NAV 計之管理費、績效分成）中來自永續載具與資料中心之部分；載具之回購與認購。
2. 可交易工具：上市另類資管普通股、上市資料中心 REIT。不選券。
3. 半衰期：月 NAV；季度回購窗；年度估值假設更新。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0161；`query/ARCH_matrix.md` L13［I］標「#5 已生成」；`export/LEADS_算力收支.md` 追加 2 筆（ODIT 不動產投資〔一手〕、BREIT／QTS 管線〔二手〕）。不寫入：FUNNEL（留給測一）、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L13-I#1–#4、L13-P#1–#5、L13-A#1–#5、C-A3／C-A4 結論；不寫 T-15。
