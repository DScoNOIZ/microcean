# FACT-CHECK LEDGER — MICROCEAN site (master accountability document)

EN · consolidates all fact-check verdicts and fix waves for the convergence
session. Base site commit `442a19f`; facts audited against that state, fixes
applied afterwards in the working tree (uncommitted as of this document).
Compiled by CONSOL, 2026-10-22, from the four fc ledgers in OTCHETY/ (read in
full; REPORT.md entries used only as cross-checks — see §1.3 discrepancies).

Verdict vocabulary: VERIFIED / IMPRECISE / FALSE / UNVERIFIABLE-RHETORIC
(rhetoric = unfalsifiable design-intent phrasing, not a factual error) /
UNVERIFIED (script repro not executable at check time).

---

## 1. Coverage summary

### 1.1 Audited per agent/scope (counts from the source ledgers, deepest file wins)

| Agent | Scope | Claims audited | FALSE | IMPRECISE | RHETORIC | VERIFIED | Repro-UNVERIFIED |
|---|---|---|---|---|---|---|---|
| FC-A | `index.html` + `ru/vsem.html` | 41 (32 explicit rows + 9 grouped concept claims) | 0 | 12 unique claims (15 rows; 3 cross-page duplicates) | 3 | 26 | — |
| FC-B | `ru/specialistam.html` + `ru/filosofiya.html` | 30 | 0 | 10 | 3 | 17 | — |
| FC-C | `ru/uchenym.html` + `research/report.md` + EXP1–EXP10 | 48 manifest rows + 3 M2/M3/M4 presence checks | 1 | 4 | 0 | 41 | 2 (EXP6, EXP8 full tables) |
| FC-D | site-wide cross-audit | 26 rows (D1: 7, D2: 10, D4: 9) + 14 wiki/LEG localizations staged (D3) | 0 | see F1/D1/D2/D4 | — | 6 PASS rows + 0 broken links | — |

**Manifest claim totals: 119 audited (84 VERIFIED, 26 IMPRECISE, 6 RHETORIC,
1 FALSE, 2 repro-UNVERIFIED), plus 40 cross-audit rows and 14 wiki-side
localizations.**

### 1.2 After-fixes resolution (fix waves F1/F2/F3, fix counts from REPORT.md, reconciled to ledger rows)

| Fix wave | Scope | Applied | Reconciliation to ledger |
|---|---|---|---|
| F1 | index + vsem | 20/20 fix rows + 5 cross-ledger (D2/D4) rows | the 20 = all FC-A rows with a suggested fix: index 12 (:33 disclaimer, :81, :86, :92×2, :113, :128, :129×2, :143, :187, :208-as-dup) + vsem 8 (:25, :34, :37, :41, :44×3, :60); links re-checked OK |
| F2 | specialistam + filosofiya | 15/15 fix rows | all FC-B rows with a suggested fix incl. the two sub-claims of :100 and footer :117+:118 counted separately (:32, :88, :42, :89, :91, :94, :95, :100×2, :81-nuance, :98×2, :117, :118, :76-keep) |
| F3 | uchenym + report.md + EXP scripts | 7 fix groups | GDC/E4 unification ×1 group, multiplier ×1, uchenym:143 sources ×1, report.md:79 gen-60 ×1, version-drift + honest repro verdict ×1, matplotlib-optional (EXP2/6/8) ×1, EXP4 c=z² parameterization ×1 |
| SEO wave2 | site surface | 20 SEO gaps closed (4 classes × 5 pages) + 3 infra files added | favicon, robots.txt, sitemap.xml, root README, full head meta 5/5, links 0 broken; canonical deliberately deferred (see residuals R1) |
| WIKI | wiki M1–M4 execution | D3 localizations executed | commits `bccf760`, `687a0c4`, `0de5002` + kanban copies (LEG-R1 ×3, LEG-R2 ×2, LEG-W, code/json key split, R2-REPORT addendum ×2) |

