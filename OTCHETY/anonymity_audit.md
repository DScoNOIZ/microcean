# ANONYMITY AUDIT — impersonal public voice (2026-10-23, agent ANONYMITY+FIXES)

Operator directive: the PUBLIC project is impersonal. The site must not disclose the
author's private infrastructure or internal systems. Allowed: "автор публикации" at
most (legal necessity: CC0, ст.1265/1267 authorship). Every internal-artifact mention
on public pages is CONFIDENTIAL and must be removed or impersonalized.

## Standing rule (added to fact-check checklist)

**impersonal-first: internal artifacts are never named on public pages.**
Any mention of the author's own tooling, internal institutes, internal channels,
internal artifact ids on public pages is a defect; classify CONFIDENTIAL →
replace with impersonal wording ("рабочие материалы концепции" /
"the concept's working materials").

## 1. Audit — full grep sweep (RU + EN patterns), classification

| # | Location | Hit | Class | Action |
|---|----------|-----|-------|--------|
| 1 | ru/specialistam.html:108 | «в собственных инструментах автора публикации (граф навыков для повторного использования кода)» | CONFIDENTIAL | replaced (operator wording) |
| 2 | en/specialists.html:108 | "in the publication author's own tooling (a graph of skills for reusing code)" | CONFIDENTIAL | replaced (EN mirror) |
| 3 | index.html:198 | «зафиксирована 2026-08-11 во внутренних материалах исследовательского института» | CONFIDENTIAL | → «в рабочих материалах концепции» |
| 4 | en/index.html:198 | "recorded internally on 2026-08-11" | CONFIDENTIAL | → "recorded on 2026-08-11 in the concept's working materials" |
| 5 | ru/filosofiya.html:91 | «во внутренних материалах исследовательского института» | CONFIDENTIAL | → «в рабочих материалах концепции» |
| 6 | en/philosophy.html:91 | "recorded internally on 2026-08-11" | CONFIDENTIAL | → "recorded on 2026-08-11 in the concept's working materials" |
| 7 | ru/uchenym.html:153 | «позиции 41–47 — внутренние артефакты Research Institute» | CONFIDENTIAL (sweep find, beyond fix list) | → «рабочие материалы концепции» |
| 8 | en/scientists.html:153 | "entries 41–47 are internal artifacts of the Research Institute" | CONFIDENTIAL (sweep find) | → "the concept's working materials" |
| 9 | research/report.md:4 | «Исполнитель: data_analyst (Research Institute, канал R1 → R2)» | CONFIDENTIAL (repo file is public) | → «data_analyst (рабочие материалы концепции)» |
| 10 | research/report.md:5 | «(R1, t_29de48c0)» internal artifact id | CONFIDENTIAL (sweep find) | → «(R1)» |
| L1 | index.html:198 "сохраняется за автором" / «Автор публикует идею и не управляет никакой инфраструктурой: не оператор, не бенефициар, не учредитель» (en mirror) | LEGAL-IDENTITY | kept (CC0 required; ст.1265/1267; D4/LEG-ratified author-status line) |
| L2 | ru/filosofiya.html:91 «ни корпорация, ни сам автор» | LEGAL-IDENTITY | kept |
| R1 | ru/vsem.html:88 / en/for-everyone.html:88 "internal programs ... lagoons" | RHETORIC | kept (hypothetical third-party case, impersonal) |

Historical board docs (OTCHETY/fc_*, FACTCHECK-LEDGER.md:157) still mention
"Research Institute" in **past entries** — left untouched per "never rewrite past
entries" (ledger integrity). No forbidden phrase remains in any site page or
`research/` (grep proves 0).

## 2. Before → after

| Fix | RU before | RU after | EN before | EN after |
|-----|-----------|----------|-----------|----------|
| Prototype para | «…но пока только в собственных инструментах автора публикации (граф навыков…). Оценка автора — грубая прикидка…» | «…так работает одна из практик повторного использования кода. Автоматизация — заявленная цель; сроки не обещаются.» | "…in the publication author's own tooling (a graph of skills…). The author's estimate is a rough guess…" | "…one of the established practices of code reuse. Automation is the stated goal; no timelines are promised." |
| Dating chain ×4 | «во внутренних материалах исследовательского института» / "recorded internally" | «в рабочих материалах концепции» / "in the concept's working materials" | ✓ | ✓ |
| Institute ×2 | «внутренние артефакты Research Institute» | «рабочие материалы концепции» | "internal artifacts of the Research Institute" | "the concept's working materials" |
| report.md | «(Research Institute, канал R1 → R2)», «(R1, t_29de48c0)» | «(рабочие материалы концепции)», «(R1)» | — | — |

Two-date chain + commit-history proof preserved: both 2026-08-11 and 2026-10-22
remain in all 4 chain sentences (index RU/EN, filosofiya RU/EN).

## 3. Live-critic round 1 (same task)

| Fix | Before → after |
|-----|----------------|
| (a) minutes cell | «Минуты: прототип собирается…» → «Минуты (проектная оценка): …» (index.html:184, en/index.html:184 "Minutes (design estimate): …") |
| (b) meta descriptions | index RU 202→145, en/index 202→130, en/philosophy 199→155, en/scientists 172→148 chars (`description` + `og:description` each); all 20 strings on 10 pages now ≤160 |
| (c) experiments link | ru/uchenym.html:153 + en/scientists.html:153 `../research/experiments/` (404 on Pages) → `https://github.com/DScoNOIZ/microcean/tree/main/research/experiments` (HTTP 200, anchor text unchanged) |
| (d) sitemap lastmod | all 10 URLs → 2026-10-23; 8 pages actually changed in commits da74624+3642dbf, ru/vsem + en/for-everyone unchanged today but their real last-change git date is already 2026-10-23 (kept real per directive) |
| (e) orphan hedge | «Оценка автора — грубая прикидка…» / "The author's estimate is a rough guess" consumed by the rewrite of fix 1 — no orphan left |

## 4. Verification (exact outputs)

- Checker (parse + href/src + anchors + protocol-relative + desc ≤160) over all 10 pages: `ISSUES 0`
- Char counts: all 20 description strings ≤160 (max 155; table above); `ALL<=160`
- Forbidden-phrase grep post-state over index.html, ru/, en/, research/, sitemap.xml, robots.txt, favicon.svg — patterns: собственных инструмент / граф навыков / skill graph / институт(institute) / Research Institute / внутренние артефакты/internal artifacts / own tooling / publication author / автора публикации / t_29de48c0 / recorded internally / inner-material phrasing → **0 hits**
- Date chain: grep "2026-08-11" + "2026-10-22" = 1 hit each in all 4 chain sentences, new impersonal wording confirmed by grep
- live after push (origin/main = 3642dbf):
  - index.html HTTP 200; contains «проектная оценка» ×1, «рабочих материалах концепции» ×1, «Навигация: материалы» ×2 (meta+og); «исследовательского института» ×0
  - en/philosophy.html HTTP 200; "concept's working materials" ×1, "internally" ×0
  - https://github.com/DScoNOIZ/microcean/tree/main/research/experiments → HTTP 200
  - ru/specialistam.html HTTP 200
- Commits: `da74624` (impersonal, 9 files) → `3642dbf` (live-critic, 6 files); pushed `6403e65..3642dbf main -> main`, origin/main == HEAD confirmed by `git rev-parse`.

## 5. Lesson

The public repo is the publication envelope: `research/` counts as a public page
surface, not just directory-protected OS specifics — the confidentiality sweep must
cover every file reachable from an HTTP 200 (report.md:4 leaked internal channel
naming although pages were already sanitized in the previous rounds).
