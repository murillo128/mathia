# VIS-145 — a second-moment packet annihilates every smooth finite-window quadratic response, not only CUE

## Claim

Let `H(x)` be any real signed integrable correction kernel supported in `[-M,M]`. It may represent the difference between a source-specific finite-window pair statistic and its finite-CUE null after the same frozen taper, unfolding, diagonal subtraction, and coordinate conventions.

Define

`Delta_H(q)=integral_(-M)^M H(x)[1-cos(2*pi*q*x)]dx`,

`mu_2(H)=integral_(-M)^M x^2 H(x)dx`,

and

`M_4(H)=integral_(-M)^M x^4 |H(x)|dx`.

Then for every real `q`,

`|Delta_H(q)-2*pi^2*mu_2(H)q^2| <= (2/3)*pi^4*M_4(H)q^4`.

Consequently, for every finite signed frequency packet `nu_b` supported in `|q|<=b`, with

`m_2(nu_b)=integral q^2 dnu_b(q)`,

one has

`|integral Delta_H(q)dnu_b(q)-2*pi^2*mu_2(H)m_2(nu_b)|`
` <= (2/3)*pi^4*M_4(H) integral q^4 d|nu_b|(q)`.

In particular, if

`m_2(nu_b)=0`,

then

`|integral Delta_H(q)dnu_b(q)|`
` <= (2/3)*pi^4*M_4(H)b^4 ||nu_b||_TV`.

Thus the signed second-moment cancellation introduced in `VIS-144` is **not selective for the universal finite-CUE quadratic term**. It annihilates the quadratic low-frequency response of every source correction that enters through the same finite-window centered-cosine transform and has finite fourth absolute moment.

Applied conditionally to the zeta-minus-CUE correction in the support-safe companion problem, this rules out the hoped-for mechanism in which `m_2(nu_b)=0` kills the CUE `q^2` term while retaining a different zeta-specific `q^2` coefficient. Any arithmetic selectivity must instead survive in a quartic-or-higher response, in an `L`-dependent moment growth/nonuniformity that changes the shrinking-band balance, or through a different observable that is not merely the same centered finite-window cosine transform.

**Evidence/status:** `EXACT-DERIVED + GENERIC FOURIER-MOMENT OBSTRUCTION + NEGATIVE/REDESIGN CONTROL + NO-NOVELTY-CLAIM`.

No finite-height zeta arithmetic coefficient, covariance theorem, Rudnick–Sarnak uniformity statement, or RH implication is claimed.

## 1. The quadratic remainder bound does not use positivity

For every real `u`,

`u^2/2-u^4/24 <= 1-cos(u) <= u^2/2`.

Therefore

`|(1-cos(u))-u^2/2| <= u^4/24`.

Substitute `u=2*pi*q*x`. Pointwise,

`|(1-cos(2*pi*q*x))-2*pi^2 q^2 x^2|`
` <= (2/3)pi^4 q^4 x^4`.

Unlike `VIS-144`, the kernel `H` need not be nonnegative. Integrating against the signed kernel and taking absolute values only on the remainder gives

`|Delta_H(q)-2*pi^2 mu_2(H)q^2|`
` <= (2/3)pi^4 M_4(H)q^4`.

Compact support makes `M_4(H)` finite whenever `H` is integrable. More generally the same statement holds without compact support whenever the fourth absolute moment exists.

## 2. The packet moment condition cancels the quadratic response universally

Integrate the preceding decomposition against `nu_b` before taking absolute values:

`integral Delta_H(q)dnu_b(q)`
` = 2*pi^2 mu_2(H)m_2(nu_b) + R_H(nu_b)`,

with

`|R_H(nu_b)|`
` <= (2/3)pi^4 M_4(H) integral q^4 d|nu_b|(q)`.

Hence `m_2(nu_b)=0` removes the full quadratic term regardless of the value, sign, or arithmetic origin of `mu_2(H)`.

This is the decisive distinction missing from the interpretation at the end of `VIS-144`. A second-moment-null packet does not distinguish two smooth finite-window kernels by giving them different quadratic coefficients: it projects **all** quadratic coefficients to zero.

If `||nu_b||_TV=O(1)`, the surviving response is at most `O(M_4(H)b^4)`. If the packet total variation is allowed to grow, the exact factor `b^4||nu_b||_TV` must be carried through the same theorem, transfer, variance, and covariance accounting required elsewhere in the support-edge program.

