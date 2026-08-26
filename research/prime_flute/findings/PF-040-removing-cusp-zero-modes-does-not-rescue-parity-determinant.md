# PF-040 — removing cusp zero modes still does not rescue the parity determinant

**Status:** `DECISIVE-NEGATIVE` for the final standard variant left open by PF-038: project away the zeroth Fourier mode in every cusp and then form an even/odd (Neumann/Dirichlet) relative heat trace or determinant without any further renormalization.

## 1. What PF-038 left open

For the intrinsic reflection of a zero-twist flute, cutting along the fixed set gives a half-flute. Even functions correspond to Neumann boundary conditions on the fixed set and odd functions to Dirichlet boundary conditions.

PF-038 showed that a reflected cusp has transverse modes

\[
\text{Neumann}:m=0,1,2,\ldots,
\qquad
\text{Dirichlet}:m=1,2,\ldots,
\]

and that the unmatched mode

\[
H_0=-\frac{d^2}{dt^2}+\frac14
\]

prevents the ordinary parity difference from being trace class.

The natural remaining idea is classical: remove the cusp zero modes first (pseudo-Laplacian / cusp-form projection) and only then compare the two parity sectors. In each ideal half-cusp the remaining positive transverse eigenvalues agree, so the local obstruction of PF-038 disappears.

The prime flute nevertheless has another intrinsic obstruction: the reflection fixed set itself has infinite non-cuspidal length.

## 2. The zero-twist reflection has a geodesic ray through every cuff

The explicit zero-twist flute construction of Arredondo--Morales--Ramirez uses a reflection \(\tau\). Its fixed set contains:

- geodesics \(\gamma_n\) connecting consecutive punctures; and
- a geodesic ray \(\beta\), starting at the initial puncture and orthogonal to **every** cuff \(\alpha_n\).

The paper explicitly states that these are connected components of the fixed-point set and uses them to cut the flute to an ideal polygon.

Thus in the half-flute, \(\beta\) is a genuine totally geodesic boundary ray. Projecting away Fourier zero modes in the side cusps does not remove \(\beta\): after the initial cusp it runs through the compact core of every successive tight pair of pants and crosses every distinguished cuff.

## 3. Its length growth is exactly controlled by the prime collar mesh

Let \(d_n\) be the distance along the zero-twist spine / reflection ray between the relevant consecutive cuff crossings. PF-032 gives the exact tight-pants identity

\[
\boxed{
d_n=w(\ell_n)+w(\ell_{n+1})
=\frac12(h_n+h_{n+1}),
}
\]

where

\[
h_n=\log\frac{u_n}{u_{n-1}},
\qquad
u_n=\cot(\pi/p_n),
\]

and

\[
w(\ell_n)=\log\coth(\ell_n/4)=h_n/2.
\]

Therefore a segment of \(\beta\) running from the \(m\)-th to the \(N\)-th stage has length

\[
\begin{aligned}
B_{m,N}
&=\sum_{n=m}^{N}d_n\\
&=\frac12h_m+\sum_{n=m+1}^{N}h_n+\frac12h_{N+1}\\
&=\log\frac{u_N}{u_m}
+\frac12h_m+\frac12h_{N+1}.
\end{aligned}
\]

Hence

\[
\boxed{B_{m,N}\to\infty}
\]

and, using \(u_N\sim p_N/\pi\) and \(h_N\to0\),

\[
\boxed{B_{m,N}=\log p_N+O_m(1)+o(1).}
\]

So even after all cusp zero channels are removed, the reflection quotient has an infinite totally geodesic boundary whose canonical cuff exhaustion has explicitly divergent length.

## 4. Neumann minus Dirichlet has an unavoidable boundary heat term

For a compact two-dimensional Riemannian manifold with smooth boundary of length \(L\), the standard heat asymptotics are

\[
\operatorname{Tr}(e^{-t\Delta_D})
=\frac{\operatorname{Area}}{4\pi t}
-\frac{L}{8\sqrt{\pi t}}+O(1),
\]

\[
\operatorname{Tr}(e^{-t\Delta_N})
=\frac{\operatorname{Area}}{4\pi t}
+\frac{L}{8\sqrt{\pi t}}+O(1).
\]

Thus

\[
\boxed{
\operatorname{Tr}(e^{-t\Delta_N})-
\operatorname{Tr}(e^{-t\Delta_D})
=\frac{L}{4\sqrt{\pi t}}+O(1)
\qquad(t\downarrow0).
}
\]

