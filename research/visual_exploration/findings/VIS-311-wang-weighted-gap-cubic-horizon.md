# VIS-311 — weighted ratio spacing lowers the hard-truncation Wang horizon from quintic to cubic

## Claim

Keep the Wang remainder and notation of `VIS-309`--`VIS-310`,

`D_x(t)=sum_(q=p^k) a_q q^(-it)`,

`a_q=(Lambda(q)/sqrt(q)) min(q/x,x/q)`,

`R_(x,H)(T)=integral_T^(T+H)|D_x(t)|^2 dt-H sum_q a_q^2`,

and put `L=log(3x)`. For a hard prime-power cutoff `Y>=2x`, write the grouped finite ratio expansion from `VIS-310` as

`R_(x,H,Y)(T)=sum_(lambda in Lambda_Y) B_(lambda,Y) exp(-i lambda T)`.

For each grouped frequency let

`delta_(lambda,Y)=min_(mu in Lambda_Y, mu!=lambda)|lambda-mu|`,

and define the weighted inverse-spacing energy

`W_(x,H)(Y)=sum_(lambda in Lambda_Y) |B_(lambda,Y)|^2/delta_(lambda,Y)`.

Then uniformly in the start point `T0` and for every averaging length `V>0`,

`V^(-1) integral_(T0)^(T0+V) |R_(x,H)(T)|^2 dT`
` << x L^3 + Y x^2 L^3/V + H^2 x^3/Y`.

Consequently, when

`Y_* = H sqrt(x V/L^3)`

is at least a fixed multiple of `x`, choosing `Y asymp Y_*` gives

`V^(-1) integral_(T0)^(T0+V) |R_(x,H)(T)|^2 dT`
` << x L^3 + H x^(5/2) L^(3/2) V^(-1/2)`.

At the active boundary

`H asymp x ell`, `ell=log log(3x)`,

the normalized estimate is

`H^(-2) V^(-1) integral |R_(x,H)(T)|^2 dT`
` << L^3/(x ell^2) + x^(3/2)L^(3/2)/(ell sqrt(V))`.

Thus the coefficient-weighted Montgomery--Vaughan route proves `o(H^2)` on the sufficient scale

`V >> x^3 L^3/ell^2`.