## 3. Fixed-window analyticity closes a nonanalytic escape at each finite stage

Because `H` is integrable and supported in `[-M,M]`,

`q -> Delta_H(q)`

is an even entire function. Its Taylor coefficients are the even moments of `H`:

`Delta_H(q)`
` = 2*pi^2 mu_2(H)q^2 - (2/3)pi^4 mu_4(H)q^4 + ...`,

where `mu_4(H)=integral x^4H(x)dx`, with higher terms defined similarly.

Therefore a fixed finite source window cannot produce a genuine local `|q|`, `q^2 log|q|`, or other nonanalytic low-frequency term through this transform. Such behavior could only emerge after an `L`-dependent limit whose kernel moments are not uniform, or because the source-specific statistic is represented by a different object/distributional term than the frozen finite-window kernel assumed here.

That distinction matters for the shrinking-band regime. Nonuniform growth of `M_4(H_L)`, `M_6(H_L)`, and higher moments can make the formal `b_L^4`, `b_L^6`, ... hierarchy quantitatively nontrivial even though every finite-`L` response is analytic. It must be proved rather than inferred from the existence of arithmetic lower-order terms in an infinite-height formula.

## 4. Consequence for the zeta support-safe companion

Let `H_L` denote the **actual frozen finite-window zeta-minus-finite-CUE correction kernel**, if the pair statistic can be reduced to this common representation. Then the proposed condition

`integral q^2 dnu_(b_L)(q)=0`

necessarily cancels both the universal CUE quadratic response from `VIS-144` and the quadratic response of `H_L`.

The remaining arithmetic question is therefore narrower than the current clue formulation. A viable packet must show one of the following under one common `L`-dependent regime:

- a nonzero quartic-or-higher zeta-minus-CUE coefficient survives the packet and dominates finite-height/theorem and stochastic errors after its required normalization;
- the zeta correction has sufficiently different `L`-dependent moment growth that the post-cancellation residual remains detectable even though its local frequency order is at least four;
- the exact source-specific contribution is not representable by the same smooth finite-window centered-cosine kernel, with that representation failure proved rather than assumed;
- a different, nonlocal or asymmetric observable isolates arithmetic information without annihilating it by the same moment condition.

Merely showing that known finite-height pair-correlation formulas contain Euler products or other arithmetic lower-order terms is not enough. Those formulas establish a plausible source-specific carrier, but the carrier must be propagated through the exact frozen packet transform.

## 5. Stress tests and boundaries

The result concerns the deterministic mean functional only. It does not say that a moment-null packet reduces variance, cross-window covariance, theorem remainder, or transfer error.

The `O(b^4)` conclusion is uniform only to the extent that `M_4(H)` and `||nu_b||_TV` are controlled in the relevant family. If `H=H_L` changes with height/window scale, a growing fourth moment may offset shrinking bandwidth. That possibility is explicitly left open.

The result also does not identify the zeta-minus-CUE kernel `H_L` or prove that currently available finite-height pair-correlation formulas furnish it with the required uniformity. Establishing that dictionary is part of the remaining research problem.

No untouched confirmation-zero data are used.

## 6. Prior-art and novelty audit

The inequality is an elementary consequence of the classical Taylor remainder for cosine and finite signed-measure integration. Vanishing-moment filters annihilating low-order polynomial/Fourier-Taylor terms are standard harmonic-analysis and filter-design structure. No general novelty is claimed.

The Mathia-specific value is the obstruction created by composing that standard fact with the exact support-safe companion architecture of `VIS-141`--`VIS-144`: the second-moment-null redesign cannot be interpreted as a selective cancellation of only the CUE quadratic mode. It forces the zeta-specific search one order deeper, or into a genuinely different information carrier.

## Research consequence

The proposed moment-cancelled companion remains worth investigating, but its acceptance criterion changes. The next derivation should first express the finite-height zeta-minus-CUE contribution in the exact frozen finite-window frequency functional. After imposing `m_2=0`, it should compute or bound the first surviving packet term and its `L`-dependence.

A claimed arithmetic advantage at quadratic order is now closed. If the first usable arithmetic term is quartic, the natural bounded-total-variation signal scale is at most of order `M_4(H_L)b_L^4`; any normalization used to make it visible must be propagated through support-theorem error, finite-height transfer, variance, and cross-window covariance before confirmation data are inspected.