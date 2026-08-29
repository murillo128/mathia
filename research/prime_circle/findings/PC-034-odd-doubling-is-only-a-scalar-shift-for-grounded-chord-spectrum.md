# PC-034 — odd doubling changes the multi-grounded chord spectrum only by a universal scalar shift

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for any prime/composite discriminator that uses only the spectral shape of the canonical multi-grounded inverse-square chord Laplacian. The cyclotomic doubling identity and the regular-polygon `csc^2` row sum are classical; no novelty is claimed for those ingredients.

## 1. The question left after PC-019 and PC-032/PC-033

PC-019 proves that for odd `n`, the primitive shells themselves satisfy

\[
\mu_{2n}^*=-\mu_n^*,
\]

so every unanchored intrinsic single-shell geometry identifies `n` with `2n`.

PC-032 and PC-033 then introduced a possible escape: rather than use only the shell geometry, take the inverse-square chord Laplacian of the **full** regular polygon and ground all old/imprimitive vertices. At level `n` the surviving primitive block is

\[
A_n:=\mathcal L_n[U(n),U(n)],
\qquad
U(n)=(\mathbb Z/n\mathbb Z)^\times,
\]

where

\[
(\mathcal L_n)_{ab}
=-\frac1{4\sin^2(\pi(a-b)/n)}
\quad(a\ne b)
\]

and every diagonal entry is the full-polygon degree

\[
d_n
=\sum_{r=1}^{n-1}\frac1{4\sin^2(\pi r/n)}
=\frac{n^2-1}{12}.
\]

This construction is no longer purely unanchored: at a prime level the only grounded vertex is the common anchor, and at a composite level the diagonal also remembers the grounded old background.

The natural question is therefore whether that extra grounded information breaks the exact `n <-> 2n` degeneracy in a genuinely arithmetic way.

It does not.

## 2. Exact half-turn conjugacy of the primitive coordinates

Let `n>1` be odd. The classical identity

\[
\Phi_{2n}(z)=\Phi_n(-z)
\]

gives the bijection

\[
R:\mu_n^*\longrightarrow\mu_{2n}^*,
\qquad
R(z)=-z.
\]

In exponent coordinates this is

\[
a\in U(n)
\longmapsto
2a+n\in U(2n).
\]

For any two primitive roots `alpha,beta`, the half-turn preserves their chord distance exactly:

\[
|-\alpha-(-\beta)|=|\alpha-\beta|.
\]

Consequently, after ordering the primitive coordinates through `R`, every off-diagonal entry of `A_{2n}` is identical to the corresponding off-diagonal entry of `A_n`.

The only possible difference is the diagonal full-polygon degree.

## 3. The grounded background contributes only a scalar

The exact regular-polygon row sum is

\[
d_n=\frac{n^2-1}{12}.
\]

Therefore

\[
d_{2n}-d_n
=
\frac{4n^2-1-(n^2-1)}{12}
=
\frac{n^2}{4}.
\]

Let `P_R` be the permutation matrix induced by the half-turn bijection of primitive vertices. Then

\[
\boxed{
P_R^T A_{2n}P_R
=
A_n+\frac{n^2}{4}I_{\varphi(n)}.
}
\]

This is an equality of the complete primitive-layer operators, not merely an equality of a trace, determinant, or asymptotic statistic.

Hence

\[
\boxed{
\operatorname{Spec}(A_{2n})
=
\operatorname{Spec}(A_n)+\frac{n^2}{4}.
}
\]

If

\[
\chi_n(t)=\det(tI-A_n),
\]

then

\[
\boxed{
\chi_{2n}(t)
=
\chi_n\!\left(t-\frac{n^2}{4}\right).
}
\]

The eigenvectors are the same after the half-turn relabeling.

## 4. All centered spectral shape is exactly blind to odd doubling

Subtract the universal full-polygon degree:

\[
\widetilde A_n:=A_n-d_nI.
\]

Then the previous identity becomes

\[
\boxed{
P_R^T\widetilde A_{2n}P_R
=
\widetilde A_n.
}
\]

