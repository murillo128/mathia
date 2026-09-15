# VIS-232 — transition-conditioned collision controls are occupancy-degenerate

## Claim

Let `x_1,...,x_m` be any finite sequence of phase-cell labels in `{1,...,J}`. Write

`N_j = #{t : x_t=j}`

for the occupancy counts and

`S(x) = sum_(1<=a<b<=m) 1_{x_a=x_b}`

for the same-cell collision statistic used in the critical phase-cell branch.

Then

`S(x) = sum_(j=1)^J binom(N_j,2)`.

Therefore `S` is a function of the occupancy histogram alone. Any surrogate that conditions on the exact confirmation-sample occupancies `(N_j)` has

`Var(S | N_1,...,N_J)=0`.

Now define the first-order transition counts

`C_(ij) = #{1<=t<m : x_t=i, x_(t+1)=j}`,

with row sums `R_i=sum_j C_(ij)` and column sums `L_i=sum_j C_(ji)`. Then exactly

`N_i = R_i + 1_{x_m=i} = L_i + 1_{x_1=i}`.

Hence a surrogate that preserves the full transition-count matrix and an endpoint also preserves every occupancy count and therefore preserves `S` exactly. In fact, when the transition imbalance is nonzero, the transition matrix itself determines the initial and terminal states, so `S` is already fixed by the Markov type. Only in the balanced closed-path case can the common start/end state vary; then

`S = sum_i binom(R_i,2) + R_tau`,

where `tau=x_1=x_m`. All remaining variation is an endpoint choice, not interior transition rearrangement.

Thus an exact transition-count-preserving or block-reordering control is **inadmissible for testing the scalar collision statistic `S`** unless the aim is deliberately to condition the statistic away. A nondegenerate dependent null for `S` must leave the confirmation-sample occupancy histogram random — for example by fitting a parametric Markov/renewal model on independent calibration data — or else the confirmation statistic must be replaced by an order-sensitive observable not measurable from the preserved counts.

