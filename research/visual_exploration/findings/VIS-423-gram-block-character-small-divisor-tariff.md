# VIS-423 — Gram blocks obey an explicit character small-divisor tariff

## Claim

Let `g_k` be the ordinary Gram points, indexed for all sufficiently large `k` by

`theta(g_k)=k pi`,

and let `alpha` be a nonzero real frequency. For

`E_N(alpha)=(1/N) sum_(N<k<=2N) exp(i alpha g_k)`,

there is an absolute constant `C` such that, for all sufficiently large `N`,

`|E_N(alpha)| <= C(1/N + |alpha|/log N + (log N)/(N |alpha|))`.

Thus a single Gram-point character is quantitatively small whenever

`(log N)/N << |alpha| << log N`.

More generally, let

`P_N(z)=sum_(m in S_N) c_(N,m) z^m`

be any finite Laurent polynomial on a finite prime torus, where the finite prime set and Fourier support may depend on `N`. Put

`nu_m=sum_p m_p log p`.

Unique factorization gives `nu_m!=0` for every nonzero character. If `c_(N,0)` denotes the Haar mean, then

`| (1/N) sum_(N<k<=2N) P_N((p^(-i g_k))_p) - c_(N,0) |`

is at most

`C[ A_0(N)/N + A_1(N)/log N + (log N/N) A_(-1)(N) ]`,

where

`A_0(N)=sum_(m!=0)|c_(N,m)|`,

`A_1(N)=sum_(m!=0)|c_(N,m)| |nu_m|`,

and

`A_(-1)(N)=sum_(m!=0)|c_(N,m)|/|nu_m|`.

Consequently any changing family satisfying

`A_0(N)=o(N)`,

`A_1(N)=o(log N)`,

`A_(-1)(N)=o(N/log N)`

has its Gram-block average converging to its own Haar mean even though the polynomial, prime support, and character set vary with `N`.

**Evidence/status:** `EXACT-DERIVED + QUANTITATIVE CONTROL + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

This is a sufficient character-polynomial control, not a general quantitative equidistribution theorem for every growing-dimensional observable. No RH consequence, optimal rate, or novelty claim is asserted.

## 1. Invert the Gram phase on one dyadic block

For large real `x`, let `g(x)` be the smooth inverse defined by

`theta(g(x))=pi x`.

The standard Riemann--Siegel theta asymptotics give, uniformly on the dyadic Gram interval corresponding to `x in [N,2N]`,

`theta'(t)=(1/2) log(t/(2 pi))+O(t^(-2))`,

`theta''(t)=1/(2t)+O(t^(-3))`.

In particular,

`g'(x)=pi/theta'(g(x))`,

`g(2N)-g(N)=O(N/log N)`,

and `log g(2N)=O(log N)`.

Set

`f(x)=exp(i alpha g(x))`.

A first-order Euler summation estimate gives

`sum_(N<k<=2N) f(k)=integral_N^(2N) f(x) dx + O(1+integral_N^(2N)|f'(x)| dx)`.

Since

`|f'(x)|=|alpha| g'(x)`,

the variation term is exactly

`|alpha|[g(2N)-g(N)]=O(|alpha| N/log N)`.

After division by `N`, this produces the middle term `O(|alpha|/log N)` in the claim.

## 2. The integral pays the reciprocal frequency

For the main integral, use `x=theta(t)/pi` and `dx=theta'(t)dt/pi`:

`J_N(alpha)=integral_N^(2N) exp(i alpha g(x)) dx`

`=(1/pi) integral_(g(N))^(g(2N)) theta'(t) exp(i alpha t) dt`.

Integration by parts gives

`J_N(alpha)`
`=[theta'(t) exp(i alpha t)/(i pi alpha)]_(g(N))^(g(2N))`
` -(1/(i pi alpha)) integral_(g(N))^(g(2N)) theta''(t) exp(i alpha t) dt`.

On this interval the boundary values of `theta'` are `O(log N)`, while

`integral_(g(N))^(g(2N)) |theta''(t)| dt=O(1)`.

Therefore

`|J_N(alpha)|=O(log N/|alpha|)`.

Combining this with the Euler-summation endpoint term and the variation term yields

`|E_N(alpha)| <= C(1/N + |alpha|/log N + (log N)/(N|alpha|))`.

The estimate is deliberately elementary and not optimized. Its useful feature here is that both ways a changing character can escape the fixed-frequency Gram-point Haar limit are visible: its frequency can grow too quickly, or it can become a sufficiently severe small divisor.

## 3. A triangular-array polynomial criterion

For a nonzero prime-torus character `z^m`, sampling at a Gram point gives

`z(g_k)^m=exp(-i nu_m g_k)`

with

`nu_m=sum_p m_p log p=log(prod_p p^(m_p))`.

If `nu_m=0`, unique factorization would force every `m_p=0`. Hence every nonconstant character may be bounded by the scalar estimate above.

Expanding `P_N` and applying the triangle inequality gives

