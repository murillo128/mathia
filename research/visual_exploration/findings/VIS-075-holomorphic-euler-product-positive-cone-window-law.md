# VIS-075 — holomorphic finite Euler products have positive-cone mixed frequencies

## Claim

Fix `sigma>0` and a finite prime cutoff `X`. Write

`P_X(sigma,t)=prod_(p<=X) (1-p^(-sigma-it))^(-1)`

and let `S_X` be the multiplicative semigroup of positive integers whose prime factors are all at most `X`. Since the product contains only finitely many absolutely convergent geometric factors,

`P_X(sigma,t)=sum_(n in S_X) n^(-sigma) exp(-i t log n)`

with absolute and uniform convergence in `t`.

Thus exponentiating the additive log-Euler field does create mixed-prime Fourier characters, but every nonconstant character lies in the **nonnegative prime-exponent cone**. Its vertical frequency is

`lambda_n=log n >= log 2`.

There is therefore no cross-prime small-divisor cancellation inside the holomorphic finite Euler product itself: mixed prime support is not enough; signed exponent differences are required to create frequencies `log(a/b)` close to zero.

For the length-`L` window average

`W_(X,L)(h)=(1/L) integral_h^(h+L) P_X(sigma,t) dt`,

direct termwise integration gives

`W_(X,L)(h)-1`
` = sum_(n in S_X, n>=2) n^(-sigma) exp(-i(h+L/2)log n)`
`   * sinc(L log n/2)`,

and hence the exact coefficient-weighted bound

`sup_h |W_(X,L)(h)-1|`
` <= (2/L) sum_(n in S_X, n>=2) n^(-sigma)/log n`
` = (2/L) integral_sigma^infinity (P_X(u,0)-1) du`
` <= 2(P_X(sigma,0)-1)/(L log 2)`.

The obstruction to a short uniform averaging corridor for `P_X` is therefore **coefficient-mass growth**, not a near-zero-frequency denominator.

For fixed `0<sigma<1`, the prime number theorem gives

`log P_X(sigma,0)`
` = sum_(p<=X) -log(1-p^(-sigma))`
` ~ X^(1-sigma)/((1-sigma) log X)`.

In particular,

`log P_X(1/2,0) ~ 2 sqrt(X)/log X`.

Consequently the crude final bound above already gives a fully explicit sufficient uniform-collapse corridor: for every fixed `epsilon>0`,

`log L >= (2+epsilon) sqrt(X)/log X`

for all sufficiently large `X` implies

`sup_h |W_(X,L)(h)-1| -> 0`.

This corridor is intentionally not claimed sharp; the exact weighted integral can be much smaller than the `1/log 2` bound.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL DIRICHLET/ALMOST-PERIODIC SPECIALIZATION + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No sharp growing-support threshold, zeta-approximation theorem, signed nonlinear-statistic bound, zero-factor statement, or RH consequence is claimed.

## 1. The finite Euler product is an absolutely convergent smooth-number Dirichlet series

For each fixed prime `p<=X`,

`(1-p^(-sigma-it))^(-1)=sum_(k>=0) p^(-k sigma) exp(-i k t log p)`

absolutely and uniformly in `t`, because `p^(-sigma)<1`. Multiplying the finitely many factors gives

`P_X(sigma,t)`
` = sum_(m_p>=0) prod_(p<=X) p^(-sigma m_p) exp(-it sum_(p<=X) m_p log p)`.

Unique factorization identifies `n=prod p^(m_p)` and converts this to the displayed sum over `S_X`. Absolute convergence follows from

`sum_(n in S_X) n^(-sigma)=prod_(p<=X)(1-p^(-sigma))^(-1)<infinity`.

The Fourier support is mixed in the sense that one character may involve many prime coordinates, but its exponent vector has no negative component. Therefore

`sum_p m_p log p = log n`

cannot exhibit cancellation between different prime logarithms.

This is the structural distinction missed by the broad boundary sentence in `VIS-074`: holomorphic multiplication can mix coordinates without producing the signed small divisors of a general torus Fourier box.

## 2. Window averaging sees coefficient mass but no small divisor

Absolute uniform convergence permits integration term by term. For `n>=2`,

`(1/L) integral_h^(h+L) exp(-it log n) dt`
` = exp(-i(h+L/2)log n) sinc(L log n/2)`.

Using

`|sinc y|<=min(1,1/|y|)`

and `log n>=log 2` gives the displayed pointwise estimates.

The integral identity for the weighted coefficient mass is also exact:

`n^(-sigma)/log n = integral_sigma^infinity n^(-u) du`.

All terms are nonnegative at `t=0`, so Tonelli gives

`sum_(n in S_X,n>=2) n^(-sigma)/log n`
` = integral_sigma^infinity sum_(n in S_X,n>=2) n^(-u) du`
` = integral_sigma^infinity (P_X(u,0)-1) du`.

