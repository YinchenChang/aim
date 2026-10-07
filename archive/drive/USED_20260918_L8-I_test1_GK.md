<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1FBpjkUsFmUgU7OPOrDttyz0-9CbETxAu；1UthEEUYzMj7mg7CgbnfowXyHHE5g-ENq；1gBwKrvv9-zeGh4QFXlpsJ1NNs91UmaBS | EMITS: （本檔；Drive work/ 上傳後填 fileId） -->
# L8-I 測一｜B 端實讀（賣方毛利／NPS vs 爭議／退件／重工）

**角色：** ANALYST@GK　**日期：** 2026-09-18　**格：** L8-I（標註／驗證：誘因）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不開 T。
**原陳述（生成卡 `1FBpjkUsFmUgU7OPOrDttyz0-9CbETxAu`）：** 標註／驗證之品質對付費方不可獨立核驗，故不能寫進可執行契約；市場看得到的是賣方毛利與單價，看不到交付爭議／退件／重工率。若把毛利擴張讀成「品質溢價」或把單價下行讀成「效率」，都把不可觀測的品質維度折進相鄰價格。
**否決觸發（生成卡寫給本輪）：** (1) 爭議／退件／重工率在已上市主體年報或 10-K／20-F 不存在，只剩 GM／NPS／質性品質框架；或 (2) 可觀測毛利／單價變動只能沿 C-I2 已殺路徑（mix／自動化／專家單價）解釋，無法把「品質不可契約」寫成獨立診斷項；或 (3) 「品質可契約」在公開層成立（outcome 計價＋公開合格率時序），使種子方向翻負。
**領域最近公開（§7-10）：** Appen FY25 AR 2026-02-25；Appen AGM 2026-05-22；TaskUs FY25 10-K 2026-03-05；Innodata FY25 10-K 2026-02-26；TELUS Q2 2026 MD&A 2026-07-31；Scale autorater 文 2025-07-28（非申報）。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260917_L2-I_generate_GK.md` `1OvV53zLLTrOt4WO_ZNfmApZ06-ZGi-B4`；`20260918_AIM_FUNNEL_body_GK.md` `1V4NGbycvBRtYRtEYpA1AWzY4W4ow-UaX`；`20260918_ARCH_matrix_body_GK.md` `1TAid1cQ295q-2llLMDZ1IkIMF2KEkS8A`；`20260918_L8-I_generate_GK.md` `1FBpjkUsFmUgU7OPOrDttyz0-9CbETxAu`
- inbox_GK：空
- query 五檔在；MECH last_sync_utc 2026-09-18T07:58:02Z role ANALYST
- L8-A 測一 Drive work `1UthEEUYzMj7mg7CgbnfowXyHHE5g-ENq`（本輪 CONSUMES，不重測條數分母）

---

## 終態

**不通過。不進 T。** 機制（誘因錯配：付費方無法從公開層獨立核驗交付品質）未被否證。失敗在指名不可見端的申報層可觀測性，以及「不可契約」被合約層原文削弱。

| 測試項 | 結果 |
|---|---|
| B 端已實讀（非指名） | **通過**　Appen FY25 AR＋PDF＋AGM、TaskUs FY25 10-K、Innodata FY25 10-K、TELUS Q2 2026 MD&A；Scale 部落格／HeroHunt＝非申報 |
| 3h 指名端「交付爭議率／驗收退件率／重工率」同表存在 | **不通過**　已上市賣方集團層無此三率時序 |
| 可見端 GM／單價與爭議率可同表對照 | **不通過**　可見端有（GM、crowd%、cNPS／客戶 NPS）；不可見端無 |
| NPS ≠ 爭議率 | **成立**　Appen 客戶 NPS 57→68 與 crowd NPS 33→22 反向；TaskUs cNPS 66。滿意度代理不是退件時序 |
| 否決觸發 (1) | **觸發**　只剩 GM／NPS／質性品質框架／平台 uptime |
| 否決觸發 (2) | **觸發**　Appen GM +100bp 管理層寫成 GenAI mix＋自動化；與已殺 C-I2 路徑不可分 |
| 否決觸發 (3) | **未完整觸發**　outcome／unit／「accepted by the customer」在合約／收入認列層存在；公開合格率時序不存在 |
| 升格 T | **否** |

失效歸因（§7-2）：不是檢索失敗。失敗在量綱——指名品質序列在已上市標註／驗證主體年報與 10-K 不存在；種子後半句「不能寫進可執行契約」被收入認列與計價原文削弱，但削弱不足以把合格率寫成可載入參數。現況檔名＝上列 work／query。複查觸發器＝生成卡原文（見下）。停。

③已從「生成錨、未實讀」推進為「已檢索、申報層無爭議／退件／重工率」。不併殺 L8-P／L8-A（§7-3）；本格不入 §1。

---

## 已實讀載體

### A. 賣方｜Appen（ASX:APX）FY25 AR，2026-02-25

實讀 listcorp 公告＋官網 PDF。

- 營收 US$230.8M（除 Google 基期 +4.5%）；GenAI 佔營收 33%（FY24 22%）；Q4 GenAI 44.1%；毛利率 40.3%（FY24 39.3%）；crowd expenses／營收 59.7%（FY24 60.7%）。管理層把毛利改善寫成 mix＋自動化／技術效率，**非**爭議率下降。
- 客戶 NPS 68（FY24 57）；crowd NPS 22（FY24 33）。STI：客戶 NPS＝119% 目標；crowd NPS 低於門檻。兩邊反向＝付費方滿意與供給方不穩可並存，不是爭議時序。
- 平台 uptime 99.9%；無重大個資／資安事故。品質用語全為質性（「high-quality datasets」「data quality as the north star」）。
- 集團層：**無**交付爭議率、驗收退件率、重工率、合格率。
- 收入認列（Note 4／KAM）：營收於「required data is delivered and **accepted by the customer**」按完工比例認列；審計抽「customer acknowledgements」。可變對價含折扣／退款／rebate，受 constraining principle 約束。**契約層存在驗收閘**；年報不給閘的通過率時序。

### B. 賣方｜TaskUs（NASDAQ:TASK）FY25 10-K，2026-03-05

- AI Services 營收 US$214.218M（FY24 135.107M，+58.6%）；佔總服務營收 18%。
- 計價原文：「bill… on either time-and-materials, cost-plus, unit-priced, fixed-price, or **outcome oriented** basis」；unit-priced「recognized monthly as transactions are processed based on objective measures of output」；outcome「recognized when it is reasonably certain that the desired outcome has been achieved」。
- 「specialized quality frameworks」質性；Data Quality Services「accuracy of our work directly impacts…」。cNPS 66（81% 同意營運預期經常被滿足）。
- 風險因子：未達客戶品質標準可致成本、失客、索賠。**無**爭議／退件／重工／合格率時序。
- 含義：合約層承認產出單位與 outcome 閘存在；申報層不給該閘之集團時序。用 AI Services 營收或 cNPS 當品質＝相鄰代理。

### C. 賣方｜Innodata（NASDAQ:INOD）FY25 10-K，2026-02-26

- 質性「industry-leading data quality」；工作臺「detect human expert inconsistencies」。通話層談缺陷在進模型前被攔住——無集團合格率。
- 會計原文：「records billing adjustments relating to **quality issues on delivered services, service penalties and price adjustments**」。品質扣款在帳上存在，**不是**公開爭議率時序。
- 集團層：**無**爭議／退件／重工率。

### D. 賣方｜TELUS Digital（併入 TU）

- Q2 2026 MD&A（2026-07-31）：AI and data solutions 客戶 ramp-down；無條數、無爭議／退件／重工、無 NPS 分到該線。沿用 L8-A 測一載體，本輪不重解讀 mix。

### E. 非申報／買方（明示不作申報 KPI）

- Scale autorater 部落格（2025-07-28）：辯論閘把終審攔截 9%→1%；產品／研究敘事。Scale 無 S-1。
- HeroHunt 2026-06：轉述 Meta 研究員視 Scale 資料品質偏低（新聞，非 10-K）。未讀到遮蓋驗收 exhibit 之百分比（生成卡錨；本輪未取得可引用之公開合格率數字）。
- 買方抽樣：Alphabet／Microsoft／Meta 最近 10-K 分列 R&D／基礎設施／SBC；**無** human-data 品質損失或驗收糾紛獨立科目。

---

## 對種子與反方

| 主張 | B 端讀後 |
|---|---|
| 付費方無法從公開層獨立核驗品質 | **成立**　指名三率不存在 |
| 因此品質不能寫進可執行契約 | **削弱**　Appen accepted-by-customer；TaskUs unit／outcome；Innodata quality billing adjustments。缺的是公開時序不是契約本身 |
| 市場只見 GM／單價 | **成立** |
| 把 GM 當品質溢價＝錯價 | **不可檢**　無爭議率可對照；GM 已被寫成 mix／自動化 |
| R1 申報層無爭議率 | **成立** |
| R2 GM＝C-I2 路徑 | **成立** |
| R3 品質可契約 | **部分成立**　契約層是；公開合格率時序否 |
| R4 私有主體／買方不分列 | **成立** |

客戶 NPS 上升不能當「爭議率下降」的充分統計量：Appen 客戶 NPS 與 crowd NPS 反向，恰是生成卡預告的並存態。

---

## 不開 T／§7-4

進 T 需數值窗、外部先驗、把 H1 寫成財富倍數。本輪可寫入的只有「申報層有 GM／NPS／無爭議率；契約層有驗收／outcome 閘」。不夠把「品質不可契約」換成可載入參數，也不夠把 GM 拆成品質溢價。

§7-4 三題本輪不答（生成卡：轉入個股層時必問；本格不轉、不進 T）。

**複查觸發器（沿用生成卡，不改寫）：** 任一美股或 ASX 上市標註／驗證主體於年報或 10-K／20-F 同期分列（i）毛利率或可重算單價與（ii）交付爭議率、驗收退件率或重工率，且該品質序列不是客戶 NPS／平台 uptime 之翻版。

---

## URL

1. https://www.listcorp.com/asx/apx/appen-limited/news/2025-annual-report-3319129.html
2. https://cdn.prod.website-files.com/656a605609413dfd3feb9d34/699fbc072974a573b2b7a48c_Appen%20Annual%20Report%202025.pdf
3. https://www.listcorp.com/asx/apx/appen-limited/news/agm-ceo-s-address-and-amp-presentation-guidance-reaffirmed-3355990.html
4. https://www.sec.gov/Archives/edgar/data/1829864/000182986426000012/task-20251231.htm
5. https://www.sec.gov/Archives/edgar/data/0000903651/000110465926020655/inod-20251231x10k.htm
6. https://www.sec.gov/Archives/edgar/data/868675/000110465926088973/tu-20260630xex99d2.htm
7. https://scale.com/blog/building_autoraters_for_expert_level_reasoning_data
8. https://www.herohunt.ai/blog/top-10-data-annotators-for-ai-labs-2026-benchmark/

**（完）**
