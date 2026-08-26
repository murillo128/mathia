# PF-047 — hierarchical prime-gap patterns produce a weighted-path small spectrum

**Status:** `POSITIVE / EXACT-DERIVED + CLASSICAL-DEGENERATION`, conditional only on the fixed-pattern isolation lemma now audited in PF-046.

PF-045/PF-046 show that one may force recurrent isolated prime patterns of fixed cardinality whose selected offsets are arbitrarily hierarchical.  PF-045 used one internal ratio only to force `lambda_1 -> 0`.  The same exact tangent matrices contain substantially more information: **all prefix separating curves pinch simultaneously**, and the entire vector of small Laplace eigenvalues is asymptotic to the spectrum of a canonical weighted path graph whose edge weights are explicit functions of cumulative prime-gap ratios.

This gives a nontrivial multi-cuff spectral law.  It does not define a graph on the primes by hand: the graph is the standard dual graph of the stable hyperbolic degeneration, and its weights are the actual lengths of the pinching geodesics.

## 1. Exact prefix holonomy formula

Let

```text
H={eta_1<...<eta_r},
d_i=eta_{i+1}-eta_i,
```

and let `Y_H` be the finite cusp-side tangent of PF-029.  Its finite cusp parabolics are `Q_1,...,Q_r`, ordered along the ideal polygon.

For each

```text
k=2,...,r-1,
```

the product

```text
M_k=Q_1 Q_2 ... Q_k
```

represents the simple separating curve `gamma_k` enclosing the first `k` finite cusps.

Put

```text
S_k=eta_k-eta_1=d_1+...+d_{k-1}.
```

After translating `eta_1` to zero, direct induction on the exact matrices `Q(c,D)` gives, up to the irrelevant central sign in `SL(2,R)`,

```text
M_k = (+/-) [[1+2 S_k/d_k,  2 S_k(S_k+d_k)/d_k],
             [2/d_k,          1+2 S_k/d_k        ]].
```

Therefore

```text
boxed:
|tr M_k|/2 = 1+2 S_k/d_k.
```

If `L_k` is the geodesic length of `gamma_k`, then

```text
|tr M_k|/2=cosh(L_k/2),
```

so exactly

```text
boxed:
sinh(L_k/4)^2 = S_k/d_k
               = (d_1+...+d_{k-1})/d_k,
```

and

```text
boxed:
L_k = 4 asinh sqrt((d_1+...+d_{k-1})/d_k).
```

PF-029's four-punctured identity is the case `k=2`.

This formula uses the actual Fuchsian holonomy of the orthogonal-circle construction; no spectral or arithmetic weight has been chosen.

## 2. Super-geometric prime patterns pinch a complete pants decomposition

PF-046 constructs fixed candidate sets for arbitrary `B>2` with

```text
h_{j+1}>B h_j,
```

and extracts recurrent exact prime subsets

```text
eta_1<...<eta_r
```

of a fixed cardinality `r=r_*` along a subsequence `B->infinity`.

Any selected consecutive offsets still satisfy

```text
eta_{k+1}>B eta_k.
```

Hence

```text
S_k=eta_k-eta_1<eta_k,
d_k=eta_{k+1}-eta_k>(B-1)eta_k,
```

and therefore

```text
boxed:
S_k/d_k < 1/(B-1)
```

for every `k=2,...,r-1`.

Thus all `r-2` prefix curves satisfy

```text
boxed:
L_k <= 4/sqrt(B-1) -> 0.
```

The curves `gamma_2,...,gamma_{r-1}` are nested disjoint simple separating curves.  Since `Y_H` has type

```text
S_{0,r+1},
```

the number `r-2=(r+1)-3` is maximal: they form a complete pants decomposition.

Cutting along them produces exactly `r-1` pairs of pants.  By Gauss--Bonnet every component has area

```text
2 pi,
```

independently of its boundary lengths.  As `B->infinity`, every boundary geodesic becomes a cusp, so each component converges to the unique thrice-punctured sphere.

Therefore the stable limit is a **chain of `r-1` thrice-punctured spheres**.  Its dual graph is not selected by us: it is canonically the path

