# L7-A#6 生成卡｜模型層：會計恆等（權益交割之非現金公益與報酬通道：法律流通股 vs 會計流通股之分離＋費用認列時點 ≠ 稀釋時點；Adjusted 口徑全排除）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/QUEUE.md；archive/drive/USED_20260930_L7-A_generate_GK.md；archive/work/20261013_L7-A#2_generate_CL.md；archive/work/20261020_L7-A#3_generate_CL.md；archive/work/20261027_L7-A#4_generate_CL.md；archive/work/20261102_L7-A#5_generate_CL.md；work/20261102_L7-A#5_test1_CL.md；archive/work/20261013_L7-I#2_generate_CL.md；work/20261013_L7-I#2_test1_CL.md | EMITS: work/20261111_L7-A#6_generate_CL.md -->
**日期：** 2026-11-11　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1→2／6）　**格：** L7-A　**序：** #6　**上限：** 生成卡，非 T／L／M
**⚠ 無金額配置、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L7-P#6 已測一，Q-0192 done）。非已殺／刻意排除格中，最後測試日最舊＝L7-A#5（2026-11-02）→ **L7-A**。既有生成數 5 → #6。
- Tokenomics 線索（CLAUDE.md §11）：已查 `tokenomics_leads.py "Public Benefit" dilution "stock-based compensation" RSU`，命中 0 筆。內部數字（§12）未取用。
- 比對之舊檔與死因型態，本卡須異型：
  - **L7-A#1**（不通過）：列表價 vs FLOP 單位成本。本卡不論單價或 FLOP。
  - **L7-A#2**（部分通過）：**持股方**之公允價值計量。本卡在**發行方**之權益交割費用與股數口徑；不論任何持股或轉債公允價值變動（S-1 Adjusted NI 之 FV 調整不納入）。
  - **L7-A#3**（部分通過）：市集總額／淨額（營收側）。無關。
  - **L7-A#4**（部分通過）：算力在功能科目間之分攤。本卡不涉算力成本。
  - **L7-A#5**（部分通過）：融資租賃利息移出營業利益。本卡不涉租賃；落差在**權益交割（非現金）項**之認列時點與股數分母。
  - **L7-I#2**（部分通過）：研究人才外部選擇權 × SBC（誘因、人才集中）。本卡不論人才或報酬誘因；只論恆等式：雙觸發 RSU 於上市前**零認列**、公益基金股**法律流通而會計不流通**、捐贈配對**以股交割**——三者使歷史 GAAP 序列與每股分母系統性缺項。
  - **L13-A#4**（不通過）：Broadcom 可轉債全成本與稀釋。本卡不論轉債。
  - **C-A5／C-P3／C-I1**（死 #13／#16／#10）：本卡不需 API 單價、權重科目或能力估值。觸發器屬 SCOUT-WATCH，不代判。
  - **T-15**：無關，不寫。
- §7-10 領域最近公開：Anthropic S-1/A 第 2 號（EDGAR，2026-11-10，`0001628280-26-072484`）；前次 S-1/A 2026-11-02、S-1 2026-10-26。下一檢查點＝S-1/A 再修、424B4、上市後首份 10-Q（含 IPO 季）。

## 1. 落差一句