This improves the `VIS-310` worst-gap sufficient horizon by two powers of `x`, from quintic to cubic, without changing the hard tail cutoff. It still misses the natural local scale `V asymp H asymp x ell` by a large polynomial factor.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL WEIGHTED-HILBERT INPUT + COEFFICIENT-WEIGHTED RATIO MOMENT + NEGATIVE/PROOF-METHOD BOUNDARY + NO-NOVELTY-CLAIM`.

The cubic scale is not a lower bound for the true dephasing time and is not claimed optimal. It is the sufficient scale produced by combining the exact Wang coefficient profile with a local-spacing Hilbert inequality while retaining the same uniform hard-tail control as `VIS-310`.

## 1. Weighted Hilbert replaces the single worst gap

For the finite exponential polynomial `R_(x,H,Y)`, put

`E_(x,H)(Y)=sum_(lambda in Lambda_Y)|B_(lambda,Y)|^2`.

`VIS-310` proves

`E_(x,H)(Y) <= M_T |R_(x,H)(T)|^2 << x L^3`.

The weighted Montgomery--Vaughan inequality used in `VIS-194` gives the finite-window identity with error

`| V^(-1) integral_(T0)^(T0+V)|R_(x,H,Y)(T)|^2 dT - E_(x,H)(Y) |`
` <= (3 pi/V) W_(x,H)(Y)`.

The estimate is uniform in `T0`: translating the interval only rotates each coefficient by a unit phase and leaves both its modulus and its local frequency spacing unchanged.

Unlike the global separation used in `VIS-310`, this bound charges a tiny gap only to the coefficient energy carried by the frequency that sees it. The remaining task is therefore to estimate `W_(x,H)(Y)` from Wang's actual ratio coefficients rather than replace every `delta_(lambda,Y)` by the global minimum.

## 2. Each retained ratio pays only its own arithmetic height

Write a grouped frequency in reduced rational form

`exp(lambda)=u_lambda/v_lambda`,

with positive coprime integers `u_lambda,v_lambda`, and define

`m_lambda=max(u_lambda,v_lambda)`.

Because every frequency in `Lambda_Y` comes from a ratio of prime powers at most `Y`, one has

`u_lambda<=Y`, `v_lambda<=Y`.

Take another distinct frequency `mu` with reduced ratio `u_mu/v_mu`. Then

`|lambda-mu|=|log((u_lambda v_mu)/(v_lambda u_mu))|`.

The two cross-products are distinct positive integers, and both are at most `m_lambda Y`. If `M>N` are these products, then

`log(M/N)=integral_N^M dt/t >= (M-N)/M >= 1/(m_lambda Y)`.

Therefore

`delta_(lambda,Y)^(-1) <= m_lambda Y`.

Define the grouped ratio-height energy

`Q_(x,H)(Y)=sum_(lambda in Lambda_Y) m_lambda |B_(lambda,Y)|^2`.

Then exactly

`W_(x,H)(Y) <= Y Q_(x,H)(Y)`.

The gain over `VIS-310` is possible only if `Q` is concentrated at arithmetic ratio heights much smaller than the hard cutoff `Y`.

## 3. Wang's taper gives `Q << x^2 log^3 x` uniformly in the cutoff

It is enough to bound the corresponding full-series grouped moment

`Q_(x,H)(infinity)=sum_lambda m_lambda |B_lambda|^2`,

because finite cutoff only removes cross-base ratio coefficients and decreases the positive same-base fibers already used in the monotonicity argument of `VIS-310`.

Split into cross-base and same-base ratios.

### Cross-base ratios

If `q=p^k` and `r=s^l` have distinct base primes, the reduced ratio is exactly `q/r`, the oriented pair is uniquely determined by that ratio, and

`m_lambda=max(q,r)`.

Hence the cross-base contribution is bounded by

`sum_(q!=r; base(q)!=base(r)) max(q,r) a_q^2 a_r^2 |K_H(q,r)|^2`,

where

`|K_H(q,r)| <= 2/|log(q/r)|`.

Repeat the dyadic estimate of `VIS-307`, now with the extra factor `max(q,r)`. On a comparable shell `Z<q<=2Z`, `q/2<r<2q`, the `VIS-307` shell contribution

`<< Z v_x(Z)^4 log^3(4Z)`

acquires only one additional factor `O(Z)`. Thus it is

`<< Z^2 v_x(Z)^4 log^3(4Z)`.

For `Z<=x` this is

`<< Z^6 x^(-4) log^3(4Z)`,

and for `Z>=x` it is

`<< x^4 Z^(-2) log^3(4Z)`.

Both dyadic sums are dominated by `Z asymp x`, giving

`Q_cross,comp << x^2 L^3`.

For noncomparable pairs, `|log(q/r)|` is bounded below absolutely. By symmetry,

`Q_cross,noncomp`
` << (sum_q q a_q^2)(sum_r a_r^2)`.

The second factor is `O(L)` from `VIS-302`. For the first, below `x` one has `q a_q^2<=Lambda(q)^2`, so the standard square-von-Mangoldt bound gives `O(xL)`; above `x`, comparison with `x^2 sum_(n>x) log^2 n/n^2` gives `O(xL^2)`. Hence

`Q_cross,noncomp << x L^3`,

which is smaller than the comparable bound.

Therefore

`Q_cross << x^2 L^3`.

### Same-base harmonic ratios

For a fixed prime `p` and exponent difference `d>=1`, the reduced ratio is `p^d`. Put

`S_(p,d)=sum_(l>=1) a_(p^(l+d)) a_(p^l)`.

The grouped coefficient has modulus

`|B_(p,d)| <= 2 |S_(p,d)|/(d log p)`.

Introduce

`U_p=sum_(k>=1) p^k a_(p^k)^2`,

`V_p=sum_(k>=1) p^(-k) a_(p^k)^2`.

Weighted Cauchy--Schwarz gives

`p^d |S_(p,d)|^2`
` = |sum_l [p^((l+d)/2)a_(p^(l+d))][p^(-l/2)a_(p^l)]|^2`
` <= U_p V_p`.

After summing `d^(-2)`, both orientations of the same-base spectrum contribute

`Q_same << sum_p U_p V_p/log^2 p`.

For `p<=x`, geometric summation on the two sides of `p^k=x` gives

`U_p << L^2`,

`V_p << L^3/(x^2 log p) + L^2/x^2`.

The crude bound `pi(x)<=x` is already enough to obtain

`sum_(p<=x) U_p V_p/log^2 p << L^5/x`.

For `p>x`, every power lies on the upper taper and

`U_p << x^2 log^2 p/p^2`,

`V_p << x^2 log^2 p/p^4`,

so integer-tail comparison gives

`sum_(p>x) U_p V_p/log^2 p << L^2/x`.

Thus `Q_same` is negligible on the cross-base scale, and altogether

`Q_(x,H)(Y) <= Q_(x,H)(infinity) << x^2 L^3`

uniformly in `H` and `Y`.

Combining with Section 2 gives the key weighted-spacing estimate

`W_(x,H)(Y) << Y x^2 L^3`.

## 4. Finite-window bound and optimization

Substitute the weighted estimate into Section 1:

`V^(-1) integral |R_(x,H,Y)(T)|^2 dT`
` << x L^3 + Y x^2 L^3/V`.

The hard-tail estimate from `VIS-310` remains unchanged:

`sup_T |R_(x,H)(T)-R_(x,H,Y)(T)|`
` << H x^(3/2)/sqrt(Y)`.

Therefore

`V^(-1) integral |R_(x,H)(T)|^2 dT`
` << x L^3 + Y x^2 L^3/V + H^2 x^3/Y`.

Balancing the last two terms gives

`Y^2 asymp H^2 x V/L^3`,

hence

`Y_* = H sqrt(xV/L^3)`.

At this choice the two errors are both

`<< H x^(5/2)L^(3/2)V^(-1/2)`,

which proves the displayed optimized estimate.

At `H asymp x ell`, the first normalized term `L^3/(x ell^2)` tends to zero, while the weighted finite-window/tail term tends to zero provided

`V >> x^3 L^3/ell^2`.

At that threshold the optimized cutoff is itself of order `x^3`; for larger windows it is larger. This makes the remaining obstruction transparent: coefficient weighting repairs the worst-gap loss, but the **uniform hard-tail approximation still forces the proof to retain support out to the cubic scale** before it can certify an `H`-small full remainder.

## 5. What changed relative to VIS-310

`VIS-310` used the single global spacing floor `delta_Y^(-1)<<Y^2`, multiplying the entire Bohr energy `O(xL^3)` by the cost of the closest retained ratio pair. The present calculation keeps the individual ratio heights long enough to prove

`sum m_lambda |B_lambda|^2 << x^2L^3`.

This changes the finite-frequency error from

`Y^2 xL^3/V`

to

`Y x^2L^3/V`.

After balancing against the same uniform tail, the sufficient observation horizon falls from order

`x^5 L^3/ell^2`

to

`x^3 L^3/ell^2`.

The improvement is substantive but still not close to `V asymp x ell`. A further argument that merely sharpens the global minimum gap is therefore unnecessary, and a further weighted-Hilbert calculation that leaves the uniform tail unchanged can at best attack the remaining coefficient moment. The more structural unresolved question is whether the infinite tail can be controlled in **energy on the finite height window**, or whether the true deterministic flow contains a sparse near-resonant component invisible to the Bohr mean.

## Prior art and novelty boundary

The analytic input is classical H. L. Montgomery and R. C. Vaughan, **Hilbert's Inequality**, *Journal of the London Mathematical Society* (2) 8 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`. `VIS-194` already specializes its weighted nearest-neighbor form to a different finite prime-ratio polynomial. The present finding does not claim a new Hilbert inequality, large-sieve theorem, or nonharmonic Fourier estimate.

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv `2609.07918v1` (2026), is the source of the coefficient profile and short-interval pair-correlation setting. `VIS-302`--`VIS-310` record the Mathia reductions from Wang's error terms to the present deterministic prime-power remainder.

