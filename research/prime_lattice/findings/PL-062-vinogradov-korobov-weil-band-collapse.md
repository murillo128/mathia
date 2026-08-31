# PL-062 — Vinogradov–Korobov PNT decay forces subcritical Weil-band collapse

## Claim

The abstract moving-band no-go of `PL-060`--`PL-061` can be made unconditional and quantitative for the ordinary rational primes by inserting the best currently available Prime Number Theorem remainder scale.

Fix `R>0` and write

```text
X_L = exp(2L),

r_(L,R)
 = sup_(X_L exp(-2R) <= x <= X_L)
     |psi(x)-x|/x,

Phi(L)
 = L^(3/5)/(log L)^(1/5).
```

There are constants `c_R,C_R>0` such that, for all sufficiently large `L`,

```text
boxed:
r_(L,R) <= C_R exp(-c_R Phi(L)).
```

Consequently, for the full completed Weil-form compression `W_(L,R,N)` of `PL-061`,

```text
||W_(L,R,N)||
 <= A_R [
      N r_(L,R)
      + exp(-L)(1+log(1+N))
    ],
```

and therefore every moving cutoff satisfying

```text
boxed:
log N(L) = o(Phi(L))
```

obeys

```text
boxed:
||W_(L,R,N(L))|| -> 0.
```

More quantitatively, after fixing any `0<eta<c_R`, every band with

```text
log N(L) <= eta Phi(L)
```

for all sufficiently large `L` also collapses in norm. In particular, this rules out all polynomial cutoffs `N(L)=L^A`, and every stretched exponential

```text
N(L)=exp(L^alpha),
alpha<3/5.
```

The same PNT input sharpens the moving-Sobolev no-go of `PL-060`. If `s_L->0` and

```text
boxed:
s_L Phi(L) -> infinity,
```

then the already-centered residual still converges to zero in the corresponding moving Sobolev-sandwiched operator norm. Equivalently, every weakening satisfying

```text
s_L >> (log L)^(1/5)/L^(3/5)
```

remains too strong to retain a mesoscopic signal.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION`. This is `DECISIVE-NEGATIVE` only for the routes

```text
fixed-depth completed Weil boundary form
+ first N(L) Dirichlet modes
+ log N(L)=o(Phi(L))
    -> nontrivial mesoscopic norm limit,
```

and

```text
completed pole/PNT-centered boundary residual
+ moving Sobolev order s_L
+ s_L Phi(L)->infinity
    -> nontrivial norm limit.
```

The finding does **not** determine the transition at `log N comparable to Phi(L)`, does not estimate the actual size of `1/r_(L,R)` from below beyond `PL-061`'s elementary staircase bound, and does not rule out a non-band topology, a frequency window concentrated around atomic prime discrepancies, or a different full-Weil form-domain scaling.

## Unconditional PNT input

The relevant analytic-number-theory input is entirely on the classical `Re(s)=1` side of the zeta problem. Johnston showed that a Vinogradov--Korobov zero-free region of the form

```text
beta
 > 1 - 1/[c (log t)^(2/3)(log log t)^(1/3)]
```

combined with a suitable zero-density estimate gives

```text
|psi(x)-x|/x
 << exp(-omega(x))
    (log x)^9/(log log x)^3,
```

where

```text
omega(x)
asymp
(log x)^(3/5)/(log log x)^(1/5).
```

Bellotti subsequently proved a zero-density estimate sufficiently sharp near the Vinogradov--Korobov boundary to obtain the corresponding optimal PNT remainder in the form

```text
psi(x)-x
 << x exp(-omega(x)),
```

with no `(1-epsilon)` loss in the exponential factor attached to the available zero-free function. `SOURCES.md` 59--60 are the literature anchors for these statements.

For the present fixed-ratio shell,

```text
x in [exp(2L-2R), exp(2L)],
```

one has uniformly

```text
log x = 2L + O_R(1),
log log x = log L + O_R(1).
```

Hence the Vinogradov--Korobov scale is uniformly comparable to

```text
Phi(L)=L^(3/5)/(log L)^(1/5),
```

and the harmless algebraic logarithmic factors in Johnston's version can be absorbed by a smaller positive exponential constant. Thus there exist `c_R,C_R>0` with

```text
r_(L,R)
 <= C_R exp(-c_R Phi(L)).
```

No RH-scale zero information is used. This is the ordinary unconditional PNT remainder resulting from the classical zero-free region and zero-density theory near `Re(s)=1`.

## Quantitative frequency barrier

Insert the preceding estimate into `PL-061`:

```text
||W_(L,R,N)||
 <= A_R [
      C_R exp(log N-c_R Phi(L))
      + exp(-L)(1+log(1+N))
    ].
```

If

```text
log N(L)=o(Phi(L)),
```

then the first term tends to zero. Since

```text
Phi(L)=o(L),
```

the second term tends to zero as well. This proves the first boxed collapse statement.

The argument gives a slightly stronger fixed-margin version: for any chosen `eta<c_R`,

```text
log N(L) <= eta Phi(L)
```

forces

```text
N(L) r_(L,R)
 <= C_R exp(-(c_R-eta)Phi(L))
 ->0.
```

Thus any full-band construction that is to evade the established norm-collapse estimate must enter at least a Vinogradov--Korobov inverse-error frequency scale. A robust way to state the necessary surviving regime is

```text
log N(L) not=o(Phi(L));
```

with a fixed quantitative margin one needs `N` of size at least `exp(c Phi(L))` for some positive constant allowed by the PNT bound.

This is a **lower barrier on candidate frequency growth**, not an assertion that a nontrivial limit exists at that scale. The actual quantity controlling the transition in `PL-060`--`PL-061` remains `N r_(L,R)`, and an upper bound for `r_(L,R)` cannot determine where that product first becomes order one.

## Moving-Sobolev consequence

`PL-060` proves norm collapse for the already-centered residual whenever

```text
s_L log(1/r_(L,R)) -> infinity.
```

The PNT estimate gives

```text
log(1/r_(L,R))
 >= c_R Phi(L)-O_R(1).
