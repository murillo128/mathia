# VIS-229 — nonuniform categorical cell collisions have an exact third-moment variance correction

## Claim

Let `X_1,...,X_m` be independent samples from a categorical law on cells `1,...,J` with probabilities `p_1,...,p_J`, and let

`n_j = #{a : X_a=j}`,

`S = sum_j binom(n_j,2)`

be the number of unordered same-cell pairs. Define the power sums

`q_2 = sum_j p_j^2`,

`q_3 = sum_j p_j^3`.

Then the exact finite-sample mean and variance are

`E[S] = binom(m,2) q_2`,

and

`Var(S) = binom(m,2)(q_2-q_2^2) + 6 binom(m,3)(q_3-q_2^2)`.

Moreover

`q_3-q_2^2 = Var(p_X) >= 0`,

where `X` has the categorical law `(p_j)`. Equality holds exactly when all positive-probability cells have the same probability. Thus nonuniform one-point occupancy changes not only the collision mean but also the collision fluctuation scale through the third power sum.

The corresponding exact independent-categorical standardization is therefore

`Z_p = [S-binom(m,2)q_2] / sqrt[binom(m,2)(q_2-q_2^2)+6binom(m,3)(q_3-q_2^2)]`,

whenever the denominator is nonzero.

For the uniform law `p_j=1/J`, one has `q_2=1/J` and `q_3=q_2^2=1/J^2`, so the shared-pair covariance term vanishes and the formula reduces exactly to the uniform variance in `VIS-228`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL U-STATISTIC/OCCUPANCY SPECIALIZATION + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that prime phase-cell occupancies are independent, that any particular nonuniform law is the correct prime null, or that a standardized critical residual is nonzero.

## 1. Pair-indicator derivation

For every unordered sample pair `a<b`, define

`I_ab = 1_{X_a=X_b}`.

Then

`S = sum_(a<b) I_ab`.

For one pair,

`E[I_ab]=q_2`,

so

`Var(I_ab)=q_2-q_2^2`.

Two indicators from disjoint sample pairs are independent. If two distinct indicators share one sample index, for example `I_ab` and `I_ac`, then

`E[I_ab I_ac] = P(X_a=X_b=X_c)=q_3`,

and therefore

`Cov(I_ab,I_ac)=q_3-q_2^2`.

Every three-element subset of the sample contributes exactly three unordered pairs of pair-indicators sharing one vertex. Hence there are

`3 binom(m,3)`

such covariance pairs. Expanding the variance of the sum counts each covariance twice, giving

`Var(S)`
` = binom(m,2)(q_2-q_2^2)`
`   + 2 * 3 binom(m,3)(q_3-q_2^2)`.

This is the stated formula.

## 2. The extra variance is exactly one-point heterogeneity

If `X` is sampled from `(p_j)`, then the random variable `p_X` takes value `p_j` with probability `p_j`. Thus

`E[p_X]=sum_j p_j^2=q_2`,

and

`E[p_X^2]=sum_j p_j^3=q_3`.

Therefore

`q_3-q_2^2 = Var(p_X)`.

The extra covariance term is consequently not evidence of pair dependence: it already appears under independent sampling whenever the one-point cell probabilities are unequal. It vanishes for a uniform law because conditioning on one endpoint of a collision does not then change the collision probability of another pair sharing that endpoint.

If the cell probabilities satisfy `p_j asy 1/J` and `m/J -> rho>0`, then `q_2=Theta(1/J)` and `q_3-q_2^2=O(1/J^2)`. Both terms in the exact variance are at most order `J`, while the first term is already `Theta(J)`. Thus the critical independent-categorical fluctuation scale remains square-root extensive, but its constant is profile-dependent and cannot in general be replaced by the uniform constant.

## 3. Consequence for the critical prime-phase occupancy clue

`VIS-228` showed that subtracting only the deterministic balanced floor is inadequate even for uniform random allocation. The present identity gives the next exact control boundary.

If a critical prime-phase test admits a nonuniform independent one-point null with probabilities `(p_j)`, then the appropriate pair-collision center is

`binom(m,2) q_2`,

and the appropriate exact variance contains both `q_2` and `q_3`. A z-score centered or scaled with the uniform formulas can therefore create an apparent residual solely from one-point heterogeneity.

This does not settle the prime problem. A logarithmic-gap-preserving or other structurally matched control will generally introduce dependence between cell labels, at which point additional covariance terms beyond the categorical formula are real and must be calibrated rather than folded into `q_2,q_3`.

If `(p_j)` is estimated from data rather than fixed analytically or from an independent calibration sample, uncertainty in the estimated null also belongs in the confirmation analysis. Plugging the same observed occupancies into the null and then treating the resulting `Z_p` as having the fixed-`p` distribution would reuse the data and understate uncertainty.

## Prior art and novelty boundary

The statistic

`U = S / binom(m,2)`

is the degree-two U-statistic with symmetric kernel `h(x,y)=1_{x=y}` and target `E[h(X_1,X_2)]=q_2`. Hoeffding's classical U-statistic framework therefore already contains this collision estimator and its finite-sample variance decomposition in general form: Wassily Hoeffding, **A Class of Statistics with Asymptotically Normal Distribution**, *Annals of Mathematical Statistics* 19:3 (1948), 293–325, DOI `10.1214/aoms/1177730196`.

No new probability theorem is claimed. The exact indicator calculation above is retained because it exposes the specific `q_3-q_2^2` term that the active prime-phase control must account for and shows directly why the uniform-null variance in `VIS-228` is exceptional.

## Boundaries and falsification

The formula assumes independent identically distributed categorical labels with fixed probabilities `(p_j)`. It does not apply unchanged to sampling without replacement, gap-preserving permutations, Markov or renewal controls, random cell probabilities, or a null estimated adaptively from the same confirmation sample.

The cell partition itself is treated as fixed. Varying the cell origin or width changes `(p_j)` and therefore changes both power sums. Representation robustness must still be checked separately under the Visual Researcher controls.

Falsify the finding by locating an error in the pair-indicator representation, the shared-index covariance `q_3-q_2^2`, the count `3 binom(m,3)` of overlapping indicator pairs, or the reduction to `VIS-228` under uniform probabilities.

## Research consequence

The active critical pair-collision clue should no longer use the uniform z-score except as the first toy null. Its independent nonuniform baseline is exactly determined by `q_2` and `q_3`. Any prime-specific claim must survive this one-point calibration and then survive a stronger dependent control that preserves the admitted logarithmic-gap structure.

If the residual disappears already at the independent nonuniform stage, pair collisions are not a useful critical discriminator. If it survives, the next question is whether the excess is due to genuine dependence beyond the one-point law and whether that dependence couples with the prime-phase kernel strongly enough to affect the critical Hamiltonian.