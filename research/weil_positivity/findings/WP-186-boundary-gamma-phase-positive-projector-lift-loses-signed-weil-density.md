# WP-186 — The boundary Gamma phase has a universal positive projector lift, but its Weil density appears only in an indefinite derivative

**Status:** `EXACT-DERIVED + DECISIVE-NARROWING + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION + NOT-WEIL-POSITIVITY`.

`WP-169` isolates the exact real-place relative phase

\[
R_\infty(t)
=\pi^{it}
\frac{\Gamma(\tfrac14-\tfrac{it}{2})}
     {\Gamma(\tfrac14+\tfrac{it}{2})},
\qquad |R_\infty(t)|=1
\quad(t\in\mathbb R).
\tag{1}
\]

`WP-183`--`WP-185` show that this phase cannot be repaired into the ordinary bounded-analytic positive-channel category while preserving its exact analytic projective coordinate. They explicitly leave boundary-only positive geometry open, provided it comes with a new sign theorem.

There is a canonical boundary-only positive lift, but it is too weak in a precise way. Put

\[
P_\infty(t)
:=\frac12
\begin{pmatrix}
1&R_\infty(t)\\
\overline{R_\infty(t)}&1
\end{pmatrix}.
\tag{2}
\]

Then `P_infty(t)` is a rank-one orthogonal projector for every real `t`, hence positive semidefinite. However this positivity is **universal for every unimodular phase**, not specific to the Gamma factor. Moreover the signed first-order quantity extracted from the Gamma phase is exactly the archimedean digamma symbol in Weil's explicit formula, while differentiating the projector produces a traceless Hermitian matrix with eigenvalues of both signs. The standard positive projective metric therefore retains only the square or absolute value of the archimedean density and loses its sign.

Thus the remaining boundary-only escape after `WP-185` cannot consist merely of embedding `R_infty` into a positive Gram/projector field and inheriting positivity from that field. A viable route needs additional oriented or nonlocal structure whose sign theorem is independent of the pointwise PSD lift, and it still must couple to the finite-prime and polar sectors.

## 1. Every unimodular phase has the same positive lift

Let

\[
\eta(t)=e^{i\theta(t)},
\qquad |\eta(t)|=1,
\tag{3}
\]

be any measurable phase, with no arithmetic content. Define

\[
P_\eta(t)
:=\frac12
\begin{pmatrix}
1&\eta(t)\\
\overline{\eta(t)}&1
\end{pmatrix}.
\tag{4}
\]

With

\[
u_\eta(t)=\frac1{\sqrt2}
\binom{\eta(t)}{1},
\tag{5}
\]

we have

\[
P_\eta(t)=u_\eta(t)u_\eta(t)^*.
\tag{6}
\]

Therefore

\[
\boxed{P_\eta(t)\succeq0,\qquad P_\eta(t)^2=P_\eta(t),\qquad
\operatorname{spec}P_\eta(t)=\{1,0\}}
\tag{7}
\]

for every phase `eta`. In fact, if

\[
D_\eta(t)=\operatorname{diag}(\eta(t),1),
\tag{8}
\]

then

\[
P_\eta(t)=D_\eta(t)P_1D_\eta(t)^*.
\tag{9}
\]

Hence every pointwise unitary-invariant positive datum of the projector — eigenvalues, trace, determinant, Schatten norms, positive spectral functions — is identical for the Gamma phase and for an arbitrary unrelated phase.

This is a matched control against reading (2) as arithmetic positivity. The phase is present in the off-diagonal orientation of the rank-one line, but **the PSD theorem itself carries no information about which phase was inserted**.

## 2. The exact Weil archimedean symbol is the signed phase velocity

Write locally

\[
R_\infty(t)=e^{i\theta_\infty(t)}.
\tag{10}
\]

Taking the logarithmic derivative of (1) and using

\[
\psi(z)=\frac{\Gamma'(z)}{\Gamma(z)},
\qquad
\psi(\overline z)=\overline{\psi(z)},
\tag{11}
\]

gives the exact identity

\[
\frac{d}{dt}\log R_\infty(t)
=i\left[
\log\pi-\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)
\right].
\tag{12}
\]

