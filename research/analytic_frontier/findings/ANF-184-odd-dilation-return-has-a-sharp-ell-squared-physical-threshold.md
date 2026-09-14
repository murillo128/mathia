# ANF-184 — Odd-dilation return has a sharp ell-squared physical threshold

**Status:** `EXACT-DERIVED + TWO-SIDED-FIRST-RETURN + SHARP-ELL-SQUARED-ACTIVATION + SOURCE-RESOLUTION-CERTIFICATE`. `ANF-143` proves that, at any frozen admissible same-profile stage, the actual first positive return density produced by a common odd dilation satisfies `theta_ell=O_G(ell^-2)`. The complementary lower bound is also forced by the exact binomial product: any point capable of causing a positive return must stay `Omega_G(ell^-1)` away from every old zero maximum, so the old pressure has already paid `Omega_G(ell^-2)` there.

Consequently, for every sufficiently large odd `ell`,

\[
\boxed{c_G\ell^{-2}\le \theta_\ell\le C_G\ell^{-2}.}
\tag{1}
\]

The same law gives a sharp physical scale. With the actual integer copy count

\[
m_{\ell,A}:=\lfloor \theta_\ell A\rfloor,
\tag{2}
\]

the layer is eventually absent when `A/ell^2 -> 0`, has diverging copy count when `A/ell^2 -> infinity`, and lives in an `O(1)`-copy transition regime when `A=Theta(ell^2)`. At a first-return maximizer the active saddle lies at distance `Theta_G(ell^-1)` from the old critical skeleton and from the relevant annihilator walls. Since its pressure Hessian remains uniformly nondegenerate after the `theta_ell~ell^-2` retuning, its physical Laplace width is `Theta(A^-1/2)`. Thus the same crossover

\[
\boxed{A\asymp \ell^2}
\tag{3}
\]

is the threshold at which the source can geometrically resolve the new `ell^-1` chamber scale.

This is a frozen-stage theorem. Its constants may deteriorate arbitrarily with the stage, and it does not turn the slow diagonal of `ANF-143` into a depth-uniform effective rate.

## 1. The first positive return has an exact variational formula

Freeze one stage of the `ANF-143` construction. Its pressure satisfies

\[
G(\alpha)\le0,
\qquad
K=\{\xi_1,\ldots,\xi_J\}\subset(0,1),
\tag{4}
\]

where `K` is exactly the finite set of zero maxima and every `xi_j` is nondegenerate. Put

\[
\tau_j:=\frac1{2\xi_j},
\qquad
Q_\ell(\alpha)
:=\prod_{j=1}^{J}
\left(1+e^{-2\pi i\ell\tau_j\alpha}\right),
\qquad \ell\in2\mathbb N+1,
\tag{5}
\]

and

\[
M_\ell(\theta)
:=\sup_{0\le\alpha<1}
\left[G(\alpha)+2\theta\log|Q_\ell(\alpha)|\right].
\tag{6}
\]

By `ANF-143`, for each fixed odd `ell`, `M_ell(theta)<0` for all sufficiently small positive `theta`, while the origin forces a later positive crossing. Hence the first strictly positive return `theta_ell` exists and satisfies `M_ell(theta_ell)=0`.

A point with `|Q_ell(alpha)|<=1` cannot create that return: there `log|Q_ell|<=0` and `G<=0`. At an old zero maximum `Q_ell=0`, so the modified pressure is `-infinity` for every positive `theta`. Therefore

\[
\boxed{
\theta_\ell
=
\inf_{\alpha:\,|Q_\ell(\alpha)|>1}
\frac{-G(\alpha)}{2\log|Q_\ell(\alpha)|}.
}
\tag{7}
\]

The formula also retains the origin and the `alpha->1` side automatically: they enter the infimum only if the product exceeds one there. It does not confuse the trivial equality `M_ell(0)=0` with the first positive return, because (7) is derived after restricting to `theta>0` and to points whose logarithmic gain is positive.

## 2. Product structure forces an `Omega(ell^-2)` return cost

Write

\[
q_{j,\ell}(\alpha)
:=\left|1+e^{-2\pi i\ell\tau_j\alpha}\right|.
\tag{8}
\]

Every factor is at most two. Hence