```text
P_{r-1}.
```

The collar lemma excludes additional transverse pinches: any simple geodesic intersecting one of these `r-2` collars has length tending to infinity.  Thus this is the complete stable degeneration associated with the hierarchical pattern.

## 3. Burger's graph asymptotics give the whole small spectrum

Burger's classical small-eigenvalue theorem associates to a degenerating hyperbolic surface a weighted graph:

- one vertex for each limiting component, with mass equal to its area;
- one edge for each pinching separating geodesic, with edge weight equal to its geodesic length.

If `lambda_j(Graph)` denotes the spectrum of the graph quadratic form

```text
sum_edges L_e (F_i-F_j)^2
```

with respect to the mass norm

```text
sum_vertices V_i F_i^2,
```

Burger proves

```text
lambda_j(surface)/lambda_j(Graph) -> 1/pi.
```

He explicitly notes that the result extends to geometrically finite surfaces.  That is the relevant case here: each `Y_H` is finite-area with cusps.

For our degeneration all vertex masses are exactly `2 pi`, and the graph is a path with edge conductances

```text
w_k=L_k,
k=2,...,r-1.
```

Let `G_B` be the ordinary `(r-1)x(r-1)` weighted path Laplacian

```text
G_B =
[[ w_2,          -w_2,              0, ...],
 [ -w_2, w_2+w_3,          -w_3, ...],
 [     0,    -w_3, w_3+w_4,      ...],
 ...].
```

Write

```text
0=mu_0(B)<mu_1(B)<=...<=mu_{r-2}(B)
```

for its eigenvalues.  Because the graph mass is `2 pi`, Burger's graph eigenvalues are `mu_j/(2 pi)`.  Consequently the `r-2` small positive eigenvalues of the tangent satisfy

```text
boxed:
lambda_j(Y_B)
 = (1/(2 pi^2)) mu_j(B) (1+o(1)),
 j=1,...,r-2.
```

The `o(1)` is along the degeneration `B->infinity`.  The remaining spectral channel stays separated from zero because the limiting components are fixed thrice-punctured spheres and the continuous spectrum begins at `1/4`.

Thus **the entire small spectrum, not only `lambda_1`, is controlled to first order by an explicit weighted path derived from prime-gap ratios.**

## 4. Explicit arithmetic edge weights

The graph edge weights are not arbitrary functions of the gaps.  They are the exact hyperbolic lengths

```text
boxed:
w_k
 = 4 asinh sqrt((d_1+...+d_{k-1})/d_k).
```

For a strongly hierarchical pattern,

```text
w_k
 = 4 sqrt((d_1+...+d_{k-1})/d_k)
   * (1+O(1/B)).
```

Since the last previous gap dominates the preceding sum in the super-geometric regime,

```text
(d_1+...+d_{k-1})/d_k
 = (d_{k-1}/d_k)(1+O(1/B)).
```

Hence, to leading order,

```text
w_k ~ 4 sqrt(d_{k-1}/d_k).
```

So the weighted graph records the hierarchy of **successive relative prime gaps**, while the hyperbolic surface turns those numbers into actual small Laplace eigenvalues through a theorem independent of arithmetic.

## 5. Exact formulation in terms of distinguished cuff contrasts

For a fixed bounded pattern occurring near a large prime scale `P`, the distinguished prime-flute cuffs satisfy

```text
ell_i(P)=2 log(4P/d_i)+o(1).
```

Therefore for every fixed pair of internal gaps,

```text
boxed:
d_i/d_k
 = lim_{P->infinity}
   exp(-(ell_i(P)-ell_k(P))/2).
```

The cumulative ratio in the exact pinching formula can therefore be written entirely in terms of **relative distinguished cuff lengths**:

```text
boxed:
sinh(L_k/4)^2
 = lim_{P->infinity}
   sum_{i=1}^{k-1}
   exp(-(ell_i(P)-ell_k(P))/2).
```

Thus the chain

