# AUDITOR@CL 手冊（CHARTER §4、§7-11：只准否決或維持）

**獨立性（C1.2）：** 稽核者模型族 ≠ 撰寫者模型族，且不讀撰寫者對話。排程主 session 只做調度，**不得自己稽核**。

1. 由 QUEUE 列取得目標 L／M 路徑與撰寫者 MODEL（亦見檔頭 `MODEL:`）。
2. 選稽核模型：撰寫者含 `Opus` → `fable`；含 `Fable` 或 `Mythos` → `opus`；含 `Sonnet` → `opus`；其他（含舊 GK 檔）→ `opus`。若可用模型無一與撰寫者不同族 → 寫 HEALTH，停。
3. 以 Agent 工具（`model`＝上一步結果，`subagent_type`＝general-purpose）啟動子代理，prompt 只給：
   - 路徑：`AIM_CHARTER.md`、目標 L、目標 M、該碼 T（若有）——讀檔請子代理自行 Read；
   - 任務：「對 L 之 `H1`／`H5` 與 M 之每一日期 `[V]` **獨立重算**；須實際 fetch 並列 URL；只准輸出『維持』或『否決』＋逐項理由；不得修改 L／M、不得提出替代數值作為新 L。結果寫入 `work/YYYYMMDD_<碼>_audit_CL.md`，標頭 `BY: AUDITOR@CL | MODEL: <你自報>`。」
   - 不得把本 session 之對話、撰寫者之推理、或 ANALYST 之 work 筆記貼給子代理。
4. 子代理回來後，主 session 只核對：audit 檔存在、標頭 MODEL 族 ≠ 撰寫者、終態 ∈ {維持, 否決}。不符 → HEALTH。
5. 維持 → `git mv` L、M 至 `cards/`；FUNNEL §1 該碼「L／M 凍結｜稽核維持」；QUEUE 不新增（P 屬 PM，非排程）。否決 → FUNNEL 標「稽核否決」、L／M 移 `archive/work/`；QUEUE 不新增。
