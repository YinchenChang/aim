# L3-I#4 生成卡｜半導體製造測試：誘因（第二供應源＝買方之議價選擇權：設計商以最低成本維持對 Intel／Samsung 代工之「評估」，用以約束 TSMC 定價，而非承諾晶圓量）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260926_L3-I_generate_GK.md；archive/work/20261009_L3-I#2_generate_CL.md；archive/work/20261017_L3-I#3_generate_CL.md；work/20261017_L3-I#3_test1_CL.md；archive/work/20261024_L3-A#4_generate_CL.md；archive/drive/USED_20260928_L6-I_generate_GK.md | EMITS: work/20261024_L3-I#4_generate_CL.md -->
**日期：** 2026-10-24　**角色：** SCOUT@CL（排程 SCOUT-GEN）　**格：** L3-I　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。各格最後測試日最舊＝2026-10-17 一批（L3-I#3、L4-P#3／A#3／I#3、L5-P#3／A#3）；依表序取 **L3-I**（非已殺、非刻意排除）。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py foundry "second source" TSMC "Intel 14A" Samsung pricing`，命中 24 筆，皆為模型 API 價目與 ChatGPT 方案（SRC_PRC_003–034、SRC_DEM_055），與本卡無關，**未採用**。內部數字（§12）未取用。
- 比對之舊檔與死因型態，本卡須異型：
  - L3-I#1（`archive/drive/USED_20260926_L3-I_generate_GK.md`）：產能**預付款**＝合約性排序權與下修損失歸屬。本卡物件恰為**無約束力之評估**（MPW、PDK、封裝先行），主張其價值在於不承諾；有預付／保量即落入 #1 型 → 否決 (4)。
  - L3-I#2（`archive/work/20261009_L3-I#2_generate_CL.md`）：政府認股權證＝分拆選擇權之或有稀釋。本卡不涉股東層權利。
  - L3-I#3（`archive/work/20261017_L3-I#3_generate_CL.md`；測一 `work/20261017_L3-I#3_test1_CL.md`）：ATE「指定者≠付款者」委託—代理。本卡為**買方對賣方之外部選項（outside option）議價**，選擇者與付款者同一。
  - L3-A#4（`archive/work/20261024_L3-A#4_generate_CL.md`）：Intel Arizona SCIP 之 NCI 歸屬（會計恆等）。同發行人、不同機制；本卡不用 NCI。
  - L6-I（`archive/drive/USED_20260928_L6-I_generate_GK.md`）：算力租賃長約之逆選擇。不同層、不同方向（本卡之買方有替代，故不簽約）。
  - ARCH_dead 19 條：無「第二供應源選擇權」型；C-I3′（UL 型）、N-01／N-02（不可分列）為否決 (5) 之警示。不併。
- §7-10 領域最近公開：TSMC 3Q26 法說（2026-10-15）與 6-K；Intel 2Q26 10-Q（期末 2026-06-27）。**Intel 3Q26 財報 2026-10-29 盤後**（intc.com 2026-10-06 公告），尚未發布；列為測一首要檢查點。Samsung 3Q26 確定業績（約 2026-10-30）。

## 1. 落差一句

