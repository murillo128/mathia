# PL-053 — Prime-log recurrence survives the Calkin quotient of the fixed-depth Weil boundary model

## Claim

`PL-052` proves that the fixed-depth boundary homogenization of the localized Weil prime operator is strong but not norm convergent. The obstruction is stronger: it survives **modulo all compact operators**.

Fix `R>0`. With the notation of `PL-051`--`PL-052`, let

```text
B_(L,R)
 = exp(-L) J_(L,R)^* K_L J_(L,R)
```

on

```text
H_R direct_sum H_R,
H_R=L^2(0,R),
```

and let

```text
B_R = [ 0    P_R ]
      [ P_R  0   ],

P_R=|h_R><h_R|,
h_R(a)=exp(-a/2).
```

Then

```text
boxed:
liminf_(L->infinity)
  ||B_(L,R)-B_R||_ess
 >= 1-exp(-R) > 0,
```

where `||.||_ess` is the essential norm, equivalently the norm in the Calkin algebra.

Consequently, for **every** family of compact counterterms `C_(L,R)`, even if `C_(L,R)` depends on `L`,

```text
liminf_(L->infinity)
 ||B_(L,R)-B_R-C_(L,R)||
 >= 1-exp(-R).
```

In particular, for all sufficiently large `L`, the centered boundary residual

```text
B_(L,R)-B_R
```

is noncompact and therefore belongs to no finite Schatten class `S_q`, including `S_1`.

The same obstruction survives the ordinary relative-resolvent repair. For every nonreal `z`,

```text
(B_(L,R)-z)^(-1) - (B_R-z)^(-1)
```

is compact, or belongs to any fixed Schatten ideal `S_q`, **if and only if** `B_(L,R)-B_R` does. Hence for all sufficiently large `L` this relative resolvent difference is noncompact and lies in no finite `S_q`, including trace class.

Thus the escape route left open after `PL-050`--`PL-052`,

```text
subtract the universal PNT boundary layer
+ add a compact / Schatten counterterm
+ obtain a norm-small or trace-class zeta-sensitive residual,
```

fails already at fixed boundary depth. The same high-frequency prime-log recurrence used in `PL-052` is not merely a norm defect against the rank-one model: it gives a macroscopic **essential** defect that no compact renormalization or ordinary bounded-pair resolvent comparison can remove.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION`, and `DECISIVE-NEGATIVE` for compact/Schatten renormalization and relative-resolvent repair of the fixed-depth, naturally normalized prime boundary operator.

The claim does not exclude weaker distributional/Sobolev topologies, mesoscopic depths `R=R(L)`, nonlinear functions of the operator whose compactness properties are not boundedly equivalent to the original difference, a canonically imposed external smoothing, threshold spectral flow, or the full Weil operator including archimedean and pole terms.

## Boundary cross block

`PL-051` writes the outer-shell cross-end block as

```text
(H_(mu_(L,R)) f)(b)
 = integral f(delta-b) d mu_(L,R)(delta),
```

with zero extension of `f` outside `(0,R)`, where

```text
mu_(L,R)
 = exp(-L)
   sum_(2L-2R<log n<2L)
     Lambda(n)/sqrt(n)
     delta_(2L-log n).
```

The PNT boundary limit is

```text
H_(mu_(L,R)) -> P_R
```

strongly, with

```text
(P_R f)(b)
 = exp(-b/2)
   integral_0^R exp(-a/2) f(a) da.
```

Since `P_R` has rank one, it is compact. Therefore it disappears in the Calkin quotient:

```text
||H_(mu_(L,R))-P_R||_ess
 = ||H_(mu_(L,R))||_ess.
```

The issue is whether the remaining atomic boundary operator itself becomes compact or compact-approximable as `L` grows. It does not.

## Weakly-null recurrent boundary states

Put

```text
N_R=1-exp(-R)
```

and use the unit boundary profiles from `PL-052`,

```text
f_xi(a)
 = N_R^(-1/2) exp(+i xi a) exp(-a/2),

g_xi(b)
 = N_R^(-1/2) exp(-i xi b) exp(-b/2).
```

As `|xi|->infinity`, both families converge weakly to zero in `L^2(0,R)`. Indeed, for any fixed `u in L^2(0,R)`, the product

```text
u(a) exp(-a/2)
```

belongs to `L^1(0,R)` by Cauchy--Schwarz, so the corresponding Fourier integral tends to zero by the Riemann--Lebesgue lemma.

For one shell atom at deficit `delta`, `PL-052` derives

```text
<g_xi,H_delta f_xi>
 = exp(i xi delta)
   exp(-delta/2) tau_R(delta)/N_R,
