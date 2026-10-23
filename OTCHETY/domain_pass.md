# DOMAIN-PASS — real-domain closure (242ff2d)

Domain: https://dsconoiz.github.io/microcean/ (GitHub Pages).

## Changes

- `sitemap.xml`: sentinel comment removed; 10 `<loc>` filled with absolute
  GitHub-Pages URLs (/, ru/*.html x4, en/*.html x5); `<lastmod>2026-10-22`
  per page group (latest commit date touching pages: 2026-10-22).
- `robots.txt`: sitemap line uncommented and filled (absolute URL).
- 10 HTML pages: `<link rel="canonical">` + `<meta property="og:url">`
  added with per-page absolute URLs (canonical absolute, depth-safe);
  `og:image` upgraded to absolute
  `https://dsconoiz.github.io/microcean/favicon.svg`.

## Verification

- `python3 /tmp/opencode/microcean_checker.py` (10 pages,
  href/src/anchors/parse/lang/og:locale/tokens): ERRORS 0, WARNINGS 0,
  exit 0. Absolute https URLs resolved as external (no FS check) — no
  canonical false-positives.
- Local grep invariants: canonical count 10/10 (one per page), each
  canonical == page's og:url, og:image absolute in 10/10, sitemap XML
  parses (xml.dom.minidom OK).
- Commit 242ff2d pushed to origin main (12 files, +61/-21).

## LIVE HTTP (poll 2026-10-23T01:4xZ, curl -w %{http_code})

```
200 /
200 /ru/vsem.html        200 /ru/specialistam.html
200 /ru/uchenym.html     200 /ru/filosofiya.html
200 /en/index.html       200 /en/for-everyone.html
200 /en/scientists.html  200 /en/specialists.html
200 /en/philosophy.html
200 /sitemap.xml         200 /robots.txt
```

Content spot-checks: / (6 MICROCEAN/<h1> matches), sitemap + robots 200.
Canonical tag not yet in served build at poll time — GitHub Pages
refresh in progress; pushed state defines the eventual live content.

## Residuals (open, operator scope)

- R2 — DOI/OTS long-term dating (unchanged).
- R3 — MICROCEAN TM-registry wider check (unchanged).
- EN mirror wiki note — wiki status flip (non-site, unchanged).