恆等（三通道）：
- 股數：`N_econ ≡ N_acc + N_PBF + N_VMO + N_TSM + N_MS(P)`；`N_PBF`＝公益基金（全資子公司）持有之 Class N 股，**法律上流通、會計上不流通**，不入加權平均股數；`N_VMO`＝已既得之捐贈配對義務股；`N_MS(P)`＝股價里程碑發行（每較前一里程碑上漲 50% 至多再發 2%），為股價之遞增函數。
- 費用：`OI_adj ≡ OI_GAAP + SBC + C_nc + 一次項`；上市前雙觸發 RSU 之 SBC 為 0（績效條件不視為可能），上市季一次認列累積數；捐贈配對（`C_nc`）以股交割、與員工權益獎酬連動，列 other operating and administrative，並自 Adjusted 排除。
- 定義 `d ≡ (N_PBF + N_VMO) ÷ N_acc`（會計分母外之已確定稀釋）；`κ ≡ (SBC + C_nc) ÷ R`（權益交割非現金費用率）。
種子主張：上市後市場以 Adjusted Operating Margin 與會計 EPS／市值讀「規模化獲利」，但 (i) 歷史 GAAP SBC／R 序列不含 RSU 之續發費用（上市後 2 年認列 241 億美元，加速歸屬），(ii) 公益基金股與已既得配對義務不在會計分母，(iii) 股價里程碑發行使稀釋隨股價上升——若比較基準（同業、自身歷史、市值資料商之股數）未調節，每股經濟值即錯置。本卡不定方向與量級，只立可拒絕之恆等。

已見數點（本輪 `sec.py` 實讀 S-1/A 第 2 號全文，M$ 或原文）：
- 「we contributed 846,840,960 shares of our Class N common stock, representing 5% of our fully diluted shares as of June 30, 2026 … to Anthropic Public Benefit Fund, LLC … our wholly owned subsidiary」；股數表註：Initial Public Benefit Issuance 之股「(i) are considered legally outstanding, (ii) are not considered outstanding for accounting purposes while held by our wholly owned subsidiary」；「The pro forma weighted-average number of shares does not give effect to the Initial Public Benefit Issuance」。
- 里程碑框架：「issue shares … representing up to an additional 2% of our then-outstanding shares (plus any shares subject to options, RSUs … and any shares held by the Anthropic Public Benefit Fund) each time our share price appreciates 50% above the prior share price milestone, beginning with our initial public offering price」；達成條件＝收盤高於門檻達尾隨 120 日中 90 日，且發行前 10 日均價亦高於門檻；董事會裁量。
- 捐贈配對：「non-cash charges from our donation matching program settled in shares of our Class N common stock, the amount and value of which is linked to employee equity awards and recorded in other operating and administrative expenses」；股數表：Vested Matching Obligation 553,441,297 股；Matching Issuance（9/30 後）27,991,850 股。
- RSU：「no stock-based compensation expense had been recognized for the RSUs because management determined that it is not probable that the performance condition will be achieved」；若 9/30 上市「$8.2 billion of cumulative … and an additional $24.1 billion of unrecognized … over a weighted-average period of approximately 2.0 years」；「Upon the completion of this offering, we will record cumulative stock-based compensation expense of approximately $14.2 billion」（含 9/30 後修改，以區間中點計）；另有其他獎酬未認列 $2.1B。RSU 淨額交割：預扣 51,578,975 股（假設 50.90% 預扣率），稅款以 IPO 淨收入支付。
- 定價：區間中點 $74.00；發行 825,000,000 股 Class A。
- 季度調節（M$）：3Q26 營收 16,956、GAAP OI (567)、SBC 1,070、非現金捐贈 1,960、Adjusted OI 2,463；OM (3)% vs Adjusted OM 15%。9M26：營收 33,242、SBC 3,255、非現金捐贈 2,086、Adjusted OM 12%。
- `[D]`（只作量綱，不作預測）：`N_PBF` × $74 ≈ 627 億美元；`N_VMO` × $74 ≈ 410 億美元。3Q26 `κ` ＝ (1,070＋1,960) ÷ 16,956 ≈ 17.9%。RSU 241 億美元／2.0 年（加速歸屬，首年占比較高）相對 3Q26 年化營收（≈ 678 億）之量綱 ≈ 18–25%/年，另加 IPO 季 142 億一次項。`N_MS`：股價 ×1.5^k 時累積上限 ≈ 1.02^k − 1（×5 對應 k＝3 → ≈ 6.1%），屬裁量上限，非確定。`d` 之分母 `N_acc` 須測一自 S-1/A 股數表與 pro forma 加權股數取，本輪不算。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | 會計恆等（ASC 718 績效條件可能性門檻；ASC 260 加權股數排除子公司持有之母公司股；以股交割之捐贈配對費用；非 GAAP 排除項） |
| 量綱 | 股數；`d`、`κ`［無量綱］；營業利益率 pp；每股 $ |
| 可見端 | S-1/A 股數表與註、pro forma EPS 註、RSU 附註、非 GAAP 季度調節、Donation Matching Plan 描述、Public Benefit Issuances 風險因子；上市後 10-Q 之 EPS 分母、SBC 按科目、非現金捐贈 |
| 指名不可見端 | 公益基金股轉出（捐贈）時是否以當時公允價值入費用及入哪一行（S-1/A 未見明文，測一核）；里程碑發行之實際裁量；捐贈配對之未來員工選擇比例；市值資料商採法律股數或會計股數 |
| 主張 | 上市後 4 季，市場若以 Adjusted OM／會計 EPS／資料商市值讀 Anthropic，而未調節 `N_PBF`、`N_VMO`、`N_MS(P)` 與 RSU 續發費用，則每股經濟值錯置。可由「具名賣方／研究機構已以含三通道之完全稀釋股數與含 SBC＋C_nc 之利潤率讀之」或「發行人已並列」拒絕 |
| 外部參照物（測一查證） | 雙觸發 RSU 上市季一次認列之既往案例（Airbnb、DoorDash、Snowflake、Uber 之 IPO 季 SBC）；Salesforce 1-1-1（以股捐贈）之會計呈現；市值資料商對多類別股之計數慣例——僅作路徑先例 |
| 表達工具型態（只指名，不選券） | 模型實驗室普通股（上市後）；不選券 |
| 重疊 | L7-I#2（同為 SBC，但為誘因）、L7-A#2（另一側之 FV）、L13-A#4（另一稀釋來源）。重疊不構成丟棄 |

