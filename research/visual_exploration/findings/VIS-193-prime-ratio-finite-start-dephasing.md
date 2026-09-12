# VIS-193 — prime-ratio spacing gives a uniform finite-start dephasing window

## Claim

Keep the notation and hypotheses of `VIS-192`. Thus `0 <= alpha < 1/2`,

`a_p=p^(-alpha)`, `Q_y=sum_(p<=y) a_p^2`,

`v in C^2([0,1])` is real-valued with `v(0)=v(1)=0` and nonzero integral, and `M_v(y;H,T)` is the normalized tapered quadratic statistic. Write

`F_(y,H)(T)=M_v(y;H,T)-1`

and, for a finite deterministic start window,

`R_(v,L)(T0;y,H)=L^(-1) int_(T0)^(T0+L) |F_(y,H)(T)|^2 dT`.

Let `R_v(y,H)` denote the infinite-start Cesaro variance from `VIS-192`. Then for every `y>=2`, `H>0`, `L>0`, and real `T0`,

`|R_(v,L)(T0;y,H)-R_v(y,H)|`
` <= [2 pi/(L log(1+y^(-2)))] R_v(y,H)`
` <= [2 pi (y^2+1)/L] R_v(y,H)`.

The estimate is **uniform in the deterministic starting height `T0`**.

Consequently, under the `VIS-192` regime `H=H(y)->infinity`, `H<=y`,

`R_(v,L)(T0;y,H) <<_(alpha,v) (1+y^2/L)/H`

uniformly in `T0`. In particular, if `L>=C y^2` for fixed `C>0`, then

`R_(v,L)(T0;y,H) <<_(alpha,v,C) 1/H`

for every start `T0`. If moreover

`H log y/y -> 0` and `L/y^2 -> infinity`,

then uniformly in `T0`,

`R_(v,L)(T0;y,H) asymp_(alpha,v) 1/H`.

Thus the infinite Cesaro start average in `VIS-192` can be replaced by **every deterministic finite start interval whose length is asymptotically larger than `y^2`**, with a quantitative relative error. A fixed multiple of `y^2` already suffices for the same uniform `O(1/H)` mean-square cancellation.

**Evidence/status:** `LITERATURE+DERIVED + UNIFORM-IN-START FINITE-WINDOW BOUND + NO-NOVELTY-CLAIM`.

The `y^2` start-window scale is only a universal sufficient scale obtained from the worst spacing among all prime-ratio frequencies. No optimality is claimed.

## Evidence

### 1. The signed statistic is a separated finite exponential polynomial

`VIS-192` writes

`F_(y,H)(T)=2 Re S_v(y;H,T)`,

where

`S_v(y;H,T)`
` = Q_y^(-1) sum_(p<q<=y) a_p a_q kappa_v(H log(q/p)) exp(i T log(q/p))`.

Introduce the symmetric frequency set

`Lambda_y={+/- log(q/p) : p<q<=y, p,q prime}`.

Then

`F_(y,H)(T)=sum_(lambda in Lambda_y) c_lambda exp(i lambda T)`

for coefficients satisfying `c_(-lambda)=conjugate(c_lambda)`. The exact Cesaro identity of `VIS-192` is equivalently

`sum_(lambda in Lambda_y) |c_lambda|^2 = R_v(y,H)`.

The frequencies in `Lambda_y` are distinct. For positive frequencies this follows because a prime ratio `q/p` is already reduced, and a positive and negative frequency cannot coincide.

### 2. Distinct prime-ratio frequencies are separated at scale at least `y^-2`

Take distinct `lambda,mu in Lambda_y`.

If they have the same sign, after possibly changing both signs,

`lambda-mu = log(q/p)-log(s/r)=log(qr/(ps))`.

Distinctness of the frequencies implies `qr != ps`. Both products are positive integers at most `y^2`.

If they have opposite signs, then after relabeling

`lambda-mu = log(q/p)+log(s/r)=log(qs/(pr))`,

and `qs>pr` because `q>p` and `s>r`. Again numerator and denominator are distinct positive integers at most `y^2`.

Therefore in every case there are distinct positive integers `A,B<=y^2` such that

`|lambda-mu|=|log(A/B)|`.

For distinct `A,B`, taking the larger over the smaller gives

`|log(A/B)| >= log(1+y^(-2))`.

Hence the minimum frequency separation satisfies

`delta_y := min_(lambda!=mu) |lambda-mu| >= log(1+y^(-2))`.

Using `log(1+x)>=x/(1+x)` for `x>0`,

`delta_y^(-1) <= y^2+1`.

This is deliberately crude but completely uniform. It uses no conjecture about prime gaps, prime ratios, or multiplicative energy.

### 3. Montgomery–Vaughan turns frequency separation into a finite-window estimate

Montgomery and Vaughan, **Hilbert's Inequality**, *Journal of the London Mathematical Society* (2) 8 (1974), 73–82, DOI `10.1112/jlms/s2-8.1.73`, Corollary 2, prove that for a finite exponential polynomial with distinct real frequencies of minimum separation `delta`,

`int_0^L |sum_j b_j exp(i lambda_j t)|^2 dt`
` = (L + 2 pi theta delta^(-1)) sum_j |b_j|^2`,

for some real `theta` with `|theta|<=1`.

