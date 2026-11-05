# L15-I#5 生成卡｜基礎設施軟體與資料：誘因（績效股之併購門檻設計：PSU 以 NGS ARR 計績效、只排除收購價 > 4% 市值之併購 → 門檻下之收購 ARR 與折價遷入之 AI 原生客戶 ARR 全數計入激勵指標，管理層邊際誘因指向「買入／讓價換取 ARR」，ARR 增速 ≠ 有機需求增速）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20261007_L15-I_generate_GK.md（經 L15-I#2 測一引用）；archive/work/20261014_L15-I#2_generate_CL.md；archive/work/20261022_L15-I#3_generate_CL.md；archive/work/20261029_L15-I#4_generate_CL.md；work/20261029_L15-I#4_test1_CL.md；archive/work/20261011_L6-I#2_generate_CL.md；archive/work/20261104_L14-I#5_generate_CL.md | EMITS: work/20261105_L15-I#5_generate_CL.md -->
**日期：** 2026-11-05　**角色：** SCOUT@CL（排程 SCOUT-GEN，本日配額 2→3／6）　**格：** L15-I　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額配置、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L15-A#5 已測，Q-0166 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-29（L2-P/A/I#5、L15-I#4；L15-A#4 已由 #5 更新至 11-05）；同日以佇列序取最早者 Q-0126＝**L15-I**（L2-P/A/I#5＝Q-0127–Q-0129）。既有 #1–#4 → #5。
- Tokenomics 線索（CLAUDE.md §11）：選格後查 `Chronosphere`、`Palo Alto`，0 筆；未用。內部數字（§12）未用。
- 比對（須異型）：
  - **L15-I#1**（出站費率／保留期之資料鎖定）：本卡不涉客戶轉換成本。
  - **L15-I#2**（`archive/work/20261014_L15-I#2_generate_CL.md`）：相容開源引擎封頂 ISV 託管價差。本卡不涉授權與相容品。
  - **L15-I#3**（`archive/work/20261022_L15-I#3_generate_CL.md`）：收購方收割（漲價、前置認列）。本卡方向相反——收購後**讓價**換 ARR，且選擇者為**薪酬委員會之指標設計**，非產品定價。
  - **L15-I#4**（`archive/work/20261029_L15-I#4_generate_CL.md`）：AI 原生買方之雙源門檻。本卡借用其已實讀之「LLM 客戶遷入 Chronosphere」事實作載體之一，但落差在**賣方高管激勵指標之計入規則**，不在買方行為。
  - **L6-I#2**（`archive/work/20261011_L6-I#2_generate_CL.md`）：業務員以 bookings 計酬 → RPO 與交付脫鉤（代理人、時程）。本卡為**高管 PSU 之無機成長計入門檻**（併購規模之選擇變數），不涉 bookings 或交付時程。
  - **L14-I#5**（`archive/work/20261104_L14-I#5_generate_CL.md`）：雇主以 AI 用量考核員工。不涉。
  - 已殺 C-I5（AI cohort 留存不可分）：本卡不需 cohort；C-I1／C-I2／C-I3′ 不涉。L8-P／L9-P／L11-P 不涉。
- §7-10 領域最近公開：PANW DEF 14A（2026-10-27 申報）；PANW 10-K FY26（期 2026-07-31，2026-09-10 申報）；PANW 8-K 4Q FY26 業績（2026-09-01）。下一檢查點＝PANW 1Q FY27 業績與 10-Q（約 2026-11 下旬）；2026-12 年會 Say-on-Pay 表決（2025 年僅 46% 支持）。

## 1. 落差一句

