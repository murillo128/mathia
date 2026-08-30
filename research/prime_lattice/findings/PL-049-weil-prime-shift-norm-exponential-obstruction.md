# PL-049 — Endpoint states force the joint localized-Weil prime-shift norm to remain exponential

## Claim

`PL-046` isolates a genuinely joint target-relative operator in the compact-window Weil problem. On

```text
H_L = L^2(-L,L)
```

let `T_u` be translation by `u>0` compressed to the window, and put

```text
K_L
 = sum_(log n<2L) Lambda(n)/sqrt(n)
     (T_(log n)+T_(log n)^*).
```

Then the prime part of the localized completed Weil quadratic form is

```text
Q_prime,L(v) = -<v,K_L v>.
```

`PL-046` used the sharp one-lag Boas--Kac/Caratheodory--Fejer bound to prove

```text
||K_L|| <= (2+o(1)) exp(L).
```

A direct endpoint-localized Rayleigh quotient gives the complementary lower bound

```text
||K_L|| >= (2(1-exp(-1))^2+o(1)) exp(L),
```

and therefore

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

Thus the unresolved possibility explicitly left in `PL-046`, for example

```text
||K_L|| = o(exp(L)),
```

is impossible. Joint compatibility among all rational-prime-power compressed translations may still improve constants, signs, low eigenvalues, or interaction with the archimedean part, but it **cannot lower the operator-norm scale below exponential order**.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the route

```text
joint prime-power lag geometry
    -> subexponential norm of the localized prime operator
    -> scalable Weil-positivity gain.
```

The upper bound is the classical support-rigidity consequence recorded in `PL-046`; the lower bound below is an exact derivation from positivity of the von-Mangoldt weights and the prime number theorem. It is not claimed as a new theorem in the literature.

## Endpoint test vector

Fix `h>0` and take `L>h`. Define the two endpoint intervals

```text
I_-=[-L,-L+h],
I_+=[L-h,L]
```

and the normalized nonnegative vector

```text
v_(L,h)
 = (2h)^(-1/2) (1_(I_-)+1_(I_+)).
```

Then

```text
||v_(L,h)||_2=1.
```

For a lag in the outer shell

```text
2L-2h < u < 2L,
```

write

```text
delta=2L-u in (0,2h).
```

Translation by `u` moves a portion of the left endpoint block onto the right endpoint block. Its overlap length is the triangular function

```text
tau_h(delta)
 = delta,       0<=delta<=h,
 = 2h-delta,   h<=delta<=2h.
```

Consequently

```text
<v_(L,h),T_u v_(L,h)>
 = tau_h(delta)/(2h)
```

for these outer lags. Since the test vector is nonnegative, all the remaining translation matrix elements are nonnegative as well. Every coefficient

```text
a_n=Lambda(n)/sqrt(n)
```

is nonnegative. Hence

```text
<K_L v_(L,h),v_(L,h)>
 >= (1/h)
    sum_(2L-2h<log n<2L)
      Lambda(n)/sqrt(n)
      tau_h(2L-log n).
```

Because `K_L` is self-adjoint,

```text
||K_L||
 >= <K_L v_(L,h),v_(L,h)>.
```

The characteristic functions above are legitimate `L^2` test vectors. If one wants to remain inside the original smooth Weil test class `C_c^infinity(-L,L)`, approximate the two endpoint blocks in `L^2` by smooth compactly supported functions. Since `K_L` is bounded for each fixed `L`, the corresponding Rayleigh quotients converge, so the operator-norm lower bound is unchanged.

## Prime-number-theorem asymptotic on the outer shell

Let

```text
psi(x)=sum_(n<=x) Lambda(n).
```

The prime number theorem is

```text
psi(x)=x+o(x).
```

For fixed `h`, the shell in the preceding sum has a fixed multiplicative width:

```text
exp(2L-2h) < n < exp(2L).
```

A standard Stieltjes partial-summation/rescaling consequence of the PNT is that for every fixed continuous piecewise-smooth `phi` on `[0,2h]`,

```text
sum_(2L-2h<log n<2L)
  Lambda(n)/sqrt(n) phi(2L-log n)

 = (1+o(1)) exp(L)
   integral_0^(2h) phi(delta) exp(-delta/2) d delta.
```

To see the scaling directly, write `x=exp(2L)` and `n=x exp(-delta)`. Replacing `d psi(n)` by `dn` at PNT accuracy gives

```text
n^(-1/2) dn
 = exp(L) exp(-delta/2) d delta
```

up to orientation. Because `delta` remains in a fixed compact interval, the PNT error is uniform after this rescaling; integration by parts makes the statement rigorous.

Taking

```text
phi=tau_h
```

gives

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

For the simple fixed choice `h=2`,

```text
C_2
 = 2(1-exp(-1))^2
 ~= 0.7991528.
```

Thus

```text
(2(1-exp(-1))^2+o(1)) exp(L)
 <= ||K_L||
 <= (2+o(1)) exp(L),
```

which proves the claimed `Theta(exp(L))` norm scale.

No optimization of `h` is needed for the obstruction. The point is the positive constant, not its best value.

## Exponent-lattice interpretation

The outer-shell terms are prime-power axis points

```text
m e_p
```

whose energies satisfy

```text
2L-2h < m log p < 2L.
```

The endpoint vector turns every such long compressed translation into a **positive bridge between the two ends of the Weil window**. Instead of asking the different prime lags to align in phase, as in the Kronecker pointwise obstruction of `PL-045`, the test state geometrically aligns a whole energy shell at once:

```text
left endpoint block
   -- translation by log(p^m) almost 2L -->
right endpoint block.
```

