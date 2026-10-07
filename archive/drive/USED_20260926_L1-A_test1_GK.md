<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1vDVDa87K0rnSqeTBcrhQ8OjeeOHOIAaj；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h | EMITS: （本檔；Drive work/ 上傳後填 fileId） -->
# L1-A 測一｜B 端實讀（鎖定 $/MWh 與現貨／關稅 $/MWh 能否同主體、同窗對帳）

**角色：** ANALYST@GK　**日期：** 2026-09-26　**格：** L1-A（能源與電力：已鎖定電價恆等式；PPA−現貨＝存量）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先鎖定 `$/MWh` 與現貨／關稅 `$/MWh` 能否同主體、同窗對帳。**禁止只疊 PPA MW 公告或 utilities 總額。** 不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T、不入 §1。
**原陳述（生成卡 `1vDVDa87K0rnSqeTBcrhQ8OjeeOHOIAaj`）：** 市場把資料中心電費讀成隨現貨或零售關稅重定價的流量。種子主張：`C = MW × LF × p × 8760` 在 `p` 已由 PPA（或同等長期合約）鎖定之後，`(p_PPA − p_spot)` 乘上剩餘約定量是一個存量。錯價只在把「電力緊張」譯成營運商損益的可變電費，而不是已鎖定差的存量與未鎖定殘差。B 端對照＝公用事業／發電商 PPA 揭露，以及營運商能源成本分列。
**對照式（生成用）：** `S_lock(t) = (p_PPA − p_spot(t)) × Q_remain(t)`；`p(t) = ω_lock · p_PPA + (1 − ω_lock) · p_spot`。本輪不估參數、不寫 H1。
**否決觸發（生成卡寫給本輪）：** (1) 對 10-K／10-Q／20-F／關稅或 PPA 附註實讀後，`p_PPA` 與 `p_spot` 無法從公開項分離，只剩 MW、年期、utilities 總額；或 (2) 可見電費幾乎全數轉嫁，未鎖定殘差無法在美股可交易主體上寫成獨立存量；或 (3) 公開層已出現穩定可拒絕之 `S_lock`，方向與「鎖定差為存量、非流量衝擊」不可辨，或只能用 T-11 已排除之設備／物理敘事翻號解釋。
**領域最近公開（§7-10）：** Equinix Q2 2026 10-Q（截止 2026-06-30，acc `0001101239-26-000147`）；Digital Realty FY2025 10-K（截止 2025-12-31，申報 2026-02-14）與 Q2 2026 補充／10-Q 窗（營運報表至 2026-06-30）；Vistra Q2 2026 10-Q（截止 2026-06-30，acc `0001692819-26-000019`，申報 2026-08-07／08-10）；Constellation Q2 2026 10-Q（截止 2026-06-30）；New Era／Luminant 8-K（2026-09-21，acc `0001213900-26-101642`）。下一官方檢查點＝任一美股可交易資料中心營運商或發電商 10-K／10-Q／20-F 首次把「已鎖定 PPA 成交單價」與「殘差現貨／關稅單價」分列成可畫至少兩期之差或剩餘約定量美元。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260926_L1-A_generate_GK.md` `1vDVDa87K0rnSqeTBcrhQ8OjeeOHOIAaj`（11893 B，2026-09-26T12:38:09Z）；`20260923_HEALTH_CL.md` `1_urT6I7RovcM73D3IBTKGIk6RY1z9nC0`；`20260923_HEALTH_GK.md` `1byQGbjCmIT1orLv51moyAH5xnABFO95e`
- query/：`ARCH_dead.md` `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`；`ARCH_matrix.md` `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`（L1［A］＝已生成）；`CHARTER_HIST.md` `1DKg3HUr-zOWw20OmNe1aDpWT_izDwdiT`；`INDEX.json` `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`（無 L1-A 測一鍵）；`MECH.md` `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-09-26T12:35:13Z role SCOUT）
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-09-26；§1 無 L1-A；§3 未生成格由 matrix 代理，L1［A］＝已生成＝3h 快照）
- 3h 快照 `1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj` L1-A B 端僅指名「公用事業 PPA 揭露；業者能源成本分列」
- 本輪上傳前 work/ 無同名 `20260926_L1-A_test1_GK.md`、無內容相近測一（Drive exact_name 空）
- work 主動維護：L1-A 生成卡未吸收進 FUNNEL／matrix（待本測一後由 SCOUT 對齊）。HEALTH 兩份非本輪標的。本輪不建 `DONE_`。

