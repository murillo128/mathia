# PF-151 — critical first-resolvent residue is pants-area only

**Status:** `DECISIVE-NEGATIVE / CLASSICAL-IDENTITY + EXACT-DERIVED` for the local Wodzicki/Dixmier-residue branch at the weak-trace-class endpoint exposed by PF-112. The general residue theorem is classical; the project-specific conclusion is that the canonical order-`-2` principal-symbol residue on the exact hyperbolic pants decomposition is topological and therefore cannot encode prime-gap fluctuations.

This finding does **not** assert that a global Dixmier trace exists for the full infinite prime flute or for the global prime/shift-clone relative resolvent.

## 1. The critical symbol of the first resolvent

Let `(M,g)` be a smooth Riemannian surface and, locally in the interior, put

```text
R_g(mu) = (Delta_g + mu)^(-1),    mu > 0.
```

The scalar Laplace--Beltrami operator has principal symbol

```text
q_g(x,xi) = |xi|_g^2 = xi^T g(x)^(-1) xi,
```

so the resolvent is a classical pseudodifferential operator of order `-2` with critical homogeneous symbol

```text
sigma_-2(R_g(mu))(x,xi) = |xi|_g^(-2).
```

The shift `mu` enters only lower-order terms and therefore cannot affect the Wodzicki residue density.

With the standard convention

```text
wres_x(A)
  = (2 pi)^(-2)
    integral_{|xi|_e=1} sigma_-2(A)(x,xi) dS_e(xi) dx,
```

the density can be evaluated exactly. Diagonalize the positive matrix `A=g^(-1)` by an orthogonal change of cotangent coordinates. If its eigenvalues are `a,b>0`, then

```text
integral_0^(2 pi)
  dtheta / (a cos(theta)^2 + b sin(theta)^2)
    = 2 pi / sqrt(a b)
    = 2 pi sqrt(det g).
```

Hence

```text
boxed:

wres_x((Delta_g+mu)^(-1))
  = (1/(2 pi)) dA_g(x).
```

Equivalently, on a closed surface where the ordinary Wodzicki residue is globally defined,

```text
Wres((Delta_g+mu)^(-1)) = Area_g(M)/(2 pi).
```

Connes' trace theorem then gives, for this positive order-`-2` operator in dimension two and the same normalization,

```text
Tr_omega((Delta_g+mu)^(-1)) = Area_g(M)/(4 pi).
```

The coefficient can also be audited independently from Weyl's law: `lambda_j ~ 4 pi j / Area`, so the resolvent eigenvalues have harmonic coefficient `Area/(4 pi)`.

## 2. Exact specialization to the prime-flute pants

Each exact prime-flute pant has curvature `-1`, one cusp, and two geodesic cuffs. Its Euler characteristic is `-1`, so Gauss--Bonnet gives

```text
Area(P_n) = 2 pi
```

independently of the two cuff lengths. In particular it is independent of

```text
ell_n ~ 2 log(4 p_n/g_n)
```

and of every prime-gap fluctuation carried by the adjacent Fenchel--Nielsen data.

Therefore the integrated **interior principal residue density** over one exact pant is

```text
integral_{P_n} wres_x(R_g(mu)) = 1.
```

For any finite chain of `N` exact pants,

```text
integral_{P_1 union ... union P_N} wres_x(R_g(mu)) = N.
```

The same statement holds for any matched all-composite shift-clone chain with the same number of pants. Thus the canonical critical-symbol mass of the first resolvent sees only the pants count/topological area, not the distinguished cuff lengths, cross-ratios, or prime gaps.

This is stronger than merely saying that the local hyperbolic model is universal: it identifies the natural scalar residue left exactly at the `S_{1,infinity}` endpoint and shows that its whole-pant aggregation is forced to be universal.

## 3. Relation to PF-112 and PF-150

PF-112 showed that on a compact interior patch where two matched metrics are genuinely nonisometric, the first relative resolvent is generically an order-`-2` operator in dimension two: the critical pseudodifferential order where weak trace class is natural but ordinary trace class fails.

That leaves an obvious temptation:

```text
first relative resolvent not in S_1
  -> use the canonical singular trace at the weak-S_1 endpoint
  -> obtain a prime-gap scalar.
```

The calculation above closes the **principal Wodzicki/Dixmier-residue version** of that temptation. On complete pants, and hence on finite unions when one retains only the interior order-`-2` residue density, the scalar is fixed by Gauss--Bonnet before the prime-dependent cuff moduli enter.

PF-150 showed abstractly that the `S_2` threshold obtained from squared-resolvent trace class cannot be improved by operator algebra alone. PF-151 complements that result from the opposite direction: the most canonical scalar trace available at the first-resolvent critical symbol is too coarse, because its leading logarithmic spectral mass is only area.

## 4. What this negative does and does not rule out

It rules out treating

```text
Wodzicki residue of the unweighted first resolvent
```

or, where Connes' trace theorem genuinely applies,

```text
Dixmier trace of the unweighted first resolvent
```

as a prime-specific spectral invariant. At the principal-symbol level, the result is already determined by Riemannian area; for the exact hyperbolic pants, that area is topological.

