# PL-050 — The naturally rescaled localized-Weil prime operator vanishes strongly while its spectral edges stay macroscopic

## Claim

The compact-window Weil branch now has a sharp large-window separation between **bulk operator convergence** and **escaping boundary spectrum**.

On

```text
H_L = L^2(-L,L)
```

let

```text
K_L
 = sum_(log n<2L) Lambda(n)/sqrt(n)
     (T_(log n)+T_(log n)^*)
```

be the non-archimedean compressed-translation operator from `PL-046` and `PL-049`, where `T_u` is translation by `u` compressed to the window. Let

```text
U_L : H_L -> H=L^2(-1,1),
(U_L f)(y)=sqrt(L) f(Ly),
```

and put the naturally norm-scaled operator

```text
A_L = exp(-L) U_L K_L U_L^*.
```

Then

```text
boxed: A_L -> 0 strongly on L^2(-1,1).
```

However the spectral edges do **not** collapse:

```text
boxed:
liminf_(L->infinity) sup sigma(A_L) >= 1,
liminf_(L->infinity) (-inf sigma(A_L)) >= 1.
```

In particular,

```text
liminf_(L->infinity) ||A_L|| >= 1,
```

so the convergence is not in operator norm. The lower bound strengthens the explicit constant in `PL-049`; more importantly, the positive and negative edges are both carried by normalized states that concentrate in `O(1)` physical boundary layers near `-L` and `+L`, hence in `O(1/L)` layers after the global dilation to `(-1,1)`.

Thus the route

```text
normalize K_L by its natural exp(L) scale
+ dilate the growing Weil window to a fixed interval
    -> nontrivial bulk strong/operator limit
    -> limiting arithmetic spectrum or determinant
```

fails already for the isolated prime operator. At this normalization the bulk strong limit is zero, while order-one spectral edges escape into moving endpoint states.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION`, and `DECISIVE-NEGATIVE` for the specific bulk-limit route above. The derivation uses only the exact compressed-shift representation and the prime number theorem. No claim is made about the full localized Weil operator after adding its archimedean and pole terms, nor about a boundary-blow-up limit adapted to the escaping states.

## Fixed-space form of the prime operator

Under `U_L`, translation by a physical lag `u` becomes the compressed shift by

```text
r=u/L
```

on `H=L^2(-1,1)`. Write this fixed-window shift as `S_r`. Then

```text
A_L
 = exp(-L)
   sum_(log n<2L) Lambda(n)/sqrt(n)
      (S_(log n/L)+S_(log n/L)^*).
```

The PNT weighted counting function used in `PL-046` and `PL-049` is

```text
S(x)=sum_(n<x) Lambda(n)/sqrt(n)
    =(2+o(1)) sqrt(x).
```

This immediately shows why `exp(L)` is the correct global normalization: the total coefficient mass below `exp(2L)` is asymptotic to `2 exp(L)`, while `PL-046` gives the sharper support-aware bound

```text
||A_L|| <= 2+o(1).
```

The question is therefore not one of unbounded growth after normalization, but of where the surviving norm lives.

## Strong convergence to zero

Fix `R>0` and split the sum into

```text
interior lags:  log n <= 2L-R,
outer lags:     2L-R < log n < 2L.
```

### Interior lags vanish uniformly when `R` is large

Using only `||S_r||<=1`,

```text
||A_L^(int)||
 <= 2 exp(-L)
    sum_(log n<=2L-R) Lambda(n)/sqrt(n).
```

By the PNT asymptotic,

```text
limsup_(L->infinity) ||A_L^(int)||
 <= 4 exp(-R/2).
```

So every lag that remains a fixed physical distance `R` away from the diameter `2L` becomes negligible after the `exp(-L)` normalization, uniformly in operator norm as `R->infinity`.

### Outer lags act only on shrinking endpoint strips

If

```text
2L-R < u < 2L,
```

then

```text
2-R/L < u/L < 2.
```

The compressed shift `S_(u/L)` can only take input from the right endpoint strip

```text
(1-R/L,1)
```

and place it in the left endpoint strip; its adjoint does the reverse. Hence for every fixed `f in L^2(-1,1)`,

```text
||S_(u/L) f||
 <= ||1_(1-R/L,1) f||,

||S_(u/L)^* f||
 <= ||1_(-1,-1+R/L) f||.
```

The normalized total outer coefficient mass is uniformly bounded because

```text
exp(-L)
 sum_(log n<2L) Lambda(n)/sqrt(n)
 = 2+o(1).
```

Therefore

```text
||A_L^(out) f||
 <= (2+o(1))
    [ ||1_(1-R/L,1) f||
      + ||1_(-1,-1+R/L) f|| ].
```

For fixed `R` the two endpoint-strip norms tend to zero as `L->infinity`, by absolute continuity of the `L^2` integral.

Combining the two pieces gives

```text
limsup_(L->infinity) ||A_L f||
 <= 4 exp(-R/2) ||f||.
