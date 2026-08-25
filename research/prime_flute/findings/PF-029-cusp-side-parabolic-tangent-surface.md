# PF-029 — cusp-side re-marking produces a finite punctured-sphere tangent candidate

**Status:** `EXACT-DERIVED + LITERATURE-BACKED CANDIDATE / NEEDS-GEOMETRIC-LIMIT-AUDIT`.

This is a corrected replacement candidate after PF-028 invalidated the positive-endpoint fixed-surface limit in PF-025. The finite matrix algebra below is exact. The identification of the limiting finite group with the double of an ideal polygon is standard once the stated generators are obtained. The remaining nontrivial gate is to prove that the **full conjugated prime-flute groups** have exactly this Chabauty/geometric limit, rather than merely containing these limiting relative holonomies.

## 1. The cancellation missed by PF-025/PF-028

Use the exact prime-flute side-pairing matrix

```text
G(a,b) = 1/(b-a) * [[a+b,-2ab],[-2,a+b]].
```

PF-028 correctly shows that an individual `G(P+x,P+y)` retains a divergent common scale and does not converge to `G(x,y)` under the positive-side recentering.

However the **relative holonomy**

```text
W(a,b;c,d) = G(a,b) G(c,d)^(-1)
```

has an exact translation covariance that the individual generator does not have. If

```text
T_t(z)=z+t,
```

then direct matrix multiplication gives

```text
T_t W(a+t,b+t;c+t,d+t) T_t^(-1)
  = W(a,b;c,d).
```

In particular the adjacent cusp word

```text
P(a,b,c)=G(a,b)G(b,c)^(-1)
```

satisfies

```text
T_t P(a+t,b+t,c+t) T_t^(-1)=P(a,b,c).
```

Thus PF-028 kills convergence of the **absolute side pairings**, but not of the relative words in which the divergent common boost cancels.

This distinction is intrinsic: the adjacent products are precisely the parabolic cusp loops found in PF-018.

## 2. The correct re-marking is on the mirror/cusp side

Scale the exact prime endpoint by

```text
v_p = pi cot(pi/p).
```

Then

```text
v_p = p - pi^2/(3p) + O(p^-3).
```

Also dilation is exactly covariant:

```text
D_k G(a,b) D_k^(-1)=G(ka,kb),

D_k(z)=kz.
```

Consider a bounded translated prime pattern

```text
p_i=P+eta_i,
eta_1<...<eta_r,
```

and define the hyperbolic re-marking

```text
C_P(z)=pi z + P.
```

This is deliberately the **opposite translation** from the failed positive-endpoint normalization in PF-025. The reason is geometric, not cosmetic: PF-018 shows that the adjacent parabolic around the vertex `b` has fixed point `-b`. Hence

```text
C_P(-cot(pi/(P+eta_i)))
  = P-v_{P+eta_i}
  -> -eta_i.
```

So `C_P` recenters the actual finite cusp fixed points on the negative/mirror side of the symmetric ideal fundamental polygon. Meanwhile the positive endpoints move to order `2P` and escape every compact set.

For every fixed relative word,

```text
C_P W(u_a,u_b;u_c,u_d) C_P^(-1)
 = W(v_a-P,v_b-P;v_c-P,v_d-P),
```

so a fixed offset pattern has a genuine finite relative-holonomy limit.

This does not reinterpret the Euclidean exterior arc of PF-017 as a second hyperbolic surface. It uses the actual `+/-` mirror side structure of the zero-twist Fuchsian fundamental polygon.

## 3. Exact limiting cusp parabolics

Let

```text
d_i=eta_{i+1}-eta_i>0.
```

PF-018 writes

```text
P(a,b,c)
```

as a trace `-2` parabolic whose fixed point is `-b`. Multiplying by `-1` in `SL(2,R)` does not change its element of `PSL(2,R)`. In the standard trace `+2` convention, write

```text
Q(c,D)
 = [[1+cD, -c^2 D],
    [D,      1-cD]],
```

which is parabolic with fixed point `c`.

