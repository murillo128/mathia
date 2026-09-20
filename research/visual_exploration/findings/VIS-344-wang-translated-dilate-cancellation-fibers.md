# VIS-344 — translated Wang dilates cannot pool uniform tail cancellation across phase fibers

## Claim

Let Wang's exact summatory-remainder multiplier from `VIS-333` be

`m(xi)=4(1+i xi)/(4+xi^2)`.

Fix finitely many triples `(a_j,b_j,c_j)` with `a_j>0`, `b_j` real and `c_j` complex, and combine duplicate pairs `(a_j,b_j)` first. Define the translated-dilate mixture

`M(xi)=sum_j c_j exp(-i b_j xi) m(a_j xi)`.

For each distinct translation `b`, let

`J_b={j:b_j=b}`

and let `n_b` be the number of distinct scales `a_j` in that fiber whose merged coefficient is nonzero. If, for an integer `r>=2`,

`M(xi)=O(|xi|^(-r))`

as real `|xi|->infinity`, then every active translation fiber must independently satisfy

`sum_(j in J_b) c_j a_j^(-k)=0`, `k=1,...,r-1`.

Consequently

`r <= min_(active b) n_b`.

If there are `B` active translation fibers and `N=sum_b n_b` active translated dilates in total, then necessarily

`N >= B r`.

Thus **distinct translations cannot pool their oscillatory phases to create extra uniform polynomial high-frequency decay**. To obtain order `r`, every translation fiber must itself contain enough dilates to cancel the first `r-1` inverse-frequency moments. In particular, adding translation phases does not evade the scale-count obstruction of `VIS-343`; for uniform tail smoothing it makes the cancellation budget at least as expensive, and strictly more expensive when several translation fibers remain active.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL EXPONENTIAL-POLYNOMIAL/ALMOST-PERIODIC STRUCTURE + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

The claim concerns real-frequency **uniform polynomial tail decay** with frequency-independent coefficients. It does not classify finite-window cancellation, frequency-dependent coefficients, source-adaptive nonlinear packet selection, or estimates that exploit arithmetic signs of `G` rather than the multiplier tail alone.

## 1. Expansion by translation fiber

From `VIS-343`, for every fixed `K>=1`,

`m(z)=sum_(k=1)^K beta_k z^(-k)+O(|z|^(-K-1))`,

with every `beta_k != 0`.

Substituting `z=a_j xi` and grouping equal translations gives

`M(xi)=sum_(k=1)^K beta_k xi^(-k) P_k(xi)+O(|xi|^(-K-1))`,

where

`P_k(xi)=sum_b S_(b,k) exp(-i b xi)`

and

`S_(b,k)=sum_(j in J_b) c_j a_j^(-k)`.

Each `P_k` is a finite exponential polynomial. The oscillatory phase does not alter the inverse-power order; it only replaces the scalar moment from `VIS-343` by one coefficient for each translation frequency.

## 2. A finite exponential polynomial cannot decay at infinity unless it vanishes

Let

`P(x)=sum_(l=1)^L d_l exp(-i lambda_l x)`

with distinct real `lambda_l`. If `P(x)->0` as `x->+infinity`, then every `d_l=0`.

A direct mean-square proof is enough. Expanding and averaging,

`(1/T) integral_0^T |P(x)|^2 dx`

`= sum_l |d_l|^2 + sum_(l!=q) d_l conjugate(d_q) [(1-exp(-i(lambda_l-lambda_q)T))/(i(lambda_l-lambda_q)T)]`.

The off-diagonal terms tend to zero, so the mean square tends to `sum_l |d_l|^2`. But if `P(x)->0`, boundedness of the finite sum implies the same Cesaro mean tends to zero. Hence all coefficients vanish.

This is the finite-dimensional instance of the classical uniqueness/mean structure of Bohr almost-periodic functions. Finite sums `sum d_l exp(i lambda_l x)` are generalized trigonometric polynomials and are standard examples in almost-periodic theory.

## 3. Uniform tail decay forces fiberwise moment cancellation

Assume `M(xi)=O(|xi|^(-r))` with `r>=2`.

Multiply the expansion by `xi`. Since all terms beyond the first are `O(|xi|^-1)`,

`xi M(xi)=beta_1 P_1(xi)+O(|xi|^-1)`.

The left side tends to zero, so `P_1(xi)->0`. By the exponential-polynomial lemma, `P_1` is identically zero, hence

`S_(b,1)=0`

for every translation fiber `b`.

Now suppose inductively that `P_1=...=P_(q-1)=0` for some `q<r`. Multiplying the remaining expansion by `xi^q` gives

