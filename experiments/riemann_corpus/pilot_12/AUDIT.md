# Fresh capability-versus-style audit

## Scope and conclusion

This audit covers freeze `riemann_pilot12_60d97cc4b13673cfcebf65f4d31e96f7533835a6ae1b50442fb6831a4d28af02`: twelve sources, twenty-four frozen units, all four analysis passes, and the cross-source synthesis. I treated the generated analyses as teacher interpretations, not as mathematical validation. I also spot-checked the exact external unit text for representative accepted, rejected, boundary-defective, and analogy-heavy cases. No outside source was used. Independent review later corrected the broad-ledger audit without changing any selected normalized-source or unit hash; the freeze identifier was deterministically rebound to those unchanged selected bytes.

**Recommended issue exit decision: `REVISE_MATHIA_EXTRACTION`.**

The revised corpus is not merely empty style. Its best cases retain exact mathematical objects, altered parameters, logical directions, failed baselines, and observations that would reject a proposed bridge. However, the evidence does not distinguish extraction of reusable capability from production of a disciplined Codex explanation. Every candidate move and transfer expectation is teacher-authored; no held-out source, notation perturbation, or downstream behavior tests whether a learner can perform the move. The cross-source synthesis demonstrates that Codex can restate recurring structures across its own outputs, not that Mathia can reuse them. The corpus is therefore valuable, but the extraction/analysis method needs revision to supply the missing causal discriminator before it is scaled.

## Evidence and method

Observed:

- The frozen panel contains twelve source records and two units per source. The four pass files each cover all twenty-four unit identifiers.
- `python3 -m experiments.riemann_corpus validate-pilot --require-artifacts` passed during this audit.
- The provenance records one GPT-5-family Codex runtime, without an exposed checkpoint, reasoning setting, or sampling parameters. Pass 3 used a fresh isolated Codex context; Pass 4 returned to the primary executor context.
- Pass 4 uses the same nine-field explanatory schema for every unit. It still supplies a candidate intuition for twenty-one of twenty-four units; only `conrey1989_u02_variational_freedom`, `baezduarte2003_u01_discrete_closure`, and `aim2004_u01_equivalence_map` say that none is warranted.

Judgment:

- File and identifier integrity are adequate for this semantic audit.
- A fresh context within the same model family is useful criticism, but it is not stylistically or mathematically independent validation.

## The ten checks

### 1. Faithfulness

Observed:

- `riemann1859_u02_mellin_bridge` retains the intermediate weighted prime-power count, the Mellin encoding in `log zeta`, vertical-line inversion, and the source's warning that substituting the individual zero/pole terms does not yet give convergent integrals. Pass 4 correctly demotes the zero/pole calculation to an intended next step.
- `platt2021_u01_certified_completeness` faithfully separates sign-change witnesses from the Turing-method completeness count, retains ball/interval error control, and records why the computation counted zeros without unnecessarily isolating them to high precision.
- `aim2004_u02_refuted_sufficient_conditions` preserves the one-way logic: each auxiliary condition would imply RH, but the condition itself is false. It does not infer that RH or the surrounding analytic/Hilbert-space language is false.
- The adversarial pass found substantive errors rather than cosmetic ones. Pass 4 corrects Bombieri's zeros to characteristic roots (reciprocals of zeros and poles), restores Connes's finite-repeat mismatch, removes Keating-Snaith's invented tail prediction, and stops Rodgers-Tao's second unit before the absent final contradiction.

Judgment:

- The strongest revised records are source-faithful at the level needed for conceptual extraction.
- Faithfulness is uneven in earlier passes, and the repair depends on another Codex reading. Agreement after self-critique is evidence of better curation, not independent mathematical correctness.

### 2. Non-paraphrase value

Observed:

- Several records expose a consequential distinction rather than merely summarize a topic: raw partial sums versus a summability family in the required Hilbert norm (`baezduarte2003_u02_summability_repair`); zero detection versus exhaustive accounting (`platt2021_u01_certified_completeness`); and prime-orbit constraints versus two explicit mismatches (`connes1999_u02_periodic_orbit_constraints`).
- `riemann1859_u02_mellin_bridge` identifies an intermediate representation that a slogan such as “primes and zeros are dual” would omit.
- By contrast, `aim2004_u01_equivalence_map` remains a catalogue of interfaces, `baezduarte2003_u01_discrete_closure` states a compression theorem without explaining its mechanism, and `lagarias2002_u01_elementary_equivalence` can support only a meta-level dependency warning while the actual Problem E display is absent.

