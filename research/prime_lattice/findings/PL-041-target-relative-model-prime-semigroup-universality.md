# PL-041 — Target-relative prime co-shifts are universal model-space time samples and cannot localize the zeta divisor

## Claim

The most direct target-relative Hardy/Nyman repair left open by `PL-040` is mathematically well defined but does **not** provide arithmetic rigidity.

Work in the shifted Hardy half-plane

```text
H = H^2(C_+),
C_+ = {z : Re z > 0},
```

so that `z=s-1/2`. Let `B` be any inner function on `C_+` and let

```text
K_B = H \ominus B H
```

be its model space. For `t>=0`, multiplication by

```text
E_t(z)=exp(-t z)
```

is an isometry of `H`. Since `BH` is invariant under every `M_{E_t}`, the model space `K_B` is invariant under every adjoint `M_{E_t}^*`. Hence

```text
T_t^B = M_{E_t}^* |_(K_B)
```

is a contraction semigroup on `K_B`.

Sampling this semigroup at the arithmetic times

```text
t = log n = <v(n),(log p)_p>
```

gives

```text
T_n^B := T_(log n)^B,
T_m^B T_n^B = T_(mn)^B,
T_n^B = product_p (T_p^B)^(v_p(n)).
```

Thus the prime-indexed family is not a new multidimensional operator geometry: it is the restriction of a single continuous model-space semigroup to the one-dimensional energy samples `{log n}`.

Moreover, if `lambda in C_+` is a zero of `B`, then the ordinary Hardy reproducing kernel `k_lambda` belongs to `K_B`, and

```text
T_t^B k_lambda = exp(-t conjugate(lambda)) k_lambda,
T_p^B k_lambda = p^(-conjugate(lambda)) k_lambda.
```

For the Nyman continuous completion of `PL-018`, take `B=B_Z`, the Blaschke product of zeta zeros `rho` with `Re rho>1/2`, shifted by `lambda=rho-1/2`. Then every hypothetical off-line zero produces a joint prime eigenvector with

```text
T_p^(B_Z) k_(rho-1/2)
  = p^(1/2-conjugate(rho)) k_(rho-1/2).
```

This is a precise target-relative operator encoding of the off-line divisor. It does **not** constrain that divisor. The decisive matched control is universal: for any prescribed `lambda in C_+`, the one-zero Blaschke factor `B=b_lambda` gives a one-dimensional model space in which the same prime semigroup has the joint eigenvalues `p^(-conjugate(lambda))`. Arbitrary interior locations therefore satisfy the same semigroup, contraction, multiplicativity, and reproducing-kernel eigenvector structure.

Consequently, the route

```text
Nyman/zeta inner defect B_Z
    -> model space K_(B_Z)
    -> compress/restrict the canonical prime dilation multipliers
    -> joint prime spectrum/eigenvectors
    -> force Re(rho)=1/2
```

is circular at the localization step. It faithfully turns a chosen inner divisor into a model operator, but the operator axioms survive unchanged when `B_Z` is replaced by an arbitrary Blaschke product. The construction can **represent** an RH violation but cannot rule one out.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the specifically stated model-space/co-shift route. Model spaces, backward-shift/adjoint-semigroup invariance, and Lax--Phillips/Sz.-Nagy--Foias functional models are classical. Nikolski's Nyman completion supplies the specific zeta Blaschke factor, and Uetake's automorphic Lax--Phillips model already illustrates the broader principle that an inner/scattering function can be converted into a semigroup generator carrying its divisor. The derived contribution is the exact prime-lattice matched-control argument above: sampling the universal model semigroup at `log p` adds no localization rigidity.

## Exact semigroup derivation

For `t>=0`, `E_t` is bounded analytic on `C_+`, with

```text
|E_t(i y)|=1
```

for almost every boundary point. Thus `E_t` is inner and `M_{E_t}` is an isometry on `H`.

Because multiplication operators commute,