A targeted audit confirms that both the weighted-Hilbert tool and Wang source are established inputs. No novelty is claimed for the dyadic summation or rational cross-product spacing argument in isolation. The durable Mathia content is the quantitative specialization showing exactly how much of the quintic `VIS-310` loss came from collapsing the spectrum to one worst gap: preserving coefficient-weighted arithmetic height recovers two powers of `x`, while leaving the hard-tail bottleneck exposed.

## Boundaries and falsification

The theorem is a sufficient finite-window upper bound for fixed `x,H` averaged over the start variable. It does not justify inserting a varying `x(T)` inside the averaging integral without an additional uniform/joint-limit argument.

The weighted spacing `delta_(lambda,Y)` is computed after exact ratio collisions are grouped. The reduced rational height `m_lambda` is part of the proof; using an unreduced pair can only weaken the bound but would obscure the same-base fibers.

The monotonic comparison `Q(Y)<=Q(infinity)` uses the same positivity property as `VIS-310`: cross-base ratios have unique oriented representations, while all contributions to a fixed same-base ratio share the same kernel factor and positive amplitude. If an unaccounted cross-base ratio collision exists, or a same-base fiber carries incompatible kernel phases, the grouped-moment argument must be revised.

The same-base estimate is deliberately crude in logarithms and is used only to show it is negligible relative to `x^2L^3`. Improving those logarithms does not change the cubic conclusion.

Falsify the finding by finding an error in the reduced-ratio spacing floor, the weighted Montgomery--Vaughan endpoint estimate, the dyadic `m_lambda`-weighted cross-base energy, the weighted Cauchy--Schwarz bound for same-base fibers, the inherited hard-tail estimate, or the final optimization.

## Dependencies

- `VIS-302`, `VIS-304`: Wang coefficient profile and current pointwise boundary.
- `VIS-307`, `VIS-308`: exact-support spacing-energy estimates and same-base harmonic grouping.
- `VIS-309`: exact Bohr-time second moment `O(xL^3)` for the true deterministic remainder.
- `VIS-310`: hard-tail truncation and quintic worst-gap finite-window control.
- `VIS-194`, `VIS-195`: weighted local-spacing precedent and arithmetic interpretation for a different finite prime-ratio spectrum.
- `CLUE-wang-fixed-source-packet-localization`: accepted source-localization clue.

## Research consequence

The coefficient-sensitive finite-window branch survives, but its first quantitative gain is now measured. Weighted local spacing alone lowers the hard-truncation proof horizon from quintic to cubic; it does not reach the natural Wang scale.

The next coherent finite-window attack should therefore stop paying the uniform tail cost `H x^(3/2)/sqrt(Y)`. A smooth or dyadic decomposition that controls the discarded ratio spectrum in mean square, or a direct infinite-series finite-window inequality with coefficient-weighted local density, would address the remaining structural loss. Alternatively, an explicit exceptional-height resonance family would show that the small Bohr energy is genuinely nonuniform in a way no generic dephasing estimate can remove.