# NB-188 — Hadamard-scale Euler aggregation forces square-root source amplification and bounded fanout

**Date:** 2026-09-17  
**Status:** `DERIVED + SOURCE-FIDELITY + EULER-WIENER + AGGREGATE-ACQUISITION + SOURCE-DENSITY-GAIN + FANOUT-BARRIER + NB-187-REFINEMENT`.

`NB-187` leaves one concrete positive route: instead of exposing only `N asymp 1/a` individual prime channels, compress the exponentially larger true-amplitude Euler population into only `O(1/a)` effective probes and try to preserve the `N^(3/2)` nuclear response required by `NB-178`.

The broadest same-frequency Wiener version of that idea already has a sharp structural tariff. Allow every probe to use an arbitrary complex coefficient mask on all Euler characters, not merely a vertical translate or Fourier--Stieltjes mixture. Then a Hadamard-scale response cannot be obtained by bounded rephasing or by broadly reusing the same source mass across many output coordinates. It forces two things simultaneously:

1. the probe family must have RMS coefficient density, relative to the actual normalized Euler-Wiener source, at least of order `sqrt N`; and
2. if every probe is kept inside unit absolute Wiener budget, the effective fanout of source coefficients across output probes must remain `O(1)`.

Thus the surviving aggregate route is not generic overlapping reuse. At leading order it must look like low-overlap routing or partitioning of the Euler mass, with an explicit square-root source-amplification tariff. On the vanishing-mass Poisson prime block from `NB-187`, that tariff becomes still larger.

## Setup

Use the exact normalized Euler-Wiener decomposition of `NB-182`. Write

\[
\lambda_n:=\log n,
\qquad
M_a(\lambda):=\max\{2,a\lambda\},
\]

\[
\phi_{n,a}(u)
:=
\frac{e^{-iu\lambda_n}}{M_a(\lambda_n)},
\qquad
\alpha_{n,a}
:=
\frac{\Lambda(n)n^{-1-a}M_a(\lambda_n)}{\mathcal W(a)}.
\tag{1}
\]

Then `alpha_(n,a)>=0`, `sum_n alpha_(n,a)=1`, and each `phi_(n,a)` is unit contractive for the capped metric

\[
d_a(u,v)=\min\left\{1,\frac{|u-v|}{a}\right\}.
\tag{2}
\]

Choose `N` zero-mass templates `nu_1,...,nu_N` with

\[
\mathsf D_a(\nu_i)\le qX.
\tag{3}
\]

For each Euler channel define its template-response column

\[
b_{i,n}
:=
\frac1q\int \phi_{n,a}(u)\,d\nu_i(u),
\qquad
b_n:=(b_{1,n},...,b_{N,n})^T.
\tag{4}
\]

Capped Kantorovich--Rubinstein duality gives

\[
|b_{i,n}|\le X,
\qquad
\|b_n\|_2\le X\sqrt N.
\tag{5}
\]

Now allow **arbitrary same-frequency Wiener aggregates**. For `1<=k<=K`, let

\[
F_k(u)
:=
\sum_{n\ge2}\beta_{k,n}\phi_{n,a}(u),
\tag{6}
\]

where each coefficient row is absolutely summable. The scalar probe is

\[
\ell_k(\sigma)
:=
\frac1q\int F_k(u)\,d\sigma(u).
\tag{7}
\]

Its absolute Wiener acquisition budget is

\[
g_k:=\sum_n|\beta_{k,n}|.
\tag{8}
\]

Because every atom in (1) is unit capped-contracting,

\[
|\ell_k(\sigma)|
\le
 g_k\frac{\mathsf D_a(\sigma)}q.
\tag{9}
\]

Thus `g_k<=1` is a sufficient source-safe condition for `NB-178` coordinatewise contractivity. This class is much larger than the Fourier--Stieltjes translates of `NB-182`: the coefficients `beta_(k,n)` may be arbitrary frequency-dependent masks.

Relative to the true Euler-Wiener source, write

\[
\beta_{k,n}=\alpha_{n,a}m_{k,n}.
\tag{10}
\]

