# PL-056 — The critical Sobolev endpoint has a universal `det_2` limit and only a geometric weak-trace residue

## Claim

The fixed Sobolev boundary regularization from `PL-055` has no hidden zeta-sensitive rescue at its numerically suggestive endpoint `s=1/2`.

Fix a boundary depth `R>0` and use the normalized fixed-depth Weil operators from `PL-051`--`PL-055`:

```text
B_(L,R) -> B_R strongly,

B_R = [ 0    P_R ]
      [ P_R  0   ],

P_R=|h_R><h_R|,
h_R(a)=exp(-a/2),
```

on `H_R direct_sum H_R`, with `H_R=L^2(0,R)`. Let

```text
Q_R=(I+Delta_D)^(-1/4),
S_R=Q_R direct_sum Q_R,

A_(L,R)=S_R B_(L,R) S_R,
A_R=S_R B_R S_R,
```

where `Delta_D` is the nonnegative Dirichlet Laplacian on `(0,R)`.

Then the general Schatten theorem already proved in `PL-055`, specialized to `s=1/2` and `q=2`, gives

```text
boxed:
||A_(L,R)-A_R||_(S_2) -> 0.
```

Therefore the canonical Hilbert--Schmidt regularized Fredholm determinant converges locally uniformly in `z`:

```text
boxed:
det_2(I-z A_(L,R))
    -> det_2(I-z A_R)
     = 1-z^2 c_R^2,

c_R=||Q_R h_R||_2^2.
```

The limiting `det_2` is the same elementary rank-two determinant of the universal PNT boundary mode that appears above the trace-class endpoint. Thus choosing the critical smoothing order exactly `s=1/2` and replacing the ordinary Fredholm determinant by `det_2` does **not** recover a Riemann-zero divisor.

There is also a sharp channel-level control at this endpoint. For the full-reflection atom `H_R` from `PL-054`,

```text
(H_R f)(a)=f(R-a),
```

one has

```text
Q_R H_R Q_R
 = H_R (I+Delta_D)^(-1/2).
```

In the Dirichlet basis

```text
e_k(a)=sqrt(2/R) sin(k pi a/R),
```

its eigenvalues are

```text
lambda_k
 = (-1)^(k+1)
   (1+(k pi/R)^2)^(-1/2).
```

Hence the singular values satisfy

```text
mu_k ~ R/(pi k).
```

The critical channel is therefore in every `S_q`, `q>1`, but not in `S_1`; it lies exactly at weak trace-class scale. Its logarithmic singular-value residue is purely geometric:

```text
boxed:
lim_(N->infinity)
  (1/log N) sum_(k<=N) mu_k
 = R/pi.
```

For the natural two-end block with real scalar coefficient `a`,

```text
D_(a,R)
 = a [ 0              Q_R H_R Q_R ]
     [ Q_R H_R Q_R    0             ],
```

the singular values occur twice and therefore

```text
boxed:
lim_(N->infinity)
  (1/log N) sum_(j<=N) s_j(D_(a,R))
 = 2 |a| R/pi.
```

The positive and negative eigenvalues occur in exact `+/-` pairs, so every signed trace obtained from this logarithmic weak-trace asymptotic cancels to zero. The surviving absolute residue is only the one-dimensional Weyl coefficient `2|a|R/pi`.

Moreover `D_(a,R)` is Hilbert--Schmidt and its regularized determinant is explicit:

```text
boxed:
det_2(I-z D_(a,R))
 = product_(k>=1)
     [1-a^2 z^2/(1+(k pi/R)^2)]

 = sinh(R sqrt(1-a^2 z^2))
   / [sqrt(1-a^2 z^2) sinh R].
```

The right-hand side is understood by its entire power-series continuation at `1-a^2 z^2=0`. For `a!=0` its zeros are the elementary real ladder

```text
z = +/- |a|^(-1)
        sqrt(1+(k pi/R)^2),

k>=1.
```

Thus even the maximally singular atomic reflection channel at the critical Sobolev endpoint has only ordinary interval spectral data after the canonical `det_2` regularization.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION` and `DECISIVE-NEGATIVE` for the route

```text
fixed critical Sobolev smoothing s=1/2
+ standard Hilbert--Schmidt det_2 or its static weak-trace residue
    -> zeta-specific limiting determinant / spectral invariant.
```

The result is deliberately scoped. It does **not** rule out an `L`-dependent order `s(L)->1/2`, a growing depth `R(L)`, a moving boundary-frequency cutoff, or another renormalization whose definition genuinely couples to the large-`L` arithmetic shell. Those are no longer fixed endpoint invariants and remain the mesoscopic question in `CLUE-mesoscopic-weil-boundary-topology`.

## The full smoothed boundary family converges in Hilbert--Schmidt norm

`PL-055` proved the general implication

```text
s > 1/(2q)
    =>
