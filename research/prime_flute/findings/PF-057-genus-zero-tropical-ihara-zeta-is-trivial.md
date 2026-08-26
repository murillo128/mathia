# PF-057 — genus-zero prime tangents have trivial tropical/Ihara zeta

**Status:** `DECISIVE-NEGATIVE` for the branch “prime-tangent degeneration -> dual graph -> Ihara/Ruelle graph zeta -> RH-type spectral signal”.

## 1. Why this branch is natural

PF-047–PF-056 show that isolated prime patterns can produce finite-area genus-zero hyperbolic tangents whose short separating curves are determined exactly by multi-gap cross-ratios. In the hierarchical regime, pinching these curves gives a weighted path and the small Laplace spectrum is controlled by the corresponding weighted graph Laplacian.

A very natural next step is therefore to ask whether the same graph carries an Ihara-type zeta, especially because Ihara zeta is the standard graph analogue of Selberg zeta and possesses a graph-theoretic “Riemann hypothesis” in the Ramanujan setting.

Recent work of Li–Matheus–Pan–Tao, *Selberg, Ihara and Berkovich* (arXiv:2412.20754), makes this route especially relevant: for certain degenerating Schottky/Kleinian surfaces, a rescaled Selberg zeta converges to the Ihara zeta of a limiting finite graph. Their theorem does **not** directly apply to the present finite-area cusped tangents, but it confirms that “hyperbolic degeneration -> graph Ihara zeta” is a standard and mathematically natural candidate rather than an ad hoc construction.

## 2. Every stable degeneration of a prime tangent has tree dual graph

Every prime tangent from PF-029/PF-034 is a punctured sphere

\[
Y_H\cong S_{0,n}
\]

for some finite number of cusps \(n\).

For a stable nodal degeneration, let \(G\) be the dual graph, with a vertex for every irreducible component and an edge for every node. The arithmetic genus satisfies the standard formula

\[
g(Y_H)=\sum_{v\in V(G)} g_v+b_1(G).
\]

Since \(g(Y_H)=0\), both nonnegative terms must vanish:

\[
\boxed{g_v=0\ \forall v,\qquad b_1(G)=0.}
\]

Hence

\[
\boxed{G\text{ is always a tree}.}
\]

In the nested prime-gap degeneration of PF-047 the tree is more specifically

\[
\boxed{G=P_N}
\]

for a finite path \(P_N\). This conclusion is independent of the actual edge lengths, collar capacities, or prime-gap ratios.

This is the standard geometry of \(\overline{\mathcal M}_{0,n}\): genus-zero stable curves have dual trees.

## 3. Ihara zeta of a tree is identically one

For a finite graph \(G\), the Ihara zeta is

\[
Z_G(u)=\prod_{[C]}(1-u^{\ell(C)})^{-1},
\]

where \([C]\) runs over primitive reduced/non-backtracking closed cycles.

A tree has no such cycles. Therefore the Euler product is empty and

\[
\boxed{Z_G(u)\equiv 1.}
\]

The same is true for the usual weighted/metric-length Ihara product: assigning arbitrary positive lengths or weights to the edges does not create a closed non-backtracking cycle.

Equivalently, the Hashimoto non-backtracking edge operator on a finite tree is nilpotent, so

\[
\boxed{\det(I-uB)=1.}
\]

Thus all weights that PF-047/PF-056 derive from the exact orthogonal-circle geometry,

\[
L_k=4\operatorname{arsinh}\sqrt{\frac{d_1+\cdots+d_{k-1}}{d_k}},
\]

or the exact collar conductances \(\kappa(L_k)\), disappear completely from the standard Ihara/Ruelle graph zeta.

## 4. The graph-RH analogy is therefore vacuous here

The familiar “Riemann hypothesis for graphs” concerns the location of nontrivial poles of Ihara zeta and, for regular graphs, is equivalent to the Ramanujan property.

For the prime tangent skeleton,

\[
Z_G\equiv1,
\]

so there are no nontrivial poles at all. Any graph-RH statement is vacuous and cannot encode the prime-gap hierarchy.

Therefore the chain

\[
\boxed{
\text{prime gaps}
\to
\text{hyperbolic tangent}
\to
\text{tropical/dual graph}
\to
\text{Ihara zeta}
\to
\text{RH mechanism}
}
\]

is structurally dead.

This is stronger than saying that the particular hierarchical path has no cycles: **every** stable degeneration of every genus-zero prime tangent has a tree as dual graph, so changing the pinching pattern cannot rescue the branch while remaining inside the same genus-zero tangent geometry.

## 5. A standard quantum-graph replacement also loses the gap profile

One could instead metrize the path and use the ordinary Kirchhoff quantum-graph Laplacian. But every interior vertex of a path has degree two, and standard/Kirchhoff degree-two vertices are spectrally inessential. They can be suppressed without changing the operator.

Hence a metric path with edge lengths \(a_1,\ldots,a_{N-1}\) is spectrally just one interval of total length

\[
\boxed{A=a_1+\cdots+a_{N-1}.}
\]

Its ordinary quantum-graph spectral determinant or wave spectrum can see at most this aggregate length (together with the chosen endpoint boundary conditions), not the ordered gap vector.

This is the same subdivision-invariance mechanism already encountered in PF-026, now applied to the graph emerging from the genuine two-dimensional degeneration.

## 6. What survives

This negative does **not** invalidate PF-047–PF-056. Their successful effective object is not a cycle zeta and not a standard metric path. It is the **weighted combinatorial Laplacian / resolvent** whose edge weights are conductances or pinching lengths:

\[
G_H=\operatorname{Laplacian}_{\rm weighted}(P_N).
\]

That operator can retain the edge-weight profile even though the underlying graph is a tree. Its finite pseudodeterminant, endpoint spectral measure, Jacobi \(m\)-function, and scattering scaling limits remain nontrivial.

What PF-057 rules out is specifically the temptation to turn the successful graph limit into a Selberg-like Euler product over graph “primes”. There are no graph primes to multiply over.

## 7. Interior/exterior duality does not rescue the cycle zeta

The original orthogonal-circle inversion produces the ambient interior/exterior duality, but PF-017 already established that this is not a second intrinsic sheet of the hyperbolic quotient. On the tangent degeneration it gives a mirrored geometric presentation, not an additional canonical edge joining two copies of the dual tree.

Artificially gluing the two trees to manufacture graph cycles would therefore introduce new topology not present in the hyperbolic surface.

## 8. Novelty check

The ingredients of the negative result are classical:

- stable genus-zero curves have tree dual graphs;
- Ihara zeta is an Euler product over primitive reduced closed graph cycles;
- the Ihara zeta of a tree is therefore \(1\);
- degree-two Kirchhoff vertices on metric graphs are spectrally inessential.

The recent Selberg-to-Ihara degeneration result of Li–Matheus–Pan–Tao is close prior art for the *idea* of looking for an Ihara limit of a degenerating Selberg zeta, though their Schottky setting has nontrivial graph cycles and is analytically different from the present cusped genus-zero tangents.

No novelty is claimed for the abstract theorem “tree -> trivial Ihara zeta”. The substantive conclusion for the prime-flute program is that **the most canonical graph-zeta continuation of the PF-047/PF-056 reduction is guaranteed to erase all prime-gap data**.

## Research consequence

Do not pursue Ihara/Bass/non-backtracking Euler products of the dual graph as a route to RH. The graph-level objects still worth studying are operator-valued/Dirichlet-form objects (weighted Laplacian, resolvent, endpoint spectral measure, scattering blow-up), because these retain edge weights on a tree without requiring closed cycles.
