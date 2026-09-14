# NB-117 — finite high-zero target rescue is exactly a weighted power-sum interpolation problem

**Status:** `EXACT-DERIVED + FINITE-CELL-NORMAL-FORM + TARGET-EXACT + ZERO-POWER-SUM-INTERPOLATION + NB-115-REPRESENTATION-SHARPENING + NB-116-INVERSE-HEIGHT-COROLLARY + REPRESENTATION-AUDIT`.

`NB-115` localizes the only surviving finite-section escape for a high packet of right-half zeta zeros: order-one finite target access must flow through target-bearing directions whose integer-cell compression retains very little of their continuum norm. `NB-116` sharpens the required retention scale to `O(1/G+1/R)` for every finite packet supported above height `G`. The remaining object is still spectral, however: it is phrased through a pseudoinverse and low-retention modes of the compression Gram.

There is an exact scalar normal form for that obstruction. For every continuum packet vector `f`, define its target-tail primitive on the natural grid by

\[
P_f(n):=
\left\langle
f,
e\,\mathbf 1_{[\log n,\infty)}
\right\rangle,
\qquad
e(t)=e^{-t/2}.
\tag{1}
\]

Then the entire finite integer-cell target problem at cutoff `R` is encoded by the weighted first differences of `P_f`:

\[
\boxed{
\|Q_Rf\|^2
=
\sum_{n<R}n(n+1)|P_f(n)-P_f(n+1)|^2,
}
\tag{2}
\]

and

\[
\boxed{
\langle Q_Rf,e_R\rangle
=P_f(1)-P_f(R),
\qquad
\|e_R\|^2=1-\frac1R.
}
\tag{3}
\]

Consequently, if `K_F` is the Burnol model space of a finite right-half zero packet and

\[
\chi_{F,R}
:=
\frac{\|P_{Q_RK_F}e_R\|^2}{\|e_R\|^2},
\tag{4}
\]

then

\[
\boxed{
\chi_{F,R}
=
\sup_{\substack{f\in K_F\\Q_Rf\ne0}}
\frac{|P_f(1)-P_f(R)|^2}
{(1-1/R)
 \sum_{n<R}n(n+1)|P_f(n)-P_f(n+1)|^2}.
}
\tag{5}
\]

The quotient in `(5)` has an exact Pythagorean interpretation. Put

\[
L_R:=1-\frac1R,
\qquad
A_f:=P_f(1)-P_f(R),
\tag{6}
\]

and let `H_f` be the unique affine function of `1/n` matching the two endpoint values:

\[
H_f(n)
:=
P_f(R)
+
\frac{A_f}{L_R}
\left(\frac1n-\frac1R\right),
\qquad 1\le n\le R.
\tag{7}
\]

Then

\[
\boxed{
\sum_{n<R}n(n+1)|\Delta P_f(n)|^2
=
\frac{|A_f|^2}{L_R}
+
\sum_{n<R}n(n+1)|\Delta(P_f-H_f)(n)|^2.
}
\tag{8}
\]

Hence a finite packet captures a fraction `c>0` of the visible target **if and only if** its model space contains a vector whose target-tail primitive approximates the harmonic profile `C+D/n` in the weighted first-difference metric at the quantitative level

\[
\boxed{
\sum_{n<R}n(n+1)|\Delta(P_f-H_f)(n)|^2
\le
\left(\frac1c-1\right)
\frac{|A_f|^2}{L_R}.
}
\tag{9}
\]

For a packet of distinct simple zeros, this primitive is not an arbitrary sequence. Up to an invertible rescaling of coefficients it is exactly a finite zero-power sum

\[
\boxed{
P_f(n)=
\sum_{\rho\in F} c_\rho n^{-\overline\rho}.
}
\tag{10}
\]

If a zero has multiplicity `m`, the corresponding block is the confluent span of

\[
n^{-\overline\rho}(\log n)^k,
\qquad 0\le k<m.
\tag{11}
\]

Thus the target-bearing near-kernel left by `NB-115`--`NB-116` is equivalent to a concrete source question: **can a finite combination of actual off-critical zero powers approximate an affine `1/n` profile on the natural grid with `O(1)` weighted Dirichlet energy while its continuum model-space norm is larger by the inverse-height factor?**

When every zero in `F` has `|Im rho|>=G`, `NB-116` gives `tau(F)=O(1/G)`. Equations `(5)` and the continuum target/tail bounds then imply that any witness to `chi_(F,R)>=c` satisfies

\[
\boxed{
\frac{\|Q_Rf\|^2}{\|f\|^2}
\ll_c
\frac1G+\frac1R.
}
\tag{12}
\]

