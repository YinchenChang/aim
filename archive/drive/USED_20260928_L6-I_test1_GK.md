<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1MLSGbk8FqWE0tjVvOZzlWnh6WuFLQtNY；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi；10aH5MscncgySFaJadvJsX3z0OXviAie_；1Pm249SbDe6OUmA3RXYdqt-O_PrC9pj_z | EMITS: PENDING_UPLOAD -->
# L6-I 測一｜B 端實讀（同一主體 10-K／10-Q 集中度佔比 × backlog／RPO 規模；可否單位化）

**角色：** ANALYST@GK　**日期：** 2026-09-28　**格：** L6-I（雲端與基礎設施服務：長約逆選擇／backlog 品質不隨規模改善）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先同一主體 10-K／10-Q **同檔**分列（i）RPO 或 contracted lease revenue 總額與（ii）≥10% 客戶營收或應收佔比（可畫至少兩期）與（iii）具名對手方承諾或預付／應收。**禁止**只重讀二手表／通話 ARR、已簽約未交付／已交付容量比（L6-A）、承租未開始租／RVG／JV（L13-A）、續約單價比 `k`（C-A4）、折舊年限（C-A3）、把指名主體改寫成空方（T-15）。不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T、不入 §1。不測 L6-P。不改測 L6-A。不重開 C-A3／C-A4。不選券。
**原陳述（生成卡 `1MLSGbk8FqWE0tjVvOZzlWnh6WuFLQtNY`；種子 3h §3.29）：** 最願簽長約、鎖容量者，是替代選項最少者；backlog 規模上升不蘊含對手方品質上升。錯價只在把「合約堆高」讀成「對手方集合改善」。
**對照式（生成用，非正式載入）：** `Q_t = f(Conc_t, Alt_t, Cap_t)`；`B_t`＝RPO 或 contracted lease revenue。`Conc_t`＝同檔 ≥10% 客戶營收／應收佔比。`Alt_t`／`Cap_t`＝具名對手方替代產能或自有資本／預付。本輪不把 RPO 總額當作品質，不把前三大佔比下降單獨當成品質改善，不寫 H1。
**否決觸發（生成卡寫給本輪）：** (1) 實讀後無法在同一主體 10-K／10-Q 並列 backlog／RPO 與 ≥10% 客戶佔比（可畫兩期），只剩通話／二手表；或 (2) 可運作對照只能寫成未交付／已交付容量比（滑回 L6-A）；或 (3) 只能寫成承租未開始租／RVG／JV（滑向 L13-A）；或 (4) 只能寫成該主體空方或委託資本外論點（滑向 T-15）；或 (5) 公開層已穩定可拒絕「backlog 變厚而對手方替代選項／自有資本不改善」——例如最長承諾穩定來自最高替代、最高自有資本對手方，且集中度下降與該事實同向。
**領域最近公開（§7-10）：** CRWV 10-Q 期 2026-06-30 acc `0001769628-26-000366`（2026-08-12）；CRWV FY2025 10-K acc `0001769628-26-000104`（2026-03-02）；APLD FY2026 10-K 期 2026-05-31 acc `0001144879-26-000048`（約 2026-07-30）；CORZ 10-Q 期 2026-06-30 acc `0001839341-26-000014`。下一官方檢查點＝任一美股可交易雲端／HPC 租賃主體於 10-K／10-Q／20-F **同檔**分列 RPO 或 contracted lease revenue、≥10% 客戶營收或應收佔比（兩期）、以及具名對手方承諾或預付／應收，且該分列與對手方自有資本或替代產能可對照。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：僅 `20260928_L6-I_generate_GK.md` `1MLSGbk8FqWE0tjVvOZzlWnh6WuFLQtNY`（12815 B，2026-09-28T12:36:34Z）。無其他進行中 work 檔。
- query/：ARCH_dead `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`；ARCH_matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`（FUNNEL §3：L6［I］＝已生成）；CHARTER_HIST `1DKg3HUr-zOWw20OmNe1aDpWT_izDwdiT`；INDEX `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`；MECH `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-09-28T12:29:26Z role SCOUT）
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-09-28；§1 無 L6-I；§3 L6［I］＝已生成；L6［A］＝測一部分通過｜不進 T）
- 本輪上傳前 work/ exact_name `20260928_L6-I_test1_GK.md` 空；無內容相近測一
- work 主動維護：L6-I 生成卡未吸收進 FUNNEL／matrix（待本測一後由 SCOUT 對齊狀態欄）。本輪不建 `DONE_`。生成卡標頭仍寫 `EMITS: PENDING_UPLOAD`（實際 fileId＝`1MLSGbk8FqWE0tjVvOZzlWnh6WuFLQtNY`）；與既有測一卡慣例相同，不另發 HEALTH、不改原檔。

