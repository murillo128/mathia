# MI-002 — Universal affine scalar pair certificates collapse to signed support one; out-of-band gain requires a new counting carrier

**Evidence level:** supported by ANF-003--ANF-005 and the exact out-of-band obstructions ANF-010--ANF-011

## Core intuition

Finite enrichment does not create new pair information when all channels are ultimately compressed into one translation-invariant scalar affine counting functional. ANF-003--ANF-005 reduce that category to one signed support-one profile plus an explicit normalization slack. The newer all-frequency audit sharpens the boundary: the unconditional pair-correlation input has a useful nonnegative tail outside support one, but **no universal scalar affine pair-count certificate can exploit that tail by becoming negative there**.

The surviving out-of-band route must therefore change the zero-side carrier before scalar affine compression: matrix/inertia structure, a zeta-specific inequality, higher-order data, or another non-affine configuration functional.

## Strongest justified principle

ANF-003 shows that common-translation vector features become one scalar Gram kernel after the common character is integrated out. ANF-004 extends this to finite convex families of already-global pair moments: affine separation yields one signed scalar dual witness. ANF-005 then exposes the unavoidable slack. For a universal certificate

`simple-real count >= A N - sum F(z-s)`,

small configurations force `delta=1+F(0)-A >= 0`, lower bounds on real and imaginary translates, and copositivity constraints. At zero slack one returns to the classical termwise-nonnegative Montgomery--Taylor class.

ANF-010 observes that the unconditional BGSST form factor is nonnegative for all real frequencies, so a negative Fourier tail beyond `|alpha|=1` would be analytically favorable if a compatible zero-side certificate existed. Positive scalar Gram kernels cannot do this by Bochner.

ANF-011 closes the broader universal affine scalar escape. If a Fourier--Laplace-admissible scalar profile is nonpositive outside support one with any nontrivial negative tail, its imaginary-axis continuation diverges negatively. A single conjugate pair, however, imposes a universal lower barrier on that same imaginary-axis response. The two requirements are incompatible. Hence the unconditional out-of-band positivity cannot be harvested by merely allowing an indefinite scalar affine pair kernel.

## What remains possible

The signed support-one extremal problem with positive slack remains open. So do carriers that preserve structure before the final scalarization: matrix-valued Hilbert inequalities, inertia/signature identities, ordered local blocks, genuine higher correlations, or source-specific nonlinear counting inequalities. The point is categorical, not that pair correlation has no more information.

Any proposed out-of-band improvement should first state which hypothesis of ANF-011 it leaves. If it remains universal, affine, scalar, translation invariant, and pairwise, the negative-tail escape is already closed.

## Status / novelty

Bochner positivity, Fourier support, affine duality, and entire Fourier--Laplace continuation are classical ingredients. The persisted synthesis is the exact information boundary: **global scalar pair enrichment stays inside a signed support-one affine class, and the unconditional out-of-band tail becomes usable only after leaving that class on the zero side**.

## Falsification criterion

Construct a universal affine scalar pair-count certificate satisfying the ANF-005 finite-configuration constraints and carrying a nontrivial negative out-of-band tail without violating the ANF-011 conjugate-pair barrier. A positive result outside those hypotheses would evade rather than falsify the intuition.

## Lean-formalizable core

- Affine scalarization of finitely many pair channels.
- Normalization-slack inequalities from finite configurations.
- Bochner obstruction for positive scalar Gram kernels.
- Imaginary-axis lower barrier from a conjugate pair.
- Incompatibility of a nontrivial negative out-of-band scalar tail with the universal affine certificate.
