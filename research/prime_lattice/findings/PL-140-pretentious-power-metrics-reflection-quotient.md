# PL-140 — Power-enriched pretentious metrics factor through a prime-wise reflection quotient

## Claim

Let `f,g` be unitary completely multiplicative functions and write their relative prime phase as

`r_p = f(p) conjugate(g(p)) = exp(i phi_p)`.

For every positive integer `k`, the standard pretentious distance between the powers `f^k` and `g^k` is

`D(f^k,g^k;x)^2 = sum_(p<=x) (1-Re(r_p^k))/p = sum_(p<=x) (1-cos(k phi_p))/p`.

Hence **the entire hierarchy of positive power distances factors coordinatewise through `cos(phi_p)`**. For arbitrary independent signs `epsilon_p in {+1,-1}`, replace the relative phase by

`r'_p = exp(i epsilon_p phi_p)`

and define the unitary completely multiplicative function `f_epsilon` by

`f_epsilon(p)=g(p) r'_p`.

Then, simultaneously for every cutoff `x` and every positive integer `k`,

`D(f_epsilon^k,g^k;x)=D(f^k,g^k;x)`.

The same prime-wise reflection/conjugation ambiguity survives the weighted prime distance `D_beta` and the stronger prime-power distance of Jung--Lemke Oliver, because their local costs are respectively functions of `Re(r_p^j)` or `|r_p^j-1|`, both invariant under `r_p -> conjugate(r_p)`.

This is a distinct obstruction from the gcd torsion gauge in `PL-139`. There, exact observation of powers with coprime exponents recovers the original phase coordinatewise. Here the **distance-level quotient survives even when all positive powers are observed**, because the real-part/chord-magnitude projection has already discarded orientation on each prime circle.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-DELIMITED`.

The pretentious metrics and their transfer theorems are literature. The reflection quotient, Chebyshev reduction, and the tomography statements below are elementary exact consequences of those definitions. They are not claimed as new theorems. The durable line-level result is a falsification boundary: enriching a pretentious metric by positive powers does not by itself restore the oriented prime-torus information that the metric discarded.

## Exact coordinatewise reflection gauge

For unitary completely multiplicative functions the usual truncated pretentious distance is

`D(f,g;x)^2 = sum_(p<=x) (1-Re(f(p) conjugate(g(p))))/p`.

This is the weighted squared chord geometry of the relative point `(r_p)_p` on the prime torus. Passing to function powers gives

`D_k(x)^2 := D(f^k,g^k;x)^2
 = sum_(p<=x) (1-Re(r_p^k))/p`.

If `r_p=exp(i phi_p)`, then

`Re(r_p^k)=cos(k phi_p)=T_k(cos phi_p)`,

where `T_k` is the `k`th Chebyshev polynomial. Thus every local contribution at every positive power depends only on the unoriented coordinate

`c_p=cos(phi_p)`.

Choose a sign field `epsilon=(epsilon_p)_p` with `epsilon_p in {+1,-1}` independently for every prime and set

`r'_p = exp(i epsilon_p phi_p)`.

Then for all `p` and all `k>=1`,

`Re((r'_p)^k)=cos(k epsilon_p phi_p)=cos(k phi_p)=Re(r_p^k)`.

Consequently

`D(f_epsilon^k,g^k;x)^2 = D(f^k,g^k;x)^2`

for every `k` and every `x`. Away from the fixed phases `r_p=+/-1`, this is an independent `Z/2Z` ambiguity at each prime coordinate. In geometric terms, the complete positive-power distance hierarchy factors through the product of circle reflections

`T^P -> (T/{z~conjugate(z)})^P`.

This algebraic degeneracy does not depend on the arithmetic sizes of the rational primes. Replacing the prime set by a generic freely generated multiplicative frequency system leaves it intact. It is therefore a matched-control obstruction rather than a zeta-specific mechanism.

## Full cutoff data makes higher powers redundant, but still unoriented

There are two different observation regimes and they should not be conflated.

Suppose first that the entire cutoff profile `x -> D(f,g;x)^2` is known. At a prime `p`, the jump of the profile is

`Delta_p D_1^2 = (1-cos phi_p)/p`.

Therefore the first-power profile already determines

