# Issue #42 completion report

## Broad corpus

The operational search produced 1,868 inventory records. After title-level scope audit and version deduplication, 394 are retained as materially relevant to classical RH or its declared conceptual neighborhood, 1,449 are screened out, and 25 are identified duplicate/alternate-version records. Every relevant record has a recorded lawful-access attempt. Five preprint/published-version pairs are explicitly linked; their acquired alternate-version text remains preserved.

Acquisition and normalization results for the 394 relevant sources:

| Outcome | Count |
| --- | ---: |
| Acquired full text and normalized | 85 |
| Partial web text/preview and normalized | 9 |
| No lawful open full text located | 210 |
| HTTP 403 block | 44 |
| HTTP 429 block | 21 |
| TLS validation block | 3 |
| Download timeout | 1 |
| Non-full-text response | 18 |
| Missing source URL (404) | 2 |
| Other download failure | 1 |

The corpus spans 1859 onward: 1 pre-1900 record, 14 from 1900-1949, 182 from 1950-1999, and 197 from 2000 onward. It includes 311 articles, 20 preprints, 18 book chapters, 17 books, primary and expository papers, conference papers, an authoritative survey, a collaborative reference, and a dissertation. Broad routing tags cover every requested viewpoint, including analytic foundations, explicit formulas, zero-free/density methods, mollifiers and moments, equivalent criteria, L-functions, spectral and random-matrix programs, computation, heat flow, history, and obstructions. Tags are discovery aids, not a Mathia ontology.

Eighteen declared metadata routes were followed by seven bibliography/citation rounds. After the stricter relevance and version-deduplication audit, citation-only marginal additions were 10, 63, 24, 28, 22, 4, and 1. The search continued beyond the initially planned six-round cap because late yield was still material. At round seven, 92% of returned records already overlapped the inventory; two new candidates passed the initial title screen and one survived the final metadata/relevance audit. This supports practical saturation for the declared route, not literal completeness.

Known gaps are unsearched citation tails beyond the round-seven stop, paywalled/inaccessible works, OpenAlex omissions or merged metadata, transient rate limits, non-English and uncatalogued historical material, and formula damage in some older scans. The 163 MiB external artifact store retains 178 original responses and 178 normalized derivatives; all are ledgered and hashed, and no redistribution-restricted source text is committed. Six relevant acquired scans required a flagged lower-confidence OCR fallback; two were the previously missed retained responses and four were found during the corrected acquisition pass. [`corpus_report.json`](../corpus_report.json), [`citation_expansion_log.json`](../citation_expansion_log.json), and the [design report](../../../docs/RIEMANN_CORPUS_DESIGN_V0.md) contain the detailed counts, routes, caveats, and hashes.

## Twelve-source pilot

### Freeze and selection

The pilot freeze is `riemann_pilot12_60d97cc4b13673cfcebf65f4d31e96f7533835a6ae1b50442fb6831a4d28af02`. The normative [`freeze.json`](freeze.json) records every exact title, author, version, identifier, canonical URL, raw artifact hash, normalized-text hash, page count, license caveat, selection rationale, and alternative candidate. Independent review changed the surrounding ledger but none of the twelve selected normalized artifacts or 24 source spans; provenance records the deterministic freeze rebind and its superseded ledger-coupled identifier.

The exact sources are Riemann/Wilkins (1859), Bombieri (2000), Conrey's Notices survey (2003), Conrey's two-fifths paper (1989), Lagarias (2002), Báez-Duarte (2003), Montgomery (1973), Keating-Snaith (2000), Connes (1999), Rodgers-Tao (2020), Platt-Trudgian (2021), and the AIM collaborative resource (2004). Together they cover historical construction, explicit formula and finite-field geometry, analytic partial results, arithmetic and function-space equivalences, spectral and random-matrix bridges, heat-flow obstruction, certified computation, exposition, and failed routes.

### Units and four passes

Exactly 24 semantic units were extracted—two from each frozen source, and none from the remaining broad corpus. Their descriptive types are all source-local: conjecture/epistemic limit, representation bridge, cross-domain analogy, structural dictionary, positivity criterion/gap, failed analogy, method synthesis, representation optimization, reformulation, extremal mechanism, discrete closure, approximation repair, conditional transform probe, model selection, model transfer, scale/factor split, open spectral reframing, analogy stress test, deformation boundary, equilibrium strategy, computational certification, bounded downstream transfer, landscape/duality, and failure catalogue.

