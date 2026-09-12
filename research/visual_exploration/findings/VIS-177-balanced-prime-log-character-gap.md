# VIS-177 — balanced prime-log characters halve the elementary moment-transfer exponent

## Claim

Keep the notation of `VIS-174`. Let `P_y` be any finite set of primes `p<=y`, let `w_p>0`, and write

`W_y = sum_(p in P_y) w_p`,

`Q_y = sum_(p in P_y) w_p^2`,

`D_2(y)=W_y^2/Q_y`,

and

`S_y(t)=Q_y^(-1/2) sum_(p in P_y) w_p [sin^2(t log p/2)-1/2]`.

For every fixed integer `k>=1`, every nonzero Fourier character appearing in the expansion of `S_y(t)^k` has frequency

`lambda = log(a/b)`

with `a!=b` and

`|lambda| >= 1/(2 y^floor(k/2))`.

Consequently, uniformly in the interval start `T`,

`| H^(-1) int_T^(T+H) S_y(t)^k dt - E[(S_y^Haar)^k] |`
` <= 2^(2-k) y^floor(k/2) D_2(y)^(k/2) / H`.

This improves the elementary factor `y^k` in `VIS-174` to `y^floor(k/2)` without any Diophantine theorem: the improvement comes only from balancing the positive and negative multiplicities of a near-resonant character.

As a direct corollary, the Gaussian full-law conclusion of `VIS-176` for prime-power weights

`w_p=p^(-alpha)`, `0<=alpha<=1/2`,

holds for every growing cutoff satisfying

`y(H)=H^o(1)`,

not merely for fixed polylogarithmic cutoffs. Thus the entire subpolynomial continuous-support regime remains inside the representation-matched Gaussian null in the Lindeberg phase.

