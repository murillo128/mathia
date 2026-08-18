# Riemann corpus and twelve-source Mathia pilot v0

## Status and boundary

This document records the exploratory work authorized by GitHub issue `#42`. It does not change the `#29` / `#32` intuition-fertility gate, define a permanent Mathia ontology, authorize training, or claim progress on the Riemann hypothesis.

The experiment deliberately separates:

1. a broad, reusable and auditable source-acquisition pass; and
2. a small teacher-generated interpretation pilot over exactly twelve frozen sources.

The broad ledger is [`experiments/riemann_corpus/inventory.jsonl`](../experiments/riemann_corpus/inventory.jsonl). Full source text is not committed: it lives under the external artifact root `/workspace/mathia-artifacts/riemann-corpus-v0`, with hashes and relative paths in the ledger. This protects redistribution-restricted texts while keeping local inspection possible.

## Part I: operationally broad corpus

### Discovery method

Discovery used eighteen declared OpenAlex title/mechanism routes covering foundations, explicit formulas, zero-free and zero-density methods, mollifiers and moments, equivalent criteria, Nyman-Beurling, de Bruijn-Newman, pair correlation, random matrices, Hilbert-Polya, noncommutative geometry, L-functions/GRH, computation, and history. A manually curated spine supplied primary and authoritative sources that catalogue search missed. Bibliographies/reference links from resolvable pilot candidates were expanded for seven rounds.

The first exact-phrase query pass was preserved as `discovery_log_pass1.json`; the first repaired title/mechanism pass is preserved as `discovery_log_pass2.json`; and `discovery_log.json` records the final refreshed pass. This matters because the first pass looked precise while missing too much. After independent review, the final pass also rejected recurring substring/homonym errors such as rational functions, Riemann surfaces, Riemann-Liouville operators, the Riemann-Hilbert correspondence, and unrelated zeta theories. The ledger retains screened-out candidates and identified duplicates instead of silently dropping them.

The final ledger contains:

- 1,868 unique inventoried records;
- 394 title-screened relevant sources;
- 1,449 screened-out candidates and 25 duplicates;
- 85 relevant acquired full texts;
- 9 relevant partial web texts/previews;
- 94 relevant normalized texts in total;
- 47 acquired/normalized artifacts later screened out or classified as alternate versions but preserved.

Every currently relevant record has a recorded acquisition attempt. Relevant-source acquisition outcomes are 85 full text, 9 partial text/preview, 44 HTTP 403 blocks, 21 HTTP 429 blocks, 3 TLS-validation blocks, 1 timeout, 2 missing URLs, 18 non-full-text responses, 1 other download failure, and 210 sources for which no lawful open full text was located. These categories describe access outcomes, not judgments of mathematical quality. Five explicit preprint/published-version pairs are linked by canonical and alternate source IDs; acquired alternate-version text remains preserved.

### Normalization and storage

Successful PDFs were converted with `pdftotext -layout`, UTF-8 output, and inserted source-page markers. HTML was reduced to visible text. Source-native text is retained when available. Two relevant scans with empty text layers were recovered with a flagged Tesseract OCR fallback (8 and 3 pages); their original scans and lower-confidence warnings remain authoritative for checking symbols. Original responses remain beside normalized derivatives; extraction warnings explicitly note formula, ligature, reading-order, OCR, and HTML-layout risks. No formula was silently repaired.

The external store currently occupies about 163 MiB. It contains 178 raw responses and 178 normalized derivatives, including short/non-full-text responses retained for audit. Every retained file is bound to a ledger row and cryptographic hash; validation fails on an unledgered retained response. The research corpus count above treats only ledger-classified full or partial source texts as acquired material. Copyrighted text without redistribution permission is never copied into Git.

### Coverage and limits

The relevant ledger spans 1859 to the present inventory snapshot: 1 pre-1900 source, 14 from 1900-1949, 182 from 1950-1999, and 197 from 2000 onward. It includes 311 articles, 18 book chapters, 17 books, 20 preprints, 3 conference papers, a dissertation, primary papers, and authoritative/expository/reference sources. Discovery tags show material in every issue-required viewpoint, but tags are broad routing aids and are neither exclusive nor a Mathia ontology.

