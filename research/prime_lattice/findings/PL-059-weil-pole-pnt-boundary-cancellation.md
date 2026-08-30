# PL-059 — The zeta pole canonically cancels the universal PNT boundary mode

## Claim

`PL-051` isolates the naturally normalized fixed-depth boundary operator of the non-archimedean Weil term,

```text
B_(L,R)=exp(-L) J_(L,R)^* K_L J_(L,R),
```

and proves the strong limit

```text
B_(L,R) -> B_R

B_R = [ 0    P_R ]
      [ P_R  0   ],

P_R=|h_R><h_R|,
h_R(a)=exp(-a/2).
```

Taken by itself, the prime-power sector therefore has a nonzero universal rank-one PNT boundary mode. In the **completed Weil form**, however, that mode is not a genuine first-order boundary term: the pole contribution cancels it canonically and with the correct sign.

For a test function `v` and

```text
phi=v*v_tilde,
v_tilde(x)=conjugate(v(-x)),
```

the pole part of the completed explicit formula is

```text
Q_pole(v)
 = integral_R phi(x)(exp(x/2)+exp(-x/2)) dx.
```

For fixed `R>0`, let `E_(L,R)` denote the bounded self-adjoint operator on `H_R direct_sum H_R`, `H_R=L^2(0,R)`, whose quadratic form is

```text
<(f,g),E_(L,R)(f,g)>
 = exp(-L) Q_pole(J_(L,R)(f,g)).
```

Then

```text
boxed:
||E_(L,R)-B_R|| = O_R(exp(-L)).
```

Consequently the canonically completed bounded pole-minus-prime boundary sector

```text
C_(L,R)=E_(L,R)-B_(L,R)
```

satisfies

```text
boxed:
C_(L,R) -> 0 strongly.
```

The cancellation is only strong, not uniform in the unit sphere. Since `E_(L,R)` is finite rank for every `L`, it disappears in the Calkin algebra, so `PL-053` gives

```text
boxed:
liminf_(L->infinity) ||C_(L,R)||_ess
 >= 1-exp(-R) > 0.
```

Thus the completed zeta pole supplies exactly the PNT counterterm that the boundary analysis would otherwise have had to insert by hand, but it **does not remove the prime-log Kronecker recurrence defect**. Completion converts the `PL-051` first-order PNT mode into a canonical centered family whose fixed vectors tend to zero while its essential norm remains order one.

On the fixed smooth boundary core there is a corresponding statement for the whole completed Weil form. For every fixed

```text
(f,g) in C_c^infinity(0,R) direct_sum C_c^infinity(0,R),
```

the remaining archimedean and scalar terms are `O_(f,g,R)(1)` as `L->infinity`. Hence

```text
boxed:
exp(-L) Q_W^L(J_(L,R)(f,g)) -> 0.
```

This last assertion is deliberately a **form statement on fixed smooth profiles**, not an operator-norm statement for the full localized Weil operator: the archimedean sector has logarithmic frequency growth and belongs naturally to the form-domain framework used in localized Weil theory.

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION`.

The result closes one part of the mesoscopic boundary search: there is no need to invent a canonical subtraction of the universal PNT rank-one mode. The completed explicit formula already provides it through the zeta pole. What remains open is whether the **already-centered** completed residual admits a moving frequency/regularity topology in which the essential prime recurrence is controlled without erasing all rational-prime-specific information.

## Exact pole factorization

For real `s`, define the two Laplace functionals

```text
V_s(v)=integral_R v(x) exp(s x) dx.
```

The convolution and involution give

```text
integral_R (v*v_tilde)(x) exp(s x) dx
 = V_s(v) conjugate(V_(-s)(v)).
```

Taking `s=+1/2` and `s=-1/2` therefore yields the exact identity

```text
Q_pole(v)
 = V_(1/2)(v) conjugate(V_(-1/2)(v))
   + V_(-1/2)(v) conjugate(V_(1/2)(v))

 = 2 Re(
       V_(1/2)(v) conjugate(V_(-1/2)(v))
     ).
```

This factorization is the boundary form of the two elementary pole terms in the completed explicit formula. No Euler product is involved.

## Endpoint expansion

Use the endpoint embedding of `PL-051`:

```text
v(-L+a)=f(a),
v( L-b)=g(b),
0<a,b<R,
```

and zero elsewhere. Put

```text
F_+ = integral_0^R f(a) exp(+a/2) da,
F_- = integral_0^R f(a) exp(-a/2) da,

G_+ = integral_0^R g(b) exp(+b/2) db,
G_- = integral_0^R g(b) exp(-b/2) db.
```

A direct change of variables gives

```text
V_(1/2)(v)
 = exp(-L/2) F_+ + exp(+L/2) G_-,

V_(-1/2)(v)
 = exp(+L/2) F_- + exp(-L/2) G_+.
