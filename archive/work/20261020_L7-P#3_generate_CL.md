# L7-P#3 生成卡｜模型層：守恆（推論算力量守恆：已上線推論容量 × 每單位容量 token 產出 × 實現單價 ≥ 用量營收——營收路徑之容量上界）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/drive/USED_20260930_L7-P_generate_GK.md；archive/drive/USED_20260930_L7-P_test1_GK.md；archive/work/20261013_L7-P#2_generate_CL.md；work/20261013_L7-P#2_test1_CL.md；work/20261013_L7-A#2_test1_CL.md；work/20261018_L6-P#3_test1_CL.md | EMITS: work/20261020_L7-P#3_generate_CL.md -->
**日期：** 2026-10-20　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1→2／6）　**格：** L7-P　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L13-A#3 本日已測一，Q-0069 done）。非已殺／刻意排除格中，最後測試日最舊＝2026-10-13（L7-P／A／I、L10-P／A／I、L11-A／I、L13-P、L13-I、L14-P、L14-A）；依表序取 **L7-P**。既有生成數 2 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py Anthropic gigawatt "revenue per" tokens capacity`，命中 16 筆；與本格相關 4 筆：SRC_DEM_034／035／036（Reuters 讀機密 S-1 之 2025 營收拆分）、SRC_DEM_013（Epoch 每日 token 推估）。本輪回原文實讀 Reuters（經 Global Banking & Finance 轉載）；只作載體指名，不作證據。
- 比對之舊檔與死因型態，本卡須異型：
  - **L7-P#1**（測一通過｜不進 T）：FLOP/token × J/FLOP＝**每 token 能量下界**（單位成本底板）。本卡守恆量為**總量**：容量（GW）→ token 產出 → 營收之**上界**，不論每 token 焦耳。
  - **L7-P#2**（部分通過）：訓練資料存量。本卡不論資料。
  - **L7-A#2**（部分通過）：持股方之公允價值計量。本卡不論持股會計。
  - **L6-P#3**（測一不通過，(2) 份額已建模）：雲供給者**自身**容量於外租／自用／研發之分割。本卡在**模型實驗室**端：專屬容量 → 推論 token → 用量營收；重疊（同為容量分割問題）照記，死因「賣方已以份額建模」須於測一重查是否同樣適用。
  - **C-A5**（死 #13，API 單價不可分離／L7 未上市）、**C-P3**（死 #16）：本卡不需分列 API 單價，只需營收 ÷ 容量之區間；上市與否列為否決 (5)。C-A5 之複查觸發器（前沿 API 商 IPO）屬 SCOUT-WATCH，本卡不代判。
  - **L1-*／L2-*／L4-*（電力、實體、硬體守恆）**：本卡之容量取實驗室自報之「dedicated computing capacity」GW，不推電網或晶片供給。
  - **T-15**：無關，不寫。
- §7-10 領域最近公開：Reuters（Echo Wang、Krystal Hu，2026-09-29）讀機密 S-1；Renaissance Capital（2026-10-05）稱公開申報「could land as soon as October 23」；decodethefuture（2026-10-13 驗）「no public S-1 from Anthropic, PBC appears on SEC EDGAR」。下一檢查點＝公開 S-1（EDGAR）。

## 1. 落差一句

