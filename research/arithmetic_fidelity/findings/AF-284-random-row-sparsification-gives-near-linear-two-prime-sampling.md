# AF-284 — Random row sparsification gives near-linear two-prime sampling

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `JOINT-SAMPLING`, `FINITE-BREADTH`, `STABILITY`, `SPARSIFICATION`, `NO-NOVELTY-CLAIM`

## Claim

AF-283 proves that the complete two-prime mixed square with coordinatewise cutoff `L=30N` gives a uniformly stable inverse on the known Dirichlet prefix `1,...,N`, but that construction pays for all

\[
L^2=900N^2
\]

mixed moments. That quadratic observation count is not intrinsic to the stable inverse.

Keep AF-283's nodes

\[
t_n=
\left(-\frac{\log n}{\log2},-\frac{\log n}{\log3}\right)
\pmod{\mathbb Z^2},
\qquad
z_n=e^{2\pi i t_n},
\]

and the full mixed index square

\[
\mathcal Q_L=\{0,\ldots,L-1\}^2,
\qquad L=30N.
\]

Then there exists an **unweighted subset of distinct mixed indices**

\[
\Omega_N\subset\mathcal Q_L
\]

with

\[
\boxed{
|\Omega_N|
\le
2\left\lceil10N\log(4N)\right\rceil
=O(N\log N)
}
\]

such that the raw observations

\[
y_\nu
=
\sum_{n=1}^N b_n z_n^\nu,
\qquad \nu\in\Omega_N,
\]

have a breadth-uniform stable inverse. In particular, if each selected scalar moment is perturbed adversarially by at most `epsilon`, least-squares recovery on the known support satisfies

\[
\boxed{
\|\widehat b-b\|_2
<\frac{20}{9}\,\epsilon.
}
\]

Thus the sufficient scalar-observation count in AF-283 drops from `Theta(N^2)` to `O(N log N)` without averaging repeated measurements, assigning acquisition weights, or assuming stochastic noise. Randomness is used only as a probabilistic-method proof that a suitable deterministic subset exists.

This is a direct arithmetic specialization of classical matrix Chernoff / random row-sampling machinery. No new general sparsification theorem is claimed.

## Full frame inherited from AF-283

Let

\[
M=L^2=900N^2
\]

and write the AF-283 observation matrix as

\[
A=V_{N,L}^{T}\in\mathbb C^{M\times N}.
\]

For `nu in Q_L`, let `r_nu` denote the corresponding row,

\[
r_\nu=(z_1^\nu,\ldots,z_N^\nu).
\]

Every entry has modulus one, so every row has exactly the same squared Euclidean norm:

\[
\boxed{\|r_\nu\|_2^2=N.}
\]

AF-283 applies the Kunis--Nagel--Strotmann separated-node theorem at `L=30N` and obtains

\[
\sigma_{\min}(A)>0.9L.
\]

Therefore the full frame operator

\[
S=A^*A
=
\sum_{\nu\in\mathcal Q_L}r_\nu^*r_\nu
\]

obeys

\[
\boxed{
\lambda_{\min}(S)>0.81L^2=0.81M.
}
\]

The key point for sparsification is that the full arithmetic frame already has a spectral lower bound proportional to its number of rows while each individual row contributes operator norm only `N`.

## Bernoulli row selection

Set

\[
m_0=\left\lceil10N\log(4N)\right\rceil,
\qquad
p=\frac{m_0}{M}.
\]

For every `nu in Q_L`, independently retain that row with Bernoulli variable `delta_nu` of mean `p`. Let

\[
\Omega=\{\nu:\delta_\nu=1\}
\]

and let the selected Gram matrix be

\[
G
=
A_\Omega^*A_\Omega
=
\sum_{\nu\in\mathcal Q_L}
\delta_\nu r_\nu^*r_\nu.
\]

Its expectation is

\[
\mathbb E G=pS,
\]

hence

\[
\mu_{\min}
:=
\lambda_{\min}(\mathbb E G)
>
0.81pM
=
0.81m_0.
\]

Each independent positive-semidefinite summand satisfies

