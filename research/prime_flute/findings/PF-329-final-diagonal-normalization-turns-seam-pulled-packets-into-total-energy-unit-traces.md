# PF-329 — final diagonal normalization turns seam-pulled packets into total-energy unit traces

**Status:** `EXACT-DERIVED + BLOCK-CONGRUENCE-INVARIANCE + PACKET-REPRESENTATION-CORRECTION + NEGATIVE/ROUTE-NARROWING`.

PF-325 expresses the local direct-angle Hilbert--Schmidt mass as an exact integral over translated unit packets in the final normalized physical-low Hilbert coordinate. PF-326--PF-328 then pull those packets back only through the seam normalizer and prove that a positive-length family retains compactification-critical pre-angle energy, with raw parity scales `w_n^{-1}` and `w_n`.

Those scales are real at the seam-pulled **pre-angle** stage, but they are not yet the raw boundary traces tested by the intrinsic angle. There is one further low-side factor, already present in PF-317, that cannot be omitted when a packet is moved back to raw pant coordinates: the inverse square root of the **completed low diagonal energy**.

On every finite direct `L/H` section, let `Q>0` be the seam DtN form and `Lambda>=0` the shear-deleted one-cusp-pant/core DtN form. Because `Q` commutes with the physical `L/H` split, write

\[
M^{\rm raw}:=Q+\Lambda
=\begin{pmatrix}A_0&B_0\\B_0^*&C_0\end{pmatrix},
\qquad
S:=Q^{-1/2}=S_L\oplus S_H,
\]

and

\[
M:=S M^{\rm raw}S
=I+Q^{-1/2}\Lambda Q^{-1/2}
=\begin{pmatrix}A&B\\B^*&C\end{pmatrix}.
\]

The raw and seam-normalized intrinsic angles

\[
T_0:=A_0^{-1/2}B_0C_0^{-1/2},
\qquad
T:=A^{-1/2}BC^{-1/2}
\]

are exactly unitarily equivalent. More precisely,

\[
U_L:=A_0^{1/2}S_LA^{-1/2},
\qquad
U_H:=C_0^{1/2}S_HC^{-1/2}
\]

are unitary and

\[
\boxed{T=U_L^*T_0U_H.}
\]

Thus seam normalization is a block-diagonal coordinate change at the intrinsic-angle level: singular values, Schatten norms, and packet response norms are unchanged after the corresponding unitary identification.

For a unit PF-325 packet `psi_t` in the normalized low coordinate, the actual raw low boundary trace entering the canonical-correlation problem is therefore

\[
\boxed{
g_t=S_LA^{-1/2}\psi_t,}
\]

not the seam-only pullback

\[
u_t=S_L\psi_t
\]

studied in PF-326--PF-328. The corrected trace has the exact normalization

\[
\boxed{\langle g_t,A_0g_t\rangle=1,}
\]

and its completed angle response is exactly

\[
\boxed{
\|T^*\psi_t\|
=
\sup_{0\ne h\in H}
\frac{|\langle \Lambda_{HL}g_t,h\rangle|}
{\langle h,C_0h\rangle^{1/2}}.
}
\]

By contrast,

\[
\langle u_t,A_0u_t\rangle
=
\langle\psi_t,A\psi_t\rangle,
\]

which can be large and strongly `t`-dependent. Hence PF-328's `w_n^{-1}` symmetric and `w_n` antisymmetric transverse-energy scales cannot be promoted to angle lower bounds by restoring a scalar normalization. In general `A^{-1/2}\psi_t` is not a scalar multiple of `\psi_t`; the completed diagonal normalizer may reshape the packet and need not commute with physical translations.

This identifies the exact remaining packet gate. The PF-328 positive-measure critical interval is a valid pre-angle calibration, but to turn it into an obstruction to the PF-318/PF-325 endpoint one must prove that `A^{-1/2}` preserves enough of that critical packet family, or else estimate the raw total-energy correlation above directly. Propagating the seam-only packet through the pant and carrying its common parity scale is insufficient.

## Claim

Work on one finite shear-deleted local direct `L/H` section. Assume:

1. `Q>0` is the canonical seam DtN form and reduces the physical split `L\oplus H`;
2. `\Lambda\ge0` is the full common-completion one-cusp-pant/core DtN form on the same boundary section;
3. `M^{\rm raw}=Q+\Lambda>0` and `M=Q^{-1/2}M^{\rm raw}Q^{-1/2}>0`.

Let

