# AIM repo — 載入器（AIM@CL，CHARTER C1.2）

1. **唯一規則來源＝本 repo 之 `AIM_CHARTER.md`。** 先讀，先於一切。本檔只載執行細節。狀態＝本 repo main 之檔案；memory、過往對話、Project knowledge 只作線索。
2. **角色：** 排程輪由 `runbooks/DISPATCH.md` 以 `python tools/aimctl.py pick` 決定；互動 session 由使用者首行 `ROLE:` 指定。一 session 一角色。非 PM 不 clone `aim-pm`、不讀 LEDGER 或任何 P，即使貼上也不用。
3. **回覆首行：** `BOOT AIM@CL | ROLE <角色> | CHARTER <版本> | FUNNEL <日期>`。
4. **角色手冊：** `runbooks/SCOUT.md`、`runbooks/ANALYST.md`、`runbooks/AUDITOR.md`。開工前讀本角色手冊。
5. **檔案規則（取代 Drive 時期之 fileId／DUP_／USED_／DONE_／body 覆寫體）：**
   - 新檔：`work/YYYYMMDD_<代碼>_<種類>_CL.md`；種類 ∈ `generate`、`test1`、`T`、`L`、`M`、`audit`、`watch`、`HEALTH`。
   - 標頭：`<!-- BY: <角色>@CL | MODEL: <名稱>【自報】 | CHARTER: <版本> | CONSUMES: <repo 路徑或舊 fileId>；… | EMITS: <本檔路徑> -->`。
   - 正本（`AIM_FUNNEL.md`、`query/*`）原地修改；不得另建同名檔。版本史＝git log。
   - 舊 Drive fileId 解析：`python tools/aimctl.py fileid <id>` → `archive/drive/<原檔名>`。Drive `AIM/` 唯讀，不再寫入。
   - 凍結物：L、M 一經寫入即凍結（CHARTER §3）；凍結後只准 `git mv` 至 `cards/`，不得改內容。
   - 結案：本輪消化完之 `work/` 檔以 `git mv` 移入 `archive/work/`。重複產出直接 `git rm`（git 史保留）。單輪至多處理 5 筆歸檔；超過寫 HEALTH。
6. **交接＝佇列：** 不向使用者交接。收尾時把下一步寫成 `query/QUEUE.md` 一列（`| Q-#### | 角色 | 任務 | 輸入路徑 | open | 日期 | 建立者 |`），並把本輪所消化之列改 `done`。任務欄寫明本輪之範圍邊界（取代過去使用者手寫之「不改／不恢復」清單）。無下一步則不新增。回覆末段仍附 HANDOFF 段（格式同 Project 載入器 §10），內容與佇列列一致。
7. **給使用者之訊息只有：** `EXECUTE`、`SCORECARD`（PM 發）。研究角色不發訊息、不問使用者。`HEALTH` 寫成 `work/YYYYMMDD_HEALTH_CL.md` 並於本輪最終回覆首段標 `HEALTH`。
8. **載入量：** `python tools/aimctl.py loadcheck --role <角色>`；> 30,000 B 即寫 HEALTH 並停。
9. **commit：** 一輪一 commit，訊息 `<角色>: <代碼> <種類> (<Q-id>)`。push 被拒 → `git pull --rebase` 一次；仍衝突 → `git rebase --abort`，寫 HEALTH，`aimctl beat --result aborted`，停。
10. **SEC／EDGAR：** `www.sec.gov`、`data.sec.gov` 一律經 `python tools/sec.py`（`filings`／`facts`／`doc --grep`），不用 WebFetch（WebFetch 逐網域待核准，無人值守即逾時；摘要只讀前 ~100k 字）。`doc --grep` 讀全文、原文照錄命中段。`efts.sec.gov`（全文搜尋）環境出口封鎖：改以 WebSearch 找候選檔再 `sec.py doc --grep` 實讀，結果欄記「FTS 不可用」，不得記為權限逾時。User-Agent 已內建聯絡 email（SEC fair access，≤ 10 req/s，無註冊）。