```text
M_(E_t)(B h) = B M_(E_t)h in B H.
```

Hence `BH` is invariant under `M_(E_t)`. Orthogonal complementation gives

```text
M_(E_t)^* K_B subset K_B.
```

The restricted adjoints therefore satisfy

```text
T_t^B T_u^B
 = (M_(E_t)^* M_(E_u)^*) |_(K_B)
 = M_(E_(t+u))^* |_(K_B)
 = T_(t+u)^B.
```

Now set `t=log n`. Since

```text
log(mn)=log m+log n,
```

we obtain

```text
T_m^B T_n^B=T_(mn)^B.
```

Unique factorization then gives

```text
T_n^B=product_p (T_p^B)^(v_p(n)).
```

But this factorization should not be over-interpreted. Every `T_p^B` is just the same one-parameter semigroup evaluated at a different scalar time:

```text
T_p^B=T_(log p)^B.
```

Thus all exponent vectors first pass through

```text
v(n) -> <v(n),(log p)_p> = log n
```

before the operator acts. The full coordinate geometry has been compressed to the energy functional.

## Zeros become joint eigenmodes

Let `k_lambda` denote the reproducing kernel of the full Hardy space at `lambda in C_+`. If `B(lambda)=0`, then for every `h in H`,

```text
<B h,k_lambda>=(B h)(lambda)=0,
```

so

```text
k_lambda in K_B.
```

For any bounded analytic multiplier `phi`, the standard reproducing-kernel identity is

```text
M_phi^* k_lambda
  = conjugate(phi(lambda)) k_lambda.
```

Taking `phi=E_t` yields

```text
T_t^B k_lambda
 = exp(-t conjugate(lambda)) k_lambda.
```

At a prime time,

```text
T_p^B k_lambda
 = p^(-conjugate(lambda)) k_lambda.
```

So every zero of `B` supplies a simultaneous eigenvector for the entire commuting prime family. The eigenvalue tuple is constrained only by the scalar point `lambda`:

```text
lambda
  -> (p^(-conjugate(lambda)))_p.
```

For `lambda=rho-1/2`, this becomes

```text
(p^(1/2-conjugate(rho)))_p.
```

If `rho=beta+i gamma` with `beta>1/2`, then

```text
|p^(1/2-conjugate(rho))| = p^(1/2-beta) < 1.
```

The critical line corresponds formally to the unit-modulus boundary `Re lambda=0`. This is only a boundary statement: a critical-line zero is not an interior zero of the off-line Blaschke product `B_Z`, and its boundary reproducing kernel is not an ordinary `H^2(C_+)` vector. Under RH, `B_Z=1` and `K_(B_Z)={0}`. The construction therefore models **failure of RH** as a nontrivial defect space; it does not produce critical-line eigenvectors when RH holds.

## Decisive matched control: one arbitrary Blaschke zero

Take any point

```text
lambda=a+i b,
a>0,
```

with no arithmetic meaning at all, and let `b_lambda` be the half-plane Blaschke factor having its single zero at `lambda`. Then

```text
K_(b_lambda)
```

is one-dimensional, spanned by `k_lambda`. On this space the entire prime family is exactly

```text
T_p^(b_lambda)=p^(-conjugate(lambda)) I.
```

All of the structural properties that initially look attractive therefore hold for an arbitrarily placed point:

```text
commuting prime operators,
T_m T_n=T_(mn),
T_n=product_p T_p^(v_p(n)),
contractivity for Re lambda>0,
exact log-prime covariance through t=log p,
a joint eigenmode encoding lambda.
```

No special property forces `a=0`. Finite or infinite Blaschke products similarly allow any admissible interior zero configuration. This control is stronger than saying that model spaces are flexible in principle: it constructs the exact same prime-indexed operator relations for a freely chosen off-axis zero.

Accordingly, any localization argument based only on these relations is impossible. It would prove the same conclusion for the arbitrary one-zero control.

