# PF-069 — prime-vector limit points force a positive interval of primitive length accumulation

**Status:** `DECISIVE-NEGATIVE` for any attempt to rescue a global Selberg/wave-trace theory merely by removing the short-orbit sector; `EXACT-DERIVED` arithmetic-to-geometric consequence.

## 1. Exact prime-flute length from three consecutive gaps

Let four consecutive prime-derived boundary points be

\[
a<b<c<d,
\]

and write their Euclidean spacings on the real boundary as

\[
X=b-a,\qquad Y=c-b,\qquad Z=d-c.
\]

The exact orthogonal-circle / side-pairing calculation from PF-004 gives a primitive simple separating closed geodesic \(\gamma\) with

\[
\boxed{
\sinh^2\frac{L}{4}
=\chi
:=\frac{(c-b)(d-a)}{(b-a)(d-c)}
=\frac{Y(X+Y+Z)}{XZ}.
}
\]

Thus

\[
\boxed{L=4\operatorname{arsinh}\sqrt\chi.}
\]

For the actual prime-circle points

\[
u_p=\cot\frac{\pi}{p},
\]

we have, whenever \(q-p=o(p)\),

\[
u_q-u_p=\frac{q-p}{\pi}(1+o(1)).
\]

Hence if three consecutive normalized prime gaps converge,

\[
\left(
\frac{g_n}{\log p_n},
\frac{g_{n+1}}{\log p_{n+1}},
\frac{g_{n+2}}{\log p_{n+2}}
\right)
\longrightarrow(x,y,z)\in(0,\infty)^3,
\]

then the exact prime-flute cross-ratio and primitive length converge to

\[
\boxed{
\chi_n\longrightarrow
F(x,y,z):=\frac{y(x+y+z)}{xz},
}
\]

and

\[
\boxed{
L_n\longrightarrow
4\operatorname{arsinh}\sqrt{F(x,y,z)}.
}
\]

## 2. Banks–Freiberg–Maynard gives a topologically large set of 3-gap limit vectors

Let \(\mathcal L_3\subset[0,\infty)^3\) denote the set of finite limit points of vectors of three consecutive normalized prime gaps.

Banks–Freiberg–Maynard prove the following multidimensional hitting theorem: for \(m=3\), if

\[
\beta_1\le\cdots\le\beta_K,
\qquad K=8m^2+16m=120,
\]

then for at least one quadruple

\[
1\le i<j<k<\ell\le K
\]

the vector

\[
(\beta_j-\beta_i,\;\beta_k-\beta_j,\;\beta_\ell-\beta_k)
\]

belongs to \(\mathcal L_3\).

Reference: W. D. Banks, T. Freiberg, J. Maynard, *On limit points of the sequence of normalized prime gaps*, Proc. LMS 113 (2016), Theorem 1.3, arXiv:1404.5094.

We now use this theorem with a one-parameter family

\[
\boxed{\beta_q(t)=q+tq^2,\qquad 1\le q\le120,\quad 0\le t\le1.}
\]

For a fixed quadruple \(T=(i,j,k,\ell)\), define

\[
V_T(t)=
(\beta_j(t)-\beta_i(t),\beta_k(t)-\beta_j(t),\beta_\ell(t)-\beta_k(t)).
\]

The limit set \(\mathcal L_3\) is closed. Therefore

\[
A_T:=\{t\in[0,1]:V_T(t)\in\mathcal L_3\}
\]

is closed. The BFM theorem says

\[
[0,1]=\bigcup_T A_T,
\]

where the union is finite. By the Baire category theorem (in fact, finite closed-cover elementary topology suffices), at least one \(A_T\) contains a nonempty open interval \(J\).

Thus there is one fixed quadruple \(i<j<k<\ell\) such that

\[
\boxed{V_T(t)\in\mathcal L_3\quad\text{for every }t\in J.}
\]

This is already stronger topologically than merely knowing \(\mathcal L_3\) has positive Lebesgue measure (the latter was proved much earlier by Hildebrand–Maier).

## 3. The prime-flute cross-ratio varies nontrivially along that curve

For the above family, put

\[
x=\beta_j-\beta_i,\quad
y=\beta_k-\beta_j,\quad z=\beta_\ell-\beta_k.
\]

Then

\[
F(x,y,z)
= C_T
\frac{(1+(j+k)t)(1+(i+\ell)t)}
{(1+(i+j)t)(1+(k+\ell)t)},
\]

where

\[
C_T=\frac{(k-j)(\ell-i)}{(j-i)(\ell-k)}>0.
\]

This rational function is not constant. Indeed, both quadratic polynomials have the same linear coefficient, while the difference of their quadratic coefficients is

\[
(j+k)(i+\ell)-(i+j)(k+\ell)
=(i-k)(j-\ell)>0.
\]

Hence \(F(V_T(t))\) is a nonconstant real-analytic function on \(J\). Its image contains a nondegenerate compact interval after shrinking \(J\) if necessary:

