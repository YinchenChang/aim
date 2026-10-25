# L5-P#4 生成卡｜儲存與 IO：守恆（HDD 裝機存量之 EB 存量—流量守恆：出貨 EB ≡ 淨增 EB ＋ 退役 EB；退役由 5–6 年前出貨世代決定 → 2020–22 高峰世代與 2023–24 谷底世代於 12–36 個月內依序到期）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260927_L5-P_generate_GK.md；archive/work/20261011_L5-P#2_generate_CL.md；work/20261011_L5-P#2_test1_CL.md；archive/work/20261017_L5-P#3_generate_CL.md；work/20261017_L5-P#3_test1_CL.md；archive/work/20261011_L5-A#2_generate_CL.md；archive/work/20261017_L5-A#3_generate_CL.md；archive/work/20261018_L5-I#3_generate_CL.md | EMITS: work/20261025_L5-P#4_generate_CL.md -->
**日期：** 2026-10-25　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L5-P　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L4-I#4 本日測一，Q-0103 done）。各格最後測試日最舊＝2026-10-17（L5-P#3、L5-A#3）；依表序取 **L5-P**；非已殺、非刻意排除。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `HDD exabyte replacement "useful life"`：**命中 0 筆**；`"useful life" depreciation server`：命中 15 筆，皆 MLPerf／機架價格，與本卡無關，未用。本卡載體全部來自下列原文 fetch。
- 比對之舊檔與死因型態，本卡須異型：
  - **L5-P#1**（HBM 頻寬守恆 decode ≤ BW／V_byte；T 已寫｜不進 L）：不同守恆量、不同介質。
  - **L5-P#2**（快閃寫入耐久預算；死因 (1) 生產 W 不可觀測、(4) 申報無分列）：本卡守恆量為**裝機存量 EB 之存量—流量**，輸入（出貨 EB）在申報層 `[V]`；不可觀測端（退役滯後 L）已預寫為否決 (1)(3)。
  - **L5-P#3**（HDD 每 TB IO 供給守恆；死因 (2) WDC 已以 IO／TB 框定、(1)(4)）：本卡不涉 IO、不涉容量點；主張落在**出貨 EB 之替換成分與世代時序**。
  - **L5-A#2**（營收 ≡ 台數×每台 TB×每 TB 價）：本卡不拆營收、不主張價格或供給封頂；只立「出貨 EB 中多少是替換」之守恆。
  - **L5-A#3**（全快閃商毛利混合）、**L5-I#2**／**L5-I#3**（NAND 資本配置、記憶體長約誘因）：不同型。
  - **C-P1**（ARCH_dead #11，checkpoint 讀取占復原比）：不涉。TrendForce 2025-10-14「AI storage demand accelerates HDD replacement」為**快閃取代 HDD**，非本卡之裝機退役替換，屬他型。
- §7-10 領域最近公開：WDC FQ1'27 10-Q（2026-10-23 申報；本系統線索檔已錄 Cloud EB 年增逾 20%）；Backblaze Drive Stats Q2 2026（2026-09-29）；Seagate FY26 10-K（2026-08-04）。下一檢查點＝Seagate FQ1'27（2026-10-27）。

## 1. 落差一句

