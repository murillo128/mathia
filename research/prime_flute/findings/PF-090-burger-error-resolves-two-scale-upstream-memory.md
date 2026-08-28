# PF-090 — Burger's quantitative graph estimate resolves the two-scale upstream-memory term in a moderate hierarchy

**Status:** `POSITIVE / RIGOROUS FINITE-TANGENT THEOREM + CONDITIONAL PRIME-REALIZATION GATE`.

PF-081 isolated, at graph/Feshbach level, the first genuinely interscale term for a three-pants chain with two shrinking separating geodesics.  The remaining concern was analytic: could the true hyperbolic-surface error be as large as the proposed `b^2/a` correction?

There is a nonempty two-scale window in which this concern can be removed immediately from Burger's classical *quantitative* surface-to-graph estimate.  No new collar PDE estimate is needed there.

The resulting statement is stronger than PF-081 in that, in this window, the `b^2/a` coefficient is a theorem for the actual Laplace eigenvalue (and hence for the associated resolvent pole), not merely for the effective graph/Ritz model.

## 1. Geometric setup

Let `Y(a,b)` be a finite-area hyperbolic surface of type `S_{0,5}` obtained as a chain of three pairs of pants, with the two internal separating geodesics having lengths

```text
a > b > 0.
```

The twists may be fixed; in the prime tangent they are the canonical zero-twist values.  Let

```text
A = {gamma_a, gamma_b}
```

be the resulting maximal pants decomposition.

The dual weighted graph has three vertices of Burger mass `1` (each limiting component is a pair of pants, so `2g-2+p+f=1`) and edge lengths `a,b`.  Its ordinary weighted Laplacian is

```text
G(a,b) =
[[ a,    -a,     0],
 [ -a, a+b,    -b],
 [  0,    -b,    b]].
```

The two nonzero graph eigenvalues are exactly

```text
mu_± = a+b ± sqrt(a^2-a b+b^2).
```

For `b/a -> 0`,

```text
boxed:
mu_-
 = 3 b/2
   - 3 b^2/(8a)
   + O(b^3/a^2).
```

The second term is PF-081's upstream-memory term: it is the Feshbach contribution from eliminating the stronger mode at scale `a`.

## 2. Burger's error parameter is controlled by `a`

Burger defines the cusp-neighborhood parameter of a partition by

```text
epsilon = l(A)/L(A),
```

where `l(A)` is the maximum partition length and `L(A)` is the minimum of `2 asinh(1)` and the length of a closed geodesic disjoint from the partition.

For the present maximal pants decomposition,

```text
l(A)=a.
```

