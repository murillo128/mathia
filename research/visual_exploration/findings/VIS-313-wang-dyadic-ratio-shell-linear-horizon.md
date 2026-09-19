# VIS-313 — dyadic ratio shells give a cutoff-free near-linear finite-window horizon

## Claim

Keep Wang's grouped remainder and coefficients from `VIS-309`--`VIS-312`,

`D_x(t)=sum_(q=p^k) a_q q^(-it)`,

`a_q=(Lambda(q)/sqrt(q)) min(q/x,x/q)`,

`R_(x,H)(T)=sum_(lambda!=0) B_lambda exp(-i lambda T)`,

and put `L=log(3x)`. Split the grouped spectrum at the fixed ratio boundary `|lambda|=log 2`:

`R_(x,H)=R_near+R_far`,

where `R_near` uses `0<|lambda|<log 2` and `R_far` uses `|lambda|>=log 2`.

Then, uniformly in the starting point `T0`, the interval length `V>0`, and `H>0`,

`sup_T |R_far(T)| << x`,

and

`V^(-1) integral_(T0)^(T0+V) |R_near(T)|^2 dT`
` << x L^3 + x^3 L^3/V`.

Consequently

`V^(-1) integral_(T0)^(T0+V) |R_(x,H)(T)|^2 dT`
` << x^2 + x L^3 + x^3 L^3/V`.

At the active Wang boundary

`H asymp x ell`, `ell=log log(3x)`,

the normalized estimate is

`H^(-2) V^(-1) integral |R_(x,H)(T)|^2 dT`
` << ell^(-2) + L^3/(x ell^2) + x L^3/(V ell^2)`.

Hence the deterministic finite-window mean square is `o(H^2)` on the sufficient scale

`V >> x L^3/ell^2`.

This is cutoff-free in the prime-power support and improves the sufficient horizon from the cubic scale of `VIS-311`,

`x^3 L^3/ell^2`,