It does **not** prove any of the following:

1. that the global relative first resolvent of the infinite prime/shift pair belongs to `L^{1,infinity}`;
2. that a global Dixmier trace on the infinite flute is defined;
3. that every singular trace of every relative operator vanishes;
4. that boundary/interface contributions of a finite-cut boundary-value problem are universal;
5. that weighted or localized residues are prime-blind;
6. that finer singular-value asymptotics, Koplienko data, the squared-resolvent trace-class channel, or the Krein/scattering phase of PF-148 are universal.

In particular, a localized expression with an externally chosen cutoff can weight the area density nonuniformly. Such a quantity may vary under a marking, but the cutoff then supplies extra noncanonical structure. It is not the intrinsic unweighted residue scalar considered here.

## 5. Boundary and noncompactness audit

The full prime flute is an infinite-area, infinite-type surface. Integrating the residue density over all pants gives `+infinity`, in agreement with PF-033's failure of the absolute heat trace/determinant. Consequently the closed-manifold Connes trace theorem must **not** be applied globally to the prime flute without a separate noncompact singular-trace theorem whose hypotheses are verified.

Likewise, if one cuts out a finite collection of pants and imposes boundary conditions on the artificial cuffs/horocycles, the relevant boundary pseudodifferential calculus can carry additional boundary terms. Fedosov--Golse--Leichtnam--Schrohe constructed the noncommutative residue for Boutet de Monvel's boundary calculus, illustrating precisely why an interior Wodzicki-density computation alone does not settle a boundary-value residue.

These caveats are not loopholes in the stated negative. They identify where any surviving prime information would have to live:

```text
not in the canonical interior order-2 principal residue,
but possibly in interface/boundary/global/nonlocal data.
```

## 6. Prior art and novelty assessment

Nothing in the general residue formula is claimed as novel.

- A. Connes, *The action functional in non-commutative geometry*, Communications in Mathematical Physics 117 (1988), 673--683, DOI `10.1007/BF01218391`, proves the identification of the noncommutative/Wodzicki residue at critical pseudodifferential order with the Dixmier trace.
- N. Kalton, S. Lord, D. Potapov, F. Sukochev, *Traces of compact operators and the noncommutative residue*, Advances in Mathematics 235 (2013), 1--55, DOI `10.1016/j.aim.2012.11.007`, gives a modern precise treatment of Connes' trace theorem and the weak-trace-class endpoint.
- B. V. Fedosov, F. Golse, E. Leichtnam, E. Schrohe, *The noncommutative residue for manifolds with boundary*, Journal of Functional Analysis 142 (1996), 1--31, DOI `10.1006/jfan.1996.0142`, is the relevant warning that boundary-value residue theory has extra structure beyond the closed/interior formula.
- E.-M. Hekkelman, E. McDonald, *A General Dixmier Trace Formula for the Density of States on Open Manifolds*, SIGMA 20 (2024), 007, DOI `10.3842/SIGMA.2024.007`, shows that noncompact Dixmier-trace formulas require their own global geometric hypotheses; they are not automatic consequences of the compact theorem.

The durable project-specific content is the exact specialization

```text
critical first-resolvent residue density
  -> hyperbolic area density
  -> 2 pi per exact prime-flute pant
  -> no cuff/gap information in the canonical whole-pant residue.
```

This is a negative bridge result, not a new theorem in noncommutative geometry.

## 7. Stress tests and falsification boundary

There are three direct audits.

**Symbol audit.** Recompute the order-`-2` parametrix coefficient of `(Delta_g+mu)^(-1)`. Any dependence on `mu`, curvature derivatives, or cuff length at homogeneous order `-2` would falsify the derivation. Standard elliptic calculus instead gives exactly `|xi|_g^(-2)`.

**Normalization audit.** On a closed surface, compare against Weyl's law. The logarithmic coefficient of the resolvent eigenvalue sum must be `Area/(4 pi)` for the Dixmier trace, hence `Area/(2 pi)` for the standard Wodzicki residue normalization.

**Geometric audit.** Apply Gauss--Bonnet to a hyperbolic pant with one cusp and two geodesic boundaries. If its area depended on either cuff length, the prime-flute specialization would fail. It does not: the area is exactly `2 pi`.

What remains genuinely open is whether a **nonlocal relative** invariant at or above this endpoint—especially one built from the globally matched prime/shift geometry rather than an arbitrary cutoff—retains the small summable geometric defects strongly enough to distinguish the prime flute from its all-composite clone.

## Research consequence

Reject the branch

```text
PF-112 weak-S_1 endpoint
  -> canonical Wodzicki/Dixmier trace of first resolvent
  -> prime-gap-sensitive scalar
  -> RH mechanism.
```

The weak-trace-class endpoint itself remains mathematically relevant, but its canonical principal residue is an area/topology observable. Any surviving RH-relevant operator channel must use information below or beyond that leading logarithmic residue: finer singular-value structure, nonlocal relative scattering/spectral-shift data, or genuinely intrinsic interface/global effects.