Moreover, any closed geodesic shorter than `2 asinh(1)` is simple (the standard short-geodesic/collar fact used explicitly in Burger's Section 1.2).  A pair of pants has no nonperipheral simple closed geodesic.  Since `A` is maximal, there is therefore no closed geodesic of length `<2 asinh(1)` disjoint from `A`.  Hence

```text
L(A)=2 asinh(1)
```

and exactly

```text
boxed:
epsilon = a/(2 asinh(1)).
```

Thus Burger's estimate is uniform even if the second pinching length `b` is much smaller than `a`.

## 3. Quantitative Burger estimate

Theorem 1.1 of Burger (1990) gives, for fixed topology, constants depending only on the signature such that

```text
1/(2 pi^2) * (1-C sqrt(epsilon))
    <= lambda_i(surface)/lambda_i(graph)
    <= 1/(2 pi^2) * (1+O(epsilon log epsilon)).
```

The right-hand correction is smaller in absolute size than `sqrt(epsilon)` as `epsilon -> 0`.  Therefore, for the weak positive eigenvalue,

```text
boxed:
lambda_weak(Y(a,b))
 = mu_-(a,b)/(2 pi^2)
   + O(mu_-(a,b) sqrt(a)).
```

Since `mu_- ~ 3b/2`, this is

```text
lambda_weak
 = mu_-/(2 pi^2) + O(b sqrt(a)).
```

The key point is that the classical error has enough resolution to see the graph's next term provided that the two pinching scales are separated, but not *too* strongly separated.

## 4. A rigorous second-order interscale window

Assume

```text
a -> 0,
b/a -> 0,
a^(3/2)/b -> 0.
```

Equivalently,

```text
boxed:
a^(3/2) << b << a.
```

Then

```text
b sqrt(a) / (b^2/a)
 = a^(3/2)/b
 -> 0,
```

so Burger's entire surface-to-graph error is `o(b^2/a)`.

The graph Taylor remainder also obeys

```text
(b^3/a^2)/(b^2/a)=b/a -> 0.
```

Consequently the true hyperbolic eigenvalue satisfies

```text
boxed:
lambda_weak(Y(a,b))
 = 3 b/(4 pi^2)
   - 3 b^2/(16 pi^2 a)
   + o(b^2/a).
```

This proves, on an actual hyperbolic surface, the coefficient predicted by PF-081.

A convenient invariant form is

```text
boxed:
[(3 b/(4 pi^2))-lambda_weak]
  /(b^2/a)
 -> 3/(16 pi^2).
```

So the weak eigenvalue does not merely detect its own neck `b`: after subtracting the universal leading term, its first resolvable singular correction remembers the previous neck `a`.

## 5. Resolvent-pole consequence

For sufficiently small `a,b`, this eigenvalue lies in `(0,1/4)`.  Put

```text
lambda_weak = s_weak(1-s_weak),
1/2 < s_weak < 1.
```

This is a real pole parameter of the meromorphically continued resolvent.  Since

```text
s_weak = 1-lambda_weak+O(lambda_weak^2)
```

and

```text
lambda_weak^2 = O(b^2) = o(b^2/a),
```

the same interscale memory appears in the pole location:

```text
boxed:
s_weak
 = 1
   - 3 b/(4 pi^2)
   + 3 b^2/(16 pi^2 a)
   + o(b^2/a).
```

No claim is made here that this pole must occur as a pole of every individual cusp-scattering matrix entry; the resolvent-pole statement is the intrinsic one.

## 6. Exact prime-gap geometry

For four ordered prime-pattern offsets with consecutive internal gaps

```text
d_1, d_2, d_3,
```

PF-047/PF-081 give the exact orthogonal-circle/tangent neck identities

```text
sinh(a/4)^2 = d_1/d_2,
sinh(b/4)^2 = (d_1+d_2)/d_3.
```

In the hierarchical regime `d_1 << d_2 << d_3`,

```text
a ~ 4 sqrt(d_1/d_2),
b ~ 4 sqrt(d_2/d_3).
```

The moderate spectral-resolution window becomes

```text
boxed:
d_2^2 << d_1 d_3,

d_1^3 d_3^2 << d_2^5.
```

These conditions are compatible.  For example, a model hierarchy

```text
d_1 ~ 1,
d_2 ~ T,
d_3 ~ T^beta
```

lies in the window whenever

```text
boxed:
2 < beta < 5/2.
```

Thus the window is a genuine open multiscale regime, not an empty comparison of error terms.

## 7. Distinguished-cuff formulation

For a fixed prime pattern translated to large prime scale `P`, the distinguished prime-flute cuffs obey

```text
ell_i(P)=2 log(4P/d_i)+o(1).
```

Define the two adjacent cuff contrasts

```text
A = ell_1-ell_2,
B = ell_2-ell_3.
```

Then

```text
a ~ 4 exp(-A/4),
b ~ 4 exp(-B/4).
```

A particularly transparent sufficient regime is

```text
B/A -> theta,
1 < theta < 3/2,
A -> infinity.
```

Equivalently, more invariantly,

```text
B-A -> +infinity,
3A-2B -> +infinity.
```

In this regime the true Laplace eigenvalue has the cuff-contrast expansion

```text
boxed:
lambda_weak
 = (3/pi^2) exp(-B/4)
   - (3/(4 pi^2)) exp(-B/2+A/4)
   + o(exp(-B/2+A/4)).
```

This is a genuinely relational two-cuff law.  The subleading term involves both adjacent distinguished-cuff contrasts and cannot be reduced to a scalar statistic of the current gap alone.

## 8. Relation to PF-089

PF-089 showed that the scalar low-energy determinant erases this information:

```text
mu_+ mu_- = 3ab
```

exactly in the three-vertex graph.  Thus the `b^2/a` displacement in `mu_-` is compensated by the opposite displacement in `mu_+`.

PF-090 makes the surviving channel precise:

```text
individual eigenvalue / resolvent pole
    -> retains upstream memory,
scalar determinant
    -> cancels it.
```

This is why the useful observable must remain spectrally resolved rather than collapsed to one determinant value.

## 9. Interior/exterior duality

The input neck lengths are defined by the exact ordered cross-ratio/orthogonal-circle geometry.  Ambient inversion exchanges the interior and exterior circle pictures while preserving those cross-ratios and hence the same `a,b` data.  As in PF-017, this does not create a second intrinsic spectrum; it confirms that the interscale coefficient is independent of which ambient side is used to draw the construction.

## 10. Serious novelty check

The ingredients themselves are classical:

1. Burger's 1990 theorem gives the weighted-graph approximation and, crucially here, the explicit `O(sqrt(epsilon))` relative control uniformly over a fixed cusp neighborhood.
2. The eigenvalues of the three-vertex weighted path are elementary.
3. Feshbach/Schur-complement interpretation of a `1/a` denominator is standard perturbation theory.

The closest sharper analytic work located is Große--Rupflin (2019), which treats a **single** disconnecting collar and obtains optimal error rates / information on the polyhomogeneous expansion.  Chaudhary's 2021 Oxford thesis treats **multiple** collapsing geodesics but states its conclusion at first order in the collapsing lengths.  The recent Erchenko--Jakobson--Tsypin preprint (29 April 2026) studies the attainable spectra of weighted graph Laplacians associated to pants decompositions; its surface-to-graph statement is again a common-scale first-order limit, while its new results concern graph spectral flexibility.

Targeted searches for

```text
"b^2/a" + hyperbolic small eigenvalue,
"a^(3/2)" + collapsing geodesics,
two-scale / nested pinching + second-order Laplace eigenvalue
```

did not locate this coefficient or the moderate-hierarchy resolution argument.

Accordingly, no novelty is claimed for Burger's estimate or for graph perturbation theory.  The potentially new, narrow observation is that **Burger's classical first-order estimate is already quantitatively strong enough to promote a hierarchical graph correction to a rigorous second asymptotic term of the true hyperbolic Laplacian whenever `a^(3/2) << b << a`**, and that the exact prime-circle geometry converts this to the explicit two-cuff formula above.

## 11. Remaining arithmetic gate

PF-046/PF-054 prove recurrence of deliberately **arbitrarily strong** hierarchical prime patterns.  Those arguments give robust lower separation of successive scales but do not presently give the upper control needed to ensure

```text
a^(3/2) << b.
```

Therefore PF-090 does **not** claim that the existing Pintz/Maynard extraction already produces infinitely many prime tangents in this moderate window.

The remaining arithmetic question is now sharply isolated:

```text
Can one force a recurrent isolated four-prime pattern whose exact necks satisfy

a^(3/2) << b << a ?
```

Equivalently, in the simple gap-power model, can the isolation machinery be made to realize a controlled hierarchy with exponent

```text
2 < beta < 5/2 ?
```

If yes, the displayed second-order eigenvalue / resolvent-pole law becomes an unconditional recurrent prime-flute spectral channel.  If not, a sharper multi-collar analytic estimate than Burger's `O(sqrt(a))` error would still be needed to reach the super-hierarchical patterns already guaranteed by PF-054.

## References

- Marc Burger, *Small eigenvalues of Riemann surfaces and graphs*, Math. Z. 205 (1990), 395--420. Theorem 1.1 gives the quantitative graph/surface comparison used above. Primary PDF: https://ethz.ch/content/dam/ethz/special-interest/math/department/Research/Research_Groups/Burger/1990_Small_eigenvalues.pdf
- Nadine Große and Melanie Rupflin, *Sharp eigenvalue estimates on degenerating surfaces*, Comm. Partial Differential Equations 44 (2019), 573--612; arXiv:1701.08491.
- Asad Chaudhary, *Estimates for small eigenvalues of the Laplacian and conformal Laplacian on closed manifolds*, DPhil thesis, Oxford (2021/2022), DOI 10.5287/ora-6gq1r27gd.
- Alena Erchenko, Dmitry Jakobson, Allison Tsypin, *Flexibility of eigenvalues for graph Laplacians arising from genus 3 surfaces*, arXiv:2604.26308 (submitted 29 April 2026).
