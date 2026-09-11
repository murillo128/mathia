# VIS-152 — fixed-dimensional Gram lag grids have a deterministic finite-difference Haar threshold

## Claim

Let `g_k` be the Gram points, with `theta(g_k)=pi k` up to the usual harmless indexing shift, and let

`z_k=(p^(-i g_k))_p in Omega`,

where `Omega` is the infinite prime torus. Fix an integer `r>=1`. Let `h=h(N)` be a positive integer with

`h=o(N)`,

put

`M_N=N-rh+1`,

and for `N<=k<=2N-rh` define the joint lag vector

`V_(k,h)^(r)=(Delta_(k,h),Delta_(k,2h),...,Delta_(k,rh)) in Omega^r`,

where

`Delta_(k,ell)=z_(k+ell) overline(z_k)`.

Then the deterministic Gram clock has a sharp fixed-dimensional scale, away from the critical boundary.

If

`M_N h^r / (N^r (log N)^2) -> infinity`,

then

`(1/M_N) sum_(k=N)^(2N-rh) delta_(V_(k,h)^(r))`

converges weakly to Haar measure on `Omega^r`.

Since `h=o(N)` gives `M_N~N`, a sufficient and equivalent form in this regime is

`h^r / (N^(r-1) (log N)^2) -> infinity`,

or heuristically

`h >> N^(1-1/r) (log N)^(2/r)`.

Conversely, if

`h^r / (N^(r-1) (log N)^2) -> 0`,

then the joint empirical law cannot converge to Haar. For every fixed prime `p`, the explicit product character

`Psi_(p,r)(omega_1,...,omega_r)`
` = product_(j=1)^r omega_j(p)^((-1)^(r-j) binom(r,j))`

has empirical average of modulus tending to one. It is exactly the character that converts the lag tuple into the `r`-th forward finite difference of the inverse Gram clock.

Thus fixed-dimensional joint lag geometry does not create a new arithmetic source merely because single-lag marginals are already Haar. The deepest character cancellation available in an `r`-lag equally spaced delay vector is a deterministic order-`r` finite-difference clock filter, and its transition scale is

`N^(1-1/r) (log N)^(2/r)`.

For `r=1` this recovers the `log^2 N` single-lag transition of `VIS-150`--`VIS-151`. For `r=2` the first genuinely joint cancellation character has threshold `sqrt(N) log N`; for `r=3` it has threshold `N^(2/3) (log N)^(2/3)`. The exponents approach one as the fixed delay dimension grows.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-GRAM-ASYMPTOTIC + FINITE-DIFFERENCE/FOURIER CONTROL + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No statement is made at the critical scale where the normalized order-`r` clock shear stays bounded away from both zero and infinity. No growing-delay-dimension, growing-prime-support, nonconsecutive-sampling, zeta-value/zero-coordinate, stochastic-mixing, or RH conclusion is claimed.

## 1. A joint torus character is a finite linear filter of exact Gram lags

A fixed character of `Omega^r` is specified by finitely supported integers `m_(j,p)` and has the form

`Chi(V)=product_(j=1)^r product_p V_j(p)^(m_(j,p))`.

For each lag coordinate define

`a_j=sum_p m_(j,p) log p`.

Unique factorization implies `a_j=0` if and only if all the integers `m_(j,p)` in that lag coordinate vanish. Hence a nontrivial product character gives a nonzero vector `(a_1,...,a_r)`.

Along the Gram lag vector,

`Chi(V_(k,h)^(r))`
` = exp(-i F_h(k))`,

where

`F_h(x)=sum_(j=1)^r a_j [g(x+jh)-g(x)]`

and `g(x)` is the smooth eventual inverse of `theta(g(x))=pi x`.

For `q=1,...,r`, set

`S_q=sum_(j=1)^r a_j j^q`.

The Vandermonde matrix `(j^q)_(1<=q,j<=r)` is invertible. Therefore every nontrivial character has a first nonzero moment

`q_0=min{q in {1,...,r}: S_q!=0}`.

This integer is the exact clock-cancellation order of the character. The single-lag argument of `VIS-151` is the case `q_0=1`; genuinely joint characters can cancel that first moment and expose a higher finite difference of the same deterministic clock.

## 2. The first surviving lag moment controls the character shear

