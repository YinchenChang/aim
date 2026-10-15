# L9-I#3 生成卡｜受規管 HITL：誘因（按件專業判讀之 RVU 時間假設——醫師簽核維持計費單位、AI 壓縮實際判讀時間、RUC 調查者無誘因下修）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260922_L9-I_generate_GK.md；archive/drive/USED_20260922_L9-I_test1_GK.md；archive/work/20261008_L9-I#2_generate_CL.md；work/20261008_L9-I#2_test1_CL.md；work/20261015_L9-A#3_test1_CL.md | EMITS: work/20261015_L9-I#3_generate_CL.md -->
**日期：** 2026-10-15　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain，配額 5／6）　**格：** L9-I　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L9-A#3 本日測一不通過）。非「已殺／刻意排除」格中最後測一最舊＝2026-10-08（L9-I#2、L12-P#2、L12-A#2、L12-I#2、L3-A#2、L1-A#2）；同日依測一先後（QUEUE Q-0007 最早）取 L9-I。既有生成 2 份 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `radiology "fee schedule" RVU "efficiency adjustment"`，命中 0 筆；未使用。
- 比對（本卡須異型）：
  - **L9-I#1**（`archive/drive/USED_20260922_L9-I_generate_GK.md`；測一 `archive/drive/USED_20260922_L9-I_test1_GK.md`）：應用層 SaaS 賣方把 AI 成本折進 SKU；死於 SKU 改版時序不在申報層。本卡不涉 SaaS SKU、不涉 AI 成本列。
  - **L9-I#2**（`work/20261008_L9-I#2_test1_CL.md`）：付款方拒付之不申訴留存率；死於 (2)：AI 連結只剩 L9-P 型載體。本卡選擇者為**提供者端**（專科學會／RUC 調查回覆者、判讀醫師團體），載體為 **CMS 費率規則**（RVU、intraservice time、efficiency adjustment）與提供者申報之專業費用，不涉拒付。
  - **L9-P**（ARCH_dead #1）：應用商揭露 AI 建議之人工核可率／HITL 工時；本卡不靠廠商揭露工時，而以**法定費率表內嵌之時間假設**對照公開之 AI 判讀效率研究；若測一發現唯一可觀測量是 HITL 工時，即依否決 (2) 併入 L9-P。
  - **L9-A#3**（`work/20261015_L9-A#3_test1_CL.md`）：MA 按人頭 RAF 編碼存量 [A]；本卡為按件計費（FFS PFS）之時間租 [I]，不涉 RAF、RADV。
  - C-A1（#6）、C-I5（#18）、C-A2（#9）：不涉。
- §7-10 領域最近公開：CY2027 PFS 提案 2026-07-14（ACR 摘要；意見截止 09-14）；CY2026 PFS 定案 2025-10-31（efficiency adjustment −2.5%）；Becker's ASC 2026-10-13；RDNT 10-Q 2Q26 2026-08-10。下一檢查點＝CY2027 PFS 定案（約 2026-11 初）、CY2028 提案（約 2027-07）、RDNT 3Q26 10-Q。

## 1. 落差一句

Medicare 醫師費率（PFS）對非按時計費之判讀類服務按件給付，work RVU 依 AMA RUC 調查之醫師 intraservice time 估定；法規要求由醫師判讀並簽署報告（HITL 為計費前提），故 AI 縮短實際判讀時間時，計費單位與單價不變，差額歸判讀醫師團體或合併其專業費之影像主體。調查回覆者（受影響專科醫師）無誘因申報較短時間。CMS 已於 CY2026 以「time assumptions … very likely overinflated」為由，對非按時計費服務施 −2.5% efficiency adjustment（依 MEI 生產力回溯，非 AI 專屬），並於 CY2027 提案就 AI 資源成本發 RFI。種子主張：AI 帶來之判讀效率（實地研究平均約 16%，部分醫師至 40%）遠大於週期性 −2.5%，規則端以 AI 專屬資料重估時將一次逆轉；**方向未定**：若重估緩慢或僅維持通用調整，租金持續由提供者保有；若商業費率不跟隨 Medicare，影響限於 Medicare 占比。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：選擇者＝RUC 調查回覆者／專科學會（時間申報）、判讀醫師團體（採用 AI 而不改計費）；規則端＝CMS（efficiency adjustment、RFI、未來以實證時間重估）；HITL＝醫師簽署為計費前提 |
| 恆等（僅定義） | 專業判讀收入＝件數 × work RVU(調查時間) × CF＋PE／MP；單件實際時間 ↓ → 每醫師每時收入 ↑，單價不變直至重估 |
| 已讀事實 | CMS CY2026 fact sheet：「a final efficiency adjustment of -2.5% for CY 2026」，適用 work RVU 與 intraservice time 之非按時計費服務；「the time assumptions built into the valuation of many PFS services are, as a result, very likely overinflated」。ACR CY2027 提案摘要：CMS 將每三年施作；CY2027 無新幅度；新增 AI 於基層醫療資源成本之 RFI；放射科 RVU 變動 +2%（未計 CF 下降）。Becker's ASC 2026-10-13：診斷放射科 wRVU −2.4%（SullivanCotter 2025-11），2026-04 更新為 −3.1%，為受影響最大專科。JAMA Netw Open 2025-06-05（Northwestern 12 院，約 24,000 份報告）：AI 輔助 X 光報告效率平均約 +16%、部分至 40%。RDNT 10-Q 2Q26：同中心薪資 +6.8% vs 同中心營收 +11.1%，歸因於「workflow optimization technologies, including early benefits from the deployment of DeepHealth technology」；同中心專業判讀費 +20.2%，加州／紐約合併 BRMG／Lenox Hill 專業費，其餘地區營收以扣除專業費淨額列示。 |
| 未證之連結 | 上市主體之專業判讀收入能否與技術收入分列並以件／醫師 FTE 標準化；Medicare FFS 占比；AI 效率是否已反映在 RUC 新調查；商業費率是否釘住 PFS |
| 量綱 | AI 判讀時間縮減（%）vs efficiency adjustment（% wRVU／3 年）；Medicare 專業判讀收入 ÷ 總收入（%）；專業費 ÷ 營收（%） |
| 半衰期 | efficiency adjustment 每 3 年一次（下次約 CY2029）；RUC 個別代碼重估 1–3 年；CMS 年度 PFS 週期（7 月提案、11 月定案） |

