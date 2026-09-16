# NB-164 — Growing moment cancellation forces linear Poisson-width support or exponential conditioning

**Date:** 2026-09-16  
**Status:** EXACT-DERIVED + GROWING-MOMENT + CHEBYSHEV-DUAL + CONDITIONING-BOUND + DECISIVE-METHOD-BOUNDARY

`NB-163` closes every fixed finite local moment order: the first uncontrolled absolute moment bounds both the Poisson target and the generic Euler response at the same boundary scale. It deliberately leaves `r=r_G -> infinity` open because its Taylor/Euler constants were only controlled for fixed `r`.

For the target side, growing order can be handled exactly without differentiating the kernel. Moment annihilation is dual to uniform polynomial approximation of the Poisson profile. The relevant Chebyshev series is explicit, and its nearest complex poles force geometric decay in the number of vanished moments. Consequently, a sampler localized to any fixed number of Poisson widths cannot let the cancellation order grow while keeping both bounded conditioning and fixed target visibility. More generally, bounded conditioning forces the support radius to grow at least linearly with the cancellation order measured in Poisson widths.

## Claim

Let `r>=1`, `x>0`, `gamma in R`, and `L>0`. Let `nu` be a finite real signed Borel measure supported in

\[
[\gamma-L,\gamma+L]
\]

and assume that it annihilates every real polynomial of degree below `r`:

\[
\int p(t)\,d\nu(t)=0,
\qquad p\in\mathcal P_{r-1}.
\]

Equivalently, the moments about any chosen center vanish through order `r-1`; in particular this is the growing-order version of the local moment hypothesis in `NB-163`.

Write

\[
V:=\|\nu\|_{\rm TV},
\qquad
C:=\frac{V}{c}
\]

for a positive reference scale `c`, and define the target Poisson response

\[
Q_\nu(x,\gamma)
:=
\int
\frac{x}{x^2+(\gamma-t)^2}
\,d\nu(t).
\]

Set

\[
\delta:=\frac{x}{L},
\qquad
s_\delta:=\sqrt{1+\delta^2},
\qquad
q_\delta:=s_\delta-\delta
=e^{-\operatorname{arsinh}\delta},
\]

and let

\[
d_r:=2\left\lceil\frac r2\right\rceil
\]

be the first even degree not below `r`.

Define

\[
g_\delta(y):=\frac{\delta^2}{\delta^2+y^2},
\qquad -1\le y\le1,
\]

and its degree-`r-1` minimax error

\[
E_{r-1}(\delta)
:=
\inf_{p\in\mathcal P_{r-1}}
\|g_\delta-p\|_{L^\infty[-1,1]}.
\]

Then:

### 1. The target capacity is exactly a polynomial-approximation distance

Among all real signed measures `mu` on `[-1,1]` with `||mu||_TV<=1` and vanishing moments through degree `r-1`,

\[
\boxed{
\sup_\mu
\left|
\int g_\delta(y)\,d\mu(y)
\right|
=
E_{r-1}(\delta).
}
\]

After scaling `t=gamma+Ly`, every admissible `nu` therefore satisfies

\[
\boxed{
\frac{x|Q_\nu(x,\gamma)|}{V}
\le
E_{r-1}(\delta).
}
\]

This is an exact dual capacity statement, not a Taylor estimate.

### 2. The capacity has an explicit geometric Chebyshev envelope

For every `r>=1`,

\[
\boxed{
\frac{\delta}{s_\delta}
q_\delta^{d_r}
\le
E_{r-1}(\delta)
\le
\frac{1}{s_\delta}
q_\delta^{d_r-1}.
}
\]

Hence

\[
\boxed{
\frac{x|Q_\nu(x,\gamma)|}{c}
\le
\frac{C}{s_\delta}
\exp\!\left(
-(d_r-1)\operatorname{arsinh}\frac{x}{L}
\right).
}
\]

If the sampler must retain a fixed fraction `eta>0` of the natural target scale,

\[
|Q_\nu(x,\gamma)|
\ge
\eta\frac{c}{x},
\]

then necessarily

\[
\boxed{
C
\ge
\eta s_\delta
\exp\!\left(
(d_r-1)\operatorname{arsinh}\frac{x}{L}
\right).
}
\]

For every fixed ratio `L/x`, the lower and upper Chebyshev bounds have the same exponential rate. Thus the exponential conditioning law is sharp up to constants depending only on that fixed ratio and the parity of `r`.

### 3. Fixed-width localization forces exponential conditioning

Suppose

