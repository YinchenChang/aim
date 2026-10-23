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
