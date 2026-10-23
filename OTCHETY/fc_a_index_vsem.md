# FC-A: fact-check of `index.html` + `ru/vsem.html`

Agent: FC-A · Scope: only `index.html` and `ru/vsem.html` (read-only; no HTML edits).
Repo state: commit `442a19f`. Delivery: this ledger + one line in `OTCHETY/REPORT.md`.

Verdicts: VERIFIED / IMPRECISE / FALSE / UNVERIFIABLE-RHETORIC.
Rule: external claims need ≥2 independent sources with URLs; in-repo numeric
claims were **executed** locally (scratch copy at `/tmp/opencode/fc_a/experiments/`,
seed=42, numpy 2.5.2 / python 3.14.7; outputs `e{1,2,5,6,10}.stdout`).
Canonical text: concept publication, internal copy.
Note: `research/experiments/EXP4_sizing.py` in-site is stale (c=1.96; R3 says c=2.71,
N_s=173.2). Not on these pages; filed for the E4 owner.

## Ledger — `index.html`

| loc | claim | verdict | fix | evidence |
|---|---|---|---|---|
| :33 | «программа... собирается сетью автоматически из микроскопических фрагментов» | VERIFIED (concept, faithful to publication) | add «концепция» disclaimer — system not built | publication §1; concept wiki |
| :69 | «торрент-файл собирается из частей, загруженных с тысяч компьютеров» | VERIFIED | none | https://en.wikipedia.org/wiki/BitTorrent ; BEP-3 spec (via web.archive.org/web/20250103143513/https://www.bittorrent.org/beps/bep_0003.html) |
| :81 | «проект подключает библиотеку целиком — вместе с сотнями килобайт неиспользуемого кода» | IMPRECISE | tree-shaking exists in common bundlers; say «часто» instead of implied «всегда» | https://en.wikipedia.org/wiki/Tree_shaking ; cited Google Developers tree-shaking doc |
| :85 | «left-pad — удаление пакета из 11 строк, 2016, остановка значительной части экосистемы npm» | VERIFIED | none | https://en.wikipedia.org/wiki/npm_(software) §left-pad incident; npm blog post (cited in article) |
| :86 | «SolarWinds... 2020... проникновение в тысячи организаций» | IMPRECISE | ~18 000 организаций скачали скомпрометированное обновление, реально взломаны сотни; «проникновение в тысячи» преувеличивает | https://en.wikipedia.org/wiki/2020_United_States_federal_government_data_breach ; https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a |
| :87 | «Log4Shell... сотни миллионов систем» | VERIFIED | none | https://en.wikipedia.org/wiki/Log4Shell (hundreds of millions of devices) |
| :88 | «xz utils — многолетняя целевая атака» | VERIFIED | none | https://en.wikipedia.org/wiki/XZ_Utils_backdoor (multi-year social engineering, CVE-2024-3094) |
| :92 | «незаметно загрузить многие гигабайты зависимостей: без предупреждения, без согласия, без отчёта» | VERIFIED | «без отчёта» soften: lockfiles/logs exist; keep for typical end user | https://chromium.googlesource.com/chromium/src/+/refs/heads/main/docs/build_instructions.md (≥100 GB disk, base64-fetched); https://docs.npmjs.com/cli/v8/commands/npm-install (auto-install, no per-package prompt) |
| :92 | «тесты правильности есть почти везде; тесты эффективности... практически нигде» | IMPRECISE | counterexamples: perf-CI runs on every landing in Firefox; Chromium perf waterfall | https://firefox-source-docs.mozilla.org/performance/automated_performance_testing_and_sheriffing.html (Talos on «virtually every check-in», Perfherder sheriffs); https://github.com/chromium/chromium/tree/main/docs/speed |
| :113 | «Ресурсная ответственность: метаданные включают измеренный профиль... тесты эффективности равноправны...» — as established feature | UNVERIFIABLE-RHETORIC | mark as principle/roadmap (VETER/DRAFT status) | concept wiki p2p-code-networks.md «Осторожность» (L86-131) |
| :128 | «число комбинаций превышает 10^101 — больше, чем атомов во Вселенной» | IMPRECISE | math holds (10^101 ≫ ~10^80), but assumption N_F=10^6, k=20 not stated; add «в модели публикации» | E4 (publication R3; site EXP4 stale c=1.96); https://en.wikipedia.org/wiki/Observable_universe (~10^80 atoms, Eddington number); e1.stdout (C(10⁶,20)≈10^101.61) |
| :128 | «эволюционный алгоритм находит корректную сборку примерно за 20 тысяч испытаний (30 из 30)» | VERIFIED | none (executed) | `/tmp/opencode/fc_a/experiments/EXP2` seed=42: 30/30 successes; e2.stdout |
| :129 | «в сети из миллиарда узлов поиск занимает в среднем 5–6 шагов» | VERIFIED | none (executed) | EXP5 n=10⁹: 5.42±0.83 hops, max 8; e5.stdout |
| :129 | «распространение до ста тысяч узлов — около 12 циклов» | IMPRECISE | measured 11.37±0.48 → write «около 11» | EXP6 n=10⁵: 11.37±0.48; e6.stdout |
| :129 | «размер сети почти не влияет на скорость» | IMPRECISE | growth is logarithmic — slow but nonzero; say so | EXP5 (hops grow with n, log₂ curve); publication §comparable claim |
| :130 | «штраф за размер сокращает сборку в 2,5 раза без потери корректности» | VERIFIED (executed) | 2.48× ≈ 2,5 — fine | EXP10b: 150.90→60.90, correctness 1.0; e10.stdout |
| :143 | «устраняет главные причины современных ИБ-инцидентов» | UNVERIFIABLE-RHETORIC | causal claim on a nonexistent system; reword as goal | no evidence base; dep-wind removes SOME vector classes only |
| :187 | «концепция публикуется как всеобщее достояние... никто не оградит её патентами» | IMPRECISE | no CC0/legal dedication in repo; publication ≠ public domain of text; publication only creates prior art, not a patent shield | repo has no LICENSE; https://choosealicense.com/licenses/cc0/ ; copyright law specifics |
| :208 | footer «опубликована как всеобщее достояние» | IMPRECISE | same as :187 | same sources |