[`units.jsonl`](units.jsonl) binds every unit to exact normalized-source line bounds, source and unit hashes, page markers, and the external unit text. The four raw analysis files each contain all 24 units exactly once:

| Pass | Records |
| --- | ---: |
| Spontaneous reading | 24 |
| Directed Mathia reading | 24 |
| Fresh isolated adversarial critique | 24 |
| Revised analysis | 24 |

The prompts are preserved under [`prompts/`](prompts/), outputs under [`analyses/`](analyses/), and hashes in [`analysis_manifest.json`](analysis_manifest.json). [`provenance.json`](provenance.json) records context separation and a material limitation: the runtime exposed a GPT-5-family Codex role but not the exact backend checkpoint, reasoning setting, or sampling parameters. Exact source, prompt, output, date, and context-role provenance is available; exact model-level replay is not. No claim to full configuration reproducibility is made.

### Extraction failures and representative outcomes

One unit is rejected for formula-level use: `conrey1989_u02_variational_freedom` has OCR too poor to recover the objective or admissible family. Two boundaries are materially incomplete: `lagarias2002_u01_elementary_equivalence` omits the displayed Problem E statement, and `rodgers2020_u02_equilibrium_contradiction` ends before the final Montgomery-based contradiction. Later Montgomery gap/simplicity consequences and the explanation for the discrete Báez-Duarte family also lie outside their respective clipped units; revised analyses no longer import them.

Strong accepted analyses include:

- `riemann1859_u02_mellin_bridge`, which retains the weighted prime-power object, transform, inversion, domain, and convergence limit;
- `baezduarte2003_u02_summability_repair`, which makes the target norm and failed baseline operational;
- `platt2021_u01_certified_completeness`, which separates witnesses from exhaustive accounting;
- `aim2004_u02_refuted_sufficient_conditions`, which preserves implication direction and localizes failed premises;
- `connes1999_u02_periodic_orbit_constraints`, accepted as analogy stress testing with both mismatches retained, not as existence evidence.

Impressive-looking rejected or narrowed analyses include the unreadable variational story, Lagarias's unseen inequality, an AIM catalogue promoted into a mechanism, and the clipped Rodgers-Tao contradiction. Bombieri's classical-geometric transfer is now inference, Montgomery's operator claim is conditional, Connes's absorption interpretation is author-motivated rather than uniquely forced, and Keating-Snaith's unsupported tail prediction was removed.

### Cross-source and capability-vs-style result

[`SYNTHESIS.md`](SYNTHESIS.md) finds five bounded recurring structures: representation change with relocated obligations; analogy that selects/rejects alternatives; auxiliary objects that amplify or certify a signal; precise localization of a failed route; and downstream usefulness constrained by exact epistemic reach. Each claim cites supporting units and retains counterexamples. It does not merge the RH programs or validate a candidate intuition.

The fresh [`AUDIT.md`](AUDIT.md) finds substantial evidence against an entirely style-only account: strong units retain incompatible mathematical details, operational distinctions, and concrete rejection conditions; negative and context-defective cases survive revision; concrete RH knowledge remains present. It also finds no causal evidence that these artifacts teach reusable capability: the same visible model family performs reading, abstraction, criticism, revision, and synthesis; the nine-field revision schema has a recognizable rhetorical cadence; no learner, held-out intervention, notation perturbation, or downstream worker was tested.

The pilot therefore demonstrates source-conditioned conceptual curation, not Mathia capability transfer. The broad corpus remains valuable independently of that result.

## Single exit decision

`REVISE_MATHIA_EXTRACTION`

Do not scale the current analysis format unchanged. A follow-on design should first repair or replace the three deficient units, reduce predictable teacher-schema fields, and add a frozen behavioral discriminator: source-grounded hidden consequences, representation choices, counterfactual failures, or analogy rejections on held-out/perturbed material, scored independently of prose similarity. The [future evaluation hypotheses](FUTURE_EVALUATION.md) separate Riemann-domain retention from out-of-domain conceptual transfer.

This decision permits a separate method-revision or training-design issue. It does not authorize training, GPU use, Qwen inference, proof search, or any change to the protected `#32` gate.
