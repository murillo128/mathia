# PL-245 — Affine imaginary-root corrections are one-variable Weyl-invariant freedom, not automatic mixed-variable rigidity

## Claim

`PL-244` left affine/imaginary-root corrections open as a possible escape from the separable rank-one zeta factors seen in finite higher-rank Weyl-group multiple Dirichlet-series residues. Classical affine WMDS theory and the recent Kac–Moody decomposition theorem show that this escape is much narrower than it first appears.

For an irreducible affine root system with minimal positive imaginary root `delta`, the Weyl group fixes the null-root direction. Consequently the functional equations leave precisely a one-dimensional family of undetermined data along multiples of `delta`. In the untwisted case the affine solution has the form

`Z(x) = C(x^delta) Z_0(x)`

with `C` a one-variable power series. Whitehead proved the corresponding statement earlier in his affine construction: the functional equations determine the series only up to multiplication by a power series in the invariant monomial `x^alpha_0`, where `alpha_0` is the minimal imaginary root.

Thus **affine Weyl symmetry by itself does not turn the imaginary-root correction into a source-forced nonseparable coupling among the root variables**. It leaves scalar boundary data in the single null-root coordinate. Extra arithmetic/local-global axioms or additional functional equations can and do select this factor in important examples, but the selection is extra input rather than a consequence of the Weyl functional equations.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE-BOUNDARY + NO-NOVELTY-CLAIM`. This is decisive against treating the mere existence of affine imaginary-root correction factors as the missing coupling left open by `PL-244`. It does not rule out a canonically selected correction factor carrying useful arithmetic information, nor non-polar/operator constructions acting before the scalar null-root factorization.

## Exact affine freedom

Whitehead's coefficient recursions for affine Weyl-group multiple Dirichlet series reduce every non-diagonal coefficient to the diagonal family

`c_(m alpha_0),   m >= 0`,

where `alpha_0` is the minimal imaginary root. Since `alpha_0` is Weyl invariant, the monomial `x^alpha_0` is invariant under every simple reflection. Whitehead therefore obtains the exact corollary that a series satisfying the affine functional equations is determined only up to multiplication by an arbitrary power series in `x^alpha_0`.

This is not merely a peculiarity of one affine type. Popa–Walsh's 2026 decomposition theorem for symmetrizable Kac–Moody root systems identifies the same mechanism representation-theoretically. In the untwisted case, the coefficients not recursively forced by the Chinta–Gunnells invariance lie on representatives of imaginary-root Weyl orbits. For an irreducible affine root system these representatives are exactly

`{ n delta : n >= 1 }`.

Their affine specialization is stated explicitly as

`Z(x) = C(x^delta) Z_0(x)`,

with `C` a power series in one variable. In finite type the corresponding invariant freedom collapses to constants; the one-variable correction is therefore genuinely affine, but it is still only the null-root coordinate rather than a new mixed-variable object.

## Why this does not yet produce RH rigidity

Write the affine null root as

`delta = sum_i d_i alpha_i`.

Under the usual Dirichlet-series change of variables `x_i=q^(-s_i)`, its invariant monomial is

`x^delta = q^(-delta(s))`,

where

`delta(s)=sum_i d_i s_i`.

Hence the correction becomes the scalar factor `C(q^(-delta(s)))`. On any one-parameter specialization `s_i=a_i s+b_i`, it is still only a one-variable meromorphic factor in the affine-linear parameter `sum_i d_i(a_i s+b_i)`.

This matters for the `prime_lattice` target because an arbitrary choice of `C` can place zeros or poles wherever that one-variable freedom permits. Such a divisor is not a localization mechanism unless independent arithmetic structure forces `C`. If one were to choose `C` after inspecting a desired zeta divisor, this would be exactly the kind of arbitrary re-encoding excluded by the research mandate.

The result therefore parallels the separability control in `PL-244`, but for a different reason. In the finite residue theorem, a lower-rank arithmetic WMDS survives as a multiplicative factor separate from rank-one zeta factors. In the affine setting, Weyl invariance itself leaves an undetermined factor supported on the one-dimensional null-root lattice. Neither situation supplies, by symmetry alone, a cross-factor positivity or self-adjointness law capable of forcing a Riemann divisor to its critical line.

## The selector is real additional structure

The negative conclusion must not be overstated. Whitehead's construction does not leave the diagonal coefficients arbitrary after all of his axioms are imposed: he emphasizes that the additional dominance and local-global axioms are needed to determine them canonically. His affine series can exhibit poles associated with imaginary roots, so the null-root sector is mathematically substantive rather than disposable normalization.

Popa–Walsh likewise show in the affine `A_1~` case that an **extra functional equation not generated by the Weyl group**, together with a specialization where the average is explicitly known, determines the one-variable normalization factor. They describe the determination of this factor as a recurring and subtle affine problem, analogous to the imaginary-root correction in Macdonald's affine denominator formula.

So the surviving question is not whether an affine correction exists. Prior art answers that decisively. The useful question is whether an independently forced selector for `C` supplies a rigidity principle stronger than the scalar factor it selects: for example a positivity law, operator relation, or target-relative coupling that constrains the same divisor used to represent ordinary zeta zeros.

## Analytic-continuation control

No Euler product is being continued formally here. Popa–Walsh prove analytic continuation of the relevant Chinta–Gunnells averages to the interior of the complexified Tits cone and formulate the decomposition at the level of invariant analytic functions. Their discussion of the affine normalization and extra functional equations is inside that established analytic framework.

Whitehead's affine construction separately proves meromorphic continuation in its stated domain from the axiomatic coefficient system. The conclusion stored here concerns the algebraic/analytic indeterminacy left by the functional equations; it does not identify `C` with an Euler product outside a convergence half-space.

## Adversarial controls

**One-variable does not mean rank one.** Affine root systems can have high rank. The collapse occurs because the Weyl-invariant imaginary-root lattice is generated by the single null root `delta`, not because the ambient root system has only one coordinate.

**The correction factor may contain deep arithmetic.** The statement is not that `C` is trivial or uninteresting. The claim is that its arithmetic content is not forced by Weyl invariance alone. Whitehead's extra axioms and the Popa–Walsh extra functional equations are explicit matched controls showing that additional input can select it.

**A selected scalar factor can still have a complicated divisor.** Complexity of that divisor is insufficient for RH relevance. The line's publication gate requires a mechanism explaining why the divisor is constrained, not merely a construction in which a one-variable factor can carry it.

**This does not close affine WMDS as a whole.** Non-polar periods, quotients, matrix-valued observables, twisted local-global selectors, or operators acting on the full multivariable object before null-root scalarization remain logically open. What is closed is the weaker proposal that the presence of imaginary-root corrections itself supplies the nonseparable coupling absent from `PL-244`.

## Prior-art and novelty audit

The one-variable affine freedom is explicit prior art. Ian Whitehead, *Multiple Dirichlet Series for Affine Weyl Groups*, arXiv:1406.0573 (2014), proves that affine functional equations determine the series up to a power series in the invariant imaginary-root monomial; see Proposition 3.1.2 and Corollary 3.1.3 in the arXiv version. His later type-`A~` construction was published as “Affine Weyl group multiple Dirichlet series: type `A~`,” *Compositio Mathematica* **152** (2016), 2503–2523, DOI `10.1112/S0010437X16007715`, arXiv:1408.0937.

Alexandru A. Popa and Jack Walsh, “A decomposition of Weyl group multiple Dirichlet series for symmetrizable Kac-Moody root systems,” arXiv:2607.11834v1 (13 July 2026), gives the modern general decomposition. In the introduction and §4.3–4.4 they identify the imaginary-root freedom and state in the affine untwisted case `Z(x)=C(x^delta)Z_0(x)`. Their §6 shows in `A_1~` how an extra functional equation and a special-value input determine the remaining one-variable normalization.

A local audit against `PL-243` and `PL-244` finds no duplication. `PL-243` closes the three polar faces of a finite rank-two model. `PL-244` proves separability of a nontrivial lower-rank residue in finite higher rank and explicitly leaves affine/imaginary-root corrections open. The present finding resolves only that named caveat at the level of Weyl-functional-equation freedom and therefore narrows, rather than repeats, the existing line.

## Research implication

Do not treat “go affine so imaginary roots add correction factors” as a sufficient escape from the separability obstruction. The affine functional equations already tell us the shape of the missing data: it lies on the one-dimensional null-root coordinate and must be selected by structure external to ordinary Weyl invariance.

The live affine target is consequently stricter: identify a **canonical arithmetic selector** for the null-root factor and then prove that the selector creates an RH-relevant constraint that is not reducible to inserting another one-variable scalar divisor. Without that second step, affine correction factors reproduce analytic freedom rather than explain critical-line localization.
