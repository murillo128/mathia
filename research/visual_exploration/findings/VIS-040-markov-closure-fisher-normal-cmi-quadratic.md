# VIS-040 — near Markov closure, CMI is the Fisher-normal interaction energy

## Claim

Let `P=(p_ijk)` be a strictly positive probability law on a fixed finite alphabet for three variables `X,Y,Z`, and suppose `P` is first-order Markov:

`p_ijk = p_ij p_jk / p_j`.

Consider a smooth probability perturbation

`P_epsilon = P + epsilon A + O(epsilon^2)`,

with `sum_(i,j,k) a_ijk=0`, and write the induced marginal perturbations as

`a_ij=sum_k a_ijk`, `a_jk=sum_i a_ijk`, `a_j=sum_(i,k) a_ijk`.

Let `Q_epsilon` be the adjacent-pair-preserving Markov closure of `P_epsilon`, as in `VIS-020`. Its first derivative at `P` is

`(Pi_P A)_ijk = p_ijk (a_ij/p_ij + a_jk/p_jk - a_j/p_j)`.

Define the residual normal component

`B = A - Pi_P A`.

Then `B` has zero `XY` and `YZ` marginals:

`sum_k b_ijk=0`, `sum_i b_ijk=0`,

and the conditional mutual information has the quadratic expansion

`I_(P_epsilon)(X;Z|Y)`
` = D(P_epsilon || Q_epsilon)`
` = (epsilon^2/2) sum_(i,j,k) b_ijk^2/p_ijk + O(epsilon^3)`.

Moreover `Pi_P A` is the Fisher-orthogonal projection of `A` onto the tangent space of the positive first-order-Markov manifold at `P`, under

`<U,V>_P = sum_(i,j,k) u_ijk v_ijk / p_ijk`.

Thus the leading CMI is exactly one half of the squared Fisher norm of the perturbation component normal to the Markov manifold. It measures the **magnitude** of irreducible conditional dependence to second order but discards its normal direction/orientation.

In particular, if

`P_N = P + N^(-2) A + O(N^(-4))`,

then

`I_N = (N^(-4)/2) sum b_ijk^2/p_ijk + O(N^(-6))`.

This sharpens the Markov-limit cancellation boundary of `VIS-039`: the first nonzero CMI term is not an arbitrary fourth-order scalar. It is the Fisher-normal energy of the `N^-2` cell-law correction.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL INFORMATION-GEOMETRY SPECIALIZATION + REPRESENTATION CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that the relevant CUE or zeta three-gap cell laws satisfy the displayed finite-size expansion, that their normal directions agree, or that a scalar CMI crossing identifies an effective matrix size or arithmetic correction.

## 1. Derivative of the Markov closure

For a strictly positive law `R`, its adjacent-pair-preserving Markov closure is

`M(R)_ijk = r_ij r_jk / r_j`.

At the Markov point `P=M(P)`, substitute

`r_ij=p_ij+epsilon a_ij+O(epsilon^2)`,
`r_jk=p_jk+epsilon a_jk+O(epsilon^2)`,
`r_j=p_j+epsilon a_j+O(epsilon^2)`.

Differentiating gives

`M(P_epsilon)_ijk`
` = p_ijk + epsilon p_ijk`
`   (a_ij/p_ij + a_jk/p_jk - a_j/p_j)`
`   + O(epsilon^2)`.

This is the stated linear map `Pi_P A`.

Now sum it over `k`. Using `sum_k p_ijk=p_ij`, `sum_k a_jk=a_j`, and `sum_k p_jk=p_j`, one obtains

`sum_k (Pi_P A)_ijk = a_ij`.

Likewise

`sum_i (Pi_P A)_ijk = a_jk`.

Therefore the residual `B=A-Pi_P A` has zero `XY` and `YZ` marginals. It is exactly the first-order part of the perturbation that cannot be explained by moving the two adjacent-pair marginals while remaining inside Markov closure.

## 2. Quadratic expansion of CMI

Because both `P_epsilon` and `Q_epsilon=M(P_epsilon)` equal `P` at `epsilon=0`, write

`P_epsilon = P + epsilon A + O(epsilon^2)`,
`Q_epsilon = P + epsilon Pi_P A + O(epsilon^2)`.

For two smooth probability paths through the same strictly positive base law, the standard local expansion of relative entropy is

`D(P+epsilon A || P+epsilon C)`
` = (epsilon^2/2) sum (A-C)^2/P + O(epsilon^3)`.

Applying `C=Pi_P A` gives

`D(P_epsilon||Q_epsilon)`
` = (epsilon^2/2) sum b_ijk^2/p_ijk + O(epsilon^3)`.

Since `VIS-020` establishes exactly that

`D(P_epsilon||Q_epsilon)=I_(P_epsilon)(X;Z|Y)`,

the CMI formula follows.

The same expansion also gives the local Pearson relation

`chi^2(P_epsilon||Q_epsilon)`
` = epsilon^2 sum b_ijk^2/p_ijk + O(epsilon^3)`,

so

`I_(P_epsilon)(X;Z|Y)`
` = (1/2) chi^2(P_epsilon||Q_epsilon) + O(epsilon^3)`.

This is the population information-geometric counterpart of the finite-table Pearson/LRT local equivalence in `VIS-037`.

## 3. Fisher-orthogonal decomposition

The positive first-order-Markov family is the smooth conditional-independence model

`X independent of Z given Y`.

A tangent vector `C` to this family at `P` has logarithmic derivative of the form

`c_ijk/p_ijk = u_ij + v_jk - w_j`,

with the usual compatibility/normalization constraints inherited from a probability path in the model. This is exactly the differential form supplied by the Markov-closure derivative above.

