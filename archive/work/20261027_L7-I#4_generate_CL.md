# L7-I#4 生成卡｜模型層：誘因（照付不議之算力承諾使邊際現金成本趨零 → 承諾容量先於需求到位時之降價／免費量填充誘因）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；AIM_FUNNEL.md；archive/drive/USED_20260930_L7-I_generate_GK.md；archive/work/20261013_L7-I#2_generate_CL.md；archive/work/20261020_L7-I#3_generate_CL.md；work/20261020_L7-I#3_test1_CL.md；work/20261027_L7-A#4_test1_CL.md；work/20261027_L7-P#4_test1_CL.md | EMITS: work/20261027_L7-I#4_generate_CL.md -->
**日期：** 2026-10-27　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 2→3／6）　**格：** L7-I　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L7-A#4 本日測一，Q-0112 done）。非已殺／刻意排除格中最後測試日最舊＝2026-10-20（L7-I#3、L10-P／A／I#3、L11-A／I#3、L13-P／I#3、L14-P#3）；依 Q 序（Q-0072 早於 Q-0073…）與表序取 **L7-I**。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py take-or-pay utilization "minimum commitment" "price cut"`，命中 0。內部數字（§12）未取用。載體全由本輪 sec.py／WebSearch／WebFetch 實讀。
- 比對之舊檔與死因型態，本卡須異型：
  - **L7-I#1**（不通過）：評測取用權合約性。本卡不論評測。
  - **L7-I#2**（部分通過）：人才外部選擇權 × SBC。本卡不論人才。
  - **L7-I#3**（部分通過；(5) 觸發、(1)(3) 部分）：通路衝突／前二大客戶換供應。本卡不論客戶集中或中介換供應；主體是**實驗室作為算力買方**之固定承諾。
  - **L7-A#4**（本日部分通過）：功能別 vs 性質別分攤（同一可替代算力池）。本卡**不以分攤口徑為落差**；閒置容量轉入研發屬 L7-A#4 之觀測面，測一不得以 COR／R&D 比例變動作本卡證據。
  - **L7-P#4**（本日部分通過）：上下文長 1/L 斜率對毛利。本卡不論上下文定價結構，只論承諾容量與需求之時序缺口所生之定價誘因。
  - **C-A4／C-A3**（死 #4／#5）：GPU 出租方續約單價／折舊。本卡在承租（買）方，不論續約單價或折舊。
  - **L6-I#4**（不通過）：出租方交付終止權 × RPO；**L6-P#2**：RPO 交付上界；**L13-I#2**：擔保人選擇權。本卡為買方照付不議之定價後果，非賣方 RPO 品質。
  - **C-I1／C-A5／C-P3**（死 #10／#13／#16）：估值歸因權重／API 單價不可分離／權重支出非科目。C-A5 複查觸發器（前沿 API 商 IPO）已近觸發（S-1 公開、未掛牌）；本卡不代判。
- §7-10 領域最近公開：Anthropic 公開 S-1（2026-10-26，A1）；Reuters 讀 S-1（2026-09-29，A3）；Implicator（2026-09-29，A4）。下一檢查點＝掛牌後首份 10-Q 之 Note 13 承諾表與期中營收。

## 1. 落差一句

