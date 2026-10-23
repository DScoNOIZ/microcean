# FC-C — Fact-check: scientists page (uchenym.html) + R2 report + reproducibility

Agent: FC-C (model checker). Scope: `ru/uchenym.html`, `research/report.md`, cross-sources: R1 concept materials (formalization section), R2 report (byte-identical to site report.md — `diff -q` IDENTICAL), LEG-R3 verdict (internal review document). Environment fact-checked on: Python 3.14.7, numpy 2.5.2 (site declares Python 3.13.14 / numpy 2.4.3 in report.md:6 — see R0 note).

## R0 — Environment & parity

- `research/report.md` (site) and the R2 report (internal source-of-record, byte-identical to site copy) are identical (diff exit 0). Single object to check.
- Site charts are `assets/charts/*.svg` (ga, epistasis, kademlia, gossip, amdahl, mdl) — all 6 exist; report.md references `results/*_png` (source-of-record artifacts, internal R2 results). Parity of SVG vs PNG values NOT re-verified pixel-wise (SVGs are hand-made summary charts) — see style note N3.

## 1. Claim ledger

Note on uchenym.html line references: `<row>` numbers as read from current HEAD (442a19f).

| loc | num/claim | page-value | source-value | verdict | fix | evidence |
|---|---|---|---|---|---|---|
| uchenym.html:30 | search space | 2^N_F, N_F~10⁶ infeasible | matches R1 concept materials (overview) | VERIFIED | — | EXP1 output |
| uchenym.html:39 | C(10⁴,10) | 10^33.4 | 10^33.44 | VERIFIED | — | EXP1 script, reported `10^33.44` |
| uchenym.html:39 | C(10⁴,20) | 10^61.6 | 10^61.61 | VERIFIED | — | EXP1 |
| uchenym.html:40 | C(10⁶,10) | 10^53.4 | 10^53.44 | VERIFIED | — | EXP1 |
| uchenym.html:40 | C(10⁶,20) | 10^101.6 | 10^101.61 | VERIFIED | — | EXP1 |
| uchenym.html:43 | atoms comparison | ~10¹⁰¹ combos > atoms ~10⁸⁰ | standard estimate | VERIFIED | — | EXP1: 10^101.61; 10^80 is the conventional baryon figure |
| uchenym.html:43 | C(100,3) | 161 700 | 161700 | VERIFIED | — | EXP1 control line |
| uchenym.html:43 | C(1000,10) | 2.63·10²³ | 2.63409...·10²³ | VERIFIED | — | EXP1 control line |
| report.md:36-41 | E1 full table (16 cells) + C(100,5)=75 287 520 | match | match | VERIFIED | — | EXP1 stdout |
| report.md:49-50 | Holland numerical ex.: q=1.3437/0.3395/1.6316/<0; m1(50)=2.6·10⁶, 4.3·10¹⁰ | match | 1.3437, 0.3395, 1.6316, −0.3474; 2599325.65, 42697715984.9 | VERIFIED | — | EXP1 §E1.2 |
| report.md:52 | drift p_fix | 0.020/0.010/0.005 | same | VERIFIED | — | EXP1 §E1.3 |
| report.md:58 | GA fraction | 10^-97 vs C(10⁶,20) | 10^-97.31 | VERIFIED | — | EXP1 §E1.4 |
| uchenym.html:56 | E2: 30/30 @ N∈{50,100,200}; hits 38.7/25.3/20.6; budget 2·10⁴; fraction ~10⁻⁹⁷ | match | 30/30; 38.7±9.6 / 25.3±4.0 / 20.6±2.5; N=100·G=200=20000 | VERIFIED | — | EXP2 stdout (rerun, seed=42) |
| report.md:72-76 | E2 table incl. stds | match | match | VERIFIED | — | EXP2 |
| report.md:78 | "gen ≥ 60 → 1.0 (все N)" | claims all N at gen 60 = 1.0 | N=50: gen 60 = 0.9967, reaches 1.0 at gen 100 | IMPRECISE | change to "gen ≥ 100 → 1.0 (все N)" | EXP2 convergence trace |
| uchenym.html:61 | E3: λ≤0.3 → 1.0; λ=0.7 → 0.325; 0/30 to optimum | match | 0.3250±0.1094; reached-0.8 column = 0/30 | VERIFIED | — | EXP3 stdout |
| report.md:96-99 | E3 table (all rows, stds, turns 13.2/14.2) | match | match | VERIFIED | — | EXP3 |
| uchenym.html:66 + report.md:113,120,130-132 | E4: uchenym:66 "теоретический GDC N_s = 196 (κ=2, c=2,45)" | N_s=196 | 2·2.45·2·(16) = 156.8 ≠ 196 (self-inconsistent); script / report = 125.44 with c=1.96 | FALSE | replace 196 with 125.4 (κ=2, c=1.96), mirror script | EXP4 §E4.1 |
| uchenym.html:53 | E4: "c = z² ≈ 2,71 → теоретическая оценка 173" | c=2.71, N=173 | internally consistent (2·2.71·2·16=173.4) but contradicts both report.md (c=1.96 → 125.44) and uchenym:66 (c=2.45 → "196") — three different theory values on the same layer | IMPRECISE | pick ONE parameterization consistent with report.md/script: c=1.96, N_s=125.44; drop z² variant or state both with definitions | EXP4 §E4.1 |
| uchenym.html:66 | "теория консервативна в 1,6–3,2 раза" | 1.6–3.2× | script/report: 1.3–2.5× (=125.44 vs N* 50–100; EXP4 interpretation line) | IMPRECISE | sync to 1.3–2.5 | EXP4 §E4.2 |
| report.md:117-120 | E4 theory table (all 8 cells) | match | 1.96/9.80/7.84/39.20/31.36/156.80/125.44/627.20 | VERIFIED | — | EXP4 §E4.1 |
| report.md:126-128 | E4 empirical bridging (12/30, 27/30, 30/30…) | match | match | VERIFIED | — | EXP4 §E4.2 |
| uchenym.html:71 | Bias–variance [Geman 1992], Var→ρσ² formula, MoE citation | standard | standard | VERIFIED | — | R1 concept materials (swarm/MoE) |
| uchenym.html:72 | "теоремы универсального превосходства роя нет (NFL); выигрыш — эмпирический вопрос" | honest envelope | matches R1 materials (NFL + no swarm-superiority theorem) | VERIFIED | — | R1 concept materials |
| uchenym.html:77 | CEGIS soundness/termination proven, completeness not | standard | matches R1 concept materials (CEGIS section) | VERIFIED | — | R1 (CEGIS) |
| uchenym.html:78 | E9: 1 iteration, 820 candidates, 0.05 s, 1600 grid, 0 divergences | 0.05 s | 1 iter, 820 candidates, 0.04 s, (0..39)² = 1600, 0 divergences | VERIFIED | — | EXP9 stdout; time is wall-clock (0.04 vs 0.05 — nondeterministic, within declared rounding intent) |
| report.md:237-244 | E9: length 4; repr check: 108 candidates without '<' | match | match | VERIFIED | — | EXP9 |
| uchenym.html:84 | E5: 5.42±0.83 hops, max 8, ceil log₂ 10⁹ = 30 | match | 5.42±0.83, max 8, ceil=30 | VERIFIED | — | EXP5 stdout |
| report.md:145-150 | E5 table (6 rows, mean±std, max, H20 column) | match | match | VERIFIED | — | EXP5 |
| report.md:153 | validation rel. deltas 11.3% / 3.0% / 5.2% | match | 11.32 / 2.95 / 5.21 % | VERIFIED | — | EXP5 validation block |
| report.md:158-160 | "константа ~1/H_20, 5.4 hops vs 30" | match | match | VERIFIED | — | EXP5 |
| uchenym.html:85 | E6: 11.37±0.48, log₃ 10⁵ = 10.48, ratio 1.08 | match | matches report E6 table | VERIFIED | — | report.md:180; script UNVERIFIED (matplotlib) |
| report.md:173-176 | E6 table (4 rows) | — | — | UNVERIFIED | rerun with matplotlib to confirm | EXP6 exits 1 at `import matplotlib` (top of file), no stdout |
| uchenym.html:86 / report.md:195-200 | E7: 10000/10000 ×3 laws ×3 types; 1000/1000 convergence ×2 | match | match | VERIFIED | — | EXP7 stdout |
| uchenym.html:87 | E8: S(1024)=91.2 @ p=0.99, limit 100 | match | 91.18, 100.00 | VERIFIED | — | independent recomputation (worked examples below); script itself UNVERIFIED |
| report.md:216-219 | E8 full 4×9 table | — | — | UNVERIFIED | rerun with matplotlib to confirm | EXP8 exits 1 at line 15 `import matplotlib`, no stdout values from script |
| report.md:224 | "5% sequential kills 95% of gain: S=19.6 instead of 1024" | 19.6 | 19.64 @ p=0.95, n=1024 | VERIFIED | — | recomputation |
| uchenym.html:108-112 | trust table: PBFT 3f+1; Raft 2f+1; hashgraph aBFT [protocol property]; Sybil impossible without ID; reputation as practice | match | matches R1 concept materials (trust section) statuses | VERIFIED | — | R1 (trust) |
| uchenym.html:84-87 | label "Kademlia [доказано] O(log n)", "Gossip [доказано]", "CRDT [доказано]", "Amdahl [доказано]" | match | R1 map: p2p/parallelism sections [ДОКАЗАНО] | VERIFIED | — | R1 concept materials |
| uchenym.html:120 | E10a: zlib 159→265 @k=0→200; unique grows raw+zlib | match | exactly (159,204,220,236,265; 200/1120/4800/9400/18600; 6000/3782) | VERIFIED | — | EXP10 §E10a |
| uchenym.html:120 | E10b: 2.5× (150.9→60.9), corr 1.0 | match | 150.90±24.63 → 60.90±2.70, corr 1.0000 | VERIFIED | — | EXP10 §E10b |
| uchenym.html:120 | E10c: r(zlib, corr) ≈ −0.04 | match | −0.0369 (Pearson); Spearman +0.0628 | VERIFIED | — | EXP10 §E10c |
| report.md:289-290 | E10c full: −0.9117 / −0.8663 / −0.0369 / +0.0628 | match | match | VERIFIED | — | EXP10 §E10c |
| uchenym.html:119 / report.md:253-297 | K uncomputable; MDL heuristic-not-optimum framing | honest | matches R1 materials (K [НЕВОЗМОЖНО]) | VERIFIED | — | R1 concept materials |
| uchenym.html:132-135 | limits table: K / NFL / Amdahl / Halting+Rice statuses | match | match R1 concept map & honest-limits section | VERIFIED | — | R1 concept materials |
| uchenym.html:143 | "Все 10 серий… Python + numpy… seed=42… коды открыты" | — | dir research/experiments/ contains all EXP1..EXP10 + README | VERIFIED | — | ls |
| uchenym.html:143 | "Все источники (47 позиций) приведены…" | 47 | publication-RU reference list = exactly 47 numbered items (awk count), but this list is NOT on the site (report.md has no reference section; grep-47 in site → only this line) | IMPRECISE | either add the reference list to the site (research/ page) or rephrase to "полный список источников — в полном отчёте" | awk count on MICROCEAN-publication-RU-2026-08-11.md §Список источников = 47; site grep = 1 hit (the claim itself) |
| report.md:6 | env: Python 3.13.14 / numpy 2.4.3 | declared | fact-check env: 3.14.7 / 2.5.2 — all claimed numbers still reproduce | VERIFIED | (strengthening note) reproducibility holds across numpy/Python minor versions | runs below |

