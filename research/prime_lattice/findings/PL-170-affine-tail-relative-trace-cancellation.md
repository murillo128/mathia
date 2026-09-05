# PL-170 — Affine additive tail renormalization crosses the zeta trace boundary only by canceling zeta to a finite head

## Claim

The first canonical way to enrich the multiplicative prime-exponent lattice with the ordinary additive law is already the classical `ax+b` semigroup. On the positive-energy Hilbert space `ell^2(N_{>=1})`, let

```text
H e_n = (log n)e_n,
S_h e_n = e_(n+h),
mu_m e_n = e_(mn),
```

for `h>=1` and `m>=1`. Then

```text
mu_m S_h = S_(mh) mu_m,
mu_m^* H mu_m = H + log m,
```

so the representation simultaneously contains ordinary addition and the prime-lattice multiplicative covariance of `PL-024`.

This semiring enrichment produces a genuine relative trace below the ordinary zeta trace-class boundary, but the result is exactly **zero-blind**. For every complex `s` with `Re(s)>0`,

```text
Q_h(s)
  := S_h^* exp(-sH) S_h - exp(-sH)
```

is trace class and

```text
boxed:
Tr Q_h(s) = - sum_(n=1)^h n^(-s).
```

For `Re(s)>1`, where both heat operators are separately trace class, this is just

```text
[zeta(s)-sum_(n<=h)n^(-s)] - zeta(s).
```

For `0<Re(s)<=1`, however, the individual traces no longer exist while their operator difference remains trace class. Thus the formula genuinely survives as a **relative operator trace** across the zeta pole/trace threshold and through the critical line. What survives is not the analytic continuation of `zeta`; the entire infinite zeta contribution cancels and only the finite additive boundary `{1,...,h}` remains.

The same phenomenon holds at resolvent level. For `z` outside `spec(H)={log n:n>=1}`,

```text
C_h(z)
  := S_h^*(H-z)^(-1)S_h - (H-z)^(-1)
```

is trace class and

```text
boxed:
Tr C_h(z)
  = -sum_(n=1)^h 1/(log n-z)
  = sum_(n=1)^h 1/(z-log n).
```

Hence its trace is the logarithmic derivative of the finite polynomial

```text
P_h(z)=product_(n=1)^h (z-log n).
```

Any determinant primitive recovered from this relative trace therefore carries only those finitely many deleted low-energy levels, modulo the usual normalization constant. It does not acquire the Riemann zero divisor.

At the Hamiltonian level the additive defect sits exactly one ideal above trace class:

```text
K_h
  := S_h^* H S_h - H
  = diag_n log(1+h/n).
```

Its singular values are `log(1+h/n)~h/n`, so `K_h` belongs to every Schatten class `S_q`, `q>1`, but not to `S_1`. Moreover

```text
sum_(n=1)^N log(1+h/n)
 = log [ (N+1)...(N+h) / h! ]
 = h log N - log(h!) + o(1).
```

Thus the canonical additive infinitesimal has a universal harmonic weak-trace coefficient `h`. Standard Dixmier-trace theory therefore reads this endpoint as the additive displacement itself, not as a prime or zero invariant.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/REDIRECT + NEGATIVE/OBSTRUCTION` for the route

```text
prime-exponent multiplicative action
+ canonical ordinary addition / ax+b completion
+ relative heat or resolvent trace
    -> analytic continuation / determinant carrying Riemann-zero rigidity.
```

The `ax+b` operator algebra is classical prior art. The trace-class, telescoping, Schatten, and covariance identities below are direct exact calculations for the line's logarithmic Hamiltonian. No novelty is claimed for the affine semigroup, Bost--Connes/Cuntz operator algebras, relative trace ideals, or singular traces. The durable line-specific result is that the most literal additive-semiring completion of the prime-lattice Hamiltonian does cross the ordinary trace barrier, but does so by **cancelling the zeta bulk completely**.

## The additive and multiplicative actions form the affine semigroup

Cuntz's canonical representation of the `ax+b` semigroup over the natural numbers uses an additive shift and multiplicative isometries on `ell^2(N)`, with the compatibility relation expressing multiplication distributing over addition. His `Q_N` construction is explicitly described as extending the Bost--Connes algebra by a generator corresponding to translation; the Toeplitz algebra of `N rtimes N^x` and its boundary quotients were subsequently studied systematically.

For the present positive-energy basis indexed by `n>=1`, the required relation is immediate:

```text
mu_m S_h e_n
  = e_(m(n+h))
  = e_(mn+mh)
  = S_(mh) mu_m e_n.
