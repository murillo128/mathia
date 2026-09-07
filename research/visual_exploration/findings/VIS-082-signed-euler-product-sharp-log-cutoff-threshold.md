# VIS-082 — the signed Euler-product energy vanishes exactly below the logarithmic cutoff scale

## Claim

Use the critical-line notation of `VIS-079`--`VIS-081`. For finite prime cutoff `X>=2` let

`F_X(u)=P_X(1,u)=prod_(p<=X) (1-p^(-1-iu))^(-1)`

and

`H_X=P_X(2,0)=prod_(p<=X) (1-p^(-2))^(-1)`.

The normalized signed energy is

`T_(X,L)`
` = (2/L^2) integral_0^L (L-u)`
`   [|F_X(u)|^2/H_X - 1] du`.

There is an absolute constant `C` such that for every finite `X>=2` and every `L>0`,

`0 <= T_(X,L) <= C P_X(1,0)/(H_X L)`.

Consequently,

`T_(X,L) << log(2X)/L`.

Combining this upper bound with the support-crowding lower bound of `VIS-080` gives the exact vanishing threshold: for every joint law `X=X(L)>=2` with `L->infinity`,

`T_(X(L),L) -> 0`

if and only if

`log X(L)/L -> 0`.

Thus the unresolved subexponential corridor from `VIS-080` is closed for this witness. No atom-separated Dickman local limit is needed to decide whether the normalized energy vanishes. Such a local theorem could still sharpen constants or asymptotics, but not the zero-versus-nonzero cutoff criterion.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL WEIGHTED-HILBERT INPUT + DECISIVE-NEGATIVE/CLOSURE + NO-NOVELTY-CLAIM`.

No sharp asymptotic constant for `T_(X,L)`, matching two-sided estimate in every joint regime, zeta approximation theorem, or RH consequence is claimed.

## 1. The finite Euler product is an absolutely convergent smooth-number Dirichlet series

Let `S_X` be the multiplicative semigroup of positive integers all of whose prime factors are at most `X`. Since `X` is finite,

`F_X(u)=sum_(n in S_X) n^(-1-iu)`

converges absolutely and uniformly in real `u`, with

`sum_(n in S_X) 1/n = P_X(1,0) < infinity`.

Also

`sum_(n in S_X) 1/n^2 = H_X`.

Therefore termwise multiplication and integration on finite intervals are justified without truncation ambiguity.

Put

`a_n=1/n` for `n in S_X`,

and `a_n=0` otherwise. Writing `lambda_n=log n`, one has

`|F_X(u)|^2`
` = sum_(m,n) a_m a_n exp(iu(lambda_n-lambda_m))`.

Hence for `T>=0`,

`integral_0^T |F_X(u)|^2 du - T H_X`

is exactly the off-diagonal sum

`sum_(m!=n) a_m a_n`
` [exp(iT(lambda_n-lambda_m))-1]`
` / [i(lambda_n-lambda_m)]`.

## 2. Weighted Hilbert controls the entire off-diagonal uniformly in the interval length

For the increasing frequency set `lambda_n=log n` restricted to `S_X`, let

`delta_n=min_(m in S_X, m!=n) |log n-log m|`.

Because `S_X` is a subset of the positive integers, removing frequencies can only increase nearest-neighbor spacing. Thus for `n>=2`,

`delta_n >= log((n+1)/n)`,

and the same bound is harmless at `n=1` after adjusting an absolute constant. Since

`log(1+1/n) >= 1/(n+1)`,

we may use

`1/delta_n <= 2n`

for all support points after an absolute adjustment at the first point.

The weighted Hilbert--Montgomery--Vaughan inequality states that for distinct real frequencies and finite coefficients `z_n`,

`|sum_(m!=n) z_m conjugate(z_n)/(lambda_m-lambda_n)|`
` <= C_H sum_n |z_n|^2/delta_n`

with an absolute constant `C_H`. Apply it first to finite truncations of the support and then pass to the limit. The weighted square sum is finite because

`sum_(n in S_X) a_n^2/delta_n`
` <= 2 sum_(n in S_X) n a_n^2`
` = 2 sum_(n in S_X) 1/n`
` = 2 P_X(1,0)`.

The off-diagonal integral above is the difference of two such Hilbert forms: one with coefficients `a_n`, and one with coefficients `a_n exp(-iT lambda_n)`. The phase rotation leaves their moduli unchanged. Therefore, uniformly for every `T>=0`,

`|integral_0^T |F_X(u)|^2 du - T H_X|`
` <= C_0 P_X(1,0)`

for an absolute constant `C_0`.

This is the only analytic estimate needed for the cutoff threshold.

## 3. The triangular energy inherits the same logarithmic error scale

Define the centered primitive

`A_X(T)=integral_0^T [|F_X(u)|^2/H_X - 1] du`.

The preceding bound gives

`|A_X(T)| <= C_0 P_X(1,0)/H_X`

uniformly in `T`.

Integration by parts in the exact triangular formula from `VIS-079` gives

`integral_0^L (L-u)[|F_X(u)|^2/H_X-1] du`
` = integral_0^L A_X(u) du`.

Therefore

`T_(X,L)`
` <= (2/L^2) integral_0^L |A_X(u)| du`
` <= 2 C_0 P_X(1,0)/(H_X L)`.

The exact sinc-spectrum representation of `VIS-078`--`VIS-080` shows independently that `T_(X,L)>=0`, even though the centered autocorrelation integrand itself need not have one sign.

Now

`P_X(1,0)=prod_(p<=X)(1-p^(-1))^(-1)`

has the classical Mertens scale `~ e^gamma log X`, while

`1 <= H_X <= zeta(2)`.

Hence

`T_(X,L) << log(2X)/L`

uniformly in finite `X` and positive `L`.

## 4. The cutoff criterion is now an equivalence

`VIS-080` proved the converse obstruction: if

`T_(X(L),L)->0`,

then necessarily

`log X(L)/L->0`.

The present upper bound proves sufficiency immediately. If

`log X(L)/L->0`,

then

`0 <= T_(X(L),L) << log(2X(L))/L -> 0`.

Thus

`T_(X(L),L)->0  <=>  log X(L)/L->0`.

The threshold is therefore not a mysterious small-divisor transition. It is the point where the ordinary mean-square error scale of the absolutely convergent smooth-number Dirichlet series ceases to be negligible after triangular normalization. `VIS-080` supplies the matching obstruction from positive near-diagonal coprime ratios.

This also explains why the Dickman scaling law in `VIS-081` is globally informative but unnecessary for the binary cutoff question. The weighted-Hilbert estimate controls the complete off-diagonal aggregate directly, without replacing the pure-point law by a continuous local approximation.

## Prior-art and novelty assessment

H. L. Montgomery and R. C. Vaughan, **Hilbert's Inequality**, *Journal of the London Mathematical Society* s2-8:1 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`, is the classical source of the weighted Hilbert inequality used above. The weighted form controls a nonuniform frequency set by the reciprocal nearest-neighbor spacings. No new Hilbert inequality or Dirichlet-series mean-value theorem is claimed here.