`xi^q M(xi)=beta_q P_q(xi)+O(|xi|^-1)`.

Again the left side tends to zero because `q<r`, so `P_q(xi)->0`; therefore `P_q` vanishes identically and

`S_(b,q)=0`

for every `b`.

Induction yields the fiberwise moment conditions for every `k=1,...,r-1`.

## 4. Vandermonde cost inside each phase fiber

Fix an active translation `b` and write its distinct inverse scales as

`x_j=a_j^(-1)`, `j in J_b`.

The required conditions are

`sum_(j in J_b) c_j x_j^k=0`, `k=1,...,r-1`.

Exactly as in `VIS-343`, the first `n_b` moment equations form an invertible Vandermonde system after multiplication by the nonzero `x_j`. A nonzero coefficient vector in this fiber therefore cannot cancel moments `k=1,...,n_b` simultaneously.

Hence a nonzero fiber capable of global order `r` must have

`r<=n_b`.

Because this is true for every active translation fiber,

`r<=min_b n_b`.

Summing `n_b>=r` over the `B` active fibers gives the total component cost

`N>=Br`.

The one-fiber case `B=1` reduces exactly to the ceiling in `VIS-343`. Multiple translation phases do not improve the uniform asymptotic order; they split the cancellation equations into independent phase fibers.

## 5. Consequence for the Wang packet escape

The accepted Wang clue left translated/phase-sensitive packets outside the pure-dilation Vandermonde obstruction. The present result closes one precise part of that escape.

If the claimed benefit of translations is **uniform high-frequency polynomial smoothing** of a finite or scale-indexed linear combination with frequency-independent weights, then cross-translation interference cannot buy the missing orders. A target effective order `r_eff(u)` must be realized independently inside every active translation fiber. Combining with `VIS-342`, a fixed Vinogradov-Korobov power-class gain `delta>0` still requires

`r_eff(u)=u^(5 delta/2+o(1))`,

and therefore each active translation fiber must contain at least that many distinct scales. With `B(u)` active translations the total translated-dilate count satisfies the stronger necessary condition

`N(u) >= B(u) u^(5 delta/2+o(1))`.

This remains only a necessary scalar-tail condition. It does not rule out a genuinely nonuniform mechanism in which a packet is localized to selected frequency windows, uses frequency-dependent/adaptive weights, or couples to signed arithmetic structure of `G` so that the relevant estimate is not a uniform multiplier-tail bound.

## Prior-art audit

The phase-separation step is classical harmonic-analysis structure. The **Encyclopedia of Mathematics**, entry **Almost-periodic function**, records generalized trigonometric polynomials `sum a_k exp(i lambda_k x)` as the basic finite objects of almost-periodic theory and cites the classical treatments of H. Bohr, A. S. Besicovitch and W. Rudin. The long-interval mean-square orthogonality used here is the elementary finite-sum uniqueness mechanism behind the argument.

The within-fiber moment cancellation is the same classical extrapolation/Vandermonde structure already bounded in `VIS-343`, where Avram Sidi, **The Richardson Extrapolation Process with a Harmonic Sequence of Collocation Points**, *SIAM Journal on Numerical Analysis* 37:5 (2000), 1729-1746, DOI `10.1137/S0036142998340137`, is the explicit prior-art anchor for cancellation of asymptotic powers by linear combinations.

No novelty is claimed for exponential-polynomial uniqueness, Bohr almost periodicity, Richardson extrapolation, or Vandermonde moment cancellation. The Mathia-specific contribution is only the exact specialization showing that real translations of Wang's rational multiplier cannot cooperate across phase fibers to improve **uniform** polynomial tail order.

## Dependencies

- `VIS-333`: exact Wang multiplier `m(xi)`.
- `VIS-342`: fixed power-class gain in the scalar Vinogradov-Korobov model requires polynomial effective-order growth.
- `VIS-343`: pure-dilation moment-cancellation ceiling and its Vandermonde proof.
- `CLUE-wang-fixed-source-packet-localization`: accepted source-localization clue whose translated/phase-sensitive escape is narrowed here.

## Research consequence

The translated-packet branch splits cleanly. **Translations do not create a new uniform tail-smoothing resource: the asymptotic cancellation equations decouple by translation frequency, and every active phase fiber must pay the full Vandermonde scale cost independently.**

A surviving non-scalar Wang mechanism must therefore use something more specific than fixed translated copies with constant weights. The remaining live possibilities are finite-window or scale-migrating localization, genuinely frequency-dependent/adaptive coefficients, or signed arithmetic information in `G` whose estimate is not equivalent to uniform multiplier-tail cancellation. Those possibilities require a different decisive test rather than another extension of the scalar moment-cancellation argument.