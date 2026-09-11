# VIS-159 — noninteger power-law Gram-index selectors are Haar through ceil(alpha) times and fail one order later

## Claim

Let `g_k` be the Gram points and

`z_k=(p^(-i g_k))_p in Omega`.

Fix a noninteger real exponent `alpha>1`, put

`m=ceil(alpha)`,

and define the deterministic sparse selector

`k_n=floor(n^alpha)`,  `w_n=z_(k_n)`.

Then the fixed-sample prime-phase law has a sharp ceiling threshold.

For every `1<=r<=m`, every fixed distinct integer offsets

`b_1,...,b_r`,

the joint population

`(w_(n+b_1),...,w_(n+b_r))`

is Haar-equidistributed on `r` copies of every fixed finite prime torus.

In contrast, for every `m+1` distinct fixed integer offsets

`b_0,...,b_m`,

there is a nontrivial fixed-prime product character whose value tends to `1`. Hence the `(m+1)`-copy population cannot converge to Haar.

Thus a noninteger power-law index selector `floor(n^alpha)` is asymptotically **ceil(alpha)-wise Haar but not `(ceil(alpha)+1)`-wise Haar** on fixed prime support.

Together with `VIS-158`, which treats integer powers as polynomial selectors, the complete fixed power family `floor(n^alpha)`, `alpha>1`, has one unified deterministic threshold: the largest fixed sample order that can look Haar is exactly `ceil(alpha)`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-UNIFORM-DISTRIBUTION/GRAM-ASYMPTOTIC + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No statement is made for exponents depending on height, general regularly varying or data-dependent selectors, offsets or prime support growing with height, zeta-value/zero-derived coordinates, stochastic mixing, or RH.

## 1. Smooth power sampling and the floor error

Let `g(x)` be the smooth eventual inverse of

`theta(g(x))=pi x`

and define

`H(x)=g(x^alpha)`.

The classical inverse-Gram expansion used in `VIS-083`, `VIS-154`, `VIS-156`, `VIS-157`, and `VIS-158` gives

`g'(x)~2 pi/log x`

and, after composition with `x^alpha`,

`H(x) = (2 pi/alpha) x^alpha/log x * (1+o(1))`.

For every fixed integer `s>=0`, differentiating the same expansion gives

`H^(s)(x) = C_s x^(alpha-s)/log x * (1+o(1))`,

where

`C_s=(2 pi/alpha) alpha(alpha-1)...(alpha-s+1)`

and `C_s!=0` because `alpha` is not an integer.

The integer selector differs negligibly from the smooth one. Since

`|floor(x^alpha)-x^alpha|<=1`

and `g'(u)=O(1/log u)`, the mean-value theorem gives

`g_(floor(x^alpha)) - H(x) = O(1/log x)`.

The same estimate is uniform over any fixed finite set of shifts `x+b_j`. Therefore every fixed character phase of the actual rounded selector differs by `o(1)` from the corresponding smooth phase. Uniform distribution modulo one is unchanged by such an `o(1)` perturbation.

## 2. Vandermonde moments reduce every fixed character to one power scale

Fix `r` distinct offsets `b_1,...,b_r` and a character of the `r`-copy finite prime torus. Write

`A_j=sum_p m_(j,p) log p`,

with finitely many integers `m_(j,p)`. Unique factorization implies that a nontrivial character has not all `A_j=0`.

For the smooth selector, the character phase is

`F(x)=sum_(j=1)^r A_j H(x+b_j)`.

Put

`M_k=sum_(j=1)^r A_j b_j^k`.

The Vandermonde matrix on the distinct offsets implies that some

`M_s!=0`,  `0<=s<=r-1`.

Taking the first such `s`, fixed-shift Taylor expansion gives

`F(x) = [M_s/s!] H^(s)(x) + O(H^(s+1)(x))`

and hence

`F(x)=C x^beta/log x * (1+o(1))`,

where `C!=0` and

`beta=alpha-s`.

The sample-order problem is therefore controlled by whether this residual power `beta` is positive or negative.

## 3. Every fixed r-time view with r<=ceil(alpha) is Haar

Write

`d=floor(alpha)`, so `m=d+1`.

Assume `r<=m`. Then the first nonzero moment satisfies

`s<=r-1<=d`,

so

`beta=alpha-s>0`.

Because `alpha` is noninteger, `beta` is also noninteger. Let

`q=floor(beta)`,  `gamma=beta-q in (0,1)`.

After `q` fixed forward differences, the phase has asymptotic form

`Delta^q F(x)=C_q x^gamma/log x * (1+o(1))`

with `C_q!=0`. Its derivative is eventually of constant sign and monotone in magnitude, tends to zero, and satisfies

`x |(Delta^q F)'(x)| ~ |C_q| gamma x^gamma/log x -> infinity`.

Fejer's monotone-derivative criterion therefore makes

`Delta^q F(n)/(2 pi)`

uniformly distributed modulo one. Iterating van der Corput's difference theorem backwards `q` times gives uniform distribution of `F(n)/(2 pi)` itself.

