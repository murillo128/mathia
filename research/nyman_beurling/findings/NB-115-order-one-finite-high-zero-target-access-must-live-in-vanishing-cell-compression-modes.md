# NB-115 — order-one finite high-zero target access must live in vanishing cell-compression modes

**Status:** `EXACT-DERIVED + FINITE-BLASCHKE-PACKET + TARGET-AWARE-CELL-COMPRESSION + PSEUDOINVERSE-SPECTRAL-LOCALIZATION + ACTUAL-ZETA-SHELL-COROLLARY + NEGATIVE/METHOD-BOUNDARY`.

`NB-114` closes the classical continuum escape for a high packet of off-critical zeros: if every selected zero has ordinate at least `G`, then its Burnol/model-space target mass is at most `d/G^2`, and an entire fixed-ratio shell of actual zeta zeros has target mass tending to zero. What remained genuinely open was the finite arithmetic escape. The integer-cell window used throughout this line is not the continuum model space itself; it compresses continuum zero states by cell averaging, and a badly conditioned compression could in principle rotate a classically target-poor packet into a target-bearing finite state.

That possibility can now be localized exactly. Let the finite arithmetic window be the orthogonal integer-cell projection of a finite Burnol packet. If the compressed packet captures an order-one fraction of the visible Nyman target while its continuum Burnol target mass is small, then **an order-one fraction of that finite target capture must be carried by packet directions whose cell-retained energy is comparably small**. In particular, for a high packet of `d` zeros above height `G`, order-one finite target access forces target-bearing cell-compression eigenvalues of size

\[
O\!\left(\frac d{G^2}+\frac1R\right),
\]

where `R` is the natural-index cutoff. For all actual right-half zeros in a fixed-ratio ordinate shell, zero counting turns this into

\[
O_A\!\left(\frac{\log G}{G}+\frac1R\right).
\]

Thus the finite escape left by `NB-114` is no longer an unspecified "arithmetic truncation defect": it must be a **target-weighted near-kernel of the integer-cell compression**. A perturbative transfer from the continuum packet cannot create order-one target access.

## 1. Canonical cell compression of a finite Burnol packet

Work in the Paley--Wiener time realization

\[
\mathcal H=L^2(0,\infty),
\qquad
e(t)=e^{-t/2},
\qquad
\|e\|^2=1.
\tag{1}
\]

For an integer `R>=2`, put

\[
\phi_n(t)=e^{-t/2}\mathbf 1_{[\log n,\log(n+1))}(t),
\qquad
\mathcal E_R=\operatorname{span}\{\phi_n:1\le n<R\},
\tag{2}
\]

and let `Q_R=P_(\mathcal E_R)` be the orthogonal cell projection. Since the cells partition `[0,\log R)`, the target itself is exactly represented on every visible cell:

\[
\boxed{
 e_R:=Q_Re
 =e^{-t/2}\mathbf 1_{[0,\log R)}(t),
 \qquad
 \|e_R\|^2=1-\frac1R,
 \qquad
 \|e-e_R\|^2=\frac1R.
}
\tag{3}
\]

Let `F` be any finite multiset of right-half off-critical zeros, with multiplicity included, and let `K_F` be the corresponding finite Burnol model space under the same Paley--Wiener unitary. Thus

\[
\dim K_F=d:=|F|,
\qquad
\tau(F):=\|P_{K_F}e\|^2=1-|B_F(1)|^2.
\tag{4}
\]

The identity in `(4)` is the classical Burnol target-mass formula already anchored in `SOURCES.md` and used in `NB-114`.

Choose an orthonormal basis `k_1,\ldots,k_d` of `K_F` and let

\[
A:\mathbb C^d\to\mathcal H,
\qquad
Ac=\sum_{j=1}^dc_jk_j.
\tag{5}
\]

The finite cell-compression Gram is

\[
\boxed{
H_{F,R}:=A^*Q_RA
=\bigl(\langle Q_Rk_i,Q_Rk_j\rangle\bigr)_{i,j=1}^d,
\qquad
0\preceq H_{F,R}\preceq I.
}
\tag{6}
\]

Its eigenvalues are exactly the squared singular values of `Q_R|_(K_F)`: an eigenvalue `lambda` is the fraction of continuum packet energy retained by the arithmetic cell window in that packet direction.

Put

\[
\mathcal S_{F,R}:=Q_RK_F\subset\mathcal E_R,
\qquad
b_{F,R}:=A^*e_R.
\tag{7}
\]

The state spaces in `NB-093`--`NB-108` are precisely this construction in source-adapted coordinates. For one zero, the Riesz state is the cell projection of the elementary exponential model state; confluence gives its projected derivative/Jordan span (`NB-108`), and a fixed distinct packet differs from the raw zero states by an invertible triangular state transformation (`NB-095`). The choice of orthonormal coordinates in `(5)` therefore removes basis conditioning without changing the finite state span.