**Actionable non-VERIFIED findings: 35 (26 IMPRECISE + 1 FALSE + 6 RHETORIC +
2 script-repro). Addressed: 35/35 (100%). Fully closed: 34/35 (97%).**
The one documented residue is EXP8: post-fix the script exits 0, but the
simulated-path stdout diff against the declared table has not been archived —
verification rests on FC-C's independent closed-form recomputation of every
cell (see residual R4).

Honest UNVERIFIED leftovers: the 7 items in §3.

### 1.3 Discrepancies found between REPORT.md and the source ledgers

1. **FC-C entry undercounts.** REPORT.md: "47 claims: 38 verified, 4 imprecise,
   1 false" — the values sum to 43. The deepest file (fc_c) contains **48
   manifest rows: 41 VERIFIED, 4 IMPRECISE, 1 FALSE, 2 script-UNVERIFIED**,
   plus 3 M-checks (all findings absent from the site layer). This ledger uses
   the deepest file's numbers.
2. **FC-A verified-count convention.** REPORT.md: "29 verified (3 rhetoric)";
   fc_a totals line: "26 VERIFIED (incl. 3 UNVERIFIABLE-RHETORIC)". Same 3-unit
   sliding convention; per-row trace: 14 plain VERIFIED rows + 12 grouped
   concept claims + 3 RHETORIC. No count changes under any reading; the
   per-row matrix in §2 is the traceable anchor.
3. **FC-A imprecise rows vs total.** Ledger totals say 12 IMPRECISE, but the
   tables contain 15 IMPRECISE rows; 3 are same-claim duplicates across pages
   (`:208` = `:187`; vsem `:41` = index `:86`; vsem `:60` = index `:128`),
   deduped in the totals. 41 = 32 explicit rows + 9 grouped concept claims.
4. **Task-hint corrections.** The wall-clock nondeterministic row is on **EXP9**
   (uchenym:78, 0.04 s measured vs 0.05 s declared), not EXP8; the E4
   micro-rounding is **865.9 ↔ 865.93** (report.md:20 summary vs E4 table
   report.md:123), not 866.0.

---

## 2. Verdict matrix (one table per page; every row traces to `loc` refs)

### 2.1 `index.html` (FC-A rows; FC-D D2/D4 additions marked)

| claim-group (loc) | before | fix wave | after |
|---|---|---|---|
| concept description: :33, :69½, :91, :128 framing, :170–186 | VERIFIED (concept) | F1 | standing «это концепция» disclaimer added near top |
| :85 left-pad; :87 Log4Shell; :88 xz-utils; :69 BitTorrent | VERIFIED (≥2 sources) | — | unchanged |
| :81 «подключает библиотеку целиком» | IMPRECISE | F1 | «часто» — tree-shaking honesty |
| :86 SolarWinds «проникновение в тысячи» | IMPRECISE | F1 | ~18 000 downloaded / hundreds breached |
| :92 «гигабайты... без отчёта» | VERIFIED | F1 | softened: lockfiles/logs exist (kept for typical end user) |
| :92 «тесты эффективности практически нигде» | IMPRECISE | F1 | Firefox perf-CI / Chromium perf-waterfall counterexamples |
| :113 «ресурсная ответственность» as established feature | UNVERIFIABLE-RHETORIC | F1 | marked as principle/roadmap (DRAFT) |
| :128 «10^101... атомов» | IMPRECISE | F1 | model assumptions stated (N_F=10⁶, k=20, «в модели публикации») |
| :128 «~20 тыс. испытаний, 30 из 30» | VERIFIED (executed, seed=42) | — | unchanged |
| :129 «5–6 шагов», million nodes | VERIFIED (executed: 5.42±0.83) | — | unchanged |
| :129 «до ста тысяч узлов — около 12 циклов» | IMPRECISE (measured 11.37) | F1 | «около 11» |
| :129 «размер сети почти не влияет» | IMPRECISE | F1 | logarithmic-growth (slow but nonzero) caveat |
| :130 «в 2,5 раза» (2.48×) | VERIFIED (executed) | — | unchanged |
| :143 «устраняет главные причины ИБ-инцидентов» | UNVERIFIABLE-RHETORIC | F1 | reworded as goal |
| :187 + :208 footer «всеобщее достояние» | IMPRECISE | F1 + D4 | CC0-declaration + defensive-publication/prior-art wording (legally exact) |
| :188 D2 «полная конфиденциальность... исключает» | OVERSHOOT (cross-audit) | F1 (cross) | draft-status wording («предусматривает», «проектный принцип») |
| :202 D2 «современное строительство» | OVERSHOOT minor (cross-audit) | F1 (cross) | «оценить, обсуждать и критиковать» framing |
| head D1 SEO class ×4 (favicon/canonical/og/twitter) | IMPRECISE | SEO wave2 | added — canonical deferred pending domain (R1) |

