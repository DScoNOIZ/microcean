# DATE-AUDIT — internal fixation vs public disclosure

**Date:** 2026-10-23
**Scope:** `index.html`, `ru/*.html` (4), `en/*.html` (5), site metadata.
**Trigger:** operator-caught defect. Pages presented 2026-08-11 as the public
publication date. 2026-08-11 is the internal fixation date (the concept's working materials). Public disclosure began 2026-10-22 with
the public GitHub repository `https://github.com/DScoNOIZ/microcean`; its
commit history is the verifiable public evidence.

## Defect

Legal claims (prior art / public domain) must bind to the PUBLIC date. The
site conflated internal fixation with public disclosure, claiming a public
record dated 2026-08-11 that did not exist publicly until 2026-10-22.

## Audit — every date-bearing sentence

| Location | Text / claim | Class | Action |
|---|---|---|---|
| `index.html:198` | "гласная фиксация раскрытых элементов от 2026-08-11 создаёт общедоступный prior art" | (b) public/legal | fixed |
| `ru/filosofiya.html:91` | "публикация создана 2026-08-11" in defensive-prior-art paragraph | (b) public/legal | fixed |
| `en/index.html:198` | "a public record … dated 2026-08-11 creates publicly accessible prior art" | (b) public/legal | fixed |
| `en/philosophy.html:91` | "the publication was created 2026-08-11" | (b) public/legal | fixed |
| `index.html:219`, `ru/{vsem,specialistam,uchenym,filosofiya}.html` footers, `en/*` footers | "… · 2026" | (c) generic year | kept |
| `ru/uchenym.html:167`, `en/scientists.html:167` | "arXiv:2604.16477 (2026)" — citation year | (c) generic year | kept |
| `sitemap.xml` lastmod ×10 | `2026-10-22` | public date | correct, kept |
| `research/report.md:3,6,339,353` (off-page, repo artifact) | internal run dates 2026-08-11; independent reproduction 2026-10-22; fact-check 2026-08-24 | (a) internal history | kept as development history |

No JSON-LD, no `datePublished`/`dateModified`, no date in meta description/og.

## Before / after

**RU index (`index.html:198`)**

Before: "…гласная фиксация раскрытых элементов от 2026-08-11 создаёт
общедоступный prior art… а надёжное датирование (DOI/OTS) — в подготовке."

After: "…она зафиксирована 2026-08-11 во внутренних материалах
исследовательского института и публично раскрыта 2026-10-22 в открытом
репозитории GitHub — история коммитов служит проверяемым доказательством
даты, а раскрытые элементы образуют общедоступный prior art… а
дополнительное тройное датирование (DOI/OTS/нотариус) — в подготовке."

**RU philosophy (`ru/filosofiya.html:91`)**

Before: "Концепция публикуется открыто (публикация создана 2026-08-11;
надёжное тройное датирование — DOI, OpenTimestamps, нотариальное — в
подготовке) как defensive prior art…"

After: "Концепция публикуется открыто (зафиксирована 2026-08-11 во внутренних
материалах исследовательского института, публично раскрыта 2026-10-22 в
открытом репозитории GitHub — история коммитов служит проверяемым
доказательством даты; дополнительное тройное датирование — DOI,
OpenTimestamps, нотариальное — в подготовке) как defensive prior art…"

**EN index (`en/index.html:198`)**

Before: "a public record of the disclosed elements dated 2026-08-11 creates
publicly accessible prior art… while reliable dating (DOI/OTS) is in
preparation."

After: "it was recorded internally on 2026-08-11 and publicly disclosed on
2026-10-22 in a public GitHub repository — the commit history is verifiable
evidence of the date, and the disclosed elements form publicly accessible
prior art… while additional triple timestamping (DOI/OTS/notary) is in
preparation."

**EN philosophy (`en/philosophy.html:91`)**

Before: "The concept is published openly (the publication was created
2026-08-11; reliable triple dating — DOI, OpenTimestamps, notarization — is in
preparation) as defensive prior art…"

After: "The concept is published openly (recorded internally on 2026-08-11,
publicly disclosed on 2026-10-22 in a public GitHub repository — the commit
history is verifiable evidence of the date; additional triple timestamping —
DOI, OpenTimestamps, notarization — is in preparation) as defensive prior
art…"

## Methodology lesson

Fact-check verified against the internal source-of-record; the
PUBLIC-vs-INTERNAL date distinction was outside the audited claim set. Add a
"dating/legal claims" checklist item to future runs: every date attached to a
prior-art, public-domain, or disclosure claim must name its basis (internal
record vs public artifact) and, where public, point to a verifiable public
artifact.

## Files changed

- `index.html` (line 198)
- `ru/filosofiya.html` (line 91)
- `en/index.html` (line 198)
- `en/philosophy.html` (line 91)
- `OTCHETY/date_audit.md` (new)
- `OTCHETY/REPORT.md` (append one line)