||S_(s,R)(B_(L,R)-B_R)S_(s,R)||_(S_q) -> 0.
```

At the endpoint relevant here,

```text
s=1/2,
q=2,
```

and the strict inequality is

```text
1/2 > 1/4.
```

Thus no endpoint argument or interpolation is required:

```text
||A_(L,R)-A_R||_(S_2) ->0
```

is already an exact specialization of the established theorem.

The standard second regularized determinant `det_2(I+T)` is continuous under `S_2` convergence, locally uniformly in any scalar spectral parameter multiplying `T`. This is classical trace-ideal theory; the standard regularized-determinant framework is already anchored in `research/prime_lattice/SOURCES.md` by Britz--Carey--Gesztesy--Nichols--Sukochev--Zanin and Hartmann--Lesch for `PL-009`.

Therefore

```text
det_2(I-z A_(L,R))
 -> det_2(I-z A_R).
```

No number-theoretic estimate beyond the strong PNT boundary limit and the fixed-smoothing Schatten upgrade of `PL-055` enters this step.

## The endpoint `det_2` limit is rank two and universal

Set

```text
u_R=Q_R h_R,
c_R=||u_R||_2^2.
```

Since

```text
Q_R P_R Q_R=|u_R><u_R|,
```

we have

```text
A_R
 = [ 0             |u_R><u_R| ]
   [ |u_R><u_R|    0            ].
```

Its only nonzero eigenvalues are

```text
+c_R,
-c_R.
```

Hence the two regularized eigenvalue factors cancel their exponential counterterms:

```text
[(1-z c_R) exp(z c_R)]
[(1+z c_R) exp(-z c_R)]
 = 1-z^2 c_R^2.
```

This proves

```text
det_2(I-z A_R)=1-z^2 c_R^2.
```

The result depends on the arithmetic input only through the first-order PNT homogenization already shown to be universal in `PL-051`. Any matched generalized-prime system with the same fixed-depth strong boundary law and the same fixed compact sandwich has the same type of endpoint limit.

Thus the numerical equality between the Sobolev order `1/2` and the zeta critical abscissa does not create a new critical-line mechanism. At this topology, the regularized determinant has already forgotten the high-frequency prime-log recurrence before its limit is taken.

## Exact critical spectrum of the full-reflection atom

The strongest local test comes from the `delta=R` channel of `PL-054`. On the Dirichlet basis,

```text
Delta_D e_k=(k pi/R)^2 e_k,
H_R e_k=(-1)^(k+1)e_k.
```

Since `H_R` commutes with `Delta_D`, it commutes with every spectral function of `Delta_D`. At `s=1/2`,

```text
Q_R=(I+Delta_D)^(-1/4),
```

so

```text
Q_R H_R Q_R
 = H_R Q_R^2
 = H_R(I+Delta_D)^(-1/2).
```

Therefore

```text
(Q_R H_R Q_R)e_k
 = (-1)^(k+1)
   (1+(k pi/R)^2)^(-1/2)e_k.
```

The magnitude sequence is

```text
mu_k=(1+(k pi/R)^2)^(-1/2)
    = R/(pi k)+O_R(k^(-3)).
```

Consequently

```text
sum_k mu_k^q < infinity
    <=> q>1,
```

while

```text
sum_(k<=N) mu_k
 = (R/pi) log N + O_R(1).
```

This supplies the displayed weak-trace residue directly; no abstract pseudodifferential trace theorem is needed.

The coefficient `R/pi` is the ordinary one-dimensional Weyl coefficient of the interval. It contains no prime, prime-power, Möbius, or zero data. Multiplying the channel by an arithmetic scalar changes only the overall factor `|a|`.

## Exact `det_2` of the critical atomic two-end block

For the two-end block `D_(a,R)`, each `k` contributes the eigenvalue pair

```text
+a mu_k,
-a mu_k.
```

The pair contribution to `det_2(I-zD_(a,R))` is

```text
(1-z a mu_k) exp(z a mu_k)
(1+z a mu_k) exp(-z a mu_k)
 = 1-z^2 a^2 mu_k^2.
```

Hence

```text
det_2(I-zD_(a,R))
 = product_(k>=1)
   [1-a^2 z^2/(1+(k pi/R)^2)].
