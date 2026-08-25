# PC-012 — finite cross-level edge geometry embeds in a single regular-polygon diagonal arrangement

**Status:** `DECISIVE-NEGATIVE` for unlabeled finite edge-incidence / crossing-geometry novelty.

## Statement

Let \(S=\{n_1,\dots,n_r\}\subset \mathbb N\) be any finite set of polygon levels and let

\[
L=\operatorname{lcm}(n_1,\dots,n_r).
\]

For each \(n\mid L\), every vertex of the regular \(n\)-gon

\[
P_n=\{e^{2\pi i j/n}:0\le j<n\}
\]

is a vertex of \(P_L\):

\[
e^{2\pi i j/n}=e^{2\pi i (jL/n)/L}.
\]

Hence every edge of \(P_n\), joining consecutive \(n\)-th roots, is exactly the chord of \(P_L\) joining vertex indices

\[
\frac{jL}{n}
\quad\text{and}\quad
\frac{(j+1)L}{n}.
\]

Therefore the full finite arrangement of edges coming from all levels in \(S\) is a **labeled subarrangement of the complete diagonal/chord arrangement of one regular \(L\)-gon**.

Consequently every finite geometric datum that forgets the level labels — intersection coordinates, inside/outside location, radii, angles, concurrency multiplicities, and incidence relations — is inherited from the classical diagonal arrangement of \(P_L\).

## Why this closes an important branch

After PC-009 and PC-011, a natural remaining proposal was to keep the full two-dimensional crossing geometry between several polygon levels rather than collapsing it to crossing counts or one-dimensional chord statistics. The lcm embedding shows that, for every finite collection of levels, this does **not** create a new geometric category: it is a selected set of diagonals of a single regular polygon.

The literature on regular-polygon diagonal arrangements is already deep:

- Poonen and Rubinstein classify the interior intersection problem using trigonometric Diophantine equations and vanishing sums of roots of unity, obtain exact intersection-count formulas, and classify possible concurrency multiplicities. In particular, away from the center no more than seven diagonals can concur.
- Their concurrency criterion for three diagonals is converted to a vanishing sum of twelve roots of unity, placing the incidence geometry directly inside cyclotomic-relation theory.
- Rigby had already studied multiple intersections of diagonals of regular polygons.
- Ryckelynck and Smoch (2026) go beyond counts and study the actual distribution of intersection points, both inside and outside the unit circle, including their circular orbits, radii, and multiplicities. Their squared-radius function \(J_n\) is written explicitly in terms of the four endpoint indices.

Thus the branch

\[
\text{several polygon levels}
\to
\text{2D crossing positions / radii / concurrence}
\to
\text{new RH geometry}
\]

is not a promising novelty route **if the level labels are discarded**.

## Exact surviving sector

This does **not** say that the prime-circle construction is exhausted. The lcm embedding preserves geometry but forgets why a particular diagonal was selected.

For example, if the chosen levels are primes \(p\mid L\), the edges of \(P_p\) become the special step-\(L/p\) diagonals of \(P_L\). A genuinely new invariant would therefore have to use at least one of:

1. the **level/birth label** attached to each selected diagonal;
2. the arithmetic rule selecting the subarrangement (e.g. prime or primitive levels), rather than the complete clique arrangement;
3. the **dynamics as the finite window grows**, so that no single fixed \(L\) captures the object;
4. off-edge structures such as the primitive-shell potential field and its interior/exterior harmonic duality.

In particular, merely using more detailed finite crossing coordinates than PC-009 does not by itself escape the classical regular-polygon diagonal literature.

## Literature check

- B. Poonen and M. Rubinstein, *The Number of Intersection Points Made by the Diagonals of a Regular Polygon*, SIAM J. Discrete Math. 11 (1998), 135–156. DOI: 10.1137/S0895480195281246. Preprint: https://math.mit.edu/~poonen/papers/ngon.pdf
- J. Rigby, *Multiple intersections of diagonals of regular polygons, and related topics*, Geometriae Dedicata 9 (1980), 207–238.
- P. Ryckelynck and L. Smoch, *Simuorb: a new method for generating and describing the intersection points of clique-arrangements*, Numerical Algorithms (published 3 July 2026). DOI: 10.1007/s11075-026-02414-8.
- The cyclotomic reduction used by Poonen–Rubinstein is closely related to Conway–Jones and the broader theory of vanishing sums of roots of unity.

## Research consequence

Treat the unlabeled finite edge arrangement as **prior art / control geometry**, not as a primary source of novelty. Future edge-based work should keep the arithmetic labels and study a growing prime-selected subarrangement, or return to off-circle fields where the lcm reduction does not collapse the construction to a standard clique arrangement.
