# PL-368 — Canonical Hardy `H^p` filters recover a universal `1/2` wall by Bohr–Bohnenblust–Hille geometry, not zeta rigidity

**Evidence:** `CLASSICAL-BAYART/BOHR-BOHNENBLUST-HILLE + EXACT-DERIVED + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-367`.

**Related findings:** `PL-001`, `PL-366`.

**Status:** `THE-CANONICAL-DIRICHLET-HARDY-SCALE-REMOVES-THE-ADJUSTABLE-ELLp-LADDER-BUT-STILL-PRODUCES-THE-RH-SHAPED-HALF-PLANE-FOR-EVERY-p-BY-GENERIC-HARDY/MONOMIAL-CONVERGENCE-GEOMETRY`.

## Precise claim

`PL-367` shows that if the divisor filter itself is placed in a coefficient space `ell^p`, then pole cancellation produces a whole adjustable ladder of ordinary-convergence walls

\[
\theta=1-\frac1p.
\]

That leaves a natural objection: perhaps `ell^p` is the wrong ambient scale, while the canonical Hardy spaces of Dirichlet series `\mathcal H^p` single out `1/2` in a structurally meaningful way.

They do single out `1/2`, but not in an RH-sensitive way.

Fix `1\le p\le\infty` and let

\[
C(s)=\sum_{d\ge1}c_dd^{-s}\in\mathcal H^p.
\tag{PL368-1}
\]

Classical Bohr--Bohnenblust--Hille theory, together with Bayart's extension to finite `p`, gives

\[
\boxed{
\sum_{d\ge1}|c_d|d^{-\sigma}<\infty
\qquad(\sigma>1/2).
}
\tag{PL368-2}
\]

The exponent is class-sharp: the supremum of the absolute-convergence abscissas over scalar `\mathcal H^p` is `1/2` for every `1\le p\le\infty`.

Now define the same divisor filter as in `PL-365`--`PL-367`,

\[
b=c*\mathbf 1,
\qquad
b_n=\sum_{d\mid n}c_d,
\tag{PL368-3}
\]

and impose only the scalar pole-neutrality condition

\[
C(1)=\sum_{d\ge1}\frac{c_d}{d}=0.
\tag{PL368-4}
\]

Then, for every `epsilon>0`,

\[
\boxed{
\sum_{n\le x}b_n
=O_{C,\epsilon}\!\left(x^{1/2+\epsilon}\right).
}
\tag{PL368-5}
\]

Consequently the ordinary Dirichlet series

\[
B(s)=\sum_{n\ge1}b_nn^{-s}
\tag{PL368-6}
\]

converges locally uniformly throughout `Re(s)>1/2`. On that half-plane,

\[
\boxed{
B(s)=\zeta(s)C(s),
}
\tag{PL368-7}
\]

with the singularity at `s=1` removed by (PL368-4). Thus a hypothetical zeta zero `rho` with `Re(rho)>1/2` is simply inherited by `B(rho)=0`; the construction supplies no restriction on the zero divisor.

The important negative control is stronger than the `ell^p` ladder. In the canonical scalar Hardy scale, the same `1/2` occurs for **every** `p`. In the vector-valued theory the corresponding absolute-convergence wall becomes

\[
1-\frac1{\operatorname{Cot}(X)},
\tag{PL368-8}
\]

where `Cot(X)` is the optimal cotype exponent of the coefficient Banach space. The scalar value `1/2` is therefore the cotype-`2` case of a general Banach-space phenomenon. It is not selected by the Riemann zeta zero set.

## 1. Classical Hardy input: absolute convergence beyond `1/2`

Bayart introduced the scalar spaces `\mathcal H^p` through the Bohr transform / vertical mean norm. The classical `p=\infty` Bohr--Bohnenblust--Hille theorem says that every bounded Dirichlet series is absolutely convergent for `Re(s)>1/2`, and the bound is optimal at the level of the class.

