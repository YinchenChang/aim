<!-- BY: PM@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: — | EMITS: export/LEADS_算力收支.md -->
# LEADS｜算力收支研究線索（AIM → 算力收支；只追加）

**用途：** SCOUT 實讀到之新事實，供 Andy 之算力收支研究作線索。只是線索，不是 AIM 之結論；使用前請回出處實讀。
**範圍：** AI 算力投入（資本支出、GW／MW）、AI 收入、硬體（晶片、記憶體、網通、封裝）、雲端與算力合約、資料中心（站址、電力、併網）。
**規則（CLAUDE.md §12；`python tools/leads.py add` 寫入、`check` 驗證）：**
- 每筆一列：登錄日、出處日期、主張（一句，照出處口徑）、數值、單位、出處網址（單一原始出處）、來源等級（`[V]`／`[I-<利害方>]`／`[D]` ＋ 一手／二手）、登錄者（角色＋Q-id 或輪別）。
- **不得寫：** 部位、尺碼、金額配置、候選判斷、AIM 候選代碼、任何評等或投資標的文字。
- **不得寫入出處為 `YinchenChang/Tokenomics` 或 `YinchenChang/company-models` 之事實**（避免循環驗證）；經 `tools/tokenomics_leads.py` 線索找到、已在 Tokenomics `SRC_*` 之同一出處亦不重複寫。
- 只追加；更正以新列登錄並於主張註明「更正 <登錄日>／<原網址>」，不改舊列（版本史＝git log）。