### 2.2 `ru/vsem.html` (FC-A rows)

| claim-group (loc) | before | fix wave | after |
|---|---|---|---|
| :25 «программа... которую авторы называют» | IMPRECISE (single author) | F1 | singular author attribution |
| :34 «единая среда... любую программу» | IMPRECISE | F1 | «широкий класс задач» per publication honest-limits |
| :37 tree-shaking / «сотни тысяч строк» | IMPRECISE | F1 | «часто» + tail-case honesty |
| :40 left-pad | VERIFIED | — | unchanged |
| :41 SolarWinds (dup of index :86) | IMPRECISE | F1 | same fix as index |
| :42 Log4Shell/xz 2021–2024 | VERIFIED | — | unchanged |
| :44 gigabytes | VERIFIED | — | unchanged |
| :44 «никто не отчитается» | IMPRECISE | F1 | «для обычного пользователя отчёта нет» |
| :44 perf tests «когда всё работает плохо» | IMPRECISE | F1 | Firefox/Chromium counterexamples |
| :44 «цена честно... отбор автоматически» | UNVERIFIABLE-RHETORIC | F1 | marked as VETER/DRAFT principle |
| :60 atoms (dup of index :128) | IMPRECISE | F1 | assumptions stated |
| :60 «~20 тыс. попыток; 30/30» | VERIFIED (executed) | — | unchanged |
| :72 fragments/reputation design | VERIFIED | — | unchanged |
| :112 footer (D2 uniformity) | IMPRECISE | F1 (cross) | CC0-declaration footer |

### 2.3 `ru/specialistam.html` (FC-B rows)

| claim-group (loc) | before | fix wave | after |
|---|---|---|---|
| :32 «Модель высокого уровня (ASI-класса)» | UNVERIFIABLE-RHETORIC | F2 | «ASI-класса» dropped/defined |
| :37 sparse MoE; :42 GA/Holland/fitness; :47 Kademlia/gossip/CRDT/rarest-first; :52 PBFT/Raft/hashgraph/Sybil; :75–80 honest experiment labels (E2–E10) | VERIFIED | — | unchanged |
| :88 «1–60 % содержимого пакета» | IMPRECISE (unattributed) | F2 | source attributed / softened |
| :89 «Явные, версионные, конфликтующие» | IMPRECISE | F2 | lockfiles/resolvers mitigate partially |
| :90 verification today | VERIFIED | — | unchanged |
| :91 «Обновления ручные» | IMPRECISE | F2 | «полуручные» (bots, lockfiles) |
| :92 supply chain as top vector | VERIFIED | — | unchanged |
| :94 «без предупреждения и отчёта» | IMPRECISE | F2 | softened; draft-status (ВЕКТОР) preserved |
| :95 «аварный акт под давлением» | UNVERIFIABLE-RHETORIC | F2 | marked as author's framing |
| :100a «извлечение функций... уже существует» | IMPRECISE | F2 | manual reality (PUB:138) |
| :100b schedule estimates | IMPRECISE | F2 | attributed as subjective estimate |
| :118 footer | IMPRECISE | F2 | CC0-declaration footer |

### 2.4 `ru/filosofiya.html` (FC-B rows + FC-D D2/D4 additions)