PANW FY26 PSU 之 NGS ARR 指標「excluding the contribution of merger and acquisition transactions … in which the purchase price for the acquisition exceeds 4% of our market capitalization」；目標 $7.20B、實際 $7.69B（已排除 CyberArk）→ 超標 $490M ≥ 封頂線 $400M，NGS ARR 分項達 300%。Chronosphere（對價 $3.0B，收購時 ARR > $160M、三位數成長）落於門檻下而**全數計入**；委員會明載「considered a lower threshold that would have captured our acquisition of Chronosphere, but determined that Chronosphere was not an acquisition that fundamentally altered the Company’s growth profile … did not result in a fundamentally new platform category」，而同公司 10-K 寫「The acquisition resulted in forming our next-generation observability platform」、致股東信寫「to enter Observability」。若 Chronosphere 貢獻 ≥ $160M，排除後超標 ≤ $330M、分項 ≤ 265% `[D]`（線性內插：+$200M＝200%、+$400M＝300%）。同期 PANW 以較在位者便宜 30–40% 之價格只對 AI 原生客戶銷售 Chronosphere，並認列「9 figure benefit from a large LLM customer migrating」（L15-I#4 測一已實讀）。故激勵指標在門檻下對「買入 ARR」與「讓價遷入之 AI 原生 ARR」中性甚至獎勵；市場以 NGS ARR（FY26 +63%、FY27 指引 +22–23%）讀平台化需求，而有機／無機與讓價 ARR 之分解未被揭露。可拒絕之主張＝門檻下無機 ARR 與 AI 原生讓價 ARR 占 NGS ARR 年增量非可忽略，且該分解可由申報與業績稿重算，而公司與具名賣方未作此分解。不主張任何主體價值方向。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因（I）**：選擇者（薪酬委員會）設定指標計入規則 θ（併購門檻＝4% 市值）；高管邊際報酬 ∂Payout/∂ARR 對有機與門檻下無機 ARR 相同；ARR 以「annualized allocated revenue of all active contracts」計，讓價與免費期合約按分配收入計入 |
| 量綱 | 美元 ARR；PSU 分項達成率（%）每 $1M 超標 ≈ 0.5pp（+$200M→+$400M 區間）`[D]`；門檻下無機 ARR ÷ NGS ARR 年增量（無因次） |
| 選擇者 | 薪酬委員會（門檻 θ、目標、封頂線）；高管（併購規模、AI 原生定價）；股東（Say-on-Pay） |
| 可見端 | DEF 14A 之 PSU 目標／實際／排除規則與委員會理由原文；10-K Note 8 併購對價與日期；收購公告之 ARR；業績稿 NGS ARR 與指引；電話會議之 Chronosphere／LLM 客戶句 |
| 指名不可見端 | Chronosphere 於 FY26 末之 ARR（未分列）；有機 NGS ARR；AI 原生客戶之讓價幅度與 ARR |
| 表達工具型態（只指名，不選券） | 美股平台型資安／可觀測軟體商；不選券 |
| 重疊 | L6-I#2（代理人計酬→合約指標，異軸）；L15-I#3（收購方，方向相反） |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. PANW DEF 14A 2026（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1327567/000130817926000432/panw-20261027.htm ：FY26 PSU 表「NGS ARR ($B) Target: $7.20 Actual: $7.69」；曲線「≥ $400 million above target 300% … = $200 million above target 200% … = target 100%」；計算方法「NGS ARR … excluding the contribution of merger and acquisition transactions consummated in the relevant fiscal year in which the purchase price for the acquisition exceeds 4% of our market capitalization」；「The Compensation and People Committee considered a lower threshold that would have captured our acquisition of Chronosphere, but determined …」；「the financial results generated from our acquisition of CyberArk during fiscal 2026 were excluded … This change resulted in an increased NGS ARR performance achievement for the fiscal 2026 performance period for the fiscal 2026 PSUs」；24 筆併購（FY19–FY26）「Excluding the CyberArk acquisition, the top end of this range was approximately 3%」；FY27 PSU 封頂線 $450M、最高 300%；2025 Say-on-Pay「46% support」。
2. PANW 10-K FY26（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1327567/000132756726000023/panw-20260731.htm ：Note 8「On January 29, 2026, we completed our acquisition of Chronosphere … The acquisition resulted in forming our next-generation observability platform. The total purchase consideration … was $ 3.0 billion」（現金 $2,842M＋替代獎酬 $109M）；CyberArk $21.1B（2026-02-11）；Koi $231M、Portkey $117M；訂閱與支援營收增加「including from our CyberArk and Chronosphere acquisitions」。
3. PANW 8-K 4Q FY26 業績稿（sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1327567/000132756726000019/ex991q426earningsrelease.htm ：NGS ARR $9.10B（+63%）；定義「annualized allocated revenue of all active contracts」；FY27 指引 NGS ARR $11.075–11.175B（+22–23%）、1Q FY27 $9.54–9.56B。報告 $9.10B − PSU 口徑 $7.69B ≈ $1.41B ≈ CyberArk 貢獻 `[D]`。
4. PANW 收購公告 8-K（2025-11，sec.py 實讀）https://www.sec.gov/Archives/edgar/data/1327567/000132756725000032/ex992pressrelease.htm ：「total consideration of $3.35 billion … Chronosphere reports generating annual recurring revenue (“ARR”) of over $160 million as of the end of September 2025, growing ARR triple-digits year-over-year」。
5. 既讀（L15-I#4 測一，`work/20261029_L15-I#4_test1_CL.md`）：PANW CFO「9 figure benefit from a large LLM customer migrating to Chronosphere」、CEO 稱較在位者便宜 30–40% 且銷售限 AI 原生——測一須回原逐字稿重讀，不得以本卡轉述為證。