In the regime `R/G -> infinity`, one may normalize `A_f=1`; then `(8)`--`(9)` give `||Q_Rf||^2=O_c(1)` while `(12)` forces `||f||^2=Omega_c(G)`. The inverse-height near-kernel is therefore not merely a spectral label. It is a **zero-power extrapolation cost**: an `O(1)` discrete harmonic-profile fit must be represented by a continuum exponential polynomial whose norm is of order at least `G`.

## 1. The natural cells turn the target into a discrete Dirichlet energy

Retain the Paley--Wiener realization and cell projection of `NB-115`. For `n>=1` put

\[
\phi_n(t)=e^{-t/2}\mathbf1_{[\log n,\log(n+1))}(t).
\tag{13}
\]

Since

\[
\|\phi_n\|^2
=\int_{\log n}^{\log(n+1)}e^{-t}\,dt
=\frac1{n(n+1)},
\tag{14}
\]

the normalized cell vectors

\[
\psi_n:=\sqrt{n(n+1)}\,\phi_n
\tag{15}
\]

are orthonormal. The visible cell space is

\[
\mathcal E_R
=\operatorname{span}\{\psi_n:1\le n<R\},
\qquad
Q_R=P_{\mathcal E_R}.
\tag{16}
\]

The target is exactly cell-constant in this basis:

\[
e_R=Q_Re
=\sum_{n<R}\frac1{\sqrt{n(n+1)}}\psi_n,
\tag{17}
\]

which immediately gives `||e_R||^2=L_R`.

By definition `(1)`,

\[
P_f(n)-P_f(n+1)
=
\langle f,\phi_n\rangle.
\tag{18}
\]

Therefore

\[
\langle f,\psi_n\rangle
=\sqrt{n(n+1)}\,
  \bigl(P_f(n)-P_f(n+1)\bigr).
\tag{19}
\]

Parseval on the finite orthonormal cell family proves `(2)`. Since `e_R` is itself in `mathcal E_R`,

\[
\langle Q_Rf,e_R\rangle
=
\langle f,e_R\rangle
=P_f(1)-P_f(R),
\tag{20}
\]

which proves `(3)`.

The endpoint `P_f(R)` is load-bearing. Replacing `(20)` by the continuum target coordinate `P_f(1)` would erase precisely the truncation term `R^(-1/2)` that appears in `NB-115`. The finite target sees a **difference of tail primitives**, not the continuum endpoint alone.

Finally, for any closed finite-dimensional packet space `K_F`, the usual one-vector projection formula gives

\[
\|P_{Q_RK_F}e_R\|^2
=
\sup_{\substack{f\in K_F\\Q_Rf\ne0}}
\frac{|\langle e_R,Q_Rf\rangle|^2}
     {\|Q_Rf\|^2}.
\tag{21}
\]

Combining `(2)`, `(3)`, and `(21)` proves `(5)` without choosing packet coordinates, diagonalizing a Gram matrix, or assuming that `Q_R|_(K_F)` is injective.

## 2. The target direction is the unique harmonic-energy minimizer

Fix `f` and abbreviate `P=P_f`, `A=A_f`. The comparison sequence `(7)` has the same endpoints as `P` and satisfies

\[
H_f(n)-H_f(n+1)
=
\frac{A}{L_R}\frac1{n(n+1)}.
\tag{22}
\]

Set

\[
r_f(n):=P_f(n)-H_f(n).
\tag{23}
\]

Then `r_f(1)=r_f(R)=0`. The cross term in the weighted energy vanishes exactly:

\[
\begin{aligned}
&\sum_{n<R}
 n(n+1)
 \bigl(H_f(n)-H_f(n+1)\bigr)
 \overline{\bigl(r_f(n)-r_f(n+1)\bigr)}\\
&\qquad=
\frac{A}{L_R}
\sum_{n<R}
\overline{\bigl(r_f(n)-r_f(n+1)\bigr)}
=0.
\end{aligned}
\tag{24}
\]

Moreover

\[
\sum_{n<R}n(n+1)|\Delta H_f(n)|^2
=
\frac{|A|^2}{L_R^2}
\sum_{n<R}\frac1{n(n+1)}
=
\frac{|A|^2}{L_R}.
\tag{25}
\]

This proves `(8)`. In particular the finite weighted Hardy inequality

\[
\boxed{
|P_f(1)-P_f(R)|^2
\le
L_R
\sum_{n<R}n(n+1)|\Delta P_f(n)|^2
}
\tag{26}
\]

is sharp, and equality occurs exactly when `P_f-H_f` is constant on `1,...,R`; because the endpoints agree, that constant is zero. Equivalently,

