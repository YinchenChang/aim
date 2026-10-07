# DISPATCH — 排程輪（每小時＋自動續跑；CHARTER C1.2 §8）

無人在場。不問問題、不等核可；不可逆且兩可之決定（刪正本、改章程）一律不做，寫 HEALTH 後停。

1. **取得 repo：** `add_repo` YinchenChang/aim（access=push）並 clone 至 `/home/claude/aim`。**不得** attach 或 clone `aim-pm`。
2. **讀：** `CLAUDE.md` → `AIM_CHARTER.md` → `AIM_FUNNEL.md`。
3. **選角：** `python tools/aimctl.py pick`。
   - `SKIP` → 最終回覆一行 `SKIP <理由>`，結束（不 commit）。
   - `IDLE` → `aimctl beat --role IDLE --task - --result idle`；commit `IDLE: heartbeat`；push；最終回覆一行 `IDLE`。
   - 其餘 → `aimctl lock --role <role>`（exit 3＝他輪持鎖 → 同 SKIP）。
4. **執行：** 讀 `runbooks/<ROLE>.md`，依 pick 之 `kind`／`queue` 做**一件事**。
   - kind=`SCOUT-WATCH`／`SCOUT-GEN` → SCOUT.md 對應節。
   - kind=`ANALYST` → ANALYST.md。
   - kind=`AUDITOR` → AUDITOR.md（必須以子代理、異模型族執行）。
5. **收尾：** 更新 `query/QUEUE.md`（本列 done、下一步新列）→ 必要之正本對齊（FUNNEL／ARCH_matrix／INDEX，只改本輪觸及之列）→ `aimctl unlock` → `aimctl beat --role <kind> --task <代碼/Q-id> --result <ok|health|aborted>` → `git add -A && git commit` → push（規則見 CLAUDE.md §9）。
5b. **自動續跑：** push 成功後跑 `python tools/aimctl.py chain`；印 `yes` → 呼叫 `fire_trigger`（trigger_id `trig_01Edy1VZpk5FzcFKtYDsoJEi`，text「chain」），成功後 `aimctl beat --role CHAIN --task <Q-id> --result ok` 並 commit＋push；`fire_trigger` 不可用或被拒 → 不重試，等下一個整點。
6. **最終回覆：** 首行 BOOT 行；次行一句本輪做了什麼（代碼、檔名、終態）；有 HEALTH 時另起一段以 `HEALTH` 開頭；末段 HANDOFF。不得含金額、部位、尺碼。
7. **失敗：** 任何步驟無法完成 → 保留已寫之 work 檔、寫 `work/YYYYMMDD_HEALTH_CL.md`（只准：不一致之路徑、缺檔、MECH 心跳距今、宿主開銷）、unlock、beat `--result health`、commit、push。