**Evidence/status:** `EXACT-DERIVED + ELEMENTARY FREQUENCY-SEPARATION SHARPENING + GROWING-CUTOFF NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This is not an optimal quantitative Kronecker theorem, a polynomial-support theorem, a discrete/Gram sampling theorem, a rare-event theorem, or an RH consequence.

## 1. Every character splits into two multiplicative sides

Write

`sin^2(t log p/2)-1/2 = -(1/2) cos(t log p)`.

A Fourier character in a product of `k` cosine factors has frequency

`lambda = sum_(j=1)^k epsilon_j log p_j`, `epsilon_j in {+1,-1}`.

Cancel equal prime factors occurring with opposite signs and collect the survivors. Then

`lambda=log(a/b)`,

where `a` is a product of `r` surviving prime factors, `b` is a product of `s` surviving prime factors, repetitions allowed, and

`r+s<=k`.

Unique factorization gives `lambda=0` exactly when no factor survives. For a nonzero character, `a!=b`.

The key point missed by the cruder `VIS-174` bound is that a small logarithmic ratio requires the two multiplicative sides to have comparable size. One cannot simultaneously exploit all `k` factors in the denominator of a near-resonance.

## 2. Near resonance forces the denominator onto the smaller side

Assume without loss of generality that `a>b` and put

`m=floor(k/2)`.

If `a>=2b`, then

`lambda=log(a/b)>=log 2 >= 1/(2 y^m)`.

Otherwise

`b<a<2b`.

Since `a` is a product of `r` primes at most `y`,

`a<=y^r`,

and therefore `b<a<=y^r`. Independently,

`b<=y^s`.

Hence

`b<=y^min(r,s)`.

But

`min(r,s) <= floor((r+s)/2) <= floor(k/2)=m`,

so

`b<=y^m`.

Because `a` and `b` are distinct integers,

`a>=b+1`,

and therefore

`lambda=log(a/b)`
` >= log(1+1/b)`
` >= 1/(b+1)`
` >= 1/(2 y^m)`.

The same bound holds after swapping `a,b` when `b>a`. Thus every nonzero `k`-character obeys

`|lambda| >= 1/(2 y^floor(k/2))`.

For `k=2`, this recovers the natural `1/y` scale of `log(p/q)` rather than the old `1/y^2` bound. For `k=4`, the worst elementary near-resonance is already of two-products-versus-two-products type, giving the `1/y^2` scale.

## 3. The moment-transfer estimate inherits the balanced exponent

For any nonzero frequency and any interval `[T,T+H]`,

`| H^(-1) int_T^(T+H) exp(i lambda t) dt |`
` <= min(1, 2/(H|lambda|))`
` <= 4 y^floor(k/2)/H`.

As in `VIS-174`, Haar expectation and deterministic time averaging agree exactly on resonant characters. Only nonresonant characters contribute to the difference.

The absolute coefficient mass of the `k`th-power expansion remains

`W_y^k/(2^k Q_y^(k/2))`
` = 2^(-k) D_2(y)^(k/2)`.

Multiplying by the improved nonresonant character bound gives

`| time_k - Haar_k |`
` <= 2^(2-k) y^floor(k/2) D_2(y)^(k/2)/H`.

Nothing else in the `VIS-174` resonance argument changes. The old theorem remains correct; this finding identifies and removes a purely elementary overpayment in its uniform frequency-separation step.

## 4. Subpolynomial support is already Gaussian in the Lindeberg prime-power phase

Take all primes `p<=y` and weights

`w_p=p^(-alpha)`, `0<=alpha<=1/2`.

`VIS-176` already proves the matched Haar triangular array is asymptotically `N(0,1/8)` because

`max_(p<=y) w_p/sqrt(Q_y) -> 0`.

To transfer the `k`th deterministic moment, the strengthened condition is now

`y^floor(k/2) D_2(y)^(k/2)/H -> 0`.

Cauchy--Schwarz gives

`D_2(y)<=pi(y)<=y`.

Hence

`y^floor(k/2) D_2(y)^(k/2)/H`
` <= y^(floor(k/2)+k/2)/H`
` <= y^k/H`.

Suppose

`log y / log H -> 0`,

which is equivalent to `y=H^o(1)`. For every fixed `k`, choose any fixed `epsilon<1/k`. Eventually `y<=H^epsilon`, so

`y^k/H <= H^(epsilon k-1) -> 0`.

Thus every fixed deterministic moment still transfers to the Gaussian Haar limit throughout arbitrary subpolynomial support growth.

The tightness, uniform-integrability, moment-determinacy, and Frechet--Shohat passage in `VIS-176` then apply unchanged. Therefore, uniformly in interval start, the complete bounded-continuous vertical law converges to

`N(0,1/8)`

for every `0<=alpha<=1/2` and every cutoff `y(H)->infinity` with `y(H)=H^o(1)`.

This closes a substantially larger support class than the fixed-polylogarithmic example originally recorded in `VIS-176`.

## 5. Prior-art and novelty boundary

No external theorem is needed for the new frequency bound. It is an elementary consequence of unique factorization, integer separation, and the observation that a near-resonant ratio must be bounded simultaneously by the multiplicative sizes of both sign groups.

Quantitative Kronecker approximation, linear forms in logarithms, and small-gap questions for almost-primes address much sharper and more general frequency geometry. This finding does not claim a new theorem in those subjects, does not claim that the exponent `floor(k/2)` is optimal for prime products, and does not infer any necessary support threshold.

The Mathia-specific value is narrower: it removes an avoidable exponent loss in the exact control used by `VIS-174` and propagates that correction to the active full-law boundary in `VIS-176`.

## 6. Boundaries and falsification

The estimate is uniform over all `k`-characters generated by primes at most `y`, so it deliberately ignores arithmetic sparsity inside the set of admissible products. Better bounds or average cancellation may exist.

The moment order `k` is fixed before the limit. The result does not give uniform control as `k->infinity`. Consequently it does not by itself handle moving thresholds, shrinking targets, total variation, extreme tails, or unbounded observables.

The corollary `y=H^o(1)` is sufficient, not necessary. A fixed positive power `y=H^delta` fails the all-fixed-moment condition for sufficiently large `k` under this argument, but that does not prove the Gaussian law fails there; it only marks the boundary of this moment-transfer method.

The result concerns continuous vertical averaging. It does not apply automatically to Gram points, sparse deterministic selectors, or hybrid prime/zero observables.

Falsify the finding by producing a nonzero character for which the positive/negative factor count argument fails, an error in the bound `b<=y^min(r,s)`, or an error in propagating the strengthened character bound through the coefficient-mass and method-of-moments steps.

## Research consequence

The accepted prime-phase clue can no longer treat support growth merely beyond polylogarithmic scale as an escape from the matched continuous prime-torus null in the Lindeberg phase. Every subpolynomial cutoff remains Gaussian for the prime-power family `0<=alpha<=1/2`.

A surviving continuous additive statistic must therefore move at least to a genuinely polynomial-or-faster support regime, a stronger functional class such as rare/shrinking or unbounded observables, or a source-bearing variable outside the additive prime torus. Discrete/Gram sampling and hybrid prime/zero constructions remain separate boundaries because the present character argument does not control them.