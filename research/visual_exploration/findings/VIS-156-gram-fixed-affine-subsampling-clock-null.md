# VIS-156 — fixed arithmetic-progression Gram subsampling preserves the prime-torus clock null

## Claim

Let `g_k` be the Gram points, let

`z_k=(p^(-i g_k))_p in Omega`,

and fix integers `q>=1` and `a`. Define the fixed affine Gram-index subsequence

`w_n=z_(a+q n)`

for all sufficiently large `n`.

Then fixed arithmetic-progression subsampling of the Gram indices does not create a new finite-dimensional prime-phase information channel.

First, for every fixed finite set of primes, the population `w_n` is Haar-equidistributed on the corresponding finite prime torus.

Second, fix `r>=2`, distinct positive integers

`1<=b_1<...<b_r`,

and an integer lag scale `h=h(N)` with `b_r h=o(N)`. Put

`Delta~_(n,ell)=w_(n+ell) overline(w_n)`

and

`V~_(n,h,b)=(Delta~_(n,b_1 h),...,Delta~_(n,b_r h)) in Omega^r`

for `N<=n<=2N-b_r h`. Then the complete fixed-node Gram-clock classification from `VIS-154`--`VIS-155` survives unchanged in threshold exponent under this nonconsecutive sampling law.

If

`h^r/[N^(r-1)(log N)^2] -> 0`,

the joint empirical law cannot converge to Haar: the same primitive deepest Vandermonde/Lagrange product character remains coherent.

If

`h^r/[N^(r-1)(log N)^2] -> infinity`,

the joint empirical law converges weakly to Haar on `Omega^r`.

At the critical scale

`h^r/[N^(r-1)(log N)^2] -> lambda in (0,infinity)`,

the law is again Haar on the codimension-one fibers of the primitive deepest product character and deterministic in the quotient. With the notation of `VIS-155`, the quotient curve is the same node-dependent inverse-clock curve with its winding multiplied by the fixed sampling stride `q`:

`Gamma~_(r,b,lambda,q)(u)`
` = (exp(-i q kappa_(r,b) lambda log(p) u^(1-r)))_p`, `1<=u<=2`.

Thus selecting one fixed congruence class of Gram indices changes only deterministic clock constants. It does not escape the prime-torus population null, the finite-lag Vandermonde threshold, or the critical Haar-fiber clock law.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-UNIFORM-DISTRIBUTION/GRAM-ASYMPTOTIC + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No statement is made for a stride or residue rule changing with `N`, irregular/data-dependent selected index sets, sparse nonlinear subsequences, growing delay dimension/node geometry/prime support/Fourier complexity, genuinely noncommensurate real-time offsets, zeta-value or zero-derived coordinates, stochastic mixing, or RH.

## 1. Affine index restriction preserves fixed-prime Haar population

Let `g(x)` be the smooth eventual inverse of

`theta(g(x))=pi x`

and define the sampled clock

`G(x)=g(a+q x)`.

The standard inverse-Gram asymptotics used in `VIS-083` give

`g'(x)~2 pi/log x`,

with `g'(x)` eventually positive, decreasing to zero, and `x g'(x)->infinity`. Therefore

`G'(x)=q g'(a+q x)`

is also eventually positive and decreasing to zero, while

`x G'(x)~2 pi q x/log x -> infinity`.

Fix distinct primes `p_1,...,p_s`. For a nonzero integer vector `m in Z^s`, put

`A_m=sum_j m_j log p_j`.

Unique factorization gives `A_m!=0`. The Fejer/van-der-Corput uniform-distribution criterion applied to

`A_m G(x)/(2 pi)`

therefore shows that

`A_m g_(a+q n)/(2 pi) mod 1`

is uniformly distributed. Weyl's multidimensional criterion then gives Haar equidistribution of

`(p_1^(-i g_(a+q n)),...,p_s^(-i g_(a+q n)))`.

