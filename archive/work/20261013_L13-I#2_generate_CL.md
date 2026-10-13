# L13-I#2 生成卡｜資本與融資結構：誘因（租約擔保人以零價認股權取得出租方股權；違約時擔保人二擇一「付終止費」或「承接租約」，前者全數先償子公司有擔保票據、後者保留出租方股權價值——擔保人兼股東之選擇決定債權／股權間之分配）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/FILEIDS.tsv；archive/drive/USED_20261002_L13-I_generate_GK.md；archive/drive/USED_20261002_L13-I_test1_GK.md；archive/work/20261013_L13-P#2_generate_CL.md；work/20261013_L13-P#2_test1_CL.md；archive/work/20261011_L13-A#2_generate_CL.md | EMITS: work/20261013_L13-I#2_generate_CL.md -->
**日期：** 2026-10-13　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3→4／6）　**格：** L13-I　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L13-P#2 測一 2026-10-13，Q-0036 done）。非已殺／刻意排除且無 #2 之格中最後測試日最舊者：`archive/FILEIDS.tsv` L13-I 測一 2026-10-02T08:00Z，早於 L14-*／L15-*（10-05 起）→ **L13-I**。既有生成數 1 → #2。
- Tokenomics 線索（CLAUDE.md §11）：已查 `backstop`、`warrant`、`termination fee`、`Fluidstack`，1 筆（GPU 保固年限），與本格無關；未用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L13-I#1**（測一不通過，`archive/drive/USED_20261002_L13-I_test1_GK.md`）：供應商兼股東兼債權人之私有資訊 → 公開信評資訊含量；死因＝否決 (1)：同一客戶應收帳齡／信用損失分桶與股權餘額不可並列。本卡不涉信評、不涉應收帳齡；論的是**擔保人兼股東之違約分支選擇**，兩分支之受益層級在 indenture 與 10-Q 原文可見。
  - **L13-P#2**（測一部分通過，`work/20261013_L13-P#2_test1_CL.md`）：MW 互斥＋限制性支付閘。本卡不以 MW 或 RP 籃子為樞紐；取其已讀之 indenture §3.11（終止費 100% 強制贖回）為一側。
  - **L13-P#1**（熱循環 vs 會計年限）、**L13-A#1**（入表租賃≠義務上界）、**L13-A#2**（預付之重大融資成分）：不涉。
  - **C-A4／C-A3**（重定價窗／折舊樞紐）、**L6-I**（backlog 變厚≠對手方變好）：本卡不以年限、`k`、backlog 品質為樞紐；不重開。不寫 T-15 或任何 CRWV 表達。
- §7-10 領域最近公開：TeraWulf 10-Q 期末 2026-06-30（2026-08-05）；Cipher 10-Q 期末 2026-06-30（2026-08-04）；TeraWulf 8-K 2026-10-05。下一檢查點＝兩家 3Q26 10-Q（2026-11 初）與任一 Fluidstack 租約 Commencement 公告。

## 1. 落差一句

市場把「Google 擔保之 Fluidstack 租約」讀成以擔保人信用替代租戶信用之長約現金流，並以出租方股權承接其價值；種子主張擔保是**擔保人之選擇權**——租戶違約時擔保人於「付終止費」與「付清欠租並承接租約」間擇一，前者依 indenture 全數用於贖回子公司有擔保票據（股權只剩空置之建物），後者保留租約與股權價值；而擔保人同時以每股 0.01 美元之認股權持有出租方約一成餘股權，其分支選擇取決於「承接成本 vs 終止費 − 所持股權因分支而生之價值差」。錯價只在把擔保視為對股權之無條件全額租約保證。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | **誘因**：擔保人 G 於違約事件之選擇 \(b \in \{\text{fee}, \text{assume}\}\)；G 選 assume 若 \(C_{assume} - F < w\cdot\Delta E\)，\(F\)＝終止費、\(C_{assume}\)＝承接後租金現值扣 G 自用價值、\(w\)＝G 經認股權之持股比、\(\Delta E\)＝出租方股權於兩分支之價值差。fee 分支：\(F\) → 100% 強制贖回子公司票據；assume 分支：租約續存，D_sub／股權保留 |
| 選擇者 | 擔保人（Google）；出租方（是否發違約通知）；子公司票據持有人（僅受領 fee 分支） |
| 可見端 | 10-Q：擔保之二擇一條款、生效時點（租約 Commencement）、認股權股數與行權價、到期、未行使時自動淨額行權、行權前質押予票據債權人；認股權公允價值變動（損益表）；Cipher 擔保資產（其他非流動資產）與 Google 認股權股數。Indenture §3.11：終止費 100% 強制贖回 |
| 指名不可見端 | 各租約終止費金額或公式（recognition agreement 全文）；擔保上限；Google 自用承接之價值 |
| 表達工具型態（只指名，不選券） | 美股可交易、租約由第三方以認股權為對價擔保、且子公司層票據以終止費強制贖回之出租方（股權或母公司可轉債）。不選券 |

