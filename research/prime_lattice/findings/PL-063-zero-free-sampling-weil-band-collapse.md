# PL-063 — Zeta zero-free sampling pushes completed Weil band collapse to almost `exp(L^(3/2))` frequency

## Claim

The fixed-depth Dirichlet-band escape left open by `PL-062` can be narrowed much further if one uses the completed explicit-formula structure before taking the crude PNT-discrepancy supremum.

Fix `R>0`. Let `P_N` be the projection onto the first `N` Dirichlet sine modes of `L^2(0,R)`, let `Pi_N=P_N direct_sum P_N`, and let `W_(L,R)` denote the naturally `exp(-L)`-normalized completed Weil boundary form used in `PL-059`--`PL-062`, with the zeta pole and the prime shell canonically centered.

There are constants `c>0` and `C_R>0` such that, for all sufficiently large `L`, all `N>=2`, and every auxiliary height `T>=max(e^e,2N)`,

```text
|| Pi_N W_(L,R) Pi_N ||

 <= C_R [
      log(2+T)
      exp( - c L / ((log T)^(2/3) (log log T)^(1/3)) )

      + N^2 log(2+T)/T

      + exp(-L)(1+log(1+N))
    ].
```

The first term is a direct consequence of the Vinogradov--Korobov zero-free region after sampling the nontrivial-zero expansion by compact boundary Laplace transforms. The second term is the high-zero tail, controlled by one integration by parts on the first `N` Dirichlet modes and the classical local zero count. The last term contains the same-end, pole-approximation, and archimedean costs already isolated in `PL-059` and `PL-061`.

Taking `T=N^3` gives

```text
|| Pi_N W_(L,R) Pi_N ||

 <= C_R [
      log N
      exp( - c_R L /
             ((log N)^(2/3) (log log N)^(1/3)) )

      + log N/N
      + exp(-L)(1+log N)
    ].
```

Consequently, if `N=N(L)->infinity` and

```text
boxed:
log N(L) * (log log N(L))^2 = o(L^(3/2)),
```

then

```text
boxed:
|| Pi_(N(L)) W_(L,R) Pi_(N(L)) || -> 0.
```

In particular every stretched-exponential band

```text
N(L)=exp(L^alpha),
alpha<3/2,
```

still collapses unconditionally.

This is a substantial strengthening of `PL-062`, whose PNT-supremum argument only forced collapse for `log N=o(L^(3/5)/(log L)^(1/5))`. The stronger result does **not** improve the prime number theorem itself. It uses the fact that a finite Dirichlet band tests the boundary discrepancy through Paley--Wiener/Laplace transforms, so the zeta zero-free region can be applied at the actual boundary frequencies instead of first compressing all arithmetic information into the scalar remainder `r_(L,R)`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION`, and `DECISIVE-NEGATIVE` for the route

```text
fixed boundary depth
+ first N(L) Dirichlet modes
+ N(L) below the zero-free sampling scale
    -> nontrivial mesoscopic completed-Weil limit
    -> RH rigidity.
```

The result is deliberately one-sided. It does not locate the actual transition, does not control unrestricted operator norm or the Kronecker recurrent states of `PL-052`, and does not claim that the scale `exp(L^(3/2))` is sharp. It only proves that an enormously larger moving-frequency regime than the one covered by `PL-062` is still forced to zero.

## Boundary-shell form and exact zero expansion

Write

```text
X=exp(2L).
```

The normalized outer-shell prime measure from `PL-051` is

```text
mu_(L,R)
 = X^(-1/2)
   sum_(X exp(-2R)<n<X)
      Lambda(n)n^(-1/2)
      delta_(log(X/n)),
```

and its PNT limit is

```text
d mu_R(delta)
 = exp(-delta/2) 1_[0,2R](delta) d delta.
```

Let

```text
D_(L,R)=H_(mu_(L,R))-P_R
```

be the centered cross-end Hankel block. For `f,g in P_N L^2(0,R)`, extended by zero outside `(0,R)`, define

```text
phi_(f,g)(delta)
 = integral conjugate(g(b)) f(delta-b) db.
```

Then

```text
<g,D_(L,R)f>
 = integral phi_(f,g) d(mu_(L,R)-mu_R).
```

Introduce the compact Laplace transform

```text
A_f(z)=integral_0^R f(a) exp(-z a) da.
```

The convolution factorization is exact:

```text
Phi_(f,g)(z)
 := integral_0^(2R) phi_(f,g)(delta) exp(-z delta) d delta

 = A_f(z) conjugate(A_g(conjugate(z))).
