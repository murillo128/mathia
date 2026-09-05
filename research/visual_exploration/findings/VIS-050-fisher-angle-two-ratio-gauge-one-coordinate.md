# VIS-050 — two-ratio Fisher flatness has one exact finite gauge coordinate

## Claim

Assume the nondegenerate all-direction first-order-flat configuration classified in `VIS-049`. Thus `Omega` is a fixed finite support, `H` is a strictly positive probability gauge, `A,B` are fixed nonzero residual tensors, and after baseline Fisher normalization

`u_x = A_x / (sqrt(H_x) ||A||_H)`,
`v_x = B_x / (sqrt(H_x) ||B||_H)`

one has `||u||_2=||v||_2=1` and

`kappa = sum_x u_x v_x`, with `0<|kappa|<1`.

Let

`t = [1+sqrt(1-kappa^2)]/kappa`.

`VIS-049` shows that every active cell lies in exactly one of the reciprocal ratio classes

`P={x:u_x=t v_x}`,
`M={x:u_x=v_x/t}`,

both classes occur, and their baseline `v^2` masses are

`p=sum_(x in P) v_x^2 = 1/(1+t^2)`,
`m=sum_(x in M) v_x^2 = t^2/(1+t^2)`.

For an arbitrary real cell function `h`, perturb the gauge by

`G_x(s)=H_x exp(-s h_x)/Z(s)`.

Define the two class moment sums

`A_P(s)=sum_(x in P) v_x^2 exp(s h_x)`,
`A_M(s)=sum_(x in M) v_x^2 exp(s h_x)`

and the single class-contrast coordinate

`q_h(s)=log[(A_P(s)/p)/(A_M(s)/m)]`.

Then the Fisher cosine under the perturbed gauge depends on the entire cellwise reweighting **only through `q_h(s)`**, with the exact formula

`kappa_(G(s))(A,B)
 = kappa cosh(q_h(s)/2)
   / sqrt(1+kappa^2 sinh(q_h(s)/2)^2)`.

Consequently:

1. `kappa_(G(s))=kappa` exactly if and only if `q_h(s)=0`. The nondegenerate stationary point therefore lies on a genuine codimension-one balance level set of finite gauges, even though `VIS-048` proves there is no open neighborhood of exact invariance.
2. For `q_h(s) != 0`, the magnitude `|kappa_(G(s))|` is strictly larger than `|kappa|` and tends monotonically to `1` as `|q_h(s)| -> infinity`.
3. Writing
   `mu_P=sum_(P) (v_x^2/p) h_x` and
   `mu_M=sum_(M) (v_x^2/m) h_x`,
   one has
   `q_h'(0)=mu_P-mu_M` and
   `d^2/ds^2 kappa_(G(s))|_(s=0)
    = [kappa(1-kappa^2)/4] (mu_P-mu_M)^2`.
   Hence the Hessian of the Fisher cosine with respect to projective log-gauge perturbations has rank one on this nondegenerate first-order-flat locus.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION CONTROL + FINITE-GAUGE CLASSIFICATION + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

No claim is made that empirical zeta/CUE residuals lie near this exceptional locus, that the one-coordinate reduction persists away from the exact two-ratio hypothesis, or that this elementary weighted-cosine classification is a new general theorem.

## 1. The two ratio classes collapse every finite gauge to two masses

As in `VIS-049`, normalization of the probability gauge contributes only a common positive factor to the Fisher numerator and both squared norms, so it cancels from the normalized cosine. Under the log-reweighting `exp(s h_x)`,

`N(s)=sum_x u_x v_x exp(s h_x)`,
`Q_u(s)=sum_x u_x^2 exp(s h_x)`,
`Q_v(s)=sum_x v_x^2 exp(s h_x)`.

On `P`, `u=t v`; on `M`, `u=v/t`. Therefore

`N(s)=t A_P(s)+t^(-1) A_M(s)`,
`Q_u(s)=t^2 A_P(s)+t^(-2) A_M(s)`,
`Q_v(s)=A_P(s)+A_M(s)`.

Thus no within-class cell arrangement enters separately: all finite gauge dependence is compressed into the two positive scalars `A_P,A_M`.

Now write

`a=A_P/p`, `b=A_M/m`.

Using `p=1/(1+t^2)` and `m=t^2/(1+t^2)` gives

`kappa_(G(s))
 = t(a+b)/sqrt[(t^2 a+b)(a+t^2 b)]`.

A common positive scaling of `a,b` cancels. Put `q=log(a/b)` and choose the symmetric representative `a=c exp(q/2)`, `b=c exp(-q/2)`. Then

`kappa_(G(s))
 = 2t cosh(q/2)
   / sqrt[(1+t^2)^2+4t^2 sinh(q/2)^2]`.

Since `kappa=2t/(1+t^2)`, this is exactly the claimed one-coordinate formula.

This strengthens the local statement in `VIS-049`: the explicit `P` versus `M` contrast used there was not a special witness. On the full two-ratio stationary family, **every finite positive diagonal gauge perturbation is seen by the angle only through one aggregate imbalance between the two ratio classes**.

## 2. The exact angle-preserving set is a balance hypersurface

For `0<|kappa|<1`, compare the squared perturbed and baseline cosines. With `y=sinh(q/2)^2 >= 0`,

`kappa_(G)^2
 = kappa^2 (1+y)/(1+kappa^2 y)`.

Equality with `kappa^2` requires

`(1-kappa^2)y=0`,

hence `y=0`, equivalently `q=0`. Therefore the exact finite angle-preserving condition is

`A_P/p = A_M/m`.

