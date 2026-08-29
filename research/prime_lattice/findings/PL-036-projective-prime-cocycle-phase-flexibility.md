# PL-036 — Projective prime-lattice curvature is arbitrary phase data, not arithmetic rigidity

## Claim

The next projective-cocycle escape left open by `PL-035` is already too flexible at the level of the bare exponent semigroup.

Let

```text
S = N_0^(P)
```

be the finite-support prime-exponent monoid, written additively. Thus `v(mn)=v(m)+v(n)`. Its group completion is

```text
G = Z^(P) ~= Q_{>0} under multiplication.
```

Fix any total ordering of the rational primes and choose **arbitrary** phases

```text
theta_(p,q) in R/Z,     p<q.
```

For finite-support `alpha,beta in S`, set

```text
B_theta(alpha,beta)
  = sum_(p<q) theta_(p,q) alpha_p beta_q     in R/Z,

omega_theta(alpha,beta)
  = exp(2 pi i B_theta(alpha,beta)).
```

Because `B_theta` is additive in each variable,

```text
omega(alpha,beta) omega(alpha+beta,gamma)
 = omega(beta,gamma) omega(alpha,beta+gamma),
```

so `omega_theta` is a normalized scalar multiplier / projective `2`-cocycle on the prime-exponent semigroup.

The twisted left shifts on `ell^2(S)`,

```text
V_alpha delta_beta
  = omega_theta(alpha,beta) delta_(alpha+beta),
```

satisfy

```text
V_alpha V_beta = omega_theta(alpha,beta) V_(alpha+beta).
```

For prime basis vectors and `p<q`,

```text
V_p V_q
  = exp(2 pi i theta_(p,q)) V_q V_p.
```

Hence the apparent projective curvature between any two prime directions can be prescribed independently. It uses neither `log p` nor any property special to the rational primes.

Moreover this pairwise commutator phase is gauge invariant. If `omega' = omega delta f` differs by a scalar `2`-coboundary, then `delta f(alpha,beta)=delta f(beta,alpha)` because the semigroup is commutative, and therefore

```text
omega'(alpha,beta)/omega'(beta,alpha)
 = omega(alpha,beta)/omega(beta,alpha).
```

Thus the arbitrary phases above are not merely a bad choice of representative: nontrivial pairwise phases define genuine projective cohomological data.

Classical multiplier theory shows that this flexibility is the expected structure, not a new phenomenon. Kleppner's theory of multipliers on abelian groups identifies multiplier classes through bicharacter/commutator data. Laca's Ore-semigroup dilation theorem states that every multiplier on an Ore semigroup extends to its group completion and that restriction induces

```text
H^2(G,T) ~= H^2(S,T).
```

The positive prime-exponent monoid is commutative cancellative and hence Ore, with group completion `Z^(P)`. Consequently there is no hidden projective rigidity caused by using only the positive cone.

**Evidence/status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the route

```text
bare prime-exponent semigroup
+ scalar projective 2-cocycle / prime-square phase
    -> arithmetic rigidity or RH zero localization.
```

The exact arbitrary-phase family is the decisive counterexample. No novelty is claimed for multipliers, projective representations, twisted group/semigroup algebras, or noncommutative-torus-type commutation relations.

## Exact cocycle calculation

For any `alpha,beta,gamma in S`, bilinearity gives

```text
B(alpha+beta,gamma)
 = B(alpha,gamma)+B(beta,gamma),

B(alpha,beta+gamma)
 = B(alpha,beta)+B(alpha,gamma).
```

Therefore

```text
B(alpha,beta)+B(alpha+beta,gamma)
 = B(alpha,beta)+B(alpha,gamma)+B(beta,gamma)

 = B(beta,gamma)+B(alpha,beta)+B(alpha,gamma)
 = B(beta,gamma)+B(alpha,beta+gamma),
```

which exponentiates to the multiplier identity.

The twisted left regular representation is then automatic:

