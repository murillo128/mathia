# PL-055 — Fixed compact Sobolev smoothing collapses the Weil boundary defect to the universal PNT model

## Claim

The mesoscopic escape left open by `PL-050`--`PL-054` cannot be obtained by inserting any **fixed, `L`-independent compact boundary smoothing** before taking the large-window limit. Such a smoothing removes exactly the high-frequency prime-log recurrence that survives in operator norm and in the Calkin algebra, and it upgrades the universal strong limit of `PL-051` to norm convergence. For standard Sobolev smoothing it also upgrades the limit to Schatten convergence above the ordinary one-dimensional ideal threshold.

Fix a boundary depth `R>0` and retain the operators from `PL-051`:

```text
B_(L,R)
 = exp(-L) J_(L,R)^* K_L J_(L,R)
```

on

```text
H_R direct_sum H_R,
H_R=L^2(0,R),
```

with

```text
B_(L,R) -> B_R strongly,

B_R = [ 0    P_R ]
      [ P_R  0   ],

P_R=|h_R><h_R|,
h_R(a)=exp(-a/2).
```

Let `Delta_D=-d^2/da^2` be the nonnegative Dirichlet Laplacian on `(0,R)` and, for `s>0`, define

```text
Q_(s,R)=(I+Delta_D)^(-s/2),
S_(s,R)=Q_(s,R) direct_sum Q_(s,R).
```

Then:

```text
boxed:
|| S_(s,R) (B_(L,R)-B_R) S_(s,R) || -> 0
```

for every fixed `s>0`.

More generally, for every `q>=1`,

```text
boxed:
s > 1/(2q)
    =>
|| S_(s,R) (B_(L,R)-B_R) S_(s,R) ||_(S_q) -> 0.
```

In particular, for `s>1/2` the convergence is in trace norm. Hence the Fredholm determinants of the smoothed operators converge locally uniformly in the spectral parameter to the determinant of a rank-two universal limit:

```text
A_(L,s,R)=S_(s,R) B_(L,R) S_(s,R),
A_(s,R)=S_(s,R) B_R S_(s,R),

A_(L,s,R) -> A_(s,R) in S_1,
```

and, writing

```text
u_(s,R)=Q_(s,R) h_R,
c_(s,R)=||u_(s,R)||_2^2,
```

one has

```text
sigma(A_(s,R)) \ {0}
 = {+c_(s,R),-c_(s,R)},

boxed:
det(I-z A_(s,R))
 = 1-z^2 c_(s,R)^2
 = 1-z^2 ||Q_(s,R)h_R||_2^4.
```

Thus fixed compact smoothing does not expose a hidden zeta-zero determinant. It removes the recurrent atomic defect and leaves the same PNT rank-one boundary geometry already identified in `PL-051`.

The trace-class threshold `s>1/2` is also **not** a new occurrence of the Riemann critical line. It is the generic one-dimensional Sobolev/Schatten threshold for a two-sided smoothing. The atomic reflection channel of `PL-054` shows that the criterion

```text
2 s q > 1
```

is sharp for the underlying delta-Hankel boundary geometry.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION`, and `DECISIVE-NEGATIVE` for the route

```text
fixed L-independent compact/Sobolev boundary smoothing
+ natural exp(-L) normalization
+ Schatten/Fredholm determinant limit
    -> zeta-specific residual spectrum or determinant.
```

The result does **not** rule out an `L`-dependent smoothing that weakens as `L->infinity`, a growing depth `R=R(L)`, a joint mesoscopic scaling of space and boundary frequency, or coupling to the archimedean and pole terms of the full Weil form. Those are genuinely different topologies because the compactness mechanism proved below is no longer uniform in `L`.

## Abstract compact-sandwich lemma

The key point is functional analytic and deliberately independent of number theory.

Let `T_L` be uniformly bounded operators on a Hilbert space with

```text
T_L -> 0 strongly.
```

If `Q` is compact, then

```text
boxed:
||T_L Q|| -> 0.
```

Indeed, the image under `Q` of the unit ball has compact closure. Strong convergence plus uniform boundedness makes `T_L x ->0` uniform on every compact subset: cover the compact image by finitely many small balls, use pointwise convergence at their centers, and use the uniform operator bound on the residual radii. Consequently

```text
||Q T_L Q||
 <= ||Q|| ||T_L Q||
 -> 0.
```

Apply this with

```text
T_L=B_(L,R)-B_R.
```

`PL-051` gives strong convergence, hence uniform boundedness by the uniform boundedness principle (and also directly from the normalized shell-mass estimate). Since `Q_(s,R)` is compact for every `s>0`, the claimed operator-norm convergence follows immediately.

This explains why the obstruction in `PL-052`--`PL-053` disappears. Their norm/Calkin lower bounds use unit profiles whose boundary oscillation frequency tends to infinity. Every fixed compact `Q` sends such weakly-null high-frequency sequences to norm zero. The smoothing does not solve the recurrence; it removes the states that witness it.

## Exact Sobolev and Schatten thresholds

The normalized Dirichlet eigenbasis on `(0,R)` is

```text
e_k(a)=sqrt(2/R) sin(k pi a/R),
k>=1,
```

with

```text
Delta_D e_k=(k pi/R)^2 e_k.
```

Therefore

```text
Q_(s,R) e_k
 = q_k e_k,