Judgment:

- There is real non-paraphrase value in a subset of the pilot: the analysis selects dependencies, failed premises, norms, parameters, or certificate roles that change what one should do next.
- That value is extraction and organization, not demonstrated reasoning transfer. Several weaker units are correctly retained as negative or context examples rather than promoted as intuition data.

### 3. Specificity

Observed:

- Unit-specific anchors survive revision: mollifier length `T^(4/7)` and incomplete Kloosterman-sum errors; matrix size `log(T/2pi)`; the `alpha < 1` Fourier range; pointwise and `L1` convergence versus divergence in `H`; the overall sign and finite-repeat denominator mismatch; and sign changes plus a Turing count.
- Strong expectations name an intervention or rejection condition. An altered Euler product must carry altered local factors through the weighted prime-power count and convergence domain. A time-reversal-invariant flow duplicates orbit contributions. A sign-change run without a completeness count cannot establish the finite RH claim.
- Many fields nevertheless share generic teacher language: “representation,” “bridge,” “obstruction,” “candidate intuition,” “discriminating expectation,” and “residual risk.” Some expectations are requirements for a future explanation rather than predictions derived or tested in the unit.

Judgment:

- Concrete anchors provide evidence against a wholly style-only account.
- The uniform schema also makes fluent imitation easy: a learner can reproduce the cadence of mechanism/expectation/risk without preserving the mathematical anchor.

### 4. Transfer content

Observed:

- The pilot contains proposed transfer content. Examples include carrying an Euler-product change through its transform representation, using an extremal divisor-sum set as a search policy, comparing CUE-plus-prime predictions with CUE alone, and propagating a certified finite height only to consequences that actually depend on it.
- The synthesis compares recurring structures across distinct sources: representation change with a relocated burden, analogy with model rejection, auxiliary objects that amplify or certify a signal, and localized repair after failure.
- None of those transfers is executed on a held-out source or task. No target model is asked to infer a hidden consequence, select a representation, repair a failed route, or reject a false analogue. No downstream prover or other independent worker is used.

Judgment:

- The corpus contains transfer hypotheses, not transfer evidence.
- Cross-source grouping by the same teacher cannot establish that the extracted move is reusable by Mathia. This is the central evidence for the selected exit decision.

### 5. Representation sensitivity

Observed:

- Several analyses are sensitive to the representation actually used. `baezduarte2003_u02_summability_repair` makes topology decisive; `montgomery1973_u01_conditional_fourier_probe` preserves the transformed observable and its frequency boundary; `keating2000_u02_scale_and_arithmetic_split` fixes the matrix parameter by mean density; and `connes1999_u02_periodic_orbit_constraints` checks sign, symmetry, and finite-repeat factors rather than accepting term resemblance.
- The revised finite-field analysis distinguishes characteristic roots from zeros and limits its internal check to rationality, the Riemann-Roch functional equation, and Frobenius magnitudes. That correction is exactly the kind of role sensitivity that generic analogy prose misses.
- There is no alpha-renaming, notation-change, alternative-presentation, or structurally equivalent realization test in the pilot.

Judgment:

- Representation-sensitive content is present in individual records.
- Robust representation-sensitive capability is untested; the available evidence comes from reading the original notation and explaining it once.

### 6. Uncertainty discipline

Observed:

- Pass 4 consistently distinguishes theorem, conjecture, heuristic, numerical evidence, author-motivated interpretation, open global step, conditional result, and finite verification. Particularly strong cases are Riemann's product versus all-root reality, Montgomery's restricted theorem versus extrapolated correlations and hypothetical operator, Connes's local trace results versus the open global formula, Rodgers-Tao's lower bound versus RH's opposite inequality, and Platt-Trudgian's finite theorem versus an unbounded claim.
- Revisions mark several abstractions explicitly as “conceptual interpretation,” “inference, not source fact,” or “conjectural transfer.” Prospective downstream results in Platt-Trudgian are separated from displayed corollaries.
- The exact generation checkpoint and sampling configuration are unavailable, and no formal or external correctness check was run for the mathematical interpretations.