`cos phi_p = 1-p Delta_p D_1^2`

for every prime. Since

`cos(k phi_p)=T_k(cos phi_p)`,

the jump of every higher-power distance is then determined algebraically from the `k=1` profile. Thus, with prime-resolved cutoff data, **adding all positive powers supplies no further information at all beyond the first distance**. In particular, it cannot decide between `phi_p` and `-phi_p`.

At one fixed cutoff `x`, the hierarchy has a standard harmonic interpretation. Define the finite weighted measure on the unit circle

`mu_x = sum_(p<=x) p^(-1) delta_(exp(i phi_p))`

and its mass

`M_x = sum_(p<=x) 1/p`.

Then

`M_x-D_k(x)^2 = sum_(p<=x) cos(k phi_p)/p`.

These are exactly the cosine Fourier moments of `mu_x`. Knowing all `k>=0` determines the conjugation-symmetrized measure

`(mu_x + check(mu_x))/2`,

where `check(mu_x)` is the pushforward under `z -> conjugate(z)`, but not the oriented measure `mu_x` itself. This is the aggregate version of the same coordinatewise reflection quotient.

## The stronger prime-power metric is reflection-blind too

`PL-138` records the weighted prime metric and stronger prime-power metric introduced by Jung--Lemke Oliver. In the unitary completely multiplicative specialization their local data can be written in terms of the same relative phases. The weighted prime metric has the form

`D_beta(f,g)^2 = sum_p (1-Re(r_p))/p^beta`

in its convergence range, so replacing `r_p` by `conjugate(r_p)` plainly leaves it unchanged.

For the stronger depth-`d` prime-power distance, complete multiplicativity gives

`f(p^j)=f(p)^j`, `g(p^j)=g(p)^j`,

and hence

`|f(p^j)-g(p^j)| = |g(p)^j| |r_p^j-1| = |r_p^j-1|`.

Under the reflection `r_p -> conjugate(r_p)`,

`|conjugate(r_p)^j-1| = |conjugate(r_p^j-1)| = |r_p^j-1|`.

Therefore every positive weight and every finite or infinite collection of prime-power depths remains exactly reflection-blind. This does **not** weaken the Jung--Lemke Oliver transfer theorems: those results use the metric as a stability hypothesis relative to a function whose cancellation is already known. The point here is narrower. The metric itself cannot recover the missing orientation, even if one keeps adding powers.

The literature anchor is:

- Junehyuk Jung and Robert J. Lemke Oliver, “Pretentiously detecting power cancellation,” *Mathematical Proceedings of the Cambridge Philosophical Society* **154**(3) (2013), 481–498. DOI: https://doi.org/10.1017/S0305004112000655. arXiv: https://arxiv.org/abs/1111.1921.

For the standard pretentious geometry and its connection with mean-value cancellation, the baseline anchor is:

- Andrew Granville and K. Soundararajan, “Decay of Mean Values of Multiplicative Functions,” *Canadian Journal of Mathematics* **55**(6) (2003), 1191–1230. DOI: https://doi.org/10.4153/CJM-2003-047-0.

Both sources were already part of the line's prior-art ledger for `PL-137` and `PL-138`; no new literature entry is needed here.

## Why this is stronger than the PL-139 gcd obstruction

`PL-139` studies exact power observations. If only powers indexed by a finite set `K` are observed and `d=gcd(K)>1`, multiplication by an arbitrary prime-wise `d`th root of unity leaves all those exact powers unchanged. When `gcd(K)=1`, Bezout removes that torsion kernel: the exact power values determine the original unitary phase coordinatewise.

The present obstruction occurs **after** applying the pretentious real-part or chord-magnitude observable. Even when `K` contains `1`, even when `gcd(K)=1`, and even when `K=N`, the identification

`r_p ~ conjugate(r_p)`

remains. Thus the natural repair suggested by `PL-139` -- use coprime powers or all powers -- succeeds for exact phase tomography but fails for these metric observables.

The distinction is important for the prime-exponent program. A proposal that says “the first pretentious metric loses phase, so enrich it by all prime powers” has not yet escaped the quotient. It has only accumulated Chebyshev functions of the same unoriented coordinates.

## What escapes the obstruction