## 3. B 端可觀測載體（只指名；URL 為錨，非測一結論）

1. Anthropic S-1/A 第 2 號（本輪 sec.py 實讀，上列原文）：https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm
2. TechYorker（2026-10-29，無具名作者）〈Anthropic's public benefit structure creates unusual risks for IPO investors〉——本輪經代理實讀：列 5%／2% 里程碑／2025 配對 $541M，稱公益支出「can lower operating margin and per-share profitability even without issuing another share」；**未論會計股數排除、未論 RSU 一次認列、未算完全稀釋股數**：https://techyorker.com/anthropics-public-benefit-structure-creates-unusual-risks-for-ipo-investors/
3. remio.ai（Olivia Johnson，2026-10-05，德文；轉述 The Information）——實讀：配對六個月逾 $660M、Calcbench CEO 批評排除於 adjusted；未算稀釋 %：https://www.remio.ai/de/post/anthropic-charity-stock-match-raises-a-billion-dollar-ipo-dilution-question-de
4. Allocations（Addhyan Negi，2026-07-13）——實讀：早於公開 S-1，無股數；只作時序錨：https://www.allocations.com/insights/anthropic-s-1-cap-table-shares-outstanding-and-what-to-watch-before-the-ipo
5. FourWeekMBA〈Anthropic's Benefit Fund Holds 3.5x Any Co-Founder's Shares〉、〈Anthropic's IPO Stock-Pay Charge Rose to $8.2B From $2.9B〉、〈Anthropic's $2B Donation Match Implies $71 a Share〉——本輪擷取失敗（client_error），測一以他路徑實讀或記失敗歸因：https://fourweekmba.com/ai-anthropics-benefit-fund-holds-3-5x-any-co-founders-shares/
6. sec-api.io〈Anthropic (ANT) S-1 IPO SEC filing analysis〉（2026-10-27，未讀，測一實讀）：https://sec-api.io/insights/anthropic-ant-s-1-ipo-sec-filing-analysis
7. FinanceBuzz〈Anthropic dilution risk〉、247wallst（2026-10-20）〈Anthropic sets aside 5% stake for public benefit fund〉（未讀，測一實讀）：https://financebuzz.com/news/anthropic-dilution-risk-retirement-savings ；https://247wallst.com/investing/2026/10/20/anthropic-sets-aside-5-stake-for-public-benefit-fund-ahead-of-november-ipo/

