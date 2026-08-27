# PF-079 — multiscale physical scattering tropicalizes to contracted prime-gap graphs

**Status:** `POSITIVE / PROOF-LEVEL MULTISCALE CONSEQUENCE OF PF-054 + PF-078`, with the arithmetic realization inheriting PF-046/PF-054's specialist-review caveat.

PF-078 proves that, for a finite prime tangent whose separating necks pinch with one fixed positive shape, the marked physical cusp-scattering matrix has a singular scaling limit equal to the resolvent of Burger's weighted dual graph. PF-054 supplies the arithmetically stronger family actually forced by the prime construction: the necks may be chosen recursively hierarchical,

\[
w_1\gg w_2\gg\cdots\gg w_{N-1}>0,
\qquad
\frac{w_{i+1}}{w_i}\to0,
\qquad
w_i\to0.
\]

The fixed-shape hypothesis is not needed if the PF-078 low/high argument is formulated with spectral **clusters/projectors** rather than individual modes. At each neck scale the physical scattering tropicalizes to the resolvent of the graph obtained by contracting all stronger edges and deleting all weaker edges. For the prime path this quotient has one nonzero edge mode, so one marked scattering channel has an explicit universal rational profile. The prime information lies in the nested physical scales at which those profiles occur.

This closes the analytic mismatch between PF-054's unconditional multiscale geometry and PF-078's previously stated fixed-shape scattering theorem.

## 1. Hierarchical prime-neck family

Let `Y_nu` be a fixed-topology finite prime tangent with `N` limiting pants components and ordered separating necks

\[
w_i^{(\nu)}=L_{i+1}^{(\nu)},
\qquad i=1,\ldots,N-1,
\]

satisfying, as `nu -> infinity`,

\[
w_i^{(\nu)}\to0,
\qquad
\frac{w_{i+1}^{(\nu)}}{w_i^{(\nu)}}\to0.
\]

PF-054 produces precisely such families from sufficiently hierarchical recurrent isolated prime patterns.

Let

\[
G_\nu
=
\sum_{i=1}^{N-1}
 w_i^{(\nu)}
 (e_i-e_{i+1})(e_i-e_{i+1})^*.
\]

Burger's small-spectrum reduction, in the multiscale form used in PF-054, identifies the full collapsing Laplace sector with this weighted path, including spectral projectors. The complement of the `N` graph modes remains uniformly separated from zero because the stable components are fixed thrice-punctured spheres.

## 2. The graph resolvent at one hierarchy scale

Fix `j in {1,...,N-1}` and use

\[
\varepsilon_\nu=w_j^{(\nu)}.
\]

Then

\[
\frac{w_i^{(\nu)}}{\varepsilon_\nu}
\to
\begin{cases}
+\infty,&i<j,\\
1,&i=j,\\
0,&i>j.
\end{cases}
\]

Thus the stronger edges force

\[
S_j:=\{x\in\mathbb C^N:x_1=\cdots=x_j\},
\]

while the weaker edges disappear at this scale. Let `P_j` be the orthogonal projection onto `S_j`, and define

\[
u_j
:=
\frac1j\sum_{i=1}^j e_i-e_{j+1}.
\]

The surviving edge form on `S_j` is

\[
A_j:=u_j u_j^*.
\]

Its unique nonzero eigenvalue is

\[
\boxed{
c_j=\|u_j\|^2=1+\frac1j=\frac{j+1}{j}.
}
\]

Finite-dimensional form/resolvent convergence gives, locally uniformly for

\[
z\notin\{0,c_j\},
\]

\[
\boxed{
\left(\frac{G_\nu}{w_j^{(\nu)}}-zI\right)^{-1}
\longrightarrow
P_j\,(A_j-zI_{S_j})^{-1}\,P_j.
}
\]

Interpretation:

- edges `i<j` have already contracted the first `j` pants into one mass-`j` component;
- edge `j` survives with unit conductance;
- edges `i>j` are invisible and leave the later components disconnected;
- the difference modes inside the contracted block escape to infinite energy.

This is the exact graph-level tropical limit predicted qualitatively by PF-054.

## 3. PF-078 is uniform with respect to pinching rates

PF-078 writes the physical marked cusp scattering of a finite tangent as

\[
\Phi_\nu^{\rm mark}(s)
=
H_\nu(s)
+
\sum_{q=0}^{N-1}
\frac{R_{q,\nu}}{s-s_{q,\nu}},
\]