## 2. Exact pseudoinverse formula for finite target access

Because `e_R` lies in `ran Q_R`,

\[
\langle e_R,Q_RAc\rangle
=\langle e_R,Ac\rangle
=\langle b_{F,R},c\rangle.
\tag{8}
\]

The orthogonal projector onto `ran(Q_RA)=\mathcal S_(F,R)` is the standard finite-rank pseudoinverse projector. Hence

\[
\boxed{
\|P_{\mathcal S_{F,R}}e_R\|^2
=b_{F,R}^*H_{F,R}^{+}b_{F,R}.
}
\tag{9}
\]

This remains exact if the cell compression loses rank. Indeed `ker H_(F,R)=ker(Q_RA)`, and `(8)` shows that `b_(F,R)` is orthogonal to that kernel, so the Moore--Penrose inverse introduces no spurious component.

The numerator vector is still controlled by the **continuum** Burnol mass. Since `A` is an isometry onto `K_F`,

\[
\|b_{F,R}\|
=\|P_{K_F}e_R\|
\le
\|P_{K_F}e\|+\|P_{K_F}(e-e_R)\|.
\tag{10}
\]

Using `(3)` and `(4)`,

\[
\boxed{
\|b_{F,R}\|
\le
\sqrt{\tau(F)}+R^{-1/2}.
}
\tag{11}
\]

Equations `(9)` and `(11)` isolate the only possible finite amplification mechanism. The continuum target coordinates have total Euclidean mass at most `sqrt(tau(F))+R^(-1/2)`; the finite section can turn them into order-one target projection only by dividing some of them by small cell-retention eigenvalues of `H_(F,R)`.

## 3. Order-one target capture is spectrally concentrated in low-retention modes

Diagonalize

\[
H_{F,R}u_j=\lambda_ju_j,
\qquad
0\le\lambda_j\le1,
\tag{12}
\]

and write

\[
\widetilde b_j=\langle u_j,b_{F,R}\rangle.
\]

Then `(9)` is the exact spectral identity

\[
\boxed{
\|P_{\mathcal S_{F,R}}e_R\|^2
=
\sum_{\lambda_j>0}
\frac{|\widetilde b_j|^2}{\lambda_j}.
}
\tag{13}
\]

Suppose the finite packet captures a fixed fraction `c in (0,1]` of the visible target,

\[
\chi_{F,R}
:=
\frac{\|P_{\mathcal S_{F,R}}e_R\|^2}{\|e_R\|^2}
\ge c.
\tag{14}
\]

Define

\[
\boxed{
\Lambda_{F,R}(c)
:=
\frac{2\bigl(\sqrt{\tau(F)}+R^{-1/2}\bigr)^2}
{c(1-1/R)}.
}
\tag{15}
\]

The contribution to `(13)` from eigenvalues larger than `Lambda_(F,R)(c)` is at most

\[
\sum_{\lambda_j>\Lambda_{F,R}(c)}
\frac{|\widetilde b_j|^2}{\lambda_j}
\le
\frac{\|b_{F,R}\|^2}{\Lambda_{F,R}(c)}
\le
\frac c2\left(1-\frac1R\right).
\tag{16}
\]

By `(14)`, the right side is at most half of the total finite target projection. Therefore

\[
\boxed{
\sum_{0<\lambda_j\le\Lambda_{F,R}(c)}
\frac{|\widetilde b_j|^2}{\lambda_j}
\ge
\frac12\,
\|P_{\mathcal S_{F,R}}e_R\|^2.
}
\tag{17}
\]

This is stronger than merely asserting that the compressed Gram has some small eigenvalue. **At least half of the target projection itself must flow through the low-retention spectral sector.** An irrelevant near-kernel elsewhere in the packet cannot satisfy `(17)`.

A simpler necessary consequence is that whenever `(14)` holds and the target projection is nonzero, there is a target-bearing eigenmode with

\[
\boxed{
0<\lambda_j\le\Lambda_{F,R}(c).
}
\tag{18}
\]

Thus a finite arithmetic window cannot perturbatively convert a continuum target-poor packet into an order-one target-bearing packet. The relevant comparison map must become singular on target-carrying directions.

## 4. High-zero packets force vanishing retention scales

Now use the source-specific target bound of `NB-114`. If every `rho in F` satisfies

\[
|\Im\rho|\ge G,
\tag{19}
\]

then

\[
\tau(F)\le\frac d{G^2}.
\tag{20}
\]

Since `(x+y)^2<=2x^2+2y^2`, `(15)` gives

\[
\boxed{
\Lambda_{F,R}(c)
\le
\frac{4}{c(1-1/R)}
\left(
\frac d{G^2}+\frac1R
\right).
}
\tag{21}
\]

