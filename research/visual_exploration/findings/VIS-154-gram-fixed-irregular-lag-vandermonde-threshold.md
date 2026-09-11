# VIS-154 — fixed irregular Gram lag sets have the same Vandermonde clock threshold

## Claim

Let `g_k` be the Gram points and

`z_k=(p^(-i g_k))_p in Omega`,

where `Omega` is the infinite prime torus. Fix an integer `r>=1` and distinct positive integers

`1 <= b_1 < ... < b_r`.

Let `h=h(N)` be a positive integer with `b_r h=o(N)`, put

`M_N=N-b_r h+1`,

and for `N<=k<=2N-b_r h` define the irregular fixed-ratio lag vector

`V_(k,h,b)=(Delta_(k,b_1 h),...,Delta_(k,b_r h)) in Omega^r`,

where

`Delta_(k,ell)=z_(k+ell) overline(z_k)`.

Then the same deterministic inverse-Gram clock threshold found for the equal-step grid in `VIS-152` persists for every fixed distinct integer lag geometry.

If

`M_N h^r / [N^r (log N)^2] -> infinity`,

then

`(1/M_N) sum_(k=N)^(2N-b_r h) delta_(V_(k,h,b))`

converges weakly to Haar measure on `Omega^r`.

Since the `b_j` are fixed and `b_r h=o(N)`, this is equivalent in the present regime to

`h^r / [N^(r-1) (log N)^2] -> infinity`.

Conversely, if

`h^r / [N^(r-1) (log N)^2] -> 0`,

then the joint empirical law cannot converge to Haar. There is an explicit nontrivial fixed-prime product character whose first `r-1` lag moments vanish and whose empirical average has modulus tending to one.

Thus replacing consecutive equal-step delays by a fixed finite irregular set of commensurate delays does not create a new arithmetic information source. The node geometry changes the integer cancellation character and constants, but not the maximal cancellation order `r` or the threshold exponent

`N^(1-1/r) (log N)^(2/r)`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-GRAM-ASYMPTOTIC + VANDERMONDE/FOURIER CONTROL + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No statement is made at the critical scale, for lag ratios changing with `N`, growing delay dimension, noncommensurate real-time sampling, selected/nonconsecutive Gram subsequences, growing prime/Fourier support, zeta-value/zero-derived coordinates, stochastic mixing, or RH.

## 1. Every fixed joint character has a finite lag-moment order at most r

A fixed character of `Omega^r` is specified by finitely supported integers `m_(j,p)` and has the form

`Chi(omega_1,...,omega_r)=product_(j=1)^r product_p omega_j(p)^(m_(j,p))`.

For each lag coordinate set

`a_j=sum_p m_(j,p) log p`.

Unique factorization implies that `a_j=0` exactly when all exponents in the `j`-th lag coordinate vanish. Hence a nontrivial character gives a nonzero vector `(a_1,...,a_r)`.

Along the irregular lag vector,

`Chi(V_(k,h,b))=exp(-i F_h(k))`,

where

`F_h(x)=sum_(j=1)^r a_j [g(x+b_j h)-g(x)]`

and `g(x)` is the smooth eventual inverse of `theta(g(x))=pi x`.

Define the lag moments

`S_q=sum_(j=1)^r a_j b_j^q`, `q=1,...,r`.

The matrix `(b_j^q)_(1<=q,j<=r)` has determinant

`(product_j b_j) product_(i<j)(b_j-b_i)`,

which is nonzero because the `b_j` are positive and distinct. Therefore every nontrivial character has a first nonzero moment

`q_0=min{q in {1,...,r}: S_q!=0}`.

This is the irregular-node analogue of the equal-step Vandermonde step in `VIS-152`: a fixed `r`-coordinate lag vector can cancel at most the first `r-1` powers of the sampling clock.

## 2. The first surviving moment gives the same clock-shear scale

Differentiate the phase. Uniformly for `x` in the dyadic sample interval, fixed `b_j`, and `h=o(N)`, Taylor expansion gives

