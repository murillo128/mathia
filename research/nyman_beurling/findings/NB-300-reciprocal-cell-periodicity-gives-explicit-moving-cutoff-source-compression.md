# NB-300 — reciprocal-cell periodicity gives explicit moving-cutoff source compression

**Status:** `EXACT-DERIVED + MOVING-CUTOFF + SOURCE-METRIC + LCM-SCALE + NB-299-EXTENSION`. `NB-299` shows that projected dilation occupation disappears for a fixed off-critical zero packet and fixed lower cutoff, but its quantitative bound contains the source compression constant `beta_n(m)=||T_m||`. For moving cutoffs that constant was opaque and could in principle deteriorate fast enough to preserve occupation. The reciprocal-cell periodicity already isolated in `NB-008` makes this source term explicit.

Let

\[
U=V_{n-1}=\operatorname{span}\{g_2,\ldots,g_{n-1}\},
\qquad
P=P_{n-1}=\operatorname{lcm}(2,\ldots,n-1),
\]

and let `S_m` be the integer dilation from the semigroup analysis. Define

\[
\varepsilon_{m,n}^2
=
\min\left\{
1,
(P+1)^2\left(\frac1{m^2}+\frac1{Pm}\right)
\right\}.
\tag{1}
\]

Then the source overlap/compression appearing in `NB-299` satisfies the basis-independent estimate

\[
\boxed{
\beta_n(m)=\|T_m\|
\le
\varepsilon_{m,n}.
}
\tag{2}
\]

In particular, for `m >= P >= 2`,

\[
\boxed{
\beta_n(m)^2
\le
\frac92\frac{P}{m}.
}
\tag{3}
\]

Hence

\[
\boxed{
\frac{m}{P_{n-1}}\to\infty
\quad\Longrightarrow\quad
\beta_n(m)\to0,
}
\tag{4}
\]

even when `n` itself tends to infinity. This removes the unknown finite-section source-conditioning factor from one substantial moving-cutoff regime.

Combining (2) with `NB-299`, for an off-critical zero packet `Z`, with

\[
\delta_Z
=
\min_{\rho\in Z}\left(\Re\rho-\frac12\right)>0,
\]

and lower sample Gram `K_{n-1,Z}`, the escaped-dilation sample Gram obeys, whenever `epsilon_{m,n}<1`,

\[
\boxed{
\|\Xi_{m,n,Z}\|
\le
\|K_{n-1,Z}\|
\frac{\bigl(m^{-\delta_Z}+\varepsilon_{m,n}\bigr)^2}
{1-\varepsilon_{m,n}^2}.
}
\tag{5}
\]

Therefore any moving family `(Z_X,n_X,m_X)` satisfying

\[
\frac{m_X}{P_{n_X-1}}\to\infty,
\qquad
\delta_{Z_X}\log m_X\to\infty,
\tag{6}
\]

also satisfies

\[
\boxed{
\frac{\|\Xi_{m_X,n_X,Z_X}\|}
{\|K_{n_X-1,Z_X}\|}
\to0.
}
\tag{7}
\]

Since `log P_{n-1}=psi(n-1)=n+o(n)`, condition (6) says, at prime-number-theorem scale, that `log m_X` exceeds the lower cutoff `n_X` by a diverging margin. The lcm barrier is therefore not merely a witness scale from `NB-008`: it is also an explicit threshold beyond which the canonical source section becomes asymptotically orthogonal to its multiplicative dilation.

The result does **not** control the regime `m asymp P_{n-1}` or below, does not compare `Xi` to the unresolved tail Gram `E`, and does not remove the separate sample-conditioning factor from target-aware relative-gain estimates. Its value is narrower but concrete: one large joint-scale region that remained open after `NB-299` cannot support persistent projected-dilation occupation merely through worsening source-section conditioning.

## 1. Reciprocal-cell periodicity for the entire lower source section

For the canonical real-space generators

\[
g_j(x)
=
\left\{\frac1{jx}\right\}
-
\frac1j\left\{\frac1x\right\},
\]

