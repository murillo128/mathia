# PL-019 — The residual integer Nyman semigroup classification is itself a classical open problem

## Claim

The discrete closed-span problem isolated by `PL-018` is not an unexplored consequence of the prime-exponent viewpoint. A directly equivalent Dirichlet-series invariant-subspace question was explicitly posed by Michel Balazard in 2014 and restated in a real-space form in 2018.

Balazard defines a Hilbert space `E^2` of Dirichlet series `D` for which `D(s)/s` continues to `H^2(Re(s)>1/2)`, and the integer multiplier semigroup

```text
T_n D(s) = n^(-s) D(s),    n >= 1.
```

It satisfies

```text
T_m T_n = T_(mn),
T_n = product_p T_p^(v_p(n)).
```

Thus `T` is exactly the positive prime-exponent semigroup in Mellin/Dirichlet coordinates. Up to the harmless scalar normalization `n^(1/2)`, it is the isometric dilation representation already recorded in `PL-017`; multiplying each generator by a nonzero scalar does not change invariant subspaces.

Let `V` be the `E^2`-closure of

```text
zeta(s) * sum_(k=1)^N c_k k^(-s),
subject to sum_(k=1)^N c_k/k = 0.
```

Balazard proves that `V` is `T`-invariant and asks explicitly whether

```text
V = {D in E^2 : D(s)/zeta(s) is holomorphic for Re(s)>1/2}.    (* )
```

He notes that RH makes the right-hand side all of `E^2`, in which case Báez-Duarte gives `V=E^2`, but the point of the question is to prove or disprove `(*)` **unconditionally**.

The condition defining `V` is exactly the Bagchi/Nyman family from `PL-017`. Indeed, every admissible polynomial can be written

```text
sum_(k=1)^N c_k k^(-s)
  = sum_(k=2)^N c_k (k^(-s) - 1/k),
```

because the constraint forces `c_1 = -sum_(k=2)^N c_k/k`. Dividing by `s`, its generators are therefore

```text
G_k(s) = (k^(-s)-k^(-1)) zeta(s)/s.
```

So Balazard's Question 3 is precisely a classification of the **same sparse integer Nyman closed span** highlighted as the residual issue in `PL-018`: are the off-line zeta-zero divisibility constraints the only Hilbert-space obstruction, or can the discrete semigroup have additional closed-span defect invisible to common point zeros?

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION` — material prior-art redirect. The `E^2` space, integer multiplier semigroup, invariant subspace `V`, and equality question are literature. The exponent-vector factorization, scalar-normalization comparison with `PL-017`, and exact identification of the admissible polynomials with the Bagchi generators are elementary derived consequences. No novelty is claimed.

## Exact bridge to the prime-exponent lattice

For

```text
n = product_p p^(v_p(n)),
```

one has, identically,

```text
n^(-s)
 = product_p p^(-s v_p(n)),
```

and hence

```text
T_n = product_p T_p^(v_p(n)).
```

This is the same one-sided positive cone `N_0^(P)` that appears throughout the line. The only difference from Bagchi's normalized operators in `PL-017` is

```text
U_n = n^(1/2) T_n,
```

which makes the dilation action isometric. Since `U_n V subset V` if and only if `T_n V subset V`, the normalization is irrelevant to the invariant-subspace question.

The time parameter is again

```text
lambda_n = log n = <v(n),(log p)_p>,
```

so `T_n` is multiplication by `exp(-lambda_n s)`. Balazard's problem is therefore not merely adjacent to the prime-lattice geometry: it is an invariant-subspace problem for exactly its sparse positive semigroup.

## Why this is the precise residual problem after PL-018

`PL-018` records Nikolski's continuous-scale theorem. When all real multiplicative times are allowed, continuous shift invariance gives a Beurling classification and the closed Nyman space is exactly `B_zeta H^2`, where the Blaschke factor carries the off-line zero divisor. In that setting there is no hidden singular inner defect.

The discrete family has the same common point zeros as the continuous family, but common zeros do not determine a closed subspace. Balazard's equality `(*)` asks exactly whether, after thinning the continuous semigroup from all `lambda>0` to

```text
Lambda_N = {log n : n in N},
```

the zeta-zero divisibility conditions still exhaust the defect.

Thus the sharper comparison is

```text
continuous real shifts
    -> Beurling/Nikolski classification
    -> zero divisor exhausts the defect

discrete prime-exponent shifts
    -> Balazard Question 3
    -> unknown whether zero divisor exhausts the defect.
```

This is a materially stronger novelty boundary than merely observing that discrete totality is hard: the exact classification problem was already isolated in the classical Nyman/Báez-Duarte literature.

## Later formulation and one proved inclusion

Balazard's later paper gives the corresponding real-space formulation. For the discrete Nyman space `Bbar`, Proposition 11 proves one direction:

```text
f in Bbar
    => F(s)/zeta(s) has a holomorphic continuation to Re(s)>1/2.
```

The proof is genuinely inside the critical half-plane: the Mellin continuation forces the approximants to vanish at every off-line zero of `zeta`, with at least its multiplicity, and those vanishing conditions survive Hilbert-space limits.

He then asks the converse as Question 2:

```text
F(s)/zeta(s) holomorphic in Re(s)>1/2
    => ? f in Bbar.
