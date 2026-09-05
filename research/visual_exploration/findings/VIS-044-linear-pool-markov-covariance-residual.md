# VIS-044 — linear pooling of Markov closures creates a panel-covariance residual

## Claim

Let `Q^(1),...,Q^(m)` be strictly positive first-order Markov laws on one common finite support `(X,Y,Z)`, written

`Q^(r)_(ijk)=q^(r)_j a^(r)_(i|j) b^(r)_(k|j)`,

and let positive weights `lambda_r` satisfy `sum_r lambda_r=1`. Define their arithmetic/linear pool

`Qbar = sum_r lambda_r Q^(r)`.

Then three exact facts hold.

First, for every strictly positive probability law `R` on the common support,

`sum_r lambda_r D_KL(Q^(r)||R)`
` = sum_r lambda_r D_KL(Q^(r)||Qbar) + D_KL(Qbar||R)`.

Hence `Qbar` is the unique unconstrained minimizer of the panel-to-gauge loss

`R -> sum_r lambda_r D_KL(Q^(r)||R)`.

Second, `Qbar` need not be Markov even though every panel member is. Put

`qbar_j = sum_r lambda_r q^(r)_j`,

and for every `j` define the reweighted panel probabilities

`w_r(j)=lambda_r q^(r)_j/qbar_j`.

Then the `Y=j` conditional law of the linear pool is

`Qbar_(ik|j)=sum_r w_r(j) a^(r)_(i|j) b^(r)_(k|j)`.

Its adjacent-pair-preserving Markov closure is

`M(Qbar)_(ijk)=qbar_j abar_(i|j) bbar_(k|j)`,

where

`abar_(i|j)=sum_r w_r(j) a^(r)_(i|j)`

and

`bbar_(k|j)=sum_r w_r(j) b^(r)_(k|j)`.

Therefore the exact interaction residual created by linear pooling is

`Qbar_(ijk)-M(Qbar)_(ijk)`
` = qbar_j Cov_(w(j))(a^(r)_(i|j), b^(r)_(k|j))`.

Thus a nonzero three-way residual can appear **purely from cross-panel co-variation of the admitted left and right Markov channels**, with zero irreducible conditional interaction inside every `Q^(r)`.

Third, among Markov reference laws the unique minimizer of the same panel-to-gauge objective is `M(Qbar)`, and the unavoidable extra price of enforcing the Markov gauge is exactly

`D_KL(Qbar||M(Qbar)) = I_Qbar(X;Z|Y)`.

Equivalently,

`min_(R Markov) sum_r lambda_r D_KL(Q^(r)||R)`
` = sum_r lambda_r D_KL(Q^(r)||Qbar) + I_Qbar(X;Z|Y)`.

This gives a sharp dual control for `VIS-042` and `VIS-043`. The gauge-to-panel KL direction used there selects the normalized geometric/logarithmic pool and stays inside the shared Markov family. Reversing the KL direction selects the arithmetic pool, which can leave that family and manufacture precisely the higher-order conditional interaction that the residual analysis is trying to measure.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL KL/LINEAR-POOL SPECIALIZATION + REPRESENTATION CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that linear pooling, mixture-induced dependence, Jensen-Shannon decomposition, KL projection onto a Markov chain, or conditional mutual information is new. The durable content is the explicit covariance-residual mechanism and its interpretation boundary for Mathia's active common-gauge three-gap comparison.

## 1. The panel-to-gauge KL barycenter is the arithmetic pool

Expand the objective:

`J(R)=sum_r lambda_r D_KL(Q^(r)||R)`
` = sum_r lambda_r sum_x Q^(r)(x) log Q^(r)(x)`
`   - sum_x Qbar(x) log R(x)`.

Likewise,

`sum_r lambda_r D_KL(Q^(r)||Qbar)`
` = sum_r lambda_r sum_x Q^(r)(x) log Q^(r)(x)`
`   - sum_x Qbar(x) log Qbar(x)`.