`F_h'(x)`
` = [S_(q_0)/q_0!] h^(q_0) g^(q_0+1)(x) (1+o(1))`.

The classical Riemann--Siegel theta asymptotic and fixed-order differentiation of its inverse give, for fixed `m>=2`,

`g^(m)(x) asymp_m x^(1-m) (log x)^(-2)`

with eventual nonvanishing and alternating sign. These are exactly the inverse-clock estimates already used in `VIS-087`, `VIS-151`, and `VIS-152`; fixed irregular nodes alter only the finite coefficients `S_q`.

Consequently

`|F_h'(x)| asymp_Chi,b h^(q_0)/[N^(q_0)(log N)^2]`

uniformly on the block, and the leading term also gives the eventual one-sign/monotonicity needed for the same first-derivative exponential-sum estimate as in `VIS-152`. Hence

`|sum_(k=N)^(2N-b_r h) exp(-iF_h(k))|`
` <<_(Chi,b) N^(q_0)(log N)^2 / h^(q_0)`.

After division by `M_N`, the character average tends to zero whenever

`M_N h^(q_0)/[N^(q_0)(log N)^2] -> infinity`.

Assume the order-`r` condition

`M_N h^r/[N^r(log N)^2] -> infinity`.

For every `q_0<=r`,

`M_N h^(q_0)/[N^(q_0)(log N)^2]`
` = [M_N h^r/(N^r(log N)^2)] (N/h)^(r-q_0)`.

The first factor diverges, and the second is at least one and diverges when `q_0<r`. Thus every nontrivial fixed character vanishes asymptotically. The compact-group Fourier criterion yields Haar convergence on `Omega^r`.

## 3. Lagrange weights give an explicit order-r obstruction for every irregular node set

The converse needs an integer character that kills the first `r-1` moments for arbitrary fixed nodes `b_j`.

Let

`P(t)=product_(ell=1)^r (t-b_ell)`

and define rational weights

`w_j = 1/[b_j P'(b_j)]`.

The standard Lagrange/Vandermonde identities give

`sum_(j=1)^r w_j b_j^q = 0`, for `q=1,...,r-1`,

and

`sum_(j=1)^r w_j b_j^r = 1`.

Indeed, with `d_j=1/P'(b_j)`, interpolation of monomials gives `sum_j d_j b_j^m=0` for `m=0,...,r-2` and `sum_j d_j b_j^(r-1)=1`; substituting `w_j=d_j/b_j` gives the displayed moments.

Choose a common positive denominator `Q` so that

`c_j=Q w_j in Z`

for all `j`, and divide by a common gcd if desired. Then

`sum_j c_j b_j^q=0`, `q=1,...,r-1`,

while `sum_j c_j b_j^r` is nonzero.

Fix a prime `p` and form the product character

`Psi_(p,b)(omega_1,...,omega_r)=product_(j=1)^r omega_j(p)^(c_j)`.

Along `V_(k,h,b)`, its phase is the same fixed linear combination of inverse-Gram increments. The first surviving term is order `r`, so its derivative has size

`asymp_(p,b) h^r/[N^r(log N)^2]`.

Across `M_N~N` starting indices, the total phase variation is therefore

`O_(p,b)(h^r/[N^(r-1)(log N)^2])`.

If this tends to zero, all values of `Psi_(p,b)(V_(k,h,b))` differ by `o(1)` from one common unimodular phase. Its normalized empirical average has modulus tending to one, whereas Haar measure would give Fourier coefficient zero. Joint Haar convergence is impossible.

The obstruction is intrinsic to the fixed node set: irregular spacing changes the coefficients `c_j`, not the existence of an order-`r` moment-null character.

## 4. Interpretation: fixed commensurate irregularity is still only clock geometry

`VIS-150`--`VIS-153` show that a fixed equal-step delay family can look frozen, partially coherent, mixed Haar-times-curve, or fully Haar solely because of deterministic inverse-Gram shear. The present result removes the simplest apparent escape from that control: choosing a visually irregular finite set of lag ratios.

