# WP-100 — The mixed-prime product completion is Haar-singular at the Weil boundary

**Status:** `EXACT-DERIVED + DECISIVE-BOUNDARY + PRIOR-ART-CLASSICALIZATION`. The measure-class mechanism below is a direct specialization of classical Kakutani infinite-product theory, not a new theorem of probability or harmonic analysis. The Mathia-specific consequence is that the explicit finite-mass positive completion from `WP-097` leaves the canonical product-Haar measure class exactly at the critical Weil exponent. Thus the surviving mixed-prime route cannot use that completion as an ordinary density perturbation of the standard Prime-Torus Hilbert geometry.

## Claim

`WP-097` shows that the critical one-prime Weil moments can coexist with a finite positive diagonal when mixed-prime Fourier coefficients are retained. Its normalized local factors are

\[
\rho_{p,C,1/2}(\theta)
=1+\frac{\log p}{C}
\left(1-P_{p^{-1/2}}(\theta)\right),
\tag{1}
\]

where

\[
P_r(\theta)
=\frac{1-r^2}{1-2r\cos\theta+r^2}
=1+2\sum_{k\ge1}r^k\cos(k\theta),
\tag{2}
\]

and `C>=C_* = 2(\sqrt2+1)\log2`. The corresponding all-prime positive carrier is

\[
\widetilde\mu_{C,1/2}
=\bigotimes_p \rho_{p,C,1/2}(\theta_p)\,dm_p,
\tag{3}
\]

with `WP-097`'s finite measure equal to `C \widetilde\mu_{C,1/2}`.

Embed (1) in the natural radial family

\[
\rho_{p,C,\sigma}(\theta)
:=1+\frac{\log p}{C}
\left(1-P_{p^{-\sigma}}(\theta)\right),
\qquad \sigma>0.
\tag{4}
\]

For fixed `sigma`, put

\[
C_*(\sigma)
:=\sup_p\frac{2(\log p)p^{-\sigma}}{1-p^{-\sigma}}<\infty.
\tag{5}
\]

If `C>=C_*(sigma)`, every factor in (4) is a nonnegative probability density. Then the normalized product measure

\[
\widetilde\mu_{C,\sigma}
:=\bigotimes_p \rho_{p,C,\sigma}\,dm_p
\tag{6}
\]

has the exact measure-class dichotomy

\[
\boxed{
\widetilde\mu_{C,\sigma}\sim m_\infty
\iff \sigma>\frac12,
\qquad
\widetilde\mu_{C,\sigma}\perp m_\infty
\iff 0<\sigma\le\frac12,
}
\tag{7}
\]

where `m_infty=\bigotimes_p dm_p` is canonical product Haar measure. In particular, for every finite admissible `C`,

\[
\boxed{
\widetilde\mu_{C,1/2}\perp m_\infty.
}
\tag{8}
\]

Thus the mixed-prime terms that repair the finite-diagonal obstruction of `WP-096` do so inside a genuine positive all-prime measure, but the explicit independent product completion lives in a **singular measure class** at exactly the exponent where its one-prime moments are the Weil coefficients.

## 1. The finite-product density has an exact square-sum threshold

Write

\[
u_{p,C,\sigma}:=\rho_{p,C,\sigma}-1.
\tag{9}
\]

Since the nonzero Fourier coefficients of `1-P_r` are `-r^{|k|}`, we have for `k!=0`

\[
\widehat u_{p,C,\sigma}(k)
=-\frac{\log p}{C}p^{-|k|\sigma}.
\tag{10}
\]

Parseval therefore gives the exact local squared deviation

\[
\begin{aligned}
q_p(\sigma)
&:=\|u_{p,C,\sigma}\|_{L^2(m_p)}^2\\
&=\frac{2(\log p)^2}{C^2}
\sum_{k\ge1}p^{-2k\sigma}\\
&=\boxed{
\frac{2(\log p)^2}{C^2}
\frac{p^{-2\sigma}}{1-p^{-2\sigma}}
}.
\end{aligned}
\tag{11}
\]

