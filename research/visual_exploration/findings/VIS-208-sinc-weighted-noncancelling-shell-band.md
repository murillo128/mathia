# VIS-208 — sinc weighting controls the full noncancelling determinant band in start-average energy

## Claim

Keep the notation and hypotheses of `VIS-192`, `VIS-193`, `VIS-203`--`VIS-207`. Fix

`0 <= alpha < 1/2`

and a constant

`0 < kappa < 1/2`.

Let `v` belong to the autocorrelation-taper subclass of `VIS-203`, suppose

`H=H(y)->infinity`,

`H log y / y -> 0`,

and write

`R=R_v(y,H)`,

`b_y=log(1+2/y^2)`.

For the exact shell amplitudes

`B_xi=sum_(lambda-mu=xi) b_lambda b_mu >=0`,

define the truncated finite-start shell polynomial

`E_(<=kappa)(T0)`
` = sum_(0<|xi|<=kappa y b_y)`
`     B_xi sinc(L xi/2)`
`     exp(i xi[T0+(H+L)/2])`.

Then there is a constant depending only on `alpha`, `v`, and `kappa` such that the following holds for all sufficiently large `y`.

First, uniformly for every real

`1 <= A <= kappa y`,

the cumulative exact-shell energy satisfies

`S_(y,H)(A)/R^2`
` <<_(alpha,v,kappa)`
` H A^(2+4alpha) (log y)^2/y^2`,

where

`S_(y,H)(A)=sum_(0<|xi|<=A b_y) B_xi^2`.

Unlike `VIS-207`, this bound is asserted on the whole constant-fraction noncancelling range; its right-hand side need not tend to zero.

Now put

`A_L=2/(L b_y)`

and assume

`1 <= A_L <= kappa y`.

Equivalently, this is the finite-window region from roughly linear up to roughly quadratic scale. The long-start Cesaro energy of the truncated shell polynomial is exactly

`W_kappa(y,H,L)`
` := lim_(X->infinity) X^(-1) int_0^X |E_(<=kappa)(T0)|^2 dT0 / R^2`
` = sum_(0<|xi|<=kappa y b_y)`
`     (B_xi^2/R^2) sinc^2(L xi/2)`.

It obeys the explicit bounds

for `0<alpha<1/2`,

`W_kappa(y,H,L)`
` <<_(alpha,v,kappa)`
` H y^(2+4alpha) (log y)^2 / L^2`,

while at the critical unweighted case `alpha=0`,

`W_kappa(y,H,L)`
` <<_(v,kappa)`
` [H y^2 (log y)^2/L^2]`
` [1+log(kappa y/A_L)]`.

Since `A_L asymp y^2/L`, the latter may be written more transparently as

`W_kappa(y,H,L)`
` <<_(v,kappa)`
` [H y^2 (log y)^2/L^2]`
` [1+log_+(L/y)]`.

Consequently, for `0<alpha<1/2`,

`L / [y^(1+2alpha) sqrt(H) log y] -> infinity`

implies

`W_kappa(y,H,L)->0`

whenever `A_L` remains in the stated range. For `alpha=0`, it is enough that

`H y^2 (log y)^2 [1+log_+(L/y)] / L^2 ->0`.

Thus the sinc factor does materially extend the `VIS-207` safe zone: after weighting by the actual finite-start kernel, the whole noncancelling determinant band up to any fixed fraction below the first prime/prime one-cancellation scale has vanishing **Cesaro start-energy** under the displayed window conditions, even though the unweighted cumulative shell energy need not vanish at `A asymp y`.

Equivalently, for every fixed `eta>0`, the Cesaro density of starts satisfying

`|E_(<=kappa)(T0)| > eta R`

tends to zero whenever `W_kappa->0`.

**Evidence/status:** `EXACT-DERIVED + SINC-WEIGHTED SHELL SUMMATION + GROWING-WINDOW INCIDENCE + TYPICAL-START CONSEQUENCE + NO-NOVELTY-CLAIM`.

This is not a uniform-in-`T0` finite-start theorem and does not control the one-cancellation-and-above shell region.

## 1. The `VIS-207` incidence estimate actually holds up to `A<=kappa y`

The vanishing hypothesis in `VIS-207` was used to state a dilute corridor, but its local incidence argument survives farther.

Take

`1<=A<=kappa y`.

Because

`b_y=log(1+2/y^2) <= 2/y^2`,

one has

`A b_y <= 2 kappa/y`.

Also

`log(1+1/y) >= 1/(y+1)`.

Since `2 kappa<1`, for all sufficiently large `y`,

`A b_y < log(1+1/y)`.

Therefore no nonzero one-cancellation shell can occur in the range

`0<|xi|<=A b_y`.

All such shells lie in the noncancelling determinant regime of `VIS-195` and retain the exact-shell multiplicity cap at four from `VIS-204`.

