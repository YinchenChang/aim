# L13-A#4 生成卡｜資本與融資結構：會計恆等（可轉換票據融資之全成本恆等：利息費用只載票息＋發行成本攤銷，capped call 權利金、誘導轉換付現、自身股票衍生品公允值變動落在籌資節／權益／非營業損益）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_live.md；query/ARCH_dead.md；archive/work/20261020_L13-A#3_generate_CL.md；work/20261020_L13-A#3_test1_CL.md；archive/work/20261011_L13-A#2_generate_CL.md；work/20261013_L13-P#2_test1_CL.md；work/20261013_L13-I#2_test1_CL.md | EMITS: work/20261026_L13-A#4_generate_CL.md -->
**日期：** 2026-10-26　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 5→6／6）　**格：** L13-A　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額配置、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L6-I#4 2026-10-26 已測一，Q-0109 done）。非已殺／刻意排除格中，最後測試日最舊＝2026-10-20 一組（L7-P/A/I#3、L10-P/A/I#3、L11-A/I#3、L13-P/A/I#3、L14-P#3）；同日以 QUEUE 序決勝，最早＝**L13-A#3**（Q-0069）。既有生成數 3 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py convertible "capped call" "convertible notes"`，**命中 0 筆**。
- 比對之舊檔與死因型態，本卡須異型：
  - **L13-A#1**（T 不進 L）：入表租賃負債≠義務上界（未開始租／RVG／JV）。本卡不涉租賃。
  - **L13-A#2**（測一不通過，(1) 已定價）：客戶預付入 OCF、融資增額入利息。本卡不涉客戶端現金流分類。
  - **L13-A#3**（測一不通過，(2) 量級／(1) 已定價）：EPS **分母**（ATM 加權時滯、強制可轉 if-converted）。本卡物件為**融資成本之分子側與現金側**（利息費用 vs 全成本），不以稀釋股數為落差；if-converted 稀釋若被測一引用，只作重疊記載。
  - **L13-P#2**（WULF 可轉債票息、限制性支付閘）、**L13-I#2**（擔保人認股權）、**L13-I#3**（依債務含量排序工具）、**L13-P#3**（母公司現金封閉）：本卡不論工具選擇誘因、評等線或現金封閉，只論既定工具之成本歸屬科目。
  - **L2-A#2**（利息資本化墊高 AFFO）：本卡不論資本化利息。**L6-A#4**（應付設備款／OEM 融資繞道 capex）：本卡不論 capex 定義。**L7-A#2**（實驗室持股公允值入 NI）：本卡之公允值項為**發行人自身股票**之衍生品，非持有他方股權。
  - **T-15**（委託資本外）：不寫；CoreWeave 只作對照，不為主載體。
- §7-10 領域最近公開：IREN 10-K（期末 2026-06-30，申報 2026-08-27）；CIFR 10-Q（期末 2026-06-30，申報 2026-08-04）。下一檢查點＝IREN FQ1 FY27 10-Q（期末 2026-09-30，約 2026-11）。ASU 2024-04（誘導轉換 vs 清償）於 2025-12-15 後之期間生效，IREN 已提前／依其採用。

## 1. 落差一句

