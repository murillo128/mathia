# PF-054 — sufficiently hierarchical prime necks make the unmarked small spectrum asymptotically inverse-readable

**Status:** `POSITIVE / EXACT-ARITHMETIC-GEOMETRY + ELEMENTARY MULTISCALE GRAPH LIMIT + CLASSICAL BURGER TRANSFER`.

PF-048 showed that the unordered small spectrum of a general weighted path is not inverse-unique. PF-049--PF-053 repaired this by retaining marked norming/scattering data. The strongest prime patterns available from PF-046, however, can be chosen much more hierarchical than PF-047 required. In that regime the spectral scales separate so strongly that the **unmarked eigenvalues themselves acquire an asymptotic ordering label** and recover the relative neck/gap hierarchy to first order.

The graph singular-perturbation mechanism is elementary and is compatible with Burger's classical multiscale analysis; novelty is not claimed for that mechanism. The prime-flute-specific content is that one can force recurrent isolated prime patterns for which the exact orthogonal-circle necks enter this regime, giving an explicit cuff-contrast/eigenvalue law inside the essential spectrum of the single infinite prime flute.

## 1. Strengthening the fixed-pattern construction to a scale hierarchy

PF-046 constructs an arbitrary fixed finite set of prime candidate offsets

```text
H={h_1<...<h_m}
```

subject to Pintz's finite divisibility conditions, and then applies the non-uniform fixed-pattern isolation lemma. Its CRT + Dirichlet induction has no upper-size restriction once `H` is fixed before the asymptotic variable is sent to infinity.

Fix `B>2`. We may therefore strengthen the induction as follows. Choose `h_1>m`, and after `h_1,...,h_j` have been chosen, use exactly the same allowed reduced residue class modulo the product of the previous `h_i`, but choose the next prime so large that

```text
h_{j+1} > B^4 h_j^2/h_1.
```

Dirichlet gives arbitrarily large primes in the allowed progression, so this extra lower bound costs nothing.

Consequently, for every triple of candidate offsets

```text
h_i<h_j<h_k,
```

we have

```text
(h_k/h_j)/(h_j/h_i)
 = h_k h_i/h_j^2
 > B^4.
```

Hence **every selected subsequence**

```text
a_1<a_2<...<a_r
```

of the candidate set inherits the ratio hierarchy

```text
A_t:=a_{t+1}/a_t,
A_{t+1}/A_t > B^4.
```

This is important: the Maynard--Tao step need not tell us which candidate primes survive. The hierarchy is robust under taking arbitrary subsets.

PF-046's one-sided isolation modification still applies unchanged, so an exact selected subset recurs infinitely often as a block of consecutive primes with the exterior gaps tending to infinity. Passing through `B->infinity` and then to a subsequence fixes the selected cardinality `r=r_*` exactly as in PF-046.

By taking the requested number `k0` of primes arbitrarily large before beginning the construction, `r_*` (and therefore the length of the spectral ladder below) can be made arbitrarily large.

## 2. Exact necks inherit a strict hierarchy

For a recurrent selected pattern

```text
H_B^*={a_1<...<a_r},
d_j=a_{j+1}-a_j,
```

PF-047 gives the exact separating necks

```text
L_k
 = 4 asinh sqrt((a_k-a_1)/(a_{k+1}-a_k))
 = 4 asinh sqrt((d_1+...+d_{k-1})/d_k),
```

for `k=2,...,r-1`.

Put

```text
A_j=a_{j+1}/a_j.
```

Since every `A_j -> infinity` and successive `A_j` grow by factors `>B^4`,

```text
d_j=a_j(A_j-1)=a_{j+1}(1+o_B(1)),
```

and

```text
(d_1+...+d_j)/d_{j+1}
 = (a_{j+1}-a_1)/(a_{j+2}-a_{j+1})
 = A_{j+1}^{-1}(1+o_B(1)).
```

Therefore, with the graph edge indexing

```text
w_j:=L_{j+1},
qquad j=1,...,N-1,
qquad N:=r-1,
```

we have

```text
boxed:
w_j
 = 4/sqrt(A_{j+1}) (1+o_B(1))
 = 4 sqrt(d_j/d_{j+1}) (1+o_B(1)).
```

Moreover

