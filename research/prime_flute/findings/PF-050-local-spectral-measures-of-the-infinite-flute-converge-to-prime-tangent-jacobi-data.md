# PF-050 — local spectral measures of the infinite flute converge to prime-tangent Jacobi data

**Status:** `POSITIVE / EXACT-DERIVED + CLASSICAL-LOCAL-SPECTRAL-CONVERGENCE`.

PF-034 established genuine pointed hyperbolic tangents `Y_H` inside the exact infinite prime-flute. PF-047--PF-049 then showed that, for hierarchical prime patterns, the small Laplace spectrum of `Y_H` is governed by a canonical weighted path and that an endpoint spectral measure of that path determines the complete ordered relative gap vector. The remaining gap was that the endpoint measure was still formulated on the finite tangent rather than directly as spectral data of the single infinite prime-flute.

This note closes that localization gap: **the local spectral measure of the global Laplacian, measured by a probe carried by successive isolated occurrences of a fixed pattern, converges to the corresponding tangent spectral measure.** Consequently the weighted-path/Jacobi data of PF-049 are genuine local spectral limits of the Laplacian on the infinite prime-flute, even though the unmarked global spectrum is far too noncompact to recover them.

## 1. Fixed isolated pattern and escaping copies

Let

```text
H={eta_1<...<eta_r}
```

be a fixed exact prime pattern that recurs in the isolated-cluster construction of PF-034. Let `Omega_j` be successive embedded occurrences in the prime-flute, with outer separating geodesic `beta_j`. PF-034 proves

```text
ell(beta_j) -> 0.
```

The collar half-width therefore satisfies

```text
W_j = asinh(1/sinh(ell(beta_j)/2)) -> infinity.
```

If `x_j` is a point in a fixed compact core of the occurrence, then

```text
boxed:
(X_prime,x_j) -> (Y_H,x)
```

in pointed smooth/geometric topology. The complement of the occurrence is pushed to distance `W_j+O(1)` from every fixed compact subset of the tangent core.

## 2. Local spectral measure of the global Laplacian

Choose a real compactly supported probe

```text
psi in C_c^infty(Y_H)
```

inside a fixed compact core of the first canonically ordered pants component. Transport it to the `j`-th occurrence, obtaining `psi_j in L^2(X_prime)`, with the same normalization up to `o(1)`.

Let `mu_j` be the scalar spectral measure of the **global** Laplacian `Delta_X` at `psi_j`:

```text
<psi_j, F(Delta_X) psi_j>
   = int F(lambda) d mu_j(lambda)
```

for bounded Borel `F`. Let `mu_H` denote the analogous spectral measure of `Delta_{Y_H}` at `psi`.

For every `a>0`, the Stieltjes transforms are

```text
S_j(a)
 = <psi_j,(Delta_X+a)^(-1)psi_j>
 = int dmu_j(lambda)/(lambda+a).
```

Pointed smooth convergence plus the collar separation gives local resolvent convergence at the negative spectral parameter `-a`:

```text
boxed:
S_j(a) -> S_H(a)
       = <psi,(Delta_{Y_H}+a)^(-1)psi>.
```

There are several standard ways to justify this step:

1. local elliptic/strong-resolvent convergence under pointed smooth convergence;
2. the convergence of hyperbolic resolvents away from the essential spectrum used in degeneration theory (Hejhal--Wolpert--Jorgenson--Lundelius--Schulze);
3. directly, the long separating collar makes the influence of the complement exponentially small for the negative resolvent, while the metric on every fixed compact part converges smoothly.

Since the measures have uniformly bounded total mass `||psi_j||^2 -> ||psi||^2` and their Stieltjes transforms converge for every `a>0`, uniqueness of the Stieltjes transform gives

```text
boxed:
mu_j => mu_H
```

weakly on `[0,infinity)`.

Thus every finite tangent spectral measure is a **local spectral limit of the single global Laplacian**. This is stronger than the PF-034 Weyl-sequence statement, which retained only the locations of tangent eigenvalues.

