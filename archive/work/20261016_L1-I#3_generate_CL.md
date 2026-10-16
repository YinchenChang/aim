# L1-I#3 生成卡｜能源與電力：誘因（買方之自願減碳宣稱誘因 → 既有核電長約溢價；溢價之價值取決於 GHG Protocol Scope 2 計帳規則）
<!-- BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | CONSUMES: query/ARCH_matrix.md；query/ARCH_dead.md；archive/drive/USED_20260926_L1-I_generate_GK.md；archive/drive/USED_20260926_L1-I_test1_GK.md；archive/work/20261009_L1-I#2_generate_CL.md；work/20261009_L1-I#2_test1_CL.md；archive/drive/USED_20260926_L1-A_generate_GK.md | EMITS: work/20261016_L1-I#3_generate_CL.md -->
**日期：** 2026-10-16　**角色：** SCOUT@CL（排程 SCOUT-GEN，chain，配額 5／6）　**格：** L1-I　**序：** #3　**上限：** 生成卡，非 T／L／M
**⚠ 無金額、無部位、無尺碼。** 不寫 H1。不執行終端篩選（§7-3）。不由目標反推（§1）。

---

## 0. 範圍與比對

- 選格（SCOUT.md §C-2）：ARCH_matrix 無【未生成】／已生成未測格（L1-A#3 已於本日測一）。非「已殺／刻意排除」格中最後測試日最舊＝2026-10-09（L1-I、L3-P、L3-I）；同日依表序取 **L1-I**（L1-P＝刻意排除 T-11 不取）。既有生成 2 份 → #3。
- Tokenomics 線索（CLAUDE.md §11）：已查 `Scope 2`／`GHG Protocol`／`hourly matching`／`nuclear`／`PPA`，命中 0 筆。
- 比對（本卡須異型）：
  - **L1-I#1**（GK）：發電側併網佇列近零成本佔位 → 公開佇列高估；死於承諾 MW 不可分離。本卡選擇者為**電力買方（超大規模雲業者）**，誘因為**自願減碳宣稱**，非佔位成本。
  - **L1-I#2**：受管電業以費率基報酬為誘因擴建、最低需量覆蓋不足；死於損失落於其他費率類別（非股東）。本卡主體為**非受管發電商（IPP）**之雙邊長約，損益直接落於上市發電商，不經費率分攤。
  - **L1-A#1**（GK）：PPA 鎖定價 − 現貨＝存量（會計恆等）；本卡不談鎖定價對現貨之差，談**屬性溢價之誘因來源與其規則依存**（型態 I）。REC 於 L1-A#1 僅為附帶問題。
  - ARCH_dead：C-I3′／N-02「利益未分列」——本卡之溢價亦可能未分列，屬測一 (1) 之否決題，非已殺同型（主體與機制不同）。
- §7-10 領域最近公開：GHG Protocol「Scope 2 Public Consultation Summary of Feedback」（2026-07-29）；Talen FY25 10-K（2026-02）；Constellation FY25 10-K（2026-02）。下一檢查點＝GHG Protocol ISB／TWG 後續草案與第二輪諮詢公告；Talen、Constellation 3Q26 10-Q（2026-11 初）。

## 1. 落差一句

超大規模雲業者對既有核電長約支付之溢價（Talen 10-K：「deliver carbon-free power to AWS … at anticipated premium prices」；Constellation–Meta Clinton 20 年 PPA「to support Meta's clean energy goals」）至少部分是**買方減碳宣稱之價值**，而宣稱之價值由 GHG Protocol Scope 2 規則決定；修訂案擬引入逐時匹配與可輸送性（deliverability），諮詢回饋「low levels of support」、另擬「legacy clause to maintain the eligibility of existing long-term contracts」。種子主張：市場把核電長約讀成「純電力＋容量之長期定價」，未拆出**依存於自願標準與買方誘因之屬性溢價**，及其對新約續約／擴約定價之規則敏感度。**方向未定**（逐時匹配亦可抬高穩定零碳電源之屬性價值；legacy clause 可保護既有約）。

## 2. 機制型態

| 項 | 內容 |
|---|---|
| 型態 | [I] 誘因：買方（雲業者）之自願淨零／24/7 目標 → 願付屬性溢價；溢價大小 ＝ f（Scope 2 規則下該合約可計之減量、買方目標之約束力、替代屬性來源之價格） |
| 選擇者 | 買方（是否續約、擴約、以何價格）；GHG Protocol ISB（規則內容、legacy 範圍、生效日）；IPP（以既有機組簽約 vs 留於批發市場） |
| 已讀事實 | Talen FY25 10-K：1,920 MW、至 2042、「minimum commitments」、爬坡至遲 2032、「front-of-the-meter」轉換 2026 春起、2027 春完成、對 AWS 開立 LC；Constellation FY25 10-K：Meta–Clinton 20 年 PPA 自 2027-06 起、「supports Meta's clean energy goals」，買方「procuring … RECs, EFECs, or emissions offsets」；GHG Protocol 2026-07-29 回饋摘要（見 §3-1） |
| 未證之連結 | 溢價是否可自申報分離（合約價格多未揭露）；溢價中屬性部分 vs 速度／容量／可靠度部分之比；合約是否含規則變動條款（重議、價格調整）；既有約是否全數落入 legacy；溢價占 IPP 盈餘之量級 |
| 量綱 | 屬性溢價（$/MWh）× 合約 MWh ÷ IPP 調整後 EBITDA（%）；規則情境下續約溢價變動（$/MWh） |
| 半衰期 | 年（規則定稿與生效數年；合約 15–20 年；續約／擴約為重定價點） |

