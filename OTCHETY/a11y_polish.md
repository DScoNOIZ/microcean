# A11y + polish sweep (2026-10-22, CONTINUOUS-IMPROVEMENT agent)

Scope: 5 pages (index.html, ru/*.html) + assets/style.css. Site RU, static, no build
system. Constraints honoured: zero text-content changes; style.css additive only
(+7 lines); no new files except this board entry; no commits.

## Findings

| loc | issue | fix | before → after |
|---|---|---|---|
| index.html:23 | h1 absent on all 5 pages (hierarchy starts at h2) | logo wrapped in `<h1 class="logo-h">` (text in place; `.logo` class keeps all styling: font-size 2.4rem, weight 800, gradient clip; global reset zeroes default h1 margins → visually identical) | 0×h1 → 1×h1 |
| ru/vsem:32, ru/specialistam:32, ru/uchenym:32, ru/filosofiya:32 | no h1 on content pages | first `<h2 class="section-title">` promoted to `<h1 class="section-title">` (class supplies color/size/weight/offset; tag-only change, text untouched) | 0×h1 → 1×h1, h1→h2→h3 strict |
| index.html:25 | `<nav class="main-nav">` without label | added `aria-label="Разделы страницы"` | — |
| ru/*.html:23 | breadcrumb `<div>` is the only page-level nav, no landmark | `<div class="breadcrumb">` → `<nav class="breadcrumb" aria-label="Цепочка навигации">` (`.breadcrumb` CSS is class-based; nav renders identically) | no nav landmark → nav landmark |
| all pages | no `<main>` landmark (content was bare `div.container`) | content wrapper `<div class="container">` → `<main class="container">` (opening + closing per page; 1:1, no text moved) | — |
| style.css (end) | no `:focus-visible` outline rule | added `:focus-visible { outline: 2px solid var(--accent2); outline-offset: 2px; }` | invisible focus → 2px cyan-cyan outline |
| style.css (end) | transitions + index JS reveal animation unconditioned | added `@media (prefers-reduced-motion: reduce)` guard (5 lines) — kills transitions/animations, forces revealed sections visible (overrides inline JS state via `!important`), disables `.card:hover` lift | — |

Not done (deliberate):
- Skip-link: skipped (`only if trivially safe`/prefer-skip clause; nav is 8 links, adding one would inject visible/hidden text = extra content).
- `@media print` block: skipped per "prefer skip" (uncertain).
- Decorative-image audit: no inline SVGs on pages; favicon.svg is head-level. All 6 `<img>` charts in ru/uchenym.html already carry descriptive Russian alt attrs, and each is preceded by textual findings in the surrounding paragraphs — no change needed.
- Interactive elements: all are real `<a href>`; zero `onclick=`/`role=`/click-handler divs (grep ×5 pages → 0). No fix needed.

## Contrast math (WCAG 2.1 relative luminance, sRGB channel)

Variables from style.css `:root`. Backgrounds: `--bg #0a1622` (L=0.0115),
`--bg-card #10233a` (L=0.0165), `--bg-card-hover #16304d` (L=0.0242).
Colors: `--text #e3f0f8` (L=0.854), `--text-dim #8fb0c4` (L=0.409),
`--text-strong #cfe7f3` (L=0.769), `--accent1 #38bdf8` (L=0.440),
`--accent2 #22d3ee` (L=0.531), `--accent3 #2dd4bf` (L=0.514).
Ratio = (L_light+0.05)/(L_dark+0.05).

| pair | bg (blended) | ratio |
|---|---|---|
| --text on --bg | #0a1622 | **15.72:1** |
| --text on --bg-card | #10233a | **13.66:1** |
| --text-dim on --bg | #0a1622 | **7.97:1** |
| --text-dim on --bg-card (card p, footer?, table td) | #10233a | **6.93:1** |
| --text-dim on --bg-card-hover | #16304d | **5.87:1** (min of sweep) |
| --text-strong on --bg / card / hover | | 14.23 / 12.37 / 10.47:1 |
| --accent2 (code, tagline, links) | rgba(56,189,248,.12) over page-bg | **8.2:1** |
| --accent2 on th-bg rgba(56,189,248,.09) over card | | **7.4:1** |
| --accent1 / --accent3 on --bg | #0a1622 | 8.52 / 9.80:1 |

**Result: 0 failing pairs** (worst case 5.87:1 ≥ 4.5:1). No variable changed;
no before/after hexes to report.

## style.css diff summary (additive only, +7 lines at EOF)

```diff
+ :focus-visible { outline: 2px solid var(--accent2); outline-offset: 2px; }
+ @media (prefers-reduced-motion: reduce) {
+   * { transition: none !important; animation: none !important; }
+   section { opacity: 1 !important; transform: none !important; }
+   .card:hover { transform: none; }
+ }
```

(One combined edit block: line 1 + 5 lines of media block incl. braces = 7 lines total.)

## Checker output (standard suite, post-edit)

- `python3 /tmp/opencode/style3/check.py` → `[CHECK] 0 issues`; section
  inventory identical to pre-edit (index 11, specialistam 3, uchenym 10,
  filosofiya 9, vsem 7; each id exactly once). exit=0.
- `sweep.py compare` → token counts unchanged on every page (index 149,
  vsem 7, specialistam 26, filosofiya 15, uchenym 244→245); `TOTAL drops: 0`.
  Known pre-edit residue uchenym `'0': 3 -> 4` present before this sweep
  (from fix(truth), accepted at GATES) — untouched by it.
- `hedgecheck.py` → `OK` on all pages; `TOTAL drops: 0`.
- Footer floor: exact CC0 string «заявлено как всеобщее достояние (CC0)»
  present ×5 (all pages, grep count 1 each).
- Heading tags balanced per page after edits: h1 1/1, h2 and h3 open/close
  counts match on all 5 pages.

## Self-caught defect (fixed before final verification)

First version of the h2→h1 promotion replaced opening tags only and left
`</h2>` closings (mismatched tags). Caught by grep on `<h1` lines, fixed via
regex `(<h1 class="section-title">.*?)</h2>` → `</h1>` (count=1 per page),
asserted, then full suite re-run green (numbers above).