```

Substitution into the pole factorization gives the exact normalized quadratic form

```text
exp(-L) Q_pole(v)

 = 2 Re(G_- conjugate(F_-))

   + 2 exp(-L)
       Re(
          F_+ conjugate(F_-)
          + G_- conjugate(G_+)
       )

   + 2 exp(-2L)
       Re(F_+ conjugate(G_+)).
```

All four functionals `F_+`, `F_-`, `G_+`, `G_-` are bounded on the fixed space `H_R`. Hence the second line is an operator of norm `O_R(exp(-L))` and the last line is `O_R(exp(-2L))`.

The leading form is exactly the `PL-051` rank-one cross-end form. Indeed, with

```text
h_R(a)=exp(-a/2),
P_R=|h_R><h_R|,
```

the operator

```text
B_R=[ [0,P_R], [P_R,0] ]
```

has quadratic form

```text
2 Re(G_- conjugate(F_-)).
```

Therefore

```text
||E_(L,R)-B_R||=O_R(exp(-L)).
```

The equality of the profile and normalization is not imposed after the fact: both sides independently produce the same `exp(-a/2)` boundary vector because the pole residue contributes `exp(+x/2)`/`exp(-x/2)` while the PNT shell at `log n=2L-delta` contributes `n^(-1/2) dn ~ exp(L)exp(-delta/2)d delta`.

## Canonical centering of the prime boundary operator

`PL-051` proves

```text
B_(L,R) -> B_R
```

strongly. Since `E_(L,R)->B_R` in operator norm,

```text
C_(L,R)=E_(L,R)-B_(L,R) ->0
```

strongly.

This changes the interpretation of the earlier boundary model. The nonzero `+/- (1-exp(-R))` eigenvalues of `B_R` are genuine for the isolated positive prime operator, but they are not a first-order spectrum of the **completed** Weil form. The pole sector supplies their opposite contribution before any further renormalization.

Equivalently, the centered residual from `PL-052`,

```text
B_(L,R)-B_R,
```

is not merely a convenient PNT subtraction. Up to a norm-vanishing finite-rank error, it is the negative of the canonical pole-minus-prime sector:

```text
C_(L,R)
 = -(B_(L,R)-B_R)
   + (E_(L,R)-B_R).
```

Thus the completed explicit formula itself selects the same centering that the boundary asymptotics discovered.

## The essential recurrence survives completion

For every finite `L`, `E_(L,R)` is finite rank: its range is generated by the finitely many fixed endpoint vectors representing the four bounded Laplace functionals above. Therefore

```text
||C_(L,R)||_ess
 = ||B_(L,R)||_ess.
```

Because `B_R` is rank two,

```text
||B_(L,R)||_ess
 = ||B_(L,R)-B_R||_ess.
```

`PL-053` proves

```text
liminf_(L->infinity)
 ||B_(L,R)-B_R||_ess
 >= 1-exp(-R).
```

Combining the identities gives

```text
boxed:
liminf_(L->infinity)
 ||C_(L,R)||_ess
 >= 1-exp(-R).
```

Hence the full completion performs a mathematically natural centering but cannot turn the raw boundary residual into a compact, Schatten, or norm-small family. The weakly-null recurrent states from `PL-052`--`PL-053` are invisible to the finite-rank pole correction for exactly the same reason that they survive every compact counterterm.

This is a useful separation:

```text
PNT main boundary mode
    -> canceled canonically by the zeta pole;

high-frequency prime-log recurrence
    -> survives in the Calkin quotient;

archimedean frequency penalty
    -> remains outside this bounded-sector cancellation
       and must be treated at the form/domain level.
```

## Remaining completed-Weil terms on fixed smooth profiles

For completeness, consider the standard remaining terms of the completed Weil functional. Besides the pole term and the two von-Mangoldt sums, there is a scalar multiple of

```text
phi(0)=||v||_2^2
```

and the archimedean integral of the form

```text
integral_0^infinity
  {phi(x)+phi(-x)-2 exp(-x/2) phi(0)}
  k_arch(x) dx,
