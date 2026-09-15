---
id: WP-312
title: Fixed boundary Julia–Nevanlinna reduction cannot repair the Mangoldt–Gamma asymptotic
branch: weil_positivity
status: supported
kind: fixed-boundary-julia-nevanlinna-gamma-obstruction
claim_strength: exact asymptotic obstruction for every finite chain of classical Julia–Nevanlinna reductions at fixed real boundary nodes of the reflected pole-normalized Mangoldt Herglotz response, with the canonical positivity-preserving normalization back to a unit logarithmic end; every regular node creates a strictly positive (log y)/y term, while an all-pole chain only increases the already-wrong positive y^-2 curvature
created: 2026-09-15
related: [WP-304, WP-305, WP-308, WP-310, WP-311]
prior_art:
  - Jim Agler and N. J. Young, Boundary Nevanlinna-Pick interpolation via reduction and augmentation, Mathematische Zeitschrift 268 (2011), no. 3-4, 791-817, DOI 10.1007/s00209-010-0696-3, arXiv:0905.4759, for the classical Julia–Nevanlinna boundary reduction formulas and preservation of the Pick class
  - NIST Digital Library of Mathematical Functions, Section 5.11, especially Eq. 5.11.2, for the Riemann digamma asymptotic used in WP-305
---

# WP-312 — Fixed boundary Julia–Nevanlinna reduction cannot repair the Mangoldt–Gamma asymptotic

## Claim

`WP-311` rules out finite Schur stripping at fixed **interior** interpolation points but deliberately leaves boundary-reference reduction open. The classical Julia–Nevanlinna boundary algorithm can also be tested exactly. For the reflected critical Mangoldt Herglotz response of `WP-305`, every finite chain at fixed real boundary nodes fails, with a sharp dichotomy.

Let `f` be a nonconstant Pick/Herglotz function with the logarithmic end

\[
\operatorname{Re} f(iy)
=
\log y+c+A\frac{\log y}{y}+O(y^{-1}),
\qquad
\operatorname{Im} f(iy)
=
q+O\!\left(\frac{(\log y)^2}{y}\right),
\qquad q>0.
\tag{1}
\]

At a regular real boundary point `x`, assume `f` extends analytically across `x`, takes a real value `w=f(x)`, and has derivative

\[
d=f'(x)>0.
\tag{2}
\]

The Julia–Nevanlinna reduction is

\[
g_x(z)
=
-\frac1{f(z)-w}
+\frac1{d(z-x)},
\tag{3}
\]

and is again Pick class. Since `g_x(iy)->0`, returning its boundary value `0` to the same logarithmic end by an upper-half-plane automorphism is unique up to a real translation once the unit logarithmic coefficient is fixed. The normalized response is therefore

\[
\mathcal J_x[f](z)
=
-\frac1{g_x(z)}+\beta
=
\frac{d(z-x)(f(z)-w)}{d(z-x)-(f(z)-w)}+\beta,
\qquad \beta\in\mathbb R.
\tag{4}
\]

It satisfies

\[
\boxed{
\operatorname{Re}\mathcal J_x[f](iy)
=
\log y+c'
+\left(A+\frac{2q}{d}\right)\frac{\log y}{y}
+O(y^{-1})
}
\tag{5}
\]

and

\[
\operatorname{Im}\mathcal J_x[f](iy)
=
q+O\!\left(\frac{(\log y)^2}{y}\right).
\tag{6}
\]

Thus every regular fixed boundary reduction adds the **strictly positive** increment `2q/d` to the logarithmic-over-linear coefficient.

The other classical boundary case is a pole. If `f` has a real simple pole at `x` with residue `R<0`, Julia–Nevanlinna reduction is simply

\[
g_x(z)=f(z)-\frac{R}{z-x}.
\tag{7}
\]

This preserves the unit logarithmic end and changes no `log(y)/y` coefficient. For the reflected Mangoldt response `m_-`, however, every pole is

\[
x_n=-\log n,
\qquad
R_n=-w_n,
\qquad
w_n:=\frac{\Lambda(n)}{n+1}>0,
\tag{8}
\]