put `t=1/x`. On a reciprocal cell `t in [k,k+1)`, `NB-008` gives

\[
g_j(1/t)=\{k/j\}.
\tag{8}
\]

Thus, for every

\[
u=\sum_{j=2}^{n-1}a_jg_j\in U,
\]

the function

\[
F_u(t)=u(1/t),\qquad t\ge1,
\tag{9}
\]

is constant on each unit interval and periodic almost everywhere with every common multiple of `2,...,n-1`. In particular it is `P`-periodic almost everywhere:

\[
F_u(t+P)=F_u(t)
\quad\text{for a.e. }t\ge1.
\tag{10}
\]

The Hilbert norm becomes

\[
\|u\|_2^2
=
\int_0^1|u(x)|^2\,dx
=
\int_1^\infty |F_u(t)|^2\frac{dt}{t^2}.
\tag{11}
\]

This weighted periodic representation is enough to quantify how much of any vector in `U` can concentrate near `x=0`.

## 2. A uniform tail-concentration bound at the lcm scale

Fix nonzero `u in U` and write

\[
A_u
=
\int_1^{P+1}|F_u(t)|^2\,dt.
\tag{12}
\]

Because `F_u` is `P`-periodic almost everywhere, every interval of length `P` has the same unweighted squared mass `A_u`. Also `A_u>0`: if `A_u=0`, periodicity would force `F_u=0` almost everywhere on `[1,infty)`, hence `u=0` almost everywhere.

On the first period, `t <= P+1`, so (11) gives

\[
\|u\|_2^2
\ge
\int_1^{P+1}|F_u(t)|^2\frac{dt}{t^2}
\ge
\frac{A_u}{(P+1)^2}.
\tag{13}
\]

Now consider the part of `u` supported in `(0,1/m]`. Under `t=1/x`,

\[
\|1_{(0,1/m]}u\|_2^2
=
\int_m^\infty |F_u(t)|^2\frac{dt}{t^2}.
\tag{14}
\]

Partition `[m,infty)` into intervals `[m+rP,m+(r+1)P)`. Periodicity gives unweighted mass `A_u` on every such interval, while `t^{-2}` is decreasing. Hence

\[
\|1_{(0,1/m]}u\|_2^2
\le
A_u\sum_{r\ge0}\frac1{(m+rP)^2}.
\tag{15}
\]

The decreasing-series comparison

\[
\sum_{r\ge0}\frac1{(m+rP)^2}
\le
\frac1{m^2}
+
\int_0^\infty\frac{dx}{(m+Px)^2}
=
\frac1{m^2}+\frac1{Pm}
\tag{16}
\]

then combines with (13) to give

\[
\boxed{
\frac{\|1_{(0,1/m]}u\|_2^2}{\|u\|_2^2}
\le
(P+1)^2
\left(\frac1{m^2}+\frac1{Pm}\right).
}
\tag{17}
\]

Taking the minimum with the trivial upper bound `1` yields exactly (1).

This estimate is deliberately crude but uniform over the whole lower section `U`: no generator Gram inverse, singular value, coefficient norm, or basis condition number appears.

## 3. From tail concentration to source compression

For integer `m`, the normalized dilation `S_m` is an isometry and `S_mv` is supported in `(0,1/m]`. Therefore, for `u,v in U`,

\[
|\langle u,S_mv\rangle|
=
|\langle 1_{(0,1/m]}u,S_mv\rangle|
\le
\|1_{(0,1/m]}u\|\,\|v\|.
\tag{18}
\]

Applying (17),

\[
|\langle u,S_mv\rangle|
\le
\varepsilon_{m,n}\|u\|\|v\|.
\tag{19}
\]

The compression operator `T_m` used in `NB-299` is precisely the cross-overlap between `U` and `S_mU`, so taking the supremum over unit vectors proves

\[
\boxed{\|T_m\|\le\varepsilon_{m,n}.}
\tag{20}
\]

When `m >= P >= 2`,

\[
\frac1{m^2}\le\frac1{Pm},
\]

hence

\[
\varepsilon_{m,n}^2
\le
2\frac{(P+1)^2}{Pm}.
\tag{21}
\]