The multiplier `m_(k,n)` is the exact coefficient gain applied to source channel `n` in probe `k`.

## Claim 1: source-relative density gain controls nuclear response

Let `S` be any set of Euler channels containing the support of every `beta_(k,.)`, and let

\[
\Theta_S
:=
\sum_{n\in S}\alpha_{n,a}.
\tag{11}
\]

Define the RMS **source-density gain**

\[
\mathcal G_\alpha^2
:=
\frac1K
\sum_{k=1}^K\sum_{n\in S}
\frac{|\beta_{k,n}|^2}{\alpha_{n,a}}
=
\frac1K
\sum_{n\in S}\alpha_{n,a}
\|m_n\|_2^2,
\tag{12}
\]

where `m_n=(m_(1,n),...,m_(K,n))^T`.

Let `A` be the `N x K` response matrix

\[
A_{ik}:=\ell_k(\nu_i).
\tag{13}
\]

Then

\[
\boxed{
\|A\|_*
\le
X\sqrt{NK\Theta_S}\,\mathcal G_\alpha.
}
\tag{14}
\]

Consequently, when `N=K`, any response with Hadamard-scale nuclear mass

\[
\|A\|_*
\ge
\gamma XN^{3/2}
\tag{15}
\]

for fixed `gamma>0` must satisfy

\[
\boxed{
\mathcal G_\alpha
\ge
\gamma\sqrt{\frac N{\Theta_S}}.
}
\tag{16}
\]

In particular, even if the probes use the **entire** Euler-Wiener source (`Theta_S=1`), a dense rank-`N` certificate forces

\[
\boxed{
\mathcal G_\alpha\ge\gamma\sqrt N.
}
\tag{17}
\]

Bounded source-relative rephasing therefore cannot produce growing Hadamard-scale response, no matter how many Euler channels are aggregated.

There is also an `ell^infinity` consequence. If

\[
|m_{k,n}|\le M
\qquad(k,n),
\tag{18}
\]

then `mathcal G_alpha<=M sqrt(Theta_S)`, so (16) forces

\[
\boxed{
M
\ge
\gamma\frac{\sqrt N}{\Theta_S}.
}
\tag{19}
\]

Thus a vanishing source-mass block cannot be repaired merely by renormalizing that block to total mass one; a dense coordinatewise code needs a further `sqrt N`-scale coefficient amplification.

## Claim 2: broad source fanout loses nuclear mass

For each channel let

\[
\beta_n
:=
(\beta_{1,n},...,\beta_{K,n})^T,
\]

and define

\[
B_1
:=
\sum_n\|\beta_n\|_1
=
\sum_{k=1}^K g_k,
\qquad
B_2
:=
\sum_n\|\beta_n\|_2.
\tag{20}
\]

When `B_2>0`, define the effective coefficient fanout

\[
\boxed{
\mathcal F_{\rm eff}
:=
\left(\frac{B_1}{B_2}\right)^2.
}
\tag{21}
\]

Since `||x||_2<=||x||_1<=sqrt(K)||x||_2`, one always has

\[
1\le\mathcal F_{\rm eff}\le K.
\tag{22}
\]

If every probe has unit Wiener budget `g_k<=1`, then

\[
\boxed{
\|A\|_*
\le
\frac{XK\sqrt N}{\sqrt{\mathcal F_{\rm eff}}}.
}
\tag{23}
\]

Hence, for `N=K`, the Hadamard-scale condition (15) implies

\[
\boxed{
\mathcal F_{\rm eff}\le\gamma^{-2}.
}
\tag{24}
\]

So a fixed-fraction dense code is incompatible with fanout growing with `N`. The same source coefficient may be reused in a bounded number of output directions, but not spread approximately evenly over a growing fraction of them.

A convenient pointwise version is the following. If every active channel obeys

\[
\|\beta_n\|_1
\ge
\sqrt L\,\|\beta_n\|_2,
\tag{25}
\]

then `mathcal F_eff>=L` and

\[
\boxed{
\|A\|_*
\le
XK\sqrt{\frac NL}.
}
\tag{26}
\]

