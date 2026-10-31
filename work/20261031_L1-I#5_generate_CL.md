# L1-I#5 生成卡｜能源與電力：誘因（大負載之「韌性 vs 可中斷」選擇——以接受限電換取較快併網；此選擇決定容量需求中屬大負載之量，進而決定 IPP 容量稀缺租之存續）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；query/ARCH_live.md；archive/drive/USED_20260926_L1-I_generate_GK.md；archive/work/20261009_L1-I#2_generate_CL.md；archive/work/20261016_L1-I#3_generate_CL.md；archive/work/20261024_L1-I#4_generate_CL.md；work/20261024_L1-I#4_test1_CL.md；query/ARCH_live.md#L2-I#4、#L2-P#3 | EMITS: work/20261031_L1-I#5_generate_CL.md -->
**日期：** 2026-10-31　**角色：** SCOUT@CL（排程 SCOUT-GEN，配額 1→2／6）　**格：** L1-I　**序：** #5　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格。非「已殺／刻意排除」格中最後測一最舊＝2026-10-24（L1-I#4、L3-P#4、L3-A#4、L3-I#4、L4-P#4）→ 依表序取 **L1-I**（L1-P＝刻意排除 T-11 不取）；既有生成 4 份 → #5。
- Tokenomics 線索（CLAUDE.md §11）：已查 `curtailment`／`flexible`／`demand response`，命中 0 筆。內部數字（§12）：未取用。
- 比對（本卡須異型）：
  - **L1-I#1**（GK）：發電開發商佇列佔位 → 公開佇列高估。本卡選擇者為**負載**，非發電側佇列。
  - **L1-I#2**：受管電業費率基誘因、最低需量覆蓋率；損失落於其他費率類別。本卡不以費率類別間轉嫁為落差（測一 (6) 防線）。
  - **L1-I#3**：買方減碳宣稱 → 核電長約屬性溢價。本卡無環境屬性。
  - **L1-I#4**：表後淨額沖減輸電／容量計費基礎（費率套利）。本卡**不談表後發電與計費淨額**；談負載**是否以韌性（firm）身分進入容量需求**——表前併網、接受限電之負載不需容量背書。
  - **L2-I#4**（表後專屬發電續約權）、**L2-P#3**（功率擺盪能量平衡）：前者為發電資產殘值、後者為物理平滑；本卡為容量市場之需求側定義。
  - **T-11**（電網容量／機組交期）：本卡不以「供給不足或交期」為機制；機制為需求側選擇如何計入容量需求。測一若發現落差只能以 T-11 表述 → 否決 (6)。
  - ARCH_dead：C-I3′／N-02（利益未分列）——測一 (1) 為同類可分離性題；主體與機制不同，非已殺同型。
- §7-10 領域最近公開：FERC 2026-10-09 令（eLibrary 20261009-3055）接受 PJM 大負載定義與 Large Load Registry（≥ 50 MW），**駁回** IRAS（不配新容量之大負載以接受限電換併網）、BYONC 及相關容量市場變更（含 2029/30 起將合格新大負載排除於容量需求計算之一部分），理由為侵入州零售管轄與歧視大負載；Rosner 協同意見要求州監理訂定限電順序。PJM 2028/29 BRA（2026-07-14 公布）全區於上限 $325/MW-day UCAP 出清，RPM 138,317.8 MW＋FRR 13,765.6 MW，低於可靠度需求；需求內含 Large Loads 1,374.5 MW UCAP；價格上下限涵蓋至 2029/30 交付年，該 BRA 排於 2026-12。下一檢查點＝PJM 是否重提資源充足方案、2029/30 BRA 結果、州（OH／PA）限電順序立法或規則、SPP 高衝擊大負載服務（2026-06 獲准）實施、VST／CEG／TLN／NRG 3Q26 10-Q。

## 1. 落差一句

