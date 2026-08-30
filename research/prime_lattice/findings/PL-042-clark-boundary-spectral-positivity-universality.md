# PL-042 — Clark boundary spectral positivity is universal and cannot localize the zeta defect divisor

## Claim

The most direct boundary-spectral repair left open by `PL-041` is mathematically canonical but still does **not** supply Riemann-zero localization.

Let `theta` be an arbitrary inner function on the unit disk `D`. For every `alpha in T`, the Aleksandrov--Clark construction starts from the Herglotz function

```text
H_(theta,alpha)(z)
  = (alpha + theta(z)) / (alpha - theta(z)),
```

whose real part is positive. Hence there is a positive finite measure `sigma_alpha` on the unit circle such that

```text
H_(theta,alpha)(z)
  = integral_T (xi+z)/(xi-z) d sigma_alpha(xi) + i C_alpha.
```

For inner `theta`, Clark's theorem identifies these measures with the spectral measures of the circle-parametrized unitary rank-one perturbations of the compressed shift/model operator on

```text
K_theta = H^2(D) \ominus theta H^2(D).
```

Thus **positive boundary spectral measures and unitary Clark perturbations exist for every inner function**, not only for an inner function whose zeros lie on a distinguished symmetry locus.

This universality is decisive for the Nyman/model-space branch. Under the Cayley transform, the off-line Nyman defect inner function `B_Z` from `PL-018` becomes an ordinary disk inner function. If RH fails, its zeros `lambda=rho-1/2` lie in the open right half-plane and therefore map to arbitrary interior disk points. Standard Clark theory nevertheless produces positive measures and unitary boundary spectra without contradiction. Consequently,

```text
zeta/Nyman inner defect B_Z
    -> Clark positive measure / unitary rank-one perturbation
    -> spectrum supported on the boundary
```

is **not** a Hilbert--Pólya localization mechanism. The Clark spectrum is a boundary representation of a pre-existing inner function; it does not prove that the zeros used to form that inner function lie on the boundary.

**Evidence/status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the specific route

```text
Nyman/model-space defect
+ standard Aleksandrov--Clark positivity/unitary perturbation theory
    -> force the zeta defect zeros to the critical boundary.
```

No novelty is claimed for Clark measures, Herglotz representation, model spaces, unitary rank-one perturbations, or their spectral measures. The durable derived contribution is the explicit arbitrary-one-zero matched control below and its consequence for the `prime_lattice` search.

## Exact one-zero matched control

Take an **arbitrary** point

```text
a in D
```

and the degree-one Blaschke factor

```text
b_a(z) = (z-a)/(1-conjugate(a) z).
```

Its model space `K_(b_a)` is one-dimensional. For any `alpha in T`, the equation

```text
b_a(zeta)=alpha
```

has the unique solution

```text
zeta_alpha = (a+alpha)/(1+alpha conjugate(a)).
```

Because `b_a` is a disk automorphism, `zeta_alpha` lies on `T`. Its derivative is

```text
b_a'(z)
  = (1-|a|^2)/(1-conjugate(a) z)^2.
```

At the boundary solution,

```text
1-conjugate(a) zeta_alpha
  = (1-|a|^2)/(1+alpha conjugate(a)),
```

so

```text
|b_a'(zeta_alpha)|
  = |1+alpha conjugate(a)|^2/(1-|a|^2).
```

The Clark atom formula for a finite Blaschke product therefore gives

```text
sigma_alpha
  = [1/|b_a'(zeta_alpha)|] delta_(zeta_alpha)

  = [(1-|a|^2)/|1+alpha conjugate(a)|^2]
    delta_(zeta_alpha).
```

The weight is strictly positive for every `a in D`. Hence an arbitrary interior zero produces, for every `alpha`, a perfectly positive Clark measure concentrated at a boundary point. Since the model space is one-dimensional, the corresponding Clark unitary has the one-point unitary spectrum

```text
sigma(U_alpha) = {zeta_alpha} subset T.
```

There is no condition in this construction that forces `a` toward `T`. The radial information about `a` has not disappeared -- it affects the atom weight and the map `alpha -> zeta_alpha` -- but **positivity, unitarity, and boundary support remain valid for every interior location**.