---

## 終態

**測一通過（可觀測／可並列）｜不進 T。** 指名 B 端在同一美股可交易出租／雲主體之 10-Q／10-K **成立**：CRWV 10-Q 同檔並列未履行 RPO 總額與 ≥10% 客戶營收／應收佔比（兩期），Item 1A 同檔具名 OpenAI／Meta／Jane Street／Microsoft 承諾；CRWV 10-K 同檔並列 RPO 與三年佔比表，且 Item 1A 把 FY2025 最大客戶釘到 Microsoft。機制（集中度附註與 backlog 規模可同檔重算對照）未被否證。否決 (1)–(4) 未觸發。否決 (5) 未觸發：最長／最大新增承諾同時來自高替代對手方（Meta／Microsoft）與較少公開替代的對手方（OpenAI、Jane Street），不能穩定拒絕種子，也不能確認種子方向。

不進 T：RPO **無**對手方分桶，故 `B_t` 不是 `Q_t`；Customer A–D「跨期可換人」，佔比列不可鍊成同一對手方時間序列；`Alt_t`／對手方自有 `Cap_t` 不在本側 10-Q 以連續參數出現；R1（長約常來自最有替代者）與 R2（前一大佔比 71%→36% 可讀成品質改善）使 `∂Q/∂B` 符號不定；R3（集中度是 ASC 606 制式段）成立到「無可分離連續參數可寫 H1 倍數窗」。無 H1。§7-4 三題本輪不答。

與相鄰格：對照不是 leased／billable MW（L6-A 未改測；CORZ 該比只作「不得滑格」邊界）；不是承租未開始租／RVG（L13-A 未併入）；不是折舊年限（C-A3 未重開）；不是 `k`（C-A4 未重開）；CRWV／CORZ／APLD 只作揭露載體，不寫空方（T-15 地位未動）。禁止把 CORZ→CRWV→Microsoft／OpenAI 三層集中度加總（R6）。

---

## A. 指名 B 端：同一主體 RPO／合約規模 × 集中度（實讀）

| 源 | URL | 本輪讀到的量 |
|---|---|---|
| CRWV 10-Q 期 2026-06-30 acc `0001769628-26-000366` 本文 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/0001769628-26-000366.txt | **Note 2 Revenue／Significant Customers（同檔）：** 三個月至 2026-06-30：Customer A 36%、B 26%、C 10%；三個月至 2025-06-30：A 71%、B/C/D 皆 *。六個月至 2026-06-30：A 40%、B 23%；六個月至 2025-06-30：A 72%。\*＝未達 10%。**明文：**「The customer references of A through D may represent different customers than those reported in a previous period。」應收：2026-06-30 A 與 B 各 32%；2025-12-31 A 68%、D 11%。承諾合約營收佔比三／六個月皆 **98%**。遞延收入 2026-06-30 **$9.7B**（2025-12-31 $8.2B）。**RPO 同檔下段：** 定義＝配置於 not delivered or partially undelivered 之交易價格（淨估計變動對價）；含已開立／未開立對價。2026-06-30 未履行 RPO **$103.7B**：41% 至 2028-06-30、39% 第 25–48 月、餘第 49–78 月。**無**按對手方分桶 |
| CRWV 10-Q 同檔 MD&A | 同上 | 營收三個月 $2.575B vs $1.212B（+112%）；六個月 $4.653B vs $2.194B（+112%）。「Approximately **93%** of the revenue increase…attributable to expansion within our existing customer base」 |
| CRWV 10-Q 同檔 Item 1A | 同上 | 前三大合計約 36%／26%／10%（三個月至 2026-06-30）；去年同期前一大約 71%。2025-05 MSA＋2025-09 order form：OpenAI 承諾至約 **$6.5B through May 31, 2031**。2026-03 order form：Meta 初約承諾約 **$21.0B**（含至 2032-12-20 之新產能與既有選擇權至 2032-04-10）。2026-04 宣布 Jane Street（私人）承諾約 **$6.0B**。「Other significant customers include Microsoft and OpenAI。」信用風險段：以 committed contracts 之 **prepayments**、信用分析、LC／保證管理；「some of our customers may be highly leveraged」；無信用保險 |
| CRWV FY2025 10-K acc `0001769628-26-000104` 本文 | https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/0001769628-26-000104.txt | 業務段：2025-12-31 RPO **$60.7B** vs 2024-12-31 **$15.1B**；承諾約加權年期約 **五年**。Item 1A：**「approximately 67% of our revenue from our top customer, Microsoft, for the year ended December 31, 2025」**；FY2024 前兩大合計約 77%；FY2023 前三大合計約 73%。OpenAI 承諾至 2031-05-31 約 $6.5B；Meta 2025-09 order form 初約至 2031-12 約 $14.2B（其後 10-Q 已更新為含選擇權之 $21.0B，不得把兩數加總）。Note「Customer Concentration」表：Customer A 67%／62%／35%（2025／2024／2023）；B *／15%／17%；C *／*／21%。跨期字母可換人。應收 2025-12-31 A 68%、D 11%。RPO 附註：2025-12-31 未履行 $60.7B，43% 初 24 個月、38% 第 25–48 月、餘第 49–84 月。**無**按對手方分桶 |