\[
\boxed{
P_f(n)
=
P_f(R)
+
\frac{P_f(1)-P_f(R)}{L_R}
\left(\frac1n-\frac1R\right)
}
\tag{27}
\]

throughout the visible grid.

For `A ne 0`, the squared cosine of the compressed vector `Q_Rf` with the visible target is therefore

\[
\boxed{
q_R(f)
:=
\frac{|\langle Q_Rf,e_R\rangle|^2}
{\|Q_Rf\|^2\|e_R\|^2}
=
\frac1{1+
L_R\,\mathcal E_R(r_f)/|A|^2},
}
\tag{28}
\]

where

\[
\mathcal E_R(r)
:=
\sum_{n<R}n(n+1)|\Delta r(n)|^2.
\tag{29}
\]

Equations `(5)` and `(28)` prove `(9)`. This is an exact target-aware normal form: the near-kernel escape is not characterized by a generic small eigenvalue but by the ability of the source class to approximate the unique weighted-energy minimizer with the correct two endpoint values.

## 3. A finite zero packet makes the primitive a confluent power sum

Let

\[
\rho=\beta+i\gamma,
\qquad
\lambda=\rho-\frac12,
\qquad
\Re\lambda>0.
\tag{30}
\]

For a finite Blaschke product with distinct zeros `lambda_j`, its half-plane model space is spanned by the reproducing kernels at those zeros. Under the Paley--Wiener unitary this is, up to harmless nonzero normalizations and conjugation convention, the exponential span

\[
t\longmapsto e^{-\overline\lambda_jt}.
\tag{31}
\]

Hence for

\[
f(t)=\sum_j a_j e^{-\overline\lambda_jt},
\tag{32}
\]

the primitive `(1)` is

\[
P_f(n)
=
\sum_j
\frac{a_j}{\overline\rho_j}
 n^{-\overline\rho_j}.
\tag{33}
\]

Absorbing the nonzero factors `1/overline(rho_j)` into the coefficients proves `(10)`.

If `rho` has multiplicity `m`, the corresponding model-space block is generated by

\[
t^k e^{-\overline\lambda t},
\qquad 0\le k<m.
\tag{34}
\]

Integrating `(34)` against `e^(-t/2)` from `log n` to infinity gives `n^(-overline rho)` times a polynomial in `log n` of degree `k`, with nonzero triangular leading coefficient. Therefore an invertible triangular coefficient change identifies the primitive block exactly with `(11)`.

This representation is basis-independent. Reordering the zeros, using the canonical deflated/Takenaka--Malmquist basis, or applying any invertible packet-coordinate change leaves the set of primitive sequences and the quotient `(5)` unchanged. The raw Cauchy conditioning and the canonical shear studied in `NB-096`--`NB-102` are therefore nuisance coordinates for this particular target question; they matter only insofar as they permit or obstruct the power-sum interpolation itself.

## 4. Selberg-weighted Burnol mass becomes a continuum-norm cost

The source-specific information from `NB-116` enters through the continuum target coordinate. Since

\[
P_f(1)=\langle f,e\rangle,
\tag{35}
\]

Burnol's model-space target identity gives, for every `f in K_F`,

\[
|P_f(1)|
\le
\sqrt{\tau(F)}\,\|f\|.
\tag{36}
\]

The far endpoint is bounded by the ordinary target tail:

\[
|P_f(R)|
\le
\left\|e\,\mathbf1_{[\log R,\infty)}\right\|
\|f\|
=
R^{-1/2}\|f\|.
\tag{37}
\]

Thus

\[
\boxed{
|A_f|
\le
\bigl(\sqrt{\tau(F)}+R^{-1/2}\bigr)\|f\|.
}
\tag{38}
\]

If `q_R(f)>=c`, equation `(28)` implies

\[
\|Q_Rf\|^2
=\mathcal E_R(P_f)
\le
\frac{|A_f|^2}{cL_R}.
\tag{39}
\]

Combining `(38)` and `(39)` yields

\[
\boxed{
\frac{\|Q_Rf\|^2}{\|f\|^2}
\le
\frac{(\sqrt{\tau(F)}+R^{-1/2})^2}
     {c(1-1/R)}.
}
\tag{40}
\]

This is the one-vector Rayleigh version of the target-weighted spectral localization in `NB-115`. It is not a replacement for `NB-115`'s stronger statement that at least half of the entire finite target projection flows through the low-retention eigenspace. Its advantage is different: the witness has now been converted exactly into the scalar source class `(10)`--`(11)`.

For an actual right-half packet supported above height `G`, `NB-116` gives

