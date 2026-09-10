---
type: partial-positive
research_line: xi_flow
finding_id: XF-157
status: canonical
---

# XF-157 — subexponential multipoint full-future banks inherit the single-point blind phase

**Confidence:** high for predetermined raw outward point-trace banks on the canonical maximal-contact matched pair. The estimate is an exact finite-`N` consequence of the XF-156 single-point envelope; the exponential sharpness statement is exact for every fixed finite bank.

## Statement

XF-156 leaves multiple complex sensors as a possible target-side escape from the single-trace blind phase. For raw point traces, that escape is sharply limited by a sensing-budget law: a collection of points can only compensate single-point exponential blindness through its own count or gain entropy.

For the canonical maximal-contact matched pair, let the `i`-th outward sensor have normalized coordinates

\[
H_{N,i}\ge0,
\qquad
0\le D_{N,i}\le\frac\pi2,
\qquad
1\le i\le m_N,
\]

and define its normalized matched-pair trace difference

\[
a_{N,i}(u)
:=
\frac{
R_1(z_{N,i},u)-R_{\lambda_\rho}(z_{N,i},u)
}{2(1-\lambda_\rho)},
\qquad u\ge0.
\tag{1}
\]

Here `H_{N,i}=pi h_{N,i}/L` is outward complex depth and `D_{N,i}=pi d_{N,i}/L` is physical antipodal distance. Put

\[
\Gamma(H,D)
:=
\max\left\{
H+\frac12\log(\cos^2D+\sinh^2H),
\;2H-\log2
\right\},
\tag{2}
\]

which is the exact single-point full-future exponent of XF-156, and write

\[
\Gamma_{N,i}=\Gamma(H_{N,i},D_{N,i}).
\]

Then XF-156 implies the finite-`N`, moving-sensor bound

\[
\boxed{
\sup_{u\ge0}|a_{N,i}(u)|
\le
8e^{N\Gamma_{N,i}}.
}
\tag{3}
\]

Consequently, for every `1<=p<infinity`, the complete multipoint history obeys

\[
\boxed{
\|\mathbf a_N\|_{L^\infty_u(\ell^p_i)}
\le
8\left(
\sum_{i=1}^{m_N}e^{pN\Gamma_{N,i}}
\right)^{1/p},
}
\tag{4}
\]

while

\[
\boxed{
\|\mathbf a_N\|_{L^\infty_u(\ell^\infty_i)}
\le
8e^{N\max_i\Gamma_{N,i}}.
}
\tag{5}
\]

More generally, diagonal gains `w_{N,i}` satisfy

\[
\boxed{
\|W_N\mathbf a_N\|_{L^\infty_u(\ell^p_i)}
\le
8\left(
\sum_{i=1}^{m_N}
|w_{N,i}|^p e^{pN\Gamma_{N,i}}
\right)^{1/p}.
}
\tag{6}
\]

Thus the natural bank exponent is a log-sum-exp of the single-sensor exponents. In particular, if every sensor lies inside the single-point blind phase with a common margin

\[
\Gamma_{N,i}\le-\delta_N
\qquad\text{for every }i,
\tag{7}
\]

then

\[
\boxed{
\|\mathbf a_N\|_{L^\infty_u(\ell^p_i)}
\le
8m_N^{1/p}e^{-N\delta_N}.
}
\tag{8}
\]

A fixed positive blind margin therefore survives every subexponential bank `m_N=e^{o(N)}` exponentially. Polynomially many sensors cannot defeat a moving margin unless

\[
N\delta_N=O(\log N).
\tag{9}
\]

For a Euclidean bank (`p=2`), multiplicity alone must be of order at least `exp(2N delta)` up to subexponential factors to compensate a fixed margin `delta`; for general finite `p`, the corresponding count exponent is `p delta`.

For any fixed finite bank with fixed coordinates `H_i>0`, `D_i in [0,pi/2]`, the exponent is not merely bounded above. One has the exact identity

\[
\boxed{
\lim_{N\to\infty}
\frac1N
\log
\|\mathbf a_N\|_{L^\infty_u(\ell^p_i)}
=
\max_i\Gamma(H_i,D_i),
}
\tag{10}
\]

