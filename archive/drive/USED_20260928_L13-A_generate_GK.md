# L13-A 生成卡｜資本與融資結構：未開始租＋RVG＋專案槓桿 vs 合併槓桿
<!-- BY: SCOUT@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | NOTE: 改寫 3h L13-A 種子；舊種子（關係人營收加總）未測、可回復、不進本卡測試一 | CONSUMES: 1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1xlw2ZAI7S8HGz1m3jntqWNAg_jHZOSZi；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi；10aH5MscncgySFaJadvJsX3z0OXviAie_；1Pm249SbDe6OUmA3RXYdqt-O_PrC9pj_z | EMITS: （上傳 work/ 後回填） -->
**日期：** 2026-09-28　**角色：** SCOUT@GK　**格：** L13-A　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 本輪只產改寫後生成卡。不測。不改 FUNNEL／matrix／INDEX／ARCH_dead／ARCH_3h。不入 §1。不重開 C-A4。不把 T-15 改寫成空方。B 端只指名可重算欄，不宣稱可分離、不寫 H1。

---

## 0. 本輪範圍與改寫理由

- **3h 原文 L13-A**（`1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj`，快照不可更新）：循環交易營收重複＝產業合計揭露營收 − 產業合計對外營收（關聯方交易加總）。B 端指名＝關係人交易附註。重疊標 C-A6（(b) 欄缺主體）。
- **3h 原文 L13-I**：供應商同時為股東與債權人 → 公開信評資訊含量下降。B 端指名＝股權投資餘額 vs 應收帳款帳齡。
- **3h 原文 L13-P**：GPU 熱循環壽命（B 端指名失敗，先歸 (a)）。
- **來源對帳** work `1xlw2ZAI7S8HGz1m3jntqWNAg_jHZOSZi`：未開始租＋RVG＋專案債 vs 合併槓桿，在 META 10-K／10-Q **同檔可重算**、與合併槓桿分列；≠ L6-A、≠ C-A4、≠ 3h L13-A；L13-I 相鄰不是同一式。
- **改寫而非另測 L13-I：** 本楔是承租方義務**入表時點**與專案／合併槓桿分列（會計恆等＝[A]）。L13-I 是供應商兼股東／債權人／保證人時，公開信評資訊含量（誘因／資訊＝[I]）。把 NVIDIA／Broadcom 循環保證塞進 L13-I 測的是另一條種子，**不能覆蓋本楔**。L13-I 維持 3h 原文，本輪不生成、不測。
- **舊 L13-A 種子處置：** 未測、不丟棄（3h 第 5 條：重疊不構成丟棄）。停在 3h 快照。本卡測試一不得改測關係人營收加總。回復觸發＝產業合計揭露營收與對外營收可在強制關係人附註對出加總差，且與本楔入表欄可分列。
- **已死／相鄰、不得合併、不得重開：**
  - **C-A4**（ARCH_dead #4，L13）：融資／續約單價比 `k`；死因＝重定價窗與觀測時序不相容。複查＝P2 窗可重推至覆蓋 M-6（2027-10-31）**且** `k` 可反解。本楔不使用 `k`，不主張窗覆蓋 M-6。觸發器未滿足。
  - **C-A3**（#5，L6）：與 C-A4 共用樞紐。本楔不是折舊年限。
  - **L6-A**（生成 `10aH5MscncgySFaJadvJsX3z0OXviAie_`；測一 `1Pm249SbDe6OUmA3RXYdqt-O_PrC9pj_z`）：`R＝已簽約未交付／已交付` 領先營收；房東／雲側容量時序。本楔是承租 hyperscaler 義務入表時點。
  - **T-15**：委託資本外，非殺。本格可指名該主體揭露；不得改寫成空方、不得選券。
- CHARTER §7-3：不執行終端篩選。§7-4 三題只標「轉入個股層時必問」。§7-10：領域最近公開＝META 10-Q 期 2026-06-30（2026-07-30 入檔，acc `0001628280-26-050705`）；Sopaipilla 定價 2026-07-27；Moody’s 會計評 2026-02-23。下一官方檢查點＝META（或同構 hyperscaler）下期 10-Q／10-K 是否仍分列未開始租、具名 JV 初約、RVG「not probable」、Venture max exposure。

---

## 1. 落差一句（改寫後生成物）

市場把 hyperscaler 槓桿讀成合併負債表上的已入表租賃負債＋有息債。種子主張：同一主體 10-K／10-Q 已分列（i）已入表未折現租賃現金流（ii）尚未開始之租賃承諾（iii）具名 JV 初約＋RVG 上限＋max exposure；專案側評級稿另給建造承諾與發債額／DSCR。錯價只在把「已入表租賃負債」當成經濟義務上界，或把專案 高 LTV 當成已在合併表上的同一欄。C-A4 死在 `k` 與窗；本格 B 端不是那一列。