\[
\tau(F)\ll\frac1G.
\tag{41}
\]

Equations `(40)` and `(41)` prove `(12)`. If `R/G -> infinity` and the packet has `chi_(F,R)>=c`, choose an optimizer of `(5)` and rescale it so that `A_f=1`. Then `(39)` gives

\[
\|Q_Rf\|^2\le\frac1{cL_R}=O_c(1),
\tag{42}
\]

while `(38)` gives

\[
\boxed{
\|f\|^2
\gg_c G.
}
\tag{43}
\]

The finite rescue therefore requires a sequence in the actual zero-power span with bounded discrete Dirichlet energy but a continuum model-space realization whose norm diverges at least linearly with the zero height. This is the same inverse-height compression scale seen by `NB-116`, now expressed as an explicit extrapolation/interpolation cost rather than an anonymous small eigenvalue.

## 5. Representation audit and matched controls

The transformation `f -> P_f` does not create a new arithmetic source. It is an injective-enough observation only for the target question at hand: `(2)`--`(5)` recover exactly the compressed norm and target pairing needed to compute `chi_(F,R)`, but they do not reconstruct the full continuum packet Gram or all pairwise geometry. That information loss is deliberate because `NB-115` has already isolated target access as the relevant observable.

The universal matched control is the target itself. For `f=e`,

\[
P_e(n)=\frac1n,
\tag{44}
\]

so `H_e=P_e`, the residual energy in `(8)` is zero, and `Q_Re=e_R`. Thus the harmonic profile is not an artifact of the proof: it is exactly the sequence whose cell differences encode the target direction. The weighted inequality `(26)` is merely Cauchy--Schwarz in target coordinates; no novelty is claimed for it as an abstract inequality.

Conversely, a generic Hilbert space can realize perfect finite target access through an arbitrarily small compression Rayleigh quotient, as the matched control in `NB-115` already shows. The present result does not contradict that example. It identifies what such a control must look like **inside the Nyman cell geometry**: its tail primitive must follow `(27)`. The additional arithmetic restriction is then precisely that, for the Burnol packet, the primitive belongs to the confluent zero-power span `(10)`--`(11)`.

The endpoint term is another falsification control. If `P_f(R)` is dropped, one gets an incorrect infinite-horizon interpolation problem and loses the `1/R` branch in `(40)`. If multiplicity is treated as duplicate copies of `n^(-rho)` rather than the confluent logarithmic block `(11)`, the source dimension is also miscounted. Both corrections are forced by the exact Paley--Wiener realization.

Finally, the normal form does **not** prove that the interpolation is impossible. A sufficiently large abstract power-sum family may fit many finite grid constraints, and growing packets can be badly conditioned. The theorem says that any successful rescue has to solve this exact weighted interpolation problem while simultaneously paying the continuum norm cost `(43)`. A future exclusion needs a lower bound for that source-specific extrapolation cost stronger than the `Omega(G)` threshold supplied by Burnol/Selberg, or a proof that actual zeta zero powers cannot achieve the required harmonic-profile energy.

## 6. Prior-art boundary and new theorem target

Finite Blaschke/model spaces, their exponential Paley--Wiener realizations, and Burnol's target projection formula are classical and already anchored in `SOURCES.md`. The weighted inequality `(26)` and the Pythagorean decomposition `(8)` are elementary discrete Hilbert geometry. No novelty is claimed for those ingredients separately.

A targeted search across Nyman--Beurling finite sections, Blaschke/model-space formulations, Müntz/power-sum approximations, discrete Sobolev energies, and recent Gram-spectral work did not identify the specific reduction `(5)`--`(11)` of the `NB-115` integer-cell compression escape to a two-endpoint weighted interpolation problem for actual zero powers. The line-local contribution is therefore the exact splice: the natural-cell target geometry converts the spectral near-kernel into a scalar zero-power interpolation certificate, and `NB-116` converts its continuum cost into the inverse-height requirement `(43)`. No new external theorem is load-bearing, so `SOURCES.md` requires no change.

The live question is now more concrete than "control the target weight of the near-kernel." For packets above height `G`, prove or disprove a source-specific inequality showing that every confluent actual-zero power sum satisfying the endpoint normalization and the harmonic-profile bound `(9)` must have

\[
\frac{\mathcal E_R(P_f)}{\|f\|^2}
\gg
\frac1G
\tag{45}
\]

by a factor tending to infinity in a useful joint regime. Such an estimate would contradict `(12)` and close the remaining high-zero finite-section rescue. Failure should be exhibited by an explicit admissible zero-power family, not by a generic Gram near-kernel.