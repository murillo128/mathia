# MC-364 — Near-endpoint product dephasing requires logarithmic Bhattacharyya depth

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-360` introduced Hellinger affinity because it tensorizes through conditionally independent transcript components, but then upper-bounded the product loss by the linear union bound

\[
1-\prod_j(1-z_j)\le \sum_j z_j.
\]

`MC-363` subsequently made the required **output** Hellinger boundary sharp near exact matched-filter-energy dephasing. Keeping the product rather than linearizing it exposes a stronger resource that the linear incidence ledger cannot see: the additive **negative log-affinity**, equivalently Bhattacharyya distance.

Continue the even-rank reciprocal endpoint notation

\[
m=2^R-1,
\qquad
q_R=\frac{m-1}{m},
\]

and let

\[
\mathfrak H_1
=\frac2m\sum_{e\in E(S)}H^2(P_x,P_{x'})
\]

be the output Hellinger edge budget. Suppose the admitted transcript has the source-independent latent/product architecture from `MC-360`: a latent variable `\Theta\sim\nu` independent of the source state, followed conditionally on `\Theta` by independent components `Y_1,\ldots,Y_k`.

For component `j`, let `A_j\subseteq\{1,\ldots,R\}` be the source coordinates on which it may depend. Assume that for every surviving source edge `e={x,x'}` in direction `i\in A_j` and `\nu`-almost every `\theta`,

\[
H^2\!\left(
K_{x,j}(\cdot\mid\theta),
K_{x',j}(\cdot\mid\theta)
\right)
\le \alpha_{j,i},
\qquad 0\le\alpha_{j,i}\le1.
\tag{1}
\]

For `i\notin A_j` set `\alpha_{j,i}=0`. Define the component log-affinity cost

\[
\lambda_{j,i}:=-\log(1-\alpha_{j,i})\in[0,\infty],
\qquad
\Lambda_i:=\sum_j\lambda_{j,i},
\tag{2}
\]

with the convention `-\log0=+\infty`.

Then every surviving edge in direction `i` satisfies

\[
\boxed{
H^2(P_x,P_{x'})
\le
1-e^{-\Lambda_i}.
}
\tag{3}
\]

Consequently

\[
\boxed{
\frac{\mathfrak H_1}{R}
\le
q_R\left(
1-\frac1R\sum_{i=1}^R e^{-\Lambda_i}
\right).
}
\tag{4}
\]

Now use the sharp `MC-363` output floor. With its notation, put

\[
z_R:=1-2\sqrt{p(y_R)(1-p(y_R))},
\qquad
\beta_R:=1-z_R
=2\sqrt{p(y_R)(1-p(y_R))}.
\tag{5}
\]

Whenever the independent information floor used in `MC-363` applies,

\[
\frac{\mathfrak H_1}{R}\ge q_R z_R.
\tag{6}
\]

Combining `(4)` and `(6)` gives the exact product-affinity constraint

\[
\boxed{
\frac1R\sum_{i=1}^R e^{-\Lambda_i}
\le \beta_R.
}
\tag{7}
\]

and therefore, by convexity of `e^{-t}`,

\[
\boxed{
\frac1R\sum_{i=1}^R\Lambda_i
\ge
-\log\beta_R.
}
\tag{8}
\]

Equation `(8)` is strictly stronger near the deterministic endpoint than the linear component-incidence tariff retained in `MC-363`. The latter only forces a normalized sum of Hellinger costs to approach a positive constant. The product architecture actually forces its additive negative-log-affinity depth to diverge as the output error tends to zero.

At matched-filter energy, `MC-363` gives for fixed `0<\varepsilon<1` and even `R\to\infty`

\[
\beta_R\longrightarrow
\sqrt{2\varepsilon-\varepsilon^2}.
\]

Hence any such source-independent product architecture with dephasing error at most `\varepsilon` obeys

\[
\boxed{
\liminf_{R\to\infty,\ R\ \mathrm{even}}
\frac1R\sum_{i=1}^R\Lambda_i
\ge
\frac12\log\frac1{2\varepsilon-\varepsilon^2}.
}
\tag{9}
\]

As `\varepsilon\downarrow0`, the required average product depth is therefore

\[
\boxed{
\frac1R\sum_i\Lambda_i
\gtrsim
\frac12\log\frac1\varepsilon
-\frac12\log2.
}
\tag{10}
\]

The conclusion is not merely an average-cost statement. For every `L\ge0`, `(7)` implies

\[
\boxed{
\frac1R\#\{i:\Lambda_i\le L\}
\le
\beta_R e^L.
}
\tag{11}
\]

Thus near exact dephasing, a large fraction of source directions must themselves accumulate large log-affinity depth; the required budget cannot be concentrated on a small exceptional set of heavily source-dependent coordinates.

In the exact endpoint limit `\beta_R=0`, `(7)` forces `\Lambda_i=+\infty` for **every** source direction. A finite product transcript can therefore dephase exactly at the matched-filter endpoint only if, in each source direction, at least one conditional component pair is mutually singular (`\alpha_{j,i}=1`), or if an infinite component family accumulates divergent Bhattacharyya depth.

If all individual component edge costs satisfy the uniform non-singularity cap

\[
\alpha_{j,i}\le a<1,
\tag{12}
\]

then

\[
-\log(1-\alpha_{j,i})
\le
\frac{\alpha_{j,i}}{1-a},
\]

so `(8)` also yields the strengthened linear-cost consequence

\[
\boxed{
\frac1R\sum_i\sum_j\alpha_{j,i}
\ge
(1-a)(-\log\beta_R).
}
\tag{13}
\]

Likewise, if each active source-component incidence has cost at most `a<1` and `d_i` is the number of components depending on source direction `i`, then

\[
\boxed{
\frac1R\sum_i d_i
\ge
\frac{-\log\beta_R}{-\log(1-a)}.
}
\tag{14}
\]

So a transcript built from uniformly weak conditionally independent pieces needs logarithmically increasing average source depth as the target dephasing error tends to zero. One nearly singular component may pay that tariff in one step; otherwise many weak pieces are required.

No estimate for `M(x)` follows. This is a finite reciprocal-endpoint admission theorem. It sharpens the source-independent latent/product branch of `MC-360`--`MC-363` and leaves the same arithmetic frontier: identify an actual Möbius-derived transcript architecture and prove that its source-direction Bhattacharyya depth cannot meet `(7)`--`(10)`, or exhibit the specific source-dependent components that pay the required depth.

## 1. Product affinity gives the nonlinear edge bound exactly

Fix a surviving source edge `e={x,x'}` in direction `i`. Because the latent law is the same under `x` and `x'`, the lifted joint laws on `(\Theta,Y_1,\ldots,Y_k)` have Hellinger affinity

\[
\operatorname{Aff}(Q_x,Q_{x'})
=
\int
\prod_{j=1}^k
\left(1-h_{e,j}^2(\theta)\right)
\,d\nu(\theta),
\tag{15}
\]

where

\[
h_{e,j}^2(\theta)
:=
H^2\!\left(
K_{x,j}(\cdot\mid\theta),
K_{x',j}(\cdot\mid\theta)
\right).
\]

If `i\notin A_j`, the component law does not change across this edge and `h_{e,j}^2=0`. For `i\in A_j`, hypothesis `(1)` gives

\[
1-h_{e,j}^2(\theta)\ge1-\alpha_{j,i}.
\]

Therefore

\[
\operatorname{Aff}(Q_x,Q_{x'})
\ge
\prod_j(1-\alpha_{j,i})
=e^{-\Lambda_i}.
\tag{16}
\]

Marginalizing away the latent variable is a Markov map and can only increase Hellinger affinity, equivalently decrease squared Hellinger distance. Thus

\[
\operatorname{Aff}(P_x,P_{x'})
\ge e^{-\Lambda_i},
\]

which is exactly `(3)`.

This is the step lost when `MC-360` replaced

\[
1-\prod_j(1-h_{e,j}^2)
\]

by `\sum_jh_{e,j}^2`. The union bound is appropriate for a linear first-pass tariff but destroys the logarithmic depth needed when the required output distance approaches one.

## 2. Punctured-cube aggregation preserves the product deficit

For every coordinate direction of the punctured even-rank source cube there are exactly

\[
\frac{m-1}{2}
\]

surviving edges. Summing `(3)` direction by direction gives

\[
\begin{aligned}
\mathfrak H_1
&=\frac2m\sum_{i=1}^R\sum_{e\parallel i}h_e^2\\
&\le
\frac2m\sum_i\frac{m-1}{2}
\left(1-e^{-\Lambda_i}\right)\\
&=
q_R\sum_i\left(1-e^{-\Lambda_i}\right),
\end{aligned}
\tag{17}
\]

which proves `(4)`.

`MC-363` supplies `(6)` from the independent transcript-information floor. Cancelling the common positive factor `q_R` between `(4)` and `(6)` gives `(7)` without an additional finite-rank loss.

Convexity of `t\mapsto e^{-t}` gives

\[
e^{-\frac1R\sum_i\Lambda_i}
\le
\frac1R\sum_i e^{-\Lambda_i},
\]

so `(7)` proves `(8)` whenever `\beta_R>0`; if `\beta_R=0`, the conclusion is interpreted as infinite average depth and follows directly from nonnegativity of every `e^{-\Lambda_i}`.

For `(11)`, if `\Lambda_i\le L`, then `e^{-\Lambda_i}\ge e^{-L}`. Hence

\[
\frac{\#\{i:\Lambda_i\le L\}}R e^{-L}
\le
\frac1R\sum_i e^{-\Lambda_i}
\le\beta_R.
\]

The weak-component consequences `(13)`--`(14)` follow from the elementary inequalities

\[
-\log(1-u)\le\frac{u}{1-a}
\qquad(0\le u\le a<1)
\]

and

\[
\Lambda_i\le d_i[-\log(1-a)].
\]

## 3. Near-endpoint scaling

At matched-filter energy and RMS dephasing error at most `\varepsilon`, `MC-363` derives

\[
\liminf\frac{\mathfrak H_1}{R}
\ge
1-\sqrt{2\varepsilon-\varepsilon^2}.
\]

In the finite-rank notation used there this means

\[
\beta_R
=2\sqrt{p(y_R)(1-p(y_R))}
\longrightarrow
\sqrt{2\varepsilon-\varepsilon^2}.
\]

Substitution into `(8)` gives `(9)`. For small positive `\varepsilon`,

\[
\frac12\log\frac1{2\varepsilon-\varepsilon^2}
=
\frac12\log\frac1\varepsilon
-\frac12\log2
+O(\varepsilon),
\]

which proves `(10)`.

The scaling has a simple interpretation. Hellinger affinity, not Hellinger distance, multiplies through independent components. To drive the output affinity from order one down to `O(\sqrt\varepsilon)`, the sum of component negative log-affinities must therefore grow like `\log(1/\sqrt\varepsilon)`. The logarithm is not a new probabilistic phenomenon; it is the additive coordinate naturally associated with a multiplicative overlap.

## 4. What this changes after MC-363

Equation `(14)` of `MC-363` says that near-exact dephasing forces a normalized linear sum of component Hellinger costs to approach at least one. That statement is sharp enough when one component may become nearly singular, but it is not sharp for architectures advertised as a composition of many **uniformly weak** source observations.

The present theorem separates those regimes.

- If a component is allowed to approach mutual singularity across a source flip, its `\lambda_{j,i}` can pay an arbitrarily large portion of the tariff in one step. The correct question is then whether that nearly singular component is arithmetically natural.
- If every component remains bounded away from singularity, `(13)`--`(14)` force cumulative source dependence or component depth to grow logarithmically as `\varepsilon\downarrow0`.
- The quantile bound `(11)` prevents a small number of exceptional source coordinates from carrying all of that depth.

This is a stricter admission test for the next architecture-specific step. A proposed Möbius-derived product transcript should now expose not only which components see each source coordinate and their Hellinger edge costs, but also the resulting product affinity or Bhattacharyya depth. A componentwise upper bound that makes the average `\Lambda_i` bounded would immediately rule out arbitrarily accurate matched-energy endpoint dephasing.

## 5. Prior art and novelty boundary

The underlying probability mechanisms are classical and no novelty is claimed for them.

A. Bhattacharyya introduced the affinity-based divergence in *On a measure of divergence between two statistical populations defined by their probability distributions*, Bulletin of the Calcutta Mathematical Society **35** (1943), 99--109. The Bhattacharyya coefficient is the Hellinger affinity, and `-\log` of that coefficient is the Bhattacharyya distance used in `(2)`.

S. Kakutani, *On Equivalence of Infinite Product Measures*, Annals of Mathematics **49** (1948), 214--224, DOI `10.2307/1969123`, made product Hellinger integrals central to the equivalence/singularity theory of infinite product measures. For finite products, the affinity tensorization used in `(15)` is the elementary factorization preceding that theory; taking `-\log` makes the product affinity additive.

A targeted literature audit on 18 September 2026 also confirms that modern treatments routinely describe Hellinger-type divergences as tensorizing over product marginals. The result here is therefore **not** presented as a new information-theoretic theorem. The durable Mathia delta is the specialization of the classical additive log-affinity coordinate to the sharp reciprocal-endpoint lower bound from `MC-363`, which produces the logarithmically diverging source-direction tariff `(9)`--`(10)` and the distributional bound `(11)`.

## Boundaries and falsification tests

- **Source-independent latent law is load-bearing.** If `\nu_x` changes with the source, its Hellinger/Bhattacharyya contribution must be charged separately. The theorem does not hide source information in an unpriced latent channel.
- **Conditional product structure is load-bearing.** Arbitrarily dependent transcript components need not have multiplicative affinity. This result does not apply to them without an additional factorization or domination theorem.
- **The component bounds are uniform over the relevant source edges and latent states.** Average-only component bounds require a separate argument; one cannot move the product through an average for free.
- **`\alpha_{j,i}=1` is intentionally singular.** Then `\lambda_{j,i}=+\infty`, correctly recording that one mutually singular component can supply exact discrimination in that direction.
- **The logarithmic weak-component corollaries require a fixed cap `a<1`.** Without it, one nearly singular component can pay the product-affinity tariff without large linear Hellinger mass or large incidence count.
- **The endpoint lower input is inherited from `MC-363`.** Any future correction to its information floor or Jensen--Shannon/Hellinger envelope propagates here through `\beta_R`; the product derivation itself remains independent.
- **Finite reciprocal calibration only.** The source cube, puncture, and matched-filter-energy endpoint are the same finite calibration object as in `MC-360`--`MC-363`.
- **No zero information is imported.** The derivation uses only the established endpoint channel lower bound plus classical product-affinity identities.
- **No RH-scale conclusion is claimed.** Neither `(8)` nor `(9)` is an estimate for `M(x)`.

## Consequence for the research line

The source-independent product branch now has a natural near-endpoint complexity coordinate: **Bhattacharyya depth per source direction**. Linear Hellinger incidence is sufficient to show an extensive positive tariff, but product affinity shows that uniformly weak components must accumulate logarithmically increasing depth as dephasing approaches exactness.

The next useful step is architecture-specific rather than another generic divergence conversion: for a concrete Möbius-derived transcript, bound the conditional product affinities generated by one source flip. If the resulting average `\Lambda_i` stays bounded, `(9)` rules out arbitrarily accurate matched-energy dephasing. If it diverges, the components responsible for that divergence identify exactly where the arithmetic source dependence is paying the endpoint information cost.