恆等（量守恆）：`R_use,t ≤ K_inf,t × u_t × τ_t × p̄_t`，其中 `K_inf`＝已上線且分配至推論之專屬容量［GW］、`u`＝利用率［無量綱］、`τ`＝每 GW 每年 token 產出［token／GW·yr］、`p̄`＝實現加權單價［$／token］；且 `K_inf = K_total − K_train − K_research`。已見數點：Reuters 讀機密 S-1——2025 營收「nearly $4.6 billion」、用量計費約 $3.8B、「total long-term commitments exceeded $417 billion, covering 3.5 gigawatts of dedicated computing capacity」；營收年化「above $65 billion at the end of July」（reported）；Anthropic 2026-04-06 稱新 TPU 容量「expected to come online starting in 2027」；媒體轉述投資人簡報約 1.4 GW（2025 末）→ 約 5 GW（2026 末）→ 約 10 GW（2027）（未證實）。種子主張：若公開市場（IPO 後）之營收外推所需之 `R／K_inf` 超出可由 `τ`、`p̄` 之物理與價格區間支撐之值，或反之容量上線遠快於可售 token，則營收路徑被容量守恆**事前約束**。本卡不定方向與量級，只立可拒絕之恆等。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 守恆（容量 → token → 營收之量守恆；容量分割 K_total＝K_inf＋K_train＋K_research） |
| 量綱 | GW；token／(GW·yr)；$／token；營收 $／yr；R／K［$／GW·yr］ |
| 可見端 | 公開 S-1（若上市）：營收拆分（用量／訂閱／雲市集）、承諾額與 GW、cost of revenue；Amazon／Alphabet 10-Q 之 Anthropic 相關揭露；官方定價頁（`p` 列表價）；Epoch 等每日 token 推估 |
| 指名不可見端 | `K_train／K_inf` 分割；`u`；實現單價 `p̄`（批次 50% 折、快取倍數、雲市集分潤使列表價≠實現價） |
| 主張 | 由公開 GW 上線時程與 `R／K` 歷史區間可事前界定營收上界之時間路徑；若市場口徑以 ARR 外推而不經容量即可錯置。可由「公司或主流賣方已以 GW 建模營收」拒絕 |
| 外部參照物（測一查證） | 雲供給者已揭露之「容量受限營收」前例（Microsoft Azure「capacity constrained」語、Oracle RPO 與上線時程）——僅作路徑先例，非量級 |
| 表達工具型態（只指名，不選券） | 模型實驗室普通股（上市後）；持股方（Amazon、Alphabet）普通股為間接。不選券 |
| 重疊 | L6-P#3（容量分割，供給端）、L7-P#1（能量底板）、C-A5（L7 上市性）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Reuters 讀機密 S-1（轉載）https://www.globalbankingandfinance.com/exclusive-anthropic-ipo-prospectus-lays-bare-deep-dependence/ （本輪實讀：$54.6B 不可取消承諾、>$417B／3.5 GW、2025 營收拆分）
2. Renaissance Capital（2026-10-05）https://www.renaissancecapital.com/IPO-Center/News/122058/9-numbers-to-look-for-in-anthropic%E2%80%99s-ipo-filing （本輪實讀：$65B ARR、>$500B 承諾、公開申報最早 10-23）
3. decodethefuture（2026-10-13）https://decodethefuture.org/en/anthropic-s1-ipo-filing-explained/ （本輪實讀：EDGAR 無公開 S-1；毛利未公開）
4. FourWeekMBA（Gennaro Cuofano，2026-09-18）https://fourweekmba.com/ai-anthropic-gigawatt-threshold-compute-unit-of-account/ （本輪實讀：官方「starting in 2027」；1.4／5／10 GW 為未證實轉述；作者自明不算比值）
5. 測一須另取：EDGAR 公開 S-1（`sec.py filings` 以實驗室名或 CIK）；Amazon、Alphabet 最近 10-Q 之 Anthropic 段（`sec.py doc --grep Anthropic`）；Anthropic 官方 2026-04-06 公告原文；具名賣方或研究機構是否已以 GW／token 建模實驗室營收（例：SemiAnalysis、Epoch）；Microsoft／Oracle「capacity constrained」原文作前例。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 實驗室本身以 GW 為公開計量單位（「3.5 gigawatts of dedicated computing capacity」），市場可直接以 GW 推營收 | Reuters 2026-09-29（#1）；FourWeekMBA（#4）之「Model Company Starts Reporting in Power」 | 已定價 |
| R2 | `K_train／K_inf` 不揭露、`p̄` 隨批次／快取／分潤異質，`R／K` 區間過寬致上界不具約束 | 定價頁 Message Batches「50% of the standard API prices」；Reuters 雲市集 47% | 不可觀測／不約束 |
| R3 | 容量可經現貨雲租用彈性擴張（非專屬），量不守恆 | 測一須找具名來源 | 機制洩漏 |
| R4 | 公開上市未發生或延後，L7 無可交易主體 | decodethefuture（#3） | 表達失敗（同 C-A5 死因） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 公開 S-1、公司原文或具名賣方／研究機構已以 GW（或 token 產能）建模營收上界，或公司明言營收受容量約束並量化——已定價（R1）。
(2) 申報層不分列 `K_inf` 與 `K_train`（或等效之推論 cost of revenue），且 `R／K` 可得區間上下界比 > 3×——不可觀測或上界不約束（R2）。
(3) 具名來源顯示實驗室可隨時以非專屬現貨雲容量補足推論（K 非約束）——守恆洩漏（R3）。
(4) 可運作對照只能寫成 L6-P#3 容量分割、L7-P#1 能量底板、L1／L2／L4 供給守恆或 C-A5。
(5) 至測一日 EDGAR 無公開 S-1，且無已上市主體能分離實驗室營收與容量（持股方 10-Q 不分列）——表達不可行（R4）。

複查觸發器（若日後殺）：EDGAR 出現模型實驗室公開 S-1 或 10-Q；任一實驗室首次分列推論／訓練算力成本或 GW；持股方 10-Q 首次分列被投資實驗室之容量承諾。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：S-1／10-Q 之營收拆分、cost of revenue、承諾附註（GW／$）、雲市集分潤。
2. 可交易工具：模型實驗室普通股（上市後）；持股方普通股（間接）。不選券。
3. 半衰期：公開 S-1（最早 2026-10-23 報導）→ 首份 10-Q；容量上線「starting in 2027」。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L7［P］標「#3 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L7-P#1／#2、L7-A／#2、L7-I／#2、L6-P#3、C-A5、C-P3、C-I1 結論；不寫 T-15。