The classical Riemann--Siegel theta asymptotic and fixed-order differentiation of its inverse imply, for every fixed `m>=2`, uniformly on a dyadic index interval,

`g^(m)(x) asymp_m x^(1-m) (log x)^(-2)`

with the eventual alternating sign supplied by the leading inverse-Gram term. Only the scale and eventual nonvanishing are needed here; `VIS-087` records the corresponding fixed-order inverse-clock hierarchy, while `VIS-151` gives explicitly

`g''(x) asymp -1/[x (log x)^2]`,
`g'''(x) asymp 1/[x^2 (log x)^2]`.

Because `h=o(N)` and `r` is fixed, Taylor expansion of `g'` is uniform for `x in [N,2N-rh]`. Using the vanishing of `S_1,...,S_(q_0-1)` gives

`F_h'(x)`
` = [S_(q_0)/q_0!] h^(q_0) g^(q_0+1)(x) (1+o(1))`.

Hence

`|F_h'(x)| asymp_Chi h^(q_0)/[N^(q_0) (log N)^2]`

uniformly over the whole sample block. Differentiating once more gives the same expansion with `g^(q_0+2)`, so `F_h'` has one sign and is monotone for all sufficiently large `N`.

Since `h=o(N)`, this derivative tends to zero. After dividing by `2 pi`, its distance from the nearest integer is therefore its absolute value. The classical first-derivative/Kusmin--Landau estimate yields

`|sum_(k=N)^(2N-rh) exp(-i F_h(k))|`
` <<_Chi N^(q_0) (log N)^2 / h^(q_0)`.

After division by `M_N`, the character average tends to zero whenever

`M_N h^(q_0) / [N^(q_0) (log N)^2] -> infinity`.

## 3. The order-r condition kills every fixed nontrivial character

Assume

`M_N h^r / [N^r (log N)^2] -> infinity`.

For a character whose first surviving moment is `q_0<=r`,

`[M_N h^(q_0)/(N^(q_0)(log N)^2)]`
` = [M_N h^r/(N^r(log N)^2)] (N/h)^(r-q_0)`.

The first factor diverges by hypothesis and the second is at least one, diverging when `q_0<r` because `h=o(N)`. Thus every nontrivial fixed product character has vanishing empirical average.

The trivial character remains one. The compact-group Fourier criterion therefore gives weak convergence of the joint empirical measures to Haar measure on `Omega^r`.

This is stronger than saying that each lag marginal is Haar: it controls every fixed cross-lag character, including the cancellation combinations that `VIS-151` explicitly left open.

## 4. An explicit order-r character proves the subcritical obstruction

Fix a prime `p` and choose the lag-coordinate exponents

`c_j=(-1)^(r-j) binom(r,j)`, `j=1,...,r`.

Then

`sum_(j=1)^r c_j [g(x+jh)-g(x)] = Delta_h^r g(x)`,

where `Delta_h^r` is the ordinary `r`-th forward finite difference. The missing `j=0` binomial term is supplied exactly by subtracting `g(x) sum_j c_j` inside the lag differences.

Therefore

`Psi_(p,r)(V_(k,h)^(r))`
` = exp(-i log(p) Delta_h^r g(k))`.

The integral form of a finite difference, or the same fixed-order Taylor estimate, gives

`|(Delta_h^r g)'(x)|`
` = |Delta_h^r g'(x)|`
` asymp_r h^r/[N^r (log N)^2]`

uniformly on the block. Consequently the total phase variation across all `M_N~N` starting indices is

`O_r(h^r/[N^(r-1)(log N)^2])`.

If this tends to zero, all values of the explicit character differ by `o(1)` from one common unimodular phase. Its normalized empirical average therefore has modulus tending to one, whereas Haar measure would give Fourier coefficient zero. Joint Haar convergence is impossible.

This proves that the order-`r` scale is not merely an artifact of the sufficient exponential-sum estimate: below it an explicit deterministic clock character survives.

## 5. Interpretation: delay dimension buys clock-cancellation order, not a new source

The first two cases make the geometry transparent.

For `r=1`, the only lag phase is `D_h(x)=g(x+h)-g(x)`. Its variation is controlled by `g''`, giving the `log^2 N` transition already isolated by `VIS-150` and extended across the well-sampled range by `VIS-151`.

