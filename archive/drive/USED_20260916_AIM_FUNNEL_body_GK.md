<!-- BY: PM@GK | MODEL: Grok Build【自報】 | CHARTER: AIM-C1.1 | NOTE: CL 不可用，GK 代行 PM | CONSUMES: AIM_FUNNEL.md 1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；work/20260915_L8-P_audit_CL.md | EMITS: FUNNEL 正本擬稿；須 drive_update 同一 fileId 1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；禁止新建同名檔 -->
# AIM_FUNNEL — 候選漏斗（共用；Drive `AIM/AIM_FUNNEL.md` 為唯一正本，兩 Project 逐位元相同）

<!-- BY: PM@GK | MODEL: Grok Build【自報】 | CHARTER: AIM-C1.1 | NOTE: CL 不可用，GK 代行 PM -->
**日期：** 2026-09-16　**寫入者：** SCOUT 主、PM 可改狀態欄與 §5　**上限：** 6,000 B
**⚠ 本檔無金額、無部位、無尺碼。** 准入門檻與量綱見 CHARTER §1。任一平台改本檔＝`aim.py sync` 原地更新同一 fileId，再覆到兩 Project knowledge；禁止只改 knowledge。

## 1. 現役候選（依 §1 准入門檻重判前，狀態欄一律【待重判】）

| 代碼 | 層 | 落差一句 | 狀態 | 下一動作 | 角色 |
|---|---|---|---|---|---|
| L9-P | 受規管產業 HITL 申報 | 翻轉事件為具日期之申報揭露 | 【待重判】序數型 | 同 L8-P 流程；申報日期 `[V]` 化；須在 §5-2 之後 | ANALYST@GK |
| L2-A | 資料中心實體：會計恆等 | 測一不過 | **已測｜不進 T**（測二 2026-09-13：`work/20260913_L2-A_test2_cost-index_GK.md`；T&T 指數僅弱支持冷卻佔比對熱密度之非線性，缺可單位化連續參數；狀態衝突已解） | 表達點 (ii)(iii) 未派；升級需新生成物 | ANALYST@GK |
| L2-I | 資料中心實體：誘因 | 【未研究】 | — | 生成 | SCOUT@GK |

## 2. 已殺（可回復者附觸發器；完整記錄在 `query/ARCH_dead.md`）

| 代碼 | 死因類別 | 複查觸發器 |
|---|---|---|
| L8-P 標註／驗證業者經濟 | 表達層／可觀測性（機制未被否證） | 任一標註／驗證供應商於財報或監理申報揭露「每條交付平均人工分鐘數」，或 AI 法規附則要求訓練資料人工審核工時揭露 |
| L11-P 人類注意力 | 結構性不可表達（主導貨幣化主體私有） | 任一主導主體上市或分部揭露消費級 AI 損益 |
| C-A4／C-A3／C-A1 | (c) 工具屬性／否／可分離性 | 見 `query/ARCH_dead.md` |
| 能力上限／Confidential／自動化 R&D | 08-26 中止 | — |
| VEEV | P1 無外部具名反方 | 出現具名反方論述 |
| T-15 CoreWeave 空方 | **委託資本外**（C1.0 §9-2，記於 `query/CHARTER_HIST.md`），非殺 | 不適用 |

**已死落差母體：17（`query/ARCH_dead.md`）。** L8-P 2026-09-16 入本表（AUDITOR@CL 維持；work `1Mnfp4T_GBgYjz1t6sObEVyVPnWM5B96h`）。

## 3. 未生成格（層 × [P][A][I]；SCOUT 逐格填，填不出標【未生成】）

| 層 | [P] | [A] | [I] |
|---|---|---|---|
| L2 資料中心實體 | 已測 | 見 §1 | 【未生成】 |
| L3 半導體製造測試 | 【未生成】（台股禁；日韓待複委託費率） | 【未生成】 | 【未生成】 |
| L4 運算硬體系統 | 【未生成】 | 【未生成】 | 【未生成】 |
| L8 標註／驗證 | 已殺 | 【未生成】 | 待重判 |
| L9 受規管 HITL | — | — | 待重判 |
| 其餘層 | 依 `query/ARCH_matrix.md` 45 格（探索輪已執行） | | |

## 4. 本季計數（SCORECARD D 節用）
生成 0／殺 1（L8-P：AUDITOR@CL 2026-09-15 維持不過／殺）／升級 0／准入拒絕 0（起算日前不計）。

## 5. 起算前未完成項（CHARTER §8；完成即刪，依序）

| # | 項 | 做者 | 驗收 |
|---|---|---|---|
| 1 | 漏斗單一正本：Drive ←→ knowledge 對齊；§1 L2-A 衝突**已解** | 使用者 `aim.py sync` | 兩 Project knowledge 與 Drive 三份位元組相同（尚待驗證）；本輪 body 待 `drive_update` `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI` |
| 2 | `query/` 最低集：`INDEX.json`、`ARCH_dead.md`（17 條各一行）、`ARCH_matrix.md`（45 格）、`MECH.md`、`CHARTER_HIST.md` | 使用者自 Archive 之 `ARCH_3*`／`ARCH_4*` 摘出 | 五檔存在但 INDEX 各代碼 `fileId` null、dead／matrix 為骨架；SCOUT 按代碼取回仍失敗 |
| 3 | `aim.py`：`sync` 寫 MECH 心跳；非 PM 不下載 `AIM/pm/`；`score` 實作 §3.3 與 §2-4 季切 | 使用者本機 | `query/MECH.md` 有 UTC（**已完成** 2026-09-15） |
| 4 | LEDGER 移至 `AIM/pm/LEDGER.md` | 使用者 | 正本 `1uKfYqf1Dr3uyMTI84Sgq0Pw2gU4Ldlmm`；根目錄 stray 已移 old（**本輪完成**） |
| 5 | L8-P 重判＋AUDITOR@CL **維持**（不過／殺）**已交**；L9-P 重判 work 檔（在 #2 之後） | ANALYST@GK；AUDITOR@CL | L8-P 1／2 已交且維持；L9-P 未交 |
| 6 | C1.1 稽核：AUDITOR@GK 對 §1 量綱表與 §3.3 只准否決或維持 | AUDITOR@GK | 一份 ≤ 2 KB 稽核檔 |
| 7 | 起算日 EXECUTE：資本轉入單＋預設袋建倉單（ETF 已指定 VTI 70／IBIT 30，見 `work/20260916_LEDGER_header_GK.md`；10-15 出單） | PM | EXECUTE 一份 |

**（AIM_FUNNEL 結束。）**
