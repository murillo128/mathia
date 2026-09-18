# VIS-297 — Wang relative-boundary remainder mean is deterministic gamma normalization

## Claim

Let `I=[T,T+H]`, `H=T^theta`, `L=log T`, with fixed `0<theta<1`, and fix `lambda<theta`. Let `x=x(T)` satisfy `x->infinity`, `x<=T^lambda`, and suppose

`x^2 log x / L -> kappa in (0,infinity)`.

Use Wang's decomposition

`A(x,t)=-D_x(t)+B_x(t)+E_x(t)`, `B_x(t)=log(t+2)/x`,

and the normalized mean remainder introduced in `VIS-296`,

`Q_E(T,x)=(x/H) integral_I E_x(t) dt`.

Then

`Re Q_E(T,x) = -log(2*pi) + o(1)`.

Consequently the finite relative crossover isolated in `VIS-296` is

`R_gamma(T,x)/(H log x)`
` = 1/(2*pi) - log(2*pi)/(pi*kappa) + o(1)`.

The previously unresolved order-one mean of `E_x` is therefore not a new arithmetic source term. Its leading contribution is the deterministic gamma-factor normalization hidden by Wang's convenient coarse baseline `log(t+2)/x`.

**Evidence/status:** `LITERATURE-SPECIALIZATION + EXACT-DERIVED + DETERMINISTIC-NORMALIZATION + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No new pair-correlation theorem, zero-density estimate, PNT remainder, RH implication, or claim of novelty for the underlying explicit-formula identities is made.

## 1. Recover the remainder from the exact Landau decomposition

Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh write Wang's source quantity through the exact identity

`A(x,t)=x R(3/2+it)-x^(-1)R(-1/2+it)`,

where

`R(s)=sum_(n<=x) Lambda(n)n^(-s) + zeta'/zeta(s)`
`     - x^(1-s)/(1-s)`
`     - sum_(m>=1) x^(-2m-s)/(2m+s)`.

Using `zeta(s)=chi(s)zeta(1-s)` at `s=-1/2+it`,

`zeta'/zeta(-1/2+it)`
` = chi'/chi(-1/2+it) - zeta'/zeta(3/2-it)`.

The prime sums and `zeta'/zeta(3/2+it)` combine exactly into `-D_x(t)`. Relative to Wang's choice `B_x(t)=log(t+2)/x`, the remaining term can therefore be written

`E_x(t)`
` = x^(-1)[-chi'/chi(-1/2+it)`
`           + zeta'/zeta(3/2-it) - log(t+2)]`
`   + P_x(t) + T_x(t)`,

with pole contribution

`P_x(t)=x^(1/2-it)[1/(1/2+it)+1/(3/2-it)]`

and trivial-zero contribution

`T_x(t)=x^(-1/2-it) sum_(m>=1) x^(-2m)`
`       *[1/(2m-1/2+it)-1/(2m+3/2+it)]`.

This is an exact refinement of the coarse `E_x(t)=O(1/x)` bound used in Wang's Proposition 2.6 regime. It is useful here only because `VIS-296` showed that the interval mean of `E_x` is precisely the load-bearing unresolved term at the finite relative crossover.

## 2. The gamma factor supplies the surviving constant

For

`chi(s)=pi^(s-1/2) Gamma((1-s)/2)/Gamma(s/2)`,

Stirling's expansion for the digamma function gives, uniformly for `t` in `I` because `H=o(T)`,

`Re[-chi'/chi(-1/2+it)] = log(t/(2*pi)) + O(1/t)`.

Therefore

`(1/H) integral_I Re[-chi'/chi(-1/2+it)-log(t+2)] dt`
` = -log(2*pi) + O(1/T)`.

Thus Wang's `log(t+2)/x` baseline has deliberately discarded a fixed gamma-normalization constant. At scales where an `O(1/x)` remainder is negligible this is harmless; at the `VIS-296` relative crossover, multiplying the remainder by `x` makes that constant visible.

## 3. The right-half-plane zeta term has zero interval mean

On `Re(s)=3/2`, the logarithmic derivative has the absolutely convergent Dirichlet series

`zeta'/zeta(3/2-it)`
` = -sum_(n>=2) Lambda(n)n^(-3/2) exp(it log n)`.

Termwise integration over `I` gives

`|(1/H) integral_I zeta'/zeta(3/2-it) dt|`
` <= (2/H) sum_(n>=2) Lambda(n)/(n^(3/2) log n)`
` = O(1/H)`.

