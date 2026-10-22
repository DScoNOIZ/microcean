# EN-MIRROR — audit report

Date: 2026-10-22. Scope: EN mirror of MICROCEAN-SITE (repo at e7975cc; working tree
current = post-truth-fix pages). No commits, no style.css / research/ changes.

## Deliverables

| EN page | Mirrors RU | Voice |
|---|---|---|
| en/index.html | index.html | neutral navigation |
| en/for-everyone.html | ru/vsem.html | plain warm |
| en/specialists.html | ru/specialistam.html | engineering plain |
| en/scientists.html | ru/uchenym.html | academic light-touch |
| en/philosophy.html | ru/filosofiya.html | essayistic |

Cross-language links (one quiet link per pair, in existing nav/breadcrumb markup):
index.html↔en/index.html, vsem→../en/for-everyone.html, specialistam→../en/specialists.html,
uchenym→../en/scientists.html, filosofiya→../en/philosophy.html; mirror `RU` links on EN pages.

## ID mapping (RU → EN slug)

Keep-same: index.html (#intro #levels #about #problem #how #evidence #security #lagoons
#scenarios #philosophy #sources — RU ids already English); specialists.html (#architecture
#workflow #stack #comparison #prototype #next); scientists.html (#model #evidence #evolution
#swarm #cegis #p2p #trust #mdl #limits #sources).

Changed: for-everyone.html #sut→#essence, #kak→#how (rest same);
philosophy.html #govnocod→#zero-excess, #swarm-asi→#swarm, #resistance→#dialogue,
#common→#commons (rest same). All internal hrefs updated to match — EN tree self-consistent;
RU tree untouched ids.

## Terminology (source: MICROCEAN-publication-EN-scientific-2026-08-11.md)

| RU | EN (used site-wide) |
|---|---|
| Океан кода / «Океан кода из миллиарда капель» | the Ocean of Code / slogan "One ocean from a billion drops" (EN form taken verbatim from ru/filosofiya.html#name, which already quotes it) |
| микро-фрагменты | micro-fragments (pub 1.2) |
| лагуна | lagoon (pub vision) |
| планктон микро-фрагментов | plankton of micro-fragments |
| рой (исполнителей) | swarm (pub "Swarm of Micro-Networks") |
| ноль лишнего | "zero excess" (pub §8, E10) |
| ресурсная ответственность | resource responsibility; cost/pФ → cost(p) kept |
| зрелые формы | mature forms |
| всеобщее достояние | common heritage of all (footer: declared common heritage (CC0)) |
| defensive prior art / enabling disclosure | kept verbatim (already EN in RU page) |
| неотчуждаемое право авторства (ст. 1265, 1267 ГК РФ) | non-waivable authorship under RF Civil Code Art. 1265/1267 (en/index #philosophy) |
| измеренный профиль производительности | measured performance profile |

The 47-entry source list on scientists page kept verbatim (authors/urls); only RU
parenthetical annotations translated to the publication-EN forms: (Eq. (14))→(eq. (14)),
исправлено R3→(corrected R3), исправлено R3: правильное авторство→(corrected R3: proper
authorship), цитируется в→(cited in), обсуждается в→(discussed in), см. Li & Vitányi→(see
Li & Vitányi).

## Verification

Checker: /tmp/opencode/en_mirror_check.py (HTMLParser per page; internal href+fragment
resolution over both trees, incl. cross-tree EN↔RU links; directory link ../research/experiments/
accepted as existing dir).

```
parse(errors): 0
broken links/anchors: 0
NUMERIC index.html vs en/index.html: ru-only=0 en-only=0
NUMERIC ru/vsem.html vs en/for-everyone.html: ru-only=0 en-only=0
NUMERIC ru/specialistam.html vs en/specialists.html: ru-only=0 en-only=0
NUMERIC ru/uchenym.html vs en/scientists.html: ru-only=0 en-only=0
NUMERIC ru/filosofiya.html vs en/philosophy.html: ru-only=0 en-only=0
RESULT: PASS  (exit=0)
```

Tag-balance check (section/table/tr/td/th/ul/ol/li/h1-3/p/div/figure/a/...): 5/5 OK.

## Numeric sweep: mapping documented

- RU decimal comma `0,325` → EN decimal dot `0.325` (auto; sweep normalizes `,`→`.`).
- RU space-grouped thousands `10 000/10 000` → EN digit string without separator `10000/10000`
  (sweep joins `\d \d{3}` groups before compare, so both sides match).
- Spelled-out numbers (RU «восемнадцати тысяч», «два́дцать тысяч») mirror as words
  («about eighteen thousand», «twenty thousand») — invisible to digit sweep by design;
  spot-checked manually against digits used on index.html.
- Numbers in tables key-results identical: 10^101(.6), 10^53.4, 10^61.6, 33.4, 61.6,
  161700, 2.63·10²³, 1.645, c=z²≈2.71, N* 50–100, N_s 173, 30/30, 38.7/25.3/20.6,
  2·10⁴, 10⁻⁹⁷, λ 0.3/0.7→0.325, 1.7–3.5, 5.42±0.83, max 8, ceil log₂ n = 30,
  11.37±0.48, log₃ n=10.48, 1.08, 10000/10000, 1000/1000, p=0.99→91.2/100,
  820 candidates, 0.05 s, 1600, 0 discrepancies, 159→265, 2.5×, 150.9→60.9, −0.04,
  1–60 %, 11 lines, 2016/2020/2021/2024, ~18 thousand, ~11 cycles, 5–6 steps,
  left-pad/Log4Shell (CVE-2021-44228)/xz (CVE-2024-3094).

## Prompt-list clarification

Operator prompt listed 173.19 / 50.5/50.6; the current working-tree RU pages carry 173 /
50–100 (N*) and z=1.645, c=2.71. Per rule "faithful to RU working tree", EN mirrors the
working-tree values; documented here to avoid a false discrepancy flag.

## Ledger

REPORT.md appended (below pre-existing uncommitted WIKI-ARTIFACT line from a sibling agent),
verbatim: `<ts> | EN-MIRROR | en pages 5/5, checker 0 broken, numeric parity ok | OTCHETY/en_mirror.md`

## Additional rules honored

- NO commits made; no style.css, research/, robots, sitemap, favicon changes
  (git status: only index.html, ru/*.html +1 nav line each, en/ new, OTCHETY/).
- Head blocks mirrored: lang="en", og:locale en_US, og:title/og:description EN,
  favicon ../favicon.svg (index: favicon.svg), theme-color unchanged.
- Honest-limit envelope kept: E3/E4 caveats, limits table, all "plausible/impossible"
  statuses translated as Proven/Plausible/Impossible.
