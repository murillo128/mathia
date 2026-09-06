# VIS-057 — adjacent-pair Markov closure is quantitatively stable under raw-law error

## Claim

Let `P` and `P_tilde` be probability laws on one fixed finite alphabet `X x Y x Z`. Assume every declared middle state has positive mass under both laws. Write

`p_j = P_Y(j)`, `p_tilde_j = P_tilde_Y(j)`,

and let the adjacent-pair-preserving first-order Markov completion be

`M(P)_(ijk) = P_XY(i,j) P_YZ(j,k) / P_Y(j)`.

Define the irreducible three-gap residual

`Delta(P) = P - M(P)`.

Use the full `L^1` distance, not the half-total-variation convention,

`delta = ||P-P_tilde||_1`.

Then the nonlinear Markov-completion map obeys the global finite-alphabet bound

`||M(P)-M(P_tilde)||_1 <= 5 delta`,

and therefore

`||Delta(P)-Delta(P_tilde)||_1 <= 6 delta`.

The constants are deliberately coarse and no sharpness is claimed. The important point is that no uniform lower bound on the middle-state probabilities is needed: although the conditional factors themselves can be badly conditioned when a middle state is rare, their contribution is multiplied by that same middle-state mass, so the completed joint law remains globally controlled in `L^1` as long as the declared middle states stay present.

Now fix one strictly positive common reference law `H` on the same finite support, as in `VIS-041`, and put

`h_min = min_(i,j,k) H_(ijk) > 0`,

`||R||_H^2 = sum_(i,j,k) R_(ijk)^2 / H_(ijk)`.

Then

`||Delta(P)-Delta(P_tilde)||_H <= 6 delta / sqrt(h_min)`.

Consequently, let `P^A,P^B` be two process laws with nonzero residuals, let `P_tilde^A,P_tilde^B` be perturbed laws on the same fixed partition/support, and keep the same common Fisher reference `H`. Set

`delta_r = ||P^r-P_tilde^r||_1`,

`E_r = ||Delta(P^r)||_H^2`,  `r in {A,B}`.

If

`eta_r = 6 delta_r / sqrt(h_min E_r) < 1`

for both processes, the perturbed residuals remain nonzero and the common-reference orientation coefficient of `VIS-041` satisfies

`|kappa_H(P_tilde^A,P_tilde^B) - kappa_H(P^A,P^B)|`
` <= min(2, 2 eta_A + 2 eta_B)`
` <= min(2, [12/sqrt(h_min)] [delta_A/sqrt(E_A) + delta_B/sqrt(E_B)]).`

Thus **raw-law error, including the error induced by recomputing each process's own nonlinear Markov closure, has an explicit deterministic path to Fisher-orientation error**. The certificate is informative exactly when the raw-law uncertainty is small relative to the surviving residual energy and the frozen common reference does not contain extremely small cells.