**Evidence/status:** `EXACT-DERIVED + MARKOV-TYPE/CONDITIONAL-RANDOMIZATION NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that a particular parametric Markov, renewal, higher-order, or block model is a faithful prime surrogate, that a prime-specific residual survives such a model, or that any RH consequence follows.

## 1. Collision count is exactly an occupancy functional

Every unordered pair of positions contributes to `S` precisely when both positions carry the same label. For a fixed cell `j`, there are `binom(N_j,2)` unordered pairs inside that cell. Summing over cells gives

`S = sum_j binom(N_j,2)`.

This identity is representation-independent: reordering the sequence while preserving the multiset of labels cannot change `S`. In particular, any permutation, block permutation, Euler-trail reshuffling, or other conditional randomization that leaves the confirmation histogram unchanged has a point-mass randomization distribution for `S`.

This also identifies exactly what `VIS-228`--`VIS-231` are calibrating. Their nonzero variances arise because the occupancy counts themselves remain random under the independent or Markov sampling laws. They are not measuring order sensitivity of `S` conditional on the realized occupancies.

## 2. First-order transition counts almost contain the histogram

For each state `i`, every occurrence except a possible terminal occurrence contributes one outgoing transition. Therefore

`R_i = N_i - 1_{x_m=i}`.

Similarly every occurrence except a possible initial occurrence contributes one incoming transition, so

`L_i = N_i - 1_{x_1=i}`.

Equivalently,

`R_i-L_i = 1_{x_1=i}-1_{x_m=i}`.

If the vector `(R_i-L_i)` is nonzero, it has one `+1` entry at the initial state and one `-1` entry at the terminal state. Thus the transition matrix fixes both endpoints and then fixes `N_i=R_i+1_{x_m=i}` exactly.

If all row and column sums balance, any realizing path is closed: `x_1=x_m=tau`. The transition matrix then fixes `R_i=L_i` and

`N_i=R_i+1_{i=tau}`.

Consequently

`S`
` = sum_(i!=tau) binom(R_i,2) + binom(R_tau+1,2)`
` = sum_i binom(R_i,2) + R_tau`.

So even without fixing the endpoint, a balanced Markov type can change `S` only through which state is chosen as the common endpoint. Once the endpoint is fixed, the conditional variance is exactly zero.

## 3. Model-admission consequence for the critical prime-phase clue

The accepted critical-occupancy clue asks for a dependence control that preserves enough prime-local structure to be credible without importing the critical collision conclusion. `VIS-230` and `VIS-231` show how to center and standardize `S` under a specified stationary Markov law. The present identity adds a different gate: **fitting a stochastic transition law and conditioning on the realized transition table are not interchangeable null constructions for this statistic**.

A parametric first-order Markov null with `pi,P` fixed independently of the confirmation sample generates new occupancy histograms and therefore gives a nondegenerate distribution for `S`; `VIS-230` and `VIS-231` apply directly. By contrast, a conditional Markov-type surrogate that shuffles only sequences with the same transition counts, or any block-reordering control that preserves the same label multiset, has already fixed the quantity that `S` measures.

This is not an argument against transition-preserving controls in general. It says that the statistic must retain information outside the sigma-field being conditioned on. If exact local transition structure is the scientifically required control, then an order-sensitive statistic — for example lag-weighted coincidences, direction-sensitive kernels, run/return geometry, or another functional that varies inside a Markov type — is needed instead of `S`.

## 4. Prior-art and novelty boundary

The counting objects are classical. Whittle's 1955 Markov-chain formula studies distributions of transition totals and the enumeration of realizations with fixed transition counts; P. Whittle, **Some Distribution and Moment Formulae for the Markov Chain**, *Journal of the Royal Statistical Society: Series B* 17:2 (1955), 235–242, DOI `10.1111/j.2517-6161.1955.tb00197.x`.

Modern method-of-types language identifies first-order Markov types with the balanced frequency matrix of adjacent symbol pairs; see Philippe Jacquet, Charles Knessl, and Wojciech Szpankowski, **Counting Markov Types**, *Discrete Mathematics & Theoretical Computer Science*, AofA 2010, DOI `10.46298/dmtcs.2768`.

Collision counts in classical occupancy models are likewise standard; for example Toshio Nakata, **A Poisson Approximation for an Occupancy Problem with Collisions**, *Journal of Applied Probability* 45:2 (2008), 430–439, DOI `10.1239/jap/1214950358`, studies collision counts in balls-and-bins occupancy.

The identities above are elementary finite counting consequences specialized to the Mathia phase-cell statistic. No new theorem about Markov types, conditional randomization, occupancy theory, or transition-count enumeration is claimed.

## Boundaries and falsification

The result concerns the scalar unordered-pair collision statistic `S`. It does not say that all phase-cell observables are occupancy-only; statistics retaining lags, order, direction, or kernel weights can vary strongly inside a fixed histogram or Markov type.

Preserving transition *probabilities* or parameters is also different from preserving the realized transition-count matrix. An independently fitted stochastic model leaves confirmation counts random and is not covered by the degeneracy statement.

For a balanced transition table with unspecified common endpoint, `S` need not be literally constant across all realizations; the exact residual freedom is the endpoint term `R_tau` derived above. Any stronger claim of complete degeneracy in that case would be false unless the endpoint is fixed or all admissible `R_tau` coincide.

Falsify the finding by producing a sequence with the same occupancy vector but a different `S`, violating `N_i=R_i+1_{x_m=i}`, or producing two endpoint-matched realizations of the same transition-count matrix with different occupancy vectors.

## Research consequence

The model-admission gate in `CLUE-prime-phase-critical-logarithmic-occupancy` can now exclude a tempting but circular control family. Do not evaluate `S` against a confirmation-sample surrogate that preserves the exact occupancy histogram, and do not use exact transition-count-preserving randomization as a stronger dependence control for `S`: it conditions away the statistic.

The live critical test should therefore choose between two genuinely different routes. Either estimate a stochastic dependence model from independent calibration information and let confirmation occupancies fluctuate under that model, carrying parameter uncertainty into the `VIS-230`/`VIS-231` standardization; or preserve stronger realized local structure and switch to an order-sensitive statistic that remains nondegenerate inside the corresponding conditional class.