---

## 終態

**不通過。不進 T。** 機制（鎖定單價與現貨之差為存量；把電費當流量重定價會把已鎖定量誤讀成季頻成本衝擊）未被否證。失敗在可觀測性——發電商給的是 MW／年期／交貨窗＋樞紐 ATC `$/MWh`（明文「不一定是已實現價」）；營運商給的是 utilities 美元總額與 tenant reimbursements — utilities。**無**已鎖定 PPA 成交 `$/MWh`，故**無**可與同主體、同窗現貨／關稅 `$/MWh` 對帳之 `p_PPA`，故**無**可畫之 `S_lock(t)`。第三方盤點（MLQ 2026-07-17）62／62 協議可用公開單價＝0，與本輪四家主體＋一件 8-K 一致。

| 測試項 | 結果 |
|---|---|
| B 端已實讀（非指名；非只疊 PPA MW／utilities 總額） | **通過**　EQIX Q2 2026 10-Q＋IR 簡報＋2025 年報 PPA 句；DLR FY2025 10-K＋Q2 2026 補充表；VST Q2 2026 10-Q；CEG Q2 2026 10-Q＋Q2 簡報／99.1；NUAI 8-K 2026-09-21；MLQ 盤點 |
| `p_PPA` 與 `p_spot`／關稅 `$/MWh` 同主體、同窗可對帳 | **不通過**　無成交 `p_PPA`。樞紐 ATC／零售關稅不是合約單價 |
| `S_lock(t)`＝差 × 剩餘約定量可成時序 | **不通過**　分子不存在。至少兩期之差序列不存在 |
| utilities 總額或 PPA MW 可否代替 `S_lock` | **否**　量綱不同。禁止把 YoY utilities 或已簽 MW 寫成存量 |
| 轉嫁後殘差可否寫成美股主體上之獨立存量 | **不可檢為 `S_lock`**　DLR 可見 utilities − reimbursements 為美元缺口，不是 `$/MWh` 鎖定差 |
| 否決觸發 (1) | **觸發** |
| 否決觸發 (2) | **部分觸發（質性／美元端）**　EQIX RPO 明示排除 metered power；DLR 租戶 utilities 報銷覆蓋大部分但非全部美元。殘差存在，卻不是可單位化之鎖定差 |
| 否決觸發 (3) | **未觸發**　`S_lock` 序列不存在，方向未翻、未用 T-11 設備／物理敘事翻號 |
| 升格 T | **否** |

失效歸因（§7-2）：不是檢索失敗。失敗在量綱——所需量（同主體同窗之 `p_PPA` 與 `p_spot`／關稅 `$/MWh`）不是所讀之量（MW／年期、樞紐 ATC、utilities 美元、RPO 固定對價、報銷美元）。現況檔名＝上列 work／query。複查觸發器＝生成卡原文（見下）。停。

本格不入 §1。不改正本（對齊屬 SCOUT）。

---

## 已實讀載體

### A. 發電商季報｜Vistra Q2 2026 10-Q（截止 2026-06-30；acc `0001692819-26-000019`）

PPA 句（原句）：「In September 2025, Vistra announced that we entered into a 20-year PPA (with options to extend for up to an additional 20 years) with Amazon Web Services (AWS), pursuant to which we agreed to supply AWS 1,200 MW of carbon-free power from the Comanche Peak Nuclear Power Plant. Vistra anticipates power delivery to begin in the fourth quarter of 2027 and ramp to full capacity by 2032。」**無成交 `$/MWh`。**

