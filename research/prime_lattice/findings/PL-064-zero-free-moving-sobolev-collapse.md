# PL-064 — Zero-free sampling collapses moving Sobolev Weil smoothing far below the PNT scale

## Claim

The zero-sampling improvement of `PL-063` also closes a much larger part of the **moving Sobolev** escape left open by `PL-060`--`PL-062`.

Fix `R>0`. Let

```text
H_R=L^2(0,R),
Delta_D=-d^2/da^2
```

with Dirichlet boundary conditions, and for `0<s<=1/2` put

```text
Q_(s,R)=(I+Delta_D)^(-s/2),
S_(s,R)=Q_(s,R) direct_sum Q_(s,R).
```

Let `J_(L,R)` be the two-end boundary embedding from `PL-051`. Define `A_(L,s,R)` to be the bounded self-adjoint operator representing the naturally `exp(-L)`-normalized **completed Weil quadratic form after the Sobolev sandwich**:

```text
<u,A_(L,s,R)u>
 = exp(-L)
   Q_W^L(J_(L,R) S_(s,R)u).
```

The boundedness here is part of the statement: the pole-minus-prime sector is already bounded by `PL-059`--`PL-060`, while the gamma/scalar sector becomes bounded after every positive Sobolev order by the estimate below.

Let `s_L in (0,1/2]`. More generally, suppose there exists a sequence `U_L->infinity` such that

```text
U_L (log U_L)^2 = o(L^(3/2)),

s_L U_L -> infinity.
```

Then

```text
boxed:
||A_(L,s_L,R)|| -> 0.
```

In particular, the explicit sufficient condition

```text
boxed:
s_L L^(3/2)/(log L)^2 -> infinity
```

implies the same norm collapse. Thus every moving Sobolev order that is asymptotically larger than

```text
(log L)^2/L^(3/2)
```

by a divergent factor still erases the completed boundary residual.

This is much stronger than the previous sufficient no-go from `PL-062`,

```text
s_L L^(3/5)/(log L)^(1/5) -> infinity.
```

The gain is exactly the same one that separates `PL-063` from `PL-062`: keep the vertical zero frequency in the completed explicit formula, control the low-frequency head through zero-free-region sampling, and use the Sobolev weight only to kill the complementary tail.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION`, and `DECISIVE-NEGATIVE` for the route

```text
completed fixed-depth Weil boundary form
+ moving Dirichlet Sobolev smoothing s_L
+ s_L L^(3/2)/(log L)^2 -> infinity
    -> nontrivial zeta-specific norm limit.
```

The scale is only a sufficient barrier. It is not claimed sharp, and the borderline `s_L` of order `(log L)^2/L^(3/2)` or smaller remains outside this theorem.

## The bounded pole-minus-prime sector

Retain the canonically centered bounded completed sector from `PL-059`--`PL-060`,

```text
C_(L,R)=E_(L,R)-B_(L,R),
```

where `E_(L,R)` is the completed zeta-pole boundary operator and `B_(L,R)` is the normalized von-Mangoldt boundary operator. For fixed `R`,

```text
M_R := sup_L ||C_(L,R)|| < infinity
```

after discarding a finite initial segment.

Let `P_N` project onto the first `N` Dirichlet sine modes of `H_R`, and put

```text
Pi_N=P_N direct_sum P_N.
```

Before adding the archimedean term, the proof of `PL-063` gives the following bound for the centered pole-minus-prime compression. For every sufficiently large `L` and every auxiliary height `T>=max(e^e,2N)`,

```text
||Pi_N C_(L,R) Pi_N||

 <= C_R [
      log(2+T)
      exp( - c L /
            ((log T)^(2/3)(log log T)^(1/3)) )

      + N^2 log(2+T)/T
      + exp(-L)
    ].
```

It comes from the exact compact-boundary zero expansion, the Paley--Wiener sampling estimate at the zeta zeros, the Vinogradov--Korobov zero-free region, and one integration by parts on the high-zero tail. No Euler product is continued into the critical strip.

Taking `T=N^3`, `PL-063` therefore implies

```text
boxed:
log N (log log N)^2=o(L^(3/2))
    =>
||Pi_N C_(L,R) Pi_N|| ->0.
```

The archimedean term was not needed to obtain this head estimate.

## Sobolev tail plus zero-sampled head

Write, for brevity,

```text
Q_L=Q_(s_L,R),
S_L=S_(s_L,R).
```

Because `Q_L` is a spectral function of `Delta_D`, it commutes with `P_N`. Its complementary spectral tail satisfies

```text
||(I-P_N)Q_L||
 <= C_R N^(-s_L).
