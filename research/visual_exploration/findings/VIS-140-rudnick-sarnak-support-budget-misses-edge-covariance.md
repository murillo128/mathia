# VIS-140 — Rudnick–Sarnak restricted support does not reach the support-edge four-level covariance

## Claim

The four-level correlation theorem of Rudnick and Sarnak does **not directly control** the disjoint-window support-edge covariance isolated in `VIS-139`.

For the Riemann zeta function (`m=1`), Rudnick–Sarnak Theorem 1.1 proves the GUE `n`-level asymptotic for translation-invariant tests whose Fourier transform is supported in

`sum_j |xi_j| < 2`.

A pair statistic at relative Fourier frequency `q` lives on the two-coordinate plane

`(xi_1,xi_2)=(q,-q)`.

The product of two disjoint pair statistics at frequencies `q` and `r`, which is exactly the four-level sector entering the covariance in `VIS-139`, lives on

`(xi_1,xi_2,xi_3,xi_4)=(q,-q,r,-r)`.

Restricting the Rudnick–Sarnak support condition to this pair-pair plane gives the exact budget

`2|q|+2|r| < 2`,

equivalently

`|q|+|r| < 1`.

The frozen Montgomery support-edge statistic from `VIS-123` is centered at `q≈1`. Two edge factors are therefore centered near `(q,r)≈(1,1)`, where the four-level Fourier `l1` mass is approximately `4`, while the Rudnick–Sarnak theorem only covers mass strictly below `2`. Even the idealized point `(q,r)=(1,0)` lies on the strict boundary rather than inside the theorem's support region.

Hence the classical restricted-support `n`-level theorem cannot be used as the missing four-level closure for the exact support-edge experiment merely by citing “Rudnick–Sarnak higher correlations.” Reaching this statistic requires additional information beyond that theorem: an extension to substantially larger support, a direct covariance/mixing argument for the frozen observable, or a redesigned statistic whose relevant Fourier mass lies inside the admitted region.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-BOUNDED NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This is an applicability obstruction, not a theorem that the desired four-level covariance law is false.

## 1. Exact support reduction on the pair-pair plane

Let a translation-invariant two-point test be represented in relative frequency by `q`. In four variables, a product of two disjoint pair tests has Fourier variables

`xi(q,r)=(q,-q,r,-r)`.

The zero-sum constraint is automatic:

`q-q+r-r=0`.

Its Fourier `l1` norm is exactly

`||xi(q,r)||_1 = |q|+|-q|+|r|+|-r|`
`                  = 2|q|+2|r|`.

Symmetrizing the pair-pair test to meet the usual `n`-level symmetry convention only permutes these four coordinates, so it does not change this `l1` support budget.

Rudnick and Sarnak prove their zeta `n`-level asymptotic for test functions whose Fourier support is contained in

`||xi||_1<2`.

Therefore the part of their theorem lying on the pair-pair plane is precisely the open diamond

`|q|+|r|<1`.

No probabilistic approximation or asymptotic estimate is used in this reduction; it is just the exact restriction of the published support hypothesis.

## 2. The frozen edge packet sits outside that diamond

`VIS-123` fixes the local form-factor coordinate so that the Montgomery/CUE support edge occurs at `q=1`. The thread `VIS-124`--`VIS-130` then keeps that edge location while accounting for the admitted pair weighting and source-window smoothing.

Thus the covariance of two copies of the frozen edge statistic naturally probes the pair-pair sector near

`(q,r)=(1,1)`.

At that point,

`2|q|+2|r|=4`,

twice the Rudnick–Sarnak total-support threshold. This is not a marginal endpoint issue that could be repaired by replacing a strict inequality with a closed one: the target is separated from the admitted diamond by an order-one support gap.

## 3. The bounded tent does not rescue compact support

`VIS-128` gives the exact normalized spectral kernel of the fixed physical tent source taper,

`Q_M^tent(u)=(3M/4) sinc^4(Mu/2)`.

It has polynomial tails and therefore is not compactly supported. Composing that taper with the support-edge test broadens the edge packet; it does not move the main edge coordinate from `q≈1` into `|q|<1/2`.

Consequently the exact frozen statistic is even farther from the literal compact-support hypothesis than an idealized monochromatic edge mode. One may of course introduce an auxiliary compact spectral truncation, but to invoke Rudnick–Sarnak that truncation would have to place the complete four-level Fourier support inside `|q|+|r|<1`. A truncation doing that cannot simply discard negligible far tails while retaining a packet centered near `(1,1)`.