```

where

```text
tau_R(delta)
 = delta,       0<=delta<=R,
 = 2R-delta,   R<=delta<=2R.
```

At fixed `L` the shell contains only finitely many prime powers. Unique factorization makes the finitely many underlying prime logarithms rationally independent, hence Kronecker recurrence supplies a sequence

```text
xi_j -> infinity
```

such that the phases `exp(-i xi_j log p)` tend simultaneously to `1`. Therefore all shell atoms align up to the common phase `exp(i 2L xi_j)`, and

```text
lim_j
 |<g_(xi_j),H_(mu_(L,R)) f_(xi_j)>|

 = A_(L,R),
```

where

```text
A_(L,R)
 = integral_0^(2R)
     exp(-delta/2) tau_R(delta)/N_R
     d mu_(L,R)(delta).
```

All weights in this integral are nonnegative.

## Compact perturbations cannot remove the recurrent matrix element

Let `C` be any compact operator on `H_R`. Since `f_(xi_j)` is weakly null,

```text
||C f_(xi_j)||_2 -> 0.
```

The vectors `g_(xi_j)` remain unit vectors, hence

```text
<g_(xi_j),C f_(xi_j)> -> 0.
```

It follows that

```text
||H_(mu_(L,R))-C||
 >= limsup_j
    |<g_(xi_j),(H_(mu_(L,R))-C)f_(xi_j)>|
 = A_(L,R).
```

Taking the infimum over all compact `C` gives the exact lower bound

```text
boxed:
||H_(mu_(L,R))||_ess >= A_(L,R).
```

Because `P_R` is compact,

```text
||H_(mu_(L,R))-P_R||_ess
 >= A_(L,R).
```

This is the standard weakly-null test for essential norm specialized to the prime-log recurrent states. No compactness theorem specific to zeta is being invoked.

## Passing from the cross block to the two-end operator

Let

```text
D_(L,R)=B_(L,R)-B_R.
```

Let `Q_-` and `Q_+` be the orthogonal projections onto the left and right copies of `H_R`. Its off-diagonal compression is

```text
Q_+ D_(L,R) Q_-
 = H_(mu_(L,R))-P_R.
```

For any bounded operator `D`, compression cannot increase essential norm:

```text
||Q_+ D Q_-||_ess <= ||D||_ess,
```

because the compression of a compact operator is compact. Hence

```text
||D_(L,R)||_ess
 >= A_(L,R).
```

The small-lag diagonal blocks discussed in `PL-051` play no role in this lower bound.

## PNT gives the macroscopic Calkin gap

The fixed-width shell convergence from `PL-049`--`PL-052` is

```text
mu_(L,R)
 -> exp(-delta/2) 1_[0,2R](delta) d delta
```

weakly. The weight in `A_(L,R)` is continuous and compactly supported on `[0,2R]`, so

```text
A_(L,R)
 -> N_R^(-1)
    integral_0^(2R)
      tau_R(delta) exp(-delta) d delta.
```

As already evaluated in `PL-052`,

```text
integral_0^(2R)
 tau_R(delta) exp(-delta) d delta
 = (1-exp(-R))^2
 = N_R^2.
```

Therefore

```text
A_(L,R) -> N_R=1-exp(-R),
```

and so

```text
boxed:
liminf_(L->infinity)
 ||B_(L,R)-B_R||_ess
 >= 1-exp(-R).
```

The essential norm is invariant under compact perturbations. Thus, for any compact family `C_(L,R)`,

```text
||D_(L,R)-C_(L,R)||
 >= ||D_(L,R)||_ess,
```

which proves the counterterm statement.

Since every finite Schatten class is contained in the compact operators, positive essential norm also gives, for all sufficiently large `L`,

```text
D_(L,R) notin S_q
```

for every finite `q`, in particular `S_1`.

At the naive second-order scale the obstruction becomes even larger:

```text
|| exp(L) D_(L,R) ||_ess
 >= (1-exp(-R)+o(1)) exp(L).
```

Thus the failure of an `exp(L)`-centered operator limit recorded in `PL-052` persists after quotienting by compact operators.

## Resolvent comparison does not smooth this bounded pair

Set

```text
A=B_(L,R),
B=B_R,
D=A-B,
R_A(z)=(A-z)^(-1),
R_B(z)=(B-z)^(-1),
```

with `z` nonreal. Both `A` and `B` are bounded self-adjoint operators. The classical second resolvent identity gives

```text
R_A(z)-R_B(z)
 = -R_A(z) D R_B(z).