```

Rewrite each factor as

```text
[(k pi/R)^2 + 1-a^2 z^2]
/
[(k pi/R)^2 + 1].
```

Euler's classical product

```text
sinh x / x
 = product_(k>=1)
   [1+x^2/(pi^2 k^2)]
```

gives the closed form

```text
sinh(R sqrt(1-a^2 z^2))
/
[sqrt(1-a^2 z^2) sinh R].
```

The square root introduces no actual branch ambiguity because `sinh(R sqrt(w))/sqrt(w)` is an entire function of `w`. Its non-removable zeros occur at

```text
R sqrt(1-a^2 z^2)=i pi k,
k>=1,
```

which gives the real ladder stated in the claim.

This is a useful adversarial control: the same critical regularization that looks potentially special because it lies exactly at weak trace-class scale already produces a completely explicit non-zeta determinant on the canonical reflection atom.

## Exponent-lattice and matched-control interpretation

The atomic channel corresponds to one exponent-lattice axis point

```text
v(q)=k e_p,
q=p^k,
```

at a fixed boundary deficit. The reflection operator itself depends only on that deficit and on the interval geometry; the rational-prime origin survives only in the scalar coefficient and in where the atom occurs as `L` varies.

Likewise, the full `S_2` limit depends only on the universal PNT boundary measure from `PL-051`. A Beurling or generalized-frequency model with a matched first-order shell law and the same atomic compression exhibits the same endpoint `det_2` collapse and the same reflection-channel weak residue.

Therefore neither invariant passes the line's matched-control test. The exact rational-prime norm map is not distinguished by holding the smoothing at this static endpoint.

## Analytic-continuation boundary

No Euler product or Dirichlet series is analytically continued in this derivation. The operators are built from the already-completed Weil explicit-formula side, and the only number-theoretic input is the fixed-depth PNT boundary limit persisted in `PL-051`.

The failure is therefore topological/operator-theoretic rather than an artifact of remaining in `Re(s)>1`.

## Prior-art and novelty audit

All ingredients used in the endpoint computation are classical:

- `S_2` continuity of the second regularized Fredholm determinant is standard trace-ideal theory and is already anchored for this line by the regularized-determinant sources supporting `PL-009`;
- the Dirichlet spectrum on an interval and its `k^(-1)` critical singular-value law are elementary one-dimensional Weyl asymptotics;
- logarithmic weak-trace residues for `1/k` singular-value sequences are standard singular-trace territory;
- the hyperbolic-sine product is Euler's classical product;
- the delta-Hankel/reflection channel itself was already classicalized in `PL-054`.

A targeted prior-art check across weak trace ideals, Dixmier/Connes trace formulas, Hilbert--Schmidt regularized determinants, and one-dimensional Laplacian determinants confirmed that these endpoint technologies are standard. No novelty is claimed for them. The durable content is their exact specialization to the `PL-051`--`PL-055` Weil boundary family and the resulting closure of the static critical-endpoint escape.

## Falsification and boundary tests

The claim reduces to independently checkable steps:

1. `PL-055` gives `S_2` convergence at `s=1/2` because `1/2>1/4`;
2. `det_2` is continuous under `S_2` convergence;
3. `A_R` has only the eigenvalues `+/-c_R` away from zero;
4. `H_R` commutes with the Dirichlet Laplacian and has alternating eigenvalues `+/-1`;
5. the critical smoothed reflection singular values are exactly `(1+(k pi/R)^2)^(-1/2)`;
6. their partial sums have coefficient `(R/pi)log N`;
7. the paired `det_2` product reduces to the displayed hyperbolic-sine quotient.

Failure of any item falsifies the corresponding conclusion. The argument does not apply uniformly to a family of smoothing operators that changes with `L`; loss of fixed compactness is precisely the surviving mesoscopic direction rather than a hidden assumption of this no-go.

## Consequence for the research line

The fixed-depth smoothing ledger is now sharper:

```text
fixed s>1/2
    -> trace-class convergence
    -> ordinary Fredholm determinant is universal          [PL-055]

fixed s=1/2
    -> Hilbert--Schmidt convergence
    -> det_2 limit is the same universal rank-two PNT mode [PL-056]
    -> canonical reflection atom is weak trace class only
       with geometric residue and an elementary det_2 ladder

raw high-frequency unit sphere
    -> prime-log recurrence survives in norm/Calkin        [PL-052, PL-053]
```

So merely parking the Sobolev regularization on the apparent critical endpoint does not interpolate between PNT homogenization and zeta-zero structure. A surviving construction must let the topology itself move with `L` in a canonically forced way and must retain a rational-prime-specific residual that fails the Beurling controls. That is the remaining content of the accepted mesoscopic clue.