# PF-089 — low-energy determinant cancels hierarchical interscale prime memory

**Status:** `DECISIVE-NEGATIVE` for using a scalar low-energy / near-one determinant to retain the multiscale prime-memory mechanism of PF-054/PF-081; `EXACT-GRAPH` + `CLASSICAL-SURFACE-DEGENERATION-COROLLARY`. No RH claim.

PF-081 identified a genuinely relational second-order effect: in a two-scale degeneration with necks `a >> b`, the weak small eigenvalue contains the singular correction `-const * b^2/a`, coming from the reduced-resolvent pole of the stronger small eigenmode. A natural question was whether a Selberg/Laplacian/Steklov-type determinant could aggregate that effect into a cleaner global scalar.

For the genus-zero path degenerations relevant to the prime flute, the answer is negative at the graph-controlled singular scale. Kirchhoff's matrix-tree identity forces the product of all nonzero low modes to collapse to the product of the neck conductances. In the strongly hierarchical prime regime of PF-054, that edge product telescopes again and retains only the two endpoint gap/cuff scales. The `b^2/a` memory visible in an individual eigenvalue cancels from the determinant.

This refines PF-048 and PF-062: the small-spectrum pseudodeterminant is certainly canonical, but on the strongest hierarchical prime patterns it is much less informative than the resolved eigenvalue ladder or marked spectral/scattering data.

## 1. Exact determinant identity for the low-energy path

Let

\[
G(w)=\sum_{j=1}^{N-1}w_j(e_j-e_{j+1})(e_j-e_{j+1})^T
\]

be the weighted path Laplacian on `N` vertices, with

\[
0=\mu_0<\mu_1\le\cdots\le\mu_{N-1}.
\]

Kirchhoff's weighted matrix-tree theorem gives for every connected weighted graph

\[
\prod_{k=1}^{N-1}\mu_k=N\,\tau_w(G),
\]

where `tau_w` is the weighted spanning-tree enumerator. A path is already a tree, so it has exactly one spanning tree. Therefore **exactly**

\[
\boxed{
\operatorname{pdet}G(w)
:=\prod_{k=1}^{N-1}\mu_k
=N\prod_{j=1}^{N-1}w_j.
}
\tag{1}
\]

No spectral approximation is involved in (1).

For a fixed-topology hyperbolic degeneration into `N` thrice-punctured pants components, Burger's surface-to-graph theorem gives, with the normalization used throughout PF-047--PF-054,

\[
\lambda_k
=\frac{\mu_k}{2\pi^2}(1+o(1)),
\qquad 1\le k\le N-1.
\]

Hence the genuine small-eigenvalue product of the finite tangent satisfies

\[
\boxed{
D_{\rm small}
:=\prod_{k=1}^{N-1}\lambda_k
=
\frac{N}{(2\pi^2)^{N-1}}
\prod_{j=1}^{N-1}w_j\,(1+o(1)).
}
\tag{2}
\]

This is the scalar low-energy determinant already implicit in PF-048 and in the near-one Selberg factorization of PF-062.

## 2. Strong prime hierarchy makes the determinant telescope to the endpoints

PF-054 constructs recurrent prime-derived patterns with consecutive internal gaps

\[
d_1,d_2,\ldots,d_N
\]

so strongly hierarchical that the nested separating necks satisfy

\[
\boxed{
w_j
=4\sqrt{\frac{d_j}{d_{j+1}}}(1+o(1)),
\qquad
\frac{w_{j+1}}{w_j}\to0.
}
\tag{3}
\]

Multiplying (3) over the full path gives

\[
\prod_{j=1}^{N-1}w_j
=4^{N-1}
\prod_{j=1}^{N-1}\sqrt{\frac{d_j}{d_{j+1}}}
(1+o(1)).
\]

The entire internal hierarchy telescopes:

\[
\boxed{
\prod_{j=1}^{N-1}w_j
=4^{N-1}\sqrt{\frac{d_1}{d_N}}\,(1+o(1)).
}
\tag{4}
\]

Combining (2) and (4),

\[
\boxed{
D_{\rm small}
=
N\left(\frac{2}{\pi^2}\right)^{N-1}
\sqrt{\frac{d_1}{d_N}}
\,(1+o(1)).
}
\tag{5}
\]

All intermediate gaps

\[
d_2,\ldots,d_{N-1}
\]

disappear from the leading determinant, even though PF-054 shows that the **resolved** eigenvalues separately recover the successive ratios `d_j/d_{j+1}`.

For a large-prime occurrence of the same pattern, the distinguished cuffs obey

\[
\ell_j(P)=2\log\frac{4P}{d_j}+o(1).
\]

Therefore

\[
\sqrt{\frac{d_1}{d_N}}
=
\exp\!\left[-\frac{\ell_1-\ell_N}{4}\right](1+o(1)),
\]

and (5) becomes

\[
\boxed{
D_{\rm small}
=
N\left(\frac{2}{\pi^2}\right)^{N-1}
\exp\!\left[-\frac{\ell_1-\ell_N}{4}\right]
(1+o(1)).
}
\tag{6}
\]

Thus the scalar determinant sees only the **net endpoint cuff contrast** at leading hierarchical order.

This is a second telescoping mechanism, distinct from PF-002's one-cuff telescoping: here the cancellation occurs after genuine multiscale spectral information has first been created, because the dual graph is a tree and the determinant multiplies all its low modes.

