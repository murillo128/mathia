# PL-184 — Bounded-variation one-point targets remain short-interval-density flat

## Claim

The one-point target obstruction of `PL-183` does not require absolute continuity or a Lipschitz bound. It extends to arbitrary bounded-variation targets, including step functions and jump discontinuities, provided their **total variation** stays below the same short-interval resolution budget.

For `X>=2`, `h>=1`, real `t`, and a complex function `w:[0,1]->C` of bounded variation, write

`kappa=h/X`, `nu=|t|h/(X+h)`, and `V=Var_[0,1](w)`.

With the same prime average and continuum profile as in `PL-183`,

`B_{X,h,w}(t) = pi(X)^(-1) sum_(q<=X, q prime) w(q/X) exp(i t log(1+h/q))`

and

`I_{kappa,t,w} = integral_0^1 w(u) exp(i t log(1+kappa/u)) du`,

fix `0<eta<13/15`. Uniformly over arbitrary sequences `h=h_X>=1`, `t=t_X`, and bounded-variation weights satisfying

`||w_X||_infinity<=1`, `V_X+nu_X<=X^(13/15-eta)`,

one has

`B_{X,h_X,w_X}(t_X) = I_{kappa_X,t_X,w_X} + o(1)`.

The `o(1)` is uniform in this family. Moreover there is an absolute constant `C` such that, whenever `nu>0`,

`|I_{kappa,t,w}| <= C(1+V)/nu`.

Consequently `nu_X->infinity` and `V_X=o(nu_X)` imply `B_{X,h_X,w_X}(t_X)->0`.

Thus a jump discontinuity, a finite step partition, or even a growing collection of one-point windows is not by itself a surviving target-relative mechanism. For example, if `w_X` is the indicator of a union of `J_X` intervals, then `V_X<=2J_X`, so the same continuum flattening holds under the explicit condition `2J_X+nu_X<=X^(13/15-eta)`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-REDIRECT`. The deep number-theoretic input is exactly the Guth--Maynard almost-all short-interval prime number theorem already audited in `PL-181`--`PL-183`. The new step is a standard bounded-variation quadrature/Stieltjes argument. No novelty is claimed for bounded-variation integration, discrepancy estimates, Stieltjes integration by parts, or weighted prime sums. The durable line-specific content is that a class explicitly left open by `PL-183`—discontinuous one-point targets of controlled total variation—still cannot preserve rational-prime-specific information below the current resolution horizon.

## 1. Total variation is the correct local complexity

On a fixed bulk interval `[delta,1]`, put

`psi(u)=t log(1+kappa/u)` and `F(u)=w(u) exp(i psi(u))`.

As in `PL-183`,

`|psi'(u)| = nu (1+kappa)/(u(u+kappa)) <= C_delta nu`

for `u in [delta,1]`, uniformly in `kappa>=0`. Hence the phase factor is absolutely continuous there and

`Var_[delta,1](exp(i psi)) <= integral_delta^1 |psi'(u)| du <= C_delta nu`.

The elementary product inequality for bounded-variation functions gives

`Var_[delta,1](F) <= ||w||_infinity Var(exp(i psi)) + Var(w) <= V+C_delta nu`.

This replaces the pointwise derivative bound `||F'||_infinity<=L+C_delta nu` used in `PL-183`. It is strictly more flexible: isolated jumps, step targets, and arbitrary regulated BV profiles are allowed, and modifying values at prime sample points is not free because every such excursion contributes to total variation.

## 2. The good-offset short-interval argument survives jumps

Use exactly the dyadic good-offset partition from `PL-181`--`PL-183`. On a dyadic block `[Y,2Y]` take cell length

`H=floor(Y^(2/15+eta/3))`.

Guth--Maynard supplies the same almost-all short-interval prime-count asymptotic on the good cells; choosing a good offset makes the total exceptional-cell contribution `o(1)` after normalization. This part is unchanged because `|F|<=1`.

For a good cell `J` and any representative point `u_J` in its normalized image,

`osc_J(F) <= Var_J(F)`.

The good-cell prime count is `O(H/log X)`, while `pi(X)~X/log X`, so replacing `F(q/X)` by `F(u_J)` on that cell costs at most

`O((H/X) Var_J(F))`.

Summing over all good cells in the bulk yields

`O_delta((H/X)(V+nu))`.

The same variation bound controls the error between the sampled step function and the continuum integral. Under `V+nu<=X^(13/15-eta)`,

`(H/X)(V+nu) << X^(2/15+eta/3-1) X^(13/15-eta) = X^(-2eta/3) = o(1)`.

The local prime-count replacement term, the exceptional cells, the incomplete edge cells, and the discarded range `q<=delta X` are exactly those of `PL-183`; they use only `|F|<=1`. Letting `X->infinity` and then `delta->0` proves the stated uniform quadrature.

