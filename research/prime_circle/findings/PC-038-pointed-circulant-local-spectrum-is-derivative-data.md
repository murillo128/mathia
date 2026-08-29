# PC-038 — a pointed circulant has flat local spectrum; anchor resolvents and rank-one defects are derivative data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the natural single-level pointed spectral repair left open by PC-035/PC-037 when the underlying pairwise operator is still a shell-independent translation-invariant kernel on the regular polygon. Marking the common vertex, taking its resolvent/Green response, or adding an arbitrary scalar rank-one potential at that vertex does not create new prime-circle spectral data at prime levels: everything is determined by the universal circulant characteristic polynomial and its derivative.

## 1. The surviving pointed-before-diagonalization question

PC-035 showed that diagonalizing the standalone inverse-square anchor profile gives only classical `L(2,chi)` data. PC-036 extended that obstruction to every fixed even inverse power. PC-037 then ruled out shell-independent rotation-invariant linear operators on the harmonic cyclotomic fields, while explicitly leaving **pointed/rotation-breaking constructions** outside its theorem.

A particularly natural escape is therefore to keep the common vertex as an active state and couple it to the entire primitive-shell operator **before** taking a scalar spectrum.

At a prime level `p`, however,

\[
\{1\}\sqcup \mu_p^*=\mu_p.
\]

So any shell-independent pairwise operator whose entry between two polygon vertices depends only on their relative rotation (equivalently on the chord class) becomes a circulant matrix on the complete `p`-gon.

Let

\[
C_p=(c_{a-b})_{a,b\in\mathbb Z/p\mathbb Z}
\]

be any Hermitian circulant of this kind and let

\[
e_0=(1,0,\ldots,0)^T
\]

denote the common anchored vertex. This includes the inverse-square chord Laplacian of PC-032, but the argument below does not use its specific kernel.

The question is whether the **pointed pair** `(C_p,e_0)` has a richer local spectral response than the unpointed circulant spectrum.

It does not.

## 2. The anchor has exactly the global average spectral measure

The normalized Fourier vectors

\[
f_k(a)=p^{-1/2}e^{2\pi i ka/p},
\qquad 0\le k<p,
\]

diagonalize every circulant:

\[
C_pf_k=\lambda_k f_k.
\]

At the anchor,

\[
|\langle e_0,f_k\rangle|^2=\frac1p
\]

for every Fourier mode. Therefore for every function `F` for which the finite functional calculus is defined,

\[
\boxed{
\langle e_0,F(C_p)e_0\rangle
=
\frac1p\sum_{k=0}^{p-1}F(\lambda_k)
=
\frac1p\operatorname{tr}F(C_p).
}
\]

Thus merely **observing a translation-invariant polygon operator from the distinguished common vertex does not break its spectral symmetry**. The anchor's local spectral measure is the normalized global eigenvalue counting measure,

\[
\boxed{
\mu_{p,0}
=
\frac1p\sum_{k=0}^{p-1}\delta_{\lambda_k},
}
\]

with repeated eigenvalues automatically carrying their multiplicity.

This is the weighted-circulant version of the standard fact that vertex-transitive matrices/graphs have identical local spectral measures. In graph-theoretic language, vertex-transitive graphs are walk-regular; Godsil--McKay already characterize walk-regularity by equality of the characteristic polynomials of all vertex-deleted subgraphs.

## 3. The pointed Green function is only `P'/P`

Let

\[
P_p(z):=\det(zI-C_p)
=\prod_{k=0}^{p-1}(z-\lambda_k).
\]

For `z` off the spectrum, the anchor Weyl/Green function is

\[
m_p(z)
:=
\langle e_0,(zI-C_p)^{-1}e_0\rangle.
\]

Using the flat local weights,

