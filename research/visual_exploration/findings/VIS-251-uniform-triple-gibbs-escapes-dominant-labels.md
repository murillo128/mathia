# VIS-251 — uniform triple Gibbs updates switch a dominant coordinate label at exact rate `2/m`

## Claim

Continue the exact three-coordinate heat-bath kernel of `VIS-249` on a regular log-product level

`S_lambda={x_i>0 : sum_i x_i=1, sum_i log x_i=lambda}`,

with `m>=3`, and specialize the random scan to the uniform distribution on unordered coordinate triples.

For a state `x`, let `j` be a coordinate satisfying the strict dominance condition

`x_j > 3 max_(k!=j) x_k`.

Then `j` is the unique global maximizer. After one exact Gibbs update,

`P(argmax X'_i != j | X=x) = 2/m`.

More precisely, for every fixed `k!=j`,

`P(argmax X'_i = k | X=x) = 2/[m(m-1)]`,

while

`P(argmax X'_i = j | X=x) = 1-2/m`.

These probabilities are exact and contain no dependence on `lambda`, the selected block sum, or the selected block product.

Thus the strongly dominant-coordinate region does **not** create a `lambda`-dependent metastable barrier merely through the identity of the dominant label. Any increasingly slow high-dimensional calibration in this regime must come from different geometry: within-label continuous motion, narrow block fibers, conductance elsewhere on the level, numerical distortion, or another collective coordinate.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE BOTTLENECK CONTROL + CLASSICAL GIBBS/EXCHANGEABILITY SPECIALIZATION + NO-NOVELTY-CLAIM`.

No spectral gap, conductance bound, mixing-time estimate, Harris recurrence statement, prime residual, or RH consequence is claimed.

## 1. A triple not containing the dominant label cannot replace it

Put

`M=max_(k!=j) x_k`,

so the hypothesis is `x_j>3M`.

Suppose the selected unordered triple `B` does not contain `j`. Its total mass satisfies

`s_B=sum_(i in B) x_i <= 3M < x_j`.

An exact heat-bath update preserves this block sum. Every updated coordinate in `B` is positive and at most `s_B`, hence remains strictly below `x_j`. Coordinates outside `B` are unchanged. Therefore a triple excluding `j` leaves `j` as the global maximizer with probability one.

This conclusion uses only block-sum preservation; it is independent of the conditional density along the block fiber.

## 2. A triple containing the dominant label transfers the maximum uniformly among its three labels

Now suppose `B={j,a,b}` contains `j`. Its preserved block sum obeys

`s_B=x_j+x_a+x_b > x_j`.

For any positive updated triple with this sum, its largest coordinate is at least `s_B/3`, so

`max_(i in B) X'_i >= s_B/3 > x_j/3 > M`.

Every coordinate outside `B` is unchanged and is at most `M`. Hence the global maximum after the update lies inside the selected triple.

`VIS-249` gives the exact labeled block conditional. Away from the repeated-root endpoints, which have zero conditional mass on every nondegenerate block fiber, the unordered three roots are assigned to the three selected labels with all six permutations equally likely. Consequently the largest updated root is assigned to each member of `B` with probability exactly `1/3`.

The selected block cannot be the degenerate equal-block case `p=1/27`: the current normalized coordinate corresponding to `j` is strictly larger than each of the other two, because `x_j>3M`. Thus the continuous nondegenerate conditional applies.

Conditional on choosing a triple containing `j`, the dominant label therefore stays `j` with probability `1/3` and changes to one of the other two labels with total probability `2/3`.

## 3. Uniform triple selection gives the exact `2/m` law

Among the `binom(m,3)` unordered triples, exactly `binom(m-1,2)` contain `j`. Therefore

`P(j in B)=binom(m-1,2)/binom(m,3)=3/m`.

Combining the two cases above,

`P(argmax X'_i != j | X=x)`
` = P(j in B) P(argmax X'_i != j | j in B,X=x)`
` = (3/m)(2/3)`
` = 2/m`.

