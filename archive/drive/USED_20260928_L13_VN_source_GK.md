# L13 來源對帳｜Van Nieuwerburgh 融資結構 vs 已有格
<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；10aH5MscncgySFaJadvJsX3z0OXviAie_；1Pm249SbDe6OUmA3RXYdqt-O_PrC9pj_z；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi | EMITS: PENDING_UPLOAD -->
**日期：** 2026-09-28　**角色：** ANALYST@GK　**上限：** 來源對帳，非生成卡、非 T／L／M
**⚠ 無金額部位、無尺碼。** 不改 FUNNEL／matrix／INDEX／ARCH_dead。不重開 C-A4。不把 T-15 改寫成空方。

**任務：** 對上輪 HANDOFF「未來租／殘值保證／專案 LTV 是否在同一主體 10-K 或評級預售中可重算、且與合併槓桿分列」做 B 端實讀；判定與 L6-A、C-A4、3h L13-A／L13-I 是否同一恆等。

**本輪開始 Drive 現況：** work＝HEALTH 兩份＋`DONE_20260923_HEALTH_GK` `1vOqAWh9feQK65EJAau9vBfA2bB47Nsys`＋L6-A generate `10aH5MscncgySFaJadvJsX3z0OXviAie_`＋L6-A test1 `1Pm249SbDe6OUmA3RXYdqt-O_PrC9pj_z`＋`DUP_PLACEHOLDER_L1-I_test1_do_not_use`。query＝ARCH_dead／matrix／CHARTER_HIST／INDEX／MECH。FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（§1 無 L13、無 L6-A）。matrix L13［P］［A］［I］＝已生成；L6-A＝已生成。C-A4＝已殺（L13；窗與 `k`）。

---

## 終態

**來源對帳完成｜不進 T｜不生成新格。** 指定楔（未開始租＋RVG＋專案債 vs 合併槓桿）在申報層**可重算**，且與三個已有種子不同構。ANALYST 不得改 3h 已生成格；升格／改寫生成屬 SCOUT。

| 已有格 | 種子恆等 | 本輪楔是否同一 |
|---|---|---|
| L6-A（測一部分通過｜不進 T，`1Pm249…`） | `R＝已簽約未交付／已交付` 領先營收；3h B 端＝RPO 附註 | **否。** L6-A 是房東／雲側容量時序。本楔是承租 hyperscaler 的義務入表時點與專案槓桿。 |
| C-A4（已殺，L13） | 融資／續約單價比 `k`；死因＝重定價窗與觀測時序不相容 | **否。** 本楔不需要 `k`，也不需要窗覆蓋 M-6。複查觸發器未滿足，不得重開。 |
| L13-A（3h 已生成未測） | 循環交易營收重複＝產業合計揭露營收 − 對外營收（關係人加總） | **否。** B 端是關係人交易附註的營收加總，不是租／RVG／專案 LTV。 |
| L13-I（3h 已生成未測） | 供應商同時為股東與債權人 → 公開信評資訊含量下降 | **相鄰、不是同一式。** 循環融資（NVIDIA RVG、模型商經 hyperscaler 借表）屬誘因／資訊；本楔是會計入表時點。L13-I 指名 B 端＝股權投資餘額 vs 應收帳齡，本輪未測該對。 |
| L13-P | GPU 熱循環壽命 | **否。** |

否決觸發未寫死於本卡。本輪停在「可觀測 ≠ 已生成 ≠ 可進 T」。

---

## A. 同一主體可重算：META 10-K／10-Q

| 源 | URL | 讀到的量 |
|---|---|---|
| META FY2025 10-K 租賃附註（edgar.tools 摘；申報 2026-01-29） | https://app.edgar.tools/companies/META/disclosures/leases | 已入表未折現租賃現金流：營運 $33.508B＋融資 $1.504B。**尚未開始**之營運＋融資租賃義務約 **$103.77B**（多為資料中心／主機代管／網路），2026–2030 開始，年期 >1 至 30 年。此表**不含** RVG。 |
| META 10-Q 期 2026-06-30 acc `0001628280-26-050705` | https://www.sec.gov/Archives/edgar/data/1326801/0001628280-26-050705-index.html ；本文 https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm | 路易斯安那校園 Venture：持有 **20%**。與 Venture 之租約 **2029 開始**，初始承諾合計約 **$12.31B**；每棟初約四年、可續至合計最多 20 年。2026-06-30：權益投資帳面 **$2.92B**（2025-12-31 $1.83B）；對該 Venture 之 **maximum exposure to loss $46.03B**（2025-12-31 $45.95B）＝權益帳面＋租賃承諾＋估計後續出資＋RVG 上限。尚未開始租賃義務約 **$278.99B**（2026 餘年至 2036；年期 >1 至 30）。2026-07 另簽約 **$68B**、預計 2027–28 開始、年期 18–20 年。不可取消合約承諾 **$349.31B**。 |
| Moody’s 引 META FY2025 10-K 原文（本輪以評級稿核對，非代替 10-K 全文） | 見下節 PDF | 「aggregate initial lease commitment is approximately $12.31 billion」；「residual value guarantees (RVG) with an aggregate threshold of approximately $28 billion that decreases over time」；「As of December 31, 2025, RVG payments are not probable and therefore, no liability has been recorded。」 |

**單位核對（非正式載入）：** 同一檔可並列 (i) 已入表租賃負債未折現現金流 (ii) 未開始租賃承諾 (iii) 具名 JV 的初約租金＋RVG 上限＋max exposure。三者不是同一欄，但同檔可對帳。合併槓桿（帳面／市值）與專案 90% LTV 不在同一張 META 負債表上——專案 LTV 在發行人 Beignet 側。