\[
\lambda_{\max}(\delta_\nu r_\nu^*r_\nu)
\le
\|r_\nu\|_2^2
=N.
\]

Tropp's matrix Chernoff lower-tail bound therefore applies directly.

## Positive probability of a small stable subset

Use the standard simplified matrix Chernoff inequality

\[
\Pr\!\left[
\lambda_{\min}(G)
\le
(1-\delta)\mu_{\min}
\right]
\le
N\exp\!\left(
-\frac{\delta^2\mu_{\min}}{2N}
\right).
\]

At `delta=1/2`,

\[
\Pr\!\left[
\lambda_{\min}(G)
\le
\frac12\mu_{\min}
\right]
\le
N\exp\!\left(-\frac{\mu_{\min}}{8N}\right).
\]

Since `mu_min>0.81m_0` and `m_0>=10N log(4N)`,

\[
\begin{aligned}
\Pr\!\left[
\lambda_{\min}(G)
\le
0.405m_0
\right]
&<
N\exp\!\left(-\frac{0.81m_0}{8N}\right)\\
&\le
N(4N)^{-81/80}\\
&<\frac14.
\end{aligned}
\]

On the other hand,

\[
\mathbb E|\Omega|=m_0.
\]

Markov's inequality gives

\[
\Pr[|\Omega|>2m_0]\le\frac12.
\]

By the union bound, with strictly positive probability both events hold:

\[
|\Omega|\le2m_0
\]

and

\[
\lambda_{\min}(A_\Omega^*A_\Omega)
>0.405m_0.
\]

Consequently there exists a fixed deterministic subset `Omega_N` satisfying both. Its observation matrix obeys

\[
\boxed{
\sigma_{\min}(A_{\Omega_N})
>
\sqrt{0.405m_0}.
}
\]

No row is selected more than once, and no row receives a reconstruction or acquisition weight in this existence statement.

## Uniform absolute-noise stability

Suppose the selected observations are perturbed by an arbitrary vector `eta` satisfying

\[
\|\eta\|_\infty\le\epsilon.
\]

Since `|Omega_N|<=2m_0`,

\[
\|\eta\|_2
\le
\sqrt{2m_0}\,\epsilon.
\]

Least-squares recovery therefore gives

\[
\begin{aligned}
\|\widehat b-b\|_2
&\le
\frac{\|\eta\|_2}
{\sigma_{\min}(A_{\Omega_N})}\\
&<
\sqrt{\frac{2}{0.405}}\,\epsilon\\
&=
\boxed{\frac{20}{9}\,\epsilon}.
\end{aligned}
\]

The cancellation of `m_0` is the relevant fidelity statement: although the selected frame gets larger with source breadth, the worst-case coefficient error produced by a fixed absolute error in every retained scalar observation remains bounded independently of `N`.

## The selected rows are genuine distinct Dirichlet samples

The mixed index `nu=(nu_1,nu_2)` corresponds to the vertical sample time

\[
t(\nu)
=
\nu_1\frac{2\pi}{\log2}
+
\nu_2\frac{2\pi}{\log3}.
\]

Two integer pairs cannot produce the same time. If `t(nu)=t(mu)`, then

\[
(\nu_1-\mu_1)\log3
+(\nu_2-\mu_2)\log2=0,
\]

so

\[
3^{\nu_1-\mu_1}2^{\nu_2-\mu_2}=1.
\]

Unique factorization forces both integer differences to vanish. Thus `Omega_N` represents `|Omega_N|` distinct scalar samples of the original Dirichlet channel rather than aliases of the same acquisition time.

## Prior art and novelty assessment

No random-matrix, row-sampling, or spectral-sparsification novelty is claimed.

Joel A. Tropp, **“User-Friendly Tail Bounds for Sums of Random Matrices,”** *Foundations of Computational Mathematics* 12 (2012), 389--434, DOI `10.1007/s10208-011-9099-z`, proves the matrix Chernoff lower-tail inequality used above for sums of independent positive-semidefinite random matrices. AF-284 is a direct application after inserting AF-283's arithmetic frame lower bound and its equal row norms.