```

Unique factorization still gives

```text
mu_m = product_p mu_p^(v_p(m)),
```

and the logarithmic Hamiltonian satisfies

```text
[H,mu_m]=(log m)mu_m
        = <v(m),(log p)_p> mu_m.
```

Thus this is not an arbitrary added shift: it is the obvious operator representation of the **full positive-integer semiring coupling** suggested by the additive off-diagonal boundary in `PL-169`.

The important question is whether the added translation makes the logarithmic Hamiltonian carry new relative spectral data rather than merely the Bost--Connes multiplicative covariance.

## Relative heat trace: a genuine continuation that erases the zeta term

Since

```text
exp(-sH)e_n=n^(-s)e_n,
```

one has

```text
Q_h(s)e_n
 = [(n+h)^(-s)-n^(-s)]e_n.
```

Let `sigma=Re(s)>0`. Along the positive real axis,

```text
(n+h)^(-s)-n^(-s)
 = -s integral_n^(n+h) x^(-s-1) dx,
```

so

```text
|(n+h)^(-s)-n^(-s)|
 <= |s| integral_n^(n+h) x^(-sigma-1) dx
 <= |s| h n^(-sigma-1).
```

Therefore

```text
sum_n |(n+h)^(-s)-n^(-s)| < infinity
```

for every `Re(s)>0`, proving `Q_h(s) in S_1` there. This is a stronger domain than the ordinary Gibbs trace

```text
Tr exp(-sH)=zeta(s),
```

which exists only for `Re(s)>1`.

The trace is nevertheless elementary. For every finite `N`,

```text
sum_(n=1)^N [(n+h)^(-s)-n^(-s)]
 = sum_(n=N+1)^(N+h) n^(-s)
   - sum_(n=1)^h n^(-s).
```

The first term tends to zero exactly when `Re(s)>0`, giving

```text
Tr Q_h(s)=-sum_(n=1)^h n^(-s).
```

This distinction is load-bearing for the analytic-continuation mandate. In `Re(s)>1` the cancellation can be written using `zeta(s)`, but the operator proof for `0<Re(s)<=1` never assigns a trace to either infinite heat operator and never substitutes the analytically continued scalar zeta function. The **difference itself** is trace class.

Consequently this is a canonical example where relative operator theory genuinely penetrates the critical strip without solving any continuation problem for the original partition trace. It penetrates by deleting the entire infinite tail common to the two spectra.

At the Riemann critical line one gets, for example,

```text
Tr Q_h(1/2+it)
 = -sum_(n=1)^h n^(-1/2-it),
```

which is a finite Dirichlet polynomial. No zero of `zeta(1/2+it)` is distinguished.

## Resolvent comparability also telescopes to the finite boundary

Write

```text
R_z=(H-z)^(-1),
f_z(n)=1/(log n-z).
```

Then

```text
C_h(z)e_n=[f_z(n+h)-f_z(n)]e_n.
```

For large `n`, the derivative of `x -> 1/(log x-z)` is

```text
-1/[x(log x-z)^2],
```

so for fixed `h`

```text
|f_z(n+h)-f_z(n)|
 = O_z,h(1/[n(log n)^2]).
```

The diagonal difference is therefore trace class. Finite telescoping gives

```text
sum_(n=1)^N [f_z(n+h)-f_z(n)]
 = sum_(n=N+1)^(N+h) f_z(n)
   - sum_(n=1)^h f_z(n),
```

and the tail tends to zero because `f_z(n)->0`. Hence

```text
Tr C_h(z)
 = -sum_(n=1)^h 1/(log n-z)
 = d/dz log P_h(z),

P_h(z)=product_(n=1)^h(z-log n).
```

This is stronger than merely saying that the resolvent difference happens to be `S_1`. Its complete scalar trace invariant is the logarithmic derivative of a **finite boundary divisor**. Relative resolvent comparability is therefore not hiding a regularized Riemann determinant in this canonical additive action.

More generally, whenever a scalar function `f` is such that

```text
sum_n |f(log(n+h))-f(log n)| < infinity
```

and `f(log n)->0`, one has the exact tail identity

```text
Tr[f(S_h^*HS_h)-f(H)]
 = -sum_(n=1)^h f(log n).