樞紐 ATC 表（原文標題 Average Power Price ($/MWh)；三個月迄 Jun 30）：

| 樞紐 | 2026 | 2025 |
|---|---|---|
| ERCOT North Hub | 30.20 | 32.02 |
| ERCOT West Hub | 24.71 | 31.44 |
| PJM AEP Dayton Hub | 43.40 | 40.58 |
| PJM Northern Illinois Hub | 29.30 | 31.03 |
| PJM Western Hub | 51.43 | 42.35 |
| MISO Indiana Hub | 39.23 | 39.35 |
| ISONE Massachusetts Hub | 47.59 | 40.07 |
| New York Zone A | 33.72 | 35.73 |
| CAISO NP15 | 17.26 | 26.62 |

原文免責：「The table below summarizes the average around-the-clock settled prices for the periods presented and **does not necessarily reflect prices we realized or costs we incurred**.」

R1 在本季已成立：可見端是 MW／年期／交貨窗＋樞紐現貨。樞紐 ATC ≠ `p_PPA`，也不是「已實現合約單價」。禁止用 ERCOT North 30.20 去減一個未揭露的 Comanche Peak 鎖定價來造 `S_lock`。Meta 2,609 MW／20 年同窗公開層同樣只有容量與年期（第三方複述；10-Q 未給單價）。

### B. 發電商季報｜Constellation Q2 2026 10-Q（截止 2026-06-30）＋Q2 簡報／99.1

剩餘履約義務（百萬美元；只含固定可確定對價）：

| | 2026 | 2027 | 2028 | 2029 | 2030 | 2031+ | 合計 |
|---|---|---|---|---|---|---|---|
| RPO | 1,051 | 1,797 | 1,541 | 1,420 | 891 | 5,155 | 11,855 |

原文：「This disclosure only includes components of contracts for which consideration is fixed and determinable. … **This disclosure excludes derivatives and certain power and gas sales contracts which contain variable volumes and/or variable pricing.**」

Crane／Microsoft：20 年 PPA 支持 TMI-1 重啟；NRC 燃料許可與 FERC CIR 轉移已在本季推進。**無成交 `$/MWh`。** Q2 另簽約 920 MW 長約（平均 18.5 年）；準備稿／通話原句方向＝「While I can't disclose pricing」。簡報情景表出現「$20–$50/MWh premium to PTC floor／$10–$25/MWh premium for long-term agreement」——這是**說明用區間**，不是已簽約單價，不得寫成 `p_PPA`。

R3 用盡可見端：RPO 美元 ≠ `$/MWh` 差 × 剩餘約定量。把 11,855 當 `S_lock`＝換量。

### C. 開發商 8-K｜New Era／Luminant（Vistra 關係企業）acc `0001213900-26-101642`（2026-09-21）

TCDC PowerCo 與 Luminant ET Services：最低 200 MW、最高 207 MW；初始 20 年；交貨預期 2027 Q3；信用支援 LC $116,000,000＋額外不超過 $82,800,000。**無能源單價、無容量單價、無 `$/MWh`。** 可見端＝MW、年期、擔保金額。擔保不是成交電價。

### D. 營運商季報｜Equinix Q2 2026 10-Q（截止 2026-06-30；acc `0001101239-26-000147`）＋IR 簡報＋2025 年報 PPA 句

CoR 最大組成含「utility costs including electricity」。Americas CoR 三個月迄 Jun 30, 2026：utilities 費用 **+$14 million**，「primarily due to increases in power costs」；六個月 Americas utilities **+$26 million**。EMEA 三個月 utilities **+$11 million**（renewable energy costs）。**無 `$/MWh`，無鎖定／現貨拆。**

RPO 約 $15.0 billion。原文：「The remaining performance obligations **do not include** variable consideration … such as the **usage of metered power**.」計量電被排除在固定對價之外——即公開層把電費當流量變動項，不是把鎖定差當存量列。

