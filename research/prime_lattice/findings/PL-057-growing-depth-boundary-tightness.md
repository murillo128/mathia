# PL-057 — Growing Weil boundary depth is exponentially tight and preserves the strong/Calkin split

## Claim

The growing-depth escape left open by `PL-051`--`PL-056` does not produce a new order-one mesoscopic boundary operator merely by taking `R=R(L)->infinity` while keeping the natural `exp(-L)` normalization and the raw localized Weil boundary family.

Let

```text
B_(L,R)
 = exp(-L) J_(L,R)^* K_L J_(L,R)
```

be the two-end boundary operator of `PL-051` on

```text
H_R direct_sum H_R,
H_R=L^2(0,R),
```

for `0<R<=L`. Embed every `H_R` by zero extension into

```text
H_infinity=L^2(0,infinity)
```

and write `Btilde_(L,R)` for the resulting operator on `H_infinity direct_sum H_infinity`.

Define

```text
h_infinity(a)=exp(-a/2),
P_infinity=|h_infinity><h_infinity|,

B_infinity
 = [ 0           P_infinity ]
   [ P_infinity  0          ].
```

Since `||h_infinity||_2^2=1`, the only nonzero eigenvalues of `B_infinity` are `+1` and `-1`.

Then for every sequence

```text
R_L -> infinity,
0<R_L<=L,
```

one has

```text
boxed:
Btilde_(L,R_L) -> B_infinity strongly,
```

but simultaneously

```text
boxed:
liminf_(L->infinity)
 ||Btilde_(L,R_L)-B_infinity||_ess >= 1.
```

In particular,

```text
liminf_(L->infinity)
 ||Btilde_(L,R_L)-B_infinity|| >= 1,
```

so the growing-depth family cannot converge in operator norm to any operator. The centered residual converges strongly to zero while retaining an order-one Calkin defect.

The mechanism is an exponential depth-tightness estimate. For every fixed `D>0` and every `D<R<=L`,

```text
boxed:
||Btilde_(L,R)-Btilde_(L,D)||
 <= C exp(-D/2)+C exp(-L/2),
```

with an absolute constant `C` independent of `D,R,L` in the displayed range. Thus all order-one mass of the naturally normalized boundary operator is already confined to an `O(1)` deficit layer; merely opening a deeper boundary window exposes only an exponentially small operator tail.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION`, and `DECISIVE-NEGATIVE` for the route

```text
natural exp(-L) normalization
+ raw boundary blow-up with R(L)->infinity
    -> new order-one mesoscopic limit or compact/Schatten residual.
```

The result is deliberately scoped. It does **not** rule out a moving boundary-frequency cutoff, an `L`-dependent smoothing order, a renormalization that explicitly amplifies the exponentially small depth tail, joint spatial/frequency scaling, or coupling to the archimedean and pole terms. Those are genuinely different moving topologies and remain within `CLUE-mesoscopic-weil-boundary-topology`.

## Common half-line realization and nested compressions

For `D<R`, zero extension gives canonical inclusions

```text
H_D subset H_R subset H_infinity.
```

Let `P_D` denote the orthogonal projection of the two-copy half-line space onto `H_D direct_sum H_D`. The endpoint embeddings in `PL-051` are nested, hence their compressed operators satisfy the exact identity

```text
boxed:
P_D Btilde_(L,R) P_D
 = Btilde_(L,D).
```

The fixed-depth PNT limit of `PL-051`, embedded in the same half-line space, is

```text
B_D
 = [ 0    P_D^0 ]
   [ P_D^0  0   ],

P_D^0=|h_D><h_D|,
h_D=1_(0,D) h_infinity.
```

Moreover

```text
||h_infinity-h_D||_2=exp(-D/2),
```

so the rank-one inequality

```text
|| |u><u|-|v><v| ||
 <= (||u||+||v||)||u-v||
```

gives

```text
boxed:
||B_D-B_infinity||=O(exp(-D/2)).
```

Thus the fixed-depth universal limits themselves converge in norm to the rank-two half-line model.

## A coarse weighted Chebyshev bound controls every deeper shell

Write

```text
W(x)=sum_(n<=x) Lambda(n)/sqrt(n).
```

The classical Chebyshev bound

```text
psi(x)=sum_(n<=x) Lambda(n)=O(x)
```

and partial summation give

```text
W(x)
 = psi(x)/sqrt(x)
   + (1/2) integral_1^x psi(t)t^(-3/2)dt
 = O(sqrt(x)).
