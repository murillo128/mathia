# PL-049 — Endpoint states force the joint localized-Weil prime-shift norm to remain exponential

## Claim

`PL-046` isolates a genuinely joint target-relative operator in the compact-window Weil problem. On

```text
H_L = L^2(-L,L)
```

let `T_u` be translation by `u>0` compressed to the window and put

```text
K_L
 = sum_(log n<2L) Lambda(n)/sqrt(n)
     (T_(log n)+T_(log n)^*).
```

Then the non-archimedean part of the localized completed Weil quadratic form is

```text
Q_prime,L(v) = -<v,K_L v>.
```

`PL-046` proves, from the sharp one-lag Boas--Kac/Caratheodory--Fejer bound,

```text
||K_L|| <= (2+o(1)) exp(L).
```

A direct endpoint-localized Rayleigh quotient gives the complementary bound

```text
||K_L|| >= (2(1-exp(-1))^2+o(1)) exp(L),
```

and hence

```text
boxed: ||K_L|| = Theta(exp(L)).
```

More generally, for every fixed `h>0`,

```text
liminf_(L->infinity) exp(-L)||K_L||
 >= C_h
 = 4(1-exp(-h/2))^2/h
 > 0.
```

Thus the possibility explicitly left open in `PL-046`, for example

```text
||K_L|| = o(exp(L)),
```

is impossible. Joint compatibility among the rational-prime-power compressed translations may still improve constants, signs, low eigenvalues, or coupling to the archimedean part, but it **cannot reduce the operator-norm scale below exponential order**.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the route

```text
joint prime-power lag geometry
    -> subexponential norm of the localized prime operator
    -> scalable Weil-positivity gain.
```

The upper bound is the support-rigidity consequence already recorded in `PL-046`; the lower bound below is an exact derivation from positivity of the von-Mangoldt weights and the prime number theorem. No literature novelty is claimed.

## Endpoint Rayleigh quotient

Fix `h>0` and, for the exact overlap formula below, take `L>3h/2`. Define

```text
I_-=[-L,-L+h],
I_+=[L-h,L]
```

and

```text
v_(L,h)
 = (2h)^(-1/2) (1_(I_-)+1_(I_+)).
```

Then `||v_(L,h)||_2=1`. For a lag

```text
2L-2h < u < 2L,
```

write `delta=2L-u`. Translation by `u` carries part of the left endpoint block onto the right endpoint block. Since these outer lags exceed `h`, there are no same-block overlaps, and

```text
<v_(L,h),T_u v_(L,h)>
 = tau_h(delta)/(2h),
```

where

```text
tau_h(delta)
 = delta,       0<=delta<=h,
 = 2h-delta,   h<=delta<=2h.
```

For all other positive lags the matrix element is nonnegative because `v_(L,h)` is nonnegative. Since every coefficient

```text
a_n=Lambda(n)/sqrt(n)
```

is nonnegative,

```text
<K_L v_(L,h),v_(L,h)>
 >= (1/h)
    sum_(2L-2h<log n<2L)
      Lambda(n)/sqrt(n)
      tau_h(2L-log n).
```

Self-adjointness gives

```text
||K_L|| >= <K_L v_(L,h),v_(L,h)>.
```

The indicator vector is a legitimate `L^2` test state. If one wants to remain inside the original smooth Weil test class, approximate the two endpoint blocks in `L^2` by functions in `C_c^infinity(-L,L)`. For fixed `L`, `K_L` is bounded, so the Rayleigh quotients converge and the norm lower bound is unchanged.

## Fixed-width PNT asymptotic

Let

```text
psi(x)=sum_(n<=x) Lambda(n)=x+o(x).
```

For fixed `h` and any fixed continuous piecewise-smooth `phi` on `[0,2h]`, Stieltjes partial summation gives

```text
sum_(2L-2h<log n<2L)
  Lambda(n)/sqrt(n) phi(2L-log n)

 = exp(L)
   integral_0^(2h) phi(delta) exp(-delta/2) d delta
   + o(exp(L)).
```

Indeed, with `x=exp(2L)` and `n=x exp(-delta)`, the interval is a fixed multiplicative annulus `x exp(-2h)<n<x`. The PNT estimate `psi(xy)=xy+o(x)` is uniform for `y` in the fixed compact interval `[exp(-2h),1]`; integration by parts then replaces `d psi(n)` by `dn` with total error `o(sqrt(x))=o(exp(L))`. The main density rescales as

```text
n^(-1/2) dn
 -> exp(L) exp(-delta/2) d delta.
```

Taking `phi=tau_h` yields

```text
liminf_(L->infinity) exp(-L)||K_L||
 >= (1/h)
    integral_0^(2h) tau_h(delta) exp(-delta/2) d delta.
```

The elementary integral is

```text
integral_0^(2h) tau_h(delta) exp(-delta/2) d delta
 = 4(1-exp(-h/2))^2,
```

so

```text
C_h=4(1-exp(-h/2))^2/h.
```

Choosing `h=2` gives

```text
C_2
 = 2(1-exp(-1))^2
 ~= 0.7991528.
```

Combining with `PL-046`,

```text
(2(1-exp(-1))^2+o(1)) exp(L)
 <= ||K_L||
 <= (2+o(1)) exp(L).
```

