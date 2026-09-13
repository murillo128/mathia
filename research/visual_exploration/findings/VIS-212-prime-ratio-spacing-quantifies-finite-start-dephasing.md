# VIS-212 — prime-ratio spacing makes finite-start dephasing quantitative at quadratic horizon

## Claim

Keep the tapered quadratic statistic and notation of `VIS-192`. Fix `0<=alpha<1/2`, let

`Q_y=sum_(p<=y) p^(-2alpha)`,

and write

`M_v(y;H,T)-1 = 2 Re S_v(y;H,T)`

with

`S_v(y;H,T)`
` = Q_y^(-1) sum_(p<q<=y) p^(-alpha) q^(-alpha)`
`   kappa_v(H log(q/p)) exp(i T log(q/p))`.

Let `R_v(y,H)` be the long-start Cesaro variance from `VIS-192`. Then there is an absolute constant `C>0` such that, for every `y>=3`, every `H>0`, every start `T_0`, and every averaging length `L>0`,

`| L^(-1) integral_(T_0)^(T_0+L) |M_v(y;H,T)-1|^2 dT - R_v(y,H) |`
` <= C (y^2/L) R_v(y,H)`.

Equivalently,

`L^(-1) integral_(T_0)^(T_0+L) |M_v(y;H,T)-1|^2 dT`
` = R_v(y,H) [1 + O(y^2/L)]`,

uniformly in the location `T_0` of the finite start window.

The only arithmetic input needed for the finite-horizon conversion is the elementary separation of distinct prime-ratio frequencies:

`min |log(q/p)-log(s/r)| >= y^(-2)`

for distinct reduced prime ratios `q/p != s/r` with all primes at most `y`, together with the same lower scale for the reflected frequencies `-log(q/p)`.

Consequently:

- if `L/y^2 -> infinity`, the finite-window mean square converges uniformly in `T_0` to the infinite-Cesaro value `R_v(y,H)`;
- if merely `L >= c y^2` for any fixed `c>0`, then the finite-window mean square is `O_c(R_v(y,H))` uniformly in `T_0`;
- using the `VIS-192` upper bound `R_v(y,H)<<1/H`, every family with `H->infinity`, `H<=y`, and `L>=c y^2` has

`sup_(T_0) L^(-1) integral_(T_0)^(T_0+L) |M_v(y;H,T)-1|^2 dT << 1/H ->0`;

- therefore, for every fixed `epsilon>0`, the fraction of starts `T` inside **every** interval `[T_0,T_0+L]`, `L>=c y^2`, for which `|M_v(y;H,T)-1|>epsilon` is `O_(c,alpha,v)(1/(epsilon^2 H))`.

