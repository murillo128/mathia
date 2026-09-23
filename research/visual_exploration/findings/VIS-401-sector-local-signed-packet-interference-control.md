# VIS-401 — sector-local signed packet interference remains exactly calibratable after energy formation

## Claim

Continue in the generic rank-one qutrit setting of `VIS-388`--`VIS-400`, with positive commutator-Laplacian support

`0 < q_1 < q_2 < q_3`

and normalized positive sector weights `W=(W_1,W_2,W_3)`.

Allow the fixed-budget exclusive packet mechanism of `VIS-399`--`VIS-400` to use **signed coherent packet amplitudes before energy formation** rather than positive additive energies.

Fix `N>=1`. Each packet chooses exactly one sector `Z_n in {1,2,3}` independently with probabilities `p_i>0`, `sum_i p_i=1`. Conditional on `Z_n=i`, give it an independent real amplitude

`X_n | (Z_n=i) ~ f_i(x) dx`, `x in R`,

where `f_i` is fixed independently of the candidate residual. For each sector define the coherent signed sum and its energy

`S_i = sum_(n:Z_n=i) X_n`,

`Y_i = S_i^2`,

and normalize

`W_i = Y_i/(Y_1+Y_2+Y_3)`

whenever the total energy is positive.

Let `K_i=#{n:Z_n=i}`. Conditional on a count vector `K=k`, the occupied sector sums are independent and have densities

`F_(i,k_i)=f_i^{*k_i}`.

Therefore, for `k_i>=1`, the sector energy `Y_i=S_i^2` has the exact positive density

`h_(i,k_i)(y)=[F_(i,k_i)(sqrt(y))+F_(i,k_i)(-sqrt(y))]/[2 sqrt(y)]`, `y>0`.

For a full-occupancy component, the normalized qutrit weight vector has exact simplex density

`g_k(w)=integral_0^infinity t^2 prod_(i=1)^3 h_(i,k_i)(t w_i) dt`.

Count vectors with empty sectors give the corresponding lower-dimensional face laws with radial Jacobian `t^(r-1)` on an `r`-sector active face. Averaging over the multinomial count vector gives a finite exact mixed simplex law. Conditioning further on the qutrit first moment

`m_1=sum_i q_i w_i=x`

again gives an exactly specified one-dimensional residual law along the affine slice `w(u)` from `VIS-389`.

Thus **signed packet amplitudes and coherent cancellation inside each independently allocated sector do not by themselves create an uncontrolled Wang residual**. After squaring the sector-local coherent sums, the mechanism reduces to a count-dependent family of positive sector-energy densities followed by the same radial normalization used in `VIS-400`.

If additionally each signed packet amplitude is centered with finite second moment

`nu_i=E[X_n^2 | Z_n=i]`,

then the raw sector energies retain the exact fixed-budget negative covariance

`Cov(Y_i,Y_j)=-N p_i p_j nu_i nu_j`, `i!=j`.

The remaining genuinely different interference mechanisms must therefore involve more than independent signed summation inside disjoint sectors: for example a latent amplitude shared coherently across sectors, cross-sector phase/amplitude coupling, packet interactions that destroy conditional independence given counts, or another mechanism whose energy vector cannot be reduced to conditionally independent positive sector totals.

**Evidence/status:** `EXACT-DERIVED + SIGNED/COHERENT SECTOR-LOCAL CONTROL + CLASSICAL CHANGE-OF-VARIABLES/COMPOSITIONAL PRIOR ART + NEGATIVE CALIBRATION + NO-NOVELTY-CLAIM FOR THE PROBABILITY TRANSFORMATION`.

No Wang anomaly, arithmetic source signal, destination gain, zeta-zero statement, or RH consequence is claimed.

## 1. Conditional signed sums remain independent across sectors

The count vector `K` is multinomial. Fix `K=k` and one assignment pattern with those counts. Sector `i` receives `k_i` independent signed amplitudes with density `f_i`, so

`S_i=sum_(j=1)^(k_i) X_(ij)`

has density `F_(i,k_i)=f_i^{*k_i}` for `k_i>=1`; for `k_i=0`, `S_i=0` identically.

Different sectors use disjoint packets, hence their signed sums are independent conditional on the assignment pattern. Their joint law depends on that pattern only through the counts, so averaging over all assignment patterns with the same `k` preserves the product law

`prod_(i:k_i>0) F_(i,k_i)(s_i)`.

Interference has therefore changed the sector-total distribution, but it has not created cross-sector dependence after conditioning on counts.

## 2. Squaring converts coherent sector sums to ordinary positive totals

For an occupied sector, the map `s -> y=s^2` has two inverse branches. The standard pushforward gives

`h_(i,k_i)(y)=[F_(i,k_i)(sqrt(y))+F_(i,k_i)(-sqrt(y))]/[2 sqrt(y)]`, `y>0`.

This formula does not require `f_i` to be symmetric or Gaussian. It records all within-sector constructive/destructive interference in a positive energy density determined completely by the pre-specified signed amplitude law and the count `k_i`.