---

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（入表時點＋表外承諾分列）；不是純物理上界、不是信評資訊含量 |
| 選擇者 | 承租方續約是否 reasonably certain（ASC 842）；RVG 是否 probable；專案是否合併 |
| 可見端 | 同一 10-K／10-Q 之租賃附註＋承諾／或有事項＋權益法／VIE max exposure；評級稿之專案 DSCR／發債額／RVG 描述 |
| 指名不可見端 | 單一可單位化連續參數把「未開始租＋RVG 上限 − 已入表租賃」寫成 H1 倍數窗；專案 LTV 在發行人側與承租人合併表之官方對帳列 |
| 主張 | 未開始租＋RVG（not probable）上升，而已入表租賃負債不變，不蘊含經濟義務上界不變 |
| 表達工具型態（只指名，不選券） | 已上市、美股可交易、10-Q 分列未開始租／RVG／JV exposure 之 hyperscaler。不選券 |
| 重疊 | L6-A 交付容量比；L13-I 循環保證／信評資訊；C-A4 之 `k`／窗。重疊不構成丟棄 |

恆等式（生成用，非正式載入）：

`Obl_onbook_t = PV 或未折現已入表租賃現金流_t`

`Obl_uncomm_t = 尚未開始租賃承諾_t`（附註明文「leases not yet commenced」或等價）

`RVG_cap_t = 殘值保證契約上限_t`（probable 之前可不入負債）

`Exp_JV_t = 具名 Venture max exposure_t`（權益帳面＋租賃承諾＋估計後續出資＋RVG 上限；與前兩項部分重疊，不得三欄相加當獨立義務）

`Lev_proj` 在發行人評級稿（建造承諾、發債額、DSCR）；`Lev_consol` 在承租人合併表。本輪不把「90% LTV」寫成已從評級稿重算。

**禁止：** `Obl_uncomm + RVG_cap + Exp_JV` 直接加總（重疊）；用 Moody’s 五家加總代替單主體分列；用 Van Nieuwerburgh／WSJ 表外總額代替附註原列。

---

## 3. 已 fetch 之公開錨（來源對帳已讀；本卡不重算）

以下只證明「指名載體存在且近期仍更新、同檔可並列」。**不宣稱已完成測試一，不宣稱可單位化，不宣稱市場錯價。** 數字引用對帳卡 `1xlw2ZAI7S8HGz1m3jntqWNAg_jHZOSZi`，缺段不得加精算。

1. META FY2025 10-K 租賃附註（edgar.tools 摘；申報 2026-01-29）：已入表未折現營運＋融資租賃現金流與「尚未開始」營運＋融資租賃義務分列；尚未開始多為資料中心／主機代管／網路，2026–2030 開始。此表不含 RVG。https://app.edgar.tools/companies/META/disclosures/leases
2. META 10-Q 期 2026-06-30 acc `0001628280-26-050705`：路易斯安那校園 Venture 持股 20%；租約 2029 開始；初約承諾、權益投資帳面、對該 Venture 之 maximum exposure to loss、尚未開始租賃義務、其後另簽約承諾、不可取消合約承諾——同檔分列。https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm
3. Moody’s 引 META FY2025 10-K：aggregate initial lease commitment；RVG aggregate threshold；「As of December 31, 2025, RVG payments are not probable and therefore, no liability has been recorded.」（對帳卡以評級稿核對，非代替 10-K 全文。）
4. S&P rating action：Beignet Investor LLC senior notes 初步 A+；Blue Owl 基金經 HoldCo 持 JV 80%；預期營運期 DSCR；RVG 在初約或後續四年租約期後不續租須補足。完整 pre-sale PDF 對帳輪未取回。https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101651795
5. Meta 新聞稿 2025-10-21：Blue Owl 80%／Meta 20%；初約四年＋續約選擇。https://about.fb.com/news/2025/10/meta-blue-owl-capital-develop-hyperion-data-center/
6. Sopaipilla 同構：PitchBook 2026-07-28 轉述定價與評級；FT 引 S&P 稱與 Hyperion carbon copy。https://pitchbook.com/news/articles/investors-flock-to-12-5b-data-center-bond-deal-for-blackrock-sponsored-sopaipilla
7. Moody’s 2026-02-23 *Hyperscalers' reported AI-related lease commitments may understate economic risk*：五家未折現未來租賃承諾中尚未開始佔調整後債務比重；續約不入負債除非 reasonably certain；RVG 須「不續租且資產低於契約門檻」兩事件。加總層，不得代替單主體分列。https://dkf1ato8y5dsg.cloudfront.net/uploads/52/504/1-sector-in-depth-accounting-us-hyperscalers-23feb2026-pbc-1467708.pdf

