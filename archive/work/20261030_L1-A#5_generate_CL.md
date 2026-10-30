# L1-A#5 生成卡｜能源與電力：會計恆等（核能 PTC 之分段收入恆等——商業核電營業收入 ≡ 總收款 GR ＋ PTC(GR) − 州方案退還額）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260926_L1-A_generate_GK.md；archive/drive/USED_20260926_L1-A_test1_GK.md；archive/work/20261008_L1-A#2_generate_CL.md；archive/work/20261016_L1-A#3_generate_CL.md；archive/work/20261024_L1-A#4_generate_CL.md；work/20261024_L1-A#4_test1_CL.md | EMITS: work/20261030_L1-A#5_generate_CL.md -->
**日期：** 2026-10-30　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1→2／6）　**格：** L1-A　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。非「已殺／刻意排除」格中最後測一最舊＝2026-10-24（L1-A#4、L1-I#4、L3-P#4、L3-A#4、L3-I#4、L4-P#4）→ 依表序取 **L1-A**（L1-P＝刻意排除 T-11 不取）；既有生成 4 份 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `45U`／`production tax credit`／`nuclear`／`PTC`，命中 0 筆。內部數字（§12）：未取用。
- 比對（本卡須異型）：
  - **L1-A#1**（GK）：PPA 鎖定價 − 現貨＝存量；死於鎖定價與現貨無法同主體分離（CEG 不揭露 `$/MWh`；簡報僅「premium to PTC floor」說明區間）。本卡不估 PPA 單價，談**政府信用額度之分段函數**如何把 GR 變動轉為收入變動。
  - **L1-A#2**：Bloom 產品／服務認列時差。主體與恆等不同。
  - **L1-A#3**：AFUDC 權益（受管電業自有資本在建報酬資本化）。本卡為商業（merchant）核電，非費率基。
  - **L1-A#4**：受管電業大負載客戶預付款攤銷。本卡無客戶資金，項目為聯邦稅額抵減（可轉讓）以**營業收入**認列。
  - ARCH_dead：C-A3（折舊年限）、C-I3′／N-02（利益未分列）——本卡項目**已分列**（CEG MD&A「Nuclear PTC revenue」表、Note 6）。T-11 不碰。
- §7-10 領域最近公開：CEG 10-Q 2Q26（2026-08-06，acc `0001868275-26-000104`）；CEG 10-K FY25（acc `0001868275-26-000032`）；IRS 45U 頁「Page Last Reviewed or Updated: 23-Sep-2026」（引 Notice 2025-37、Notice 2026-41）。下一檢查點＝CEG 3Q26 10-Q（約 2026-11 初）；Notice 2026-41（IRB 2026-29）之 2026 調整係數原文。

## 1. 落差一句

商業核電之營業收入 ≡ GR ＋ PTC(GR) − 州方案退還（「refund that compensation up to the amount of the nuclear PTC received」），其中 PTC(GR) 對每 MWh 之 GR 為分段遞減（基礎額 0.3¢×5，於 GR 超過 reduction amount 後依比例遞減至零；reduction amount 2024＝2.5¢、2025＝2.6¢／kWh，逐年依 GDP 平減指數調整，**至 2032 年底止**）→ 收入對電價之斜率**分段**：高於淘汰點為 1、帶內遠小於 1、低於帶為平。CEG：Nuclear PTC revenue FY24 2,080M → FY25 320M（−84.6%），10-K 將 FY25 歸屬普通股淨利 −1,430M 首列「Lower Nuclear PTC revenues」；2Q26 Note 6「did not record a material nuclear PTC benefit as the estimate of full year gross receipts exceeded the phase-out … for most units」（1H26 25M）。種子主張：市場以「電價／容量價／資料中心 PPA 溢價 × 核能 MWh」線性外推商業核電收益，未把 PTC 分段造成之**(i) 2025 年毛收入增量被 PTC 減少吸收、(ii) 2026 起增量 1:1 流入、(iii) 下行時 PTC 重新啟動之聯邦下限、(iv) 2032-12-31 下限到期之斷崖**自 GR 中分離。**方向未定**：可為上行斜率已恢復（2026 收益加速屬機械性），亦可為下行受保護（逆向情境被高估）而 2033 起保護消失。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：Rev_nuc,u ＝ GR_u ＋ PTC_u(GR_u/MWh) × MWh_u − Refund_u(州方案)；PTC_u 依**年度** GR 預估逐季認列（10-K：「quarterly results rely on forecasted gross receipts for the fiscal year … could materially impact our quarterly recognition of nuclear PTC revenues」）；已享州支援之機組另依退還條款扣抵 |
| 已讀事實 | CEG 10-K FY25（sec.py 全文）：「The nuclear PTC provides increasing levels of support as unit revenues decline below levels established in the IRA and is further adjusted for inflation annually」；「Absence of prescriptive guidance requires the application of judgment in determining annual gross receipts」；表：Nuclear PTC revenue 320 vs 2,080；State-sponsored programs net revenue (125) vs (50)。CEG 10-Q 2Q26：Nuclear PTC revenue 3M 15 vs 45、6M 25 vs 45；State-sponsored programs net revenue 6M (275) vs 190；資產負債表 nuclear PTC 約 150M（vs 120M）列 Other deferred debits。VST 10-Q 2Q26：「Transferable PTC revenues」3M 3（僅「qualifying solar assets」），未見核能 PTC 收入列。TLN 10-Q 2Q26：grep `PTC|tax credit` 0 筆（§7-2：檢索失敗非不存在）。IRS：2024 line-7 rate $0.025、2025 $0.026（Notice 2025-37；調整係數 1.0242）。 |
| 未證之連結 | 各機組（或 CEG 合計）PTC 帳面淘汰點之 `$/MWh` 與實現 GR 之距離；GR 是否含容量收入、避險結算、PPA 收款（Treasury 指引未定，CEG 自承判斷）；州方案（IL CMC、NY ZEC、NJ ZEC）退還與 PTC 之相互抵消淨額；VST（Comanche Peak、Beaver Valley 等）、PEG、TLN 是否於其他科目（所得稅、其他收入）認列；賣方模型是否以分段函數建模 2026–2032 下行；2033 起之期後處理 |
| 量綱 | ΔRev_nuc ÷ ΔGR（無量綱，分段斜率）；PTC ÷ 核能段收入（%）；下行情境下 PTC 重啟額 ÷ EBITDA（%）；淘汰點與遠期 GR 之距離（`$/MWh`） |
| 半衰期 | 至 2032-12-31（法定終止）；季度可觀測 |