To average over `[T0,T0+L]`, translate `T=T0+t`. This only replaces each coefficient `c_lambda` by

`c_lambda exp(i lambda T0)`,

which leaves both the frequency set and every coefficient modulus unchanged. Applying the classical theorem with `delta=delta_y` gives

`|R_(v,L)(T0;y,H)-sum_lambda |c_lambda|^2|`
` <= 2 pi (L delta_y)^(-1) sum_lambda |c_lambda|^2`.

Substituting the exact coefficient mass from `VIS-192` yields

`|R_(v,L)(T0;y,H)-R_v(y,H)|`
` <= [2 pi/(L delta_y)] R_v(y,H)`
` <= [2 pi/(L log(1+y^(-2)))] R_v(y,H)`.

This proves the claim, including uniformity in `T0`.

### 4. The finite-window consequences follow directly from `VIS-192`

`VIS-192` proves, for `H->infinity` with `H<=y`,

`R_v(y,H) <<_(alpha,v) 1/H`.

Hence

`R_(v,L)(T0;y,H)`
` <= [1+2 pi(y^2+1)/L] R_v(y,H)`
` <<_(alpha,v) (1+y^2/L)/H`.

If `L>=C y^2`, this is uniformly `O_(alpha,v,C)(1/H)`.

If `L/y^2->infinity`, the relative Montgomery–Vaughan error is `o(1)`, uniformly in `T0`, so

`R_(v,L)(T0;y,H)=R_v(y,H)(1+o(1))`.

Combining with the matching lower bound of `VIS-192` when `H log y/y->0` gives the asserted uniform `Theta(1/H)` finite-window energy.

Finally, for every fixed `epsilon>0`, Chebyshev gives on every deterministic start interval

`L^(-1) meas{T in [T0,T0+L] : |M_v(y;H,T)-1|>epsilon}`
` <= epsilon^(-2) R_(v,L)(T0;y,H)`.

Thus for `L>=C y^2`,

`L^(-1) meas{...} <<_(alpha,v,C) 1/(epsilon^2 H)`

uniformly in `T0`. This is a finite-interval density statement, not a pointwise bound at an individual start.

## Prior-art audit

The quantitative separated-frequency mean-square theorem is classical. The exact source used here is H. L. Montgomery and R. C. Vaughan, **Hilbert's Inequality**, *Journal of the London Mathematical Society* (2) 8 (1974), 73–82, DOI `10.1112/jlms/s2-8.1.73`; their Theorem 2 is the real-line Hilbert inequality for separated frequencies and Corollary 2 gives the finite-interval mean-square formula used above. The paper explicitly presents the corollary as a result for almost-periodic polynomials.

This finding makes no novelty claim for Hilbert's inequality, Ingham/Wiener-type gap estimates, almost-periodic mean-square theory, or Dirichlet-polynomial mean values. `VIS-192` already identified Montgomery–Vaughan as the classical quantitative machinery relevant to replacing its infinite Cesaro average by a finite interval.

The Mathia-specific derivation is the specialization to the symmetric prime-ratio spectrum `+/-log(q/p)`: unique factorization and the integer-product representation give the explicit uniform spacing lower bound `delta_y>=log(1+y^-2)`, and therefore the concrete deterministic start-window scale `L>>y^2` for the exact `VIS-192` statistic. A targeted search did not motivate any claim that this `y^2` scale or this specialization is new; it is recorded as an elementary consequence of classical separated-frequency theory.

## Boundaries

The hypotheses on `alpha`, `v`, `H`, and the normalization are exactly those of `VIS-192`. The new finite-window estimate itself is deterministic and does not require `H->infinity`; the `1/H` consequences import the corresponding assumptions from `VIS-192`.

The result controls the **mean square over each finite start interval**, uniformly in the location of that interval. It does not imply a pointwise estimate for every individual `T`, and it does not rule out exceptional starts inside each interval.

The scale `y^2` comes from the worst unweighted spacing among the entire frequency set. It may be very pessimistic because a near-collision can involve coefficients carrying negligible mass after tapering and prime weights. Improving `L>>y^2` therefore requires weighted/local frequency-spacing information, a large-sieve refinement adapted to the actual coefficient profile, or a direct count of multiplicative near-collisions; this finding supplies none of those.

No lower bound is proved showing that intervals shorter than order `y^2` fail to dephase. No new prime-gap, prime-ratio, multiplicative-energy, or zeta theorem is claimed.

Falsify the finding by locating a collision missed in `Lambda_y`, an error in the integer-product spacing reduction, a mismatch between the symmetric coefficient mass and `R_v`, or an invalid use of the Montgomery–Vaughan finite-interval theorem under translation.

## Research consequence

The effective-start frontier left by `VIS-192` now has a completely unconditional coarse answer: `L>>y^2` recovers its Cesaro variance uniformly over every deterministic starting height, and `L>=C y^2` already transfers the `O(1/H)` cancellation bound.

The remaining question is no longer whether a finite deterministic horizon can replace Cesaro averaging, but **how far below the worst-case `y^2` horizon one can go by exploiting the weighted geometry of the prime-ratio spectrum**. That is a separate natural thread: it requires information about near-collisions among `log(q/p)` frequencies relative to the actual tapered coefficient mass, not another extension of the present separated-frequency argument.
