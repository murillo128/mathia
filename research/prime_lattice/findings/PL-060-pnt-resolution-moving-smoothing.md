# PL-060 — Quantitative PNT resolution forces an expanding low-frequency collapse of the centered Weil boundary residual

## Claim

The moving-frequency escape left open by `PL-055`--`PL-059` already has a quantitative no-go regime. The point is stronger than fixed compact smoothing: an **expanding** boundary-frequency window can still see only the PNT continuum model, provided its resolution grows more slowly than the quantitative PNT remainder allows.

Fix `R>0`. Write

```text
X_L=exp(2L),
psi(x)=sum_(n<=x) Lambda(n),

r_(L,R)
 = sup_(X_L exp(-2R) <= x <= X_L)
     |psi(x)-x|/x.
```

The prime number theorem gives

```text
r_(L,R) -> 0.
```

Let `B_(L,R)` be the naturally normalized fixed-depth prime boundary operator from `PL-051`, let `B_R` be its rank-one PNT limit, and let `E_(L,R)` be the pole operator from `PL-059`. Thus the canonically centered bounded completed sector is

```text
C_(L,R)=E_(L,R)-B_(L,R),

||E_(L,R)-B_R|| = O_R(exp(-L)),
C_(L,R) -> 0 strongly,
```

while `PL-059` and `PL-053` show that `C_(L,R)` retains an order-one essential-norm defect.

Let `Delta_D` be the Dirichlet Laplacian on `H_R=L^2(0,R)`, let `P_N` project onto its first `N` sine modes, and put

```text
Pi_N=P_N direct_sum P_N.
```

Then there is a constant `A_R<infinity` such that, for every `N>=1` and all sufficiently large `L`,

```text
boxed:
|| Pi_N C_(L,R) Pi_N ||
 <= A_R [ N^2 r_(L,R) + exp(-L) ].
```

Consequently, for every integer sequence `N(L)->infinity` satisfying

```text
N(L)^2 r_(L,R) -> 0,
```

one has

```text
boxed:
|| Pi_(N(L)) C_(L,R) Pi_(N(L)) || -> 0.
```

Thus the completed centered residual vanishes **uniformly on a growing low-frequency sector**, not merely on each fixed vector.

There is a corresponding moving-Sobolev consequence. For `0<s_L<=1`, define

```text
Q_L=(I+Delta_D)^(-s_L/2),
S_L=Q_L direct_sum Q_L.
```

If, with the convention `log(1/0)=+infinity`,

```text
boxed:
s_L log(1/r_(L,R)) -> infinity,
```

then

```text
boxed:
|| S_L C_(L,R) S_L || -> 0.
```

So even a Sobolev regularization whose order tends to zero still erases the Calkin-visible prime residual whenever it weakens sufficiently slowly compared with the logarithmic accuracy of the PNT on the boundary shell.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION`, and `DECISIVE-NEGATIVE` for the routes

```text
completed pole/PNT-centered fixed-depth boundary residual
+ growing Dirichlet frequency cutoff N(L)
+ N(L)^2 r_(L,R) -> 0
    -> nontrivial zeta-specific mesoscopic spectral limit,
```

and

```text
completed pole/PNT-centered fixed-depth boundary residual
+ moving Sobolev order s_L
+ s_L log(1/r_(L,R)) -> infinity
    -> nontrivial zeta-specific norm limit.
```

The rate is **not claimed sharp**. The result does not rule out the transition regime `N(L)^2 r_(L,R)` bounded away from zero, much faster frequency growth, Sobolev orders at or below the inverse-log-PNT-error scale, or a full completed-Weil form scaling in which the archimedean logarithmic frequency cost participates nontrivially. Those are precisely the thinner regimes left to `CLUE-mesoscopic-weil-boundary-topology`.

## Quantitative shell testing from the PNT remainder

The cross-end prime shell measure from `PL-051` is

```text
mu_(L,R)
 = exp(-L)
   sum_(2L-2R<log n<2L)
     Lambda(n)/sqrt(n)
     delta_(2L-log n).
```

Its PNT limit is

```text
d mu_R(delta)
 = exp(-delta/2) 1_[0,2R](delta) d delta.