## 3. B 端可觀測載體（只指名）

1. GHG Protocol「Scope 2 Public Consultation Summary of Feedback」https://ghgprotocol.org/sites/default/files/2026-07/S2-ExecutiveSummary-PublicConsultation%20ummaryofFeedback-2026.07.29.pdf （已讀摘要：hourly matching／deliverability「low levels of support」；legacy clause 獲廣泛支持；無定稿／生效日）；開放諮詢公告 https://ghgprotocol.org/blog/release-ghg-protocol-opens-public-consultations-scope-2-and-electricity-sector-consequential （未讀）。
2. Talen 10-K FY25 https://www.sec.gov/Archives/edgar/data/1622536/000162253626000017/tln-20251231.htm （AWS PPA 條款敘述；已讀 §2 所錄）；Talen 10-Q 2Q26（未讀）。
3. Constellation 10-K FY25 https://www.sec.gov/Archives/edgar/data/1868275/000186827526000032/ceg-20251231.htm （Meta–Clinton、Microsoft–Crane；已讀 §2 所錄）；Vistra 10-K／10-Q（Comanche Peak 長約，未讀）。
4. 買方揭露：Amazon、Meta、Microsoft、Google 永續報告之 Scope 2 市場法口徑與 24/7 目標（未讀）；InfluenceMap 企業對 Scope 2 諮詢之立場 https://influencemap.org/insight/Corporate-Engagement-on-the-GHG-Protocol-Scope-2-Consultation-39494 （未讀）。
5. 具名賣方對核電長約價格之估計與是否拆屬性溢價（未讀）。

缺段（§7-2）：合約價格與溢價分解之原文；本輪未讀；非「不存在」。

## 4. 最強反方（具名）

| # | 反方 | 出處 | 打擊 |
|---|---|---|---|
| R1 | 溢價主因為「速度到電力」與穩定容量，非屬性；規則變動不影響買方支付意願 | 載體 2、3（買方動機未直接揭露） | 機制 |
| R2 | legacy clause 保護既有長約；且 minimum commitments 使合約期內現金流不依規則 | 載體 1、2 | 傳導 |
| R3 | 逐時匹配反而抬高穩定零碳（核電）屬性價值；方向對 IPP 有利 | 載體 1（修訂方向） | 方向 |
| R4 | 合約價格不揭露，溢價不可分離 → 不可觀測 | 載體 2、3 | 可觀測性 |

## 5. 否決觸發（寫給 ANALYST 測一）

(1) ≥ 2 份既有核電長約之價格或溢價（$/MWh）在申報、法說或具名可信估計中均不可得，致屬性溢價不可分離；或
(2) 合約條款（申報所述）顯示買方義務為固定量價且與屬性計帳無關，且無重議／規則變動條款，致合約期內無傳導，而續約點落於 ≥ 10 年後；或
(3) GHG Protocol 現行修訂文件之 legacy clause 明確涵蓋既有長期合約，**且**修訂方向對穩定零碳電源屬性價值為正（方向非本卡所設之風險）——此時落差不存在於既有約，只存於新約；或
(4) `[D]` 量級：可估之屬性溢價 × 合約量 < 主要 IPP 調整後 EBITDA 之 5%；或
(5) 買方於公開揭露明示簽約主因為容量／速度而非減碳宣稱（R1 成立）；或
(6) 公司或具名賣方已逐項揭露或建模屬性溢價對規則之敏感度（已定價）。

## 6. 轉入個股層時必問（§7-4，本輪不答）

1. 財報科目：合約收入（Contracted Revenues）、LC／擔保、REC／EFEC 銷售收入。2. 可交易工具：美股上市 IPP（不選）。3. 半衰期：年（規則定稿；續約點）。

## 7. 本輪寫入

寫入：本卡；`query/ARCH_matrix.md` L1［I］格加「#3 已生成」；`AIM_FUNNEL.md` §3 句與日期行；`query/QUEUE.md` 新增 ANALYST 列 Q-0056。不改 L1-I#1／#2、L1-A#1／#2／#3、L1-P（T-11）、C-I3′、N-02 結論。
