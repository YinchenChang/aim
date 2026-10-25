# L12-I#4 生成卡｜監理與法制：誘因（併購事前申報門檻下之「非專屬授權＋聘用」結構——HSR 不申報 vs ASC 805 認列企業合併之雙重定性）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260922_L12-I_generate_GK.md；archive/work/20261008_L12-I#2_generate_CL.md；archive/work/20261016_L12-I#3_generate_CL.md；work/20261016_L12-I#3_test1_CL.md；archive/work/20261008_L12-A#2_generate_CL.md；archive/work/20261025_L12-A#4_generate_CL.md；archive/work/20261023_L12-P#4_generate_CL.md | EMITS: work/20261025_L12-I#4_generate_CL.md -->
**日期：** 2026-10-25　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 3／6）　**格：** L12-I　**序：** #4　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。非「已殺／刻意排除」格中最後測一最舊＝L12-I（#3，2026-10-16）；其次 L4-A／L4-I／L5-P／L5-A（2026-10-17）。既有生成 3 份 → #4。
- Tokenomics 線索（CLAUDE.md §11）：已查 `Groq`／`acquihire`／`license`／`LPU`，命中 0 筆。內部數字（§12）未取用。
- 比對（本卡須異型）：
  - **L12-I#1**（GK）：法規合規成本落部署者；死於部署者 SG&A 無分列。本卡非合規成本，為**反壟斷事前審查門檻**塑造之交易法律形式。
  - **L12-I#2**：AI 產出 IP 補償＝賣方零保費賣權；死於觸發事件 0 件。本卡之誘因已由交易形式實現（交易已完成、已入帳），不待第三方求償。
  - **L12-I#3**：§232 配額在建期倍數；死於行為端方向相反（TSMC 提前）、在建期由官方核定。本卡之選擇者為**收購方**，選擇變數為**交易法律形式**（非時點），已觀測行為與誘因同向（見 §2）。
  - L12-A#2（著作權法定賠償 vs ASC 450）、L12-A#3（稅法時序）、L12-A#4（營業動產稅）、L12-P#2–#4（FDA 流量、出口管制質量平衡、InP 許可）：皆非併購審查。
  - L3-I#2（DOC 認股權證）、L3-A#4（Intel SCIP NCI）：政府／合資權益結構，非反壟斷形式選擇。
  - ARCH_dead：C-I3′、N-02（L4，「本機制之利益分列」型）與本卡同涉 NVDA，但死因為分部毛利／CPO 營收未分列；本卡載體為已分列之 Note 2 與監理行動，非毛利分列。不得以「LPU 營收未分列」作本卡答案（否則併入 C-I3′ 型）。
- §7-10 領域最近公開：FTC 主席 Ferguson 2026-01-16（Bloomberg）稱將密切檢視 acquihire、可能「in the coming months」發指引（Torys Q3 2026 轉述）；參議員 Warren／Wyden／Blumenthal 致 FTC／DOJ 函 2026-02-04；Warren／Blumenthal 致 NVIDIA 函 2026-03-23（回覆期限 04-03）；DOJ 代理反壟斷主管 Assefi 2026-03-18 稱 acqui-hire 為「red flag」；NYT 2026-09-09 報導 DOJ 向 NVIDIA 發出資訊要求（DCD 2026-09-10 轉述）；HSR 交易規模門檻 2026-02-17 起 US$133.9M。截至 2026-10-25 未見 FTC 指引正文或執法案。下一檢查點＝FTC 指引、DOJ 對 Groq 案之處置、NVIDIA 3Q FY27 10-Q（約 2026-11 下旬）。

## 1. 落差一句

