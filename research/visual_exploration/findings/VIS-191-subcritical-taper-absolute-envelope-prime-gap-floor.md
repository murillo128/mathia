# VIS-191 — subcritical smooth-taper absolute envelope has a consecutive-prime floor

## Claim

Keep the notation of `VIS-190`. Fix `0 <= alpha < 1/2`, put

`a_p=p^(-alpha)`, `Q_y=sum_(p<=y) a_p^2`, `beta=1-2alpha>0`,

and let `v in C^2([0,1])` satisfy

`v(0)=v(1)=0`, `V=int_0^1 v(u) du != 0`.

Write

`K^v_(H,T)(p,q)=(H V)^(-1) int_T^(T+H) v((t-T)/H) exp(it log(q/p)) dt`

and

`O_v(y;H,T)=Q_y^(-1) sum_(p<q<=y) a_p a_q |K^v_(H,T)(p,q)|`.

If `H=H(y)>=1` satisfies

`H log y / y -> 0`,

then

`liminf_(y->infinity) O_v(y;H,T) >= beta/2`,

uniformly in `T` (indeed `O_v` is independent of `T`).

Consequently the absolute-envelope mechanism of `VIS-190` cannot prove quadratic diagonalization below the scale `y/log y`: its sufficient condition `H >> y/log y` is order-sharp as a threshold for **absolute** off-diagonal disappearance.

This does **not** show that the signed tapered mean square `M_v(y;H,T)` fails to diagonalize when `H=o(y/log y)`. The remaining off-diagonal terms may cancel. The result pins only the absolute-value method boundary.

**Evidence/status:** `EXACT-DERIVED + PRIME-NUMBER-THEOREM INPUT + NEGATIVE/METHOD-BOUNDARY + NO-NOVELTY-CLAIM`.

## 1. The absolute kernel forgets the interval start

After the change of variables `t=T+Hu`,

`K^v_(H,T)(p,q)`
` = exp(iT log(q/p)) kappa_v(H log(q/p))`,

where

`kappa_v(theta)=V^(-1) int_0^1 v(u) exp(i theta u) du`.

Therefore

`|K^v_(H,T)(p,q)|=|kappa_v(H log(q/p))|`

is independent of `T`. Since `kappa_v(0)=1` and `v` is integrable, continuity gives

`|kappa_v(theta)| -> 1`

as `theta->0`.

The lower bound below therefore needs no sign condition on the taper and no phase choice for `T`.

## 2. A positive proportion of top-half consecutive prime gaps is `O(log y)`

Let

`p_1 < ... < p_m`

be the primes in `(y/2,y]`. The prime number theorem gives

`m=pi(y)-pi(y/2)=(1/2+o(1)) y/log y`.

For the internal consecutive gaps

`g_j=p_(j+1)-p_j`, `1<=j<m`,

one has the deterministic telescoping bound

`sum_(j<m) g_j=p_m-p_1 <= y/2`.

Fix any constant `A>1`. If `N_large(A)` counts gaps with

`g_j>A log y`,

then

`N_large(A) A log y <= y/2`,

so

`N_large(A) <= y/(2A log y)`.

Hence the number `N_small(A)` of internal consecutive prime pairs with

`q-p <= A log y`

satisfies

`N_small(A) >= [(1/2)(1-1/A)+o(1)] y/log y`.

No bounded-gap theorem or Hardy--Littlewood prime-pair asymptotic is used. This is only the prime number theorem plus telescoping of consecutive gaps.

## 3. Every such pair is unresolved when `H=o(y/log y)`

For a selected pair `y/2<p<q<=y`,

`0<log(q/p)=log(1+(q-p)/p) <= (q-p)/p <= 2A log y/y`.

Therefore

`0 <= H log(q/p) <= 2A H log y/y -> 0`.

For fixed `A`, continuity of `kappa_v` at zero now yields uniformly over all selected pairs

`|K^v_(H,T)(p,q)|=1-o(1)`.

Thus these ordinary consecutive-prime pairs alone remain completely unresolved by the smooth observation kernel at every strictly subcritical scale.

## 4. Their normalized absolute mass is already order one

Because `0<=alpha<1/2` and `p,q<=y`,

`a_p a_q=(pq)^(-alpha) >= y^(-2alpha)`.