For fixed distinct integer `b_j`, the lag geometry is still a finite-dimensional polynomial-moment filter of one deterministic clock. The Vandermonde system guarantees that every character acquires a first surviving moment by order `r`, while the Lagrange weights construct a matching deepest cancellation character. Therefore the subcritical/supercritical exponent is a dimension effect, not a consequence of equal spacing.

This does **not** classify the critical irregular-node law. For consecutive nodes `b_j=j`, `VIS-153` has the especially clean unimodular Newton-difference torus automorphism and its explicit `Haar^(r-1)` times curve limit. For general fixed nodes, an adapted integer moment basis can have nontrivial finite-index lattice structure, so the exact critical compact-group factorization is a separate question and is not needed for the present away-from-critical classification.

## 5. Prior art and novelty audit

The proof ingredients are classical: Gram/Riemann--Siegel theta asymptotics, fixed-order inverse-function differentiation, Vandermonde and Lagrange interpolation identities, the first-derivative exponential-sum estimate, and the Fourier criterion for Haar convergence on compact tori.

Richard P. Brent, *On the Accuracy of Asymptotic Approximations to the Log-Gamma and Riemann-Siegel Theta Functions*, Journal of the Australian Mathematical Society 107:3 (2019), 319--337, DOI `10.1017/S1446788718000393`, remains an authoritative theta-asymptotic error-control anchor for the inverse-clock estimates used here.

Antanas Laurinčikas, *Joint Discrete Approximation of Analytic Functions by Shifts of the Riemann Zeta-Function Twisted by Gram Points*, Mathematics 11 (2023), 565, DOI `10.3390/math11030565`, establishes joint Gram-point weak-distribution/universality prior art for zeta shifts. Its objects are joint analytic-function shifts involving powers of Gram points, not the fixed irregular lag-character threshold above.

A targeted search around Gram-point finite differences, irregular lag vectors, joint delay coordinates, and Gram-point weak distribution found no basis for claiming this control theorem as new literature. **No novelty is claimed.** The durable Mathia contribution is the explicit falsification boundary: fixed finite commensurate irregular lag geometry, away from its critical scale, is still generated by the deterministic Gram clock.

## Boundary and falsification

The theorem fixes both `r` and the integer node set `{b_1,...,b_r}` while `N->infinity`. It is not uniform in changing node geometry. Letting the `b_j`, their separation, the dimension, prime support, Fourier complexity, or character coefficients vary with `N` requires new quantitative control.

The critical regime

`h^r/[N^(r-1)(log N)^2] -> lambda in (0,infinity)`

is not classified here. Nor are selected/nonconsecutive Gram subsequences, which change the sampling index law rather than merely the set of fixed delays from each starting index.

Falsify the result by producing a nontrivial fixed joint character whose first `r` node moments all vanish, invalidating the fixed-node inverse-clock expansion/monotonicity in the stated range, or breaking the first-derivative cancellation estimate under the stated hypotheses.

## Visual consequence

No canonical PNG is retained. An irregular-delay embedding can look substantially less structured than an equal-step grid, but the theorem already shows that its subcritical coherence and supercritical Haar appearance are deterministic clock controls. A finite rendering would illustrate the false-positive rather than add evidence.

## Research consequence

The accepted `CLUE-zeta-prime-phase-recursive-geometry` should no longer treat a fixed finite irregular set of commensurate Gram lags as an automatic escape from the equal-step null. Away from the critical boundary, every such fixed node set has the same order-`r` deterministic clock threshold, with an explicit node-adapted deepest cancellation character.

The remaining lag-based escape routes must change a real hypothesis: analyze the irregular critical compact-group law, let node geometry/dimension/support grow with quantitative uniformity, change the Gram-index sampling rule, or introduce an independently anchored analytic source not determined by prime phases and the inverse Gram clock.