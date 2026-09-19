# RE-226 — Vanishing arcs force divergent real single-center Wiener rate

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + EXACT-REMAINDER + WIENER-NORM-PARITY-PROBE + FIXED-CORRIDOR-LOCALIZATION + REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-221--RE-225.

RE-225 reduces every putative factor-two escape of the fixed-corridor positive-real single-center predictor to one remaining singular regime: the observed arc must shrink, `alpha_m -> 0`, while `m alpha_m -> infinity`. The contraction-boundary subcase is nested inside the same limit. The open question was therefore whether exact incomplete-beta cancellation can become unusually cheap when the observed arc collapses.

It cannot. In fact the vanishing-arc regime is not merely above the factor-two floor: once the center stays bounded and the truncation ratio stays bounded away from zero, its normalized Wiener cost **diverges**. The proof is elementary and does not require a uniform incomplete-beta asymptotic. It evaluates the exact normalized polynomial at the anti-aligned point `z=-1`, outside the observed arc. The Wiener norm controls that value globally, and contraction makes the real DC denominator too small to compensate the negative-axis growth.

Let

\[
Q_{m,N,a}(z)
:=
z^m a^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(1-\frac za\right)^k,
\qquad
F_{m,N,a}(z):=\frac{Q_{m,N,a}(z)}{Q_{m,N,a}(1)},
\tag{1}
\]

with `m>=2`, `N>=0`, `a>0`, and assume `Q_{m,N,a}(1) != 0`. For some `0<alpha<pi/2`, suppose the single-center contraction condition holds,

\[
r(\alpha,a)
:=
\left|1-\frac{e^{-i\alpha}}a\right|<1.
\tag{2}
\]

If also `a<=A` for a fixed finite `A`, then

\[
\boxed{
\|F_{m,N,a}\|_A
\ge
 e^{-1}
\left(1+\frac1{2A}\right)^N.
}
\tag{3}
\]

Consequently, for any family with

\[
a_m\le A,
\qquad
\lambda_m:=\frac{N_m}{m}\ge\lambda_->0,
\qquad
\alpha_m\to0,
\qquad
m\alpha_m\to\infty,
\tag{4}
\]

one has

\[
\boxed{
\frac{\log\|F_m\|_A}{m\alpha_m}
\longrightarrow+\infty.
}
\tag{5}
\]

Applied to the fixed-corridor frontier of RE-223--RE-225, this closes the last positive-real single-center rate-two escape. Every exact normalized fixed-corridor predictor of this form that predicts uniformly on its expanding window satisfies

\[
\boxed{
\liminf_{m\to\infty}
\frac{\log\|F_m\|_A}{m\alpha_m}>2,
}
\tag{6}
\]

with the understanding that the liminf may be `+infinity`. Equation (6) is family-wise rather than a new uniform class constant: the argument does not produce one `eta_R>0` valid simultaneously for every possible family in a corridor. It therefore does **not** improve the global separated-prediction lower bound `C_sep>=1`, nor does it rule out an infimum of two over a sequence of differently tuned single-center families. What it rules out is an actual asymptotic fixed-corridor positive-real single-center family attaining or crossing rate two.

## 1. Contraction alone bounds the real normalization denominator

The exact integral identity from RE-221 is

\[
F_{m,N,a}(z)
=
\frac{
\displaystyle\int_0^z
s^{m-1}\left(1-\frac sa\right)^Nds
}{
\displaystyle D_{m,N,a}
},
\qquad
D_{m,N,a}
:=
\int_0^1
s^{m-1}\left(1-\frac sa\right)^Nds.
\tag{7}
\]

The contraction condition (2) is equivalent to

\[
a>\frac1{2\cos\alpha}>rac12.
\tag{8}
\]

Hence for every real `s in [0,1]`,

\[
\left|1-\frac sa\right|\le1.
\tag{9}
\]

This gives the crude but uniform bound

\[
\boxed{
|D_{m,N,a}|
\le
\int_0^1s^{m-1}ds
=\frac1m.
}
\tag{10}
\]

No sign information, saddle localization, or tail estimate is used. If `a<1`, cancellation in the real denominator can only make `|D|` smaller and strengthen what follows.

## 2. The anti-aligned value `F(-1)` grows exponentially in `N`

Because the integrand in (7) is a polynomial, the path from `0` to `-1` may be taken along the negative real axis. With `s=-u`,

\[
\int_0^{-1}
 s^{m-1}\left(1-\frac sa\right)^Nds
=
(-1)^m
\int_0^1
u^{m-1}\left(1+\frac ua\right)^Ndu.
\tag{11}
\]

Write the positive integral on the right as `P_{m,N,a}`. Restrict it to the last interval of length `1/m`. For `u in [1-1/m,1]`,

\[
u^{m-1}
\ge
\left(1-\frac1m\right)^{m-1}
\ge e^{-1},
\tag{12}
\]

where the last inequality follows from `log(1-x)>=-x/(1-x)` with `x=1/m`. If `a<=A`, then for `m>=2`,

\[
1+\frac ua
\ge
1+\frac{1-1/m}{A}
\ge
1+\frac1{2A}.
\tag{13}
\]

Therefore

\[
P_{m,N,a}
\ge
\frac{e^{-1}}m
\left(1+\frac1{2A}\right)^N.
\tag{14}
\]

Combining (7), (10), and (14),

\[
|F_{m,N,a}(-1)|
\ge
 e^{-1}
\left(1+\frac1{2A}\right)^N.
\tag{15}
\]

For every polynomial `F(z)=sum_j c_j z^j`, its Wiener norm dominates every unit-circle value,

\[
|F(-1)|
\le
\sum_j|c_j|
=\|F\|_A.
\tag{16}
\]