```

Balazard explicitly describes a positive answer as a **discrete analogue** of the Bercovici–Foias theorem for the continuous Nyman setting. This confirms that the unresolved issue is not identification of common zeros but completeness of the sparse integer-generated subspace subject to those zero constraints.

The same paper also recalls Vasyunin's biorthogonal system

```text
<e_j - e_1/j, f_k> = delta_(j,k),
```

constructed through Möbius inversion. This gives classical dual structure for the discrete generators, but no theorem there proves the missing converse; the paper lists it as an open question.

## Current novelty audit

The literature search was performed structurally rather than by wording alone: Nyman/Báez-Duarte invariant subspaces, integer dilation semigroups, Hardy-space closures, zeta divisibility, Vasyunin biorthogonality, weighted-composition semigroups, and recent zero-free-half-plane approximation work were checked.

The strongest direct prior art found is:

- Balazard's 2014 Question 3, which states the `E^2` equality `(*)` explicitly;
- Balazard's 2018/2021 Proposition 11 plus Question 2, proving one inclusion and asking the converse;
- later operator-theoretic work on integer weighted-composition semigroups, which continues to treat cyclicity/invariant-subspace questions as RH-level problems;
- the 2026 Manzur–Noor–Quintero work already recorded in `SOURCES.md`, which obtains zero-free implications and numerical critical-strip evidence but does not supply this unconditional classification.

No reliable source was found that resolves Balazard's discrete converse. This is a **search result, not a theorem of nonexistence**: the durable claim here is the prior-art identification and exact reduction, not an absolute claim that no solution exists anywhere.

## Boundary conditions and adversarial audit

### The classification question is not itself RH

If RH is true, `(*)` collapses to `V=E^2`. If RH is false, the equality could still hold with `V` a proper subspace characterized by divisibility at off-line zeros. Therefore proving `(*)` would classify the discrete defect but would not by itself force the zero set onto the critical line.

### Do not infer a discrete Beurling theorem

The continuous Nyman result uses invariance under all positive real shifts. The integer semigroup has no inverses and `log N` is not dense in `R_+`; the density of `log Q` becomes available only after taking differences, which the one-sided isometries do not provide. Nothing here upgrades integer invariance to continuous invariance.

### Divisibility means multiplicity-sensitive zero constraints

The condition `D/zeta` holomorphic is stronger than saying merely that `D(rho)=0` at each off-line zero: the vanishing multiplicity must be at least that of `zeta`. Balazard's Proposition 11 explicitly preserves these derivative/Mellin moment conditions in the limit.

### The exponent-vector factorization is not new mathematics

Writing `T_n=product_p T_p^(v_p(n))` only exposes the classical semigroup in Mathia's coordinates. The substantive outcome is the novelty redirect: the residual sparse-semigroup classification was already formulated as an open problem.

## Falsification / audit test

The finding should be withdrawn if either of the following fails:

1. Balazard's 2014 `E^2` Question 3 does not state the unconditional equality `(*)` for the integer multiplier-invariant subspace `V`;
2. the algebraic identification of `V/s` with the closed span of the Bagchi generators `G_k` is incorrect.

The second point is directly checkable from the constraint `sum c_k/k=0`. A stronger claim that the question remains unresolved should be updated if a later theorem proving or disproving the converse is located.

## Consequence for the research line

`PL-018` suggested looking for a new one-sided rigidity or completeness theorem specific to the sparse times `log n`. The present audit shows that **this exact target is already a named classical frontier**. Future `prime_lattice` work should therefore not spend cycles rediscovering a discrete Beurling-style formulation.

A genuinely additional contribution would have to attack the missing converse itself or expose new structure that bears on it—for example a quantitative frame/Riesz estimate for the integer generators or Vasyunin dual system, a defect-space theorem tied to the independent prime directions, or a counterexample showing that zero-divisibility does not exhaust the discrete invariant-subspace defect. Any such proposal must be checked against Balazard's formulation rather than presented as a new RH encoding.

## Sources

- Michel Balazard, “Nyman's and Báez-Duarte's criteria for the Riemann hypothesis: survey and open problems,” contribution to *Dirichlet Series and Function Theory in Polydiscs*, Oberwolfach Report 06/2014, *Oberwolfach Reports* 11 (2014), 335–393, especially pp. 351–352. DOI: `10.4171/OWR/2014/06`.
- Michel Balazard, “An arithmetical function related to Báez-Duarte's criterion for the Riemann hypothesis,” arXiv:1812.04309 (2018); later published in *From Arithmetic to Zeta-Functions*, Springer Proceedings in Mathematics & Statistics, 2021.
- Luis Báez-Duarte, “A strengthening of the Nyman-Beurling criterion for the Riemann hypothesis,” *Rendiconti Lincei. Matematica e Applicazioni* 14 (2003), 5–11, arXiv:math/0202141.
- S. Waleed Noor, “A Hardy space analysis of the Báez-Duarte criterion for the Riemann hypothesis,” *Advances in Mathematics* 350 (2019), 242–255. Supporting operator-theoretic context for the discrete semigroup frontier.
