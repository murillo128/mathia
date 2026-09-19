# VIS-304 — prime-power frequency spacing moves Wang's mean-value boundary to `x log log x`

## Claim

Let

`I=(T,T+H]`, `H=T^theta`, `0<theta<1`, `L=log T`,

and let Wang's Dirichlet polynomial be

`D_x(t)=sum_(n>=2) a_n n^(-it)`,
`a_n=(Lambda(n)/sqrt(n)) min(n/x,x/n)`.

Write `Q` for the set of prime powers. Since `Lambda(n)=0` off `Q`, only frequencies `lambda_q=log q`, `q in Q`, occur. For each `q in Q` let

`delta_q=min_(r in Q, r!=q) |log q-log r|`.

Then

`sum_(q in Q) a_q^2/delta_q << x log log(3x)`,

and the Montgomery--Vaughan weighted Hilbert inequality therefore gives

`integral_I |D_x(t)|^2 dt`
` = H sum_q a_q^2 + O(x log log(3x))`.

Combining this support-sensitive mean-value estimate with the already established diagonal asymptotic and the localization/gamma estimates of `VIS-298`--`VIS-302` yields

`F_I(x) = (H/(2*pi))[log x+(L-log(2*pi))^2/x^2]+o(H)`

for every moving source `x=x(T)->infinity` satisfying

`x log log(3x)=o(H)`.

Thus the `x log x asymp H` layer exposed in `VIS-302` and narrowed by `VIS-303` is still not a structural boundary of the pointwise argument. The first unresolved generic mean-value scale moves to

`x log log(3x) asymp H`.

**Evidence/status:** `LITERATURE+DERIVED + SUPPORT-SENSITIVE MEAN-VALUE REFINEMENT + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This does not prove that the actual off-diagonal remainder has order `x log log x`, does not improve the weighted Hilbert inequality or any prime-pair sieve theorem, and does not establish a new transition of Wang's pair-correlation statistic. It only feeds the true prime-power frequency support into a classical weighted inequality instead of paying the integer-lattice spacing cost.

## 1. Use the actual nonzero frequency set

For a finite truncation of `D_x`, expand the mean square. The off-diagonal term is the difference of two Hilbert forms, one at each endpoint of `I`, with distinct real frequencies

`lambda_q=log q`.

The weighted Montgomery--Vaughan Hilbert inequality states that for distinct real `lambda_q`

`|sum_(q!=r) w_q conjugate(w_r)/(lambda_q-lambda_r)|`
` << sum_q |w_q|^2/delta_q`.

Applying it to `w_q=a_q q^(-iT)` and to `w_q=a_q q^(-i(T+H))` gives

`|integral_I |D_x(t)|^2 dt-H sum_q a_q^2|`
` << sum_q a_q^2/delta_q`.

After the spacing sum below is shown finite, truncation may be removed. Wang's displayed mean-value estimate instead bounds the frequency spacing at the ambient integer scale and obtains an error controlled by `sum n a_n^2`. `VIS-302` evaluates that weight as `asymp x log x`; the present step retains the sparser support before applying the Hilbert bound.

## 2. A dyadic reciprocal-spacing bound for prime powers

For `Y>=3`, consider prime powers `q in [Y,2Y]`. Frequencies whose ratio is outside a fixed neighborhood of one already have `delta_q >> 1`; for the remaining frequencies,

`delta_q^(-1) << 1 + Y/d(q)`,

where `d(q)` is the distance from `q` to the nearest other prime power in a fixed enlarged interval such as `[Y/2,4Y]`.

The needed arithmetic input is

`sum_(q in Q intersect [Y,2Y]) Lambda(q)^2/d(q)`
` << Y log log(3Y)`.

To see this, first take `q=p` prime. Let `g(p)` be the distance to the nearest other prime and let `e(p)` be the distance to the nearest higher prime power `r=l^k`, `k>=2`. Then

`1/d(p) <= 1/g(p)+1/e(p)`.

Put `D=ceil(log Y)`. For prime-prime proximity, overcounting by all shifts `1<=h<=D` gives

`sum_(p in [Y,2Y]) 1/g(p)`
` << pi(2Y)/D`
`    + sum_(h<=D) (1/h) # {p in [Y,2Y]: p and p+h are prime}`.

