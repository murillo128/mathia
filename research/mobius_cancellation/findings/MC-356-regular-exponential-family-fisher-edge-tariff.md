# MC-356 — Regular exponential-family readouts pay an exact Fisher edge tariff

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-354` prices additive log-smooth readouts and `MC-355` prices source-dependent Gaussian mean/covariance side channels. A large remaining smooth non-Gaussian class can be priced without choosing a noise metric at all: for a regular exponential family, the neighboring-row half-Jeffreys divergence is exactly the integrated Fisher information along the natural-parameter edge.

Let the source state be `X`. Suppose an intermediate readout `Z` has, conditional on `X=x`, density or mass function

\[
p_{\theta_x}(z)
=
h(z)\exp\!\bigl(\langle\theta_x,T(z)\rangle-A(\theta_x)\bigr),
\qquad \theta_x\in\Theta,
\tag{1}
\]

where `Theta` is the open natural-parameter domain of a regular exponential family, `A` is its log-partition function, and the carrier `h` and support are independent of `x`. Assume the complete admitted transcript `Y` is downstream through one source-independent Markov kernel,

\[
X\longrightarrow Z\longrightarrow Y.
\tag{2}
\]

For a natural source edge `e={x,x'}`, write

\[
\Delta_e:=\theta_{x'}-\theta_x,
\qquad
\theta_e(t):=\theta_x+t\Delta_e,
\qquad 0\le t\le1.
\tag{3}
\]

The convexity of the natural-parameter domain keeps the whole segment in `Theta`. Let

\[
\mathcal I(\theta)
:=\nabla^2 A(\theta)
=\operatorname{Cov}_{\theta}(T(Z))
\tag{4}
\]

be the Fisher information matrix in natural coordinates. Define the Fisher edge action

\[
\mathcal F_e
:=
\int_0^1
\Delta_e^{T}\mathcal I(\theta_e(t))\Delta_e\,dt.
\tag{5}
\]

If `P_e,Q_e` are the two complete transcript laws of `Y`, with the Mathia half-Jeffreys normalization

\[
b_e(Y)
:=\frac12\left(D(P_e\|Q_e)+D(Q_e\|P_e)\right),
\tag{6}
\]

then

\[
\boxed{
 b_e(Y)\le \frac12\mathcal F_e.
}
\tag{7}
\]

Before downstream post-processing there is equality:

\[
\boxed{
 \frac12\left(
 D(p_{\theta_x}\|p_{\theta_{x'}})
 +D(p_{\theta_{x'}}\|p_{\theta_x})
 \right)
 =\frac12\mathcal F_e.
}
\tag{8}
\]

Equivalently, with `mu(theta)=nabla A(theta)`,

\[
\mathcal F_e
=
\langle
\theta_{x'}-\theta_x,
\mu(\theta_{x'})-\mu(\theta_x)
\rangle.
\tag{9}
\]

Thus changing Bernoulli probabilities, Poisson rates, categorical weights, Gaussian natural parameters, or any other regular exponential-family sufficient-statistic law does not create a free smooth side channel. The exact reverse-discrimination cost is the symmetrized Bregman divergence of `A`, equivalently the integrated Fisher action `(5)`.

Under bounded coefficient energy and fixed nontrivial dephasing,

\[
\mathcal E(W)\le C,
\qquad
\delta(W)\le1-\eta,
\qquad C<\infty,\ \eta>0,
\tag{10}
\]

`MC-353` gives for the natural source-edge law

\[
\mathbf E_e b_e(Y)
\ge
\frac{\eta^2}{C}-o(1).
\tag{11}
\]

Combining `(7)` and `(11)` yields the exact exponential-family resource tariff

\[
\boxed{
\mathbf E_e\mathcal F_e
\ge
\frac{2\eta^2}{C}-o(1).
}
\tag{12}
\]

Hence a family of admitted readouts satisfying

\[
\mathbf E_e\mathcal F_e\longrightarrow0
\tag{13}
\]

cannot sustain fixed nontrivial dephasing at bounded coefficient energy.

A convenient sufficient version follows if the Fisher matrix is uniformly bounded along every natural source edge. If

\[
\mathcal I(\theta_e(t))\preceq L_R I
\qquad
\text{for all admitted }e,t,
\tag{14}
\]

and

\[
G_{\theta,R}^2
:=\mathbf E_e\|\Delta_e\|_2^2,
\tag{15}
\]

then

\[
\boxed{
\frac{L_R}{2}G_{\theta,R}^2
\ge
\frac{\eta^2}{C}-o(1).
}
\tag{16}
\]

The invariant statement is `(12)`; `(16)` is only its natural-coordinate quadratic upper bound.

There is also an exact-endpoint obstruction. For finite-dimensional regular exponential-family rows with both natural parameters in the interior `Theta`, the two rows have common support and finite directed KL. Therefore every downstream edge has finite `b_e(Y)`. But `MC-351` proves that exact unit-energy dephasing makes every surviving natural source edge pairwise singular and gives infinite KL in both directions. Consequently

\[
\boxed{
\mathcal E(W)\le1,
\quad
\delta(W)=0
\quad\Longrightarrow\quad
\text{no factorization `(1)`--`(2)` with all }\theta_x\in\Theta.
}
\tag{17}
\]

An exact endpoint architecture in this class must leave the regular interior somewhere: parameters approach a singular boundary, the common-support hypothesis fails, the complete transcript contains an unpriced side channel, or the readout leaves the exponential-family model.

No estimate for `M(x)` follows. The advance is a finite reciprocal-endpoint admission theorem that closes a broad smooth non-Gaussian escape route left after `MC-354`--`MC-355`.

## 1. Exponential-family KL is a Bregman divergence of the log partition

For two natural parameters `theta,eta in Theta`, direct substitution into `(1)` gives

\[
D(p_\theta\|p_\eta)
=
A(\eta)-A(\theta)
-\langle\eta-\theta,\nabla A(\theta)\rangle.
\tag{18}
\]

This is the Bregman divergence of `A` with the corresponding orientation. Reversing the parameters and adding cancels the log-partition increments:

\[
D(p_\theta\|p_\eta)
+D(p_\eta\|p_\theta)
=
\langle
\eta-\theta,
\nabla A(\eta)-\nabla A(\theta)
\rangle.
\tag{19}
\]

Let `Delta=eta-theta`. By the fundamental theorem of calculus,

\[
\nabla A(\eta)-\nabla A(\theta)
=
\int_0^1
\nabla^2A(\theta+t\Delta)\Delta\,dt.
\tag{20}
\]

Substituting `(20)` into `(19)` proves `(8)`--`(9)`. For a regular exponential family, differentiation of the log partition gives

\[
\nabla A(\theta)=\mathbf E_\theta T(Z),
\qquad
\nabla^2A(\theta)=\operatorname{Cov}_\theta(T(Z)),
\tag{21}
\]

which is exactly the Fisher information matrix in natural coordinates. KL data processing through `(2)` in both directions proves `(7)`.

## 2. The source-edge lower budget turns Fisher action into a compulsory resource

Averaging `(7)` over the same parity-appropriate natural edge law used by `MC-351`--`MC-353` gives

\[
\mathbf E_e b_e(Y)
\le
\frac12\mathbf E_e\mathcal F_e.
\tag{22}
\]

Equation `(11)` therefore proves `(12)`. Under `(14)`,

\[
\mathcal F_e
\le
L_R\|\Delta_e\|_2^2,
\tag{23}
\]

and averaging proves `(16)`.

The distinction from a generic forward-Lipschitz bound is important. `MC-342` showed that arbitrarily small forward coordinate motion can still encode the whole source if the readout has effectively infinite reverse precision. Here the reverse conditioning is already inside `mathcal F_e`: a small parameter displacement is cheap only when the Fisher curvature encountered along that edge is also controlled. Approaching a highly informative or singular statistical boundary is automatically recorded by growing Fisher action or by leaving the regular-interior hypotheses.

## 3. Calibration examples

### Bernoulli

For a Bernoulli row with success probability `p`, use natural parameter

\[
\theta=\log\frac{p}{1-p},
\qquad
A(\theta)=\log(1+e^\theta),
\qquad
\mathcal I(\theta)=p(1-p).
\]

For `p,q in (0,1)`, `(8)` becomes

\[
 b
=
\frac12
\left(\log\frac{p/(1-p)}{q/(1-q)}\right)(p-q).
\tag{24}
\]

This is finite in the interior. Exact source discrimination can appear only by driving rows to a support-degenerate boundary such as `p=0` or `1`, precisely outside the regular-interior condition.

### Poisson

For positive rate `lambda`, `theta=log lambda`, `A(theta)=e^theta`, and `I(theta)=lambda`. Hence

\[
 b
=
\frac12(\lambda-\lambda')\log\frac{\lambda}{\lambda'}.
\tag{25}
\]

Again finite positive rates cannot supply the infinite edge divergence required by exact dephasing.

### Gaussian

The finite-dimensional multivariate Gaussian location-scale family is itself an exponential family in the natural parameters built from `Sigma^{-1}mu` and `-Sigma^{-1}/2`. Therefore `MC-355` is a specialization of the exact identity `(8)`. Its separate value is that it rewrites the generic Fisher/Bregman action explicitly as whitened mean motion plus the relative-covariance term `tr(A+A^{-1}-2I)/4`, exposing the Gaussian side-channel geometry in physical mean/covariance coordinates.

## 4. Prior art and novelty boundary

No novelty is claimed for exponential-family information geometry, KL/Bregman duality, Fisher information, or the symmetrized-Bregman identity.

Arindam Banerjee, Srujana Merugu, Inderjit S. Dhillon and Joydeep Ghosh, *Clustering with Bregman Divergences*, JMLR **6** (2005), 1705--1749, proves the regular exponential-family/Bregman correspondence and records explicitly that KL between members of a regular exponential family is the corresponding Bregman divergence in natural or expectation coordinates: https://jmlr.org/papers/v6/banerjee05b.html.

The same paper derives the expectation parameter as the gradient of the log-partition function and treats the natural/expectation spaces as Legendre-dual coordinates. The Fisher-Hessian identity is standard information geometry; modern exponential-family treatments likewise use `nabla^2 A` as the Fisher information metric.

A targeted audit on 17 September 2026 therefore found no basis for novelty claims about `(18)`--`(21)`. The durable Mathia-specific delta is the composition with the independently derived reciprocal-source lower tariff of `MC-351`/`MC-353`: an entire regular exponential-family readout class now has an exact local statistical resource that must remain extensive enough on natural source edges.

## Boundaries and falsification tests

- **Common support is load-bearing.** The carrier and support in `(1)` must not depend on the source state. Parameter-dependent support can create singular rows and is outside this theorem.
- **Interior regularity is load-bearing for the exact-endpoint obstruction.** Approaching the boundary of `Theta` may make Fisher information or directed KL diverge. That is an explicit resource/degeneration, not a contradiction of `(17)`.
- **The complete transcript must factor through `Z`.** Source metadata, adaptive branch labels, random seeds, or another observation outside the Markov chain `(2)` are unpriced side channels.
- **The Fisher action, not Euclidean natural-parameter distance, is the canonical tariff.** Reparameterization can change the coordinate norm and the constant `L_R`; the Jeffreys divergence in `(8)` is statistical and invariant, while the straight path in `(5)` is the exponential-affine natural-coordinate representation of it.
- **Mixtures are not generally one exponential-family row.** A source-dependent mixture of family members can fall outside `(1)` even when each component is regular. Such mixture channels require a separate divergence bound.
- **Infinite-dimensional families are not covered.** The exact finite-dimensional regular-family argument does not automatically extend to nonparametric exponential families or Gaussian measures on infinite-dimensional spaces.
- **No arithmetic factorization has been proved.** Nothing here shows that a natural Möbius endpoint construction has small Fisher action or even admits an exponential-family readout representation.

## Research consequence

The smooth-readout frontier is narrower again. After additive log-smooth noise (`MC-354`) and explicit Gaussian location-scale modulation (`MC-355`), a broad class of smooth source-dependent non-Gaussian rows cannot use changing higher moments or sufficient-statistic laws for free: their exact edge cost is the integrated Fisher action `(5)`.

The next useful escape tests are now structurally sharper. A proposed Möbius/endpoint architecture must either (i) prove that its natural source-edge Fisher action stays large enough, (ii) exploit a singular/boundary or parameter-dependent-support mechanism, (iii) use a genuinely non-exponential mixture/nonparametric channel, or (iv) expose a side channel outside the priced readout. For any concrete architecture in case (i), an arithmetic upper bound forcing `E_e F_e -> 0` would immediately contradict bounded-energy dephasing through `(12)`.