Thus the finite-window problem for the holomorphic product is a weighted mass problem. There is no hidden `1/|log(a/b)|` factor in this representation.

## 3. Growing support can still make the corridor extremely expensive

Absence of small divisors does not imply a dimension-free useful window length. For fixed `0<sigma<1`,

`log P_X(sigma,0)`
` = sum_(p<=X) p^(-sigma) + O(sum_(p<=X) p^(-2sigma)/(1-p^(-sigma)))`.

The error is lower order than the first sum for every fixed `sigma>0`. Prime-number-theorem partial summation gives

`sum_(p<=X) p^(-sigma)`
` ~ X^(1-sigma)/((1-sigma)log X)`,

which proves the stated product-mass asymptotic.

At `sigma=1/2`, the elementary `1/log 2` window bound therefore becomes useful only once `L` beats an exponential-in-`sqrt(X)/log X` coefficient scale. This is much worse than the additive corridor in `VIS-074`, but for a completely different reason: the analytic exponentiation has accumulated many positive-cone coefficients rather than created near-zero frequencies.

The exact integral

`integral_sigma^infinity (P_X(u,0)-1) du`

is the correct quantity for any sharper witness-specific analysis. No asymptotic for that integral is needed for the present structural conclusion.

## 4. Signed mixing is where `log(a/b)` re-enters

The distinction becomes explicit for a holomorphic-antiholomorphic observable. For example,

`|P_X(sigma,t)|^2`
` = sum_(a,b in S_X) (ab)^(-sigma) exp(-it log(a/b))`.

Now exponent vectors occur with both signs. Distinct `X`-smooth integers `a` and `b` can have `log(a/b)` much smaller than `log 2`, so the small-divisor geometry from `VIS-072`--`VIS-073` genuinely returns.

The same warning applies to ratios, signed cross-products, or nonlinear/path observables whose actual Fourier expansion contains both positive and negative prime-coordinate exponents. By contrast, merely saying that an observable is nonlinear or mixes primes is not enough: its **signed Fourier support** must be inspected.

This supplies a cleaner visual-control classification:

- coordinate-separable additive prime harmonics: `VIS-074` weighted one-coordinate corridor;
- holomorphic mixed-prime Euler-product characters: positive-cone law and coefficient-mass corridor here;
- signed mixed-coordinate observables: potential `log(a/b)` small divisors, requiring the quantitative controls of `VIS-072`--`VIS-073` or a sharper witness-specific theorem.

## 5. Prior art and novelty boundary

The finite Euler-product expansion, smooth-number Dirichlet series, and almost-periodic vertical interpretation are classical. The existing source anchor S. M. Gonek, **Finite Euler products and the Riemann hypothesis** (2012), already bounds any claim that finite Euler products themselves or their critical-strip use are new. The general almost-periodic interpretation is part of classical Bohr Dirichlet-series theory; a targeted literature audit found the same modern framing in Schoolmann, **On Bohr's theorem for general Dirichlet series** (2020).

No new theorem in Dirichlet-series theory or almost periodicity is claimed. The Mathia-specific delta is the control diagnosis forced by the active visual thread: the boundary after `VIS-074` is not “nonlinear mixing versus additive coordinates.” It is finer. Holomorphic exponentiation mixes coordinates while retaining a one-sided frequency cone; near-resonant ratio geometry begins only when the chosen observable introduces signed exponent differences.

## Boundary and falsification

The result concerns the raw holomorphic truncated product `P_X(sigma,t)` and its linear continuous-time window average. It does not cover `|P_X|`, `|P_X|^2`, ratios, phase-unwrapped statistics, maxima, zero-sensitive transforms, or arbitrary nonlinear path functionals unless their actual Fourier support is separately analyzed.

The uniform-collapse condition derived from `P_X(sigma,0)` is sufficient and deliberately crude. Failure to satisfy it is not evidence of arithmetic-specific structure; it only means coefficient mass defeats this simple bound.

Falsify the exact result by producing a nonconstant Fourier character in the raw holomorphic product with a negative prime exponent, a frequency smaller than `log 2`, or a directly integrated window average exceeding the displayed weighted coefficient bound.

## Research consequence

`VIS-074` correctly closes additive log-Euler growth but states its nonlinear boundary too broadly. Exponentiating to the raw holomorphic finite Euler product does **not** restore cross-prime small divisors: its mixed characters remain in the positive exponent cone. The next admissible prime-torus visual question must therefore distinguish coefficient-mass growth from genuinely signed mixed-coordinate resonance.

For `CLUE-zeta-prime-phase-recursive-geometry`, a proposed finite-window escape based only on the raw holomorphic Euler product should first be tested against the exact positive-cone bound here. The small-divisor route becomes live only after the statistic introduces signed mode differences, or after genuinely independent anchor/residual information enters the observable.