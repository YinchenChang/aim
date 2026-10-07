<!-- BY: PM@GK | MODEL: Grok Build【自報】 | CHARTER: AIM-C1.1 | NOTE: CL 不可用，GK 代行 PM（載入器 §3） | CONSUMES: AIM_CHARTER.md 12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi；AIM_FUNNEL.md 1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；query/MECH.md 1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；aim_config.json 17pxTe8XkUvYInPgOf8rKq8d7CAHPiQkd；work/20260915_L8-P_rejudge_GK.md 1m1gnD5EzVjT_WsLAoA9l8nQVJwVsrSGP；work/20260915_L8-P_audit_CL.md 1Mnfp4T_GBgYjz1t6sObEVyVPnWM5B96h；query/INDEX.json 1kEYOvaRkCIYNHWkMWfvc44zZCmMrjQhX | EMITS: FUNNEL 狀態欄與 §5 擬稿（正本須 drive_update 同一 fileId）；LEDGER 標頭擬稿；不發 EXECUTE（未屆起算日） -->
# PM@GK session 2026-09-16

**平台：** GK 代行 PM（CL 不可用）。正本仍為 Drive `AIM/`；本檔是 work，不是 FUNNEL／LEDGER 正本。
**GK 工具無 `files.update(media)`：** `aim.py sync` 只拉 FUNNEL、只推 `out/LEDGER.md`。本輪不新建同名正本（禁雙 fileId）。使用者下一次 `aim.py` 對 FUNNEL 做 `drive_update(funnel_file_id)`、對 LEDGER 做既有 PM 推送。

## 1. AUDITOR@CL 裁定已收

`work/20260915_L8-P_audit_CL.md`：**維持（不過／殺）**。死因＝表達層／可觀測性；機制未被否證；觸發器照 ARCH_3h 原文，不改寫。稽核者不動狀態欄，交本 session。

擬寫入 FUNNEL 正本（fileId `1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI`）之全文見同目錄 `20260916_AIM_FUNNEL_body_GK.md`。變更摘要：

- §1 刪 L8-P 列；§2 增 L8-P（觸發器原文）
- §3 L8 列校正：`[P]=已殺`／`[A]=【未生成】`／`[I]=待重判`（稽核附註 C）
- §4 殺 0→1
- §5-5 L8-P 半數完成；L9-P 仍待 #2 之後
- 不改觸發器（裁定「不改寫」優先於附註 B）

`USED_` 前綴：正本未 `drive_update` 前不加。

## 2. 預設袋 ETF（FUNNEL §5-7；寫入 LEDGER 標頭，非 EXECUTE）

CHARTER §2-6／§5：(a)＝預設袋兩支 ETF 總報酬。`aim_config.json` 現為 `VTI` 0.7 + `BTC-USD` 0.3。`BTC-USD` 非 §2-8 可交易 BTC ETF，預設袋與 (a) 會裂開。

指定（Firstrade 美股上市 ETF；流動性最大之現貨 BTC ETF）：

| 權重 | 代號 | 名稱 | 角色 |
|---|---|---|---|
| 0.70 | VTI | Vanguard Total Stock Market ETF | 美股寬基（≠ (b) 之 S&P 500 TR） |
| 0.30 | IBIT | iShares Bitcoin Trust ETF | BTC ETF |

再平衡＝§2-4 季切同日。擬稿見 `20260916_LEDGER_header_GK.md`。`aim_config.benchmark_a` 須改為同對（機械層，本輪不新建 config）。**不發 EXECUTE**（§8：資本轉入與預設袋建倉僅 2026-10-15）。

## 3. 本輪已搬（`update_file` parentId→`old/`；不 `trash`）

| 原位置 | fileId | 新名（old/） |
|---|---|---|
| `AIM/LEDGER.md`（根；0 B；非 config 正本） | `1RT1b3EoOjq79FykOJIQ1mEsfKd5TJQj1` | `STRAY_root_LEDGER.md` |
| `AIM/MECH.md`（根；正本在 `query/`） | `1Yaubrp7eHIGkuncF2L8HTNaBcaqZTqRS` | `STRAY_root_MECH.md` |

LEDGER 正本仍為 `AIM/pm/LEDGER.md` `1uKfYqf1Dr3uyMTI84Sgq0Pw2gU4Ldlmm`（0 B，待標頭）。

## 4. 未做（非本角色或缺機械寫入）

- FUNNEL／LEDGER／`aim_config` 正本原地更新（待 `aim.py` `drive_update`）
- FUNNEL §5-2 query 完稿（INDEX 各 `fileId` null；ARCH_dead／matrix 骨架）
- §5-6 C1.1 稽核＝AUDITOR@GK
- §5-7 EXECUTE＝2026-10-15

**（完）**
