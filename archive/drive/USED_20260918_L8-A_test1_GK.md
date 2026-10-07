<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1gBwKrvv9-zeGh4QFXlpsJ1NNs91UmaBS；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1kjyrtcpH_9kHp2-Cizvc19BPQBRAIaH8；1m1gnD5EzVjT_WsLAoA9l8nQVJwVsrSGP | EMITS: （本檔；Drive work/ 上傳後填 fileId） -->
# L8-A 測一｜B 端實讀（賣方 crowd／產出單位＋買方 human-data 科目）

**角色：** ANALYST@GK　**日期：** 2026-09-18　**格：** L8-A（標註／驗證：會計恆等）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFlezc86uZvd3EqXI`、不開 T。
**原陳述（生成卡 `1gBwKrvv9-zeGh4QFXlpsJ1NNs91UmaBS`）：** 可形式化標註被模型預標與合成資料吃掉之後，剩餘分母是「不可形式化任務」的存量上界，不是隨模型能力單調擴張的條數趨勢；市場若把標註支出當量、把條數當可外推流量，會把有效單價讀成趨勢項。恆等式本身為真；錯價只在把上界誤讀成趨勢。
**種子單位：** 3h＝標註支出÷交付有效條數；4d＝標註支出÷交付工時（單位不同，不可 silently 互換）。
**否決觸發（生成卡寫給本輪）：** (1) 任何可重算序列都必須借用 L8-P「分鐘／條」或無法與工時／營收桶分離；或 (2) 「不可形式化任務存量」找不到可單位化代理，只剩 mix／質性敘事。
**領域最近公開（§7-10）：** Appen FY25 AR 2026-02-25；Appen AGM 2026-05-22；TaskUs FY25 10-K 2026-03-05；TELUS Q2 2026 MD&A 2026-07-31。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260917_L2-I_generate_GK.md` `1OvV53zLLTrOt4WO_ZNfmApZ06-ZGi-B4`；`20260918_L2-I_s74_GK.md` `1fwgTwX9Y8KyxTu-ZACyMGDYYzqfV9kYm`；`20260918_L8-A_generate_GK.md` `1gBwKrvv9-zeGh4QFXlpsJ1NNs91UmaBS`
- inbox_GK：空
- query 五檔在；MECH last_sync_utc 2026-09-18T07:01:54Z role ANALYST
- L8-P 重判已 USED_ 於 archive_work `1m1gnD5EzVjT_WsLAoA9l8nQVJwVsrSGP`

---

## 終態

**不通過。不進 T。** 機制（會計恆等）未被否證。失敗在分母與上界的申報層可觀測性。

| 測試項 | 結果 |
|---|---|
| B 端已實讀（非指名） | **通過**　Appen FY25 AR＋PDF、TaskUs FY25 10-K、TELUS Q2 2026 MD&A／通話；買方 10-K 抽樣 |
| 3h 分母「交付有效條數」同表存在 | **不通過**　集團層無有效條數／任務數時序 |
| 分子與分母可同表重算單價 | **不通過**　分子有（crowd%／crowd service costs）；分母無 |
| 4d 分母「交付工時」集團層 | **僅案例**　Cohere 2,400 專家小時／12 週；Nearmap 年承諾 18 萬小時。非集團 KPI |
| 上界「不可形式化任務存量」可單位化 | **不通過**　只見 GenAI mix、複雜度質性、自動化省本。R3 未分離 |
| 否決觸發 (1) | **觸發**　可重算序列＝營收桶／crowd%／案例工時；條數序列不存在 |
| 否決觸發 (2) | **觸發**　存量無代理 |
| 升格 T | **否** |

失效歸因（§7-2）：不是檢索失敗。失敗在量綱——3h 分母在已上市賣方年報／10-K 不存在；4d 工時只在案例；上界主張沒有獨立於任務 mix 的連續參數。現況檔名＝上列 work／query。複查觸發器＝生成卡原文（見下）。停。

4d §4.22 切分 1（工時為既有單位、值待揭露＝計算型＋P8 未完成）**不在本輪改判**；本輪只測 3h 種子之 B 端。③已從「未檢索」推進為「已檢索、申報層無有效條數」。

---

## 已實讀載體

### A. 賣方｜Appen（ASX:APX）FY25 AR，2026-02-25

實讀 listcorp 公告＋官網 PDF。

- 營收 US$230.8M；GenAI 佔營收 33%（FY24 22%）；Q4 GenAI 44.1%（對照期 34.8%）；毛利率 40.3%（FY24 39.3%）；AR 定義毛利＝營收−crowd expenses；crowd expenses／營收 59.7%（FY24 60.7%）。
- 法定損益「Crowd service costs」FY25 US$108.214M（FY24 126.933M）。**不得與 59.7% 混為同一欄**——後者為管理用 crowd expenses；前者為法定科目，口徑較窄。
- 前五大客戶 74.3%（FY24 67.3%）。Global 營收（除 Google 基期）−21%；China +75% 至 102.9M。
- 集團層：**無**交付有效條數、無任務數、無「分鐘／條」。
- 案例工時（≠集團分母）：Cohere／Command「2,400 expert hours in 12 weeks」；Nearmap「180,000-hour minimum annual commitment」。
- 案例條數（≠集團分母）：AGM 2026-05-22 與官網案例「50,000+ units」＝單一 Physical AI／egocentric video 專案累計，非年報時序。
- 自動化／複雜度（質性，非存量）：「$10 million cost reduction… technology enabled efficiencies」；「increasingly complex LLM projects」；「project complexity continues to increase」。