\[
|Q_\ell(\alpha)|>1
\quad\Longrightarrow\quad
q_{j,\ell}(\alpha)>2^{1-J}
\quad\text{for every }j.
\tag{9}
\]

Indeed, if one factor were at most `2^(1-J)`, multiplying by the maximal value `2` of the remaining `J-1` factors would give product at most one.

Oddness makes the `j`th factor vanish exactly at the corresponding old maximum:

\[
1+e^{-2\pi i\ell\tau_j\xi_j}=0.
\tag{10}
\]

Using `|e^{iu}-e^{iv}|<=|u-v|`,

\[
q_{j,\ell}(\alpha)
\le
2\pi\ell\tau_j|\alpha-\xi_j|.
\tag{11}
\]

Combining (9) and (11), every point in the return-capable set obeys

\[
|\alpha-\xi_j|
\ge
\frac{2^{1-J}}{2\pi\tau_j}\,\ell^{-1}
\qquad(1\le j\le J).
\tag{12}
\]

Because the zero set of `G` is the finite nondegenerate set `K`, there are frozen-stage constants `rho,c_1,eta>0` such that

\[
-G(\alpha)\ge c_1|\alpha-\xi_j|^2
\quad (|\alpha-\xi_j|<\rho),
\tag{13}
\]

while

\[
-G(\alpha)\ge\eta
\quad\text{outside the }\rho\text{-neighborhoods of }K.
\tag{14}
\]

Equations (12)--(14) imply, for all sufficiently large odd `ell`,

\[
-G(\alpha)\ge c_2\ell^{-2}
\qquad\text{whenever }|Q_\ell(\alpha)|>1,
\tag{15}
\]

with `c_2>0` depending only on the frozen stage. Since

\[
\log|Q_\ell(\alpha)|\le J\log2,
\tag{16}
\]

the variational formula (7) gives

\[
\boxed{
\theta_\ell
\ge
\frac{c_2}{2J\log2}\,\ell^{-2}
=:c_G\ell^{-2}.
}
\tag{17}
\]

`ANF-143` already supplies, from compact phase-orbit recurrence and one `O(ell^-1)` correction of an old maximum,

\[
\theta_\ell\le C_G\ell^{-2}.
\tag{18}
\]

Together, (17) and (18) prove (1). No rational independence among the `tau_j` is needed for the lower bound; the arithmetic orbit closure enters only the existing upper-bound constant `C_G`.

## 3. Integer flooring makes `A~ell^2` the activation clock

Return to the physical layer count (2). From (1),

\[
c_G\frac{A}{\ell^2}
\le
\theta_\ell A
\le
C_G\frac{A}{\ell^2}.
\tag{19}
\]

Therefore:

- if `A/ell^2 -> 0`, then `theta_ell A<1` eventually and `m_(ell,A)=0`;
- if `A/ell^2 -> infinity`, then `m_(ell,A)->infinity`;
- if `A=kappa ell^2` with fixed positive `kappa`, then `theta_ell A=Theta_G(kappa)` and the layer has only `O_G,kappa(1)` copies, with possible inactivity for small `kappa` because of the floor.

Thus the exponent that was only known to be cheap in `ANF-143` has a genuine physical clock: its first possible integer activation is neither arbitrarily earlier nor arbitrarily later than `ell^2`, up to frozen-stage constants.

For a prescribed finite collection of frozen stages and chosen odd dilations `ell_1,...,ell_r`, taking `A` below a sufficiently small constant multiple of `min_q ell_q^2` leaves every such layer inactive, while taking `A` above a sufficiently large constant multiple of `max_q ell_q^2` activates every layer. If `A/ell_q^2 -> infinity` along a physical family, the corresponding copy counts diverge. This is a finite-prefix certificate; no stage-uniform constant is asserted as the depth grows.

## 4. First-return saddles sit at the same `ell^-1` geometric scale

Let `alpha_ell` be any maximizer at the first positive return with finite modified pressure. Then `|Q_ell(alpha_ell)|>1` and

\[
-G(\alpha_\ell)
=2\theta_\ell\log|Q_\ell(\alpha_\ell)|
\le 2C_GJ\log2\,\ell^{-2}.
\tag{20}
\]