For a specified `k!=j`, there are `m-2` triples containing both `j` and `k`, so

`P({j,k} subset B)=(m-2)/binom(m,3)=6/[m(m-1)]`.

Given such a triple, the largest updated root lands on `k` with probability `1/3`. Hence

`P(argmax X'_i=k | X=x)=2/[m(m-1)]`.

Summing over the `m-1` possible new labels recovers `2/m`.

## 4. What the calculation removes and what it leaves open

The result removes one visually natural but misleading bottleneck story. On very uneven log-product levels, the state can look like one dominant coordinate plus a cloud of small coordinates, suggesting `m` deep vertex-like lobes separated by rare label changes. Inside the explicit dominance region

`D_j={x in S_lambda : x_j>3 max_(k!=j)x_k}`,

the exact chain does not acquire any additional `lambda` penalty for changing which coordinate is largest. Under uniform triple scanning, the one-step label-switch probability is fixed at `2/m` everywhere in `D_j`.

This does **not** imply rapid mixing. A chain may change the identity of its largest coordinate while retaining nearly all other slow information. The sizes and logarithmic shares of the small coordinates, motion near discriminant endpoints of individual block fibers, or other global functions may still evolve on much longer scales. `VIS-250` supplies irreducibility, not a quantitative rate, and this finding removes only one candidate source of that rate.

For nonuniform fixed triple-selection probabilities `w_B`, the same argument gives a state-independent label-switch probability

`(2/3) sum_(B contains j) w_B`

on `D_j`. The exact `2/m` value is the uniform-scan specialization used by the frozen numerical qualification design.

## 5. Prior art and novelty boundary

The heat-bath/Gibbs principle, conditional exchangeability under symmetric coordinates, and random-scan mixtures are classical. `VIS-249` already records Luke Tierney, **Markov Chains for Exploring Posterior Distributions**, *The Annals of Statistics* 22:4 (1994), 1701–1762, DOI `10.1214/aos/1176325750`, as the general MCMC prior-art boundary.

No new general Gibbs or Markov-chain theorem is claimed here. The durable content is the elementary Mathia-specific specialization obtained by combining the exact `VIS-249` three-root conditional with a dominance cone: it converts an apparent vertex-label metastability mechanism into the explicit transition probability `2/m` and shows that this particular obstruction cannot worsen with the conditioned log-product level.

## Boundaries and falsification

The strict condition `x_j>3 max_(k!=j)x_k` is sufficient, not claimed necessary. The factor `3` comes from the three-coordinate block size and the worst-case inequality `max(X'_B)>=s_B/3`.

The exact formula assumes uniform selection of unordered triples and the exact symmetric labeled heat-bath conditional of `VIS-249`. State-dependent scan probabilities, asymmetric labeling, approximate root reconstruction, clipping, projection, or another numerical block rule require a separate transition calculation.

This finding says nothing about how often the stationary chain visits `D_j`, how long it remains there, or whether another statistic has a small conductance cut. It cannot be used as evidence that the chain has a useful spectral gap or practical burn-in.

Falsify the claim by exhibiting, under the exact `VIS-249` kernel and uniform triple selection, a state in `D_j` for which a triple excluding `j` can produce a larger coordinate than `x_j`, a triple containing `j` can leave the updated global maximum outside the block, or the largest conditional root is not uniformly assigned among the three labels.

## Research consequence

The accepted critical-logarithmic-occupancy question still requires quantitative sampler qualification before any prime residual is examined. This result sharpens the diagnosis of a failure: on strongly dominant configurations, a slow chain cannot be explained simply by a `lambda`-dependent reluctance to move the dominant label between coordinate vertices.

High-dimensional convergence diagnostics should therefore include continuous within-level observables, not merely the identity of the largest gap. In particular, apparent motion among coordinate labels is not evidence that the full `bar T`-relevant geometry has mixed; the remaining risk is quantitative motion inside and between the continuous shapes that share those labels.