```

Split both copies of `S_L` into their `Pi_N` head and complementary tail. Since `C_(L,R)` is uniformly bounded,

```text
||S_L C_(L,R) S_L||

 <= ||Pi_N C_(L,R) Pi_N||
    + C_R M_R N^(-s_L).
```

(The harmless constant absorbs the two cross terms and the tail-tail term.)

Now take

```text
N_L=floor(exp(U_L)).
```

The first hypothesis gives exactly the zero-sampled head condition of `PL-063`, hence

```text
||Pi_(N_L) C_(L,R) Pi_(N_L)|| ->0.
```

The second hypothesis gives

```text
N_L^(-s_L)
 = exp(-s_L U_L+o(1))
 ->0.
```

Therefore

```text
boxed:
||S_L C_(L,R) S_L|| ->0.
```

This already controls the entire prime-plus-pole part of the moving smoothed construction.

## The gamma factor stays negligible under the same moving smoothing

What remains is the scalar plus archimedean part of the completed Weil form. `PL-061` records its Fourier multiplier bound

```text
|m_infinity(t)|
 <= C [1+log(2+|t|)].
```

For fixed positive Sobolev order, `PL-055` already makes this harmless. The only issue here is whether the constant can be controlled as `s_L->0`.

Let `0<s<=1/2` and set

```text
r=s/2 <= 1/4.
```

For `f in H_R`, the spectral Sobolev norm of `Q_(s,R)f` at order `r` is uniformly bounded:

```text
||(I+Delta_D)^(r/2) Q_(s,R)f||_2
 <= ||f||_2,
```

because `r<=s`. For `0<=r<=1/4`, the Dirichlet spectral `H^r` norm is uniformly equivalent to the ordinary interval `H^r` norm, and zero extension from `(0,R)` to the line is uniformly bounded because `r` stays strictly below the trace threshold `1/2`. Consequently, if `w` is the zero extension of `Q_(s,R)f`,

```text
integral_R
 (1+t^2)^r |w_hat(t)|^2 dt
 <= C_R ||f||_2^2.
```

The elementary inequality

```text
log(2+|t|)
 <= C (1+r^(-1)) (1+t^2)^r
```

therefore gives

```text
boxed:
integral_R
 [1+log(2+|t|)] |w_hat(t)|^2 dt
 <= C_R (1+s^(-1)) ||f||_2^2.
```

The two-end embedding only translates and sums two such zero-extended profiles, so the same estimate, with another `R`-dependent constant, holds for `J_(L,R)S_(s,R)u`. After the natural boundary normalization,

```text
boxed:
| exp(-L) Q_infinity(J_(L,R)S_(s,R)u) |
 <= C_R exp(-L)(1+s^(-1)) ||u||_2^2.
```

The remaining scalar term has the smaller `O_R(exp(-L))||u||^2` bound.

Under the general head-tail hypotheses, `U_L(log U_L)^2=o(L^(3/2))` implies `U_L=O(L^(3/2))`, while `s_L U_L->infinity` implies `s_L^(-1)=o(U_L)`. Hence

```text
exp(-L)(1+s_L^(-1)) ->0.
```

Combining this with the pole-minus-prime estimate proves

```text
||A_(L,s_L,R)|| ->0.
```

## An explicit sufficient scale

Put

```text
Lambda_L=L^(3/2)/(log L)^2,
eta_L=s_L Lambda_L.
```

Assume

```text
eta_L -> infinity.
```

Choose

```text
U_L=Lambda_L/sqrt(eta_L).
```

Since `s_L<=1/2`, one has `U_L->infinity`. Also `log U_L=O(log L)`, so

```text
U_L (log U_L)^2/L^(3/2)
 <= C/sqrt(eta_L)
 ->0,
```

while

```text
s_L U_L
 = sqrt(eta_L)
 ->infinity.
```

Thus the general criterion applies and proves the stated corollary

```text
s_L L^(3/2)/(log L)^2 -> infinity
    =>