\[
\boxed{I_\chi\subset(0,\infty).}
\]

For every \(\chi\in I_\chi\), there is a 3-gap limit vector in \(\mathcal L_3\) whose prime-flute cross-ratios converge to \(\chi\).

Therefore, by the strictly increasing map \(L(\chi)=4\operatorname{arsinh}\sqrt\chi\), there is a nondegenerate interval

\[
\boxed{I_L\Subset(0,\infty)}
\]

such that every \(L\in I_L\) is an accumulation point of lengths of the explicit primitive simple separating geodesics \(\gamma_n\) of the prime-flute.

Equivalently,

\[
\boxed{
I_L\subset
\overline{\{\ell(\gamma_n):n\ge1\}}.
}
\]

The primitive separating lengths are therefore dense in a genuine positive-length interval.

## 4. Stronger trace/zeta obstruction away from zero

PF-020/PF-035/PF-036 established severe failures caused by primitive lengths accumulating at zero and by their iterates. PF-069 shows that this is **not merely a short-orbit pathology**.

Let \(J_0\Subset I_L\) be any nonempty open subinterval. Since every point of \(I_L\) is an accumulation point, \(J_0\) contains infinitely many distinct primitive simple separating geodesics of the family above.

For \(L\in J_0\), the primitive \(k=1\) Selberg weight

\[
W(L)=\frac{L}{2\sinh(L/2)}
\]

is bounded below by a positive constant depending only on \(J_0\). Consequently

\[
\boxed{
\sum_{\substack{\gamma\ \mathrm{primitive}\\ \ell(\gamma)\in J_0}}
\frac{\ell(\gamma)}{2\sinh(\ell(\gamma)/2)}
=+\infty.
}
\]

Thus the **primitive-only** Selberg orbital measure already has infinite mass on every open subinterval of \(I_L\), without using iterates and without using any geodesic whose length tends to zero.

Likewise, even after deleting all primitive geodesics shorter than any fixed cutoff \(\delta<\inf I_L\), an ordinary Selberg/Ruelle Euler product still cannot regain a conventional half-plane of convergence from the remaining primitive family: infinitely many factors have lengths confined to the compact interval \(I_L\), so the corresponding factors do not approach \(1\).

Therefore a renormalization which merely subtracts/factors the \(L\to0\) sector cannot restore the standard trace/zeta architecture.

## 5. Relation to the distinguished cuffs

The BFM vectors consist of prime-gap fluctuations at the natural \(\log p\) scale. The distinguished cuffs satisfy

\[
\ell_n
=2\log\frac{4p_n}{g_n}+o(1)
\]

along such subsequences. Thus the three normalized gaps, equivalently the relative fluctuations of three neighboring cuffs after removal of their common \(2\log p\) growth, feed the exact Möbius-invariant cross-ratio

\[
\chi=\frac{Y(X+Y+Z)}{XZ},
\]

which then gives the primitive geodesic length \(4\operatorname{arsinh}\sqrt\chi\).

This is a genuinely multi-gap effect; it does not contradict the earlier negative results showing that a single cuff is spectrally universal locally.

## 6. Novelty / prior-art check

Known ingredients:

1. Hildebrand–Maier (Proc. AMS 104 (1988)) prove that the limit set of \(m\) consecutive normalized prime gaps has positive \(m\)-dimensional Lebesgue measure in large cubes.
2. Banks–Freiberg–Maynard (Proc. LMS 113 (2016), Theorem 1.3) prove the stronger finite hitting statement used above.
3. Infinite-type hyperbolic surfaces can certainly have non-discrete length spectrum. Fanoni–Fisac (arXiv:2602.19670, 2026) explicitly contrast this with the discrete-length-spectrum regime and note easy constructions of non-discreteness.
4. The relation between cross-ratios/traces and hyperbolic translation lengths is classical.

Directed searches for combinations of `normalized prime gaps + cross-ratio`, `prime gaps + hyperbolic length spectrum`, and `primitive length spectrum + prime gaps` did not locate this composition. No novelty is claimed for any ingredient separately.

The substantive new point for the present program is the composition

\[
\boxed{
\text{BFM 3-gap limit geometry}
\to
\text{exact prime-flute cross-ratio}
\to
\text{a whole positive interval in the closure of primitive simple lengths}.
}
\]

This is much stronger than merely restating prime-gap statistics: the scalar map is forced by the exact orthogonal-circle/Fuchsian geometry, and the consequence is an intrinsic geometric obstruction to trace/zeta local finiteness.

## 7. Research consequence

Do not spend further effort on a global Selberg/Ruelle/trace construction whose only proposed cure is to renormalize the primitive orbits accumulating at \(0\). Even after that sector is removed, the prime-flute has a positive compact length interval with infinitely dense primitive separating lengths and infinite primitive orbital mass in every subwindow.

Any viable global object must therefore renormalize a **continuum-like positive-length accumulation sector** as well, or abandon global orbit summation in favor of spatially localized/tangent observables.
