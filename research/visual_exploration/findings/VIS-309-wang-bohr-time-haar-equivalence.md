# VIS-309 — Haar phase control equals the Bohr-time mean of the true Wang remainder

## Claim

Keep Wang's deterministic prime-power Dirichlet polynomial/series

`D_x(t)=sum_(q=p^k) a_q q^(-it)`,

with

`a_q=(Lambda(q)/sqrt(q)) min(q/x,x/q)`

as in `VIS-302`--`VIS-308`. For `H>0` define the exact signed mean-square remainder at starting height `T` by

`R_(x,H)(T)=integral_T^(T+H) |D_x(t)|^2 dt - H sum_q a_q^2`.

Let `f` be the completely multiplicative Steinhaus field from `VIS-308`, one independent Haar phase per base prime and `f(p^k)=f(p)^k`. Then the deterministic vertical translate has the exact Bohr-mean identities

`lim_(V->infinity) (1/V) integral_0^V R_(x,H)(T) dT = 0`,

and

`lim_(V->infinity) (1/V) integral_0^V |R_(x,H)(T)|^2 dT`
` = E |R_I^f|^2`
` << x log^3(3x)`.

Consequently, for every `eta>0`,

`limsup_(V->infinity) (1/V) meas{0<=T<=V: |R_(x,H)(T)|>=eta H}`
` << x log^3(3x)/(eta^2 H^2)`.

At the active boundary `H asymp x log log(3x)`, this upper-density bound is

`<< log^3(3x)/(eta^2 x (log log(3x))^2) -> 0`.

Thus the completely multiplicative Haar control of `VIS-308` is not merely an artificial ensemble unrelated to the true coefficient phases: it is exactly the long-time mean-square law of the **actual one-parameter vertical prime-phase flow**. An `H`-scale obstruction at the Wang log-log boundary cannot be a positive-density generic feature of vertical translation. If it exists, it must be carried by height-localized exceptional coherence, by a joint moving-`x(T)` effect not controlled by this iterated Bohr mean, or by another mechanism outside this remainder.

