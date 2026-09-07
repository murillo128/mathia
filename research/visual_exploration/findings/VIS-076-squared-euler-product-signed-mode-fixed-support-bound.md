# VIS-076 — squared finite Euler products have signed modes but fixed-support O(1/L) window collapse

## Claim

Fix `sigma>0` and a finite prime cutoff `X`. Write

`P_X(sigma,t)=prod_(p<=X) (1-p^(-sigma-it))^(-1)`.

Unlike the holomorphic product in `VIS-075`, the signed observable `|P_X(sigma,t)|^2` has Fourier modes with both positive and negative prime-coordinate exponents. Nevertheless, at every fixed `X` its full signed spectrum has exponentially decaying coefficients, and Baker-type lower bounds for nonzero linear forms in the fixed logarithms `(log p)_(p<=X)` make the coefficient-weighted small-divisor sum finite.

More precisely, put

`lambda_k=sum_(p<=X) k_p log p`

for `k in Z^(pi(X))`, and

`w_k=prod_(p<=X) p^(-sigma |k_p|)`.

Then the absolutely and uniformly convergent Fourier expansion is

`|P_X(sigma,t)|^2`
` = P_X(2 sigma,0) sum_(k in Z^(pi(X))) w_k exp(-i t lambda_k)`.

The zero mode is therefore exactly

`P_X(2 sigma,0)=prod_(p<=X)(1-p^(-2 sigma))^(-1)`.

For the length-`L` moving average

`M_(X,L)(h)=(1/L) integral_h^(h+L) |P_X(sigma,t)|^2 dt`,

termwise integration gives

`M_(X,L)(h)-P_X(2 sigma,0)`
` = P_X(2 sigma,0) sum_(k!=0) w_k exp(-i(h+L/2)lambda_k) sinc(L lambda_k/2)`.

For the fixed prime set there exist constants `c_X>0` and `A_X>0` such that every nonzero integer vector satisfies a Baker lower bound

`|lambda_k| >= c_X (1+||k||_infinity)^(-A_X)`.

Hence

`B_(X,sigma)=sum_(k!=0) w_k/|lambda_k| < infinity`,

and therefore

`sup_h |M_(X,L)(h)-P_X(2 sigma,0)|`
` <= [2 P_X(2 sigma,0) B_(X,sigma)]/L`.

Thus **signed `log(a/b)` near-resonances are real, but at fixed finite prime support they do not by themselves sustain a non-Haar moving-window mean**. The fixed-support squared Euler product converges uniformly in the starting height to its torus/Haar mean at rate `O_(X,sigma)(1/L)`.

The remaining live question is genuinely uniform: how the weighted resonance constant `B_(X,sigma)` behaves when the prime support `X=X(L)` grows. Baker's theorem used here is deliberately not treated as a useful dimension-uniform estimate.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL POISSON/LINEAR-FORMS-IN-LOGARITHMS SPECIALIZATION + DECISIVE-NEGATIVE + NO-NOVELTY-CLAIM`.

No useful asymptotic for `B_(X,sigma)` as `X->infinity`, sharp growing-support threshold, zeta approximation theorem, zero-factor statement, or RH consequence is claimed.

## 1. Exact signed Fourier series

For one prime let `r=p^(-sigma)`. The classical Poisson-kernel identity gives

`|1-r exp(-i theta)|^(-2)`
` = (1-r^2)^(-1) sum_(j in Z) r^(|j|) exp(-i j theta)`.

The series is absolutely and uniformly convergent because `0<r<1`. Multiplying these finitely many one-prime expansions at `theta=t log p` yields

`|P_X(sigma,t)|^2`
` = prod_(p<=X)(1-p^(-2 sigma))^(-1)`
`   * sum_k prod_(p<=X) p^(-sigma |k_p|)`
`     exp(-it sum_(p<=X) k_p log p)`,

which is the claimed formula.

Absolute convergence is immediate from

`sum_k w_k = prod_(p<=X) [1+2 sum_(j>=1) p^(-sigma j)] < infinity`.

This exact factorization is also the grouped smooth-ratio expansion from `VIS-075`. If

`a_k=prod_(k_p>0) p^(k_p)` and `b_k=prod_(k_p<0) p^(-k_p)`,

then `gcd(a_k,b_k)=1`,

`lambda_k=log(a_k/b_k)`,

and

`w_k=(a_k b_k)^(-sigma)`.

So the signed spectrum is indexed by reduced ratios of `X`-smooth integers, with an explicit multiplicative coefficient.

## 2. The small divisors are genuine

Unique factorization gives `lambda_k!=0` for every `k!=0`, but there is generally no positive frequency gap once at least two primes are present. For example, rational approximation to `log 2/log 3` gives integer pairs `(u,v)` for which

`|u log 2-v log 3|`

is arbitrarily small.

Thus `|P_X|^2` really does cross the structural boundary isolated in `VIS-075`: its Fourier support contains both signs and admits cross-prime near-resonances. Replacing the positive-cone product by its modulus square is not merely increasing coefficient mass.

This does **not**, however, imply a persistent finite-window signal. The coefficient attached to a mode with exponent vector `k` decays exponentially in the size of that vector, and that decay must be compared with the small divisor.

## 3. Baker lower bounds beat the fixed-support resonance tail

For the fixed algebraic numbers `p<=X`, classical lower bounds for nonzero linear forms in logarithms imply constants `c_X,A_X>0` such that

`|sum_(p<=X) k_p log p|`
` >= c_X (1+||k||_infinity)^(-A_X)`

