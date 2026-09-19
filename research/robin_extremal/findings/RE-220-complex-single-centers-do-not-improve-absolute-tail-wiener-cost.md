# RE-220 — Complex single centers do not improve absolute-tail Wiener cost

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + COMPLEX-CENTER-REDUCTION + WIENER-NORM-REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDIT`.

**Parent findings:** RE-216, RE-217, RE-218, RE-219.

RE-219 proves a factor-two Wiener floor for the single-positive-real-center negative-binomial predictor when its discarded tail is certified termwise in absolute value. It leaves complex expansion centers as an explicit possible escape. That escape is illusory inside the same absolute-tail architecture.

Let `a` be any nonzero complex center, put `rho=|a|`, and consider

\[
z^{-m}
=
 a^{-m}\left(1-\frac{a-z}{a}\right)^{-m}
=
\sum_{k\ge0}
\binom{m+k-1}{k}a^{-m-k}(a-z)^k
\tag{1}
\]

on the symmetric arc

\[
\mathcal A_\alpha
=
\{e^{-i\theta}:|\theta|\le\alpha\}.
\tag{2}
\]

Truncate (1) at degree `N`, control the remainder by the sum of the absolute values of the omitted negative-binomial terms, multiply by `z^m`, and measure the resulting predictor by the coefficient Wiener norm, exactly as in RE-216--RE-219.

Then replacing the complex center `a` by the positive real center `rho=|a|` has two simultaneous properties:

\[
\boxed{
 r(\rho,\alpha)\le r(a,\alpha),
}
\tag{3}
\]

where

\[
 r(a,\alpha)
:=
\max_{|\theta|\le\alpha}
\frac{|a-e^{-i\theta}|}{|a|},
\tag{4}
\]

and

\[
\boxed{
\|P_{m,N,a}\|_{A}
=
\|P_{m,N,\rho}\|_{A},
}
\tag{5}
\]

where `P` denotes the truncated polynomial before the harmless final DC normalization and `||.||_A` is the `ell^1` norm of its monomial coefficients.

Thus every complex-center predictor whose remainder vanishes under the same absolute-tail certificate has a positive-real-center comparator with no worse certified error, identical support geometry, and exactly the same Wiener cost. Consequently the RE-219 floor already covers **all complex single centers** in this architecture:

\[
\boxed{
\liminf
\frac{\log\|\mu_T\|_{TV}}{HT}
\ge2.
}
\tag{6}
\]

If `C_(1c,abs,C)` denotes the optimal leading exponent when the single expansion center is allowed to be complex, then

\[
\boxed{
2\le C_{1c,abs,\mathbb C}\le5.996390.
}
\tag{7}
\]

The upper bound is still supplied by the real-center construction of RE-218. The new point is structural: **complex phase of a single Taylor center cannot lower either side of the error-versus-Wiener tradeoff that RE-219 prices.** Any improvement below the factor-two floor must use several centers, a different approximation basis, or a remainder argument that exploits cancellation rather than termwise absolute domination.

## 1. Symmetry of the observed arc makes the positive real center minimax at fixed modulus

Write

\[
a=\rho e^{i\varphi},
\qquad \rho>0.
\tag{8}
\]

For the two endpoints of the symmetric arc,

\[
\begin{aligned}
|a-e^{-i\alpha}|^2
&=\rho^2+1-2\rho\cos(\varphi+\alpha),\\
|a-e^{ i\alpha}|^2
&=\rho^2+1-2\rho\cos(\varphi-\alpha).
\end{aligned}
\tag{9}
\]

The smaller of the two endpoint cosines is no larger than their average. Since

\[
\frac{
\cos(\varphi+\alpha)+\cos(\varphi-\alpha)
}{2}
=
\cos\varphi\cos\alpha
\le
\cos\alpha,
\tag{10}
\]

at least one endpoint satisfies

\[
|a-e^{\pm i\alpha}|^2
\ge
\rho^2+1-2\rho\cos\alpha.
\tag{11}
\]

The right side is exactly the squared endpoint distance for the positive real center `rho`. Hence

\[
\max_{|\theta|\le\alpha}|a-e^{-i\theta}|
\ge
\sqrt{\rho^2+1-2\rho\cos\alpha}.
\tag{12}
\]

For the positive real center, the distance from `rho` to the unit-circle arc is monotone in `|theta|`, so its maximum is attained at the endpoints and equals the right side of (12). Dividing by `rho` proves (3).

This comparison is pointwise in `rho`, `alpha`, `m`, and `N`. In particular, if a complex center satisfies the full-arc contraction condition `r(a,alpha)<1`, then the radial center `rho` also satisfies it and has a weakly better contraction factor.

## 2. Complex phase creates no hidden cancellation in the Wiener norm

The less obvious part is the coefficient norm. One might hope that a complex center changes the phases of different negative-binomial terms and permits cancellation after they are re-expanded in powers of `z`. It does not.

Let

\[
P_{m,N,a}(z)
:=
\sum_{k=0}^{N}
\binom{m+k-1}{k}a^{-m-k}(a-z)^k.
\tag{13}
\]

Expanding `(a-z)^k` gives

\[
\begin{aligned}
P_{m,N,a}(z)
&=
\sum_{j=0}^{N}c_j(a)z^j,\\
c_j(a)
&=
(-1)^j a^{-m-j}
\sum_{k=j}^{N}
\binom{m+k-1}{k}
\binom{k}{j}.
\end{aligned}
\tag{14}
\]

For each fixed output degree `j`, every contribution from `k>=j` therefore has **exactly the same phase** `(-1)^j a^{-m-j}`. The complex argument of the center factors out rather than generating cancellation. Consequently

\[
|c_j(a)|
=
\rho^{-m-j}
\sum_{k=j}^{N}
\binom{m+k-1}{k}
\binom{k}{j}.
\tag{15}
\]

Summing over `j` and reversing the finite sums gives the exact identity

\[
\begin{aligned}
\|P_{m,N,a}\|_A
&=
\sum_{j=0}^{N}|c_j(a)|\\
&=
\rho^{-m}
\sum_{k=0}^{N}
\binom{m+k-1}{k}
\left(1+\frac1\rho\right)^k.
\end{aligned}
\tag{16}
\]

The right side depends only on `rho=|a|`; it is precisely the coefficient norm of the polynomial with positive real center `rho`. This proves (5).

Multiplication by `z^m` merely shifts all exponents, so it leaves the coefficient `ell^1` norm unchanged and gives the same delay set for `a` and `rho`. Thus complex phase buys neither a cheaper coefficient vector nor a different support corridor.

## 3. The absolute-tail certificate is also radially dominated

For `z` on the observed arc, the magnitude of the `k`th omitted term is

\[
\binom{m+k-1}{k}
\rho^{-m}
\left(
\frac{|a-z|}{\rho}
\right)^k.
\tag{17}
\]

Therefore the same termwise certificate used in RE-216--RE-219 is bounded by

\[
E_{m,N}(a)
\le
\rho^{-m}
\sum_{k>N}
\binom{m+k-1}{k}
 r(a,\alpha)^k.
\tag{18}
\]

For the radial center `rho`, the identical estimate has `r(rho,alpha)` in place of `r(a,alpha)`. Equation (3) therefore gives

\[
E_{m,N}(\rho)
\le
E^{\rm abs}_{m,N}(\rho)
\le
E^{\rm abs}_{m,N}(a),
\tag{19}
\]

where the superscript emphasizes the termwise absolute certificate rather than the possibly smaller cancellation-sensitive analytic remainder.

Hence, whenever a complex-center family has vanishing uniform error **by this absolute-tail argument**, its positive-real radialization has vanishing uniform error with the same `m,N`, the same output degrees, and the same Wiener norm. If exact DC normalization is imposed after truncation, both truncated predictors differ from one at `t=0` by `o(1)`, so the two normalization factors are `1+o(1)` and cannot change the leading exponent.

Applying RE-219 to the radial comparator proves (6)--(7).

## 4. Representation audit and falsification controls

This is a representation result, not a new source-rigidity theorem. It says that allowing one complex expansion center does not enlarge the effective single-center **absolute-tail negative-binomial** class. The global separated-prediction interval remains

\[
1\le C_{\rm sep}\le5.996390;
\tag{20}
\]

RE-220 does not raise its lower endpoint and does not alter the ordinary-prime realization of RE-208.

The decisive scope boundary is the remainder certificate. Equation (19) compares termwise absolute tails. A contour estimate, minimax polynomial, incomplete-binomial analysis, or another argument that uses cancellation among the discarded complex terms is not covered. Likewise several centers can interfere at the final coefficient level and are not reduced by (14)--(16).

A useful negative control is to break the symmetry of the observed arc. On a one-sided arc, for example `theta in [0,alpha]`, rotating a center toward the arc midpoint can reduce its maximum geometric distance compared with the positive real center of the same modulus. Thus (3) is not a generic statement that complex centers are useless; it depends on the symmetric frequency window of the present predictor problem. This is exactly the relevant geometry for RE-216--RE-219, where the approximation is required uniformly on `[-T,T]`.

Another possible objection is that a complex center might reduce the **actual** polynomial `ell^1` norm despite leaving its triangle-inequality estimate unchanged. Equation (14) rules that out exactly: at every output degree the center phase is common to all contributing truncation levels, so (16) is the true coefficient norm, not an upper bound.

The prior-art audit again finds classical one-sided band-limited prediction, Newton/Chebyshev predictor constructions, and work on accelerating negative-binomial series. None supplies or is needed for (3)--(19). The radial minimax comparison is elementary symmetry of a circular arc, while the coefficient identity is an exact specialization of the RE-216 expansion. No novelty is claimed for Taylor expansion about a complex point or for band-limited prediction in general, and no new load-bearing external source is added to `SOURCES.md`.

## Research consequence

RE-219 listed complex centers, several centers, non-binomial bases, and cancellation-sensitive remainder control as possible exits from its factor-two representation floor. RE-220 removes the first of those exits completely within the same absolute-tail architecture.

The reason is stronger than a heuristic preference for a real center. At fixed modulus, radialization **simultaneously improves the worst-case tail contraction and preserves the exact Wiener norm**. Complex phase therefore has no tradeoff to exploit. The next meaningful constructive test should move to genuinely multi-center/minimax geometry or to a tail analysis that retains complex cancellation; further exploration of a lone complex Taylor center cannot lower the leading Wiener cost already bounded in RE-219.