so stripping that pole changes the first even real curvature by

\[
\boxed{
A_{\rm M}\longmapsto A_{\rm M}+R_nx_n
=A_{\rm M}+\frac{\Lambda(n)\log n}{n+1}>A_{\rm M}>0.
}
\tag{9}
\]

Consequently every finite fixed-boundary chain starting from `m_-` falls into one of two classes:

- if the chain contains at least one regular boundary node, its final response has a strictly positive `log(y)/y` coefficient, whereas the Riemann Gamma channel has none;
- if the chain consists only of pole nodes, it has no `log(y)/y` defect but its `y^-2` coefficient stays positive and becomes strictly larger, whereas the Riemann Gamma coefficient is `-1/24`.

Hence

\[
\boxed{
\text{finite fixed-boundary Julia–Nevanlinna reduction cannot turn the WP-305 source into the Riemann Gamma asymptotic.}
}
\tag{10}
\]

**Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + FIXED-BOUNDARY-JULIA-NEVANLINNA-NO-GO + REGULAR-NODE-LOG-OVER-LINEAR-CONTAMINATION + POLE-STRIPPING-CURVATURE-WORSENING + FINITE-CHAIN-STABILITY + CLASSICAL-REDUCTION-PRIOR-ART + MATCHED-CONTROLS + NOT-WEIL-POSITIVITY`.

## 1. Classical boundary reduction supplies the positivity theorem

Agler and Young formulate the Julia–Nevanlinna reduction for Pick functions in exactly the two cases needed here. If `f` is analytic and real at `x`, then every nonconstant Pick function has `f'(x)>0`, and (3) is Pick class. If `f` has a pole at `x`, its residue is negative and (7) is Pick class. Their reduction corresponds to Schur complementation of the associated boundary Pick matrix.

Thus positivity is not being imposed after the arithmetic source is inspected: it is inherited from the classical Pick-class theorem. The question is whether this independent sign-preserving operation can supply the missing finite–archimedean structure. Equations (5) and (9) show that, for the already-fixed Mathia source, it cannot.

For the reflected source `m_-`, the representing measure is the positive atomic reflection of `WP-304`'s pole-normalized Mangoldt measure,

\[
\mu_-
=
\sum_{n=p^k}
\frac{\Lambda(n)}{n+1}\,\delta_{-\log n}.
\tag{11}
\]

Away from its atoms, `m_-` extends analytically through the real axis and is real there. Moreover

\[
m_-'(x)
=
\sum_{n=p^k}
\frac{\Lambda(n)}{(n+1)(-\log n-x)^2}
\in(0,\infty)
\tag{12}
\]

for every fixed real `x` outside the support: positivity is termwise, while convergence follows from the tail `sum Lambda(n)/(n (log n)^2)`. Hence the regular-node case is genuinely available on the canonical source and not a formal boundary limit of the interior calculation.

## 2. The regular-node normalization is forced

Put

\[
F(z):=f(z)-w,
\qquad
Z:=z-x.
\tag{13}
\]

Then (3) is

\[
g_x(z)=\frac{F(z)-dZ}{dZF(z)}.
\tag{14}
\]

Because `F(iy)=log y+O(1)+iq+o(1)` while `Z=iy-x`,

\[
g_x(iy)=-\frac1{F(iy)}+O(y^{-1})\longrightarrow0.
\tag{15}
\]

Every upper-half-plane automorphism sending the real boundary point `0` to infinity has the form

\[
T(u)=\beta-\frac{\lambda}{u},
\qquad
\lambda>0,
\quad \beta\in\mathbb R.
\tag{16}
\]

Since `-1/g_x(iy)=log y+O(1)`, the transformed leading logarithmic coefficient is `lambda`. Matching the unit logarithmic end therefore forces `lambda=1`; only the real constant `beta` remains. This gives (4). There is no hidden scalar normalization parameter available to cancel the subleading term.

The exceptional possibility `g_x identically 0` would mean `f(z)=w+d(z-x)`, a half-plane automorphism with linear growth. It is incompatible with the logarithmic end (1), so the inversion in (4) is nondegenerate throughout the present class.