Consequently, if `d/G^2 -> 0` and `R -> infinity`, any order-one finite target capture by the high packet must have at least half of its target projection carried by cell-compression modes with retained-energy fraction `o(1)`.

For an actual zeta packet consisting of all selected right-half zeros with positive ordinates in a fixed-ratio shell

\[
G\le\Im\rho\le AG,
\qquad A>1\text{ fixed},
\tag{22}
\]

Bellotti--Wong zero counting, already load-bearing in `NB-112` and `NB-114`, gives

\[
d=O_A(G\log G).
\tag{23}
\]

Therefore an order-one finite target fraction forces the target-weighted compression scale

\[
\boxed{
\lambda_j
=
O_{A,c}\!\left(
\frac{\log G}{G}+\frac1R
\right)
}
\tag{24}
\]

for modes carrying at least half of the finite target projection in the sense of `(17)`. Along any joint limit `G,R->infinity`, those modes retain a vanishing fraction of their continuum packet norm.

This sharply separates the four currencies already isolated in the line. Actual zero **rank supply** gives only `O(G log G)` states in the shell; continuum Burnol **target mass** is `O(log G/G)`; the finite arithmetic window can recover order-one **target access** only by paying a matching collapse in its cell-compression spectrum. Large raw or normalized zero-state **conditioning/shear** remains a different quantity and does not by itself establish `(17)`.

## 5. Matched control: the compression scale is genuinely necessary

The scale in the theorem cannot be removed by abstract Hilbert geometry. Take

\[
\mathcal H=\operatorname{span}\{e,f\},
\qquad
\langle e,f\rangle=0,
\qquad
\|e\|=\|f\|=1,
\]

and let

\[
k=\sqrt\tau\,e+\sqrt{1-\tau}\,f,
\qquad
K=\operatorname{span}\{k\}.
\tag{25}
\]

Then the continuum target mass is exactly

\[
\|P_Ke\|^2=\tau.
\]

Let `Q` be orthogonal projection onto `span{e}`. The visible target is unchanged, `Qe=e`, while

\[
Qk=\sqrt\tau\,e.
\]

Hence the compressed packet is exactly the target line,

\[
\|P_{QK}e\|^2=1,
\tag{26}
\]

but its sole retention eigenvalue is

\[
\lambda=\|Qk\|^2=\tau.
\tag{27}
\]

Thus an arbitrarily target-poor continuum packet can become perfectly target-bearing after orthogonal compression, and it does so precisely by the near-kernel mechanism isolated above. Any stronger conclusion for the Nyman cell projection must use arithmetic structure of `Q_R` and the actual zeta packet; no universal Hilbert-space argument can rule the escape out.

## 6. Prior-art boundary and the new theorem frontier

The ingredients around the theorem are classical. Burnol supplies the model-space target identity `(4)`. Orthogonal compression, Moore--Penrose projection formulas, and the spectral expansion `(13)` are standard Hilbert/linear-algebra facts. Ziad's 2026 preprint is the closest contemporary Nyman-specific boundary: it explicitly separates a rigid finite Blaschke component from an arithmetic Gram projection defect and uses spectral whitening. Yang's 2026 paper establishes a separate Friedrichs-angle viewpoint for Nyman--Beurling subspaces. No novelty is claimed for Blaschke model spaces, pseudoinverses, principal angles, or generalized Gram spectra themselves.

A targeted audit of recent Nyman--Beurling finite-section, Blaschke/model-space, Gram-spectral, cell-averaging, and subspace-angle literature did not locate the source-specific implication `(17)`--`(24)`: combining the Burnol high-zero target mass with the **actual integer-cell compression** to prove that any surviving finite target access is target-weighted into vanishing retention modes. The appropriate novelty classification is therefore line-local `EXACT-DERIVED`; no claim of broad literature novelty is needed. No new external theorem is load-bearing beyond the Burnol, Bellotti--Wong, Ziad, and Yang boundaries already anchored in `SOURCES.md`, so that file requires no change.

The finding also has strict boundaries. It does **not** lower-bound the retention spectrum of `H_(F,R)`, exclude the near-kernel sector, or prove a Nyman distance estimate. It applies to the canonical orthogonal integer-cell compression; a different nonorthogonal truncation requires its own transfer law. It also does not identify raw zero-state shear with retention collapse: `NB-098`--`NB-099` already show those can behave differently.

The new live theorem target is correspondingly precise. To eliminate the multi-zero escape left after `NB-114`, it is enough to prove either that actual high-zero packets cannot develop the vanishing cell-retention sector required by `(24)`, or more weakly that the finite target coordinates have negligible spectral weight on that sector. Conversely, any proposed finite-section rescue must exhibit this near-kernel explicitly; order-one target access with a uniformly well-retained continuum packet is now ruled out exactly.
