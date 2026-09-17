# VIS-271 — Wang's fixed-alpha source scale does not preserve fixed Rodgers prime labels

## Claim

The first-prime packet of `VIS-270` is source-selective for the Rodgers quadratic carrier, but it is **not** source-selective for the same fixed prime inside Wang's short-interval explicit-formula mechanism.

In Wang's notation,

`D_x(t)=sum_(n>=2) a_n(x) n^(-it)`

with

`a_n(x)=Lambda(n)/sqrt(n) min(n/x,x/n)`.

The pair-correlation variable is parameterized by

`x=T^alpha`.

Fix any `epsilon>0` and restrict to a compact positive Fourier band

`epsilon <= alpha <= lambda < theta`.

Then for every fixed finite set `S` of prime powers, removing the terms indexed by `S` from `D_(T^alpha)` changes its short-interval mean-square energy by

`O_S(H sqrt(log T) T^(-epsilon))=o(H)`

uniformly on that band. In particular, the fixed prime `p=2` cannot contribute at the `H` scale hidden by the `O(H)` remainder in Wang's Proposition 2.6 on any fixed positive-alpha band.

Equivalently, a fixed prime `p` sits naturally in Wang's explicit formula near

`alpha_p(T)=log(p)/log(T) -> 0`,

whereas the Rodgers quadratic carrier samples the same prime at the fixed frequency

`xi_p=log(p)/(2*pi)`.

These are different asymptotic source coordinates. Evaluating the same smooth test function at `alpha=xi_2` in Wang and at `q=xi_2` in the Rodgers carrier is algebraically legitimate, as used in `VIS-270`, but it does **not** identify the underlying arithmetic source: Wang's fixed band near `xi_2` probes prime-power scale `n` near `T^(xi_2)`, not the fixed prime `2`.

Thus a direct sharpening of Wang's present fixed-alpha proof cannot turn the first-prime Rodgers sample isolated by `VIS-270` into a same-source short-interval secondary coefficient merely by resolving the existing `O(H)` term. Such a transfer would require an additional theorem that reorganizes Wang's collective growing-prime scale into the fixed-prime Rodgers carrier, or a different scaling regime approaching `alpha=0`.