```

Only this coarse estimate is needed below; no zero-free region, RH-strength estimate, or explicit-formula cancellation enters.

Recall the endpoint decomposition of `PL-051`. At depth `R`, a lag `u=log n` either acts within one endpoint strip when `u<R`, or bridges the two endpoint strips through the deficit

```text
delta=2L-u.
```

Every individual compressed translation/reflection has operator norm at most `1`, and its coefficient in the normalized operator is `exp(-L)Lambda(n)/sqrt(n)` up to the fixed two-end multiplicity.

## Uniform exponential depth-tail estimate

Fix `D<R<=L`. There are only two ways in which `Btilde_(L,R)` can differ from the zero-extended `Btilde_(L,D)`.

First, the larger strip admits additional same-end pieces. Their total normalized operator norm is bounded by

```text
C exp(-L)
  sum_(log n<R) Lambda(n)/sqrt(n)

 <= C exp(-L) W(exp(R))
 <= C exp(-L+R/2)
 <= C exp(-L/2),
```

because `R<=L`.

Second, a cross-end piece can touch the region outside depth `D` only if at least one inward coordinate exceeds `D`. Since the cross-end geometry is

```text
delta=a+b,
```

this implies `delta>D`, hence

```text
log n=2L-delta<2L-D.
```

Discarding the lower shell restriction only enlarges the positive coefficient sum, so all such cross-end pieces have total norm at most

```text
C exp(-L) W(exp(2L-D))
 <= C exp(-D/2).
```

Combining the two contributions yields

```text
boxed:
||Btilde_(L,R)-Btilde_(L,D)||
 <= C exp(-D/2)+C exp(-L/2).
```

The estimate is uniform in the moving depth `R` all the way up to the geometric maximum `R=L`.

This is stronger than the fixed-depth PNT statement in one specific direction: after the natural normalization, increasing the spatial boundary depth cannot uncover a second order-one layer. The tail beyond depth `D` is exponentially tight before any limiting argument is taken.

## Every growing depth has the same strong half-line limit

Let `R_L->infinity` with `R_L<=L`. Fix a vector `F` in `H_infinity direct_sum H_infinity` and a fixed depth `D`. For all sufficiently large `L`, `R_L>D`, and

```text
||(Btilde_(L,R_L)-B_infinity)F||

 <= ||Btilde_(L,R_L)-Btilde_(L,D)|| ||F||
    +||(Btilde_(L,D)-B_D)F||
    +||B_D-B_infinity|| ||F||.
```

For fixed `D`, `PL-051` gives

```text
Btilde_(L,D) -> B_D strongly.
```

Taking `limsup` in `L` and using the depth-tail estimate gives

```text
limsup_(L->infinity)
||(Btilde_(L,R_L)-B_infinity)F||
 <= C exp(-D/2)||F||.
```

Now let `D->infinity`. Therefore

```text
boxed:
Btilde_(L,R_L) -> B_infinity strongly.
```

The first-order PNT boundary model is consequently stable under arbitrary decompactification of the raw boundary depth permitted by the original window.

## The essential recurrence defect survives every growing depth

Strong convergence does not improve the Calkin behavior. Fix `D`. For all sufficiently large `L`, `R_L>D`, and the nested-compression identity gives

```text
P_D
 (Btilde_(L,R_L)-B_infinity)
 P_D

 = Btilde_(L,D)-B_D.
```

Compression cannot increase essential norm. Hence

```text
||Btilde_(L,R_L)-B_infinity||_ess
 >= ||Btilde_(L,D)-B_D||_ess.
```

`PL-053` proved at every fixed depth that

```text
liminf_(L->infinity)
 ||Btilde_(L,D)-B_D||_ess
 >= 1-exp(-D).
```

Therefore, for every fixed `D`,

```text
liminf_(L->infinity)
 ||Btilde_(L,R_L)-B_infinity||_ess
 >= 1-exp(-D).
```

Letting `D->infinity` yields

```text
boxed:
liminf_(L->infinity)
 ||Btilde_(L,R_L)-B_infinity||_ess >= 1.
```

Thus the same high-frequency prime-log recurrence that obstructs norm and Calkin convergence at fixed depth remains embedded isometrically inside every sufficiently deep moving window. Spatial decompactification does not dilute it.

Since operator norm dominates essential norm, no norm convergence to `B_infinity` is possible. Strong convergence already identifies the only possible norm limit, so the family cannot converge in norm to any other operator either.

The centered residual

```text
Btilde_(L,R_L)-B_infinity
```

therefore has the exact qualitative split

```text
strong topology:     -> 0,
Calkin/operator norm: stays order one.
```

This is the same split as at fixed depth, now uniformly propagated to every raw growing-depth regime.

## Exponent-lattice interpretation

The cross-end shell consists of prime-power axis points

```text
v(n)=k e_p
```

with energy deficit

```text
delta=2L-<v(n),(log p)_p>.
```

The weighted Chebyshev estimate shows that, after multiplying by `exp(-L)`, the total operator weight of all axis points with deficit larger than `D` is `O(exp(-D/2))`. Thus the natural boundary normalization imposes an exponential tightness in the scalar energy-deficit coordinate:

```text
all deficits
    -> O(1) layer delta=O(1)
    -> universal PNT rank-one strong limit.