Bayart proved the same scalar abscissa for every finite `1\le p<\infty`. Carando--Defant--Sevilla-Peris record this explicitly and prove the vector-valued extension: for a Banach space `X`, the supremum of absolute-convergence abscissas over `\mathcal H^p(X)` is

\[
1-\frac1{\operatorname{Cot}(X)}
\]

for every `1\le p<\infty`; the `p=\infty` vector-valued version was already known. Taking `X=\mathbb C`, whose optimal cotype is `2`, gives (PL368-2) with the same `1/2` for the entire scalar Hardy scale.

This input is strictly stronger than the point-evaluation boundary recorded in `PL-001`: it controls the weighted `ell^1` norm of the Dirichlet coefficients, not merely continuity of evaluation along the Bohr curve.

## 2. Pole cancellation plus Hardy absolute convergence gives the RH-shaped summatory bound

Let

\[
S_b(x)=\sum_{n\le x}b_n.
\]

Finite divisor rearrangement gives

\[
S_b(x)=\sum_{d\le x}c_d\left\lfloor\frac{x}{d}\right\rfloor.
\tag{PL368-9}
\]

Because (PL368-2) in particular makes `C(1)` absolutely meaningful, (PL368-4) yields the exact residual identity

\[
S_b(x)
=
\sum_{d\le x}c_d
\left(\left\lfloor\frac{x}{d}\right\rfloor-\frac{x}{d}\right)
-
x\sum_{d>x}\frac{c_d}{d}.
\tag{PL368-10}
\]

Fix

\[
\frac12<\sigma<1,
\qquad
A_\sigma(C)=\sum_{d\ge1}|c_d|d^{-\sigma}<\infty.
\tag{PL368-11}
\]

For the first term in (PL368-10),

\[
\sum_{d\le x}|c_d|
\le
x^\sigma A_\sigma(C).
\tag{PL368-12}
\]

For the tail, since `d^{\sigma-1}\le x^{\sigma-1}` when `d>x`,

\[
\begin{aligned}
x\sum_{d>x}\frac{|c_d|}{d}
&=
x\sum_{d>x}|c_d|d^{-\sigma}d^{\sigma-1}\\
&\le
x^\sigma A_\sigma(C).
\end{aligned}
\tag{PL368-13}
\]

Therefore

\[
\boxed{
|S_b(x)|\le 2A_\sigma(C)x^\sigma
\qquad(1/2<\sigma<1).
}
\tag{PL368-14}
\]

Taking `sigma=1/2+epsilon` gives (PL368-5) for `0<epsilon<1/2`; larger `epsilon` are immediate. Abel summation then gives ordinary, locally uniform convergence of `B` on every compact subset of `Re(s)>1/2`.

Nothing in (PL368-10)--(PL368-14) uses multiplicativity of `c`, prime distribution, Mobius cancellation, the functional equation, or any information about zeta zeros. The `1/2` enters only through the generic coefficient theorem (PL368-2).

## 3. The continuation step is legitimate but zero-blind

For `Re(s)>1`, both factors are absolutely convergent and ordinary Dirichlet multiplication gives

\[
B(s)=\zeta(s)C(s).
\tag{PL368-15}
\]

Independently, Section 2 gives a holomorphic `B` on `Re(s)>1/2`, while (PL368-2) gives a holomorphic `C` there. Since `C(1)=0`, the simple pole of zeta at `1` is removable in `zeta(s)C(s)`. Hence the identity theorem extends (PL368-15) to the full half-plane `Re(s)>1/2`, proving (PL368-7).

This distinction matters: the extension is not obtained by formally continuing an Euler product or an absolutely convergent Dirichlet product. The two holomorphic functions are first identified in `Re(s)>1`, where multiplication is valid, and only then continued by uniqueness.

But that analytically valid continuation supplies no RH mechanism. If zeta had an off-line zero in this half-plane, multiplying by an arbitrary pole-neutral `C in \mathcal H^p` would preserve it. The Hardy hypothesis controls coefficient convergence, not the zero divisor of zeta.