## 3. Every regular boundary node creates positive `log(y)/y`

From (4),

\[
\mathcal J_x[f](z)-\beta
=
F(z)\left(1-\frac{F(z)}{dZ}\right)^{-1}.
\tag{17}
\]

Along `z=iy`, `|F/(dZ)|=O((log y)/y)`, hence

\[
\mathcal J_x[f](iy)-\beta
=
F(iy)+\frac{F(iy)^2}{d(iy-x)}
+O\!\left(\frac{(\log y)^3}{y^2}\right).
\tag{18}
\]

Write

\[
F(iy)=L(y)+iQ(y),
\qquad
L(y)=\log y+O(1),
\qquad
Q(y)=q+O\!\left(\frac{(\log y)^2}{y}\right).
\tag{19}
\]

Since

\[
\frac1{iy-x}=-\frac{i}{y}+O(y^{-2}),
\tag{20}
\]

we obtain

\[
\operatorname{Re}\frac{F(iy)^2}{d(iy-x)}
=
\frac{2L(y)Q(y)}{dy}
+O\!\left(\frac{(\log y)^2}{y^2}\right)
=
\frac{2q}{d}\frac{\log y}{y}+O(y^{-1}).
\tag{21}
\]

Combining (1), (18), and (21) proves (5). The imaginary part of the same correction is `-(L^2-Q^2)/(dy)+O((log y)/y^2)`, which is `O((log y)^2/y)` and proves (6). Therefore the limiting phase `q` survives and the argument iterates.

For `m_-`, `q=pi/2`. Before the first regular node, any number of pole reductions changes only inverse-power terms and leaves `q=pi/2` and the `log(y)/y` coefficient zero. The first regular node therefore creates

\[
\frac{2q}{d}=\frac{\pi}{d}>0.
\tag{22}
\]

Every later regular node adds another positive increment, while pole stripping cannot alter that order. Once a regular boundary step occurs, the Gamma comparison is already lost before the `y^-2` curvature is reached.

## 4. Pole stripping moves the curvature in the wrong direction

For a simple real pole at `x` with residue `R<0`, the classical reduction (7) changes the imaginary-axis response by

\[
-\frac{R}{iy-x}
=
\frac{Rx}{x^2+y^2}
+i\frac{Ry}{x^2+y^2}.
\tag{23}
\]

Thus it leaves both the leading logarithm and any `log(y)/y` coefficient unchanged, while its first real contribution is

\[
\frac{Rx}{y^2}+O(y^{-4}).
\tag{24}
\]

For `m_-`, (8) gives

\[
R_nx_n
=
\frac{\Lambda(n)\log n}{n+1}>0.
\tag{25}
\]

Starting from `WP-305`,

\[
\operatorname{Re}m_-(iy)
=
\log y-B+\frac{A_{\rm M}}{y^2}+o(y^{-2}),
\qquad A_{\rm M}>0,
\tag{26}
\]

so stripping any finite set `S` of Mangoldt poles gives

\[
\operatorname{Re}m_{-,S}(iy)
=
\log y-B_S
+
\frac{A_{\rm M}+\sum_{n\in S}\Lambda(n)\log n/(n+1)}{y^2}
+o(y^{-2}).
\tag{27}
\]

The Riemann archimedean term instead satisfies

\[
\operatorname{Re}\psi\!\left(\frac14+\frac{iy}{2}\right)
=
\log\frac y2-\frac1{24y^2}+O(y^{-4}).
\tag{28}
\]

An all-pole boundary chain therefore makes the existing sign mismatch strictly worse. This is not a tunable subtraction: the negative residue and the negative pole location are both fixed by positivity and by the reflected arithmetic source.

## 5. Finite-chain classification and aggressive falsification

The two cases above exhaust the classical Julia–Nevanlinna reduction at a fixed real node for the meromorphic reflected Mangoldt response and for every function obtained from it by a finite sequence of the same meromorphic operations.

Consider any finite chain, with each regular reduction returned to the unit-log end by the forced normalization (4).