## 3. The PF-081 `b^2/a` memory cancels exactly in the two-neck determinant

The cancellation is already visible in the smallest nontrivial example.

For three pants and two necks `a >> b`, PF-081 uses

\[
G(a,b)=
\begin{pmatrix}
a&-a&0\\
-a&a+b&-b\\
0&-b&b
\end{pmatrix}.
\]

Its nonzero eigenvalues are

\[
\mu_\pm
=a+b\pm\sqrt{a^2-ab+b^2}.
\]

Writing `b/a -> 0`,

\[
\mu_-
=\frac32b-\frac38\frac{b^2}{a}
-\frac{3}{16}\frac{b^3}{a^2}+\cdots,
\]

while

\[
\mu_+
=2a+\frac12b+\frac38\frac{b^2}{a}
+\frac{3}{16}\frac{b^3}{a^2}+\cdots.
\]

The weak eigenvalue therefore contains exactly the PF-081 upstream-memory term. But the product is not merely asymptotic:

\[
\boxed{
\mu_+\mu_-=3ab
}
\tag{7}
\]

by the matrix-tree theorem, or by direct multiplication.

Hence the `b^2/a` singular correction is **eigenvalue-resolved but determinant-invisible**. The mixing with the stronger mode redistributes the two low eigenvalues while preserving their product at the graph/Feshbach singular order.

On the true surface, PF-081's remaining analytic gate is still needed to promote the individual two-scale expansion to a full theorem. If that gate closes, the `1/a` reduced-resolvent contribution is forced by the two-mode low sector; (7) shows that this singular interscale contribution cannot survive as an independent term in the product of those low modes. The full surface determinant may of course contain ordinary local collar/high-mode corrections; the statement here is specifically that the amplified `b^2/a` memory mechanism is destroyed by determinant compression.

## 4. This is exactly what natural determinant degeneration theory predicts

This cancellation is not evidence for a new general determinant theorem. The surrounding theory is already very close.

- Burger's classical degeneration theorem identifies the small hyperbolic eigenvalues with weighted graph eigenvalues.
- Wentworth, *A Meyer--Vietoris formula for the determinant of the Dirichlet-to-Neumann operator on Riemann surfaces* (J. Geom. Anal. 2023, arXiv:2209.11863), derives determinant degeneration formulas using an extension of Kirchhoff's weighted matrix-tree theorem with external potential.
- Jin--Wang, *The Steklov Determinant and Compactness of Isospectral Planar Domains* (arXiv:2608.22330, 23 Aug 2026), give normalized Steklov-determinant asymptotics in terms of products of small Neumann/Dirichlet eigenvalues and, in genus zero, compare those small spectra with weighted graph Laplacians. They explicitly invoke the matrix-tree theorem for the tree graph produced by separating degeneration.
- PF-062 already showed that the standard pinching-renormalized Selberg zeta near `s=1` reduces, under the prime-tangent scaling, to the characteristic polynomial `det(G-zI)`. Setting `z=0` after removing the permanent zero mode gives precisely the pseudodeterminant in (1).

So determinant-to-tree-product collapse is standard structure, not a novelty claim. The project-specific consequence is the composition with the exact prime hierarchy:

\[
\boxed{
\text{prime cuff hierarchy}
\to
\text{resolved multiscale small spectrum}
\to
\text{scalar determinant}
\to
\text{endpoint contrast only at leading order}.
}
\]

Directed literature searches did not locate this prime-cuff specialization, but historical novelty is not needed for the negative conclusion.

## 5. Relation to PF-048

PF-048 correctly recorded, for a general pinching path,

\[
D_{\rm small}
\asymp
\prod_k
4\operatorname{arsinh}
\sqrt{\frac{d_1+\cdots+d_{k-1}}{d_k}},
\]

which can depend on all gaps. PF-089 does **not** retract that statement.

The new point is narrower and stronger: on the deliberately extreme hierarchical family of PF-054/PF-079/PF-081, where the individual eigenvalues become asymptotically inverse-readable scale by scale, every cumulative numerator is dominated by its final gap and the determinant simplifies to (5). Precisely in the regime where the resolved spectrum carries the most transparent prime information, its scalar product carries almost the least.

## 6. Interior/exterior duality

The argument uses only the intrinsic separating neck lengths obtained from Möbius-invariant cross-ratios of the exact orthogonal-circle endpoints. Ambient circle inversion preserves those cross-ratios and therefore does not produce a second independent determinant factor.

The interior/exterior realization remains useful geometric bookkeeping, but it cannot undo the tree/matrix-tree cancellation.

## 7. Research consequence

This closes the branch

\[
\boxed{
\text{PF-081 interscale memory}
\to
\text{product of small eigenvalues / scalar near-one determinant}
\to
\text{prime-sensitive multiscale invariant}.
}
\]

At leading/singular order, that branch loses the intermediate hierarchy by an exact tree identity.

The surviving observables must retain **resolved or marked spectral information**, for example:

- the individual multiscale eigenvalue ladder of PF-054;
- endpoint/local spectral measures and Jacobi Weyl data of PF-049/PF-050/PF-052;
- marked physical scattering residues of PF-051/PF-053/PF-078/PF-079;
- or genuinely subleading surface corrections after the universal/tree determinant factor has been divided out.

In particular, if the PF-081 two-scale PDE estimate is closed, the interesting `b^2/a` coefficient should be sought in a resolved pole/eigenvalue or residue, **not** in a scalar determinant of the low sector.