Conditional on `K=k`, the positive energies `Y_i` remain independent because each is a measurable function of the corresponding independent `S_i`. The full-occupancy joint density is therefore

`prod_i h_(i,k_i)(y_i)`.

Using `y_i=t w_i`, `t>0`, `w_i>0`, `sum_i w_i=1`, with Jacobian `t^2`, gives

`g_k(w)=integral_0^infinity t^2 prod_i h_(i,k_i)(t w_i) dt`.

This is exactly the same radial normalization principle as `VIS-400`; the only change is that the positive sector-total density now comes from convolution in signed amplitude space followed by squaring, rather than convolution of positive packet energies.

## 3. Empty sectors and fixed-`m_1` qutrit calibration remain explicit

If only `r` sectors are occupied, the identical argument on that simplex face uses radial Jacobian `t^(r-1)`. One occupied sector gives a vertex atom. The unconditional law is therefore the finite multinomial mixture of interior and face components.

For fixed generic qutrit support and interior first moment `x`, the affine constraint

`sum_i q_i w_i=x`

cuts the simplex in the same segment used from `VIS-389` onward. On each full-dimensional component,

`p(u | x,k) proportional_to g_k(w(u))`,

because the line Jacobian is constant. Face intersections contribute the corresponding exact atoms or lower-dimensional pieces. A probability-integral transform, randomized when atoms are present, therefore calibrates the residual exactly once `N`, `p_i`, and the signed amplitude laws `f_i` are fixed independently.

Exact specification does not imply an elementary closed form. Convolution, the square pushforward, the radial integral, or the final CDF may require deterministic numerical evaluation. That computational cost does not introduce a free residual-fitting parameter.

## 4. Centered signed packets preserve the fixed-budget negative covariance

Assume now `E[X|Z=i]=0` and `nu_i=E[X^2|Z=i]<infinity`. Conditional on `K_i=k_i`, cross terms vanish and

`E[Y_i | K_i=k_i]=E[S_i^2 | K_i=k_i]=k_i nu_i`.

For `i!=j`, `Y_i` and `Y_j` are conditionally independent given the full count vector, hence

`Cov(Y_i,Y_j)=Cov(E[Y_i|K],E[Y_j|K])`.

Using the multinomial identity

`Cov(K_i,K_j)=-N p_i p_j`

gives

`Cov(Y_i,Y_j)=-N p_i p_j nu_i nu_j`.

So even visible cancellation inside sectors does not remove the distribution-free negative dependence produced by exclusive allocation when the signed packet law is centered. With nonzero signed means, the simple covariance formula changes because `E[S_i^2|K_i]` contains a quadratic count term, but the exact conditional simplex calibration above remains valid.

## 5. Consequence for the Wang localization clue

`VIS-400` left signed/interfering latent contributions before energy formation as a candidate mechanism outside the positive-packet control. The present result separates two cases.

**Sector-local coherent interference is not a new escape.** If packets are still exclusively assigned and independent across sectors, arbitrary pre-specified signed amplitude laws merely induce count-dependent positive sector-energy densities `h_(i,k_i)`, after which the normalized weight and qutrit residual laws are exactly calibrated by radial integration.

A genuinely new interference null must therefore change the dependence architecture, not merely the sign of local packet amplitudes. Examples include one signed latent entering several sectors before squaring, cross-sector phase locking, interacting packet amplitudes, or another coherent construction for which the sector energies remain coupled after conditioning on the packet counts.

## Prior-art and novelty audit

The probability transformations used here are classical: convolution of independent real variables, the two-branch pushforward under `s -> s^2`, and normalization of an independent positive vector onto the simplex. The compositional/simplex prior-art anchors already recorded in `SOURCES.md` for `VIS-400`—Aitchison (1982) and Rayens--Srinivasan (1994)—bound any claim of novelty for the normalized-vector law.

No new theorem about convolutions, squared random variables, Liouville/compositional distributions, or multinomial allocation is claimed. The Mathia-specific content is the falsification boundary for the Wang qutrit route: merely allowing signs and within-sector coherent cancellation does not create an uncalibrated residual when the signed packet mechanism is independently specified.

## Boundaries

- The packet budget `N` is finite and fixed independently of the candidate residual.
- Packets choose exactly one sector independently with fixed probabilities `p_i`.
- Conditional on sector choice, packet amplitudes are independent real random variables with fixed absolutely continuous densities `f_i`.
- Signed amplitudes may interfere arbitrarily through their sector-local sum before squaring; there is no coherent sharing across sectors.
- Exact residual calibration does not require centered amplitudes. Centering and finite second moment are needed only for the displayed negative-covariance formula.
- The amplitude laws, count law, assignment probabilities, and any numerical evaluation procedure may not be tuned using the candidate residual being judged.
- The result does not cover shared signed latent amplitudes entering several sectors before squaring, cross-sector phases, packet interactions, arbitrary copulas, infinite-budget scaling limits, or Wang-admissibility constraints tied to arithmetic source data.
- No retained visualization is required because the useful result is a representation-independent probability decomposition once the qutrit reduction is fixed.