## 3. B 端可觀測載體（只指名）

1. CMS CY2026 PFS 定案 fact sheet https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2026-medicare-physician-fee-schedule-final-rule-cms-1832-f
2. ACR CY2027 MPFS 提案詳細摘要 https://edge.sitecorecloud.io/americancoldf5f-acrorgf92a-productioncb02-3650/media/ACR/Files/Medicare-Medicaid/MPFS/2027-MPFS-PR-Detailed-Summary.pdf
3. Becker's ASC 2026-10-13 https://www.beckersasc.com/?p=110362
4. Northwestern／JAMA Netw Open 2025-06（轉述）https://www.powershealth.org/about-us/newsroom/health-library/2025/06/09/ai-can-boost-radiologists-efficiency-without-sacrificing-accuracy
5. RadNet 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/790526/000162828026055338/rdnt-20260630.htm ；10-K FY25 https://www.sec.gov/Archives/edgar/data/790526/000162828026013337/rdnt-20251231.htm （10-K「efficiency adjustment」0 筆；CY2026 PFS 僅概括風險句）
6. 未讀：CY2027 PFS 定案原文、CMS-1832-F Federal Register 之 efficiency adjustment 理由段、RUC 調查方法與放射科代碼近年重估、其他上市判讀主體（如病理專業費）、Radiology Partners（私有）債券揭露、具名賣方量化。

缺段（§7-2）：上市主體 Medicare 專業判讀占比、每醫師判讀量；本輪未讀；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | CMS 已施通用 −2.5% 並每 3 年重施，逆轉已制度化、公開 | 載體 1、2 | 已定價 |
| R2 | 放射科 CY2027 RVU 變動 +2%，規則端未見 AI 專屬下修 | 載體 2 | 12 個月無驅動 |
| R3 | RDNT 等主體多以技術收入為主、專業費多以淨額列示；AI 效益落在技術端人力而非專業判讀單價 | 載體 5 | 機制落點錯置／不可分列 |
| R4 | 研究為單一網絡 X 光；CT／MR 等高 RVU 檢查之 AI 效率證據較弱 | 載體 4 | 量級 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) ≥ 2 家上市主體之 10-K／10-Q 無法分列或代理專業判讀收入（含 Medicare FFS 占比或每醫師／每件標準化），亦無 PFS efficiency adjustment 之主體特有影響揭露；或
(2) 能把機制連上 AI 之唯一可觀測量為 HITL 工時或 AI 建議核可率（L9-P 型），或只剩付款方拒付（L9-I#2 型）；或
(3) `[D]` 量級：可得最佳代理（Medicare 專業判讀收入占比 × 可預見之 AI 專屬重估幅度）< 1% 收入；或
(4) 12 個月內無可觀測驅動：CY2027 PFS 定案無 AI 相關重估、RFI 無後續、RUC 無放射科代碼重估；或
(5) 公司或具名賣方已逐家量化 efficiency adjustment 與 AI 重估之影響（已定價）。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：專業判讀費（毛額／淨額列示）、Medicare 收入占比、薪資與專業費率。2. 可交易工具：影像中心／判讀醫師團體（不選）。3. 半衰期：PFS 年度週期、efficiency adjustment 三年週期。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L9［I］格加「#3 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0050。不改 L9-I#1／#2、L9-A#1–#3、L9-P、C-A1、C-I5 結論。
