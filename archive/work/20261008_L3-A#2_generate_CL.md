# L3-A#2 生成卡｜半導體製造測試：會計恆等（政府補助淨額法：補助／投資抵減沖減 PP&E → 申報折舊與毛利率含隱性補助）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260924_L3-A_generate_GK.md；archive/drive/USED_20260924_L3-A_test1_GK.md | EMITS: work/20261008_L3-A#2_generate_CL.md -->
**日期：** 2026-10-08　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain）　**格：** L3-A　**序：** #2　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。L2／L8／L9／L12 之 #2 已於 10-07／10-08 測畢；其餘格最後測試最舊＝**L3-A（2026-09-24）**（L1-P 刻意排除；L8-P／L9-P／L11-P 已殺）。既有生成數 1 → #2。
- 比對之舊檔與死因型態，本卡須異型：
  - L3-A#1（`archive/drive/USED_20260924_L3-A_generate_GK.md`；測一 `archive/drive/USED_20260924_L3-A_test1_GK.md`）：單價恆等 `P_eff = P_waf/(Y_fe×Y_pkg×N_die)`，死於**量綱／可觀測性**——節點出貨、層別良率非申報科目。本卡不用單價、良率、節點 mix；載體為**成本側**之補助會計（現金流量表「proceeds from government incentives」、遞延補助負債、補助沖減 PP&E 之政策句、子公司損益），皆為申報科目。
  - ARCH_dead #5 C-A3（折舊年限離散）與 L13-P（GPU 年限 vs 熱循環）：皆為**年限**假設；本卡年限不動，動的是**折舊基數**（成本扣補助）。#14 C-I3′（分部毛利由非機制項解釋）為 L4，型態相近者列為本卡否決 (4)。
- §7-10 領域最近公開：Micron FY26 Q4 8-K 新聞稿 2026-09-30（FY 至 2026-09-03）；Micron FY26 10-K 預期 2026-10 申報（未見）；TSMC 1Q26 子公司損益與補助（Taiwan News 2026-05-16 轉述）；TSMC 3Q26 季報約 2026-10-16。

## 1. 落差一句

先進製程與記憶體廠商之政府補助（CHIPS 補助、日／德補助、§48D 投資抵減 25%→35%）多以**淨額法沖減 PP&E 成本**，使其後 5 年左右之折舊低於毛建置成本——申報毛利率與海外廠「已獲利」敘事**內含補助**，且公司不分列「補助所致折舊減少額」；**落差＝市場把淨額法毛利率讀成無補助之成本結構，而補助流入已斷崖式下降（TSMC 1Q26 補助 NT$5.05 億 vs 1Q25 NT$351.5 億），未獲補助之新增產能將以毛成本折舊**。**方向未定**：補助相對毛利之量級可能極小（Micron FY26 補助收現 33.2 億美元 vs 毛利 1,075 億美元）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [A] 會計恆等：`D_reported = (C_gross − G)/n`；`GM = 1 − (D_reported + 其他成本)/Rev`；`ΔGM_grant = G/(n·Rev)`。補助流量 G 停止後，舊批 ΔGM 於 n 年內遞減至 0，新批以 C_gross 入帳 |
| 選擇者 | 公司（IAS 20／US GAAP 類推下選淨額法或遞延收益法）；政府（補助條件、轉股，如美國對 Intel 補助轉約 10% 股權） |
| 可見端 | 現金流量表補助收現；遞延（unearned）補助負債；補助應收；子公司損益（TSMC Arizona、JASM）；補助用途句「mainly used to subsidize the purchase costs of property, plant and equipment」 |
| 指名不可見端 | 各期折舊中因補助減少之金額；海外廠毛利率稀釋指引中補助之貢獻 |
| 已讀錨 | Micron 8-K（https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000018/a2026q4ex991-pressrelease.htm，2026-09-30）：FY26 營收 133.19B、GAAP 毛利率 80.7%、毛 capex 30.71B、補助收現 3.32B、net capex 27.37B、折舊攤銷 9.50B、非流動 unearned government incentives 786M；Taiwan News（https://www.taiwannews.com.tw/en/news/6363874，2026-05-16）：TSMC 1Q26 補助 NT$5.05 億（1Q25 NT$351.5 億，−98.56%）；Arizona 1Q26 獲利 NT$188 億（> 2025 全年 161.4 億）；JASM 首季獲利；Taipei Times（https://www.taipeitimes.com/News/biz/archives/2025/11/19/2003847426，2025-11-19）：約兩年 NT$1,470 億補助「largely used for purchasing property, facilities and equipment」；Aztech Council（https://www.aztechcouncil.org/tsmcs-arizona-fab-generates-first-profit/，2025-08-22）：1H25 補助 2.21B 美元沖抵 PP&E；CPA Practice Advisor（https://www.cpapracticeadvisor.com/?p=165556，2025-07-25）：§48D 25%→35%，Micron Clay 一期原估約 11.3B；FourWeekMBA（https://fourweekmba.com/ai-intel-q2-2026-non-gaap-gaap-gap-chips-act-escrowed-shares/，2026-07-24）：Intel Q2'26 GAAP 損失主因託管予商務部之股份按市價評價 |
| 量綱 | G：美元／期；n：年；ΔGM：百分點；**補助收現 ≠ 當期折舊減少額**（後者為存量攤提），不可直接相減 |
| 未證之連結 | ① 各主體實際採淨額法（Micron 10-K 政策句未讀到；FY25 10-K fetch 於 Item 1A 截斷）；② 補助所致折舊減少額可否由附註重算；③ 量級對毛利率是否非邊際 |
| 半衰期 | 年（n≈5 年之機器設備）；觸發點＝補助流入斷層後之新產能投產 |