Any proposal to replace the actual kernel by an admissible compactly supported one therefore needs a **new quantitative approximation theorem** showing that the discarded edge-centered contribution is below the target `1/L` arithmetic scale. The restricted-support theorem itself supplies no such approximation.

## 4. Prior art and theorem boundary

The classical source is:

- Zeév Rudnick and Peter Sarnak, **Zeros of principal L-functions and random matrix theory**, *Duke Mathematical Journal* 81:2 (1996), 269–322, DOI `10.1215/S0012-7094-96-08115-6`. Their Theorem 1.1 assumes `sum_j |xi_j|<2/m`; for zeta, `m=1`, hence total support below `2`. Their remarks explicitly describe the support restriction and conjecture full universality beyond it.

This finding does not claim a new higher-correlation theorem. Its Mathia-specific content is the exact pullback of the classical Rudnick–Sarnak support polytope onto the pair-pair Fourier plane consumed by `VIS-139`.

There is also conjectural machinery beyond the restricted-support theorem:

- J. B. Conrey and N. C. Snaith, **Correlations of eigenvalues and Riemann zeros**, arXiv:`0803.2795` (2008), derives arbitrary-order zeta correlation formulae assuming the Ratios Conjecture.
- J. B. Conrey and N. C. Snaith, **In support of n-correlation**, arXiv:`1212.5537` (2012), develops an arbitrary-support random-matrix representation designed to expose which terms survive support restrictions.

These works show that “larger/arbitrary support” is a meaningful higher-correlation direction, but the zeta formula in the 2008 route is Ratios-Conjecture-based. It therefore cannot be silently substituted for the unconditional/rigorous four-level covariance gate in the accepted support-edge clue.

A bounded search for a later unconditional theorem directly covering this exact four-level edge packet did not identify one. That search is not an exhaustive nonexistence claim; the durable obstruction here is specifically that the classical Rudnick–Sarnak theorem itself does not cover the frozen kernel.

## 5. Secondary localization mismatch

Rudnick–Sarnak's theorem is formulated with smooth height localization on the natural large-`T` scale. The current Mathia statistic uses separated bounded physical source windows whose unfolded width is `Theta(log T)` and then asks for their cross-height covariance.

Even if the relative Fourier support were moved into the admissible diamond, applying the classical theorem to this shrinking-relative-height, two-window covariance geometry would still require a localization/transfer argument uniform in the `L`-dependent family. This is secondary to the support obstruction above but prevents treating support admissibility alone as a complete covariance theorem.

## Boundary and falsification

This finding does **not** prove that four-level zeta information is inaccessible, that GUE four-level statistics fail at the edge, or that the accepted support-edge clue is false. Rudnick and Sarnak themselves conjecture the unrestricted-support universality that would remove this particular theorem-applicability obstruction.

The result is also specific to the frozen support-edge frequency. A different statistic whose pair frequencies satisfy `|q|+|r|<1` could fall within the classical support budget, subject to its own localization and quantitative-uniformity requirements. Such a redesign would have to demonstrate that it still carries the arithmetic signal the edge statistic was introduced to isolate.

The obstruction is falsified as an operational gate if one supplies either:

1. an unconditional higher-correlation theorem covering the exact `L`-dependent pair-pair kernel and bounded source-window geometry used here; or
2. a rigorous reduction of the frozen covariance to an admissible restricted-support test with error `o(1/L)` (or below the finally predeclared arithmetic amplitude).

A conjectural ratios formula may be useful for prediction or experiment design, but it must remain labelled conjectural and cannot satisfy this rigorous gate by itself.

## Research consequence

`VIS-139` made the missing covariance a four-level problem. The present result kills the most immediate classical shortcut: **the standard Rudnick–Sarnak `n`-level theorem does not reach the support-edge four-level sector**.

The accepted support-edge program therefore has a cleaner fork. Either derive a direct cross-height covariance/mixing theorem for the exact frozen statistic, obtain genuinely wider-support four-level zeta information with the required uniform localization, or deliberately redesign the statistic inside the restricted-support diamond and then re-establish that the redesigned observable still has a relevant arithmetic `1/L` target.

No fresh confirmation-zero data is needed for this conclusion.