\[
\boxed{
m_p(z)
=
\frac1p\sum_{k=0}^{p-1}\frac1{z-\lambda_k}
=
\frac1p\frac{P_p'(z)}{P_p(z)}.
}
\]

So the full frequency-dependent response of the marked anchor is not an additional spectral object. It is the logarithmic derivative of the already-existing circulant characteristic polynomial.

This is stronger than comparing one determinant or one moment: every pole, residue, moment, Stieltjes transform, and scalar functional-calculus observable seen from the common vertex is fixed by the unpointed spectrum.

## 4. The apparently noncommuting anchor-shell Schur complement also collapses

Write the operator in anchored block form

\[
C_p=
\begin{pmatrix}
c_0 & b^*\\
b & G_p
\end{pmatrix},
\]

where `G_p` acts on the primitive vertices and `b` is the complete anchor-to-shell coupling vector.

This is exactly the kind of joint data left open after PC-035: retain the shell operator and the anchor coupling together rather than diagonalizing `b` separately.

For `z` away from the spectrum of `G_p`, Schur complementation gives

\[
m_p(z)
=
\frac1{
z-c_0-b^*(zI-G_p)^{-1}b
}.
\]

Combining this with the exact `P'/P` formula yields

\[
\boxed{
z-c_0-b^*(zI-G_p)^{-1}b
=
p\,\frac{P_p(z)}{P_p'(z)}.
}
\]

Equivalently,

\[
\boxed{
b^*(zI-G_p)^{-1}b
=
z-c_0-p\,\frac{P_p(z)}{P_p'(z)}.
}
\]

Hence even the natural **noncommuting self-energy** obtained by letting the anchor propagate through the full primitive block is completely determined by the universal circulant spectrum.

Cramer's rule gives the companion identity

\[
m_p(z)
=
\frac{\det(zI-G_p)}{P_p(z)},
\]

so

\[
\boxed{
\det(zI-G_p)=\frac1pP_p'(z).
}
\]

For the inverse-square kernel this recovers the derivative-spectrum identity of PC-032, but the Schur-complement formula identifies what happens when the anchor coupling vector is retained rather than discarded: its entire resolvent feedback is still only `P_p/P_p'`.

## 5. A scalar anchor defect gives only `P - alpha P'/p`

One may try to make the anchor genuinely active by modifying the operator itself with an arbitrary local potential

\[
C_p^{(\alpha)}
=
C_p+\alpha e_0e_0^*.
\]

This does break cyclic symmetry at the operator level. But the matrix determinant lemma and the formula above give

\[
\begin{aligned}
\det(zI-C_p^{(\alpha)})
&=
P_p(z)\left(1-\alpha m_p(z)\right)\\
&=
\boxed{
P_p(z)-\frac{\alpha}{p}P_p'(z)
}.
\end{aligned}
\]

Therefore every one-parameter rank-one anchor perturbation has a characteristic polynomial lying in the two-dimensional span of `P_p` and `P_p'`.

For real `alpha` and Hermitian `C_p`, the perturbed eigenvalues are the standard rank-one interlacing roots of this explicit polynomial. The anchor has not generated an independent arithmetic spectral law; it has only selected a classical rank-one deformation of the universal polygon spectrum.

## 6. Inverse-square specialization

For the canonical inverse-square chord Laplacian,

\[
C_p=\mathcal L_p,
\qquad
c_0=d_p=\frac{p^2-1}{12},
\]

and PC-032 gives

\[
\lambda_k=\frac{k(p-k)}2,
\qquad
P_p(z)
=
z\prod_{k=1}^{p-1}
\left(z-\frac{k(p-k)}2\right).
\]

Hence the full pointed transfer function is explicitly

\[
\boxed{
b^*(zI-G_p)^{-1}b
=
z-\frac{p^2-1}{12}
-
p\,\frac{P_p(z)}{P_p'(z)}.
}
\]

Adding any scalar potential at the common vertex gives

\[
\boxed{
\det(zI-(\mathcal L_p+\alpha e_0e_0^*))
=
P_p(z)-\frac{\alpha}{p}P_p'(z).
}
\]

So the most immediate attempt to combine the PC-032 shell block with the PC-035 pointed anchor **before diagonalization** still has no spectral content beyond the elementary regular-polygon eigenvalues `k(p-k)/2` and their derivative/interlacing algebra.

## 7. Why this is a decisive negative for the natural pointed spectral repair

This route escaped the hypotheses of PC-037 because choosing the common vertex breaks rotation symmetry at the observable level, and it escaped PC-035/PC-036 because the anchor coupling is not transformed independently: it is allowed to interact with the whole shell resolvent.

Nevertheless, prime levels themselves force

\[
\boxed{
\text{anchor + primitive shell}
=
\text{complete regular polygon}.
}
\]

For every shell-independent translation-invariant pairwise kernel on that polygon,

\[
\boxed{
\text{pointed local spectral measure}
\to
\frac1p\operatorname{tr},
}
\]

\[
\boxed{
\text{anchor resolvent / Schur self-energy}
\to
P_p'/P_p,
}
\]

and

\[
\boxed{
\text{scalar rank-one anchor defect}
\to
P_p-\frac{\alpha}{p}P_p'.
}
\]

No Riemann-zero divisor, gamma factor, functional equation, or critical-line center can emerge from this pointing operation unless it was already present in the chosen circulant kernel.

For the inverse-square kernel the underlying `P_p` is elementary, so this branch is completely explicit.

## 8. Prior art and novelty audit

No general theorem novelty is claimed.

- Fourier diagonalization of circulant matrices is classical.
- The equality of local spectral data at vertices of a vertex-transitive operator is the weighted-matrix analogue of standard walk-regular graph theory. Godsil and McKay, *Feasibility conditions for the existence of walk-regular graphs*, Linear Algebra Appl. 30 (1980), 51--61, characterize walk-regular graphs by equality of vertex-deleted characteristic polynomials and note vertex-transitive graphs as examples.
- `m_p=P_p'/(pP_p)` follows immediately from cyclic symmetry plus the trace resolvent identity, or from equal principal cofactors.
- The Schur-complement and matrix-determinant-lemma formulas are standard finite-dimensional linear algebra.
- PC-032 already contains the special inverse-square cofactor identity `det(zI-G_p)=P_p'(z)/p`.

The durable project-specific result is the **scope obstruction**: the "pointed before diagonalization" escape does not work if pointing means taking local spectral data, Schur feedback, or a scalar rank-one defect of an otherwise translation-invariant regular-polygon operator. The anchor must change more than the observation point or one diagonal entry.

## 9. Boundary and falsification test

This finding does **not** classify:

- operators whose off-diagonal kernel itself depends asymmetrically on the common vertex;
- nonlinear anchor-shell couplings that cannot be represented by functional calculus or a scalar Schur self-energy;
- composite levels, where `anchor + primitive shell` is not the complete regular polygon;
- cross-level operators coupling several `n` before spectralization;
- shell-dependent metrics/kernels forced by the primitive configuration;
- global uniformization, monodromy, Liouville, or Weil--Petersson data from PC-017.

So the surviving pointed frontier is narrower but nonempty: a viable construction must break cyclic universality **inside the operator/coupling structure itself**, or use cross-level/nonlinear geometry, rather than merely mark the common vertex of a shell-independent circulant.

The exact claim can be falsified by any of the following:

1. find a circulant `C_p` for which the Fourier eigenvectors do not have anchor weight `1/p`;
2. find `z` for which the diagonal resolvent differs from `P_p'(z)/(pP_p(z))`;
3. find an anchored block decomposition for which the Schur complement differs from `pP_p/P_p'`;
4. find a scalar rank-one anchor perturbation whose determinant differs from `P_p-(alpha/p)P_p'`.

All four would contradict elementary finite-dimensional identities, so the obstruction is exact under its stated hypotheses.