```

The phenomenon is structural: `S_h^*HS_h` is simply the logarithmic spectrum with its first `h` entries removed and the remainder reindexed.

## The infinitesimal additive defect is a universal weak-trace boundary

On the finite-support core,

```text
S_h^*HS_h e_n=log(n+h)e_n,
```

so the difference extends to the bounded positive compact diagonal operator

```text
K_h e_n=log((n+h)/n)e_n.
```

The sequence is decreasing and

```text
log(1+h/n)=h/n+O_h(1/n^2).
```

It follows immediately that

```text
K_h in S_q  for every q>1,
K_h notin S_1.
```

The borderline coefficient is exact rather than merely asymptotic:

```text
sum_(n=1)^N s_n(K_h)
 = sum_(n=1)^N log((n+h)/n)
 = log[(N+1)...(N+h)/h!].
```

Hence

```text
(1/log N) sum_(n=1)^N s_n(K_h) -> h.
```

In any standard singular-trace convention for which this ordinary logarithmic Cesaro limit gives measurability, the resulting Dixmier trace of `K_h` is `h`. The endpoint residue therefore measures only how many additive basis positions were skipped.

This also explains a small but important discontinuity at `s=0`. Exactly at `s=0`,

```text
Q_h(0)=S_h^*IS_h-I=0,
```

while

```text
Tr Q_h(s) -> -h
```

as `s->0` through positive real values. The relative family is not trace-norm continuous at the endpoint, and its formal infinitesimal is precisely the non-trace-class weak-`S_1` operator `-K_h`. There is no hidden ordinary trace crossing at `s=0`.

## Multiplicative covariance does not restore the lost bulk

The affine relation intertwines these relative operators cleanly with the prime-lattice multiplicative action. First,

```text
mu_m^* K_(mh) mu_m = K_h.
```

For the heat difference,

```text
mu_m^* exp(-sH) mu_m
 = m^(-s) exp(-sH),
```

and `S_(mh)mu_m=mu_m S_h`, so

```text
boxed:
mu_m^* Q_(mh)(s) mu_m
 = m^(-s) Q_h(s).
```

At resolvent level,

```text
mu_m^* R_z mu_m=R_(z-log m),
```

which yields

```text
boxed:
mu_m^* C_(mh)(z) mu_m
 = C_h(z-log m).
```

These are genuine addition--multiplication compatibility identities involving the same `log m=<v(m),log p>` energy that drives the prime torus. But their relative traces remain finite boundary expressions. The semiring covariance organizes the cancellation; it does not undo it.

## Where the arithmetic in shifted correlations actually enters

`PL-169` found that the first standard beyond-diagonal ratios correction is governed by shifted coefficient correlations such as

```text
sum_n I_(A,C)(n) I_(B,D)(n+h).
```

The affine shift `S_h` is exactly the operator that implements the argument translation `n -> n+h`, but the bare shift does not contain those arithmetic coefficients. If

```text
A e_n=a(n)e_n
```

is a diagonal coefficient observable and `P_X` projects onto `e_1,...,e_X`, then the elementary identity

```text
Tr[P_X A^* S_h^* A S_h]
 = sum_(n<=X) conjugate(a(n)) a(n+h)