Thus `L->infinity` broad reuse destroys a fixed-fraction Hadamard-scale certificate.

## Derivation

Equation (13) has the rank-one expansion

\[
A
=
\sum_n b_n\beta_n^T.
\tag{27}
\]

The trace norm of a rank-one matrix is the product of the Euclidean norms of its two factors. Using (5),

\[
\|A\|_*
\le
\sum_n\|b_n\|_2\|\beta_n\|_2
\le
X\sqrt N\,B_2.
\tag{28}
\]

For Claim 1, weighted Cauchy--Schwarz on the support `S` gives

\[
B_2
=
\sum_{n\in S}
\sqrt{\alpha_{n,a}}
\frac{\|\beta_n\|_2}{\sqrt{\alpha_{n,a}}}
\le
\sqrt{\Theta_S}
\left(
\sum_{n\in S}
\frac{\|\beta_n\|_2^2}{\alpha_{n,a}}
\right)^{1/2}.
\tag{29}
\]

By (12), the second factor is `sqrt(K) mathcal G_alpha`; inserting this into (28) proves (14). Equations (16)--(19) are immediate.

For Claim 2, (21) gives `B_2=B_1/sqrt(mathcal F_eff)`, while `g_k<=1` gives `B_1<=K`. Insert both into (28) to obtain (23). Equations (24)--(26) follow.

No probabilistic, zero-density or prime-distribution input enters these inequalities. They are exact factorization constraints once the Euler-Wiener atoms and the coefficient acquisition architecture have been declared.

## The two extremal architectures

The theorem interpolates cleanly between the two acquisition extremes already isolated by `NB-180`--`NB-182`.

For genuine vertical translates,

\[
\beta_{k,n}
=
\alpha_{n,a}e^{-it_k\lambda_n}.
\tag{30}
\]

Then every row has `g_k=1`, while

\[
\mathcal G_\alpha=1,
\qquad
\mathcal F_{\rm eff}=K.
\tag{31}
\]

Thus the actual scalar source maximally reuses every Euler coefficient across all output coordinates and lands at the worst fanout end. Equations (14) and (23) both reduce to the `NB-182` order-`X sqrt(NK)` nuclear ceiling.

At the opposite extreme, partition the source channels into disjoint sets `S_1,...,S_K` of masses

\[
\theta_k:=\sum_{n\in S_k}\alpha_{n,a}>0
\]

and normalize each bin separately:

\[
\beta_{k,n}
=
\frac{\alpha_{n,a}}{\theta_k}
 e^{i\vartheta_{k,n}}
\mathbf 1_{n\in S_k}.
\tag{32}
\]

Then every row again has `g_k=1`, but now

\[
\mathcal F_{\rm eff}=1
\tag{33}
\]

and

\[
\mathcal G_\alpha^2
=
\frac1K\sum_{k=1}^K\frac1{\theta_k}.
\tag{34}
\]

If the partition covers source mass `Theta=sum_k theta_k`, Cauchy--Schwarz gives

\[
\boxed{
\mathcal G_\alpha
\ge
\sqrt{\frac K\Theta}.
}
\tag{35}
\]

Equality occurs for equal-mass bins. Thus a balanced full-source partition (`Theta=1`) pays exactly the `sqrt K` source-density gain required by (17), while achieving the minimum possible fanout. The two tariffs are therefore not artifacts of loose estimates: the partition architecture sits exactly on their common boundary.

This does **not** construct a successful phase code from such bins. It says that after `NB-187`, the only obvious same-frequency Wiener architecture that is not already excluded at the representation level is partition-like or bounded-fanout routing, and it necessarily pays the square-root source-density amplification.

## Consequence for the NB-186 prime block

`NB-187` proves that for `N asymp 1/a`, any Poisson-scale set of individual prime channels has normalized Euler-Wiener mass

\[
\Theta_N(a)
=O\!\left(a\log\frac1a\right),
\tag{36}
\]

with the first `N` primes attaining the sharp asymptotic constant displayed there.