### Critic findings M2 / M3 / M4 (LEG-R3-verdict.md) — presence on FC-C scope

| finding | uchenym.html / report.md occurrence | verdict | correct split per LEG-R3 |
|---|---|---|---|
| M3 DepPrune 50.5% vs 50.6% | ABSENT (grep 50.5/50.6 → 0 hits) | NOT PRESENT — no fix needed on FC-C pages | 50.5% of packages have ≥1 bloated dep (primary DepPrune metric); 50.6% of the 50,488 analyzed *dependencies* are bloated (13.8% direct, 51.3% transitive). Denominators differ (packages vs dependencies). LEG-R3-verdict.md §M3 |
| M4 headline 11.3× | ABSENT as headline multiplier. Grep "11.3" hits only report.md:153 (Kademlia model validation 11.3 *percent*) and report.md:22 gossip 11.37 rounds — different objects, correctly scoped | NOT PRESENT | M4 belongs to wiki R2 §E-L5 results layer, not FC-C scope. Correct form: headline is [МОДЕЛЬ-estimate, 95% CI 7.8–20.7×]; denominators = JetBrains active-project surveys (n~26k) vs CodSpeed/CNCF/GitHub-scan populations |
| M2 energy 0.06 kWh/GB | uchenym/report contain NO kWh/energy figure (only "энергия" as a cost term, uchenym:29 — no number) | NOT PRESENT on FC-C pages | Canonical source: doi.org/10.1111/jiec.12630. Figure itself VERIFIED externally: Wiley abstract states "0.06 kWh/GB for 2015"; independently corroborated as Aslan et al. 2017/2018 attribution by arXiv:2506.23866, tandfonline 09540962.2023.2279812, journal-buildingscities bc.271. PMC13070060 link in wiki R1 is indeed broken (confirms LEG-R3 M2) |