Restricting the nonnegative sum defining `O_v` to the selected consecutive pairs gives

`O_v(y;H,T)`
` >= Q_y^(-1) N_small(A) y^(-2alpha) [1-o(1)]`.

The prime number theorem and partial summation give

`Q_y ~ y^beta/(beta log y)`.

Consequently, for every fixed `A>1`,

`liminf O_v(y;H,T) >= (beta/2)(1-1/A)`.

Since this holds for every fixed `A`, letting `A` increase after taking the lower limit gives

`liminf O_v(y;H,T) >= beta/2`.

The constant is not asserted to be the true limiting absolute mass; it is only a universal floor contributed by top-half consecutive primes.

A fixed-constant version follows as well. By continuity there is `delta_v>0` such that `|kappa_v(theta)|>=1/2` for `|theta|<=delta_v`. Taking, for example, `A=2`, every sufficiently large `y` with

`H <= delta_v y/(4 log y)`

has

`O_v(y;H,T) >= beta/8+o(1)`.

Thus the failure of absolute disappearance already persists throughout a nontrivial constant-width corridor at the critical scale.

## 5. Relation to `VIS-190`

`VIS-190` proves

`O_v(y;H,T) << y/(H log y)`

for `1<=H<=y`, and hence `O_v->0` whenever `H log y/y->infinity`. The present lower bound supplies the opposite asymptotic side:

- above `y/log y` by a diverging factor, the absolute envelope vanishes;
- below `y/log y` by a vanishing factor, the absolute envelope stays bounded away from zero.

So `y/log y` is not merely an artifact of the upper-bound proof. It is the genuine Fourier-resolution scale at which a positive-density population of ordinary consecutive prime gaps moves between unresolved and potentially resolved status for this absolute envelope.

The exact constant-scale transition remains open because `kappa_v(theta)` is sampled at order-one frequencies and the distribution of normalized prime gaps then matters. More importantly, none of this settles the **signed** off-diagonal: cancellation among pair phases can still make `M_v-1` small even while `O_v` is order one.

## 6. Prior art and novelty boundary

The inputs are classical. The prime number theorem gives the top-half prime count and, equivalently, logarithmic average prime-gap scale. The observation that many consecutive gaps cannot all exceed a fixed multiple of that average is the elementary telescoping/Markov consequence used above. Stronger small-gap results such as GPY/Maynard--Tao/Zhang are unnecessary.

Smoothly weighted Dirichlet-polynomial mean squares and Fourier localization are classical, as already audited in `VIS-179`, `VIS-188`, `VIS-189`, and `VIS-190`. No novelty is claimed for the prime number theorem, average prime gaps, taper Fourier transforms, or mean-value machinery.

The Mathia-specific content is only the exact interaction of these classical facts with the particular absolute envelope introduced in `VIS-189`/`VIS-190`: the unresolved consecutive-prime population supplies an order-one normalized floor throughout `H=o(y/log y)`, proving that the previous sufficient observation scale is asymptotically sharp for this absolute-value strategy.

## Boundaries and falsification

The exponent `alpha` and taper `v` are fixed as `y` grows. The argument uses only `kappa_v(0)=1` and continuity for the lower bound; the endpoint-zero `C^2` assumptions are retained to remain in the exact observation class of `VIS-190`.

The conclusion is about `O_v`, not directly about `M_v`. It must not be cited as evidence for surviving signed prime-pair correlation, an RH-sensitive signal, or failure of quadratic mean-square diagonalization below the threshold.

Falsify the finding by locating an error in the top-half prime count, the telescoping bound on internal consecutive gaps, the frequency estimate `H log(q/p)=o(1)`, the kernel continuity step, the weight lower bound, or the asymptotic `Q_y ~ y^beta/(beta log y)`.

## Research consequence

The absolute-envelope branch is now asymptotically bracketed at the same scale from both sides. Repeating stronger absolute prime-pair estimates cannot by itself make the full envelope vanish in the subcritical regime, because a positive-density set of ordinary consecutive primes has kernel weight tending to one there.

The next genuinely different question is therefore the one left open by `VIS-190`: whether **signed cancellation** inside the kernel-unresolved short-gap population can force `M_v-1 -> 0` at or below `H~y/log y`, or whether another observable is required. That is a separate coherent investigation.