Since `|R_infty|=1`, the bracket is `theta_infty'(t)`. Thus

\[
\boxed{
\theta_\infty'(t)
=\log\pi-\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)
}
\tag{13}
\]

and therefore the standard zeta archimedean explicit-formula symbol

\[
\Psi_\infty(t)
:=-\log\pi+\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)
\tag{14}
\]

satisfies

\[
\boxed{\Psi_\infty(t)=-\theta_\infty'(t).}
\tag{15}
\]

This is the strongest reason the boundary phase is tempting: its first-order motion already contains the exact Gamma/digamma density required by the global Weil formula. No zero data or fitted kernel is needed for (15).

But the density is signed. At `t=0`, the classical value

\[
\psi(1/4)=-\gamma-\frac\pi2-3\log2
\tag{16}
\]

gives `Psi_infty(0)<0`, whereas the digamma asymptotic

\[
\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)
=\log(|t|/2)+o(1)
\tag{17}
\]

makes `Psi_infty(t)>0` for sufficiently large `|t|`. Thus the exact archimedean symbol is not itself a nonnegative density that could simply be identified with the PSD mass of (2).

## 3. Differentiating the positive projector exposes an indefinite direction

For a differentiable phase `eta=e^{i theta}`, differentiating (4) gives

\[
P_\eta'(t)
=\frac{\theta'(t)}2
\begin{pmatrix}
0&i\eta(t)\\
-i\overline{\eta(t)}&0
\end{pmatrix}.
\tag{18}
\]

This matrix is Hermitian and satisfies

\[
\bigl(P_\eta'(t)\bigr)^2
=\frac{\theta'(t)^2}{4}I.
\tag{19}
\]

Consequently

\[
\boxed{
\operatorname{spec}P_\eta'(t)
=\left\{\frac{|\theta'(t)|}{2},-rac{|\theta'(t)|}{2}\right\}
}
\tag{20}
\]

whenever `theta'(t) != 0`. The first derivative that contains the signed phase velocity is therefore **indefinite** even though the projector itself is PSD.

The natural positive quadratic differential quantities are instead

\[
\operatorname{Tr}\bigl(P_\eta'(t)^2\bigr)
=\frac{\theta'(t)^2}{2},
\qquad
\|P_\eta'(t)\|_{HS}
=\frac{|\theta'(t)|}{\sqrt2}.
\tag{21}
\]

For the Gamma phase, (15) turns these into

\[
\operatorname{Tr}\bigl(P_\infty'(t)^2\bigr)
=\frac{\Psi_\infty(t)^2}{2},
\qquad
\|P_\infty'(t)\|_{HS}
=\frac{|\Psi_\infty(t)|}{\sqrt2}.
\tag{22}
\]

Thus standard positive projective/Fubini--Study energy keeps the **magnitude** of the exact archimedean symbol but not its sign. This is not a harmless normalization error: replacing `Psi_infty` by `|Psi_infty|` or `Psi_infty^2` changes the explicit formula.

There is also a first-order invariant obstruction. Since `P^2=P` and `Tr P=1`, differentiation yields

\[
PP'+P'P=P',
\qquad
\operatorname{Tr}P'=0,
\qquad
\operatorname{Tr}(PP')=0.
\tag{23}
\]

So the obvious conjugation-invariant scalar contractions linear in `P'` vanish. The first nontrivial metric scalar is quadratic, exactly as in (21).

## 4. An oriented connection can recover the sign, but positivity no longer supplies it

One can recover `theta'` from a chosen phase convention for a lift of the rank-one line. For the vector (5), the usual connection coefficient is proportional to

\[
-i\langle u_\eta,u_\eta'\rangle
=\frac{\theta'}2.
\tag{24}
\]

However this is not determined by positivity of the projector. Multiplying the lift by the scalar gauge `e^{-i\theta/2}` gives

\[
\widetilde u_\eta
=\frac1{\sqrt2}
\binom{e^{i\theta/2}}{e^{-i\theta/2}},
\qquad
\widetilde u_\eta\widetilde u_\eta^*=P_\eta,
\tag{25}
\]

but now

\[
-i\langle\widetilde u_\eta,\widetilde u_\eta'\rangle=0.
\tag{26}
\]

The same positive projector therefore admits lifts with different connection coefficients. To extract the signed quantity (15), one must specify extra orientation/gauge/boundary data or another nonlocal observable. That additional structure may be legitimate, but its sign theorem is **new input**; it is not inherited from `P_infty\succeq0`.

This distinguishes two statements that would otherwise be easy to conflate:

\[
\boxed{
R_\infty\text{ embeds exactly in a PSD rank-one boundary field}
}
\tag{27}
\]

is true and universal, while

\[
\boxed{
\text{the PSD field forces the signed Weil archimedean functional}
}
\tag{28}
\]

is false for the canonical pointwise/projective readouts above.

## 5. Aggressive falsification and scope

This finding closes only a specific boundary-only escape after `WP-185`.

**It does not rule out boundary geometry altogether.** A source-forced oriented connection, symplectic pairing, nonlocal holonomy, Toeplitz/Hankel compression, singular integral, or indefinite intermediate form could use the phase motion differently. Such a construction must prove its own sign theorem and cannot cite the rank-one PSD lift as that theorem.

**It does not rule out pre-quotient coupling.** `WP-185` leaves open operations that change the projective coordinate before bounded scalarization. Equation (2) begins after the exact relative phase has already been formed.

**It does not produce finite-prime or polar terms.** The calculation is purely archimedean. Even an independent sign theorem for an oriented boundary observable would still have to couple intrinsically to the Mangoldt sector and the global/polar counterterms required by the research mandate.

**It does not use RH or nontrivial zero data.** Equations (12)--(22) use only the explicit Gamma factor and elementary projector algebra.

**The matched control is maximally strong.** Replacing `R_infty` by any smooth unimodular function gives the same PSD theorem (7), the same derivative spectrum formula (20), and the same positive square/absolute-value readouts (21). Therefore the pointwise positivity mechanism cannot distinguish the arithmetic Gamma phase from a hand-picked phase.

## 6. Prior-art and novelty audit

Nothing in the abstract geometry is new. Rank-one projectors, the Fubini--Study/quantum metric, and Berry-type connection coefficients are classical projective Hilbert-space geometry; a targeted literature search found the expected standard projector/quantum-geometric formulations and no need for a new theorem. The identities (7), (18)--(23), and the gauge witness (25)--(26) are direct `2 x 2` calculations.

The arithmetic input is likewise classical: the digamma function is the logarithmic derivative of Gamma, and `SOURCES.md` already anchors the zeta Weil explicit formula with the archimedean symbol (14), including modern compact-window formulations. `WP-169` supplies the project-specific exact phase (1).

The Mathia-specific contribution is the **matched combination** of these two established structures: the exact `WP-169` Gamma phase admits a perfectly positive boundary Gram lift, but the operation that exposes its required Weil density immediately leaves the positive cone, while the canonical positive differential metric squares away the sign. This is a decisive audit of a concrete surviving architecture, not a claim of new projector or Gamma-function theory.

## Consequence for the research line

The exact archimedean phase is more informative than a mere representation: its derivative already is the required digamma symbol. But **pointwise positive projective geometry cannot turn that fact into Weil positivity**. The positivity is universal for arbitrary phases, and the sign-sensitive first derivative is indefinite.

The surviving search must therefore couple the Gamma phase to additional structure **before** invoking a sign theorem: an intrinsically oriented/nonlocal boundary response, or preferably the still-missing nonseparable finite--archimedean geometry in which mixed-prime data and the archimedean/polar completion participate in one global form. Any future proposal that merely places `R_infty` in a PSD Gram/projector matrix and then reads positivity from that matrix is now a matched-control repackaging, not a solution to the Weil-positivity mandate.
