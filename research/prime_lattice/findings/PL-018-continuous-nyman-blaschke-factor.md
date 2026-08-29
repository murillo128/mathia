# PL-018 — Continuous Nyman scale completion is exactly the zeta Blaschke factor; the sparse integer lattice is the unresolved part

## Claim

Nikolski's 1995 invariant-subspace formulation of the Nyman construction gives an exact description of what happens when the arithmetic dilation family is completed from integer scales to **all** real multiplicative scales.

For `gamma>0`, let

```text
E_{a,gamma}(x) = x^gamma ( floor(a/x) - a floor(1/x) ),   0<a<1,
```

and let `K_gamma` be the closed span of these functions in `L^2((0,1),dx/x)`. Under the Mellin isometry

```text
M : L^2((0,1),dx/x) -> H^2(Re z>0),
```

write `E_gamma=M K_gamma`. Nikolski proves that

```text
E_gamma = B_gamma H^2(Re z>0),
```

where `B_gamma` is the Blaschke product whose zeros are exactly

```text
{ rho-gamma : zeta(rho)=0, Re(rho)>gamma }.
```

There is **no singular inner factor**. Thus at `gamma=1/2`,

```text
RH
<=> B_(1/2) = 1
<=> E_(1/2) = H^2(Re z>0).
```

This is a strong prior-art redirect for the prime-lattice line. The continuous multiplicative semigroup already has a complete Hardy invariant-subspace classification, and its only inner obstruction is literally the off-line zeta zero divisor. Consequently, completing the integer prime-exponent action to all positive real scales does not create an independent mechanism forcing RH; it repackages the zero set as a Blaschke inner factor.

The genuinely arithmetic residue is the **sparse restriction to integer scales** `a=1/n`, equivalently to semigroup times

```text
lambda = log n = <v(n),(log p)_p>.
```

Báez-Duarte proves that this much smaller integer family is still RH-equivalent, but Nikolski's Beurling classification uses invariance under the full continuous scale semigroup and therefore does not identify the integer-generated closed span unconditionally.

**Evidence/status:** `LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION` — Nikolski's Mellin invariant-subspace theorem and elimination of the singular inner factor are classical literature. Báez-Duarte's integer-scale strengthening is classical literature. The explicit comparison with the prime-exponent time set `log N`, the common-zero audit for the integer subfamily, and the resulting identification of sparse semigroup completeness as the residual lattice problem are exact derived consequences. No novelty is claimed for the Nyman, Beurling, Mellin, or Blaschke constructions.

## The continuous scale semigroup and Mellin diagonalization

Nikolski uses the Mellin transform as the Fourier transform of the multiplicative group. With his normalization,

```text
(M g)(z) = const * integral_0^1 g(x) x^z dx/x,
Re z>0,
```

which is an isometry onto `H^2(Re z>0)`. A direct calculation gives, initially through the classical integral representation of zeta,

```text
M E_{a,gamma}(z)
  = const * (a^(z+gamma)-a) zeta(z+gamma)/(z+gamma).
```

This formula is not an Euler-product extrapolation. Nikolski obtains it from the floor-function integral representation; the resulting expression gives the analytic Hardy function on `Re z>0`, with the apparent zero at `z+gamma=1` canceled by the pole of zeta.

The real-space multiplicative shifts

```text
(r_beta f)(x) = f(x/beta),   0<beta<1,
```

preserve `K_gamma`. Under Mellin they become multiplication by

```text
exp(-lambda z),   lambda=log(1/beta)>0.
```

Hence `E_gamma` is invariant under the **entire** continuous inner semigroup `{exp(-lambda z):lambda>0}`. After transporting the half-plane to the disk, Beurling's invariant-subspace theorem applies and yields

```text
E_gamma = Theta_gamma H^2,
Theta_gamma = B_gamma S_gamma,
```

with `B_gamma` Blaschke and `S_gamma` singular inner.

## The inner factor is exactly the shifted zeta zero divisor

Nikolski first determines the common point zeros of the generating family. For fixed `a`, zeros can come from zeta or from

```text
a^(z+gamma-1) = 1.
```

But requiring the latter for **every** `0<a<1` eliminates all such points; `z+gamma=1` is not a zero because the zeta pole cancels the vanishing factor. Thus the common zeros are exactly

```text
zeta(z+gamma)=0,   Re z>0.
```

Therefore the Blaschke part `B_gamma` of `Theta_gamma` is precisely the Blaschke product of the zeta zeros in `Re s>gamma`, shifted by `-gamma`.

The remaining possibility is a singular inner factor. Nikolski rules it out. Since the Mellin generators extend analytically across the finite boundary, a common singular inner divisor can only be the half-plane exponential factor

