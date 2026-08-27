# PF-081 — two-scale Feshbach isolation fixes the first upstream-memory coefficient

**Status:** `SUPPORTED-SECOND-ORDER-CANDIDATE` with an exact finite-dimensional coefficient and a reduced-resolvent mechanism on the true surface. The remaining analytic gate is a uniform two-scale collar remainder estimate. No RH claim.

PF-080 found, in the exact harmonic-collar Ritz operator, an effective-resistance correction of size \(w_j^2/w_{j-1}\). The key uncertainty was whether the true surface Laplacian could generate unrelated corrections at the same or larger scale and thereby erase the finite-matrix coefficient.

The simplest genuinely multiscale case shows that the candidate is much more rigid than a generic Ritz artifact. For two nested separating necks, the only spectral denominator capable of producing the singular scale \(b^2/a\) is the stronger small eigenvalue itself. After that mode is projected out, the remaining surface spectrum stays uniformly separated from zero. Consequently the coefficient of the \(b^2/a\) term is forced by the limiting graph eigenvectors.

This does not yet replace the final uniform PDE estimate, but it reduces PF-080's open problem to controlling nonsingular collar/high-mode remainders; the interscale coefficient itself is no longer free.

## 1. Two nested necks

Consider a genus-zero finite-area tangent consisting of three pairs of pants in a chain. Let the two separating geodesics have lengths

\[
a\to0,\qquad b\to0,\qquad \frac ba\to0.
\]

The \(a\)-neck is the stronger neck joining the first two pants; the much weaker \(b\)-neck joins that two-pants cluster to the third pants.

At the graph level the weighted path Laplacian is

\[
G(a,b)=
\begin{pmatrix}
a&-a&0\\
-a&a+b&-b\\
0&-b&b
\end{pmatrix}.
\]

Its nonzero eigenvalues are exactly

\[
\mu_\pm
=a+b\pm\sqrt{a^2-ab+b^2}.
\]

Thus, for \(b/a\to0\),

\[
\boxed{
\mu_-
=\frac32 b-\frac38\frac{b^2}{a}
+O\!\left(\frac{b^3}{a^2}\right).
}
\]

Burger's normalization for a chain of pants of area \(2\pi\) is \(1/(2\pi^2)\), giving the candidate surface expansion

\[
\boxed{
\lambda_{\rm weak}
=\frac{3}{4\pi^2}b
-\frac{3}{16\pi^2}\frac{b^2}{a}
+\cdots.
}
\]

The issue is whether the second coefficient survives the full hyperbolic surface.

## 2. The coefficient is a reduced-resolvent pole

Set \(b=0\). The surface splits into

- a left four-punctured component \(X_a\), itself containing the short \(a\)-neck;
- a right thrice-punctured sphere.

Besides the constants, \(X_a\) has one small positive eigenvalue

\[
\lambda_a=\frac{a}{\pi^2}(1+o(1)),
\]

with normalized eigenfunction tending to the antisymmetric graph mode on its two pants.

On the three-vertex normalized low-mode space, let

\[
u=\frac1{\sqrt2}(1,-1,0)
\]

be that stronger internal mode. In the \(b=0\) zero eigenspace, the weak-neck first-order nonconstant state is

\[
\psi=\frac1{\sqrt6}(1,1,-2).
\]

The weak edge perturbation is

\[
V_b=\frac{b}{2\pi^2}B_2,
\qquad
B_2=(e_2-e_3)(e_2-e_3)^T.
\]

A direct calculation gives

\[
\boxed{
|\langle \nu,B_2\psi\rangle|^2=\frac34.
}
\]

Therefore the contribution obtained by eliminating the stronger small mode is

\[
-\frac{|\langle \nu,V_b\psi\rangle|^2}{\lambda_a}
=
-\frac{3b^2}{16\pi^4\lambda_a}.
\]

Using \(\lambda_a\sim a/\pi^2\),

\[
\boxed{
-\frac{3b^2}{16\pi^4\lambda_a}
= -\frac{3}{16\pi^2}\frac{b^2}{a}(1+o(1)).
}
\]

This is exactly the PF-080 effective-resistance coefficient.

The important point is conceptual: the denominator \(1/a\) is not supplied by a local collar expansion. It is the pole of the reduced resolvent caused by the *previous small eigenvalue*.

## 3. Why the high sector cannot create another \(b^2/a\) term

After the constants and the single eigenfunction at \(\lambda_a\) are removed from \(X_a\), the remaining spectral sector is uniformly separated from zero as \(a\to0\). The stable limit is a union of thrice-punctured spheres, whose nonconstant spectral threshold is \(1/4\); genus-zero small-eigenvalue bounds likewise leave only the neck mode in this two-pants component.

Hence a Feshbach decomposition of the weak-neck problem has the form

\[
H_{\rm eff}(\lambda)
=H_{00}(b)
-
H_{0s}(b)(H_{ss}-\lambda)^{-1}H_{s0}(b)
-
H_{0h}(b)(H_{hh}-\lambda)^{-1}H_{h0}(b),
\]

where \(s\) is the one-dimensional stronger small mode and \(h\) is the uniformly gapped high sector.

The \(s\)-term carries

\[
(H_{ss}-\lambda)^{-1}\sim\lambda_a^{-1}\asymp a^{-1},
\]

while the high resolvent is \(O(1)\). Thus:

\[
\boxed{
\text{the only possible }b^2/a\text{ correction comes from the stronger small mode.}
}
\]

