---
id: CLUE-weil-inertia-cyclotomic-transversality-pairwise-rank
type: research-clue
status: resolved
origin: independent-review
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-081-pairwise-lcm-boundary-rank-controls-finite-window-ramanujan-leakage.md
  - research/weil_inertia/formalization/WI081PairwiseRamanujanRank.lean
---

# Does pairwise Ramanujan rank stay maximal until both Vandermonde blocks are overcomplete, with all residual defect controlled by cyclotomic transversality?

## Observation

The Lean formalization of WI-081 makes the nearest-boundary factorization more explicit than the canonical theorem statement. After cancellation of complete `lcm(m,n)` periods and, when necessary, passage to the translated complementary boundary, the cross Gram is, up to an overall sign and invertible diagonal phase factors, a product

\[
G_{m,n}^{(N)} \sim (V_m^{(\delta)})^*V_n^{(\delta)},
\qquad
\delta=\delta_N(m,n),
\]

where `V_m^(delta)` and `V_n^(delta)` are consecutive-sample Vandermonde matrices on the distinct primitive roots of orders `m` and `n`.

WI-081 and the public Lean theorem prove exact rank only under

\[
\delta\le\min\{\varphi(m),\varphi(n)\}.
\]

However, the formal proof separates the two ingredients as surjectivity of one truncated Vandermonde and injectivity of the adjoint of the other. This suggests that requiring both simultaneously may be stronger than necessary. Ordinary Vandermonde rank would instead give

\[
\operatorname{rank}V_m^{(\delta)}=\min\{\delta,\varphi(m)\}
\]

for every `delta`.

## Research question

Is the following stronger universal pairwise formula valid for all distinct positive moduli `m,n` whenever the nearest-boundary length has not exceeded both Ramanujan dimensions?

\[
\boxed{
\delta_N(m,n)\le\max\{\varphi(m),\varphi(n)\}
\Longrightarrow
\operatorname{rank}\bigl((U_m^{(N)})^*U_n^{(N)}\bigr)
=\min\{\delta_N(m,n),\varphi(m),\varphi(n)\}.
}
\]

If so, can every genuinely exceptional rank deficiency in the remaining regime

\[
\delta>\max\{\varphi(m),\varphi(n)\}
\]

be reformulated exactly as a failure of transversality between the two primitive-frequency Vandermonde subspaces, and then as a cyclotomic divisibility condition on a short polynomial?

More precisely, with `a=phi(m)<=b=phi(n)`, does

\[
\operatorname{rank}((V_m^{(\delta)})^*V_n^{(\delta)})
=a-\tau_{m,n}(\delta)
\]

hold with

\[
\tau_{m,n}(\delta)
:=
\dim\bigl(\operatorname{ran}V_n^{(\delta)}\cap(\operatorname{ran}V_m^{(\delta)})^\perp\bigr)-(b-a)\ge0,
\]

and can membership in `(ran V_m)^perp` be expressed, up to the harmless inversion/phase convention of the sampling matrix, by divisibility of

\[
F_f(X)=\sum_{x=0}^{\delta-1}f_xX^x
\]

by the cyclotomic polynomial `Phi_m`?

## Why it may matter

The strengthened rank formula would move the universal onset of possible pairwise rank deficiency from `delta > min(phi(m),phi(n))` to the substantially narrower regime where the boundary is larger than both Ramanujan spaces. For prime pairs, WI-081 already proves maximal rank on a larger region by a prime-specific residue-class argument, so the main new value would be a modulus-uniform theorem, especially for composite moduli.

The transversality formulation could also replace isolated low-rank examples by a quantitative defect invariant. In the WI-081 example `(p,q,delta)=(11,13,47)`, rank `8` instead of `10` would correspond to two dimensions of excess intersection beyond the dimension forced by ambient linear algebra. A cyclotomic formulation may expose arithmetic structure in those extra intersections that pairwise rank bookkeeping alone hides.

This would not by itself evade WI-082--WI-085's global scalar overcompleteness/aliasing obstructions, but it could identify a sharper source-sensitive object to test inside the only pairwise regime where exceptional dependencies are actually possible.

## Decisive test

First prove or refute the strengthened exact rank statement above without prime-specific hypotheses. A direct route is to establish the full Vandermonde rank identity `rank V_m^(delta)=min(delta,phi(m))`, then use surjectivity of one factor whenever `delta<=phi(n)` or injectivity of the other adjoint whenever `delta<=phi(m)`.

If that succeeds, enter only the complementary regime `delta>max(phi(m),phi(n))` and:

1. prove the exact intersection formula for the rank defect and isolate the nonnegative excess-transversality dimension `tau`;
2. prove the polynomial/cyclotomic equivalence carefully, including the conjugation, inversion, and translated-boundary phase conventions;
3. recover the known `(11,13,47)` rank-8 certificate as `tau=2`;
4. test composite-modulus examples computationally for whether nonzero `tau` correlates with a tractable arithmetic condition on `Phi_m`, `Phi_n`, or their short multiples;
5. perform a serious prior-art check on partial Fourier/Vandermonde subspace intersections, cyclotomic divisibility, and Ramanujan subspace rank before making any novelty claim.

A counterexample to the `delta<=max(phi(m),phi(n))` rank formula kills the first part. If the intersection identity is tautologically correct but the cyclotomic representation yields no sharper constraint than arbitrary subspace geometry, then the second part should be treated as an unproductive reparameterization rather than a new mechanism.

## Evidence boundary

The existing Lean artifact proves only the WI-081 boundary-rank upper bound and the small-boundary equality under `delta<=min(phi(m),phi(n))`; it does not prove the proposed `max` threshold, the full rectangular Vandermonde rank identity in the form needed here, the excess-transversality formula as a research invariant, or any cyclotomic classification of exceptional defects.

The proposed strengthening is motivated by reconstructing the formal proof's separate injectivity/surjectivity steps, not by an accepted new theorem. The cyclotomic viewpoint is likewise an unvalidated change of representation. No claim is made that either statement is novel, useful for the global zero-proportion bound, or sufficient to escape the scalar obstructions already established in WI-082--WI-085.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/weil_inertia/findings/WI-086-pairwise-ramanujan-rank-defect-starts-past-both-totient-dimensions]]

The proposed `delta<=max(phi(m),phi(n))` strengthening is exact. In the residual regime the rank defect is exactly the excess intersection dimension `tau`, and orthogonality to one primitive-frequency block is exactly cyclotomic divisibility of the coefficient polynomial. The cyclotomic representation itself is only a normal form for the same subspace geometry, so any further saving requires source-specific or genuinely additional structure.