# VIS-158 — fixed degree-d polynomial Gram-index selectors are Haar through d times and fail at d+1

## Claim

Let `g_k` be the Gram points and

`z_k=(p^(-i g_k))_p in Omega`.

Let `P in Z[x]` have fixed degree `d>=1` and positive leading coefficient `a_d`, and define for all sufficiently large integers `n`

`w_n=z_(P(n))`.

Then the fixed-sample prime-phase law has an exact degree threshold determined only by the deterministic sampled Gram clock.

For every `1<=r<=d`, every fixed distinct integer offsets

`b_1,...,b_r`,

the joint population

`(w_(n+b_1),...,w_(n+b_r))`

is Haar-equidistributed on `r` copies of every fixed finite prime torus.

In contrast, for every `d+1` distinct fixed integer offsets

`b_0,...,b_d`,

there is a nontrivial fixed-prime product character whose value tends to `1`. Hence the `(d+1)`-copy population cannot converge to Haar.

For equally spaced offsets `0,h,...,dh`, the obstruction is the ordinary order-`d` finite-difference character with binomial exponents:

`product_(j=0)^d w_(n+jh)(p)^((-1)^(d-j) binom(d,j)) -> 1`

for every fixed prime `p`.

Thus a fixed degree-`d` polynomial index selector is asymptotically **d-wise Haar but not `(d+1)`-wise Haar** on fixed prime support. The affine fixed-offset case `d=1` and the quadratic pairwise-Haar/triple-clock case `d=2` are the first two members of one deterministic hierarchy.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-UNIFORM-DISTRIBUTION/GRAM-ASYMPTOTIC + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No statement is made for polynomial degree growing with height, offsets or prime support growing with height, arbitrary non-polynomial or data-dependent selectors, zeta-value/zero-derived coordinates, stochastic mixing, or RH.

## 1. A degree-d selector moves the Fejer scale to the d-th derivative

Let `g(x)` be the smooth eventual inverse of

`theta(g(x))=pi x`

and put

`G(x)=g(P(x))`.

The same classical inverse-Gram asymptotics used in `VIS-083`, `VIS-154`, `VIS-156`, and `VIS-157` give

`g'(x)~2 pi/log x`

and the corresponding differentiable asymptotic expansion obtained from the Riemann-Siegel theta formula. Since

`P(x)=a_d x^d+O(x^(d-1))`,

one gets

`G(x) = [2 pi a_d/d] x^d/log x * (1+o(1))`.

More precisely, for each fixed `0<=s<=d`, repeated implicit/chain differentiation gives

`G^(s)(x) ~ [2 pi a_d/d] [d!/(d-s)!] x^(d-s)/log x`,

while

`G^(d+1)(x) ~ -2 pi a_d (d-1)!/[x (log x)^2]`.

In particular,

`G^(d)(x) ~ 2 pi a_d (d-1)!/log x`.

Therefore `G^(d)` is eventually positive and decreasing, tends to zero, and satisfies

`x G^(d)(x) -> infinity`.

This is exactly the first-derivative Fejer scale after enough fixed finite differences. The polynomial degree does not create an independent source; it only decides how many differences are needed before the sampled Gram clock reaches that scale.

## 2. Fixed shifted characters are organized by Vandermonde moments

Fix `r` distinct offsets `b_1,...,b_r` and a character of the `r`-copy finite prime torus. For the `j`-th copy write

`A_j=sum_p m_(j,p) log p`,

where only finitely many integers `m_(j,p)` are nonzero. Unique factorization implies that `A_j=0` exactly when all exponents in the `j`-th copy vanish.

The character phase is

`F(x)=sum_(j=1)^r A_j G(x+b_j)`.

For `k>=0` put

`M_k=sum_(j=1)^r A_j b_j^k`.

If the character is nontrivial, the Vandermonde matrix on the distinct nodes `b_j` implies that not all of

`M_0,...,M_(r-1)`

can vanish. Let `s<=r-1` be the first index with `M_s!=0`.

Fixed-offset Taylor expansion gives

`F(x) = [M_s/s!] G^(s)(x) + O(G^(s+1)(x))`.

The same expansion remains valid after any fixed finite collection of forward differences. In particular, after

`d-s-1`

fixed forward differences when `s<=d-1`, the derivative of the resulting phase has the form

`C G^(d)(x)(1+o(1))`

for a nonzero constant `C` depending on the character, offsets, and chosen difference steps.

Because `G^(d)(x)` is eventually monotone, tends to zero, and `x|G^(d)(x)|->infinity`, the classical Fejer criterion makes that final difference sequence uniformly distributed modulo one. Iterating van der Corput's difference theorem backwards then makes the original sequence

`F(n)/(2 pi)`

uniformly distributed modulo one.

## 3. Every fixed r-time view with r<=d is Haar

Assume `r<=d`. The first nonzero Vandermonde moment from the previous section satisfies

`s<=r-1<=d-1`,

so the Fejer/van-der-Corput reduction always applies.

Hence every nontrivial character of the `r`-copy fixed finite prime torus has vanishing empirical average. Multidimensional Weyl's criterion gives Haar equidistribution of