## 3. Canonical first-pants probe and graph endpoint weights

Now take a hierarchical family `H_B` as in PF-047. Cutting the `r-2` short nested separating curves produces an ordered chain

```text
P_1,...,P_N,
N=r-1,
```

of pants components, each of area exactly `2 pi`.

For the ideal endpoint probe one may take

```text
psi_B = (2 pi)^(-1/2) 1_{P_1}.
```

This is an `L^2` vector of norm one. If one wants a smooth compactly supported probe for the pointed-convergence argument, truncate the cusp tails and smooth the characteristic function; the omitted cusp area tends to zero, so the resulting spectral measures approximate the ideal one uniformly in total mass. Equivalently one may use any fixed smooth thick-core probe with known nonzero integral; its low-mode residues differ from the endpoint weights by a known scalar factor.

Let

```text
0=lambda_0(B)<lambda_1(B)<=...<=lambda_{N-1}(B)
```

be the constant mode and the `N-1` small eigenvalues of `Y_{H_B}`, and `phi_m` corresponding normalized eigenfunctions. Define

```text
beta_m(B)
 = (2 pi)^(-1/2) int_{P_1} phi_m dA.
```

Burger's proof of the surface-to-graph asymptotic decomposes low eigenfunctions as

```text
phi_m = h_m + g_m,
```

where `h_m` is constant on each component and `g_m` has mean zero there. In the pinching limit the mean-zero part vanishes in the low-energy reduction. If

```text
v_m(i)=sqrt(2 pi) * h_m|_{P_i},
```

then `v_m` is the corresponding normalized eigenvector of the weighted dual graph to first order. Therefore

```text
boxed:
beta_m(B) -> v_m(1)
```

whenever the graph shape is kept nondegenerate during the degeneration. The normalization is exact: the factor `sqrt(2 pi)` is precisely the square root of the pants area.

Together with Burger's eigenvalue asymptotic

```text
2 pi^2 lambda_m(B) = mu_m(G_B)(1+o(1)),
```

this gives the finite-measure convergence

```text
boxed:
sum_m |beta_m(B)|^2 delta_{2 pi^2 lambda_m(B)}
   =>
nu_{G_B,1},
```

where `nu_{G_B,1}` is the endpoint spectral measure of the canonical weighted path `G_B`.

For arbitrarily multiscale paths, individual eigenvectors can become ill-conditioned when graph eigenvalue scales collide. The invariant statement is convergence of the compressed low-energy quadratic form/spectral measure; a uniform quantitative inverse bound over every PF-046 hierarchy remains a separate stability question. No such uniformity is required for the fixed-pattern local-limit statement of section 2.

## 4. Direct local-spectral bridge inside the infinite prime-flute

Combining sections 2 and 3 gives a two-stage limit entirely inside the spectral theory of the **same infinite surface**.

For each sufficiently pinched hierarchical pattern `H_B`, choose an occurrence index `j(B)` so far out that its exterior collar makes the global local spectral measure arbitrarily close to the tangent measure. Then

```text
boxed:
local spectral measure of Delta_{X_prime}
 at the first-pants probe of occurrence j(B)

 -> tangent small spectral measure
 -> endpoint measure of G_B.
```

The graph edge weights are the actual pinching lengths

```text
w_k
 = L_k
 = 4 asinh sqrt((d_1+...+d_{k-1})/d_k),
```

and PF-049's inverse Jacobi theorem gives

```text
nu_{G_B,1}
  -> (w_1,...,w_{N-1})
  -> (d_1:...:d_{r-1}).
```

Equivalently, using the distinguished cuffs of a large-prime occurrence,

```text
d_i/d_j
 = lim exp(-(ell_i-ell_j)/2).
```

Hence the exact chain is now

```text
boxed:
relative prime cuffs
 -> exact nested orthogonal-circle necks
 -> finite prime tangent
 -> local spectral measure of the global prime-flute Laplacian
 -> endpoint Jacobi measure
 -> ordered relative gap vector.
```