q_k=(1+(k pi/R)^2)^(-s/2)
    asymp k^(-s).
```

Hence, for every `p>=1`,

```text
Q_(s,R) in S_p
    <=>
sp>1.
```

The same criterion holds for the two-copy operator `S_(s,R)`.

Now fix `q>=1` and suppose

```text
s>1/(2q).
```

Then

```text
S_(s,R) in S_(2q).
```

The ideal Holder inequality gives the uniform bound

```text
||S T_L S||_(S_q)
 <= ||S||_(S_(2q))^2 ||T_L||.
```

To obtain convergence rather than merely boundedness, approximate `S` in `S_(2q)` by its finite-rank spectral truncations `S_N`. Split

```text
S T_L S
 = S_N T_L S_N
   + (S-S_N) T_L S
   + S_N T_L (S-S_N).
```

The last two terms are uniformly small in `S_q` when `N` is large, by the same Holder inequality and the uniform bound on `T_L`. For fixed `N`, strong convergence of `T_L` is uniform on the finite-dimensional range of `S_N`, so

```text
||S_N T_L S_N|| ->0.
```

Finite rank makes operator-norm convergence equivalent to `S_q` convergence there. First choose `N` large and then `L` large. This proves

```text
||S T_L S||_(S_q) ->0.
```

No arithmetic estimate beyond the already-audited strong limit is used.

## Trace-class determinant limit is universal

For `q=1`, the sufficient condition becomes

```text
s>1/2.
```

Thus

```text
A_(L,s,R)-A_(s,R)
 = S_(s,R)(B_(L,R)-B_R)S_(s,R)
 ->0
```

in trace norm.

Continuity of the Fredholm determinant in trace norm therefore gives, locally uniformly for complex `z`,

```text
det(I-z A_(L,s,R))
 -> det(I-z A_(s,R)).
```

But `B_R` is already rank two after the two-end decomposition. Since

```text
Q P_R Q
 = |Q h_R><Q h_R|
 = |u_(s,R)><u_(s,R)|,
```

we have

```text
A_(s,R)
 = [ 0             |u><u| ]
   [ |u><u|        0       ].
```

The symmetric and antisymmetric vectors `(u,u)` and `(u,-u)` give its only nonzero eigenvalues

```text
+c_(s,R),
-c_(s,R),

c_(s,R)=||u||^2.
```

Hence

```text
det(I-z A_(s,R))
 = (1-z c_(s,R))(1+z c_(s,R))
 = 1-z^2 c_(s,R)^2.
```

All zeros of this determinant are the two elementary real points

```text
z=+/- 1/c_(s,R).
```

They come from the smoothed universal PNT boundary mode, not from nontrivial Riemann zeros. Inserting more regularity only makes the convergence stronger; it cannot restore information already removed by the fixed compact sandwich.

## Why `s=1/2` here is a generic ideal threshold

The numerical coincidence between the trace-class condition `s>1/2` and the Riemann critical abscissa is potentially misleading. The parameter `s` in this section is a **Sobolev smoothing order**, not the real part of the zeta variable.

The atomic channel from `PL-054` gives an exact sharpness control. For deficit

```text
delta=R,
```

the delta-Hankel operator is the full reflection

```text
(H_R f)(a)=f(R-a)
```

on `L^2(0,R)`. It acts on the Dirichlet basis by

```text
H_R e_k=(-1)^(k+1)e_k,
```

so it commutes with `Delta_D` and with `Q_(s,R)`. Therefore

```text
Q_(s,R) H_R Q_(s,R)
 = H_R Q_(s,R)^2.
```

Its singular values are exactly

```text
q_k^2
 = (1+(k pi/R)^2)^(-s)
 asymp k^(-2s).
```

Consequently

```text
boxed:
Q_(s,R) H_R Q_(s,R) in S_q
    <=>
2 s q>1.
```

For trace class this is precisely

```text
s>1/2,
```

with logarithmic divergence at `s=1/2`. For Hilbert--Schmidt it is `s>1/4`; for general `S_q` it is `s>1/(2q)`.

This channel occurs in the raw boundary geometry whenever a prime-power atom has deficit `R`; multiplying by its nonzero arithmetic coefficient does not change ideal membership. Thus the threshold is already present in a completely generic reflection channel. It cannot be evidence that the smoothing has discovered the zeta critical line.

No claim is made that every full finite-`L` boundary sum fails to lie in `S_q` at the endpoint threshold; cancellations among channels are a separate issue. The sharp statement needed here is only that the **uniform atomic boundary geometry itself** has exactly this classical threshold.

## Exponent-lattice and matched-control interpretation

Before smoothing, the outer shell consists of prime-power exponent vectors

```text
v(n)=k e_p,
```

with deficit

```text
delta=2L-<v(n),(log r)_r>.
```

`PL-051` shows that every fixed boundary profile sees only the PNT continuum density

```text
exp(-delta/2)d delta,
```

whereas `PL-052`--`PL-053` show that arbitrarily high boundary frequency can still recover coherent information about the exact primitive phases `log p`.

A fixed compact smoothing selects the first regime. Compactness suppresses every weakly-null high-frequency sequence and therefore forces the exact atomic shell back onto its fixed-profile PNT limit. Symbolically,

```text
atomic prime-power shell
    -> strong PNT homogenization on fixed profiles
    -> fixed compact smoothing kills escaping frequencies
    -> norm / Schatten convergence
    -> smoothed universal rank-one boundary model.
