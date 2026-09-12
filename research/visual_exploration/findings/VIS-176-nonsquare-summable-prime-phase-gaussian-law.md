# VIS-176 — Lindeberg prime-phase weights have a full Gaussian vertical law

## Claim

For each cutoff `y`, let `P_y` be a finite set of primes `p<=y` with positive weights `w_p`, and write

`W_y = sum_(p in P_y) w_p`,

`Q_y = sum_(p in P_y) w_p^2`,

`D_2(y)=W_y^2/Q_y`.

Define

`V(theta)=sin^2(theta/2)-1/2=-(1/2)cos(theta)`,

`S_y(t)=Q_y^(-1/2) sum_(p in P_y) w_p V(t log p)`.

Let `Theta_p` be independent Haar-uniform angles and let

`S_y^Haar=Q_y^(-1/2) sum_(p in P_y) w_p V(Theta_p)`.

Assume along a family `H->infinity`, `y=y(H)->infinity` that

`max_(p in P_y) w_p/sqrt(Q_y) -> 0`,

and, for every fixed integer `k>=1`,

`y^k D_2(y)^(k/2)/H -> 0`.

Then the empirical laws of `S_y(t)` on arbitrary intervals `[T,T+H]` converge weakly, uniformly in the starting point `T`, to

`N(0,1/8)`.

Equivalently, for every bounded continuous `F:R->R`,

`sup_T | H^(-1) int_T^(T+H) F(S_y(t)) dt - E[F(G)] | -> 0`,

where `G~N(0,1/8)`.

For the prime-power taper

`w_p=p^(-alpha)`, `p<=y`, `0<=alpha<=1/2`,

and any fixed `A>0`, the polylogarithmic cutoff

`y(H)=(log H)^A`

satisfies the hypotheses. Hence the complete bounded-continuous vertical law is Gaussian throughout the nonsquare-summable phase `0<=alpha<=1/2`.

Together with `VIS-175`, this gives a representation-matched full-law phase boundary for prime-power weights under polylogarithmic support:

- `0<=alpha<=1/2`: after quadratic normalization, the growing weighted prime-phase field has the Gaussian law `N(0,1/8)`;
- `alpha>1/2`: the square-summable field converges instead to the generally non-Gaussian infinite weighted Haar law of `VIS-175`.

Thus a visually Gaussian prime-phase bulk in the nonsquare-summable regime is no more source-sensitive than the persistent non-Gaussian low-prime law in the square-summable regime. Both are forced by the representation-matched null.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL LINDEBERG/FRECHET-SHOHAT SPECIALIZATION + GROWING-CUTOFF NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This is not a theorem about Gram-point sampling, hybrid prime/zero variables, shrinking rare events, unbounded observables, optimal support growth, or RH.

## 1. The matched Haar triangular array is asymptotically Gaussian

For one Haar phase,

`E[V(Theta)]=0`, `Var(V(Theta))=1/8`,

and `|V(Theta)|<=1/2`.

Set

`a_(y,p)=w_p/sqrt(Q_y)`.

Then

`sum_p a_(y,p)^2=1`.

The hypothesis

`max_p a_(y,p)->0`

is exactly the bounded-coordinate Lindeberg negligibility condition. Therefore the classical Lindeberg--Feller theorem gives

`S_y^Haar => N(0,1/8)`.

For the later moment argument it is useful to record the stronger fixed-order statement directly. For every `r>=3`, the `r`th cumulant of the normalized Haar sum is

`kappa_r(S_y^Haar)=kappa_r(V) sum_p w_p^r/Q_y^(r/2)`.

Since

`sum_p w_p^r <= (max_p w_p)^(r-2) Q_y`,

one has

`|kappa_r(S_y^Haar)| <= |kappa_r(V)| [max_p w_p/sqrt(Q_y)]^(r-2) -> 0`.

The first cumulant is zero and the second is exactly `1/8`. Hence every fixed Haar moment converges to the corresponding moment of `N(0,1/8)` by the ordinary moment--cumulant relations.

## 2. Every fixed deterministic moment transfers from Haar

`VIS-174` proves, uniformly in the interval start `T`, that for every fixed integer `k>=1`,

`| H^(-1) int_T^(T+H) S_y(t)^k dt - E[(S_y^Haar)^k] |`
` <= 2^(2-k) y^k D_2(y)^(k/2)/H`.

The present support/window hypothesis makes the right-hand side tend to zero for each fixed `k`.

Combining this with Section 1 gives, uniformly in `T`,

`H^(-1) int_T^(T+H) S_y(t)^k dt -> E[G^k]`

for every fixed `k`, where `G~N(0,1/8)`.

So the deterministic vertical orbit and its growing weighted Haar comparator have the same limiting moment sequence, and that sequence is Gaussian.

## 3. Moment convergence upgrades to the full weak law

Let `mu_(H,T)` be the empirical probability law of `S_y(t)` under uniform `t` on `[T,T+H]`.

The second moments converge uniformly to `1/8`, so the family `mu_(H,T)` is uniformly tight by Markov's inequality. More generally, convergence of every even moment gives uniform bounds on a higher moment than any fixed order, so powers are uniformly integrable along arbitrary sequences of starts.