以可轉換票據為 AI 資料中心／GPU 建置籌資之發行人，GAAP 利息費用只含票息與發行成本攤銷（ASU 2020-06 後單一負債按攤銷成本），而融資之其餘成本——capped call 權利金（現金，入籌資節）、誘導轉換付現（大部分沖負債與權益，只超額入「inducement expense」）、對自身股票衍生品之公允值變動（入非營業損益）——不進利息費用、不進 Adjusted EBITDA、不進 OCF−capex。恆等：
`融資全成本_t ≡ 票息_t ＋ 發行成本攤銷_t ＋ capped call 權利金淨額（付−結算）_t ＋ 誘導轉換溢價_t ＋ 放棄之轉換選擇權價值`；其中只有前兩項進「Finance expense」。
種子載體（IREN 10-K FY2026，本輪 `sec.py` 實讀）：可轉債流通本金 6,745.7M；債務「Contractual interest expense 37,166」＋「Amortization of debt issuance costs 9,408」＝**46,574 千美元**；同年籌資節「Payment of capped call transactions (448,922)」「Payment for induced conversion of convertible notes (1,623,484)」「Payment of borrowing transaction costs (165,536)」；「Debt conversion inducement expense … $111.8 million」；capped call 列衍生資產 412,500（FV 入「Unrealized gain (loss) on financial instruments」，capped call 部分 101,848）；票面利率 0%–3.50%、初始轉換價 $13.64–$85.63。種子主張：以 GAAP 利息費用或利息覆蓋率衡量 AI 建置之債務成本者，低估可由已申報科目事前加總之全成本；票據到期／贖回日若未轉換，再融資之利差步升亦由條款決定。本卡不定方向與量級，只立可拒絕之恆等。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（ASC 470-20 攤銷成本＋ASU 2020-06 單一負債；ASC 815-40 自身股票合約權益／資產分類；ASU 2024-04 誘導轉換）；非守恆、非誘因 |
| 量綱 | 利息費用、權利金、誘導付現［$］；全成本 ÷ 平均可轉本金［%／年］；票息 ÷ 本金［%］；比值 κ＝（權利金淨額＋誘導溢價＋發行成本）÷ 期內利息費用［無量綱］ |
| 可見端 | 10-K／10-Q：Debt 附註（票據明細表、利息費用拆分）、Derivatives 附註（capped call 公允值與損益行）、現金流量表籌資節、權益變動表（capped call／prepaid forward 重分類行）、MD&A「Finance expense」「Debt conversion inducement expense」 |
| 指名不可見端 | 放棄之轉換選擇權之發行日公允值（發行人不揭；需以發行價、轉換溢價、波動率 `[A]` 推）；共識模型是否把權利金／誘導付現計為融資成本 |
| 主張 | 全成本 − GAAP 利息費用之差額可由已申報科目算出；若市場與評等以利息費用或 Adjusted EBITDA 衡量 AI 建置之資本成本，即錯置。可由「主流口徑已納入權利金與誘導付現」或「差額相對營運現金流不足量」而拒絕 |
| 外部參照物（測一查證） | 軟體／生技可轉債發行人之 capped call 權利金占本金比之慣常區間（只作會計路徑與量級先例） |
| 表達工具型態（只指名，不選券） | 美股上市之 AI 資料中心／GPU 雲供給者普通股或其可轉債（IREN 為主載體；CIFR、WULF、Nebius 為對照）。不選券 |
| 重疊 | L13-A#3（同屬可轉工具，分母 vs 成本）、L13-P#2（WULF 票息）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. IREN 10-K（FY2026）https://www.sec.gov/Archives/edgar/data/1878848/000187884826000052/iren-20260630.htm （票據明細表、利息費用拆分 46,574、capped call 付款 448,922、誘導轉換付現 1,623,484、inducement expense 111.8M、衍生資產 412,500、權益重分類 (259,600)——本輪 `sec.py doc --grep` 實讀）
2. IREN 10-Q（期末 2026-03-31）https://www.sec.gov/Archives/edgar/data/1878848/000187884826000026/iren-20260331.htm （季序列；未實讀，測一取）
3. Cipher Mining 10-Q（期末 2026-06-30）https://www.sec.gov/Archives/edgar/data/1819989/000181998926000041/cifr-20260630.htm （「With the net proceeds of the 2031 Convertible Notes, we funded capped call transactions」——本輪實讀；權益或資產分類未讀）
4. TeraWulf 10-Q（期末 2026-06-30）https://www.sec.gov/Archives/edgar/data/1083301/000108330126000166/wulf-20260630.htm （對照；未實讀）
5. 市場報導：The Block〈IREN closes $3 billion convertible notes offering …〉https://www.theblock.co/post/401447/iren-closes-3-billion-convertible-notes-offering-as-bitcoin-miners-ai-infrastructure-push-accelerates （未實讀）
6. 測一須另取：IREN 法說原文是否以全成本口徑說明可轉融資成本；具名賣方是否把 capped call 權利金與誘導付現計入資本成本／FCF；評等機構（Moody's／S&P）對 IREN／CIFR／WULF 之債務調整是否含 capped call；IREN FQ1 FY27 10-Q 之新 capped call 與誘導轉換。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 賣方／投資人社群已逐檔解析可轉條款與稀釋（標題〈IREN Just Dropped $2B Of Converts, What Does It Actually Mean?〉） | Seeking Alpha https://seekingalpha.com/article/4849641-iren-dropped-2b-of-converts （本輪只見標題，未實讀；測一取原文） | 已定價 |
| R2 | 權利金與誘導付現於現金流量表籌資節逐行列示、inducement expense 單列損益——讀 10-K 者可得 | IREN 10-K 原文（#1） | 資訊已公開，無落差 |
| R3 | 可轉債成本之經濟本質由票據持有人以選擇權定價，股東經稀釋承擔；以利息費用為成本之誤讀不影響以 EV／營收或 EV／EBITDA 定價之股票 | 測一須找具名來源 | 機制不入價格 |
| R4 | capped call 為資產、可於股價上漲時結算回收（IREN FY26「Settlement of capped call transactions 38,812」、衍生資產 412,500），淨成本可能為負 | IREN 10-K 原文（#1） | 方向不定／量級抵銷 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 公司指引或法說原文已以含權利金／誘導付現之全成本說明融資成本，或 ≥ 1 家具名賣方／評等機構已將 capped call 權利金與誘導付現計入資本成本或 FCF——已定價（R1／R2 擴及主流口徑）。
(2) `[D]` κ＝（capped call 權利金淨額＋誘導溢價＋發行成本付現）÷ 同期 GAAP 利息費用，於 IREN 以外之 ≥ 1 家對照發行人 < 1，或全成本 − 利息費用之差額 ÷ 同期 OCF 絕對值 < 5%——量級不足／單一發行人特異。
(3) capped call 公允值回收（R4）使權利金淨額於可觀測期間為負或近零，致恆等之差額方向不可定——方向不定。
(4) 可運作對照只能寫成 L13-A#3 EPS 分母、L13-P#2 限制性支付閘、L13-I#3 工具排序、L7-A#2 持股公允值或 T-15。
(5) 主流估值口徑以 EV 基礎倍數為主，且無具名證據顯示利息費用或覆蓋率入定價（R3 成立）。
(6) 12 個月內無可檢驗事件（例：IREN FQ1／FQ2 FY27 10-Q 新增可轉／capped call／誘導轉換；首個贖回日最早 2027-12-20〔2030 Notes〕）。

複查觸發器（若日後殺）：任一 AI 資料中心／GPU 雲上市發行人於 10-K／10-Q 首次以「all-in cost of convertible financing」或同義口徑揭露；或評等機構公開將 capped call 權利金計入債務成本；或 IREN／CIFR／WULF 任一票據於贖回日以現金按面額贖回並以高收益債再融資。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：Debt 附註利息拆分；Derivatives 附註 capped call 公允值與損益；籌資節權利金、誘導付現、發行成本；inducement expense。
2. 可交易工具：美股 AI 資料中心／GPU 雲供給者普通股或可轉債（不選券）。
3. 半衰期：權利金與誘導付現於發行／交易季一次入籌資節；票息逐季；首個贖回日 2027-12-20 起（IREN 2030 Notes），到期 2029-12～2033-12。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列；`query/ARCH_matrix.md` L13［A］標「#4 已生成」；`AIM_FUNNEL.md` §3 一句；`export/LEADS_算力收支.md` 一列（IREN GPU 融資約 3.6B，10-K 原文）。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live。不改 L13-A#1–#3、L13-P／#2／#3、L13-I／#2／#3、L2-A#2、L6-A#4、L7-A#2、C-A3／C-A4 結論；不寫 T-15。