---

## B. 專案側：S&P Beignet／Sopaipilla（評級稿，預售全文 PDF 本輪未取回）

| 源 | URL | 讀到的量 |
|---|---|---|
| S&P rating action：Beignet Investor LLC $27.30B senior notes，初步 **A+** | https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101651795 | Blue Owl 基金經 HoldCo 持 JV 80%；Meta AA-/Stable。發行 $27.30B 攤還票據到期 2049-05。校園 2.064 GW、Richland Parish。承諾建造約 $28.79B。預期營運期 DSCR **平坦 1.12x** 至 2049。RVG：若 Meta 在初約或後續四年租約期後不續租，須補足。本輪對該頁摘要可讀；**完整 pre-sale PDF 未取回**（瀏覽工具回 Insufficient）。 |
| IFR 對 S&P 方法之轉述（二手；只作方法線索） | https://www.ifre.com/people-and-markets/2363199/the-metablue-owl-deal-broken-down-off-balance-sheet-gymnastics-24-years-after-enron | 興建期用「Meta-adjusted」＝AA− 減一檔 → A+；營運期專案法、DSCR 1.12x＋RVG。S&P **不按會計合併**；基準案初只納 **八年** 租金。RVG 覆蓋 16 年；債最後四年改為等同未償餘額之終止費。ASC 842：若續約非 reasonably certain，入表年期可停在四年。 |
| Meta 新聞稿 2025-10-21 | https://about.fb.com/news/2025/10/meta-blue-owl-capital-develop-hyperion-data-center/ | Blue Owl 80%／Meta 20%；開發成本約 $27B（廠房＋長壽電力／冷卻／連線）。Blue Owl 現金出資約 $7B；Meta 一次性分配約 $3B。初約四年＋續約選擇。 |
| Sopaipilla（同構複製品） | PitchBook 2026-07-28 https://pitchbook.com/news/articles/investors-flock-to-12-5b-data-center-bond-deal-for-blackrock-sponsored-sopaipilla | Sopaipilla Investor $12.547B 7.534% 攤還至 2048-11-30；960 MW El Paso；80:20 BlackRock 基金／Meta。S&P A+／Fitch AA-。S&P 稱 RVG「provides strong lender protection」。FT 引 S&P：與 Hyperion「carbon copy」。 |

專案 LTV：S&P 稿給建造承諾與發債額，**未在本輪取回之摘要中寫「90%」**。90% 來自 Van Nieuwerburgh 以 $27B 債／$30B 資產。本輪不把 90% 寫成已從 S&P 原文重算。

---

## C. 加總層：Moody’s 2026-02-23

| 源 | URL | 讀到的量 |
|---|---|---|
| Moody’s Ratings, *Accounting – US: Hyperscalers' reported AI-related lease commitments may understate economic risk*, 2026-02-23, Gonzales／Drake | https://dkf1ato8y5dsg.cloudfront.net/uploads/52/504/1-sector-in-depth-accounting-us-hyperscalers-23feb2026-pbc-1467708.pdf | 五家（AMZN A1 pos、META Aa3、GOOGL Aa2、ORCL Baa2 neg、MSFT Aaa）未折現未來租賃承諾 **$969B**（至 2025-12-31 申報）。其中尚未開始 **$662B**＝當時調整後債務之 **113%**。續約不入負債除非 reasonably certain（>70% 門檻）。RVG 須「不續租 **且** 資產低於契約門檻」兩事件；probable 之前可不入負債。硬體經濟壽命 4–6 年被用來主張續約非 reasonably certain。 |

2026-07 Moody’s 後續評論（CNBC 2026-07-24）把承諾上修至約 $1.2T、未開始約 $820B——**本輪不以二手數字覆蓋 02-23 原文**。WSJ $2.4T 表外為 Van Nieuwerburgh 轉述，本輪未取 WSJ 原表。

---

## D. 論文其餘數字本輪不測

不測：$10.3T／3.63% GDP、回本 $3.73T、$5.5／GPU-小時、REIT β、NVIDIA $500B 信貸＋25% RVG。後者若測，應走 L13-I 種子（供應商兼保證人），B 端須 NVIDIA／融資文件，本輪未 fetch。

---

## E. 對 SCOUT 的邊界（非指示部位）

1. 本楔可觀測。META 同檔已分列未開始租、具名 JV 初約、RVG 上限、max exposure；S&P 給專案評級與 DSCR；Moody’s 給五家加總。  
2. 3h L13-A 種子不是這個量。若要把本楔寫進漏斗，須**新生成或改寫 L13-A**，不得宣稱 3h L13-A 已覆蓋。  
3. 不得用本楔重開 C-A4（`k`／窗）。  
4. 不得與 L6-A 合併：一個是交付容量比，一個是義務入表時點。  
5. L13-I 可另測循環保證（NVIDIA／Broadcom）；本卡不是該測。  
6. S&P pre-sale 全文 PDF、META 10-K 租賃附註原頁、Beignet 144A OM 本輪缺。缺段不得作存在性主張以外的精算（CHARTER §7-2）。

**§7-10：** 領域最近公開＝META 10-Q 期 2026-06-30（2026-07-30 入檔）；Sopaipilla 定價 2026-07-27；Moody’s 會計評 2026-02-23。下一官方檢查點＝META 下期 10-Q／10-K 是否仍分列 Venture max exposure、未開始租、RVG「not probable」。
