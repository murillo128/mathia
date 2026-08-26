# PF-048 — the small tangent spectrum has a canonical gap determinant, but is not inverse-unique

**Status:** `MIXED / POSITIVE-INVARIANT + DECISIVE-NEGATIVE` for recovering the full relative cuff/gap hierarchy from the unordered leading small spectrum alone.

PF-047 identifies the complete small spectrum of a hierarchical prime-derived tangent, to first order, with the spectrum of a canonical weighted path. This finding asks the next inverse-spectral question: does that unordered small spectrum determine the path weights, and therefore the relative prime gaps/cuffs?

The answer is **no in the ambient hyperbolic tangent family**. There are distinct positive weighted paths, not related by reversal, with exactly the same Laplacian spectrum. At the same time, one nontrivial symmetric invariant survives canonically: the product of all small eigenvalues is asymptotic to the product of the pinching lengths, hence to an explicit multiplicative functional of the relative gap/cuff hierarchy.

No claim is made here that an exactly isospectral pair has already been realized by two integer prime-offset patterns. The negative result is for the effective geometric inverse map supplied by PF-047; injectivity on the much thinner prime-derived integer subclass remains open.

## 1. PF-047 setup

Let

```text
H={eta_1<...<eta_r},
d_i=eta_{i+1}-eta_i.
```

For `k=2,...,r-1`, the exact separating length in the cusp-side tangent `Y_H` is

```text
L_k = 4 asinh sqrt(R_k),
R_k = (d_1+...+d_{k-1})/d_k.
```

In the hierarchical degeneration all `L_k -> 0`, and the stable dual graph is the path on

```text
N=r-1
```

vertices with edge conductances

```text
w_k=L_k,   k=2,...,r-1.
```

Let `G_H` be its ordinary symmetric weighted Laplacian and

```text
0=mu_0<mu_1<=...<=mu_{r-2}
```

its eigenvalues. Burger's small-eigenvalue asymptotic, with all component areas equal to `2 pi`, gives

```text
lambda_j(Y_H)
 = mu_j/(2 pi^2) * (1+o(1)),
 j=1,...,r-2.
```

The number `r` is fixed while the hierarchy tends to infinity, so products of the finitely many `1+o(1)` factors remain `1+o(1)`.

## 2. A canonical reduced determinant survives

For a connected weighted graph with `N` vertices, Kirchhoff's weighted Matrix-Tree theorem gives

```text
prod_{j=1}^{N-1} mu_j
 = N * tau_w(G),
```

where `tau_w(G)` is the weighted spanning-tree enumerator.

A path is already a tree, so it has exactly one spanning tree and

```text
tau_w(P_N)=prod_edges w_e.
```

Therefore the PF-047 path satisfies exactly

```text
boxed:
prod_{j=1}^{r-2} mu_j
 = (r-1) prod_{k=2}^{r-1} L_k.
```

Combining with Burger gives the finite tangent small-spectrum invariant

```text
boxed:
prod_{j=1}^{r-2} lambda_j(Y_H)
 = (r-1)/(2 pi^2)^(r-2)
   * prod_{k=2}^{r-1} L_k
   * (1+o(1)).
```

Substituting the exact prime-gap geometry,

```text
boxed:
prod_{j=1}^{r-2} lambda_j(Y_H)
 = (r-1)/(2 pi^2)^(r-2)
   * prod_{k=2}^{r-1}
       [4 asinh sqrt((d_1+...+d_{k-1})/d_k)]
   * (1+o(1)).
```

In the strongly hierarchical regime,

```text
L_k
 = 4 sqrt((d_1+...+d_{k-1})/d_k) * (1+o(1)),
```

hence

```text
boxed:
prod_{j=1}^{r-2} lambda_j(Y_H)
 ~ (r-1) (2/pi^2)^(r-2)
    prod_{k=2}^{r-1}
    sqrt((d_1+...+d_{k-1})/d_k).
```

Using the distinguished cuffs from PF-047,

```text
(d_1+...+d_{k-1})/d_k
 = lim_{P->infinity}
   sum_{i<k} exp(-(ell_i(P)-ell_k(P))/2),
```

so the same reduced determinant is a canonical spectral aggregate of the **relative cuff vector**.

This should not be confused with a zeta-regularized determinant of the infinite prime-flute; PF-033/PF-035 rule out the ordinary global constructions. It is simply the finite product of the genuine small eigenvalues of the finite tangent, and its graph-side interpretation is forced by the degeneration.

## 3. Exact isospectral weighted paths: the inverse map is not injective

For a path on five vertices with positive edge weights

```text
(a,b,c,d),
```

the weighted Laplacian has characteristic polynomial

```text
det(x I-L)
 = x [
     x^4
     -2(a+b+c+d)x^3
     +(3ab+4ac+4ad+3bc+4bd+3cd)x^2
     -(4abc+6abd+6acd+4bcd)x
     +5abcd
   ].
```

Now take

```text
w       = (1,4,6,4),
w_tilde = (2,3,2,8).
```

They are positive and are not related by path reversal. Direct exact substitution gives in both cases

```text
boxed:
det(x I-L)
 = x (x^4 - 30 x^3 + 260 x^2 - 720 x + 480).
```

Thus

```text
boxed:
Spec(L_w)=Spec(L_w_tilde)
```