Judgment:

- Epistemic calibration is one of the pilot's strongest properties and is useful training content in its own right.
- Correct uncertainty labels do not establish conceptual-move ability. They may themselves be a recognizable teacher style.

### 7. Teacher-style confound

Observed:

- The transformation is always `source -> GPT-5-family Codex schema`. Pass 2 assigns every unit concepts, performed moves, a candidate intuition, a discriminating expectation, Mathia relevance, and style risk. Pass 4 retains the same rhetorical slots even when the mathematical conclusion is only a warning or requirement.
- Recurring formulations—preserve an exact boundary, expose where difficulty moved, demand a concrete falsifier, distinguish local from global, and retain a residual risk—appear across mathematically different sources. These formulations are often sound, but their regularity supplies a strong stylistic shortcut.
- The adversarial process does sometimes resist its own template: three revised units deny that an intuition is warranted; source-external claims are removed; and attractive analogies are narrowed rather than uniformly celebrated.

Judgment:

- Evidence against style-only: outputs retain incompatible mathematical details and reject some apparently elegant records.
- Evidence for style-only: no learner behavior is measured, the analyst and critic are from the same model family, and the corpus offers highly predictable discourse fields. A learner could improve at producing calibrated “mechanism/limitation/expectation” prose without improving at selecting or performing mathematical moves.

### 8. Unit-boundary sufficiency

Observed:

- `conrey1989_u02_variational_freedom` has materially unreadable formula OCR. The polished Pass 2 story about admissible families, a common objective, and dominance was not verifiable. Pass 4 rejects a formula-level intuition and requires transcription before mathematical use.
- `lagarias2002_u01_elementary_equivalence` omits the displayed statement of Problem E. Pass 4 therefore keeps only the elementary-versus-hard dependency warning.
- `rodgers2020_u02_equilibrium_contradiction` ends before the final Montgomery-based contradiction. Pass 4 stops at the local-equilibrium consequence instead of claiming the full interface.
- Further soft limits are correctly noted: the Montgomery first unit does not contain the later gap/simplicity consequences; the first Báez-Duarte unit states the discrete closure theorem but not why the discrete family suffices.

Judgment:

- Boundary failures are material for the affected units but localized, visible, and mostly quarantined after revision.
- They are valuable negative examples for the audit, but they should not be silently converted into positive training records.

### 9. Source diversity

Observed:

- The panel spans 1859–2021 and includes a foundational memoir, primary partial-result papers, an authoritative problem description, modern computation, and a collaborative reference. Mathematical mechanisms include explicit formulas, positivity, mollifiers, divisor sums, Hilbert-space closure, Fourier statistics, random matrices, noncommutative trace ideas, heat flow, and certification.
- Seven of the twelve sources fall in 1999–2004. Two sources are by Conrey, and every source concerns one famous conjecture. There are two correlated units per source, not twenty-four independent source draws.
- All interpretive outputs come from the same visible model family and English-language corpus presentation.

Judgment:

- Mechanism diversity is strong enough to prevent the synthesis from being a single-method paraphrase.
- It is not diversity evidence for out-of-domain mathematical transfer, novel-problem reasoning, or robustness to a different teacher.

### 10. Retention of concrete Riemann mathematics

Observed:

- The revised records preserve substantial RH-specific content: xi roots and the reality conjecture; logarithmic Euler-product weights; Weil/Li positivity quantities; mollifier scale and off-diagonal errors; colossally abundant inputs; the Nyman-Beurling target norm; pair-correlation frequency ranges and symmetry classes; density-matched CUE size plus prime factors; prime-labelled periodic orbits and mismatches; the de Bruijn-Newman inequality directions; and finite zero certification.
- The synthesis cites unit identifiers and preserves important exclusions, including the absence of an operator construction, the open Connes global trace formula, finite versus global RH, and three context defects.
- The synthesis also compresses these cases into generic records such as representation gain/burden, analogy selection/rejection, and failure tuples. Those abstractions are the intended product, but they can be learned independently of the source mathematics.

