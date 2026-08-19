# Full Riemann–Mathia corpus report

## Outcome

Final issue #42 corpus decision: `RIEMANN_MATHIA_CORPUS_READY`.

This is a corpus-generation result only. It does not authorize training, choose a mixing ratio, run Qwen or qwen-lean, use the GPU, perform RL, merge weights, or bypass #32.

## Inputs and source usability

The audited ledger contains 393 relevant bibliographic rows. Of those, 94 had full, OCR, preview, or partial-web normalized responses in the source-of-truth acquisition statuses. Per-source inspection classified 86 as usable for mathematical interpretation and 8 as excluded.

The usable set is 79 ordinary normalized sources, six OCR sources usable only through checked prose-rich spans, and one coherent three-page book preview usable only within the retained pages. All eight partial web captures were excluded because manual inspection found publisher/repository landing pages, access challenges, or abstract-only metadata rather than coherent mathematical source text. The 18 sub-1KB non-fulltext responses are acquisition failures and were never counted among the 94 candidate inputs.

## Semantic units and interpretations

The release contains 274 accepted exact source units across all 86 usable sources: 24 calibrated pilot spans (including the three versioned v1 repairs), 74 first coverage-pass spans, and 176 units from a separate non-quota whole-source expansion. Source text remains a separate trainable object.

The non-quota expansion decisions were {'expanded': 69, 'no_additional_unit': 2, 'quarantined': 3}; additional-unit counts per non-pilot source were {0: 5, 1: 10, 2: 25, 3: 20, 4: 14}. This variable distribution replaces the initial one-unit coverage artifact and avoids treating papers as equally rich.

Multi-pass interpretation decisions: {'accepted': 267, 'quarantined': 6, 'rejected': 1}. Accepted interpretations cover 84 of 86 usable sources. Source units remain eligible even when their derived interpretation is quarantined or rejected.

Speculation handling across revised records: {'downgraded': 39, 'explicitly_marked': 36, 'none': 199}. This count includes explicit marking and downgrades; it is not a truth score.

## Coverage

Accepted-interpretation source coverage by era: `{'1900-1949': 1, '1950-1999': 25, '2000-present': 57, 'pre-1900': 1}`.

Accepted-interpretation source coverage by source type: `{'article': 58, 'authoritative-survey': 1, 'collaborative-reference': 1, 'conference-paper': 1, 'expository-survey': 1, 'preprint': 13, 'primary-expository-paper': 1, 'primary-paper': 7, 'primary-paper-translation': 1}`.

Accepted-interpretation source coverage by broad discovery viewpoint: `{'analytic-continuation-functional-equation': 2, 'debruijn-newman': 1, 'equivalent-criteria': 12, 'explicit-computation': 5, 'historical-foundational': 1, 'l-functions-families': 14, 'mean-values-moments': 10, 'other-rh-neighborhood-mechanism': 15, 'spectral-physics': 8, 'survey-or-foundational-overview': 4, 'zero-distribution': 22, 'zero-statistics-random-matrix': 9}`. These tags are audit strata, not a Mathia ontology.

## Cross-source synthesis

Twenty source-linked synthesis candidates (twelve initial and eight non-quota-expansion candidates) received separate fresh criticism and revision. Final decisions: {'accepted': 16, 'quarantined': 1, 'rejected': 3}. Every accepted synthesis resolves at least two distinct source parents and retains limits/mismatches in model-visible content.

## Layered quality control

All records receive deterministic hash/span/parent/rendering/exclusion validation. Every interpretation received a source-linked fresh adversarial critique. The pilot's nine RH and six transfer behavioral tasks remain frozen as evaluation-only QA seeds; they are not trainable objects and no artificial task-count target was pursued.

The fresh independent stratified audit reviewed 84 objects, including all OCR/partial/non-accepted interpretation strata, era/source-type/viewpoint/unit-type coverage, and every synthesis. Decisions: {'accept': 73, 'quarantine': 6, 'reject': 5}. The sample is an audit estimate, not independent mathematical proof.

