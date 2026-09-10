# RE-029 — threshold-tangent selectors force an opposite-sign standard prime-race cone

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + THRESHOLD-TANGENT-CA + STANDARD-PRIME-RACE-CONE + SAME-PARAMETER-SELECTION + PRIOR-ART-ALIGNED`. `RE-027` shows that Robin's quantitative false-RH witnesses can be selected by a moving tangent so that the external CA event coordinate `Z` has a prescribed super-square-root defect `D(Z)=Z-\Phi(Z)`. `RE-028` then shows that the same selected CA states force a divergent endpoint-subtracted Mertens--Chebyshev mixed race at their largest active first-layer primes. The source defect can be decomposed more directly: at the **same real event parameters `Z`**, the ordinary Chebyshev error is forced negative at the full defect scale while the ordinary logarithmic Mertens-product error is forced positive at the complementary threshold scale.

Assume RH is false and put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12.
\tag{1}
\]

Fix

\[
1-\Theta<b<\frac12.
\tag{2}
\]

Let `c_b>0` and the infinite threshold-tangent CA sequence `C` be as in `RE-027`--`RE-028`. Write

\[
Y:=\log C,
\qquad
\tau_b(Y):=\log(1+c_bY^{-b}),
\tag{3}
\]

and let `Z>Y` be the external event coordinate determined by

\[
\frac1{Z\log Z}
=
\frac1{Y\log Y}
-
\frac{b c_b}{Y(Y^b+c_b)}.
\tag{4}
\]

Then

\[
Y=\Phi(Z),
\qquad
D(Z):=Z-Y
\sim b c_b Z^{1-b}\log Z,
\tag{5}
\]

and

\[
\log G(C)-\gamma\ge\tau_b(Y).
\tag{6}
\]

For real `x>=2`, use the standard normalized errors already fixed in `RE-009`,

\[
\mathcal E_{\vartheta}(x)
:=\frac{\vartheta(x)-x}{\sqrt x},
\tag{7}
\]

\[
E(x)
:=
\sum_{r\le x}-\log(1-r^{-1})-\gamma-\log\log x,
\qquad
\mathcal E_{\pi_\ell}(x):=E(x)\sqrt x\log x.
\tag{8}
\]

Along the threshold-selected sequence one has

\[
\boxed{
\vartheta(Z)-Z
=-(1+o(1))D(Z)
=-(b c_b+o(1))Z^{1-b}\log Z.
}
\tag{9}
\]

At the same parameters,

\[
\boxed{
E(Z)
\ge
\bigl((1-b)c_b+o(1)\bigr)Z^{-b}.
}
\tag{10}
\]

Consequently

\[
\boxed{
\mathcal E_{\vartheta}(Z)
=-(b c_b+o(1))Z^{1/2-b}\log Z
\longrightarrow-\infty,
}
\tag{11}
\]

while

\[
\boxed{
\mathcal E_{\pi_\ell}(Z)
\ge
\bigl((1-b)c_b+o(1)\bigr)Z^{1/2-b}\log Z
\longrightarrow+\infty.
}
\tag{12}
\]

In particular the selected points enter the opposite-sign cone

\[
\boxed{
\liminf
\frac{\mathcal E_{\pi_\ell}(Z)}{-\mathcal E_{\vartheta}(Z)}
\ge\frac{1-b}{b}.
}
\tag{13}
\]

Equivalently, eliminating `c_b`,

\[
Z-\vartheta(Z)=(1+o(1))D(Z)
\tag{14}
\]

and

\[
\boxed{
E(Z)
\ge
\left(\frac{1-b}{b}+o(1)\right)
\frac{D(Z)}{Z\log Z}.
}
\tag{15}
\]

Thus the moving-threshold reduction does not merely force a large abstract prime-layer discrepancy or a mixed error at a nearby boundary prime. It selects infinitely many exact event parameters where the two **ordinary** prime errors themselves point in opposite directions with a quantitative slope fixed by the threshold exponent `b`.

## 1. First-layer event mass differs from `vartheta(Z)` by at most one endpoint prime

Split the event measure into first and higher layers,

\[
\Phi(Z)=\Phi_1(Z)+\Phi_{\ge2}(Z).
\tag{16}
\]

The first-layer localization from `RE-006` gives, for every prime `r`,

\[
r\le\eta_{r,1}<r+1.
\tag{17}
\]

Hence every prime `r<=Z-1` has its first layer active at `Z`, while no prime `r>Z` can have its first layer active. The only possible discrepancy between the active first-layer primes and the ordinary primes `r<=Z` is therefore a prime in `(Z-1,Z]`. Since this interval contains at most one integer, there exists a quantity `delta_theta(Z)` with

\[
0\le\delta_\vartheta(Z)\le\log Z
\tag{18}
\]

such that

\[
\boxed{
\Phi_1(Z)=\vartheta(Z)-\delta_\vartheta(Z).
}
\tag{19}
\]

Endpoint conventions at a first-layer event only change `delta_theta` within the same bound and are negligible below.

Using `Y=Phi(Z)` and `D(Z)=Z-Phi(Z)`, equations (16) and (19) give the exact decomposition

\[
\boxed{
Z-\vartheta(Z)
=D(Z)+\Phi_{\ge2}(Z)-\delta_\vartheta(Z).
}
\tag{20}
\]

This removes the ordinary-prime-gap term that appears when the same geometry is expressed at the largest active boundary prime `p`. The comparison is made at the external event coordinate itself.

## 2. Higher layers are negligible against the forced off-critical defect

Only a coarse event-count estimate is needed. The active-layer condition from `RE-013` gives, for every active `(r,j)`,

\[
r^j\log r\le Z\log Z.
\tag{21}
\]

For `j=2`, Chebyshev's elementary bound `vartheta(u)=O(u)` yields

\[
\Phi_2(Z)=O\!\left(\sqrt{Z\log Z}\right).
\tag{22}
\]

For `j>=3`, equation (21), together with the elementary bound `j=O(log Z)`, gives

\[
\Phi_{\ge3}(Z)
=O\!\left(Z^{1/3}(\log Z)^{4/3}\right).
\tag{23}
\]

Thus

\[
\boxed{
\Phi_{\ge2}(Z)=O\!\left(\sqrt{Z\log Z}\right).
}
\tag{24}
\]

The sharper all-logarithmic second-layer analysis of `RE-016` is consistent with (24), but is not needed here. By (5) and `b<1/2`,

\[
\frac{D(Z)}{\sqrt{Z\log Z}}
\asymp_b Z^{1/2-b}\sqrt{\log Z}
\longrightarrow+\infty.
\tag{25}
\]

Equations (18), (20), (24), and (25) prove

\[
Z-\vartheta(Z)=D(Z)(1+o(1)),
\tag{26}
\]

which is (9) and hence (11). No short-interval prime theorem is used. In particular, the `0.52` prime-gap boundary needed to move between `Z` and a specific frontier prime plays no role in this same-parameter statement.

## 3. The finite Euler product forces the ordinary Mertens error positive

Let

\[
\pi_\ell(Z):=
\sum_{r\le Z}-\log(1-r^{-1}).
\tag{27}
\]

The same first-layer endpoint comparison used above applies with the Euler-product weight. There is a quantity `delta_l(Z)>=0` satisfying

\[
\delta_\ell(Z)=O(Z^{-1})
\tag{28}
\]

such that the first-layer Euler product of the selected CA state is

\[
\sum_{\eta_{r,1}<Z}-\log(1-r^{-1})
=\pi_\ell(Z)-\delta_\ell(Z).
\tag{29}
\]

As in `RE-028`, define the finite exponent tail

\[
T(C):=-\sum_{r\mid C}\log(1-r^{-(a_r+1)})\ge0.
\tag{30}
\]

The exact factorization of `sigma(C)/C` now gives

\[
\log G(C)-\gamma
=
E(Z)-\delta_\ell(Z)-T(C)
+\log\frac{\log Z}{\log Y}.
\tag{31}
\]

Therefore

\[
\boxed{
E(Z)
=
\log G(C)-\gamma
+T(C)+\delta_\ell(Z)
-\log\frac{\log Z}{\log Y}.
}
\tag{32}
\]

The signs are load-bearing. The exponent tail and possible missing endpoint-prime contribution are both nonnegative after solving for `E(Z)`; the only cost of normalizing the Mertens product at `Z` rather than the Robin denominator at `Y` is the final logarithmic displacement.

Because `Y/Z->1`, the mean-value theorem gives

\[
\log\frac{\log Z}{\log Y}
=
\int_Y^Z\frac{dt}{t\log t}
=(1+o(1))\frac{D(Z)}{Z\log Z}.
\tag{33}
\]

Using (5),

\[
\boxed{
\log\frac{\log Z}{\log Y}
=(b c_b+o(1))Z^{-b}.
}
\tag{34}
\]

On the other hand, the threshold-selected height satisfies (6), and

\[
\tau_b(Y)
=c_bY^{-b}+O(Y^{-2b})
=(c_b+o(1))Z^{-b}.
\tag{35}
\]

Dropping the two nonnegative terms in (32) and combining (34)--(35) gives

\[
E(Z)
\ge
\bigl((1-b)c_b+o(1)\bigr)Z^{-b},
\tag{36}
\]

which proves (10). Multiplying by `sqrt(Z) log Z` proves (12). Since `0<b<1/2`, the coefficient `(1-b)c_b` is strictly positive and the normalized excursion diverges.

## 4. The threshold exponent fixes a standard two-error cone

Equations (11)--(12) concern the exact pair of normalized errors used by Bhattacharya--Martin--Simpson. Since (11) is an asymptotic equality and `c_b>0`, division yields (13). Combining (5), (26), and (36) instead gives the source-coordinate form (14)--(15).

The coefficient split has a simple geometric origin. The moving Robin threshold contributes `c_b Z^{-b}` to the selected height. Moving the normalization point from the intrinsic size `Y` to the external event parameter `Z` costs asymptotically

\[
\frac{D(Z)}{Z\log Z}
\sim b c_b Z^{-b}.
\tag{37}
\]

The remaining fraction `(1-b)c_b Z^{-b}` must therefore survive in the ordinary Mertens-product error. Simultaneously, the event identity `Y=Phi(Z)` converts the same displacement `D` into a negative ordinary Chebyshev error at `Z`, because all higher event layers are only square-root scale.

For a fixed

\[
0<\varepsilon<\Theta-\frac12
\tag{38}
\]

one may choose

\[
b=1-\Theta+\varepsilon.
\tag{39}
\]

Then the selected sequence satisfies

\[
\mathcal E_\vartheta(Z)
= -\Omega_\varepsilon\!\left(
Z^{\Theta-1/2-\varepsilon}\log Z
\right),
\tag{40}
\]

and

\[
\mathcal E_{\pi_\ell}(Z)
= \Omega_{+,\varepsilon}\!\left(
Z^{\Theta-1/2-\varepsilon}\log Z
\right)
\tag{41}
\]

at the **same** threshold-selected parameters. The selected sequence and constants depend on `b`, exactly as in Robin's quantitative theorem.

## 5. Relation to `RE-028`

`RE-028` proves at the largest active first-layer prime `p` that

\[
\mathscr Y(p)
=\mathcal E_{\pi_\ell}(p)-\mathcal E_\vartheta(p)+o(1)
\gg_b p^{1/2-b}\log p.
\tag{42}
\]

That statement has an advantage: it places the mixed race on actual boundary primes, which is the natural coordinate for the self-tangent selector and event-ladder geometry. Moving from `Z` to `p`, however, requires short-interval control because the standard error functions jump at primes.

The present result makes the complementary choice. It stays at the exact external event coordinate `Z`, where `D=Z-Phi(Z)` is defined. This removes the prime-gap transport completely and separates the mixed source condition into the two standard observables (11)--(12). In particular, `RE-028` should not be read as arising from an arbitrary cancellation between a large positive Mertens error and a large positive Chebyshev error: at the event coordinate itself, the selected geometry forces the Chebyshev component to have the **opposite** sign.

Using the unconditional dictionary of `RE-009`, equations (11)--(12) also imply

\[
\mathscr Y(Z)
\ge(c_b+o(1))Z^{1/2-b}\log Z,
\tag{43}
\]

but (43) is not the main delta. The stronger information is the resolved same-parameter cone rather than only its difference coordinate.

## 6. Stress tests and failure modes

The first-layer endpoint mismatch is explicitly retained through `delta_theta` and `delta_l`; no assertion that event thresholds equal ordinary primes is used. Tied events do not affect the asymptotic conclusion because a possible first-layer endpoint discrepancy is at most one prime, while higher-layer ties are already included in `Phi_(>=2)` and in the nonnegative exponent tail.

The proof does not assume RH-quality control of `theta`, the Mertens product, or prime gaps. The only size estimate on the event correction is the elementary `Phi_(>=2)=O(sqrt(Z log Z))`, which is negligible because the defect forced by the moving threshold is super-square-root for every `b<1/2`.

The result is conditional on hypothetical RH failure through Robin's quantitative theorem. It does not give an unconditional sign theorem for either standard error, nor does it assert that arbitrary negative Chebyshev excursions are accompanied by positive Mertens excursions. The cone occurs only on the sparse parameters selected by the threshold-tangent CA extremum.

Likewise, (13) is a necessary condition, not a contradiction. Under false RH the normalized standard error terms can have power-scale excursions; a global attempt to forbid their mixed difference would be RH-equivalent by `RE-009`. Any closing argument must use the additional CA selection of the points `Z`.

## 7. Prior art and research consequence

The ordinary Mertens product and its two-sided oscillation are classical; Diamond--Pintz is already anchored in `SOURCES.md`. Bhattacharya--Martin--Simpson are direct current prior art for the joint normalized `theta`/`pi_l` errors and for the fact that global one-sided control of their difference is RH-equivalent. Recent CA-window work also combines explicit Chebyshev and Mertens-product estimates with the elementary bound of `sigma(n)/n` by a prime Euler product. No novelty is claimed for those ingredients, the factorization (31), or for global false-RH oscillations of the standard errors.

A targeted literature search did not locate the specific moving-threshold consequence proved here: Robin's quantitative CA selector simultaneously fixes `D(Z)`, forces `theta(Z)-Z` negative at asymptotically the same scale, and leaves at least the complementary `(1-b)` fraction in the positive logarithmic Mertens error at the **same event parameters**. This is the repository-level delta. No new load-bearing external theorem is introduced, so `SOURCES.md` does not need expansion.

The next source-side target can therefore be stated without the artificial endpoint subtraction: determine whether the threshold-tangent CA event set can support the cone

\[
\mathcal E_\vartheta(Z)\sim-bc_b Z^{1/2-b}\log Z,
\qquad
\mathcal E_{\pi_\ell}(Z)\ge(1-b)c_b Z^{1/2-b}\log Z
\tag{44}
\]

infinitely often. A theorem excluding this cone **conditioned on the CA event selector**, or deriving an incompatible event-ladder signature from the same `Z`, would attack the false-RH witness without requiring a global RH-equivalent error bound.