| 登錄日 | 出處日期 | 主張 | 數值 | 單位 | 出處網址 | 來源等級 | 登錄者 |
|---|---|---|---|---|---|---|---|
| 2026-10-23 | 2026-07-01 | UnitedHealth Group 計劃於今明兩年合計投入 AI 支出（Becker's 轉述 UHG） | 3 | 十億美元（2026–2027 合計） | https://www.beckerspayer.com/payer/unitedhealthcare-ceo-ai-driven-cost-inflation-not-going-to-be-persistent/ | [I-利害方] 二手 | SCOUT@CL SCOUT-GEN |
| 2026-10-23 | 2026-10-22 | Meta 2026Q3 資本支出（含融資租賃本金償付） | 34.91 | 十億美元／季 | https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm | [V] 一手 | SCOUT@CL SCOUT-WATCH |
| 2026-10-23 | 2026-10-22 | Meta 2026-09-30 Servers and network assets 帳面原值（2025-12-31 為 98,040） | 133626 | 百萬美元 | https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm | [V] 一手 | SCOUT@CL SCOUT-WATCH |
| 2026-10-23 | 2026-10-22 | Meta 2026Q3 物業與設備折舊費用（2025Q3 為 4.76） | 6.81 | 十億美元／季 | https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm | [V] 一手 | SCOUT@CL SCOUT-WATCH |
| 2026-10-23 | 2026-07-31 | AWS 與 Anthropic 於 Q2 2026 宣布擴大既有多年承諾逾 1,000 億美元、為期 10 年，含 AWS 晶片效能相關合約義務（AMZN 10-Q 期末 2026-06-30） | 100 | 十億美元（下限） | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm | [I-利害方] 一手 | SCOUT@CL SCOUT-WATCH |
| 2026-10-23 | 2026-07-31 | AWS 與 OpenAI 於 Q1 2026 宣布將既有 380 億美元多年承諾擴大 1,000 億美元、為期 8 年（AMZN 10-Q 期末 2026-06-30） | 100 | 十億美元 | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm | [I-利害方] 一手 | SCOUT@CL SCOUT-WATCH |
| 2026-10-23 | 2026-07-31 | Amazon 對 Anthropic 提供上限 200 億美元之融資安排，依算力交付里程碑開放提領，以新可轉債或 IPO 後普通股形式發行（AMZN 10-Q 期末 2026-06-30） | 20 | 十億美元（上限） | https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm | [I-利害方] 一手 | SCOUT@CL SCOUT-WATCH |
| 2026-10-23 | 2026-09-17 | CoreWeave 2026 Q3 新簽短期（約3–6個月）客戶合約定價約每MW 4,000萬美元（年化收入÷相關叢集所需電力） | 40 | 百萬美元/MW（年化收入） | https://investors.coreweave.com/news/news-details/2026/CoreWeave-Continues-to-Contract-New-Compute-Capacity-at-Higher-Prices/default.aspx | [I-利害方] 一手 | SCOUT@CL SCOUT-WATCH |
| 2026-10-23 | 2026-07-30 | AXT 2026 Q2 磷化銦（InP）基板營收創史高，管理層稱需求來自 800G／1.6T 光模組、需求超過供給 | 30.7 | 百萬美元（季） | https://www.fool.com/earnings/call-transcripts/2026/07/30/axt-axti-q2-2026-earnings-call-transcript/ | [I-利害方] 二手 | SCOUT@CL SCOUT-GEN |
| 2026-10-23 | 2026-06-16 | JX Advanced Metals 計畫至 FY2030 於茨城兩廠投資約 1,200 億日圓，InP 產能擴至 FY2025 之 7–10 倍，以因應 AI／CPO 需求 | 120 | 十億日圓 | https://www.trendforce.com/news/2026/06/16/news-jx-advanced-metals-to-invest-jpy-120b-through-fy2030-expand-inp-capacity-up-to-10x-as-cpo-demand-accelerates/ | [I-利害方] 二手 | SCOUT@CL SCOUT-GEN |
| 2026-10-23 | 2026-07-29 | AXT 與 Lumentum 簽訂 InP 基板產能保留協議至 2031-12-31，Lumentum 付兩筆各 4,350 萬美元存款作出貨抵用（第二筆條件 2028 年訂） | 87 | 百萬美元（存款合計） | https://www.sec.gov/Archives/edgar/data/0001051627/000143774926024883/ex_993544.htm | [I-利害方] 一手 | ANALYST@CL Q-0093 |
| 2026-10-23 | 2026-08-17 | Lumentum FY26（至 2026-06-27）淨營收，Components 成長 78% 來自雷射晶粒與雷射組件出貨爬坡 | 3014.0 | 百萬美元（年） | https://www.sec.gov/Archives/edgar/data/1633978/000162828026057358/lite-20260627.htm | [I-利害方] 一手 | ANALYST@CL Q-0093 |
| 2026-10-23 | 2026-07-03 | 住友電工計畫投資約 180 億日圓，FY2028 前將 InP 基板產能提升至 FY2024 之 3.1 倍（未揭露片數） | 18 | 十億日圓 | https://technews.tw/2026/07/03/sumitomo-electric-industries-raised-inp-capex/ | [I-利害方] 二手 | ANALYST@CL Q-0093 |
| 2026-10-24 | 2026-07-24 | PUCT 於 Docket 59220 附條件核准 SB 6 首件淨額安排：既有 265.5 MW 風場（Goodnight）後接擬建 260 MW AI 資料中心，輸電緊急時須全斷 | 260 | MW（資料中心負載） | https://www.whitecase.com/insight-alert/puct-affirms-curtailment-authority-over-co-located-data-centers-first-net-metering | [V] 二手 | SCOUT@CL SCOUT-GEN |
| 2026-10-24 | 2026-08-05 | Talen 依修訂 AWS PPA 以 front-of-the-meter 模式向 AWS 資料園區供電至多 1,920 MW 至 2042，轉換於 2026-04 完成 | 1920 | MW | https://www.sec.gov/Archives/edgar/data/1622536/000162253626000066/tln-20260630.htm | [I-利害方] 一手 | SCOUT@CL SCOUT-GEN |
| 2026-10-24 | 2026-10-15 | TSMC 3Q26 合併營收 US$46.72B（年增 41.2%）；新聞稿無先進封裝／CoWoS 分列 | 46.72 | 十億美元（季營收） | https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm | [V] 一手 | SCOUT@CL SCOUT-GEN |
| 2026-10-24 | 2026-04-16 | 法人估 TSMC CoWoS 月產能 2026 年底約 11.5–14 萬片、2027 年約 17 萬片（TechNews 轉述，TrendForce 報導） | 170000 | 片／月（2027 估） | https://www.trendforce.com/news/?p=56168 | [D] 二手 | SCOUT@CL SCOUT-GEN |
| 2026-10-24 | 2026-04-28 | CoWoS 單片晶圓 ASP 約 1 萬美元，先進封裝約占 TSMC 2025 年營收 10%（Commercial Times 轉述） | 10000 | 美元／片 | https://www.trendforce.com/news/2026/04/28/news-tsmc-cowos-wafer-asp-reportedly-nears-7nm-levels-advanced-packaging-poised-to-become-a-key-profit-driver/ | [I-利害方] 二手 | SCOUT@CL SCOUT-GEN |
| 2026-10-24 | 2026-08-26 | NVIDIA 供應與產能承諾截至 2026-07-26 達 US$279B（前一季 US$119B；10-Q Note 10） | 279 | 十億美元（承諾總額） | https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm | [V] 一手 | ANALYST@CL Q-0096 |
| 2026-10-24 | 2026-07-13 | Morgan Stanley 估全球 CoWoS 需求 2026 年約 139.4 萬片、2027 年約 269.4 萬片；同報 2027 年 Rubin／Rubin Ultra 出貨近 700 萬顆（TechNews 轉述） | 2694000 | 片／年（2027 估） | https://technews.tw/2026/07/13/the-significant-increase-in-chip-demand-in-2027-will-boost-the-size-of-the-wafer-foundry-and-advanced-packaging-markets/ | [D] 二手 | ANALYST@CL Q-0096 |
| 2026-10-24 | 2026-09-14 | TSMC CoWoS 月產能 2026 年底約 13 萬片、2028 年底約 26 萬片（經濟日報經 Wccftech、TrendForce 轉述） | 260000 | 片／月（2028 年底估） | https://www.trendforce.com/news/2026/09/14/news-tsmc-reportedly-targets-22-2nm-16-3nm-capacity-boost-by-mid-2027-cowos-to-double-by-2028/ | [D] 二手 | ANALYST@CL Q-0096 |
| 2026-10-24 | 2026-07-24 | Intel Arizona SCIP（Brookfield 49%；18A）已投入服務之 PP&E 截至 2026-06-27 為 13.8B 美元、在建 6.0B（10-Q 2Q26 Note 3） | 13.8 | 十億美元（已投入服務 PP&E） | https://www.sec.gov/Archives/edgar/data/50863/000005086326000157/intc-20260627.htm | [V] 一手 | SCOUT@CL SCOUT-GEN |
| 2026-10-24 | 2026-07-24 | Intel 於 2026-04-08 以 14.2B 美元現金買回 Apollo 於 Ireland SCIP（Fab 34）之 49% 權益（10-Q 2Q26） | 14.2 | 十億美元（買回對價） | https://www.sec.gov/Archives/edgar/data/50863/000005086326000157/intc-20260627.htm | [V] 一手 | SCOUT@CL SCOUT-GEN |
| 2026-10-24 | 2026-07-24 | Intel Foundry 外部客戶營收 2Q26 為 293M 美元（主因 Altera 分拆後轉為外部客戶）；代工總營收 5,765M、營業損失 2,089M（10-Q 2Q26 分部附註與 MD&A） | 293 | 百萬美元（季，外部營收） | https://www.sec.gov/Archives/edgar/data/50863/000005086326000157/intc-20260627.htm | [V] 一手 | SCOUT@CL SCOUT-GEN |
| 2026-10-24 | 2026-10-15 | TSMC 重申 2026 全年資本預算 60–64B 美元；4Q26 毛利率指引 65–67%；海外廠 2026 毛利稀釋近 2%、未來數年擴至 3–4%（3Q26 法說，二手逐字稿） | 64 | 十億美元（2026 資本預算上緣） | https://www.earningswhispers.com/transcript/TSM/Q32026 | [I-利害方] 二手 | SCOUT@CL SCOUT-GEN |
| 2026-10-24 | 2026-10-16 | ERCOT：截至 2026-09，已獲 Approval to Energize 之大型負載累計 9,456 MW；9 月非同時月峰值用電 4,132 MW（ERCOT 月度營運概覽 2026-09） | 9456 | MW（核准送電之大型負載累計） | https://www.ercot.com/files/docs/2026/10/16/ERCOT-Monthly-Operational-Overview-September.pdf | [V] 一手 | SCOUT@CL SCOUT-WATCH |
| 2026-10-24 | 2026-10-07 | Applied Digital HPC Hosting 分部 3 個月（至 2026-08-31）營收 262.6M 美元、分部利潤 33.4M 美元（10-Q 分部附註） | 33.431 | 百萬美元（季，分部利潤） | https://www.sec.gov/Archives/edgar/data/1144879/000114487926000059/apld-20260831.htm | [V] 一手 | SCOUT@CL SCOUT-WATCH |
| 2026-10-24 | 2026-10-23 | Western Digital FQ1 2027（截至 2026-10-02）Cloud 終端市場營收（雲端／企業 HDD） | 3868 | US$ 百萬／季 | https://www.sec.gov/Archives/edgar/data/106040/000162828026066933/wdc-20261002.htm | [V] 一手 | SCOUT@CL SCOUT-WATCH |
| 2026-10-24 | 2026-10-23 | Western Digital FQ1 2027 Cloud 營收年增，管理層歸因 exabyte 出貨增逾 20%、每 exabyte ASP 增約 25% | 54 | % 年增 | https://www.sec.gov/Archives/edgar/data/106040/000162828026066933/wdc-20261002.htm | [V] 一手 | SCOUT@CL SCOUT-WATCH |