For a finite prime set `F`, let

\[
W_{F,C,\sigma}(\theta)
:=\prod_{p\in F}\rho_{p,C,\sigma}(\theta_p).
\tag{12}
\]

Each `u_p` has mean zero, so independence gives

\[
\boxed{
\|W_{F,C,\sigma}\|_{L^2(m_F)}^2
=\prod_{p\in F}(1+q_p(\sigma)).
}
\tag{13}
\]

At the critical exponent,

\[
q_p\!\left(\frac12\right)
=\frac{2(\log p)^2}{C^2(p-1)}.
\tag{14}
\]

Hence

\[
\sum_p q_p\!\left(\frac12\right)=\infty,
\tag{15}
\]

already from Euler's divergence of `sum_p 1/p`. For `sigma<1/2` the terms are larger in the tail, so the series also diverges. For `sigma>1/2`,

\[
q_p(\sigma)\ll_{C,\sigma}(\log p)^2p^{-2\sigma},
\]

and convergence follows by comparison with

\[
\sum_{n\ge2}(\log n)^2n^{-2\sigma}<\infty.
\tag{16}
\]

Consequently the finite-cylinder densities have uniformly bounded `L^2` norm precisely above the critical boundary. At `sigma=1/2`, their `L^2` norms diverge for **every fixed finite `C`**. Raising the allowed diagonal mass from the sharp `C_*` to any other finite value changes only the constant `C^{-2}` in (14) and cannot regularize the all-prime product.

This `L^2` explosion is already a useful warning, but by itself it would not prove singularity. The exact measure-class statement comes from Kakutani.

## 2. Kakutani turns the same square sum into singularity

For each local factor define its Hellinger affinity with Haar,

\[
A_p(\sigma)
:=\int_{\mathbb T}\sqrt{\rho_{p,C,\sigma}(\theta)}\,dm_p(\theta).
\tag{17}
\]

The local perturbation satisfies

\[
\|u_{p,C,\sigma}\|_\infty
=\frac{2(\log p)p^{-\sigma}}
{C(1-p^{-\sigma})}
\longrightarrow0.
\tag{18}
\]

Thus for all sufficiently large primes, `|u_p|<=1/2`. Since `int u_p dm_p=0`,

\[
1-A_p(\sigma)
=\int
\left(1-\sqrt{1+u_p}+\frac{u_p}{2}\right)dm_p.
\tag{19}
\]

On `[-1/2,1/2]`, the scalar function

\[
g(t)=1-\sqrt{1+t}+\frac t2
\]

is bounded above and below by positive constant multiples of `t^2`: it has `g(0)=g'(0)=0` and strictly positive bounded second derivative there. Hence

\[
1-A_p(\sigma)\asymp q_p(\sigma)
\qquad(p\to\infty).
\tag{20}
\]

Kakutani's equivalence/singularity theorem for countable product measures says that, because each local factor is equivalent to Haar, the all-prime product is equivalent to product Haar exactly when the product of local Hellinger affinities is positive, equivalently when

\[
\sum_p(1-A_p(\sigma))<\infty.
\tag{21}
\]

Equations (11), (20), and the threshold calculation above prove (7).

At the endpoint `sigma=1/2`, `C=C_*`, the dyadic factor from `WP-097` vanishes only at `theta_2=0`; it is positive Haar-almost everywhere, so the local measure is still equivalent to circle Haar and Kakutani applies. Multiplying (6) by the finite scalar `C` does not change measure class, so (8) applies equally to the finite measure `mu_C` of `WP-097`.

## 3. This is a boundary on the surviving mixed-prime route, not a contradiction

