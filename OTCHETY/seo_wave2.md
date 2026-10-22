# SEO wave2 — favicon, robots, sitemap, head meta (2026-10-22)

## Added (new files, repo root)

- `favicon.svg` — wave-of-dots glyph: 9 dots along one sine period
  (x=8..56, y=32−8·sin(2π(x−8)/48)), crest dots slightly larger. All colors
  from `assets/style.css` :root (bg `#0a1622` rounded card + accents
  `#38bdf8`, `#22d3ee`, `#2dd4bf` left→right). 13 lines, viewBox 0 0 64 64.
- `robots.txt` — `User-agent: *` / `Allow: /` + sitemap line in **blocked
  commented form** (see decision below).
- `sitemap.xml` — 5-URL template with `EMPTY-PENDING-DOMAIN` sentinel in every
  `<loc>` + leading XML comment `ORCHESTRATOR: fill domain before publish`.
  Parses as well-formed XML.
- `README.md` (EN) — concept blurb, pages map table, `research/` layout,
  `python3 -m http.server` preview, agent-reports pointer.

## Per-page head additions (5/5: index.html, ru/vsem.html, ru/specialistam.html, ru/uchenym.html, ru/filosofiya.html)

- `<link rel="icon" href="..." type="image/svg+xml">` — page-relative
  (`favicon.svg` at root depth, `../favicon.svg` for ru/*). Page-relative chosen
  over root-absolute so the local `http.server` link check passes and serving
  from a subpath keeps working.
- `og:type=website`, `og:title` (verbatim from each `<title>`),
  `og:description` (verbatim from each existing meta description), `og:site_name=MICROCEAN`, `og:locale=ru_RU`, `og:image` → same favicon path as
  `rel="icon"`, `twitter:card=summary`. No body content touched (verified:
  additions match exactly the 9 head lines; `rel="icon"`/`twitter:card` count = 1 per page).

## Decisions

- **Domain**: no production domain proposed anywhere in OTCHETY (fc_b:38
  mentions third-party `microcean.*` trademarks/projects only — that strengthens
  the case for not inventing one). fc_d D1 row (:16) asked for robots/sitemap/
  README without a domain.
- **Sitemap**: kept as the loudly-blocked template (sentinel `loc` values +
  orchestrator comment) rather than skipping it — zero fake URLs are committed
  silently, and the file is publish-ready after one find-replace. Skipping was
  the fallback if a template were judged unwise; the template wins because it
  makes the pending step *visible in the repo*, not just in a side report.
- **robots.txt sitemap line**: same constraint — written as a commented-out
  absolute-URL placeholder; crawlers parse the file fine (only `User-agent`/
  `Allow` are active).
- **Canonical**: omitted. A canonical href requires an absolute origin; any
  placeholder would be a fake URL in the canonical slot (stronger SEO signal
  than og:tags). Deferred to the domain-filling step (same orchestrator pass).
  No `meta robots index,follow` added — it is the crawler default and adds
  nothing.
- **og:image**: granted as favicon-only. Page-relative path works for local
  preview but is *not* resolved by most crawlers until an absolute URL exists;
  effective og:image needs the domain pass too (or a separate large/vector
  emblem — note for the orchestrator).

## Verification (checker: /tmp/opencode/microcean_seo_check.py)

- Ran after all edits `python3 /tmp/opencode/microcean_seo_check.py` →
  `sitemap.xml: XML parse OK`, `checked pages: 5`, `head problems: 0`,
  `broken links: 0`, exit 0.
- Checks per page: full HTMLParser feed; body-ish tags inside `<head>`;
  12-item head checklist (charset/viewport/title/description/favicon/og:type/
  og:title/og:description/og:site_name/og:locale ru_RU/og:image/twitter:card);
  favicon href resolves; all `<a href>` (incl. `#fragment`, cross-page
  anchors), `<link href>`, `<script src>`, `<img src>` resolve within repo;
  external http(s)/mailto/data skipped; `EMPTY-PENDING-DOMAIN` skipped as
  sentinel.

## Not touched

- Sibling agents' uncommitted prose fixes (working tree), `research/`,
  `OTCHETY/fc_*`, body content of the 5 pages. No commits, no adds.

## Orchestraction follow-ups (blocked on domain)

1. Fill domain in `sitemap.xml` (replace sentinel, drop comment) + uncomment
   robots.txt Sitemap line in one pass.
2. Add `<link rel="canonical">` ×5 + absolute `og:url`/`og:image` in same pass.
3. Any late footer wording mentioning domain stays consistent with (1).