\[
M^{\rm raw}=\begin{pmatrix}A_0&B_0\\B_0^*&C_0\end{pmatrix},
\qquad
M=\begin{pmatrix}A&B\\B^*&C\end{pmatrix}.
\tag{1}
\]

Then:

1. `B_0=\Lambda_{LH}` and `B=S_LB_0S_H` because `Q` has no `L/H` cross block;
2. with
   \[
   U_L=A_0^{1/2}S_LA^{-1/2},
   \qquad
   U_H=C_0^{1/2}S_HC^{-1/2},
   \tag{2}
   \]
   one has
   \[
   \boxed{U_L^*U_L=I_L,\qquad U_H^*U_H=I_H,}
   \tag{3}
   \]
   and
   \[
   \boxed{A^{-1/2}BC^{-1/2}=U_L^*A_0^{-1/2}B_0C_0^{-1/2}U_H;}
   \tag{4}
   \]
3. consequently the two intrinsic angles have identical singular values and identical two-sided symmetric-ideal norms;
4. for every unit `\psi\in L`, if
   \[
   g:=S_LA^{-1/2}\psi,
   \tag{5}
   \]
   then
   \[
   \boxed{\langle g,A_0g\rangle=1;}
   \tag{6}
   \]
5. its normalized angle response admits the raw variational representation
   \[
   \boxed{
   \|T^*\psi\|
   =
   \sup_{0\ne h\in H}
   \frac{|\langle B_0^*g,h\rangle|}
   {\langle h,C_0h\rangle^{1/2}}.
   }
   \tag{7}
   \]

For the PF-325 packet orbit `\psi=\psi_{n,t}`, equations (5)--(7) identify the exact raw trace and denominator that must be controlled before PF-328's critical pre-angle energy can say anything about the completed direct angle.

## 1. Block-diagonal congruence preserves the intrinsic angle

Since `A=S_LA_0S_L` and `C=S_HC_0S_H`, equation (2) gives

\[
U_L^*U_L
=A^{-1/2}S_LA_0S_LA^{-1/2}
=I,
\]

and similarly for `U_H`. Moreover

\[
\begin{aligned}
U_L^*T_0U_H
&=A^{-1/2}S_LA_0^{1/2}
 A_0^{-1/2}B_0C_0^{-1/2}
 C_0^{1/2}S_HC^{-1/2}\\
&=A^{-1/2}S_LB_0S_HC^{-1/2}\\
&=A^{-1/2}BC^{-1/2}=T.
\end{aligned}
\]

This is the finite-section version of the same coordinate invariance already implicit in PF-320's intrinsic-angle normalization. It is stronger than saying that a common scalar cancels: the full positive block-diagonal seam multiplier is absorbed by left/right unitaries once each side is normalized by its own total diagonal energy.

The statement does **not** say that the seam geometry is irrelevant. In raw coordinates it appears as the positive summand `Q` inside `A_0` and `C_0`, so it changes the total energy against which the pant cross form is measured. What disappears is only its status as an independent coordinate-amplitude factor.

## 2. The packet seen by the raw pant includes the completed diagonal inverse square root

Let `\psi\in L` be unit. From (5),

\[
\begin{aligned}
\langle g,A_0g\rangle
&=\langle A^{-1/2}\psi,S_LA_0S_LA^{-1/2}\psi\rangle\\
&=\langle A^{-1/2}\psi,AA^{-1/2}\psi\rangle\\
&=1,
\end{aligned}
\]

which proves (6).

Also

\[
U_L\psi=A_0^{1/2}g.
\tag{8}
\]

Using (4), unitary invariance of the norm, and (8),

\[
\begin{aligned}
\|T^*\psi\|
&=\|T_0^*U_L\psi\|\\
&=\|C_0^{-1/2}B_0^*g\|.
\end{aligned}
\tag{9}
\]

The standard Riesz variational formula for the `C_0` energy is exactly (7).

For the seam-only pullback `u=S_L\psi`, one instead has

\[
\boxed{
\langle u,A_0u\rangle
=\langle\psi,A\psi\rangle
=1+\langle\psi,K_{LL}\psi\rangle.
}
\tag{10}
\]

Therefore `u` is generally not a unit vector for the raw low total energy. Replacing `u` by a scalar normalization does not fix the issue unless `\psi` happens to be an eigenvector of `A`, because the true trace uses `A^{-1/2}\psi` before seam pullback.

## 3. Consequence for the PF-328 parity scales

