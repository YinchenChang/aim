<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 13jTlzo75O0uyuq1D-D-FM3Nz7zFG7DDI；1xlw2ZAI7S8HGz1m3jntqWNAg_jHZOSZi；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi；10aH5MscncgySFaJadvJsX3z0OXviAie_；1Pm249SbDe6OUmA3RXYdqt-O_PrC9pj_z | EMITS: PENDING_UPLOAD -->
# L13-A 測一｜B 端實讀（同一主體 10-K／10-Q 已入表租賃 vs 未開始租 vs RVG／JV exposure；評級稿專案槓桿分列）

**角色：** ANALYST@GK　**日期：** 2026-09-28　**格：** L13-A（資本與融資結構：未開始租＋RVG＋專案槓桿 vs 合併槓桿）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先同一主體 10-K／10-Q 同檔分列（i）已入表租賃現金流／負債（ii）尚未開始租賃承諾（iii）具名 JV 初約＋RVG 上限或 not probable＋max exposure；次為發行人評級稿之建造承諾／發債額／DSCR，**僅當**能與承租人合併表分列。**禁止**只重讀五家加總、論文／WSJ 表外總額、關係人營收加總（舊 3h L13-A）、續約單價比 `k`（C-A4）、已簽約未交付／已交付容量比（L6-A）、供應商股權 vs 應收帳齡（L13-I）。不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T、不入 §1。不重開 C-A4。不把 T-15 改寫成空方。不選券。
**原陳述（改寫生成卡 `13jTlzo75O0uyuq1D-D-FM3Nz7zFG7DDI`）：** 市場把 hyperscaler 槓桿讀成合併負債表上的已入表租賃負債＋有息債。同一主體申報已分列未開始租、RVG（probable 前可不入負債）、具名 JV max exposure；專案側評級稿另給建造承諾與發債額／DSCR。錯價只在把已入表租賃負債當成經濟義務上界，或把專案高 LTV 當成已在合併表上的同一欄。
**對照式（生成用，非正式載入）：** `Obl_onbook`＝已入表租賃（PV 或未折現現金流）；`Obl_uncomm`＝leases not yet commenced；`RVG_cap`＝殘值保證上限（not probable 則不入負債）；`Exp_JV`＝具名 Venture max exposure（權益帳面＋租賃承諾＋估計後續出資＋RVG 上限，與前兩項部分重疊，不得三欄相加）。`Lev_proj` 在發行人評級稿；`Lev_consol` 在承租人合併表。本輪不寫 H1。
**否決觸發（生成卡寫給本輪）：** (1) 實讀後無法在同一主體 10-K／10-Q 並列未開始租與已入表租賃，只剩五家加總或論文表外總額；或 (2) 可運作對照只能寫成 `k` 或窗覆蓋 M-6；或 (3) 只能寫成已簽約未交付／已交付容量比；或 (4) 只能寫成供應商股權 vs 應收帳齡或供應商 RVG 資訊含量；或 (5) 公開層已穩定可拒絕「未開始租＋not-probable RVG 只是 ASC 842 時序，與合併槓桿讀法不可辨」。
**領域最近公開（§7-10）：** META 10-Q 期 2026-06-30 acc `0001628280-26-050705`（2026-07-30 入檔）；META 10-Q 期 2026-03-31 acc `0001628280-26-028526`；META FY2025 10-K acc `0001628280-26-003942`（2026-01-29）；Moody’s 會計評 2026-02-23；Sopaipilla 定價 2026-07-27。下一官方檢查點＝任一美股可交易 hyperscaler 下期 10-Q／10-K 是否仍同檔分列未開始租、已入表租賃、RVG 上限或 probable 判定、具名 JV max exposure，且可畫至少兩期。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：HEALTH_CL `1_urT6I7RovcM73D3IBTKGIk6RY1z9nC0`；L6-A generate `10aH5MscncgySFaJadvJsX3z0OXviAie_`；L6-A test1 `1Pm249SbDe6OUmA3RXYdqt-O_PrC9pj_z`；FUNNEL_body `1COi9kgtSAZTzYRzSr63w1vOoscC7CoCd`；ARCH_matrix_body `136fikdjqjDRFNir9-ZUF_BqcNZ9bfbtH`；INDEX_body `1OOXQ43htBDrX1bU-Tce9wqEyXUQ5Tago`；L13-A generate `13jTlzo75O0uyuq1D-D-FM3Nz7zFG7DDI`（13088 B，2026-09-28T09:30:21Z）；L13 VN source `1xlw2ZAI7S8HGz1m3jntqWNAg_jHZOSZi`；`DUP_PLACEHOLDER_L1-I_test1_do_not_use` `1lci-pu8ekOI7T-za2Sl93q-j1GUoNAjl`
- query/：ARCH_dead `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`；ARCH_matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`（L13［A］＝已生成）；CHARTER_HIST `1DKg3HUr-zOWw20OmNe1aDpWT_izDwdiT`；INDEX `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`；MECH `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-09-28T10:20:32Z role SCOUT）
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-09-28；§1 無 L13-A；§3 其餘層依 matrix）
- 本輪上傳前 work/ exact_name `20260928_L13-A_test1_GK.md` 空；無內容相近測一
- work 主動維護：L13-A 生成卡未吸收進 FUNNEL／matrix（待本測一後由 SCOUT 對齊）。L6-A 兩檔狀態已入 FUNNEL §3／matrix，本輪不建 `DONE_`（單一 session 配額留給結案標記；body 三檔與 HEALTH／DUP 非本輪標的）。無檔名／fileId 自報衝突須發 HEALTH。