For `P >= 2`,

\[
\frac{(P+1)^2}{P}
=P+2+\frac1P
\le
\frac94P,
\tag{22}
\]

so

\[
\boxed{
\varepsilon_{m,n}^2
\le
\frac92\frac Pm.
}
\tag{23}
\]

This proves (3)--(4).

The important point is the quantifier order. `NB-299` already gives `beta_n(m)->0` for each fixed `n`. Equation (23) gives a simultaneous statement: `n` may move, and source compression still vanishes whenever `m/P_{n-1}->infty`.

## 4. Explicit projected-dilation occupation beyond the lcm barrier

Retain the notation of `NB-299`. For the lower source section `U=V_{n-1}`, let

\[
K=K_{n-1,Z}
\]

be the first-free sample Gram, and let `Xi_{m,n,Z}` be the sample Gram of the part of `S_mU` that escapes `U`. `NB-299` proves, under the same surjectivity assumptions and for `beta_n(m)<1`,

\[
\|\Xi_{m,n,Z}\|
\le
\|K\|
\frac{\bigl(m^{-\delta_Z}+\beta_n(m)\bigr)^2}
{1-\beta_n(m)^2}.
\tag{24}
\]

Substituting (20) gives (5):

\[
\|\Xi_{m,n,Z}\|
\le
\|K\|
\frac{\bigl(m^{-\delta_Z}+\varepsilon_{m,n}\bigr)^2}
{1-\varepsilon_{m,n}^2}.
\tag{25}
\]

Now let `(Z_X,n_X,m_X)` vary. If

\[
\frac{m_X}{P_{n_X-1}}\to\infty,
\]

then (23) implies `epsilon_{m_X,n_X}->0`. If simultaneously

\[
\delta_{Z_X}\log m_X\to\infty,
\]

then

\[
m_X^{-\delta_{Z_X}}\to0.
\]

The numerator in (25) therefore tends to zero and the denominator tends to one, proving (7).

The exact source threshold is the lcm `P_{n-1}`. Using the prime number theorem in the standard form

\[
\log\operatorname{lcm}(1,\ldots,N)=\psi(N)=N+o(N),
\tag{26}
\]

we have

\[
\log P_{n-1}=n+o(n).
\tag{27}
\]

Thus a sufficient asymptotic source-separation regime is

\[
\log m_X-n_X\to+\infty
\]

with enough margin to absorb the `o(n_X)` term. The exact statement (6), not this heuristic shorthand, is the theorem.

## 5. Target-aware corollary and the conditioning that remains

The target-aware gain in `NB-299` can be bounded by the same substitution. If `G_{m,n,Z}(y)` denotes the escaped-dilation repair gain for first-free datum `y` and `C_U(m;y)` its lower-section baseline cost, then

\[
\boxed{
\frac{G_{m,n,Z}(y)}{\mathcal C_U(m;y)}
\le
\min\left\{
1,
\kappa(K_{n-1,Z})
\frac{\bigl(m^{-\delta_Z}+\varepsilon_{m,n}\bigr)^2}
{1-\varepsilon_{m,n}^2}
\right\}.
}
\tag{28}
\]

So source conditioning is no longer hidden: in the regime `m/P -> infinity`, its contribution vanishes at least at the explicit `sqrt(P/m)` scale. But a uniform statement about **relative target repair** still requires the sample condition number `kappa(K)` not to overwhelm that decay.

This distinction matters. Equation (7) is an operator-norm statement normalized by `||K||`; it does not imply that `Xi` is small relative to the unresolved tail Gram `E_{n-1,Z}`, and it does not by itself imply that every relevant target sees negligible gain. The source-side obstruction and the sample-side obstruction are now cleanly separated rather than conflated.

## 6. What this rules out in the moving Ford regime

The fixed-parameter conclusion of `NB-299` left open a broad escape hatch: perhaps `n_X` grows so fast that the lower source section becomes nearly invariant under the dilation `S_{m_X}`, keeping `beta_{n_X}(m_X)` near one even while `m_X` grows. Equation (23) rules that out whenever