A standard Brun--Selberg upper-bound sieve for the two linear forms gives, uniformly for these logarithmic shifts,

`# {p in [Y,2Y]: p and p+h are prime}`
` << (Y/log^2 Y) (h/phi(h))`

for admissible even `h`; the finitely exceptional parity cases are harmless. Hence

`sum_(p in [Y,2Y]) 1/g(p)`
` << Y/log^2 Y`
`    + (Y/log^2 Y) sum_(h<=D) 1/phi(h)`
` << Y log log(3Y)/log^2 Y`.

The last estimate follows, for example, from

`n/phi(n)=sum_(d|n) mu(d)^2/phi(d)`

and harmonic summation, which give `sum_(h<=D)1/phi(h)<<log(2D)`.

Higher prime powers do not change this scale. There are `O(Y^(1/2))` of them in a fixed enlargement of the shell. For primes whose nearest higher prime power lies farther than `D`, the contribution is again at most `pi(2Y)/D`. For the remaining pairs, trivial counting around each higher prime power gives

`sum_(p in [Y,2Y]) 1/e(p)`
` << Y/log^2 Y + Y^(1/2) log log(3Y)`.

Since `Lambda(p)^2 asymp log^2 Y` on the prime part, its weighted contribution is `O(Y log log(3Y))`. The higher-prime-power points themselves contribute only

`O(Y^(1/2) log^2 Y)`

because `d(q)>=1`. This proves the dyadic spacing bound.

This argument uses only an upper-bound sieve. No lower bound for twin primes, bounded gaps, or Hardy--Littlewood asymptotic is assumed.

## 3. Wang's taper converts the shell bound to `x log log x`

Write

`v_x(q)=min(q/x,x/q)`,

so

`a_q^2=(Lambda(q)^2/q) v_x(q)^2`.

On `q in [Y,2Y]`, one has `q asymp Y`, so Section 2 and
`delta_q^(-1)<<1+Y/d(q)` give

`sum_(q in Q intersect [Y,2Y]) a_q^2/delta_q`
` << v_Y^2 [Y^(-1) sum_(q in Q intersect [Y,2Y]) Lambda(q)^2`
`             + sum_(q in Q intersect [Y,2Y]) Lambda(q)^2/d(q)]`
` << v_Y^2 Y log log(3Y)`,

using the standard bound `sum_(q in Q intersect [Y,2Y]) Lambda(q)^2 << Y log(3Y)`.
Here `v_Y << Y/x` for `Y<=x` and `v_Y<<x/Y` for `Y>=x`.

Summing dyadically below `x` gives

`sum_(Y<=x) (Y/x)^2 Y log log(3Y)`
` << x log log(3x)`,

because the shell sizes decay geometrically like `x/8^j`. Summing above `x` gives

`sum_(Y>=x) (x/Y)^2 Y log log(3Y)`
` << x log log(3x)`,

with geometric decay like `x/2^j`. Therefore

`sum_q a_q^2/delta_q << x log log(3x)`.

The lower-order `sum a_q^2` contribution from the `+1` in the spacing comparison is `O(log(2x))` by `VIS-291` and is absorbed.

## 4. Reassemble the pointwise Wang statistic

`VIS-291` gives

`sum_q a_q^2=log x+O(exp(-cV(log x)))`.

Thus Section 1 yields

`integral_I |D_x(t)|^2 dt`
` = H log x`
`   + O(H exp(-cV(log x))+x log log(3x))`.

Under `x log log(3x)=o(H)`, the interior error is `o(H)`.

The larger source window does not reactivate the localization terms. `VIS-301` gives the zero-free-region bounds

`pure leakage << x q_T(x)^2 L^2 + x L^2 H/T^2`,

`cross coherence << x q_T(x)^2 L^3 + x q_T(x)L^2 H/T`,

