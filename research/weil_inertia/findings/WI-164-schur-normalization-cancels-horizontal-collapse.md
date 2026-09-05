# WI-164 — normalized Schur cancellation does not charge Lamzouri horizontal collapse

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`. The operator-level Schur complement suggested after WI-137 is exact, but its natural normalization removes precisely the horizontal conditioning one hoped to charge. If Lamzouri's signed odd synthesis is split relative to `W=V\oplus H` as `K=(K_V,K_H)`, then the horizontal block is negative definite and

\[
\boxed{
A_{VV}-A_{VH}A_{HH}^{-1}A_{HV}=A_+,
}
\]

where `A_+` is the positive retained Gram operator. More importantly,

\[
\boxed{
A_{VH}(-A_{HH})^{-1}A_{HV}=K_VK_V^*,
}
\]

and `A_{VH}(-A_{HH})^{-1/2}` has exactly the same singular values as `K_V`. Thus no inverse power of the collapsing horizontal map `K_H` survives: the normalized cross interaction is only the vertical projection of the odd synthesis in unitary coordinates. An isolated simple off-line conjugate pair gives the decisive control: `K_V=0` identically, hence the whole Schur correction is zero for every nonzero horizontal depth, while the pair remains genuinely off the critical line and its Lamzouri deficit tends to zero under confluence. Therefore the Schur identity by itself cannot supply a positive cost per off-line pair or prevent the WI-140 collapse. Any use of this identity in a defect-to-zero bootstrap must add independent zeta-source information that quantitatively controls `K_V` or another singular invariant.

No unconditional zero proportion changes in this finding.

## 1. Exact source decomposition

Use Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1, Proposition 2.1. For one representative `z_j` from each distinct non-real conjugate pair, with multiplicity `m_j`, Lamzouri writes the signed tensor contribution as

\[
2m_j(g_j\otimes g_j-h_j\otimes h_j).
\]

Let `E` be the `k`-dimensional real coefficient space indexed by these pairs and define the weighted odd synthesis

\[
K e_j:=\sqrt{2m_j}\,h_j.
\tag{1}
\]

Let

\[
A_+
:=\sum_{x\in R}m_x f_x\otimes f_x
  +2\sum_{j=1}^k m_j g_j\otimes g_j.
\tag{2}
\]

Then WI-137's self-adjoint Lamzouri operator is exactly

\[
\boxed{A_F=A_+-KK^*.}
\tag{3}
\]

The range of `A_+` is contained in Lamzouri's retained space `V`. Put `H=W\ominus V` and decompose

\[
K_V:=P_VK:E\to V,
\qquad
K_H:=P_HK:E\to H.
\tag{4}
\]

WI-126/WI-132 establish that the odd residuals are linearly independent modulo `V`; WI-138 identifies `\dim H=k`. Hence `K_H` is a square isomorphism for every finite configuration. In particular `K_HK_H^*` is positive definite on `H`.

Relative to `W=V\oplus H`, equation (3) gives the exact blocks

\[
A_{VV}=A_+-K_VK_V^*,
\quad
A_{VH}=-K_VK_H^*,
\tag{5}
\]

\[
A_{HV}=-K_HK_V^*,
\quad
A_{HH}=-K_HK_H^*.
\tag{6}
\]

Thus `A_{HH}` is negative definite, so its ordinary Schur complement is well defined.

## 2. The Schur complement really does recover the retained positive operator

Since `K_H` is invertible,

\[
A_{HH}^{-1}
=-(K_HK_H^*)^{-1}
=-(K_H^*)^{-1}K_H^{-1}.
\tag{7}
\]

Substituting (5)--(7),

\[
\begin{aligned}
A_{VH}A_{HH}^{-1}A_{HV}
&=(-K_VK_H^*)
  \bigl(-(K_H^*)^{-1}K_H^{-1}\bigr)
  (-K_HK_V^*)\\
&=-K_VK_V^*.
\end{aligned}
\tag{8}
\]

Therefore

\[
\boxed{
A_{VV}-A_{VH}A_{HH}^{-1}A_{HV}=A_+.
}
\tag{9}
\]

Equivalently, with the positive horizontal block `-A_{HH}=K_HK_H^*`,

\[
\boxed{
C:=A_{VH}(-A_{HH})^{-1}A_{HV}=K_VK_V^*,
}
\tag{10}
\]

so

\[
A_+=A_{VV}+C.
\tag{11}
\]

This confirms the proposed operator cancellation exactly. It also identifies what the positive correction actually measures: not horizontal transversality, but the part of the weighted odd synthesis already lying in `V`.

In particular,

\[
\boxed{
\operatorname{tr}C
=\|K_V\|_{\rm HS}^2
=2\sum_{j=1}^k m_j\|P_Vh_j\|^2.
}
\tag{12}
\]

## 3. Normalization cancels the horizontal singular values completely

The tempting hope was that a small horizontal block might make the normalized cross term large. The exact polar algebra shows the opposite.

Define

\[
Q:=K_H^*(K_HK_H^*)^{-1/2}:H\to E.
\tag{13}
\]

Because `K_H:E\to H` is square and invertible,

\[
Q^*Q=I_H,
\qquad QQ^*=I_E,
\tag{14}
\]

so `Q` is unitary. Then

\[
\boxed{
A_{VH}(-A_{HH})^{-1/2}
=-K_VQ.
}
\tag{15}
\]

Consequently the normalized cross operator has exactly the singular values of `K_V`. Every unitarily invariant norm satisfies

\[
\boxed{
\|A_{VH}(-A_{HH})^{-1/2}\|_*=\|K_V\|_*.
}
\tag{16}
\]

For the Hilbert--Schmidt norm this is just (12), and multiplying (15) by its adjoint recovers (10).

Equation (15) is the decisive obstruction. If `K_H` becomes poorly conditioned or tends to zero under off-line confluence, its singular values are removed by the factor `(-A_{HH})^{-1/2}`. There is no compensating blow-up. The normalization records only the orientation/mass of the odd columns inside `V`, expressed through the unitary polar factor of `K_H`.

This does not say that `K_V` is always small. It says that a lower bound for the normalized Schur interaction is exactly a lower bound for `K_V`, so it cannot be obtained from horizontal collapse or invertibility of `K_H` alone.

## 4. Isolated off-line pair kills every autonomous Schur charge

WI-140 supplies a matched control inside the exact finite Lamzouri class. Take one simple non-real conjugate pair

\[
z=x+iy,\qquad \bar z=x-iy,\qquad y>0,
\]

with no real points. For Lamzouri's real even window,

\[
g(u)=\eta(u)e^{-2\pi iux}\cosh(2\pi uy),
\qquad
h(u)=-i\eta(u)e^{-2\pi iux}\sinh(2\pi uy),
\]

and even/odd parity gives

\[
\langle g,h\rangle=0.
\tag{17}
\]

Here

\[
V=\operatorname{span}\{g\},
\qquad
H=\operatorname{span}\{h\}.
\]

With `K e=\sqrt2 h`, equation (17) yields

\[
\boxed{K_V=0,\qquad K_H e=\sqrt2 h.}
\tag{18}
\]

For every `y>0`, `h\ne0`, so `K_H` and `A_{HH}` are invertible on their one-dimensional spaces. Nevertheless

\[
\boxed{
A_{VH}=0,
\qquad
C=0,
\qquad
A_{VH}(-A_{HH})^{-1/2}=0
}
\tag{19}
\]

**identically**, not merely asymptotically.

At the same time WI-140 computes, with `t(y)=\|h\|^2`,

\[
\lambda_-(A_F)=-2t(y),
\qquad
\Delta=8t(y)+8t(y)^2,
\tag{20}
\]

and

\[
t(y)=4\pi^2\mu_2y^2+O(y^4).
\tag{21}
\]

Thus the configuration contains one genuine off-line pair and one negative eigenvalue for every `y>0`, while both the horizontal block and the full Lamzouri slack collapse as `y\to0`; the proposed normalized Schur correction remains exactly zero throughout.

Therefore no universal implication of the form

\[
\text{off-line pair present}
\Longrightarrow
\operatorname{tr}C\ge c>0
\tag{22}
\]

or any analogous positive lower bound on a unitarily invariant norm of `A_{VH}(-A_{HH})^{-1/2}` can hold in the abstract class of Proposition 2.1.

## 5. What the identity does and does not add to WI-132/WI-137/WI-139

The Schur identity is useful as an exact bookkeeping statement. It says that after eliminating the horizontal block, the signed Lamzouri operator reconstructs the positive retained Gram operator with no remainder. But this is **lossless algebra**, not a new coercive reservoir.

WI-132 studies the genuinely relevant quotient object

\[
U^*(I-P_V)U,
\]

whose small eigenvalues encode horizontal screening after dividing out the unavoidable pair depth. WI-137 charges the full operator distance to the `2/1/0` target, and WI-139 shows that near saturation aligns the negative eigenspace with `H`. Equation (15) does not contradict or strengthen those charges: it removes `K_H` and returns `K_V`.

A future zeta-specific theorem could still make (10) useful. For example, an independent source estimate might force

\[
\|K_V\|_{\rm HS}^2\ge cN
\]

on a positive-density off-line sector, or couple `K_VK_V^*` to an arithmetic statistic inaccessible to the present finite Hilbert inequality. Such a theorem would be new input. The Schur cancellation alone supplies no reason for it to hold.

The finding therefore narrows the bootstrap target: **conditioning of `A_{HH}` cannot be converted into a charge by inverse-square-root normalization**. One must control a quantity that does not algebraically cancel the horizontal singular scale, or bring in source-specific information coupling the vertical and horizontal pieces.

## 6. Prior art and novelty audit

The algebra in (7)--(11) is classical Schur-complement/block Gaussian elimination. Standard references include Emilie V. Haynsworth, *Determination of the inertia of a partitioned Hermitian matrix*, Linear Algebra and its Applications 1 (1968), 73--81, and Fuzhen Zhang (ed.), *The Schur Complement and Its Applications*, Springer, 2005. No novelty is claimed for Schur complements, polar decomposition, unitary invariance of singular values, or the identity obtained by eliminating an invertible block.

Lamzouri's current preprint (arXiv:2609.02882v1, submitted 2 September 2026; manuscript dated 4 September in the current arXiv rendering) states Proposition 2.1 through nested Hilbert spaces and Bessel/Gram--Schmidt estimates. A targeted search of the current text finds no Schur-complement, inertia, or eigenvalue formulation. That absence is not evidence of priority. WI-132 and WI-138 already use Schur-complement and determinant ideas internally, so the only durable line-specific content here is the exact evaluation (10)--(16) of the newly proposed operator normalization and the WI-140 one-pair control showing that it cannot be an autonomous anti-confluence mechanism.

The decisive negative conclusion is therefore not "Schur complements are useless." It is the narrower statement that this **particular normalized cross-block route cannot turn a collapsing Lamzouri horizontal sector into positive quantitative slack without additional source information**.

## 7. Research implication

The operator-Schur clue is resolved negatively as a stand-alone bootstrap. The exact cancellation makes the inverse horizontal block look stronger than it is: after normalization its scale disappears, and the remaining quantity can vanish identically even for a genuine simple off-line pair.

For the live defect-to-zero program, this favors invariants that remain singularity-sensitive under confluence rather than normalizations that quotient the singular scale away. A viable next step must either prove source-level anti-confluence for actual zeta configurations, extract a lower bound on `K_V` from an independent arithmetic/correlation observable, or use a genuinely singular/non-continuous statistic capable of distinguishing the `y>0` off-line pair from its real-double limit. The finite Schur identity alone cannot do that.