```

Conversely, multiplying by the bounded factors `A-z` and `B-z` gives the exact inverse relation

```text
D
 = -(A-z)(R_A(z)-R_B(z))(B-z).
```

Therefore for every two-sided operator ideal `J` in `B(H_R direct_sum H_R)`,

```text
boxed:
R_A(z)-R_B(z) in J
    <=>
D in J.
```

This applies in particular to the compact operators and every finite Schatten class `S_q`. The positive essential norm above therefore implies that, for all sufficiently large `L`,

```text
R_(B_(L,R))(z)-R_(B_R)(z)
```

is noncompact and belongs to no finite `S_q`. Ordinary relative-resolvent trace class, spectral-shift, or Fredholm-determinant machinery cannot be reached merely by replacing this bounded operator difference with its resolvent difference.

The Calkin gap also yields a quantitative resolvent gap. From the inverse relation and submultiplicativity of the quotient norm,

```text
||R_A(z)-R_B(z)||_ess
 >= ||D||_ess / (||A-z|| ||B-z||).
```

At `z=i`, `PL-046` gives `||A||<=2+o(1)` after the `exp(-L)` normalization, while `||B||=1-exp(-R)<=1`. Hence

```text
liminf_(L->infinity)
 ||(B_(L,R)-i)^(-1)-(B_R-i)^(-1)||_ess
 >= (1-exp(-R))/6 > 0.
```

The constant `1/6` is only a convenient coarse bound; the ideal-equivalence statement is the substantive point.

This argument is specific to the present **bounded** pair. For genuinely unbounded self-adjoint pairs, resolvent comparability can be strictly weaker than Schatten membership of an operator difference and is a classical subject of perturbation theory. The present calculation therefore closes a local escape in this boundary model rather than a general resolvent-comparable program.

## What this closes, and what it does not

This result closes a concrete trace/determinant repair suggested by the boundary program:

```text
PNT leading layer B_R
    -> subtract finite-rank universal term
    -> hope residual is compact / Schatten
    -> use trace, spectral shift, or Fredholm determinant.
```

The direct residual is not even compact. More generally, adding or subtracting arbitrary compact counterterms cannot make it norm-small, because the recurrent atomic shell remains visible in the Calkin algebra. For this bounded pair, replacing the operator difference by a relative resolvent difference also cannot improve ideal membership: the two differences are related by bounded invertible sandwiches in both directions.

This does **not** imply that no determinant or trace construction can ever be built from localized Weil data. A nonlinear functional calculus, an independently canonical smoothing operator, a weaker topology, a mesoscopic boundary scaling, or the full Weil operator including its archimedean and pole terms can change the mathematical problem and must be audited separately. The present claim is only about the natural fixed-depth boundary operator, compact/Schatten renormalizations of it, and the ordinary relative resolvent of this bounded pair.

The smooth-test zero expansion of `PL-052` is also unaffected. Fixed smooth probes deliberately suppress the high-frequency weakly-null states used here; after that smoothing the classical explicit formula recovers the zero divisor. The present obstruction says that this smoothing cannot be replaced by merely discarding compact operator structure or by taking the ordinary relative resolvent.

## Exponent-lattice interpretation

The fixed-depth boundary shell consists of prime-power axis points

```text
v(n)=k e_p
```

with energy deficit

```text
delta=2L-<v(n),(log p)_p>.
```

PNT averaging forgets the discrete axis labels and yields the rank-one continuum model `P_R`. The Calkin quotient does **not** complete that homogenization. High boundary frequency can still interrogate the exact primitive energies `log p`; finite Kronecker recurrence then coherently reassembles the atomic shell.

Thus two quotients forget different information:

```text
weak / fixed-profile limit
    -> sees only PNT shell density;

Calkin quotient
    -> removes finite-rank/compact structure
    -> still sees O(1) prime-log recurrent atomicity.
