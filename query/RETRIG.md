# RETRIG — 複查觸發器掃描表（1/2；SCOUT-WATCH 用，CHARTER §7-2）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_dead.md；query/INDEX.json；AIM_FUNNEL.md | EMITS: query/RETRIG.md -->
**日期：** 2026-10-07　**建表：** SCOUT@CL（runbooks/SCOUT.md §B-1）。本表 R-01–R-19＝`query/ARCH_dead.md` 全列；R-20 起見 `query/RETRIG_2.md`（INDEX／FUNNEL 補列，ARCH_dead 已涵蓋之碼不重列）。觸發器原文照錄，不改寫、不補定義。結果只三種：未觸發／觸發／無法判定（失敗歸因）。

| R-## | 代碼 | 觸發器（原文照錄） | 可觀測來源（URL 或申報類別） | 最近檢查日 | 結果 |
|---|---|---|---|---|---|
| R-01 | L9-P | 應用商揭露「AI 建議之人工核可率」；或金融／醫療監理要求 HITL 工時申報。適用註 D：NOW＝acc 0001373715-26-000007／2026-01-29，不沿用 ARS | EDGAR 10-K／10-Q／ARS；金融／醫療監理公告 | 2026-10-07 | 未觸發。EDGAR FTS "human approval rate" 10-K/10-Q 2026-01-01..10-07＝0 筆（https://efts.sec.gov/LATEST/search-index?q=%22human%20approval%20rate%22）；"human oversight"+"approval rate"+AI＝5 筆，SOFI 10-K 已讀無此指標，FSLY×3／RBLX 未逐讀；FINRA 2026 報告僅監督紀錄期待、無工時申報義務（https://fintech.global/2026/04/17/how-finras-2026-report-reshapes-genai-compliance/） |
| R-02 | L8-P | 任一標註／驗證供應商於財報或監理申報揭露「每條交付平均人工分鐘數」；或 AI 法規附則要求訓練資料人工審核工時揭露 | EDGAR 10-K／10-Q（僅已上市主體）；AI 法規附則 | 2026-10-07 | 未觸發。INOD 10-Q 2026-06-30 無每條人工分鐘（https://www.sec.gov/Archives/edgar/data/0000903651/000110465926092021/inod-20260630x10q.htm）；EDGAR FTS "minutes per task" annotation 10-K/10-Q/20-F 2026＝0 筆。AI 法規附則未查（無法判定該半） |
| R-03 | L11-P | 任一主導主體上市或分部揭露消費級 AI 損益 | EDGAR S-1／F-1；分部揭露 | 2026-10-07 | 未觸發。OpenAI 僅 2026-06 機密 S-1，EDGAR 無公開版、未上市；CFO 2026-08-19 稱 2027 或更早（https://aitoolsrecap.com/Blog/openai-ipo-2026-valuation-timeline-what-investors-need-to-know）；無消費級 AI 損益分部揭露。其他主導主體未逐一查 |
| R-04 | C-A4 | P2 窗可重推至覆蓋 M-6（2027-10-31）且續約單價比 `k` 可反解 | 內部推算（P2 窗×M-6）；無外部 URL | — | 未檢查 |
| R-05 | C-A3 | 樞紐重開且折舊年限離散可歸因減損附註拆假設 vs 實際 | EDGAR 10-K 減損附註 | — | 未檢查 |
| R-06 | C-A1 | 10-K 首次以美元分列 consumption／Agentforce 營收與毛利 | EDGAR 10-K（CRM） | — | 未檢查 |
| R-07 | 能力上限／Confidential／自動化 R&D | — | 無（無觸發器） | — | 未檢查 |
| R-08 | VEEV | 出現具名反方論述 | 公開具名反方論述（研報／媒體） | — | 未檢查 |
| R-09 | C-A2 | L9 對應論點達門檻且條款非可撤回、單位經濟揭露恢復 | 內部（L9 論點）＋EDGAR 單位經濟揭露 | — | 未檢查 |
| R-10 | C-I1 | 已上市、估值可歸因於「模型權重能力」而非執行層工程之標的對照 | EDGAR／上市標的估值資料 | — | 未檢查 |
| R-11 | C-P1 | 營運商揭露 checkpoint 讀取占復原 >50%；儲存分列訓練／推論且訓練側成長不低於 GPU；非同步 checkpoint 三年採用 <50% | 營運商技術揭露；EDGAR 10-K | — | 未檢查 |
| R-12 | C-I2 | 上市主體毛利擴張經管理層歸因專家單價上升；或人類回饋支出分離為獨立科目 | EDGAR 10-K／10-Q MD&A | — | 未檢查 |
| R-13 | C-A5 | 任一前沿 API 商 IPO，或 10-Q 首次分列 API 已實現單價 | EDGAR S-1／F-1；10-Q | — | 未檢查 |
| R-14 | C-I3′ | 該公司 10-K 首次出現本機制之利益分列 | EDGAR 10-K | — | 未檢查 |
| R-15 | N-02 | 同利益分列觸發器 | EDGAR 10-K | — | 未檢查 |
| R-16 | C-P3 | 同 C-A5 | EDGAR S-1／F-1；10-Q | — | 未檢查 |
| R-17 | N-01 | GOOGL 首次分列 TPU 外部產品線，或 NVDA 分列異質／舊卡折價利益 | EDGAR 10-K（GOOGL、NVDA） | — | 未檢查 |
| R-18 | C-I5 | CRM／NOW／SNOW 首次按 AI 採用時序分群披露留存，或 AI vs 非 AI 之 NRR | EDGAR 10-K／10-Q（CRM、NOW、SNOW） | — | 未檢查 |
| R-19 | C-P4 | 某 DC REIT／冷卻商首次以美元分列水約束所致延期或成本 | EDGAR 10-K（DC REIT／冷卻商） | — | 未檢查 |