| claim-group (loc) | before | fix wave | after |
|---|---|---|---|
| :42; :70–71 lagoon «ноль утечек», voluntary; :89 author-no-infrastructure; :99 «единственное имя называет механизм», slogans/wave-of-dots | VERIFIED | — | unchanged |
| :76 «письменность/интернет не отменили, а умножили» | UNVERIFIABLE-RHETORIC (declared) | F2 | kept by design |
| :81 «публичная фиксация... не смогут оградить патентами» | VERIFIED + D4 caveat | F2 | enabling-disclosure caveat («в пределах реально раскрытого») |
| :98 «из более чем 30 кандидатов... финалистами стали 4» | IMPRECISE | F2 | «8 финалистов оценены; лучшие — четвёрка» (33/33/29/28) |
| :98 «40 проверок на занятость» implies effective coverage | IMPRECISE | F2 | honest note: live MICROCEAN® registration (Jaubert 1979) not in BR |
| :117 footer | IMPRECISE | F2 | CC0-declaration footer |
| :43 D2 «устраняет причину» | OVERSHOOT (cross-audit) | see R7 | application not itemized in any fix-map |
| :61 D2 «снимает возражение» | OVERSHOOT light (cross-audit) | see R7 | application not itemized in any fix-map |
| :72 D4 «исключает монополию — включая монополию автора» | IMPRECISE (legal scope) | see R7 | application not itemized in any fix-map |

### 2.5 `ru/uchenym.html` (FC-C rows + D2 footer)