---

## 終態

**測一通過（可觀測／可並列）｜不進 T。** 指名 B 端在同一美股可交易主體之 10-K／10-Q **成立**：已入表營運租賃負債、尚未開始租賃承諾、具名 Venture 初約／RVG 上限／not probable／max exposure 可在同檔或同發行人相鄰附註並列，且未開始租可畫 **三個** 報告日。機制（入表時點＋表外承諾分列）未被否證。否決 (1)–(4) 未觸發。不進 T：R1（分列存在 ≠ 市場把已入表負債當成經濟上界）未解；R2（`RVG_cap` 是上限不是期望損失）；R3（`Exp_JV` 已含租賃承諾＋RVG＋出資，三欄不可加）；R4（`Lev_proj` 在 Beignet／Sopaipilla 發行人，不在 META 合併表，不可同表相減）；無單一不重疊連續參數可寫 H1 倍數窗。無 H1。§7-4 三題本輪不答。

與相鄰格：對照不是 `k`／M-6（C-A4 未滑回）；不是交付 MW 比（L6-A 未併入）；不是供應商股權／帳齡或供應商保證資訊含量（L13-I 未改測）；舊 3h L13-A 關係人營收加總未進本輪 B 端。

---

## A. 指名 B 端：同一主體已入表 vs 未開始租 vs RVG／JV（實讀）

| 源 | URL | 本輪讀到的量 |
|---|---|---|
| META FY2025 10-K acc `0001628280-26-003942` 本文 | https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm | 租賃附註（XBRL 摘同檔 R16）＋非上市權益／Venture 段：已入表未折現營運 $33.508B／融資 $1.504B；PV 營運 $25.153B（流動 $2.213B＋非流動 $22.940B）／融資 $1.184B。**尚未開始**營運＋融資租賃義務約 **$103.77B**（資料中心／主機代管／網路；2026–2030 開始；年期 >1 至 30）。路易斯安那 Venture 持股 20%；租約 2029 開始；初約約 **$12.31B**；RVG 合計門檻約 **$28B**（隨時間下降）；「As of December 31, 2025, RVG payments are not probable and therefore, no liability has been recorded。」對該 Venture **maximum exposure to loss $45.95B**＝權益帳面 $1.83B＋租賃承諾＋估計後續出資＋RVG 上限 |
| META 10-K 租賃 XBRL 表 R16 | https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/R16.htm | 上列到期表原文。表註：不含 commencement／修改時尚未固定之付款。尚未開始義務與到期表分列 |
| META 10-K 租賃摘（edgar.tools；對 10-K 原文） | https://app.edgar.tools/companies/META/disclosures/leases | 與 R16／10-K 同數。此摘**不含** RVG（RVG 在權益法／Venture 附註，不是租賃到期表） |
| META 10-Q 期 2026-03-31 acc `0001628280-26-028526` | https://www.sec.gov/Archives/edgar/data/1326801/000162828026028526/meta-20260331.htm | 營運租賃負債流動 $2.414B＋非流動 $25.607B（2025-12-31 $2.213B＋$22.940B）。尚未開始約 **$182.88B**（餘 2026 至 2036）。Venture 權益帳面 $2.37B／$1.83B；max exposure **$45.99B**／$45.95B。初約 $12.31B、RVG 門檻 $28B、not probable、無負債——與年報同文 |
| META 10-Q 期 2026-06-30 acc `0001628280-26-050705` | https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm ；index https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705-index.html | 營運租賃負債流動 $2.425B＋非流動 $26.229B；長期有息債帳面 $83.664B（面額 $84.00B）。尚未開始約 **$278.99B**（餘 2026 至 2036；年期 >1 至 30）。2026-07 另簽約 **$68B**（2027–28 開始；18–20 年）＝期後，不併入期末 $278.99B。Venture 權益 $2.92B／$1.83B；max exposure **$46.03B**／$45.95B。初約 $12.31B、RVG $28B、not probable。其他未合併 VIE max exposure $6.41B／$5.58B（帳面投資，**不是**本楔 Venture 欄）。不可取消合約承諾 $349.31B（雲容量／伺服器／資料中心／RL；**不是**未開始租）。期後 Note：El Paso 校園排他協議、擬持股 20%、擬貢獻待售資產約 $2.3B、擬收分配約 $1B、RVG 最大曝險約 **$13B**——同構複製品已進同檔，惟「subject to definitive agreements」 |
| Moody’s 2026-02-23 引 META 10-K／10-Q 原文 | https://dkf1ato8y5dsg.cloudfront.net/uploads/52/504/1-sector-in-depth-accounting-us-hyperscalers-23feb2026-pbc-1467708.pdf | 核對 META 初約 $12.31B、RVG 門檻 $28B、not probable 無負債。五家未折現未來租賃承諾 $969B、尚未開始 $662B＝調整後債務 113%。「reasonably certain」＞70%；RVG 須不續租**且**資產低於門檻兩事件。硬體經濟壽命 4–6 年被用來主張續約非 reasonably certain。**加總層不得代替單主體分列**；本輪通過條件只用 META 原列 |