Current release labels were withheld from that auditor. Its frozen output produced 2 synthesis-label disagreements; both are preserved in `audit/synthesis_reconciliation.jsonl` and applied to the final eligibility state rather than overwritten or forced into agreement.

Source-faithful final interpretation acceptance rate: 267/274 (97.4%). Paraphrase/style rejection is represented by 1 final rejections; context/OCR insufficiency by 6 quarantines. Speculation/generalization was downgraded or explicitly marked in 75 records.

Recurring critic failures were metaphorical explanation replacing mechanism, imported theorem context, exact claims reconstructed from OCR, and physical/proposed-RH reformulations presented too literally. The revision pass applied these at batch scale; the independent audit is a separate check for remaining systematic defects.

## Representative evidence

Strong accepted examples:

- `aim2004_u01_equivalence_map` — Accepted because the excerpt is a clear survey map rather than unsupported mathematical importation.
- `aim2004_u02_refuted_sufficient_conditions` — The source names the failed bridges and the exact reason each bridge collapses, which makes the unit cleanly trainable.
- `baezduarte2003_u01_discrete_closure` — Accepted because the theorem statement encodes a specific strengthening, not merely a restatement of the older criterion.

Rejected or quarantined examples:

- `full_openalex_w1605891845_u01` (quarantined) — Quarantined because source quality and missing geometric context make the claimed conclusion untrustworthy.
- `full_openalex_w1764772889_u01` (quarantined) — The source itself disclaims the rigorous scalar-product meaning, so the conceptual object is not reliable enough for accepted interpretation use.
- `full_openalex_w2050389282_u01` (quarantined) — Severe OCR corruption prevents a reliable accepted interpretation even though a coarse comparative claim is visible.

Uncertain material is retained through `context_limit`, OCR/partial flags, critic outputs, and non-accepted objects rather than repaired from memory. The six OCR sources never certify damaged exact formulas unless the readable unit supports them.

## Shared interchange and release integrity

The release uses `mathia-interchange-v1` with a single deterministic renderer shared with the representative #44 agnostic fixture. Eligible source, interpretation, and synthesis roles render without exposing corpus origin, release, quality state, teacher identity, or acceptance metadata. The synthetic mixed manifest materializes records from both releases with no corpus-specific conversion and detects hash/canonical-lineage duplicates.

Freeze: `riemann_mathia_full_e9f9f663e6f3a777ab7545f088f39d0662462f5da622364204e52be6fcf42cd6`.

Core release hashes: `{'objects.jsonl': '52245391e270f938dd54bf1f23c5c43319572789e58ad4d77df2d0787fdaebb1', 'trainable_manifest.json': '5e08fbc45bc39b158112b8e26742cbd6be5ca6530a08043045ef3000be92e0b1', 'mixed_manifest.json': 'bd7a7f668e21dc679ab7e298abe0d5dcde9e9a2500510861d290e41d99bb7191'}`.

Trainable object counts: `{'source': 274, 'interpretation': 267, 'synthesis': 16}`. QA tasks, raw passes, critiques, rejection records, and audits are not automatically trainable.

## Storage, licensing, and limitations

Raw sources, normalized full text, and semantic source-unit text remain under the external local artifact store. Git retains provenance, hashes, small derived teacher outputs, audit evidence, and manifests. Freely accessible text with no redistribution grant is not committed. Each source object records the reported license boundary and an external content reference.

Teacher prose is distillation, not independent mathematical validation. Famous-source familiarity remains a confound. Some acquired sources contain speculative, physical, or purported-proof programs; accepted interpretations must preserve that epistemic status. The inventory is broad but not literally complete: paywalled/inaccessible works, non-digitized historical material, non-English tails, repository omissions, and the stopped citation frontier remain gaps.

The release is ready as one native side of a later compatibility-preserving training mix. That later design is a separate issue and remains gated by the repository's training/compute discipline.