Equations (15)--(16) prove (3).

The key point is representation-specific but cancellation-insensitive. The observed arc can become arbitrarily small, yet the same coefficient vector must also define the polynomial at `z=-1`. A positive real expansion center turns that point into a direction where every factor `1+u/a` reinforces rather than cancels. Exact cancellation of the incomplete-beta remainder on the observed arc cannot hide this global Wiener cost.

## 3. Vanishing arcs are infinitely expensive at fixed positive truncation density

Put `lambda_m=N_m/m`. Taking logarithms in (3) gives

\[
\frac{\log\|F_m\|_A}{m\alpha_m}
\ge
\frac{\lambda_m}{\alpha_m}
\log\left(1+\frac1{2A}\right)
-
\frac1{m\alpha_m}.
\tag{17}
\]

Under (4), the first term tends to `+infinity` and the second tends to zero. This proves (5).

This is stronger than the normal-form question left by RE-225. There is no need to distinguish an interior center `a_m -> a_*>1/2` from the contraction corner `(alpha_m,a_m)->(0,1/2)`: as long as the center has a finite upper bound and `N_m/m` does not collapse, both regimes pay the same divergent normalized surcharge. In particular, the half-center corner does not provide a hidden cancellation route.

The assumptions are also exactly aligned with the fixed-corridor localization already available. The fixed delay corridor bounds `lambda_m` above. RE-223 supplies a positive lower bound for `lambda_m` on every subsequence with bounded normalized Wiener rate; more generally its corridor bound supplies such a lower bound for every fixed finite target rate. RE-224 then bounds `a_m` above. Thus every bounded-rate subsequence has the hypotheses needed for (17).

## 4. The fixed-corridor positive-real single-center factor-two escape is closed

Consider a uniformly predicting family in the fixed-corridor RE-216 scaling,

\[
\epsilon_m
:=
\sup_{|\theta|\le\alpha_m}
|F_m(e^{-i\theta})-1|
\to0,
\qquad
m\alpha_m\to\infty,
\tag{18}
\]

with contraction `r(alpha_m,a_m)<1` and delay support in one fixed corridor `[H,RH+o(H)]`, `R>1`. Suppose its normalized Wiener rate has finite liminf `L`. Choose a subsequence realizing that liminf and fix `M>L+1`.

RE-223's general finite-rate corridor surcharge then bounds `lambda_m=N_m/m` away from zero on this subsequence, while the fixed corridor bounds it above by `R-1+o(1)`. RE-224 gives `a_m<=R+o(1)` whenever `a_m>1`, and the branch `a_m<=1` is already bounded. Hence a fixed `A` works in (17).

If `alpha_m->0` along a further subsequence, (17) forces the normalized Wiener rate to `+infinity`, contradicting the choice of a finite-rate subsequence. Therefore `alpha_m` is bounded away from zero there. RE-225 now prevents `r(alpha_m,a_m)->1`. The contraction condition together with the center bound also keeps `alpha_m` away from `pi/2`, while `lambda_m` remains in a compact positive interval. The triples `(alpha_m,a_m,lambda_m)` consequently lie in a compact subset of the interior domain of RE-222.

RE-222 then supplies a strict compact-interior margin,

\[
\liminf
\frac{\log\|F_m\|_A}{m\alpha_m}
\ge2+\eta
\tag{19}
\]

for some `eta>0` on that subsequence. Since the subsequence realizes `L`, one gets `L>2`. If the original liminf is infinite, the same conclusion is automatic. This proves (6).

The chain RE-222--RE-226 has therefore exhausted the positive-real single-center boundary mechanisms in a fixed corridor: nondegenerate drift, truncation collapse, center escape, contraction-boundary escape, and finally vanishing arcs. None can produce an actual rate-two exact-remainder family.

## 5. Prior-art boundary and falsification checks

The ingredients of the proof are classical and elementary. The incomplete-beta integral identity is already recorded in RE-221; the inequality `||P||_A >= |P(z)|` on the unit circle is immediate from the triangle inequality; and using an anti-aligned unit-circle point to expose coefficient growth is standard polynomial/Wiener-algebra geometry. Broad prior-art search continues to recover the classical superoscillation, band-limited prediction, incomplete-beta, and Wiener-algebra literature already neighboring RE-221--RE-225, but no external theorem is needed for (3)--(19). No `SOURCES.md` update is required.

Several boundaries are important. The proof uses a **positive real** single center; at `z=-1` this makes the numerator in (11) sign-coherent. A genuinely complex center can change that geometry, and RE-220 only radializes absolute-tail estimates, not the exact cancellation-sensitive polynomial. Several centers can also cancel after coefficient recombination, so the parity probe does not transfer directly to a multi-center predictor. The fixed-corridor hypothesis is used to keep the center bounded and the truncation ratio from escaping; broad-corridor families are outside the corollary. Finally, (6) is a representation obstruction before ordinary-prime realization and does not raise the universal `C_sep>=1` lower bound for arbitrary separated measures.

## Research consequence

The vanishing-arc asymptotic problem posed by RE-225 has a simpler answer than expected: **within the fixed-corridor positive-real single-center architecture, shrinking the arc makes the normalized Wiener cost diverge rather than approach two.** The entire real single-center exact-cancellation route to the factor-two boundary is therefore closed family-by-family.

The constructive frontier should now move rather than continue refining real single-center incomplete-beta asymptotics. The live directions are genuinely complex-center exact cancellation, multi-center/minimax geometry, or a different approximation basis. Any improvement toward the global separated-prediction floor `C_sep=1` must use one of those genuinely different geometries rather than another degeneration of the current positive-real single-center representation.