S. M. Gonek and J. P. Keating, **Mean values of finite Euler products**, *Journal of the London Mathematical Society* 82:3 (2010), 763--786, DOI `10.1112/jlms/jdq049`, is the direct finite-Euler-product prior-art boundary. Their work studies when modulus-squared means of finite Euler products factor as independent local means. The present finding does not claim novelty for the mean-square phenomenon; it uses the elementary weighted-Hilbert specialization at `Re(s)=1` to close the specific `VIS-079` normalized triangular-energy threshold.

The Mathia-specific content is therefore the exact bridge between that classical mean-value control and the already-derived positive lower bound `VIS-080`, yielding a sharp necessary-and-sufficient vanishing corridor for this visual witness.

## Boundary and falsification

The result applies to the exact normalized signed squared-Euler-product witness `T_(X,L)` defined in `VIS-079`--`VIS-080`. It does not classify arbitrary nonlinear prime-torus observables, externally anchored windows, hybrid factor/residual statistics, or zeta itself.

The upper bound is an order estimate, not an asymptotic. In regimes where `log X/L` stays bounded away from zero, the theorem does not determine the limiting value of `T_(X,L)`; `VIS-080` only prevents vanishing. A local Dickman theorem or finer finite-Euler-product mean-value analysis may still determine constants or profiles there.

Falsify the argument by finding a failure in one of the exact inputs: absolute convergence of the fixed-`X` smooth-number Dirichlet series, the nearest-neighbor bound for `log n`, applicability of the weighted Hilbert inequality after finite truncation, or the `VIS-079` triangular identity. The joint-limit conclusion additionally depends on the already-persisted lower implication in `VIS-080`.

## Research consequence

The signed growing-support branch of `CLUE-zeta-prime-phase-recursive-geometry` is closed as a positive separator for this witness. The exact normalized energy vanishes throughout the entire subexponential corridor `log X=o(L)`, and outside that corridor any persistence is already forced by generic reduced-ratio support crowding from `VIS-080`.

Accordingly, neither a nonvanishing `T_(X,L)` nor a visually dense near-resonance pattern can provide a discriminating zeta signal through this squared-Euler-product observable. Further work on this branch is justified only if it changes the witness or asks for a finer classical asymptotic rather than reopening the closed zero-versus-nonzero cutoff question.