Malik Magdon-Ismail, **“Row Sampling for Matrix Algorithms via a Non-Commutative Bernstein Bound,”** arXiv:`1008.0587` (2010), is representative prior art for preserving matrix/subspace information by retaining a small number of actual rows through random sampling and matrix concentration. The present `O(N log N)` count belongs to that classical methodological family.

Joshua Batson, Daniel A. Spielman, and Nikhil Srivastava, **“Twice-Ramanujan Sparsifiers,”** *SIAM Journal on Computing* 41(6) (2012), 1704--1721, DOI `10.1137/090772873`, establishes linear-size weighted spectral sparsification in a closely related rank-one/quadratic-form setting. It is an important boundary marker rather than the theorem used here: AF-284 specifically retains an **unweighted subset of raw acquisition rows**, so the possibility of removing the logarithmic factor with weights does not by itself supply an `O(N)` raw-sample theorem for this channel.

The retained contribution is therefore the arithmetic resource consequence: once AF-283's two-prime frame is recognized as a highly redundant stable frame, standard concentration reduces its raw scalar acquisition count from quadratic to near-linear while preserving a breadth-independent inverse modulus under adversarial per-sample absolute noise.

## Boundaries and failure modes

- The theorem is existential. Independent Bernoulli sampling proves that a good subset exists; no explicit deterministic formula for `Omega_N` is supplied.
- The source support is known a priori to be `1,...,N`. Unknown-support super-resolution remains a different problem.
- The recovered variables are the weighted coefficients `b_n=a_n n^{-c}` from AF-283. Converting to another coefficient norm can reintroduce an `N`-dependent weight bill.
- The noise model is adversarial absolute error bounded separately on every selected scalar sample. Relative error, timing error, or another norm requires a separate propagation analysis.
- The selected indices remain inside the AF-283 square `0<=nu_j<30N`; this result reduces observation count, not coordinatewise mixed degree or maximal time horizon.
- The constant `10` in `m_0` and the final `20/9` error factor are convenient explicit consequences of the coarse Chernoff/Markov argument. They are not optimized.
- `O(N log N)` is a sufficient count, not a lower bound and not an optimality claim. Rank still gives only the elementary requirement of at least `N` scalar observations for arbitrary recovery of `N` coefficients.
- Weighted spectral sparsification, repeated/averaged observations, leverage-score sampling, and rescaled measurement operators are distinct acquisition models. They cannot be silently substituted for the raw unweighted subset proved here.
- The probabilistic proof does not assert that a uniformly random subset of every size `O(N log N)` is good, only that the declared Bernoulli experiment has positive probability of producing a subset satisfying both the size and spectral conditions.
- No analytic continuation, zero-location statement, functional equation, or RH consequence follows from this finite-prefix sampling theorem alone.

## Decisive audit test

When a two-prime finite-prefix proposal treats AF-283's `Theta(N^2)` complete square as the unavoidable price of stable coefficient recovery, inspect whether the argument uses any property beyond the full-frame lower spectral bound and the norm of each acquisition row.

For the AF-283 frame those two quantities already imply, by classical matrix concentration, the existence of an unweighted raw subset of at most `2 ceil(10N log(4N))` distinct mixed moments with coefficient error below `(20/9) epsilon` under per-sample absolute error `epsilon`. A claimed quadratic observation lower bound must therefore impose an additional restriction not present here, such as a deterministic geometric pattern, a much smaller time window, timing precision, a different source/target norm, unknown support, or a stronger robustness requirement.

## Consequence for the research line

AF-283's `Omega(N)` versus `O(N^2)` scalar-observation gap narrows to

\[
\boxed{
\Omega(N)
\quad\text{versus}\quad
O(N\log N).
}
\]

The next meaningful sparsity question is now precise: determine whether the logarithmic factor is an artifact of generic independent row sampling or is forced by **unweighted raw mixed-moment acquisition** on this arithmetic node family. Two concrete branches remain distinct: construct an explicit/deterministic `O(N)` or `O(N log N)` index family with comparable stability, or prove a superlinear lower bound under a clearly stated unweighted timing geometry. Weighted `O(N)` spectral sparsification is relevant prior art but should be analyzed separately because weights change the physical observation/noise semantics.