缺段（§7-2）：Chronosphere FY26 末 ARR 未取；有機 NGS ARR 一手口徑未取；FY27 PSU 之 NGS ARR 目標值未取（DEF 14A 是否揭露未查）；具名賣方或代理顧問（ISS／Glass Lewis 2026 報告）是否量化門檻下無機 ARR 未取；同業（CRWD、ZS、FTNT DEF 14A）之 ARR 型 PSU 與併購排除規則未取。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 門檻下無機 ARR 量級小：Chronosphere ≈ $0.2–0.3B 對 NGS ARR $9.1B；即使排除，分項仍 ≥ 200% | DEF 14A；收購公告 | 量級不足（→(2)） |
| R2 | 委員會已把最大筆（CyberArk）排除並提高封頂線、降最高倍數，治理已收緊；激勵扭曲已被股東壓力修正 | DEF 14A（Say-on-Pay 46% 後之改動） | 誘因不作用（→(4)） |
| R3 | 公司已在業績稿與電話會議拆示 CyberArk／Chronosphere 對 ARR 之貢獻，市場已知 | 業績稿／逐字稿（待測一實讀） | 已定價（→(3)） |
| R4 | 本質為 bookings 計酬（L6-I#2 型）或收購方收割（L15-I#3 型） | — | 歸他型（→(5)） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) PSU 之 NGS ARR 目標／實際／排除規則無法由 ≥ 2 期 DEF 14A（2025、2026）重算，或 Chronosphere 對 FY26 NGS ARR 之貢獻無一手數值或可錨定區間（收購時 ARR × 成長之 `[D]` 須有一手錨）；或
(2) `[D]` 門檻下無機 ARR（Chronosphere＋Koi＋Portkey）÷ FY26 NGS ARR 年增量（PSU 口徑）< 10%，**且**排除後 NGS ARR 分項達成率仍 = 300%（計入與否不改支付；門檻凍結於此）；或
(3) 公司業績稿、10-K、電話會議官方逐字稿或具名賣方已就有機 vs 無機 NGS ARR（含 Chronosphere）作量化分解；或
(4) DEF 14A 原文顯示 FY27 PSU 已將門檻下併購排除或改以有機 ARR 計，使誘因於 12 個月窗內不作用；或
(5) 可運作對照只能寫成 L6-I#2（bookings 計酬→RPO）或 L15-I#3（收購方收割）；或
(6) 12 個月內無檢驗事件（1Q–4Q FY27 業績稿 NGS ARR、2026-12 年會 Say-on-Pay 結果、2027 DEF 14A 之 FY27 PSU 實際與排除）。

複查觸發器（若日後殺）：PANW 首次揭露有機 NGS ARR 或 Chronosphere ARR；任一資安／基礎設施軟體商 DEF 14A 首次以併購規模門檻調整 ARR 型 PSU；代理顧問對門檻下無機 ARR 計入出具反對建議。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：DEF 14A PSU 表；Note 8 併購；訂閱與支援營收；RPO。2. 可交易工具：平台型資安軟體商普通股（不選）。3. 半衰期：PSU 年度評量（FY27 期末 2027-07-31，揭露於 2027-10 DEF 14A）。

## 7. 本輪寫入

寫入：本卡；`query/QUEUE.md` 新 ANALYST 列 Q-0167；`query/ARCH_matrix.md` L15［I］加「#5 已生成」；`AIM_FUNNEL.md` §3 一句與日期行。線索輸出（§D）：0 筆（實讀事實屬資安／可觀測軟體之併購與薪酬，非算力投入、AI 收入、硬體、雲端合約或資料中心）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L15-I#1–#4、L15-A#1–#5、L15-P#1–#5、L6-I#2、L14-I#5、C-I5；不碰 L1-P；不寫 T。