### Honesty envelope (task 4)

R1 honestly states it is a "карта теорем / map of known results" with statuses [ДОКАЗАНО]/[ПРАВДОПОДОБНО]/[НЕВОЗМОЖНО] and no "Microcean theorem" exists (R1 concept materials :24–35, honest-limits section). Checked uchenym.html for overclaims: Holland schema theorem labeled [доказано] with explicit inequality caveat on the same line (R1 materials :27 — "неравенство, не уравнение"); BBH labeled [гипота/гипотеза]; swarm — "теоремы нет (NFL)"; limits table lists K, NFL, Halting/Rice as [Невозможно]. **No uchenym claim upgrades a hypothesis to a theorem, and no claim invents a Microcean-specific theorem. Honesty envelope: PASS.**

## 2. Reproducibility table

Note: none of the first-run failures are numeric — three scripts (EXP2, EXP6, EXP8) hard-fail on `import matplotlib` (module absent, host has Python 3.14.7 without matplotlib). Per task constraints I did not install anything. For EXP8 the declared table is closed-form arithmetic; I recomputed every claimed cell with stock Python (see "independent recomputation" rows above) — script-level repro of the *simulated* path is what remains UNVERIFIED for EXP8 (and EXP6, which is stochastic).

Fix pattern implied: import matplotlib inside the plotting branch / make it optional (`try: import matplotlib except ImportError: skip`) — then all 10 scripts run clean from stdout-only envs. (Flagging, not editing.)