`[D]` 可重算對照（公開申報數，非測一結論）：TeraWulf Google 認股權 73,580,000 股（41,011,803＋32,568,197）÷ 流通股 498,968,677（2026-07-31）≈ 14.7%（完全稀釋前比）／12.9%（行權後占比）；同季認股權公允價值變動損失 755.7（百萬美元，2Q26）。Cipher Google 認股權 24,178,576 股；擔保資產 544.5。**不主張 G 之選擇方向、不主張違約機率、不寫 H1。**

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. TeraWulf 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1083301/000108330126000166/wulf-20260630.htm ：「Google will have the option to either (i) pay the termination fee under such Fluidstack HPC Lease (the “Termination Fee”) or (ii) pay all rent currently due under the Fluidstack HPC Lease and assume the Fluidstack HPC Lease as the tenant thereunder」；「issued to Google Warrants … to purchase a total of 73,580,000 shares of Common Stock for an exercise price of $ 0.01」；「If the Google Warrants are not exercised by these dates and the market value of Common Stock exceeds the exercise price, the Google Warrants are automatically exercised on a net basis」；「Google has agreed to pledge the Google Warrants for the benefit of the lenders … until such time as the Google Backstop becomes effective」；「change in fair of the Google Warrants」損失 755.7／972.0（三／六個月）。
2. Indenture（8-K 2025-10-23 Ex.4.1）https://www.sec.gov/Archives/edgar/data/1083301/000110465925101866/tm2529300d1_ex4-1.htm §3.11：「the Issuer will be required to apply 100% of the proceeds of such Datacenter Lease Termination Fee to redeem Notes … at a redemption price equal to 100% of the principal amount」。
3. TeraWulf 8-K 2025-08 https://www.sec.gov/Archives/edgar/data/1083301/000110465925078084/tm2523008d2_8k.htm ：Recognition Agreements CB-3／CB-4（2025-08-13），二擇一條款原文；認股權 41,011,803 股；本文無擔保金額。
4. Cipher 10-Q 2Q26 https://www.sec.gov/Archives/edgar/data/1819989/000181998926000041/cifr-20260630.htm ：「issued to Google warrants to purchase 24,178,576 shares」（2025-09-24，Barber Lake）；「an asset of $ 544.5 million … representing the value of Google agreeing to make the lease payments from Fluidstack」；風險因子「backstop arrangements … will only be effective after rent commencement … subject to certain limitations, like event of default triggers or caps」。
5. DCD 2025-10-29 https://www.datacenterdynamics.com/en/news/terawulf-and-fluidstack-to-develop-texas-data-center-in-google-backed-deal/ ：「Google backing approximately $1.3bn of Fluidstack's long-term lease obligations」（Abernathy）；Cipher「backstopping $1.4bn」；「Google also took a 14 percent stake in TeraWulf」；CEO「contracted megawatts with investment-grade counterparties」。

缺段（§7-2）：recognition agreement 全文（終止費公式、擔保上限）未取；8-K 附件是否遮蔽未查；Cipher 流通股與 Cipher 子公司票據是否有同型終止費贖回條款未查。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 對種子之打擊 |
|---|---|---|---|
| R1 | 二擇一條款、生效時點、上限於 10-Q 與風險因子明文，「caps」已揭露 → 已定價 | Cipher 10-Q 風險因子；TeraWulf 10-Q（§3-1、§3-4） | 落差可能不存在 |
| R2 | 公司與媒體明言擔保額有限（約 1.3bn／1.4bn），市場本以擔保額而非全租約讀之 | DCD 2025-10-29（§3-5） | 「全額保證」之讀法可能不是市場讀法 |
| R3 | 擔保人持股使其誘因偏向 assume，對股權有利；種子之「股權只剩空殼」分支機率可能極低 | 認股權股數（§3-1） | 方向可能與種子之風險敘事相反；種子不主張方向 |
| R4 | 擔保僅於 Commencement 後生效，違約須先發生；12 個月內可能無任何違約事件，分支永不被觀測 | TeraWulf 10-Q（§3-1） | 窗與可觀測性風險 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 實讀後無法就同一主體取得終止費金額或公式、或擔保上限（recognition agreement 或 8-K 附件，含遮蔽之確認），致 fee 分支之 \(F\) 不可界定；或無法取得 ≥ 2 家同型主體之認股權股數與二擇一條款原文；或
(2) 可運作對照只能寫成信評資訊含量／應收帳齡（L13-I#1）、MW 互斥或 RP 籃子（L13-P#2）、熱循環（L13-P#1）、租賃上界（L13-A#1）、預付（L13-A#2）、backlog 品質（L6-I）或折舊樞紐／重定價窗（C-A3／C-A4）；或
(3) 具名賣方、信評機構或公司原文已就 fee vs assume 兩分支分列對票據與股權之回收（已定價）；或
(4) `[D]` 終止費 \(F\) ≥ 子公司票據未償本金且 assume 分支租金現值 ≈ \(F\)（兩分支對股權之價值差 < 股權市值之 5%，量級不足）；或
(5) 12 個月內無可觀測驅動：無新增以認股權為對價之擔保、無 Commencement 使擔保生效、無租戶信用事件或租約修訂。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：fee／assume 分支之價值不入任何申報行，須由認股權、擔保資產、indenture 與租約條款拼合。2. 可交易工具：股權與母公司可轉債對分支之曝險不同；子公司票據非可交易範圍（§2-8 待確認）。3. 半衰期：認股權 2030-08 到期（自動淨額行權）；擔保隨租約期。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L13［I］格加「#2 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列。不改 L13-I#1、L13-P#1／#2、L13-A／L13-A#2、C-A3／C-A4、L6-I 結論。