with genuinely different edge-weight vectors.

This is an exact algebraic counterexample, not a numerical near-collision.

Scaling every edge by any `epsilon>0` scales the Laplacian by `epsilon`, so

```text
epsilon*w
and
epsilon*w_tilde
```

remain exactly isospectral for every `epsilon`. Letting `epsilon -> 0` places both families directly in the all-necks-pinching regime relevant to Burger/PF-047.

Hence the leading unordered small spectrum of the surface cannot, in general, recover the complete vector of pinching weights.

## 4. The counterexample lies inside the ambient prime-tangent geometry

The PF-047 map from positive real gap profiles to positive pinching lengths is surjective at the level needed here.

Given arbitrary target lengths

```text
L_2,...,L_{r-1}>0,
```

set

```text
R_k = sinh(L_k/4)^2.
```

Choose any `d_1>0` and recursively define

```text
boxed:
d_k = (d_1+...+d_{k-1})/R_k,
       k=2,...,r-1.
```

Then every `d_k>0` and, by construction,

```text
(d_1+...+d_{k-1})/d_k = R_k,
```

so the exact prime-flute tangent formula returns precisely the prescribed `L_k`.

For the scaled isospectral pairs `epsilon*w` and `epsilon*w_tilde`,

```text
R_k = sinh(epsilon w_k/4)^2
    ~ epsilon^2 w_k^2/16,
```

and the recursion makes successive gaps strongly hierarchical as `epsilon -> 0`. Therefore the nonuniqueness is not outside the geometric regime used in PF-047: it occurs arbitrarily deep inside its degenerating real-moduli model.

**Arithmetic caveat.** The recursively produced `d_k` are positive real gap lengths. This does not yet give two exact integer offset patterns, let alone two recurrent prime patterns, with identical graph spectra. The conclusion proved here is therefore:

```text
the effective leading small-spectrum map
(real prime-tangent moduli -> unordered spectrum)
is non-injective.
```

A separate arithmetic rigidity theorem would be required to show injectivity after restricting to the sparse subset of actually realizable prime-offset patterns. No such theorem is known here.

## 5. What the spectrum does and does not retain

The exact isospectral pair shows that the full unordered list

```text
(mu_1,...,mu_{r-2})
```

contains fewer recoverable degrees of freedom than the ordered edge vector in a globally injective sense.

Nevertheless it determines nontrivial symmetric combinations. In particular the Matrix-Tree identity forces

```text
prod_edges L_k
 = (1/(r-1)) prod_{j=1}^{r-2} mu_j,
```

so any isospectral pair must have the same edge product. The explicit example indeed satisfies

```text
1*4*6*4 = 2*3*2*8 = 96.
```

At the surface level this is exactly the small-spectrum product in Section 2.

Thus PF-047 should be interpreted as providing a genuine spectral image of the relative gap/cuff hierarchy, but **not an injective encoding by eigenvalues alone**.

## 6. Literature check: extra marked data are standard in inverse graph problems

The negative conclusion is consistent with inverse-spectral graph theory rather than being an anomaly of the example.

- Parlangeli (2023), *A Distributed Algorithm for the Assignment of the Laplacian Spectrum for Path Graphs*, treats inverse eigenvalue assignment for weighted paths and uses additional polynomial/interlacing structure rather than asserting that an arbitrary symmetric edge-weight vector is uniquely recovered from the unordered Laplacian spectrum alone.
- Blåsten--Isozaki--Lassas--Lu (J. Spectr. Theory 2023), *Gel'fand's inverse problem for the graph Laplacian*, recover weighted graphs from **boundary spectral data** `(lambda_j, phi_j|_B)`, not from eigenvalues alone.
- Gernandt--Rohleder, *A Calderón type inverse problem for tree graphs*, recover a weighted tree from a boundary Dirichlet-to-Neumann matrix.
- The weighted Matrix-Tree theorem and Burger's surface-to-graph asymptotics used above are classical.

Directed searches did not locate the explicit isospectral pair `(1,4,6,4)` / `(2,3,2,8)` in the literature. Historical novelty is not important for the conclusion: the pair is a short exact certificate that the desired inverse map cannot be globally injective.

## 7. Research consequence

This closes the branch

```text
relative prime cuffs
 -> PF-047 weighted path
 -> unordered small eigenvalues alone
 -> unique reconstruction of all relative gaps.
```

The next legitimate inverse-spectral target must retain **marked data forced by the finite tangent geometry**, for example:

1. boundary values/norming constants of the small eigenfunctions on the two end pants;
2. a Dirichlet-to-Neumann map on canonically chosen pants interfaces;
3. the marked finite-cusp scattering matrix of `Y_H`;
4. a spectral measure relative to a geometrically distinguished end/cusp.

These are standard types of data that can remove graph inverse ambiguities, but they will count as progress here only if the marking comes from the exact orthogonal-circle / tangent construction rather than being added solely to force uniqueness.

The positive invariant from this finding should also be retained:

```text
small-spectrum pseudodeterminant
 <-> product of true pinching lengths
 <-> explicit product of cumulative relative prime-gap/cuff ratios.
```

It is a finite, geometrically forced spectral quantity and avoids the global determinant obstructions of the infinite flute, while not pretending to encode more arithmetic information than it actually does.
