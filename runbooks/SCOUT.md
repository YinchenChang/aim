# SCOUT@CL 手冊（CHARTER §4：候選生成；不做尺碼、不知金額）

固定載入：`AIM_CHARTER.md`＋`AIM_FUNNEL.md`。`query/` 按需取 ≤ 8 KB。禁 LEDGER、任何 P、`aim-pm`。

## A. 佇列任務（kind=SCOUT，pick 回傳 queue 列）
照該列「任務」欄做，邊界以該列為準。完成後把列改 done。

## B. SCOUT-WATCH：複查觸發器掃描（配額 4 輪／日）
目的：把已殺／不進 T 之候選的**複查觸發器**變成可觀測的定期檢查（CHARTER §7-2）。
1. 若 `query/RETRIG.md` 不存在：本輪只建它。來源＝`query/ARCH_dead.md` 全列＋`query/INDEX.json` 各碼之 `retrigger`＋`query/ARCH_live.md`（原 FUNNEL §1 全列）與 `AIM_FUNNEL.md` §2 之複查觸發器。表頭：`| R-## | 代碼 | 觸發器（原文照錄） | 可觀測來源（URL 或申報類別） | 最近檢查日 | 結果 |`。觸發器只照錄，不改寫、不補定義。≤ 8 KB；超過則拆 `RETRIG_2.md`。
2. 否則：取 `最近檢查日` 最舊之 **3 列**，逐列實際 fetch（WebSearch／WebFetch；SEC 一律 `python tools/sec.py`（`filings`／`facts`／`doc --grep`；見 CLAUDE.md §10），EDGAR full-text 不可用），列 URL 與日期。
3. 每列結果只三種：`未觸發`／`觸發`／`無法判定（失敗歸因）`。檢索失敗不是存在性主張（§7-2）。
4. 有 `觸發` → 寫 `work/YYYYMMDD_<代碼>_watch_CL.md`（觸發器原文、證據 URL、為何算觸發），並於 QUEUE 新增 `ANALYST` 列：「重測 <代碼>：以 watch 檔之新證據重跑測一；不改他碼」。
5. 更新 RETRIG 表之該 3 列日期與結果（原地改）。

## C. SCOUT-GEN：新生成（配額 2／日）
1. 讀 `query/ARCH_matrix.md`。若有【未生成】或「已生成未測」格 → 先做該格。
2. 全表已測時：取「最後測試日最舊」且非「已殺／刻意排除」之格，生成**該格第 n 份**候選（代碼 `<格>#n`，n＝該格既有生成數＋1）。必須與該格既往候選與 `ARCH_dead` 之死因**型態不同**；生成卡 §0 列出比對過之舊檔路徑。
3. 格選定後，可以 `python tools/tokenomics_leads.py <格之關鍵詞>` 找 B 端載體線索（CLAUDE.md §11；只作線索，須回原文實讀）。生成卡：`work/YYYYMMDD_<格>#n_generate_CL.md`，結構沿用 `archive/drive/USED_*_generate_GK.md`：§0 範圍、落差一句、機制型態［P／A／I］、B 端可觀測載體（只指名）、否決觸發 (1)…(k)、不寫 H1。
4. 終端篩選條件不得在生成階段執行（§7-3）；不得由目標反推（§1）。
5. QUEUE 新增 `ANALYST` 列：「測一 <格>#n；依生成卡否決觸發逐條實讀」。ARCH_matrix 該格標「已生成 #n」。

## 收尾
FUNNEL §3 與 ARCH_matrix 只改本輪觸及之格。依 DISPATCH §5 commit。