For an internal prime of the bounded pattern, the cusp-side limit is exactly

```text
c_i=-eta_i,
D_i=2(1/d_{i-1}+1/d_i).
```

If the pattern is isolated by exterior gaps tending to infinity on both sides, the two end cusps satisfy

```text
D_1=2/d_1,
D_r=2/d_{r-1}.
```

These are not arbitrary matrices. They are exactly the standard parabolics obtained by composing reflections in the two sides adjacent to a vertex of the ideal polygon with ordered vertices

```text
-eta_r < ... < -eta_1 < infinity.
```

For a finite ideal polygon, the orientation-preserving index-two subgroup of its reflection group uniformizes the double of the polygon, a finite-area punctured sphere.

## 4. The missing cusp at infinity appears automatically

The adjacent prime cusp words telescope before taking the limit:

```text
P_1 ... P_r
 = G(a_ext, eta_1) G(eta_r, d_ext)^(-1),
```

where the transformed exterior endpoints tend to `-infinity` and `+infinity` under two-sided isolation.

The exact matrix limit is, projectively,

```text
Q_1 ... Q_r
 = [[1, 2(eta_r-eta_1)],
    [0, 1]].
```

Therefore adding

```text
Q_infinity
 = [[1, -2(eta_r-eta_1)],
    [0, 1]]
```

gives

```text
Q_1 ... Q_r Q_infinity = I.
```

This is the standard peripheral relation for a genus-zero surface with `r+1` cusps.

Thus the finite relative-holonomy limit is naturally the Fuchsian group associated with the **double of the ideal `(r+1)`-gon** having vertices

```text
{-eta_1,...,-eta_r,infinity}.
```

Call this finite-area reflection-symmetric surface `Y_H`.

Its area is

```text
area(Y_H)=2 pi (r-1).
```

## 5. First genuinely nonlocal example: three primes give a four-punctured sphere

For two internal gaps

```text
d_1=eta_2-eta_1,
d_2=eta_3-eta_2,
```

the tangent surface is the double of an ideal quadrilateral, hence a four-punctured sphere in the reflection-symmetric real slice of `M_{0,4}`.

Direct multiplication gives

```text
|tr(Q_1 Q_2)|/2 = 1 + 2 d_1/d_2,
|tr(Q_2 Q_3)|/2 = 1 + 2 d_2/d_1.
```

If `L_12` and `L_23` are the corresponding primitive hyperbolic translation lengths, then exactly

```text
sinh(L_12/4)^2 = d_1/d_2,
sinh(L_23/4)^2 = d_2/d_1.
```

Equivalently,

```text
L_12 = 4 asinh(sqrt(d_1/d_2)).
```

This is an important sanity check against the earlier negative results:

- a two-prime tangent gives an ideal triangle double, i.e. the unique thrice-punctured sphere, so one isolated gap has **no modulus**;
- three primes are the first case with a genuine modulus, and it is a ratio of two gaps / a four-point cross-ratio;
- the local common scale `P` and all individual divergent distinguished cuffs have disappeared, while relational multi-gap data survive.

## 6. Why this yields a legitimate spectral candidate

`Y_H` is finite area and finite type. Therefore its ordinary spectral objects are standard and well-defined:

```text
Delta_{Y_H},
scattering matrix Phi_H(s),
scattering determinant phi_H(s),
Selberg zeta Z_H(s),
resonances / scattering poles,
L^2 small spectrum below 1/4.
```

No ad hoc prime generating function is introduced.

For the four-punctured example, the standard Selberg product contains the primitive geodesic above through the ordinary factor

```text
prod_{k>=0} (1-exp(-(s+k)L_12)),
```

with

```text
L_12=4 asinh(sqrt(d_1/d_2)).
```

More generally, proper consecutive products of the `Q_i` telescope to relative `G G^(-1)` words, so their traces are precisely the multi-gap/cross-ratio quantities of PF-004. Thus the finite tangent surface packages the surviving multi-gap invariants into a genuine finite-type length spectrum and hence into standard Selberg/scattering data.