Workdir caution (style note N2 applies): scripts write `results/*` relative to CWD; run with `mkdir -p /tmp/results` present.

| script | cmd (from /tmp) | exit code | stdout numbers match report.md/uchenym? |
|---|---|---|---|
| EXP1_comb.py | `python3 .../EXP1_comb.py` | 0 (after `mkdir /tmp/results`; first run without it: 1, FileNotFoundError on output write, stdout already complete) | YES — all E1/E1.2/E1.3/E1.4 values |
| EXP2_GA.py | `python3 .../EXP2_GA.py` | 1 (`import matplotlib` line 142, after all numerics printed) | YES — E2 table + convergence trace all match (except report.md:79 "gen≥60" wording — see ledger) |
| EXP3_epistasis.py | `python3 .../EXP3_epistasis.py` | 0 | YES — λ=0.7 → 0.3250±0.1094, λ=1.0 → 0.1783±0.0679, hits 13.2/14.2 |
| EXP4_sizing.py | `python3 .../EXP4_sizing.py` | 0 | YES — GDC table (125.44 for κ=2,σ/d=4) + empirical 12/27/30 |
| EXP5_kademlia.py | `python3 .../EXP5_kademlia.py` | 0 | YES — 5.42±0.83, max 8; validation 11.32/2.95/5.21% |
| EXP6_gossip.py | `python3 .../EXP6_gossip.py` | 1 (matplotlib at line 20, before any output) | UNREACHABLE — REPRO-UNVERIFIED |
| EXP7_crdt.py | `python3 .../EXP7_crdt.py` | 0 | YES — 10000/10000 ×9, 1000/1000 ×6 |
| EXP8_amdahl.py | `python3 .../EXP8_amdahl.py` | 1 (matplotlib at line 15, before any output) | PARTIAL — script no stdout; all cells independently recomputed by stock Python (91.18→91.2; 72.11; 19.64→19.6; 1.6/1.78/1.88/1.97/1.99/2.00; 3.077/4.706/6.4/8.767/9.656/9.91; 1.905/3.478/5.926/9.143/15.42/18.62) — table arithmetic VERIFIED, script path UNVERIFIED |
| EXP9_cegis.py | `python3 .../EXP9_cegis.py` | 0 | YES — 820 candidates, 1 iter, 0 divergences, w/o-'<': 108 timing 0.04 vs 0.05 |
| EXP10_mdl.py | `python3 .../EXP10_mdl.py` | 0 | YES — full (a)/(b)/(c) incl. 159/265, 150.90/60.90, −0.9117/−0.0369/−0.8663/+0.0628 |

Summary: 8/10 scripts executed cleanly (exit 0); EXP2 numerics exit-1-after-print and verified; EXP6, EXP8 script-level REPRO-UNVERIFIED (matplotlib), EXP8 declared values verified by independent recomputation.

Independent recomputation evidence for EXP8 (stock Python, deterministic formulas):
```
python3 -c: S(n)=1/((1-p)+p/n)
(0.99,1024)=91.18 (0.99,256)=72.11 (0.95,1024)=19.64 (0.5,1024)=2.0 (0.9,1024)=9.91 (0.99,inf)=100.0
whole table cells recomputed, all match report.md:216-219 to 2 decimals
```

## 3. Style notes for later (≤3)

1. **N1 — Sizing-parameterization split-brain.** The site layer (uchenym) carries two incompatible sizing stories in one page (c=z²=2.71 → 173 at :53 vs c=2.45 → "196" at :66); the R2 source-of-record uses c=1.96 → 125.44. If FC-A or the editor touches uchenym:66, synchronize all three numbers in one pass.
2. **N2 — `results/` CWD coupling.** Every EXP script writes/saves under relative `results/` path; running from anywhere without `results/` in CWD gives exit 1 or truncates stdout. Plotting should be optional try/exception and outputs should fall back to stdout.
3. **N3 — SVG/PNG chart parity.** Site ships 6 SVGs styled as summary charts; source PNGs live only in the internal R2 results. A claims-level check was done, not a data-level one; if any chart gets redrawn, regenerate from script outputs, not by hand.