```

shows precisely where the Hardy--Littlewood/ratios information lives: in the **target coefficient observable `A` coupled to the additive shift**, not in the affine-semigroup relation or logarithmic Hamiltonian by themselves.

For `a(n)=1`, this coefficient layer disappears and the canonical relative spectral data above is completely universal. For `a=Lambda`, Möbius/divisor convolutions, Nyman data, or another zeta-specific target, the resulting shifted-correlation problem can be highly arithmetic, but that is exactly the additional input classified in `PL-075` and `PL-169`; it is not generated by the bare prime lattice plus addition.

## Prior-art and novelty audit

The affine operator framework itself is classical.

- **Joachim Cuntz**, “C*-algebras associated with the ax+b-semigroup over N,” in *K-Theory and Noncommutative Geometry*, EMS Series of Congress Reports, 2008, DOI `10.4171/060-1/8`, arXiv `math/0611541`. Section 2 gives the canonical additive and multiplicative isometries on `ell^2(N)` and their compatibility relation; the introduction explicitly describes the construction as extending Bost--Connes by a translation generator and relates it to finite adeles.
- **Nathan Brownlowe, Astrid an Huef, Marcelo Laca, Iain Raeburn**, “Boundary quotients of the Toeplitz algebra of the affine semigroup over the natural numbers,” *Ergodic Theory and Dynamical Systems* **32**(1) (2012), 35--62, DOI `10.1017/S0143385710000830`. This is direct prior art for the Toeplitz algebra of `N rtimes N^x` and its additive/multiplicative boundary quotients.
- **Jean-Benoit Bost, Alain Connes** (1995), already source `5` in `SOURCES.md`, is the multiplicative/logarithmic-Hamiltonian ancestor used in `PL-024`.
- Standard Dixmier/singular-trace theory supplies the interpretation of a convergent logarithmic singular-value mean; the coefficient `h` itself is obtained here by an exact elementary telescoping product and is not imported from that theory.

A bounded novelty search around `ax+b` semigroup C*-algebras, Bost--Connes extensions by addition, Toeplitz affine semigroups, logarithmic number operators, and Dixmier/weak trace endpoints found the affine operator framework and the general singular-trace machinery as established prior art. No source located in this audit turns the particular tail relative trace above into a Riemann-zero localization mechanism. The displayed trace identities are elementary enough that no novelty is claimed for them independently; their value is the exact route classification relative to `PL-169` and the accepted trace-class operator clue.

## Adversarial boundaries

1. **This is a no-go only for the canonical tail/additive-shift relative pair.** Other representations of the affine semigroup, adelic crossed products, scattering systems, or target-relative compressions can contain much richer information. Cuntz's `Q_N` itself has nontrivial K-theory and arithmetic structure; none of that is claimed to be exhausted by this calculation.
2. **Fixed finite `h` is load-bearing for the finite-head interpretation.** A displacement `h=h(T)` growing with another parameter may create a mesoscopic problem. The exact formula still identifies what is being accumulated, but no uniform asymptotic no-go is asserted for every moving-shift regime.
3. **Relative trace is not analytic continuation of the zeta trace.** For `0<Re(s)<=1`, neither individual heat operator is trace class. Only their difference is. Writing the finite-head answer as a difference of two analytically continued zeta values would obscure the operator fact proved here.
4. **The weak-trace coefficient `h` is not a critical-line selector.** It arises from `log(1+h/n)~h/n`, so its harmonic endpoint is the ordinary one-dimensional tail geometry of additive translation. No functional equation or zero divisor enters.
5. **Coefficient-decorated shifts remain live but classicalize quickly.** The identity with `A^*S_h^*AS_h` shows that one can encode shifted arithmetic correlations operatorially, but doing so does not explain them. For the canonical zeta coefficients those correlations are Hardy--Littlewood/ratios territory already audited in `PL-075` and `PL-169`.
6. **No claim is made about arbitrary determinant normalizations.** The exact invariant proved is the resolvent-difference trace. Its logarithmic primitive has finite divisor `P_h`; a specialized relative determinant may add normalization factors but cannot manufacture an infinite Riemann-zero divisor from this trace without additional data.
7. **The additive semiring is genuine extra rational-integer structure.** Unlike Beurling matched controls, an arbitrary generalized-prime monoid need not possess the canonical shift `n->n+h`. The negative is therefore not that addition is universal; it is that the most literal rational-integer additive action, when paired only with `H=log N`, has trivial relative spectral content.

A falsification of the main claim would require one of the exact diagonal calculations to fail: `Q_h(s)` not to be trace class for some `Re(s)>0`, its trace not to telescope to the finite head, the resolvent difference not to telescope similarly, or the affine covariance relations not to hold. None depends on RH, an Euler product, or an asymptotic prime theorem.

## Consequence for the research line

`PL-169` showed that arithmetic specificity beyond multiplicative diagonal pairings first reappears through ordinary additive shifted correlations. The present result tests the cheapest operator realization of that extra structure and rules it out as an RH mechanism:

```text
bare multiplication
    -> Bost--Connes logarithmic covariance                    [PL-024]

add canonical integer translation
    -> ax+b semigroup
    -> relative heat trace exists already for Re(s)>0
    -> zeta tail cancels exactly to a finite head             [PL-170]

add zeta-specific coefficient observable
    -> shifted Lambda/divisor/ratio correlations
    -> genuine arithmetic input, but classical additive
       correlation theory                                     [PL-075, PL-169]
```

Therefore the instruction “couple the exponent lattice to addition” is still too weak. A viable semiring/affine route must use a **non-tail, target-sensitive coupling** whose invariant is not reduced by additive reindexing to finitely many boundary states and not merely a rewritten shifted-correlation sum. If it is to attack RH, it must additionally explain how that target-relative additive--multiplicative interaction constrains the continued zeta zero divisor rather than merely providing another relative trace that is already regular in the critical strip because the zeta bulk has disappeared.