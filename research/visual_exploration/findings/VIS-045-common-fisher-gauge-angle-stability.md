# VIS-045 — common Fisher residual angles are quantitatively stable under bounded gauge change

## Claim

Let `V` be any nonzero real linear subspace of residual tensors on one fixed finite support `Omega`; in the three-gap application one may take the interaction space of tensors with zero `XY` and `YZ` marginals. Let `H` and `G` be two strictly positive common reference laws on `Omega`, and equip `V` with the Fisher-type inner products

`<R,S>_H = sum_(x in Omega) R_x S_x / H_x`,

`<R,S>_G = sum_(x in Omega) R_x S_x / G_x`.

For nonzero residuals `A,B in V`, let `theta_H, theta_G in [0,pi]` be their signed vector angles under the two inner products, so

`cos(theta_H)=kappa_H(A,B)`,  `cos(theta_G)=kappa_G(A,B)`.

Define the intrinsic norm-comparison constants on the actual residual space

`m_V = inf_(0 != R in V) ||R||_G / ||R||_H`,

`M_V = sup_(0 != R in V) ||R||_G / ||R||_H`,

and `K_V=M_V/m_V`. Since the support is finite and both gauges are positive, `0<m_V<=M_V<infinity`.

Then the generalized Wielandt angle inequality gives the exact representation-stability bound

`K_V^(-1) tan(theta_H/2) <= tan(theta_G/2) <= K_V tan(theta_H/2)`.

For collinear residuals the angle is `0` or `pi` under every positive gauge, so the same conclusion holds by the limiting interpretation.

There is also a simple pointwise bound requiring no generalized-eigenvalue computation. Put

`r_x = H_x/G_x`,

`r_min = min_x r_x`,  `r_max = max_x r_x`,

`K_pt = sqrt(r_max/r_min)`.

Then `K_V<=K_pt`, hence

`K_pt^(-1) tan(theta_H/2) <= tan(theta_G/2) <= K_pt tan(theta_H/2)`.

Equivalently, if

`omega = max_x log(H_x/G_x) - min_x log(H_x/G_x)`,

then `K_pt=exp(omega/2)`. In particular a residual-angle sign is certified against every such gauge change whenever

`kappa_H > tanh(omega/2)  =>  kappa_G > 0`,

`kappa_H < -tanh(omega/2) =>  kappa_G < 0`.

Thus `VIS-041`'s warning that orientation is reference-dependent can be sharpened: gauge dependence is not arbitrary when the two positive gauges are uniformly comparable. Strong alignment or opposition cannot flip sign under a bounded likelihood-ratio spread, while weak orientation remains legitimately gauge-sensitive.