PF-328 proves, on a positive-length interval of critical packet centers, that the seam-only pullbacks carry explicit pre-angle transverse-form scales: order `w_n^{-1}` in the symmetric face-parity channel and order `w_n` in the antisymmetric channel. Those statements remain correct.

Equation (10) shows why they are not angle amplitudes. The same pant energy that makes a seam-only packet large also enters the low diagonal block `A`, and the intrinsic angle inserts `A^{-1/2}` before the packet reaches the raw cross form. The cancellation need not be a scalar cancellation and need not preserve the translation shape.

Thus the following inference is invalid without an additional theorem:

\[
\text{large PF-328 pre-angle energy on }I_n
\quad\Longrightarrow\quad
\text{large completed angle response on }I_n.
\]

The correct implication needs control of the preconditioned family

\[
\boxed{
g_{n,t}=Q_{L,n}^{-1/2}A_n^{-1/2}\psi_{n,t}.}
\tag{11}
\]

A useful positive transfer theorem would show, on a fixed positive-measure subset of the PF-328 critical interval, that `A_n^{-1/2}` preserves enough localization/critical transverse content to keep the raw total-energy correlation (7) non-negligible. A useful endpoint theorem may instead show that this diagonal preconditioner suppresses or redistributes the critical family strongly enough to meet PF-318.

Either outcome is mathematically meaningful. PF-328 by itself decides neither.

## 4. The packet-position identity remains exact in angle coordinates

Nothing here weakens PF-325. Its identity

\[
\|T\|_{\mathcal S_2}^2
=\frac{m_n}{L_n}\int_0^{L_n}\|T^*\psi_{n,t}\|^2dt
\]

is exact in the normalized angle coordinate and needs no translation symmetry of `T`.

What changes is the raw-PDE interpretation of each integrand. The seam map `Q^{-1/2}` commutes with translations, but the completed diagonal factor `A^{-1/2}` generally does not. Hence the raw family `g_{n,t}` need not be a translate of one fixed profile. PF-326's translation-preserving seam pullback and PF-328's positive-measure critical interval remain useful calibrations, but they stop one operator before the actual intrinsic-angle input.

This also suggests a cleaner alternative to propagating packets explicitly: estimate the canonical raw correlation (7) directly in the total energies `A_0` and `C_0`. That formulation automatically includes the common positive completion and cannot be fooled by raw seam-amplitude growth.

## Prior-art and novelty audit

The block algebra is classical. In finite-dimensional canonical-correlation language, canonical correlations are invariant under nonsingular changes of coordinates in the two variable blocks; the calculation above is the positive-form/operator version of that fact. PF-320 already contains the same unitary-equivalence mechanism for intrinsic angles under diagonal renormalization. A targeted literature check found the standard canonical-correlation invariance statement and no basis for claiming a new general linear-algebra theorem here.

The project-specific contribution is the application to the exact PF-317 decomposition

\[
Q+\Lambda
\longleftrightarrow
I+Q^{-1/2}\Lambda Q^{-1/2}
\]

and, especially, to the PF-325--PF-328 packet program. It identifies the raw trace actually represented by a unit packet of the completed intrinsic angle and rules out treating the explicit PF-328 seam parity factors as standalone angle lower bounds.

## Boundaries and falsification

1. **No endpoint estimate is proved.** Equations (4)--(7) are exact representation identities; they neither prove nor refute the PF-318 Hilbert--Schmidt budget.
2. **PF-326--PF-328 remain valid.** Their seam-only packet localization, critical energy, positive-measure interval, and parity-scale statements are pre-angle facts. The present finding only fixes the missing final-diagonal step.
3. **No scalar cancellation is asserted.** `A^{-1/2}` may mix low modes and may depend on packet position through the non-translation-invariant pant response. The point is precisely that a scalar correction is not enough in general.
4. **The seam form still matters physically.** It survives as the raw positive energy `Q` in `A_0,C_0`; only coordinate-dependent amplification from `Q^{-1/2}` is removed by intrinsic normalization.
5. **Finite sections are the safe formulation.** The proof is exact on every finite PF-311/PF-317 section. Any infinite-tail statement must be taken through the same finite-section-compatible limiting realization already required by the direct-angle program.
6. **The new decisive packet test is total-energy normalized.** To convert the PF-328 critical family into an obstruction, control (11) or the equivalent variational correlation (7), not only `Q^{-1/2}\psi_{n,t}`.

No scattering/determinant theorem, zeta-zero correspondence, critical-line result, or RH implication is established.