to a near-linear scale, at the cost of using a fixed near-ratio/far-ratio decomposition and treating the far-ratio component pointwise.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL SEPARATED-FREQUENCY MEAN VALUE + DYADIC AGGREGATE-DENSITY CONTROL + PROOF-METHOD IMPROVEMENT + NO-NOVELTY-CLAIM`.

The result still does not reach the natural local scale `V asymp H asymp x ell`: the remaining gap is logarithmic, of size roughly `L^3/ell^3` in the sufficient averaging horizon. It does not prove pointwise cancellation at every starting height.

## 1. Far ratio frequencies are already negligible at the log-log boundary

For `lambda!=0`,

`|K_H(lambda)| = |integral_0^H exp(-iu lambda) du| <= 2/|lambda|`.

Therefore on `|lambda|>=log 2`, before or after grouping,

`|R_far(T)|`
` <= (2/log 2) (sum_q a_q)^2`.

It remains to bound the positive coefficient mass. Write `psi(y)=sum_(n<=y) Lambda(n)`. The classical Chebyshev bound `psi(y)<<y`, followed by partial summation, gives

`sum_(q<=x) a_q`
` = x^(-1) sum_(n<=x) Lambda(n) sqrt(n)`
` << sqrt(x)`,

and

`sum_(q>x) a_q`
` = x sum_(n>x) Lambda(n) n^(-3/2)`
` << sqrt(x)`.

Here `Lambda` already restricts the sum to prime powers. Thus

`sum_q a_q << sqrt(x)`

and uniformly in `T,H`,

`|R_far(T)| << x`.

At `H asymp x ell` this gives

`R_far(T)/H << 1/ell -> 0`

pointwise. So frequencies outside the fixed multiplicative window `1/2<q/r<2` cannot by themselves sustain the unresolved `H`-scale remainder.

## 2. The near band has no same-base harmonic collisions

If `q=p^k` and `r=p^l` have the same base prime with `k!=l`, then

`|log(q/r)| = |k-l| log p >= log 2`.

Hence every frequency in the strict near band

`0<|lambda|<log 2`

comes from prime powers with **distinct base primes**. Such `q` and `r` are coprime, so the reduced rational ratio `q/r` uniquely determines the oriented pair `(q,r)`.

This removes the same-base fibers that required separate grouping in `VIS-308`--`VIS-311`. In the near band, the grouped coefficient is simply

`B_(log(q/r))=a_q a_r K_H(log(q/r))`

for the unique oriented cross-base pair.

## 3. Dyadic height shells recover separation without a global cutoff

For dyadic `M`, let `F_M(T)` be the part of `R_near(T)` with

`M < max(q,r) <= 2M`.

Every contributing ratio lies in `(1/2,2)`, and both numerator and denominator are at most `2M`.

Take two distinct frequencies in the same shell,

`alpha=q/r`, `beta=u/v`.

Both fractions are reduced. Therefore the integer cross-products differ by at least one:

`|qv-ur|>=1`.

Since `r,v<=2M`,

`|alpha-beta| >= 1/(4M^2)`.

On `(1/2,2)`, the derivative of `log` is at least `1/2`, so

`|log alpha-log beta| >= 1/(8M^2)`.

Thus each individual dyadic shell is a finite `delta_M`-separated exponential polynomial with

`delta_M >> M^(-2)`.

The classical Montgomery--Vaughan Hilbert/mean-value inequality then gives, uniformly in `T0`,

`V^(-1) integral_(T0)^(T0+V) |F_M(T)|^2 dT`
` << (1+M^2/V) E_M`,

where

`E_M=sum_(lambda in shell M)|B_lambda|^2`.

The full spectrum is dense by `VIS-312`; the point is that **density arrives only after infinitely many arithmetic-height shells are superposed**. Each shell remains separated, and the shell energy decays fast enough to recombine them in `L^2`.

## 4. Wang's taper makes the shell norms summable

The comparable-pair calculation of `VIS-307` applies directly to the present near band. Its dyadic estimate gives

`E_M << M v_x(M)^4 log^3(4M)`,

where

`v_x(M)=min(M/x,x/M)`

up to absolute constants on a dyadic shell. Equivalently,

`E_M << (M^5/x^4) log^3(4M)` for `M<=x`,

and

`E_M << (x^4/M^3) log^3(4M)` for `M>=x`.

Apply Minkowski to the dyadic decomposition. For finite partial sums,

`||R_near||_(L^2_V)`
` <= sum_M (1+M^2/V)^(1/2) E_M^(1/2)`
` <= sum_M E_M^(1/2) + V^(-1/2) sum_M M E_M^(1/2)`,

where `||.||_(L^2_V)` denotes normalized `L^2` on `[T0,T0+V]`.

The lower shells satisfy

`sum_(M<=x) E_M^(1/2) << sqrt(x) L^(3/2)`,

`sum_(M<=x) M E_M^(1/2) << x^(3/2) L^(3/2)`.

For `M>=x`, writing `M=2^j x`, the factors `2^(-3j/2)` and `2^(-j/2)` dominate the polynomial growth of `log(4M)`, so the same bounds hold:

`sum_(M>=x) E_M^(1/2) << sqrt(x) L^(3/2)`,

`sum_(M>=x) M E_M^(1/2) << x^(3/2) L^(3/2)`.

The sums therefore converge, justifying passage from finite partial sums to the full near spectrum, and

`||R_near||_(L^2_V)`
` << sqrt(x) L^(3/2) + x^(3/2) L^(3/2)/sqrt(V)`.

Squaring gives

`V^(-1) integral |R_near(T)|^2 dT`
` << x L^3 + x^3 L^3/V`.

No support cutoff `Y` remains.

## 5. Recombination and the new sufficient horizon

By Minkowski once more,

`||R||_(L^2_V) <= ||R_near||_(L^2_V) + ||R_far||_(L^2_V)`.

The far component has normalized `L^2` norm `O(x)`, so

`V^(-1) integral |R(T)|^2 dT`
` << x^2 + x L^3 + x^3 L^3/V`.

At `H asymp x ell`, division by `H^2` yields

`<< 1/ell^2 + L^3/(x ell^2) + x L^3/(V ell^2)`.

The first two terms vanish automatically. The last tends to zero whenever

`V >> x L^3/ell^2`.

Thus the polynomial gap exposed by `VIS-310`--`VIS-312` was not intrinsic to the dense ratio spectrum. A fixed ratio split plus dyadic arithmetic-height shells replaces pointwise nearest-neighbor isolation of the whole spectrum by **aggregate shell separation**, recovering two further powers of `x` beyond `VIS-311`.

The remaining loss is logarithmic rather than polynomial. Reaching `V asymp x ell` would require improving the shell-energy/large-sieve logarithms, exploiting cancellation between shells, or replacing the pointwise `O(x)` far-band treatment by a sharper signed estimate in a way that materially affects the current logarithmic gap.

## Prior art and novelty boundary

The separated-frequency mean-value input is classical Montgomery--Vaughan Hilbert technology: H. L. Montgomery and R. C. Vaughan, **Hilbert's Inequality**, *Journal of the London Mathematical Society* (2) 8 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`. `VIS-194` and `VIS-311` already use the corresponding weighted finite-frequency form inside Mathia.