```

But inside each fixed deficit layer, the exact primitive frequencies `log p` remain available to high-frequency boundary states. Kronecker recurrence therefore survives every growing spatial window in the essential norm.

The two effects are compatible because they live in different directions: increasing `R` explores farther in the **deficit coordinate**, while the obstruction of `PL-052`--`PL-053` escapes in the **dual boundary-frequency coordinate**. Growing only the first coordinate cannot regularize or stabilize the second.

## Beurling and matched-control audit

The depth-tail estimate uses only a positive weighted counting bound of the form

```text
sum_(omega_j<=X) a_j exp(-omega_j/2)
 = O(exp(X/2)),
```

while the strong fixed-depth model uses the PNT-type shell law from `PL-051` and the essential lower bound uses the finite rational-independence recurrence mechanism from `PL-053`.

A generalized-prime or positive-frequency system satisfying matched analogues of these three inputs has the same growing-depth behavior: exponential spatial tightness, the same continuum strong limit, and a recurrent Calkin defect. Consequently the result is an obstruction, not zeta-specific rigidity, and it does not distinguish the ordinary primes from suitably matched Beurling controls.

## Analytic-continuation boundary

No Euler product or Dirichlet series is analytically continued in this argument. Every finite-`L` operator is the finite von-Mangoldt prime-power component already extracted from the completed Weil explicit formula. The only additional number-theoretic input beyond `PL-051`--`PL-053` is the elementary Chebyshev bound `psi(x)=O(x)`.

The no-go therefore lies entirely on the completed explicit-formula/operator side. It cannot be attributed to remaining in `Re(s)>1`.

## Prior-art and novelty audit

The ingredients are classical or already persisted:

- `PL-051` supplies the exact endpoint decomposition and fixed-depth strong PNT limit;
- `PL-052`--`PL-053` supply the prime-log recurrence and fixed-depth norm/Calkin lower bounds;
- `psi(x)=O(x)` is the classical Chebyshev upper bound, and the estimate for `W(x)` is elementary partial summation;
- zero extension, nested compression, rank-one norm estimates, and monotonicity of essential norm under compression are standard operator theory.

A targeted check of uniform weighted prime-number estimates, moving-window prime sums, and Hankel/convolution operator limits found much stronger modern PNT technology but no theorem needed beyond the elementary bound above. No novelty is claimed for any ingredient or for generic tightness/compactness principles. The durable content is the exact specialization to the stored Weil boundary family and the resulting closure of the raw `R(L)->infinity` escape explicitly left open by `PL-051`, `PL-055`, and `PL-056`.

Search absence is not used as evidence of novelty.

## Falsification and boundary tests

The claim reduces to the following independently checkable statements:

1. the boundary realizations are nested and fixed-depth compression of depth `R` equals the depth-`D` operator;
2. `W(x)=O(sqrt(x))` follows from `psi(x)=O(x)` by partial summation;
3. same-end contributions gained between depths `D` and `R<=L` are `O(exp(-L/2))` after normalization;
4. every cross-end matrix element touching depth larger than `D` has deficit `delta>D`, so its total positive coefficient mass is `O(exp(-D/2))`;
5. the embedded fixed-depth PNT limits converge in norm to `B_infinity`;
6. fixed-depth strong convergence plus the uniform tail estimate implies strong convergence for every `R_L->infinity`;
7. compression of the growing-depth centered residual recovers the fixed-depth residual, so `PL-053` gives the essential lower bound `1-exp(-D)` for every `D`.

Failure of any item falsifies the corresponding conclusion. The theorem ceases to apply if one multiplies the depth tail by an `L`-dependent amplification, changes the natural normalization, or inserts an `L`-dependent frequency/smoothing operator; those are precisely the surviving moving-topology questions rather than hidden assumptions.

## Consequence for the research line

The localized Weil boundary ledger is now

```text
fixed depth
    -> universal rank-one PNT strong limit                 [PL-051]
    -> order-one norm/Calkin recurrence defect             [PL-052, PL-053]

fixed compact smoothing
    -> recurrence suppressed
    -> universal norm/Schatten determinant limit           [PL-055, PL-056]

growing raw depth R(L)->infinity
    -> exponentially tight in spatial deficit
    -> same half-line rank-two PNT strong limit
    -> same order-one Calkin recurrence defect              [PL-057]
```

So **spatial decompactification alone is not the missing mesoscopic topology**. Any surviving construction must also move in the dual boundary-frequency/regularity direction or explicitly renormalize the exponentially small depth tail. That substantially narrows `CLUE-mesoscopic-weil-boundary-topology` without resolving it.