### B. 賣方｜TaskUs（NASDAQ:TASK）FY25 10-K，2026-03-05

- AI Services 營收 US$214.218M（FY24 135.107M，+58.6%）；佔總服務營收 18%。
- 計價原文：「bill… on either time-and-materials, cost-plus, unit-priced, fixed-price, or outcome oriented basis」；unit-priced「recognized monthly as transactions are processed based on objective measures of output」。
- 10-K／MD&A **未揭露**處理件數、有效條數、交付工時。Cost of services＝人員薪資為主，未把標註直接成本與產出單位同表分列。
- 含義：合約層承認「產出單位」存在，申報層不給該單位之集團時序。用 AI Services 營收當量＝營收桶，觸發 (1)。

### C. 賣方｜TELUS Digital（併入 TU，無獨立 TIXT 10-K）

- Q2 2026 MD&A（2026-07-31，ex99d2）：四條服務線含 **AI and data solutions**；Digital 營收季減 US$75M，原因之一＝「client ramp-downs in our AI and data solutions service line」。Digital Adj. EBITDA Q2 US$72M（−20%）。CGU 減損 US$2,135M，未分到該服務線。
- 展望段：hyperscale 舊服務「automated faster than anticipated」（點名 content moderation、ad relevancy、search-related）；AI-enabling services「slower pace and scale」「deal sizes have compressed」（通話 2026-08-07）。
- **無**條數、工時、有效產出單位。Ramp-down＋自動化是 mix／需求敘事，不是存量上界的單位。

### D. 買方 10-K 抽樣（human data／RLHF 分列）

- Alphabet／Microsoft／Meta 最近 10-K：R&D、基礎設施、SBC 分列；**無** human data／RLHF／標註支出獨立科目。
- OpenAI 外洩審計（第三方報導，非 10-K）：R&D／Azure 算力為主，不報有效條數。
- 第三方「每實驗室約 US$1B human training data」（HeroHunt／SemiAnalysis 轉述）≠申報層分母。C-I2 已殺路徑，本輪不把估價當科目。

### E. 價目／第三方（明示非申報層）

- Scale Rapid FAQ：任務點價目（英 expert 7×；self-label 超額 US$0.05／unit）。產品 SKU ≠年報有效條數。
- PCCVDI 2026-05-18 市價帶（框 US$0.04–0.12；專家偏好 US$5–20）＝第三方區間，不可與 crowd% 相除。

---

## 對種子與反方

| 主張 | B 端讀後 |
|---|---|
| 恆等式可寫 | 可寫。缺公開分母則不可重算 |
| 錯價＝把上界當趨勢 | 上界本身未單位化；市場「把條數當流量」在申報層無條數可讀，錯價句無觀測錨 |
| R1 無有效條數 | **成立** |
| R2 單位被換成工時／分鐘 | **成立**（唯一產出單位＝案例工時或產品 SKU） |
| R3 mix 可解釋單價／毛利 | **未分離**　GenAI 22%→33% 與 GM +100bp 同向，無獨立存量序列 |
| R4 買方未分列、私有主體≠申報 | **成立** |

TaskUs AI Services +58.6% 與「分母被存量封頂」方向衝突；衝突可被 mix（機器人／AV／GenAI 單價上升）消化，故不能當上界之否證，也不能當上界之證實。

---

## 不開 T／§7-4

進 T 需數值窗、外部先驗、把 H1 寫成財富倍數。本輪可寫入的只有「申報層有 crowd 美元／無有效條數」。不夠把上界換成可載入參數。

§7-4 三題本輪不答（生成卡：轉入個股層時必問；本格不轉、不進 T）。

**複查觸發器（沿用生成卡，不改寫）：** 任一美股或 ASX 上市標註／驗證主體於年報或 10-K／20-F 同期分列（i）標註／驗證直接成本與（ii）交付有效條數或可重算之等效產出單位，且該產出單位不是已殺 L8-P 之「分鐘／條」翻版。

---

## URL

1. https://www.listcorp.com/asx/apx/appen-limited/news/2025-annual-report-3319129.html
2. https://cdn.prod.website-files.com/656a605609413dfd3feb9d34/699fbc072974a573b2b7a48c_Appen%20Annual%20Report%202025.pdf
3. https://www.listcorp.com/asx/apx/appen-limited/news/agm-ceo-s-address-and-amp-presentation-guidance-reaffirmed-3355990.html
4. https://www.appen.com/case-studies/physical-ai-robotics-annotation-eval
5. https://www.sec.gov/Archives/edgar/data/1829864/000182986426000012/task-20251231.htm
6. https://www.sec.gov/Archives/edgar/data/868675/000110465926088973/tu-20260630xex99d2.htm
7. https://www.fool.com/earnings/call-transcripts/2026/08/07/telus-tu-q2-2026-earnings-call-transcript/
8. https://api-reference.scale.com/docs/rapid-faq
9. https://www.pccvdi.com/insights/ai-training-data-cost-benchmarks-2026

**（完）**