The high sector can contribute ordinary \(O(b^2)\) terms (and collar geometry can produce \(b^2|\log b|\)-type terms), but it cannot independently change the coefficient of the singular \(b^2/a\) term.

This is the main strengthening relative to PF-080.

## 4. Mild scale condition separating memory from local collar corrections

To make the upstream term asymptotically visible above the standard local collar error, it is enough to impose

\[
\boxed{
a\,|\log b|\to0.}
\]

Then

\[
b^2|\log b|
=o\!\left(\frac{b^2}{a}\right).
\]

Together with \(b/a\to0\), this also makes the next graph term

\[
O(b^3/a^2)
=o(b^2/a).
\]

The algebraic/hierarchical prime patterns used in PF-054 and PF-079 lie naturally in such a regime; the condition excludes only extremely super-exponential separation where the ordinary collar logarithm could compete with the memory scale.

Under the corresponding uniform collar-to-Feshbach remainder estimate, the true surface statement is

\[
\boxed{
\lambda_{\rm weak}
=
\frac{3}{4\pi^2}b
-
\frac{3}{16\pi^2}\frac{b^2}{a}
+o\!\left(\frac{b^2}{a}\right).
}
\]

Equivalently, the second term can be written spectrally as

\[
\boxed{
-\frac{3b^2}{16\pi^4\lambda_a}(1+o(1)).
}
\]

This form makes the recursive mechanism explicit: a weaker spectral scale feels the stronger part of the surface through its reduced resolvent.

## 5. Exact prime-gap geometry

For four ordered prime offsets with consecutive gaps \(d_1,d_2,d_3\), the exact multi-gap necks are

\[
\boxed{
\sinh^2\frac a4=\frac{d_1}{d_2},
\qquad
\sinh^2\frac b4=\frac{d_1+d_2}{d_3}.
}
\]

In the strongly hierarchical regime \(d_1\ll d_2\ll d_3\),

\[
a\sim4\sqrt{\frac{d_1}{d_2}},
\qquad
b\sim4\sqrt{\frac{d_2}{d_3}}.
\]

Since the distinguished prime cuffs obey

\[
\ell_i(P)=2\log\frac{4P}{d_i}+o(1),
\]

we also have

\[
a\sim4e^{-(\ell_1-\ell_2)/4},
\qquad
b\sim4e^{-(\ell_2-\ell_3)/4}.
\]

The singular correction therefore depends on two ordered cuff contrasts at once:

\[
\boxed{
\frac{b^2}{a}
\sim
4\exp\!\left[
-\frac{\ell_2-\ell_3}{2}
+\frac{\ell_1-\ell_2}{4}
\right].
}
\]

This is qualitatively different from the PF-079 leading tropical profile, which sees only the current scale.

## 6. Consequence for scattering

For the finite tangent, a small residual eigenvalue corresponds to a physical scattering pole

\[
s(1-s)=\lambda,
\qquad s\to1.
\]

Hence

\[
1-s=\lambda+O(\lambda^2).
\]

Whenever \(\lambda^2=o(b^2/a)\) in the selected hierarchy, the same upstream term appears in the pole location:

\[
1-s_{\rm weak}
=
\frac{3}{4\pi^2}b
-
\frac{3}{16\pi^2}\frac{b^2}{a}
+o(b^2/a).
\]

This is a finite-tangent statement. It does not assert the existence of a global scattering matrix for the infinite prime flute.

## 7. Literature / novelty audit

Known results already cover the surrounding machinery:

- Burger gives the first-order weighted-graph reduction of small eigenvalues under hyperbolic degeneration.
- Große--Rupflin obtain sharp one-disconnecting-collar estimates and identify the optimal local error scale.
- Chaudhary treats multiple collapsing disconnecting geodesics and proves that the small eigenvalues are determined by their lengths to first order. Importantly, the thesis explicitly notes that more precise dependence on the *relative lengths* of several small geodesics remains complicated and requires further analysis; its collar derivative formula points directly to that dependence.
- General Feshbach/reduced-resolvent perturbation theory is classical.

Directed searches for *two collapsing geodesics + second-order eigenvalue*, *nested hyperbolic collars + eigenvalue expansion*, and *multiple pinching + effective resistance second order* did not locate the coefficient above.

No novelty is claimed for Feshbach theory or graph perturbation. The potentially new narrow statement is that, in a nested hyperbolic two-scale degeneration, the first singular subleading coefficient of the **true** small spectrum is fixed by the previous small eigenmode and agrees with the prime-gap effective-resistance coefficient.

## 8. Remaining analytic gate / falsification

The only unresolved step for a theorem-level joint asymptotic is to make the weak-neck collar matching estimate uniform as the left component simultaneously develops the \(a\)-neck, after explicitly removing its one small eigenmode.

A decisive sufficient estimate is

\[
R_{\rm high}(a,b)
=O(b^2|\log b|+b^2)
\]

uniformly in \(a\), after the \(\lambda_a^{-1}\) pole is extracted. Under

\[
b/a\to0,
\qquad
a|\log b|\to0,
\]

this is \(o(b^2/a)\).

The mechanism is falsified if the pole-subtracted high-sector matching develops another term of order \(b^2/a\) with an independent coefficient. Spectrally, that would require a second mode with eigenvalue comparable to \(a\); the topology of this three-pants chain predicts none.

The most informative next calculation is therefore not another graph expansion but a uniform constant-mode DtN/Feshbach expansion across the weak collar with the \(\lambda_a\) pole separated explicitly.