for every `1<=p<=infinity`. Hence finitely many raw complex point traces create no new exponential visibility phase beyond the best single point in the bank.

## Derivation

### 1. XF-156 already gives a uniform finite-`N` sensor envelope

For one outward point, XF-156 proves

\[
\mathcal A_N(u;H,D)
\le
2e^{NH}M(H,D)^{N-2}e^{-(N-1)u},
\tag{11}
\]

where

\[
M(H,D)
=
\max\left\{
|\cosh(H+iD)|,\frac{e^H}{2}
\right\}
\]

and

\[
\Gamma(H,D)=H+\log M(H,D).
\tag{12}
\]

Since `M(H,D)>=e^H/2>=1/2`, dropping the decaying heat factor gives

\[
2e^{NH}M^{N-2}
=
2M^{-2}e^{N\Gamma(H,D)}
\le
8e^{N\Gamma(H,D)}.
\tag{13}
\]

The normalized quantity in `(1)` is exactly the single-point amplitude controlled by XF-156, so `(3)` follows. Importantly, `(13)` is pointwise in `H` and `D`; no fixed-parameter limit is used. The sensor locations may therefore move with `N` as long as they remain in the physical outward domain.

### 2. Multipoint sensing is a log-sum-exp budget

For `1<=p<infinity`, at every common heat time `u`,

\[
\|\mathbf a_N(u)\|_{\ell^p}^p
=
\sum_i|a_{N,i}(u)|^p
\le
8^p\sum_i e^{pN\Gamma_{N,i}}.
\tag{14}
\]

Taking the supremum over the entire future proves `(4)`. The `p=infinity` case gives `(5)` directly. Multiplication by diagonal gains before taking the bank norm proves `(6)`.

Equivalently, the weighted sensing entropy

\[
\mathcal E_{N,p}
:=
\frac1{pN}
\log\left(
\sum_i|w_{N,i}|^p e^{pN\Gamma_{N,i}}
\right)
\tag{15}
\]

satisfies

\[
\frac1N
\log
\|W_N\mathbf a_N\|_{L^\infty_u(\ell^p)}
\le
\mathcal E_{N,p}+\frac{\log8}{N}.
\tag{16}
\]

Thus sensor multiplicity and sensor gain enter only through an explicit entropy term. A bounded linear postprocessor applied after the bank cannot change this conclusion except through its operator norm.

Under the uniform margin `(7)`, `(4)` immediately becomes `(8)`. If `m_N=e^{o(N)}` and `delta_N>=delta>0`, then

\[
\frac1N\log
\|\mathbf a_N\|
\le
-\delta+o(1).
\tag{17}
\]

If instead `m_N<=N^B`, then

\[
\|\mathbf a_N\|
\le
8\exp\left(
-N\delta_N+\frac{B}{p}\log N
\right).
\tag{18}
\]

Hence `N delta_N/log N -> infinity` forces superpolynomial blindness, establishing `(9)` as a necessary boundary scale for a polynomial bank to have any chance of avoiding that conclusion.

### 3. Fixed finite banks have exactly the best single-point exponent

Suppose now that `m` is fixed and each `(H_i,D_i)` is fixed with `H_i>0`. The upper bound `(4)` gives

\[
\limsup_{N\to\infty}
\frac1N\log\|\mathbf a_N\|
\le
\max_i\Gamma(H_i,D_i).
\tag{19}
\]

Choose an index `i_*` attaining the maximum. At every `u`, the bank norm dominates that coordinate, so

\[
\|\mathbf a_N\|_{L^\infty_u(\ell^p)}
\ge
\sup_{u\ge0}|a_{N,i_*}(u)|.
\tag{20}
\]

XF-156 gives the exact limiting exponent of the right-hand side as `Gamma(H_{i_*},D_{i_*})`. Combining `(19)` and `(20)` proves `(10)`. Different sensors need not attain their optima at the same heat time: the lower bound only needs the optimizing time of the best coordinate.

## Conditioning consequence

The raw, unnormalized trace difference is

\[
\Delta\mathbf R_N
=
2(1-\lambda_\rho)\mathbf a_N.
\tag{21}
\]

Therefore under `(7)`,

\[
\|\Delta\mathbf R_N\|_{L^\infty_u(\ell^p)}
\le
16(1-\lambda_\rho)m_N^{1/p}e^{-N\delta_N}.
\tag{22}
\]