```

`PL-052` already derived the smooth shell explicit formula. The same identity extends to the present finite sine-band profiles by approximation: the zero extensions of `f` and `g` lie in `H^1`, their convolution has compact support, and the factorization above gives enough `1/|gamma|^2` decay for absolute convergence of the zero sum. After the additional `X^(-1/2)=exp(-L)` normalization used in the boundary operator, one obtains

```text
boxed:
<g,D_(L,R)f>
 = - sum_rho
       X^(rho-1)
       A_f(rho-1/2)
       conjugate(A_g(conjugate(rho)-1/2))
   + O_R(X^(-3)) ||f|| ||g||.
```

The sum is over nontrivial zeros with multiplicity. The error is the far-off trivial-zero term on the shell; its uniform bound uses only compact support and Cauchy--Schwarz.

This formula is not a formal continuation of the Euler product. It is the already-continued von Mangoldt/Weil explicit formula tested against a compact boundary correlation.

## A zero-sampling inequality for compact boundary Laplace transforms

The key estimate is independent of `N`.

For every `f in L^2(0,R)` and `T>=3`,

```text
boxed:
sum_(rho: |Im rho|<=T)
 |A_f(rho-1/2)|^2
 <= C_R log(2+T) ||f||_2^2.
```

To see this, put

```text
F_f(x,y)=A_f(x+i y),
-1/2 <= x <= 1/2.
```

Partition the strip into unit-height rectangles. The Riemann--von Mangoldt formula gives, with multiplicity,

```text
# {rho: m <= Im rho < m+1}
 = O(log(2+|m|)).
```

On an enlarged rectangle, two-dimensional Sobolev evaluation bounds the supremum of `|F_f|^2` by the local `L^2` norms of finitely many `x`- and `y`-derivatives. But

```text
partial_x^j partial_y^k F_f(x,y)
```

is, up to a unit scalar, the Fourier transform in `y` of

```text
a^(j+k) f(a) exp(-x a) 1_[0,R](a).
```

Plancherel therefore gives, uniformly for `|x|<=1/2`,

```text
integral_R
 |partial_x^j partial_y^k F_f(x,y)|^2 dy
 <= C_(R,j,k) ||f||_2^2.
```

The enlarged rectangles have bounded overlap. Summing their Sobolev bounds and multiplying by the maximal number `O(log T)` of zeros in one unit-height rectangle proves the displayed sampling inequality.

This is just a Paley--Wiener/Bessel estimate adapted to the zeta-zero multiset. No separation hypothesis for individual zeros is used; possible multiplicities are absorbed by the local zero count.

## Low zeros are exponentially suppressed by the zero-free region

The Vinogradov--Korobov zero-free region supplies a constant `c_0>0` such that, after decreasing it harmlessly to cover bounded heights,

```text
1-Re rho
 >= eta(T)
 := c_0 /
    ((log T)^(2/3) (log log T)^(1/3))
```

for every nontrivial zero with `|Im rho|<=T`, once `T` is large enough.

Hence

```text
|X^(rho-1)|
 = exp(-2L(1-Re rho))
 <= exp(-2L eta(T)).
```

Apply Cauchy--Schwarz to the low-zero part of the exact expansion and use the sampling inequality for both `f` and `g`:

```text
sum_(|Im rho|<=T)
 |X^(rho-1)|
 |A_f(rho-1/2)|
 |A_g(conjugate(rho)-1/2)|

 <= C_R log(2+T)
    exp(-2L eta(T))
    ||f|| ||g||.
```

This is the gain that the scalar PNT remainder of `PL-060`--`PL-062` cannot see. The boundary transform localizes each zero by its vertical frequency before any supremum over the prime-counting discrepancy is taken.

## High zeros are cheap on a finite Dirichlet band

For `f in P_N L^2(0,R)`, the Dirichlet boundary conditions give `f(0)=f(R)=0`. Integration by parts yields

```text
z A_f(z)
 = integral_0^R f'(a) exp(-z a) da.
```

The first `N` sine modes satisfy the standard Bernstein estimate

```text
||f'||_2 <= (pi N/R) ||f||_2.
```

Therefore, uniformly for `|Re z|<=1/2` and `|Im z|>=2`,

```text
|A_f(z)|
 <= C_R N ||f||_2 / |Im z|.