The no-go is deliberately not stated for all prime-torus observables. Several orientation-sensitive enrichments escape it.

First, complex rather than real-part correlations retain orientation. For example a quantity such as

`sum_(p<=x) r_p/p^beta`

is generally changed by independent prime-wise conjugation. The obstruction applies to metrics whose local data factor through `Re(r_p^j)` or `|r_p^j-1|`, not to arbitrary complex observables.

Second, the **full time profile** against the Kronecker comparator `n^(it)` is much richer than one distance or its minimizing value. Let

`A_x(t) = M_x-D(f,n^(it);x)^2
 = Re sum_(p<=x) f(p) p^(-1-it)`.

For a fixed prime `q<=x`, orthogonality of the distinct frequencies `log p` gives

`lim_(T->infinity) (1/(2T)) integral_(-T)^T A_x(t) exp(i t log q) dt = f(q)/(2q)`.

Thus retaining the entire real function `t -> A_x(t)` recovers the oriented complex coefficient `f(q)` at each prime. Independent prime-wise reflection is **not** a symmetry of that full profile. This is why the result must not be overextended to the bounded-time minimization geometry in `PL-137`, much less to all Kronecker-flow observables.

Third, if the relevant relative phases are already real, as for a `+/-1` state relative to the trivial comparator, conjugation acts trivially. Liouville or Möbius sign information therefore is not erased by this particular reflection quotient. The result is a design boundary for phase-metric mechanisms, not a direct disproof of every pretentious route to RH.

## Domain and analytic-continuation boundary

Everything above is an exact statement about finite prime sums or about the convergence region of the corresponding weighted metrics. No Euler product is analytically continued, no value of `1/zeta(s)` is inferred in the critical strip, and no assertion is made that the reflection quotient itself detects zeros.

This separation matters because the main research mandate requires a mechanism that genuinely crosses the analytic barrier rather than re-encoding facts from the absolute-convergence side. The present result is negative: it shows that one natural attempt to make the prime-torus geometry richer still remains algebraically universal before any continuation issue is reached.

## Prior-art and novelty audit

The standard pretentious distance, its Hilbert-like prime-coordinate geometry, and the use of stronger weighted/prime-power distances for transfer of cancellation are established prior art in Granville--Soundararajan and Jung--Lemke Oliver. `PL-138` already stores the latter theorem-level content, including its optimality boundary.

The identities

`Re(z^k)=T_k(Re z)` for `|z|=1`

and

`|conjugate(z)^k-1|=|z^k-1|`

make the all-power reflection quotient elementary. A targeted novelty search around pretentious power distances, power cancellation, conjugation, and Chebyshev/power observables did not locate a theorem framed as this independent prime-wise reflection quotient. That absence is **not** evidence of novelty, and no novelty is claimed. The finding is stored because the exact quotient closes a live escape from `PL-139` and materially narrows what kind of power enrichment could add zeta-specific information.

`PL-130` is a nearby but different nonidentifiability result: it concerns finite real phase fingerprints in the Grosswald--Schnitzer deformation class and arbitrary tails. `PL-133` concerns synthetic affine reflection axes for a Grosswald--Schnitzer analytic quotient. Neither is the present coordinatewise conjugation symmetry of pretentious power metrics.

## Adversarial limits and consequence for the line

Several stronger conclusions would be false. The result does not say that pretentious distances are useless; they have strong mean-value and transfer consequences. It does not say that all power-sensitive data are redundant; exact complex power values with coprime exponents recover phase, and full Kronecker time profiles recover oriented coefficients. It does not claim that orientation must be the missing ingredient in RH. Nor does it prohibit combining a reflection-blind metric with a genuinely global structure -- functional equation, explicit-formula positivity, an operator model, or target-relative data -- that supplies the missing orientation or otherwise forces critical-line localization.

The reusable boundary is exact: **positive-power enrichment does not remove the conjugation quotient of any prime-phase geometry built only from real parts or chord magnitudes**. A future metric proposal should therefore pass an orientation audit before being treated as a richer prime-lattice mechanism. If it remains invariant under independent `r_p -> conjugate(r_p)`, it has not extracted more than the unoriented cosine geometry of the prime torus and still needs an additional global, zeta-specific coupling to address RH.