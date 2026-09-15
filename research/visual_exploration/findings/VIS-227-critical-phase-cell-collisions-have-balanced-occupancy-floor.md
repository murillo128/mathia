# VIS-227 — critical phase-cell collisions have an exact balanced-occupancy floor

## Claim

Let `N` points be assigned to `M>=1` cells with occupancies `n_1,...,n_M`, and define the same-cell collision count

`S = sum_j binom(n_j,2)`.

Write `N=qM+r` with `0<=r<M`. Then

`S >= M binom(q,2) + rq`,

with equality exactly when every occupancy is `q` or `q+1` and exactly `r` cells have occupancy `q+1`.

Applied to the phase-coherence cells used in `VIS-225`, whose prime-coordinate width is

`ell = eta_v y/(8H)`,

let `m=pi(y)-pi(y/2)` be the number of primes in `(y/2,y]` and let `J` be the number of coherence cells meeting that interval. At the critical scale

`H=lambda y/log y`,

one has

`J = (4lambda/eta_v + o(1)) y/log y`,

while the prime number theorem gives

`m = (1/2 + o(1)) y/log y`.

Hence

`m/J -> rho_lambda = eta_v/(8lambda)`.

This already splits the critical family at a purely combinatorial level. If `lambda>eta_v/8`, then eventually `m<J`, so the exact balanced-occupancy floor is zero. If `lambda=eta_v/8`, first-order asymptotics force no positive linear floor. If `lambda<eta_v/8`, occupancy alone forces a positive linear number of same-cell pairs. In particular, when

`eta_v/16 < lambda < eta_v/8`,

one has `1<rho_lambda<2`, and therefore

`S >= m-J = (1/2 - 4lambda/eta_v + o(1)) y/log y`.

More generally, the exact finite formula above gives the piecewise-linear balanced floor for every occupancy ratio.

Therefore a positive linear raw same-cell pair count at critical scale is **not by itself an arithmetic clustering signal**. The discriminating quantity must be an excess above the exact balanced-occupancy floor, or a matched control that already fixes the same `m` and `J`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-CONVEXITY/FINITE-OCCUPANCY + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

## 1. Exact finite occupancy floor

Suppose two cells have occupancies `a>=b+2`. Moving one point from the first cell to the second changes their contribution to `S` by

`binom(a-1,2)+binom(b+1,2)-binom(a,2)-binom(b,2) = b-a+1 <= -1`.

Thus any occupancy vector with two entries differing by at least two is not minimizing. Repeating this exchange strictly lowers `S` until all occupancies differ by at most one. Since their sum is `N=qM+r`, the unique occupancy multiset at that point consists of `M-r` cells of size `q` and `r` cells of size `q+1`. Substitution gives

`S_min(N,M) = (M-r)binom(q,2) + r binom(q+1,2) = M binom(q,2)+rq`.

This is an exact finite statement; no probabilistic model or prime-distribution input enters it.

## 2. Critical phase-cell specialization

`VIS-225` partitions `(y/2,y]` into cells of prime-coordinate length `ell=eta_v y/(8H)`, up to endpoint rounding. Since the interval has length `y/2`,

`J = y/(2ell) + O(1) = 4H/eta_v + O(1)`.

At `H=lambda y/log y`, this becomes

`J = (4lambda/eta_v + o(1)) y/log y`.

The prime number theorem gives

`m = pi(y)-pi(y/2) = (1/2+o(1)) y/log y`,

so the mean occupancy tends to `rho_lambda=eta_v/(8lambda)`.

When `rho_lambda<1`, the exact finite minimum is eventually zero. When `rho_lambda>1`, the exact minimum is already linear in `y/log y`; no prime-specific clustering theorem is needed to obtain that raw collision scale. At integer transition values of `rho_lambda`, the exact finite formula remains authoritative; first-order asymptotics alone should not be used to infer lower-order collision terms.

## 3. Consequence for the critical arithmetic discriminator

The latest critical-occupancy clue treated `Theta(1)` mean occupancy as the point where coarse forcing ceases automatically. The exact minimization shows that this is too coarse: the relevant threshold is whether `m/J` lies above or below one, with further piecewise transitions as the limiting occupancy crosses larger integers.

Accordingly, a critical-scale experiment should not use raw

`S_lambda(y)=sum_j binom(n_j,2)`

as its arithmetic signal. It should first compute the exact finite baseline

`S_min(m,J)=J binom(q,2)+rq`, where `m=qJ+r`,

and study the excess `S_lambda(y)-S_min(m,J)`, or compare against controls conditioned on the same `m` and `J`. A raw positive linear collision count for `lambda<eta_v/8` is a generic consequence of fitting more points than cells, not evidence of special prime geometry.

## Evidence boundary

This finding uses only the exact occupancy minimization, the coherence-cell construction already fixed in `VIS-225`, and the prime number theorem. It establishes no prime-specific excess above the balanced floor, no critical-scale worst-start energy lower bound, no random-control asymptotic, and no RH consequence.

The result also does not say that the balanced floor is the correct stochastic baseline for every refined statistic. It only removes raw same-cell collision mass that is forced before any arithmetic ordering information is used.

## Prior-art and novelty note

The balancing argument is elementary discrete convexity / balls-in-cells mathematics, and no novelty is claimed for it. The durable contribution here is its exact specialization to the current Mathia phase-coherence representation, where it corrects the proposed critical-scale discriminator. No source-dependent theorem beyond the prime number theorem is imported; the finite minimization is proved above.