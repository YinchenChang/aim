# RETRIG_3 — 複查觸發器掃描表（續 1/2 之 R-13–R-19）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/RETRIG.md；query/ARCH_dead.md #13–#19 | EMITS: query/RETRIG_3.md -->
**日期：** 2026-10-07　**拆出：** SCOUT@CL（`query/RETRIG.md` 逾 8 KB，runbooks/SCOUT.md §B-1）。列內容自 RETRIG.md 原樣移入；規則同 RETRIG.md。

| R-## | 代碼 | 觸發器（原文照錄） | 可觀測來源（URL 或申報類別） | 最近檢查日 | 結果 |
|---|---|---|---|---|---|
| R-13 | C-A5 | 任一前沿 API 商 IPO，或 10-Q 首次分列 API 已實現單價 | EDGAR S-1／F-1；10-Q | 2026-10-07 | 未觸發。Anthropic 僅 2026-06-01 機密 draft S-1（https://www.anthropic.com/news/confidential-draft-s1-sec）；截至 2026-09-29 EDGAR 無公開 S-1、僅 Reuters 報導之外洩草稿（https://decodethefuture.org/en/anthropic-s1-ipo-filing-explained/；https://leverageshares.com/us/anthropic-ipo-tracker/）；OpenAI 同為機密 S-1（見 R-03）；無前沿 API 商提交 10-Q。Zhipu／MiniMax 港交所 2026-01 上市早於本碼死亡日（ARCH_4b §4.15，2026-09-02），非新事件、亦無 10-Q（見 R-10）。EDGAR FTS 直讀本輪未獲許可，以二手追蹤頁為據 |
| R-14 | C-I3′ | 該公司 10-K 首次出現本機制之利益分列 | EDGAR 10-K | 2026-10-07 | 未觸發。「該公司」依 Drive 唯讀 ARCH_4b §4.15（`1IIpN9tt1L4JP_ZstWVAV3ad3ntqTq_9c`）＝NVDA（分部毛利 UL 型）；「本機制」原文【未摘】。NVDA 最新 10-K＝FY2026（期末 2026-01-25，https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm）早於死亡日 2026-09-02，此後無新 10-K（下一份預期 2027-02），故無「首次出現」之新載體；該 10-K 內容不重判 |
| R-15 | N-02 | 同利益分列觸發器 | EDGAR 10-K | 2026-10-07 | 未觸發。死因＝CPO 營收於上市主體未分列（ARCH_4b §4.15：COHR／LITE）。LITE FY2026 10-K（期末 2026-06-27，提交 2026-08-17，acc 0001628280-26-057358）改單一報導主體、僅 Components／Systems 兩類，CPO 未以美元分列（https://sec-api.io/insights/financial-analysis-of-lumentum-fiscal-2026）；COHR FY2026 10-K（期末 2026-06-30）分部 Datacenter & Communications／Industrial、垂直市場分列，CPO 無美元額（https://www.sec.gov/Archives/edgar/data/0000820318/000082031826000020/iivi-20260630.htm，前 100k 字摘要讀取，末 17k 字未讀） |
| R-16 | C-P3 | 同 C-A5 | EDGAR S-1／F-1；10-Q | — | 未檢查 |
| R-17 | N-01 | GOOGL 首次分列 TPU 外部產品線，或 NVDA 分列異質／舊卡折價利益 | EDGAR 10-K（GOOGL、NVDA） | — | 未檢查 |
| R-18 | C-I5 | CRM／NOW／SNOW 首次按 AI 採用時序分群披露留存，或 AI vs 非 AI 之 NRR | EDGAR 10-K／10-Q（CRM、NOW、SNOW） | — | 未檢查 |
| R-19 | C-P4 | 某 DC REIT／冷卻商首次以美元分列水約束所致延期或成本 | EDGAR 10-K（DC REIT／冷卻商） | — | 未檢查 |