## Relation to the Nyman branch

`PL-018` proves, from Nikolski's theorem, that after completing the Nyman dilation family to all real scales one obtains

```text
E_(1/2)=B_Z H^2(C_+),
```

where `B_Z` contains exactly the zeta zeros to the right of the critical line. The orthogonal complement is therefore

```text
K_(B_Z)=H^2(C_+) \ominus B_Z H^2(C_+).
```

`PL-020` already shows that this model-space component is exactly the part invisible to generator-only Gram geometry. It was therefore natural to ask whether acting on that target-relative defect space with the arithmetic dilation semigroup could restore the missing information.

The present calculation gives the answer for the canonical action: the defect space is indeed invariant under the adjoints of the dilation multipliers, and its zeros do become joint eigenmodes, but the resulting prime operators are merely samples of the universal co-shift semigroup associated with **any** inner function.

Thus target relativity alone does not solve the information-loss problem identified in `PL-020`. One needs an additional relation tying `B_Z` to arithmetic data that is not valid for an arbitrary inner function.

## Relation to automorphic scattering

This result is also a bridge to the prior-art warning in `PL-033`. Uetake's automorphic Lax--Phillips construction uses a model-space/translation-semigroup mechanism in which the causal scattering inner factor carries the completed zeta divisor and the compressed generator realizes the corresponding zeros as eigenvalues.

The present Nyman calculation is not the same automorphic operator, and no claim is made that their generators are unitarily identical. The relevant common structure is more basic:

```text
inner function / scattering divisor
    -> invariant Hardy subspace
    -> orthogonal model space
    -> compressed or adjoint shift semigroup
    -> divisor points as spectral modes.
```

That structure is classical and works for arbitrary inner functions. Therefore obtaining the zeta divisor as model-space spectrum is not, by itself, a localization mechanism. Automorphic scattering supplies a canonical global source for its inner function; Nyman supplies another canonical zeta-dependent inner defect. In both cases the hard RH step is a theorem forcing the divisor to the symmetry boundary, not its spectral realization.

## Analytic-continuation boundary

No Euler product is used in the derivation above. For the zeta specialization, the input `B_Z` is the inner factor supplied by the analytically continued Nyman/Mellin theory of `PL-018`.

The operator identities then live entirely inside `H^2(C_+)` and remain valid for that inner function. Hence this negative result genuinely addresses the critical-strip formulation rather than extrapolating identities from `Re s>1`.

At the same time, this makes the circularity boundary explicit: the off-line zero divisor has already entered through `B_Z`. The model-space semigroup subsequently converts those zeros into eigenmodes but contributes no independent reason for where the zeros may occur.

## Prior-art and novelty audit

The ingredients are classical:

- **Nikolai Nikolski**, “Distance formulae and invariant subspaces, with an application to localization of zeros of the Riemann zeta-function,” *Annales de l'Institut Fourier* **45**(1) (1995), 143–159, DOI `10.5802/aif.1451`. This is the source, already anchored in `PL-018`, for the continuous Nyman invariant space `B_Z H^2` and the exact zeta Blaschke divisor.
- **Yoichi Uetake**, “The Lax--Phillips infinitesimal generator and the scattering matrix for automorphic functions,” *Annales Polonici Mathematici* **92**(2) (2007), 99–122, DOI `10.4064/ap92-2-1`. As recorded in `PL-033`, this is direct number-theoretic prior art for turning an inner/scattering zeta divisor into a semigroup-generator spectrum.
- Classical Beurling/model-space and Sz.-Nagy--Foias/Lax--Phillips functional-model theory supplies the general fact that orthogonal complements of inner invariant subspaces are natural adjoint-shift model spaces. The semigroup identities and the prime-time specialization used here are elementary consequences and were re-derived explicitly rather than treated as a novelty claim.