```text
boxed:
w_{j+1}/w_j
 = sqrt(A_{j+1}/A_{j+2})(1+o_B(1))
 < B^{-2}(1+o_B(1)).
```

Thus

```text
w_1 >> w_2 >> ... >> w_{N-1} > 0
```

with arbitrarily strong multiplicative separation, while all weights tend to zero.

## 3. Multiscale spectrum of a weighted path

Let `G(w)` be the ordinary weighted path Laplacian on `N` vertices,

```text
G(w)=sum_{j=1}^{N-1} w_j (e_j-e_{j+1})(e_j-e_{j+1})^T,
```

with

```text
0=mu_0<mu_1<...<mu_{N-1}.
```

Assume

```text
w_{j+1}/w_j -> 0
```

for every `j`. Then

```text
boxed:
mu_{N-j}
 = ((j+1)/j) w_j (1+o(1)),
qquad j=1,...,N-1.
```

### Proof sketch

Fix `j` and divide the quadratic form by `w_j`.

- Every stronger edge `i<j` has coefficient `w_i/w_j -> infinity`, so every bounded-energy vector must satisfy
  ```text
  x_1=...=x_j.
  ```
  The first `j` vertices contract to a single vertex of mass `j`.
- The edge `j` has limiting conductance `1` and connects that mass-`j` vertex to vertex `j+1`, of mass `1`.
- Every weaker edge `i>j` has coefficient `w_i/w_j ->0`, so the remaining vertices are disconnected at this scale.

The only nonzero finite eigenvalue created at this scale is therefore the nonzero generalized eigenvalue of a two-vertex graph with masses `j` and `1` joined by unit conductance:

```text
1/j + 1 = (j+1)/j.
```

The stronger-edge modes have already escaped to infinity on this scale and the weaker-edge modes remain at zero. Min--max (equivalently Schur-complement singular perturbation) identifies this finite mode with `mu_{N-j}/w_j`, proving the formula.

This is the standard contraction picture for a graph with widely separated conductances. Burger's own proof already allows normalized pinching lengths to converge to zero and then passes to the subgraph of nonzero limiting edges, so the existence of successive graph scales is not a new degeneration principle.

## 4. Explicit surface eigenvalue ladder

Burger's theorem, with every limiting pants component of area `2 pi`, gives PF-047's relation

```text
lambda_q(Y_B)
 = mu_q(G(w))/(2 pi^2) (1+o(1)).
```

Combining with the path lemma yields, for `j=1,...,N-1`,

```text
boxed:
lambda_{N-j}(Y_B)
 = (j+1)/(2 pi^2 j) w_j (1+o(1)).
```

Using the exact prime-derived neck asymptotic,

```text
boxed:
lambda_{N-j}(Y_B)
 = 2(j+1)/(pi^2 j)
   sqrt(d_j/d_{j+1})
   (1+o(1)).
```

Thus the sorted **unmarked** small spectrum already labels the successive gap scales. Inverting the leading relation gives

```text
boxed:
d_j/d_{j+1}
 = [pi^2 j/(2(j+1))]^2
   lambda_{N-j}(Y_B)^2
   (1+o(1)).
```

This does not contradict PF-048. PF-048 gives exact isospectral weighted paths at finite, non-separated weights. PF-054 says that on this much thinner singular family, different edges occupy asymptotically disjoint spectral scales, so the ordering of the eigenvalues itself supplies the missing labels.

## 5. Direct law in terms of the distinguished cuffs

For an occurrence of the same bounded pattern near large prime scale `P`, the distinguished cuffs satisfy

```text
ell_j(P)=2 log(4P/d_j)+o(1).
```

Hence

```text
sqrt(d_j/d_{j+1})
 = exp(-(ell_j(P)-ell_{j+1}(P))/4)(1+o_P(1)).
```

Therefore the multiscale tangent law becomes

```text
boxed:
lambda_{N-j}(Y_B)
 ~ 2(j+1)/(pi^2 j)
    exp(-(ell_j-ell_{j+1})/4),
qquad j=1,...,N-1.
```

The order of limits is the one forced by the construction: first take the large-prime occurrence of each fixed recurrent pattern to form its tangent/cuff contrast, then take the hierarchy parameter `B->infinity`.

This is the sharp form of the qualitative lesson accumulated since PF-032/PF-037:

```text
one cuff -> universal local cylinder data,
but successive cuff contrasts -> distinct genuine low-energy scales.
```

