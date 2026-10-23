# FC-D — cross-audit: site-wide technical integrity, positioning, wiki M1–M4, legal sweep

Agent: FC-D (cross-auditor). Site state: commit `442a19f`, plus working ledgers A/B/C (not committed). Read-only everywhere except this file + one REPORT.md append line.
Rule base: concept wiki notes (86-131 resource principles ВЕКТОР/НАБРОСОК; 518-594 status/novelty/format spec) + canonical publication text + LEG spread (internal legal-risk documents) + LEG-R3 verdict (internal review verdict).
Duplication policy: rows already in FC-A/FC-B/FC-C are referenced, not restated; only cross-page blind spots are ledgered here.

## D1 — Site-wide technical integrity

Checked: all href/src/#anchor targets across 5 HTML files, CSS `url()`, `research/report.md` internal links, chart references. Python checker at `/tmp/opencode/fc_d_linkcheck.py` (escaped `fn` syntax fixed, rerun OK).

| loc | issue | verdict | proposed fix | evidence |
|---|---|---|---|---|
| all 5 pages | broken href/src/page-targets/cross-page #anchors/in-page #anchors | PASS — 0 broken | none | checker output: 0 BROKEN-TARGET/BROKEN-ANCHOR lines |
| all 5 pages | missing-alt `<img>`, missing `lang`, missing viewport/description | PASS — none found | none | checker: zero A11Y/SEO-A11Y hits for these classes |
| all 5 pages | favicon, canonical, og:title, twitter:card missing | IMPRECISE (SEO surface) | add `<link rel="icon">`, `<link rel="canonical">`, `og:title/og:description/og:locale=ru_RU`, `twitter:card=summary_large_image` to each page head | checker: 4 MISSING × 5 files |
| 5 pages + root + `research/` | README.md absent at site root (visitors/JSON readers see nothing indexable beyond HTML); `robots.txt`, `sitemap.xml` absent | IMPRECISE | add root README.md (project one-pager + DOI when issued — LEGAL-RISK-REPORT checklist item), robots.txt (allow all), sitemap.xml (5 URLs) | `find` over repo: no robots.txt/sitemap.xml/root README |
| index.html:118, vsem — level links | link targets `ru/vsem.html#kak`, `#security`, `#scenarios`, `specialistam#architecture`, `uchenym#model`, `#trust` | PASS — all anchors exist | none | checker cross-file anchor resolution |
| charts | 6 SVGs (`assets/charts/{ga,epistasis,kademlia,gossip,amdahl,mdl}.svg`) all referenced exactly once (uchenym.html:58,63,90,94,98,122); no root *.svg to orphan; report.md md-links resolve (git-relative `results/` refs are source-of-record in wiki, not site paths) | PASS | none (parity caveat = FC-C N3, not duplicated) | per-SVG ref count = 1 each; md-link scan 0 broken |
| `research/report.md:6`, `:334` | declared Python 3.13.14 / numpy 2.4.3 (matplotlib 3.11.1) vs fact-check env Python 3.14.7 / numpy 2.5.2 (matplotlib absent, host) | VERIFIED-DRIFT — declared env does not match current reality; all reproduced numbers still match (FC-C) | add one line to report.md: "numbers reproduce also on 3.14.7 + numpy 2.5.2 (check 2026-10-22, EXP6/EXP8 pending matplotlib install)" or rerun + re-baseline the declared environment | FC-C repro table; site grep: only 2 version lines exist, none on HTML pages |

D1 totals: **0 broken/outdated link targets; 20 SEO-surface gaps (4 classes × 5 pages); 3 infrastructure files missing (README/robots/sitemap); 1 version-drift pair (report.md:6,334).**

## D2 — Cross-page positioning consistency vs concept envelope

Envelope: resource principles are ВЕКТОР/НАБРОСОК (draft), honest-limits section outlaws "Microcean theorem"/solved-cause claims, publication = paradigm proposal/public interest, author = not operator/beneficiary/developer.