A targeted literature audit of half-plane shift semigroups and model spaces also finds the modern work of **Yuxia Liang and Jonathan R. Partington**, “Nearly invariant subspaces for shift semigroups,” *Science China Mathematics* **65** (2022), 1895–1908, DOI `10.1007/s11425-020-1915-y`, which explicitly relates right-half-plane shift-semigroup adjoints to model spaces. This confirms that the ambient semigroup/model-space construction is established operator theory.

No novelty is claimed for model spaces, adjoint shift semigroups, kernel eigenvectors, or spectral encoding by an inner function. The durable contribution for `prime_lattice` is the exact **matched-control no-go**: after sampling at the canonical prime times `log p`, every structural relation survives for an arbitrary Blaschke zero, so this target-relative operator layer cannot itself distinguish the Riemann divisor or force the critical line.

## Boundary conditions and escape routes

### The result does not rule out all target-relative operators

It rules out the canonical family obtained solely by restricting the adjoints of the Hardy dilation multipliers to `K_(B_Z)`. A different target-relative operator that also uses Möbius coefficients, the distinguished Nyman target `1/s`, explicit-formula positivity, or another arithmetic observable may contain information absent from the universal model-space semigroup.

### A scalar time parameter is the source of the collapse

The prime family factors through

```text
v(n) -> log n -> T_(log n)^B.
```

A genuinely multidimensional construction that acts separately on prime coordinates and is not equivalent to one-parameter sampling is outside the no-go. It must still pass the Beurling/generalized-prime and normalization controls established earlier in the line.

### Boundary spectral theory can be richer

Clark/Aleksandrov perturbations and boundary model-space theory can turn boundary values of an inner function into unitary spectral measures. This finding does not rule out a construction that derives a **canonical arithmetic boundary measure** and proves a positivity/localization theorem from it. Merely applying standard Clark theory to an already-chosen `B_Z`, however, would again inherit rather than constrain its divisor.

### Global coupling remains the live requirement

`PL-039` and `PL-040` show that standard automorphic local operators scalarize at almost every prime; the present finding shows that the simplest Nyman/model-space target compression is universal. What remains open is a construction whose global/target coupling is not determined solely by a pre-existing inner function and whose identities fail for the arbitrary one-zero Blaschke control.

## Falsification / audit tests

The finding would be falsified or materially narrowed if any of the following failed:

1. `BH` is invariant under every multiplier `M_(exp(-tz))`, so `K_B` is invariant under the adjoints;
2. the restrictions `T_t^B` satisfy the semigroup law;
3. for a zero `B(lambda)=0`, the full Hardy kernel `k_lambda` lies in `K_B` and is an eigenvector with eigenvalue `exp(-t conjugate(lambda))`;
4. sampling at `t=log n` gives the exact multiplicative prime-lattice law;
5. a one-zero Blaschke factor at arbitrary `lambda in C_+` supplies the same relations, proving that those relations alone do not select the boundary `Re lambda=0`.

Items 1--5 are direct Hardy-space calculations. A future construction would escape this no-go only if it uses additional data or relations that the arbitrary Blaschke control cannot reproduce.

## Consequence for the research line

The target-relative branch can now be separated as

```text
continuous Nyman completion
    -> B_Z H^2                                  [PL-018]

orthogonal RH defect
    -> K_(B_Z)=H^2 \ominus B_Z H^2              [PL-020]

canonical prime action on that defect
    -> T_p = M_(p^(-z))^* | K_(B_Z)
    -> zeros become joint eigenmodes
    -> but T_p=T_(log p) samples one universal
       model-space semigroup                    [PL-041]

arbitrary one-zero Blaschke control
    -> identical operator laws at any chosen
       off-axis point
```

Therefore the next viable target is **not** another spectral invariant of this compressed co-shift family alone. It must add a genuinely arithmetic/global coupling that is false for arbitrary inner functions and that forces the zeta-specific defect to disappear (or forces an equivalent positive boundary condition). This sharpens, rather than resolves, the accepted trace-class/target-relative clue.