大負載可二選一：以**韌性負載**進入容量需求（等待配對新容量），或以**可中斷負載**換取較快併網（PJM IRAS／Connect and Manage、SPP 高衝擊大負載服務、ERCOT SB 6 限電義務、Google 與 I&M／TVA／Entergy Arkansas／Minnesota Power／DTE 合計約 1 GW 需量反應長約「allow new data centres to connect more rapidly」）。若選後者之比例上升，容量需求中歸屬大負載之增量（2028/29 BRA 之 Large Loads 1,374.5 MW 與「約 2,000 MW」預測增量）可被移出或抵減，容量稀缺租縮小；FERC 10-09 令把此選擇權推回州層，使其時點與規模不可見。種子主張：市場把 IPP 容量收入（2027/28、2028/29 連續於上限出清；Jefferies：「higher capacity prices for longer」）讀成資料中心韌性需求之結構性稀缺，未拆出依存於「大負載不得以可中斷身分入網」此一監理狀態之成分；collar 於 2029/30 後失效之同時，若州層限電規則或 PJM 修正方案落地，上限後之價格路徑取決於可中斷比例。**方向未定**：FERC 駁回本身延長稀缺（對 IPP 為正）；若大負載偏好韌性（24/7 訓練負載、Bressler「tends to run 24/7」），可中斷比例低，落差不存在。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：大負載之服務型態選擇 ＝ f（併網等待時長、可接受之限電時數與補償、可靠度需求之負載型態（訓練 vs 推論）、州零售規則）；監理決定此選項是否存在 |
| 選擇者 | 資料中心開發商／雲業者（韌性 vs 可中斷）；PJM（方案設計與重提）；FERC（管轄邊界）；州監理（限電順序、零售費率） |
| 已讀事實 | Utility Dive 2026-10-12（FERC 10-09 駁回 IRAS／BYONC、接受 Registry；FERC：「appear to dictate which retail customers taking retail service will be curtailed」；Jefferies：利於 CEG／NRG／TLN／VST）；TechTarget 2026-10-14（Registry ≥ 50 MW、欄位含供電安排與備援；IRAS 含 2029/30 起排除合格新大負載於部分容量需求計算；PJM 未說明下一步）；POWER 2026-07-17（2028/29 BRA 全區 $325 上限、Large Loads 1,374.5 MW UCAP、預測峰值約 +2,000 MW 主因資料中心、collar 涵蓋至 2029/30、DR 出清 7,017.4 MW）；Utility Dive 2026-07-15（無上限模擬約 $555/MW-day；DR 7,365 MW——與 POWER 數不合，待測一核對）；AI Magazine（Google 1 GW 需量反應入長約、DTE 350 MW DR；「There are limits to how flexible a given data centre can be」） |
| 未證之連結 | 大負載選可中斷服務之比例（任何 ISO／州）；可中斷大負載是否與如何自容量需求移出（PJM 方案已駁回；SPP／ERCOT 口徑）；IPP 容量收入中屬上限出清 × 大負載增量之敏感度；2029/30 BRA 後之規則狀態 |
| 量綱 | 可中斷大負載 MW ÷ 大負載預測增量 MW（%）；容量需求變動 MW → 出清價變動（$/MW-day，依 VRR 斜率）；IPP 容量收入 ÷ 總收入（%） |
| 半衰期 | 年（2029/30 BRA 2026-12；collar 後首個 BRA 約 2027；州立法 1–2 年；IPP 容量收入按交付年鎖定） |

## 3. B 端可觀測載體（只指名）

1. FERC 2026-10-09 令報導 https://www.utilitydive.com/news/ferc-pjm-large-load-interconnection-iras-byonc/832716/ ；https://www.techtarget.com/it-infrastructure/news/366652121/FERC-approves-PJM-load-registry-rejects-curtailment-plan ；FERC eLibrary 20261009-3055、PJM 申請 20260813-5118（未讀原文）
2. PJM 2028/29 BRA https://www.powermag.com/pjms-2028-2029-capacity-auction-falls-short-of-reliability-standard-for-second-straight-year/ ；https://www.utilitydive.com/news/pjm-capacity-auction-price-cap-reserve-shortfall/825282/ ；PJM 結果報告 https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2028-2029/2028-2029-bra-results-report.pdf （未讀）
3. Google 需量反應長約 https://aimagazine.com/news/google-1gw-milestone-for-ai-grid-flexibility ；https://www.datacenterdynamics.com/en/news/google-partners-with-im-and-tva-to-expand-use-of-demand-response-at-its-ai-data-centers/ （未讀）
4. Duke Nicholas Institute「Rethinking Load Growth」https://nicholasinstitute.duke.edu/news/publication/24519 （本輪 fetch 被機器人防護拒絕；失敗歸因＝站方封鎖，非存在性主張）
5. 未讀：VST／CEG／TLN／NRG 10-Q 3Q26（sec.py）之容量收入與 PJM 規則風險段；SPP 高衝擊大負載服務令（2026-06）；ERCOT SB 6 限電規則（PUCT 58481 系列）；OH／PA 限電順序立法；具名賣方就可中斷大負載對容量價格之量化。

## 4. 不寫

H1／H5、表達工具選擇、方向判斷。

## 5. 否決觸發（測一逐條實讀）

1. **可分離性：** 任一 ISO、州監理或上市 IPP／負載之一手或具名來源均無法給出可中斷大負載之 MW、比例或對容量需求之量化 → 否決（C-I3′／N-02 型）。
2. **誘因不存在或不重要：** 具名一手顯示大負載幾乎全選韌性服務（例如可中斷選擇 < 10% 大負載增量），或可中斷負載本就不入容量需求、不改出清 → 否決。
3. **已被定價／已揭露：** 具名賣方、評等機構或 IPP 本身已就「大負載可中斷化」量化容量價格或盈餘敏感度 → 否決（無錯價）。
4. **窗不足：** 2029/30 BRA 前之規則狀態已定、且其後 12 個月內無規則變動可能（PJM 不重提、州無立法進程）→ 否決（重定價窗 < 12 個月或不存在）。
5. **方向抵銷：** FERC 駁回延長稀缺之效果與可中斷化之效果無法定號（例如 collar 後無上限價格上升蓋過需求移出）→ 不否決但標方向不定，不得合併為同向落差。
6. **主體錯置：** 落差只能以供給不足／機組交期（T-11）或費率類別轉嫁（L1-I#2 型）或表後淨額（L1-I#4 型）表述 → 否決本卡、不得改寫為他卡。
