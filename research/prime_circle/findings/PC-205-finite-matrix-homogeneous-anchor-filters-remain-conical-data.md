# PC-205 — finite matrix homogeneous anchor filters remain conical data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for obtaining a new Prime-Circle/RH carrier by replacing the scalar homogeneous anchor filter of PC-204 with any fixed finite-dimensional operator-valued rotation-invariant filter whose Fourier multiplier depends on one homogeneous mismatch scale.

PC-204 left matrix/operator-valued anchor propagation outside its scalar theorem. A natural repair is therefore to let the common anchor carry a finite internal state and to use a matrix-valued Fourier multiplier, potentially with noncommuting positive- and negative-frequency channels, before taking any scalar spectral observable.

That finite-state repair still does not retain a new arithmetic degree of freedom under the same source-forced homogeneous scaling. After angular contraction and Mellin transform in the anchor scale, the entire matrix profile collapses to at most two matrix Mellin moments, one for each sign of the Fourier mismatch. The arithmetic coefficients remain exactly the two one-extra-leg rational-cone series already classified by PC-202/PC-204. Matrix entries are therefore finite linear combinations of established conical Dirichlet data, while determinants, traces, characteristic polynomials, and other fixed finite matrix spectralizations are only algebraic wrappers around those scalar cone functions.

The obstruction is not commutativity. The matrix profiles may be fully noncommuting. What fails is finite homogeneous state retention: the mismatch magnitude `|Delta|` survives only through the scalar power `|Delta|^{-alpha w}`, while all internal operator structure is integrated into shell-independent matrix coefficients.

## 1. Source packet and finite internal anchor state

Use the same fixed finite source-native Cauchy–Poisson packets as PC-197--PC-204. For primitive nonprincipal characters `chi_i (mod n_i)` and `psi_j (mod m_j)`, write

\[
\mathcal K_{n_i,\chi_i}(x_i,\theta)
=
2\tau(\overline\chi_i)
\sum_{k_i\ge1}\chi_i(k_i)e^{-k_i x_i}e^{ik_i\theta},
\tag{1}
\]

and similarly for the conjugate packets. Their fixed finite product is

\[
F(\theta)
=
\prod_{i=1}^{r}\mathcal K_{n_i,\chi_i}(x_i,\theta)
\prod_{j=1}^{q}\overline{\mathcal K_{m_j,\psi_j}(y_j,\theta)}.
\tag{2}
\]

After expansion,

\[
F(\theta)
=
C_{\boldsymbol\chi,\boldsymbol\psi}
\sum_{\mathbf k,\boldsymbol\ell\ge1}
 a_{\mathbf k,\boldsymbol\ell}
 e^{i\Delta(\mathbf k,\boldsymbol\ell)\theta},
\tag{3}
\]

where

\[
a_{\mathbf k,\boldsymbol\ell}
=
\left(\prod_i\chi_i(k_i)\right)
\left(\prod_j\overline{\psi_j(\ell_j)}\right)
\exp\!\left(-\sum_i k_i x_i-\sum_j\ell_j y_j\right)
\tag{4}
\]

and

\[
\Delta(\mathbf k,\boldsymbol\ell)
=
\sum_i k_i-\sum_j\ell_j.
\tag{5}
\]

Let `V` be a fixed finite-dimensional complex vector space. Fix `alpha>0` and two matrix profiles

\[
K_\pm:(0,\infty)\longrightarrow \operatorname{End}(V)
\tag{6}
\]

such that the Fourier series and Mellin integrals below converge absolutely in a nonempty common strip. No commutativity is assumed either between `K_+` and `K_-` or among values of either profile at different scales.

Define the centered operator-valued anchor filter

\[
W_u(\theta)
=
\sum_{h\ge1}
\left[
K_+(u h^\alpha)e^{ih\theta}
+
K_-(u h^\alpha)e^{-ih\theta}
\right],
\qquad u>0.
\tag{7}
\]

The zero mode is excluded because it is the ordinary finite Haar fusion already classified by PC-202.

The operator-valued anchored observable is

\[
\mathcal A_u
=
\frac1{2\pi}\int_0^{2\pi}W_u(\theta)F(\theta)\,d\theta
\in\operatorname{End}(V).
\tag{8}
\]

## 2. Angular contraction leaves only the sign and magnitude of the mismatch

Haar orthogonality forces the filter frequency to cancel the packet mismatch. Hence