```

The relative resolvent adds no further information loss at the level of compact/Schatten ideals for this bounded pair, because it is ideal-equivalent to the same Calkin-visible difference.

The surviving essential defect is therefore a precise form of microscopic prime-frequency information, but it is not yet zeta-specific rigidity.

## Beurling and universality audit

The proof uses only

```text
1. positive atomic shell weights;
2. finitely many rationally independent primitive energies at each L;
3. the fixed-width PNT-type shell limit.
```

A matched generalized-prime or positive-frequency system with the same properties has the same essential-norm obstruction. Neither the zeta functional equation nor the Riemann zero divisor enters. The bounded-pair resolvent equivalence is purely functional analytic and therefore propagates this same matched-control obstruction automatically.

Accordingly, the result is a no-go statement, not an RH mechanism. The Calkin survival of atomic recurrence distinguishes weak homogenization from compact homogenization, but by itself it does not distinguish rational primes from suitably matched Beurling controls.

## Analytic-continuation boundary

No Euler product is used or analytically continued. At each finite `L`, the operator is the finite prime-power term extracted from the already-completed Weil explicit formula. The large-`L` input is the prime number theorem, and the essential-norm lower bound uses finite-dimensional Kronecker recurrence.

The obstruction therefore lives entirely on the completed explicit-formula side and does not arise from illegitimately transporting a `Re(s)>1` identity into the critical strip. The resolvent strengthening is an algebraic consequence of bounded operator theory and introduces no additional analytic continuation.

## Prior-art and novelty audit

The functional-analytic principles behind the proof are standard: compact operators map weakly convergent sequences to norm-convergent sequences, weakly-null test sequences are a classical way to lower-bound essential norm, Schatten classes are two-sided ideals, and the second resolvent identity is classical. Generic Calkin-algebra, finite-section boundary, and resolvent-comparable perturbation phenomena are standard operator theory.

The arithmetic inputs are also already anchored: `PL-045`/`PL-052` supply prime-log Kronecker recurrence, while `PL-049`--`PL-051` supply the PNT shell measure and fixed-depth boundary model. Modern resolvent-comparable perturbation theory treats the genuinely broader unbounded setting in which a Schatten resolvent difference need not come from a Schatten operator difference; that distinction does not apply to the present bounded pair because the second resolvent identity is invertible by bounded factors in both directions. A targeted literature audit did not identify any theorem that changes this elementary ideal-equivalence calculation.

No novelty claim is made. The durable contribution is the exact consequence for the concrete localized-Weil boundary family: the recurrent norm gap of `PL-052` remains macroscopic in the Calkin quotient, so neither a compact/Schatten counterterm nor an ordinary relative-resolvent replacement can expose a norm-small or trace-class second layer.

## Falsification and boundary tests

The claim reduces to eight checkable statements:

1. `f_xi` and `g_xi` are weakly null as `|xi|->infinity`;
2. the one-atom matrix element is the formula from `PL-052`;
3. finite rational-prime logarithms admit simultaneous recurrent phases;
4. compact operators send the recurrent `f_(xi_j)` to norm zero;
5. cross-block compression cannot increase essential norm;
6. fixed-width PNT sends `A_(L,R)` to `1-exp(-R)`;
7. the two displayed resolvent identities hold for bounded `A`, `B` and nonreal `z`;
8. compact and Schatten classes are two-sided ideals under multiplication by bounded operators.

Items 1, 4, 5, 7, and 8 are standard Hilbert/operator-space facts; items 2 and 3 are already audited in `PL-052`; item 6 is the fixed-width PNT computation already audited in `PL-049`--`PL-052`.

Any failure of one of these steps falsifies the stated lower bounds or the ideal-equivalence strengthening.

## Consequence for the research line

The boundary ledger now separates four operator viewpoints:

```text
fixed profiles
    B_(L,R) -> B_R strongly
    -> universal rank-one PNT model                         [PL-051]

uniform norm
    ||B_(L,R)-B_R|| stays O(1) from zero
    -> high-frequency prime recurrence                     [PL-052]

modulo compact operators
    ||B_(L,R)-B_R||_ess stays O(1) from zero
    -> no compact/Schatten renormalization                 [PL-053]

ordinary relative resolvent of the bounded pair
    ideal membership <=> ideal membership of B_(L,R)-B_R
    -> no trace-class resolvent repair                     [PL-053]
```

So a useful next mechanism cannot obtain zeta-specific spectral data merely by subtracting the universal boundary model, passing to the compact/Schatten part, or replacing this bounded difference by its ordinary relative resolvent. It must instead impose a canonical smoothing/topology that genuinely controls the recurrent frequencies, exploit threshold or mesoscopic information before homogenization, or couple the prime boundary distribution to an additional arithmetic positivity/target structure that fails matched generalized-prime controls.