```

The qualitative weak convergence was already used in `PL-051`. Here we keep the PNT remainder. Let `F` be absolutely continuous on `[0,2R]` with bounded derivative. Since `X_L=exp(2L)`, testing `mu_(L,R)` gives

```text
I_L(F)
 = X_L^(-1/2)
   integral_(X_L exp(-2R))^(X_L)
     x^(-1/2)
     F(log(X_L/x))
     d psi(x).
```

Write

```text
psi(x)=x+E(x).
```

On the shell,

```text
|E(x)| <= r_(L,R) x.
```

The `dx` part is exactly

```text
integral_0^(2R)
  F(delta) exp(-delta/2) d delta.
```

For the remainder, set

```text
w_L(x)
 = X_L^(-1/2) x^(-1/2)
   F(log(X_L/x)).
```

Stieltjes integration by parts gives

```text
integral w_L dE
 = [w_L E]
   - integral E(x) w_L'(x) dx.
```

Moreover

```text
|w_L'(x)|
 <= X_L^(-1/2) x^(-3/2)
    [ |F'| + |F|/2 ].
```

Using `|E(x)|<=r_(L,R)x` and integrating `X_L^(-1/2)x^(-1/2)` over the fixed-ratio shell yields the uniform estimate

```text
boxed:
| I_L(F)
  - integral_0^(2R) F(delta) exp(-delta/2)d delta |

 <= A_R r_(L,R)
    [ ||F||_infinity + ||F'||_infinity ].
```

This is just the fixed-width partial-summation argument of `PL-049` with its error term retained. It uses no zero sum and no analytic continuation.

## Dirichlet-mode matrix elements

Use the normalized Dirichlet basis

```text
e_k(a)=sqrt(2/R) sin(k pi a/R),
k>=1.
```

Extend every `e_k` by zero outside `(0,R)`. Because `e_k` vanishes at both endpoints, its zero extension lies in `H^1(R)`. For the Hankel cross block define

```text
F_(j,k)(delta)
 = integral_R
     conjugate(e_j(b)) e_k(delta-b) db.
```

Then

```text
<e_j,H_(mu_(L,R)) e_k>
 = integral F_(j,k)(delta) d mu_(L,R)(delta),
```

and the same identity with `mu_R` gives the matrix element of the PNT rank-one limit.

Cauchy--Schwarz gives

```text
||F_(j,k)||_infinity <= 1.
```

Differentiating the zero-extended convolution in the weak/absolutely-continuous sense gives

```text
F_(j,k)'(delta)
 = integral_R
     conjugate(e_j(b)) e_k'(delta-b) db,
```

hence

```text
||F_(j,k)'||_infinity
 <= ||e_j||_2 ||e_k'||_2
 = k pi/R.
```

Interchanging the two factors gives the symmetric coarse bound

```text
||F_(j,k)'||_infinity
 <= (pi/R) max(j,k).
```

Therefore, for `j,k<=N`, the quantitative shell estimate yields

```text
| <e_j,(H_(mu_(L,R))-P_R)e_k> |
 <= A_R N r_(L,R).
```

An `N x N` matrix whose entries are bounded by `epsilon` has operator norm at most `N epsilon` (for example by its Hilbert--Schmidt norm). Thus

```text
boxed:
||P_N(H_(mu_(L,R))-P_R)P_N||
 <= A_R N^2 r_(L,R).
```

The same-end small-lag blocks of `B_(L,R)` are `O_R(exp(-L))` in full operator norm by `PL-051`. Hence, on the two-end projection,

```text
||Pi_N(B_(L,R)-B_R)Pi_N||
 <= A_R [N^2 r_(L,R)+exp(-L)].
```

Finally `PL-059` gives

```text
||E_(L,R)-B_R||=O_R(exp(-L)),
```

which proves the displayed estimate for

```text
C_(L,R)=E_(L,R)-B_(L,R).
```

## A genuinely growing uniform sector

The estimate is non-vacuous because `r_(L,R)->0`. Let

```text
eta_L=log(1/r_(L,R))
```

whenever `0<r_(L,R)<1`; if `r_(L,R)=0`, set `eta_L=+infinity` and the shell discrepancy is already zero at this level.

For example, when `eta_L<infinity`, choose

```text
N_L=floor(exp(eta_L/4)).
```

Then `N_L->infinity` and

```text
N_L^2 r_(L,R)
 <= exp(-eta_L/2)
 ->0.
```

So the centered operator has a low-frequency subspace of dimension tending to infinity on which it converges to zero in operator norm. This sharpens the topology ledger from `PL-052`--`PL-055`:

```text
fixed profiles
    -> PNT homogenization / completed cancellation;

expanding low-frequency sector below PNT resolution
    -> uniform norm collapse                         [PL-060];

unrestricted unit sphere
    -> prime-log recurrence survives in Calkin      [PL-052, PL-053].
```

The recurrent witnesses therefore cannot remain at arbitrary slowly growing boundary frequency. They must escape beyond an expanding PNT-controlled resolution window. The theorem does **not** estimate the smallest Kronecker recurrence frequency needed at a given `L`; it only gives a one-sided uniform region in which such a witness cannot produce an order-one centered matrix element.

## Moving Sobolev orders that still collapse

The family `C_(L,R)` is uniformly bounded for fixed `R`: `B_(L,R)` is uniformly bounded by the strong-convergence result of `PL-051`, and `E_(L,R)` is norm-convergent by `PL-059`. Let

```text
M_R=sup_L ||C_(L,R)|| < infinity
```

after discarding a finite initial segment.

Because `Q_L` is a spectral function of `Delta_D`, it commutes with `P_N`. Splitting at `P_N` gives

```text
||S_L C_(L,R) S_L||
 <= ||Pi_N C_(L,R) Pi_N||
    + 2 M_R ||(I-P_N)Q_L||.
```

The tail multiplier is

```text
||(I-P_N)Q_L||
 = [1+((N+1)pi/R)^2]^(-s_L/2).
```

For `0<s_L<=1` and fixed `R`, this is bounded by

```text
A_R N^(-s_L).
```

Therefore

```text
boxed:
||S_L C_(L,R) S_L||
 <= A_R [N^2 r_(L,R)+N^(-s_L)+exp(-L)].
```

Take again

```text
N=floor(exp(eta_L/4)).
```

for large `L`. Then

```text
N^2 r_(L,R) ->0,

N^(-s_L)
 <= A_R exp(-s_L eta_L/4).
```

Hence

```text
s_L eta_L -> infinity
```

implies

```text
||S_L C_(L,R) S_L|| ->0.
```

This extends `PL-055` in the direction the mesoscopic clue explicitly left open: the smoothing order may now tend to zero. Fixed compactness is no longer being used uniformly; instead, the quantitative PNT remainder controls an expanding finite-dimensional head while the weakening Sobolev weight controls the complementary tail.

The condition is sufficient, not necessary. In particular, no claim is made that `s_L` of order `1/eta_L` produces a nontrivial limit. It is only the first scale not eliminated by this estimate.

## Exponent-lattice interpretation

At fixed boundary depth the prime term samples axis vectors

```text
v(n)=m e_p
```

whose logarithmic energy lies in

```text
2L-2R
 < <v(n),(log q)_q>
 < 2L.
```

The scalar deficit

```text
delta=2L-log n
```

forgets the axis label at PNT level, while high boundary frequency can recover coherence of the exact atomic deficits through the prime logarithms (`PL-052`). The present result inserts a quantitative layer between those two facts.

The PNT remainder controls how accurately the atomic exponent-axis shell mimics its continuum deficit measure against test functions with one derivative. Dirichlet mode `k` costs one derivative of size `O(k)`, and an `N`-dimensional operator norm costs one further factor `N`. This is the origin of

```text
N^2 r_(L,R).
```

Thus the estimate is a **resolution bound**: below that scale the exact prime-axis shell is uniformly indistinguishable from the continuum PNT shell after canonical pole centering; only beyond it can the free prime-log phase geometry remain visible to the raw operator topology.

## Beurling / matched-control audit

Nothing in the proof after defining the shell uses unique factorization, the functional equation, or the Riemann zero divisor. It uses only a positive von-Mangoldt-type counting measure with a quantitative remainder

```text
psi_G(x)=x+E_G(x)
```

on a fixed-ratio shell.

If a generalized-prime system satisfies the analogous bound

```text
r^G_(L,R)
 = sup_shell |E_G(x)|/x ->0,
```

then the same Stieltjes argument gives the same finite-mode and moving-Sobolev estimates with `r^G_(L,R)` in place of `r_(L,R)`.

Therefore the collapse regime is **not rational-prime-specific rigidity**. Any successful construction in the remaining transition region must still pass the line's matched-control test; simply choosing a moving cutoff at the PNT-resolution scale does not by itself explain RH.

## Analytic-continuation boundary

No Euler product or Dirichlet series is analytically continued here. The operator `B_(L,R)` is the finite prime-power part already extracted from the completed Weil formula, and `E_(L,R)` is the completed pole term. The only number-theoretic input in the new estimate is the quantitative remainder in

```text
psi(x)=x+E(x),
```

plus the canonical pole/PNT centering proved in `PL-059`.

The no-go therefore lives entirely on the completed explicit-formula side. It does not obtain zero sensitivity by inserting the classical zero sum, and its failure to distinguish rational primes from matched generalized systems is part of the conclusion rather than an analytic-continuation artifact.

## Prior-art and novelty audit

The ingredients are classical or already canonical in this line:

- `PL-049` gives the fixed-ratio Stieltjes partial-summation argument from the prime number theorem;
- `PL-051` gives the boundary Hankel measure, the Dirichlet-independent strong PNT limit, and the `O_R(exp(-L))` same-end blocks;
- `PL-052`--`PL-053` give the complementary unrestricted-frequency norm/Calkin recurrence obstruction;
- `PL-055`--`PL-056` classify fixed Sobolev smoothing and its Schatten endpoints;
- `PL-059` proves that the completed pole term supplies the canonical PNT centering;
- quantitative PNT remainders, Stieltjes integration by parts, Dirichlet spectral cutoffs, and Sobolev tail estimates are standard analytic-number-theory and functional-analysis tools.

A targeted literature check across localized Weil operators, quantitative PNT remainders, moving Galerkin/frequency cutoffs, and Sobolev regularization did not locate this exact fixed-depth boundary specialization. Recent localized-Weil work of Suzuki and compact-window work of Chuk address adjacent operator/positivity questions, but do not supply this quantitative expanding-band estimate. Search absence is not treated as evidence of novelty, and no novelty claim is made for the analytic ingredients.

The durable content is the exact quantitative bridge between two already-persisted regimes that previously appeared disconnected: PNT homogenization on fixed profiles and order-one prime-log recurrence on the unrestricted unit sphere.

## Falsification and boundary tests

The result reduces to independently checkable statements:

1. `r_(L,R)->0` follows from the prime number theorem uniformly on the fixed-ratio shell;
2. Stieltjes integration by parts gives the displayed `C^1` test bound with error `O_R(r_(L,R))`;
3. zero-extended Dirichlet eigenfunctions belong to `H^1(R)` and the convolution test satisfies `||F_(j,k)'||_infinity=O_R(max(j,k))`;
4. an `N x N` entrywise `O_R(N r_(L,R))` bound gives operator norm `O_R(N^2 r_(L,R))`;
5. `PL-051` supplies the `O_R(exp(-L))` same-end term;
6. `PL-059` supplies `||E_(L,R)-B_R||=O_R(exp(-L))`;
7. the Sobolev tail satisfies `||(I-P_N)Q_L||=O_R(N^(-s_L))` uniformly for `0<s_L<=1`;
8. choosing `N=exp(eta_L/4)` makes both the PNT head error and, under `s_L eta_L->infinity`, the Sobolev tail vanish.

Failure of any item invalidates the corresponding conclusion. Improving the `N^2` loss, using additional cancellation in the matrix, or obtaining sharper PNT remainder information may enlarge the proven collapse window; none is needed for the present no-go.

## Consequence for the research line

The accepted mesoscopic clue is narrowed to a genuine transition problem. The completed fixed-depth boundary ledger is now

```text
fixed profiles
    -> pole/PNT cancellation -> 0 strongly             [PL-059]

expanding low-frequency cutoff
    N(L)^2 r_(L,R) ->0
    -> centered operator ->0 in compressed norm        [PL-060]

moving Sobolev smoothing
    s_L log(1/r_(L,R)) -> infinity
    -> centered sandwich ->0 in full norm              [PL-060]

unrestricted high-frequency unit sphere
    -> order-one prime-log recurrence in Calkin        [PL-052, PL-053].
```

Thus `s(L)->0` or `N(L)->infinity` is not, by itself, a mesoscopic mechanism. A surviving candidate must enter the quantitative transition where the smoothing no longer dominates the PNT remainder **and** must simultaneously control the archimedean logarithmic-frequency cost omitted from this bounded-sector estimate. Even there, a positive result must distinguish the rational-prime shell from matched generalized-prime controls rather than merely locating the boundary between weak homogenization and atomic recurrence.