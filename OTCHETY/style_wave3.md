# STYLE wave3 — voice pass over 5 pages ("War and Peace, not a spec sheet")

Agent: STYLE wave3. Base: commit `442a19f` + uncommitted F1–F3 truth-fixes in the
working tree (none reverted; all fact tokens preserved). Scope: text nodes only —
tags/classes/ids/comments/section order untouched; footers verbatim as passed by
F1/F2. No commits. Checker scripts in `/tmp/opencode/style3/` (check.py =
html.parser + href/anchor (fc_d_linkcheck pattern), sweep.py = numeric-token
diff, hedgecheck.py = rail-1 hedge-string counts).

## Voice targets applied

- ru/vsem.html — strongest literary treatment for a reader with no IT background.
- index.html — warm, clear, honest; table structure intact.
- ru/specialistam.html — engineering clarity; every dense term gets a short
  parenthetical gloss at FIRST occurrence; remaining канцеляризмы removed.
- ru/filosofiya.html — essayistic; metaphors sharpened; grammar fix.
- ru/uchenym.html — light touches ONLY: mixed-script typo fix, one term gloss.
  Numbers/formulas/statuses untouched.

## Per-page work summary

vsem (7 edits): "существует → живёт", streams-feed-the-river image in the opening;
simplified "собрать программу самому" paragraph; blockquote re-phrased to the
hedge-preserving "только в тех пределах, которые публикация сама честно называет"
(hedge «широкий класс задач» verbatim); bathroom-faucet paragraph de-dashed and
given clean subject ("нередко в готовой программе всё равно остаются десятки и
сотни тысяч ненужных строк", grammar of старая run-on fixed); water metaphors
refreshed ("затянет пробоину", "весть … морской волной", "точь-в-точь"); «гоняются
проверки» kept. Footer/CC0 untouched.

index (6 edits): removed the dash-pile "а — по замыслу концепции —" (hedge kept,
moved into commas); "функции распределены → вещи разбросаны по отдельным
инструментам"; "работающего вручную → работающего руками"; shorter warm lagoons
phrase ("не отменяет права на приватность"); smooth philosophy paragraph
("Эти вопросы справедливы, и ответы в архитектуре предусмотрены — пока в статусе
проектных принципов"); «устранять → убирать» in security intro. All tables verbatim.

specialistam (+76 words, intentional: mandated term glosses): sparse MoE
(«разреженная смесь экспертов»), GA/GP, fitness, Kademlia DHT, push-pull gossip,
CRDT, rarest-first, PBFT vs Raft (ложь участников vs честные), Sybil («толпа
фальшивых личин»), XOR-метрика, AEAD, CEGIS/SyGuS, MDL, skill-graph. Removed
канцеляризм "задействованы"; kept every hedge ("часто без полного заранее
объявленного ресурсного следа", "принцип-набросок из концепции, требующий
проверки", "авторская прикидка, а не обещание сроков", "диапазон требует проверки"
via "по доступным оценкам").

filosofiya (5 edits): archipelago→"одной сплошной водой"; dead bureaucratic list
("функции … передачи практик разнесены") → "обмен кодом, сама работа, хранение
истории и передача опыта живут по разным углам"; "не тащить то, что не
используется" → "не тащить за собой…"; "масштабируется горизонтально" → "растёт
вширь"; grammar fix "так же, когда-то" → "так же, как когда-то"; "делает их труд
вечным" → "делает этот труд вечным (продолжает …, а не пылится)". Legal sections
(§common, §character) untouched. §name numbers verbatim (33 из 40; 9, 7, 9, 8;
Liquidform 33; Seawell 29; Pelagic 28; восемь финалистов; 1979).

uchenym (2 edits): Latin+A typo `Aмдал` → Cyrillic `Амдал` (line 95); sparse MoE
gloss «разреженная смесь экспертов» in §swarm. Zero numeric/formula/status edits.

## Stats (tag-free plain text; sentence split on [.!?…] with >2 words)

| page | words before→after | avg words/sentence before→after | drift |
|---|---|---|---|
| index | 1660→1670 | 15.05→15.14 | +0.6 % |
| vsem | 1054→1059 | 14.72→14.79 | +0.5 % |
| specialistam | 691→767 | 11.72→13.03 | +11.0 % (term glosses) |
| filosofiya | 1125→1135 | 15.19→15.32 | +0.9 % |
| uchenym | 1703→1707 | 8.00→7.98 | +0.2 % |

All pages within the ±15 % rail. Baselines reconstructed from saved pre-edit
copies (/tmp/opencode/style3/base_*.html; reverse-verified for vsem).

## Fact-preservation sweeps (results)

1. Numeric-token sweep (regex over tag-free body text, before vs after):
   index 37→37, vsem 7→7, specialistam 26→26, filosofiya 15→15, uchenym
   244→244 — ZERO diffs on all five pages.
2. Hedge-string sweep (rail-1 list incl. «(CC0)», «ст. 1265/1267», «широкий
   класс задач», «по замыслу», «около 11 циклов», 173/2,71, 50.5/50.6, 33 из 40,
   9, 7, 9, 8, восемь финалистов, 47, «по доступным оценкам», «диапазон требует
   проверки», prior art, enabling disclosure, 2026-08-11, No Free Lunch,
   «принцип-набросок», «авторская прикидка», MICROCEAN®/1979, 161 700,
   2,63·10²³, 10^101, ~10⁸⁰, 5,42 ± 0,83, 11,37 ± 0,48, 10 000/10 000,
   1000/1000, 150,9 → 60,9, 159 → 265, −0,04, OpenTimestamps/DOI): **0 drops,
   0 count changes** on every page.
3. html.parser + href/anchor check (fc_d pattern, includes cross-page anchors,
   img passes through unchanged): **0 issues**; section inventory identical to
   pre-edit (index 11, specialistam 3, uchenym 10, filosofiya 9, vsem 7; each
   id appears exactly once).
4. Hype-word check: no «прорыв / революция / уникальный / невозможный» introduced;
   existing honesty-hedges untouched.

## Notes

- One transient bad edit during vsem (English placeholder sentence accidentally
  substituted for the "Вода принимает форму любого сосуда" paragraph) was caught
  by the same edit and erased; final file verified free of it (grep exit 1).
- Trainer note: agent fingerprints of F3 remain in sources block (uchenym) — kept
  verbatim per "extracted-verbatim-47-sources block" rail.