## 3. B 端可觀測載體（只指名）

1. CEG 10-K FY25 https://www.sec.gov/Archives/edgar/data/1868275/000186827526000032/ceg-20251231.htm （MD&A Nuclear PTC revenue 表、淨利變動歸因、關鍵會計估計「Government Assistance」、Note 6）
2. CEG 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1868275/000186827526000104/ceg-20260630.htm （同表季度；Note 6「did not record a material nuclear PTC benefit」）
3. VST 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1692819/000169281926000019/vistra-20260630.htm （Other revenues 之 Transferable PTC revenues；核能 PTC 之認列科目待查）
4. TLN 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm （grep 0 筆；待以 10-K、所得稅附註再查）
5. IRS 45U 調整頁 https://www.irs.gov/forms-pubs/section-45u-zero-emission-nuclear-power-production-credit-reduction-amount-rate-has-been-updated-by-the-inflation-adjustment ；Holland & Knight 2025-07-23 https://www.hklaw.com/en/insights/publications/2025/07/irs-releases-2025-inflation-adjustments-for-sections-45u-45v-and-45z ；IRB 2026-29 https://www.irs.gov/pub/irs-irbs/irb26-29.pdf （Notice 2026-41，未讀）
6. 未讀：CEG 業績電話會「PTC floor」原句（GK 測一曾見簡報「premium to PTC floor」說明區間）；PEG 10-Q；Treasury 45U gross receipts 指引；具名賣方對 PTC 下限之量化。

缺段（§7-2）：具名第三方以分段函數量化 2026–2032 下行之原文本輪未見；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 管理層自身即以「premium to PTC floor」框定合約價，賣方沿用；下限已定價 | CEG 簡報（GK 測一引述）、載體 1 | 已定價 |
| R2 | GR 已遠高於淘汰點，PTC 下限深度價外，下行保護對 H5 無實質影響 | 載體 2 Note 6 | 量級 |
| R3 | 州方案退還條款使 PTC 對享州支援機組淨效果近零（雙向互抵） | 載體 1、2 | 量級 |
| R4 | 2025 收入下滑已全揭露並分列，YoY 比較之吸收效果無資訊落差 | 載體 1 | 已定價 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 除 CEG 外無任何上市主體可分列核能 PTC 認列額，且 CEG 之 Nuclear PTC revenue 不足 4 季可對齊序列；或
(2) `[D]` 量級：以 2026–2027 遠期（具名公開來源）計，下行 20% 電價情境下 PTC 重啟額 ÷ 核能段（或公司）EBITDA < 5%；或淘汰點低於遠期 GR 逾 30%；或
(3) 州方案退還條款確認對 ≥ 70% 核能 MWh 全額互抵（R3 成立）；或
(4) 具名賣方或評等機構已以分段函數（PTC 下限）量化下行或 2033 斷崖（已定價）；或
(5) 與 L1-A#1（PPA 鎖定價 − 現貨）為同一金額之重述——即 PTC 效果無法與合約價分離；或
(6) 12 個月內無可觀測驅動：無季報變動、無 Treasury 指引、無 2027 調整係數公告。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：營業收入內 Nuclear PTC revenue、State-sponsored programs net revenue、Other deferred debits 之 PTC 資產。2. 可交易工具：商業核電（不選）。3. 半衰期：至 2032-12-31；季度。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L1［A］格加「#5 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0130。`export/LEADS_算力收支.md`：本輪事實（核能 PTC 收入）非 AI 算力投入／收入／硬體／雲端合約／資料中心之直接事實，不寫。不改 L1-A#1–#4、L1-I#1–#4、L1-P（T-11）、C-A3、N-02 結論。
