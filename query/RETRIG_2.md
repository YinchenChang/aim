# RETRIG_2 — 複查觸發器掃描表（2/2；R-20–R-35）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/INDEX.json；AIM_FUNNEL.md §1 | EMITS: query/RETRIG_2.md -->
**日期：** 2026-10-07　**建表：** SCOUT@CL。續 `query/RETRIG.md`；來源＝`query/INDEX.json` 各碼 `retrigger`（L2-I 依 INDEX 指向取 FUNNEL §1 原文）。規則同 RETRIG.md。R-36–R-46 於 2026-10-07 因 8 KB 上限原樣移至 `query/RETRIG_4.md`。

| R-## | 代碼 | 觸發器（原文照錄） | 可觀測來源（URL 或申報類別） | 最近檢查日 | 結果 |
|---|---|---|---|---|---|
| R-20 | L2-A | 新生成物 | 內部（ARCH_matrix 新生成） | 2026-10-07 | 未觸發。`query/ARCH_matrix.md` L2 列 A 格仍「已測｜不進 T」，無「已生成 #n」；`work/` 無 L2-A 生成卡；QUEUE 無 L2-A 列（內部檢查，無外部 URL） |
| R-21 | L2-I | 任一美股上市開發商或資料中心 REIT 於 10-K／10-Q 分列許可／併網撤回或附條件之已發生損失或有負債，且與租戶信用損失分列（FUNNEL §1；INDEX：見 FUNNEL §1） | EDGAR 10-K／10-Q | 2026-10-07 | 未觸發。EQIX 10-Q 2026-06-30 前 100k 字無許可／併網撤回或附條件之已發生損失或有負債（URL 見 RETRIG_3 R-19，末 16k 字未讀）；DLR 10-Q 2026-06-30 損益／資產負債表無此科目，附註未讀（同上）。環境：德州州長 2026-09-21 令 TCEQ 暫停全部資料中心許可至 ERCOT 稽核完成（約 2026-12 中，https://www.bracewell.com/resources/governor-abbott-orders-tceq-to-pause-all-permit-issuance-for-data-center-projects/），屬季後事件，尚無對應 10-Q；下次以 Q3 10-Q（2026-10 底起）再查。其他開發商未逐查 |
| R-22 | L1-A | 10-K分列已鎖定PPA單價與殘差現貨／關稅且可畫兩期 | EDGAR 10-K／10-Q | 2026-10-07 | 無法判定（失敗歸因：VST FY2025 10-K 可讀部分無 PPA $/MWh 或避險價量表，但 MD&A／7A／附註13 未讀到，https://www.sec.gov/Archives/edgar/data/1692819/000169281926000006/vistra-20251231.htm；EDGAR FTS 權限逾時未取）。TLN Q1 2025 新聞稿僅避險量比例、無 AWS PPA 單價（https://ir.talenenergy.com/node/8551/pdf）。非存在性主張 |
| R-23 | L1-I | ISO／RTO佇列或LBNL年報分列已繳保證金／場址控制／財務承諾MW vs 裸申請且可畫兩期 | ISO／RTO 佇列；LBNL Queued Up 年報 | 2026-10-07 | 未觸發（LBNL 半）。Queued Up 2026（2026-06，資料至 2025 底）active 容量只分有無 IA、單一時點；保證金／場址控制僅為改革條文、未分列 MW（https://eta-publications.lbl.gov/sites/default/files/2026-06/queued_up_2026_edition.pdf）。ISO／RTO 佇列未逐查 |
| R-24 | L3-A | 申報分列節點ASP或封裝營收與層別良率且可與晶粒面積對帳 | EDGAR 10-K／10-Q | 2026-10-07 | 未觸發（TSMC 半）。TSMC 3Q25 earnings release 僅節點占晶圓營收 %（3nm 23%／5nm 37%／7nm 14%），無節點 ASP、封裝營收、良率（https://investor.tsmc.com/schinese/encrypt/files/encrypt_file/reports/2025-10/ff1cf977182dad2178b6d158e61d375ac98ff517/3Q25EarningsRelease.pdf）。20-F 與其他申報人未查 |
| R-25 | L4-P | 10-K分列scale-up域內銅／光且可與CEI／IEEE對帳 | EDGAR 10-K／10-Q | 2026-10-07 | 未觸發（CRDO 半）。CRDO FY2026 10-K（期末 2026-05-02）全文兩段摘要讀取：營收未按 AEC／銅 vs 光、亦未按 scale-up vs scale-out 分列；scale-up／scale-out 僅見於市場敘述，copper cables 僅見於成本風險（https://www.sec.gov/Archives/edgar/data/0001807794/000162828026043303/crdo-20260502.htm；XBRL 揭露表未見於取回文本）。ALAB／MRVL／AVGO 未查 |
| R-26 | L4-I | 10-K分列系統／機櫃vs加速器或參考設計／系統授權收入 | 條款／授權頁；EDGAR 10-K／10-Q | 2026-10-07 | 未觸發（NVDA 半）。NVDA FY2026 10-K（期末 2026-01-25）全文兩段摘要讀取：Data Center 以「rack-scale systems, subsystems, or modules」敘述供貨型態，未以美元分列系統／機櫃 vs 加速器，無參考設計／系統授權收入行；軟體授權僅敘述（https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm）；二手稿僅給 Data Center 總額與 compute／networking 成長率（https://www.theenergymag.com/news/market-news/nvidia-reports-215-9-billion-in-fy-2026-revenue-as-data-center-networking-surges-142）。AMD／SMCI 與條款頁未查 |
| R-27 | L5-P | 10-K分列裝置BW與運算吞吐且可與產品頁／V_byte對帳 | EDGAR 10-K／10-Q | 2026-10-07 | 未觸發（MU 半）。MU 10-Q 期末 2026-05-28（提交 2026-06-24）只按事業單位（CMBU／CDBU／AEBU／MCBU）與 DRAM／NAND 技術分列營收，無 GB/s／TB/s 頻寬或運算吞吐（https://last10k.com/sec-filings/mu/0000723125-26-000015.htm，二手鏡像摘要讀取）。MU FY2026 10-K 本輪檢索未取得（失敗歸因：搜尋未回 EDGAR 連結），非存在性主張；其他申報人未查 |
| R-28 | L5-A | 10-K分列儲存vs運算或KV／context-cache營收且可與價目對帳 | EDGAR 10-K／10-Q | — | 未檢查 |
| R-29 | L5-I | 10-K分列出站／切換貸項或價目拆切換vs並行；或裁定出站＝違法切換 | EDGAR 10-K／10-Q | — | 未檢查 |
| R-30 | L6-A | 10-K同表分列已簽未交付MW或signed-not-commenced年化租金 vs 已交付／已計費且可畫兩期 | EDGAR 10-K／10-Q | — | 未檢查 |
| R-31 | L7-P | 10-K／10-Q／20-F同檔分列推論FLOP與每token或每FLOP焦耳 | EDGAR 10-K／10-Q／20-F | — | 未檢查 |
| R-32 | L7-A | 同檔並列檔位列表價與每百萬token FLOP；或10-K／10-Q／20-F同檔分列已實現單價與每FLOP成本 | EDGAR 10-K／10-Q／20-F | — | 未檢查 |
| R-33 | L7-I | 授權頁同頁分列持有人與holdout排除且可與標明版本的分數時序對照；或10-K／10-Q／20-F同檔分列評測取用支出與該評測分數 | 條款／授權頁；EDGAR 10-K／10-Q | — | 未檢查 |
| R-34 | L10-P | 10-K／10-Q／20-F同檔分列端側能量或殼溫／降頻門檻與留端vs回雲功能類或請求占比，且標明裝置類與是否含無線電 | EDGAR 10-K／10-Q／20-F | — | 未檢查 |
| R-35 | L10-A | 10-K／10-Q／20-F同檔分列轉介量或因此離開平台之點擊與每次分潤率或TAC÷該轉介收入，且標明分潤率是否內生於轉介量 | EDGAR 10-K／10-Q／20-F | — | 未檢查 |
