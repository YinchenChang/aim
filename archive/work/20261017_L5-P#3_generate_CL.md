# L5-P#3 生成卡｜儲存與 IO：守恆（HDD 機群 IO 供給守恆：每碟頻寬近乎固定 → 每 TB 之 IO 隨容量下降，工作負載之 MB/s／TB 給出可用容量上界）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260927_L5-P_generate_GK.md；archive/work/20261011_L5-P#2_generate_CL.md；work/20261011_L5-P#2_test1_CL.md；work/20261011_L5-A#2_test1_CL.md；archive/work/20261011_L5-I#2_generate_CL.md | EMITS: work/20261017_L5-P#3_generate_CL.md -->
**日期：** 2026-10-17　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L5-P　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L4-I#3 本日已測一，Q-0061 done）。最後測試日最舊＝2026-10-11（L5-P／A／I、L6-P／A／I、L13-A）；依表序取 **L5-P**；非已殺、非刻意排除。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `HDD "hard disk" actuator "IOPS per TB"`：**命中 0 筆**。本卡載體全部來自下列原文 fetch。
- 比對之舊檔與死因型態，本卡須異型：
  - **L5-P#1**（`archive/drive/USED_20260927_L5-P_generate_GK.md`；T 已寫｜不進 L）：HBM 頻寬守恆 `decode 吞吐 ≤ BW／V_byte`。本卡守恆量為 **HDD 機群之機械 IO 供給**（磁頭時間），介質＝硬碟，非 HBM、非推論 decode。
  - **L5-P#2**（`work/20261011_L5-P#2_test1_CL.md`；(1)(4) 觸發）：快閃寫入耐久預算。本卡非快閃、非耐久；死因 (1)「生產輸入不可觀測」已預寫為否決 (1)，須由測一再驗。
  - **L5-A#2**（`work/20261011_L5-A#2_test1_CL.md`；(2)(4) 觸發）：HDD 營收恆等（台數 × 每台 TB × 每 TB 價）與供給封頂。本卡**沿用其已讀事實**（台數持平、EB 靠面密度）**作為輸入**，但守恆量為頻寬／TB，主張落在需求側之可用容量上界，不主張價格或供給封頂。
  - **L5-I#2**：NAND 供給者資本配置誘因。不同型。
  - **C-P1**（ARCH_dead #11）：訓練 checkpoint 讀取占復原比。本卡不涉訓練復原。
- §7-10 領域最近公開：Athlur 等 OSDI '26（CMU／Google／Microsoft Azure 合著）；Everpure 2Q FY27 8-K（第二家前五大超大規模業者設計勝出 2026-08-10）；Everpure 資源頁 last-modified 2026-08-31；Seagate FY26 10-K 2026-08-04；WDC FY26 10-K 2026-08-14。下一檢查點＝Seagate FQ1'27 財報 2026-10-27（公司公告）及 WDC FQ1'27。

## 1. 落差一句