The fixed negative gap away from `K` and nondegenerate quadratic loss near `K` imply

\[
\operatorname{dist}(\alpha_\ell,K)
=O_G(\ell^{-1}).
\tag{21}
\]

Equation (12) gives the matching lower bound for the nearest old maximum, so

\[
\boxed{
\operatorname{dist}(\alpha_\ell,K)
=\Theta_G(\ell^{-1}).
}
\tag{22}
\]

There is also a uniform phase-space separation from every zero wall of each binomial factor. From (9),

\[
2|\cos(\pi\ell\tau_j\alpha_\ell)|>2^{1-J},
\tag{23}
\]

so the phase `ell*tau_j*alpha_ell` stays a frozen positive distance from every half-integer. In the physical `alpha` coordinate this means distance `Omega_G(ell^-1)` from every zero of that factor.

On the resulting zero-free chamber,

\[
\frac{d^2}{d\alpha^2}
\log\left|1+e^{-2\pi i\ell\tau_j\alpha}\right|
=-(\pi\ell\tau_j)^2
\sec^2(\pi\ell\tau_j\alpha).
\tag{24}
\]

At a return maximizer, (23) bounds the secant factors from above by a frozen-stage constant. Since `theta_ell ell^2=Theta_G(1)`, the retuned contribution `2 theta_ell (log|Q_ell|)''` is negative and of order one. The old pressure already has strictly negative curvature near each old maximum. Hence the first-return saddle remains uniformly nondegenerate on the `ell^-1` chamber scale.

If the source exponent is `A`, the local Laplace width is therefore

\[
w_A=\Theta_G(A^{-1/2}).
\tag{25}
\]

Resolving the active saddle inside a chamber whose walls and neighboring old skeleton lie `Theta_G(ell^-1)` away requires

\[
w_A=o(\ell^{-1}),
\qquad\text{i.e.}\qquad
\boxed{A/\ell^2\to\infty.}
\tag{26}
\]

At `A=Theta(ell^2)` the saddle width and chamber scale are comparable, exactly when the integer copy count is only `Theta(1)`. Thus activation and geometric source resolution have the same critical scale. This explains why the slow physical diagonal in `ANF-143` had to absorb both floor activation and dilation-dependent chamber/Hessian constants: they are two aspects of one `ell^2` transition.

## 5. What this resolves, and what it does not

The fixed-stage quantitative question posed by `CLUE-odd-dilation-two-sided-return-and-physical-activation` is resolved positively. The exact product supplies the missing lower return bound, and the resulting `theta_ell~ell^-2` law turns the qualitative activation clause of `ANF-143` into an explicit scale relation. For any finite prescribed prefix, the finitely many stage constants give finite activation and source-resolution thresholds once the chosen dilations are known.

This does **not** make the infinite cascade effective in depth. The constants `c_G`, `C_G`, recurrence radius, curvature radii, number of chambers, and source normalization constants may deteriorate arbitrarily as the critical skeleton evolves. A growing-depth rate still requires quantitative control of those stage data. Nor does (26) by itself prove a two-sided source asymptotic uniformly when `ell` grows with `A`; it identifies the necessary and natural geometric regime in which the fixed-stage Laplace argument can be resolved.

The downstream affine-completion and near-extremizer questions are unchanged. A source-heavy positive cascade with a certified physical clock is not yet a fatal non-excisable Montgomery--Taylor near-extremizer.

## 6. Prior-art audit

The ingredients used here are classical at the mechanism level: local quadratic optimization near a nondegenerate maximum, finite-dimensional almost-periodic recurrence from `ANF-143`, and one-dimensional Laplace localization. A targeted literature search for a specialized theorem matching the present first-positive-return problem did not identify a result that supplies the two-sided law (1) for this annihilating binomial product, nor the coincidence of the floor-activation and chamber-resolution scales (3). The proof above is elementary and self-contained once the frozen-stage hypotheses of `ANF-143` are granted, so no new external dependency is load-bearing and `SOURCES.md` need not change.

The useful structural conclusion is not novelty of the classical ingredients but the exact scale match: the same odd dilation that buys `theta_ell=Theta_G(ell^-2)` forces both the integer physical clock and the local source-resolution clock to be `A=Theta_G(ell^2)`.