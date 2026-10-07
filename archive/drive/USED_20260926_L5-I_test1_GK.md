<!-- BY: ANALYST@GK | MODEL: Grok 4.6【自報】 | CHARTER: AIM-C1.1 | CONSUMES: 1RaVhNa9EEeMUq6dssdfGjQTIdwex7osx；1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70；1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9；1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；1VaVhI3eGdH_h6rT9Cso3BwUHiz4wVoOm | EMITS: PENDING_UPLOAD -->
# L5-I 測一｜B 端實讀（官方出站費率表＋Data Act Art. 29／34 生效日與切換／並行分界）

**角色：** ANALYST@GK　**日期：** 2026-09-26　**格：** L5-I（儲存與 IO：資料重力＝出站費結構性取用權；法規把出站費由合約性壓向法定上限）
**任務邊界：** 只做測試一。B 端須實際 fetch 並列 URL。優先官方出站費率表之列名＋Data Act Art. 29／34 生效日與切換／並行分界；次為遷離方案官方條款是否等於法定零收費。**禁止只重讀 L5-A 雲端總額、「Data Act 取消 egress」評論、或非申報零出站價目。** 不寫 T／L／M、不取 LEDGER／P、不改 FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`、不改 matrix `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`、不改 INDEX、不開 T、不入 §1。
**原陳述（生成卡 `1RaVhNa9EEeMUq6dssdfGjQTIdwex7osx`；種子 3h §3.29）：** 資料一旦進雲，出站費使取用權為結構性；Data Act Chapter VI 把切換／攜出由合約定價壓向法定上限、再壓向零。錯價只在把價目表網際網路出站列當成完整重力，或把「已有免出站方案」當成型態已轉完。
**對照式（生成用）：** `P_egr(use, juris, t) ∈ {P_list, P_direct_cost, 0}`。`use`＝切換／遷離 vs 並行／網際網路；`juris`＝Data Act 域 vs 其餘。切換段 `P_egr → 0`（法定日）且清單價仍 > 0 ⇒ 型態轉換可拒絕。本輪不估參數、不寫 H1。
**否決觸發（生成卡寫給本輪）：** (1) 對官方價目與法規條文實讀後，切換段與清單出站無法按用途×管轄分開，只剩一張全球 $/GB 表與「遷離免收」行銷句；或 (2) 可見對照只能寫成「方案已等於 Art. 29，2027-01-12 無增量轉換」，且並行／非 EU 殘差無獨立可拒絕項；或 (3) 可運作對照只能寫成 L5-A 雲端總額、L15-I 遙測結構性、或 C-P1 訓練儲存。
**領域最近公開（§7-10）：** EU Data Act（Regulation (EU) 2023/2854）Chapter VI 適用 **2025-09-12**（BNetzA 官方頁）；Art. 29 切換收費全面禁止 **2027-01-12**；Art. 34 並行出站得收實際成本。AWS 官方 EC2／S3 價目＋遷離 DTO 方案（公告 2024-03-05；FAQ 2025-09-30 改 90 日）；Azure Bandwidth 價目＋Learn 遷離段（頁面更新 2026-06-07）；GCP VPC network pricing＋`cloud.google.com/exit-cloud`＋Data Transfer Essentials（2025-09-10，EU／UK 並行零價）。下一官方檢查點＝生成卡原文：2027-01-12 後任一超大規模雲於 10-K／10-Q 分列出站／切換方案貸項之已實現美元行，或官方價目把「切換出站」與「並行／網際網路出站」拆成可對帳兩列；或主管機關裁定清單出站列屬違法切換收費。

**本輪開始時 Drive 現況（狀態來源＝檔案，非記憶）：**
- work/：`20260926_L5-I_generate_GK.md` `1RaVhNa9EEeMUq6dssdfGjQTIdwex7osx`（12422 B，2026-09-26T14:41:02Z）；`20260923_HEALTH_CL.md` `1_urT6I7RovcM73D3IBTKGIk6RY1z9nC0`；`20260923_HEALTH_GK.md` `1byQGbjCmIT1orLv51moyAH5xnABFO95e`；`DUP_PLACEHOLDER_L1-I_test1_do_not_use.md` `1lci-pu8ekOI7T-za2Sl93q-j1GUoNAjl`
- L5-A 生成／測一已 `USED_`（`1vbroLuAzR1ayP0SuO23VN-5nhr8p5AV8`／`1VaVhI3eGdH_h6rT9Cso3BwUHiz4wVoOm`），不在 work/ 現況清單；本輪只引用測一 fileId 作「禁止重讀雲端總額」邊界，不重貼其美元行
- query/：`ARCH_dead.md` `1Ef6V-bsOEVjOZo9eNEnjMgHHzxUxPXC9`；`ARCH_matrix.md` `1YfXzIEOsJ640lWQ3fudLTLb30AuT6K70`（L5［I］＝已生成）；`CHARTER_HIST.md` `1DKg3HUr-zOWw20OmNe1aDpWT_izDwdiT`；`INDEX.json` `1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX`；`MECH.md` `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h`（last_sync_utc 2026-09-26T14:43:26Z role ANALYST）
- FUNNEL 正本 `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`（2026-09-26；§1 無 L5-I；§3 L5［I］＝已生成＝3h 快照）
- 3h 快照 `1vCilG4Px8g7vqybZNQ-9hWDNee-M-ofj` L5-I B 端僅指名「各雲出站費率表；法規生效日」
- 本輪上傳前 work/ exact_name `20260926_L5-I_test1_GK.md` 空；無內容相近測一
- work 主動維護：L5-I 生成卡未吸收進 FUNNEL／matrix（待本測一後由 SCOUT 對齊）。HEALTH 兩份與 DUP_ 占位非本輪標的。本輪不建 `DONE_`。

---

## 終態

**部分通過｜不進 T。** 機制（出站費＝結構性取用權；Data Act 把**切換段**由合約價壓向直接成本、再壓向零）未被否證。B 端指名兩欄均已實讀：三家官方出站價目＋遷離方案條款；Art. 29／34 條文與適用日。失敗在量綱合成——

1. **法規層可拆。** Art. 2(35)(36) 定義出站費 ⊂ 切換收費（不含標準服務費、提前終止罰）；Art. 29：2024-01-11→2027-01-12 得收直接成本、**2027-01-12 起切換收費＝0**；Art. 34(2)：**並行**得出站、僅實際成本。Chapter VI 適用 **2025-09-12**（BNetzA）。用途×時間分界可拒絕。
2. **價目表層不可拆成可對帳兩列。** AWS／Azure／GCP 公開網際網路出站表是**用途無關**的分級 $/GB（或 $/GiB）。切換零價不在表上成 SKU，而在申請／貸項／Addendum 路徑。AWS 本輪 HTML 未吐出完整分級格（JS）；Azure、GCP 表完整。管轄差（EU Data Act 減價）在 AWS 頁是「聯絡 Support」句，不是表上一條 EU 列。
3. **遷離方案 ≠ Art. 29。** 三家 2024-01／03 全球方案把「全量遷離」出站作成貸項，但附申請、時窗（AWS 90 日／Azure 60 日／GCP 啟動＋遷移窗）、排除專線／CDN、且 GCP／Azure 綁終止該服務或全部訂閱。2027-01-12 的增量是**法定義務性格**（得申請的貸項 → 不得收切換收費），不是清單價 Δ。
4. **並行／非 EU 殘差可獨立拒絕。** Art. 34 明文允許並行出站收實際成本；三家清單價對常規網際網路出站仍 > 0。GCP 於 2025-09-10 另開 EU／UK「Data Transfer Essentials」把並行做成**零價命名產品**——這是管轄×用途的產品層分列，仍不是 VPC 價目表上的第二列，也不是 10-K 出站美元行。

否決觸發 (1) 在**價目表列名**上觸發、在**法規條文**上未觸發。(2) 未觸發（方案可拒絕等於 Art. 29；並行殘差獨立）。(3) 未觸發（未用 L5-A 總額、L15-I、C-P1）。無單一可單位化連續參數把「型態轉換」寫成 H1 倍數窗：清單 `P_list` 不是切換段的 `P_egr`；切換段在方案層已近 0，法定日改的是義務而非可見單價。不進 T。不入 §1。

| 測試項 | 結果 |
|---|---|
| B 端已實讀（非指名；非 L5-A 雲端總額／評論／非申報零出站價目） | **通過**　見下節 URL |
| 官方價目按用途（切換 vs 並行／網際網路）拆成可對帳兩列 | **不通過**　公開表＝用途無關清單出站；切換＝方案／貸項 |
| 官方價目按管轄（Data Act 域 vs 其餘）拆成可對帳兩列 | **不通過**　AWS＝Support 句；Azure／GCP 清單全球分區，不是 Data Act 列。GCP DTE＝EU／UK 並行產品，非價目第二列 |
| Art. 29／34 生效日與切換／並行分界可拒絕 | **通過**　2025-09-12 適用；2024-01-11→2027-01-12 直接成本；2027-01-12 切換收費＝0；並行≠切換 |
| 遷離方案條款＝Art. 29 法定零收費已提前完成 | **可拒絕**　申請、時窗、排除項、終止條件；非自動法定零 |
| 2027-01-12 對清單價是否仍有增量轉換 | **法律性格有、清單單價無**　增量不在 $/GB 表 |
| 並行／非 EU 殘差有獨立可拒絕項 | **有**　Art. 34＋清單價仍 > 0；GCP DTE 反證「並行已被法定歸零」不成立於全市場 |
| 否決觸發 (1) | **部分觸發**（價目表）；法規分界未觸發 |
| 否決觸發 (2) | **未觸發** |
| 否決觸發 (3) | **未觸發** |
| 升格 T | **否** |

失效歸因（§7-2）：不是檢索失敗（法規與 Azure／GCP 表完整；AWS 分級格本輪 JS 未入 HTML，失敗歸因＝頁面渲染，不作「AWS 無分級價」主張；靜態句已讀到 100 GB 免費、Ireland 例 $0.09／GB、>500 TB 洽詢、Data Act 減價須 Support）。失敗在量綱——所需量（用途×管轄之可對帳兩列，或切換段單價隨 2027-01-12 可畫的 Δ）不是所讀之量（一張清單出站表＋三份申請制貸項方案＋一條法定分界）。現況檔名＝上列 work／query。複查觸發器＝生成卡原文。停。

本格不入 §1。不改正本（對齊屬 SCOUT）。

---

## 已實讀載體

### A. 法規｜Regulation (EU) 2023/2854（Data Act）Art. 2／29／34；適用日

入口：https://eur-lex.europa.eu/eli/reg/2023/2854/oj  
EN 條文交叉：https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng  

定義（Art. 2）：
- (35) **data egress charges**＝自資料處理服務提供者基礎設施經網路擷取資料至另一提供者或本地 ICT 之傳輸費。
- (36) **switching charges**＝除標準服務費或提前終止罰外、為本規章所強制之切換行為而收的費用，**包括 data egress charges**。

Art. 29 Gradual withdrawal of switching charges（EUR-Lex 原文結構）：
- (1) **From 12 January 2027**, providers shall **not impose any switching charges** on the customer for the switching process.
- (2) From **11 January 2024 to 12 January 2027**, may impose **reduced** switching charges.
- (3) Reduced charges **shall not exceed the costs incurred** that are **directly linked** to the switching process concerned.
- (4) 締約前須清楚告知標準服務費、提前終止罰、以及過渡期減收之切換收費。

Art. 34 In-parallel use：
- (2) Where a data processing service is being used **in parallel** with another, providers **may impose data egress charges, but only for the purpose of passing on egress costs incurred, without exceeding such costs.**

敘文 88（公開轉載與 EUR-Lex 一致）：切換收費之典型例＝資料出站費；**標準服務費本身不是切換收費**。

適用日：Chapter VI 自 **2025-09-12** 適用於新舊契約。主管機關說明（非評論）：BNetzA「Data processing services and provider switching」https://www.bundesnetzagentur.de/EN/Areas/Digitalisation/DataAct/background/3-provider/start.html  
原文：「All contracts, that is both existing contracts concluded before and new contracts concluded after **12 September 2025**, when the Data Act became applicable, must comply with the provisions of Chapter VI。」同頁複述 Art. 29 兩段日與 Art. 34(2)「並行得出站、限實際成本、不得加價」。

R2／R4 在條文層成立：出站費不是單一量；法定零只覆蓋**切換過程之 switching charges**；並行殘差被 Art. 34 明文留下。

### B. 出站費率表｜Azure Bandwidth（官方表完整）

https://azure.microsoft.com/pricing/details/bandwidth/  
（本輪 fetch；Learn 遷離段 last updated **2026-06-07**）

Zone 1（北美／歐洲）Internet Egress，Microsoft Premium Global Network：

| 來源 | 首 100 GB／月 | 次 10 TB | 次 40 TB | 次 100 TB | 次 350 TB |
|---|---|---|---|---|---|
| NA／EU → 任一目的 | Free | $0.087／GB | $0.083／GB | $0.07／GB | $0.05／GB |

同區經 ISP transit 路由：Free／$0.08／$0.065／$0.06／$0.04。Zone 2／3 更高（亞洲首檔 $0.12；南美 $0.181，Premium）。同 AZ 免費；同區域服務間無收費。跨區北美／歐洲內 $0.02／GB。

同頁遷離句（價目頁，非評論）：「Azure offers **free egress for customers leaving Azure** when taking their data out of the Azure infrastructure via the internet to switch to another cloud provider or an on-premises data center。」與上表「首 100 GB 免費」並列——**兩句，不是一列「出站已免費」。**

方案條款（官方 Learn，非價目列）：https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/cancel-azure-subscription  
- 須先開 Support request（訂閱／註冊 ID、預定開始日、估計 GB）。
- 自載明開始日起 **60 日**內完成（UK 帳單地址＋UK 資料中心＝180 日；UK 可含單一服務退出與 MGN）。
- 資料遷出後須 **取消帳戶下全部 Azure 訂閱** 才能申請發票層貸項（UK 單一服務則須結束該服務用量）。
- **排除：** ExpressRoute／ExpressRoute Direct、VPN、Azure Front Door、CDN；僅「因遷離 Azure 而產生之 egress」可貸。
- 標準服務費不在方案內。

清單列名＝「Internet Egress」分區分級。無「Switching egress」列。

### C. 出站費率表｜GCP VPC network pricing＋遷離＋並行產品

價目：https://cloud.google.com/vpc/network-pricing  

Premium Tier 網際網路出站（本輪摘；$／GiB；帳戶層少量免費檔）：

| 目的地 | 1 GiB–1,024 GiB | 1,024–10,240 GiB | 10,240 GiB+ |
|---|---|---|---|
| North America | $0.12 | $0.11 | $0.08 |
| Europe | $0.12 | $0.11 | $0.085 |
| Asia（韓／印尼除外） | $0.12 | $0.11 | $0.085 |
| Australia／Indonesia／Korea／South America／Saudi | $0.19（自 0） | $0.18 | $0.15 |

Standard Tier：帳戶月 200 GiB 免費，其後 $0.085／$0.065／$0.045。價目頁**無**遷離零價列、無 Data Act 列。

遷離方案：公告 2024-01-11 https://cloud.google.com/blog/products/networking/eliminating-data-transfer-fees-when-migrating-off-google-cloud  
條款頁 https://cloud.google.com/exit-cloud  
- 適用「停止使用相關 Google Cloud **服務**並把該服務全部工作負載／生產資料遷出」。
- Exit Notice → 14 日指派帳務 → **Initiation Period 30 日**內啟動 → **Migration Period 至少再 30 日** → Completion Notice（遷移期結束後、最長 180 日內）→ 該服務契約於 Completion 後至少 30 日至次月月底視為終止 → **最終發票貸項**＝Exit Notice 當下平台上該批資料之傳輸成本。
- **不終止該服務契約＝不合格。** 不得只遷一部份同一服務。其他 GCP 服務可留。
- 可攜產品名單另頁 `cloud.google.com/terms/data-portability`。

並行產品（管轄×用途，仍非 VPC 表第二列）：2025-09-10 https://cloud.google.com/blog/products/networking/new-for-the-uk-and-eu-no-cost-multicloud-data-transfer-essentials  
官方句：為 EU／UK 客戶之 **in-parallel** 跨雲傳輸；「Although the Act allows cloud providers to pass through costs to customers, Data Transfer Essentials is available today **at no cost**.」此句同時確認：(i) Art. 34 允許轉嫁成本；(ii) GCP 選擇把該產品做成零價；(iii) 這不是全球清單出站歸零。

### D. 出站費率表｜AWS EC2／S3 價目＋遷離方案＋EU Addendum

價目：https://aws.amazon.com/ec2/pricing/on-demand/  
https://aws.amazon.com/s3/pricing/  

本輪官方 HTML 穩定可見句（非第三方轉述）：
- 「AWS customers receive **100 GB** of free data transfer out to the internet free each month, aggregated across all AWS Services and Regions (**except China and GovCloud**).」
- 「**EU customers may request reduced data transfer rates for eligible use cases under the European Data Act.** Please contact AWS Customer Support for more information.」
- 「AWS also offers eligible customers **free data transfer out to the internet when they move all of their data off of AWS or all of their data off of a particular AWS service**.」→ FAQ。
- S3 頁靜態例：Europe（Ireland）出站 **$0.09 per GB**；>500 TB／月洽詢。
- **本輪未從官方 HTML 讀到完整 US-East 分級格**（頁面分級表為 JS 渲染）。不作「AWS 無分級」主張；亦不把第三方彙整之 $0.09／$0.085／$0.07／$0.05 寫成本輪已實讀列。

遷離公告（生成卡舊錨 `/moving-off-aws/`＝**404**；現行官方）：  
https://aws.amazon.com/blogs/aws/free-data-transfer-out-to-internet-when-moving-out-of-aws/  
2024-03-05，Sébastien Stormacq。2025-09-30 更新註：合格客戶有 **90 日**完成遷離；需更長須立即通知 Support；「If you are an EU customer exercising a switch under the EU Data Act, please review … **AWS EU Data Act Addendum**.」並刪「過渡期須 >100 GB／月才准聯絡 Support」之條件。

FAQ（官方程序）：https://aws.amazon.com/ec2/faqs/#Data_transfer_fees_when_moving_all_data_off_AWS  
- 帳戶良好；<100 GB 存量走既有月免額、不另給貸項。
- Support 標「free data transfer to move off AWS」；**核准前不得開始遷**。
- 貸項依計算當下全帳戶存量估算，**只抵 DTO**，不抵其他服務。
- 核准後 **90 日**內刪該服務／帳戶剩餘資料與工作負載，或關戶。
- 可「全部離開 AWS」或「某一服務之全部資料」。
- **排除：** CloudFront、AWS Direct Connect、AWS Snow Family、AWS Global Accelerator。
- EU 切換走 Addendum：https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/legal/approved/eu-data-act-addendum.pdf  

清單列名仍是 Data Transfer Out to Internet。切換零價＝貸項路徑＋（EU）Addendum，不是價目第二列。

### E. 本輪明確不讀、不引用為通過條件

- L5-A 測一 `1VaVhI3eGdH_h6rT9Cso3BwUHiz4wVoOm` 之 AMZN／GOOGL／MSFT **雲端總額**美元行。所需量不是雲端分部總額。
- 「Data Act 取消 egress」新聞句——以 EUR-Lex／BNetzA／三家官方方案頁取代。
- 非申報零出站物件儲存商價目（R6／L15-I 邊界）。
- 10-K 出站美元行：本輪不開；生成卡已預告該列不存在於 L5-A 所讀之總額。複查觸發器保留給該列首次出現。

---

## 對 R1–R6 之測一處分（不寫 H1）

| # | 反方 | 本輪 |
|---|---|---|
| R1 | 2024 方案已提前，2027-01-12 不是新事件 | **半成立**　方案把全量遷離 DTO 作成貸項，早於法定零。2027-01-12 仍改義務性格（得申請 → 不得收），不是清單價事件 |
| R2 | 法定上限只覆蓋切換／EU；清單網際網路與非 EU 仍合約 | **成立**　Art. 29 ≠ Art. 34 ≠ `P_list`。三家公開表仍對網際網路出站收費 |
| R3 | 鎖定搬到期限費／適度提前終止 | **本輪不測**　Art. 29(4)／Art. 2(36) 把提前終止罰排除在 switching charges 外；未讀各家固定約文本。標「轉個股層必問 #3」 |
| R4 | 並行出站仍得收實際成本 | **成立**　Art. 34(2)。GCP DTE 是 EU／UK 產品選擇，反證全市場並行未歸零 |
| R5 | 10-K 無出站美元行 | **本輪不重讀總額**　可觀測性風險保留；不是本測一通過條件 |
| R6 | 做成買零出站／賣超大規模雲＝換格 | **未觸發**　本輪不選券、不寫表達點 |

---

## 轉入個股層時必問（§7-4，本輪仍不答）

1. 財報科目：出站／切換貸項能否從雲端總額再拆；能否拒絕一般頻寬、CDN、專線。
2. 可交易工具：型態轉換落在美股可交易雲端揭露主體，而非僅私有物件儲存或無申報遷雲中介。
3. 半衰期：2027-01-12 後鎖定是否改由固定約終止費／專線／並行出站承接，使 ≥12 個月窗內「型態轉換」不再可分離。

---

## 本輪寫入／不寫入

寫入：本測一入 Drive `work/`（fileId 見標頭 EMITS，上傳後回填）。
不寫入：FUNNEL 正本、matrix、INDEX、ARCH_dead、CHARTER。禁止新建同名正本。狀態欄對齊屬下一 SCOUT session。