Thus the density-one start cancellation of `VIS-192` does not require taking an unspecified infinite Cesaro horizon. A deterministic quadratic start horizon `L asymp y^2` already gives uniform sliding-window mean-square dephasing. This is still not a pointwise-in-`T` theorem.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + QUANTITATIVE FINITE-START MEAN VALUE + NO-NOVELTY-CLAIM`.

## 1. The signed statistic is one finite separated exponential polynomial

For each prime pair `p<q<=y`, define

`lambda_(p,q)=log(q/p)`

and

`c_(p,q)=Q_y^(-1) p^(-alpha) q^(-alpha) kappa_v(H lambda_(p,q))`.

Then

`M_v(y;H,T)-1`
` = sum_(p<q) c_(p,q) exp(i lambda_(p,q) T)`
`   + sum_(p<q) conjugate(c_(p,q)) exp(-i lambda_(p,q) T)`.

So the real signed statistic is itself a finite exponential polynomial on the symmetric frequency set

`Lambda_y={+/- log(q/p): p<q<=y, p,q prime}`.

The coefficient square mass of this symmetric polynomial is exactly

`2 sum_(p<q) |c_(p,q)|^2 = R_v(y,H)`,

by the exact Cesaro identity in `VIS-192`.

The finite-horizon problem is therefore reduced to one question: how closely can two distinct frequencies in `Lambda_y` approach each other?

## 2. Distinct prime ratios have deterministic spacing at least `y^-2`

First take two positive frequencies

`lambda=log(q/p)`, `mu=log(s/r)`

with distinct prime pairs and `q/p != s/r`. Since each fraction is reduced, equality of the ratios would force the same pair by unique factorization. Hence

`qr != ps`.

Assume `qr>ps`. Both are positive integers at most `y^2`, so

`qr-ps >=1`.

Using `log x >= (x-1)/x` for `x>=1`,

`lambda-mu`
` = log(qr/ps)`
` >= (qr-ps)/qr`
` >= y^(-2)`.

The same estimate applies to two negative frequencies.

For opposite signs, the distance is

`log(q/p)+log(s/r)`.

Every positive prime-ratio frequency satisfies

`log(q/p) >= log(1+1/y) >= 1/(2y)`

for `y>=3`, so opposite-sign frequencies are separated by at least `1/y`, which is stronger than `y^-2`.

Therefore the complete symmetric frequency set obeys the deterministic global separation

`delta(Lambda_y) >= y^(-2)`.

No prime-gap conjecture, pair-correlation model, or random-phase assumption enters this step. It is only the rational geometry of reduced prime ratios.

## 3. Montgomery–Vaughan converts separation into a finite-window mean value

The Montgomery–Vaughan generalized Hilbert inequality gives the standard separated-frequency mean-value estimate: for a finite exponential polynomial

`F(T)=sum_j d_j exp(i lambda_j T)`

whose real frequencies have minimum spacing `delta>0`,

`integral_(T_0)^(T_0+L) |F(T)|^2 dT`
` = L sum_j |d_j|^2 + O(delta^(-1) sum_j |d_j|^2)`,

uniformly in the interval location `T_0`. Translating the interval only multiplies each coefficient by a phase and therefore does not change the estimate.

Apply this theorem directly to

`F(T)=M_v(y;H,T)-1`

with the symmetric frequency set `Lambda_y`. The preceding section gives `delta^(-1)<=y^2`, while the coefficient square mass is exactly `R_v(y,H)`. Hence

`integral_(T_0)^(T_0+L) |M_v(y;H,T)-1|^2 dT`
` = L R_v(y,H) + O(y^2 R_v(y,H))`.

Division by `L` proves the claim.

This argument is stronger than applying a mean-value theorem only to `S_v` and then bounding `2 Re S_v` crudely: treating the positive and negative frequencies together recovers the exact Cesaro main term `R_v`, not merely a constant-factor upper bound.

## 4. Uniform sliding-window density-one cancellation

`VIS-192` already proves, whenever `H=H(y)->infinity` and `H<=y`,

`R_v(y,H)<<_(alpha,v) 1/H`.

If `L>=c y^2`, the finite-horizon formula therefore gives uniformly in `T_0`

`L^(-1) integral_(T_0)^(T_0+L) |M_v(y;H,T)-1|^2 dT`
` <<_(c,alpha,v) 1/H`.

Chebyshev on each interval yields

`L^(-1) meas{T in [T_0,T_0+L]: |M_v(y;H,T)-1|>epsilon}`
` <<_(c,alpha,v) 1/(epsilon^2 H)`.

Thus as `H->infinity`, every sliding start window of quadratic length contains an asymptotic density-one set of good starts. The interval may begin anywhere; unlike the original Cesaro statement, no limit `T_0=0`, `L->infinity` is built into the conclusion.

In the strictly subcritical regime `H log y/y->0`, `VIS-192` also has `R_v(y,H) asymp 1/H`. If in addition `L/y^2->infinity`, then

`L^(-1) integral_(T_0)^(T_0+L) |M_v(y;H,T)-1|^2 dT`
` = (1+o(1)) R_v(y,H)`
` asymp 1/H`

uniformly in `T_0`.

## 5. What the quadratic horizon means geometrically

The scale `y^2` comes from the worst deterministic collision geometry of the ratio frequencies, not from the taper and not from the long-start variance itself. Two frequencies differ by

`log(qr/ps)`,

so the obstruction is a near-collision between two semiprime cross-products. The crude universal fact `|qr-ps|>=1` produces the `y^-2` spacing and therefore the `y^2` dephasing horizon.

This identifies a sharper frontier than the qualitative phrase "finite-start coherence". Any attempt to prove dephasing on substantially shorter start horizons must exploit more than global distinctness of prime ratios. It must show that the coefficients cannot place enough mass on the rare near-collision geometry, or otherwise use arithmetic structure of the weighted determinant

`qr-ps`.

That is a different problem from the one-cancellation shell classification closed by `VIS-211`: the present theorem concerns quantitative orthogonality among the original prime-ratio frequencies in the start variable.

## Prior-art audit

The separated-frequency mean-value theorem is classical. H. L. Montgomery and R. C. Vaughan, **Hilbert's Inequality**, *Journal of the London Mathematical Society* s2-8:1 (1974), 73–82, DOI `10.1112/jlms/s2-8.1.73`, develops the generalized Hilbert inequality underlying the `L+O(delta^-1)` mean-value estimate for separated exponential frequencies. Montgomery's **Mean and large values of Dirichlet polynomials**, *Inventiones Mathematicae* 8 (1969), 334–345, DOI `10.1007/BF01404637`, is a classical anchor for the broader Dirichlet-polynomial mean-value viewpoint already cited in `VIS-192`.

No novelty is claimed for the Montgomery–Vaughan inequality, finite exponential-polynomial mean values, Chebyshev's inequality, or the elementary spacing estimate for distinct bounded rationals. The Mathia-specific step is to combine them with the exact `VIS-192` prime-ratio representation and normalization, making the previously qualitative finite-start frontier explicit: quadratic start windows already recover the long-start mean square uniformly in their location.

## Boundaries and falsification

The theorem does **not** give a pointwise bound on `|M_v(y;H,T)-1|` for every start `T`. It gives a uniform mean-square statement over every sufficiently long finite start interval, and hence a density-one statement inside each such interval.

The quadratic horizon is a sufficient deterministic scale, not a claimed optimum. The global separation `delta>=y^-2` deliberately ignores coefficient weights, the taper suppression, distribution of the determinants `qr-ps`, and the possibility that the closest frequency pairs carry negligible mass. Any of those could permit a shorter effective horizon.

Conversely, the theorem does not assume that prime-ratio spacings actually attain order `y^-2`; no such lower construction is needed. Therefore it gives no lower bound showing that `y^2` is necessary.

The `R_v<<1/H` consequence uses the hypotheses of `VIS-192`, in particular fixed `alpha<1/2` and the same endpoint-zero taper class. The finite-frequency mean-value identity itself only needs the finite coefficient representation and the ratio-frequency separation.

Falsify this finding by locating an error in the reduction to the symmetric frequency polynomial, the identification of its coefficient square mass with `R_v`, the rational separation bound, or the application of the Montgomery–Vaughan separated-frequency mean-value estimate.

## Research consequence

The open finite-start problem now has a quantitative baseline. Infinite Cesaro averaging is unnecessary for density-one cancellation: a deterministic start horizon of order `y^2` already works uniformly over where the start interval is placed.

The unresolved question is not whether finite-horizon dephasing can be proved at all, but whether the quadratic worst-rational-spacing horizon can be compressed toward a scale relevant to the observation problem by exploiting weighted prime-ratio collision geometry. That next question requires new information about the coefficient mass carried by small determinants `|qr-ps|`; it is not needed to establish the present result.