**單位核對（非正式載入；只證明可重算）：**

| 報告日 | 已入表營運租賃負債 PV | 尚未開始租賃承諾 | Venture max exposure | RVG 門檻／入表 |
|---|---|---|---|---|
| 2025-12-31 | $25.153B | $103.77B | $45.95B | $28B／not probable、無負債 |
| 2026-03-31 | $28.021B | $182.88B | $45.99B | $28B／not probable、無負債 |
| 2026-06-30 | $28.654B | $278.99B | $46.03B | $28B／not probable、無負債 |

融資租賃：年報 PV $1.184B、未折現 $1.504B；兩份 10-Q 面表未單列融資租賃負債（ROU 在 PPE：2026-06-30 總額 $9.467B），本輪不把 ROU 總額寫成負債 PV。`Obl_uncomm / 營運租賃 PV` 三期約 4.1 → 6.5 → 9.7——**不是 H1**，且分子含將 commence 之 Venture 租約，與 `Exp_JV` 重疊。

---

## B. 專案側：發行人評級稿 vs 承租人合併表（實讀）

| 源 | URL | 本輪讀到的量 |
|---|---|---|
| S&P presale HTML：Beignet Investor LLC | https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/3469376 | 建造承諾 **$28.79B**；HoldCo 發債 **$27.30B** 到期 2049-05；Blue Owl 基金經 HoldCo 持 80%（出資 $23.03B）、Meta 成員 20%（建造出資 $5.76B）。發行人來源／用途表把建設債與權益分列。評級 **A+**。本輪對該 HTML 以搜尋摘錄讀到上列；先前 rating-action 頁 `sourceId/101651795` 本輪瀏覽回 Insufficient，不以該頁作新數字 |
| IFR 對 S&P 方法之轉述（二手；只作方法線索） | https://www.ifre.com/people-and-markets/2363199/the-metablue-owl-deal-broken-down-off-balance-sheet-gymnastics-24-years-after-enron ；獎項稿 https://www.ifre.com/ifr-awards/2327933/financing-package-blue-owl-capitalbeignet-investors-us27.3bn-23.6-year-bond | 興建期「Meta-adjusted」＝AA− 減一檔 → A+；營運期專案法、DSCR **1.12x**＋RVG。S&P **不按會計合併**。基準案初約年期短於債到期；RVG 覆蓋後債末四年改終止費＝未償餘額。144A／Reg S，$27.3B、6.581%、2049-05 |
| Meta 新聞稿 2025-10-21 | https://about.fb.com/news/2025/10/meta-blue-owl-capital-develop-hyperion-data-center/ | Blue Owl 80%／Meta 20%；開發成本約 $27B；Blue Owl 現金約 $7B；Meta 一次性分配約 $3B。初約四年＋續約；RVG 涵蓋營運前 16 年 |
| Sopaipilla 同構（PitchBook 2026-07-28） | https://pitchbook.com/news/articles/investors-flock-to-12-5b-data-center-bond-deal-for-blackrock-sponsored-sopaipilla | Sopaipilla Investor $12.547B 攤還至 2048-11-30；960 MW El Paso；80:20 BlackRock 基金／Meta。S&P A+。FT 引 S&P：與 Hyperion carbon copy。META 10-Q 期後 Note 之 El Paso 排他＋RVG ~$13B 與本條同構，惟 10-Q 仍寫「subject to definitive agreements」 |