So even a visibly nonconsecutive fixed congruence class of Gram indices has the same fixed-finite-prime population law as the full Gram sequence.

## 2. The sampled clock has the same fixed-order derivative hierarchy

For every fixed `m>=2`, the inverse-Gram estimates used in `VIS-154`--`VIS-155` give

`g^(m)(x) asymp_m x^(1-m)(log x)^(-2)`

with eventual nonvanishing and alternating sign. Since `q` and `a` are fixed,

`G^(m)(x)=q^m g^(m)(a+q x)`

and hence

`G^(m)(x) asymp_(m,q) x^(1-m)(log x)^(-2)`.

More precisely, uniformly for `u in [1,2]`,

`G^(m)(Nu)`
` = q [2 pi (-1)^(m-1)(m-2)!]/[N^(m-1)(log N)^2] u^(1-m)(1+o(1))`.

The fixed affine index restriction therefore preserves every power of `N` and `log N` in the Gram-clock hierarchy. It inserts only the constant factor `q` into the leading fixed-order clock derivative.

This is the key control. A residue-class selection looks like a different sampling pattern in index space, but at fixed stride it is merely a deterministic reparameterization of the same smooth inverse Gram clock.

## 3. Fixed lag vectors inherit the same Vandermonde threshold

A fixed character of `Omega^r` gives real coefficients

`alpha_j=sum_p m_(j,p) log p`

and phase

`F_h(x)=sum_(j=1)^r alpha_j [G(x+b_j h)-G(x)]`.

Define moments

`S_d=sum_j alpha_j b_j^d`, `d=1,...,r`.

Exactly as in `VIS-154`, the Vandermonde matrix of the fixed distinct nodes has full rank, so every nontrivial character has a first nonzero moment

`d_0<=r`.

Taylor expansion and the sampled-clock derivative estimate give

`F_h'(x)`
` = [S_(d_0)/d_0!] h^(d_0) G^(d_0+1)(x)(1+o(1))`,

therefore

`|F_h'(x)| asymp_(character,b,q) h^(d_0)/[N^(d_0)(log N)^2]`

uniformly on the dyadic sample block. The same first-derivative exponential-sum estimate as in `VIS-154` gives cancellation for every fixed character whenever

`h^r/[N^(r-1)(log N)^2] -> infinity`.

Conversely, let `c=(c_1,...,c_r)` be the primitive integer generator of the deepest moment-null lattice

`sum_j c_j b_j^d=0`, `d=1,...,r-1`.

Its first surviving moment is order `r`. Across `Theta(N)` sampled starting indices, the total phase variation is

`O_(b,q)(h^r/[N^(r-1)(log N)^2])`.

If that quantity tends to zero, the corresponding nontrivial product character remains asymptotically coherent, so Haar convergence is impossible.

The stride `q` affects constants but not the threshold exponent. Fixed arithmetic-progression selection therefore does not turn the finite-lag clock hierarchy into a new arithmetic source.

## 4. The critical law is the same Haar fiber with a rescaled clock winding

At critical scale, the deepest product coordinate is

`pi_c(V~_(n,h,b))(p)`
` = exp(-i log(p) sum_j c_j [G(n+b_j h)-G(n)] )`.

The first `r-1` node moments vanish. With

`C_b=sum_j c_j b_j^r>0`,

Taylor expansion gives

`sum_j c_j [G(x+b_j h)-G(x)]`
` = (C_b/r!) h^r G^(r)(x)+o(1)`

uniformly on the dyadic block. Using the explicit leading term for `G^(r)`,

`(C_b/r!) h^r G^(r)(Nu)`
` -> q kappa_(r,b) lambda u^(1-r)`,

where

`kappa_(r,b)=2 pi (-1)^(r-1) C_b/[r(r-1)]`.

Thus the quotient converges to the displayed deterministic curve with winding multiplied by `q`.