## 3. B 端可觀測載體（只指名，未實讀者標明）

1. Micron FY26 10-K（未申報／未讀）：Government Incentives 附註之政策句、沖減 PP&E 累計額、§48D 抵減入帳方式、unearned 遞延餘額。
2. TSMC 20-F 2025 與 3Q26 合併財報：政府補助附註（沖減成本 vs 遞延收益）、子公司損益；管理層海外廠毛利稀釋指引（法說原文未讀）。
3. Intel 10-K 2025／10-Q 2026：補助轉股前之補助會計、託管股份評價（只讀轉述）。
4. GlobalFoundries、Texas Instruments 10-K：CHIPS 補助／§48D 入帳（未讀）。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 量級極小：Micron FY26 補助收現約毛利 3%，且只部分轉入當期折舊 | Micron 8-K 2026-09-30 | ΔGM 為邊際 |
| R2 | 補助已在現金流量表與 net capex 指引中公開，賣方模型以 net capex 建模 | Micron 8-K；Kalkine 2026-06-09 轉述 net capex 指引 | 已定價 |
| R3 | 海外廠獲利主因 AI 需求與 N4／N3 定價，非補助 | Taiwan News 2026-05-16（Arizona 獲利於補助斷層之季仍升） | 機制被需求淹沒 |
| R4 | 政策延續：§48D 合格期限、後續 CHIPS 改組或轉股可能使補助以其他形式續存 | CPA Practice Advisor 2025-07-25；FourWeekMBA 2026-07-24 | 斷層不成立 |

## 5. SCOUT 裁決

**留。** 不進 T。下一動作＝ANALYST 測一（實際 fetch 並列 URL）。終端三題（§7-4）只標「轉入個股層時必問」，本輪不執行。

否決觸發（寫給 ANALYST）：
- (1) 指名主體（Micron、TSMC、Intel、GlobalFoundries、TI）之最近 10-K／20-F／10-Q 皆採**遞延收益法或總額列示**（補助不沖減 PP&E），或已分列補助所致折舊減少額——淨額法隱藏不成立；
- (2) 由附註可重算之補助所致折舊減少額 < 該主體最近一年毛利 2%（量級不足）；
- (3) 主要主體之補助流入未斷層（最近四季補助收現相對前四季未降逾半），且已公告之後續補助／抵減足以覆蓋規劃中之新產能；
- (4) 管理層或賣方已公開以「含／不含補助」兩口徑揭露海外廠或美國廠毛利（落差已被承認）；
- (5) 補助所致 ΔGM 之變動方向與申報毛利率變動同向且量級 < 其 1/10（被 AI 需求定價淹沒，R3 成立）。

複查觸發器（若日後殺）：任一主體首次分列補助所致折舊減少額；或主要補助計畫撤回、追回（clawback）或轉股並改變入帳方式；或補助斷層後首座無補助先進廠投產且其毛利稀釋指引上修。