```

The proof depends on the rational primes only through the previously established strong PNT boundary limit. Any Beurling/generalized-frequency control with the same fixed-depth strong limit undergoes the same compact-sandwich upgrade and has the same type of rank-two determinant after smoothing.

Therefore the construction fails the line's matched-control test: **fixed smoothing cannot distinguish the exact rational-prime norm map from generalized systems sharing the same first-order shell law.**

## Analytic-continuation boundary

No Euler product or Dirichlet series is analytically continued in this derivation. The operators `B_(L,R)` are finite prime-power pieces extracted from the already-completed Weil explicit formula. The number-theoretic input is only the strong boundary limit proved in `PL-051`, itself based on the prime number theorem.

The obstruction therefore lives entirely on the completed explicit-formula side. The loss of zero-sensitive information is caused by the topology of the fixed compact smoothing, not by staying in `Re(s)>1`.

## Prior-art and novelty audit

The functional-analytic ingredients are classical:

- compact operators turn uniformly bounded strongly convergent families into norm-convergent families after a fixed compact sandwich;
- the Dirichlet Laplacian on a bounded interval has eigenvalues `(k pi/R)^2`;
- Schatten membership is determined by summability of singular values, with the standard ideal Holder inequality;
- Fredholm determinants are continuous under trace-norm perturbations;
- reflection on an interval diagonalizes in the sine basis up to alternating signs.

These facts are standard trace-ideal/operator theory and are not claimed as new. A targeted literature check across Schatten smoothing, Hankel operators, compact-window Weil operators, and explicit-formula boundary models did not identify a stronger arithmetic theorem that would invalidate the direct compact-sandwich argument. Search absence is not treated as evidence of novelty.

The durable content is the specialization to the exact `PL-051`--`PL-054` boundary family and the resulting no-go statement for one of the explicit topological escape routes proposed by `CLUE-mesoscopic-weil-boundary-topology`.

## Falsification and boundary tests

The result reduces to independently checkable statements:

1. `PL-051` supplies `B_(L,R)->B_R` strongly for every fixed `R`;
2. a uniformly bounded strongly-null operator family tends uniformly to zero on the compact image of the unit ball under a fixed compact operator;
3. `Q_(s,R)` has singular values asymptotic to `k^(-s)`;
4. `S_(s,R) in S_(2q)` exactly when `2sq>1`;
5. finite-rank approximation plus ideal Holder yields `S_q` convergence of the sandwich;
6. the smoothed limit has only the two nonzero eigenvalues `+/-||Q_(s,R)h_R||^2`;
7. the full reflection channel has smoothed singular values exactly `(1+(k pi/R)^2)^(-s)`.

Failure of any of items 1--7 falsifies the corresponding conclusion. The theorem also fails to apply if the smoothing depends on `L` in a way that destroys uniform compact approximation; that failure of hypothesis is precisely the surviving mesoscopic direction rather than a loophole in the fixed-smoothing result.

## Consequence for the research line

The fixed-depth boundary topology ledger now becomes

```text
raw fixed profiles
    -> universal rank-one PNT strong limit                 [PL-051]

raw unit sphere / high boundary frequency
    -> norm and Calkin recurrence gap                     [PL-052, PL-053]

fixed compact/Sobolev smoothing
    -> recurrence is compactly suppressed
    -> norm/Schatten convergence to the same PNT model
    -> trace determinant is elementary and universal      [PL-055]

individual raw thresholds
    -> essential delta-Hankel reflection channels         [PL-054]
```

So a useful intermediate topology cannot be obtained merely by choosing a fixed Sobolev weight or another fixed compact boundary regularizer. To remain sensitive to rational-prime microscopic structure while gaining enough compactness for a stable spectral invariant, the regularization itself must become mesoscopic: for example its boundary frequency cutoff must tend to infinity, its Sobolev order may need to weaken with `L`, or the depth `R(L)` must grow.

That residual question is nontrivial because two opposite limits must be balanced simultaneously:

```text
enough smoothing
    -> suppress universal essential recurrence,

but not so much smoothing
    -> collapse back to the PNT rank-one model.
```

Any candidate scale must be forced by the localized Weil construction rather than tuned to the zero divisor, and it must still distinguish rational primes from matched Beurling controls.