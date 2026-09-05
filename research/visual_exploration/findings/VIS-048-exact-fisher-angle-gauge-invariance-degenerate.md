# VIS-048 — exact Fisher-angle invariance under any nontrivial gauge neighborhood is degenerate

## Claim

Let `Omega` be a fixed finite support and let `A,B` be fixed nonzero real residual tensors. For every strictly positive probability gauge `G` on `Omega`, define

`<A,B>_G = sum_x A_x B_x / G_x`

and the Fisher-angle coefficient

`kappa_G(A,B) = <A,B>_G / (||A||_G ||B||_G)`.

Fix one strictly positive baseline gauge `H` and any `omega>0`, and let

`F_omega(H) = { G : osc_x log(H_x/G_x) <= omega }`.

Then `kappa_G(A,B)` is exactly constant for every `G in F_omega(H)` if and only if one of the following two degenerate cases holds:

1. `A=lambda B` for some nonzero real scalar `lambda`; then `kappa_G=sign(lambda)` for every positive gauge;
2. `A_x B_x=0` for every cell `x`; then `kappa_G=0` for every positive gauge.

Therefore exact Fisher-angle invariance on **any nontrivial bounded gauge neighborhood already forces global invariance over all positive diagonal gauges**, and the only globally invariant angles are `0` from cellwise-disjoint support and `0` or `pi` from proportional residuals.

Equivalently, if the residuals overlap in at least one cell and are not globally proportional, then every positive baseline gauge has arbitrarily nearby positive gauge perturbations that change the Fisher angle.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION CONTROL + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

No claim is made that a scientifically reasonable gauge family should be unrestricted, that approximate angle stability is impossible, or that finite empirical agreement across several gauges implies either degeneracy. The statement concerns exact mathematical invariance over a genuine neighborhood.

## 1. Positive probability gauges realize an open projective weight neighborhood

Write

`a_x=A_x/sqrt(H_x)`,

`b_x=B_x/sqrt(H_x)`.

For a positive gauge `G`, put

`r_x=H_x/G_x`.

Then

`kappa_G = [sum_x a_x b_x r_x] / sqrt([sum_x a_x^2 r_x][sum_x b_x^2 r_x])`.

Multiplying every `r_x` by the same positive constant cancels from this quotient. Conversely, every positive projective weight ray is realized by a probability gauge: for any positive vector `u`, define

`Z=sum_x H_x/u_x`,

`G_x=(H_x/u_x)/Z`.

Then `G` is a positive probability law and

`H_x/G_x = Z u_x`.

Thus the Fisher angle depends only on the projective class of the positive reweighting vector. The family `F_omega(H)` contains an open projective neighborhood of the constant ray `r_x=1` whenever `omega>0`.

## 2. Constancy on one neighborhood gives a polynomial identity

Suppose `kappa_G=c` throughout `F_omega(H)`. On the corresponding open projective neighborhood define

`N(r)=sum_x a_x b_x r_x`,

`Q_A(r)=sum_x a_x^2 r_x`,

`Q_B(r)=sum_x b_x^2 r_x`.

Then

`N(r)^2 = c^2 Q_A(r) Q_B(r)`

throughout that open set. Both sides are homogeneous quadratic polynomials in the coordinates `r_x`. After fixing any projective normalization, their difference is a polynomial vanishing on an open set, hence the homogeneous identity holds coefficientwise.

If `c=0`, then `N(r)=0` on an open set. Since `N` is linear, every coefficient must vanish:

`a_x b_x=0` for every `x`.

Because `H_x>0`, this is exactly

`A_x B_x=0` for every `x`.

So the two residual tensors have no cell in which both are nonzero, and their Fisher numerator is identically zero for every positive gauge.

Now suppose `c!=0`. Then some cell has `a_x b_x!=0`. Comparing the coefficient of `r_x^2` in the quadratic identity gives

`(a_x b_x)^2 = c^2 a_x^2 b_x^2`,

hence

`c^2=1`.

In particular the baseline gauge `H` satisfies equality in Cauchy-Schwarz:

