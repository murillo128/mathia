# WI-131 — conjugate-lattice exponentials refute the blanket real-projection Riesz equivalence

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-CORRECTION`. This finding replaces withdrawn WI-129 after adversarial review. The exact bounded-strip equivalence quoted by Semmler (2010), and attributed there to Young, cannot be used literally without an additional hypothesis: for every fixed `b>0` the conjugate lattice

\[
\lambda_{n,+}=2n+ib,\qquad \lambda_{n,-}=2n-ib,\qquad n\in\mathbb Z,
\tag{1}
\]

has uniformly bounded imaginary parts and duplicated real projections, yet the full complex exponential family is a Riesz basis of `L^2(-\pi,\pi)`. Thus conjugation symmetry by itself does **not** obstruct scalar Riesz-basis stability. Any theorem used to transfer a bounded-strip complex system to its real projections must carry an additional separation/grouping/parametrization hypothesis that excludes (1), or else be interpreted in a different multiplicity convention.

This is a correction of a proof route, not a positive theorem about zeta zeros. It does not show that Lamzouri's actual frequency family is a scalar Riesz basis, does not contradict the macroscopic near-null requirement in WI-128, and does not change the certified simple-critical-zero proportion. It sharpens the reason that the grouped/confluent `g/h` geometry isolated in WI-130 is the relevant invariant.

## 1. Exact counterexample

Let

\[
I=(-\pi,\pi),\qquad J=(-\pi,0),
\]

and define the unitary fiberization

\[
U:L^2(I)\longrightarrow L^2(J;\mathbb C^2),\qquad
(Uf)(t)=\binom{f(t)}{f(t+\pi)}.
\tag{2}
\]

For the two exponentials attached to (1),

\[
\phi_{n,+}(t)=e^{i(2n+ib)t}=e^{i2nt}e^{-bt},
\qquad
\phi_{n,-}(t)=e^{i(2n-ib)t}=e^{i2nt}e^{bt}.
\tag{3}
\]

Since `e^{i2n(t+pi)}=e^{i2nt}`, their fibers are

\[
U\phi_{n,+}(t)
=e^{i2nt}
\binom{e^{-bt}}{e^{-b(t+\pi)}},
\qquad
U\phi_{n,-}(t)
=e^{i2nt}
\binom{e^{bt}}{e^{b(t+\pi)}}.
\tag{4}
\]

Introduce the matrix symbol

\[
A_b(t)=
\begin{pmatrix}
e^{-bt} & e^{bt}\\
e^{-b(t+\pi)} & e^{b(t+\pi)}
\end{pmatrix}.
\tag{5}
\]

Its determinant is independent of `t`:

\[
\det A_b(t)
=e^{b\pi}-e^{-b\pi}
=2\sinh(b\pi)>0.
\tag{6}
\]

On the compact interval `J`, all entries of `A_b(t)` are bounded. Equation (6) gives a fixed nonzero determinant, so all entries of `A_b(t)^{-1}` are bounded as well. Hence multiplication by `A_b` is a boundedly invertible operator on `L^2(J;\mathbb C^2)`.

The vector-valued Fourier family

\[
\{e^{i2nt}e_1,e^{i2nt}e_2:n\in\mathbb Z\}
\tag{7}
\]

is an orthogonal basis of `L^2(J;\mathbb C^2)`. Multiplication by `A_b` sends (7) exactly to the fiberized family in (4). Therefore

\[
\boxed{
\{e^{i(2n+ib)t},e^{i(2n-ib)t}:n\in\mathbb Z\}
\text{ is a Riesz basis of }L^2(-\pi,\pi).
}
\tag{8}
\]

No external theorem is needed for (8); it follows from the explicit boundedly invertible matrix multiplier.

By contrast, the real projections of (1) are

\[
2n,\qquad 2n,
\tag{9}
\]

so the projected exponential family contains every `e^{i2nt}` twice. The coefficient pair `(1,-1)` on either duplicate gives zero synthesis with coefficient norm squared `2`. Thus the projected family is not minimal and cannot satisfy a positive lower Riesz bound:

\[
\boxed{
\{e^{i\operatorname{Re}\lambda_{n,\pm}t}\}
\text{ is not a Riesz basis.}
}
\tag{10}
\]

Equations (8)--(10) directly refute the blanket implication used in WI-129.

## 2. Primary-source audit

Semmler, *Complete interpolating sequences, the discrete Muckenhoupt condition, and conformal mapping* (Ann. Acad. Sci. Fenn. Math. 35 (2010), 23--46), prints near the end of the paper the statement that when the imaginary parts of `{lambda_n}` are bounded, Corollary 1 of Section 8, Chapter 4 of Young's *An Introduction to Nonharmonic Fourier Series* asserts

\[
\{e^{i\operatorname{Re}\lambda_n t}\}
\text{ is a Riesz basis}
\quad\Longleftrightarrow\quad
\{e^{i\lambda_n t}\}
\text{ is a Riesz basis}.
\tag{11}
\]

The wording (11) is genuinely present in the published Semmler paper; this audit rechecked the primary PDF rather than relying on an informal summary. However, the explicit family (1) satisfies the stated bounded-imaginary-part hypothesis and contradicts (11) under the ordinary scalar Riesz-basis interpretation. Therefore the safe evidence-level conclusion is not that a classical theorem proves (11), but that **the printed sentence is missing some hypothesis or convention needed for literal validity in the duplicated-real-projection regime**.

Semmler cites R. M. Young, *An Introduction to Nonharmonic Fourier Series*, Chapter 4, Section 8, Corollary 1. The present audit has not yet reconciled the exact Young corollary with the counterexample. Until that source-level discrepancy is resolved, Mathia must not use (11) as an established implication for conjugation-invariant zeta frequencies.

Relevant established neighboring theory remains:

- Yurii I. Lyubarskii and Kristian Seip, *Complete interpolating sequences for Paley-Wiener spaces and Muckenhoupt's (A_p) condition*, Rev. Mat. Iberoam. 13 (1997), 361--376, arXiv:`math/9511212`, DOI `10.4171/RMI/224`;
- S. A. Avdonin and S. A. Ivanov, *Exponential Riesz bases of subspaces and divided differences*, Algebra i Analiz 13:3 (2001), 1--17; English transl. St. Petersburg Math. J. 13:3 (2002), 339--351, arXiv:`math/0103160`;
- S. Avdonin and W. Moran, *Ingham-type inequalities and Riesz bases of divided differences*, Int. J. Appl. Math. Comput. Sci. 11:4 (2001), 803--820.

These sources do not supply the false inference (11) for duplicated real projections; the grouped/divided-difference papers instead provide the natural theorem surface when frequencies cluster or conflate.

## 3. Why the counterexample is structurally relevant to Lamzouri screening

The geometry in (1) is not an artificial violation unrelated to the research line. It consists of conjugate pairs of fixed bounded depth at half-density centers, exactly the sort of symmetry that WI-129 had treated as automatically fatal to a scalar Riesz basis. The two imaginary directions restore the degree of freedom lost by the duplicated real projections: after two-fiberization, they become the two pointwise independent columns of `A_b(t)`.

This also explains why simply replacing every complex frequency by its real part is too destructive for the Lamzouri problem. Projection forgets the orientation encoded by the pair. In Lamzouri's coordinates that orientation is carried by

\[
g_z=\frac{f_z+f_{\bar z}}2,
\qquad
h_z=\frac{f_z-f_{\bar z}}{2i}.
\tag{12}
\]

WI-130 independently shows that raw scalar Vandermonde singular collapse can coexist with extensive `g/h` horizontal transversality. The present counterexample supplies the complementary correction on the harmonic-analysis side: scalar complex exponentials can remain perfectly Riesz-stable even when their real projections collide exactly. Both facts point away from projection-only criteria and toward grouped/vector-valued or divided-difference finite-section invariants.

## 4. Stress tests and scope

The Riesz constants in (8) are not uniform as `b -> 0`. Indeed

\[
\det A_b=2\sinh(b\pi)\sim2\pi b,
\tag{13}
\]

so the condition number of the matrix multiplier degenerates in the confluent limit. This is consistent with the need to renormalize the odd pair direction by `1/b`, which produces the derivative/divided-difference mode. Thus (8) does **not** provide a uniform near-critical-line lower bound for Lamzouri's `h` sector.

Nor can the common Lamzouri envelope be ignored. Multiplication by a bounded envelope is harmless for upper estimates but, if the envelope vanishes or is not bounded away from zero, it need not preserve a global lower Riesz constant. The counterexample therefore refutes only the claimed blanket projection equivalence and the inference from conjugation symmetry alone. It is not a black-box positive Riesz theorem for the weighted Lamzouri family.

Finally, the example is a full infinite basis statement, whereas WI-128 asks about a positive-density bottom singular-value sector of finite reciprocal-node Vandermonde sections. A global Riesz basis theorem would be stronger than some finite-section statements and weaker than others depending on ordering/grouping. No contradiction with WI-128 follows in either direction without an explicit finite-section transfer.

## 5. Research consequence

The following route is now closed:

\[
\text{conjugate pairs}
\Longrightarrow
\text{duplicate real projections}
\Longrightarrow
\text{complex scalar family not Riesz}.
\tag{14}
\]

The second implication is false. A viable obstruction to extensive Lamzouri screening must instead use information that survives the conjugate-pair orientation: grouped/subspace Riesz bounds, divided differences, vector-valued complete interpolation, or zeta-specific geometry/correlation constraints. In particular, WI-130's conclusion that the `g/h` quotient rather than the raw scalar tail is the relevant invariant is strengthened rather than weakened by this correction.

A useful future source audit is to recover Young's Chapter 4, Section 8, Corollary 1 in its full context and identify the missing hypothesis or convention behind Semmler's printed sentence. That source reconciliation is worthwhile, but it is not needed to establish the mathematical correction: the counterexample (1)--(10) is exact and self-contained.

## 6. Novelty and claim boundary

The matrix-fiber proof above is an elementary exact deduction. No priority is claimed for the example or for noticing the source discrepancy. The substantive Mathia result is the correction of WI-129's load-bearing inference and the resulting narrowing of the relevant theorem surface for WI-128/WI-130.

No unconditional zeta-zero proportion changes. No off-line screening configuration is asserted to occur for zeta. No scalar Riesz-basis theorem is claimed for Lamzouri's weighted functions.