```text
S_gamma(z)=exp(-c z),   c>=0.
```

He then uses the large-positive-real asymptotics of the Mellin generators, together with `zeta(s)->1` as `Re s->+infinity`, to force `c=0`. Hence

```text
S_gamma=1,
E_gamma=B_gamma H^2(Re z>0).
```

This is stronger than merely observing that zeta zeros are common zeros: the full continuously invariant closed subspace has no hidden singular inner obstruction beyond that Blaschke divisor.

## Critical specialization

Set `gamma=1/2`. Multiplication by `x^(1/2)` is a unitary map

```text
L^2((0,1),dx) -> L^2((0,1),dx/x).
```

Moreover

```text
{a/x} - a {1/x}
  = -( floor(a/x) - a floor(1/x) ),
```

so Nikolski's `gamma=1/2` family is, up to this unitary weight and an irrelevant sign, the classical Hilbert-space Nyman family.

Therefore

```text
E_(1/2)=B_(1/2) H^2(Re z>0),
```

where `B_(1/2)` contains exactly the nontrivial zeros with `Re rho>1/2`, shifted into the right half-plane. Since RH is equivalent to the absence of such zeros,

```text
RH <=> B_(1/2)=1 <=> E_(1/2)=H^2.
```

The critical-line `1/2` here still comes from the `L^2`/Mellin normalization, consistently with `PL-017`; this result does not show that the abstract exponent cone alone selects `1/2`.

## Reproducing-kernel geometry becomes exactly Blaschke geometry

Nikolski's broader paper studies distances from reproducing kernels to closed subspaces. For an invariant Hardy subspace

```text
E=B H^2
```

with `B` inner, multiplication by `B` is an isometry and the projection of a reproducing kernel `k_s` onto `E` has norm

```text
||P_E k_s|| = |B(s)| ||k_s||.
```

Equivalently, independently of the chosen kernel normalization,

```text
dist(k_s,E)^2 = (1-|B(s)|^2) ||k_s||^2.
```

Thus in the continuous Nyman completion the Hilbert-space distance geometry is not a new latent spectral variable: it is exactly the modulus geometry of the Blaschke product of zeta zeros. Nikolski uses this relation to produce explicit zero-free disks.

This gives a useful falsification rule for future proposals: if a proposed continuous-scale distance, angle, or invariant-subspace quantity can be reduced to the Beurling inner factor of `E_(1/2)`, it has not explained why the zeros lie on the critical line; it has encoded the off-line zero divisor into `B_(1/2)`.

## What remains when the scales are restricted to the prime lattice

The integer version uses

```text
a = 1/n,
n = product_p p^(v_p(n)).
```

Writing `lambda=log(1/a)` gives

```text
lambda = log n = sum_p v_p(n) log p.
```

So the prime-exponent lattice is exactly the restriction of Nikolski's continuous shift time `lambda in R_+` to

```text
Lambda_N = {log n : n in N}.
```

Under Mellin, the continuous semigroup is

```text
{exp(-lambda z) : lambda>=0},
```

whereas the lattice sees only

```text
{n^(-z) : n>=1}
 = {exp(-z <v(n),log p>)}.
```

This distinction cannot be removed by a density argument. `log N` is discrete in `R_+` (its only accumulation is at infinity), so invariance at integer times does not extend by strong continuity to arbitrary positive times. The difference group

```text
log Q_(>0) = log N - log N
```

is dense in `R`, as already relevant to `PL-011`, but obtaining differences would require inverse/adjoint actions. The integer dilation operators are proper isometries, not a unitary group, as recorded in `PL-017`. Therefore the dense rational-log group does not automatically upgrade the one-sided integer semigroup to Nikolski's continuous semigroup.

This is the exact point at which the prime lattice retains arithmetic information.

## The sparse integer family already has the same common point zeros

There is an additional negative check. Restrict Nikolski's generators to `a=1/n`, `n>=2`. Their zeta factor is unchanged. Could the sparse factors introduce extra **common** point zeros? Such a point would have to satisfy

```text
n^(1-(z+gamma)) = 1
```

for every integer `n>=2`. Taking `n=2` and `n=3`, if `z+gamma!=1` this would imply a rational relation between `log 2` and `log 3`, contradicting unique factorization. Hence the only common solution is `z+gamma=1`, again canceled by the zeta pole.

Therefore the continuous family and the integer family have the same common point-zero set:

```text
{z: Re z>0, zeta(z+gamma)=0}.
```

So merely detecting common zeros of the Mellin generators cannot distinguish the full continuous Nyman space from the sparse arithmetic one. The unresolved issue is **closed-span completeness under the sparse generator set**, not identification of its common point zeros.

