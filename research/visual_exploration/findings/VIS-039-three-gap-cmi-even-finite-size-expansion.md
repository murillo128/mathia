# VIS-039 — binned three-gap CMI inherits an even finite-size correction from the cell law

## Claim

Let `P_N=(p_ijk(N))` be a family of strictly positive probability laws on one fixed finite alphabet for three consecutive binned variables `X,Y,Z`. Suppose, componentwise,

`p_ijk(N) = p_ijk + N^(-2) a_ijk + O(N^(-4))`,

with limiting law `P=(p_ijk)` also strictly positive. Let `p_ij`, `p_jk`, and `p_j` denote the corresponding limiting marginals, and let `a_ij`, `a_jk`, and `a_j` be the marginals of the perturbation tensor `A=(a_ijk)`.

Then the population conditional mutual information has the expansion

`I_N = I_P(X;Z|Y) + N^(-2) L_P(A) + O(N^(-4))`,

where

`L_P(A) = sum_(i,j,k) a_ijk log( p_ijk p_j / (p_ij p_jk) )`.

Thus an even `N^(-2)` finite-size expansion of the underlying fixed-bin triple law transfers automatically to CMI. A visible stabilization of `N^2[I_N-I_infinity]` is therefore a **generic compatibility signature of the cell-law expansion**, not by itself evidence for a special effective-size mechanism or an arithmetic residual.

There is also an exact cancellation boundary. If the limiting law is first-order Markov,

`p_ijk p_j = p_ij p_jk`

on every cell, then `L_P(A)=0`, so under the displayed even expansion

`I_N = O(N^(-4))`.