IR 簡報 Q2 26：Utilities Cost as a % of Revenues 時序（Q1 24–Q2 26，約 12–15% 帶）。這是佔比，不是單價。2025 年報質性：29 件 PPA、合約 >1,400 MW（另處 1,472 MW）、2025 營運 PPA **854 MW**（對 2024 的 299 MW）。MW 上升不是 `p_PPA`。

### E. 營運商年報／季補｜Digital Realty FY2025 10-K＋Q2 2026 補充表（窗至 2026-06-30）

FY2025 10-K 財產層（千美元）：

| | 2025 | 2024 |
|---|---|---|
| Stabilized utilities | 1,031,119 | 1,001,884 |
| Non-stabilized utilities | 395,366 | 331,532 |
| **Total Utilities** | **1,426,485** | **1,333,416** |

非穩定組合變動拆項含「a decrease in **power agreement charges** by $13.1 million」——這是協議費用美元增減，不是 `$/MWh` 鎖定／現貨拆。10-K 原句：多數租約含租戶報銷全部或部分物業營運費與房地產稅。

FY2025 穩定組合補充（千美元）：Tenant reimbursements — Utilities **932,787**／2024 885,545；同列 Utilities **1,031,119**／1,001,884。

Q2 2026 合併營運表（千美元）：

| | Q2 26 | Q2 25 | 1H 26 | 1H 25 |
|---|---|---|---|---|
| Tenant reimbursements — Utilities | 352,897 | 294,503 | 686,807 | 565,692 |
| Utilities（費用） | 396,454 | 339,288 | 768,839 | 652,673 |

同窗穩定組合：reimbursements — utilities 269,255 vs utilities 298,503（Q2 26）。美元缺口存在，但是 **utilities $ − 報銷 $**，不是 `(p_PPA − p_spot) × Q`。禁止把缺口當 `S_lock`。

### F. 橫斷盤點｜MLQ.ai 2026-07-17

62 件協議、50.47 GW。揭露欄：容量 62／62；年期 17／62；交貨日 18／62；**usable price per MWh 0／62**。原句：「None of the 62 agreements discloses a usable price per megawatt-hour。」16 件明示未揭露；其餘 46 件無價格。本輪四家主體＋NUAI 8-K 未推翻此盤點。

### G. 明示不採

- 只疊「已簽 1,200 MW／2,609 MW／920 MW／207 MW」或 EQIX 854→1,400 MW。這是生成卡禁止項。
- 只疊 EQIX utilities % of revenues 或 DLR Total Utilities YoY +7.0%。總額不是單價。
- LevelTen 大陸風／光 PPA 指數（Q1 2026 混合約 $71.94/MWh）——市場報價指數，不是本格指名主體之成交 `p_PPA`，不得與 VST 樞紐 ATC 或 DLR utilities $ 同表對帳。
- CEG 簡報 $20–50/MWh premium 情景、第三方「Comanche est ~$110/MWh」——非官方成交列。
- 受規管公用事業零售 cents/kWh 或平均購電 `$/MWh`（BHE／PGE／PNW 等）——關稅／燃料調整，不是資料中心營運商或本格指名發電商之 PPA 成交單價。本輪讀到這些列只為確認「關稅單價存在於**別的**主體」，不能補本格缺的 `p_PPA`。
- T-11 設備／物理層敘事、L2-A capex、C-P4 水。本輪不借。

---

## 對種子與反方