For every character transverse to the deepest quotient, some moment order `d_0<=r-1` survives. At critical scale its total shear grows like

`q lambda^(d_0/r) (N/(log N)^2)^(1-d_0/r)`,

up to a nonzero character/node constant, and therefore diverges. The same first-derivative cancellation argument as in `VIS-155` makes all transverse fixed characters vanish. Compact-group Fourier convergence gives Haar conditional measure on each quotient fiber.

So the critical appearance is not rescued by congruence-class sampling either: it is still `Haar^(r-1)` over one deterministic inverse-clock curve, only with a fixed stride-dependent winding speed.

## 5. Prior art and novelty audit

The population statement is a direct affine-index specialization of classical Fejer/van-der-Corput uniform-distribution theory and Weyl's criterion. The same ingredients and the fixed-prime Gram-point weak-distribution context are already anchored in `VIS-083` by Kuipers and Niederreiter, *Uniform Distribution of Sequences* (Wiley, 1974), and Antanas Laurinčikas, **Joint Discrete Approximation of Analytic Functions by Shifts of the Riemann Zeta-Function Twisted by Gram Points**, *Mathematics* 11:3 (2023), 565, DOI `10.3390/math11030565`.

A targeted literature check for Gram-point arithmetic-progression subsequences and related discrete universality did not identify a source that makes the fixed-index-stride lag classification above a literature novelty claim. Related Gram-point universality work treats full Gram sequences and other deterministic zeta shifts; for example Darius Šiaučiūnas and Monika Tekorė, **Gram Points in the Universality of the Dirichlet Series with Periodic Coefficients**, *Mathematics* 11:22 (2023), 4615, studies shifts `L(s+i h t_k)` rather than selection of one index congruence class.

No novelty is claimed. The durable Mathia value is the control boundary: one of the simplest genuinely nonconsecutive index selectors, a fixed arithmetic progression, is still exactly in the deterministic Gram-clock information class after the induced sampling null is derived.

## Boundary and falsification

The stride `q` and residue `a` are fixed while `N->infinity`. The argument is not uniform in `q=q(N)`, and it does not cover selectors chosen from the prime phases, `Z(g_k)`, zero occupancy, another arithmetic signal, or any data-dependent rule.

Nor does it cover nonlinear sparse subsequences such as `k=n^2`, selectors with growing gaps, irregular deterministic subsets without a smooth affine reparameterization, or genuinely noncommensurate real-time offsets. Such selectors require their own induced sampling law rather than being declared independent merely because they are nonconsecutive.

The lag classification fixes the delay dimension, node set, prime/Fourier character, and sampling stride. Growing geometry remains outside the theorem.

Falsify the population statement by finding a nonzero fixed prime character for which the Fejer derivative criterion fails after the affine reparameterization. Falsify the lag statement by breaking the sampled-clock derivative asymptotics, producing a nontrivial fixed character whose first `r` node moments all vanish, or finding a transverse fixed character that does not cancel in the stated critical/supercritical regime.

## Visual consequence

No canonical PNG is retained. A residue-class-colored Gram plot would make the samples look visibly separated in index space, but the theorem shows that fixed-prime population and fixed finite lag geometry still obey the same deterministic null family. Rendering that separation would risk making a coordinate choice look like a new information channel.

## Research consequence

The accepted `CLUE-zeta-prime-phase-recursive-geometry` should narrow its selected/nonconsecutive escape. A fixed affine selector `a+q n` is now closed: its fixed-prime population remains Haar, and every fixed finite commensurate lag geometry has the same subcritical obstruction, critical Haar-fiber clock curve, and supercritical Haar law, with only deterministic constants changed.

A genuinely different sampling route must therefore use a selector whose induced law is not a fixed affine reparameterization of the Gram clock — for example a growing-stride, nonlinear, irregular, or data-dependent subsequence — and derive that selector's null before residual visual structure is interpreted as arithmetic evidence.