# PC-275 — fixed-bandwidth centered near-resonance bias is logarithmic-integral data

**Status:** `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the first centered/subleading source-fluctuation escape left open by PC-273/PC-274.

PC-273 proves that, at fixed bandwidth `B`, the raw prime-pair near-resonance law converges to the same continuum law as the all-residue grid control. PC-274 then closes the unscaled raw law at every moving bandwidth, while explicitly leaving centered/subleading source fluctuations as a possible escape.

At fixed `B`, the first such centered layer is still completely classical. Write

\[
D_B(x,y)
:=
\min_{0<\max(|h|,|k|)\le B}
\|hx+ky\|_{\mathbb R/\mathbb Z},
\tag{1}
\]

and let `rho^prime_{q,B}` and `rho^grid_{q,B}` be the unordered distinct-pair laws from PC-273. Then for every fixed integer `B>=1` and every Lipschitz test function `phi:[0,1/2]\to\mathbb R`,

\[
\boxed{
\log q\left(
\int \phi\,d\rho^{\mathrm{prime}}_{q,B}
-
\int \phi\,d\rho^{\mathrm{grid}}_{q,B}
\right)
\longrightarrow
\int_0^1\!\int_0^1
\phi(D_B(x,y))\,
[-2-\log x-\log y]\,dx\,dy.
}
\tag{2}
\]

Equivalently, if

\[
\sigma(dt):=-(1+\log t)\,dt,
\qquad
\sigma([0,1])=0,
\tag{3}
\]

then the first centered signed law is

\[
\boxed{
\kappa_B
:=
(D_B)_*\bigl(\sigma\otimes dt+dt\otimes\sigma\bigr),
}
\tag{4}
\]

and

\[
\log q\,
(\rho^{\mathrm{prime}}_{q,B}-\rho^{\mathrm{grid}}_{q,B})
\Longrightarrow
\kappa_B
\tag{5}
\]

against fixed Lipschitz tests.

Thus the first nonzero correction discarded by the raw weak limit is not a zeta-zero statistic. It is the deterministic first logarithmic-integral correction to the scaled prime density, pushed through the already-classical finite-bandwidth Diophantine observable `D_B`. The same statement holds for the normalized variable `(B+1)^2D_B` when `B` is fixed, because the normalization is then only a constant rescaling.

## 1. The scaled prime source has an explicit first correction

Let

\[
P_q=\{p:2<p<q,\ p\text{ prime}\},
\qquad
M_q=|P_q|,
\qquad
\nu_q=\frac1{M_q}\sum_{p\in P_q}\delta_{p/q},
\tag{6}
\]

and let `m=dt` be Lebesgue probability measure on `[0,1]`.

The prime number theorem in its classical logarithmic-integral form gives, for a fixed Lipschitz function `g`,

\[
\sum_{p<q}g(p/q)
=
q\int_{2/q}^1\frac{g(t)}{\log q+\log t}\,dt
+o\!\left(\frac{q}{(\log q)^2}\right).
\tag{7}
\]

The same formula with `g=1` gives the normalization. Put `L=\log q`. The interval `2/q\le t<q^{-1/2}` has normalized mass `o(L^{-1})`, while on `t\ge q^{-1/2}` one may expand the reciprocal denominator and use the integrability of powers of `|\log t|`. Thus

\[
q\int_{2/q}^1\frac{g(t)}{L+\log t}\,dt
=
\frac qL
\left[
\int_0^1g(t)\,dt
-
\frac1L\int_0^1g(t)\log t\,dt
+O_g(L^{-2})
\right],
\tag{8}
\]

whereas

\[
\operatorname{Li}(q)
=
\frac qL\left(1+\frac1L+O(L^{-2})\right).
\tag{9}
\]

Dividing (8) by (9) yields

\[
\boxed{
\int g\,d\nu_q
=
\int_0^1g(t)\,dt
-
\frac1L
\int_0^1g(t)(1+\log t)\,dt
+O_g(L^{-2})+o_g(L^{-1}).
}
\tag{10}
\]

Omitting the prime `2` changes the normalized average by only `O(L/q)`. Therefore

\[
\boxed{
L(\nu_q-m)\Longrightarrow\sigma,
\qquad
\sigma(dt)=-(1+\log t)dt,
}
\tag{11}
\]

against every fixed Lipschitz test.

This correction is genuinely nontrivial but entirely smooth. For example, with `g(t)=t`,

\[
\int_0^1 t\,\sigma(dt)=-\frac14,
\tag{12}
\]

so the normalized prime source has mean `1/2-1/(4\log q)+o(1/\log q)` before any Prime-Circle observable is applied.

## 2. Fixed-bandwidth pair observables inherit only the product correction

For fixed `B` and fixed Lipschitz `phi`, define

\[
G_B(x,y):=\phi(D_B(x,y)).
\tag{13}
\]

PC-273 proves that `D_B` is `B`-Lipschitz in the source coordinates. Hence `G_B` is a fixed Lipschitz function on `[0,1]^2` once `B` and `phi` are fixed.

Apply the one-dimensional PNT/logarithmic-integral approximation successively in the two variables. Uniformity is harmless because the Lipschitz norm of each slice of `G_B` is bounded by a constant depending only on the fixed pair `(B,phi)`. The ordered prime-pair expectation is therefore, up to `o(L^{-1})`, the normalized logarithmic-integral product

\[
\frac{
q^2\displaystyle\int\!\!\int
\frac{G_B(x,y)}{(L+\log x)(L+\log y)}\,dx\,dy
}{\operatorname{Li}(q)^2}.
\tag{14}
\]

Expanding the two source densities gives

\[
\frac1{(L+\log x)(L+\log y)}
=
\frac1{L^2}
\left[
1-rac{\log x+\log y}{L}+O(L^{-2})
\right]
\tag{15}
\]

in the bulk, with the small-coordinate tails negligible at order `L^{-1}`. Since

\[
\operatorname{Li}(q)^2
=
\frac{q^2}{L^2}
\left(1+\frac2L+O(L^{-2})\right),
\tag{16}
\]

we obtain

\[
\int G_B\,d(\nu_q\otimes\nu_q)
=
\int\!\!\int G_B\,dx\,dy
+
\frac1L
\int\!\!\int
G_B(x,y)[-2-\log x-\log y]\,dx\,dy
+o(L^{-1}).
\tag{17}
\]

The all-residue product grid differs from Lebesgue product measure by `O_{B,phi}(1/q)` for fixed `B`. Passing from ordered product pairs to distinct unordered pairs changes the prime law by `O(1/M_q)=O(L/q)` and the grid law by `O(1/q)`. After multiplication by `L`, all three corrections vanish. Equation (2) follows.

The formula can also be read representation-wise. In source coordinates, the correction is the smooth signed product density in (3). Under the Prime-Circle/dual-lattice representation, `D_B` maps that density to the centered near-resonance law (4). Nothing new is created by changing representation: the geometry transports the classical source bias but does not alter its arithmetic origin.

## 3. Why this is a real closure beyond PC-273 and PC-274

PC-273 established only the zeroth-order statement

\[
\rho^{\mathrm{prime}}_{q,B}
-
\rho^{\mathrm{grid}}_{q,B}
\Longrightarrow0
\qquad(B\text{ fixed}),
\tag{18}
\]

with a quantitative `O(1/\log q)` transport bound. That bound left open the possibility that multiplying the difference by `\log q` might reveal a new prime-circle statistic.

Equation (2) determines that entire first layer. The `1/\log q` scale is already occupied by the deterministic bias of the elementary prime intensity `dt/\log(qt)`. No zero sum, oscillatory explicit-formula term, critical-line exponent, or new spectral datum is needed to produce it.

PC-274's normalized carrier

\[
X_{q,B}=(B+1)^2\Delta_B
\tag{19}
\]

does not escape this conclusion at fixed bandwidth: `(B+1)^2` is constant there, so its first centered law is simply the scalar pushforward of `\kappa_B`. The genuinely unresolved normalized problem is therefore a **moving-bandwidth** problem, where the observable itself changes with `q` and the fixed-test expansion above is no longer uniform.

## 4. Prior-art and novelty audit

The analytic-number-theory input is classical. H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I: Classical Theory*, Cambridge University Press (2006), Chapter 6, develops the prime number theorem and the logarithmic-integral approximation used in (7)--(10); the same PNT source was already recorded in PC-273. The asymptotic expansion of `Li(q)` and partial summation against a fixed test function are standard consequences of that theory.

A targeted search for scaled prime empirical measures, first-order normalized-prime corrections, and second-order PNT formulations found no distinct nonclassical mechanism needed here. The source correction `-(1+\log t)dt` is just the first coefficient obtained by normalizing the classical density `dt/\log(qt)`. No novelty is claimed for the PNT, `Li`, partial summation, weak convergence, or the product-measure expansion.

The durable project-local result is narrower: **the specific first centered source-statistics escape left open by PC-273/PC-274 at fixed Fourier bandwidth is completely determined by that classical logarithmic-integral bias after pushing through the exact Prime-Circle near-resonance observable `D_B`.** It therefore cannot be counted as a new bridge to zeta zeros or the critical line.

No new external source dependency is introduced beyond the PNT reference already used and bibliographically recorded in PC-273, so no additional line-local source anchor is required for this finding.

## 5. What survives after subtracting the smooth bias

The result does not say that every centered source statistic is prime-blind. It identifies only the first deterministic layer at fixed bandwidth. A legitimate continuation must remove or outrun this layer rather than rediscover it.

The principal survivors are:

1. **Moving bandwidth.** If `B=B(q)` grows, the Lipschitz complexity and cell structure of `D_B` grow as well. Equation (2) is not a uniform-in-`B` theorem.
2. **Li-centered residuals.** One may compare the prime source to the normalized logarithmic-integral source itself, rather than to the flat grid. The remaining error is the ordinary PNT remainder; any zeta-zero sensitivity inherited solely through that remainder belongs to the classical explicit-formula channel unless the geometry adds an independent mechanism.
3. **Singular or directional observables.** The minimizing vector `(h,k)`, discontinuous cell labels, shrinking targets, or singular weights can see information not controlled by a fixed Lipschitz pushforward.
4. **Conditioned or nonlocal source coupling.** Conditioning the prime pair or coupling near resonance to another source-forced operator lies outside the fixed product-law calculation.

This sharpens the search boundary: the next useful question is not whether the prime/grid difference has a `1/\log q` term at fixed resolution, but whether anything remains after the exact smooth `Li` bias is removed or after the observation scale itself grows.

## 6. Falsification and audit tests

The statement has direct checks.

1. For a fixed Lipschitz `g`, show that `\log q(\int g\,d\nu_q-\int g\,dt)` converges to anything other than `-\int g(t)(1+\log t)dt`; this would contradict the classical normalized logarithmic-integral expansion.
2. For `g(t)=1`, the correction must vanish because `\int_0^1(1+\log t)dt=0`. Failure would expose a normalization error.
3. For `g(t)=t`, the first coefficient must be `-1/4`, providing a simple one-dimensional numerical check of the sign and normalization.
4. For fixed `B` and fixed Lipschitz `phi`, compute the prime/grid pair difference and multiply by `\log q`. Any limiting value inconsistent with the right side of (2) would falsify the two-variable pushforward step.
5. Let `B` grow with `q`, use a discontinuous minimizer label, or subtract the full normalized `Li` source before centering. These are outside the theorem and are valid continuations rather than counterexamples.

## 7. Consequence for the research line

The fixed-resolution centered route

\[
\text{prime source minus flat control}
\longrightarrow
\log q\text{-magnified near-resonance law}
\longrightarrow
\text{new RH-sensitive signal}
\]

is closed at first order. Its entire limit is the pushforward of the smooth logarithmic-integral density correction (3).

Accordingly, any future Prime-Circle mechanism built from the ordered near-resonance branch must either remove the `Li` profile before looking at fluctuations, let the resolution grow in a way that invalidates the fixed-test asymptotics, retain directional/singular information, or introduce an additional nonlocal coupling. Merely magnifying the fixed-bandwidth prime/grid discrepancy by `\log q` does not expose a new critical-line structure.