where:

1. the pole-subtracted remainder `H_nu` is uniformly `O(1)` near `s=1`;
2. every `1/w` singularity comes from the finite-dimensional graph sector;
3. pole positions satisfy
   \[
   1-s_{q,\nu}
   =\frac{\mu_{q,\nu}}{2\pi^2}+o(\mu_{q,\nu});
   \]
4. grouped residue matrices converge to the corresponding graph spectral projectors, with the normalization `2 pi R -> projector`.

The proof of the `O(1)` remainder uses only the uniform spectral gap on the **orthogonal complement of the whole N-dimensional small sector** and source/observation maps supported in persistent normalized cusp annuli. Neither ingredient requires comparable neck lengths. When graph eigenvalues collide at a weaker scale, one groups their orthogonal projectors; no individual-eigenvector choice is needed.

Therefore the PF-078 Feshbach argument can be combined directly with the graph resolvent limit above.

## 4. Multiscale physical-scattering limit

For the `j`-th scale set

\[
\boxed{
s_{j,\nu}(z)
=
1-
\frac{w_j^{(\nu)}z}{2\pi^2}.
}
\]

Then, locally uniformly away from `z=0,c_j`,

\[
\boxed{
\frac{w_j^{(\nu)}}{\pi}
\Phi_\nu^{\rm mark}
\!\left(
1-\frac{w_j^{(\nu)}z}{2\pi^2}
\right)
\longrightarrow
P_j(A_j-zI_{S_j})^{-1}P_j.
}
\]

The mechanism is transparent in the pole decomposition:

- graph modes carried by stronger edges have `mu/w_j -> infinity`, hence vanish from the scaled resolvent;
- the `j`-th edge produces the finite pole `z=c_j=(j+1)/j`;
- weaker modes have `mu/w_j ->0` and merge into the zero-pole projector;
- the physical-scattering remainder is `O(1)`, so multiplication by `w_j` kills it.

Thus **the raw physical scattering matrix itself**, with no pole subtraction, has a nested sequence of graph-resolvent blow-ups at the prime-derived neck scales.

## 5. One canonical physical channel has a universal rational profile

Take the persistent cusp in the first pants component. The endpoint matrix element is

\[
m_j(z)
:=
\langle e_1,
P_j(A_j-zI_{S_j})^{-1}P_j e_1\rangle.
\]

The projection of `e_1` onto `S_j` has squared norm `1/j`. Its weight on the nonzero eigenvector of `A_j` is

\[
\frac1{j(j+1)},
\]

and its weight on the zero eigenspace is

\[
\frac1{j+1}.
\]

Hence

\[
\boxed{
m_j(z)
=-\frac{1}{(j+1)z}
+\frac{1}{j(j+1)(\frac{j+1}{j}-z)}
=
\frac{1-z}{jz\left(z-\frac{j+1}{j}\right)}.
}
\]

Consequently

\[
\boxed{
\frac{w_j^{(\nu)}}{\pi}
\Phi_{11,\nu}
\!\left(
1-\frac{w_j^{(\nu)}z}{2\pi^2}
\right)
\longrightarrow
\frac{1-z}{jz\left(z-\frac{j+1}{j}\right)}.
}
\]

This formula is useful in two opposite ways:

- **positive:** the physical scattering of the actual multiscale prime tangents develops a canonically ordered ladder of singular zoom scales;
- **negative boundary:** once the correct scale is factored out, the leading profile is universal. In the extreme hierarchy, scattering does not carry extra leading-order arithmetic beyond the neck scale itself.

Higher-order corrections may still contain finer shape information; the leading tropical profile does not.

## 6. Exact prime-gap / cuff scale

For the hierarchical patterns of PF-054,

\[
\boxed{
w_j
=L_{j+1}
\sim
4\sqrt{\frac{d_j}{d_{j+1}}}
\sim
4\exp\!\left[-\frac{\ell_j-\ell_{j+1}}4\right].
}
\]

Therefore the natural width of the `j`-th scattering zoom around `s=1` is

\[
\boxed{
\delta s_j
:=\frac{w_j}{2\pi^2}
\sim
\frac{2}{\pi^2}
\exp\!\left[-\frac{\ell_j-\ell_{j+1}}4\right].
}
\]

The unique nonzero pole of the tropical profile occurs at

