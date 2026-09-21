# AF-480 — Prime Gibbs global half-line margin has the local boundary asymptotic

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-INPUT`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `GLOBAL-CONDITIONING`, `BOUNDARY-ASYMPTOTIC`, `NO-NOVELTY-CLAIM`

## Claim

AF-479 proved that the local lower-margin ratio of the canonical coordinate Hilbert embedding along the prime Gibbs curve collapses like `1/log(1/(sigma-1))` as `sigma downarrow 1`, and therefore gave only the upper bound

\[
c(\sigma_0)
:=
\inf_{\sigma_0\le \sigma<\tau}
\frac{\|H(\mu_\sigma)-H(\mu_\tau)\|_2}
     {\|\mu_\sigma-\mu_\tau\|_1}
\le \rho(\sigma_0).
\]

That local obstruction is asymptotically the whole global story.

For

\[
P(\sigma)=\sum_p p^{-\sigma},
\qquad
\mu_\sigma(p)=\frac{p^{-\sigma}}{P(\sigma)},
\qquad
H(\mu)=\sqrt2\,\mu,
\]

one has

\[
\boxed{
P(\sigma_0)c(\sigma_0)
\longrightarrow
\sqrt{\frac{P(2)}2}
\qquad (\sigma_0\downarrow1).
}
\tag{1}
\]

Since

\[
P(1+\epsilon)
\sim
\log\frac1\epsilon,
\]

this is equivalently

\[
\boxed{
c(1+\epsilon)
\sim
\frac{\sqrt{P(2)/2}}
     {\log(1/\epsilon)}.
}
\tag{2}
\]

Thus the logarithmic collapse identified infinitesimally in AF-479 is not merely an upper obstruction coming from nearly coincident parameters. It is the exact first-order asymptotic of the **best global lower Lipschitz constant on the entire anchored half-line**.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{for this rigid single-crossing source law, boundary-local norm spreading determines the global fidelity scale.}
}
\tag{3}
\]

In particular, AF-478's existence theorem and AF-479's local boundary calculation now meet sharply: every fixed anchor has positive global fidelity, while the optimal global margin deteriorates at exactly the prime-zeta normalization rate.

## Exact derivation

Fix

\[
1<s<t,
\qquad
A=P(s),\quad B=P(t),\quad h=t-s,\quad \Delta=A-B>0,
\tag{4}
\]

and write

\[
d_p:=\mu_t(p)-\mu_s(p).
\tag{5}
\]

Because the likelihood ratio is monotone in `p`, the vector `d` has one sign crossing, as in AF-478.

### An exact total-variation upper bound from the normalization drop

On the positive part of `d`,

\[
\frac{\mu_s(p)}{\mu_t(p)}
=
\frac BA p^h,
\]

so

\[
0<d_p
=
\mu_t(p)\left(1-\frac BA p^h\right)
\le
\mu_t(p)\left(1-\frac BA\right)
=
\mu_t(p)\frac{\Delta}{A}.
\tag{6}
\]

Summing the positive Jordan part and using `\sum_p d_p=0` gives the exact estimate

\[
\boxed{
\|\mu_t-\mu_s\|_1
\le
\frac{2\Delta}{A}.
}
\tag{7}
\]

Near the prime-zeta boundary this bound is asymptotically saturated by infinitesimal pairs, by AF-479.

### Fixed prime coordinates see the same normalization drop

For every prime `p`, direct subtraction gives

\[
d_p
=
\frac{p^{-s}}{AB}
\left[A p^{-h}-B\right]
=
\frac{p^{-s}\Delta}{AB}
\left[1-\frac{A(1-p^{-h})}{\Delta}\right].
\tag{8}
\]

We now show that the bracket tends uniformly to `1` for all boundary-near pairs, on every fixed finite set of prime coordinates.

Write

\[
s=1+\epsilon,
\qquad
t=1+\delta,
\qquad 0<\epsilon<\delta.
\]

The classical prime-zeta expansion obtained from Möbius inversion of `log zeta` is

\[
P(1+x)
=
\log\frac1x+C_P+O(x)
\qquad (x\downarrow0),
\tag{9}
\]

with a bounded derivative for the regular remainder. Hence, uniformly for `0<epsilon<delta<=eta`,

\[
A
=
\log\frac1\epsilon+O(1),
\qquad
\Delta
=
\log\frac\delta\epsilon+O(\delta-\epsilon).
\tag{10}
\]

Put

\[
L=\log\frac1\epsilon,
\qquad
D=\log\frac1\delta,
\qquad
r=L-D=\log\frac\delta\epsilon.
\]

Since

\[
r=\log\frac\delta\epsilon
\ge
\frac{\delta-\epsilon}{\delta},
\tag{11}
\]

we have `(delta-epsilon)/r<=delta`. Moreover

\[
\sup_{0<\epsilon<\delta\le\eta}
L\frac{\delta-\epsilon}{r}
\longrightarrow0
\qquad (\eta\downarrow0).
\tag{12}
\]

Indeed, if `r>=L/2`, the expression is at most `2 eta`. If `r<L/2`, then `L<2D`, so it is at most

\[
2\delta\log\frac1\delta
\le
2\eta\log\frac1\eta
\]

for sufficiently small `eta`. Equations `(10)`--`(12)` therefore imply

\[
\sup_{0<\epsilon<\delta\le\eta}
\frac{A(\delta-\epsilon)}{\Delta}
\longrightarrow0.
\tag{13}
\]

For each fixed prime `p`,

\[
0\le1-p^{-h}\le h\log p,
\]

so `(13)` yields

\[
\sup_{1<s<t\le1+\eta}
\frac{A(1-p^{-h})}{\Delta}
\longrightarrow0.
\tag{14}
\]

Consequently, for every fixed finite set `F` of primes, `(8)` gives uniformly over all `1<s<t<=1+eta`,

\[
\left(\sum_{p\in F}d_p^2\right)^{1/2}
=
\frac{\Delta}{AB}
\left(
\sqrt{\sum_{p\in F}p^{-2}}+o_F(1)
\right)
\qquad (\eta\downarrow0).
\tag{15}
\]

Therefore

\[
\sqrt2\,\|\mu_t-\mu_s\|_2
\ge
\frac{\sqrt2\,\Delta}{AB}
\left(
\sqrt{\sum_{p\in F}p^{-2}}+o_F(1)
\right).
\tag{16}
\]

Combining `(7)` and `(16)` gives, uniformly for boundary-near pairs,

\[
\frac{\sqrt2\,\|\mu_t-\mu_s\|_2}
     {\|\mu_t-\mu_s\|_1}
\ge
\frac1B
\left(
\sqrt{\frac12\sum_{p\in F}p^{-2}}+o_F(1)
\right).
\tag{17}
\]

If `s>=sigma_0`, then `B=P(t)<=P(sigma_0)`, so

\[
P(\sigma_0)
\frac{\sqrt2\,\|\mu_t-\mu_s\|_2}
     {\|\mu_t-\mu_s\|_1}
\ge
\sqrt{\frac12\sum_{p\in F}p^{-2}}+o_F(1).
\tag{18}
\]

### Pairs away from the boundary cannot control the asymptotic infimum

Fix `eta>0`. If `s>=1+eta/2`, AF-478 supplies a positive lower fidelity constant depending only on `eta/2`.

If instead

\[
s<1+\eta/2,
\qquad
t\ge1+\eta,
\]

then the probability of the lowest-energy prime `2` is strictly increasing with the Gibbs parameter, because

\[
\frac{d}{du}\mu_u(2)
=
\mu_u(2)\left(m(u)-\log2\right)>0.
\]

Hence

\[
\mu_t(2)-\mu_s(2)
\ge
\mu_{1+\eta}(2)-\mu_{1+\eta/2}(2)
=:\gamma_\eta>0.
\tag{19}
\]

Using `\|\mu_t-\mu_s\|_1<=2`, such separated pairs satisfy

\[
\frac{\sqrt2\,\|\mu_t-\mu_s\|_2}
     {\|\mu_t-\mu_s\|_1}
\ge
\frac{\gamma_\eta}{\sqrt2}>0.
\tag{20}
\]

Thus for every fixed `eta`, all pairs with `t>=1+eta` have a lower bound independent of `sigma_0`. Since `P(sigma_0)->infinity`, they are asymptotically much better conditioned than the `1/P(sigma_0)` scale and cannot determine `c(sigma_0)`.

Combining this far-pair observation with `(18)` yields, for every fixed finite `F`,

\[
\liminf_{\sigma_0\downarrow1}
P(\sigma_0)c(\sigma_0)
\ge
\sqrt{\frac12\sum_{p\in F}p^{-2}}.
\tag{21}
\]

Letting `F` increase through the primes gives

\[
\liminf_{\sigma_0\downarrow1}
P(\sigma_0)c(\sigma_0)
\ge
\sqrt{\frac{P(2)}2}.
\tag{22}
\]

### AF-479 supplies the matching upper bound

For every fixed `sigma_0>1`, take `tau downarrow sigma_0`. By differentiability in both `ell^1` and `ell^2`,

\[
c(\sigma_0)
\le
\rho(\sigma_0),
\tag{23}
\]

where `rho` is AF-479's local ratio. AF-479 proves

\[
\rho(\sigma_0)
\sim
\frac{\sqrt{P(2)/2}}{P(\sigma_0)}.
\tag{24}
\]

Therefore

\[
\limsup_{\sigma_0\downarrow1}
P(\sigma_0)c(\sigma_0)
\le
\sqrt{\frac{P(2)}2}.
\tag{25}
\]

Equations `(22)` and `(25)` prove `(1)` and `(2)`.

## What the sharp constant means

The constant `P(2)` appears for a concrete structural reason. Near `sigma=1`, the source normalization `P(sigma)` diverges, so each fixed prime coordinate is diluted by approximately `1/P(sigma)`. But the squared fixed-coordinate profile remains summable:

\[
\sum_p p^{-2}=P(2)<\infty.
\]

For a pair of nearby boundary sources, the total-variation difference is driven by the full normalization shift, while the Hilbert norm can retain the coherent contribution of all fixed prime coordinates. Taking larger and larger finite coordinate windows recovers exactly the `sqrt(P(2))` factor.

This sharpens AF-479's phrase **effective norm breadth**. The boundary loss is not caused by a failure of the single-crossing sign law: that combinatorial structure remains intact. It is caused by the growing mismatch between the `ell^1` mass of a source difference and the `ell^2` energy visible in any fixed-coordinate Hilbert geometry. The global half-line constant is asymptotically governed by the same mismatch already visible in the boundary tangent.

## Prior art and novelty audit

The analytic and statistical ingredients remain classical, and this finding makes **no novelty claim** for the component facts.

- C.-E. Fröberg, **“On the Prime Zeta Function,”** *BIT* 8, 187--202 (1968), DOI `10.1007/BF01933420`. This is the classical prime-zeta reference underlying the Möbius-inversion representation and the logarithmic singularity at `s=1` used in `(9)`.
- Samuel Karlin and Herman Rubin, **“Distributions Possessing a Monotone Likelihood Ratio,”** *Journal of the American Statistical Association* 51(276), 637--643 (1956), DOI `10.1080/01621459.1956.10501355`. The one-crossing likelihood-ratio structure used here is classical exponential-family/MLR mathematics.
- Samuel Karlin and Herman Rubin, **“The Theory of Decision Procedures for Distributions with Monotone Likelihood Ratio,”** *The Annals of Mathematical Statistics* 27(2), 272--299 (1956), DOI `10.1214/aoms/1177728259`. This is broader classical prior art for ordered families with monotone likelihood ratios.

A targeted search for prime-zeta Gibbs distributions, total-variation-to-`ell^2` conditioning, and lower-Lipschitz asymptotics did not identify a standard theorem matching `(1)`. That absence is not treated as evidence of novelty. The durable Arithmetic Fidelity contribution is the source-specific sharpening of AF-478/AF-479: the local prime-zeta boundary obstruction gives the exact first-order global conditioning law for this canonical compression.

## Boundaries and falsification audit

- **The result is specific to the canonical coordinate Hilbert encoding.** It determines the optimal lower constant for `H(mu)=sqrt(2)mu` on the prime Gibbs half-line. It does not rule out a different nonlinear Hilbert representation with better boundary behavior.
- **The theorem is metric, not injective.** No pair of finite-parameter prime Gibbs laws is identified. What vanishes is uniform inverse-Lipschitz robustness as the normalization boundary is approached.
- **Single crossing remains load-bearing but is not sufficient for uniform boundary fidelity.** It supplies the exact total-variation control `(7)`; the `P(2)` factor comes from how the normalization shift is distributed across fixed coordinates.
- **The rational primes are not certified as uniquely selective.** The proof uses the prime-zeta logarithmic boundary law and the square-summable fixed profile. Other ordered Gibbs/Dirichlet source laws with analogous partition asymptotics can exhibit the same mechanism and should be used as matched controls before assigning arithmetic significance.
- **Equation `(1)` does not locate an exact finite pair attaining the infimum.** It shows that the best global constant has the same first-order asymptotic as the local boundary ratio. The infimum may be approached by parameter pairs whose separation also tends to zero.
- **The boundary expansion is essential.** A source family with a different partition-function singularity can have a different global fidelity rate even if its likelihood ratios remain single-crossing.
- **No RH-facing consequence follows.** The theorem quantifies preservation inside a prime-derived source family; it does not show that a rational-prime discriminator survives a later zeta, spectral, positive, quotient, or asymptotic compression.

## Research consequence

AF-479 left open whether a much worse finite secant could hide somewhere on the anchored half-line and make the local `1/log` collapse only a weak upper bound on global fidelity. AF-480 closes that gap: no such worse scale exists asymptotically. The global and local margins have the same first-order constant.

This gives a sharper template for future Arithmetic Fidelity source laws near singular boundaries. After proving a local tangent deterioration, the next question should be whether finite secants introduce an additional loss. Here the monotone-likelihood-ratio geometry plus the fixed-coordinate square-summability show that they do not. For candidate arithmetic source restrictions, separating **local boundary conditioning** from **finite-secant degradation** is therefore a useful two-stage audit before any downstream compression is trusted.