裝機 HDD 容量為存量：`S_t ≡ S_{t−1} + X_t − R_t`（X＝出貨 EB，R＝退役 EB）。若退役滯後近似出貨後 L 年，則 `R_t ≈ X_{t−L}`，出貨可拆為 `X_t ≡ ΔS_t + X_{t−L}`。Seagate 申報之出貨 EB `[V]`：FY18 338／FY19 347／FY20 442／FY21 535／FY22 631／FY23 441／FY24 398／FY25 595／FY26 789（FY20–24 另列 mass capacity 317／417／541／380／355；FY25–26 改列 nearline 497／695——**口徑改變，量綱須先對齊**，§7-1）。超大規模業者伺服器耐用年限 `[V]`：Amazon 一部分由 6 年改 5 年（2025-01-01 起，歸因 AI 技術步調）、Meta 5.5 年（2025-01-01 起）、Alphabet 6 年、Microsoft 2–6 年。若 L ≈ 5：FY26 替換基數 ≈ FY21 535，FY27 ≈ FY22 631（高峰），FY28 ≈ FY23 441、FY29 ≈ FY24 398（谷底）`[D]`。**種子主張：** 公開敘事把出貨 EB 全數讀為 AI／雲端「需求」並以 mid-20s% EB 成長外推，而守恆式中有一項由 5–6 年前之世代機械決定；2022 高峰世代到期後，同一淨增 ΔS 下之出貨 EB 會因替換基數自高峰轉入谷底而放緩（或反之，若 L 長於 7 年則替換項小且平滑、無此效應）。本卡不定方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（存量—流量；EB 不生不滅，只有出貨、淨增、退役三項）；非會計恆等之營收拆分、非誘因 |
| 選擇者 | 退役時點由業者決定（折舊年限、故障率、機櫃槽位／電力換密度），但守恆式本身無選擇 |
| 可見端 | Seagate 10-K 年度出貨 EB 與口徑；WDC 10-K／10-Q EB 年增率；四家超大規模 10-K 伺服器耐用年限；Backblaze 季報（35 萬碟；Q2 2026 兩型號約 8–9 年才全數退役；部署集中 20 TB+）；Seagate 管理層 2026-05「installed base is fewer units but chock full」、mid-20s% EB 成長、不擴廠 |
| 指名不可見端 | 超大規模業者之 HDD 實際退役年齡分布（折舊年限≠實體退役）；為換密度提前退役之比例；WDC 與 Toshiba 之世代 EB 歷史（測一須取）；產業總出貨 EB 之世代序列 |
| 主張 | 出貨 EB 之替換成分由已發生之世代決定、可事前計算；若 L 落在 5–6 年，FY27→FY28 替換基數降約三成 `[D]`，在淨增不變下出貨 EB 成長率被機械壓低；可被實際退役年齡、提前換密度、或業者揭露拒絕 |
| 表達工具型態（只指名，不選券） | 美股可交易之 HDD 供給者（Seagate、Western Digital）。不選券 |
| 重疊 | L5-A#2（同供給者、營收恆等）、L5-P#3（同機群、IO 守恆）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Seagate 10-K FY26／FY24／FY22／FY20（EB 出貨表）：https://www.sec.gov/Archives/edgar/data/1137789/000113778926000159/stx-20260703.htm ；https://www.sec.gov/Archives/edgar/data/1137789/000113778924000068/stx-20240628.htm ；https://www.sec.gov/Archives/edgar/data/1137789/000113778922000055/stx-20220701.htm ；https://www.sec.gov/Archives/edgar/data/1137789/000113778920000057/stx-20200703.htm
2. WDC 10-K FY26（EB 年增、每 EB ASP）：https://www.sec.gov/Archives/edgar/data/106040/000162828026057139/wdc-20260703.htm ；FQ1'27 10-Q：https://www.sec.gov/Archives/edgar/data/106040/000162828026066933/wdc-20261002.htm
3. 伺服器耐用年限：Amazon 10-K 2025 https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm ；Meta 10-K 2025 https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm ；Alphabet 10-K 2025 https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm ；Microsoft 10-K FY26 https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
4. Backblaze Drive Stats Q2 2026（2026-09-29）：https://backblaze.com/blog/backblaze-drive-stats-for-q2-2026
5. Seagate 於 JPM TMC 2026（2026-05，二手摘要）：https://semiconalpha.substack.com/p/seagate-jpm-54th-annual-tmt-key-takeaways
6. 測一須另取：Seagate FQ1'27 法說（2026-10-27）是否提及替換／汰換／installed base；WDC 歷年 EB 出貨絕對量；任一具名賣方或 TrendForce／IDC 是否以裝機退役世代估 HDD EB 需求；超大規模業者實體退役年齡之一手（論文、OCP、業者部落格）。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 實體退役遠長於折舊：Backblaze 型號約 8–9 年才全退 | #4 | L 大 → 替換項小且平滑 |
| R2 | 裝機「滿載 100% 利用」、不擴廠，需求受供給限，出貨由產能決定而非替換 | #5 | 守恆式之替換項不驅動出貨 |
| R3 | 換密度（槽位／電力）使退役與年齡脫鉤 | 生成假說，測一須找原文 | 世代時序失效 |
| R4 | 口徑改變（mass capacity→nearline）使世代序列不可比 | #1 | 量綱題 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 超大規模業者之 HDD 實體退役年齡（或其區間）無任何一手原文；只剩折舊年限與 Backblaze 單一小型業者——守恆之 L 不可觀測。
(2) HDD 供給者或具名賣方／研究機構已明文以裝機退役世代或替換需求估算 EB 需求（R 項已入共識）。
(3) 可得證據顯示 L ≥ 7 年或退役分布寬到使 `X_{t−L}` 之世代高低差於 12–36 個月窗內不顯現（R1 成立）。
(4) 申報層除年度出貨 EB 外無任何可拒絕之科目，且口徑改變使世代序列無法對齊（R4；§7-4 財報科目題不可答）。
(5) 可運作對照只能寫成營收恆等／供給封頂（L5-A#2）或 IO 密度（L5-P#3）。
(6) 業者原文顯示出貨受產能封頂、交期／配額制（R2），使替換項之變動只改變排隊長度而不改出貨 EB。

複查觸發器（若日後殺）：任一 HDD 供給者於申報層或法說揭露替換／汰換需求占比或裝機年齡；或任一超大規模業者公開 HDD 實體退役年齡分布。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：年度／季度出貨 EB、nearline／mass capacity 口徑、每 EB ASP。
2. 可交易工具：Seagate、Western Digital 美股（不選券）。
3. 半衰期：FY22 世代到期時點（L＝5 → FY27；L＝6 → FY28）對 12 個月窗之相容性，測一須查。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0104；`query/ARCH_matrix.md` L5［P］標「#4 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 兩筆。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L5-P#1–#3、L5-A#1–#3、L5-I#1–#3、C-P1 結論。