\[
z=c_j=\frac{j+1}{j},
\]

so its physical location satisfies

\[
\boxed{
1-s_j^{\rm edge}
\sim
\frac{2(j+1)}{\pi^2j}
\exp\!\left[-\frac{\ell_j-\ell_{j+1}}4\right].
}
\]

This is exactly the eigenvalue ladder of PF-054 viewed through **physical cusp scattering** rather than through the Laplacian alone.

The common divergence `2 log P` of individual prime cuffs disappears; the surviving physical scales are controlled by relative cuff contrasts.

## 7. Interior/exterior and geometric status

The result uses only the intrinsic finite-tangent scattering channels. The ambient prime-circle inversion/interior-exterior duality remains an exact symmetry of the construction but does not create a second intrinsic scattering channel, consistently with the earlier audit.

The ordering of pants, persistent cusps, necks, and contractions is forced by the original exact orthogonal-circle geometry. No graph, damping factor, or generating function is inserted independently of the hyperbolic surface.

## 8. Serious novelty / prior-art audit

Known ingredients, with no novelty claim:

- Burger's reduction of small Laplace eigenvalues/eigenfunctions under hyperbolic pinching to weighted graph Laplacians, including multiscale graph contractions after normalization;
- finite-dimensional strong-edge contraction / Schur-complement limits of weighted graph resolvents;
- Schulze-type resolvent and scattering analysis for degenerating finite-geometry hyperbolic surfaces;
- physical cusp scattering as a boundary functional of a compact-core Neumann-to-Dirichlet map;
- Feshbach/low-high resolvent decomposition.

There is also broad norm-resolvent literature for graph-like/thin manifolds. Those results concern different geometric limits and do not by themselves identify the physical cusp-scattering blow-up of a pinching hyperbolic surface.

Directed searches for combinations of

```text
multiscale pinching hyperbolic surface + physical scattering + graph resolvent,
hierarchical necks + cusp scattering + contracted graph,
weighted graph resolvent + scattering matrix + hyperbolic degeneration,
Feshbach + cusp scattering + pinching
```

found the adjacent theories above but not the nested limit

\[
\frac{w_j}{\pi}
\Phi^{\rm physical}
\left(1-\frac{w_jz}{2\pi^2}\right)
\to
P_j(A_j-z)^{-1}P_j
\]

or the explicit one-channel profile displayed above.

No historical-priority claim is made. The candidate-new content is narrow: **successive physical cusp-scattering blow-ups of a multiscale pinching hyperbolic path tropicalize to the resolvents of its contracted graph filtration**, specialized here to the exact prime-derived neck hierarchy.

## 9. Falsification criteria and limits

The result would fail if any of the following fails:

1. PF-078's complement gap or bounded persistent-cusp source/observation estimates cease to be uniform when pinching rates separate;
2. the multiscale Burger reduction does not give projector/resolvent convergence to the actual weighted path at the relevant scale;
3. the residue normalization `2 pi R -> graph projector` fails after grouping colliding weak modes.

The first point is insensitive to relative rates because it treats the **entire** small sector together. The second is the graph/surface content already used in PF-054. The third is best formulated with cluster projectors and is the main normalization checkpoint for a publication proof.

Further boundaries:

- this is a theorem about finite tangents, not a global scattering matrix for the infinite prime flute;
- it does not identify Riemann zeros or provide an RH criterion;
- the leading multiscale scattering profiles are universal, so any arithmetic beyond the already known scale ladder must live in subleading corrections or interactions between scales;
- the prime application inherits PF-046/PF-054's non-uniform fixed-pattern sieve argument, which should receive specialist analytic-number-theory review before publication.

## 10. Lean-formalizable finite-dimensional core

The graph part is a clean formalization target independent of analytic scattering:

1. for positive path weights with `w_i/w_j -> infinity` for `i<j`, `w_j/w_j=1`, and `w_i/w_j ->0` for `i>j`, prove resolvent convergence to the contracted-edge operator on `S_j`;
2. prove `A_j=u_j u_j^*` has spectrum `{0,(j+1)/j}`;
3. compute exactly
   \[
   \langle e_1,P_j(A_j-z)^{-1}P_j e_1\rangle
   =\frac{1-z}{jz(z-(j+1)/j)}.
   \]

These lemmas isolate the algebraic content from the hyperbolic scattering analysis.