Let

`E_y(A)=exp(A b_y)-1`.

Because `A<=kappa y`, one has `A b_y=O_kappa(1/y)`, hence

`E_y(A) <<_kappa A/y^2`.

For a close pair, write the two associated prime products as `U,V` and

`h=|U-V|>=2`.

Exactly as in `VIS-207`,

`h/min(U,V) <= E_y(A)`.

Since `min(U,V)<=y^2`, this gives

`h <<_kappa A`.

Conversely, `h>=2` gives

`min(U,V) >>_kappa y^2/A`.

Every prime factor in either product is at most `y`, so every participating prime is at least

`>>_kappa y/A`.

Fix one prime-ratio frequency represented by `p<q`. For each determinant level `h=O_kappa(A)` and each of the constantly many sign/orientation choices, a neighboring prime pair lies on one linear Diophantine fiber such as

`q r-p s=+/-h`.

Its integer solutions form a progression with step `(p,q)`. Since `p,q>>_kappa y/A`, only `O_kappa(A)` progression parameters can keep both coordinates in `(0,y]`.

There are `O_kappa(A)` determinant levels. Hence the close-pair graph at radius `A b_y` has

`deg_A(lambda) <<_kappa A^2`

on every non-isolated vertex.

The coefficient calculation of `VIS-207` is unchanged. A non-isolated frequency has both primes `>>_kappa y/A`, so

`|c_lambda|^2`
` <<_(alpha,v,kappa)`
` A^(4alpha) (log y)^2/y^2`.

The strict subcritical normalization gives

`R asymp_(alpha,v) 1/H`,

therefore

`nu(lambda)=|c_lambda|^2/R`
` <<_(alpha,v,kappa)`
` H A^(4alpha)(log y)^2/y^2`.

Degree times maximal non-isolated vertex mass yields

`Q_(y,H)(A)`
` <<_(alpha,v,kappa)`
` H A^(2+4alpha)(log y)^2/y^2`.

Since every shell in the present range is noncancelling and has multiplicity at most four, `VIS-205` gives

`S_(y,H)(A)/R^2 <= 4 Q_(y,H)(A)`,

proving the cumulative bound in the claim without assuming that its right-hand side tends to zero.

## 2. The sinc factor converts cumulative shell growth into a weighted integral

Set

`beta=2+4alpha`,

`epsilon_y=H(log y)^2/y^2`,

and define the nondecreasing cumulative function

`F(A)=S_(y,H)(A)/R^2`.

Section 1 gives

`F(A) << epsilon_y A^beta`

uniformly on

`1<=A<=kappa y`.

For a shell with normalized coordinate

`a=|xi|/b_y`,

one has

`L|xi|/2=a/A_L`.

The elementary bound

`|sinc x| <= min(1,1/|x|)`

therefore gives

`sinc^2(L xi/2) <= min(1,(A_L/a)^2)`.

Interpreting the shell energies as the jumps of `F`,

`W_kappa`
` <= int_[1,kappa y] min(1,(A_L/a)^2) dF(a)`.

Because `1<=A_L<=kappa y`, split at `A_L`. Stieltjes integration by parts gives

`W_kappa`
` <= (A_L/(kappa y))^2 F(kappa y)`
`    + 2 A_L^2 int_(A_L)^(kappa y) F(a) a^(-3) da`.

The unweighted term `F(A_L)` cancels exactly between the two pieces. This is the analytic reason sinc attenuation can use a cumulative incidence estimate beyond the radius at which the unweighted shell mass itself is small.

## 3. Evaluation for `alpha>0`

When `alpha>0`,

`beta-2=4alpha>0`.

Insert

`F(a)<<epsilon_y a^beta`

into the preceding bound. Then

`W_kappa`
` << epsilon_y A_L^2 (kappa y)^(beta-2)`
`    + epsilon_y A_L^2 int_(A_L)^(kappa y) a^(beta-3) da`
` <<_(alpha,kappa)`
` epsilon_y A_L^2 y^(4alpha)`.

Since

`b_y asymp y^(-2)`,

`A_L=2/(L b_y) asymp y^2/L`.

Therefore

`W_kappa`
` <<_(alpha,v,kappa)`
` [H(log y)^2/y^2] [y^4/L^2] y^(4alpha)`
` = H y^(2+4alpha)(log y)^2/L^2`.

This tends to zero under

`L / [y^(1+2alpha)sqrt(H)log y] -> infinity`.

The estimate reaches `A asymp y`, far beyond the unweighted `VIS-207` corridor

`epsilon_y A^beta ->0`.

It works because shells near the edge of the band carry a sinc penalty of order `(A_L/A)^2`.

## 4. The endpoint exponent `alpha=0` is logarithmic

