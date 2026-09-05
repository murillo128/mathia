# VIS-035 — conditional correspondence-analysis modes are principal-inertia/maximal-correlation modes

## Claim

Use the fully supported three-gap setup of `VIS-020` through `VIS-025`. Let `X,Y,Z` be the three consecutive binned gaps, and for a fixed middle state `j` write

`p_j=P(Y=j)`,
`R_j(i,k)=P(X=i,Z=k | Y=j)`,
`a_j(i)=P(X=i | Y=j)`,
`b_j(k)=P(Z=k | Y=j)`.

Define

`T_j = D_(a_j)^(-1/2) R_j D_(b_j)^(-1/2)`

and the centered correspondence-analysis matrix

`S_j = D_(a_j)^(-1/2) (R_j-a_j b_j^T) D_(b_j)^(-1/2)`.

Then `T_j` has the trivial singular pair

`sqrt(a_j), sqrt(b_j)`

with singular value `1`, and `S_j` is exactly `T_j` with that marginal rank-one component removed. Hence the singular values of `S_j` are the nontrivial singular values of the normalized joint table `T_j`.

Write them

`rho_(j,1) >= ... >= rho_(j,s-1) >= 0`.

These are the square roots of the classical principal inertia components of the conditional table `R_j`; in particular,

`rho_(j,1) = rho_HGR(X;Z | Y=j)`,

the Hirschfeld-Gebelein-Renyi maximal correlation of the first and third gap bins inside the fixed middle-gap fiber.

The Pearson-weighted residual from `VIS-024`/`VIS-025` is

`W_j = sqrt(p_j) S_j`,

so its singular values satisfy exactly

`sigma_l(W_j) = sqrt(p_j) rho_(j,l)`.

Consequently the complete Pearson interaction energy has the exact principal-inertia decomposition

`chi_P^2`
` = sum_(i,j,k) (P_ijk-Q_ijk)^2 / Q_ijk`
` = sum_j ||W_j||_F^2`
` = sum_j p_j sum_(l=1)^(s-1) rho_(j,l)^2`
` <= s-1`,

where `Q_ijk=P_12(i,j)P_23(j,k)/P_2(j)` is the adjacent-pair-preserving Markov closure. The last bound follows from `0<=rho_(j,l)<=1` and `sum_j p_j=1`.

Finally, because `I(X;Z|Y)=D(P||Q)`, Jensen's inequality gives the exact control

`I(X;Z|Y) <= log(1+chi_P^2)`
`            <= log s`.

Thus the CA singular spectrum is not merely a coordinate-invariant visualization of the three-gap residual. Fiber by fiber it is the classical spectrum of optimal nonlinear correlations between functions of the two outer gap bins, and its squared weighted spectrum is exactly the global Pearson divergence from first-order Markov closure.

**Evidence/status:** `CLASSICAL-PRINCIPAL-INERTIA/MAXIMAL-CORRELATION + EXACT-DERIVED CONDITIONAL SPECIALIZATION + REPRESENTATION CONTROL + NO-NOVELTY-CLAIM`.

No zeta-specific higher-order dependence, arithmetic signal, asymptotic law, or RH implication is claimed.

## 1. Removing the marginal singular direction

Put

`alpha_j=sqrt(a_j)`, `beta_j=sqrt(b_j)`

entrywise. Since `R_j` has row marginal `a_j` and column marginal `b_j`,

`T_j beta_j`
` = D_(a_j)^(-1/2) R_j 1`
` = D_(a_j)^(-1/2) a_j`
` = alpha_j`.

Likewise

`alpha_j^T T_j = beta_j^T`.

Both `alpha_j` and `beta_j` have Euclidean norm one, so they form a left/right singular pair of `T_j` with singular value `1`.

Moreover,

`D_(a_j)^(-1/2) a_j b_j^T D_(b_j)^(-1/2)`
` = alpha_j beta_j^T`,

and therefore

