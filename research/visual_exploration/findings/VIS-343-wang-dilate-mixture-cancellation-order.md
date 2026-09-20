# VIS-343 — an N-dilate Wang mixture has at most N orders of high-frequency cancellation

## Claim

Let Wang's exact summatory-remainder multiplier from `VIS-333` be

`m(xi)=4(1+i xi)/(4+xi^2)`.

Fix `N>=1`, distinct positive dilation factors `a_1,...,a_N`, and frequency-independent complex coefficients `c_1,...,c_N`, not all zero. Define

`M(xi)=sum_(j=1)^N c_j m(a_j xi)`.

Then the high-frequency decay order of `M` is at most `N`. More precisely, for every integer `K>=1`,

`M(xi)=sum_(k=1)^K beta_k xi^(-k) [sum_(j=1)^N c_j a_j^(-k)] + O(|xi|^(-K-1))`,

where every `beta_k` is nonzero. Therefore

`M(xi)=O(|xi|^(-r))`

for an integer `r>=2` only if

`sum_(j=1)^N c_j a_j^(-k)=0`, `k=1,...,r-1`.

Because the `a_j` are distinct, the first `N` moment equations form an invertible Vandermonde system. Hence a nonzero `N`-dilate combination cannot satisfy all cancellations for `k=1,...,N`, so it cannot have decay `O(|xi|^(-N-1))`.

Conversely, the first `N-1` equations have a one-dimensional nonzero solution space, and every such nonzero solution has

`sum_j c_j a_j^(-N) != 0`.

Thus **order `N` is the maximal possible polynomial high-frequency decay of a nontrivial linear combination of `N` distinct pure dilates of Wang's multiplier**.

Combined with `VIS-342`, this yields a necessary scale-count condition for a scalarized multiscale explanation. If a family at log-scale `u` uses `N(u)` distinct pure dilates and its only claimed gain is the resulting polynomial tail order, then its effective scalar order satisfies

`r_eff(u) <= N(u)`.

Consequently, subpolynomially many dilates cannot produce a fixed improvement in the Vinogradov–Korobov `u`-power class through that scalar mechanism. A target gain `delta>0` over `3/5` requires at least

`N(u) >= u^(5 delta/2+o(1))`

within the `VIS-342` model, before coefficient growth, leakage, source norms, or destination repayment are even charged.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL MOMENT-CANCELLATION/VANDERMONDE STRUCTURE + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This finding concerns pure dilations with frequency-independent coefficients. Translations, frequency-dependent coefficients, nonlinear packet selection, arithmetic sign information, or other genuinely non-scalar constructions are outside the claim.

## 1. Exact high-frequency expansion

For `|z|>2`,

`m(z)`
` = 4(1+i z) z^(-2) [1+4 z^(-2)]^(-1)`
` = 4(1+i z) z^(-2) sum_(q>=0) (-4)^q z^(-2q)`.

Hence

`m(z)=sum_(q>=0) [4 i (-4)^q z^(-(2q+1)) + 4(-4)^q z^(-(2q+2))]`.

Define

`beta_(2q+1)=4 i (-4)^q`,
`beta_(2q+2)=4(-4)^q`.

Every coefficient is nonzero. Substituting `z=a_j xi` and summing over `j` gives, to arbitrary finite order,

`M(xi)=sum_(k>=1) beta_k xi^(-k) S_k`,

where

`S_k=sum_(j=1)^N c_j a_j^(-k)`.

Thus the first surviving inverse-frequency power is exactly the first nonzero moment `S_k`.

## 2. Vandermonde obstruction

Put `x_j=a_j^(-1)`. The cancellation conditions through order `N` are

`sum_j c_j x_j^k=0`, `k=1,...,N`.

Their coefficient matrix is

`V_(k,j)=x_j^k`.

Its determinant equals a nonzero diagonal factor times the ordinary Vandermonde determinant:

`det V = (prod_j x_j) prod_(j<l)(x_l-x_j)`.

The scales are positive and distinct, so the `x_j` are nonzero and distinct. Therefore `V` is invertible and the only coefficient vector cancelling the first `N` asymptotic terms is `c=0`.

It follows that every nontrivial `N`-dilate combination has some `S_k != 0` with `1<=k<=N`, and therefore has high-frequency order at most `N`.

For sharpness, impose only

