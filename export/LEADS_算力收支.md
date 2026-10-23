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