At `alpha=0`, `beta=2`, so the Stieltjes integral is exactly at its logarithmic boundary:

`W_kappa`
` <<_v epsilon_y A_L^2`
`    [1+int_(A_L)^(kappa y) da/a]`
` <<_(v,kappa)`
` epsilon_y A_L^2 [1+log(kappa y/A_L)]`.

Using

`epsilon_y=H(log y)^2/y^2`

and

`A_L asymp y^2/L`

gives

`W_kappa`
` <<_(v,kappa)`
` H y^2(log y)^2/L^2`
` [1+log_+(L/y)]`.

The additional logarithm is not a claim about the true shell distribution. It is the critical exponent produced by summing the available cumulative upper bound `F(A)<<epsilon_y A^2` against the `A^-2` sinc envelope.

A simple stronger but easier sufficient condition is

`L >> y sqrt(H) (log y)^(3/2)`

when `L<=y^2`, because then `1+log_+(L/y)<=1+log y`.

## 5. Cesaro-typical starts inherit the shell-energy gain

`VIS-203` already gives exact orthogonality between distinct shell frequencies in the long average over `T0`. Applied to the truncated polynomial,

`lim_(X->infinity) X^(-1) int_0^X |E_(<=kappa)(T0)|^2 dT0`
` = R^2 W_kappa`.

Hence whenever `W_kappa->0`, Chebyshev gives for every fixed `eta>0`,

`limsup_(X->infinity)`
` X^(-1) meas{0<=T0<=X: |E_(<=kappa)(T0)|>eta R}`
` <= W_kappa/eta^2`
` ->0`.

So the complete noncancelling determinant band below any fixed fraction of the first one-cancellation scale is negligible for a Cesaro-density-one set of finite-window starts under the stated conditions.

This conclusion is deliberately weaker than uniformity in `T0`. A small long-start `L^2` norm does not exclude rare starts where many distinct shell phases align.

## Prior-art audit

No new analytic theorem is used here. The sinc envelope, Stieltjes/Abel summation, and Cesaro orthogonality of a finite exponential polynomial are classical. `VIS-193` already anchors the relevant finite-interval Fourier framework in Montgomery--Vaughan's Hilbert inequality, while `VIS-203` records the exact shell expansion and long-start orthogonality used here.

The determinant-fiber and prime-normalization inputs are exactly those audited in `VIS-195`--`VIS-207`; in particular the determinant-surface literature cited there already bounds any novelty claim for the incidence geometry. The present result does not improve a general determinant-counting theorem, a large-sieve theorem, or a classical sinc-kernel estimate.

The Mathia-specific content is the combination of the actual prime-ratio cumulative shell bound with the exact finite-start sinc kernel. It shows that the `VIS-207` local-degree mechanism remains useful even after its unweighted dilution corridor ends: weighted summation carries it through the entire noncancelling determinant band below the first cancellation scale.

No novelty is claimed beyond this specialization and bookkeeping consequence.

## Boundaries and falsification

The constant `kappa` is fixed strictly below `1/2`. The proof deliberately stops before the first prime/prime one-cancellation scale. At and above that scale, shared-anchor shells can have different and growing multiplicity, so the factor-four shell comparison cannot simply be reused.

The estimate concerns the autocorrelation-taper subclass of `VIS-203`, where within-shell amplitudes are nonnegative. Sign-changing centered tapers require a different exact-shell decomposition and may have additional cancellation.

The conclusion is about the long-start mean square of the **truncated noncancelling shell contribution**. It does not bound the full finite-start error, does not control shells at or above the one-cancellation scale, and does not imply a uniform-in-start estimate.

The cumulative estimate uses only worst-case local degree and maximal dangerous vertex mass. It may be far from sharp. In particular, the logarithmic loss at `alpha=0` and the factor `y^(4alpha)` for `alpha>0` may be artifacts of this coarse cumulative bound.

Falsify the finding by exhibiting, for some fixed `kappa<1/2`, a shell below `kappa y b_y` that enters the one-cancellation regime; a failure of the `O(A^2)` local-degree or `A^(4alpha)` vertex-mass bounds for some `A<=kappa y`; a noncancelling shell with multiplicity exceeding four; or an error in the Stieltjes summation of the sinc-weighted shell measure.

## Research consequence

The positive-shell route has now crossed the gap that `VIS-207` left explicitly open. The unweighted pair-crowding estimate becomes too large before the first cancellation scale, but the actual finite-start sinc kernel suppresses successive widening determinant shells strongly enough to control their **start-averaged energy** all the way to any fixed fraction below that scale.

The remaining obstruction is sharper: one must now understand the one-cancellation-and-above shells, or strengthen start-average control to uniform-in-`T0` control. Reopening the subcritical noncancelling determinant band without one of those new ingredients would not address the surviving frontier.