`S_j = T_j-alpha_j beta_j^T`.

The marginal constraints from `VIS-024` become

`S_j beta_j=0`, `alpha_j^T S_j=0`.

Hence `S_j` is precisely the restriction of `T_j` to the orthogonal complements of the two trivial marginal directions. Its singular values are the nontrivial singular values of `T_j`.

This is the same interaction quotient described geometrically in `VIS-025`, now interpreted through the classical principal-inertia decomposition of a joint distribution.

## 2. Maximal correlation interpretation

For finite random variables with joint law `R_j`, the Hirschfeld-Gebelein-Renyi maximal correlation is

`rho_HGR(X;Z | Y=j)`
` = sup E[f(X)g(Z) | Y=j]`,

where the supremum is over real functions with conditional means zero and conditional variances one.

The classical singular-value characterization says that this supremum is the largest nontrivial singular value of

`D_(a_j)^(-1/2) R_j D_(b_j)^(-1/2)`.

Therefore

`rho_HGR(X;Z | Y=j)=rho_(j,1)`.

If `u_(j,l),v_(j,l)` are corresponding unit singular vectors of `S_j`, the associated score functions can be written

`f_(j,l)(i)=u_(j,l)(i)/sqrt(a_j(i))`,
`g_(j,l)(k)=v_(j,l)(k)/sqrt(b_j(k))`.

They have zero conditional means and unit conditional variances, and

`E[f_(j,l)(X) g_(j,l)(Z) | Y=j] = rho_(j,l)`.

Thus a visually dominant rank-one CA mode has an exact statistical meaning: after conditioning on the middle-gap bin, it is the strongest possible correlation between arbitrary standardized functions of the two outer gap bins. The remaining singular values are successive orthogonal principal-inertia modes.

This removes another possible over-interpretation. A striking low-rank residual pattern is not automatically a new geometric invariant; it may simply be the standard maximal-correlation mode of an ordinary dependent conditional table.

## 3. Exact global Pearson decomposition and bound

`VIS-025` gives

`W_j=sqrt(p_j)S_j`.

Therefore

`||W_j||_F^2`
` = p_j ||S_j||_F^2`
` = p_j sum_l rho_(j,l)^2`.

Summing over middle states yields

`sum_j ||W_j||_F^2`
` = sum_j p_j sum_l rho_(j,l)^2`.

On the other hand, because

`P_ijk=p_j R_j(i,k)`,
`Q_ijk=p_j a_j(i)b_j(k)`,

one has directly

`sum_(i,k) (P_ijk-Q_ijk)^2/Q_ijk`
` = p_j sum_(i,k) [R_j(i,k)-a_j(i)b_j(k)]^2/[a_j(i)b_j(k)]`
` = ||W_j||_F^2`.

Hence the summed CA inertia is exactly the Pearson chi-square divergence `chi_P^2=chi^2(P||Q)` from the fitted first-order Markov closure.

Every nontrivial singular value of a normalized joint-distribution matrix lies in `[0,1]`. There are at most `s-1` of them in each `s x s` fiber, so

`chi_P^2`
` = sum_j p_j sum_l rho_(j,l)^2`
` <= sum_j p_j (s-1)`
` = s-1`.

Thus `chi_P^2/(s-1)` is a bounded `[0,1]` normalization of the complete Pearson interaction strength for a fixed `s`-bin design. This normalization introduces no new information; it is only a scale control for comparing visual interaction spectra under the same partition size.

For unequal outer alphabets the identical argument replaces `s-1` by `min(s_X-1,s_Z-1)`.

## 4. Relation to conditional mutual information

`VIS-020` established

`I(X;Z|Y)=D(P||Q)`.

For any `P,Q` with common support,

`D(P||Q)`
` = E_P[log(P/Q)]`
` <= log E_P[P/Q]`
` = log sum P^2/Q`
` = log(1+chi^2(P||Q))`,

where the inequality is Jensen applied to the concave logarithm.