This argument also handles jumps located exactly at sampled primes. The continuum integral is insensitive to isolated point values, but the prime sum is not; nevertheless a point excursion increases `Var(w)`, and the cellwise variation estimate charges that excursion explicitly. A target cannot encode many chosen primes through isolated spikes while keeping `V` small.

## 3. Bounded variation also gives the high-frequency cancellation bound

Assume `nu>0`. On `(0,1]`, `psi'` has fixed sign, `|psi'|` is monotone, and `|psi'|>=nu`. The first-derivative oscillatory-integral estimate therefore gives, for every `0<=a<b<=1`,

`|integral_a^b exp(i psi(u)) du| <= C/nu`

with an absolute constant `C`. The endpoint at `0` causes no convergence problem because the integrand has modulus one.

Let `G(x)=integral_0^x exp(i psi(u)) du`. Then `||G||_infinity<=C/nu`. For the continuum integral we may replace `w` on its measure-zero set of exceptional point values by a right-continuous BV representative; this does not change `I` and does not increase total variation. That representative defines a finite complex Stieltjes measure `dw` with total variation at most `V`. Integration by parts gives

`I_{kappa,t,w} = w(1)G(1) - integral_(0,1] G dw`,

with the usual harmless endpoint convention. Therefore

`|I_{kappa,t,w}| <= C(1+V)/nu`.

This is the BV analogue of the `(3+L)/nu` estimate in `PL-183`. A target can still phase-match the oscillation if its total variation is comparable with the phase complexity, but that is exactly the boundary the theorem exposes rather than an arithmetic mechanism supplied by the lattice.

## 4. What this removes, and what remains live

The simplest discontinuous repairs of the Kronecker branch are now in the same one-point-density universality class as smooth targets. A bounded number of hard cutoffs, a sub-resolution number of windows, piecewise-constant masks, and other bounded one-variable BV selectors are all homogenized by local prime density. Their discontinuities do not create an RH-sensitive invariant.

The result does **not** remove genuinely arithmetic or high-complexity target structure. In particular it does not cover target variation at or beyond the current `X^(13/15-o(1))` horizon; a selector with enough oscillation to mark a positive proportion of individual primes; factorization, congruence, Möbius/Liouville, or shifted-prime conditions not reducible to a function of `q/X`; joint conditions involving several moving primes; nonlocal transport/operators; or completed couplings that change the averaging law before the one-point quadrature.

The practical redirect is sharper than in `PL-183`: **“make the target discontinuous or thin in the real variable” is not enough unless doing so forces genuinely large total variation or introduces arithmetic/joint information that the one-variable BV model cannot express.**

## 5. Prior-art, matched control, and analytic boundary

The arithmetic theorem remains the published Guth--Maynard almost-all short-interval PNT used in `PL-181`--`PL-183`. Weighted prime sums with slowly varying weights are classical, as already audited there through Büthe. Passing from Lipschitz control to total variation is a standard one-dimensional quadrature/discrepancy principle, and the cancellation estimate is ordinary Stieltjes integration by parts after the first-derivative test. A targeted literature check found no reason to treat this BV extension as a new general theorem; no such novelty claim is made.

The matched-control objection becomes stronger, not weaker. The proof uses only the same almost-all local counting law plus a bound on total variation. Any synthetic or generalized point system with the same local counting and exceptional-set control obeys the same statement. No Euler product, Dirichlet series, functional equation, zero divisor, or analytic continuation enters. Therefore this regime cannot distinguish the rational-prime zeta function from a matched local-density control and cannot by itself select `Re(s)=1/2`.

## Decisive audit test

To falsify the main claim, it is enough to produce a fixed `eta>0` and admissible sequences `h_X,t_X,w_X` with `||w_X||_infinity<=1` and `Var(w_X)+nu_X<=X^(13/15-eta)` for which

`B_{X,h_X,w_X}(t_X)-I_{kappa_X,t_X,w_X}`

does not tend to zero. The only new proof obligation beyond `PL-183` is the cellwise BV replacement; an objection must therefore identify a failure of `osc_J(F)<=Var_J(F)`, of the product-variation estimate, or of summing the good-cell prime-count weights against local variation. The deep short-interval input and its exceptional-set handling are inherited unchanged from `PL-183`.

## Consequence for the research line

The accepted affine non-Haar clue should no longer treat jump discontinuities or a finite/sub-resolution step mask as a structural escape. Within the current short-interval phase-resolution band, a bounded one-point target of sub-resolution total variation is still only a continuum density weight; if its variation is asymptotically smaller than a diverging Kronecker frequency, the readout vanishes.

A live target-relative branch must therefore pay for one of the ingredients that this theorem excludes: genuinely high variation, arithmetic conditioning not encoded by `q/X`, joint/non-product prime relations, nonlocal or completed transport, or analytic control beyond the present short-interval resolution horizon.