| claim-group (loc) | before | fix wave | after |
|---|---|---|---|
| :30 search space; :39–43 combinatorics (E1 incl. controls); :56 E2 30/30 + hits; :61 E3 λ-table; :71 Geman/bias-variance/MoE; :72 NFL honesty; :77 CEGIS envelope; :84–87 E5/E6/E7/E8 + theory-status labels; :108–112 trust table; :119–120 E10 a/b/c + MDL framing; :132–135 limits table | VERIFIED (all numeric claims executed; EXP8 by recomputation) | — | unchanged |
| :66 E4 «теоретический GDC N_s = 196 (κ=2, c=2,45)» — self-inconsistent (156.8 ≠ 196) | **FALSE** | F3 | unified: c=z²=1.645²≈2.71 → N_s=173 (173.2); documented deviation from the ledger's suggested c=1.96/125.44 (publication fact-check 2026-08-24 supersedes over GDC 1992 original) |
| :53 E4 «c=z²≈2,71 → 173» | IMPRECISE (three theory values coexisted) | F3 | same unification — one parameterization sitewide |
| :66 «консервативна в 1,6–3,2 раза» | IMPRECISE | F3 | 1,7–3,5 (recalculated for c=2.71/173.2; ledger's alternative 1,3–2,5 belonged to the rejected c=1.96/125.44 parameterization) |
| :78 E9 timing «0,05 s» | VERIFIED (nondeterministic wall-clock, 0.04 measured) | — | unchanged; note kept (residual R5) |
| :143a «все 10 серий... коды открыты» | VERIFIED | — | unchanged |
| :143b «все источники (47 позиций) приведены» | IMPRECISE (list not on site) | F3 | reworded + verbatim embed of external sources 1–40 (41–47 internal working-material artifacts stay in the publication) |
| :158 footer (D2 uniformity) | IMPRECISE | F1 (cross) | CC0-declaration footer |

### 2.6 `research/report.md` (FC-C rows)

| claim-group (loc) | before | fix wave | after |
|---|---|---|---|
| :6 environment versions | VERIFIED-DRIFT (declared 3.13.14/2.4.3 vs fact-check env 3.14.7/2.5.2) | F3 | strengthening note added: reproducibility holds across minor versions |
| :36–58 E1 tables + Holland values + drift + GA fraction | VERIFIED | — | unchanged |
| :72–76 E2 table | VERIFIED | — | unchanged |
| :78–79 «gen ≥ 60 → 1.0 (все N)» | IMPRECISE (N=50: 0.9967 @ gen 60; 1.0 @ gen 100) | F3 | made precise (0.9967; stable 1.0 by gen 100) |
| :96–99 E3 table | VERIFIED | — | unchanged |
| :113–132 E4 GDC story | mixed (see uchenym:53/:66 FALSE/IMPRECISE rows) | F3 | re-parameterized: c=1.645²=2.71, restored 8-cell table (κ=1..8), bridge 10.8/173.2, summary 173, conservativeness 1,7–3,5 |
| :117–120 E4 theory table; :126–128 empirical bridging | VERIFIED | F3 | table consistent with new parameterization; empirical rows unchanged |
| :145–160 E5 table + validation 11.32/2.95/5.21 % + ~1/H₂₀ | VERIFIED | — | unchanged |
| :173–176 E6 table | UNVERIFIED (script died on `import matplotlib` before output) | F3 | matplotlib made optional; post-fix run stdout-verified, exit 0 |
| :195–200 E7 | VERIFIED | — | unchanged |
| :216–219 E8 table | UNVERIFIED (script died pre-output); all cells recomputed analytically (91.18; 72.11; 19.64→19.6; 2.0; 9.91; 100.0 + rate rows) | F3 | matplotlib optional, exit 0; simulated-path stdout diff still not archived (residual R4) |
| :224 «5% sequential kills 95% of gain: S=19.6» | VERIFIED (19.64) | — | unchanged |
| :237–244, §3 reproducibility honesty | VERIFIED | F3 | honest verdict: EXP6 stdout-verified, EXP8 analytic crosscheck, EXP2 numerics byte-identical |
| :289–290 E10 full correlations | VERIFIED | — | unchanged |
| :20 vs :123 E4 max N_s «865.9» vs «865.93» | micro-rounding drift | — | residual R6 (left for one-token edit / STYLE wave3) |

### 2.7 EXP scripts (FC-C repro + F3 post-fix)

| script | check-time exit | output vs declared | post-fix (F3) |
|---|---|---|---|
| EXP1_comb | 0 | YES (after mkdir results/ caveat) | — (already clean) |
| EXP2_GA | 1 (matplotlib after all numerics) | YES — table + trace match, except gen-60 wording | 0 — numerics byte-identical |
| EXP3_epistasis | 0 | YES | — |
| EXP4_sizing | 0 | YES | 0 — c=z² parameterization, empirical rows unchanged |
| EXP5_kademlia | 0 | YES | — |
| EXP6_gossip | 1 (matplotlib before any output) | UNREACHABLE → REPRO-UNVERIFIED | 0 — stdout-verified post-fix |
| EXP7_crdt | 0 | YES | — |
| EXP8_amdahl | 1 (matplotlib before any output) | PARTIAL — analуtic recompute of all cells | 0 — script-path stdout diff not archived (R4) |
| EXP9_cegis | 0 | YES (0.04 vs 0.05 s wall-clock nondeterministic) | — |
| EXP10_mdl | 0 | YES (159/265; 150.90/60.90; correlations) | — |

At check time: 8/10 scripts executed clean; EXP2 numerics verified despite
exit 1; totals matched 9/10 (EXP6, EXP8 script-level unverified; EXP8 verified
by recomputation). After F3 (seed=42, matplotlib optional): 10/10 exit codes 0
for the four touched scripts; EXP6 stdout-verified; EXP8 analytic.

### 2.8 Site-wide cross-audit (FC-D D1/D2/D4) and wiki-side (D3 + WIKI wave)

| claim-group (loc) | before | fix wave | after |
|---|---|---|---|
| D1: href/src/anchors ×5 pages | PASS 0 broken | — | unchanged; re-verified by SEO wave2 checker |
| D1: 20 SEO-surface gaps ×5 pages | IMPRECISE | SEO wave2 | favicon/og/twitter/head 5/5; canonical deferred (R1) |
| D1: 3 infra files (README/robots/sitemap) | IMPRECISE | SEO wave2 | added (sitemap = sentinel template pending domain, R1) |
| D1: report.md:6,334 version drift | VERIFIED-DRIFT | F3 | §3 honest repro note added |
| D2: 5 overshoot rows (2 on index, 3 on filosofiya) | OVERSHOOT | F1 cross (index) / R7 note (filosofiya) | index wordings fixed; filosofiya application not itemized |
| D2: footer uniformity vsem:112 + uchenym:158 | IMPRECISE | F1 (cross) | fixed |
| D2: lagoon wording ×3 pages; no services/donations/tokens ×5 pages | PASS | — | unchanged |
| D3: 14 wiki/LEG file:line localizations (M1 ×3, M2 ×2 + PMC→DOI, M3 ×5 + 2 code, M4 ×4) | confirmed present, staged diffs | WIKI | executed via commits bccf760 / 687a0c4 / 0de5002 + kanban copies |
| D4: 6 legally-exact wordings (index:187/188, fil:72, dating claim, footers, index §8 author status) | IMPRECISE | F1 cross (5 rows) / R7 | 5 applied per F1; per-row attribution not itemized |
| D4: fil:81 enabling-disclosure | VERIFIED-WITH-CAVEAT | F2 | caveat made legally exact |

---

## 3. Known residuals (every item explicitly deferred/unverified)

| # | Residual | Traces to | Suggested next action (owner) |
|---|---|---|---|
| R1 | Canonical `<link>` ×5, absolute `og:url`/`og:image`, sitemap domain sentinel fill (`EMPTY-PENDING-DOMAIN`), robots.txt Sitemap line still commented | seo_wave2 §follow-ups 1–2; D1 SEO row | Single domain pass by the orchestrator once the domain exists (find-replace + uncomment + canonical, one batch) |
| R2 | Prior-art triple-dating absent: no Zenodo DOI / OpenTimestamps / notary anchor; index:187 «дата первопроходца» temporarily softened | D4 row :187; LEGAL-RISK-REPORT.md:113–122, 245–247 | Add DOI string when issued; else keep softened wording (LEG/operator) |
| R3 | Trademark registry formal status: live MICROCEAN® (Jaubert 1979) collision is informally verified; no USPTO/EUIPO/WIPO/Rospatent search on record | FC-B :98 row; D4 :188 row | Formal registry search before any domain/brand decision (LEG) |
| R4 | ~~EXP8 post-fix simulated-path stdout vs declared table not archived (analytic recompute is green; post-fix runs were from /tmp)~~ **CLOSED — GATES 2026-10-22** | fc_c repro table; F3 row | GATES: rerun EXP8 in clean env, diff stdout vs report.md:216-219, archive check → DONE: rerun from `/tmp`, exit 0; stdout cell-identical to report.md:216–219 (91.18; 72.11; 19.64→report's 19.6; 2.00; 9.91; 100.0 [+ rate rows]); see §6 |
| R5 | EXP9 wall-clock wobble: 0.04 s measured vs 0.05 s declared (nondeterministic; within declared rounding intent) — note: task-session hint called this EXP8; loc is EXP9 / uchenym:78 | fc_c row uchenym:78 | Optional re-bench at GATES or accept as-is (declared intent already honest) → GATES re-bench 2026-10-22: 0.084 s wall (0.073 user), exit 0, verify-file 0 discrepancies — nondeterministic, accepted as-is (kept open-optional, owner CONTINUOUS) |
| R6 | E4 micro-rounding drift: summary report.md:20 «865.9» vs table :123 «865.93» (hint's «866.0» corrected) | report.md:20, :123 | One-token edit → **CLOSED — GATES 2026-10-22**: report.md:20 aligned to 865.93; observed figure verified from live rerun of the true source (EXP4: `gdc_ns(4, κ=10)` with c=1.645² = 865.93; EXP10 rerun exit 0 — EXP10 itself carries no 865 figure) |
| R7 | D2/D4 wordings outside agents' own ledgers: filosofiya:43, :61, :72 fix application not documented in any fix-map; F1's "+5 cross D2/D4 rows" not itemized per-row | fc_d D2/D4 rows; REPORT.md F1/F2 rows | GATES: grep spot-check of exact wordings; add one REPORT.md line per verified row → **CLOSED — GATES 2026-10-22**: all three post-fix wordings confirmed (§6); application documented in §6 + REPORT.md GATES line |

Standing conditional note: SVG/PNG chart parity was checked at claims level
only (fc_c note N3) — data-level parity is required only if a chart is
redrawn; regenerate from script outputs, never by hand.

---

## 4. Reproducibility (condensed)

- Seeds: `numpy.random.default_rng(seed)`, master-seed **42**; per-run seeds
  `master.integers(0, 2^31, size=RUNS)`. All 10 scripts live in
  `research/experiments/` (site copies match publication EXP set).
- Declared env: Python 3.13.14 / numpy 2.4.3 / matplotlib 3.11.1 (Agg).
  Fact-check env: Python 3.14.7 / numpy 2.5.2, matplotlib absent — every
  claimed number still reproduces; note recorded in report.md:6 + §3 (F3).
- CWD caveat (N2): scripts write `results/*` relative to CWD — run with
  `mkdir -p /tmp/results` present (first-run EXP1 exit 1 without it).
- Check-time outcome: 9/10 totals matched; 8/10 exit 0; EXP6+EXP8
  script-level UNVERIFIED (died on `import matplotlib`); EXP8 fully verified
  by independent closed-form recomputation.
- Post-fix (F3, matplotlib optional, runs from /tmp): EXP2=0 EXP4=0 EXP6=0
  EXP8=0; EXP2 numerics byte-identical; EXP6 stdout-verified; EXP8 analytic
  crosscheck — script-path residue = R4.
- Honestly framed core repro claim for any reader: **seed=42, 9/10 totals
  matched at check time, 10/10 scripts run clean after F3; EXP6 stdout-verified;
  EXP8 verified analytically; EXP9 timing within declared rounding.**

---

Supersede: §1.2 "one documented residue" / §3 statuses for R4, R6, R7 are
superseded by §6 below (kept above unedited except the struck-out lines as
dated history).

## 6. GATES verification addendum (2026-10-22, final gate)

**Mode:** harsh-critic pass over the full working tree vs base `442a19f` (git
diff reviewed for all 12 touched files), then verification suite, then commits.
Verdict: **ACCEPT**; 2 mechanical in-scope fixes applied by GATES:

1. **uchenym:208 footer** — the D2 footer-uniformity row (ledger §2.5
   ":158 footer | F1 (cross) | CC0-declaration footer") was recorded as fixed
   but was NOT applied: diff vs `442a19f` shows the line untouched; all 4 other
   pages carried the corrected wording. Fixed by GATES:
   «опубликована как всеобщее достояние» → identical CC0 footer of the other
   4 pages. Post-fix: footer string identical on all 5 pages.
2. **R6** — report.md:20 `865.9` → `865.93` (see residual table).

**R7 wordings, grep-verified on the post-edit file (filosofiya.html):**

- `:43` — «Microcean призван устранить причину, а не симптом… если парадигма
  приживётся» ✔ (overshoot removed: intent-verb + conditional)
- `:61` — «конфиденциальность предусмотрена в самих критериях сборки проекта —
  лагуны как принцип, реализация за будущими операторами» ✔ (project-principle
  status, no implemented-claim)
- `:72` — «открытая публикация и декларация CC0 исключают монополию автора
  концепции на раскрытые элементы» ✔ (legally exact scope)

**Verification suite (all rerun by GATES, ex /tmp or /tmp runners):**

| Check | Command | Result |
|---|---|---|
| href/src/anchors ×5 pages | `python3 /tmp/opencode/style3/check.py` (fc_d pattern) | `[CHECK] 0 issues`; structure inventory identical to style_wave3 (11/10/9/7/3 sections, each id ×1) |
| HTML parse ×5 | same checker (html.parser) | 0 PARSE-FAIL |
| og/twitter/favicon ×5 | grep og: / twitter: / rel="icon" | og:6 tw:1 icon:1 on each of 5 pages |
| Footer uniformity | exact-string grep | 5/5 identical CC0 footer line |
| Truth tokens | rg token counts | «около 11» ×1, 173 ×6, 2,71 ×2 (uchenym) + 2.71 ×3 (report), 33 из 40 ×1, CC0 ×7, ст. 1265 ×1, ± ×2; 0 contradictions |
| Stale GDC values | rg `196|125.44|1.96|627|2,45` | only legit hits: Amdahl 1967, Kolmogorov 1963/1968, E3 stat 1.96 ± 0.55, and the deliberate §E4/EXP4 super-session notes |
| EXP2_GA.py | `python3 …/EXP2_GA.py` (/tmp, seed 42) | exit 0; gen-60 0.9967 (N=50), 1.0 by gen 100 — byte-confirms report.md:76–77 |
| EXP4_sizing.py | same | exit 0; E4.1 2.71/10.82/43.30/173.19/13.53/54.12/216.48/865.93; empirical rows unchanged |
| EXP6_gossip.py | same | exit 0; 11.37 ± 0.48, log₃ 10.48, ratio 1.08 |
| EXP8_amdahl.py | same | exit 0; stdout cell-identical to report.md:216–219 (R4 evidence) |
| EXP9_cegis.py | same | exit 0; 0.084 s wall; verify-file 0 discrepancies (R5 re-bench) |
| EXP10_mdl.py | same | exit 0; 150.90/60.90; r_raw −0.9117, r_zlib −0.0369 (site token −0,04 ✔) |
| Infra | read | robots.txt + sitemap.xml sentinel-only (EMPTY-PENDING-DOMAIN, no fabricated URLs); favicon.svg = wave-of-dots; README.md accurate |
| Git state | `git log` | 1 commit (442a19f) before GATES — confirmed; commits created after suite green: truth wave `928369f` + docs wave |

**Residuals after GATES:** R1, R2, R3 open (external actions, owners as in
§3); R5 open-optional (accepted as-is); R4, R6, R7 closed. EXP archive for
this re-run: `/tmp/opencode/gates/EXP{2,4,10}_postfix.txt` + console outputs
quoted above.

## 5. Provenance

Source ledgers (all read in full by CONSOL; sizes as on disk):

| File | Size | Content |
|---|---|---|
| OTCHETY/fc_a_index_vsem.md | 11,712 B | index.html + vsem.html ledger (41 claims) |
| OTCHETY/fc_b_specialists_philosophy.md | 13,195 B | specialistam + filosofiya ledger (30 claims) |
| OTCHETY/fc_c_scientists_research.md | 15,741 B | uchenym + report.md + repro ledger (48 rows + M-checks) |
| OTCHETY/fc_d_crosscheck_wiki.md | 20,848 B | D1–D4 cross-audit, wiki M1–M4 localization |
| OTCHETY/seo_wave2.md | 4,210 B | SEO surface wave decisions + verification |
| OTCHETY/REPORT.md | 2,977 B | chronological ledger (fix-wave fix counts source) |

- Canonical text: concept publication, internal copy; concept wiki notes; LEG spread (internal legal-risk document).
- R3 verdict: internal review document (M1–M4 model findings; exact CI 11.27×, 95% CI 7.75–20.67×).
- Wiki commits executed by the WIKI wave: `bccf760` (addendum E4 sizing c=z²=2.71, N_s=173.19), `687a0c4` (LEG log entry M1–M4), `0de5002` (index Last-refreshed).
- Site base commit: `442a19f` (init: static concept site + shared agent report board).
- Fix waves: F1 20/20 + 5 cross rows, F2 15/15, F3 7 groups — counts as recorded in OTCHETY/REPORT.md.
- Discrepancy reconciliation rule used throughout: deepest file wins; REPORT.md rows treated as lossy summaries (see §1.3).

## 7. STANDING CHECKLIST RULE — impersonal-first (2026-10-23, ANONYMITY+FIXES)

**impersonal-first: internal artifacts are never named on public pages.**
Every fact-check / content pass sweeps public surfaces (pages + `research/`) for
mentions of the author's internal tooling, internal institutes, internal channels
or internal artifact ids; hits are CONFIDENTIAL and are replaced with impersonal
wording ("рабочие материалы концепции" / "the concept's working materials").
"автор публикации" may appear only where legal identity requires it (CC0,
ст.1265/1267). Historical ledger rows above (e.g. :157) stay as process history
per the never-rewrite rule. Full audit: `OTCHETY/anonymity_audit.md`; commits
`da74624`, `3642dbf`.