Intel 2Q26 10-Q：「the scale and pace of our manufacturing expansion projects will ultimately be dictated by the amount of committed demand for Intel 14A that we are able to obtain from … design wins with potential significant external customers」；同季代工外部營收 US$293M（「primarily due to Altera's transition to an external customer」），「substantially all of our Intel Foundry business supports internal manufacturing」。同時，二手報導以「評估」「MPW 試產」「封裝訂單」描述 NVIDIA、Google、Apple 對 Intel 之接觸（TrendForce 2026-06-09：NVIDIA「early testing of Intel 18A through multi-project wafer (MPW) runs」；Google 之 TPU 單以 EMIB 封裝為主、未述晶圓），而 TSMC 同期向客戶提價 5–10%（7 nm 以下；EDAILY 2026-06-28 引 Culpium）並於 3Q26 法說稱「we try to get our value to be recognized」「We have no intention to leave any food on the table for others」。**落差＝評估之誘因與承諾之誘因不同**：對設計商，維持一個可信但未承諾之第二供應源，其價值主要在於壓低對主供應商之議價（選擇權價值），其成本（MPW、PDK 移植、封裝小量）遠小於晶圓量承諾；故「評估／接觸」訊號對 Intel（或 Samsung）晶圓量之資訊含量，可能低於市場將其讀為「設計勝出」之程度，而對 TSMC 定價之約束可能高於其財報顯示。**方向未定**：TSMC 產能吃緊時，選擇權被迫履約（溢出量真實流向第二源）；產能寬鬆時，選擇權只用於議價而不履約。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因：買方外部選項（outside option）＋實質選擇權；評估成本低、承諾成本高，買方偏好「保持可信但不承諾」 |
| 選擇者 | 設計商（NVIDIA、Apple、Google、AMD、Qualcomm、Broadcom 客戶）：評估深度、是否承諾晶圓量；TSMC：提價幅度、是否讓步；Intel／Samsung：是否以低價或封裝先行換取承諾、擴產節奏是否等待承諾 |
| 可見端 | Intel 10-Q：擴產規模取決於「committed demand」；14A「demand commitments from potential significant external customers」為風險因子；外部營收 US$293M（2Q26）主要為 Altera；14A 初始設計承諾預期 2026 末至 2027 初（XenoSpectrum 2026-07-24 轉述）。TSMC：3Q26 法說「we do not allow our customer to sublet or auction off the capacity」、美國產地定價不同、海外廠毛利稀釋近 2%→未來 3–4%、4Q26 毛利率指引 65–67%。二手：Tesla 對 Samsung US$16.5B 合約（2025-07，具約束力之反例）；Google TPU 部分轉 Intel（EDAILY 2026-06-28） |
| 指名不可見端 | 個別客戶與 TSMC 之報價是否因第二源評估而讓步；Intel 外部承諾之條款（保量、預付、價格）；評估→承諾之轉換率 |
| 主張 | 「評估」與「承諾」為不同誘因下之行為；公開層以前者推論後者，可能同時高估第二源之晶圓量、低估 TSMC 定價受到之約束 |
| 表達工具型態（只指名，不選券） | 美股上市之代工／IDM 普通股與上市選擇權（含 TSMC ADR）。Samsung 非本池可交易範圍。不選券 |

對照式（生成用，非正式載入）：買方評估之價值 `V_eval ≈ ΔP_TSMC × Q_TSMC + max(0, 缺口 Q_short) × 溢價`；承諾之成本 `C_commit = Q_commit × (P_2nd − P_TSMC + 風險)`。`V_eval > C_eval` 而 `C_commit > 0` 時，均衡為「評估而不承諾」，除非 `Q_short > 0`（產能不足）。本輪不估參數、不寫 H1。

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

| 載體 | 入口 |
|---|---|
| Intel 2Q26 10-Q（committed demand 句；代工外部營收；風險因子） | https://www.sec.gov/Archives/edgar/data/50863/000005086326000157/intc-20260627.htm |
| Intel 3Q26 財報（2026-10-29 盤後；測一實讀 10-Q 與電話會之承諾／評估用語） | https://www.intel.com/content/www/us/en/newsroom/news/corporate/intel-reports-third-quarter-2026-financial-results.html |
| TSMC 3Q26 法說逐字稿（二手轉錄；測一須回 TSMC 官方逐字稿） | https://www.earningswhispers.com/transcript/TSM/Q32026 |
| TSMC 3Q26 6-K／業績稿 | https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm ；https://pr.tsmc.com/system/files/newspdf/attachment/70d8a93214795fa88f83fb47e0e45e7b0435e52b/3Q26%20%28E%29_with%20gudiance_final_wmn.pdf |
| TSMC 提價與客戶分散（二手，引 Culpium） | https://en.edaily.co.kr/news/eda202606265566 |
| NVIDIA 18A MPW、Google TPU／EMIB（二手，未證實） | https://www.trendforce.com/news/2026/06/09/news-intel-foundry-gains-momentum-as-google-reportedly-orders-3m-tpus-nvidia-evaluates-18A-for-multi-die-gpu-design/ |
| Intel 14A 時程與承諾預期（二手） | https://xenospectrum.com/en/intel-14a-2028-volume-commitment/ |
| Tesla–Samsung 具約束力合約（反例） | https://www.nbcnews.com/business/business-news/elon-musk-confirms-tesla-signed-16point5-billion-chip-contract-samsung-rcna221512 |
| 具名「第二源＝議價」論述（Motley Fool，Timothy Green，2022-10-04；舊，測一須找 ≥ 2026 具名來源） | https://www.nasdaq.com/articles/the-bull-case-for-intel:-tsmcs-crazy-pricing-power |