**Evidence/status:** `EXACT-DERIVED FROM WANG'S EXPLICIT-FORMULA COEFFICIENTS + SOURCE-SCALE OBSTRUCTION + LITERATURE-GROUNDED NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No absence of all lower-order terms in short-interval pair correlation is claimed. No contradiction with Rodgers' macroscopic expansion, Chan's second-main-term results in a different pair-correlation regime, or the algebraic packet construction of `VIS-270` is claimed.

## 1. Fixed primes are exponentially suppressed on a fixed Wang band

Biao Wang's short-interval proof uses

`a_n(x)=Lambda(n)/sqrt(n) min(n/x,x/n)`.

Let `S` be any fixed finite set of prime powers. Once `x>max(S)`, every `n in S` lies on the `n/x` side of the minimum, so

`a_n(x)=Lambda(n) sqrt(n)/x`.

Write

`D_(x,S)(t)=sum_(n in S) a_n(x)n^(-it)`.

Because `S` is fixed,

`sup_t |D_(x,S)(t)| <= C_S/x`

and therefore on `I=(T,T+H]`,

`||D_(x,S)||_(L^2(I)) <= C_S sqrt(H)/x`.

Wang's Lemma 2.5 and the Montgomery-Vaughan mean-value step give, uniformly for `x<=T^lambda`,

`||D_x||_(L^2(I))^2 = H log x + O(H+x log^2(2x))`.

For `x=T^alpha`, `epsilon<=alpha<=lambda<theta` and `H=T^theta`, this implies

`||D_x||_(L^2(I)) = O(sqrt(H log T))`.

Now remove the finite packet:

`D_x = D_(x,S) + D_(x,S^c)`.

The energy difference satisfies

`| ||D_x||_2^2 - ||D_(x,S^c)||_2^2 |`

` <= 2 ||D_(x,S)||_2 ||D_x||_2 + ||D_(x,S)||_2^2`

` = O_S(H sqrt(log T)/x + H/x^2)`.

Uniformly for `alpha>=epsilon`, this is

`O_S(H sqrt(log T) T^(-epsilon))=o(H)`.

This includes both the direct fixed-prime energy and every cross term between that finite packet and the rest of Wang's Dirichlet polynomial. The conclusion is therefore stronger than observing that the individual diagonal coefficient is small.

## 2. The arithmetic scale in Wang moves with `T`

The coefficient profile also makes the source scale transparent. The factor

`min(n/x,x/n)`

is largest around `n approximately x`. With `x=T^alpha`, a fixed positive `alpha` therefore probes von-Mangoldt mass around a prime-power scale growing like `T^alpha`.

Conversely, to keep one fixed prime `p` near the center of this coefficient profile requires

`T^alpha approximately p`,

hence

`alpha approximately log(p)/log(T)`.

For every fixed `p`, this tends to zero as `T` grows.

This is the exact scaling distinction relevant to `VIS-270`. Its first-prime Rodgers packet is centered at the fixed test-function coordinate

`xi_2=log(2)/(2*pi) approximately 0.110317`.

Putting the same function into Wang's theorem at `alpha=xi_2` means

`x=T^(xi_2)`,

so the Wang explicit formula is centered on prime powers of size `T^(xi_2)`. The actual `n=2` coefficient is already on the small-`n` tail and has size

`a_2(T^(xi_2)) = Lambda(2) sqrt(2) T^(-xi_2)`.

The identical numerical test coordinate therefore has different source semantics in the two expansions.

## 3. What remains inside Wang's `O(H)` remainder

Wang proves

`sum_(n>=2) a_n(x)^2 = log x + O(1)`

and consequently

`int_I |D_x(t)|^2 dt = H log x + O(H+x log^2(2x))`.

His Proposition 2.6 then gives

`F_I(x) = H/(2*pi) [L^2/x^2 + log x]`

plus errors including an unspecialized `O(H)` term and terms that decay with positive powers of `1/x` or are negligible when `x<=T^lambda`, `lambda<theta`.

The estimate above shows that no fixed finite set of prime powers can account for an `H`-scale part of that remainder on `alpha>=epsilon`. The unresolved `O(H)` is instead compatible with collective arithmetic from the growing coefficient range, including whatever bounded remainder remains after replacing the full weighted von-Mangoldt energy by `log x`.

This does **not** prove that the `O(H)` has a scalar secondary asymptotic, nor that it is free of finer arithmetic. It only rules out interpreting its `H` scale as the direct survival of any fixed finite Rodgers prime-power packet in Wang's fixed-positive-alpha source decomposition.

## 4. Consequence for the `VIS-270` transfer question

`VIS-270` remains algebraically correct: one fixed smooth function can simultaneously annihilate Wang's leading functional

`g(0)+int |alpha|g(alpha)dalpha`

and isolate the `p=2,m=1` sample in the Rodgers quadratic carrier. That is a useful test-function interface result.

What fails is the stronger source interpretation one might next try to infer from it. The two formulas attach different arithmetic scales to the same fixed test coordinate. In Rodgers, the derivative sample at `xi_2` is explicitly labelled by the fixed prime `2`; in Wang at fixed `alpha=xi_2`, the explicit formula is asymptotically supported on integers growing like `T^(xi_2)` and the direct `p=2` contribution vanishes far below the theorem's `H`-scale remainder.

Therefore the next theorem-transfer problem cannot be merely:

"sharpen Wang's `O(H)` and read off the first-prime Rodgers coefficient."

A valid transfer would need an additional mechanism showing how the collective `n approximately T^alpha` arithmetic in Wang reorganizes, after the relevant integral transform and lower-order expansion, into Rodgers' fixed prime-power sampler. No such mechanism is present in Wang's current proof.

The other possible route is to move Wang's band toward

`alpha=log(2)/log(T) -> 0`

so that the explicit formula tracks the literal fixed prime. But that is a different asymptotic regime from the fixed-support hypothesis used in `VIS-270`, and in Rodgers coordinates it moves away from the fixed sample `xi_2`. The mismatch is therefore structural rather than a choice of packet width.

## 5. Prior-art and novelty boundary

The decisive source is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026). Theorem 2.2 gives the short-interval fixed-support pair-correlation formula; equations (2.7)--(2.9) define the explicit-formula decomposition and the coefficients `a_n`; Lemma 2.5 gives `sum a_n^2=log x+O(1)`; Proposition 2.6 and equation (2.19) propagate this to the `H log x + O(H+...)` mean-square scale. The finite-source estimate above is an elementary consequence of those displayed coefficients plus Cauchy-Schwarz.

Siegfred Alan C. Baluyot, Daniel Alan Goldston, Ade Irma Suriajaya, and Caroline L. Turnage-Butterbaugh, **An unconditional Montgomery Theorem for Pair Correlation of Zeros of the Riemann Zeta Function**, *Acta Arithmetica* 214 (2024), 357--376, arXiv:2306.04799, is the global explicit-formula framework that Wang adapts. Its Theorem 1 likewise expresses the fixed-alpha pair correlation through `x=T^alpha`, reinforcing that this moving arithmetic scale is standard Montgomery machinery rather than a new Mathia construction.

Tsz Ho Chan, **More precise pair correlation of zeros and primes in short intervals**, arXiv:math/0206292 (2002), derives second main terms in a related strong-pair-correlation/prime-short-interval setting under RH and additional asymptotic hypotheses. That literature prevents a blanket claim that pair-correlation secondary terms are absent or necessarily universal. The present finding is narrower: within Wang's current fixed-positive-alpha explicit-formula decomposition, a finite set of fixed prime powers is `o(H)` and therefore cannot itself be the source of the `H`-scale remainder.

Brad Rodgers, **Macroscopic Pair Correlation of the Riemann Zeroes for Smooth Test Functions**, *Quarterly Journal of Mathematics* 64:4 (2013), 1197--1219, arXiv:1203.3275, remains the external source for the fixed prime-power lower-order carrier already audited in `VIS-260`--`VIS-264`. This finding does not rederive that carrier; it compares its fixed prime labels with the moving source scale visible directly in Wang's coefficients.

No novelty is claimed for the elementary estimate or for the observation that `x=T^alpha` makes the arithmetic scale move with `T`. The durable value is the explicit obstruction it places on the proposed cross-statistic source transfer.

## Boundaries and falsification

The result applies on bands bounded away from `alpha=0`. It does not control a test family whose support approaches zero with `T`; such a regime requires a new uniform version of Wang's theorem and separate conditioning analysis.

The result removes any **fixed finite** prime-power set from the `H` scale. It does not rule out lower-order information produced collectively by prime powers with size growing with `T`, nor an identity that transforms such collective information into a fixed-prime expansion after additional analysis.

It also does not invalidate the test-function construction of `VIS-270`. That finding explicitly stopped short of asserting coefficient transfer. The present result answers its next source-level question by showing why the most direct transfer interpretation is unavailable.

A falsification would require either an error in the displayed Wang coefficient formula or a derivation showing that deleting a fixed finite prime-power set changes Wang's fixed-positive-alpha statistic at `Theta(H)` despite the `L^2` estimate above. A different statistic or a shrinking-alpha scaling would be a new regime, not a counterexample.

No untouched confirmation-zero data are used.

## Research consequence

The useful next question is no longer whether the first-prime `VIS-270` packet exists; it does. Nor is it enough to ask for the constant hidden in Wang's present `O(H)`.

The live transfer question is whether there is a mathematically justified transform from Wang's **collective moving prime scale** `n approximately T^alpha` to the fixed-prime lower-order carrier appearing in Rodgers, with enough uniformity to survive the Wang-leading-null test. Without such a transform, the first-prime packet should be treated as a cross-statistic calibration coordinate rather than evidence that the same prime source survives in short-interval pair correlation.