**Evidence/status:** `EXACT-DERIVED + BOHR/KRONECKER TIME-AVERAGE IDENTIFICATION + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No pointwise estimate in `T`, no quantitative finite-window equidistribution theorem, no bound for a jointly moving `x=x(T)`, and no RH consequence is claimed.

## 1. The actual remainder is an absolutely convergent ratio-frequency series

For fixed `x`,

`sum_q |a_q| < infinity`.

Indeed the part `q<=x` is finite, while for `q>x`,

`|a_q| = x Lambda(q)/q^(3/2)`,

and `sum_n Lambda(n)n^(-3/2)` converges. Hence `D_x(t)` converges absolutely and uniformly in real `t`, so its squared modulus can be expanded and integrated termwise.

Put

`K_H(q,r)=integral_0^H exp(-iu log(q/r)) du`.

Then

`R_(x,H)(T)`
` = sum_(q!=r) a_q a_r K_H(q,r) exp(-iT log(q/r))`.

The coefficient series is absolutely summable because `|K_H(q,r)|<=H` and `sum_q |a_q|<infinity`. The corresponding quadruple series for `|R_(x,H)(T)|^2` is also absolutely summable. Therefore long-time averaging may be interchanged with the sums below without a truncation ambiguity.

## 2. Time orthogonality is exactly prime-torus Haar orthogonality

For `q!=r`,

`lim_(V->infinity) (1/V) integral_0^V exp(-iT log(q/r)) dT = 0`,

so the Bohr mean of `R_(x,H)` is zero.

For the second moment, a pair of oriented ratio frequencies survives time averaging exactly when

`log(q/r)=log(u/v)`,

that is,

`q/r=u/v`.

Therefore

`M_T |R_(x,H)(T)|^2`
` = sum_(q!=r,u!=v; q/r=u/v)`
`   a_q a_r a_u a_v K_H(q,r) conjugate(K_H(u,v))`,

where `M_T` denotes the long-time mean.

Now write prime factorizations as exponent vectors. For the Steinhaus field,

`f(q) conjugate(f(r))`

is precisely the prime-torus character with exponent vector `v(q)-v(r)`. Haar orthogonality gives

`E[f(q) conjugate(f(r)) conjugate(f(u)) f(v)] = 1`

exactly when

`v(q)-v(r)=v(u)-v(v)`,

which by unique factorization is equivalent to `q/r=u/v`; otherwise the expectation is zero.

Thus the time-average collision classes of the actual deterministic flow and the Haar-character collision classes of `VIS-308` are identical, proving the exact identity

`M_T |R_(x,H)(T)|^2 = E |R_I^f|^2`.

This is also the elementary Bohr/Kronecker picture of ordinary Dirichlet series: vertical translation follows the prime-frequency flow `p^(-iT)` on the prime torus, and rational independence of the prime logarithms is just unique factorization.

## 3. Import the VIS-308 second-moment bound

`VIS-308` already proves, uniformly in interval location and length,

`E |R_I^f|^2 << x log^3(3x)`.

The exact Bohr/Haar identity therefore transfers that estimate directly to the deterministic time mean:

`M_T |R_(x,H)(T)|^2 << x log^3(3x)`.

No new spacing estimate is needed here. The same-base equal-exponent-difference collision fibers isolated in `VIS-308` are exactly the repeated rational ratios `p^(k-l)` that survive deterministic time averaging; all cross-base rational ratios are unique by factorization.

Applying Markov/Chebyshev to the time mean yields

`upper-density{|R_(x,H)(T)|>=eta H}`
` << x log^3(3x)/(eta^2 H^2)`.

When `H asymp x log log(3x)`, the right-hand side tends to zero with `x`.

## 4. What this removes from the surviving phase hypothesis

`VIS-308` left open the possibility that its product-Haar ensemble destroyed a special cross-prime relation present in the actual vertical phases. The present identity shows that this objection is too broad.

The actual phases are

`epsilon_p(T)=p^(-iT)`,

so they lie on a single deterministic Kronecker orbit rather than being independently resampled at each height. Nevertheless, for the quadratic remainder under study, the long-time mean and mean square of that orbit are exactly the same Haar moments used by `VIS-308`.

Hence **the one-parameter common-time relation across all primes is not by itself enough to make the `x log log x` remainder generically large**. A surviving obstruction must be exceptional in height, require quantitative finite-window failure of equidistribution on the relevant moving frequency set, or exploit a different statistic/error term.

This narrows the live phrase “cross-prime deterministic alignment”: the issue is no longer generic deterministic dependence of the phases, but exceptional coherent alignment at the heights and scales relevant to Wang's pointwise argument.

## 5. Prior art and novelty boundary

The prime-torus/vertical-translation dictionary is classical Bohr theory. Andreas Defant, Domingo García, Manuel Maestre, and Pablo Sevilla-Peris, **Dirichlet Series and Holomorphic Functions in High Dimensions**, Cambridge University Press (2019), Chapter 3 “Bohr's Vision”, DOI `10.1017/9781108691611.005`, develops the Bohr transform from prime-exponent coordinates to ordinary Dirichlet series. Ingo Schoolmann, **On Bohr's theorem for general Dirichlet series**, *Mathematische Nachrichten* 293:8 (2020), 1591--1612, DOI `10.1002/mana.201800542`, explicitly records the `Q`-linear independence of `(log p)` in this framework.

No new Kronecker, ergodic, or almost-periodic theorem is claimed. The durable Mathia content is the exact specialization to the Wang remainder: its Bohr-time second moment is **identical** to the completely multiplicative Steinhaus second moment already bounded in `VIS-308`, so that bound controls the upper density of `H`-scale deviations of the true translated remainder.

## Boundaries and falsification

The density statement is an iterated one: for each fixed `x,H`, first take the long-time mean `V->infinity`; only then inspect the large-`x` boundary `H asymp x log log x`. It does **not** justify replacing `x` by a function `x(T)` inside the same limit.

The exceptional set may depend strongly on `x`. A moving choice of `x(T)` could in principle track increasingly rare resonant heights. Controlling that regime requires a quantitative finite-window equidistribution or large-sieve-type estimate uniform enough in the relevant prime-ratio frequencies; none is supplied here.

Likewise, zero asymptotic density does not mean absence of exceptional heights, bounded gaps between them, or pointwise cancellation. A sparse resonance sequence could still matter to a pointwise theorem.

Falsify the result by finding a failure of absolute convergence/termwise averaging for Wang's coefficient profile, a surviving time-frequency collision with `q/r!=u/v`, a mismatch between rational-ratio equality and the Steinhaus character collision condition, or an error in the inherited `VIS-308` second-moment estimate.

## Dependencies

- `VIS-302`--`VIS-304`: Wang's coefficient profile and the current `x log log x` mean-value boundary.
- `VIS-307`: exact-support independent-phase control.
- `VIS-308`: completely multiplicative Steinhaus control and `E|R_I^f|^2 << x log^3(3x)`.
- `CLUE-wang-fixed-source-packet-localization`: accepted source-localization clue.

## Research consequence

The moving upper-source frontier narrows again. The relevant distinction is not “deterministic one-parameter prime phases versus independent Haar phases” at the level of long-time quadratic moments: those are exactly the same after Bohr averaging.

The remaining target is **exceptional-height cross-prime coherence or a genuinely quantitative moving-frequency effect**. A useful next result must either control the actual remainder on finite height windows uniformly enough for `x=x(T)`, or identify a concrete resonance mechanism producing a sparse but `H`-scale exceptional set.