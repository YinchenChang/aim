# L11-I 測一｜人類注意力：取用權由結構性轉合約性

<!-- BY: ANALYST@GK | MODEL: Grok 4.7【自報】 | CHARTER: AIM-C1.1 | NOTE: 測一不通過｜不進 T。不重開 L11-P。不改測 L11-A／L10-P／L10-A／L10-I。不生成 L13。不改正本 | CONSUMES: 1bFG5Y3Asy_utAdnD56LYFCW36tGiTgJq；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi | EMITS: SELF -->

**日期：** 2026-10-02　**角色：** ANALYST@GK　**格：** L11-I　**上限：** 測一，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 本輪只測生成卡。不寫 T。不改正本狀態欄。

---

## 0. 本輪範圍

- 被測＝生成卡 `20261002_L11-I_generate_GK.md` fileId `1bFG5Y3Asy_utAdnD56LYFCW36tGiTgJq`（12655 B，全文已讀，未截斷）。種子＝ARCH_3h §3.29 L11-I（`1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj`）：代理代表使用者議價，使注意力由「平台可販售之存量」轉為「買方可代理之權利」→ 取用權由結構性轉合約性。B 端載體＝主要平台之 agent API 授權條款。3h 註明該欄僅指名、未實讀。
- 並列對＝同一授權頁上的兩句：（i）注意力或廣告存量是買方代理可行使之權利；（ii）該權利為合約性，而非結構性預設槽／憑證門。缺一則不可並列。
- 不重開 L11-P（FUNNEL §2／ARCH_dead #3，結構性不可表達）。不改測 L11-A `1rdB7GwskexnH84TiO_k2zO4dzzZpNLVe`、L10-P、L10-A、L10-I。不把本格改寫成曝光×單價、選擇畫面、端側能量、清醒秒數，或 C-A5／API 列表價。
- session 列 `work/` `1CEprzXwFF4FA0HRHDe9prm2cIYRLB12z` 僅本生成卡；`inbox_GK` `1ZbILrSDyO71BiAS8yV_Ccx9W_WUKDm-S` 空；`query/` 5 筆（ARCH_dead、matrix、CHARTER_HIST、INDEX、MECH）。MECH `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h` last_sync_utc 2026-10-02T05:48:09Z role SCOUT。正本 FUNNEL `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI` 日期 2026-10-01，§1 已含 L11-A＝測一不通過｜不進 T；§3 仍列 L11-I 已生成未測。matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70` L11［I］＝已生成。本輪不改正本。

---

## 1. 實讀（URL；B 端）

1. OpenAI Service Terms，頁面 Updated September 29, 2026，§14 Dots and Agentic Features。https://openai.com/policies/service-terms/  
   (a) 使用者決定如何使用 dots 與相關 agentic 功能，包括給予何種 access、authority、instructions；使用者對其代為採取之行動與分享之內容負責。(b) 使用者負責與後果相稱之監督。(c) 付款帳戶須自有權限；代為交易由使用者負責；第三方條款仍可能適用。未寫注意力或廣告存量轉為買方可代理之合約權利。
2. OpenAI Advertising Terms，Updated August 25, 2026。https://openai.com/policies/advertising-terms/  
   §1.4：Ads Manager 或任何 API 之存取不保證廣告存量可得。§2.2：「your authorization does not transfer ownership of, or grant any independent right in, advertising inventory. OpenAI retains exclusive control over … inventory allocation, Ad delivery and presentation …」。§5.1：除明示外，條款不授予對 Advertising Services 之 IP 權利。同頁點名存量，並否認獨立權利。
3. OpenAI Agents API 介紹頁，September 10, 2026。https://openai.com/index/introducing-the-agents-api/  
   公開 beta；無額外 Agents API 費，依 token 與工具計價。呼叫與計價頁，不是權利讓與。
4. Google Ads Developer Policies 更新通知，Posted August 31, 2026。https://support.google.com/adspolicy/answer/18105638?hl=en  
   通知改名並連至 Developer Policies（answer/6169371）。頁內無權利讓與句。
5. Google Ads Developer Policies 正文。https://support.google.com/adspolicy/answer/6169371?hl=en  
   頁面未顯示發布日。Programmatic use：禁止第三方經由 programmatic proxy 迴避自有 developer access 與 GCP 專案；禁止「third-party hosted interface, secondary API, wrapper service, or MCP server, proxy endpoint, or any similar service that solely replicates, wraps, or re-exposes Google Ads programmatic capabilities」。代理商或廣告主須使用自己的 GCP 帳戶與 Google Ads access。無一句把存量寫成買方代理可行使之合約權利。
6. Programmatic proxy: Definition。https://support.google.com/google-ads/answer/18103182?hl=en  
   頁面未顯示發布日。定義＝第三方代管介面、次級 API、wrapper、MCP server、proxy endpoint，或僅複製／包裝／再暴露 Google Ads 程式能力之中間層。
7. IAB Tech Lab AAMP，Last updated September 22, 2026。生成卡 URL `https://iabtechlab.com/new-aamp-page/` 開到 `https://iabtechlab.com/standards/aamp-agentic-advertising-management-protocols/`。AAMP 2.0 加交易型與 Buyer／Seller Agent SDK；AAMP 3.0 延至 RFP／OpenProposal。協議與 SDK，不是平台授權頁。無平台授權把存量改成買方代理之合約權利。
8. Meta Ads MCP Server 概述，Updated July 14, 2026。https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview  
   本輪 browse 一次失敗；下列取自同 URL 之檢索摘錄，不作全文已讀。摘錄：Meta 代管之 MCP server，以 permission-scoped tools 暴露廣告面。未見存量權利讓與句。連接器頁檢索摘錄另有「agent acting on your behalf are bound by the Meta Platform Terms」（https://developers.facebook.com/documentation/mcp ，Updated June 12, 2026）；該頁本輪未全文實讀，只作旁證，不進並列。