不宣稱任一客戶將或不將承諾 Intel、不宣稱 TSMC 已讓步、不宣稱市場如何定價。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 已揭露：Intel 自己即區分「評估」與「committed demand」，並將擴產綁在承諾上；資訊已公開 | Intel 2Q26 10-Q | 落差已被揭露 |
| R2 | 產能不足使選擇權必然履約：AI 晶片供給短缺下，第二源評估即真實溢出量（Google TPU、Tesla–Samsung 為具約束力之量） | EDAILY 2026-06-28；NBC 2025-07 | 「評估不承諾」均衡不成立 |
| R3 | TSMC 定價未受約束：提價 5–10% 照行、毛利率 65–67% 指引、管理層稱無人可替代 | TSMC 3Q26 法說 | 選擇權對主供應商無可測效果 |
| R4 | 第二源之議價角色早被具名論述（2022 起），屬共識 | Motley Fool／Nasdaq 2022-10-04 | 無錯價 |

## 5. 否決觸發（寫給 ANALYST 測一）

- (1) Intel 3Q26（或此前）10-Q／8-K／電話會揭露 ≥ 1 家重大外部客戶之 18A-P／14A **晶圓量**承諾附保量、預付或 take-or-pay 條款（評估＝承諾；R2）；或 TSMC 3Q26 前後客戶溢出量已以具約束力合約可見（Tesla 型 ≥ 2 例）。
- (2) TSMC 官方逐字稿／20-F／6-K 與 ≥ 1 具名來源顯示提價照計畫落實、無客戶別讓步，且無任何具名一手將客戶之 Intel／Samsung 評估連結至 TSMC 報價（R3；選擇權效果不可測）。
- (3) Intel 已逐期分列「評估中」與「已承諾」客戶數或量，且 ≥ 1 位具名賣方以承諾量（非評估數）建模 Intel 代工外部營收（R1、R4）。
- (4) 本卡只能以 L3-I#1 之預付排序權、L3-I#2 之認股權證、L3-I#3 之指定者／付款者、L3-A#4 之 NCI 歸屬，或 L6-I 之長約逆選擇重述（重疊判讀）。
- (5) 公開層不可分列：TSMC 價格效果無法自晶圓組合、匯率、海外廠稀釋分離（C-I3′／N-01 型），且 Intel 外部晶圓營收於 12 個月內不分列（N-02 型）。測一自定量級門檻並寫明。
- (6) 評估→承諾之決策週期（設計定案至量產）< 12 個月或公開層不可見，使效果在重定價窗內不可辨。

複查觸發器（若日後殺）：Intel 首次揭露外部 14A／18A-P 承諾之量或條款；TSMC 首次承認客戶別價格讓步或份額流失；具名賣方以評估→承諾轉換率建模。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Intel Foundry 外部營收（分部附註）、RPO／客戶預付（若有）；TSMC 晶圓 ASP 敘述、毛利率、海外廠稀釋。
2. 可交易工具：美股上市 INTC、TSM（ADR）普通股與上市選擇權；Samsung 不在可交易範圍。
3. 半衰期：14A 設計承諾窗（2026 末至 2027 初）、TSMC 年度報價週期（每年第四季議定次年價）。

## 7. 本輪寫入

本卡；QUEUE 新列（ANALYST 測一）；ARCH_matrix L3-I 格標「已生成 #4」；FUNNEL §3 未測格計數。不改 L3-I#1–#3、L3-A#1–#4、L3-P#1–#4、L4-I#2、L6-I、C-I3′、N-01、N-02。