`S_1=...=S_(N-1)=0`.

The `(N-1) x N` Vandermonde submatrix has rank `N-1`, so its nullspace is one-dimensional. A nonzero vector in that nullspace cannot also satisfy `S_N=0`, because that would solve the full invertible `N x N` system. Hence there are nontrivial weights with exact decay order `N`.

## 3. Multiscale consequence

The accepted Wang clue leaves open whether a multiscale packet can generate an effective high-frequency order that grows with `u`. The present calculation distinguishes two very different uses of "many scales".

If the construction is only a frequency-independent linear combination of `N(u)` dilates of the same one-order Wang filter, then the number of scales itself bounds the cancellation order:

`r_eff(u)<=N(u)`.

No arrangement of the dilation locations changes that algebraic ceiling. Choosing the coefficients optimally can cancel the first `N-1` asymptotic powers, but not the `N`th as well.

Insert this necessary bound into `VIS-342`. There a fixed power-class gain `delta` in the scalar zero-free-width/truncation objective requires

`r_eff(u)=u^(5 delta/2+o(1))`.

Therefore an `N(u)`-dilate explanation requires at least polynomially many distinct scales of the corresponding order. Finite, logarithmic, polylogarithmic, or otherwise subpolynomial scale counts remain in the original `u^(3/5+o(1))` power class under this scalar interpretation.

This is only a necessary condition. Even polynomially many scales do not establish a gain: the cancellation weights may be large or ill-conditioned, finite-frequency leakage may dominate, the source may not realize the required asymptotic regime, and Wang's complete destination may repay the apparent smoothing through derivative-sensitive terms.

## 4. What this does not classify

A translated packet has Fourier factors such as `e^(-i b_j xi)m(a_j xi)`. Those oscillatory factors do not share the common inverse-power expansion used above, so the finite Vandermonde argument does not reduce them to scalar moment cancellation. The same is true for frequency-dependent coefficients or source-adaptive nonlinear combinations.

Such mechanisms are not validated by escaping this theorem. They simply fall on the genuinely non-scalar side of the accepted clue and must supply their own signed/arithmetic estimate, normalization, leakage control, and destination audit.

Likewise, the theorem does not say that the actual Wang transform is iterated `N` times, nor that every packet's tail order can be inserted into Bellotti's truncation balance. It only closes the narrower pure-dilation route when that route is the claimed source of the scalar tail exponent.

## Prior-art audit

Cancellation of successive terms in a known asymptotic expansion by linear combinations at several scales is classical extrapolation theory. Avram Sidi, **The Richardson Extrapolation Process with a Harmonic Sequence of Collocation Points**, *SIAM Journal on Numerical Analysis* 37:5 (2000), 1729–1746, DOI `10.1137/S0036142998340137`, formulates generalized Richardson extrapolation through linear systems that cancel prescribed asymptotic powers and studies its convergence and stability. This bounds novelty for the general cancellation mechanism.

The specific statement here is the elementary specialization to Wang's rational multiplier. The nonzero coefficients `beta_k` and the exact `N`-dilate ceiling follow directly from its expansion and an ordinary Vandermonde determinant. No novelty is claimed for Richardson extrapolation, moment cancellation, Vandermonde systems, finite-difference weights, or wavelet-style vanishing moments.

## Dependencies

- `VIS-333`: gives the exact nonvanishing Wang multiplier `m(xi)` and its one-order high-frequency decay.
- `VIS-341`: classifies fixed scalar truncation order in the Vinogradov–Korobov optimization.
- `VIS-342`: classifies variable scalar order and shows that a fixed power-class gain requires polynomial order growth.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose remaining branch asks whether genuine multiscale source structure can evade the scalar controls.

## Research consequence

The accepted Wang source clue narrows again. **A pure multiscale superposition does not acquire arbitrarily high polynomial smoothing merely because it uses several dilations of Wang's one-order filter: `N` distinct dilates buy at most `N` cancelled inverse-frequency orders.**

Therefore a scalarized fixed power-class gain cannot come from a small or slowly growing dilation bank. It would require polynomially many distinct scales before any stability or downstream costs are counted. A viable alternative must either meet that scale-count requirement with controlled coefficients and leakage, or use a genuinely non-scalar translated/signed/arithmetic mechanism whose gain cannot be reduced to these Vandermonde moment cancellations.