\[
L\le\Lambda x
\]

for a fixed `Lambda>0`. Put

\[
q_\Lambda
:=
\sqrt{1+\Lambda^{-2}}-\Lambda^{-1}
<1.
\]

Since `delta>=1/Lambda` and `q_delta` decreases with `delta`,

\[
\boxed{
\frac{x|Q_\nu(x,\gamma)|}{c}
\le
C q_\Lambda^{r-1}.
}
\]

Therefore fixed target visibility implies

\[
\boxed{
C
\ge
\eta
\exp\!\left(
(r-1)\operatorname{arsinh}(\Lambda^{-1})
\right).
}
\]

In particular, at exactly one Poisson radius, `L=x`,

\[
q_1=\sqrt2-1,
\qquad
q_1^{-1}=1+\sqrt2,
\]

so increasing moment order costs a factor asymptotic to a power of `1+sqrt(2)` in total-variation conditioning. Bounded, polynomial, or otherwise subexponential conditioning cannot support `r->infinity` while the sampler remains within a fixed number of Poisson widths and retains natural-scale target gain.

### 4. Bounded conditioning forces support to spread linearly in the moment order

The preceding estimate can be inverted before fixing `L/x`. If

\[
|Q_\nu(x,\gamma)|
\ge
\eta\frac{c}{x}
\]

and `C>eta`, then

\[
(r-1)\operatorname{arsinh}\frac{x}{L}
\le
\log\frac C\eta.
\]

Thus

\[
\boxed{
\frac{L}{x}
\ge
\frac{1}
{\sinh\!\left(\dfrac{\log(C/\eta)}{r-1}\right)}.
}
\]

For fixed `C/eta>1`, this gives

\[
\boxed{
\frac{L}{x}=\Omega(r).
}
\]

More generally, if `log C=o(r)`, then the support radius in Poisson units must diverge; if `C` is polynomial in `r`, the necessary scale is at least `L/x=Omega(r/log r)`. Growing cancellation order therefore cannot remain a genuinely local one-width architecture unless it pays exponential conditioning.

## Derivation

### Exact annihilator/minimax duality

Push `nu` forward by

\[
y=\frac{t-\gamma}{L}.
\]

The resulting signed measure `mu` is supported on `[-1,1]`, has the same total variation, and annihilates `P_{r-1}`. Moreover

\[
xQ_\nu(x,\gamma)
=
\int g_\delta(y)\,d\mu(y).
\]

For every polynomial `p` of degree below `r`,

\[
\int g_\delta\,d\mu
=
\int(g_\delta-p)\,d\mu,
\]

so

\[
\left|
\int g_\delta\,d\mu
\right|
\le
\|\mu\|_{\rm TV}
\|g_\delta-p\|_\infty.
\]

Taking the infimum over `p` proves the upper half of the capacity identity. Conversely, the quotient norm of `g_delta + P_{r-1}` in `C[-1,1]/P_{r-1}` equals its distance to `P_{r-1}`. Hahn--Banach supplies a norm-one functional annihilating `P_{r-1}` and attaining that quotient norm; the Riesz representation theorem realizes the functional as a real signed measure of total variation one. This proves the reverse inequality and hence the exact capacity identity.

### Explicit Chebyshev series

Put `y=cos theta`. Then

\[
g_\delta(\cos\theta)
=
\frac{\delta^2}
{\delta^2+\tfrac12+\tfrac12\cos(2\theta)}.
\]

With `s=s_delta` and `q=q_delta`, the elementary Fourier expansion of `1/(A+B cos phi)` gives

\[
\boxed{
g_\delta(y)
=
\frac{\delta}{s}
\left[
1+2\sum_{n\ge1}
(-q^2)^nT_{2n}(y)
\right].
}
\]

Only even Chebyshev modes occur. Truncating immediately before the first even degree `d_r` not annihilated by the degree restriction yields

\[
E_{r-1}(\delta)
\le
\frac{2\delta}{s}
\sum_{n\ge d_r/2}q^{2n}
=
\frac{2\delta}{s}
\frac{q^{d_r}}{1-q^2}.
\]

Since

\[
1-q^2=2\delta q,
\]

this is exactly

\[
E_{r-1}(\delta)
\le
\frac{q^{d_r-1}}{s}.
\]

For the lower bound, every polynomial of degree below `r` has zero Chebyshev coefficient in degree `d_r`. The `d_r` coefficient of `g_delta` has magnitude

\[
\frac{2\delta}{s}q^{d_r}.
\]