The shell energy estimate is not a new external theorem: it is exactly the comparable-prime-power calculation already established in `VIS-307`, now used as a scale-local input instead of summed before the finite-window step. The bound `sum_q a_q<<sqrt(x)` uses only the classical Chebyshev estimate for `psi(x)` and partial summation.

A targeted prior-art check confirms the Montgomery--Vaughan inequality is established classical input; no new large-sieve or nonharmonic-Fourier theorem is claimed. The durable Mathia contribution is the specialization and recombination: the fixed `log 2` split removes same-base fibers from the dense near band, dyadic ratio-height shells retain enough separation for the classical mean-value theorem, and Wang's taper makes the resulting shell norms summable without a hard support cutoff.

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv `2609.07918v1` (2026), remains the source of the coefficient profile and short-interval setting; `VIS-302`--`VIS-312` record the reductions used here.

## Boundaries and falsification

The result is a sufficient **mean-square-in-starting-height** estimate. It does not prove `R_(x,H)(T)=o(H)` for every individual `T`, and it does not justify a moving `x(T)` inside the averaging integral without an additional uniform/joint-limit argument.

The strict near band `|lambda|<log 2` is deliberate. The boundary frequencies `|lambda|=log 2`, including the first same-base harmonic, are assigned to `R_far` and covered by the pointwise bound.

The shell separation argument relies on cross-base ratios being reduced and uniquely represented. This is valid because distinct prime-power bases are coprime. If a nontrivial cross-base collision exists after reduction, the shell decomposition must be revised.

The `VIS-307` shell estimate is inherited with only finite-overlap changes. An error in that comparable-pair energy calculation would propagate here.

The far-band bound is intentionally crude. It is enough because `x=o(x log log x)`. It does not say the far band has Bohr energy of order `x^2`, nor that the fixed split is optimal.

Falsify the finding by finding a same-base nonzero frequency strictly inside `(-log 2,log 2)`, a failure of the `M^(-2)` separation within one dyadic reduced-ratio shell, a failure of the Montgomery--Vaughan shell mean-value bound, divergence of either dyadic Minkowski sum under the stated `VIS-307` energy profile, or an error in the `sum a_q<<sqrt(x)` far-band estimate.

## Dependencies

- `VIS-307`: comparable prime-power shell energy `M v_x(M)^4 log^3(4M)`.
- `VIS-309`: grouped deterministic Wang remainder and Bohr interpretation.
- `VIS-311`: finite-cutoff weighted local-spacing cubic horizon.
- `VIS-312`: dense full ratio spectrum and failure of a cutoff-free nearest-neighbor functional.
- `CLUE-wang-fixed-source-packet-localization`: accepted finite-window localization clue.

## Research consequence

The accepted Wang localization clue now has a cutoff-free aggregate-density mechanism. The dense full spectrum does not force the cubic hard-cutoff horizon: after the fixed ratio split, the coefficient-heavy near band can be controlled shellwise and the far band is already `o(H)` pointwise at `H asymp x log log x`.

The live question narrows from polynomial finite-window transfer to the remaining logarithmic gap between

`V >> x log^3 x/(log log x)^2`

and the natural target

`V asymp x log log x`.

A next useful result should attack that logarithmic loss or identify a genuine exceptional-height mechanism. Another hard support cutoff or unpartitioned nearest-neighbor estimate is no longer informative.