**單位核對（非正式載入；只證明可並列，不是 H1）：**

| 報告窗 | `B_t` RPO | 前一大營收佔比 | 第二／第三 | 具名承諾（同檔 Item 1A，非 RPO 分桶） |
|---|---|---|---|---|
| FY2024 末 | $15.1B | A 62%（10-K 表） | B 15% | 10-K 未把當年最大客戶釘名於表；Item 1A 彙總前兩大 77% |
| FY2025 末 | $60.7B | A 67%；Item 1A＝Microsoft | 其餘 <10% | OpenAI $6.5B 至 2031-05-31；Meta 當時 $14.2B 至 2031-12 |
| 2025-Q2 | （本 10-Q 未給該季末 RPO） | A 71% | 其餘 <10% | — |
| 2026-Q2 | $103.7B | A 36% | B 26%、C 10% | OpenAI $6.5B；Meta $21.0B（含選擇權至 2032）；Jane Street $6.0B；Microsoft 具名仍在 |

`B` 上升與前一大佔比下降同窗出現。因 A–D 可換人，不得讀成「同一 Microsoft 從 67% 降到 36%」。RPO 時序桶是義務年期，不是對手方信用桶。

---

## B. 相鄰主體：同檔有規模＋集中度，但不得改寫本格通過條件

| 源 | URL | 本輪讀到的量 | 本格用法 |
|---|---|---|---|
| APLD FY2026 10-K 期 2026-05-31 acc `0001144879-26-000048` | https://www.sec.gov/Archives/edgar/data/1144879/000114487926000048/0001144879-26-000048.txt | **同檔 Contracted Lease Portfolio：** 1,410 MW／約 **$36.2B** 初約 15 年 take-or-pay、不可取消。表：Polaris Forge 1 **CoreWeave 400 MW／~$11.0B**；其餘四校園為未具名 investment-grade／high investment-grade hyperscaler（200／300／300／210 MW；~$5.0B／$7.5B／$7.5B／$5.2B）。Item 1A：HPC 段 FY2026 **一客戶佔繼續經營收入 59%**；Data Center Hosting 段 **一客戶 25%**。HPC 段於 FY2026 首棟營運後才有意義收入，本檔**無**第二個可比 HPC 佔比期 | 規模＋具名／未具名租戶＋單年收入佔比可並列。兩期 ≥10% HPC 佔比不足。CoreWeave 在本檔是**承租方**，與 CRWV 側集中度是同一需求池的另一層（R6），不得加總 |
| CORZ 10-Q 期 2026-06-30 acc `0001839341-26-000014` | https://www.sec.gov/Archives/edgar/data/1839341/000183934126000014/core-20260630.htm | Note 集中度：Colocation 段單一客戶三個月／六個月佔**總營收** 83%／**77%**（2025 同期 13%／12%＝當時主業仍是挖礦）。MD&A 具名該客戶＝**CoreWeave**；「colocation revenue is currently derived entirely from a single customer」。同檔：leased 590 MW／billable 395 MW。遞延收入（colocation）2026-06-30 **$652.3M**（2025-12-31 $553.9M），含「advance payments…for contracted capacity, including prepaid base license fees」及尚未交付容量 | 具名 100%＋預付存在。77% vs 12% 是業務組合切換，不是同一 backlog 的品質序列。**leased／billable 是 L6-A 所需量，本輪不拿來當 L6-I 通過條件** |