Subtracting gives exactly

`J(R) - sum_r lambda_r D_KL(Q^(r)||Qbar)`
` = D_KL(Qbar||R)`.

Strict positivity makes the displayed quantities finite and Gibbs' inequality gives the unique minimum at `R=Qbar`.

This is the opposite KL direction from `VIS-043`. There the variable gauge appears in the **first** argument, `D_KL(R||Q^(r))`, and the weighted geometric pool is the unique barycenter. Here it appears in the **second** argument, `D_KL(Q^(r)||R)`, and the arithmetic pool is the unique barycenter. The KL direction is therefore part of the representation contract rather than a cosmetic choice.

## 2. Linear pooling creates a covariance residual

For fixed `j`, normalize the linear pool by `qbar_j`:

`Qbar_(ik|j)`
` = sum_r [lambda_r q^(r)_j/qbar_j] a^(r)_(i|j)b^(r)_(k|j)`
` = sum_r w_r(j) a^(r)_(i|j)b^(r)_(k|j)`.

Its conditional `X` and `Z` marginals are

`abar_(i|j)=sum_r w_r(j)a^(r)_(i|j)`

and

`bbar_(k|j)=sum_r w_r(j)b^(r)_(k|j)`.

The Markov closure therefore has conditional table `abar bbar`. Subtracting yields

`Qbar_(ik|j)-abar_(i|j)bbar_(k|j)`
` = sum_r w_r(j)a^(r)_(i|j)b^(r)_(k|j)`
`   - [sum_r w_r(j)a^(r)_(i|j)]`
`     [sum_s w_s(j)b^(s)_(k|j)]`
` = Cov_(w(j))(a^(r)_(i|j),b^(r)_(k|j))`.

Multiplication by `qbar_j` gives the claim.

Consequently `Qbar` is Markov exactly when every conditional mixture matrix

`sum_r w_r(j) a^(r)_(.|j) (b^(r)_(.|j))^T`

has rank one, equivalently when all of its `2 x 2` minors vanish. Shared left conditionals or shared right conditionals are sufficient but not necessary special cases. In general the Markov family is not closed under arithmetic mixtures.

The covariance formula is the important representation control. A residual seen after pooling can be induced by **heterogeneity of lower-order channels across panel members**, even when every member individually has zero conditional mutual information. It must not be interpreted as evidence of a common irreducible three-gap mechanism.

## 3. Explicit strictly positive counterexample

Take `X,Y,Z` binary and two equally weighted panel laws. Let `Y` be uniform under both laws. Conditional on either value of `Y`, let `X` and `Z` be independent Bernoulli variables with success probability `0.9` in `Q^(1)` and `0.1` in `Q^(2)`.

Both panel laws are strictly positive and Markov. For either middle state, their arithmetic pool has conditional `(X,Z)` table

`[[0.41, 0.09],`
` [0.09, 0.41]]`.

Both conditional marginals are `(0.5,0.5)`, so the Markov product with those marginals is the uniform table with every cell `0.25`. Hence the arithmetic pool is not Markov.

Its pooling-induced conditional mutual information is

`I_Qbar(X;Z|Y)`
` = 2(0.41) log(0.41/0.25) + 2(0.09) log(0.09/0.25)`
` approx 0.2217536937` nats.

Nothing inside either panel member carries this conditional dependence; it is created entirely by mixing the two opposite lower-order channel regimes.

## 4. The Markov-constrained barycenter pays exactly the induced CMI

For any positive law `P`, its adjacent-pair-preserving Markov closure

`M(P)_(ijk)=P_(ij) P_(jk)/P_j`

is the unique minimizer of `D_KL(P||R)` over positive Markov laws `R` on the same support. To see this, write

`R_(ijk)=r_j alpha_(i|j) beta_(k|j)`.

The ordinary KL chain rule gives

