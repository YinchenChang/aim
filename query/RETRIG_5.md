# RETRIG_5 — 複查觸發器掃描表（續 RETRIG_4 之 R-40–R-46）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/RETRIG_4.md | EMITS: query/RETRIG_5.md -->
**日期：** 2026-10-08　**拆出：** SCOUT@CL（`query/RETRIG_4.md` 將逾 8 KB，runbooks/SCOUT.md §B-1）。列內容自 RETRIG_4.md 原樣移入；規則同 RETRIG.md。

| R-## | 代碼 | 觸發器（原文照錄） | 可觀測來源（URL 或申報類別） | 最近檢查日 | 結果 |
|---|---|---|---|---|---|
| R-40 | L13-I | 任一已上市供應方於 10-K／10-Q 同檔分列對具名客戶之股權投資餘額與該客戶應收帳齡或信用損失分桶，且該客戶之公開信評行動可對照是否引用該分桶 | EDGAR 10-K／10-Q | 2026-10-08 | 未觸發。NVDA 10-Q 2026-07-26：應收集中只以未具名客戶列（五客戶 22/14/13/11/10%），無帳齡或信用損失分桶，股權投資僅分類列（上市 $42.8B／非上市 $47.9B／權益法），未具名對客戶（https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm；WebFetch 摘要讀前 100k 字元，Note 8 以後未讀）；CRWV 申報亦只列 AR 集中、無帳齡（https://sec-api.io/insights/coreweave-crwv-2026-revenue-analysis-top-customer-concentration-exposure，二手）。其他供應方未逐查 |
| R-41 | L14-P | 任一已上市主體於 10-K／10-Q 同檔分列付費席次期末存量與同一母體期末員工數，且導入／部署工時與被稱取代之職類工時可對帳 | EDGAR 10-K／10-Q | 2026-10-08 | 未觸發。MSFT FY2026 10-K（2026-06-30）未見付費席次期末存量，僅定性「installed base growth and ARPU expansion」，員工數只列自身約 22.3 萬（https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323660/msft-20260630.htm；WebFetch 摘要兩段讀取）；M365 Copilot「逾 3,000 萬付費席次」只見於 2026-07-29 法說，非 10-K，且無同母體員工數或部署工時（https://ai2.work/blog/microsoft-365-copilot-hits-30m-paid-seats-backlog-tops-678b，二手）。其他上市主體未逐查 |
| R-42 | L14-A | 任一已上市買方於 10-K／10-Q 同檔分列 IT 支出與總營收，且 AI 行與非 AI 行同檔可對帳，並標明是否含資本支出與 IT 部門以外支出 | EDGAR 10-K／10-Q | 2026-10-08 | 無法判定（失敗歸因：抽查對象 JPM 2Q26 10-Q PDF 回傳二進位不可讀 https://jpmorganchaseco.gcs-web.com/static-files/b42d7387-c6d9-4b6c-9abc-46a6b52bda43）。旁證：JPM 科技預算於 2026-01-13 法說揭露、Dimon 拒揭 AI 專項支出、未分資本／費用（https://letsdatascience.com/news/jpmorgan-increases-tech-and-ai-spending-bfbf4d00，二手）；全市場檢索未得任何 10-K／10-Q 同檔分列 AI／非 AI IT 支出。非存在性主張 |
| R-43 | L14-I | 任一已上市買方於 10-K／10-Q 同檔分列採購或 IT 採購之績效指標與被稱節省之人力成本，且該節省是否回流該採購預算可對帳，並標明預算擁有者 | EDGAR 10-K／10-Q | — | 未檢查 |
| R-44 | L15-P | 任一官方統計序列，或已上市資安軟體／SOC 營運主體之 10-K／10-Q，同檔分列界定母體之分析師人數與每人每日警報作業秒數或工時，使乘積可重算，並標明 on-call 是否在秒數內 | 官方統計序列；EDGAR 10-K／10-Q | — | 未檢查 |
| R-45 | L15-A | 任一已上市基礎設施軟體主體於10-K／10-Q同檔分列使用量與有效單價，使消費式營收可重算，且AI營收佔比同檔可對帳，並標明單價是否內生於使用量。s之定義仍以ARCH_3c §3.19實讀為準，不由測一補 | EDGAR 10-K／10-Q | — | 未檢查 |
| R-46 | L15-I | 任一已上市基礎設施軟體主體於條款頁或 10-K／10-Q 同頁分列出站費率與資料保留期，並標明客戶遙測之取用權是結構性計價還是可行使之合約權利 | 條款／授權頁；EDGAR 10-K／10-Q | — | 未檢查 |