```text
V_alpha V_beta delta_gamma
 = omega(beta,gamma) omega(alpha,beta+gamma)
   delta_(alpha+beta+gamma)

 = omega(alpha,beta) omega(alpha+beta,gamma)
   delta_(alpha+beta+gamma)

 = omega(alpha,beta) V_(alpha+beta) delta_gamma.
```

For `p<q`, the chosen triangular bilinear form gives

```text
omega(e_p,e_q)=exp(2 pi i theta_(p,q)),
omega(e_q,e_p)=1,
```

hence the displayed projective commutation law.

Nothing in this calculation sees the energy map

```text
E(alpha)=<alpha,(log p)_p>.
```

It depends only on the fact that the exponent vectors form a free commutative monoid.

## Classical cohomological prior art

Adam Kleppner's classical paper *Multipliers on Abelian Groups* develops the multiplier theory of locally compact abelian groups; for discrete abelian groups, multiplier classes may be represented by bicharacters, with the antisymmetric commutator bicharacter carrying the projective noncommutativity.

Primary source:

- Adam Kleppner, “Multipliers on Abelian Groups,” *Mathematische Annalen* **158** (1965), 11–34.

For the one-sided semigroup issue, Marcelo Laca proves for any Ore semigroup `S` with enveloping group `G=S^{-1}S` that every multiplier on `S` extends to `G` and restriction induces an isomorphism `H^2(G,T) -> H^2(S,T`. The result is traced there to the earlier semigroup-multiplier work of Laca and Raeburn.

Primary/audit sources:

- Marcelo Laca, “From Endomorphisms to Automorphisms and Back: Dilations and Full Corners,” *Journal of the London Mathematical Society* **61**(3) (2000), 893–904, Theorem 1.2.2. DOI: https://doi.org/10.1112/S0024610799008492. arXiv: https://arxiv.org/abs/math/9911135.
- Marcelo Laca, Iain Raeburn, “Extending Multipliers from Semigroups,” *Proceedings of the American Mathematical Society* **123**(2) (1995), 355–362. DOI: https://doi.org/10.2307/2160888.

Thus a projective representation of the positive prime cone does not gain an extra arithmetic constraint merely from one-sidedness. Its multiplier theory is inherited from the free abelian group completion.

## Beurling matched control

The obstruction survives the strongest control already used in `PL-015`.

A Beurling system with independent generalized-prime logarithms still has exponent semigroup

```text
S = N_0^(N)
```

and group completion `Z^(N)`. Replacing the rational-prime energy vector

```text
(log 2, log 3, log 5, ...)
```

by

```text
(log q_1, log q_2, log q_3, ...)
```

changes none of the cocycle formulas above. The same arbitrary phase matrix `theta_(j,k)` defines the same projective geometry.

Therefore a prime-square relation such as

```text
V_p V_q = c_(p,q) V_q V_p
```

is not arithmetically discriminating simply because `c_(p,q)` is nontrivial. A matched Beurling system can carry the identical projective phase data while having a radically different zeta zero set.

This is a stronger control than the scalar `1`-coboundary flatness of `PL-035`: allowing nonzero projective curvature does create genuine cohomology, but that cohomology is still **freely assignable background structure** rather than a consequence of the rational-prime norm map.

## Higher scalar cocycles do not become special merely by increasing degree

The decisive statement above concerns projective `2`-cocycles, where the semigroup/group cohomology comparison is classical and directly applicable.

There is also a simple warning for proposed scalar higher-cocycle escapes. For any `k>=2`, an arbitrary `k`-multilinear map

```text
C : G^k -> R/Z
```

exponentiates to a scalar inhomogeneous `k`-cocycle because the bar differential cancels by multilinearity. Restricting it to the positive cone gives a higher cocycle on the same prime semigroup. Alternating forms can be assigned freely on finite sets of prime basis directions, just as ordinary torus cohomology supplies exterior classes on every finite-rank free abelian subgroup.

