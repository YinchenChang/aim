# L8-A 生成卡｜標註／驗證：會計恆等
<!-- BY: SCOUT@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1kjyrtcpH_9kHp2-Cizvc19BPQBRAIaH8；1m1gnD5EzVjT_WsLAoA9l8nQVJwVsrSGP；1FcrhXNs53jWu_8fFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9 | EMITS: （本檔；Drive work/ 上傳後填 fileId） -->
**日期：** 2026-09-18　**角色：** SCOUT@GK　**格：** L8-A　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 本輪改 FUNNEL §3 L8［A］與 matrix 同格＝已生成；不入 §1 現役、不開 T。

---

## 0. 本輪範圍

- 種子＝ARCH_3h §3.29 L8-A（`1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj`）：驗證勞動有效單價＝標註支出÷交付有效條數；分母受「不可形式化任務存量」封頂，為**上界而非趨勢**。B 端指名（3h 未實讀）：⚠ 主體未具名——③欄仍為【未檢索】（ARCH_4d §4.22）。
- 4d §4.22（`1kjyrtcpH_9kHp2-Cizvc19BPQBRAIaH8`，判定日 2026-09-04）寫的分母是**交付工時**，判 L8-A＝計算型＋P8 未完成，③未檢索、不得逕判無載入。3h（09-06）把分母改成**有效條數**並加上存量上界。本格以 3h 為生成種子，4d 為負向約束。
- 同層已處置：L8-P 已殺（表達層／可觀測性，work `1m1gnD5EzVjT_WsLAoA9l8nQVJwVsrSGP`；機制未否證；觸發器＝分鐘／條或法規工時揭露）；C-I2 已殺（所測價格由相鄰機制驅動）。本格是會計恆等，不是守恆工時、不是專家單價歸因。
- CHARTER §7-3：本檔不執行終端篩選。§7-4 三題只標「轉入個股層時必問」。§7-10：領域最近公開＝Appen FY25 AR 2026-02-25；TELUS Digital 已私有化併入 TU 分部（2025-10），2026-Q2 MD&A 2026-07-31。

---

## 1. 落差一句（生成物 → 候選陳述）

可形式化標註被模型預標與合成資料吃掉之後，剩餘分母是「不可形式化任務」的存量上界，不是隨模型能力單調擴張的條數趨勢；市場若把標註支出當量、把條數當可外推流量，會把有效單價讀成趨勢項。恆等式本身為真；錯價只在把上界誤讀成趨勢。

---

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等＋分母存量上界（非價格守恆） |
| 分子 | 標註／驗證支出（買方）或 crowd／專案直接成本（賣方） |
| 分母 | 3h＝交付有效條數；4d＝交付工時。兩者單位不同，不可 silently 互換 |
| 上界主張 | 不可形式化任務存量封頂分母；形式化任務被自動化後，條數不隨總需求線性上升 |
| 表達工具型態（只指名，不選券） | 已上市標註／驗證主體之 crowd 成本、毛利率、GenAI 營收佔比；買方 10-K 若分列 human data／RLHF 支出 |
| 重疊 | L8-P（分鐘／條，已殺，機制未否證）；C-I2（相鄰機制驅動價格，已殺）；L8-I（誰驗證驗證者，待重判）。重疊度未判，不構成丟棄 |

---

## 3. 已 fetch 之公開錨（URL；非完整 B 端實讀）