```

Since `R` is arbitrary,

```text
A_L f -> 0
```

for every fixed `f in H`. This proves strong convergence.

The proof is deliberately insensitive to fine prime correlations: after global dilation, coefficient mass of order `exp(L)` is forced into lags whose normalized length tends to the full diameter `2`, and those shifts disappear on every fixed bulk vector because their domains collapse to the endpoints.

## Boundary states retain both spectral edges

Strong convergence does not control vectors that themselves depend on `L`. Such moving vectors give a sharper version of the endpoint mechanism in `PL-049`.

Fix `R>0` and define the normalized half-line profile

```text
g_R(a)
 = exp(-a/2) / sqrt(1-exp(-R)),
0<=a<=R,
```

and `g_R(a)=0` otherwise. It has `L^2(0,infinity)` norm one.

For `L>R`, place copies of this profile at the two ends of the physical window:

```text
g_(L,-)(-L+a)=g_R(a),

g_(L,+)(L-a)=g_R(a),
```

and set

```text
v_(L,R)^+ = (g_(L,-)+g_(L,+))/sqrt(2),
v_(L,R)^- = (g_(L,-)-g_(L,+))/sqrt(2).
```

Both are unit vectors. For an outer lag

```text
u=2L-delta,
0<delta<2R,
```

the only overlap is between opposite endpoint layers, and

```text
<v_(L,R)^+, T_u v_(L,R)^+>
 = +(1/2) (g_R*g_R)(delta),

<v_(L,R)^-, T_u v_(L,R)^->
 = -(1/2) (g_R*g_R)(delta).
```

Lags `R<=u<=2L-2R` give no overlap. Lags `0<u<R` contribute only same-end overlaps; since `R` is fixed, their total contribution is `O_R(1)` and disappears after multiplication by `exp(-L)`.

For every fixed compactly supported continuous test function `phi(delta)`, the fixed-width PNT rescaling from `PL-049` gives

```text
exp(-L)
 sum_(2L-2R<log n<2L)
   Lambda(n)/sqrt(n)
   phi(2L-log n)

 -> integral_0^(2R)
      phi(delta) exp(-delta/2) d delta.
```

Taking

```text
phi=g_R*g_R
```

and using Fubini,

```text
integral_0^(2R)
  (g_R*g_R)(delta) exp(-delta/2) d delta

 = [ integral_0^R g_R(a) exp(-a/2) da ]^2
 = 1-exp(-R).
```

Consequently,

```text
lim_(L->infinity)
 exp(-L)<K_L v_(L,R)^+,v_(L,R)^+>
 = +(1-exp(-R)),

lim_(L->infinity)
 exp(-L)<K_L v_(L,R)^-,v_(L,R)^->
 = -(1-exp(-R)).
```

For the minus state the fixed small-lag same-end contribution changes the numerator only by `O_R(1)`, so it does not affect the displayed normalized limit.

By the variational characterization of the spectral edges of a bounded self-adjoint operator,

```text
liminf sup sigma(A_L) >= 1-exp(-R),
liminf (-inf sigma(A_L)) >= 1-exp(-R).
```

Letting `R->infinity` proves

```text
liminf sup sigma(A_L) >= 1,
liminf (-inf sigma(A_L)) >= 1.
```

This also strengthens the earlier block-indicator lower bound in `PL-049`, where the explicit constant was

```text
2(1-exp(-1))^2 ~= 0.79915.
```

The improvement is not an optimization of the old block width; it comes from choosing the boundary profile matched to the PNT shell density `exp(-delta/2)`.

## The escaping states disappear from every fixed bulk probe

Under the global dilation `U_L`, the vectors `v_(L,R)^+/-` remain normalized but are supported in endpoint strips of width `R/L`. Hence

```text
U_L v_(L,R)^+/- -> 0 weakly
```

for each fixed `R`: their scalar product with every fixed `L^2(-1,1)` vector is bounded by that vector's `L^2` mass in shrinking endpoint strips.

Thus the two statements

```text
A_L -> 0 strongly
```

and

```text
spectral edges of A_L stay at distance >=1 from 0
```

are not contradictory. The edge states escape from every fixed bulk probe as the window grows.

Because `||A_L||` is uniformly bounded, strong convergence also implies that for every fixed vector and every fixed positive integer `k`,

```text
A_L^k f -> 0.
```

So fixed-state polynomial spectral moments collapse to those of the zero operator even while moving endpoint states retain macroscopic spectral values. Any limiting construction that samples only fixed bulk vectors after the global dilation will therefore erase precisely the part of the prime operator responsible for its natural `exp(L)` norm scale.

## Exponent-lattice interpretation

The mechanism uses the outer energy shell

```text
2L-O(1)
 < <v(n),(log p)_p>
 < 2L.