Báez-Duarte's theorem makes this sharp at `gamma=1/2`: restricting the classical Nyman family from all real dilations to integer dilations remains equivalent to RH. Thus the smaller arithmetic family is sufficient *if RH is true*, but the proof of that equivalence does not provide an unconditional Beurling-type identity saying that its closed span already equals `B_(1/2)H^2`.

## Prior art and novelty assessment

- **Nikolski (1995)** is the primary source for the continuous-scale result: Mellin isometry, full multiplicative-shift invariance, Beurling factorization, identification of the Blaschke zeros with shifted zeta zeros, elimination of the singular inner factor, and reproducing-kernel distance localization.
- **Báez-Duarte (2003)** proves that the Nyman-Beurling RH criterion remains equivalent when the real dilation parameter is restricted to positive integers. This is exactly the arithmetic thinning relevant to the exponent lattice.
- `PL-017` already records Bagchi's integer isometric semigroup and its Mellin characters `exp(-it<v(n),log p>)`. The present finding does not duplicate that operator dictionary; it identifies what is gained and lost when that semigroup is completed to all real scales.

No novelty is claimed for the invariant-subspace theorem or the RH criteria. The derived contribution for this research line is the precise boundary:

```text
continuous multiplicative scales
    -> full shift invariance
    -> exact Beurling classification B_zeta H^2
    -> zero divisor is already built into the inner factor

integer / prime-exponent scales
    -> same common point zeros
    -> no automatic continuous-shift invariance
    -> totality/completeness remains the RH-level arithmetic problem.
```

## Boundary conditions and failure modes

### Do not transfer `E_gamma=B_gamma H^2` to the integer-generated span

Nikolski's proof needs invariance under all `0<beta<1`, equivalently all `lambda>0`. The integer-generated subspace is invariant under the integer multiplication semigroup, not under arbitrary real dilations. Beurling's continuous-shift classification therefore cannot simply be applied to it.

### Same common zeros do not imply the same closed subspace

Two Hardy subspaces can share the same common point-zero set and still differ greatly. The equality `E_gamma=B_gamma H^2` uses full invariant-subspace structure, not only zero detection. Hence the exact common-zero calculation for `a=1/n` does not solve the discrete completeness problem.

### The Blaschke factor is not a Hilbert–Pólya spectrum

The zeros of `B_gamma` are encoded as common zeros of functions in a Hardy invariant subspace. They are not eigenvalues of a self-adjoint operator. The fact that an inner factor packages them geometrically does not impose `Re rho=1/2`.

### Analytic continuation is genuine

The Mellin formula is based on a classical integral representation of zeta and yields analytic Hardy functions in `Re z>0`; it does not continue an Euler product term by term from `Re s>1`. The argument therefore survives the analytic-continuation audit relevant to this line.

## Audit / falsification criterion

The finding is falsified if any of the following source-level statements fails:

1. Nikolski's `K_gamma` is invariant under every real multiplicative shift `r_beta`, `0<beta<1`.
2. Its Mellin image is therefore a Beurling invariant subspace `Theta_gamma H^2(Re z>0)`.
3. The common zeros of the continuous generators are exactly the shifted zeta zeros in `Re z>0`.
4. Nikolski's argument forces the singular inner part of `Theta_gamma` to be trivial, yielding `Theta_gamma=B_gamma`.
5. Báez-Duarte's strengthened Nyman-Beurling criterion really does restrict the dilation parameters to positive integers.

The prime-lattice interpretation is then checked exactly by `a=1/n` and `log n=<v(n),log p>`. Any future claim that integer-scale invariance automatically yields all real-scale invariance must explicitly provide the missing inverse/limit mechanism; the topology of `log N` alone does not do so.

## Consequence for the research line

After `PL-017`, one natural next move was to classify the Nyman invariant subspace more deeply and hope that the prime-lattice semigroup forced a special inner/spectral structure. Nikolski shows that **after continuous completion this classification is already classical and is exactly the zeta Blaschke divisor**. That branch therefore cannot supply an independent proof mechanism without becoming circular.

The sharper remaining target is discrete:

```text
Why can the sparse semigroup times
    log n = <v(n),log p>
carry enough information to force the Nyman integer span to be total,
when the full continuous-scale span is classified only by the zeta zero divisor itself?
```

Any genuinely new prime-lattice contribution should distinguish the arithmetic semigroup `{log n}` from the continuous scale semigroup, for example through a quantitative completeness/Gram estimate, a one-sided semigroup rigidity principle, or additional global arithmetic structure. Replacing `{log n}` by all real times removes precisely the discreteness that still contains the unresolved RH content.