**Evidence/status:** `LITERATURE+DERIVED + EXACT SPECIALIZATION + REPRESENTATION CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that the Fisher gauge is canonical, that the pointwise bound is always sharp on the residual subspace, that zeta and CUE residual directions agree, or that this supplies an RH criterion.

## 1. Two positive gauges define two inner products on the same interaction space

The residual tensors in `VIS-041` are formed before common whitening:

`Delta(P)=P-M(P)`.

They therefore belong to a fixed linear interaction space determined by the common support and the zero adjacent-marginal constraints. Choosing a positive gauge changes the metric on that same vector space; it does not change the residual tensor itself.

For any `R in V`,

`||R||_G^2`
` = sum_x R_x^2/G_x`
` = sum_x (R_x^2/H_x) (H_x/G_x)`.

Dividing by `||R||_H^2` shows that

`||R||_G^2 / ||R||_H^2`

is a weighted average of the pointwise ratios `r_x=H_x/G_x`, with nonnegative weights proportional to `R_x^2/H_x`. Consequently

`sqrt(r_min) <= ||R||_G/||R||_H <= sqrt(r_max)`

for every nonzero residual. Restricting to `V` can only tighten these extrema, so

`sqrt(r_min) <= m_V <= M_V <= sqrt(r_max)`

and therefore `K_V<=K_pt`.

The intrinsic `K_V` is the condition number of the identity map from `(V,<.,.>_H)` to `(V,<.,.>_G)`. In finite coordinates it can be obtained from the extreme generalized eigenvalues of the two Gram forms restricted to any basis of `V`. The pointwise `K_pt` is a conservative ambient bound that is immediate from the two gauge tables.

## 2. Generalized Wielandt gives the sharp intrinsic angle distortion

Lin and Sinnamon's generalized Wielandt inequality compares vector angles under two inner products. With

`m=inf ||R||_G/||R||_H`,  `M=sup ||R||_G/||R||_H`,

their Theorem 2.4 gives, for independent vectors with angles in `[0,pi]`,

`(m/M) tan(theta_H/2) <= tan(theta_G/2) <= (M/m) tan(theta_H/2)`.

Apply the theorem to the finite-dimensional residual space `V`. The constants are exactly `m_V,M_V`, yielding the first displayed claim. Substituting `K_V<=K_pt` yields the easier pointwise corollary.

This result is stronger than merely bounding the change of the cosine additively. It respects the full signed vector angle: near `theta=0`, multiplicative half-angle distortion measures loss of alignment; near `theta=pi`, the reciprocal behavior controls loss of opposition. It is therefore the appropriate classical control for `VIS-041`'s signed Fisher residual orientation rather than the line-angle version that would identify `A` and `-A`.

The equivalent cosine form, writing

`chi_V=(K_V^2-1)/(K_V^2+1)`,

is

`(-chi_V+kappa_H)/(1-chi_V kappa_H) <= kappa_G <= (chi_V+kappa_H)/(1+chi_V kappa_H)`.

The same statement with `K_pt` instead of `K_V` is generally weaker but requires only the gauge-ratio envelope.

## 3. The logarithmic ratio oscillation is the natural coarse robustness diagnostic

Multiplying one inner product by a positive scalar does not change angles. Accordingly only the **oscillation** of the pointwise gauge ratio matters to `K_pt`, not its absolute level:

`omega = osc_x log(H_x/G_x)`.

Since `K_pt=exp(omega/2)`, gauges that differ by an almost constant multiplicative factor have nearly identical residual angles even if their raw probabilities are numerically small. Conversely, a gauge assigning radically different relative weights to some cells can have large `omega` and large possible angle distortion.

The cosine distortion parameter becomes

`chi_pt=(K_pt^2-1)/(K_pt^2+1)=tanh(omega/2)`.

Hence the sign-stability corollary follows directly from the cosine bounds. If `kappa_H>chi_pt`, even the worst admissible decrease leaves `kappa_G>0`; if `kappa_H<-chi_pt`, even the worst admissible increase leaves `kappa_G<0`. At equality a right angle can occur, so strict inequalities are required for a strict sign conclusion.

This is only a sufficient certificate. A large `omega` does not prove that the measured orientation will change; it says that the proposed gauge comparison is poorly conditioned by this coarse control. Computing `K_V` on the exact interaction space can substantially sharpen the certificate because residual constraints may exclude the cells or directions that realize the ambient extremes.

## 4. Relation to the three-gap common-gauge program

`VIS-041` established that two own-process Markov residuals can be compared directionally only after both are embedded in one common positive Fisher metric. `VIS-042` and `VIS-043` then supplied a predeclared logarithmic-pool construction and its weighted-KL barycenter meaning, while `VIS-044` showed that reversing the KL direction selects a linear pool that can manufacture conditional interaction from lower-order panel covariance.

Those results decide **how a common gauge may be constructed without creating the target residual**, but they deliberately do not make that gauge canonical. The present bound closes the next representation question: how much can the signed Fisher orientation change when a reasonable alternative positive gauge is used?

A future zeta/CUE direction comparison can therefore freeze its primary gauge exactly as already required and also predeclare one or more source-compatible alternative gauges. For each alternative it can report either the sharper interaction-space condition number `K_V` or the immediate pointwise spread `K_pt`. If the observed primary `kappa_H` lies outside the corresponding sign-instability band `[-chi,chi]`, its alignment/opposition sign is certified for that gauge family without searching gauges for favorable agreement.

If `K` is large enough that the certificate is vacuous, that is a representation warning rather than evidence against either process. The empirical comparison may still be informative under its frozen primary gauge, but a claim of gauge-robust residual orientation has not been established.

## 5. Prior art and novelty boundary

The angle-distortion theorem is classical prior art. Minghua Lin and Gord Sinnamon, **The Generalized Wielandt Inequality in Inner Product Spaces**, *Eurasian Mathematical Journal* 3:1 (2012), 72–85, arXiv `1201.6294`, formulate the two-inner-product norm extrema and prove the sharp half-angle comparison in Theorem 2.4, together with equivalent cosine inequalities. No novelty is claimed for Wielandt-type angle inequalities, condition-number control, generalized eigenvalues, Fisher inner products, or the weighted-average estimate above.

The Mathia-specific durable content is the specialization to the exact residual geometry already fixed by `VIS-041`: the theorem turns an acknowledged gauge dependence into an auditable quantitative control, while the cellwise Fisher form makes the conservative condition number equal to a simple oscillation of the log gauge ratio. This supplies a pre-registration criterion for distinguishing a genuinely robust residual direction from an orientation that is fragile because the chosen common metric reweights cells too unevenly.

## 6. Boundary conditions and falsification

Both gauges must be strictly positive on one common fixed support. Structural or sampling zeros require the same predeclared support/regularization discipline as `VIS-041`--`VIS-044`; allowing different supports makes the two inner products live on different spaces and invalidates the comparison.

The residuals must be held fixed while the gauge changes. Recomputing bins, changing the Markov closure, selecting a support, rotating process-specific coordinates, or changing the panel at the same time mixes metric sensitivity with a different statistical object and falls outside this theorem.

The `K_pt` bound may be conservative because the interaction constraints restrict allowable residual directions. Claims of sharpness should use `K_V` and the equality conditions of the generalized Wielandt theorem, not the ambient ratio spread alone.

Falsify the specialization by exhibiting a fixed finite positive pair `H,G` and residuals in the same interaction space for which the measured angles violate the `K_V` half-angle inequality, or by finding a nonzero residual whose norm ratio lies outside the displayed pointwise interval. Either failure would indicate an error in the support, inner-product, or ratio construction.

## Research consequence

The common-gauge branch now has an exact robustness gate rather than only a warning that `kappa_H` depends on `H`. Freeze the primary gauge before inspection as required by `VIS-041`--`VIS-044`; for any predeclared alternative positive gauge, quantify its distortion by `K_V` when practical or `K_pt` otherwise. Treat an orientation sign as gauge-robust only when it clears the corresponding `chi=(K^2-1)/(K^2+1)` threshold, and report weakly conditioned cases as gauge-sensitive rather than optimizing the reference.

This does not unblock the currently blocked higher-window CMI/direction confirmation, which still lacks the authoritative high-zero inputs required by its Gate 0. It closes one coherent representation-control question and requires no new visualization or clue.