More generally the `N^(-2)` coefficient can vanish by the single orthogonality condition `L_P(A)=0` even when the limiting law is not Markov. Hence the power at which a derived statistic first changes can be later than the power appearing in the underlying finite-size law.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL INFORMATION-FUNCTIONAL DIFFERENTIATION + FINITE-SIZE REPRESENTATION CONTROL + NO-NOVELTY-CLAIM`.

This finding does **not** prove that the exact CUE three-consecutive-spacing cell probabilities used by the active numerical clue satisfy the assumed expansion, and it does not identify any observed `N=8` crossing with a physical effective matrix size.

## 1. First variation of conditional mutual information

For a strictly positive finite triple law `R=(r_ijk)`, write CMI in entropy-sum form:

`I(R)`
` = sum_(i,j,k) r_ijk log r_ijk`
`   + sum_j r_j log r_j`
`   - sum_(i,j) r_ij log r_ij`
`   - sum_(j,k) r_jk log r_jk`.

Let `R(epsilon)=P+epsilon A+O(epsilon^2)`, where probability normalization gives `sum a_ijk=0`. Differentiating at `epsilon=0` yields

`dI_P[A]`
` = sum a_ijk (1+log p_ijk)`
`   + sum a_j (1+log p_j)`
`   - sum a_ij (1+log p_ij)`
`   - sum a_jk (1+log p_jk)`.

The four constant terms cancel because every marginal perturbation has the same total mass `sum a_ijk=0`. Expanding each marginal sum back over `(i,j,k)` gives

`dI_P[A]`
` = sum_(i,j,k) a_ijk`
`     [log p_ijk + log p_j - log p_ij - log p_jk]`
` = sum_(i,j,k) a_ijk log( p_ijk p_j / (p_ij p_jk) )`.

Strict positivity makes the entropy functional smooth in a neighborhood of `P`. Taking `epsilon=N^(-2)` therefore gives the claimed expansion through `O(N^(-4))` whenever the cell law itself has the corresponding even expansion.

The same calculation with only

`P_N=P+N^(-2)A+o(N^(-2))`

gives the weaker but assumption-matched statement

`I_N=I(P)+N^(-2)L_P(A)+o(N^(-2))`.

## 2. Why Markov closure kills the first correction

`VIS-020` identifies the adjacent-pair-preserving Markov condition as

`p_ijk = p_ij p_jk / p_j`.

Under this condition the logarithm in every summand of `L_P(A)` is zero. The first variation of CMI therefore vanishes in every mass-preserving direction, as it must because conditional independence is a global minimum of the nonnegative CMI functional.

Consequently a perturbation of size `epsilon=N^(-2)` away from a full-support Markov limit produces CMI only at quadratic order, generically `O(epsilon^2)=O(N^(-4))`. This is the same structural warning already encountered elsewhere in the finite-size program: a leading correction in the probability law can disappear after passing through a nonlinear statistic.

Nishigaki's finite-CUE analysis provides a concrete neighboring example of this general phenomenon. The joint law of two consecutive spacings has an `O(N^(-2))` finite-size correction, while the gap-ratio distribution cancels that order and first differs at `O(N^(-4))`. The present result is not a rederivation of that spacing theorem; it gives the analogous cancellation criterion for the fixed-bin CMI functional.

## 3. Relation to known finite-CUE expansions

Forrester and Shen prove that, for the circular beta ensembles with `beta=1,2,4`, general bulk `n`-point correlation functions have asymptotic expansions in powers of `1/N^2`, and that the expansion lifts to spacing distributions and their generating functions. For `beta=2`, this places even-power finite-size behavior on a strong classical footing well beyond a single nearest-neighbor statistic.

That literature makes an even expansion for the present CUE control **natural but does not by itself establish the exact hypothesis used above**. A binned vector of three consecutive spacings is a four-eigenvalue/three-empty-interval Janossy-type object, and the active computation also applies a finite-sample plug-in estimator to cyclic within-matrix triples. Passing from correlation or ordinary spacing expansions to this exact joint cell law requires the relevant Janossy/inclusion-exclusion control and uniformity; passing further to the expected empirical estimator adds another layer. Those steps are not supplied by this finding.

The prior-art boundary is stronger on the zeta side as well. Bogomolny and Keating already gave a finite-height three-point correlation framework for Riemann zeros that combines the universal random-matrix limit with non-universal trace-formula/small-prime contributions. Therefore neither finite-height three-point structure nor a universal-plus-arithmetic decomposition is new here. The Mathia question is narrower: whether the **specific three-consecutive-gap conditional statistic and its matched finite-circle baseline** transfer in the way assumed by the active experiment.

## 4. Consequence for the observed finite-`N` CMI curve

The current proposed clue records that, with one frozen partition and fixed finite-sample protocol, the measured CUE mean CMI decreases with `N`, crosses all three tested zeta windows at the descriptive integer size `N=8`, and has approximately stable values of

`N^2 Delta_B(N)`

for `N=12,16,24,32`, where `Delta_B(N)` is measured relative to the still-finite `CUE_64` reference.

The present identity changes what that large-`N` pattern can mean. **Approximate `N^(-2)` behavior is expected whenever the relevant population cell law has a generic even finite-size correction and its first CMI coefficient does not cancel.** It is therefore a consistency check for finite-CUE behavior, not a discriminator between an order-specific effective-size transfer, ordinary finite-circle correction, and the remaining arithmetic/process mismatch.

The integer `N=8` crossing remains an empirical fact of the predeclared statistic, but it should stay descriptive. A crossing of one nonlinear statistic can occur because its finite-size coefficient and limiting value happen to bracket the zeta value; the first-variation formula supplies no reason that this crossing must equal the pair-derived effective size or transfer coherently to other statistics.

## 5. Empirical-estimator boundary

`I_N` in the claim is the **population** CMI of a fixed categorical law. The values persisted by the active clue are means of a plug-in estimator built from a fixed number of sampled cyclic triples drawn through finite CUE matrices. Those triples are not independent within a matrix, the number of contributing matrices changes with `N`, and sparse-cell bias depends on the full sampling protocol.

Accordingly, even a proved `1/N^2` expansion for the population three-gap law would not automatically prove the same coefficient or remainder for the measured mean estimator. Conversely, an empirical `N^2 Delta(N)` plateau does not prove the population expansion. The distinction is material because the current clue is trying to decide whether a finite-circle effect is sufficient as a baseline, not merely fit a smooth curve through simulated means.

A decisive control can come from either direction: derive the exact finite-CUE joint three-spacing/Janossy expansion and propagate it through the frozen bins and estimator, or repeat the frozen protocol at independent higher zeta windows whose pair-derived effective sizes are materially larger and test whether the descriptive CMI bracket moves coherently. The existing clue already identifies windows near `N_e≈7.74` and `11.30` for that purpose.

## 6. Prior art and novelty assessment

The differential identity is an elementary consequence of the standard entropy representation of conditional mutual information; Cover and Thomas remain the canonical information-theory anchor already recorded for `VIS-020`. No novelty is claimed for differentiability of entropy or CMI on the interior of the probability simplex.

Peter J. Forrester and Bo-Jian Shen, **Finite size corrections in the bulk for circular beta ensembles**, *Forum of Mathematics, Sigma* 14 (2026), e105, DOI `10.1017/fms.2026.10240`, prove the even `1/N^2` expansion for general bulk correlation functions in the classical circular ensembles and its lift to spacing distributions/generating functions. This bounds any interpretation of the observed even-power CUE trend as a new numerical discovery.

E. Bogomolny and J. P. Keating, **A method for calculating spectral statistics based on random-matrix universality with an application to the three-point correlations of the Riemann zeros**, *Journal of Physics A: Mathematical and Theoretical* 46:30 (2013), 305203, DOI `10.1088/1751-8113/46/30/305203`, give a heuristic finite-height three-point zeta correlation combining universal random-matrix and non-universal small-prime contributions. This bounds the novelty of the broader finite-height three-point interpretation.

The Mathia-specific value is the exact information-accounting statement for the active binned three-gap statistic: **even finite-size structure transfers generically through CMI, but the leading order can cancel, so the power law of the derived statistic is itself a quotient/control rather than an independent signal.**

## 7. Boundary conditions and falsification

Strict positivity is essential for the displayed smooth derivative. If a limiting cell probability or required marginal vanishes, logarithmic singularities can change the expansion and the result must be restricted to the common positive support or rederived with boundary terms. Data-dependent bin deletion would also change the statistic being analyzed.

The partition must be fixed as `N` varies. Moving quantile edges with `N` adds a second perturbation through the coordinates themselves and can manufacture or cancel finite-size terms. This is why the common frozen partition in the current clue is the appropriate object for this control.

The result says nothing if the underlying cell law contains an `O(N^(-1))`, logarithmic, oscillatory, or otherwise non-even leading correction. Likewise, Forrester-Shen's correlation/spacing results should not be cited as a proof of the exact three-consecutive-gap cell expansion until the required Janossy step is established.

Falsify the derived formula by constructing a strictly positive finite family with a verified

`P_N=P+N^(-2)A+O(N^(-4))`

for which the computed CMI coefficient differs from `L_P(A)`. Such a counterexample would be a calculus/bookkeeping error. Failure of the **CUE hypothesis** is different: it would mean the active joint cell law or empirical estimator does not possess the assumed even expansion, not that the first-variation identity is false.

## Research consequence

The `CLUE-zeta-three-gap-cmi-equivalent-size-eight` direction remains mathematically worth testing, but its current large-`N` `N^2 Delta` behavior is now a **non-discriminating baseline control**. The next useful evidence is not a better fit of the existing CUE curve. It is either an exact joint-spacing/Janossy transfer calculation for the frozen statistic or new high-window data showing whether the descriptive CMI-equivalent bracket moves with the independently pair-derived scale.

No new visualization is retained for this finding. The useful progress is an exact quotient on the interpretation of the existing finite-size curve; rendering that curve again would add no independent information.