No optimization of `h` is needed for the obstruction; only a positive constant matters.

## Exponent-lattice interpretation

The lower bound uses only prime-power axis points

```text
m e_p
```

in the outer energy shell

```text
2L-2h < m log p < 2L.
```

The endpoint state geometrically aligns that entire shell: every such long compressed translation carries a positive overlap from the left endpoint block to the right endpoint block. The PNT says that the weighted von-Mangoldt mass in a fixed-width outer logarithmic shell is already of order `exp(L)`, and the triangular overlap loses only a fixed factor.

This is a different obstruction from the prime-phase recurrence in `PL-045`:

```text
PL-045:
finite prime phases + Kronecker recurrence
    -> pointwise symbol regains amplitude ~4 exp(L)

PL-046:
compact-support autocorrelation
    -> termwise support rigidity lowers the universal upper envelope
       to ~2 exp(L)

PL-049:
endpoint-localized states
    -> the exact joint compressed-shift operator still has norm
       at least c exp(L), c>0.
```

Thus target-relative support structure genuinely improves the pointwise envelope but cannot change the exponential order of the worst non-archimedean operator contribution.

## Scope: this is not a Weil-positivity lower bound

The completed localized Weil form contains the archimedean and pole terms in addition to `-K_L`. Positivity concerns the bottom of the **full** form/operator, not `||K_L||` alone. The present bound therefore says nothing by itself about the sign of the localized Weil ground state or about RH.

It also leaves open finer questions such as

```text
- the optimal constant in exp(-L)||K_L||;
- top and bottom eigenvalue asymptotics separately;
- spectral localization or effective rank of K_L;
- cancellation created by the archimedean term;
- identities across the thresholds L=(m log p)/2;
- global Weil positivity or a valid large-L limiting determinant.
```

What is closed is only the suggestion that incompatibility among the individual compressed-shift extremizers might make the **joint prime operator norm** subexponential.

## Beurling and universality audit

The lower-bound mechanism uses only

```text
1. positive lag weights;
2. an outer logarithmic shell near 2L;
3. weighted shell mass of order exp(L).
```

Accordingly, any generalized-prime or positive-frequency system with the analogous weighted counting law admits the same endpoint construction. Rational independence of `{log p}`, the functional equation, and the detailed zeta divisor do not enter.

This is therefore an obstruction rather than an RH mechanism. It strengthens the matched-control lesson of `PL-046`: even the exact joint operator has a coarse norm scale governed by positive shell mass and one-sided window geometry, not by subtle rational-prime correlations.

## Analytic-continuation boundary

No Euler product is used or continued into the critical strip. For each fixed `L`, `K_L` is the finite non-archimedean term extracted from the completed Weil explicit formula, with `log n<2L`. The asymptotic then uses only the prime number theorem.

The argument therefore lives entirely on the already-completed explicit-formula side.

## Prior-art and novelty audit

The ingredients are classical or already persisted:

- `PL-046` derives `K_L` and the upper bound `||K_L||<=(2+o(1))exp(L)` from the classical Boas--Kac/Caratheodory--Fejer support theorem.
- The prime number theorem in the form `psi(x)=x+o(x)` supplies the fixed-width outer-shell asymptotic.
- Marcus Chuk's August 2026 compact-window Weil paper, already recorded in `SOURCES.md` and `PL-045`, proves the distinct pointwise Kronecker-envelope obstruction and its doubly exponential consequence for one positivity certificate. Its argument concerns the trigonometric prime-comb supremum, not the compressed-translation operator norm above.

A targeted literature search for localized Weil quadratic forms combined with von-Mangoldt weighted compressed/truncated translations, Boas--Kac bounds, and operator-norm asymptotics did not locate this endpoint Rayleigh estimate or a stronger classification of `||K_L||`. That absence is **not** evidence of novelty. The durable claim is only the exact no-go derived here.

## Falsification and boundary tests

The lower bound reduces to four independently checkable steps:

1. the overlap of the two endpoint blocks at `u=2L-delta` is `tau_h(delta)`;
2. the von-Mangoldt coefficients are nonnegative;
3. fixed-width PNT rescaling gives the displayed `exp(L)` weighted-shell asymptotic;
4. `Q_prime,L(v)=-<v,K_Lv>` fixes the factor of two.

Items 1, 2, and 4 are elementary from the definitions; item 3 is a standard fixed-ratio consequence of `psi(x)~x`. An exact limit for `exp(-L)||K_L||` would strengthen the result but is not claimed.

## Consequence for the research line

The compact-Weil scale ledger is now

```text
pointwise prime comb             A_L ~ 4 exp(L)       [PL-045]
support-aware termwise envelope  B_L ~ 2 exp(L)       [PL-046]
exact joint prime operator        c exp(L) <= ||K_L|| <= 2 exp(L)  [PL-049]
```

with the explicit admissible constant `c=2(1-exp(-1))^2>0`.

Further work should therefore not seek an RH mechanism in a subexponential norm of the non-archimedean compressed-shift sum. Any genuine gain must use finer spectral/sign information, the archimedean coupling, threshold-to-threshold evolution, or another zeta-specific global observable.