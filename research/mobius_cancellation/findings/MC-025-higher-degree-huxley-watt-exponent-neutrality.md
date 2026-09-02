# MC-025 — Higher-degree Huxley–Watt factorization is power-exponent neutral

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DECISIVE-NEGATIVE`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The higher-degree Huxley–Watt identities do not evade the exponent-neutrality barrier of `MC-024` merely by replacing the quadratic `N -> N^2` transfer with a degree-`d` factorization and a longer scale jump `N -> N^d`.

The source identity underlying Huxley and Watt's general theorem factorizes the truncated reciprocal-zeta error multiplicatively. Let, for `Re(s)>1`,

\[
F_N(s)=\sum_{n\le N}\frac{\mu(n)}{n^s},
\qquad
R_N(s)=\frac1{\zeta(s)}-F_N(s)
=\sum_{n>N}\frac{\mu(n)}{n^s}.
\tag{1}
\]

For positive cutoffs `N_1,...,N_d`, Huxley and Watt record

\[
\frac1{\zeta(s)}
\prod_{j=1}^{d}\left(1-\zeta(s)F_{N_j}(s)\right)
=
\zeta(s)^{d-1}\prod_{j=1}^{d}R_{N_j}(s).
\tag{2}
\]

Since

\[
1-\zeta(s)F_{N_j}(s)=\zeta(s)R_{N_j}(s),
\tag{3}
\]

equation (2) is the exact product factorization whose coefficient extraction yields their general finite Möbius identity.

Suppose a candidate analytic argument controls the tail errors in any submultiplicative norm on a region where `zeta` is bounded:

\[
\|R_{N_j}\|\le C_j N_j^{-\alpha_j}.
\tag{4}
\]

Then the product side of (2) satisfies

\[
\left\|\zeta^{d-1}\prod_{j=1}^{d}R_{N_j}\right\|
\le
\|\zeta\|^{d-1}
\left(\prod_{j=1}^{d}C_j\right)
\prod_{j=1}^{d}N_j^{-\alpha_j}.
\tag{5}
\]

If the Huxley–Watt cutoffs are chosen at power scales

\[
N_j=K^{\theta_j+o(1)},
\qquad
\theta_j>0,
\qquad
\sum_{j=1}^{d}\theta_j=1,
\tag{6}
\]

as in their admissible parameterization, the polynomial exponent on the right of (5) is

\[
\boxed{
\alpha_{\rm out}
=
\sum_{j=1}^{d}\theta_j\alpha_j.
}
\tag{7}
\]

Thus the generic product exponent is a **convex combination** of the input exponents. In particular,

\[
\alpha_{\rm out}\le \max_j\alpha_j,
\tag{8}
\]

and if all inputs have the same exponent `alpha`, then

\[
\boxed{\alpha_{\rm out}=\alpha.}
\tag{9}
\]

For the symmetric specialization `N_1=...=N_d=N` and `K=N^d`, this is simply

\[
(N^{-\alpha})^d=N^{-d\alpha}=(N^d)^{-\alpha}=K^{-\alpha}.
\tag{10}
\]

Therefore increasing the algebraic degree and the scale-jump degree together produces **no power-exponent amplification** under generic product/norm control. The apparent gain from multiplying `d` small errors is exactly consumed by the fact that the target scale is the product of the `d` input scales.

This remains true at the polynomial level in the one-sided shrinking regime left open by `MC-024`. At a point

\[
s_K=1+\frac{c}{\log K},\qquad c>0,
\tag{11}
\]

one has classically `zeta(s_K)=O_c(log K)`. Hence any hypotheses of the form

\[
|R_{N_j}(s_K)|
\le
C_jN_j^{-\alpha_j}(\log K)^{A_j}
\tag{12}
\]

give only

\[
\left|\zeta(s_K)^{d-1}
\prod_jR_{N_j}(s_K)\right|
\ll
K^{-\sum_j\theta_j\alpha_j}
(\log K)^{d-1+\sum_jA_j+o(1)}.
\tag{13}
\]

The pole contributes logarithmic factors but does not change the power ledger. So neither fixed `d>2` nor unequal power-scale cutoffs can turn a weaker common power exponent into a stronger one by factorization alone.

The conclusion is deliberately narrow. Huxley–Watt coefficient extraction may still expose **additional signed arithmetic cancellation** inside the finite multilinear sums; different inputs may carry genuinely different independently proved exponents; and cancellations between terms of different degrees may outperform the absolute product budget. What is ruled out is the degree-only bootstrap: the slogan "use `d=3,4,...` because higher-order errors contract faster" is false at the exact scale dictated by the source identity.

## 1. Source identity and coefficient extraction

Huxley and Watt prove a general identity for

\[
M(g,K)=\sum_{n\le K}\mu(n)g(n)
\]

with arbitrary totally multiplicative `g` and independent cutoffs `N_1,...,N_d`, under the condition

\[
K<(1+N_1)\cdots(1+N_d).
\tag{14}
\]

Their Theorem 1 is obtained by inclusion–exclusion and Möbius contraction. They also give (2), in their notation equation (1.10), as a second Dirichlet-series proof: multiply out the factors and extract Dirichlet coefficients under the same cutoff condition.

For equal ranges and `K=N^d`, the resulting finite formula expresses `M(g,N^d)` using products of at most `d` Möbius values whose arguments are at most `N`. The paper explicitly notes that these equal-range special cases are classical and are related to Vaughan/Linnik/Heath-Brown-type identities; the flexibility of independent ranges is the part they single out as new.

For the present audit, no detailed estimate of the finite coefficient sums is needed. Equation (2) already fixes the algebraic degree and the multiplicative scale bookkeeping of any argument that tries to obtain a gain solely from the product of truncated Dirichlet-series errors.

## 2. Anisotropic cutoffs cannot beat the best input exponent generically

The independent ranges in Huxley–Watt might appear to offer a way around the symmetric neutrality (10). Equation (7) shows exactly what they buy under a product estimate.

If, for example, two input families have exponents `alpha_1<alpha_2`, choosing a larger `theta_2` gives an output exponent closer to `alpha_2`, but never beyond it. More generally,

\[
\min_j\alpha_j
\le
\sum_j\theta_j\alpha_j
\le
\max_j\alpha_j.
\tag{15}
\]

Thus range optimization can allocate scale toward an already stronger input, but it cannot manufacture a new exponent. A strict improvement beyond the best available input requires a bound not implied by submultiplicativity of the separate tail controls.

This distinction matters for the active Möbius line. `MC-024` showed that the centered `d=2` analytic map is quadratic and therefore exponent-neutral under `N -> N^2`. Moving to a higher Huxley–Watt degree changes both numbers in lockstep: degree `d` is paired with a target whose natural size parameter is the product of `d` input cutoffs. The same obstruction persists.

## 3. The one-sided shrinking regime only adds logarithmic pole cost

`MC-024` left a shrinking neighborhood of the pole as the non-circular analytic regime worth considering, because a fixed leftward displacement can itself encode a fixed zero-free half-plane.

The present calculation shows that higher degree does not alter the power arithmetic there either. Taking `s_K` as in (11), the classical pole expansion

\[
\zeta(1+t)=\frac1t+O(1)
\qquad(t\to0^+)
\tag{16}
\]

gives

\[
\zeta(s_K)^{d-1}=O_c((\log K)^{d-1}).
\tag{17}
\]

Substitution into the exact factorization yields (13). For fixed `d`, all additional cost is polylogarithmic. It can be absorbed into `K^epsilon` in RH-scale bookkeeping, but it cannot supply the missing fixed power gain.

This does not analyze the removable singularities that arise after the more delicate reciprocal-zeta centering of `MC-023`; those cancellations can reorganize the individual finite terms. It proves only that the **raw d-fold error factorization itself** has no hidden polynomial amplifier as the evaluation point approaches the pole from the right.

## 4. Prior art and novelty boundary

The mathematical identity is prior art. The primary source is M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20–34, arXiv `1807.05890`, DOI `10.22405/2226-8383-2018-19-3-20-34`. Their abstract states the `M(N^d)` family, and Theorem 1 plus equation (1.10) give the independent-range and Dirichlet-factorization forms used here. The same paper explicitly places the equal-range special cases beside Vaughan, Linnik, and Heath-Brown-type identities.

Heath-Brown's generalized Vaughan identity is adjacent classical prior art for using higher-order truncated Dirichlet factorizations to create Type I/II decompositions in analytic number theory. No novelty is claimed for that general method, for the elementary tail factorization (3), for submultiplicativity, or for the convex-combination algebra in (7).

A targeted literature search for Huxley–Watt higher-degree identities together with Mertens power-exponent bootstrapping located the original source and the standard Vaughan/Heath-Brown decomposition lineage, but no authoritative source was found presenting the specific exponent-neutrality ledger (7) as an RH mechanism audit. Absence from that search is not evidence of novelty. The durable result is the negative conclusion inside the current Mathia route: **higher Huxley–Watt degree by itself cannot repair the exponent-neutral analytic closure identified at degree two.**

## 5. Consequence for the active frontier

This closes one obvious escape from `MC-024`. The active route should not spend further effort on fixed higher degrees merely to obtain a higher-order product contraction.

A surviving higher-degree use must identify information beyond the product norm, for example:

- a signed multilinear estimate that gains a fixed power over the product of separate tail bounds;
- cancellation between different inclusion–exclusion degrees that survives exact recombination;
- an input observable with an independently stronger exponent whose coupling forces improvement of the weaker Möbius state rather than merely averaging exponents;
- or a scale geometry not tied to `K` being the product of the input cutoffs.

Any such proposal must be tested against the exact ledger (7). If its proof reduces to multiplying independently controlled errors with `prod N_j` comparable to `K`, it is exponent-neutral and does not constitute a bootstrap.

The remaining question is therefore the same one exposed at degree two but now with the entire classical Huxley–Watt hierarchy audited: **where can a genuinely Möbius-specific signed power gain enter, beyond the generic algebra of truncated reciprocal-zeta factorization?**