This is one scalar constraint on the positive projective gauge weights. It has empty interior, in agreement with `VIS-048`, but it is much larger than the single baseline gauge: nontrivial within-class reweightings can preserve the angle exactly whenever their normalized aggregate moment factors remain balanced.

The same formula shows

`d/dy [kappa_(G)^2]
 = kappa^2(1-kappa^2)/(1+kappa^2 y)^2 > 0`.

Therefore `|kappa_(G)|` increases strictly with `|q|` away from the balance surface and approaches `1` as the imbalance becomes extreme. On this exceptional stationary locus the baseline value is not an arbitrary saddle in the transverse coordinate: it is the unique minimum of the angle magnitude along the one-dimensional quotient.

## 3. The first nontrivial local geometry is rank one

Normalize `v^2` separately on the two ratio classes:

`pi_P(x)=v_x^2/p` for `x in P`,
`pi_M(x)=v_x^2/m` for `x in M`.

Then

`q_h(s)
 = log E_(pi_P)[exp(s h)]
   - log E_(pi_M)[exp(s h)]`.

Hence

`q_h(0)=0`,
`q_h'(0)=E_(pi_P)[h]-E_(pi_M)[h]=mu_P-mu_M`.

Expanding the exact outer function at `q=0` gives

`kappa cosh(q/2)/sqrt(1+kappa^2 sinh(q/2)^2)
 = kappa + [kappa(1-kappa^2)/8] q^2 + O(q^4)`.

Substituting `q_h(s)=(mu_P-mu_M)s+O(s^2)` yields

`kappa_(G(s))
 = kappa
   + [kappa(1-kappa^2)/8](mu_P-mu_M)^2 s^2
   + O(s^3)`,

and therefore

`kappa_(G)''(0)
 = [kappa(1-kappa^2)/4](mu_P-mu_M)^2`.

The second variation is the square of one linear functional of `h`. Modulo the irrelevant constant-gauge direction, the Hessian therefore has rank one. Its kernel consists of perturbations whose `v^2`-weighted mean is the same in `P` and `M`.

This also explains the `h=+1` on `P`, `h=-1` on `M` witness from `VIS-049`: there `mu_P-mu_M=2`, so the displayed Hessian gives `kappa(1-kappa^2)`, exactly matching the quadratic coefficient derived there.

Higher-order flatness inside the Hessian kernel is controlled by higher differences between the two classwise log-moment-generating functions. Classifying that cumulant hierarchy is a separate question and is not needed for the present finite-gauge reduction.

## 4. Prior art and novelty boundary

The general dependence of vector angles on the chosen inner product is classical. The closest persisted specialized anchor remains Lin and Sinnamon's generalized Wielandt inequality in `research/visual_exploration/SOURCES.md`, which gives sharp angle distortion under changes of inner product and underlies `VIS-045`.

A targeted search for weighted-cosine stationarity, positive diagonal metric perturbation, and cosine gauge freedom also finds neighboring embedding literature. Steck, Ekanadham, and Kallus, *Is Cosine-Similarity of Embeddings Really About Similarity?* (WWW 2024 Companion; arXiv:2403.05440), show that diagonal gauge freedom in learned matrix-factorization embeddings can make cosine similarities non-unique or arbitrary. Bouhsine, *In Defense of Cosine Similarity: Normalization Eliminates the Gauge Freedom* (arXiv:2602.19393), studies how unit-sphere constraints remove that particular embedding-factorization ambiguity. Those results concern reparameterization freedom of learned embeddings, not fixed residual tensors measured under a common varying Fisher metric, and they do not supply the two-ratio finite-gauge reduction above.

No novelty is claimed for the weighted-cosine algebra, moment-generating-function reduction, or rank-one Hessian observation. The durable Mathia contribution is the exact representation-control boundary for the current visual residual program: the exceptional nondegenerate first-order-flat locus is much more structured than a generic stationary point, but its apparent local robustness still collapses to one gauge-imbalance coordinate.

## 5. Boundary conditions and falsification

The finite support, residual tensors, baseline gauge, and two-ratio partition from `VIS-049` must remain fixed while the gauge varies. Rebinning cells, changing support, refitting the residual tensors, recomputing a Markov closure, or changing the statistic is outside the claim.

Both ratio classes must be nonempty and `0<|kappa|<1`. The proportional and cellwise-disjoint cases are the globally invariant degeneracies already classified in `VIS-048`.

All gauges must remain strictly positive. The formula permits arbitrary finite log-reweightings but does not cover support-changing limits in which a gauge cell is set exactly to zero.

Falsify the claim by giving a two-ratio stationary pair from `VIS-049` and a positive finite gauge reweighting for which two gauges have the same `q` but different Fisher cosines; by finding `q != 0` with unchanged cosine; or by producing a second-variation direction not represented by the single mean-difference functional above.

## Research consequence

The active residual-direction program should not interpret the all-direction zero gradient of `VIS-049` as a high-dimensional basin of gauge robustness. On the exceptional two-ratio locus, the full finite dependence is exactly one-dimensional after quotienting the gauge: the angle is preserved only on the balance hypersurface `q=0`, and any transverse imbalance increases its magnitude toward `1`.

For empirical work this gives a sharper diagnostic than checking a generic Hessian numerically. If a residual pair appears close to the two-ratio stationary geometry, first estimate the class-contrast coordinate and challenge it with predeclared finite gauge changes. A tiny first-order gradient or many flat within-class directions are expected from the exact geometry and are not evidence of an arithmetic invariant.

This closes the finite-gauge geometry naturally exposed by `VIS-049`. Testing actual zeta/CUE residual tables against the two-ratio locus, or classifying the higher-cumulant flatness hierarchy inside the rank-one Hessian kernel, is intentionally left for later invocations.