\[
\boxed{
\begin{aligned}
\mathcal A_u
&=
C_{\boldsymbol\chi,\boldsymbol\psi}
\sum_{\Delta>0}
 a_{\mathbf k,\boldsymbol\ell}
 K_-(u\Delta^\alpha)\\
&\quad+
C_{\boldsymbol\chi,\boldsymbol\psi}
\sum_{\Delta<0}
 a_{\mathbf k,\boldsymbol\ell}
 K_+(u|\Delta|^\alpha).
\end{aligned}}
\tag{9}
\]

Thus allowing a finite internal anchor space has not created a new Fourier conservation law. Relative to PC-204, the only additional information before Mellinization is which matrix profile is attached to each sign chamber.

This already separates the finite-state issue from a genuinely mismatch-indexed operator. In (7), the internal space `V` is fixed independently of `h`; the magnitude of the mismatch is not itself an orthogonal state label.

## 3. Mellinization collapses every matrix profile to one matrix moment per sign

Define the operator-valued Mellin moments

\[
M_\pm(w)
=
\int_0^\infty v^{w-1}K_\pm(v)\,dv
\in\operatorname{End}(V),
\tag{10}
\]

where in finite dimension ordinary entrywise convergence and Bochner convergence are equivalent under the stated absolute-convergence assumptions.

For every positive integer `H`, the change of variable `v=uH^alpha` gives the exact scaling identity

\[
\boxed{
\int_0^\infty u^{w-1}K_\pm(uH^\alpha)\,du
=
H^{-\alpha w}M_\pm(w).
}
\tag{11}
\]

Therefore the Mellin transform of (9) is

\[
\boxed{
\begin{aligned}
\widetilde{\mathcal A}(w)
&=
C_{\boldsymbol\chi,\boldsymbol\psi}
\Bigg[
M_-(w)
\sum_{\Delta>0}
 a_{\mathbf k,\boldsymbol\ell}\Delta^{-\alpha w}\\
&\qquad\qquad+
M_+(w)
\sum_{\Delta<0}
 a_{\mathbf k,\boldsymbol\ell}|\Delta|^{-\alpha w}
\Bigg].
\end{aligned}}
\tag{12}
\]

The complete scale-dependent matrix profiles have disappeared. They survive only as the two shell-independent matrices `M_-(w)` and `M_+(w)`.

Now Mellin-transform the positive packet depths independently. In a common absolute-convergence region,

\[
\boxed{
\begin{aligned}
\mathcal M\mathcal A
&=
C_{\boldsymbol\chi,\boldsymbol\psi}
\prod_i\Gamma(s_i)
\prod_j\Gamma(t_j)\\
&\quad\times
\left[
M_-(w)Z_+(\mathbf s;\mathbf t;\alpha w)
+
M_+(w)Z_-(\mathbf s;\mathbf t;\alpha w)
\right],
\end{aligned}}
\tag{13}
\]

where

\[
Z_+
=
\sum_{\substack{\mathbf k,\boldsymbol\ell\ge1\\\Delta>0}}
\frac{
\prod_i\chi_i(k_i)
\prod_j\overline{\psi_j(\ell_j)}
}{
\prod_i k_i^{s_i}
\prod_j\ell_j^{t_j}
\Delta^{\alpha w}
},
\tag{14}
\]

and `Z_-` is the analogous `Delta<0` sum.

Exactly as in PC-204, introducing `h=|Delta|` turns each sign chamber into a balanced Haar relation with one additional positive conductor-one leg. Hence both `Z_+` and `Z_-` are fixed finite colored rational-cone Dirichlet series in the PC-202 class.

Equation (13) is the finite-matrix closure theorem. Every matrix entry belongs to the two-dimensional module over the scalar conical packet algebra generated by `Z_+` and `Z_-`.

## 4. Noncommutativity does not restore a hidden arithmetic carrier

The result does not assume the matrix moments commute. Suppose, for example,

\[
K_\pm(v)=e^{-v}A_\pm
\tag{15}
\]

with arbitrary fixed matrices `A_+` and `A_-`, possibly satisfying `[A_+,A_-] != 0`. Then

\[
M_\pm(w)=\Gamma(w)A_\pm,
\tag{16}
\]

so

\[
\widetilde{\mathcal A}(w)
=
\Gamma(w)
\left[A_-Z_+(w)+A_+Z_-(w)\right]
\tag{17}
\]

up to the fixed packet gamma/Gauss factors.

A matrix commutator can certainly be nonzero, but its noncommuting part is imported entirely by `A_+` and `A_-`; the arithmetic factors remain scalar members of the already classified cone algebra. More generally, for two Mellin parameters `w_1,w_2`,