**Evidence/status:** `EXACT-DERIVED + FIXED-PARTITION MODEL-ERROR CONTROL + REPRESENTATION CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that the constant `5` is optimal, that overlapping empirical three-gap tables satisfy an i.i.d. concentration law, that changing the partition/support/reference `H` is covered, or that a stable residual orientation is arithmetic-specific. The result is a deterministic interface into which a separately justified process-aware error radius may later be inserted.

## 1. Marginalization contracts `L^1`

Write the `Y=j` slices of the two adjacent marginals as

`a_j(i)=P_XY(i,j)`, `b_j(k)=P_YZ(j,k)`,

and similarly `a_tilde_j,b_tilde_j`. Their common slice masses are

`||a_j||_1=||b_j||_1=p_j`,
`||a_tilde_j||_1=||b_tilde_j||_1=p_tilde_j`.

Marginalization is an `L^1` contraction, hence

`sum_j ||a_j-a_tilde_j||_1 <= delta`,
`sum_j ||b_j-b_tilde_j||_1 <= delta`,
`sum_j |p_j-p_tilde_j| <= delta`.

For each middle state define the normalized conditionals

`A_j=a_j/p_j`, `B_j=b_j/p_j`,
`A_tilde_j=a_tilde_j/p_tilde_j`, `B_tilde_j=b_tilde_j/p_tilde_j`.

The Markov-completion slice is exactly

`M(P)_j = p_j A_j tensor B_j`.

This form isolates the apparent denominator problem: the conditionals can move strongly when `p_j` is tiny, but the whole slice is weighted by `p_j`.

## 2. The Markov-completion map is `5`-Lipschitz in the coarse global bound

For one middle state, the product-law triangle inequality gives

`||p_j A_j tensor B_j - p_tilde_j A_tilde_j tensor B_tilde_j||_1`
` <= |p_j-p_tilde_j|`
`    + p_tilde_j ||A_j-A_tilde_j||_1`
`    + p_tilde_j ||B_j-B_tilde_j||_1`.

The conditional terms can be bounded without dividing the final estimate by a small middle mass. Indeed,

`p_tilde_j ||A_j-A_tilde_j||_1`
` = ||(p_tilde_j/p_j) a_j - a_tilde_j||_1`
` <= |p_tilde_j-p_j| + ||a_j-a_tilde_j||_1`,

and identically

`p_tilde_j ||B_j-B_tilde_j||_1`
` <= |p_tilde_j-p_j| + ||b_j-b_tilde_j||_1`.

Therefore

`||M(P)_j-M(P_tilde)_j||_1`
` <= ||a_j-a_tilde_j||_1`
`    + ||b_j-b_tilde_j||_1`
`    + 3 |p_j-p_tilde_j|`.

Summing over the disjoint middle-state slices and using the three contraction inequalities yields

`||M(P)-M(P_tilde)||_1 <= 5 delta`.

Finally,

`Delta(P)-Delta(P_tilde)`
` = (P-P_tilde) - (M(P)-M(P_tilde))`,

so another triangle inequality gives

`||Delta(P)-Delta(P_tilde)||_1 <= 6 delta`.

This is a global bound on the completed joint law, not a claim that the conditional kernels themselves are uniformly stable. If a middle mass tends to zero, the corresponding conditional law can become arbitrarily sensitive while its weighted contribution to `M(P)` remains small.

## 3. A fixed positive Fisher gauge converts raw-law error into residual-vector error

For any tensor `R` on the fixed support,

`||R||_H`
` <= ||R||_2 / sqrt(h_min)`
` <= ||R||_1 / sqrt(h_min)`.

Applying this to the residual difference gives

`||Delta(P)-Delta(P_tilde)||_H`
` <= 6 delta / sqrt(h_min)`.

In particular,

`||Delta(P_tilde)||_H`
` >= ||Delta(P)||_H - 6 delta/sqrt(h_min)`.

Hence `eta<1` guarantees that a nonzero reference residual cannot collapse to zero under the permitted raw-law perturbation. The same inequality also exposes the two conditioning factors that an empirical direction claim must report rather than hide: a tiny residual norm and a tiny reference cell both amplify uncertainty.

The `h_min` dependence is intentionally conservative. `VIS-045` already shows that common Fisher gauges should be audited on the actual residual subspace rather than judged only by ambient cellwise extremes when sharper control matters. The present theorem uses `h_min` only to provide an immediate deterministic certificate from raw probability error to the already frozen `H`-metric.

## 4. Normalizing the residual vectors adds only the expected relative-error penalty

Let `u` be a nonzero vector in any Hilbert space and let `u_tilde=u+e`. If `||e||<||u||`, then `u_tilde` is nonzero and

`||u/||u|| - u_tilde/||u_tilde|||| <= 2 ||e||/||u||`.

One proof is to insert `u_tilde/||u||` between the two unit vectors. The first difference has norm `||e||/||u||`; the second is

`|||u_tilde||-||u|||/||u|| <= ||e||/||u||`

by the reverse triangle inequality.

Apply this separately to the two Fisher residuals. If `u_r=Delta(P^r)` and `e_r=Delta(P_tilde^r)-Delta(P^r)`, then

`||e_r||_H/||u_r||_H <= eta_r`.

For unit vectors, the change of their inner product is at most the sum of the two unit-vector changes. Therefore

`|kappa_tilde-kappa| <= 2 eta_A+2 eta_B`.

Since both coefficients lie in `[-1,1]`, the absolute change is also at most `2`, giving the stated capped certificate.

This step controls the exact direction statistic from `VIS-041`; it does not replace the separate gauge-change theorem in `VIS-045`. Here the gauge is held fixed while the two underlying process laws, their adjacent marginals, their Markov completions, and therefore their residual vectors move. `VIS-045` instead holds the residual vectors fixed and changes the common metric. The two controls cover different axes of the empirical representation.

## 5. Prior art and novelty boundary

The factorization

`M(P)(x,y,z)=P_Y(y) P_(X|Y)(x|y) P_(Z|Y)(z|y)`

and its role as the adjacent-pair-preserving conditional-independence completion are classical; `VIS-020` already records the corresponding conditional-mutual-information and maximum-entropy interpretation with Cover and Thomas as the standard information-theory anchor.

A targeted audit also finds Steffen Lauritzen, **Total variation convergence preserves conditional independence**, *Statistics & Probability Letters* 214 (2024), 110200, DOI `10.1016/j.spl.2024.110200`. Lauritzen proves the qualitative closure statement that conditional independence is preserved under total-variation limits. That is neighboring prior art for the topology used here, but it is not the quantitative statement being applied: the present argument directly compares the particular finite-alphabet completion `M(P)` and `M(P_tilde)` and records one explicit coarse global constant.

No novelty is claimed for total variation, marginal contraction, product-measure perturbation inequalities, conditional independence, Hilbert-space normalization bounds, or Fisher cosine geometry. The durable Mathia-specific content is the assembled **error interface for the already active three-gap residual experiment**: raw-law uncertainty may be propagated through recomputed lower-order closure all the way to the signed common-reference residual orientation without pretending that the closure is a fixed linear operator.

The search did not identify a reason to promote the numerical constant `5` itself as a new theorem. It should be treated as an auditable sufficient bound; any sharper standard inequality can replace it later without changing the research consequence.

## 6. Boundary conditions and falsification

The partition and declared support are fixed. Both compared laws must have positive mass on every declared middle state so that the displayed conditional factors are defined. Full three-dimensional cell positivity is not required for `P` or `P_tilde`; zeros are allowed there. The common Fisher reference `H`, however, must remain strictly positive on the declared support.

Changing bin edges, deleting sparse cells differently between processes, changing which states are admitted, or recomputing the common reference `H` is not raw-law perturbation under this theorem. Those operations change the representation itself and require separate controls. `VIS-045` handles bounded changes of the common positive gauge only when the residual tensors are held fixed; combining simultaneous gauge and residual motion requires composing the two bounds explicitly rather than attributing everything to `delta`.

The bound also supplies no sampling theorem. The three-gap tables in the live zeta/CUE experiment are built from overlapping triples, so an i.i.d. multinomial confidence radius must not be inserted automatically. A valid `delta_r` must come from a process-aware argument, independent windows, a justified resampling scheme, or another source appropriate to the actual data-generating process.

The certificate becomes vacuous when `E_r` is too small relative to raw-law uncertainty or when `h_min` is too small. That is a genuine conditioning warning: a normalized direction is not a stable object when the vector being normalized is near zero, and a Fisher metric strongly magnifies cells assigned vanishing reference mass.

Falsify the exact result by producing two finite laws satisfying the stated positive-middle-mass assumptions for which the `5 delta` completion bound or `6 delta` residual bound fails; by finding a fixed positive `H` that violates the Fisher-norm conversion; or by giving nonzero residuals satisfying `eta_A,eta_B<1` whose normalized common-reference orientation exceeds the displayed perturbation bound. Such a counterexample would invalidate the certificate directly rather than merely weaken its empirical usefulness.

## Research consequence

The current Fisher branch no longer needs to treat “recompute each process's Markov closure under data error” as an unquantified model-error category. On one frozen partition, support rule, and common positive reference, any separately justified raw-law `L^1` radius now gives a deterministic residual-vector radius and hence an explicit orientation-error budget.

For the accepted higher-window three-gap transfer test, this means the direction-sensitive comparison can be pre-registered with three distinct diagnostics instead of one vague robustness claim: the process-aware raw-law radius `delta_r`, the surviving Fisher residual energy `E_r`, and the common-reference floor/conditioning through `h_min` (or a later sharper subspace certificate). Only when the resulting orientation interval remains informative should a measured zeta/CUE alignment or opposition be interpreted as a stable geometric comparison.

This does **not** unblock the missing higher-window data, identify the correct finite-CUE scale, or establish an arithmetic residual. It closes one coherent deterministic model-error gap left by `VIS-041`, `VIS-045`, and `VIS-056`. The next independent step is empirical: obtain or justify the new-window inputs and a process-aware raw-law uncertainty radius, then test whether the scalar CMI bracket and signed residual orientation survive together. That step belongs to a later invocation.