This is the decisive matched control. Any proposed localization argument that uses only those structural properties would also "prove" a false boundary conclusion for an arbitrarily chosen `a`.

## Application to the Nyman off-line defect

`PL-018` identifies the continuous Nyman invariant subspace, after shifting the critical half-plane to

```text
C_+ = {lambda : Re lambda > 0},
```

as

```text
B_Z H^2(C_+),
```

where `B_Z` is the Blaschke product formed from hypothetical zeta zeros

```text
rho with Re rho > 1/2,
```

written as

```text
lambda = rho - 1/2 in C_+.
```

Its model-space defect is

```text
K_(B_Z) = H^2(C_+) \ominus B_Z H^2(C_+).
```

`PL-041` showed that the canonical adjoint dilation semigroup on this defect space is universal for arbitrary inner functions: sampling it at the prime times `log p` faithfully turns each interior zero into a joint prime eigenmode, but does not restrict where that zero may lie.

The Clark construction does not repair that information problem. Apply a Cayley map

```text
C_+ -> D.
```

Every off-line `lambda in C_+` becomes some interior `a in D`. The transformed `B_Z` is again inner, so it has its full Clark family `{sigma_alpha}` and corresponding unitary model perturbations. The one-zero control proves that these boundary spectral objects remain completely consistent with a zero at **any** positive distance from the critical boundary.

Therefore an RH violation is not incompatible with Clark unitarity. In fact, standard functional-model theory automatically moves the spectral representation to the boundary even when the divisor encoded by the model space is interior.

Under RH there is a separate degeneracy: the off-line Blaschke factor is trivial,

```text
B_Z = 1,
K_(B_Z) = {0}.
```

So this particular defect-space construction does not turn the actual critical-line zeros into Clark eigenvalues when RH holds. It models the hypothetical **failure** of RH and then supplies a universal boundary spectral representation of that defect.

## Why a boundary unitary is not a zero-localization theorem

The distinction is structural:

```text
location of zeros of theta
        |
        v
model space K_theta
        |
        v
Clark family of unitary perturbations
        |
        v
spectral measures on T.
```

The last arrow is available for arbitrary `theta`. The support of a Clark spectral measure is on the boundary because the perturbation is unitary; it is not a theorem that the zeros determining `theta` have moved to, or were forced onto, that boundary.

Equivalently, the operation changes **which object carries the information**. Interior zero data can reappear in the boundary measure through support geometry, masses, singular-continuous structure, or the dependence on `alpha`. A spectral theorem for the Clark unitary therefore cannot be read backwards as a localization theorem for the inner divisor without an additional arithmetic identity.

This is the same type of information-relocation obstruction already encountered elsewhere in the line: a representation can be exact and spectrally natural while the difficult RH constraint has already been supplied as input rather than derived.

## Analytic-continuation boundary

No Euler product is continued in this argument.

For the zeta specialization, the inner function `B_Z` is supplied by the analytically continued Nyman/Mellin theory recorded in `PL-018`. The Clark step begins **after** that inner factor has been rigorously identified and then uses only standard Hardy/model-space theory.

Thus the negative genuinely applies in the critical-strip formulation. It does not infer a Clark object by substituting the Euler product outside `Re(s)>1`; it asks whether a standard boundary spectral representation of the already-continued defect adds a new localization constraint, and the arbitrary-Blaschke control shows that it does not.

## Prior art and novelty audit

The ambient mechanism is classical.

- **Douglas N. Clark**, “One dimensional perturbations of restricted shifts,” *Journal d'Analyse Mathématique* **25** (1972), 169--191. DOI: https://doi.org/10.1007/BF02790036. Clark's paper is the primary source for the one-parameter family of unitary one-dimensional perturbations of restricted/compressed shifts and their spectral measures.
- **Eero Saksman**, “An elementary introduction to Clark measures,” in *Topics in Complex Analysis and Operator Theory*, Universidad de Málaga, 2007, pp. 85--136. This is an audit-friendly survey of the Herglotz/Aleksandrov--Clark construction and its model-space/operator interpretation.
- For an explicit modern statement of the analytic construction, see **Oleg Ivrii**, “Analytic mappings of the unit disk which almost preserve hyperbolic area,” *Proceedings of the London Mathematical Society* **129** (2024), e70001, DOI: https://doi.org/10.1112/plms.70001. It records that `(alpha+F)/(alpha-F)` has positive real part, hence a positive Clark measure for every disk self-map, and gives the standard atomic mass `1/|F'(zeta)|` at boundary points with finite angular derivative.
- For the finite-Blaschke atomic formula used in the matched control, see **Kelly Bickel, Joseph A. Cima, Alan A. Sola**, “Clark measures on polydiscs associated to product functions and multiplicative embeddings,” *Complex Analysis and Operator Theory* (2024), DOI: https://doi.org/10.1007/s11785-024-01547-9; its one-variable review states `sigma_alpha=sum 1/|B'(eta_k)| delta_(eta_k)` for finite Blaschke products.