| 主張 | B 端讀後 |
|---|---|
| 鎖定差為存量，不是流量衝擊 | 機制可陳述。缺 `p_PPA` 則不可拒絕「電費隨現貨重定價」也不可接受「差已鎖成存量」 |
| 錯價＝把電力緊張譯成營運商可變電費 | 可見端已被 MW／年期、樞紐 ATC、utilities $、報銷 $、RPO 固定對價用盡。錯價句無官方單價對照錨 |
| R1 所需量不是所讀之量 | **成立**　成交 `$/MWh` 不是科目 |
| R2 轉嫁把存量移出租戶外之可交易主體 | **在可見端部分成立**　EQIX 排除 metered power；DLR 報銷覆蓋大部分 utilities $。殘差是美元缺口，不是 `S_lock` |
| R3 發電商 RPO 不可譯成 `$/MWh` 差 | **成立**　CEG RPO 明文排除變動數量／變動定價合約 |
| R4 翻轉 T-11 已排除方向 | **本輪不用該列**。T-11 構成＝物理／設備、方向負；本格構成＝會計鎖定差 |
| R5 滑到買發電商／賣營運商或台股設備 | **本輪不選券、不開 T** |

「同主體同窗可對帳之鎖定單價與現貨單價」在本輪兩邊都沒有官方序列，故既不能接受也不能拒絕種子。發電商有現貨沒有鎖定價；營運商有美元總額沒有任一端單價。

---

## 不開 T／§7-4

進 T 需數值窗與可拒絕之 H1 倍數。本輪可寫入的只有「MW／年期／交貨窗、樞紐 ATC、utilities 與報銷美元、RPO 固定對價、擔保金額、PPA 件數」。不夠把 `S_lock` 寫成財富倍數窗。

§7-4 三題本輪不答（生成卡：轉入個股層時必問；本格不轉、不進 T）。題目本身已由本輪讀數預示方向（utilities／燃料與購電／PPA 附註再拆不出成交單價對；美股可交易主體存在但存量落在未分列科目或租戶；提前解約／重議／on-site 是否打開流量——公開層連鎖定價都沒有，半衰期不可檢），但不在本輪作答。

**複查觸發器（沿用生成卡，不改寫）：** 任一美股可交易資料中心營運商或發電商於 10-K／10-Q／20-F，分列已鎖定 PPA 成交單價與殘差現貨／關稅單價，並可畫至少兩個報告期之差或剩餘約定量美元。

---

## URL

1. https://www.sec.gov/Archives/edgar/data/1692819/000169281926000019/vistra-20260630.htm
2. https://www.sec.gov/Archives/edgar/data/1692819/000169281926000019/0001692819-26-000019-index.htm
3. https://investors.constellationenergy.com/static-files/ffe5acb1-a976-4963-85f7-28551efd3929
4. https://investors.constellationenergy.com/static-files/354c0998-964f-4f86-b294-1d3fc965d839
5. https://investors.constellationenergy.com/static-files/980078c9-ab31-49ce-8498-8044c0794cd7
6. https://www.sec.gov/Archives/edgar/data/2028336/000121390026101642/0001213900-26-101642.txt
7. https://investor.equinix.com/sec-filings/all-sec-filings/content/0001101239-26-000147/0001101239-26-000147.pdf
8. https://d1io3yog0oux5.cloudfront.net/_9ba6cb0d115918c3323873efb27118e8/equinix/db/2160/27063/pdf/Intro+to+Equinix_IR_Presentation+Q2+26.pdf
9. https://d1io3yog0oux5.cloudfront.net/_08b2449e8774523c0fc3334c23e3fa27/equinix/db/2183/27011/annual_report/Equinix-Inc_2025_Annual-Report.pdf
10. https://investor.equinix.com/sec-filings/annual-reports/content/0001101239-26-000032/0001101239-26-000032.pdf
11. https://www.sec.gov/Archives/edgar/data/1494877/000110465926015365/dlr-20251231x10k.htm
12. https://investor.digitalrealty.com/node/30551/pdf
13. https://www.sec.gov/Archives/edgar/data/1297996/000110465926086270/dlr-20260723xex99d1.htm
14. https://www.sec.gov/Archives/edgar/data/1297996/000110465926086270/dlr-20260723xex99d2.htm
15. https://mlq.ai/research/how-ai-buys-power/
