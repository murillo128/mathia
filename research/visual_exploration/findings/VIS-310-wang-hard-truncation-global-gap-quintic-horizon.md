# VIS-310 — hard truncation plus global ratio spacing gives only a quintic finite-Bohr horizon

## Claim

Keep Wang's deterministic prime-power Dirichlet series and signed remainder from `VIS-309`,

`D_x(t)=sum_(q=p^k) a_q q^(-it)`,

`a_q=(Lambda(q)/sqrt(q)) min(q/x,x/q)`,

`R_(x,H)(T)=integral_T^(T+H)|D_x(t)|^2 dt-H sum_q a_q^2`.

Put `L=log(3x)`. For a hard support cutoff `Y>=2x`, let

`D_(x,Y)(t)=sum_(q<=Y) a_q q^(-it)`

and define `R_(x,H,Y)(T)` by the same formula with `D_x` and its diagonal coefficient mass truncated at `Y`.

Then for every real start `T0` and every averaging length `V>0`,

`V^(-1) integral_(T0)^(T0+V) |R_(x,H)(T)|^2 dT`
` << x L^3 (1+Y^2/V) + H^2 x^3/Y`.

The constants are absolute and the estimate is uniform in `T0`.

When

`Y_*=(H^2 x^2 V/L^3)^(1/3)`

is at least a fixed multiple of `x`, choosing `Y asymp Y_*` gives

`V^(-1) integral_(T0)^(T0+V) |R_(x,H)(T)|^2 dT`
` << x L^3 + H^(4/3) x^(7/3) L V^(-1/3)`.

At the active boundary

`H asymp x ell`, `ell=log log(3x)`,

this becomes

`H^(-2) V^(-1) integral_(T0)^(T0+V) |R_(x,H)(T)|^2 dT`
` << L^3/(x ell^2) + x^(5/3) L/(ell^(2/3) V^(1/3))`.

Thus this **particular proof route** — hard truncate the absolutely convergent Wang series, use only the global minimum spacing of the resulting ratio frequencies, then control the discarded tail in uniform norm — yields `o(H^2)` only on the sufficient scale

`V >> x^5 L^3/ell^2`.

That scale is enormously larger than the natural local scale `V asymp H asymp x ell`. Therefore the simplest quantitative upgrade of the Bohr mean in `VIS-309` is structurally too lossy for the moving-`x` problem.

**Evidence/status:** `EXACT-DERIVED + QUANTITATIVE BOHR-TRUNCATION CONTROL + NEGATIVE/PROOF-METHOD BOUNDARY + NO-NOVELTY-CLAIM`.

The quintic scale is **not** a lower bound for the true dephasing time, not an obstruction to a sharper finite-window theorem, and not evidence for exceptional heights. It is only the cost of combining a hard tail cutoff with the worst spacing among all retained rational-ratio frequencies.

## 1. Wang's coefficient tail is uniformly small only after a long cutoff

All coefficients `a_q` are nonnegative. Standard Chebyshev/PNT-level bounds for the von Mangoldt mass give

`sum_q |a_q| << sqrt(x)`.

Indeed, below the source scale,

`sum_(q<=x) a_q`
` = x^(-1) sum_(q<=x) Lambda(q) sqrt(q)`
` << x^(-1/2) sum_(q<=x) Lambda(q)`
` << sqrt(x)`.

Above the source scale,

`sum_(q>x) a_q`
` = x sum_(q>x) Lambda(q) q^(-3/2)`
` << sqrt(x)`

by partial summation from `psi(u)<<u`.

For `Y>=2x`, the same calculation gives the sharper tail bound

`A_(x,Y)=sum_(q>Y) a_q << x/sqrt(Y)`.

Write

`E_(x,Y)(t)=D_x(t)-D_(x,Y)(t)`.

Uniformly in real `t`,

`|D_x(t)|+|D_(x,Y)(t)| << sqrt(x)`,

`|E_(x,Y)(t)| << x/sqrt(Y)`.

Therefore

`||D_x(t)|^2-|D_(x,Y)(t)|^2|`
` << x^(3/2)/sqrt(Y)`.

The omitted diagonal mass satisfies

`sum_(q>Y) a_q^2 <= A_(x,Y)^2 << x^2/Y`.

Consequently, uniformly in `T`,

`|R_(x,H)(T)-R_(x,H,Y)(T)|`
` << H x^(3/2)/sqrt(Y)`.

This is the first loss. To make the truncation error itself `o(H)` by this uniform argument one already needs `Y>>x^3`.

## 2. The truncated remainder has a finite prime-ratio spectrum