If at least one node is regular, take the first such node. All preceding steps are pole removals, so the input still has zero `log(y)/y` coefficient and limiting imaginary height `pi/2`. Equation (22) creates a strictly positive coefficient. Subsequent regular steps add positive increments by (5), and pole steps affect only inverse powers. The final coefficient cannot return to zero.

If no node is regular, every step removes a Mangoldt pole. Equation (27) applies and the `y^-2` coefficient is strictly more positive than the already-positive `A_M`. It cannot equal the negative Gamma coefficient.

The obstruction survives arbitrary choices of fixed regular nodes because `d>0` only changes the magnitude of the defect. Taking a sequence of fixed nodes close to a pole can make `d` large and an individual regular increment small, but every nonzero finite increment remains positive; the exact pole limit switches to (7), where the curvature obstruction takes over instead.

Several genuine escape routes remain outside the claim. A node that itself moves with the high-energy scale is a scale-dependent cutoff/renormalization, not a fixed Julia–Nevanlinna reduction. An infinite chain needs separate convergence and boundary-limit control. Matrix/operator-valued Schur complements, generalized resolvents, noninvertible boundary maps, and an independently supplied archimedean channel can change the mechanism. So can a nonseparable finite–archimedean geometry acting before scalar Herglotz reduction. Those are precisely the kinds of added structure still allowed by the research mandate.

The boundary point at infinity is also separate: `WP-310` already shows that the classical moment-Schur transform there cannot start on the critical infinite-mass Mangoldt source. The present result closes the remaining **fixed finite real boundary** version left open by `WP-311`; it does not silently extend that theorem to moving or operator-valued boundary data.

## 6. Prior-art and novelty audit

The boundary reduction itself is classical. Agler and Young give both formulas used here: at a regular real node, Julia reduction is `-1/(f-f(x))+1/(f'(x)(z-x))`; at a real pole, reduction subtracts the pole. They prove that reduction preserves the Pick class and identify it with Schur complementation of boundary Pick matrices. No novelty is claimed for these facts, for Julia–Caratheodory positivity of the derivative, or for the Möbius normalization.

A bounded literature audit over Julia–Nevanlinna boundary reduction, boundary Nevanlinna–Pick interpolation, logarithmic Herglotz asymptotics, and Gamma/digamma asymptotics did not identify the specific high-energy comparison (5), the pole-sign calculation (9), or their finite-chain collision with the reflected pole-normalized Mangoldt source. The Mathia-specific content is therefore not a new interpolation theorem; it is the exact falsification of a live completion route produced by applying classical positivity-preserving boundary reduction to the source and normalization already forced by `WP-304`–`WP-311`.

Primary reference:

- Jim Agler and N. J. Young, *Boundary Nevanlinna-Pick interpolation via reduction and augmentation*, Math. Z. 268 (2011), 791–817, DOI `10.1007/s00209-010-0696-3`, arXiv:`0905.4759`.

The Riemann Gamma asymptotic is the same DLMF 5.11 expansion audited in `WP-305`.

## 7. Consequence for the research frontier

The scalar fixed-reference Schur/Nevanlinna escape is now closed at all three natural locations: `WP-310` excludes the classical moment step at infinity, `WP-311` excludes fixed interior interpolation points, and the present result excludes fixed real boundary nodes. The mechanisms differ but the asymptotic lesson is consistent: positivity-preserving scalar stripping does not manufacture the missing Gamma completion from the critical Mangoldt source.

The surviving frontier therefore has to change a hypothesis that mattered. In particular, it must use a genuinely scale-dependent boundary construction with an independently forced renormalization law, an infinite-dimensional/operator-valued boundary sector, or a nonseparable finite–archimedean coupling before the scalar asymptotic is formed. Merely moving the Schur reference from the interior to a fixed boundary point does not evade the obstruction.

## Conclusion

Classical Julia–Nevanlinna positivity does not rescue the reflected critical Mangoldt Herglotz source. At a regular fixed boundary node, the unique unit-log end normalization creates a positive `log(y)/y` defect; at a source pole, the classical reduction removes a positive atom and pushes the already-wrong `y^-2` curvature farther positive. Every finite fixed-boundary chain therefore misses the Riemann Gamma asymptotic before it can supply a global Weil-positive geometry.