The singularity in (8) does **not** invalidate `WP-097`. The infinite product measure exists and remains positive. It simply cannot be represented by an ordinary Radon--Nikodym density with respect to canonical product Haar measure at the critical exponent. A Hilbert space such as `L^2(\widetilde\mu_{C,1/2})` is perfectly legitimate, but it is no longer the regular Haar `L^2` geometry from which the Prime-Torus construction started.

This distinction matters for the open completion route after `WP-098` and `WP-099`. Those findings already show that the mixed sector cannot be erased by a same-algebra positive quotient or by passive positive auxiliary elimination. `WP-100` now shows that **retaining the explicit `WP-097` mixed sector all the way to the global object also has a price**: at the Weil exponent it forces a singular finite-place measure class. Therefore this particular route cannot be completed by treating the mixed interaction as a small or regular density correction inside `L^2(m_\infty)`.

The conclusion is deliberately narrower than several tempting overstatements:

- it does not rule out a singular global Hilbert geometry carrying an independent sign theorem;
- it does not rule out a different, genuinely correlated non-product positive completion with the same one-prime marginals;
- it does not produce the archimedean Gamma/digamma contribution or the polar test functional;
- it does not show that singularity itself implies Weil positivity;
- it does not permit importing zero data or RH into the singular measure in order to recover the missing sign.

A successful continuation from `WP-097` must therefore either embrace a singular finite-place representation and derive the archimedean/global coupling plus sign theorem there, or replace the independent product completion by a structurally forced correlated/global architecture before the final pairing.

## 4. Matched free-generator control and prior-art boundary

The mechanism is not specific to rational primes. For free multiplicative generators with energies `E_j>0`, set

\[
r_j=e^{-\sigma E_j},
\qquad
\rho_j
=1+\frac{E_j}{C}(1-P_{r_j}).
\tag{22}
\]

Whenever the local nonnegativity bound holds, the exact squared deviation is

\[
\boxed{
q_j
=\frac{2E_j^2}{C^2}
\frac{e^{-2\sigma E_j}}
{1-e^{-2\sigma E_j}}.
}
\tag{23}
\]

The same Kakutani argument makes `sum_j q_j` the equivalence/singularity criterion against product Haar. Choosing `E_j=log p` specializes (23) to (11). Thus the measure-class theorem is universal product-measure harmonic analysis; the prime sequence determines where the square sum crosses its threshold, not a new arithmetic positivity theorem.

This is also the correct novelty classification. `SOURCES.md` already records Kakutani's 1948 product-measure dichotomy and the Poisson/GCD literature of Aistleitner--Berkes--Seip. More closely, `PL-030` and `WP-022` already establish a `sigma=1/2` Haar measure-class transition for the **pure product-Poisson family** `\bigotimes_p P_{p^{-\sigma}}dm_p`. In `WP-022`, however, those Poisson moments encode the GCD kernel and the Weil ray appears only after taking a logarithmic radial score, whose Fisher norm then diverges at the boundary.

The present carrier is different: its local density is the affine factor (4), its moments themselves are the critical one-prime Weil rays, and its mixed moments are exactly the positivity-restoring sector derived in `WP-097`. Applying Kakutani to that distinct carrier is therefore a new project-level boundary on the reopened route, but the underlying theorem and square-summability mechanism are classical. No theorem-level novelty is claimed.

## Consequence for the research line

The cover-positive chain is now constrained on both sides:

```text
force sparse one-prime support
    -> WP-096: infinite diagonal positivity debt

allow mixed-prime product completion
    -> WP-097: finite positive diagonal restored

try to remove mixed sector positively
    -> WP-098 / WP-099: quotient and passive elimination fail

retain the explicit mixed product sector globally at sigma=1/2
    -> WP-100: positive carrier is singular to canonical product Haar
```

This does not close the global Weil-positivity program. It does make the remaining obligation sharper: a viable Mathia-native geometry must explain why a singular or genuinely correlated finite-place sector is canonical, couple it intrinsically to the archimedean and polar terms, and obtain the final sign from one independent global theorem rather than from the already prescribed Weil coefficients.