**禁止寫成已重算：** 「90% LTV」本輪未在 S&P 原文讀到該詞。評級稿給建造 $28.79B 與發債 $27.30B，二者比不是承租人合併槓桿，也不是 `Obl_uncomm`。不得把 $27.30B 加進 META 長期債 $83.664B。

---

## C. 本輪明確不讀、不引用為通過條件

- 舊 3h L13-A：產業合計揭露營收 − 對外營收／關係人附註加總。
- C-A4：`k`、窗覆蓋 M-6。
- L6-A：已簽約未交付／已交付 MW 或 RPO 總額。
- L13-I：NVIDIA／Broadcom 股權投資 vs 應收帳齡、供應商 RVG 資訊含量。
- Moody’s 五家 $969B／$662B、CNBC／WSJ／Van Nieuwerburgh 表外總額——只作加總層反例，不代替單主體分列。
- 144A OM 全文、S&P pre-sale PDF 原檔（HTML 摘可用；PDF 本輪未取回）。
- 把 2026-07 另簽 $68B 與期末 $278.99B 加成「同一報告日官方存量」。
- 把其他 VIE max exposure $6.41B 併入 Louisiana Venture 欄。
- 把不可取消合約承諾 $349.31B 寫成未開始租。

---

## 對 R1–R6 之測一處分（不寫 H1）

| # | 反方 | 本輪 |
|---|---|---|
| R1 | 未開始租是承諾不是負債；分列存在 ≠ 市場把已入表負債當成經濟上界 | **成立為錯價主張。** 測一只證明分列可觀測、可畫三期。入表規則自己寫 commencement 才入表。不進 T |
| R2 | RVG 入表要兩事件且 probable；not probable 期間欄位是上限 | **成立。** 三期原文均「not probable…no liability」。`RVG_cap` 不得當義務存量 |
| R3 | `Exp_JV` 已含租賃承諾＋RVG＋出資，與 `Obl_uncomm`、`RVG_cap` 重疊 | **成立。** 10-Q 自定義 max exposure＝四項合計。無單一不重疊連續參數 |
| R4 | 專案 LTV／DSCR 在發行人，評級方法不按會計合併 | **成立。** Beignet $27.30B／建造 $28.79B 與 META 合併債 $83.664B＋營運租賃 PV $28.654B 不可同表相減 |
| R5 | 硬體 4–6 年壽命用來主張續約非 reasonably certain＝規則輸入不是隱匿 | **成立為解讀風險。** Moody’s 原文即此論。測一不把「表外」寫成漏列 |
| R6 | 滑向 `k`／L6-A／L13-I＝換格 | **未觸發。** 本輪對照停在入表時點與分列欄 |

否決 (5) 未寫死：公開層可拒絕的是「未開始租應已入負債」（與 ASC 842 原文相反），不是「四欄不可辨」。四欄可辨；錯價未證。

---

## 轉入個股層時必問（§7-4，本輪仍不答）

1. 財報科目：未開始租、RVG、JV exposure 能否拒絕重疊加總；專案發債是否出現在承租人合併表或只在發行人。
2. 可交易工具：恆等落在美股可交易 hyperscaler 揭露，而非僅 144A 發行人或無申報之基金 HoldCo。
3. 半衰期：commencement 批次入表、或管理層改口 RVG probable、或續約改判 reasonably certain 之後，≥12 個月窗內「表外存量」是否消失。

---

## 本輪寫入／不寫入

寫入：本測一入 Drive `work/`（fileId 見標頭 EMITS，上傳後回填）。
不寫入：FUNNEL 正本、matrix、INDEX、ARCH_dead、CHARTER、ARCH_3h。禁止新建同名正本。狀態欄對齊屬下一 SCOUT session。