HSR 只審「assets or stock」之取得；PNO 非正式解釋以「專屬授權＝可申報、非專屬＝不申報」為框架。收購方因此以**非專屬授權＋聘用核心團隊**（或無表決權少數股）取得目標之能力，免事前審查；但同一交易在財報上被**認列為企業合併**——NVIDIA 對 Groq 認列商譽 US$14.4B 與技術無形資產 US$2.5B（總對價 13.0B＋一年內應付 4B），「Goodwill, primarily attributable to the workforce」。法律形式（未取得 business）與會計實質（取得 business）互斥，至少一側未被定價：**若形式為真**，殘存之 Groq Inc. 可再授權同一 LPU 技術予他人，商譽背後之排他性法律上不存在；**若實質為真**，交易屬可申報之取得，Clayton §7 事後挑戰（無追溯時效）與 HSR 未申報罰則之尾端仍開。方向未定。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：規則端（HSR 申報觸發＝取得資產或股權；非專屬授權不觸發）給收購方「避事前審查」之報酬；行為端（收購方）選擇法律形式；會計端（ASC 805 business 定義）不跟隨法律形式 |
| 選擇者 | 收購方（NVDA；同型 META–Scale AI 49%、GOOGL–Character.AI／Windsurf、MSFT–Inflection、AMZN–Adept） |
| 誘因式（僅定義） | 選非專屬形式之期望報酬＝避開事前審查之時間與禁止機率 × 交易價值 − [排他性喪失之價值損失 ＋ 事後挑戰機率 × 救濟成本]；收購方只內化前項，市場是否計後兩項為本格題 |
| 已讀事實 | NVDA 10-K FY26 Note 2：「non‑exclusive license agreement … hired certain Groq employees. No customer contracts, existing products, or equity interests were purchased. We recorded $14.4 billion of goodwill and a $2.5 billion developed technology intangible asset … The goodwill is tax deductible.」現金流量表投資活動「Groq, Inc. (13,000)」；10-Q 2Q FY27 融資活動「Groq, Inc. (2,944)」，應付款附註「Related to the Groq, Inc. non-exclusive license agreement」。META 10-K FY25：Scale AI 少數投資 US$13.80B，按 measurement alternative，「We do not have significant influence」。GOOGL 10-K FY25：Windsurf 0 筆（未達重大性，未分列）。DCD 2026-09-10：Groq 仍營運；NVIDIA「Groq 3 LPU」為 LPX 機櫃平台基礎、已入量產。 |
| 未證之連結 | 授權合約是否另有限制條款（field-of-use、不競爭、優先權）使「非專屬」名不副實；殘存 Groq 是否實際對第三方授權或販售 LPU；DOJ 資訊要求之範圍與是否轉為第二階段式調查；FTC 指引是否把「授權＋聘用」納入「取得資產」 |
| 量綱 | 事後救濟情境下受影響之已認列商譽＋無形資產 ÷ 收購方權益（%）；殘存主體第三方授權收入（美元／年）；監理行動時點（月） |
| 半衰期 | FTC 指引（「coming months」，未定）；DOJ 調查（不定期）；Clayton §7 無時效；商譽年度減損測試（每年） |

## 3. B 端可觀測載體（只指名）

1. NVDA 10-K FY26 https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm （Note 2、現金流量表、風險因素 Groq 段；本輪 sec.py 實讀）；10-Q 2Q FY27 https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm （應付款與融資現金流；本輪實讀）；後續 10-Q 之商譽、法律程序、承諾段（未讀）。
2. META 10-K FY25 https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm （Scale AI 投資附註；本輪實讀）；GOOGL 10-K FY25 https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm （Windsurf 0 筆）；MSFT、AMZN 10-K 同型交易附註（未讀）。
3. 監理端：FTC 主席談話（Bloomberg 2026-01-16）https://www.bloomberg.com/news/articles/2026-01-16/us-is-scrutinizing-big-tech-talent-acquisitions-ftc-chief-says ；Mintz 2026-02-20 https://www.mintz.com/insights-center/viewpoints/54731/2026-02-20-ai-acquihires-under-fire-ftc-signals-hsr-scrutiny-ai ；Torys Q3 2026 https://www.torys.com/our-latest-thinking/torys-quarterly/q3-2026/us-antitrust-regulators-concerned ；DCD 2026-09-10 https://www.datacenterdynamics.com/en/news/nvidias-groq-deal-facing-doj-probe-amid-regulator-scrutiny-into-acqui-hires-report/ （DOJ 資訊要求，轉述 NYT）。
4. 國會端：Warren／Wyden／Blumenthal 2026-02-04 https://www.warren.senate.gov/newsroom/press-releases/warren-wyden-blumenthal-call-on-federal-regulators-to-investigate-meta-google-nvidia-reverse-acqui-hire-deals ；Warren／Blumenthal 2026-03-23 https://www.warren.senate.gov/newsroom/press-releases/warren-blumenthal-question-whether-nvidias-20-billion-groq-deal-is-attempt-to-avoid-antitrust-laws （「effectively acquired Groq in all but name」）。
5. HSR 授權申報框架：PNO 非正式解釋 1106006 https://www.ftc.gov/legal-library/browse/hsr-informal-interpretations/1106006 （問句以「non-exclusive and therefore non-reportable / exclusive and therefore reportable」為框架；屬非正式解釋，非條文；16 CFR 801 原文未讀）。
6. 殘存主體行為：Groq Inc.／GroqCloud 對第三方授權或客戶公告（未讀）；歐盟執委會對 acqui-hire 之審查（Torys 引 2025-08-01 Reuters；未讀）。
7. 未讀：NVIDIA 對 03-23 函之回覆；具名賣方對 Groq 交易之監理尾端或排他性之量化。