缺段（CHARTER §7-2）：S&P pre-sale 全文 PDF、META 10-K 租賃附註原頁、Beignet 144A OM。專案「90% LTV」來自論文資產／債比，對帳輪未在 S&P 摘要重算，測試一不得寫成已從評級稿得出。

---

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | 未開始租是承諾不是負債；ASC 842 在 commencement 才入表。分列存在 ≠ 市場把已入表負債當成經濟上界 | ASC 842；META 租賃附註結構 | 測試一可能停在「可觀測但無錯價載體」 |
| R2 | RVG 入表要「不續租且資產低於門檻」且 probable；管理層寫 not probable 期間，欄位是上限不是期望損失 | META／Moody’s RVG 段 | `RVG_cap` 不能當義務存量 |
| R3 | `Exp_JV` 已含租賃承諾＋RVG＋出資，與 `Obl_uncomm`、`RVG_cap` 重疊；三欄相加高估 | META 10-Q max exposure 定義 | 無單一不重疊連續參數 |
| R4 | 專案 LTV／DSCR 在發行人（Beignet／Sopaipilla），不在承租人合併表；評級方法「不按會計合併」 | S&P 稿；IFR 轉述 | `Lev_proj` 與 `Lev_consol` 不可在同一張表相減 |
| R5 | 硬體經濟壽命 4–6 年被用來主張續約非 reasonably certain——這是入表規則的輸入，不是隱匿 | Moody’s 2026-02-23 | 「表外」可能是規則結果而非漏列 |
| R6 | 滑向 `k`／續約單價或窗覆蓋 M-6＝重開 C-A4；滑向交付 MW 比＝併入 L6-A；滑向 NVIDIA 保證＝改測 L13-I | ARCH_dead #4；L6-A 測一；3h L13-I | 表達點選錯＝換格，不是本格通過 |

種子仍可能在「同一主體、同一張 10-Q，同時出現已入表租賃現金流、未開始租、RVG 上限或 not probable 陳述、具名 JV max exposure，且可畫至少兩期」上寫成可重算對照。五家加總與論文表外總額不夠。

---

## 5. SCOUT 裁決

**改寫 L13-A 並留。** 不進 T。不測 L13-I。不重開 C-A4。下一動作＝ANALYST@GK 對**改寫後**本格做測試一。

理由（只到殺／留／改寫）：
- 楔可陳述，層正確（資本與融資結構／會計入表），與 3h 舊 L13-A、L13-I、L6-A、C-A4 不同構。
- 另測 L13-I 循環保證不能承載本楔；會把 [A] 量寫進 [I] 格。
- 舊種子未否證、未測；停在 3h，不進本卡 B 端。
- R1–R5 足夠強，預設風險＝可觀測但三欄重疊、RVG 是上限、專案槓桿不在合併表、入表規則被誤讀成隱匿；不是機制已被否證。
- 終端三題本階段不答（§7-3）。

否決觸發（寫給 ANALYST，不是本輪執行）：
- 實讀後無法在同一主體 10-K／10-Q 並列未開始租與已入表租賃，只剩五家加總或論文表外總額；或
- 可運作對照只能寫成續約單價比 `k` 或窗覆蓋 M-6（滑回 C-A4）；或
- 可運作對照只能寫成已簽約未交付／已交付容量比（滑向 L6-A）；或
- 可運作對照只能寫成供應商股權投資 vs 應收帳齡或供應商 RVG 資訊含量（滑向 L13-I）；或
- 公開層已穩定可拒絕「未開始租＋not-probable RVG 只是 ASC 842 時序，與合併槓桿讀法不可辨」。

複查觸發器（若日後殺）：任一美股可交易 hyperscaler 於 10-K／10-Q／20-F 同檔分列未開始租賃承諾、已入表租賃現金流、RVG 上限或 probable 判定、具名 JV max exposure，且可畫至少兩個報告期。

舊種子回復觸發：產業合計揭露營收 − 對外營收可在強制關係人附註對出，且與本楔入表欄分列。

---

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：未開始租、RVG、JV exposure 能否拒絕重疊加總；專案發債是否出現在承租人合併表或只在發行人。
2. 可交易工具：恆等落在美股可交易 hyperscaler 揭露，而非僅 144A 發行人或無申報之基金 HoldCo。
3. 半衰期：commencement 批次入表、或管理層改口 RVG probable、或續約改判 reasonably certain 之後，≥12 個月窗內「表外存量」是否消失。

---

## 7. 本輪寫入／不寫入

寫入：本生成卡入 Drive `work/`（fileId 見標頭 EMITS，上傳後回填）。
不寫入：FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（§3 L13 仍依 matrix＝已生成；不入 §1）；matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`；INDEX.json；ARCH_dead；ARCH_3h（快照不可更新）。禁止新建同名正本。狀態欄對齊屬測試一之後 session。
L13-I／L13-P 本輪不生成。