## 6. Essential spectral ladders in the single infinite prime flute

Every exact selected pattern recurs infinitely often with exterior gaps tending to infinity, so PF-034 implants every small tangent eigenvalue into the essential spectrum of the same infinite surface:

```text
lambda_q(Y_B) in sigma_ess(Delta_Xprime).
```

Because

```text
w_{j+1}/w_j ->0,
```

the positive small eigenvalues satisfy, in increasing order,

```text
lambda_1 << lambda_2 << ... << lambda_{N-1} << 1/4.
```

More quantitatively, after choosing the candidate hierarchy strongly enough,

```text
lambda_q/lambda_{q+1} ->0
```

for every adjacent pair in the finite ladder.

Since `k0` can be chosen arbitrarily large before running PF-046, the prime flute contains **arbitrarily long finite ladders of positive essential spectral points with arbitrarily strong multiplicative separation**, all generated at fixed topology within each `B`-subsequence by relative prime-gap/cuff moduli.

This substantially strengthens PF-043's statement that positive essential points merely accumulate at zero.

## 7. Relation to PF-053 and multiscale scattering

PF-053 proves, for a fixed positive graph shape,

```text
epsilon/pi * Phi_epsilon^mark(1-epsilon z/(2 pi^2))
 -> (G_a-zI)^(-1).
```

The present hierarchy is outside that single-scale hypothesis because the normalized graph weights themselves tend to zero successively.

PF-054 shows what the iterated blow-up must see at the **eigenvalue level**: at scale `w_j`, stronger edges contract, weaker edges disappear, and the surviving quotient is the two-mass edge with eigenvalue `(j+1)/j`.

Thus an eventual multiscale extension of PF-053 should not be guessed arbitrarily. Its successive scattering blow-ups are forced to converge to the resolvents of these contracted quotient graphs / Schur complements. Proving that matrix-valued statement remains a separate analytic problem.

## 8. Serious novelty check

Known components, for which no novelty is claimed:

- Burger's weighted-graph description of small eigenvalues of degenerating hyperbolic surfaces, including geometrically finite surfaces.
- Burger's proof already accommodates subsequential normalizations in which some edge-length ratios tend to zero; this substantially limits any novelty claim for `multiple pinching rates -> graph filtration` itself.
- Singular perturbation / contraction of weighted graph Laplacians and Schur complements are standard.
- Hyperbolic surfaces can approach boundary strata with pinching curves at wildly different rates; this phenomenon is standard in moduli-space geometry.
- Prime gaps have been connected to spectra of deliberately constructed graphs in prior literature (for example almost-Ramanujan graph constructions), but those graphs are not the dual graphs of the exact prime-flute geometry.

Directed searches for combinations of

```text
prime gaps + hyperbolic surface + small Laplace eigenvalues,
consecutive prime gaps + degenerating Riemann surface,
prime gaps + weighted dual graph + hyperbolic spectrum,
hierarchical pinching + weighted-path eigenvalue asymptotics
```

found the adjacent theories above but no instance of the exact prime-flute composition or the displayed cuff-contrast law.

The candidate-new content is therefore narrowly the forced chain

```text
super-hierarchical recurrent consecutive-prime pattern
 -> exact orthogonal-circle neck hierarchy
 -> canonically weighted dual path
 -> asymptotically labelled unmarked Laplace eigenvalues
 -> essential spectral ladder of the infinite prime flute,
```

and in particular the explicit first-order relation

```text
lambda_{N-j}
 ~ 2(j+1)/(pi^2 j)
    exp(-(ell_j-ell_{j+1})/4).
```

No historical-priority claim is made.

## 9. Limitations

- This does not identify Riemann zeros and is not an RH proof mechanism by itself.
- The spectral ladder is forced using deliberately very spread-out fixed candidate patterns; it establishes what the exact prime flute **contains**, not a statistical law for typical consecutive prime gaps.
- The inverse-readable statement is asymptotic in the hierarchical regime, not an exact finite-weight uniqueness theorem.
- The fixed-pattern Pintz extraction in PF-046 is a proof-level non-uniform extension that should receive specialist analytic-number-theory review before publication.
- A full multiscale scattering theorem extending PF-053 would be a stronger analytic result, but is not needed for the Laplace-eigenvalue ladder proved here.
