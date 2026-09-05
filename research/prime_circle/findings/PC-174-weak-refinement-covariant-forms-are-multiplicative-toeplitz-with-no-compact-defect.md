# PC-174 — weak refinement-covariant first-order forms are multiplicative Toeplitz with no compact defect

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` for the relatively compact/Schatten/Fredholm-determinant escape inside the weak form-covariant boundary branch left open by PC-170/PC-171/PC-173. After the canonical first-order `|D|^{1/2}` normalization, every fixed continuous Hermitian boundary form satisfying exact Prime-Circle power-refinement covariance is a matrix-valued multiplicative Toeplitz operator: its Fourier matrix depends only on the rational ratio of absolute frequencies and the two orientation signs. This is a classical operator-theoretic class on the infinite polydisc, not a new Prime-Circle spectral object. More decisively, a normalized operator with this covariance is compact only when it is zero, so exact weak refinement admits no nonzero finite-rank, Schatten, trace-class, or Hilbert-Schmidt arithmetic defect from which an ordinary Fredholm determinant could be built.

PC-170 derived the weak covariance relation `C_n^*AC_n=nA` and observed that, at the raw Fourier-matrix level, it leaves arbitrary data on primitive lattice directions. PC-171 showed that the stronger intertwining `AC_n=nC_nA` collapses to four universal first-order parameters, while PC-173 closed fixed distributional multiplication coefficients. The natural remaining question is therefore whether the genuinely larger **weak** form relation supplies a tractable prime-sensitive operator class. It does supply a large class, but after the correct first-order normalization that class is exactly multiplicative Toeplitz and its compact-determinant subbranch vanishes.

## 1. First-order normalization removes the forced refinement scale

Work on the mean-zero homogeneous trace space

\[
\dot H^{1/2}(S^1)
=\left\{f=\sum_{k\ne0}f_ke_k:
\sum_{k\ne0}|k|\,|f_k|^2<\infty\right\},
\qquad e_k(\theta)=e^{ik\theta},
\]

with norm

\[
\|f\|_{\dot H^{1/2}}^2
=\sum_{k\ne0}|k|\,|f_k|^2.
\tag{1}
\]

Let

\[
J=|D|^{1/2}:
\dot H^{1/2}(S^1)\longrightarrow L^2_0(S^1),
\qquad
Je_k=|k|^{1/2}e_k,
\tag{2}
\]

where `L^2_0` denotes the mean-zero subspace. With the norm (1), `J` is unitary. For the Prime-Circle refinement isometry

\[
(C_nf)(\theta)=f(n\theta),
\qquad n\ge2,
\tag{3}
\]

one has exactly

\[
\boxed{JC_n=n^{1/2}C_nJ.}
\tag{4}
\]

Let `b` be a continuous Hermitian form on `\dot H^{1/2}`. By Riesz representation through `J`, there is a unique bounded self-adjoint operator `B` on `L^2_0(S^1)` such that

\[
\boxed{
b(f,g)=\langle Jf,BJg\rangle_{L^2}.
}
\tag{5}
\]

Demand the exact weak first-order covariance forced in PC-170,

\[
\boxed{
b(C_nf,C_ng)=n\,b(f,g)
\qquad(n\ge2).}
\tag{6}
\]

Using (4) in (5), equation (6) is equivalent to

\[
\boxed{C_n^*BC_n=B
\qquad(n\ge2).}
\tag{7}
\]

Thus the apparently unbounded first-order problem becomes a bounded fixed-point problem after the intrinsic DtN half-density normalization. No auxiliary spectral parameter or chosen arithmetic weight has been introduced.

## 2. The complete Fourier matrix is multiplicative Toeplitz

Write

\[
b_{jk}=\langle e_j,Be_k\rangle,
\qquad j,k\in\mathbb Z\setminus\{0\}.
\tag{8}
\]

Since `C_ne_k=e_{nk}`, equation (7) gives

\[
\boxed{b_{nj,nk}=b_{jk}}
\qquad(j,k\ne0,\ n\ge2).
\tag{9}
\]

Separate the two orientations. For `\varepsilon,\eta\in\{+1,-1\}` and positive integers `m,l`, define

\[
\Phi_{\varepsilon\eta}(m/l)
=b_{\varepsilon m,\eta l}.
\tag{10}
\]

This is well-defined on `\mathbb Q_{>0}`. Indeed, if `m/l=a/b` in lowest terms, then `m=da`, `l=db` for one positive integer `d`, and repeated use of (9) gives

\[
b_{\varepsilon m,\eta l}
=b_{\varepsilon a,\eta b}.
\]

Hence

\[
\boxed{
b_{\varepsilon m,\eta l}
=\Phi_{\varepsilon\eta}(m/l),
}
\tag{11}
\]

with Hermiticity equivalent to

\[
\boxed{
\Phi(q^{-1})=\Phi(q)^*,
}
\tag{12}
\]

where `\Phi(q)` is the `2 x 2` orientation matrix. Conversely, every bounded operator whose matrix has the form (11) satisfies (7). Therefore the full weak-covariant continuous first-order class is **exactly a `2 x 2` matrix-valued multiplicative Toeplitz class**.

The standard Bohr lift makes the prior-art identification explicit. Prime factorization sends

\[
m=\prod_p p^{\nu_p(m)}
\]

to the monomial `z^{\nu(m)}` and unitarily identifies `\ell^2(\mathbb N)` with the Hardy space `H^2(\mathbb T^\infty)`. Multiplication of the Fourier index by a prime becomes the coordinate shift `f\mapsto z_pf`. On each orientation block, (7) is therefore the infinite-polydisc Brown--Halmos relation, and (11) is precisely the multiplicative Toeplitz matrix condition `a_{ml}=F(m/l)` studied in the classical literature. The two orientations add only a finite matrix coefficient; they do not create a new arithmetic direction.

This also sharpens the phrase “arbitrary primitive lattice directions” in PC-170. Those directions are not an unclassified new Prime-Circle object: after first-order normalization they are coordinates on the multiplicative ratio group `\mathbb Q_{>0}^{\times}`, equivalently the free abelian lattice of prime valuations underlying the infinite-polydisc/Dirichlet-series model.

## 3. Exact covariance forbids every nonzero compact normalized defect

The large multiplicative Toeplitz class might still have supported a natural relative-compact perturbation of the universal `|D|` boundary scale, allowing a Fredholm determinant or discrete perturbative spectrum. Exact covariance rules this out without any regularity assumption on the Toeplitz symbol.

Assume `B` is compact and satisfies (7) for one fixed `n>1`. For any nonzero Fourier index `k`, the sequence

\[
e_{n^rk},\qquad r=0,1,2,\ldots,
\]

is orthonormal and hence converges weakly to zero. Compactness gives

\[
\boxed{\|Be_{n^rk}\|\longrightarrow0.}
\tag{13}
\]

Iterating (7), for any nonzero `j,k`,

\[
\begin{aligned}
b_{jk}
&=\langle e_j,Be_k\rangle\\
&=\langle e_{n^rj},Be_{n^rk}\rangle.
\end{aligned}
\tag{14}
\]

Therefore

\[
|b_{jk}|
\le \|Be_{n^rk}\|
\longrightarrow0,
\]

so every matrix entry vanishes and

\[
\boxed{B=0.}
\tag{15}
\]

This proof needs only one nontrivial refinement. Consequently, in the canonical first-order normalization,

\[
\boxed{
B\text{ compact and exactly weak-covariant}
\Longrightarrow B=0.
}
\tag{16}
\]

Finite-rank, Schatten-class, trace-class and Hilbert--Schmidt operators are compact, so all of them vanish as well. If a first-order boundary correction is written in form sense as

\[
A=|D|^{1/2}B|D|^{1/2},
\tag{17}
\]

then there is no nonzero exact-covariant correction whose normalized defect `|D|^{-1/2}A|D|^{-1/2}=B` is compact. In particular, the standard determinant route based on `det(I+zB)` for trace-class `B`, or its usual Schatten regularizations, cannot produce a new Prime-Circle zeta function inside this fixed exact-covariant class.

The noncompactness is not an accident of a particular symbol. Guo--Yan prove a related no-compact phenomenon for natural Toeplitz algebras on `H^2(\mathbb T^\infty)`; equation (16) is the stronger direct statement needed here for **every compact operator satisfying the refinement fixed-point relation**, regardless of whether one first represents it by a regular symbol.

## 4. The remaining symbol freedom is not yet Prime-Circle geometry

Equations (7)--(12) classify the ambient weak-covariant form, but they do not select `\Phi`. The same multiplicative Toeplitz class exists on the bare circle equipped with the power maps before primitive roots, cyclotomic shells, chord distances, old/new incidence, or the common-anchor von Mangoldt identity are inserted. Thus exact refinement covariance alone still supplies only a universal multiplicative coordinate system.

This is a particularly important novelty control because multiplicative Toeplitz matrices already have explicit number-theoretic and Riemann-zeta connections in the literature. Hilberdink's work treats matrices whose `(i,j)` entry is a function of `i/j`, their determinants, and their relation to extreme values of the Riemann zeta function. Therefore choosing a zeta-bearing `\Phi`, or wrapping an Euler product around the free ratio symbol, would be precisely the kind of external spectral wrapper excluded by the Prime-Circle mandate unless the symbol is **derived canonically from the embedded root geometry** and survives matched controls.

A viable continuation of the weak branch must therefore do substantially more than satisfy (7). It must derive a specific noncompact matrix-valued ratio symbol from intrinsic old/new chord or shell data, show that the derivation is not already a standard multiplicative Toeplitz/Dirichlet-series construction, and then obtain an RH-relevant spectral consequence that is not inherited from a chosen zeta-containing symbol.

## 5. Prior art and novelty audit

The ambient functional-analytic structure is classical. Hedenmalm--Lindqvist--Seip's Hardy space of Dirichlet series supplies the Bohr/infinite-polydisc model already recorded in `research/prime_circle/SOURCES.md`. Titus Hilberdink, **Determinants of multiplicative Toeplitz matrices**, *Acta Arithmetica* 125:3 (2006), 265--284, DOI `10.4064/aa125-3-4`, explicitly studies matrices `a_{ij}=f(i/j)` and their number-theoretic determinants. His chapter **Multiplicative Toeplitz matrices and the Riemann zeta function**, in *Four Faces of Number Theory* (EMS, 2015), pp. 77--122, DOI `10.4171/142`, makes the zeta connection itself explicit.

Kunyu Guo and Fugang Yan, **Toeplitz operators on the Hardy space over the infinite-dimensional polydisc**, *Acta Scientiarum Mathematicarum* 88 (2022), 223--262, DOI `10.1007/s44146-022-00016-z`, explicitly identify infinite multiplicative Toeplitz matrices with Toeplitz operators on `H^2(\mathbb T^\infty)`, prove a Brown--Halmos-type theorem, and show that natural infinite-polydisc Toeplitz algebras contain no nonzero compact operators.

No historical novelty is claimed for multiplicative Toeplitz structure, the Bohr lift, or zeta connections in that class. The durable Prime-Circle contribution is the exact compression (4)--(12) of the **specific weak Robin/refinement loophole left by PC-170** into this classical class, together with the elementary compactness obstruction (13)--(16), which closes the relative-compact/Schatten determinant route without assuming a regular symbol.

## 6. Stress tests and exact boundary of the result

The mean-zero homogeneous trace space is load-bearing only for the `|D|^{1/2}` normalization. The constant Fourier mode lies in the kernel of `|D|` and is not represented by (2); strong zero-mode behavior and fixed singular anchor distributions were treated separately in PC-171--PC-173. A boundary construction coupling the zero mode to nonzero modes through a more singular relation lies outside this theorem.

Continuity on `\dot H^{1/2}` is also load-bearing. Forms more singular than first order need not admit a bounded normalized operator `B`. Likewise the same form is required at every refinement. Level-dependent or shell-dependent families, cross-level relations, nonlinear forms, and renormalized growing-level limits do not obey one fixed equation (7) and are not classified here.

Most importantly, (16) is **not** a no-go for the entire weak branch. Nonzero bounded multiplicative Toeplitz operators are generally noncompact, and exact refinement leaves a large noncommutative matrix-valued symbol class. The result only kills the natural idea that the missing arithmetic could enter as a relatively compact/finitely supported/Schatten perturbation of the canonical first-order scale while exact covariance is retained. Noncompact determinants or renormalized spectral invariants require separate justification and cannot be inferred from (16).

The theorem has direct falsifiers. A counterexample to the classification must give a bounded normalized operator satisfying (7) whose entry `b_{\varepsilon m,\eta l}` is not a function of `m/l` and the two signs; equality of rational ratios plus (9) excludes this. A counterexample to the compactness obstruction must give a nonzero compact `B` satisfying `C_n^*BC_n=B` for one `n>1`; the weakly-null orbit argument (13)--(15) excludes this.

## 7. Consequence for the Prime-Circle/RH search

The weak form-covariant opening left by PC-170 is now structurally located:

\[
\boxed{
\text{exact first-order weak refinement}
\xrightarrow{|D|^{1/2}\text{ normalization}}
\text{matrix-valued multiplicative Toeplitz}.
}
\]

That localization is useful precisely because it separates a classical ambient operator algebra from the still-missing Prime-Circle input. The refinement semigroup does not choose the Toeplitz symbol, and its nonzero fixed points cannot be compact after normalization. Hence neither “primitive Fourier-pair freedom” nor a compact Fredholm defect is by itself evidence of a new RH mechanism.

What remains open is narrower and genuinely geometric: derive a **specific noncompact** multiplicative-Toeplitz symbol from embedded primitive-shell/chord/old-new data, or leave the fixed weak-form class through shell dependence, cross-level coupling, stronger singularity, or nonlinearity. Any successful continuation must then survive the existing Hilberdink/Dirichlet-series prior-art boundary rather than merely reproducing a known zeta-bearing multiplicative Toeplitz construction. No `s`-parameter, gamma factor, functional equation, zeta-zero set, or critical-line selector is produced by the classification itself.