Expand the truncated remainder:

`R_(x,H,Y)(T)`
` = sum_(q!=r; q,r<=Y) a_q a_r K_H(q,r) exp(-iT log(q/r))`,

where

`K_H(q,r)=integral_0^H exp(-iu log(q/r)) du`.

Group equal rational ratios and write

`R_(x,H,Y)(T)=sum_(lambda in Lambda_Y) B_(lambda,Y) exp(-i lambda T)`.

Here `lambda=log(q/r)` for prime powers `q,r<=Y`, `q!=r`, after exact collisions have been combined.

The coefficient energy of this truncated exponential polynomial is bounded by the full Bohr energy from `VIS-309`:

`sum_(lambda in Lambda_Y) |B_(lambda,Y)|^2`
` <= M_T |R_(x,H)(T)|^2`
` << x L^3`.

The inequality deserves an explicit check because equal ratios can occur. If `q=p^k` and `r=s^l` use different base primes, unique factorization makes the reduced ratio determine the ordered pair. If both are powers of the same prime, a fixed ratio `p^d` collects the pairs `(p^(l+d),p^l)`. Every term in that fiber has the same kernel factor `K_H(p^d)` and a positive amplitude `a_(p^(l+d))a_(p^l)`. Increasing the support cutoff therefore increases the absolute value of each grouped coefficient monotonically. Hence every finite-cutoff ratio coefficient is dominated by its absolutely convergent full-series coefficient, and the squared coefficient energy is no larger than the full Bohr mean.

By `VIS-309`, that full energy is exactly the completely multiplicative Haar second moment from `VIS-308`, which is `O(x L^3)`.

## 3. Global ratio spacing pays `Y^2`

Take two distinct frequencies

`lambda=log(q/r)`, `mu=log(u/v)`

in `Lambda_Y`. Then

`lambda-mu=log(qv/(ru))`.

Because the frequencies are distinct, the positive integers `qv` and `ru` are different; both are at most `Y^2`. Therefore

`|lambda-mu| >= log(1+Y^(-2))`.

Thus the minimum separation of the entire truncated frequency set satisfies

`delta_Y^(-1) <= Y^2+1`.

Montgomery--Vaughan's finite-interval mean-square theorem for separated real frequencies now gives, uniformly in the starting point `T0`,

`V^(-1) integral_(T0)^(T0+V) |R_(x,H,Y)(T)|^2 dT`
` <= [1+2 pi (Y^2+1)/V] sum_lambda |B_(lambda,Y)|^2`
` << (1+Y^2/V) x L^3`.

This is the second loss. It remembers only the single closest pair of retained rational frequencies. It discards the coefficient weighting and collision geometry that `VIS-194`--`VIS-195` already showed can matter decisively in finite prime-ratio problems.

## 4. Combine the truncation and spacing losses

From Section 1, write

`R_(x,H)=R_(x,H,Y)+E_Y`

with

`sup_T |E_Y(T)| << H x^(3/2)/sqrt(Y)`.

Hence

`V^(-1) integral |R_(x,H)(T)|^2 dT`
` << V^(-1) integral |R_(x,H,Y)(T)|^2 dT`
`    + H^2 x^3/Y`.

Using Section 3 proves

`V^(-1) integral |R_(x,H)(T)|^2 dT`
` << x L^3 + x L^3 Y^2/V + H^2 x^3/Y`.

Balancing the last two terms gives

`Y^3 asymp H^2 x^2 V/L^3`,

and therefore, when the optimizer lies in the admitted range `Y>=2x`,

`V^(-1) integral |R_(x,H)(T)|^2 dT`
` << x L^3 + H^(4/3)x^(7/3)L V^(-1/3)`.

At `H asymp x ell`, division by `H^2` gives the displayed normalized bound. The first term already tends to zero. The second tends to zero by this estimate only if

`V/(x^5 L^3/ell^2) -> infinity`.

In particular `V asymp H` is nowhere near sufficient: substitution leaves a normalized upper bound growing like a positive power of `x`.

This does not mean the true finite-window mean square is large there. It means the hard-cutoff/global-gap proof has thrown away too much information to see the cancellation already present in the Bohr mean.

## 5. What the failure localizes

`VIS-309` shows that the infinite-time second moment of the true deterministic vertical flow is only `O(x L^3)`, far below `H^2` at `H asymp x ell`. The present calculation asks whether classical finite-frequency dephasing can transfer that small Bohr energy to a local deterministic height window with no additional arithmetic input.

The answer is negative at useful scales for the most naive transfer. There are two distinct bottlenecks:

1. uniform approximation of the infinite Wang series by a hard support cutoff forces the retained support far beyond `x`;
2. after that enlargement, replacing the actual ratio-spectrum geometry by its global minimum gap pays the square of the cutoff.

Neither loss is intrinsic to Wang's remainder. Both are artifacts of the proof representation.

This points directly to the kinds of information a useful quantitative upgrade must preserve: coefficient-weighted ratio spacing rather than the worst ratio gap, a large-sieve/Hilbert estimate adapted to the actual grouped ratio coefficients, or a finite-window argument that controls the infinite tail in energy rather than uniform norm.

`VIS-194` and `VIS-195` are relevant precedent: for a different finite prime-ratio statistic they replace a global minimum gap by a coefficient-weighted inverse-spacing functional and then identify its dangerous mass with bounded-determinant incidences. They do not automatically solve the present problem because Wang's ratio series has infinite prime-power support, a moving source scale, and different coefficients, but they show exactly why another worst-gap estimate would be the wrong next abstraction.

## Prior art and novelty boundary

The finite-frequency mean-square input is classical H. L. Montgomery and R. C. Vaughan, **Hilbert's Inequality**, *Journal of the London Mathematical Society* (2) 8 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`. Their separated-frequency inequality and mean-square corollary are precisely the machinery already used in `VIS-193` and the weighted form used in `VIS-194`.

The prime-torus/vertical-translation interpretation is classical Bohr theory; `VIS-309` already records Andreas Defant, Domingo García, Manuel Maestre, and Pablo Sevilla-Peris, **Dirichlet Series and Holomorphic Functions in High Dimensions**, Cambridge University Press (2019), Chapter 3 “Bohr's Vision”, DOI `10.1017/9781108691611.005`.

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), supplies the coefficient profile and pair-correlation setting being specialized here.

A targeted audit found these ingredients in established Dirichlet-series, almost-periodic, and separated-frequency theory. No novelty is claimed for hard truncation, the integer-product frequency-gap bound, or optimizing two elementary error terms. The durable Mathia result is the quantitative **negative control on this proof strategy**: when the classical pieces are assembled in the most direct way around `VIS-309`, their information loss is large enough to make the resulting finite-Bohr window useless for the active moving-source scale.

## Boundaries and falsification

The estimate concerns one fixed `x,H` while averaging the start variable `T` over a deterministic interval. Uniformity in `T0` does not by itself justify replacing `x` by a varying function inside the averaging integral. The point is weaker: the crude fixed-`x` route already fails by several powers before the genuinely joint moving-parameter issue is reached.

The optimized quintic condition is sufficient **for this derived upper bound**, not necessary for the true remainder. A different truncation, weighted-spacing inequality, cancellation estimate, smooth support decomposition, or direct infinite-series argument may improve it drastically.

The bound `sum |B_(lambda,Y)|^2 <= M_T|R|^2` uses positivity of Wang's coefficient magnitudes inside each exact same-base ratio fiber. If a missed ratio collision mixes different base primes, or if grouped terms at a fixed ratio fail to share the same kernel phase, that monotonicity argument must be revised.

Falsify the finding by showing an error in the `ell^1` tail bounds, a truncated ratio coefficient whose modulus exceeds its full-series coefficient, a distinct ratio-frequency pair violating the integer-product spacing floor, an invalid application of the Montgomery--Vaughan finite-window theorem after exact collision grouping, or an algebraic error in the optimization.

## Dependencies

- `VIS-304`: the current `x log log x` pointwise mean-value boundary.
- `VIS-308`: completely multiplicative Haar second-moment bound `O(x log^3 x)`.
- `VIS-309`: exact identification of that Haar second moment with the Bohr-time second moment of the true Wang remainder.
- `VIS-193`--`VIS-195`: finite-window and weighted-spacing precedent for finite prime-ratio spectra.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue asking for a quantitative finite-window upgrade or explicit exceptional-height mechanism.

## Research consequence

Do not pursue the accepted Wang clue by merely truncating farther and reusing a global minimum ratio gap. That route converts an already-small Bohr second moment into a sufficient local averaging horizon of order beyond

`x^5 log^3 x/(log log x)^2`

at the active boundary, while the desired height scale is only order `x log log x`.

The next useful finite-window attempt must preserve more of the ratio-spectrum energy: a coefficient-weighted local-spacing/large-sieve bound for the grouped Wang ratio frequencies, an energy-controlled smooth tail decomposition, or a direct estimate of exceptional-height coherence. A proof that only improves constants in the hard-cutoff global-gap argument would not address the live frontier.