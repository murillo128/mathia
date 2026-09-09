# MC-173 — Doyle's additive autocorrelation transfer is blind to Möbius prime phase

**Status:** `LITERATURE+EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `PHASE-BLIND-CONTROL`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

A recent short-interval result of Doyle gives a strong new `ell^2` engine for `k`-free exponential sums and transfers it to a lower bound for the `L^1` norm of a Möbius-twisted additive exponential sum. For the live `MC-172` frontier, however, that transfer has an exact information-loss point: its autocorrelation removes every square-free-supported prime phase before the `k`-free estimate is used.

Let

\[
I=(N-K,N]\cap\mathbb N,
\qquad
z=(z_p)_p\in\mathbb T^{\mathcal P},
\qquad
\chi_z(n)=\prod_p z_p^{v_p(n)},
\]

and define the support-matched phase deformation

\[
a_z(n)=\mu(n)^2\chi_z(n),
\qquad
G_z(\alpha)=\sum_{n\in I}a_z(n)e(n\alpha).
\tag{1}
\]

The true Möbius coefficients are the all-minus prime phase `z_p=-1`; the all-plus control is `z_p=1`.

Then for every prime-phase vector `z`, Fourier orthogonality gives the exact identity

\[
\boxed{
\int_0^1 \overline{G_z(\beta)}G_z(\alpha+\beta)\,d\beta
=
\sum_{n\in I}\mu(n)^2e(n\alpha)
=:S_2(\alpha;K).
}
\tag{2}
\]

Thus this additive autocorrelation depends only on square-free support and is **identical for every support-matched prime phase**. In particular, Young's inequality yields

\[
\boxed{
\|S_2(\cdot;K)\|_{L^1(\mathbb T)}
\le
\|G_z\|_{L^1(\mathbb T)}^2
}
\tag{3}
\]

for every `z`.

Doyle's Theorem 1.7 is exactly the specialization of `(2)`–`(3)` to the Möbius phase, combined with his `k=2` estimate for the square-free sum `S_2`. Therefore the resulting lower bound

\[
\|G_\mu\|_1\gg K^{1/6}
\]

in the stated short-interval range is not a Möbius-orientation discriminator: the same argument proves

\[
\|G_z\|_1\gg K^{1/6}
\tag{4}
\]

for every support-matched phase deformation `z` in exactly the same range.

Consequently, **Doyle's current middle-part `ell^2` estimate and the autocorrelation transfer built from it cannot by themselves provide the signed intermediate currency sought in `MC-172`.** They can substantially improve information about square-free support and additive Fourier moments, but the transfer to the Möbius-twisted sum has already quotiented out the prime orientation that `MC-172` must retain.

This is a no-go only for the existing support/autocorrelation route. It does not rule out a modification of Doyle's analytic machinery that inserts a genuinely phase-sensitive quantity before the autocorrelation collapse.

## 1. Exact phase-blindness of the autocorrelation

Expanding `(2)` gives

\[
\begin{aligned}
\int_0^1 \overline{G_z(\beta)}G_z(\alpha+\beta)\,d\beta
&=
\sum_{m,n\in I}
\overline{a_z(m)}a_z(n)e(n\alpha)
\int_0^1 e((n-m)\beta)\,d\beta\\
&=
\sum_{n\in I}|a_z(n)|^2e(n\alpha).
\end{aligned}
\]

Since `|chi_z(n)|=1` and `mu(n)^4=mu(n)^2`, one has

\[
|a_z(n)|^2=\mu(n)^2,
\]

which proves `(2)`. No multiplicativity beyond the definition of the phase deformation is needed for the orthogonality step; any unit-modulus decoration of the square-free support has the same autocorrelation.

Taking absolute values and integrating in `alpha` gives

\[
\begin{aligned}
\|S_2\|_1
&\le
\int_0^1\int_0^1
|G_z(\beta)|\,|G_z(\alpha+\beta)|\,d\beta\,d\alpha\\
&=\|G_z\|_1^2,
\end{aligned}
\]

which is `(3)`.

The direction matters. A lower bound for the square-free `L^1` norm transfers to a lower bound for every phase-decorated `G_z`; it does not supply an upper bound measuring cancellation of the Möbius orientation.

## 2. What Doyle's new `ell^2` estimate actually controls

Ben Doyle, *Subconvexity of Short k-Free Exponential Sums*, arXiv:2608.16679v1 (17 August 2026), studies

\[
S_k(\alpha;K)
=
\sum_{N-K<n\le N}\mu_k(n)e(n\alpha),
\]

where `mu_k` is the indicator of `k`-free integers. The technical bottleneck is the middle-part coefficient

\[
c_n(y,z)
=
\sum_{\substack{y<d\le z\\d^k\mid n}}\mu(d),
\tag{5}
\]

which enters through the classical support identity

\[
\mu_k(n)=\sum_{d^k\mid n}\mu(d).
\tag{6}
\]

Doyle proves an improved quadratic estimate for `sum |c_n(y,z)|^2` and shows that improvements to the corresponding exponent `Delta_k` would immediately improve the short-interval moment thresholds for `S_k`. For `k=2`, this is a refined `ell^2` control on the inclusion-exclusion decomposition of the square-free indicator `mu^2`.

The paper's Möbius application appears in Theorem 1.7. It defines

\[
G(\alpha)=\sum_{N-K<n\le N}\mu(n)e(n\alpha)
\]

and explicitly uses

\[
\int_0^1\overline{G(\beta)}G(\alpha+\beta)\,d\beta
=S_2(\alpha;K),
\]

followed by the `L^1` inequality in `(3)`. With the paper's current `Delta_2` bound this yields the stated `K^{1/6}` lower bound once `K\gg N^{105/317+\varepsilon}`.

The occurrence of the Möbius function inside `(5)` is therefore not, by itself, retained Möbius **orientation**. There it performs inclusion-exclusion over square divisors in order to reconstruct the support function `mu^2`; after `(2)`, the signs `mu(n)` of the target exponential sum have disappeared as well.

## 3. Matched-control obstruction for the `MC-172` target

The distinction from `MC-172` is exact. Its Gallagher energy has expansion

\[
\mathcal G_z(\beta,T)
=
\sum_{m,n\ge1}
\mu(m)^2\mu(n)^2
\chi_z(m)\overline{\chi_z(n)}
 e^{-\beta((\log m)^2+(\log n)^2)}
\left(1-T\left|\log\frac mn\right|\right)_+.
\tag{7}
\]

The off-diagonal factors

\[
\chi_z(m)\overline{\chi_z(n)},
\qquad m\ne n,
\]

are precisely the signed near-diagonal information carrier. By contrast, additive autocorrelation `(2)` enforces `m=n` and deletes this carrier exactly.

This is not merely a difference in notation. For every `0<tau<3/8`, `MC-172` proves for the all-plus control

\[
\lim_{\beta\downarrow0}
\beta\log\mathcal G_+
\!\left(\beta,e^{\tau/\beta}\right)
=
\frac12-\tau
>
\frac18,
\tag{8}
\]

whereas its live Möbius target asks whether the true phase can have diagonal exponential type `<=1/8` for some such `tau`. Any premise that depends only on `S_2`, the coefficients `c_n(y,z)` in `(5)`, or the phase-blind autocorrelation `(2)` is the same for the all-plus phase as for the Möbius phase. Such a premise therefore cannot, without an additional phase-sensitive input, imply the `MC-172` diagonal-type target: it would imply the same false conclusion for the all-plus matched control.

So improvements to Doyle's `Delta_2` may push the `k`-free moment theory to much shorter intervals, but **improving `Delta_2` alone does not close the information gap identified by `MC-172`.** The missing object must survive off the additive autocorrelation diagonal.

## 4. Prior-art and novelty audit

The autocorrelation identity used here is classical Fourier orthogonality, and Doyle states its Möbius specialization explicitly in the proof of Theorem 1.7, referring to the earlier complete-sum Balog--Ruzsa argument. No novelty is claimed for `(2)`, Young's inequality, the `k`-free decomposition `(6)`, Doyle's middle-part estimate, or the resulting `L^1` lower bound.

The new literature input is current: Doyle's preprint was submitted on 17 August 2026 and explicitly identifies the middle-part `ell^2` estimate as the bottleneck for his short `k`-free moment exponents. A targeted check of the paper finds the Möbius-twisted conclusion only through Theorem 1.7's autocorrelation transfer, where the coefficient becomes `mu^2` exactly.

The Mathia-specific contribution is the matched-control classification relative to the already persisted `MC-172` target: extending the displayed autocorrelation to arbitrary support-matched phases makes the lost discriminator explicit and proves that the tempting new `ell^2` route is still on the support side of the signed-cancellation boundary.

## 5. Boundaries and falsification controls

This finding does **not** claim that Doyle's analytic techniques are intrinsically phase-blind. It classifies the information content of the current middle-part `k`-free estimate and the specific autocorrelation transfer used for the Möbius application.

It would be falsified as a route-level obstruction by an additional theorem using Doyle's machinery that, before collapsing to `mu^2`, controls a quantity depending on `chi_z(m)overline{chi_z(n)}` for distinct `m,n` and yields a phase-sensitive upper bound relevant to `(7)`. Merely improving the exponent `Delta_2`, the moments of `S_2`, or the lower bound in `(4)` does not do so.

The conclusion also does not say that additive Fourier analysis is useless for Möbius cancellation. A different additive statistic can retain phase. The obstruction applies only when the relevant arithmetic information is passed through the autocorrelation `(2)` or an equivalent support-only quotient.

## Consequence for the research line

`MC-172` remains the live intermediate target, but the newest sub-square-root `k`-free `ell^2` technology does not directly supply its missing signed energy estimate. The decisive search should therefore ask for a **pre-autocorrelation or off-diagonal refinement** of short-interval machinery: a source-forced quadratic or bilinear quantity that keeps the relative Möbius phase of distinct nearby integers instead of reducing first to square-free support.
