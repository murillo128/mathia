# MC-355 — Gaussian location-scale readout prices covariance side channels

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-351`–`MC-354` leave a specific escape route after the additive log-smooth tariff: a readout may let its **noise law itself depend on the source state**, so neighboring source states can be distinguished through covariance modulation even when their mean locations barely move. A source-dependent Gaussian location-scale channel makes that side channel exactly measurable.

Let `X` be the reciprocal source state. For every admissible source state `x`, suppose an intermediate readout has the conditional law

\[
Z\mid X=x\sim\mathcal N(\mu_x,\Sigma_x),
\qquad
\Sigma_x\succ0,
\tag{1}
\]

and assume the complete admitted coefficient observation `Y` is downstream through a source-independent Markov kernel,

\[
X\longrightarrow Z\longrightarrow Y.
\tag{2}
\]

For a natural source edge `e={x,x'}`, put

\[
\Delta_e:=\mu_{x'}-\mu_x,
\qquad
A_e:=\Sigma_x^{-1/2}\Sigma_{x'}\Sigma_x^{-1/2}.
\tag{3}
\]

Let `P_e,Q_e` be the two complete transcript laws of `Y` and retain the half-Jeffreys edge divergence

\[
b_e(Y)
:=\frac12\left(D(P_e\|Q_e)+D(Q_e\|P_e)\right).
\tag{4}
\]

Then data processing and the exact Gaussian KL formula give

\[
\boxed{
 b_e(Y)
\le
\mathcal M_e+\mathcal C_e,
}
\tag{5}
\]

where

\[
\mathcal M_e
:=
\frac14\Delta_e^{\!T}
\left(\Sigma_x^{-1}+\Sigma_{x'}^{-1}\right)
\Delta_e
\tag{6}
\]

is the symmetric whitened mean-displacement cost and

\[
\mathcal C_e
:=
\frac14\operatorname{tr}
\left(A_e+A_e^{-1}-2I\right)
\tag{7}
\]

is the covariance-modulation cost.

If `lambda_{e,j}=e^{t_{e,j}}` are the generalized covariance eigenvalues, then

\[
\boxed{
\mathcal C_e
=
\frac12\sum_j\bigl(\cosh t_{e,j}-1\bigr).
}
\tag{8}
\]

Thus covariance is not a free side channel: every relative variance/correlation deformation contributes directly to the same Jeffreys currency that `MC-351`–`MC-353` force to be extensive.

Choose a natural source edge uniformly, with the parity-appropriate edge law already normalized in `MC-353`. Under bounded coefficient energy and fixed nontrivial dephasing,

\[
\mathcal E(W)\le C,
\qquad
\delta(W)\le1-\eta,
\qquad C<\infty,\ \eta>0,
\tag{9}
\]

`MC-353` gives

\[
\mathbf E_e b_e(Y)
\ge
\frac{\eta^2}{C}-o(1).
\tag{10}
\]

Combining `(5)` and `(10)` yields the exact Gaussian location-scale resource tariff

\[
\boxed{
\mathbf E_e\bigl(\mathcal M_e+\mathcal C_e\bigr)
\ge
\frac{\eta^2}{C}-o(1).
}
\tag{11}
\]

This formulation is already coordinate-free at the statistical level: it is simply the half-Jeffreys divergence between neighboring Gaussian rows, split into mean and covariance contributions.

A more geometric corollary makes the price explicit. Assume

\[
\Sigma_x\succeq \sigma_R^2 I
\quad\text{for every source state }x,
\tag{12}
\]

and define the affine-invariant covariance edge distance

\[
d_{\mathrm{AI}}(\Sigma_x,\Sigma_{x'})^2
:=
\left\|
\log\left(\Sigma_x^{-1/2}\Sigma_{x'}\Sigma_x^{-1/2}\right)
\right\|_F^2
=
\sum_j t_{e,j}^2.
\tag{13}
\]

Let

\[
r_R
:=
\sup_e\max_j|t_{e,j}|,
\tag{14}
\]

and set

\[
\kappa(r)
:=
\begin{cases}
\dfrac{\cosh r-1}{2r^2}, & r>0,\\[6pt]
\dfrac14, & r=0.
\end{cases}
\tag{15}
\]

Then every natural edge satisfies

\[
\boxed{
 b_e(Y)
\le
\frac{\|\Delta_e\|_2^2}{2\sigma_R^2}
+
\kappa(r_R)\,
d_{\mathrm{AI}}(\Sigma_x,\Sigma_{x'})^2.
}
\tag{16}
\]

Writing

\[
G_{\mu,R}^2
:=\mathbf E_e\|\Delta_e\|_2^2,
\qquad
G_{\Sigma,R}^2
:=\mathbf E_e d_{\mathrm{AI}}(\Sigma_x,\Sigma_{x'})^2,
\tag{17}
\]

fixed bounded-energy dephasing therefore requires

\[
\boxed{
\frac{G_{\mu,R}^2}{2\sigma_R^2}
+
\kappa(r_R)G_{\Sigma,R}^2
\ge
\frac{\eta^2}{C}-o(1).
}
\tag{18}
\]

When relative covariance changes are small, `r_R -> 0` and

\[
\kappa(r_R)=\frac14+O(r_R^2),
\tag{19}
\]

so covariance modulation is locally quadratic in the affine-invariant log-covariance motion. In particular,

\[
\frac{G_{\mu,R}}{\sigma_R}\to0,
\qquad
G_{\Sigma,R}\to0,
\qquad
\sup_R r_R<\infty
\tag{20}
\]

is incompatible with `(9)`. A channel cannot hide the required source-edge discrimination simultaneously in vanishing mean motion and vanishing covariance motion while keeping a nondegenerate Gaussian resolution scale.

There is also an exact-endpoint consequence. For every finite `R`, two nondegenerate finite-dimensional Gaussian rows have finite KL in both directions. But exact unit-energy dephasing forces infinite neighboring-edge KL by `MC-351`. Hence

\[
\boxed{
\mathcal E(W)\le1,
\quad
\delta(W)=0
\quad\Longrightarrow\quad
\text{no factorization of the form `(1)`--`(2)` with all }\Sigma_x\succ0.
}
\tag{21}
\]

Allowing source-dependent covariance therefore enlarges the common-noise model of `MC-343`/`MC-354`, but it does not restore exact dephasing at finite nondegenerate Gaussian resolution.

No estimate for `M(x)` follows. The advance is a finite reciprocal-endpoint admission theorem: a Gaussian side channel carried by source-dependent noise covariance now has an exact, affine-invariant price in the same local statistical currency required by the dephasing converse.

## 1. Exact half-Jeffreys decomposition for Gaussian rows

For two `d`-dimensional Gaussian laws

\[
P=\mathcal N(\mu,\Sigma),
\qquad
Q=\mathcal N(\nu,\Theta),
\qquad
\Sigma,\Theta\succ0,
\]

the classical KL formula is

\[
D(P\|Q)
=
\frac12\left[
\operatorname{tr}(\Theta^{-1}\Sigma)
+(\nu-\mu)^T\Theta^{-1}(\nu-\mu)
-d
+\log\frac{\det\Theta}{\det\Sigma}
\right].
\tag{22}
\]

Adding the reversed divergence cancels the log-determinant terms. Dividing by two to match the Mathia convention `(4)` gives

\[
\begin{aligned}
b(P,Q)
=
\frac14\Bigl[&
(\nu-\mu)^T(\Sigma^{-1}+\Theta^{-1})(\nu-\mu)\\
&+\operatorname{tr}(\Sigma^{-1}\Theta+\Theta^{-1}\Sigma-2I)
\Bigr].
\end{aligned}
\tag{23}
\]

Taking `Sigma=Sigma_x`, `Theta=Sigma_x'` proves the equality `b(Z_x,Z_x')=M_e+C_e`. Since `Y` is downstream of `Z` by the common kernel in `(2)`, KL data processing in both directions proves `(5)`.

The determinant cancellation is useful here: changing only the local volume element cannot be analyzed by a single log-determinant term after symmetrization. What remains is the full relative covariance deformation `A+A^{-1}-2I`, which is nonnegative and vanishes exactly when the covariances agree.

## 2. Relative covariance eigenvalues expose the side-channel cost

The matrices

\[
\Sigma_x^{-1}\Sigma_{x'}
\quad\text{and}\quad
A_e=\Sigma_x^{-1/2}\Sigma_{x'}\Sigma_x^{-1/2}
\]

have the same positive eigenvalues `lambda_{e,j}`. Likewise the reverse relative covariance contributes their reciprocals. Therefore

\[
\operatorname{tr}(A_e+A_e^{-1}-2I)
=
\sum_j\left(\lambda_{e,j}+\lambda_{e,j}^{-1}-2\right).
\tag{24}
\]

Writing `lambda_{e,j}=e^{t_{e,j}}` gives

\[
\lambda+\lambda^{-1}-2
=2(\cosh t-1),
\]

which proves `(8)`.

This identifies two distinct ways for neighboring source states to remain statistically distinguishable:

- move the Gaussian centers relative to their local covariance scale, paying `M_e`;
- change the covariance shape/scale itself, paying `C_e`.

A construction that makes the centers almost identical but encodes source bits in variances or correlations has not evaded the reverse-discrimination budget; it has moved that budget into `C_e`.

In one dimension, if the means coincide and neighboring variances satisfy

\[
\sigma_{x'}^2=e^t\sigma_x^2,
\]

then

\[
b_e=\frac12(\cosh t-1)=\frac{t^2}{4}+O(t^4).
\tag{25}
\]

Thus even a pure variance side channel must sustain a nonvanishing root-mean-square **log-variance** motion across natural source edges if it is to carry the constant per-edge tariff forced by `(10)`.

## 3. Affine-invariant log-covariance motion upper-prices the exact covariance tariff

Equation `(12)` implies

\[
\Sigma_x^{-1}\preceq\sigma_R^{-2}I,
\qquad
\Sigma_{x'}^{-1}\preceq\sigma_R^{-2}I,
\]

so `(6)` gives

\[
\mathcal M_e
\le
\frac{\|\Delta_e\|_2^2}{2\sigma_R^2}.
\tag{26}
\]

For the covariance part, define

\[
g(t):=\frac{\cosh t-1}{t^2},
\qquad g(0):=\frac12.
\]

The function `g` is increasing for `t>=0`: after differentiation the numerator has derivative `t cosh t-sinh t`, whose derivative is `t sinh t>=0`. Hence, for `|t|<=r_R`,

\[
\cosh t-1
\le
\frac{\cosh r_R-1}{r_R^2}t^2.
\tag{27}
\]

Combining `(8)`, `(13)` and `(27)` gives

\[
\mathcal C_e
\le
\kappa(r_R)d_{\mathrm{AI}}(\Sigma_x,\Sigma_{x'})^2.
\tag{28}
\]

Equations `(26)` and `(28)` prove `(16)`. Averaging over the natural edge law and composing with `(10)` proves `(18)`.

The affine-invariant distance in `(13)` is not introduced to claim new covariance geometry. It is the standard SPD-cone log metric, used only because the exact Gaussian Jeffreys covariance term is already a spectral function of the same generalized eigenvalues. Near equal covariances, `(19)` shows that Jeffreys cost and squared affine-invariant covariance distance agree to second order up to the factor `1/4` in the Mathia half-Jeffreys normalization.

## 4. Exact dephasing forces departure from finite nondegenerate Gaussian rows

Every Gaussian density with positive-definite covariance is positive on all of `R^d`. Hence any two rows in `(1)` are mutually absolutely continuous and their KL divergences are finite whenever their means and covariance matrices are finite.

Data processing through `(2)` cannot increase either directed KL, so every complete transcript edge has finite `b_e(Y)`. By contrast, `MC-351` proves that exact unit-energy dephasing makes neighboring source rows statistically singular and forces the aggregate edge KL budget to `+infinity`.

This proves `(21)`. An exact endpoint architecture that resembles a Gaussian location-scale readout must therefore leave the theorem's finite nondegenerate class somewhere: a covariance must become singular, a limiting mean/covariance resource must diverge, the complete transcript must contain a side channel outside `Z`, or the readout must cease to be Gaussian.

This is the covariance analogue of the zero-noise boundary in `MC-343`, but it is strictly broader because the covariance may vary arbitrarily with the source state.

## 5. Prior art and novelty boundary

The statistical ingredients are classical and no novelty is claimed for them.

The multivariate Gaussian KL formula `(22)` is standard; an accessible derivation is the Statistical Proof Book entry *Kullback-Leibler divergence for the multivariate normal distribution*, which records exactly the mean, trace and log-determinant terms used above: `https://statproofbook.github.io/P/mvn-kl`. Christian Röver's `bayesmeta` documentation gives the same formula and explicitly defines its symmetrized version, citing Kullback's 1959 *Information Theory and Statistics*: `https://www.rdocumentation.org/packages/bayesmeta/versions/3.3/topics/kldiv`.

Yufeng Zhang, Wanwei Liu, Zhenbang Chen, Ji Wang and Kenli Li, *On the Properties of Kullback-Leibler Divergence Between Multivariate Gaussian Distributions*, arXiv `2102.05485`, studies structural bounds for KL between multivariate Gaussian laws; it confirms that Gaussian KL geometry itself is established prior art: `https://arxiv.org/abs/2102.05485`.

The affine-invariant Riemannian geometry of positive-definite covariance matrices is also standard. Xavier Pennec, Pierre Fillard and Nicholas Ayache, *A Riemannian Framework for Tensor Computing*, International Journal of Computer Vision **66** (2006), 41–66, DOI `10.1007/s11263-005-3222-z`, develops the affine-invariant SPD metric and its geometric properties. No novelty is claimed for `(13)` or for using generalized covariance eigenvalues as intrinsic coordinates.

A targeted prior-art audit on 17 September 2026 found no basis for claiming novelty for Gaussian KL/Jeffreys formulas, covariance-discrimination costs, generalized-eigenvalue parametrization, or affine-invariant covariance geometry. The durable Mathia-specific delta is the composition with the independently derived reciprocal-source tariff `MC-351`/`MC-353`: source-dependent Gaussian covariance is now explicitly charged as a local side-channel resource rather than left outside the additive common-noise model of `MC-354`.

## Boundaries and falsification tests

- **The complete transcript must be downstream of one common kernel from `Z`.** If the architecture reveals source-dependent metadata, random seeds, covariance labels, adaptive branch decisions, or any other observation not mediated by `Z`, equation `(5)` need not upper-bound the complete transcript.
- **Positive-definite covariance is load-bearing.** Singular Gaussian rows may live on different subspaces and can have infinite KL. Such singularity is an escape route only by paying an explicit degenerating-covariance resource.
- **The exact tariff `(11)` does not require the spectral floor `(12)`.** The floor is used only for the simpler Euclidean-mean upper bound `(16)`. Highly anisotropic channels should be judged first by the exact whitened cost `(6)`.
- **A bounded `r_R` is required only for the quadratic log-covariance simplification.** Large relative covariance eigenvalues are not a loophole; they make `C_e` large directly through `(8)`.
- **Covariance modulation is necessary, not sufficient, when mean motion vanishes.** Spending Jeffreys divergence in variance/correlation changes does not itself produce Möbius cancellation or a useful coefficient architecture.
- **Finite-dimensionality matters for the literal Gaussian formula.** Infinite-dimensional Gaussian measures require equivalence/singularity criteria such as Cameron-Martin/Feldman-Hájek and are not covered by this finding.
- **No arithmetic regularity has been proved.** Nothing here shows that a natural Möbius endpoint construction has small `G_mu`, small `G_Sigma`, a covariance floor, or a Gaussian factorization.

## Research consequence

The current reverse-discrimination frontier is narrower again. An architecture that evades the common additive-noise tariff of `MC-354` by making its readout noise source-dependent cannot cite heteroskedasticity as a free source of distinguishability. In the Gaussian class, the complete local cost splits exactly into whitened mean motion plus relative covariance motion, and bounded-energy dephasing forces their natural-edge average to stay bounded away from zero.

The next live analytic test is therefore representation-specific: for any proposed Möbius/endpoint channel that is approximately Gaussian after normalization, determine whether its source-edge covariance modulation is genuinely `O(1)` in the Jeffreys currency or whether an independent arithmetic estimate forces both the whitened mean and affine-invariant covariance motions to vanish. Only the latter would turn the present admission theorem into a new cancellation obstruction.