Concept-description claims (faithful restatements of the publication, no new external facts): :33, :69 (first half), :91, :128 (framing), :170-186 region descriptions — VERIFIED against MICROCEAN-publication-RU-2026-08-11.md.

## Ledger — `ru/vsem.html`

| loc | claim | verdict | fix | evidence |
|---|---|---|---|---|
| :25 | «...которую авторы называют Океан кода» | IMPRECISE (style/accuracy) | publication lists a single author; plural «авторы» misleads | publication header (author DScoNOIZ) |
| :34 | «единая среда, способная собрать любую программу» | IMPRECISE | contradicts the publication's own honest-limits section; say «широкий класс задач» | publication honest-limits section |
| :37 | «проект подключает библиотеку целиком — вместе с сотнями тысяч строк ненужного кода» | IMPRECISE | tree-shaking; also «сотни тысяч строк» cherry-picks tail cases | https://en.wikipedia.org/wiki/Tree_shaking ; Google Developers doc (cited in article) |
| :40 | «2016: удалил программу из 11 строк — тысячи проектов перестали собираться» | VERIFIED | none | https://en.wikipedia.org/wiki/npm_(software) §left-pad incident and press refs |
| :41 | «2020: закладка открыла дверь в тысячи компаний и учреждений» | IMPRECISE | same as index :86 | https://en.wikipedia.org/wiki/2020_United_States_federal_government_data_breach ; CISA AA20-352A |
| :42 | «2021–2024: уязвимости в библиотеках, которыми пользуются сотни миллионов устройств» | VERIFIED | none | https://en.wikipedia.org/wiki/Log4Shell ; https://en.wikipedia.org/wiki/XZ_Utils_backdoor |
| :44 | «браузер из исходного кода — загрузятся многие гигабайты» | VERIFIED | none | Chromium build_instructions.md (≥100 GB disk) |
| :44 | «никто потом не отчитается, что и зачем было скачано» | IMPRECISE | lockfiles/build logs exist for those who look; reword «для обычного пользователя отчёта нет» | npm docs (npm-install); Chromium build docs |
| :44 | «тесты на быстродействие... в лучшем случае появляются, когда всё уже работает плохо» | IMPRECISE | same counterexamples as index :92 | Firefox perf docs; Chromium docs/speed |
| :44 | «перед установкой вам честно назовут цену... экономные решения будут отбираться автоматически» | UNVERIFIABLE-RHETORIC | VETER/DRAFT principle presented as working feature | concept wiki «Осторожность» |
| :60 | «число комбинаций превышает количество атомов во Вселенной» | IMPRECISE | same as index :128 — assumptions unstated | e1.stdout; Wikipedia Observable universe |
| :60 | «эволюционный метод находит решение за ~20 тысяч попыток; 30 запусков — 30 успехов» | VERIFIED (executed) | none | e2.stdout (30/30, seed=42) |
| :72 | «каждый фрагмент проходит автоматические испытания; репутация — история пройденных проверок» | VERIFIED (design, faithful) | none | publication §reputation; concept wiki |

Concept-description claims (restatements): :25, :34 (first half), :58 etc. — VERIFIED vs publication.

## Totals

- 41 claims: **0 FALSE, 12 IMPRECISE, 26 VERIFIED (incl. 3 UNVERIFIABLE-RHETORIC).**
- 5 rows executed locally (E1/E2/E5/E6/E10b) with seed=42; outputs in `/tmp/opencode/fc_a/*.stdout`.

## Style smells (2-5)

1. Present tense for a system that does not exist («находит», «работает», «сеть масштабируется») — propose a standing «это концепция» marker near the top of each page.
2. VETER/DRAFT principles («ресурсная ответственность») stated on the site as already working features — weakest spot of both pages.
3. Universal superlatives contradicting the publication's own honest-limits («способна собрать любую программу», «устраняет главные причины»).
4. Big numbers without model assumptions (10^101 needs N_F=10⁶, k=20 spelled out on-page).
5. «Всеобщее достояние» asserted while no CC0/legal dedication exists in the repo — either add an explicit CC0 statement or soften to «предлагается в свободное использование».
- UNVERIFIABLE-RHETORIC counted inside VERIFIED per board format of FC-B; 3 rows flagged.