The PNT says that the weighted von-Mangoldt mass in any fixed-width outer logarithmic shell is already of order `exp(L)`. The triangular overlap loses only a fixed factor. Therefore no cancellation among shorter lags, and no incompatibility among their individual extremizers, can remove this positive Rayleigh quotient.

This is a different obstruction from `PL-045`:

```text
PL-045:
finite prime phases + Kronecker recurrence
    -> pointwise symbol regains amplitude ~4 exp(L)

PL-046:
compact-support autocorrelation
    -> termwise support rigidity lowers the universal upper envelope
       to ~2 exp(L)

PL-049:
endpoint-localized admissible states
    -> the exact joint compressed-shift operator still has norm
       at least c exp(L), c>0.
```

Thus target-relative support structure genuinely helps, but it cannot change the exponential order of the worst prime contribution.

## Why this does not decide localized Weil positivity

The completed localized Weil form contains more than `-K_L`. In particular, the archimedean/pole part is essential, and positivity concerns the bottom of the **full** self-adjoint form/operator, not the absolute norm of the prime contribution alone.

The lower bound also says nothing about the sign or size of the relevant extremal eigenvalue after combining prime and archimedean pieces. A large positive eigenvalue of `K_L` produces a large negative prime quadratic contribution, but the completed form may have compensating structure. Conversely, controlling `||K_L||` sharply is not equivalent to RH.

The following remain live:

```text
- a better constant in exp(-L)||K_L||;
- asymptotics of the top and bottom eigenvalues separately;
- spectral localization or low-rank structure of K_L;
- cancellation created specifically by the archimedean term;
- cross-scale identities as L crosses m log p/2;
- global Weil positivity or a valid large-L limiting determinant.
```

What is closed is only the hope that the **joint prime-lag operator norm itself** becomes subexponential because the different compressed shifts cannot share extremizing vectors.

## Beurling and matched-control audit

The mechanism is not specific enough to distinguish the ordinary rational primes from all generalized systems. The proof uses only:

```text
1. positive weights;
2. an outer logarithmic shell of lags near 2L;
3. weighted shell mass of order exp(L).
```

Any generalized-prime or positive frequency system with the analogous weighted counting law gives the same lower-bound construction. Unique factorization, rational independence of `{log p}`, the functional equation, and the detailed zero divisor do not enter.

This is therefore an **obstruction**, not a candidate RH mechanism. It strengthens the control lesson of `PL-046`: even after replacing independent one-lag inequalities by the exact joint operator, its coarse norm scale is governed by positive outer-shell mass and window geometry rather than subtle rational-prime correlations.

## Analytic-continuation boundary

No Euler product is used or continued into the critical strip.

For each fixed `L`, `K_L` is the finite non-archimedean part extracted from the completed Weil explicit formula, with support restricted by `log n<2L`. The lower bound is an `L^2` operator calculation on that finite sum, followed by the prime number theorem as `L->infinity`.

Thus the derivation lives entirely on the already-completed explicit-formula side and survives the analytic-continuation audit.

## Prior-art and novelty audit

The ingredients are classical or already persisted:

- `PL-046` derives the exact joint compressed-translation operator and the upper bound `||K_L||<=(2+o(1))exp(L)` from the classical Boas--Kac/Caratheodory--Fejer support theorem.
- The prime number theorem in the form `psi(x)=x+o(x)` supplies the outer-shell weighted asymptotic.
- Marcus Chuk's August 2026 compact-window Weil paper, already recorded in `SOURCES.md` and `PL-045`, proves the different pointwise Kronecker-envelope obstruction and its doubly exponential consequence for one certificate. Its stated argument concerns the trigonometric prime-comb supremum, not the compressed-translation operator norm used here.

A targeted search for combinations of localized Weil quadratic forms, von-Mangoldt weighted compressed/truncated translations, Boas--Kac bounds, and operator-norm asymptotics did not locate a source stating this endpoint Rayleigh lower bound or a stronger classification of `||K_L||`. That search result is **not** treated as proof of novelty. The stable claim is only the exact derived no-go above.

## Falsification and boundary tests

The core lower bound would fail if any of the following were false:

1. for `u=2L-delta`, the two endpoint intervals had overlap other than `tau_h(delta)`;
2. some von-Mangoldt coefficient in `K_L` were negative;
3. the fixed-log-width PNT rescaling failed to have the displayed `exp(L)` asymptotic;
4. the `K_L` used in `PL-046` differed from the prime quadratic-form operator by a sign or factor that changes the Rayleigh calculation.

Items 1 and 2 are elementary. Item 3 is a standard fixed-ratio consequence of `psi(x)~x`; item 4 follows directly from

```text
Q_prime,L(v)
 = -2 sum_n Lambda(n)/sqrt(n) Re <v,T_(log n)v>
 = -<v,K_L v>.
```

The finding would be materially strengthened by an exact limit for `exp(-L)||K_L||`, but no such limit is claimed.

## Consequence for the research line

The compact-Weil branch now has a sharper scale ledger:

```text
pointwise prime comb             A_L ~ 4 exp(L)      [PL-045]
support-aware termwise envelope  B_L ~ 2 exp(L)      [PL-046]
exact joint prime operator        c exp(L) <= ||K_L|| <= 2 exp(L) [PL-049]
```

with the explicit admissible constant `c=2(1-exp(-1))^2>0`.

Accordingly, the next useful question is **not** whether joint prime-power translations make the worst prime operator subexponential. They do not. Any further gain relevant to RH must use finer spectral/sign information, the archimedean coupling, threshold-to-threshold evolution, or another zeta-specific global observable rather than the coarse norm of the non-archimedean compressed-shift sum alone.