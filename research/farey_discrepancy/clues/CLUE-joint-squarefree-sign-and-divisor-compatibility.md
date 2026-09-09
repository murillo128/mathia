---
id: CLUE-joint-squarefree-sign-and-divisor-compatibility
type: research-clue
status: proposed
origin: master-researcher
target_line: farey_discrepancy
based_on:
  - research/farey_discrepancy/findings/FD-005-mobius-total-sum-compatibility-still-does-not-improve-leading-dual-constant.md
  - research/farey_discrepancy/findings/FD-006-fixed-jordan-moment-hierarchy-does-not-improve-leading-dual-constant.md
  - research/farey_discrepancy/findings/FD-007-squarefree-ternary-increment-relaxation-does-not-improve-leading-dual-constant.md
---

# Does one exact divisor identity obstruct the squarefree-sign realization of the GCD extremizer?

## Observation

FD-006 leaves the leading Franel--Mertens coordinate constant unchanged after imposing any fixed Jordan-moment hierarchy on a real-valued block-constant staircase. FD-007 obtains the same limiting constant after imposing the exact squarefree zero pattern and unit sign amplitudes on one discrete increment sequence, but its sign construction does not generally satisfy the actual divisor/Jordan identities.

The two constructions therefore concern different relaxations. Their separate negative conclusions do not prove a negative conclusion on their intersection. The smallest coupled test is not another moment on the old real relaxation: it is the exact total-sum identity imposed simultaneously with every squarefree sign constraint.

## Research question

Retain `K_N(d,e)=gcd(d,e)^2/(de)`. For an increment sequence `a`, set

\[
A_a(x)=\sum_{n\le x}a_n,\qquad
m_d(a)=A_a(\lfloor N/d\rfloor).
\]

Let `U_N^div` consist of sequences with `a_1=1`, `a_n=0` on nonsquarefree integers, `a_n in {-1,+1}` on squarefree integers, and the additional exact constraint

\[
\sum_{d=1}^N m_d(a)=1.
\]

The actual Mobius sequence belongs to this class. At the same fixed horizon, interchange the finite sums to express the extra constraint equivalently as

\[
\sum_{n\le N}a_n\lfloor N/n\rfloor=1.
\]

Does the coupled sharp constant

\[
\Theta_N^{\mathrm{div}}
=\max_{a\in U_N^{\mathrm{div}}}
\frac{m_1(a)^2}{m(a)^TK_Nm(a)}
\]

still tend to `zeta(2)`, or does this coupling produce a persistent improvement? The first test uses this single identity at one horizon, not a growing hierarchy or an assumed asymptotic cancellation law.

## Why it may matter

FD-007 shows that support and amplitude alone can realize a growing principal-block GCD extremizer with negligible relative energy error. FD-006 shows that finitely many moment constraints cost little in a continuous relaxation. What neither establishes is whether the moment correction is realizable by the same discrete signs while preserving the small energy error.

This tests an interaction between exact arithmetic constraints rather than independently adding further restrictions already known to be insufficient. Saturation of the coupled class would close a genuinely stronger relaxation. A uniform gap would identify a concrete compatibility effect, although an improvement of a scalar constant alone would still not improve the Mertens exponent or prove RH.

## Decisive test

Reconstruct the FD-007 witness with `R=floor(N^(1/5))`, `u^(R)=K_R^(-1)e_1`, amplification `t_N` of order `N^(3/5)`, and the induced staircase `m=t_N(u^(R),0)+z` with `||z||_(K_N)=O(sqrt N)`. Compute its divisor-identity defect exactly before attempting any correction.

Try to correct that defect by balanced sign changes on actual squarefree positions, preserving `a_1=1`, every required unit amplitude, and parity of the relevant block totals. To retain the saturation argument, a sufficient repair must have both

\[
\|\delta m\|_{K_N}=o(t_N),\qquad
|\delta m_1|=o(t_N).
\]

These are targets to establish, not a claim that a repair exists. Sign permutations preserving every hyperbola-block total cannot change the divisor identity, because `floor(N/n)` is constant on each such block. Any successful repair must account for changes of those totals and their induced cumulative energy. The real inverse-Gram projection behind FD-006 may suggest a direction but does not itself provide an integer sign realization.

If the original witness cannot be repaired, that alone is not an obstruction theorem. Either construct a different exactly feasible near-extremal family, or prove a constrained upper certificate with a nonvanishing gap from `zeta(2)` on a stated asymptotic range. Exact small-horizon enumeration or certified discrete optimization can distinguish plausible mechanisms, but finite numerical gaps and failure of an optimizer are not uniform bounds. Keep any corrected witness feasible before evaluating its quotient; a rounded real-valued projection is not sufficient evidence.

Do not impose the divisor identity at every smaller horizon merely to obtain uniqueness: the full prefix family reconstructs the Mobius increments by divisor inversion and risks replacing the proposed relaxation by the original source without a cheaper estimate. Likewise, witnesses may depend on `N`, as in FD-007; such a family disproves a uniform bound on this relaxation but does not identify the actual Mertens staircase with an extremizer.

Compare the resulting question and proof with the existing FD-005--FD-007 statements before promoting an outcome. If saturation is established, state exactly that the joint sign-plus-single-identity relaxation remains sharp. If a gap survives, state its size and derive its actual consequence in the unchanged Franel normalization before claiming relevance beyond a constant improvement. The existing ordered-gap and Plucker clues concern different observables and remain separate.

## Evidence boundary

Sources were inspected through `8d3ded047405f07aa10140dd7baa7c036faa293b`; check their current claim and review state before use. No joint saturation construction, uniform gap, finite optimization, or improved estimate for the true Mobius sequence is supplied here. FD-006 and FD-007 must not be combined by intersection without this missing feasibility argument. Failure to construct a repair is not a refutation, and an exact feasible synthetic sign assignment is a control for this relaxation, not a counterexample to RH.