Thus every shift-invariant spectral quantity agrees exactly between `n` and `2n`, including

- every eigenvalue gap and spacing statistic;
- every centered spectral moment;
- the complete centered characteristic polynomial;
- every eigenvector-dependent invariant transported by the half-turn;
- any spectral statistic built only from differences of eigenvalues.

The absolute spectral offset does distinguish the two levels, but it is the explicit universal quantity `n^2/4`. It contains no hidden prime/composite information: once the level size is known, the offset is known before inspecting the primitive arrangement.

In particular, for every odd prime `p`,

\[
\boxed{
\operatorname{Spec}(A_{2p})
=
\operatorname{Spec}(A_p)+\frac{p^2}{4},
}
\]

although `p` is prime and `2p` is composite.

As a small exact audit, `A_3` has eigenvalues

\[
\left\{\frac13,1\right\},
\]

while `A_6` has eigenvalues

\[
\left\{\frac{31}{12},\frac{13}{4}\right\}
=
\left\{\frac13,1\right\}+\frac94.
\]

## 5. Why this is stronger than the unanchored PC-019 obstruction

PC-019 could be escaped in principle by retaining the common anchor or some other absolute information from the full polygon. The multi-grounded operator of PC-032/PC-033 seemed to do exactly that: its diagonal includes the interaction with every grounded old vertex, and at prime level this means grounding the common anchor itself.

PC-034 shows that, for this canonical nonlocal operator, the attempted recovery of absolute information is spectrally trivial under the most important half-turn test. The entire difference between the prime shell `p` and the congruent composite shell `2p` is a scalar background energy.

Therefore the chain

\[
\boxed{
\text{primitive shell}
\to
\text{ground all old vertices in the full }csc^2\text{ Laplacian}
\to
\text{centered spectral shape}
\to
\text{prime/RH discriminator}
}
\]

is ruled out.

Equivalently: **multi-grounding does not repair the `n <-> 2n` information loss at the level of spectral shape; it only adds a known level-dependent scalar gauge.**

## 6. Prior-art and novelty audit

The proof uses only classical ingredients already present in this line:

- the standard odd-level cyclotomic identity `Phi_{2n}(z)=Phi_n(-z)`, which is the basis of PC-019;
- the classical trigonometric sum

  \[
  \sum_{r=1}^{n-1}\csc^2(\pi r/n)=\frac{n^2-1}{3},
  \]

  and the associated regular-polygon inverse-square spectrum anchored in Calogero--Perelomov for PC-032;
- elementary conjugacy of principal blocks under a permutation of the primitive vertices.

A targeted search of `csc^2` principal submatrices, primitive/reduced-residue restrictions, and inverse-square root-of-unity Laplacians did not identify an RH mechanism based on this exact odd-doubling comparison. That absence is not used as evidence of novelty.

No theorem-level novelty is claimed. The durable contribution is the project-specific obstruction tying PC-019 directly to the canonical nonlocal operator introduced in PC-032/PC-033.

## 7. Boundary of the no-go

This finding does **not** rule out every anchored operator.

The obstruction applies because `A_n` treats all grounded vertices only through the Dirichlet principal-block construction; it does not keep the common vertex `1` as a separately marked degree of freedom. A genuinely pointed operator that couples the primitive shell asymmetrically to the distinguished anchor can escape this scalar-shift conjugacy.

Likewise, the result does not classify:

- non-shift-invariant uses of the absolute spectrum, although their `n <-> 2n` change is now completely explicit and universal;
- cross-level couplings performed before spectralization;
- kernels whose entries depend nonlinearly on the primitive configuration rather than only on pairwise inverse-square chords;
- the global pointed uniformization/monodromy sector of PC-017, where the anchor remains a distinguished puncture rather than an undifferentiated grounded boundary vertex.

For the inverse-square chord route specifically, however, the surviving arithmetic content must now lie beyond centered single-level spectral shape. Squarefree multi-prime radicals may still produce nontrivial absolute characteristic polynomials, but they cannot repair this exact odd-doubling degeneracy without adding genuinely pointed or cross-level structure.