This paragraph is **not** a classification theorem for all higher semigroup cohomology. Its narrower point is enough for the present audit: the mere existence or nonvanishing of a scalar higher cocycle cannot be treated as arithmetic evidence when such cocycles can be written down from arbitrary multilinear phase data with no use of `log p` or zeta.

## Relation to PL-034, PL-035, and the accepted clue

`PL-034` showed that trace-class perturbation/determinant machinery is either trivial or freely engineerable unless an additional cross-prime constraint is supplied. `PL-035` then showed that the ordinary scalar translated `1`-cocycle law is a freely chosen coboundary.

The natural next escape was to replace flat scalar compatibility by nontrivial projective curvature. This finding removes that escape **when the curvature is only a scalar multiplier of the free prime semigroup**:

```text
flat scalar 1-cocycle
    -> arbitrary transfer function F          [PL-035]

projective scalar 2-cocycle
    -> arbitrary pairwise prime phases theta  [PL-036]
```

Thus increasing from a scalar chain rule to a noncommuting/projective prime square does not yet couple the determinant or spectrum to the Riemann divisor.

The accepted local clue remains open only at a more structured level. A viable candidate must explain why its joint prime data are canonically fixed by arithmetic and cannot be replaced by an arbitrary multiplier on the same free monoid.

## Boundary conditions and surviving escapes

### A canonical arithmetic cocycle is not ruled out

The negative concerns **bare semigroup cohomology as the source of rigidity**. Arithmetic may canonically choose a particular cocycle using extra structure — for example local symbols, reciprocity, an adelic product formula, a metaplectic extension, or another finite/archimedean compatibility law. Such a construction would have to prove that its normalization is forced and that matched Beurling systems do not share it.

### Operator-valued curvature is outside the proof

The explicit counterexample is scalar. An operator-valued cocycle whose noncommutativity interacts with a target, scattering operator, or completed trace formula may contain information not reducible to a scalar multiplier. It requires a separate existence/domain/gauge audit.

### Nontrivial projective geometry is not a zero mechanism

One may choose phases producing a highly noncommutative twisted algebra, but the choice can be made independently of the zeta divisor. Conversely, inserting zeta-dependent phases by hand would only move the re-encoding problem from a transfer function into the cocycle.

### Analytic continuation remains external

The cocycle identities are algebraic on exponent vectors. They do not continue an Euler product through `Re(s)=1`, do not produce the functional equation, and do not single out `Re(s)=1/2`.

## Falsification / escape test

A future projective prime-action proposal escapes this negative only if it proves at least one additional statement of the following kind:

1. the multiplier/cohomology class is **canonically forced** by rational-prime arithmetic rather than chosen as free pairwise phase data;
2. the proposed invariant uses `log p`, local-global reciprocity, an archimedean completion, or another global datum in a way that fails for matched Beurling systems;
3. the relevant curvature is operator-valued or higher in a way whose gauge class is constrained by a theorem beyond the free-monoid cocycle identity;
4. that extra constraint controls analytic continuation or a zero-sensitive determinant/trace rather than merely decorating the prime shifts.

Conversely, if the construction still works after replacing its pairwise phase matrix by arbitrary `theta_(p,q)`, or after replacing rational-prime weights by arbitrary Beurling weights, then its projective structure is background flexibility rather than an RH mechanism.

## Consequence for the research line

The trace-class clue has now lost two successive notions of joint compatibility:

```text
ordinary scalar 1-cocycle     -> freely forgeable,
scalar projective 2-cocycle   -> freely forgeable up to genuine arbitrary cohomology.
```

The surviving target is therefore not “find a nonzero cocycle.” It is

```text
find a canonically normalized joint prime invariant whose gauge/cohomology class
is forced by global arithmetic and demonstrably fails for the Beurling controls.
```

That pushes the plausible mechanism toward operator-valued scattering or genuinely global adelic/reciprocity structure, rather than cohomology of the free exponent monoid itself.