1. Appen FY25 AR（2026-02-25）：營收 US$230.8M；crowd 費用佔營收 59.7%（FY24 60.7%）；毛利率 40.3%；GenAI 佔營收 33%（FY24 22%）；案例工時（Nearmap 年承諾 18 萬小時）有，集團「有效條數」無。https://www.listcorp.com/asx/apx/appen-limited/news/2025-annual-report-3319129.html
2. Appen FY25 AR PDF 同文：前五大客戶 74.3%；Global 營收 −21%（除 Google 基期）。https://cdn.prod.website-files.com/656a605609413dfd3feb9d34/699fbc072974a573b2b7a48c_Appen%20Annual%20Report%202025.pdf
3. TELUS 2026-Q2 MD&A（2026-07-31）：Digital 之 AI and data solutions 為 ramp-down 項之一；不再有獨立 TIXT 10-K。https://www.sec.gov/Archives/edgar/data/868675/000110465926088973/tu-20260630xex99d2.htm
4. Scale Rapid FAQ：語言流利度乘數（英 expert 7×、日 expert 25×）；self-label 超額 US$0.05／unit——價目是任務點，不是年報層有效條數。https://api-reference.scale.com/docs/rapid-faq
5. HeroHunt 2026-09-06：Mercor＝專家小時；Surge＝完成任務；Scale 企業約把人工加價藏進平台包。無公開「支出÷有效條數」。https://www.herohunt.ai/blog/mercor-vs-surge-vs-scale-ai-2026-buyer-guide/
6. PCCVDI 2026-05-18：2026 市價區間（圖像框 US$0.04–0.12；專家偏好 US$5–20）；總成本框架把 QA／SME 另列 25–35%。第三方區間≠申報層分母。https://www.pccvdi.com/insights/ai-training-data-cost-benchmarks-2026
7. L8-P 重判已實讀：Appen／TIXT FY24／TaskUs 皆無「分鐘／條」KPI；EU Art.50／GPAI 模板無工時揭露。https://www.listcorp.com/asx/apx/appen-limited/news/2025-annual-report-3319129.html

以上為生成錨，**不宣稱科目可分離**。測試一之 B 端實讀屬 ANALYST。

---

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | 已上市賣方只報營收、crowd%、案例工時，不報有效條數；3h 分母在申報層不存在 | Appen FY25 AR；L8-P 重判 | 恆等式右端缺公開分母，計算型停在 P8 |
| R2 | 4d 分母是工時，3h 改條數——單位被換過；用 crowd% 或工時代理條數＝把已殺 L8-P 從後門載入 | ARCH_4d §4.22 vs ARCH_3h L8-A | 本格若只能用分鐘／條或工時，與 L8-P 撞車 |
| R3 | 單價上升可由任務組合（框→推理跡）解釋，不必有「不可形式化存量」上界 | PCCVDI 價帶；Appen GenAI 佔比 22%→33% | 上界主張無獨立觀測，只是 mix 敘事 |
| R4 | 買方 human-data 支出未分列；私有主體（Scale／Mercor／Surge）估價≠申報 | Scale 無 S-1；C-I2 已殺 | ③仍可能停在未檢索或不可分離，而非錯價 |

種子仍可能在「賣方 crowd 成本÷某種已揭露產出單位」上寫成可重算恆等；上界是否可單位化是測試一的題，不是本輪終端篩。

---

## 5. SCOUT 裁決

**留。** 不進 T。下一動作＝ANALYST@GK 對本格做測試一（B 端須實際 fetch 並列 URL）。

理由（只到殺／留）：
- 3h 生成物仍是可陳述之會計恆等，與已殺 L8-P／C-I2 不同型。
- 4d 已預先把本格標成計算型＋P8 未完成，禁止在③未檢索時逕判無載入。
- R1–R2 足夠強，故預設風險＝分母單位（條數 vs 工時）與申報層可否同時看到分子分母；不是機制已被否證。
- 終端三題未在本階段執行。

否決觸發（寫給 ANALYST，不是本輪執行）：
- 測試一 B 端實讀後，任何可重算序列都必須借用 L8-P 之「分鐘／條」或無法與工時／營收桶分離；或
- 「不可形式化任務存量」找不到可單位化代理，只剩 mix／質性敘事。

複查觸發器（若日後殺）：任一美股或 ASX 上市標註／驗證主體於年報或 10-K／20-F 同期分列（i）標註／驗證直接成本與（ii）交付有效條數或可重算之等效產出單位，且該產出單位不是已殺 L8-P 之「分鐘／條」翻版。

---

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：crowd／專案直接成本與產出單位是否同表分列；買方 human data／RLHF 是否獨立科目。
2. 可交易工具：恆等落在哪一類已上市主體（ASX 標註商／北美數位服務分部／尚未 S-1 之私有商），而非不可交易之實驗室內部。
3. 半衰期：形式化任務被自動化後，剩餘存量上界是否在 ≥12 個月重定價窗內仍可被同一科目觀測。

---

## 7. 本輪寫入／不寫入

寫入：FUNNEL §3 L8［A］【未生成】→已生成；matrix 同格。不寫入：FUNNEL §1 現役列、§2、§4 計數、§5、INDEX.json、ARCH_dead。正本仍同一 fileId，禁止新建同名檔。