The important distinction from all failed global-zeta constructions is **spatial localization before spectral compression**. The global Laplacian may have wildly noncompact spectral behavior, but a probe trapped behind a collar whose width tends to infinity forgets the rest of the flute in the local resolvent limit.

## 5. Why this is not contradicted by the earlier negative results

- PF-021/PF-024 concern only the coarse set of global essential spectral values.
- PF-033/PF-035/PF-036 show that global heat/Selberg/Ruelle traces and determinants diverge.
- PF-037 shows that a microlocal invariant of a **single cuff** is universal.
- PF-042 shows that deterministic one-path principal-series transport telescopes.
- PF-048 shows that the **unmarked eigenvalue list** of the effective graph is not inverse-unique.

PF-050 uses none of those compressed global objects. It uses a canonically marked local spectral measure, whose residues retain the eigenfunction amplitudes that PF-048 proved were missing from the unordered spectrum.

## 6. Literature and novelty audit

Known analytic ingredients:

- Marc Burger, *Asymptotics of small eigenvalues of Riemann surfaces* (1988) and *Small eigenvalues of Riemann surfaces and graphs* (1990), gives the graph asymptotic and explicitly decomposes low eigenfunctions into componentwise constants plus mean-zero remainders. Burger notes the extension to geometrically finite surfaces.
- Jorgenson--Lundelius and Michael Schulze prove convergence of heat/resolvent kernels for degenerating finite-geometry hyperbolic surfaces. Schulze proves local resolvent convergence away from the essential spectrum and convergence of Riesz projectors.
- Local spectral-measure convergence from strong/local resolvent convergence and uniqueness of Stieltjes transforms is standard operator theory.
- Endpoint spectral measures determining finite Jacobi matrices are classical inverse Jacobi theory.
- Jin--Wang, arXiv:2608.22330 (23 Aug 2026), is very close current prior art on the **surface-to-weighted-graph** side: their Steklov-determinant analysis compares small Neumann/Dirichlet eigenvalues of degenerating genus-zero hyperbolic surfaces with weighted graph Laplacians. It does not appear to study local endpoint spectral measures, prime-derived tangents, or inverse reconstruction of the pinching weights from a canonical component probe.

Directed searches for `prime gaps + local spectral measure + degenerating hyperbolic surface`, `prime gaps + weighted path + hyperbolic Laplacian`, and `prime tangent + endpoint Jacobi spectral measure` did not locate this composition.

No novelty is claimed for any individual convergence theorem. The candidate new statement is specific to the exact prime-flute geometry: **the ordered relative gap/cuff data occur as a recoverable local spectral limit of the global Laplacian on one deterministic infinite-type hyperbolic surface.**

## 7. Limitations

- This is marked/local spectral data, not reconstruction from the unmarked global spectrum alone.
- It does not identify Riemann zeros or imply RH.
- Uniform stable inversion for arbitrarily extreme multi-scale PF-046 paths still requires condition-number estimates for the endpoint Jacobi inverse problem.
- The interior/exterior duality remains ambient rather than an independent `L^2` symmetry of the flute; the argument preserves the exact orthogonal-circle construction but does not obtain a second spectral copy from the exterior.

## 8. Research consequence

The global determinant/trace program is largely obstructed, but the exact surface still possesses a mathematically natural prime-sensitive spectral observable:

```text
boxed:
mu_{psi_j}^{X_prime}
```

for probes `psi_j` attached to escaping isolated prime blocks. These measures converge to finite tangent spectral measures and, in the graph degeneration regime, to Jacobi endpoint measures whose continued fractions recover the relative cuff/gap path.

The next nontrivial question is no longer whether prime-gap information reaches the Laplacian—it does, in this local spectral sense—but whether one can extract from the family of escaping local measures a **canonical scale-invariant statistic** that is constrained enough to have arithmetic content beyond the deliberately forced prime-pattern flexibility.