Specializing to the Markov closure gives

`I(X;Z|Y)`
` <= log(1+sum_j p_j sum_l rho_(j,l)^2)`
` <= log s`.

The first inequality can be substantially sharper than the alphabet-only bound when the Pearson/CA spectrum is weak. It also clarifies the relation between the exact nonlinear CMI statistic and the visual singular spectrum: the latter is not equal to CMI away from the local regime of `VIS-024`, but it gives an exact chi-square envelope for it.

Conversely, a large Pearson singular mode does not by itself imply a zeta-specific CMI excess. The same spectrum must be compared with the matched finite-size CUE/arithmetic process under the identical binning and estimation rule.

## 5. Prior art and novelty assessment

The identification is classical rather than a new correspondence-analysis or dependence theorem.

Flavio P. Calmon, Ali Makhdoumi, Muriel Medard, Mayank Varia, Mark M. Christiansen, and Ken R. Duffy, **Principal Inertia Components and Applications**, *IEEE Transactions on Information Theory* 63:8 (2017), 5011–5038, DOI `10.1109/TIT.2017.2700857`, develops principal inertia components for discrete random variables and their relation to maximal correlation and optimal estimation.

Hsiang Hsu, Salman Salamatian, and Flavio P. Calmon, **Correspondence Analysis Using Neural Networks**, *Proceedings of AISTATS 2019*, PMLR 89, 2671–2680, explicitly connects correspondence analysis with the principal-inertia functional optimization viewpoint. The correspondence-analysis side is also already anchored in `SOURCES.md` through Greenacre and the standard chi-square/SVD formulation used in `VIS-025`.

The Mathia-specific content is the exact conditional specialization to the active three-gap Markov fiber: the visual singular values in `VIS-025` are not merely convenient invariant coordinates but weighted conditional principal-inertia/maximal-correlation modes, and their full squared spectrum is exactly the Pearson divergence from the adjacent-pair-preserving closure.

No novelty is claimed for HGR maximal correlation, principal inertia components, correspondence analysis, the chi-square bound, or `D<=log(1+chi^2)`.

## 6. Boundary conditions and falsification

The displayed matrices assume full support so that all inverse square roots are finite. With structural or sampling zeros the decomposition must be restricted to the actual positive support, and both the interaction dimension and the simple `s-1` bound can tighten. Deleting sparse bins after inspecting zeta data would violate the fixed-partition control.

The `rho_(j,l)` are invariant to relabeling bins and orthogonal contrast choices, but they are not invariant to changing bin boundaries, unfolding, height window, estimator, or conditioning scheme. A stable spectral shape across those perturbations is an empirical question, not a consequence of principal-inertia theory.

The per-fiber quantity `rho_HGR(X;Z | Y=j)` should not be confused with every possible global definition of conditional maximal correlation in which the optimizing functions may themselves vary with `Y`. This finding uses only the exact fixed-fiber interpretation needed by the conditional correspondence-analysis decomposition.

Most importantly, nonzero maximal correlation is expected in generic higher-order dependent point processes, including matched random-matrix controls. It is evidence against first-order Markov closure for the binned sequence, not evidence for arithmetic specificity.

## Research consequence

The live clue `CLUE-zeta-three-gap-conditional-residual` can treat the CA singular spectrum from `VIS-025` as a classical principal-inertia spectrum rather than as a newly invented visual descriptor. In each fixed middle-gap fiber, the leading normalized singular value is HGR maximal correlation; the remaining values are orthogonal dependence modes; and the aggregate squared spectrum is the Pearson interaction divergence.

A future zeta-versus-CUE test should therefore compare these quantities under exactly the same partition, unfolding, support rule, and windowing, alongside the exact nonlinear CMI/LRT statistic from `VIS-023`. A reproducible zeta-specific claim would have to be a **difference from the matched control spectrum**, not merely a visually strong singular mode or a large maximal correlation in the zeta data alone.