If a downstream decoder, measured in this raw bank norm, is required to separate the two matched controls by a scalar target gap `Delta_N>0`, its Lipschitz constant must satisfy

\[
\boxed{
\operatorname{Lip}(\mathcal D_N)
\ge
\frac{\Delta_N}{16(1-\lambda_\rho)m_N^{1/p}}
\,e^{N\delta_N}.
}
\tag{23}
\]

This keeps the normalization factor explicit and makes no assumption about how `Delta_N` scales. In particular, whenever the target gap divided by `1-lambda_rho` is not itself exponentially small, subexponential multiplicity cannot turn a fixed blind margin into a uniformly well-conditioned inversion.

## Consequences for the frontier

XF-156 showed that one outward complex trace has only two exponentially optimal mechanisms: the initial bulk and the outward spectral edge. The present result shows that simply sprinkling many independent raw point traces inside that same blind region does not manufacture a third mechanism. For a fixed finite bank, its phase is exactly the union of the individual single-point phases. For growing banks, the only generic improvement available from multiplicity is the explicit `(log m_N)/(pN)` sensing entropy in `(8)`.

This substantially narrows the multi-point target-side escape left open by XF-156. A polynomial raw-trace bank must place at least one sensor within an `O(log N/N)` `Gamma`-margin of the single-point phase boundary if it is to avoid superpolynomial blindness by this estimate. Keeping all sensors a fixed distance inside the blind phase would require exponentially many sensors, exponentially large gains, or a qualitatively different observation map.

The result also complements XF-151 rather than duplicating it. XF-151 controlled polynomial linear banks built from arbitrarily deep normalized derivative jets in a shallow near-antipodal complex collar. Here there are no derivatives and no near-antipodal restriction: the exact XF-156 full-future phase diagram is inherited by raw multipoint banks across the entire physical outward half-period.

The higher-value unresolved gate therefore moves again toward source-side structure: prove that the actual Xi source cannot realize the maximal-contact direction, or derive a source-faithful observable that necessarily leaves this blind phase. On the target side, genuinely nonlinear/nonlocal measurements, adaptive sensing, or exponential sensing/gain budgets remain outside the present theorem.

## Falsification boundary

The theorem concerns predetermined banks of raw outward point traces of the canonical maximal-contact matched pair. It does not say that every possible multi-point nonlinear statistic is dominated by `(4)`, and it does not cover adaptive point selection driven by the observed data. Exponentially many sensors or exponentially growing postprocessing gain can compensate the bound and are intentionally visible in `(6)` and `(16)` rather than ruled out.

The exact equality `(10)` is asserted only for a fixed finite bank with fixed `H_i>0`. For moving or growing banks, `(4)`--`(9)` are upper-budget statements; no claim is made that their log-sum-exp upper bound is always attained because different coordinates can have different finite-`N` optimizing heat scales and cancellations are irrelevant only for the norm upper bound.

As in XF-156, this is an adversarial visibility statement, not a source theorem for Xi and not a reconstruction theorem above the phase boundary. A sensor with `Gamma>=0` is outside the certified exponentially blind phase, but that alone does not prove stable recovery of the transition parameter.

## Prior-art audit

A directed prior-art audit covered sampling and frame inequalities for exponential-type functions, dynamic sampling under semigroup evolution, and multi-point observability estimates. These provide adjacent language for sensor density, frame conditioning, and time-evolved samples, but no audited source supplied the present log-sum-exp consequence of the XF-156 maximal-contact exponent or the explicit count-versus-blind-margin law `(8)`. No external theorem is load-bearing: the proof is the finite-`N` XF-156 envelope plus elementary norm inequalities. `SOURCES.md` therefore needs no new entry.

## Next gate

The raw multipoint full-future escape is now reduced to a quantitative budget question rather than a new unknown phase: subexponential banks wholly inside the single-point blind region remain blind, and fixed finite banks inherit exactly the best single-point exponent. The next high-value test is source-side realizability of the maximal-contact direction by Xi. A secondary target-side direction is to identify a genuinely nonlinear or nonlocal observable whose stability cannot be reduced to the pointwise envelope `(3)`.