Suppose an aggregate acquisition is supported only on that raw phase block and seeks the `NB-186` nuclear scale `||A||_* >= gamma X N^(3/2)`. Equation (16) then forces

\[
\boxed{
\mathcal G_\alpha
\gg_\gamma
\frac1{a\sqrt{\log(1/a)}}.
}
\tag{37}
\]

This is stronger than merely renormalizing the whole block by its reciprocal mass `Theta_N(a)^(-1) asymp 1/(a log(1/a))`: block renormalization still treats the selected source as one aggregate coordinate. Recovering `N` dense coordinatewise directions requires an additional square-root rank tariff.

If one insists on uniformly bounded source-relative multipliers on that block, (19) is even harsher:

\[
M
\gg_\gamma
\frac1{a^{3/2}\log(1/a)}.
\tag{38}
\]

The exact exponent in (38) is a tariff for this bounded-multiplier model, not a universal lower bound on arbitrary arithmetic cancellation.

## Generality audit

**Generality audited.** The rank-one trace-norm estimate, weighted Cauchy--Schwarz, and the `ell^1/ell^2` fanout ratio are generic functional-analytic facts. Similar mixed-norm quantities occur throughout sparse factorization, Schur-multiplier and operator-ideal theory. Nothing in Claims 1--2 depends on primes once a positive convex atomic source `alpha_n` has been supplied.

The line-specific content is the choice of atoms and source density: `alpha_(n,a)` is the true normalized Euler-Wiener mass from `NB-182`; `NB-187` identifies its logarithmic-frequency distribution and proves that Poisson-many prime channels have vanishing `Theta_S`; and the target nuclear scale is exactly the one that feeds the `NB-178` approximate-source-complexity certificate. The finding therefore narrows a live source-fidelity route rather than asserting a new generic matrix theorem.

## Prior-art audit

Focused searches were made for coefficient multipliers of Wiener--Dirichlet algebras, Schur-multiplier/factorization norms, nuclear bounds with mixed `ell^1/ell^2` coefficient structure, and Nyman--Beurling uses of such source-relative acquisition costs. The surrounding ingredients are classical: Wiener algebras of Dirichlet series and coefficient multipliers are standard, `gamma_2`/Schur factorization theory provides a much broader operator-theoretic setting, and `ell^1/ell^2` ratios are common sparsity/fanout surrogates. No source located in this pass states the line-specific Euler-Wiener source-density gain (16), fanout obstruction (24), or the `NB-187` Poisson-block consequence (37).

No external theorem is load-bearing: every inequality above is derived directly from the already established `NB-182` atomic decomposition and `NB-187` mass estimate. `SOURCES.md` therefore remains unchanged.

## Self-review

The result is intentionally a representation theorem, not a new approximation theorem for the Nyman distance. It does not prove that low-fanout partitioned aggregates can actually realize the required height-phase matrix, and it does not rule out nonlinear probes or probes whose effective contractivity comes from arithmetic cancellation despite a large absolute Wiener budget.

The fanout statement (24) uses the absolute coefficient budgets `g_k<=1`. If a probe has much larger Wiener coefficient mass but nevertheless a small actual capped-Lipschitz norm because of source-specific cancellation, that extra cancellation is outside Claim 2. Claim 1 still records the corresponding source-density gain and shows that a dense code cannot obtain it from bounded relative reweighting.

Likewise, `mathcal G_alpha` is a source-relative acquisition currency, not a computational cost. It measures how far the probe coefficients move from the actual Euler-Wiener mass in weighted `ell^2`; for positive normalized coefficients it is the familiar chi-square-type density scale, but complex phases are allowed here and no probabilistic interpretation is required.

The remaining positive route is therefore substantially narrower but still real: construct `N asymp 1/a` **bounded-fanout, strongly reweighted aggregate probes** from the true Euler population, prove that their large source-density gain is paid by actual height-specific arithmetic cancellation rather than by an artificial coefficient oracle, and retain `N^(3/2)` nuclear mass on acquisition-good heights. A negative next step would show that such low-fanout partitions themselves have small phase response once their true Euler amplitudes and available height window are imposed.