This coefficient is local. Removing the transverse zero Fourier mode sufficiently deep in the cusps can cancel the PF-038 cusp channel, but it does not alter the local Neumann/Dirichlet boundary coefficient on compact portions of the geodesic ray \(\beta\).

Take the canonical compact core ending at the \(N\)-th cuff and truncate every cusp in the same way in the two parity sectors. Its reflection boundary contains the \(\beta\)-segment of length \(B_{m,N}\). Consequently the parity-relative heat asymptotic contains at least the boundary contribution

\[
\boxed{
\frac{B_{m,N}}{4\sqrt{\pi t}}
\sim
\frac{\log p_N}{4\sqrt{\pi t}}.
}
\]

It diverges as \(N\to\infty\).

Therefore projecting away the cusp zero modes does **not** by itself produce an exhaustion-independent ordinary relative heat trace, zeta function, or determinant.

## 5. The natural local counterterm is arithmetically coarse

One could attempt a second regularization by subtracting the infinite-boundary heat coefficient. But the exact formula above shows that its divergence is telescopic:

\[
B_{m,N}
=\log u_N + C_m + o(1).
\]

It does not retain fine prime-gap fluctuations.

Moreover, because the boundary \(\beta\) is geodesic and the ambient curvature is constantly \(-1\), all local boundary heat invariants are universal constants per unit boundary length (with zero geodesic curvature). Their divergent local part is therefore again proportional to \(B_{m,N}\), hence to the same endpoint growth.

So the additional counterterms forced by the infinite reflection boundary do not themselves provide a new prime-sensitive spectral observable.

This does **not** prove that every conceivable doubly-renormalized nonlocal parity determinant is impossible. It proves that the proposed canonical cure

\[
\text{reflection parity}
+\text{remove cusp zero modes}
\]

is still insufficient: a second infinite-boundary renormalization is unavoidable, and its local divergent content is universal/telescopic rather than gap-sensitive.

## 6. Relation to the distinguished cuff lengths

This obstruction uses the exact prime cuff geometry rather than merely the existence of infinitely many cusps:

\[
\ell_n
\longleftrightarrow
w(\ell_n)=h_n/2
\longrightarrow
 d_n=w_n+w_{n+1}
\longrightarrow
 B_{m,N}\to\infty.
\]

Thus the same exact collar identity that made local cuff spectral data universal in PF-032/PF-037 also forces the reflection-axis boundary divergence after the cusp channels have been projected out.

The asymptotic

\[
\ell_n\sim2\log\frac{4p_n}{g_n}
\]

controls the individual collar widths, but the sum relevant to the boundary counterterm telescopes and loses the gap fluctuations.

## 7. Literature / novelty check

Known ingredients:

- Zero-twist tight flutes and their intrinsic reflection/fixed geodesics are standard; Arredondo--Morales--Ramirez explicitly construct the fixed geodesics \(\gamma_n\) and the ray \(\beta\).
- Dirichlet/Neumann heat trace boundary coefficients are classical (McKean--Singer/Seeley/Gilkey theory).
- Burghelea--Friedlander--Kappeler determinant gluing and Guillarmou--Guillope Dirichlet-to-Neumann determinant formulas work with compact cutting hypersurfaces / compact surfaces with boundary.
- Relative zeta determinants on noncompact manifolds with cylindrical ends (e.g. Loya--Park and related work) require an additional regularized trace precisely because ordinary heat traces diverge at infinity.

Those theories do not automatically provide a determinant for an infinite-type half-flute whose reflection boundary has infinite length and crosses infinitely many changing pairs of pants. No novelty is claimed for the general heat coefficient. The project-specific result is the exact identification

\[
\text{boundary length through cuff }N
\sim\log p_N,
\]

with the divergence forced by the prime-flute collar sequence and telescoping after the standard zero-mode cure.

## 8. Research consequence

The branch

\[
\boxed{
\text{intrinsic reflection}
\to
\text{remove all cusp zero modes}
\to
\text{ordinary parity-relative determinant}
}
\]

is closed.

A surviving parity construction would have to perform **two** independent canonical renormalizations:

1. remove the infinitely many cusp zero channels;
2. renormalize the infinite geodesic reflection boundary (and still handle the short-orbit accumulation of PF-035/PF-036).

Unless the second subtraction is forced by a deeper geometric identity and leaves a nonlocal remainder that can be shown to depend nontrivially on prime-gap relations, it should not be counted as a natural prime zeta/determinant.