缺段（CHARTER §7-2）：定義頁與 Developer Policies 正文無發布日。Meta 概述 browse 失敗，不以檢索摘錄作不存在主張。Anthropic 商業條款本輪未逐條實讀；不拿來補本格 B 端。

---

## 2. 可觀測／可並列

| 欄 | 判定 | 讀到什麼 |
|---|---|---|
| 責任句／監督句 | 可觀測 | OpenAI §14(a)(b)(c)：access、authority、後果留在使用者 |
| 存量被點名，且獨立權利被否認 | 可觀測 | OpenAI Advertising Terms §2.2：授權不移轉所有權、不授予 advertising inventory 之獨立權利；分配仍由平台專屬控制 |
| 結構性憑證門 | 可觀測 | Google Developer Policies：中間層／MCP／wrapper 不得迴避自有憑證；須 per-entity 認證 |
| 行業協議／SDK | 可觀測 | IAB AAMP 2.0／3.0 與 Buyer／Seller Agent SDK；不是平台授權 |
| 呼叫計價 | 可觀測 | Agents API：token 與工具計價；無存量句 |
| （i）存量權利＝買方代理可行使 | 不可並列 | 無一份已讀授權頁寫此句。同頁最近者是否認獨立權利 |
| （ii）該權利為合約性而非結構性預設槽 | 不可並列 | 無替代條款頁寫明轉換已發生。Google 同來源方向相反：中間層仍被關在憑證門外 |

可運作對照只剩：責任句、存量獨立權利之否認、憑證門禁止、行業 SDK、token 計價。這四類不是「權利已經易手」的兩側。

---

## 3. 否決

生成卡寫給本輪之觸發，本輪執行：

- **(1) 觸發。** 實讀後無法在同一授權頁並列「存量權利」與「合約性而非結構性」。剩下的是使用者責任句（§14）、存量獨立權利之否認（Advertising Terms §2.2）、token 計價、行業 SDK。
- **(2) 同向。** Google 同一政策把再暴露能力之 MCP／wrapper／proxy 寫成不得迴避平台憑證之中間層。無替代條款頁寫明權利已轉合約性。
- (3) 未改格。不把對照寫成曝光×單價、選擇畫面、端側能量或清醒秒數。不重開 L11-P。不改測 L11-A／L10。
- (4) 未改格。不以 API 列表價或 C-A5 支撐。

終端三題本輪不答（CHARTER §7-3；生成卡 §6 本階段不答）。

---

## 4. 次級路徑

上市主體＝Alphabet。10-Q 索引可開：acc `0001652044-26-000071`，申報 2026-07-23，期間止 2026-06-30，主檔 `goog-20260630.htm`。索引與正文 URL 可開；摘要層未見 agent／MCP／存量權利型態句。不以摘要層之「未見」作全文不存在。Google 政策更新 Posted 2026-08-31，晚於該季 10-Q，故該申報本來就不是 August 政策的載體。廣告收入科目不是本格並列對。**10-Q 次級路徑未成立。**

複查觸發器（沿生成卡）：任一主要平台之 agent API 授權條款同頁寫明注意力或廣告存量是使用者之代理可行使之權利，且該權利為合約性而非結構性預設槽，並標明生效日。

---

## 5. 終態

**測一不通過（條款頁、存量獨立權利之否認、與憑證門禁止可觀測；存量權利與合約性而非結構性不可並列）｜不進 T。**

不重開 L11-P。不改測 L11-A／L10-P／L10-A／L10-I。不生成 L13。不重開 C-A5。不寫 T。不改正本 FUNNEL／matrix／INDEX。

---

## 6. 本輪寫入／不寫入

寫入：本測一入 Drive `work/`（fileId 見上傳回傳；標頭 EMITS＝SELF）。
不寫入：FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`；matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`；INDEX.json `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`；ARCH_dead；ARCH_3h。禁止新建同名正本。狀態欄對齊屬下一 session。生成卡尚未入 §1，本輪不建 `DONE_`。