```

Therefore the sufficient condition

```text
s_L Phi(L) -> infinity
```

implies the `PL-060` hypothesis. This rules out, for example, all moving Sobolev orders of the form

```text
s_L=L^(-alpha)
```

with `alpha<3/5` (and the corresponding logarithmic margins), even though `s_L->0`.

Again the endpoint scale

```text
s_L about (log L)^(1/5)/L^(3/5)
```

is not resolved. The estimate only says that regularity decaying asymptotically more slowly than this still averages the completed prime discrepancy strongly enough to kill the candidate norm signal.

## Relation to the exponent lattice

The fixed-ratio shell in `PL-059`--`PL-061` samples the prime-power axis skeleton

```text
v(n)=m e_p,

<v(n),(log q)_q>
approximately 2L.
```

The PNT pole cancellation replaces the first-order atomic mass of these axis points by its continuum density. The residual quantity `r_(L,R)` measures how accurately the rational-prime axis staircase imitates that continuum on the energy shell. The current finding says that unconditional Vinogradov--Korobov cancellation is already strong enough that **every boundary Fourier band growing below an exponential of `L^(3/5)/(log L)^(1/5)` still sees only the homogenized zero limit after completion**.

This is therefore a quantitative obstruction to extracting new RH information from slowly growing harmonic resolution of the prime-exponent boundary. It does not turn the PNT remainder itself into a spectral mechanism.

## Matched-control audit

The new barrier is not rational-prime-specific in the sense required for a positive `prime_lattice` mechanism. Broucke's 2026 zero-free-region/PNT-remainder theory applies to broad classes of Beurling zeta functions and constructs Beurling systems with zeros on prescribed zero-free contours together with PNT-error oscillations showing the resulting transfer bounds are close to sharp (`SOURCES.md` 61).

Therefore the logical chain

```text
zero-free region near Re(s)=1
 -> quantitative PNT remainder
 -> collapse of bands with N r ->0
```

persists in matched generalized-prime settings under corresponding analytic hypotheses. The exact ordinary-integer staircase lower bound of `PL-061` remains a separate rational-integer feature, but the Vinogradov--Korobov **upper** bound used here supplies no new rational-prime rigidity and cannot by itself single out `Re(s)=1/2`.

## Analytic-continuation boundary

There is no continuation of the Euler product in this derivation. The full completed Weil form in `PL-061` is already the analytically continued explicit-formula object. The current step uses only an unconditional estimate for the finite Chebyshev function `psi(x)` on large real `x`.

The literature proof of that PNT remainder uses zero-free information for zeta near `Re(s)=1`; that input is classical and strictly weaker than RH. It is used here only to quantify `r_(L,R)`, not to identify or insert nontrivial zeros into the localized operator.

## Prior-art and novelty audit

The number-theoretic scale itself is prior art:

- Johnston derives the `3/5` Vinogradov--Korobov PNT exponent from a generic zero-free region plus zero-density input (`SOURCES.md` 60);
- Bellotti sharpens the density estimate near unity and obtains the optimal exponential PNT remainder associated with the available Vinogradov--Korobov boundary (`SOURCES.md` 59);
- Broucke develops a modern general zero-free/PNT transfer and near-sharp Beurling controls (`SOURCES.md` 61).

A targeted audit around Weil quadratic forms, localized Weil operators, moving/Galerkin boundary cutoffs, PNT remainders, Vinogradov--Korobov scales, and boundary Sobolev regularization found no source stating the specific insertion of this remainder into the `PL-060`--`PL-061` operator bounds. **No novelty is claimed for the PNT estimate or its `3/5` exponent.** The stored result is an exact line-specific consequence that closes a large previously unquantified portion of the accepted mesoscopic search space.

The claim would fail if either:

1. the cited unconditional PNT remainder did not imply a uniform `exp(-c_R Phi(L))` relative bound on the fixed-ratio shell; or
2. the `PL-060`/`PL-061` moving-band and moving-Sobolev inequalities were incorrect.

Item 1 follows directly from `log x=2L+O_R(1)` on the shell; item 2 is the existing canonical dependency. There is no extra probabilistic, numerical, or zero-sum assumption.

## Consequence for the research line

The accepted mesoscopic-boundary target can now be narrowed from arbitrary growing frequency/vanishing regularity to the genuinely high-resolution regime

```text
Dirichlet bands:
    log N(L) at least of Vinogradov--Korobov scale
    Phi(L)=L^(3/5)/(log L)^(1/5),
    with the exact transition still governed by N r_(L,R);

moving Sobolev:
    s_L no larger than order 1/Phi(L)
    if a residual norm signal is to survive the current no-go.
```

Combined with `PL-061`, the first unresolved fixed-depth band is therefore not a polynomial or mildly stretched-frequency window. It is the exact atomic discrepancy regime at or beyond the inverse PNT error scale. Any future positive mechanism there must still pass the Beurling/control audit and must produce structure beyond the already-known zero-free-region/PNT cancellation.

## Sources

- `SOURCES.md` 59 — Chiara Bellotti, current sharp zero-density/PNT remainder near the Vinogradov--Korobov boundary.
- `SOURCES.md` 60 — Daniel R. Johnston, explicit generic zero-free-region to PNT-error transfer and the `3/5` scale.
- `SOURCES.md` 61 — Frederik Broucke, 2026 zero-free/PNT transfer and Beurling near-sharp controls.