For the residual `B`, zero `XY` and `YZ` marginals imply

`sum_(i,j,k) b_ijk u_ij = 0`,
`sum_(i,j,k) b_ijk v_jk = 0`,
`sum_(i,j,k) b_ijk w_j = 0`.

Hence for every Markov tangent `C`,

`<B,C>_P`
` = sum b_ijk c_ijk/p_ijk`
` = 0`.

Therefore `B` lies in the Fisher-normal space and `Pi_P A` is the Fisher-orthogonal tangent projection of the perturbation. The quadratic CMI term is simply

`(epsilon^2/2) ||B||_P^2`.

This supplies an exact information-loss map for the active three-gap program: passing from the full normal residual `B` to scalar CMI retains its Fisher length but quotients out which normal direction carries the dependence.

## 4. Consequence for finite-size transfer

`VIS-039` shows that a generic non-Markov limiting law can pass an `N^-2` correction directly into CMI through the first variation `L_P(A)`, while a Markov limit cancels that linear term and forces `I_N=O(N^-4)` under an even cell-law expansion.

The present result identifies the surviving Markov-limit coefficient. With `epsilon=N^-2`,

`I_N = (N^-4/2)||B||_P^2 + O(N^-6)`.

Thus an observed scalar `N^-4` law would establish, at most, that the size of the normal conditional-dependence perturbation follows the corresponding scale. It would **not** show that two processes have the same normal direction, the same conditional residual tensor, the same middle-fiber allocation, or the same CA/principal-inertia modes.

Likewise a scalar crossing at some finite `N` can occur when two different normal directions happen to have comparable Fisher norm. A statistic-dependent CMI-equivalent size therefore cannot be promoted into a process-level transfer statement without a direction-sensitive comparison.

## 5. Relation to the existing Pearson/CA quotient

`VIS-035` identifies the conditional correspondence-analysis spectrum as the principal-inertia decomposition of the Pearson interaction energy, while `VIS-037` and `VIS-038` show that Pearson and likelihood-ratio/CMI statistics are locally the same quadratic channel, with their first scalar separation arising from higher powers of the same fitted residual.

The Fisher-normal formulation explains those controls at the population level. Near a Markov law, the whitened conditional residual is a coordinate representation of the normal vector `B`, and its squared norm is the common leading Pearson/CMI energy. The full residual tensor, or an equivalent complete set of whitened fiber coordinates, retains direction; the scalar totals do not.

A singular-value spectrum retains more geometry than the scalar norm but still quotients left/right orientation within degenerate or rotated singular subspaces. Therefore agreement of CMI, Pearson energy, or even singular values across two processes should not be counted as independent evidence that their irreducible conditional-dependence mechanisms coincide.

## 6. Prior art and novelty assessment

The local quadratic relation between Kullback-Leibler divergence and the Fisher information metric is foundational information geometry, and conditional-independence/Markov models are standard statistical models. Shun-ichi Amari and Hiroshi Nagaoka, **Methods of Information Geometry**, Translations of Mathematical Monographs 191, AMS/Oxford University Press (2000), is a standard reference for Fisher-metric and divergence geometry. Cover and Thomas remain the standard information-theory anchor already recorded in `SOURCES.md` for conditional mutual information and relative entropy.

Pearson/LRT local equivalence and power-divergence expansions are also classical, as already bounded by the Cressie-Read prior art recorded for `VIS-037` and the higher-order comparison cited in `VIS-038`.

No novelty is claimed for the Fisher metric, KL Hessian, conditional-independence model, orthogonal projection language, or local chi-square/KL equivalence. The Mathia-specific value is the explicit specialization to the active adjacent-pair-preserving three-gap closure: the exact normal residual is `B=A-Pi_P A`, its two adjacent-pair marginals vanish, and its Fisher norm gives the leading CMI coefficient. This makes precise which information the current scalar visual statistics discard.

## 7. Boundary conditions and falsification

Strict positivity is essential for the displayed smooth Fisher coordinates and Taylor expansion. If a cell or required marginal tends to zero, boundary singularities can change the local order and the calculation must be repeated on a justified common positive support rather than extrapolated through zero cells.

The alphabet and partition must remain fixed along the perturbation. Moving bin boundaries, data-dependent support trimming, or changing conditioning variables introduces extra tangent directions and changes both `Pi_P` and `B`.

The `N^-4` specialization requires the stated smooth even law `P_N=P+N^-2 A+O(N^-4)` with a Markov limiting `P`. It does not follow merely from an empirical `N^-4` fit, and the Forrester-Shen even-power correlation results cited in `VIS-039` do not by themselves prove the exact required three-consecutive-spacing cell expansion.

Falsify the derivation if the displayed `Pi_P A` fails to reproduce the `XY` or `YZ` perturbation marginals, if `B` is not Fisher-orthogonal to a valid Markov tangent, or if a smooth full-support numerical perturbation violates the quadratic coefficient as `epsilon->0`. Such a failure would indicate an algebraic/support error rather than a new empirical effect.

## Research consequence

The active three-gap program should treat scalar CMI/Pearson finite-size transfer as a **norm-level** comparison only. A stronger claim of transferred irreducible three-gap structure must compare a pre-registered direction-sensitive object: the full normal residual tensor after whitening, an equivalent signed/fiber-resolved coordinate system, or mode information whose remaining quotient is stated explicitly.

This does not create a new empirical task by itself. `CLUE-zeta-three-gap-conditional-residual` already asks for the full residual and matched spectrum, and `CLUE-zeta-three-gap-cmi-equivalent-size-eight` already requires higher-window testing before interpreting its descriptive crossing. The present result supplies the exact information-geometric reason those stronger controls are necessary. No new visualization is required for this finding.