`|<A,B>_H| = ||A||_H ||B||_H`.

The weighted vectors `(A_x/sqrt(H_x))_x` and `(B_x/sqrt(H_x))_x` must therefore be proportional, so

`A=lambda B`

for one nonzero real scalar `lambda`. Its sign is the constant value of `kappa_G`.

This proves necessity.

## 3. The two cases are sufficient and globally invariant

If `A=lambda B`, then for every positive gauge

`<A,B>_G=lambda ||B||_G^2`,

`||A||_G=|lambda| ||B||_G`,

so

`kappa_G=sign(lambda)`.

If instead `A_xB_x=0` cellwise, then

`<A,B>_G=0`

for every positive gauge while both norms remain positive, giving `kappa_G=0`.

Thus a local exact invariance assumption already yields one of two configurations that are invariant under the entire positive diagonal gauge family.

When both residual tensors are nonzero in every retained cell, the disjoint-support alternative is impossible. In that common full-support regime, **exact gauge-independent Fisher angle is equivalent simply to global proportionality**.

## 4. Relation to VIS-045, VIS-046, and VIS-047

`VIS-045` gives a sharp generalized-Wielandt bound on how much an angle can move when two positive gauges have bounded likelihood-ratio spread. That is a quantitative stability result, not an invariance theorem.

`VIS-046` classifies the much weaker property that the **sign** of the Fisher angle is invariant over all positive diagonal gauges: coordinatewise agreement or opposition of `A_xB_x` is enough even when the angle magnitude changes drastically.

`VIS-047` then gives the exact sign criterion inside a finite log-ratio-oscillation ball by comparing the positive and negative cross-masses.

The present result closes the corresponding exact **full-angle** question. Preserving an entire angle value is far more rigid than preserving orientation. Except for proportional or disjoint-support residuals, there is no exact representation-independent Fisher angle waiting to be recovered by choosing a sufficiently natural positive gauge.

## 5. Prior-art and novelty boundary

The closest specialized source already anchored in `research/visual_exploration/SOURCES.md` is Lin and Sinnamon's generalized Wielandt inequality, which gives sharp angle distortion between inner products and equality information under norm comparison. A targeted check of weighted-cosine, positive diagonal reweighting, and angle-invariance formulations found no reason to claim a new general theorem here.

The proof above uses only projective positive reweighting, a polynomial identity on an open set, and the ordinary equality case of Cauchy-Schwarz. These are classical ingredients. The durable Mathia content is the exact specialization as a **representation-control obstruction** for the active common-gauge residual-direction program; no novelty is claimed for the underlying linear-algebra facts.

## 6. Boundary conditions and falsification

The support and residual tensors must remain fixed while the gauge changes. Rebinning, deleting cells, recomputing a Markov closure, changing the residualization rule, or rotating each dataset into its own fitted coordinates changes the mathematical object and lies outside this theorem.

All gauges are strictly positive. Structural zeros in the gauge change the support and are not an infinitesimal or bounded positive-gauge perturbation.

The result is about exact constancy over all gauges in a neighborhood. It does **not** say that the derivative of the angle cannot vanish in one selected direction, that the angle cannot be numerically stable over a declared finite family, or that the quantitative envelopes in `VIS-045` and `VIS-047` are unnecessary.

Falsify the claim by exhibiting fixed nonzero `A,B`, a positive baseline `H`, and some `omega>0` such that `kappa_G` is exactly the same for every `G in F_omega(H)` while `A` is not proportional to `B` and some cell has `A_xB_x!=0`.

## Research consequence

A residual-direction comparison such as the accepted three-gap zeta/CUE program should not seek a supposedly canonical Fisher angle by testing whether several convenient gauges happen to agree. Outside the two degenerate configurations above, the exact angle is inherently gauge-dependent even locally.

The correct control is therefore the one already suggested by the recent findings: freeze a scientifically justified common gauge before inspecting the target comparison, then quantify sensitivity with `VIS-045` and orientation robustness with `VIS-047`. Agreement under that frozen representation can be meaningful; exact invariance under arbitrary positive reweighting is not a realistic nondegenerate target.
