# FC-B — fact-check `ru/specialistam.html` + `ru/filosofiya.html`

Agent B, MICROCEAN convergence project. Site state: commit 442a19f. Read-only check; no html edits.
Sources of truth abbreviated: **PUB** = canonical publication text; **BR** = brand report (concept working materials); **CON** = concept wiki notes; **LEGAL** = internal legal-risk verdict. Web evidence live-checked 2026-10-22 via searxng.

## Prior flags from R3 critic (M2, M3) — checked on MY pages

`50.5`, `50.6`, `0.06`, `10.1111` — **0 matches** in both files (grep). The M3/M2 figures do not appear on `specialistam.html` or `filosofiya.html`. The related "1–60%" range does appear (rows S12, F1) and is handled below.

## Ledger

| loc (file:line) | claim | verdict | suggested fix | evidence |
|---|---|---|---|---|
| ru/specialistam.html:32 | Верхний уровень = «Модель высокого уровня (ASI-класса)» | UNVERIFIABLE-RHETORIC | Drop "ASI-класса" or define; ASI presupposes a non-existing system class | No entity in PUB/CON uses "ASI"; design intent, not a fact |
| ru/specialistam.html:37 | «принцип sparse MoE» для роя микро-сетей | VERIFIED | — | Established technique (Mixture-of-Experts with sparse activation); consistent with PUB soul-lines |
| ru/specialistam.html:42 | GA-отбор; «схема-теорема Холланд‑а как теоретический фундамент»; fitness = ошибка+вес+конфликты | VERIFIED | — | Holland schema theorem real; fitness formula matches PUB:80 `Φ = ошибка + вес + конфликты` |
| ru/specialistam.html:47 | Kademlia O(log n); push-pull gossip O(log n); CRDT convergence; rarest-first | VERIFIED | — | Maymounkov & Mazières 2002; Karp et al. 2000 (FOCS); Shapiro et al. 2011 CRDT; Legout 2006 (PUB ref #21) |
| ru/specialistam.html:52 | PBFT (3f+1); Raft (2f+1); hashgraph aBFT; Sybil (Douceur, 2002) | VERIFIED | — | Castro–Liskov PBFT; Ongaro–Ousterhout Raft (2f+1 tolerates f crashes); Leouski–Baird aBFT; Douceur IPTPS 2002; mirrors PUB:93-97 |
| ru/specialistam.html:75 | Поиск: «Доказано O(log n); симуляция E5 подтверждает» | VERIFIED | — | PUB:84-85 (E5: 5.4 hop при n=10⁹, верхняя оценка 30); O(log n) из литературы по Kademlia |
| ru/specialistam.html:76 | «Доказано: Karp et al., 2000; симуляция E6 согласуется» | VERIFIED | — | Karp, Schindelhauer, Shenker, Vöcking, FOCS 2000 — push-pull rumor spreading O(log n) w.h.p.; PUB:86-87 |
| ru/specialistam.html:77 | CRDT «10 000/10 000 проверок аксиом моноида (E7)» | VERIFIED | — | PUB:88-89 (10000/10000 проверок законов моноида) |
| ru/specialistam.html:78 | GA: «Правдоподобно на модельных ландшафтах; границы исследованы (E2–E4)» | VERIFIED | — | PUB:120 `[ПРАВДОПОДОБНО] на модели`; honest status wording preserved |
| ru/specialistam.html:79 | CEGIS/SyGuS: «Доказан каркас; toy-эксперимент E9 успешен» | VERIFIED | — | Alur et al. SyGuS; PUB:340 (max via ite, 1 CEGIS iter, 0.05 s, 1600 points, 0 mismatches) |
| ru/specialistam.html:80 | MDL: «−2,5× длины при сохранении корректности; абсолютная минимальность невычислима» | VERIFIED | — | PUB:572 (E10: MDL-GA 150.9→60.9 = 2.48× ≈ 2,5× при корр. 1.0); Kolmogorov K uncomputable (PUB:472) |
| ru/specialistam.html:88 + ru/filosofiya.html:42 | «используется 1–60 % / от одного до шестидесяти процентов содержимого» пакета | IMPRECISE | Attribute source or soften to «часто меньшая часть пакета»; range currently unattributed | Matches PUB:130/514 (canonical), but canonical itself carries no external citation; R3 critic (M3) found internal inconsistencies (50.5% packages vs 50.6% dependencies) in the study chain behind these stats |
| ru/specialistam.html:89 | Зависимости «Явные, версионные, конфликтующие» | IMPRECISE | «Версионные конфликты реальны, но lock-файлы и резолверы их частично снимают» | Blanket claim; canonical PUB:131 says same; conflicts documented (pip/npm), but tooling mitigates |
| ru/specialistam.html:90 | Верификация сегодня: «Тесты пакета (если есть), доверие мейнтейнеру» | VERIFIED | — | Fair summary; matches PUB:132 |
| ru/specialistam.html:91 | Обновления «Ручные, ломающие совместимость» | IMPRECISE | «Обновления полуручные (Dependabot/npm update); semver-аккорды нередко ломают совместимость на практике» | npm updates ARE user-triggered, but not purely manual (bots, lockfiles); PUB:133 adds «semver не спасает» |
| ru/specialistam.html:92 | Цепочка поставок — главный вектор атак (SolarWinds, xz) | VERIFIED | — | SolarWinds 2020, xz-utils backdoor 2024 — real, documented (also PUB:26); industry reports rank supply-chain as top threat |
| ru/specialistam.html:94 | «Расходуются без предупреждения и отчёта; установка из исходников тянет гигабайты зависимостей молча» | IMPRECISE | Soften: «часто без полного заранее объявленного ресурсного следа» | Gigabyte node_modules real, but npm/pip print package counts/progress; per CON:86-129 these resource claims are explicitly author draft, status «ВЕКТОР/НАБРОСОК», pending LEG research |
| ru/specialistam.html:95 | «[Оптимизация —] аварийный акт под давлением…» | UNVERIFIABLE-RHETORIC | Mark as observation/intent, not fact | Author's framing (CON:110-114); no external measure |
| ru/specialistam.html:100 | «автоматическое извлечение нужных функций из модулей (code-extraction) … уже существует в миниатюре» | IMPRECISE | «Извлечение нужных функций из модулей достигается (частично вручную) в миниатюре» | PUB:138: skill-graph + resource-economy-mandate «уже **вручную** "вытягивают" микро-функции» — canonical says manual, site says automatic |
| ru/specialistam.html:100 | Оценки этапов: «реестр+поиск — недели; эволюционная сборка — следующий квартал; рой верификаторов — параллельная ветка» | IMPRECISE | Attribute: «наша субъективная оценка» / "rough estimate"; or delete | NOT in canonical PUB/CON; unattributed schedule projections presented in same paragraph as existence facts; no honest authorship of the estimate |
| ru/filosofiya.html:76 | «когда-то письменность не отменила память, а умножила её; интернет не отменил общения, а расширил его» | UNVERIFIABLE-RHETORIC | Keep, it is declared rhetoric | Per task brief: rhetorical analogy, not factual claim |
| ru/filosofiya.html:81 | «defensive prior art: публичная фиксация означает, что никто … не сможет оградить идею патентом» | VERIFIED | Add nuance «в пределах того, что реально раскрыто» | Defensive publication mechanism real (LEGAL:102, MPEP §901 / ст.54 EPC); caveat: blocks novelty on disclosed subject matter only |
| ru/filosofiya.html:91 | «Автор публикует идею и не управляет никакой инфраструктурой» | VERIFIED | — | LEGAL:7: author is private person, no infrastructure, no benefit, no legal entity |
| ru/filosofiya.html:98 | «Из более чем тридцати кандидатов после сорока проверок … финалистами стали Microcean, Liquidform, Seawell и Pelagic» | IMPRECISE | «оценке подверглись восемь финалистов; лучший четвёркой стали…» | BR header: «оценка **8 финалистов**»; the four named are the top-4 by score (33/33/29/28); Freshet, Synthocean, Thalassic, Ocean(эталон) also evaluated. "30+ кандидатов / 40+ проверок" matches PUB:544 |
| ru/filosofiya.html:98 | «сорока проверок на занятость (товарные знаки, домены, ассоциации)» implies coverage was effective | IMPRECISE | Honest note: fresh web check surfaced a documented registered «MICROCEAN®» (Jaubert NNR aquarium water-purification system, 1979); plus marine-research accounts @microcean (X), microcean.hanyang.ac.kr, MICROcean Raman imaging system — none of which are in BR | Live check 2026-10-22: bulkreefsupply.com/content/post/dr-jean-jaubert-reef-keeping-ecology-macna-2018 («MICROCEAN® or JAUBERT NNR SYSTEM»); fpa2.org/en/branches/monaco/scientific-and-technical-committee; BR:23 lists only SeaWorld attraction + Pure Ocean project |
| ru/filosofiya.html:99 | «единственное из имён называет сам механизм»… оба корня — международные когнаты | VERIFIED | — | BR:22 and BR:61 — brand-report evaluative claim, correctly carried |
| ru/filosofiya.html:99 | Слоганы «Океан кода из миллиарда капель»/«One ocean from a billion drops»; символ — волна из точек | VERIFIED | — | PUB:553 |
| ru/filosofiya.html:117 + ru/specialistam.html:118 | Footer: «концепция опубликована как всеобщее достояние · 2026» | IMPRECISE | «Концепция публикуется открыто · декларация как всеобщее достояние (CC0) · 2026» — declaration, not accomplished registration | Author has no legal personhood/registration (LEGAL:7); RU: авторство/личные неимущественные права неотчуждаемы (LEGAL:268, ст.1265 ГК РФ); "public domain" by unregistered declaration is legally a license+future-proofing, not a formal status. Site does not claim filing/registration — hence IMPRECISE, not FALSE |
| ru/filosofiya.html:70-71,89 | Лагуна «ноль утечек»; участие добровольно | VERIFIED | — | CON:133-139 «ничего не утекает наружу»; design claims consistent with CON |

Verdicts on rows with two sub-claims (loc 100 specialistam) are counted separately. Association-verification claims (web):

- **SeaWorld Abu Dhabi MicroOcean attraction — VERIFIED** (≥2 sources): https://www.seaworldabudhabi.com/en/realms/micro-ocean (official park site, official realm page); https://en.wikipedia.org/wiki/SeaWorld_Abu_Dhabi; https://miral.ae/news-item/seaworld-yas-island-abu-dhabi-crowned-the-largest-indoor-marine-life-theme-park-by-guinness-world-records/
- **Pure Ocean fund Microcean marine-microbiology project — VERIFIED** (≥2 sources): https://www.pure-ocean.org/en/our-projects/microcean/ (official fund page, 2024 cohort); https://www.youtube.com/watch?v=-3IoeWlBrlc («DISCOVER OUR PURE OCEAN 2024 PROJECTS: MICROCEAN», @pureoceanfund)
- **New collision found (not on site, not in BR): registered MICROCEAN®** — Jean Jaubert's 1979 water-purification process, cited as MICROCEAN®/JAUBERT NNR SYSTEM on advisories of FPA2 Monaco and Oceans For All foundation (URLs in ledger row ru/filosofiya.html:98).

## Style smells (EN, ≤5)

- Estimated schedules («недели работы», «следующий квартал») sit in the same paragraph as existence claims — the reader cannot tell projection from fact.
- «ASI-класса» is a neologism used as if it named an existing model class — quiet authority by jargon.
- The comparison table "Сегодня" column mixes measured statements («SolarWinds, xz») with blanket rhetoric («молча», «без отчёта»), so a true cell shields an exaggerated neighbor.
- The numeric «1–60%» is repeated on two pages with zero source attribution.
- Footer states legal status in perfective («опубликована как всеобщее достояние») instead of the accurate declaration phrasing.

## Counts

30 claims total: 17 VERIFIED, 10 IMPRECISE, 0 FALSE, 3 UNVERIFIABLE-RHETORIC.
Note: `git commit` of this check pending operator decision (task says no commits).