Hence this piece tends to zero. In particular, no prime-sensitive mean survives through the absolutely convergent right-half-plane term at this normalization.

## 4. Pole and trivial-zero terms are negligible

The pole terms cancel to second order in `t`:

`1/(1/2+it)+1/(3/2-it)`
` = 2/[(1/2+it)(3/2-it)]`.

Thus, for `t` asymptotic to `T`,

`P_x(t)=O(x^(1/2)/T^2)`

and therefore

`(x/H) integral_I P_x(t) dt = O(x^(3/2)/T^2)=o(1)`

under `x<=T^lambda`, `lambda<theta<1`.

For eventually `x>=2`, the geometrically convergent trivial-zero tail gives the weaker but sufficient bound

`T_x(t)=O(x^(-5/2)/T)`,

so

`(x/H) integral_I T_x(t) dt = O(x^(-3/2)/T)=o(1)`.

Combining the four pieces proves

`Re Q_E(T,x)=-log(2*pi)+o(1)`.

## 5. Resolve the finite relative crossover

`VIS-296` established, whenever

`x^2 log x/L -> kappa in (0,infinity)`,

that

`R_gamma(T,x)/(H log x)`
` = 1/(2*pi) + Re Q_E(T,x)/(pi*kappa) + o(1)`.

Substitution now yields

`R_gamma(T,x)/(H log x)`
` = 1/(2*pi) - log(2*pi)/(pi*kappa) + o(1)`.

This also explains the correction structurally. Replacing the coarse gamma scale `L` by `L-log(2*pi)` changes

`H L^2/(2*pi*x^2)`

by

`-H L log(2*pi)/(pi*x^2)`

at leading order; at `x^2 log x/L -> kappa` this is exactly the new constant-order contribution relative to `H log x`. The remaining square of `log(2*pi)` is lower order on that normalization.

The finite-`kappa` correction is therefore a **baseline normalization effect**, not evidence that new arithmetic enters at the `sqrt(L/log L)` relative boundary.

## Prior art and evidence boundary

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918 (2026), uses the decomposition `A=-D_x+B_x+E_x` with `B_x=log(t+2)/x` and `E_x=O(1/x)` in the short-interval pair-correlation argument.

The exact `R(s)` identity used above is inherited from Baluyot, Goldston, Suriajaya, and Turnage-Butterbaugh, **An unconditional Montgomery Theorem for Pair Correlation of Zeros of the Riemann Zeta Function**, arXiv:2306.04799, Lemma 1 and its Landau-formula proof. The functional equation and digamma asymptotic used to isolate `-log(2*pi)` are classical; see NIST DLMF sections 25.4 and 5.11.

No novelty is claimed for those identities or asymptotics. The Mathia contribution here is the channel accounting forced by `VIS-296`: once the exact remainder is averaged in the normalization that survives at the relative boundary, its only leading mean is the classical gamma normalization.

This does **not** close the absolute-`H` crossover at `x=O(sqrt(L))`, produce a source-specific improvement over the Korobov--Vinogradov envelope, justify a moving upper source ceiling, or settle the fixed-power real-axis source branch. Those remain distinct questions in `CLUE-wang-fixed-source-packet-localization`.

## Dependencies

- `VIS-293`: the source Dirichlet-series half-plane and its RH-equivalent pole barrier.
- `VIS-294`: the absolute-`H` lower moving-source `sqrt(L)` crossover.
- `VIS-295`: relative linearization for `x^2 log x >> L`.
- `VIS-296`: reduction of the finite relative boundary to the order-one mean `Q_E`.
- `CLUE-wang-fixed-source-packet-localization`: accepted source-localization clue whose remaining branches are narrowed below.

## Research consequence

The relative moving-source branch is now cleaner than `VIS-296` left it. At finite `x^2 log x/L`, the surviving mean remainder is explicitly deterministic and removable by using the natural gamma normalization rather than Wang's coarse `log(t+2)` baseline. Further work on this branch should therefore not interpret that constant as a new arithmetic signal.

The next lower-boundary question is again the genuinely harder one: after this deterministic gamma normalization is accounted for, can the **absolute `H`-scale** errors near `x=O(sqrt(L))` be sharpened or structurally resolved? That question requires returning to the load-bearing terms in Wang's Proposition 2.6 rather than extending the now-closed relative-mean calculation.