For any continuous `h`, a nonconstant Chebyshev coefficient has magnitude at most `2||h||_infty`. Applying this to `h=g_delta-p` gives

\[
E_{r-1}(\delta)
\ge
\frac{\delta}{s}q^{d_r}.
\]

This also identifies the geometric factor as the Bernstein-ellipse distance to the two poles `y=+-i delta`: `q_delta=exp(-arsinh delta)`.

## Why this is stronger than the fixed-order Taylor bound

`NB-163` uses

\[
M_r\le VL^r
\]

and therefore only obtains `Xi_r<=C(L/a)^r`. At `L asymp a` that expression is merely `O(C)` and supplies no decay, while its Euler-side constants are not uniform when `r` grows.

The minimax argument does not estimate the `r`-th Taylor remainder. It removes the **best polynomial of every degree below `r`** from the target kernel at once. Because the Poisson profile is analytic and its nearest poles stay a fixed scaled distance from a fixed-width interval, its polynomial quotient norm decays geometrically even when `L` equals the Poisson width. No Euler estimate and no assumption about prime phases enters this conclusion.

Consequently, even perfect zeta-specific cancellation on the Euler side cannot rescue an increasing-order sampler that stays within `O(1)` Poisson widths with bounded conditioning: the target itself has already become exponentially invisible. The increasing-order escape from `NB-163` is therefore converted into one of two already visible resources—nonlocal support growth or worsening conditioning.

## Prior-art and novelty audit

The functional-analytic identity between distance to a finite-dimensional polynomial subspace and norm-one annihilating functionals is classical Hahn--Banach duality, and geometric convergence of Chebyshev approximation for analytic functions is classical approximation theory. Standard modern expositions also describe Bernstein-ellipse control and exact Chebyshev coefficients for functions with poles. No novelty is claimed for those ingredients separately.

A fresh search around best polynomial approximation, annihilating measures, Chebyshev coefficients of rational kernels, Bernstein ellipses, vanishing moments, and Poisson kernels found those standard mechanisms but no source giving the line-specific consequence above: increasing local moment order in a signed exterior zeta sampler forces either exponential total-variation conditioning at fixed Poisson-width support or support growth at least linear in the moment order for bounded conditioning. The proof is self-contained, and no new external theorem is load-bearing beyond standard Hahn--Banach/Riesz and elementary Chebyshev/Fourier identities, so `SOURCES.md` requires no new anchor.

## Boundaries and failure modes

This result is a target-side obstruction. It does **not** say that source-specific von Mangoldt phase cancellation is impossible at a fixed or slowly growing moment order. That genuinely arithmetic regime remains open.

The localization radius is measured about the target ordinate. If a sampler is originally described relative to another local center, moment annihilation itself is translation invariant, while the theorem applies with the actual radius needed to contain the support about the target. A deliberately nonlocal sampler with `L/x` growing on the order required above is outside the fixed-width conclusion by design.

The sharp exponential statement is for a fixed scaled radius `L/x`; the lower Chebyshev bound proves that the exponent cannot be improved uniformly there from moment annihilation and total variation alone. When `L/x->infinity`, the theorem supplies the stated necessary spreading law but does not claim that this spreading is sufficient to preserve a useful arithmetic sampler.

Finally, the result concerns the exterior signed Poisson architecture of `NB-154` onward. It neither proves an RH implication nor replaces the source-faithful finite-section analysis of the original Nyman--Beurling approximation problem.

## Source map

- `NB-161`: collapsing Jordan transport loses target gain at fixed horizontal scale.
- `NB-162`: the scale-invariant first-order transport currency `Theta=C ell/a` leaves one-Poisson-width interlacing as the bounded-conditioning regime.
- `NB-163`: every fixed finite vanishing-moment order shares one generic target/Euler moment currency but leaves `r->infinity` open.

## Consequence for the line

The increasing-order local-moment escape left by `NB-163` is closed at bounded conditioning. **A signed sampler that annihilates `r` polynomial modes and remains inside any fixed number of Poisson widths has target capacity decaying geometrically in `r`; fixed target visibility therefore requires exponentially growing total variation.** If conditioning stays bounded, the support radius must instead grow at least linearly with `r` in Poisson units.

The bounded-conditioning frontier is now narrower: one-width local interlacing can only remain viable by exploiting genuinely source-specific arithmetic cancellation at bounded/controlled effective order, not by piling up arbitrarily many local vanishing moments. Increasing-order constructions must become nonlocal, and nonlocality itself is now quantitatively priced against the cancellation order.