```

with

```text
k_arch(x)=exp(x/2)/(exp(x)-exp(-x)).
```

For a fixed smooth endpoint pair `(f,g)`:

- `phi(0)=||f||_2^2+||g||_2^2` is independent of `L`;
- same-end autocorrelation pieces live at `|x|<R` and are independent of the absolute endpoint position;
- cross-end pieces live near `|x|=2L+O_R(1)`, where `k_arch(x)=O(exp(-x/2))`, so their archimedean contribution is `O_(f,g,R)(exp(-L))`;
- near `x=0`, the subtraction by `2 exp(-x/2)phi(0)` cancels the kernel singularity on the smooth core.

Thus the scalar and archimedean pieces are `O_(f,g,R)(1)`. After multiplication by the boundary normalization `exp(-L)` they vanish. Combining this with the pole-prime strong cancellation gives

```text
exp(-L) Q_W^L(J_(L,R)(f,g)) ->0
```

for each fixed smooth boundary profile.

No stronger uniform statement is inferred. High boundary frequencies are precisely where `PL-052`--`PL-053` find nonuniform prime recurrence, while the archimedean form itself grows logarithmically in frequency. Any joint limit in which the frequency scale moves with `L` requires a separate analysis.

## Exponent-lattice interpretation

At the outer boundary scale, the non-archimedean term samples only prime-power axis vectors

```text
v(n)=m e_p
```

with energy

```text
<v(n),(log q)_q>
 = m log p
 = 2L-delta.
```

The PNT compresses their weighted shell to the universal deficit density

```text
exp(-delta/2)d delta,
```

which produces the `PL-051` rank-one Hankel profile `h_R(a)=exp(-a/2)`.

The present result shows that completion already contains the dual first-order object needed to remove that density: the zeta pole has exactly the same endpoint Laplace profile and opposite sign in the Weil form. Thus the first boundary scale is not an independent prime-lattice spectral invariant. It is the familiar residue-versus-prime-main-term balance of the explicit formula expressed in boundary coordinates.

What survives is the topology-sensitive discrepancy between the atomic prime-power shell and its continuum PNT approximation. The prime logarithms retain enough coherent recurrence that this discrepancy remains macroscopic in essential norm even after the universal residue/PNT component has been canceled.

## Analytic-continuation boundary

Everything here is formulated on the **completed Weil explicit-formula side**. The pole term, archimedean term, and finite prime-power sum at fixed `L` are already parts of the analytically continued/completed object. No Euler product is evaluated or formally continued in the critical strip.

The PNT is used only through the already-audited boundary-shell limit in `PL-051`; the essential-norm lower bound is the exact recurrent-state argument of `PL-053`. The new calculation is the exact factorization and endpoint asymptotic of the pole term.

## Prior-art and novelty audit

The ingredients are classical or already persisted:

- Weil's explicit formula and Bombieri's treatment of the Weil quadratic functional supply the completed pole/prime/archimedean decomposition already anchored in `SOURCES.md`.
- Suzuki's localized Weil form provides current operator/form-domain context for finite apertures and the full completed object.
- `PL-051` proves the universal rank-one PNT boundary limit of the isolated prime operator.
- `PL-052`--`PL-053` prove that the centered prime boundary residual remains order one in norm and in the Calkin algebra.

The cancellation between the pole residue and the PNT main term is a classical structural feature of explicit formulas. The boundary-operator calculation above is a derived specialization of that balance, not a novelty claim. A targeted audit did not supply a stronger theorem that would turn this cancellation into an RH localization mechanism.

The same matched-control warning applies as before: a generalized-prime explicit formula with a matching simple pole and the same PNT main density will exhibit the analogous first-order cancellation. Therefore the cancellation is **canonical but not rational-prime-specific rigidity**.

## Falsification and boundary tests

The core claim is reduced to independently auditable steps:

1. the completed Weil pole term is the displayed integral against `exp(x/2)+exp(-x/2)`;
2. the convolution involution gives `Q_pole=2 Re(V_(1/2) conjugate(V_(-1/2)))`;
3. the endpoint embedding gives the two exact Laplace expansions above;
4. their leading normalized cross term is precisely the quadratic form of `B_R`;
5. `PL-051` gives `B_(L,R)->B_R` strongly;
6. finite rank of `E_(L,R)` plus `PL-053` preserves the essential-norm lower bound.

Failure of any item 1--4 would invalidate the new cancellation. Items 5--6 are existing canonical dependencies. The smooth-core statement would need narrowing if the localized archimedean term failed to remain `O(1)` for a fixed translated endpoint profile, but it is not used for the stronger bounded pole-prime Calkin conclusion.

## Consequence for the research line

The accepted mesoscopic boundary question is now more constrained. The first-order ledger is

```text
isolated prime sector:
    exp(-L) J^* K_L J
        -> B_R strongly;

completed pole sector:
    exp(-L) J^* Q_pole J
        -> B_R in norm;

completed pole-minus-prime sector:
    C_(L,R)
        -> 0 strongly
        but liminf ||C_(L,R)||_ess >= 1-exp(-R).
```

Therefore a future mesoscopic construction should **not** search for an ad hoc PNT rank-one counterterm: completion has already fixed it. The unresolved target is a simultaneously moving frequency/regularity topology for this canonically centered completed residual, likely one that treats the archimedean logarithmic frequency cost and the atomic prime-log recurrence on the same scale. It must still survive matched generalized-prime controls and must not obtain zero sensitivity merely by inserting the classical explicit formula as a smoothing identity.