```text
relative cuff vector
 -> exact prefix geodesic lengths L_k
 -> canonical weighted path G_B
 -> small spectrum of Delta_{Y_B}
 -> essential spectral points of Delta_{X_prime}
```

is mathematically forced.

It is crucial that only **differences** of cuffs survive.  The common divergence `2 log P` cancels, in agreement with the earlier negative results showing that one cuff alone carries only universal local spectral data.

## 6. The four-punctured special case gives a sharp first-order law

For `r=3` the tangent is a four-punctured sphere and there is one pinching edge `L_2`.  The weighted path has two vertices and one edge, so its nonzero ordinary graph eigenvalue is

```text
mu_1=2L_2.
```

Burger's asymptotic becomes

```text
boxed:
lambda_1(Y_H) ~ L_2/pi^2.
```

Using the exact gap ratio,

```text
boxed:
lambda_1(Y_H)
 ~ (4/pi^2) asinh sqrt(d_1/d_2)
 ~ (4/pi^2) sqrt(d_1/d_2)
```

as `d_1/d_2->0`.

Equivalently, in the corresponding large-prime realization,

```text
lambda_1(Y_H)
 ~ (4/pi^2) exp(-(ell_1-ell_2)/4).
```

PF-046 does not force the recurring selected subset to have exactly three primes, so this four-punctured formula is an exact spectral degeneration law for that topology rather than the unconditional global conclusion of the hierarchical construction.  The unconditional fixed-cardinality subsequence is described by the full weighted path above.

## 7. Implantation into the essential spectrum of the infinite flute

Each exact hierarchical pattern used above recurs infinitely often with exterior prime gaps tending to infinity.  PF-034 therefore applies to every corresponding tangent:

```text
Spec_L2(Delta_{Y_B}) cap (0,1/4)
  subset sigma_ess(Delta_{X_prime}).
```

For large `B`, all `r-2` graph-controlled eigenvalues are below `1/4`.  Hence the single deterministic prime-flute contains, in its essential spectrum, the small spectral vectors generated by these finite weighted paths.

This is stronger than merely proving accumulation at zero.  It identifies the first-order **finite-dimensional effective operator** governing the prime-derived spectral channels.

## 8. Novelty audit

The analytic mechanism is classical:

1. Burger's 1988/1990 theorems relate small Laplace eigenvalues of degenerating hyperbolic surfaces to weighted dual graphs;
2. the theorem explicitly extends to geometrically finite surfaces;
3. pants decompositions and stable nodal limits are standard Teichmuller theory.

The arithmetic isolation mechanism is PF-046's audited fixed-pattern extension of Pintz.

Targeted searches for combinations of `prime gaps`, `degenerating hyperbolic surface`, `weighted graph`, `small eigenvalues`, `punctured sphere`, and `Burger` did not locate this composition.  Searches do find ad hoc graph Hamiltonians whose vertices are primes and whose weights are chosen from prime gaps; those are categorically different.  Here the graph is **not an invented prime graph**: it is the canonical dual graph of an actual finite-area hyperbolic surface that occurs as a pointed tangent of the exact prime-flute.

The potentially new content is therefore the exact bridge

```text
(d_1,...,d_{r-1})
 -> L_k=4 asinh sqrt((d_1+...+d_{k-1})/d_k)
 -> weighted dual path
 -> asymptotic small Laplace spectrum
 -> essential spectrum of the prime-flute.
```

## 9. Limitations and next gate

- This does not identify Riemann zeros or establish RH.
- Burger's asymptotic is universal once the degenerating hyperbolic moduli are given; the arithmetic content is that these moduli are forced by recurrent prime patterns in the exact construction.
- The unordered spectrum of a weighted path need not trivially determine every edge weight uniquely for arbitrary path length.  No inverse-spectral injectivity is claimed here.
- The next genuinely stronger question is whether the **marked** scattering matrix, Dirichlet-to-Neumann data on the pants interfaces, or an appropriate spectral measure of the tangent recovers the weighted path (and hence the relative cuff/gap hierarchy) uniquely.  That would be an inverse-spectral statement rather than another restatement of the gap ratios.