||A_(L,s_L,R)|| ->0.
```

This is a deliberately non-sharp way to state the zero-sampling barrier. It avoids pretending that the logarithmic factors or the exponent `3/2` locate the true transition.

## Why this is not another critical-line mechanism

The moving parameter `s_L` is a **Sobolev regularity order**, not the real part of the zeta variable. Nothing distinguished happens here at the numerical value `1/2`; the theorem is explicitly about orders tending toward `0`.

The exponent `3/2` comes instead from combining:

```text
Vinogradov--Korobov zero-free geometry
+ compact-boundary zero sampling
+ high-zero integration-by-parts decay
+ one-dimensional Sobolev tail suppression.
```

Changing the available zero-free envelope or the frequency model would change the resulting barrier. It therefore cannot be interpreted as an intrinsic selection of the Riemann critical line.

## Beurling and matched-control audit

The Sobolev head-tail argument itself is universal functional analysis. The number-theoretic information enters only through the `PL-063` compressed head estimate:

```text
explicit-formula zero expansion
+ zero-free envelope near Re(s)=1
+ local zero-count bound.
```

A generalized-prime zeta object with analogous completed explicit formula, zero-free region, and local zero-density control would satisfy the same moving-Sobolev collapse after the identical boundary construction. `PL-062` and the Beurling zero-free/PNT literature already show that this style of scale transfer is not uniquely rational-prime rigidity.

Thus the theorem is a **negative topology barrier**, not evidence toward RH. Reaching the surviving scale does not by itself distinguish the ordinary primes from matched generalized-prime controls.

## Analytic-continuation audit

No Euler-product identity is used outside `Re(s)>1`.

For each `L` the von-Mangoldt boundary shell is finite. The zero-sensitive estimate inherited from `PL-063` uses the classical completed Weil/von-Mangoldt explicit formula, whose meromorphic continuation is already part of the global theorem. The Vinogradov--Korobov input is an unconditional zero-free region near `Re(s)=1`, and the high-zero tail uses only the unconditional strip location `0<Re(rho)<1` and local zero count.

The additional Sobolev argument is purely on the completed boundary form and does not introduce any new continuation step.

## Prior-art and novelty audit

All external ingredients are classical or already anchored in `SOURCES.md`:

- Weil and Bombieri supply the completed explicit-formula/Weil-form framework (`SOURCES.md` 25--26);
- Suzuki and current localized-Weil work provide nearby operator/localization context (`SOURCES.md` 56--58);
- Bellotti and Johnston provide the Vinogradov--Korobov zero-free/PNT scale used in `PL-062`--`PL-063` (`SOURCES.md` 59--60);
- Broucke supplies the generalized-prime matched-control perspective (`SOURCES.md` 61);
- fractional Sobolev spectral calculus, zero extension below order `1/2`, Paley--Wiener sampling bounds, and the logarithm-versus-small-power inequality are standard functional analysis.

A targeted literature audit across localized/truncated Weil operators, Galerkin frequency windows, Paley--Wiener sampling at zeta zeros, and Sobolev regularization did not locate this exact moving-order boundary theorem. Recent localized-Weil/Galerkin work studies finite windows, explicit zero dictionaries, positivity, or archimedean tails rather than this `s_L->0` zero-free collapse regime. Search absence is not evidence of novelty.

The durable content is the line-specific consequence: the much stronger zero-sampled band barrier of `PL-063` automatically propagates through the spectral tail calculus and removes almost all of the moving-Sobolev regime that `PL-060`--`PL-062` had left open.

## Falsification and boundary tests

The result reduces to the following independently checkable points:

1. the pre-archimedean part of the `PL-063` proof gives the displayed compressed estimate for `C_(L,R)`;
2. `C_(L,R)` is uniformly bounded for fixed `R` by `PL-059`--`PL-060`;
3. `||(I-P_N)Q_(s,R)||=O_R(N^(-s))`;
4. the head-tail decomposition loses only a fixed constant times that spectral tail;
5. `U_L(log U_L)^2=o(L^(3/2))` makes the zero-sampled head vanish;
6. `s_L U_L->infinity` makes the Sobolev tail vanish;
7. for `r=s/2<=1/4`, zero extension is uniformly bounded in `H^r` and the Dirichlet spectral `H^r` norm of `Q_s f` is bounded by `||f||`;
8. `log(2+|t|)<=C(1+r^(-1))(1+t^2)^r` gives the `O_R(1+s^(-1))` archimedean form bound;
9. the natural `exp(-L)` normalization then kills the archimedean/scalar sector under the same hypotheses.

Failure of any item invalidates the corresponding conclusion. In particular the theorem does not apply to a moving topology that is not spectrally comparable to the Dirichlet Sobolev scale, to unrestricted high-frequency states, or to a boundary depth/scaling outside the reductions already established in `PL-057`--`PL-058`.

## Consequence for the research line

`CLUE-mesoscopic-weil-boundary-topology` remains open but is narrowed again.

The fixed-depth ledger now contains the stronger implication

```text
moving Sobolev order s_L
+ s_L L^(3/2)/(log L)^2 -> infinity
    -> full completed smoothed form ->0 in norm.
```

Therefore a surviving **Sobolev** mesoscopic mechanism must weaken at least to the unresolved scale

```text
s_L = O((log L)^2/L^(3/2))
```

along the relevant sequence, or else leave the Dirichlet spectral-Sobolev topology altogether. Even at that scale, survival would only show that the present zero-free sampling estimate has stopped forcing collapse; it would not establish a nontrivial limit, rational-prime specificity, zero localization, or RH rigidity.