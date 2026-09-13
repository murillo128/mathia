---
id: CLUE-visual-four-form-average-local-factor
type: research-clue
status: proposed
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-197-same-sign-gap-fiber-local-conductor.md
  - research/visual_exploration/findings/VIS-198-polynomial-subcritical-three-form-sieve.md
  - research/visual_exploration/findings/VIS-199-four-form-sieve-stretched-exponential-horizons.md
  - research/visual_exploration/findings/VIS-200-four-form-cutoff-optimization-barrier.md
---

# Can averaging the four-form local factor remove the remaining log-log horizon loss?

## Observation

`VIS-197` reduces every nondegenerate fixed-`A` dangerous gap fiber to four affine forms with finite conductor carrier

`Q=d_0 e_0 g m (m^2-g^2 d_0^2 e_0^2)`

and bounds its singular/local factor pointwise by

`S_4(d,e) <<_A (|Q|/phi(|Q|))^4 <<_A (1+log log y)^4`.

`VIS-199` then inserts this worst-case factor before summing the fibers, while `VIS-200` proves that changing the scalar sieve/taper cutoff cannot remove the resulting threshold. The remaining logarithmic loss therefore enters at a very specific place: **pointwise maximization of the exceptional local arithmetic before the `e`-fiber average is taken**.

There is a plausible averaging route that was not used in those findings. For fixed `g,m,d_0`, the variable part of `Q` factors through the three linear polynomial values

`e_0`, `m-g d_0 e_0`, `m+g d_0 e_0`.

The top-scale relation `e p=d r+O_A(1)` with all four primes `Theta_A(y)` also confines `e_0` to an interval of length and location `Theta_A(d_0)`. Kevin Henriot's discriminant-uniform Nair--Tenenbaum bounds give short-interval upper bounds for multiplicative weights evaluated on polynomial values with explicit dependence on the polynomial discriminant. In this three-linear-form specialization, the variable discriminant support appears to be carried only by primes dividing `d_0`, up to the fixed `A`-dependent factors coming from `g,m`.

Relevant prior art is Kevin Henriot, **Nair--Tenenbaum bounds uniform with respect to the discriminant**, *Math. Proc. Cambridge Philos. Soc.* 152:3 (2012), 405--424, DOI `10.1017/S0305004111000752`, together with the 2014 erratum DOI `10.1017/S0305004114000280`. Gallagher's classical averaging of fixed-dimensional singular series is a broader precedent for average local-factor cancellation, but it is not by itself the coefficient-dependent estimate needed here.

## Research question

Can the nondegenerate four-form fibers be averaged before taking the worst local factor, with a bound of the form

`sum_(e in I_A(d)) S_4(d,e) <<_A d G_A(d)`

where `I_A(d)` is the top-scale admissible `e` interval and `G_A` has bounded mean,

`sum_(d<=D) G_A(d) <<_A D`?

A sufficient version would follow if the discriminant-uniform polynomial-value estimate yields only a correction

`G_A(d) <= prod_(p|c_A d) (1+C_A/p)`

or another multiplicative majorant with bounded first mean. Indeed such products have bounded mean by the elementary divisor expansion against `sum k^(-2)`.

If this average estimate holds, the four-form sieve region in `VIS-199`/`VIS-200` would lose the pointwise factor `B(y)=(1+log log y)^4`. The expected replacement bound is

`C_(y,H)(A) <<_A (log y)^2/[log(H/L)]^4 + (log y)^2/L^3 + H/(y log y)`.

With a tail-safe `L=(log y)^(2/3) omega(y)`, this would move the present sufficient horizon condition from

`(1+log log y) sqrt(log y) = o(log H)`

to essentially

`sqrt(log y) = o(log H)`,

without changing the dephasing resource `D_v` or the four-form sieve dimension.

## Why it may matter

`VIS-200` closes cutoff tuning as an independent escape route and identifies average local-factor/fiber mass as one of the few remaining ways to improve the same proof architecture. Removing the worst-case `(log log y)^4` penalty would therefore be a genuine mathematical advance within that architecture rather than another parameter optimization.

The question is also sharply falsifiable. Either the coefficient-dependent affine family admits a bounded-mean discriminant correction after averaging `e`, or some persistent arithmetic concentration forces an average loss of the same order as the pointwise bound. In the latter case the current local-factor bottleneck becomes substantially more structural and attention should move to coupled incidence estimates or a different resource.

## Decisive test

Fix the finite `A`-dependent choices of `g,m` and one first gap `d_0`. Separate the already-classified `Q=0` branch. On the top-scale interval `e_0=Theta_A(d_0)`, apply the corrected discriminant-uniform Nair--Tenenbaum/Henriot theorem to the three pairwise non-proportional linear factors

`R_1(E)=E`, `R_2(E)=m-g d_0 E`, `R_3(E)=m+g d_0 E`

with a positive multiplicative majorant sufficient to dominate `(Q/phi(Q))^4`. Before using the result, verify explicitly the hypotheses and the 2014 erratum: primitive/pairwise-coprime normalization after bounded fixed contents, coefficient-norm versus interval-length condition, treatment of signs/absolute values, and the exact discriminant correction.

Then prove or refute both required stages:

1. the discriminant correction is bounded by a fixed-factor multiple of `prod_(p|d_0)(1+C_A/p)` (or a comparably mild majorant), rather than reintroducing a worst-case `log log y` loss;
2. its weighted first-gap average remains bounded after the taper, namely

`sum_d min(1,(Y/d)^4) G_A(d/g) <<_A Y`.

If both stages pass, insert the averaged estimate into the exact `VIS-199` fiberwise four-form sieve and rederive the normalized crowding bound above, keeping the conductor-zero branch and unsieved tail unchanged.

Kill this route if the corrected theorem is not uniform in the required coefficient/interval regime, if common contents or discriminant primes introduce a correction with unbounded mean, if the top-scale `e` interval is too short for the polynomial-value theorem, or if the resulting weighted aggregate still necessarily carries a `(log log y)^c` factor large enough to leave the `VIS-200` threshold unchanged.

## Evidence boundary

No averaged four-form singular-series estimate for the Mathia fibers is established here, and the Henriot theorem has **not yet been checked line by line against this coefficient-dependent specialization and its erratum**. The displayed improved crowding bound and `sqrt(log y)` horizon are conditional consequences of the proposed average estimate, not findings.

The observation only isolates a concrete route that appears compatible with existing discriminant-uniform multiplicative polynomial-average machinery. It makes no novelty claim for Nair--Tenenbaum bounds, Henriot's discriminant uniformity, Gallagher singular-series averaging, Selberg sieve, or average orders of elementary multiplicative products.