缺段（§7-2）：授權合約全文未公開；本輪未讀；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 執法者至今無任何 acqui-hire 執法案；Ferguson 傾向指引而非規則制定，且稱無一體適用之規則 | Mintz 2026-02-20；Torys Q3 2026 | 監理尾端可能永不實現 |
| R2 | ASC 805 之 business 定義（輸入＋實質過程，含有組織之勞動力）與 HSR「取得資產或股權」本為不同法域之不同測試，兩者分歧不構成矛盾，更不構成違法 | NVDA Note 2 用語（「No customer contracts, existing products, or equity interests were purchased」） | 「互斥」之前提可能不成立 |
| R3 | 非專屬授權之排他性損失可能為零：核心工程團隊已轉至收購方，殘存主體缺乏再授權或續研之能力 | Warren／Blumenthal「hired many of Groq's key employees, including its CEO and President」 | 「形式為真」一側之價值損失小 |
| R4 | 量級：救濟情境下受影響之商譽＋無形資產相對 NVDA 權益與現金流可能甚小；救濟多為行為承諾而非解除 | NVDA 10-K（Pro forma「not material」） | `[D]` 量級不足 |
| R5 | 市場已知悉：參議員函、NYT／DOJ 報導皆公開，賣方可能已計入 | 載體 3、4 | 已定價 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 規則端：12 個月內（至 2027-10-25）FTC／DOJ 無指引、無資訊要求升級、無執法或和解，且 DOJ 對 Groq 案之資訊要求經公開確認結案或無後續（監理尾端無拘束力）；或
(2) 雙重定性不成立：收購方附註或監理文件顯示交易已依 HSR 申報、或授權實為專屬（申報已完成），或 ASC 805 之認列係依 asset acquisition 而非 business combination；或
(3) 排他性端：殘存主體（Groq Inc. 等）已公開不具再授權能力或已停止營運／被收購方實質控制，且無第三方授權或客戶；同時監理端 (1) 亦未觸發（兩側皆空）；或
(4) `[D]` 量級：救濟情境下受影響之已認列商譽＋無形資產 < 收購方權益 2%，且無其他同型交易可合併計算；或
(5) 具名賣方或評等機構已明示量化監理尾端或排他性折價（已定價）；或
(6) 已觀測之監理行動或股價反應由非本機制項（出口管制、AI 需求、其他反壟斷案如 CUDA 生態調查）解釋，且一手原文如此歸因。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：商譽／無形資產附註、應付對價、法律程序、或有事項。2. 可交易工具：收購方（不選）。3. 半衰期：FTC 指引不定期；DOJ 調查不定期；Clayton §7 無時效。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L12［I］格加「#4 已生成」；`AIM_FUNNEL.md` §3 與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0101；`export/LEADS_算力收支.md` 追加 1 筆（NVDA Note 2）。不改 L12-I#1–#3、L12-A#1–#4、L12-P#1–#4、L3-I#2、L3-A#4、C-I3′、N-02 結論。