Known spectral perturbation theory and numerical scattering work show that eigenvalues/resonances/scattering data can vary when a finite-area cusped surface moves in Teichmuller space. The **count** of small eigenvalues can have a large topological component (PF-015), but their positions and the rest of the scattering/resonance data are not fixed solely by the cusp count.

The candidate relation is therefore

```text
recurrent isolated prime gap pattern H
  -> cusp-side ideal-polygon tangent Y_H
  -> ordinary finite-area spectral/scattering data of Y_H.
```

This is materially different from PF-022/PF-027: no divergent infinite-flute determinant is being regularized, and no universal pinching factor is being mistaken for arithmetic information.

## 7. What remains before claiming implantation into the spectrum of the full flute

The exact finite algebra does **not yet prove**

```text
C_{P_j} Gamma_prime C_{P_j}^(-1) -> Gamma_H
```

in Chabauty topology.

The geometric reason this now looks plausible is much stronger than in PF-025: the known zero-twist fundamental polygon is symmetric with sides at the positive and negative endpoint sequences. Under `C_P`:

- the selected negative/mirror vertices converge to `-eta_i`;
- the two adjacent sides across growing exterior gaps tend to the two sides ending at `infinity`;
- all positive sides and all nonselected distant sides leave compact subsets;
- the surviving adjacent relative words are exactly the cusp generators of the finite ideal-polygon double.

But a proof must still exclude extra Chabauty-limit elements arising from long words. This is the main gate.

If exact pointed geometric convergence to `Y_H` is established for infinitely many occurrences of the same isolated pattern, then the usual compact-support transplantation/Weyl argument becomes legitimate again: `L^2` eigenvalues of `Y_H` below `1/4` would provide candidates for essential spectral points of the full prime-flute. That spectral implantation is **not** claimed here.

## 8. Literature / novelty check

The ingredients are standard separately:

1. zero-twist tight flutes admit explicit symmetric infinite ideal-polygon Fuchsian models;
2. the orientation-preserving subgroup of reflections in a finite ideal polygon uniformizes its double, a punctured sphere;
3. parabolic cusp generators of punctured-sphere groups have the matrix form `Q(c,D)` above and satisfy a product relation;
4. Chabauty convergence of discrete groups is the standard group-side language for pointed geometric convergence of hyperbolic quotients;
5. finite-area punctured spheres have the usual Selberg/scattering/resonance theory.

A targeted search for combinations of `prime gaps`, `tight flute`, `ideal polygon`, `punctured sphere`, and `Fuchsian` did not locate this prime-gap specialization or this cusp-side re-marking mechanism.

The potentially new content is therefore narrow and explicit:

```text
prime-flute relative holonomy has exact translational covariance;
```

and, under an isolated bounded prime pattern,

```text
the divergent absolute side-pairings cancel to the parabolic generators
of a finite ideal-polygon punctured-sphere tangent.
```

Do not claim novelty for ideal-polygon doubles, punctured-sphere spectral theory, or Chabauty convergence themselves.

## 9. Relation to PF-028

PF-028 remains correct.

The distinction is:

```text
positive-side recentering + individual G
  -> divergent cuff traces, no fixed marked finite surface;

cusp-side recentering + relative G_i G_j^(-1)
  -> finite parabolic/cross-ratio holonomy.
```

The distinguished cuffs still satisfy `ell_i -> infinity`. Their divergence is not erased. Instead it explains why the individual pairings disappear from the tangent while the relative cusp holonomy survives.

This is exactly the kind of singular re-marked/geometric limit PF-028 left open.

## Lean candidates

High-value finite targets:

1. prove dilation covariance of `G`;
2. prove exact translation covariance of `G(a,b)G(c,d)^(-1)`;
3. derive the adjacent limiting `Q(c,D)` matrices;
4. prove the telescoping product and the parabolic at infinity;
5. for three offsets, prove
   `sinh(L_12/4)^2=d_1/d_2` and its reciprocal partner.

The finite ideal-polygon uniformization and Chabauty/geometric convergence should remain imported theorem layers until the full-group limit is independently audited.