The `o(1)` floor error from Section 1 preserves that conclusion for the actual sequence `g_(floor((n+b_j)^alpha))`. Hence every nontrivial character of the `r`-copy fixed finite prime torus has vanishing empirical average. Multidimensional Weyl's criterion gives Haar equidistribution of

`(w_(n+b_1),...,w_(n+b_r))`

for every fixed `r<=ceil(alpha)`.

## 4. One more sample recovers the deterministic clock

Now take `m+1=d+2` distinct fixed integer offsets

`b_0,...,b_m`.

The `(d+1) x (d+2)` moment matrix

`(b_j^k)_(0<=k<=d, 0<=j<=d+1)`

has rank `d+1`. Its one-dimensional rational nullspace therefore contains a nonzero integer vector

`c=(c_0,...,c_(d+1))`

after clearing denominators, with

`sum_j c_j b_j^k=0`,  `0<=k<=d`.

The full Vandermonde matrix through power `d+1` is invertible, so

`sum_j c_j b_j^(d+1) != 0`.

Taylor expansion then gives

`sum_j c_j H(x+b_j)`
` = C H^(d+1)(x)(1+o(1))`
` = O(x^(alpha-d-1)/log x)`
` -> 0`,

because `alpha-d-1<0`.

The rounding errors also sum to `o(1)`. Fix one prime `p` and use the product character

`Chi(omega_0,...,omega_m)=product_j omega_j(p)^(c_j)`.

Along the rounded power-law Gram selector,

`Chi(w_(n+b_0),...,w_(n+b_m)) -> 1`.

A nontrivial Haar character has expectation zero, so the `(m+1)`-copy population cannot be Haar.

For equally spaced offsets one may take the ordinary order-`m` binomial finite-difference vector. The apparent finite-order mixing therefore remains a deterministic sampled-clock effect even though the selector is non-polynomial.

## 5. Prior art and novelty audit

The proof uses the same classical uniform-distribution machinery as `VIS-158`: Weyl's criterion, Fejer's monotone-derivative criterion, and van der Corput's difference theorem, as in L. Kuipers and H. Niederreiter, *Uniform Distribution of Sequences* (Wiley, 1974).

Michael Boshernitzan, **Uniform distribution and Hardy fields**, *Journal d'Analyse Mathematique* 62 (1994), 225-240, DOI `10.1007/BF02835955`, gives a substantially broader classical criterion for polynomial-growth Hardy-field phases. In particular, noninteger power/log phases belong to established uniform-distribution territory. Boshernitzan and Wierdl, **Ergodic theorems along sequences and Hardy fields**, *PNAS* 93:16 (1996), 8205-8207, DOI `10.1073/pnas.93.16.8205`, explicitly treats `floor(n^delta)`-type deterministic sampling in the wider Hardy-field/ergodic setting.

Antanas Laurincikas, **Joint Discrete Approximation of Analytic Functions by Shifts of the Riemann Zeta-Function Twisted by Gram Points**, *Mathematics* 11:3 (2023), 565, DOI `10.3390/math11030565`, supplies established Gram-point uniform-distribution context, but studies powers of Gram values rather than the index selector `g_(floor(n^alpha))` classified here.

A targeted literature check did not identify a basis for presenting the exact `ceil(alpha)`-wise-Haar/next-order-clock formulation as a new theorem. **No novelty is claimed.** Its durable value is as a Mathia visual null: non-polynomial Piatetski-Shapiro-style sparsity can still manufacture arbitrarily high fixed-order Haar appearance without introducing a new arithmetic information source.

## Boundary and falsification

The exponent `alpha`, offsets, torus dimension, prime support, and tested characters are fixed before `n->infinity`. The result is not uniform as `alpha`, sample order, offsets, prime support, or Fourier complexity vary with height.

The floor is harmless here only because changing the Gram index by `O(1)` changes the Gram ordinate by `O(1/log n)`. A selector with larger or structured index perturbations requires a separate audit.

The Haar statements concern only fixed prime phases. They do not imply independence after adjoining `Z(g_(k_n))`, derivatives, zero occupancy, nearby-zero geometry, or another independently anchored analytic coordinate.

Falsify the result by breaking the inverse-Gram derivative asymptotics, the `o(1)` rounding reduction, the Vandermonde first-moment classification, the Fejer/van-der-Corput reduction for `beta>0`, or the integer moment-null character at `ceil(alpha)+1` samples.

## Visual consequence

No canonical PNG is retained. A fixed scatter, delay embedding, or finite-time prime-phase view using at most `ceil(alpha)` samples can look asymptotically Haar under the entirely deterministic selector `floor(n^alpha)`. The first exact clock obstruction lives one sample order higher, so increasing visual sparsity or using a noninteger power law does not by itself create an independent source.

## Research consequence

The accepted `CLUE-zeta-prime-phase-recursive-geometry` can now close the full fixed power-law family `floor(n^alpha)`, `alpha>1`, as a positive information escape on fixed prime support when combined with `VIS-158` for integer exponents.

A genuinely new sampling route must change another hypothesis: selector exponent/complexity varying with height with quantitative uniformity, a non-power non-polynomial or data-dependent selector with a separately derived null, genuinely noncommensurate real-time sampling, or an independently anchored analytic coordinate whose joint information is not determined by the prime-phase/clock state.