Take any sequence `H_n->infinity` and any starts `T_n`. Tightness gives a weakly convergent subsequence. Uniform integrability plus the moment limits from Section 2 shows that every moment of the subsequential limit equals the corresponding Gaussian moment. The Gaussian distribution is moment-determinate, so the classical Frechet--Shohat moment theorem forces that subsequential limit to be `N(0,1/8)`.

Every possible sequence of starts has the same unique subsequential limit. Therefore convergence is uniform in `T` for the bounded-Lipschitz metric, hence for weak convergence. This proves the displayed full-law statement.

The use of moments here is not a new probability theorem. It is only the bridge that turns the existing fixed-order deterministic transfer from `VIS-174` into a complete distributional null once the matched Haar array itself is in the Lindeberg phase.

## 4. Prime-power weights `alpha<=1/2`

Take all primes `p<=y` and `w_p=p^(-alpha)` with `0<=alpha<=1/2`.

Then

`Q_y=sum_(p<=y) p^(-2alpha) -> infinity`.

At `alpha=1/2` this is the classical divergence of the reciprocal-prime sum; for smaller `alpha`, every term dominates the corresponding reciprocal-prime term beyond a fixed point. Since the largest weight is bounded independently of `y`,

`max_(p<=y) w_p/sqrt(Q_y) -> 0`.

Thus the Haar triangular array is in the Gaussian Lindeberg phase already identified abstractly in `VIS-173`.

For the deterministic transfer condition, Cauchy--Schwarz gives the universal bound

`D_2(y)=W_y^2/Q_y <= |P_y| <= y`.

Hence for each fixed `k`,

`y^k D_2(y)^(k/2)/H <= y^(3k/2)/H`.

If `y=(log H)^A` with any fixed `A>0`, then

`y^(3k/2)/H = (log H)^(3Ak/2)/H -> 0`.

Therefore every fixed moment transfers, and Section 3 gives the full Gaussian weak law for every `0<=alpha<=1/2` under any fixed polylogarithmic support exponent.

No prime-number-theorem estimate is needed for this conclusion. The crude count `|P_y|<=y` and reciprocal-prime divergence at the endpoint already suffice.

## 5. Prior art and novelty boundary

The Gaussian limit of a negligible weighted independent triangular array is classical Lindeberg--Feller theory; `VIS-173` already records this as the exact Haar shape boundary `max_p w_p/sqrt(Q_y)->0` and makes no novelty claim for the central-limit theorem.

The passage from convergence of all moments to weak convergence toward a moment-determinate law is the classical Frechet--Shohat second-limit theorem. Maurice Frechet and J. Shohat, **A Proof of the Generalized Second-Limit Theorem in the Theory of Probability**, *Transactions of the American Mathematical Society* 33:2 (1931), 533--543, is the canonical prior-art anchor.

Jessen--Wintner value-distribution theory, already anchored for `VIS-175`, is the broader classical background for almost-periodic distribution laws. The present finding does not claim a new general value-distribution theorem, central-limit theorem, or method-of-moments theorem.

The Mathia-specific content is the direct combination of three already exposed control mechanisms: the weighted Haar Lindeberg phase (`VIS-173`), the explicit growing-cutoff deterministic moment transfer (`VIS-174`), and the full-law question sharpened by `VIS-175`. Their combination closes the previously explicit nonsquare-summable prime-power boundary for ordinary bounded-continuous vertical statistics under a broad polylogarithmic cutoff.

## 6. Boundaries and falsification

The result uses continuous vertical averaging. It does not transfer automatically to Gram points, sparse deterministic selectors, short discrete blocks, or hybrid observables containing a zero/Hadamard factor.

The conclusion is weak convergence for fixed bounded continuous tests. Moving thresholds, shrinking targets, collision extremes, decoder singularities, and unbounded statistics can distinguish sequences with the same weak limit and therefore require stronger control.

The support condition is sufficient and intentionally conservative. The fixed-moment estimate in `VIS-174` pays the elementary factor `y^k`; sharper Diophantine or discrepancy estimates could allow much faster support growth.

The Lindeberg condition is essential for the Gaussian null. If a nonnegligible fraction of `Q_y` remains in finitely many large coordinates, the matched Haar law can remain non-Gaussian, exactly as `VIS-173` and `VIS-175` describe.

Falsify the finding by finding an error in the cumulant negligibility bound, the use of the `VIS-174` moment estimate, the tightness/uniform-integrability passage, or the Frechet--Shohat determinacy step.

## Research consequence

The nonsquare-summable boundary named in `VIS-175` is now closed for the ordinary additive prime-phase field under polylogarithmic continuous windows: for `p^(-alpha)` weights with `alpha<=1/2`, the full matched law Gaussianizes rather than exposing a new arithmetic source.

A surviving prime-phase visual mechanism must therefore leave more than square summability. It must exploit a genuinely different sampling regime, a rare or unbounded functional beyond weak convergence, a source-bearing hybrid/zero variable, or another observable not reducible to the same normalized additive prime torus. Crossing from non-Gaussian to Gaussian at `alpha=1/2` is a representation phase transition, not evidence for RH-facing structure.