`D_KL(P||R)`
` = I_P(X;Z|Y)`
` + D_KL(P_Y||r)`
` + sum_j P_j D_KL(P_(X|j)||alpha_(.|j))`
` + sum_j P_j D_KL(P_(Z|j)||beta_(.|j))`.

Every term after the CMI is nonnegative and they vanish simultaneously exactly when `R=M(P)`. Thus

`min_(R Markov) D_KL(P||R)=I_P(X;Z|Y)`.

Apply this with `P=Qbar` and combine it with the decomposition from section 1. The constrained panel barycenter is `M(Qbar)` and the exact gap between the unconstrained and Markov-constrained optima is the pooling-induced CMI.

This same identity is the information-theoretic baseline already anchored in `VIS-020` and `SOURCES.md`; here it is applied to the **panel mixture itself**, where the conditional interaction has a different origin from the own-process residuals `P^(r)-Q^(r)` studied in `VIS-040`--`VIS-043`.

## 5. Prior-art and novelty boundary

Linear opinion pooling and its failure to preserve unanimous independence are classical. `VIS-042` already records the complementary graphical-model fact that logarithmic pooling preserves commonly held Markov independencies, while `VIS-043` records the weighted-KL variational characterization of that logarithmic pool. Standard KL chain rules, conditional mutual information, and the Markov completion identity are anchored in Cover and Thomas through `SOURCES.md` and `VIS-020`.

The decomposition in section 1 is the standard weighted relative-entropy/Jensen-Shannon barycenter identity. Mixtures of conditionally independent laws producing conditional dependence are likewise a classical latent-mixture phenomenon. No novelty is claimed for those general facts.

The Mathia-specific contribution is only the exact specialization needed to close an active representation loophole: when the candidate common gauge is built from the panel's **already residualized Markov closures**, the linear-pool interaction tensor is exactly a weighted covariance of their left/right conditional channels, and the cost of projecting that artificial interaction away is exactly its CMI.

## 6. Boundary conditions and falsification

Strict positivity and a common support make every KL expression finite and the Markov closure unique in the displayed form. Structural or sampling zeros require the same predeclared support/regularization discipline as `VIS-042` and `VIS-043`; changing support after inspecting residual alignment can alter both the pooling covariance and the projection penalty.

The panel and weights must be frozen before residual comparison. Choosing weights to make the linear pool nearly Markov, or to make `M(Qbar)` favor a desired zeta/CUE angle, is post-selection rather than a neutral gauge rule.

The induced CMI is a property of the **pooled reference construction**, not evidence that any original process has three-gap interaction. Conversely, `I_Qbar=0` does not imply that the own-process residuals agree in magnitude or orientation; it says only that this particular arithmetic mixture introduced no conditional interaction.

The covariance identity is falsified by any finite positive panel for which a cell of `Qbar-M(Qbar)` differs from the displayed weighted covariance. The constrained-barycenter statement is falsified if a positive Markov law has smaller `D_KL(Qbar||R)` than `M(Qbar)` or if the optimum gap differs from `I_Qbar(X;Z|Y)`.

## Research consequence

For the accepted `CLUE-zeta-three-gap-cmi-equivalent-size-eight`, a panel-wide common gauge should not be selected by first linearly pooling the process Markov closures and then interpreting the resulting non-Markov structure as part of the residual geometry. Linear pooling can create exactly such structure from lower-order panel heterogeneity.

The logarithmic-pool gauge of `VIS-042` now has a second exact justification beyond the `VIS-043` variational interpretation: under the same predeclared panel it remains inside the admitted Markov reference family, whereas the opposite KL barycenter can leave that family. If an empirical analysis nevertheless uses a linear pool for another reason, it should report the induced tensor `Qbar-M(Qbar)` or at least `I_Qbar(X;Z|Y)` as a representation artifact and separate it from every own-process residual.

No new visualization or clue is required. This completes one coherent gauge-direction control and leaves the accepted higher-window transfer test unchanged.