```

Since the completed Weil prime term is supported on `Lambda(n)`, the active lattice points are still only the prime-power rays

```text
v(n)=m e_p.
```

The PNT puts normalized weight density

```text
exp(-delta/2) d delta,
delta=2L-log n,
```

in a fixed-width outer shell. Geometrically, those almost-diameter translations couple only the two physical endpoints of the Paley--Wiener window. Global rescaling compresses that interaction into sets of vanishing measure; endpoint-adapted vectors retain it.

This is therefore a concrete example of information loss under a natural geometric quotient:

```text
prime-power energy shell
    -> near-diameter compressed translations
    -> O(1) physical endpoint layer
    -> O(1/L) layer after global dilation
    -> invisible to fixed bulk states,
       but still visible in operator norm/spectral edges.
```

It is not evidence that the escaping layer contains Riemann-zero information. The construction uses only positive von-Mangoldt shell mass and not the zero divisor.

## Beurling and universality audit

The strong-zero proof requires only a weighted counting law of the form

```text
sum_(omega_j<=X) a_j
 ~ C exp(X/2)
```

for positive lags `omega_j`, after the logarithmic normalization used here. The boundary-state edge lower bound similarly uses convergence of fixed-width outer-shell measures to a positive density.

Accordingly, matched generalized-frequency or Beurling systems with the same weighted square-root counting law exhibit the same qualitative phenomenon:

```text
global strong limit zero
+ nonvanishing endpoint spectral edges.
```

Neither unique factorization, prime-log rational independence, the zeta functional equation, nor the Riemann zero divisor enters the proof. The result is therefore a **large-window obstruction/universality statement**, not arithmetic rigidity.

## Analytic-continuation boundary

No Euler product is used or continued into the critical strip. For every fixed `L`, `K_L` is the finite non-archimedean term extracted from the already-completed Weil explicit formula. The only asymptotic input is the prime number theorem in the weighted form

```text
sum_(n<x) Lambda(n)/sqrt(n)
 = (2+o(1))sqrt(x).
```

The result therefore lives entirely on the continued/completed explicit-formula side.

## Prior-art and novelty audit

The underlying ingredients are classical or already anchored in this line:

- `PL-046` identifies `K_L` and proves the support-aware upper scale `||K_L||<=(2+o(1))exp(L)` using the classical Boas--Kac/Caratheodory--Fejer theorem.
- `PL-049` gives the first endpoint Rayleigh lower bound `||K_L||>=c exp(L)` from fixed-width von-Mangoldt shell mass.
- Marcus Chuk, arXiv:`2608.24827` (25 August 2026), studies the distinct pointwise prime-comb barrier and notes that order-space truncations retain prime-shift coupling; his theorem does not provide the strong-limit/boundary-escape statement above.
- The weighted shell asymptotics used here are standard consequences of the prime number theorem.

A targeted search across localized Weil operators, compressed/truncated translations, finite-section/strong-limit language, and endpoint Rayleigh constructions did not locate this exact rescaled statement. Generic finite-section and boundary-effect phenomena are standard operator theory, so that search absence is **not** treated as evidence of novelty. The durable content is the explicit audited consequence for the concrete Weil prime operator and its implications for this research line.

## Falsification and boundary tests

The claim reduces to independently checkable steps:

1. after dilation, a lag `u>2L-R` acts only through endpoint strips of width `R/L`;
2. the normalized coefficient mass below `2L-R` is `O(exp(-R/2))`;
3. fixed-vector `L^2` mass in endpoint strips of width `R/L` tends to zero;
4. the fixed-width PNT shell measure converges to `exp(-delta/2)d delta`;
5. the matched endpoint profile satisfies

```text
[ integral g_R(a) exp(-a/2) da ]^2
 = 1-exp(-R).
```

Items 1, 3, and 5 are elementary. Items 2 and 4 follow from the PNT by partial summation, exactly as in `PL-049`.

The conclusion would need revision if the normalization, the global dilation, or the operator itself is changed. In particular, it does **not** rule out:

```text
- a separate boundary blow-up retaining O(1) distance from +/-L;
- an arithmetic limit of the full Weil operator including archimedean terms;
- threshold-by-threshold spectral-flow identities;
- a determinant or trace built after subtracting a universal boundary layer;
- finer prime-specific information in spectral values below the coarse exp(L) edge scale.
```

## Consequence for the research line

The large-window ledger is now sharper:

```text
pointwise prime comb
    -> recurrent amplitude ~4 exp(L)                     [PL-045]

support-aware aggregate bound
    -> ||K_L|| <= (2+o(1)) exp(L)                       [PL-046]

endpoint shell
    -> ||K_L|| = Theta(exp(L))                          [PL-049]

natural global rescaling
    -> exp(-L) U_L K_L U_L^* -> 0 strongly
    -> yet both spectral edges have liminf magnitude >=1 [PL-050]
```

So a naive fixed-interval large-`L` limit of the isolated non-archimedean operator loses its macroscopic spectrum. The next viable compact-Weil mechanism must either keep the moving endpoint layer in view, couple it nontrivially to the archimedean/pole operator, renormalize/subtract a universal boundary contribution, or use a genuinely arithmetic cross-threshold observable. Merely exhibiting bounded normalized operators and taking a bulk strong limit cannot retain the prime information responsible for the natural spectral scale.