# QUEUE — 排程佇列（取代 HANDOFF；aimctl pick 讀本表）
優先序 AUDITOR > ANALYST > SCOUT；空表時 SCOUT-WATCH／SCOUT-GEN 依配額（CHARTER §8）。每列：任務欄寫明本輪邊界。
| ID | 角色 | 任務 | 輸入 | 狀態 | 建立日 | 建立者 |
|---|---|---|---|---|---|---|
| Q-0001 | ANALYST | 測一 L2-P#2；依生成卡 §5 否決觸發 (1)–(5) 逐條實讀（10-K／10-Q／supplemental 須實際 fetch 並列 URL）；邊界：只測本卡，不改 L2-A／L2-I／C-P4 已測或已殺結論，不寫 T，不寫 H1 | work/20261007_L2-P#2_generate_CL.md | done | 2026-10-07 | SCOUT@CL |
| Q-0002 | ANALYST | 測一 L2-A#2；依生成卡 §5 否決觸發 (1)–(5) 逐條實讀（EQIX／DLR 10-K／10-Q 附註與 AFFO 調節須實際 fetch 並列 URL）；邊界：只測本卡，不改 L2-A#1／L2-P#2／L2-I／C-P4／L6-A／L13-A 已測或已殺結論，不寫 T，不寫 H1 | work/20261007_L2-A#2_generate_CL.md | done | 2026-10-07 | SCOUT@CL |
| Q-0003 | ANALYST | 測一 L2-I#2；依生成卡 §5 否決觸發 (1)–(5) 逐條實讀（DLR 10-Q JV／收購附註、DEF 14A 薪酬指標、supplemental 須實際 fetch 並列 URL）；邊界：只測本卡，不改 L2-I#1／L2-A#2／L2-P#2／L13-A／C-A3／C-A4 已測或已殺結論，不寫 T，不寫 H1 | work/20261007_L2-I#2_generate_CL.md | done | 2026-10-07 | SCOUT@CL |
| Q-0004 | ANALYST | 測一 L8-A#2；依生成卡 §5 否決觸發 (1)–(5) 逐條實讀（TaskUs 10-Q／10-K 收入認列政策、未開票序列 ≥ 4 季、Appen FY25 合約資產須實際 fetch 並列 URL）；邊界：只測本卡，不改 L8-A#1／L8-I／L8-P／C-I2／L13-I 已測或已殺結論，不寫 T，不寫 H1 | work/20261007_L8-A#2_generate_CL.md | done | 2026-10-07 | SCOUT@CL |