`(w_(n+b_1),...,w_(n+b_r))`.

The important point is that the proof does not use visual sparsity, genericity of the polynomial coefficients, or probabilistic independence. The degree alone provides enough sampled-clock curvature to wash out every fixed character involving at most `d` time samples.

For `d=1`, this recovers the fixed-offset face of `VIS-156`: the one-time population is Haar while a fixed two-time relation remains coherent. For `d=2`, it recovers `VIS-157`: every fixed pair is Haar.

## 4. d+1 fixed times recover the deterministic polynomial clock

Now choose `d+1` distinct fixed integer offsets

`b_0,...,b_d`.

The integer matrix

`(b_j^k)_(0<=k<=d-1, 0<=j<=d)`

has rank `d`. Therefore its one-dimensional rational nullspace contains a nonzero integer vector

`c=(c_0,...,c_d)`

after clearing denominators, with

`sum_j c_j b_j^k=0`,  `0<=k<=d-1`.

The full Vandermonde matrix through power `d` is invertible, so necessarily

`M_d=sum_j c_j b_j^d !=0`.

Taylor expansion therefore gives

`sum_j c_j G(x+b_j)`
` = [M_d/d!] G^(d)(x) + O(G^(d+1)(x))`
` -> 0`.

Fix one prime `p` and use the product character

`Chi(omega_0,...,omega_d)=product_j omega_j(p)^(c_j)`.

Along the polynomially sampled Gram sequence,

`Chi(w_(n+b_0),...,w_(n+b_d))`
` = exp(-i log(p) sum_j c_j G(n+b_j))`
` -> 1`.

A nontrivial Haar character has expectation zero, so the `(d+1)`-copy empirical law is not Haar.

For equally spaced nodes `b_j=jh`, one may take

`c_j=(-1)^(d-j) binom(d,j)`,

which makes the obstruction the order-`d` forward finite difference. The hidden deterministic clock therefore appears exactly one sample beyond the largest fixed sample order that looks Haar.

## 5. Prior art and novelty audit

The proof uses only classical uniform-distribution tools: Weyl's criterion, Fejer's monotone-derivative criterion, and van der Corput's difference theorem, as in L. Kuipers and H. Niederreiter, *Uniform Distribution of Sequences* (Wiley, 1974). Michael Boshernitzan, **Uniform distribution and Hardy fields**, *Journal d'Analyse Mathematique* 62 (1994), 225-240, DOI `10.1007/BF02835955`, gives a substantially broader classical framework for uniform distribution of polynomial-growth Hardy-field phases. The present finding does not claim a new general equidistribution theorem; it records the explicit fixed-shift Vandermonde consequence for the sampled Gram clock needed as a Mathia visual null.

Antanas Laurincikas, **Joint Discrete Approximation of Analytic Functions by Shifts of the Riemann Zeta-Function Twisted by Gram Points**, *Mathematics* 11:3 (2023), 565, DOI `10.3390/math11030565`, supplies established Gram-point prime-phase/uniform-distribution context. Its shifts are built from powers of Gram values, not the fixed polynomial **index selector** `g_(P(n))` classified here.

A targeted literature check did not identify a basis for presenting the exact `d`-wise-Haar/`(d+1)`-clock formulation as a new theorem. **No novelty is claimed.** Its durable value is the control boundary: every fixed-degree polynomial thinning can manufacture apparent finite-order mixing without adding an arithmetic source.

## Boundary and falsification

The degree `d`, polynomial `P`, offsets, torus dimension, prime support, and every tested character are fixed before `n->infinity`. The theorem gives no uniformity when any of those complexities grow with height.

The coefficients of `P` are integers only to make `P(n)` an actual Gram index without an additional rounding rule. The argument is eventual, so finitely many initial values and any early failure of positivity/monotonicity are irrelevant.

The Haar statements concern only fixed prime phases. They do not imply independence after adjoining `Z(g_(P(n)))`, derivatives, zero occupancy, nearby-zero geometry, or another independently anchored analytic coordinate.

Falsify the result by breaking the derivative asymptotic for `G=g o P`, the Vandermonde first-moment classification, the iterated Fejer/van-der-Corput reduction, or the integer moment-null product character at `d+1` samples.

## Visual consequence

No canonical PNG is retained. Any collection of plots using at most `d` fixed time samples can look asymptotically Haar under a completely deterministic degree-`d` selector, while the first exact clock obstruction lives one sample order higher. The character calculation is therefore a stronger visual control than another finite scatter plot.

## Research consequence

The accepted `CLUE-zeta-prime-phase-recursive-geometry` can now close **all fixed-degree polynomial Gram-index thinning** as a positive information escape on fixed prime support. The quadratic result `VIS-157` was not exceptional; it was the degree-two instance of the general hierarchy.

A genuinely new sampling route must change a hypothesis: degree or selector complexity growing with height with quantitative uniformity, a non-polynomial or data-dependent selector with a separately derived null, genuinely noncommensurate real-time sampling, or an independently anchored analytic coordinate whose joint information is not determined by the prime-phase/clock state.