for every nonzero integer vector `k`.

The precise constants are irrelevant here; only polynomial growth of the reciprocal small divisor is needed. Since every prime is at least `2`,

`w_k <= 2^(-sigma ||k||_1)`.

The number of integer vectors with `||k||_1=n` grows only polynomially in `n` for fixed dimension `pi(X)`. Therefore

`sum_(k!=0) w_k/|lambda_k|`
` <= c_X^(-1) sum_(k!=0) 2^(-sigma ||k||_1) (1+||k||_infinity)^(A_X)`
` < infinity`.

This is the decisive fixed-support step. Arbitrarily small signed frequencies exist, but they occur only at exponent heights where the analytic Euler-factor coefficients have already decayed exponentially enough to make the weighted reciprocal-frequency series summable.

## 4. Uniform moving-window bound

Absolute uniform convergence of the Fourier series permits integration term by term. For every `k!=0`,

`(1/L) integral_h^(h+L) exp(-it lambda_k) dt`
` = exp(-i(h+L/2)lambda_k) sinc(L lambda_k/2)`.

Using

`|sinc y|<=min(1,1/|y|)`

and the finite constant `B_(X,sigma)` gives

`sup_h |M_(X,L)(h)-P_X(2 sigma,0)|`
` <= (2 P_X(2 sigma,0)/L) B_(X,sigma)`.

The bound is uniform in the window start `h`. This is stronger than merely invoking fixed-dimensional unique ergodicity: it gives an explicit `1/L` rate once the fixed-support coefficient-weighted resonance constant is accepted.

`VIS-072` proved the same sinc mechanism for finite trigonometric-polynomial witnesses. The present observable is not a finite Fourier polynomial even at fixed `X`; the new control is that its infinite signed Fourier tail is absolutely summable after division by the small divisor.

## 5. Growing support remains the real boundary

Nothing above makes `B_(X,sigma)` harmless as `X` grows. The number of prime coordinates increases, the set of signed smooth ratios becomes richer, and the constants supplied by general linear-forms-in-logarithms bounds deteriorate with the dimension and the primes involved.

Therefore the statement

`sup_h |M_(X,L)(h)-P_X(2 sigma,0)| -> 0`

under a joint limit `X=X(L)->infinity` requires a genuinely uniform estimate on the exact weighted signed spectrum. The fixed-support theorem does not supply one.

This sharply separates two questions that a visualization can otherwise conflate:

- signed beat patterns at one frozen prime cutoff are part of the same finite prime-torus null and disappear in sufficiently long windows;
- persistence while the prime support itself grows is a different asymptotic problem and must be tested against a dimension-dependent quantitative mean-value/small-divisor theory.

## 6. Prior art and novelty boundary

The ingredients are classical and the finding makes no general novelty claim.

S. M. Gonek and J. P. Keating, **Mean values of finite Euler products**, *Journal of the London Mathematical Society* 82:3 (2010), 763–786, DOI `10.1112/jlms/jdq049`, explicitly studies mean values of the modulus squared of finite Euler products and, in particular, when those means factor as the product of the mean squares of the individual Euler factors. This is the nearest direct prior-art boundary: modulus-square mean values of finite Euler products are an established analytic-number-theory object, including nontrivial regimes in which the cutoff varies.

A. Baker, **Linear forms in the logarithms of algebraic numbers (IV)**, *Mathematika* 15:2 (1968), 204–216, DOI `10.1112/S0025579300002588`, is a classical source for effective lower bounds on nonzero linear forms in logarithms of fixed algebraic numbers. The present proof uses only the qualitative consequence that, for a fixed finite set of primes, `1/|lambda_k|` grows at most polynomially in the integer coefficient height.

The one-variable Poisson-kernel Fourier expansion and the product construction are standard harmonic analysis. The Mathia-specific delta is only the control diagnosis at the current visual frontier: **introducing signed frequencies with `|P_X|^2` is not yet an escape at fixed `X`, because analytic coefficient decay beats the fixed-dimensional small divisors.**

## Boundary and falsification

The theorem concerns the linear moving-window average of the exact squared modulus of a raw finite Euler product at fixed `sigma>0` and fixed finite `X`. It does not cover maxima, threshold events, phase-unwrapped observables, adaptive windows, general nonlinear path functionals, or an independently defined hybrid residual.

The `O(1/L)` constant depends on `X` and `sigma` and is not asserted to be small or useful numerically. No extrapolation to `X=X(L)` is permitted without a uniform estimate.

Falsify the exact result by producing a Fourier coefficient of `|P_X|^2` that differs from the displayed Poisson-product coefficient, a nonzero prime-log linear form violating the stated fixed-set Baker consequence, or a fixed `X,sigma` for which the weighted reciprocal-frequency series diverges.

## Research consequence

The first signed example left open by `VIS-075` is now closed at fixed prime support. `|P_X|^2` genuinely contains arbitrarily small `log(a/b)` frequencies, but those resonances are exponentially suppressed in Fourier coefficient size strongly enough that every fixed-support moving-window mean still collapses uniformly to the Haar value `P_X(2 sigma,0)` at `O_(X,sigma)(1/L)`.

For `CLUE-zeta-prime-phase-recursive-geometry`, a signed finite-window escape must therefore be **growing-support** (or use genuinely independent anchor/residual information). The next quantitative object is not the mere existence of small divisors, but the joint growth of the coefficient-weighted resonance sum as new prime coordinates are admitted.