For `r=2`, the character

`Delta_(k,2h)(p) / Delta_(k,h)(p)^2`

has phase

`-log(p) [g_(k+2h)-2g_(k+h)+g_k]`.

The first-order lag motion cancels exactly. What remains is the second finite difference of the same inverse Gram clock. Its variation across a dyadic block becomes order one only near

`h~sqrt(N) log N`.

Thus a two-lag plot can appear to retain coherent joint structure long after each lag marginal has individually entered its clock-generated Haar regime. That coherence is still deterministic sampling geometry, not evidence of arithmetic dependence.

The same mechanism iterates. An `r`-lag delay vector permits characters annihilating the first `r-1` lag moments, so the final deterministic obstruction is the order-`r` finite difference. Increasing a fixed delay dimension simply pushes the sampling-clock transition closer to linear scale.

## 6. Prior art and novelty audit

The mathematical ingredients are classical: the Riemann--Siegel theta/Gram asymptotics, finite-difference identities, the Vandermonde moment test, the first-derivative exponential-sum estimate, and the Fourier criterion for Haar convergence on compact tori.

Richard P. Brent, *On the Accuracy of Asymptotic Approximations to the Log-Gamma and Riemann-Siegel Theta Functions*, Journal of the Australian Mathematical Society 107:3 (2019), 319--337, DOI `10.1017/S1446788718000393`, provides rigorous theta-asymptotic error control supporting the fixed-order differentiated clock estimates already used in this line.

Antanas Laurinčikas, *Joint Discrete Approximation of Analytic Functions by Shifts of the Riemann Zeta-Function Twisted by Gram Points*, Mathematics 11 (2023), 565, DOI `10.3390/math11030565`, is established joint Gram-point weak-distribution/universality prior art. It confirms that joint weak laws under Gram sampling are classical territory, but its joint shifts are not the fixed equal-step lag-delay character calculation above.

A targeted search around Gram-point finite differences, joint lag increments, delay vectors, and discrete universality did not provide a basis for claiming this threshold theorem as new literature. **No novelty is claimed.** The durable Mathia contribution is the control interpretation and the explicit sharp scale separating deterministic finite-difference coherence from joint clock-generated Haar behavior.

## Boundary and falsification

The theorem fixes `r` while `N->infinity` and assumes `h=o(N)`. It is not uniform in delay dimension. Sending `r=r(N)` to infinity would require uniform control of inverse-clock derivatives, Vandermonde conditioning, character complexity, and the exponential-sum constants.

The critical regime

`h^r / [N^(r-1)(log N)^2] -> lambda in (0,infinity)`

is deliberately left open here. The explicit order-`r` character then has order-one deterministic clock variation and should be analyzed as its own finite-difference sampling law rather than called arithmetic residual structure.

The result concerns equally spaced consecutive Gram lag vectors. Irregular lag sets, nonconsecutive Gram indices, growing prime/Fourier support, or extra analytic coordinates may have different nulls and require separate proofs.

Falsify the claim by exhibiting a nontrivial product character whose lag-moment order exceeds `r`, breaking the fixed-order inverse-Gram derivative scale or monotonicity used above, or invalidating the first-derivative cancellation bound in the stated regime.

## Visual consequence

No canonical PNG is retained. A two- or three-lag delay embedding would make the nested transition visually attractive, but the theorem already shows that the apparent persistence and later loss of joint coherence are generated by finite differences of the deterministic Gram clock. A finite rendering would add illustration rather than evidence.

## Research consequence

The accepted `CLUE-zeta-prime-phase-recursive-geometry` should no longer treat a fixed finite equal-step delay embedding as an automatic escape from the single-lag null. For each fixed delay dimension `r`, there is a corresponding deterministic order-`r` clock obstruction below `N^(1-1/r)(log N)^(2/r)` and joint clock-generated Haar behavior above it, away from the critical boundary.

A surviving consecutive-order route must therefore either analyze a genuinely informative critical finite-difference residual after its clock null is explicit, let delay/prime/Fourier complexity grow with quantitative uniformity, use irregular or nonconsecutive sampling with a derived null, or introduce an independently anchored analytic source such as zeta/zero data not determined by the prime phases and Gram clock.