Judgment:

- Concrete Riemann mathematics has not been washed out of the revised corpus. This is the strongest evidence against the claim that the artifacts are only prose style.
- Retention is necessary but not sufficient: it shows source-conditioned explanation, not independent conceptual capability or downstream fertility.

## Concrete case ledger

### Strong accepted analyses

- `riemann1859_u02_mellin_bridge`: accepted as a concrete representation bridge because it retains the weighted prime-power object, transform/inversion pair, domain, and convergence failure. The general transfer expectation remains untested.
- `baezduarte2003_u02_summability_repair`: accepted as a performed repair because the failed baseline, wrong/right topologies, parameterized replacement, and conditional/unconditional stages are all visible.
- `platt2021_u01_certified_completeness`: accepted as an operational evidence distinction because witness detection and completeness are separately necessary and yield a clear failure test.
- `aim2004_u02_refuted_sufficient_conditions`: accepted as strong negative material because it preserves implication direction and identifies the exact failed premises without overgeneralizing.
- `connes1999_u02_periodic_orbit_constraints`: accepted as analogy stress testing, not existence evidence, because it produces prime-orbit constraints, excludes time reversal, and retains both mismatches.

### Impressive-looking analyses rejected or sharply narrowed

- `conrey1989_u02_variational_freedom`: the original “preserve freedom and optimize later” account sounded reusable, but the central formulas, objective, inclusion relation, and dominance claim are unreadable. Formula-level use is rejected.
- `lagarias2002_u01_elementary_equivalence`: the original elementary-inequality interpretation outran a span that omits Problem E itself. Only the proof-dependency warning survives.
- `aim2004_u01_equivalence_map`: the directed pass promoted a catalogue into conceptual ranking and generalized a half-exponent expectation. Pass 4 correctly downgrades it to interface context with no new mechanism.
- `rodgers2020_u02_equilibrium_contradiction`: the earlier account imported the final contradiction from outside the clipped unit. The revision keeps the proved paper's strategy but stops at the in-span local-equilibrium consequence.

### Downgraded analogies and generalizations

- `bombieri2000_u01_finite_field_analogy`: “find the missing classical geometry” is now labeled inference; the check is confined to the proved finite-field dictionary, which supplies no classical transfer map.
- `montgomery1973_u02_unitary_analogy`: symmetry-class selection is conditional on an operator existing, and higher correlations remain predictions rather than construction evidence.
- `connes1999_u01_absorption_spectrum`: the negative sign motivates Connes's interpretation but does not uniquely select it; matching local roles is necessary within the program, not sufficient for the global formula.
- `keating2000_u02_scale_and_arithmetic_split`: the unsupported distribution-tail ablation is removed; only the stated moments/ranges support the comparison.
- `platt2021_u02_finite_evidence_utility`: downstream consequences remain concrete, while the general Mathia-fertility analogy is explicitly project interpretation rather than source mathematics.

## Final balance

Observed evidence against the style-only hypothesis is substantial but limited: exact mathematical roles survive; several outputs make source-conditioned counterpredictions; failures and missing context are retained; and Pass 4 sometimes refuses an intuition entirely.

Observed evidence for the style-only hypothesis remains material: the pipeline has generated explanations and proposed tests, but has run none of the tests that would establish reusable performance. The same teacher family supplies the reading, abstraction, criticism, revision, and synthesis, while the fixed schema creates a learnable rhetorical signature. This keeps the alternative hypothesis live and rules out scaling the current analysis method unchanged; it does not show that the outputs are mainly rhetorical or paraphrastic.

Final judgment: this pilot establishes a curated set of plausible, source-grounded conceptual interpretations and valuable negative cases. It does **not** establish that training on them would teach reusable mathematical capability rather than a highly competent style of mathematical explanation. Because the evidence supports corpus value while locating the main defect in the missing capability-versus-style discriminator, the single recommended exit decision is `REVISE_MATHIA_EXTRACTION`.