```

Using the same bound for `g` and again the local zero count,

```text
sum_(rho: |Im rho|>T)
 |A_f(rho-1/2)|
 |A_g(conjugate(rho)-1/2)|

 <= C_R N^2 ||f|| ||g||
    sum_(|gamma|>T) 1/gamma^2

 <= C_R N^2 log(2+T)/T
    ||f|| ||g||.
```

Here we used only `|X^(rho-1)|<=1`, since every nontrivial zero lies in `0<Re rho<1`. Thus no unproved information about zeros deeper in the critical strip enters the tail estimate.

Combining the low and high pieces proves

```text
||P_N D_(L,R) P_N||

 <= C_R [
      log(2+T) exp(-2L eta(T))
      + N^2 log(2+T)/T
      + X^(-3)
    ].
```

## From the prime block to the full completed Weil form

`PL-059` identifies the zeta pole as the canonical finite-rank term that cancels the PNT rank-one boundary model. Its difference from that model is `O_R(exp(-L))` in norm. The same-end prime pieces are also `O_R(exp(-L))`.

`PL-061` gives the independent archimedean estimate on the first `N` boundary modes,

```text
O_R(exp(-L)(1+log(1+N))).
```

Adding these already-audited terms to the cross-end bound above gives the claimed estimate for the full compressed completed Weil form.

The point of this step is important: the zero-free sampling estimate is not being applied to a prime-only surrogate and then declared to be the completed operator. The completion terms are carried explicitly and are uniformly negligible throughout the band regime proved here.

## Choosing the zero-height cutoff

Take

```text
T=N^3.
```

Then

```text
N^2 log T/T = O(log N/N),
```

while the low-zero term becomes

```text
O_R(
  log N
  exp(-c_R L /
      ((log N)^(2/3)(log log N)^(1/3)))
).
```

Write

```text
u_L=log N(L).
```

The condition

```text
u_L (log nu_L)^2=o(L^(3/2))
```

is equivalent, after taking the `2/3` power, to

```text
nu_L^(2/3) (log nu_L)^(4/3)=o(L).
```

Therefore

```text
L /
 [nu_L^(2/3)(log nu_L)^(1/3)]
 >> log nu_L,
```

so the exponential suppression dominates the prefactor `nu_L=log N`. The high-zero tail and archimedean term vanish as well. This proves full compressed norm collapse.

The scale comparison with `PL-062` is

```text
PNT-supremum route:
    log N << L^(3/5)/(log L)^(1/5)

zero-sampled boundary route:
    log N (log log N)^2 << L^(3/2).
```

The improvement comes from preserving the vertical spectral variable instead of differentiating an arbitrary test against the scalar PNT remainder.

## Relation to prime-log recurrence

There is no contradiction with `PL-052` or `PL-053`. Those findings construct, separately for each `L`, arbitrarily high boundary frequencies at which the finite prime-log phases recur close to coherent alignment. The present theorem says that the recurrent norm-defect states cannot be found inside any Dirichlet band satisfying the displayed zero-free sampling condition.

Thus the topology ledger becomes more quantitative:

```text
fixed profiles
    -> strong completed cancellation;

moving Dirichlet bands with
log N (log log N)^2=o(L^(3/2))
    -> still norm collapse;

unrestricted frequency
    -> order-one recurrent norm/Calkin defect.
