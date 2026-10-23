# OTCHETY — Shared Agent Report Board

Shared board for ALL agents of this MICROCEAN site session. Every agent commits
its first action as an entry in `REPORT.md` (chronological ledger) and may later
add detail files in this directory. Site prose (`*.html`, site CSS) is never
edited here without first recording intent in `REPORT.md`.

## Entry format (one line per action, append at the end of REPORT.md)

```
<ISO8601 UTC> | <agent-name> | <topic> | 1-line result | link to detail file
```

Link field: path to detail file in this directory, or `-` if none.

## Agent roster

| Agent | Assigned phase | Status (scope + result) |
|-------|----------------|------------------------|
| BOOTSTRAP | repo-init + board setup | DONE — git init -b main (442a19f), shared board created, first commit carries all site files + OTCHETY/ |
| FC-A | FACT-CHECK-A: index.html + ru/vsem.html | DONE — 41 claims: 0 false, 12 imprecise (15 rows, 3 cross-page dups), 26 verified incl. 3 rhetoric; ledger fc_a_index_vsem.md |
| FC-B | FACT-CHECK-B: specialistam + filosofiya | DONE — 30 claims: 0 false, 10 imprecise, 17 verified incl. 3 rhetoric; ledger fc_b_specialists_philosophy.md |
| FC-C | FACT-CHECK-C: uchenym + research/report.md + EXP1-10 repro | DONE — 48 ledger rows: 41 verified, 4 imprecise, 1 false (E4 GDC split-brain), 2 script-UNVERIFIED (EXP6/EXP8, matplotlib); repro 9/10 matched, 8/10 exit 0; ledger fc_c_scientists_research.md |
| FC-D | FACT-CHECK-D: cross-audit + wiki M1-M4 | DONE — 0 broken links, 20 SEO gaps, D2 5 overshoots + 2 footers, D4 6 legal wordings, 14 wiki localizations; ledger fc_d_crosscheck_wiki.md |
| F1 | FIXES: index + vsem | DONE — 20/20 ledger fix rows + 5 cross D2/D4 rows, links OK |
| F2 | FIXES: specialistam + filosofiya | DONE — 15/15 fix rows, links OK |
| F3 | FIXES: uchenym + report.md + numbers | DONE — 7 fix groups; post-fix EXP2/4/6/8 exit 0; E4 unified c=z^2=2.71, N_s=173 (documented deviation from 1.96/125.44 per newer publication fact-check) |
| SEO | SURFACE: favicon/robots/sitemap/head-meta | DONE — seo_wave2.md; head meta 5/5, links 0 broken; canonical + sitemap domain pending (sentinel EMPTY-PENDING-DOMAIN kept in repo) |
| WIKI | WIKI M1-M4 execution | DONE — 3 commits (bccf760, 687a0c4, 0de5002) + kanban copies (LEG-R1 x3, LEG-R2 x2, LEG-W, code/json key split, R2-REPORT addendum x2) |
| CONSOL | CONSOLIDATION: master fact-check ledger | DONE — FACTCHECK-LEDGER.md (119 claims audited; 34/35 fully resolved = 97%; 7 residuals; ledger cross-checked against all 4 fc files) |
| STYLE | STYLE wave3: typography/layout consistency | DONE — style_wave3.md; 5 pages within rails, fact-sweep clean, parse/anchor 0 issues (verified by GATES) |
| GATES | GATES: final quality gates | DONE — verdict ACCEPT; suite 0/0/0 (links/parse/tokens), EXP2/4/6/8/9/10 exit 0; fixes: uchenym footer (D2), R6 865.93; residuals R4/R6/R7 closed, R1 CLOSED (real-domain pass 242ff2d), R2/R3 open, R5 accepted as-is; commits 928369f + docs wave |
| DOMAIN-PASS | real-domain publishing pass | DONE — sitemap 10 absolute URLs w/ lastmod, canonical+og:url per page, og:image absolute, robots sitemap line; checker 0/0; live HTTP 200 x12; domain_pass.md; commit 242ff2d |
| ANONYMITY+FIXES | privacy sweep + live-critic round 1 | DONE — 10 CONFIDENTIAL hits removed/impersonalized (pages + research/report.md), LEGAL-IDENTITY (CC0/ст.1265/1267) kept; live-critic: minutes hedge, descriptions ≤160 x20, experiments links absolute, sitemap lastmod 2026-10-23; checker 0 issues, live verified; anonymity_audit.md; commits da74624, 3642dbf |
| CONTINUOUS | CONTINUOUS: regression watch | RUNNING |

## Current session phases

- BOOTSTRAP — init repo, create this board, first commit — **COMPLETE**
- FACT-CHECK-A..D — verify site claims against research/ — **COMPLETE** (ledgers fc_a..fc_d)
- FIXES — factual corrections after fact-check — **COMPLETE** (F1 20/20+5 cross, F2 15/15, F3 7 groups)
- SURFACE — SEO wave2 (favicon, robots, sitemap, head meta) — **COMPLETE** (canonical/domain filled by DOMAIN-PASS)
- WIKI — M1-M4 execution on wiki layer — **COMPLETE** (commits bccf760, 687a0c4, 0de5002)
- CONSOLIDATION — master accountability ledger — **COMPLETE** (OTCHETY/FACTCHECK-LEDGER.md)
- STYLE — typography/layout consistency pass — **COMPLETE** (style_wave3.md; GATES-verified)
- GATES — final quality gates before convergence — **COMPLETE** (verdict ACCEPT; FACTCHECK-LEDGER.md §6)
- DOMAIN-PASS — real-domain: sitemap + canonical + og:url/og:image — **COMPLETE** (OTCHETY/domain_pass.md)
- LIVE-CRITIC ROUND 1 — hedge minutes cell, description bounds, experiments link, sitemap lastmod — **COMPLETE/FIXED** (OTCHETY/anonymity_audit.md, commit 3642dbf)
- ANONYMITY — impersonal public voice sweep — **COMPLETE** (OTCHETY/anonymity_audit.md, commit da74624)
- CONTINUOUS — regression watch after convergence — RUNNING (wave4 EN mirror shipped + gated)

## Standing rules (mandatory for every future fact-check / content pass)

- impersonal-first: internal artifacts are never named on public pages
  (no author's own tooling, internal institutes, channels or artifact ids;
  replace with "рабочие материалы концепции" / "the concept's working
  materials"). "автор публикации" may appear only where legal identity is
  required (CC0, ст.1265/1267).
- every date attached to a dating/legal claim must be sourced (see
  date_audit.md:85).

## Outstanding improvements queue (post-convergence)

- DOI/OTS dating — reliable long-term dating of the disclosed elements (site pages
  currently state "DOI/OTS in preparation", no DOI identifier on site by design)
- TM-registry — wider trademark-check of the MICROCEAN name beyond the recorded
  MICROCEAN® (water purification, 1979) prior mark
- EN mirror wiki note — flip wikis/main/projects/microcean-site.md status
  in-progress → shipped (wiki commit 2e516bd registered the page)