恆等骨架：`C_cash,t ≥ F_t`（照付不議之最低承諾付款）；在承諾容量內，服務邊際一單位請求之**現金**成本 ≈ 0（只剩電力等若有轉嫁者），會計成本卻按承諾全額認列。誘因：當承諾容量到位快於付費需求（`K_t > D_t`），實驗室之最適行為是以降每任務價格、擴大免費使用、加速遷移至「較低每任務成本」之新模型來填充容量，且同結構之同業（OpenAI 等）同時面對同一誘因 → 產業 API 實現單價下行快於單位成本。已見數點（A1）：截至 2026-06-30 固定或最低保證承諾約 2,656 億美元（1–20 年）；2025-12-31 後新訂約 4,170 億；2025-12-31 之不可取消承諾 2027 年 111.28 億；S-1 自述「may be committed to excess compute that remains underutilized」「take-or-pay provisions … regardless of actual utilization」，並把 Opus 4.5「lower price」列為 2026Q1 營收加速因素之一。種子主張：市場以「需求受算力供給所限」（A4 引 S-1）讀承諾，即視承諾為需求下界；本卡主張承諾到位後之**容量過剩區間**會經定價誘因傳導為實現單價下行，其路徑（承諾付款曲線 vs 營收、價目表變更日、免費存取成本）在 S-1 與後續 10-Q 可驗。本卡不定方向與量級，只立可拒絕之誘因鏈。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 誘因（沉沒之照付不議承諾 → 邊際定價；同業對稱誘因） |
| 量綱 | 年度最低承諾付款 $／yr；營收 $／yr；列表價 $／M token；`[D]` ψ_t＝F_t ÷ 營收_t（無量綱） |
| 可見端 | S-1／10-Q Note 13 承諾付款表（逐年）、期後事項；營收；價目頁與模型發布日；S&M 註腳「providing free access」 |
| 指名不可見端 | 實際利用率；各合約交付時程；內部轉入研發之容量（L7-A#4 範圍，不用） |
| 主張 | ψ_t 上升（承諾付款增速 > 營收增速）之季度，先行於列表價或每任務價下修與免費額度擴大；可由「承諾付款增速 ≤ 營收增速」「具名賣方已以容量過剩建模單價」或「承諾可展延／轉售」拒絕 |
| 外部參照物（測一查證） | 照付不議產能過剩導致價格戰之前例（例：電信光纖 1999–2002、LNG／航空座位）；測一取具名一手案例 |
| 表達工具型態（只指名，不選券） | 模型實驗室普通股（上市後）；不選券 |
| 重疊 | L7-A#4（同池分攤）、L7-I#3（同 S-1）、C-A5（L7 上市性）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. A1 Anthropic 公開 S-1（2026-10-26，sec.py 全文實讀）https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm ——Note 13「expected future fixed or minimum guaranteed commitments under these agreements were approximately $265.6 billion with terms ranging from one to 20 years」；2025-12-31 承諾表（2026 7,059／2027 11,128／2028 10,832／2029 8,304／2030 5,428／其後 11,808，合計 54,559 百萬）；期後「approximately $417 billion」；風險因素「minimum purchase commitments, take-or-pay provisions … obligate us to pay for resources regardless of actual utilization」「committed to excess compute that remains underutilized」；定價風險「we may be required to reduce our prices」；MD&A「lower prices and improved capability」。MD&A 合約義務表與 aggregate committed spend 之金額於 S-1 留白，待 S-1/A。
2. A3 Reuters（Echo Wang、Sabrina Valle，2026-09-29；BusinessDay 轉載）https://www.businessday.co.za/world/international-companies/2026-09-29-anthropic-plans-518bn-ai-infrastructure-spend-80-non-cancellable/ ——「at least $518bn over a decade」「about 80% … non-cancellable or requires payment regardless of usage」；Google「If our actual spend falls short, we must pay Google the difference」；無分析師、無利用率或定價敘述。
3. A4 Implicator（Marcus Schuler，2026-09-29）https://www.implicator.ai/anthropic-ipo-prospectus-518-billion-compute-commitments/ ——分夥伴承諾（Google ≥ 111.1B、Amazon 110B、Microsoft 31.4B、Broadcom 相關租賃約 161.2B、xAI ≤ 84.5B 90 日可取消）；轉述 TradingKey（Yulia Zeng）「must lower unit costs quickly enough」；Zitron 2025 成本；無容量過剩→定價之論述。
4. A5 Decrypt（Jose Antonio Lanz，2026-06-11）https://decrypt.co/370854/openai-wants-a-price-war-with-anthropic-is-it-proving-deepseek-right ——WSJ 報 OpenAI 考慮降開發者／企業價格；Delphi（Tommy Shaughnessy）論訂閱虧損；未以固定承諾為動機。
5. 指名未讀：WSJ 750B 報導（https://letsdatascience.com/news/wsj-reports-anthropic-could-spend-750-billion-on-computing-a3618629 ）；Augment〈S-1 Reconstructed〉（https://augment.market/pulse/anthropics-s-1-reconstructed-from-the-record ）；Renaissance Capital 九數字。
6. 測一須另取：S-1/A 之合約義務表金額；Anthropic 價目頁歷史（Opus 4.1→4.5→5.5 每 M token 價與日期）；OpenAI／Google 同期調價；具名賣方是否以承諾容量過剩建模實現單價；承諾是否可展延、轉售或轉租（xAI 90 日取消為反例）；外部前例。

## 4. 最強反方（具名，測一驗）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 需求受算力供給所限，承諾只是追上需求（S-1 自述過去「significantly underestimated our compute requirements」） | A1、A4 | 容量過剩區間不出現 |
| R2 | 降價已發生且被 S-1 與媒體歸因於能力／成本效率，市場已計入單價下行 | A1 MD&A、A5 | 已定價 |
| R3 | 承諾可轉入研發或內部使用（可替代池），過剩容量不需經定價出清 | A1「fungible by design」 | 誘因被吸收（且落入 L7-A#4 觀測面） |
| R4 | 部分承諾可取消（xAI 90 日）或可轉售予第三方 | A3、A4 | 非照付不議 |
| R5 | L7 未掛牌，無可交易主體 | `work/20261027_L7-A#4_test1_CL.md` (5) | 表達失敗（C-A5 型） |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 具名賣方／研究機構已以「承諾容量 > 需求 → 降價填充」建模實驗室實現單價或毛利——已定價（R2）。
(2) S-1／S-1/A 或後續申報顯示主要承諾可展延、轉售或轉租，或照付不議占比 < 50%——非沉沒（R4）。
(3) `[D]` ψ_t＝年度最低承諾付款 ÷ 年度營收（或最近一季 ×4），以 S-1 可得數計 2026→2027：若承諾付款增速 ≤ 營收增速（ψ 不升），且至測一日無一手證據顯示容量到位先於需求——過剩區間不成立（R1）。門檻：ψ 不升即觸發，凍結於此。
(4) 唯一可觀測之過剩出清管道為內部研發／免費使用之成本重分類（即只能用 COR／R&D 比例作證據）——落入 L7-A#4，型態重疊（R3）。
(5) 可運作對照只能寫成 L7-I#3、L7-A#4、L7-P#4、C-A4、L6-I#4 或 C-A5。
(6) 至測一日 Anthropic（或其他前沿實驗室）未掛牌，且無已上市主體能分離實驗室承諾與定價——表達不可行（R5）。

複查觸發器（若日後殺）：首份 10-Q 更新 Note 13 承諾表且營收同列；任一前沿實驗室公告列表價下修並於申報歸因於容量或利用率；具名賣方發布容量過剩→單價模型。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Note 13 承諾付款表、期後事項承諾、營收、S&M 免費存取成本、價目變更揭露。
2. 可交易工具：模型實驗室普通股（上市後）。不選券。
3. 半衰期：S-1/A → 掛牌 → 首份 10-Q（承諾與營收同期）。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` Q-0113；`query/ARCH_matrix.md` L7［I］標「#4 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 3 列（S-1 承諾數）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L7-I#1–#3、L7-A#1–#4、L7-P#1–#4、L6-I#4、C-A3、C-A4、C-A5、C-P3、C-I1 結論；不寫 T-15。