\[
m_X\gg P_{n_X-1}.
\]

Thus a persistent projected-dilation mechanism must avoid at least one of two decays:

- it must remain at or below the reciprocal-cell lcm scale, so that `m_X/P_{n_X-1}` does not diverge; or
- its off-critical damping must remain weak, so that `delta_{Z_X} log m_X` does not diverge.

This is a genuine narrowing of the joint-scale window. It is not yet a closure of that window: the potentially relevant region `m_X lesssim P_{n_X-1}` is exponentially large in the lower cutoff and is exactly where bare common-period arguments cease to force source separation.

The result also explains why the lcm scale keeps reappearing in this line for two apparently different reasons. In `NB-008`, `P_N` was the first universal reciprocal-cell period at which a finite Nyman section exposes a deterministic tail witness. Here the same common period controls how far a vector from that section can push its `L^2` mass toward zero, which in turn controls overlap with a multiplicatively dilated copy. Both effects come from the same arithmetic synchronization of the canonical generators.

## 7. Adversarial audit

Several possible overstatements were checked explicitly.

First, the periodicity is only needed almost everywhere. All arguments use integrals, so reciprocal-cell boundaries have measure zero and cause no issue.

Second, the estimate does not assume a favorable coefficient representation of `u`. It is expressed directly in the Hilbert norm of `u`, and therefore survives arbitrary ill-conditioning of the canonical generator basis.

Third, the lower bound (13) is intentionally one-sided and uses only the first full period. It remains valid for every nonzero `u in U`; `A_u=0` would force `u=0` almost everywhere by periodicity.

Fourth, the series estimate (16) has the correct scale and direction. The `r=0` term is separated and the rest is dominated by the integral of the decreasing function `x -> (m+Px)^{-2}`.

Fifth, (25) is used only once `epsilon_{m,n}<1`, exactly matching the invertibility requirement inherited from `NB-299`. Condition `m/P -> infinity` guarantees this eventually.

Sixth, no comparison `Xi/E -> 0` is claimed. Both the escaped-dilation Gram and the unresolved tail Gram may shrink, and this finding does not determine their ratio.

Seventh, the result does not convert the band mechanism into a bound for the original Nyman distance. It only sharpens the projected-dilation occupation route isolated in `NB-297`--`NB-299`.

## 8. Prior-art and dependency audit

The reciprocal-cell identity and its lcm period are already internal to this research line through `NB-008`. The dilation geometry and projected sample bound used in (24) are internal results from `NB-297`--`NB-299`. The remaining steps are elementary weighted-periodic estimates and Hilbert-space Cauchy--Schwarz.

A fresh prior-art search for Nyman--Beurling dilation semigroups, multiplicative Gram structure, reciprocal-cell periodicity, and recent Gram-compressibility work did not surface this particular moving-cutoff compression estimate. Classical semigroup formulations and recent multiplicative Gram-decay results are adjacent background, but none is load-bearing for the proof here. No new external dependency is therefore introduced, and `SOURCES.md` does not need an update.

## 9. Frontier consequence

Before this finding, the active projected-dilation question had three coupled unknowns: off-critical damping, source compression `beta_n(m)`, and target/sample geometry. The source term is now explicit in the region beyond the universal reciprocal-cell period:

\[
\beta_n(m)
\lesssim
\sqrt{\frac{P_{n-1}}m}.
\tag{29}
\]

The next discriminating regime is consequently the near/sub-lcm window

\[
m_X\lesssim P_{n_X-1},
\tag{30}
\]

especially when simultaneously `delta_{Z_X} log m_X` is only `O(1)`. Any stronger continuation should either improve the universal period estimate by exploiting the actual projection/normal-equation structure of the relevant source vector, or show that the Ford scaling necessarily lies in the already-excluded super-lcm region.

The finding therefore advances the frontier by turning one previously opaque moving-cutoff quantity into an explicit arithmetic scale. It does not consume any open clue: the accepted target-aware and visible-semigroup clues remain broader than the lcm compression estimate proved here, and the proposed skeleton clue is not tested by this argument.