每碟機械 IO 供給 `b`（磁頭時間；頻寬近乎與容量無關，36 TB Mozaic 外圈最大持續傳輸 270 MB/s）守恆，機群 IO 供給 `B ≡ N × b`；容量成長靠面密度、台數持平 → IO 密度 `ρ ≡ B／EB ≈ b／每碟 TB` 隨容量單調下降。工作負載若有每 TB 之 IO 需求 `d`（MB/s／TB，含背景維護 IO），則每碟可用容量上界 `C_max ≡ u·b／d`。OSDI '26 以某超大規模業者資料推得：維護 IO 用 50% 磁頭時間時「imperative IO can only use 36 TB disks」。種子主張：公開敘事以 EB 與容量路線（40 TB 近期、100 TB 至 2030）計量 HDD 需求，而約束實為 IO 守恆——超過 `C_max` 之容量只能由多致動器（每 IO 單位 TB 下降）、軟體減 IO、或快閃替代吸收。本卡不定方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（磁頭時間／頻寬為每碟固定預算）；非會計恆等、非誘因、非快閃耐久 |
| 選擇者 | 無（物理）；`b` 由轉速與單致動器決定；`d` 由工作負載（重建、清洗、壓縮、遷移、冷熱比）決定 |
| 可見端 | OSDI '26：「the IO supply per TB of HDD storage is trending precipitously downward」；「maintenance tasks will use an additional 0.9% of a disk's time for each additional TB of HDD capacity」；「Beyond this wall, storage systems will be unable to use higher-capacity HDDs」；DINGO 使可用碟容量約 1.7×（64／58 TB）。Everpure：「the IOPS/TB goes down as the device size goes up」。Seagate 10-K：「complement our areal density-driven technology roadmap with … multi-actuation」。WDC 10-K：路線含「triple stage actuators」 |
| 指名不可見端 | 生產機群之 `d` 分布（論文以匿名 Hyperscaler A／B）；各容量點出貨組合；多致動器出貨占比；申報層台數（Seagate 10-K「actuator」「IOPS」「terabyte」0 筆，只揭 nearline EB 695／非 nearline 94；WDC 10-K「IOPS」0 筆，只揭 EB 與每 EB ASP 年增率） |
| 主張 | 同一 `d` 下，每碟容量超過 `C_max` 之部分不能貢獻有效 EB；EB 成長率與每 TB 定價力因而受 `b` 之守恆約束，可被出貨組合與業者揭露拒絕 |
| 表達工具型態（只指名，不選券） | 美股可交易之 HDD 供給者（Seagate、Western Digital）與全快閃替代者（Everpure）。不選券 |
| 重疊 | L5-A#2（同供給者、不同守恆量）、L5-P#2（同層儲存）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Athlur et al., "Scaling the IO wall with Declarative IO", USENIX OSDI '26。https://www.usenix.org/system/files/osdi26-athlur.pdf
2. Seagate FY26 10-K（acc 0001137789-26-000159）。https://www.sec.gov/Archives/edgar/data/1137789/000113778926000159/stx-20260703.htm
3. WDC FY26 10-K（acc 0001628280-26-057139）。https://www.sec.gov/Archives/edgar/data/106040/000162828026057139/wdc-20260703.htm
4. Everpure 2Q FY27 8-K ex99.1。https://www.sec.gov/Archives/edgar/data/0001474432/000147443226000084/everpure-ex991q2fy2027xpre.htm ；資源頁 https://www.everpuredata.com/resources/all-flash-data-center-is-imminent.html
5. SNIA 2026-02-17（Kutcipal／Le Moal）：CDL「directly improves IOPS per terabyte」；「24%+ capacity CAGR」。https://www.snia.org/blog/2026/hdd-innovation-hyperscale
6. 36 TB 規格（二手彙編，測一須取 Seagate 原廠 datasheet）。https://datacenterdisk.com/seagate-exos-36tb
7. 測一須另取：Seagate FQ1'27（2026-10-27）／WDC FQ1'27 法說之容量點組合、多致動器、客戶認證口徑；任一具名賣方是否以 IOPS／TB 約束 HDD 需求或容量點採用。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | IO 密度下降為業界公開常識，全快閃商以此行銷 | Everpure 資源頁（#4）；SNIA（#5） | 已定價 |
| R2 | 軟體可推遠 IO 牆（DINGO 約 1.7×；CDL 提升 IOPS／TB） | OSDI '26（#1）；SNIA（#5） | 約束可鬆 |
| R3 | 快閃快取吸收前景 IO，HDD 只承載冷資料，`d` 很低 | OSDI '26 Sec. 2.1（但亦稱「remaining disk IO is increasingly hard to cache」） | 約束不綁 |
| R4 | 多致動器以同碟容量換 IO，不減 EB 需求 | Seagate／WDC 10-K 路線（#2、#3） | 只改組合不改總量 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 生產機群之每 TB IO 需求 `d` 或其區間，除 OSDI '26 匿名資料外無任何一手原文；守恆之輸入不可觀測。
(2) HDD 供給者或具名賣方已明文以 IOPS／TB（IO 密度）約束估算 HDD 需求、容量點採用或快閃替代（R1 成立且非僅競爭者行銷）。
(3) 業者原文顯示 ≥ 36 TB 單致動器容量點已為 nearline EB 主體且客戶滿載採用，使 `C_max` 於現行容量不綁。
(4) 申報層（10-K／10-Q／8-K 附件）無容量點組合、台數或多致動器占比，且無替代科目可拒絕（§7-4 財報科目題不可答）。
(5) 可運作對照只能寫成 HDD 營收恆等／供給封頂（L5-A#2）、NAND 供給（L5-I#2）或快閃耐久（L5-P#2）。
(6) 軟體或介面緩解（宣告式 IO、CDL、多致動器）已由業者原文宣稱部署，使 IO 牆後移超過 12 個月重定價窗內之容量路線。

複查觸發器（若日後殺）：任一 HDD 供給者於申報層或法說首次揭露容量點組合或多致動器出貨占比；或任一超大規模業者公開每 TB 背景 IO 需求。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：nearline EB、每 EB ASP 年增率、容量點組合（法說）。
2. 可交易工具：Seagate、Western Digital、Everpure 美股（不選券）。
3. 半衰期：40 TB 級量產與認證週期；IO 牆顯現或長於 12 個月窗，測一須查。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列 Q-0063；`query/ARCH_matrix.md` L5［P］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1／§2、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L5-P#1 之 T／L、L5-P#2、L5-A#2、L5-I#2、C-P1 結論。
