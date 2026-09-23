# FD-284 — Prime phases preserve a signed outer Perron strip plateau below square-root height

- **Date:** 2026-09-23
- **Status:** proved RH-conditional route-narrowing bound
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** grouped Perron collar / signed horizontal contour / prime self-divisor coordinates / RH prime-density input / route narrowing
- **Depends on:** FD-261, FD-282, FD-283
- **Classification:** `LITERATURE+DERIVED + RH-CONDITIONAL + SIGNED-PERRON-LOWER-BOUND + PRIME-PHASE-WITNESS + ROUTE-NARROWING`

## Claim

FD-283 reduces every strict-right horizontal Perron subcollar to a genuinely signed Möbius Mellin average, leaving open the possibility that coefficient cancellation makes that signed field polynomially smaller than the absolute plateau of FD-282. On a fixed thin strip at the **outer edge** of the usual Perron collar, prime self-divisor coordinates rule out that possibility through square-root spectral height.

Assume the Riemann hypothesis, let

\[
x=N^{\lambda+o(1)},\qquad \lambda>0,
\tag{1}
\]

put

\[
L:=\log(2Nx),\qquad
c:=1+\frac1L,
\tag{2}
\]

and fix a sufficiently small constant `kappa>0`. Set

\[
b:=c-\frac{\kappa}{L}
 =1+\frac{1-\kappa}{L}.
\tag{3}
\]

For `s=sigma+iT`, keep the grouped physical kernel

\[
K_s(d)
:=\sum_{q\mid d}\frac{q^s-(q-1)^s}{s}
 =\sum_{q\mid d}\int_{q-1}^{q}u^{s-1}\,du,
\tag{4}
\]

and define the upper/lower-paired signed field contributed only by the outer strip `[b,c]` by

\[
\mathcal H_d^{\rm out}(T)
:=-\frac1\pi\operatorname{Im}
\int_b^c
\frac{N^{\sigma+iT}K_{\sigma+iT}(d)}
     {\zeta(\sigma+iT)}\,d\sigma.
\tag{5}
\]

Then for every fixed `epsilon in (0,1/2)`, uniformly in

\[
x^\varepsilon\le T\le x^{1/2-\varepsilon},
\tag{6}
\]

one has

\[
\boxed{
\sum_{x<d\le2x}
\left|\mathcal H_d^{\rm out}(T)\right|
\gg_{\lambda,\varepsilon,\kappa}
\frac{Nx}{L^2\log x}.
}
\tag{7}
\]

In particular, because `L asymp_lambda log x` in (1),

\[
\sum_{x<d\le2x}
\left|\mathcal H_d^{\rm out}(T)\right|
\ge Nx^{1-o(1)}.
\tag{8}
\]

Thus the strict-right Möbius Mellin field from FD-283 is **not** polynomially small after the `sigma` integration and upper/lower pairing, at least on this outer strip and throughout the low polynomial-height range (6). Any rescue of the current hard-Perron route must cancel this signed strip against another part of the horizontal contour, or change the contour/truncation architecture.

## 1. The reciprocal zeta factor has almost constant phase across the outer strip

Write

\[
g(\sigma):=\frac1{\zeta(\sigma+iT)}.
\tag{9}
\]

Because `b>1`, the logarithmic derivative has an absolutely convergent Dirichlet series, so

