<!-- BY: PM@GK | MODEL: Grok Build【自報】 | CHARTER: AIM-C1.1 | NOTE: CL 不可用，GK 代行 PM（載入器 §3）；未追認之代行決定不生效，本檔留 work/，不寫入正本 | CONSUMES: 1aY6etUFtEzzDN0wm2neABQ864RIyPk4W；12K5eqBNP6OMkM_c35ko4hqO8vMDbPuBi；1FcrhXNs53jWu_8fFFlezc86uZvd3EqXI；17pxTe8XkUvYInPgOf8rKq8d7CAHPiQkd；1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h；1uKfYqf1Dr3uyMTI84Sgq0Pw2gU4Ldlmm；1B5V0Xl5GV_2BaiSAV0e5P7jVKsZEP9GV；15S4oei2plGVif8eDxP0nm25Suqa7lQ3w | EMITS: 本檔；20260916_aim_GK.py（整份修補，取代本機 AIM/aim.py 同一 fileId，禁新建同名正本） -->
# aim.py 修補｜MECH／LEDGER 路徑＋根目錄 stray 代移

**日期：** 2026-09-16　**地位：** work 擬稿（使用者覆寫本機後生效）  
**正本：** Drive `AIM/aim.py` fileId `1aY6etUFtEzzDN0wm2neABQ864RIyPk4W`（27,355 B，2026-09-16T00:10:36Z）  
**修補檔：** 同目錄 `20260916_aim_GK.py`（32,127 B）。**禁止**在 AIM 根目錄再上傳一份 `aim.py`（禁雙 fileId）。

## Drive 現況（本輪列夾，非 FUNNEL 狀態欄）

| 位置 | 檔 | fileId | 判定 |
|---|---|---|---|
| `query/` | MECH.md | `1LvUn7mhWHYdMmcyyMl5k_dbdtGyC0Z7h` | 正本（心跳 2026-09-16T00:13:11Z） |
| `pm/` | LEDGER.md | `1uKfYqf1Dr3uyMTI84Sgq0Pw2gU4Ldlmm` | 正本（0 B，標頭未寫入） |
| **AIM 根** | MECH.md | `1B5V0Xl5GV_2BaiSAV0e5P7jVKsZEP9GV` | **stray**（2026-09-15T23:35:29 新建；內容＝心跳） |
| **AIM 根** | LEDGER.md | `15S4oei2plGVif8eDxP0nm25Suqa7lQ3w` | **stray**（0 B；前輪已移之根 stray 被 sync 重建） |
| `old/` | STRAY_root_MECH.md | `1Yaubrp7eHIGkuncF2L8HTNaBcaqZTqRS` | 前輪已移 |
| `old/` | STRAY_root_LEDGER.md | `1RT1b3EoOjq79FykOJIQ1mEsfKd5TJQj1` | 前輪已移 |
| `work/` | 未結案 | `1tUgqv0yjmf05548nFnobMsa5EvHFdhov`；`1aKgwxslikOV-2Bk5yUsUlACM6EqDtdd2` | C1.1 稽核；LEDGER 標頭擬稿 |

FUNNEL §5-4 寫「根目錄 stray 已移 old／已完成」。**現況否證：** 根目錄兩 stray 仍在。死因＝`sync` 路徑，不是漏搬一次。

## 根因（腳本不做判斷；此段是機械層缺陷）

`cmd_sync` 於 Drive 桌面版掛載之 AIM 根目錄寫檔，桌面版建成**第二個 fileId**：

1. LEDGER：`path = ROOT / "LEDGER.md"`，正本卻是 `pm/LEDGER.md`。
2. MECH：`mech_path = ROOT / "MECH.md"` 後 API 更新 `query/MECH.md`——本地根檔仍被桌面版上傳。

前輪 PM 代移後，下一次 `sync` 立刻重建。只搬不改路徑＝循環。

## 修補（已寫入 `20260916_aim_GK.py`）

- `canon_path`：CHARTER／FUNNEL＝根；LEDGER＝`pm/LEDGER.md`。
- MECH：`tempfile`＋API 更新 `query/`，**不寫** `ROOT/MECH.md`。
- `_retire_local_root_strays`：本機根 `MECH.md`／`LEDGER.md` → 本地 `old/STRAY_root_*`。
- `_sweep_root_strays`：AIM 根同名且 fileId ≠ 正本 → 改名 `STRAY_root_*` 移 `old/`（重名加 `_2`）。不 `trash`。
- `init` 建本地 `pm/`、`query/`。
- 單元測試 5 項通過（路徑、唯一名、本地移、Drive 掃只動非正本）。

未改：`cmd_ledger` 仍寫 `out/LEDGER.md`；PM 自動推仍 `drive_update(ledger_file_id)`。`aim_config.json` 不新建。

## 處置

| 項 | 值 |
|---|---|
| Project | AIM |
| 取代 | 本機／Drive `AIM/aim.py` 同一 fileId `1aY6etUFtEzzDN0wm2neABQ864RIyPk4W` |
| 是否 `aim.py sync` | **是**（覆寫本機後跑一次，代移現存 stray） |
| 正本 | 本輪不 `drive_update` aim.py（GK 無 media update；禁新建同名） |

**（完）**