## 4. Matched controls identify the wall as ambient Hardy/Banach geometry

There are three independent controls against interpreting (PL368-5) as arithmetic square-root cancellation.

First, the scalar `1/2` wall is independent of `p` across the whole canonical Hardy scale. This is the opposite behavior from the raw coefficient spaces of `PL-367`, but it remains universal rather than source-specific.

Second, evaluation at `s=1` is continuous in the scalar Hardy spaces by the standard infinite-polydisk evaluation theory already recorded in `PL-001`. Thus `C(1)=0` is only a closed codimension-one condition on a vast ambient class. It does not inject a functional equation, prime-power phase, explicit-formula sign, or any other zeta-specific rigidity.

Third, Carando--Defant--Sevilla-Peris show that changing the coefficient Banach geometry changes the Bohr absolute-convergence wall to (PL368-8). The same proof as Section 2 then gives, for `X`-valued `C in \mathcal H^p(X)` with `C(1)=0`,

\[
\left\|\sum_{n\le x}(c*\mathbf 1)(n)\right\|_X
=O_{C,\epsilon}
\left(x^{1-1/\operatorname{Cot}(X)+\epsilon}\right)
\tag{PL368-16}
\]

whenever `X` has finite cotype. Thus the exponent follows the ambient Banach-space cotype under a matched deformation while the rational-prime divisor convolution is unchanged.

That is a direct falsification control for source specificity: scalar `1/2` is the cotype-`2` member of a generic functional-analytic family.

## 5. Literature / novelty audit

- **Frederic Bayart**, “Hardy Spaces of Dirichlet Series and Their Composition Operators,” *Monatshefte fuer Mathematik* **136** (2002), 203--236. DOI: https://doi.org/10.1007/s00605-002-0470-7. This is the original scalar `\mathcal H^p` framework and source of the finite-`p` absolute-convergence result cited by later work.
- **Daniel Carando, Andreas Defant, Pablo Sevilla-Peris**, “Bohr's absolute convergence problem for `\mathcal H_p`-Dirichlet series in Banach spaces,” *Analysis & PDE* **7**(2) (2014), 513--527. DOI: https://doi.org/10.2140/apde.2014.7.513; arXiv: https://arxiv.org/abs/1304.5377. The paper explicitly records the scalar `1/2` theorem for all finite `p` and proves the vector-valued cotype formula used as the matched control above.
- `PL-001` already records the separate Cole--Gamelin point-evaluation boundary `Re(s)=1/2` throughout the classical infinite-polydisk `H^p` scale. The present finding does not rebrand that boundary: its new derived content is the bridge from Hardy absolute coefficient convergence plus the exact pole-neutral divisor residual to (PL368-5), followed by the cotype deformation control.
- Targeted searches for the exact pole-neutral convolution statement `b=c*1`, its summatory residual (PL368-10), and the resulting continuation (PL368-7) did not locate a direct literature statement. The classical Hardy theorems are prior art; the derived application here is used only as a route classification/no-go result, not claimed as a new theorem of independent literature novelty.

## Boundaries

This finding closes only the route “replace the `ell^p` coefficient hypothesis of `PL-367` by ordinary membership in the canonical Dirichlet Hardy scale and read the resulting `1/2` as RH evidence.” It does **not** show that all Hardy-space structures are irrelevant to RH.

A surviving route must impose an additional constraint that is not shared by generic pole-neutral `\mathcal H^p` elements and is not stable under the cotype deformation above. Examples would have to come from source-specific structure such as a functional-equation involution, a target-relative quotient/model-space condition, an explicit-formula positivity law, a non-coefficientwise coupling, or another global invariant that hypothetical off-line zeros would violate.

In particular, the correct next test for any “critical Hardy” proposal is not merely whether it produces `1/2`, but whether its decisive estimate fails for generic `\mathcal H^p` data and survives the line's matched-control requirement only for the arithmetic zeta source.