\[
\left|\frac{g'(\sigma)}{g(\sigma)}\right|
=
\left|\frac{\zeta'}{\zeta}(\sigma+iT)\right|
\le
-\frac{\zeta'}{\zeta}(\sigma).
\tag{10}
\]

Near `sigma=1`,

\[
-\frac{\zeta'}{\zeta}(\sigma)
=
\frac1{\sigma-1}+O(1).
\tag{11}
\]

Hence

\[
\int_b^c
\left|\frac{g'(\sigma)}{g(\sigma)}\right|d\sigma
\le
\log\frac{c-1}{b-1}+O(L^{-1})
=
\log\frac1{1-\kappa}+o(1)
=O(\kappa).
\tag{12}
\]

For fixed sufficiently small `kappa`, every `g(sigma)` therefore lies in a fixed narrow multiplicative cone around `g(c)`. In particular, if

\[
A_p
:=
\int_b^c
N^\sigma p^{\sigma-1}g(\sigma)\,d\sigma,
\qquad p\in(x,2x],
\tag{13}
\]

then

\[
A_p
=
g(c)R_p\bigl(1+O(\kappa)\bigr),
\qquad
R_p:=\int_b^cN^\sigma p^{\sigma-1}\,d\sigma>0,
\tag{14}
\]

uniformly in `p`. Since `(Np)^(sigma-1)` stays between positive constants on this strip,

\[
R_p\asymp_\kappa \frac{N}{L}.
\tag{15}
\]

Also

\[
|\zeta(c+iT)|\le\zeta(c)\ll L,
\tag{16}
\]

so

\[
\boxed{
|A_p|\gg_\kappa \frac{N}{L^2},
\qquad
\arg A_p=\arg g(c)+O(\kappa).
}
\tag{17}
\]

The key point is that the full Möbius sum encoded by `1/zeta(s)` has already been retained in `A_p`; (17) is not an absolute-value estimate term by term in Möbius coefficient space.

## 2. Prime self-divisor coordinates expose the common phase

For a prime `p`, the only divisors are `1` and `p`, hence

\[
K_s(p)
=
\frac1s+
\int_{p-1}^{p}u^{s-1}\,du.
\tag{18}
\]

Uniformly for `sigma in [b,c]`, Taylor expansion over the unit cell gives

\[
\int_{p-1}^{p}u^{s-1}\,du
=
p^{s-1}
\left(1+O\!\left(\frac{T+1}{p}\right)\right).
\tag{19}
\]

Substituting (19) into (5) yields

\[
\mathcal H_p^{\rm out}(T)
=
-\frac1\pi
\operatorname{Im}
\left(
 e^{iT\log(Np)}A_p
\right)
+
O_\kappa\!\left(
N\left(\frac{T}{x}+\frac1T\right)
\right).
\tag{20}
\]

Here the first error comes from the finite-cell replacement (19), using the absolutely convergent bound

\[
|1/\zeta(\sigma+iT)|
\le\sum_{n\ge1}n^{-\sigma}
=\zeta(\sigma)\ll_\kappa L,
\tag{21}
\]

and the second from the `q=1` term `1/s` in (18). Under (6),

\[
N\left(\frac{T}{x}+\frac1T\right)
=o\!\left(\frac{N}{L^2}\right).
\tag{22}
\]

Let

\[
\Phi:=T\log N+\arg g(c).
\tag{23}
\]

By (17), for sufficiently small fixed `kappa`, every prime satisfying

\[
\left|\sin(T\log p+\Phi)\right|\ge\frac34
\tag{24}
\]

therefore obeys

\[
\boxed{
|\mathcal H_p^{\rm out}(T)|
\gg_\kappa \frac{N}{L^2}.
}
\tag{25}
\]

This is already a signed statement: the `sigma` integral, the entire reciprocal-zeta coefficient sum, and the upper/lower horizontal pairing have all occurred before the absolute value in (25).

## 3. RH supplies enough primes with robust phase

Let

\[
G_{T,\Phi}(x)
:=
\{y\in[x,2x]: |\sin(T\log y+\Phi)|\ge3/4\}.
\tag{26}
\]

Because `T -> infinity` in (6), this set is a union of `O(T)` intervals and occupies a fixed positive proportion of `[x,2x]` in ordinary length:

\[
|G_{T,\Phi}(x)|\gg x.
\tag{27}
\]

Under RH, Schoenfeld's Chebyshev estimate gives

\[
\vartheta(y)=y+O\!\left(y^{1/2}\log^2 y\right).
\tag{28}
\]

Apply (28) at both endpoints of every interval composing (26). Their total endpoint error is

\[
O\!\left(Tx^{1/2}\log^2x\right)
=o(x)
\tag{29}
\]

through the upper range in (6). Combining (27)--(29),

\[
\sum_{\substack{x<p\le2x\\p\in G_{T,\Phi}(x)}}\log p
\gg x,
\tag{30}
\]

and therefore

\[
\#\{p\in(x,2x]: p\in G_{T,\Phi}(x)\}
\gg\frac{x}{\log x}.
\tag{31}
\]

Summing (25) over these prime coordinates proves (7).

## 4. Consequence for the repair barrier

The deep repair barrier isolated in FD-261 has power scale

\[
N^\theta x^{2-\beta_*},
\qquad
\beta_*:=\log_2(3/2).
\tag{32}
\]

Ignoring only logarithms, the new signed outer-strip witness has scale `Nx`. Their ratio is

\[
N^{1-\theta}x^{\beta_*-1-o(1)}
=
N^{1-\theta-\lambda(1-\beta_*)+o(1)}.
\tag{33}
\]

Consequently, whenever

\[
\boxed{
\lambda<\frac{1-\theta}{1-\beta_*},
}
\tag{34}
\]

the signed outer strip by itself is power-larger than the repair target. At the RH calibration `theta=1/2`, the boundary in (34) is approximately

\[
\lambda<1.2047.
\tag{35}
\]

In particular the first-row polynomial-depth regime `lambda<=1` lies strictly inside this range.

This does **not** prove a lower bound for the complete horizontal contour. The remaining segment to the left of `b` can in principle cancel (5) coordinate by coordinate. The result instead removes a narrower escape left by FD-283: the strict-right Möbius Mellin field is not itself polynomially depleted once the physical prime coordinates are retained. The current hard-Perron route must now obtain a comparably strong **cross-strip/cross-collar cancellation**, or use a different smoothed/modified truncation whose boundary architecture avoids this witness.

## Prior-art and novelty boundary

The RH estimate (28) is classical; a convenient explicit primary anchor is Lowell Schoenfeld, *Sharper Bounds for the Chebyshev Functions theta(x) and psi(x). II*, Mathematics of Computation **30** (1976), 337--360, Theorem 10. No novelty is claimed for RH prime counts in intervals of length above square-root scale, for prime phase selection, or for the absolutely convergent Dirichlet series of `1/zeta(s)` on `Re(s)>1`.

The derived content here is their specialization to the exact FD-282/FD-283 grouped Perron field: a prime self-divisor witness that survives signed `sigma` integration and upper/lower pairing and still forces an `Nx^{1-o(1)}` outer-strip band norm. The literature check found no source asserting this Farey-repair consequence.

## Boundaries and adversarial checks

- **RH is load-bearing only in the phase-sector prime count.** The analytic strip and prime-coordinate reduction are unconditional. Replacing (28) by another prime-distribution theorem would change the admissible height range accordingly.
- **The square-root height ceiling is prime-density, not kernel, limited.** The error in (29) is why this proof stops at `T<=x^(1/2-epsilon)`; it does not show failure above that height.
- **The polynomial lower height is technical and explicit.** `T>=x^epsilon` makes both errors in (22) negligible relative to the prime main term. No claim is made here for bounded or subpolynomial `T`.
- **The strip is deliberately thin but fixed in logarithmic scale.** Shrinking from width `1/L` to `kappa/L` costs only logarithms and keeps `1/zeta` in a common phase cone. Taking `kappa` large enough to lose (12) would invalidate the argument.
- **No full-contour lower bound is claimed.** The unanalysed horizontal portion `Re(s)<=b` may cancel the outer strip. This is the live residual mechanism after the present result.
- **No coefficientwise absolute-value shortcut is used.** Absolute values enter only after each paired strip coordinate is formed. Replacing `1/zeta` by `sum |mu(n)|n^-sigma` is used only for the two error terms in (20), not for the main lower bound.

## Audit test

A decisive audit should verify three interfaces independently: the cone estimate (12)--(17), including constants for a fixed admissible `kappa`; the uniform approximation (20) in the full height window (6); and the RH phase-sector count (30), with the `O(T)` endpoint losses tracked explicitly. Failure of any one of these at power scale would invalidate (7). Numerical sampling of prime coordinates can check normalization and phase conventions but is not evidence for the theorem.

## Research consequence

FD-282 showed that absolute grouped Perron collars retain a self-divisor plateau. FD-283 then showed that preserving signs reduces the strict-right collar to a Möbius Mellin cancellation problem. FD-284 closes the most direct version of that escape at low polynomial heights: **even after preserving the signs through the horizontal integration and pairing the upper and lower edges, a thin outer strip still has power-scale `Nx` mass on a positive density of prime coordinates**.

The unresolved question is therefore no longer whether the right-collar Möbius sum can simply collapse by itself. The live mechanism must transfer comparable mass with opposite sign from the remainder of the horizontal contour, or alter the Perron representation so that the outer-strip prime witness is no longer present.