The post-screening, post-deduplication citation-only marginal yields were 10, 63, 24, 28, 22, 4, and 1 sources over rounds one through seven. The search was not saturated at the earlier six-round cap, so it continued. Round seven returned 180 metadata records but only 14 new candidates; 92% already overlapped the inventory, two were initially in scope, and one survived the final metadata/relevance audit. This is evidence of practical saturation for the declared search route, not literal bibliographic completeness.

Known gaps remain:

- unsearched tails beyond the round-seven overlap/diminishing-yield stop;
- inaccessible or paywalled primary papers and monographs;
- OpenAlex omissions, merged records, incomplete reference lists, and transient rate limits;
- non-English, older, uncatalogued, and non-digitized historical sources;
- author pages or repositories not reachable from the declared routes;
- normalization damage in scanned formulas, especially older papers;
- title-level relevance screening, which can reject an indirectly relevant work or retain an only superficially relevant one.

The corpus is therefore broad and reusable, but not a claim of a complete RH bibliography.

## Part II: exact twelve-source freeze

Only after the broad ledger, acquisition attempts, normalization, and citation audit were complete was the pilot frozen. The freeze identifier is:

`riemann_pilot12_60d97cc4b13673cfcebf65f4d31e96f7533835a6ae1b50442fb6831a4d28af02`

Independent review corrected the broad-ledger relevance, duplicate, and retained-scan audit after the analyses had been produced. The selected twelve normalized artifacts and all 24 exact source-span hashes were unchanged. The freeze was therefore rebound to a deterministic identifier over the selected source versions/hashes and selection rule; provenance retains the superseded ledger-coupled identifier rather than implying that the analyses were regenerated.

The exact versions, artifact and normalized hashes, selection rationales, and role alternatives are in [`pilot_12/freeze.json`](../experiments/riemann_corpus/pilot_12/freeze.json). The panel is deliberately heterogeneous rather than statistically representative:

1. Riemann (1859), Wilkins translation — foundational construction and conjectural boundary;
2. Bombieri (2000) — authoritative overview, finite-field geometry, and explicit formula;
3. Conrey (2003) — analytic/spectral exposition and a documented false spectral coincidence;
4. Conrey (1989) — a major mollifier-based partial result;
5. Lagarias (2002) — elementary-looking arithmetic equivalence;
6. Báez-Duarte (2003) — function-space closure and discretization;
7. Montgomery (1973) — conditional pair correlation and unitary statistics;
8. Keating-Snaith (2000) — random-matrix transfer, scale matching, and arithmetic correction;
9. Connes (1999) — noncommutative trace/absorption-spectrum program and its open global step;
10. Rodgers-Tao (2020) — heat-flow deformation and an obstruction theorem;
11. Platt-Trudgian (2021) — rigorous finite verification and its epistemic/downstream limits;
12. AIM (2004) — equivalence landscape and documented failed sufficient conditions.

## Parts III-IV: semantic units and four-pass analysis

Two contiguous semantic units were selected from each source, for 24 units total. A unit can be motivating prose, a theorem/criterion with interpretation, a construction, a proof-strategy fragment, a method comparison, or a failure diagnosis. It is not equated with a lemma. [`unit_plan.json`](../experiments/riemann_corpus/unit_plan.json) records why each span is coherent; [`units.jsonl`](../experiments/riemann_corpus/pilot_12/units.jsonl) binds it to exact normalized-source lines and hashes. Unit text remains in the external store beside its source.

The analysis passes are intentionally separate:

- spontaneous source reading without the Mathia checklist;
- directed reading through the provisional concepts/moves/intuition lens;
- adversarial criticism in a fresh isolated Codex context;
- minimum revision using the source and all preserved earlier passes.

Prompts and raw outputs remain distinct under `pilot_12/prompts/` and `pilot_12/analyses/`. The runtime exposed only a GPT-5-family Codex role, not the exact backend checkpoint, reasoning setting, or sampling parameters. [`provenance.json`](../experiments/riemann_corpus/pilot_12/provenance.json) records that reproducibility limitation rather than inventing precision.

## Scientific interpretation boundary

The unit analyses are teacher-generated interpretations. Source faithfulness, logical calibration, and nontrivial predictions can make them plausible training candidates, but Codex agreement cannot validate them as mathematical truth or reusable capability. The cross-source synthesis and capability-vs-style audit therefore preserve rejected cases, boundary failures, and alternative explanations.

No Qwen/Mathia inference, qwen-lean proof search, training, GPU use, formalization, or open-conjecture search occurred in this issue.