`| (1/N) sum_(N<k<=2N) P_N(z(g_k)) - c_(N,0) |`

`<= sum_(m!=0) |c_(N,m)| |E_N(-nu_m)|`,

which is exactly the three-tariff bound in the claim. The conditions on `A_0`, `A_1`, and `A_(-1)` are therefore a direct sufficient criterion for a changing Laurent-polynomial family to retain the Haar mean along dyadic Gram blocks.

This is not the same as saying that an increasing-dimensional Gram phase vector converges in one fixed ambient probability space. It controls only the changing observables whose Fourier mass satisfies the displayed tariff, which is the form needed for the current Wang-shell question.

## 4. Consequence for the growing-shell Wang escape route

`VIS-422` used Laurincikas's qualitative prime-torus theorem to close ordinary Gram points as an anomalous selector for every **fixed** finite Wang shell and fixed continuous observable. It deliberately left a growing-shell/height regime open because fixed-test-function weak convergence gives no uniform rate.

The present estimate closes a nontrivial part of that gap. Whenever a changing Wang-shell diagnostic can be represented, or uniformly approximated, by Laurent polynomials whose coefficient mass obeys the three tariff conditions above, its Gram-block average is forced back to the corresponding Haar mean. A growing shell does not evade the fixed-shell null merely because the number of active primes or characters increases.

For a proposed Gram-point anomaly to lie outside this control, at least one genuine obstruction must remain visible in the approximating Fourier family: substantial high-frequency mass through `A_1`, severe near-resonant prime-log characters through `A_(-1)`, excessive total Fourier mass through `A_0`, or a nonlinear/tail observable whose uniform Fourier approximation error cannot be made negligible together with those costs.

This is especially important for the accepted normalized-amplitude and persistence clue. Absolute value, supremum over a time window, and tail indicators are not finite character polynomials. `VIS-423` therefore does not declare those growing-shell statistics Haar. It converts the phrase "needs a uniform quantitative theorem" into an explicit sufficient route: construct a uniform torus approximation and pay its Gram character tariff. If that route fails, the failure mode itself identifies what the next analysis must explain.

## 5. Prior art and novelty audit

Antanas Laurincikas, **Joint Discrete Approximation of Analytic Functions by Shifts of the Riemann Zeta-Function Twisted by Gram Points**, *Mathematics* 11:3 (2023), 565, DOI `10.3390/math11030565`, proves the qualitative Gram-point prime-torus Haar convergence used in `VIS-422` as part of a stronger discrete-universality argument. Related short-interval and Gram-point universality papers likewise use exponential-sum/equidistribution machinery.

A targeted search for quantitative Gram-point equidistribution, Gram-point Weyl sums, and estimates for `sum exp(i alpha g_k)` did not locate a source asserting the particular elementary two-sided frequency tariff displayed here. That search is not evidence of novelty. The proof above is only Euler summation plus integration by parts against the classical Riemann--Siegel theta asymptotics, and a comparable estimate may be implicit in the discrete-universality literature.

Accordingly no novelty is claimed for Gram-point equidistribution, inverse-Gram asymptotics, Euler summation, exponential-sum estimates, or Fourier-character criteria. The durable Mathia content is the explicit control boundary for the live growing-shell Wang/Gram question.

## 6. Boundaries and falsification

The bound is useful but intentionally crude. For frequencies outside the window where its right-hand side tends to zero, it does not assert non-equidistribution; it merely stops certifying cancellation. Stronger oscillatory estimates can improve this sufficient region.

The polynomial criterion concerns first empirical moments. Distributional or tail convergence of a changing nonlinear observable needs a uniformly controlled approximation by suitable test functions or a separate argument. In particular, a small average error for a polynomial surrogate does not by itself control a discontinuous low-tail indicator at an atom or poorly regular boundary.

The dyadic block `N<k<=2N` is used only to keep the Gram scale uniform. Fixed index shifts in the definition of Gram points change no conclusion.

Falsify the derivation by showing that, on large dyadic blocks, the inverse-Gram variation is not `O(N/log N)`, the stated theta derivative asymptotics fail, the integration-by-parts estimate is incorrect, or a nonzero integer prime character has `nu_m=0`. Any such failure would break a displayed step directly.

## Dependencies

- `VIS-419`: fixed Wang shells are Laurent character polynomials on the base-prime torus.
- `VIS-420`: continuous-translation calibration already exhibits the corresponding prime-log small-divisor cost.
- `VIS-421`: any distinguished-height panel is a separate selector/interface choice.
- `VIS-422`: ordinary Gram points are qualitatively Haar for every fixed finite prime shell.

## Research consequence

The accepted Wang phase-anchoring clue should keep ordinary Gram points only as a **growing-family** candidate, and even there only after checking this character tariff. Before numerical evaluation, any proposed polynomial or Fourier approximation to the changing shell statistic should expose `A_0`, `A_1`, and `A_(-1)`. If all three sufficient costs vanish, the Gram selector is already certified asymptotically Haar for that observable family and the anomaly route should be killed rather than simulated.