with `q_T(x)=x^(-eta_T)` and `eta_T asymp L^(-2/3)(log L)^(-1/3)`.

If `x<=H/L^4`, Wang's original `O(xL^3)` localization bound is already `o(H)`. Otherwise `log x>=theta L-4log L`, so `q_T(x)` is super-polynomially small in `L`; it absorbs the polynomial logarithmic factors throughout the new range `x log log(3x)=o(H)`. The far-zero term is also `o(H)` because `x=o(H/log log(3x))` and `H/T=T^(theta-1)`.

The gamma-recentered remainder analysis of `VIS-298`--`VIS-302` requires only a moving source and `x<T` at this stage, both of which follow here. Reassembling therefore gives the claimed pointwise asymptotic.

## 5. What boundary remains

`VIS-303` is still a valid classification of the previous `x log x asymp H` layer: at that scale odd additive shifts are negligible. But its hypothesis `x log x=O(H)` does not cover the larger range now reached here, so the present proof does not extend `VIS-303` by assumption. Instead it handles the complete prime-power support directly through its logarithmic nearest-neighbor spacing.

The unresolved question is now whether the weighted Hilbert cost

`sum_q a_q^2/delta_q << x log log(3x)`

is itself sharp for Wang's coefficients, or whether the actual endpoint Hilbert forms exhibit further cancellation. The `log log x` factor comes from summing the reciprocal small-shift spectrum allowed by the Brun--Selberg upper bound; it is an upper-bound-sieve cost, not an established term in the pair-correlation statistic.

A further improvement must therefore either sharpen the support-spacing average relevant to these coefficients, exploit cancellation in the signed/oscillatory Hilbert form rather than its absolute weighted norm, or produce an admissible lower/control construction showing an `x log log x` obstruction.

## Prior art and evidence boundary

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), supplies the coefficient sequence and the Montgomery--Vaughan mean-value step. His Lemma 2.5 bounds `sum n a_n^2` by `O(x log^2(2x))`; `VIS-302` already replaces that coefficient majorant by its exact `x log x` asymptotic.

H. L. Montgomery and R. C. Vaughan, **Hilbert's inequality**, *J. London Math. Soc.* (2) 8 (1974), 73--82, is the classical source of the weighted Hilbert inequality with local spacings `delta_q`. Brad Rodgers, **On the optimal constant in the Montgomery-Vaughan weighted Hilbert inequality**, arXiv:2608.12315 (2026), records the modern formulation explicitly; only existence of an absolute constant is used here.

The prime-pair input is the classical Brun--Selberg upper-bound sieve. In standard form it gives the expected upper bound `<< Y/log^2 Y` times the usual singular-series/local-factor correction for a fixed difference; the argument above uses it only for `h<=log Y` and sums those upper bounds. This is classical sieve machinery, not a new prime-gap theorem.

A targeted prior-art search found the weighted Hilbert inequality, support-sensitive local-spacing formulations, and classical prime-pair sieve bounds as established ingredients, but no need for a novelty claim is made for their present combination. The durable conclusion is deliberately limited to the Wang specialization and its proof boundary.

## Dependencies

- `VIS-291`: diagonal coefficient asymptotic and classical prime-number-theorem envelope.
- `VIS-298`: exact gamma recentering.
- `VIS-301`: zero-free suppression of localization terms.
- `VIS-302`: coefficient-specific `x log x` Montgomery--Vaughan boundary.
- `VIS-303`: parity/support decomposition at the previous `x log x asymp H` layer.
- `CLUE-wang-fixed-source-packet-localization`: accepted source-localization clue.

## Research consequence

Replace the previous generic upper pointwise condition

`x log(2x)=o(H)`

by

`x log log(3x)=o(H)`.

The `H/log T` source scale is therefore another proof-packaging boundary, not a demonstrated transition. The next coherent target is the support-sensitive `H/log log x` layer: determine whether the reciprocal prime-power spacing cost is genuinely attained by Wang's endpoint Hilbert forms or can be reduced by arithmetic/oscillatory cancellation.