| loc | issue | verdict | proposed fix | evidence |
|---|---|---|---|---|
| index.html:188 | «…на все эти вопросы архитектура уже отвечает: закрытые контуры дают организациям **полную конфиденциальность**, открытые механизмы — прозрачность…а всеобщее достояние исключает и монополию, и присвоение» — draft design principles presented as implemented guarantees ("уже отвечает", "дают", "исключает") | OVERSHOOT | «призваны давать… (это проектный принцип, статуса наброска)»: e.g. «архитектура предусматривает ответы: закрытые контуры (лагуны) — проект приватности со статусом наброска; прозрачность — цель; всеобщее достояние — декларируемая лицензионная установка (см. D4)» | CON:86-131 ВЕКТОР/НАБРОСОК; task brief "полная confidentiality guaranteed by lagoons" example; FC-A flagged index:113 (same principle class) but NOT this sentence |
| index.html:202 | «Мы приглашаем всех участников… не в борьбу со старым, а в **современное строительство** нового» — call-to-action framing; page's own :204-205 limits «единственный призыв — к созиданию: изучать, обсуждать…» — «строительство» goes beyond the disclaimer | OVERSHOOT (minor) | «Мы приглашаем представителей цифрового мира — оценить, обсуждать и критиковать концепцию — не в борьбу со старым, а в осознание нового» | publication spec (CON:594): «show prospects…without propagandistic pathos»; filosofiya:117-121 explicitly disclaims program-of-action — cross-page consistency demands index read the same way |
| ru/filosofiya.html:43 | «Microcean **устраняет причину**, а не симптом: базовой единицей…**становится** фрагмент» — present-tense causal claim about a nonexistent system; mirrors task example «устраняет причину» | OVERSHOOT | «Microcean призван устранить причину, а не симптом: если парадигма приживётся, базовой единицей повторного использования станет фрагмент…» | CON:110-114: author's *direction* «глобальная оптимизация кода…», draft status; CON:94-99 items are "В Microcean:" requirements, not facts. FC-B flagged spec:95 (related, different page) and FC-A flagged index:143 — neither covered filosofiya:43 |
| ru/vsem.html:112 | footer «концепция опубликована как всеобщее достояние · 2026» | IMPRECISE | same fix as B proposed for spec:118/fil:117, applied uniformly to all 5 footers: «MICROCEAN · концепция публикуется открыто · заявлено как всеобщее достояние (CC0) · 2026» | FC-B flagged 2 of 5 footers, FC-A 1 of 5; cross-page blind spot = remaining footers must change in the same edit batch |
| ru/uchenym.html:158 | same footer | IMPRECISE | same as above | FC-C honest-envelope PASS did not cover footer wording |
| ru/filosofiya.html:61 | «Это **снимает** главное возражение критиков … конфиденциальность встроена в саму модель мира» — design response stated as an accomplished resolution | OVERSHOOT (light) | «Это конструктивный проектный ответ на главное возражение критиков: конфиденциальность предусмотрена в самой модели мира (лагуны — принцип, реализация за будущими операторами)» | CON:505-510 pub: «система обязана работать в двух режимах» — a design obligation, not a shipped property |
| index:174-175 / vsem:76-79 / filosofiya:57-60 | lagoon promise wording «…из которой ничего не утекает наружу» on 3 pages | PASS — consistent across pages, faithful to CON:133-139 design text | none (but strings change together with D2 index:188 fix to keep tense) | diff of 3 phrasings; CON:133-139 |
| all 5 pages | no promises of services, donations, tokens anywhere (grep токен/донат/пожертв/вклад — only `токенизаторы` spec:61, false positive; «вложенные годы» = users' products, not author fundraising) | PASS | none | rg over 5 pages; author position 2026-08-24 (LEGAL-RISK-REPORT.md:7: author is private, no infrastructure/legal entity) |
| — | author-position sentence present where needed: filosofiya:89 «Автор публикует идею и не управляет никакой инфраструктурой» (FC-B VERIFIED) | PASS | none | LEGAL-RISK-REPORT.md:7,245-246 checklist wants this status statement on first page/preampule — only filosofiya carries it today (see D4 row) |

D2 net: **5 overshoot rows + 2 footer uniformity rows + 3 PASS bookkeeping rows.** Combined with A/B/C ledgers, after fixes the envelope holds.

## D3 — Wiki-side M1–M4 fix localization (proposed diffs only; wiki out of edit scope today)

Duplicated file instances: LEG-R1 (three internal copies — all must be patched in lockstep); LEG-R2 (two internal copies); LEG-W (already carries some fixes).

**M1 — truncated Stepsize URL behind $85B claim** (3 copies: `LEG-R1-global-optimization.md:41`)
- current: `- Stepsize blog (2021) — расчёт $85B — https://stepsize.com/blog/...`
- finding: the $85B figure is Stripe's Developer Coefficient (2018) primary; Stepsize is a secondary interpreter. Both model-figures; R1 already tags [МОДЕЛЬ].
- proposed replacement (keep RU doc language):
  `- Stripe, The Developer Coefficient (2018) — первичный источник $85B: https://stripe.com/files/reports/the-developer-coefficient.pdf ; Stepsize как вторичный пересказ методологии: https://stepsize.com/blog/cost-of-technical-debt (доступ 2026-10-22)`
- evidence: LEG-R3-verdict.md:163-166; live searxng 2026-10-22: stripe.com/files/reports/the-developer-coefficient.pdf "$85 billion annually"; stepsize.com/blog/cost-of-technical-debt (2020-11, Stripe $3T framing).

**M2 — broken PMC id where DOI 10.1111/jiec.12630 belongs; 0.06 kWh/GB chain** (3 copies: `LEG-R1-global-optimization.md:131` and `:491`)
- current: `- Aslan et al. (2017) *Electricity Intensity of Internet Data Transmission* — PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC13070060` (and in lists at :491)
- proposed replacement (both lines):
  `- Aslan et al. (2017) *Electricity Intensity of Internet Data Transmission* — DOI (канонический): https://doi.org/10.1111/jiec.12630`
- status: LEG-W already fixed (final-section copy :256 carries DOI "исправлено per LEG-R3 M2"); R2 use-site chain `LEG-R1:125-127` («Best estimate 2015 [ИЗМЕРЕНО-литература]»; «0.01–0.06») stays as-is — figure itself external-verified (FC-C: Wiley abstract "0.06 kWh/GB for 2015", + arXiv:2506.23866 attribution).
- evidence: LEG-R3-verdict.md:168-171.

**M3 — 50.5% (packages) vs 50.6% (dependencies) denominators**
- source-of-correct-split: `LEG-R1-global-optimization.md:143` «**50.5% пакетов**…; **50.6% из 50 488 зависимостей**…» — keep.
- `LEG-R2-global-optimization-calcs.md:65` (internal doc, 2 copies) current: `DepPrune (Jiang et al., ICSE 2023): **50.6% npm-пакетов содержат ≥1 bloated dependency**, из них 51.3% — неиспользуемые прямые зависимости.`
  replacement: `DepPrune (Jiang et al., ICSE 2023): **50.5% npm-пакетов содержат ≥1 bloated dependency**; из 50 488 проанализированных зависимостей **50.6%** — bloated (13.8% прямых, 51.3% транзитивных).`
- `LEG-R2…:34` current «**DepPrune 2023** (50.6% пакетов содержат bloated deps…)» → `(50.5% пакетов содержат ≥1 bloated dep; 50.6% зависимостей bloated)`
- `LEG-R2…:17` TL;DR cell «[ИЗМЕРЕНО литература npm 50.6% bloated]» → `[ИЗМЕРЕНО литература npm: 50.5% пакетов / 50.6% зависимостей bloated]`
- `LEG-R2…:297` assumptions row «npm bloated | **50.6% пакетов**» → `npm bloated | 50.5% пакетов; 50.6% зависимостей`
- code: internal experiment script `e_l1_bloat.py:174` + internal summary report key `depprune_2023_any_bloated_pct: 50.6` → rename/split into `depprune_2023_packages_pct: 50.5`, `depprune_2023_dependencies_pct: 50.6` (script comment :171 similar).
- evidence: LEG-R3-verdict.md:173-176; key clarification LEG-R3-verdict.md:205.

**M4 — 11.3× headline needs [МОДЕЛЬ-оценка, 95% CI 7.8–20.7×] + denominator disclaimer**
- `LEG-R2-global-optimization-calcs.md:271` headline current: `Лишь **5.5%** проектов гоняют perf-регрессию против **~62%** с unit-тестами — разрыв **11×**… [ИЗМЕРЕНО опросы + скан, 95% CI 2–10%]`
  replacement: `Лишь **5.5%** проектов с CI гоняют perf-регрессию против **~62%** с unit-тестами (опросы активных dev-проектов: JetBrains n~26k) — разрыв **11× [МОДЕЛЬ-оценка, 95% CI 7.8–20.7×]**; знаменатели смешивают JetBrains-опрос (активные dev-проекты, n~26k) и CodSpeed/CNCF/GitHub-scan (все публичные repo) — популяции неоднородны [ИЗМЕРЕНО опросы + скан, perf 95% CI 3–8%]`
- `LEG-R2…:268` summary-table row `«Разрыв | 56.5 п.п., 11.3×» (7.8–20.7×)` → append «; среди активных кодовых проектов, по опросам; [МОДЕЛЬ-оценка]» (перцентиль-интервал already present).
- `LEG-R2…:17` TL;DR E-L5 cell «→ разрыв 11.3× (диапазон 7.8–20.7×)… [ИЗМЕРЕНО опросы+скан]» → `… [МОДЕЛЬ-оценка, 95% CI 7.8–20.7×; среди активных проектов]`
- `LEG-W-final-section.md:183` already carries 95% CI; `:334` current `→ **gap 11.3×** (95% CI 7.8–20.7×) [ИЗМЕРЕНО]` → `[МОДЕЛЬ-оценка, 95% CI 7.8–20.7×]` (tag downgraded per R3 M4).
- evidence: LEG-R3-verdict.md:177-181; точный CI 11.27× (95% CI 7.75–20.67×) LEG-R3-verdict.md:203-204.

D3 totals: **M1 ×3 file:line, M2 ×2 file:line (×3 copies), M3 ×5 file:line (+2 code), M4 ×4 file:line. All four findings confirmed present in wiki/LEG layer; zero of them leak onto site pages (matches FC-B/FC-C absence checks).**

## D4 — Legal/public-domain consistency sweep (per internal legal-risk verdict)

| loc | issue | verdict | proposed fix | evidence |
|---|---|---|---|---|
| index.html:187 | «Концепция публикуется как всеобщее достояние: **зафиксирована публично с датой первопроходца**, чтобы никто — включая автора — не смог оградить её патентами» (FC-A flagged; D4 adds the legally exact repair per LEGAL verdicts) | IMPRECISE | proposed wording: «Концепция предана гласной фиксации (defensive publication) с датой релиза; в объеме раскрытого здесь это создаёт publicly available prior art (MPEP §901, ст.54 EPC, ст.1358 ГК РФ). Декларируется CC0 1.0 Universal как лицензионная установка; неотчуждаемое право авторства (ст.1265, 1267 ГК РФ) сохраняется за автором. Надёжность prior art требует тройного датирования (Zenodo DOI + OpenTimestamps + нотариально) — см. чек-лист LEG» | LEGAL-RISK-REPORT.md:102-135 (defensive publication mechanics), :126-127 (псевдоним сохраняет силу prior art), :240-242 CC0 checklist; ст.1265 (псевдоним/неотчуждаемость) |
| index.html:188 | «всеобщее достояние исключает и монополию, и присвоение» | IMPRECISE (legal) | «всеобщее достояние» (декларация + prior art) не может исключать патентную монополию на *нераскрытые* детали и не блокирует чужие товарные знаки; replace with «всеобщее достояние — открытая, а не монопольная установка: автор не претендует на ограничение других…» — avoid legal guarantee | MPEP §901 / ст.54 EPC novelty logic (blocks only disclosed subject matter); FC-B found live registered MICROCEAN® (Jaubert 1979) — trademark exclusion exists regardless |
| ru/filosofiya.html:72 | FAQ «а всеобщее достояние исключает монополию — включая монополию автора концепции» | IMPRECISE (legal) | «а открытая публикация и декларация CC0 исключают монополию автора на раскрытые элементы» — same scope caveat; FAQ wording acceptable if «исключает»→«исключает авторскую монополию на раскрытое» | same; plus author non-possession of assets (no monopoly possible factually — cf. filosofiya:89) |
| index.html:187 «с датой первопроходца» | vague dating claim; LEG checklist requires Zenodo DOI + OTS + notary triple-anchor; site shows no DOI/OTS anchor | IMPRECISE | either add DOI string once obtained (`doi:10.5281/zenodo.XXX…`) or soften: «публикация создана 2026-08-11 (см. полную публикацию); надёжное датирование (DOI/OTS) — в подготовке» | LEGAL-RISK-REPORT.md:113-122 (достоверное датирование tools), :245-247 checklist |
| filosofiya.html:81 | «публичная фиксация означает, что никто … не сможет оградить идею патентами» (FC-B VERIFIED + nuance suggested) | VERIFIED-WITH-CAVEAT | B's nuance made legally exact: «в пределах того, что реально раскрыто (enabling disclosure) и при доказуемой дате/accessibility» | LEGAL-RISK-REPORT.md:102-108 |
| ru/vsem.html:112, ru/uchenym.html:158 | footers (uniform with D2 fix) | IMPRECISE | same CC0-declaration wording as D2 footer rows | FC-A:187/208, FC-B:117/118 partially covered; these two pages unflagged before |
| all 5 pages | author-status statement «не оператор, не бенефициар, не учредитель юридического лица» present only on filosofiya:89 | IMPRECISE (surface placement) | per LEG checklist item «в преамбуле» — duplicate one-line author status into index.html §8 «Философия и правовое положение» | LEGAL-RISK-REPORT.md:245-246 |
| all 5 pages | services/donations/tokens promises | PASS — none | none | grep sweep; author position 2026-08-24 honored |

D4 net: **6 rows needing legally-exact wording, 3 PASS rows.** No page claims legal formalities (registration, DOI, license filing) that do not exist anywhere — the risk is uniform *perfective* tense («опубликована», «исключает», «не сможет оградить») where declaration/proposal tense is accurate.

## Totals

- D1: 0 broken links; 20 SEO gaps; 3 missing infra files; 1 version-drift note.
- D2: 5 overshoots + 2 footer uniformity edits; 3 PASS confirmations.
- D3: 14 wiki/LEG file:line localizations ready as copy-paste diffs (P2 code changes optional).
- D4: 6 legal wordings + 3 PASS confirmations.
- Author-position safeguards (no services/donations/tokens) — PASS everywhere; author status line should be added to index per LEG checklist.