Microsoft FY2026 業績之 commercial RPO（生成卡列為客戶側自有承諾錨）本輪**不列為通過條件**：那是客戶側總承諾，不是出租方集中度表，也不能把 OpenAI 安排從 CRWV RPO 裡拆出。

---

## C. 本輪明確不讀、不引用為通過條件

- 二手佔比表（sec-api.io 2026-09-08 等）——生成卡已禁止代替原附註。
- CRWV／APLD 業績稿、簡報、通話 ARR 或 contracted power GW（非 10-Q 集中度表）。
- CORZ leased／billable MW 比、EQIX RPO／bookings（L6-A 已測；本輪不改測）。
- 承租 hyperscaler 未開始租／RVG／JV max exposure（L13-A 已測）。
- 折舊年限、減損附註（C-A3）；續約單價比 `k`（C-A4）。
- 把 CRWV、CORZ、APLD 任一主體寫成空方或選券（T-15）。
- 跨主體加總前三大佔比或加總 RPO。
- 把 Customer A 跨期當成同一對手方。
- 把 Meta 10-K $14.2B 與 10-Q $21.0B 加總成兩筆獨立承諾。

---

## 對 R1–R6 之測一處分（不寫 H1）

| # | 反方 | 本輪 |
|---|---|---|
| R1 | 最長、最大承諾常來自最有替代者（MSFT／META），逆選擇方向可能反轉 | **未決、方向不穩。** 同檔具名最大新增美元承諾含 Meta $21.0B（高替代）與 OpenAI $6.5B、Jane Street $6.0B（替代較不可見）。FY2025 已認列營收之最大客戶具名 Microsoft。不能用本輪資料確認「長約＝弱替代」，也不能穩定拒絕種子 |
| R2 | 前三大／前一大佔比下降可讀成品質改善 | **成立為讀法衝突。** 同檔可見前一大 71%（2025-Q2）→ 36%（2026-Q2），同時 RPO $60.7B→$103.7B。種子把「不隨規模改善」寫成單調命題，與已揭露時序衝突；但因字母可換人，下降也不是同一對手方的品質改善證明 |
| R3 | 集中度是風險因素制式段；RPO 無對手方分桶則 `Q` 不可寫 | **成立到單位化失敗。** 佔比與 RPO 可並列、可重算，但沒有「按信用／替代分桶的 RPO」把 `Conc×Alt×Cap` 寫成單一連續參數 |
| R4 | 預付／應收上升可讀成承諾增強 | **極性未釘。** CRWV 遞延收入 $8.2B→$9.7B、CORZ colocation 遞延 $553.9M→$652.3M，同檔寫成尚未交付容量之預付。可讀成 `Cap_t` 上升（品質升）或鎖住少替代對手方的預付（逆選擇）。本側 10-Q 無對手方自有資本表 |
| R5 | 滑向 L6-A／L13-A／T-15＝換格 | **未滑。** 通過條件只用同檔 `B`×`Conc`（＋具名承諾存在）。CORZ MW 比只標邊界。未寫空方、未選券 |
| R6 | 出租鏈三層投影，加總會把同一對手方算三次 | **遵守。** APLD 具名 CoreWeave $11.0B 與 CORZ 具名 CoreWeave 77% 只證明鏈存在，不進加總、不進通過條件 |

否決 (1) 未觸發：CRWV 10-Q／10-K 原檔已並列，不是只剩二手表。(2)(3)(4) 未觸發：對照不是交付比、不是承租表外、不是空方。(5) 未觸發：高替代對手方確實出現在最長承諾裡，但不是「穩定唯一」來源。

複查觸發器（若日後殺，沿用生成卡並收緊）：任一美股可交易雲端／HPC 租賃主體於 10-K／10-Q／20-F 同檔分列 RPO 或 contracted lease revenue **按對手方或按信用／替代桶**、≥10% 客戶營收或應收佔比（兩期、字母可對上同一對手方或具名），以及具名對手方承諾或預付／應收，且該分列與對手方自有資本或替代產能可對照。

---

## 本輪寫入／不寫入

寫入：本測一卡入 Drive `work/`（fileId 見上傳回傳；標頭 EMITS 於上傳前為 PENDING）。
不寫入：FUNNEL 正本、matrix、INDEX、ARCH_dead、ARCH_3h、CHARTER。不建 `DONE_`。狀態欄對齊＝下一 session SCOUT@GK。
L6-A 測一終態不改。L6-P 不生成。T-15 不寫。C-A3／C-A4 不重開。