## 4. 最強反方（具名，測一驗）

- **已被讀出**：TechYorker、remio（轉 The Information／Calcbench）、FourWeekMBA 已就公益基金 5%、里程碑 2%、配對費用、RSU 一次認列撰文；IPO 定價本身以完全稀釋股數為慣例（S-1/A 自列 fully diluted 口徑）——落差可能僅存於零售與資料商層，不足以重定價。
- **發行人已中和**：S-1/A 已並列 GAAP 與 Adjusted、已揭露 $14.2B／$24.1B 與股數表，雙觸發 RSU 為 IPO 慣例（先例皆於定價前即知）。
- **量級**：`N_MS` 為裁量且需 90/120 日條件；若上市後股價未達 ×1.5，此通道 12 個月內為 0。

## 5. 否決觸發（寫給 ANALYST 測一）

(1) 具名賣方、研究或評等機構於 S-1 公開後，已以含 `N_PBF`＋`N_VMO`（及 `N_MS` 情境）之完全稀釋股數，且以含 SBC＋非現金捐贈之利潤率讀 Anthropic——已定價（R1）。
(2) 發行人於 S-1/A、424B4 或首份 10-Q 之 EPS 註、非 GAAP 調節或 MD&A 已並列含公益基金股之每股數或「含權益交割費用」之利潤率——已中和（R2）。
(3) `[D]` `d` < 3%，或上市後首 4 季（剔除 IPO 季一次項）`κ` < 10%（兩門檻於生成時凍結）——量級不足（R3）。
(4) 可運作對照只能寫成 L7-I#2 人才誘因、L7-A#2 持股方 FV、L13-A#4 轉債稀釋或一般「SBC 是真成本」論述（無本卡之會計／法律股數分離與認列時點斷點）。
(5) 至測一日 Anthropic 未掛牌，且上市後 12 個月內季報不揭 EPS 分母組成或非現金捐贈——表達或可觀測不可行（R4）。
(6) 公益基金股轉出時不入損益（直接權益分配）且市值資料商已採法律股數——費用通道不成立、股數通道已被資料商中和（只削弱，不單獨否決）。

複查觸發器（若日後殺）：首次里程碑發行公告（8-K 或 10-Q）；公益基金首次轉出股份；市值資料商改變 Anthropic 股數口徑；發行人改變 Adjusted Operating Margin 定義（納入 SBC 或非現金捐贈）。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：SBC 按科目、other operating and administrative 之非現金捐贈、EPS 註之加權股數與排除項、權益變動表之公益基金股轉出。
2. 可交易工具：模型實驗室普通股（上市後）；不選券。
3. 半衰期：IPO 季一次認列（2026 第四季）；RSU 續發加權 2.0 年；里程碑發行依股價路徑。

## 7. 本輪寫入

寫入：本生成卡；`query/QUEUE.md` 新 ANALYST 列（Q-0193）；`query/ARCH_matrix.md` L7［A］標「#6 已生成」；`AIM_FUNNEL.md` §3 一句。不寫入：§1、INDEX.json、ARCH_dead、RETRIG、ARCH_live、`export/LEADS_算力收支.md`（本輪新事實為權益交割與股數，非算力收支；營收數點已在檔）。不改 L7-A#1–#5、L7-P#1–#6、L7-I#1–#5、L13-A#4、C-A5、C-P3、C-I1 結論；不寫 T-15。