A targeted audit for Clark/Aleksandrov measures tied specifically to Nyman--Beurling or the Riemann zeta divisor did not uncover a theorem that turns this universal Clark positivity into an RH localization mechanism. That absence is **not** used as a novelty claim. The negative follows from the explicit arbitrary-one-zero control and classical Clark theory itself.

## Boundary conditions and surviving escape routes

### Clark measures do retain zero information

The claim is not that the Clark family forgets `theta`. In fact, sufficiently rich Clark data can determine substantial information about the inner function. In the one-zero example, the atom location and weight depend explicitly on `a`.

The no-go is narrower and stronger where needed: **positivity, unitary rank-one realizability, and boundary spectral support alone do not constrain the interior divisor**, because they are universal across arbitrary inner functions.

### Non-atomic Clark spectra do not change the argument

For general infinite inner functions, Clark measures may have more complicated singular spectral type. No claim of pure-point spectrum is made in that setting. The universality of positive measures and unitary perturbations is enough for the obstruction.

### A canonical arithmetic Clark identity could escape

A future construction could still be meaningful if it derives, rather than assumes, an additional relation between the Clark family and arithmetic data such as the distinguished Nyman target, Möbius coefficients, an explicit-formula distribution, or Weil positivity.

To escape this finding, that relation must fail for the arbitrary `b_a` control or for a comparably flexible inner-function family. Merely giving `B_Z` its standard Clark measures, or observing that those measures are positive and the associated perturbations are unitary, does not pass this test.

### Cayley self-adjoint realizations inherit the same warning

One may Cayley-transform an appropriate Clark unitary to a self-adjoint operator. The resulting real/boundary spectrum is still a representation-theoretic consequence of unitarity and does not force the zeros of the input inner function onto the corresponding symmetry boundary. Domain points where the Cayley transform is singular require the usual operator-domain care; no bounded self-adjoint claim is needed here.

## Falsification / audit tests

The decisive negative would be materially narrowed only if one of the following failed or an additional theorem escaped the matched control:

1. the Herglotz function `(alpha+theta)/(alpha-theta)` yields a positive Clark measure for arbitrary inner `theta`;
2. Clark's model associates those measures with unitary rank-one perturbations of the compressed/restricted shift;
3. for arbitrary `a in D`, the degree-one Blaschke factor has the displayed positive atomic Clark measure;
4. the Cayley image of any hypothetical off-line Nyman zero is just such an unconstrained interior disk point;
5. a proposed arithmetic identity involving the Clark family can be proved and shown **not** to survive replacement of `B_Z` by arbitrary one-zero or finite Blaschke controls.

Items 1--4 are classical/direct calculations. Item 5 is the only kind of additional structure that could turn Clark theory from a spectral representation into a localization mechanism.

## Consequence for the research line

The target-relative escape chain is now narrower:

```text
continuous Nyman completion
    -> off-line inner defect B_Z                         [PL-018]

canonical model-space prime co-shifts
    -> arbitrary inner functions have the same
       semigroup/eigenmode structure                    [PL-041]

standard Clark boundary spectralization
    -> arbitrary inner functions have positive Clark
       measures and unitary boundary perturbations      [PL-042]
```

Thus the next useful target is **not** another standard functional-model representation of `B_Z`. A surviving mechanism must couple the Nyman/zeta defect to an external arithmetic observable or global trace/positivity identity whose content is not a theorem of inner-function theory and whose decisive relation fails for the arbitrary-Blaschke matched controls.