\[
[\widetilde{\mathcal A}(w_1),\widetilde{\mathcal A}(w_2)]
=
\sum_{\sigma,\tau\in\{+,-\}}
Z_\sigma(w_1)Z_\tau(w_2)
[M_\sigma(w_1),M_\tau(w_2)]
\tag{18}
\]

up to the same scalar packet factors. Thus any noncommutativity lives in shell-independent profile moments multiplied by classical scalar arithmetic data.

If the filter is sign-even, `K_+=K_-=K`, equation (13) collapses further to

\[
\mathcal M\mathcal A
=
M_K(w)\,[Z_+(w)+Z_-(w)]
\tag{19}
\]

up to the packet factors: every eigenvalue is simply an eigenvalue of the profile moment multiplied by the same scalar conical function.

## 5. Fixed finite spectralization is only an algebraic wrapper

Let `d=dim V`. Because (13) is a linear combination of two scalar functions with matrix coefficients, its characteristic polynomial has the form

\[
\boxed{
\det(\lambda I-\mathcal M\mathcal A)
=
\sum_{a+b\le d}
 c_{a,b}(\lambda,\mathbf s,\mathbf t,w)
 Z_+^a Z_-^b,
}
\tag{20}
\]

where each coefficient `c_{a,b}` depends only on the fixed matrix Mellin moments, packet gamma/Gauss factors, and the spectral parameter, not on an additional Prime-Circle arithmetic state.

The same conclusion holds for traces, fixed finite products, exterior powers, resolvents where defined, and any other fixed finite algebraic matrix functional. Such operations can create new zero sets algebraically, but those zeros depend on the freely chosen matrix profiles and are therefore an arbitrary spectral wrapper around the classical cone packet data unless an independent source principle selects the matrices and proves a new arithmetic implication.

In particular, finite matrix dimension does not create an intrinsic `s <-> 1-s` involution, the completed-zeta gamma factor, a self-adjoint operator whose spectrum is the zeta zero ordinates, or a critical-line selection principle.

## 6. Prior-art and novelty audit

Operator-valued Fourier multipliers on periodic/vector-valued function spaces are established harmonic-analysis machinery; directed searches reached the standard periodic multiplier framework of Arendt--Bu and later toroidal operator-valued pseudodifferential work. Those theories confirm that matrix/operator-valued Fourier symbols on the circle are not a new analytic species.

On the arithmetic side, PC-202 already anchors the relevant classical boundary in Terasoma's rational-cone/cyclotomic multiple-zeta framework and in Guo--Paycha--Zhang's conical-zeta subdivision theory. A directed modern search also found current work packaging cyclotomic conical zeta data through matrices, reinforcing that matrix notation alone is not a novelty boundary.

No external theorem is required for the new implication (9)--(13): it is the elementary homogeneous Mellin scaling rule applied entrywise, followed by the exact PC-202 cone classification. No historical novelty is claimed for operator-valued multipliers, matrix Mellin transforms, conical zeta functions, or finite matrix spectral calculus.

The durable Mathia-specific result is the closure boundary: **a fixed finite-dimensional matrix anchor state does not evade PC-204 when the multiplier remains rotation-invariant, shell-independent, and self-similar in one homogeneous mismatch scale.**

## 7. Scope and surviving frontier

The assumptions carrying the no-go are essential. The internal dimension is fixed and finite; the filter is diagonal in angular Fourier frequency; its magnitude dependence is through one homogeneous combination `u|h|^alpha`; the matrix profiles do not depend on shell incidence or conductor; and the source uses a fixed finite number of packet legs before the matrix observable is formed.

The theorem does **not** classify:

- a mismatch-indexed state space such as an infinite-dimensional channel retaining distinct `h` values;
- matrix dimension growing with refinement level or packet valence;
- shell-dependent symbols derived from old/new incidence, chord blocks, or exact-order projectors;
- non-rotation-invariant operators that genuinely mix different angular Fourier modes;
- nonhomogeneous multi-scale symbols that cannot be separated by the scaling substitution (11);
- infinite-depth/refinement limits whose state space survives before finite scalar contraction;
- indefinite non-scalar positivity or global uniformization/monodromy constructions.

Thus the matrix/operator-valued escape left by PC-204 narrows substantially. **Finite internal matrix packaging is not enough.** A surviving operator construction must retain mismatch or shell relational information in its state space before the homogeneous Mellin quotient, rather than attach an arbitrary finite matrix response to a mismatch that is still summarized only by its sign and magnitude.