```

The surviving arithmetic transition is therefore pushed to frequencies beyond every `exp(L^alpha)` with `alpha<3/2`, unless one changes the topology rather than merely enlarging the fixed-depth Dirichlet band.

The theorem does **not** give a matching lower bound on the first Kronecker recurrence time. Converting the band exclusion into a sharp simultaneous-Diophantine recurrence theorem would require quantitative approximation of the modulated `PL-052` witnesses by the Dirichlet basis and matching upper constructions; neither is claimed here.

## Beurling and matched-control audit

The proof uses four inputs:

```text
1. an explicit-formula zero expansion for the centered prime shell;
2. a zero-free envelope near Re(s)=1;
3. O(log T) local zero density;
4. compact-support Paley--Wiener sampling geometry.
```

The last item is universal harmonic analysis. The first three are analytic data of the completed zeta object, not consequences of the abstract free exponent lattice. A generalized-prime system with a comparable explicit formula, zero-free region, and local zero-count bound would satisfy the same collapse theorem.

Accordingly, this is a **negative scale barrier**, not rational-prime RH rigidity. In particular the Vinogradov--Korobov boundary itself is not special enough to force the critical line; `PL-062` already records Beurling analogues of the zero-free-to-PNT mechanism. What is new in the present derivation is that keeping the boundary frequency variable intact allows the ordinary zeta zero-free region to exclude a much larger class of moving-band candidates.

## Analytic-continuation audit

No identity from the Euler-product half-plane is continued formally.

The prime shell is finite for each `L`. The passage to zeros uses the classical completed von Mangoldt/Weil explicit formula, already part of the canonical `PL-013`, `PL-052`, and `PL-059` evidence. The only location theorem used is the unconditional Vinogradov--Korobov zero-free region near `Re(s)=1`; no RH-strength assumption is made.

The split at height `T` is absolutely convergent for finite-band profiles because their compact Laplace transforms have `1/|gamma|` decay after one integration by parts, so the product has `1/gamma^2` decay and the zeta zeros have only `O(log gamma)` local multiplicity.

## Prior-art and novelty audit

Every external ingredient is classical or already anchored in `SOURCES.md`:

- Weil's explicit formula and Bombieri's analysis of the Weil quadratic functional provide the completed prime/zero identity (`SOURCES.md` 25--26);
- the Vinogradov--Korobov zero-free scale and its modern sharp PNT consequences are anchored by Bellotti and Johnston (`SOURCES.md` 59--60);
- the Riemann--von Mangoldt zero count, local `O(log T)` consequence, Plancherel, Sobolev evaluation, and the Dirichlet-mode Bernstein inequality are standard.

A targeted literature audit across localized Weil forms, Paley--Wiener sampling at zeta zeros, moving finite-frequency compressions, and zero-free-region estimates did not locate this exact boundary-compression theorem. Search absence is not used as evidence of novelty. No novelty is claimed for the zero-free region, the sampling lemma as a general harmonic-analytic principle, or the explicit formula.

The durable contribution is the **line-specific synthesis and no-go**: the `PL-052` boundary zero expansion and a zero-sampling argument bypass the `N r_(L,R)` loss that limited `PL-062`, showing that the completed fixed-depth Dirichlet-band family remains trivial on an almost `exp(L^(3/2))` frequency scale.

## Falsification and boundary tests

The result reduces to the following independently checkable points:

1. the normalized centered cross-end form is `X^(-1/2)` times the `PL-052` shell probe and hence has zero weights `X^(rho-1)`;
2. `Phi_(f,g)(z)=A_f(z) conjugate(A_g(conjugate(z)))`;
3. zeta zeros in each unit-height strip number `O(log T)` with multiplicity;
4. compact boundary Laplace transforms satisfy the stated strip sampling inequality by local Sobolev evaluation plus Plancherel;
5. the Vinogradov--Korobov zero-free region gives the displayed low-zero exponential weight;
6. the Dirichlet boundary condition plus one integration by parts gives `A_f(x+i gamma)=O_R(N/|gamma|)` on `P_N`;
7. summing `1/gamma^2` against local zero density gives `O(log T/T)`;
8. the pole/same-end and archimedean terms have the bounds already established in `PL-059` and `PL-061`.

Failure of any item invalidates the corresponding estimate. The theorem also ceases to apply if the moving subspace is not controlled by the first `N` Dirichlet modes, if boundary depth itself changes in a way not reduced by `PL-057`, or if one seeks the unrestricted high-frequency norm where `PL-052`--`PL-053` prove recurrence survives.

## Consequence for the research line

`CLUE-mesoscopic-weil-boundary-topology` is narrowed again, without being resolved.

The fixed-depth Dirichlet-band search no longer begins at the Vinogradov--Korobov PNT inverse-error scale of `PL-062`. Preserving the vertical zero frequency shows that **all** bands satisfying

```text
log N (log log N)^2=o(L^(3/2))
```

are still too low-frequency to retain a nontrivial completed Weil residual.

A surviving mesoscopic mechanism must therefore do at least one of the following:

```text
- reach frequencies at or beyond this much larger zero-free sampling barrier;
- use a moving subspace/topology not reducible to first-N Dirichlet frequency control;
- couple frequency to another canonical variable in a way that defeats the zero-sampling bound;
- or introduce a genuinely rational-prime/global invariant absent from matched generalized-prime explicit-formula systems.
```

Merely increasing the boundary cutoff through polynomial or ordinary stretched-exponential scales is now ruled out much more strongly than in `PL-062`.