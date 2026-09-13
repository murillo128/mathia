# PF-331 — the completed low polar factor has a uniform gap and cannot amplify locality defects

**Status:** `EXACT-DERIVED + GAPPED-POLAR-COMMUTATOR + LOCALITY-TRANSFER + ROUTE-SHARPENING`.

PF-330 identifies the only extra packet reshaping introduced by completed low normalization as the unitary polar factor

\[
U_L=A_0^{1/2}Q_L^{-1/2}A^{-1/2},
\qquad
A=Q_L^{-1/2}A_0Q_L^{-1/2}=I+K_{LL},
\]

of

\[
F:=A_0^{1/2}Q_L^{-1/2}.
\]

That finding correctly leaves open whether `U_L` is spatially local enough to transport the PF-323--PF-328 packet obstruction. There is, however, no independent **polar-instability** mechanism in this particular factor. The positive identity term in the completed normalized energy gives

\[
\boxed{F^*F=A=I+K_{LL}\ge I,}
\]

so every finite-section singular value of `F` is at least one. A standard gapped-sign argument then gives an exact quantitative transfer: commutator or off-diagonal locality bounds for `F` pass to its polar unitary with no loss in the present normalization.

In particular, for every bounded self-adjoint spatial localizer `\chi`,

\[
\boxed{\|[U_L,\chi]\|\le \|[F,\chi]\|,}
\]

and for every physical translation `\tau_t`,

\[
\boxed{\|[U_L,\tau_t]\|\le \|[F,\tau_t]\|.}
\]

Thus the PF-330 localization gate can be sharpened. One does **not** need to prove locality of an abstract, potentially unstable polar factor. It is enough to prove locality/quasilocality of the concrete completed-energy whitening map `F=A_0^{1/2}Q_L^{-1/2}`. Polar extraction cannot make its translation or cutoff commutators larger.

This is materially different from the PF-254/PF-257 Robin polar factor. There the relative injection operator may have singular values approaching zero, so a naked polar partial isometry can indeed be unstable and PF-257 must recombine it with its vanishing amplitude. Here the completed positive identity produces a uniform singular-value floor before the polar factor is taken.

## Claim

Let `F` be an invertible operator on one finite low section and write its right polar decomposition

\[
F=U|F|,
\qquad |F|=(F^*F)^{1/2}.
\]

Assume

\[
F^*F\ge \gamma^2 I
\tag{1}
\]

for some `\gamma>0`. Then:

1. for every bounded self-adjoint operator `X`,
   \[
   \boxed{
   \|[U,X]\|\le \gamma^{-1}\|[F,X]\|;
   }
   \tag{2}
   \]
2. for every unitary `V`,
   \[
   \boxed{
   \|[U,V]\|\le \gamma^{-1}\|[F,V]\|;
   }
   \tag{3}
   \]
3. if `P,R` are orthogonal projections and `0\le\chi\le I` satisfies
   \[
   \chi P=P,
   \qquad R\chi=0,
   \tag{4}
   \]
   then
   \[
   \boxed{
   \|RUP\|\le \gamma^{-1}\|[F,\chi]\|;
   }
   \tag{5}
   \]
4. consequently, for any unit vector `\psi`,
   \[
   \boxed{
   \|RU\psi\|
   \le
   \gamma^{-1}\|[F,\chi]\|
   +\|(I-P)\psi\|.
   }
   \tag{6}
   \]

For the PF-329/PF-330 completed low normalization,

\[
F=A_0^{1/2}Q_L^{-1/2},
\qquad
F^*F=A=I+K_{LL}\ge I,
\]

so one may take `\gamma=1`. Therefore every finite-section cutoff or translation commutator estimate for the concrete map `F` transfers to `U_L` with constant one.

Because the seam normalizer `Q_L^{-1/2}` commutes with the physical translations used in PF-325--PF-330, (3) specializes further to

\[
\boxed{
\|[U_L,\tau_t]\|
\le
\|[A_0^{1/2},\tau_t]Q_L^{-1/2}\|.
}
\tag{7}
\]

The remaining locality question is therefore a completed DtN square-root question, not a free polar-orientation question.

## 1. The polar factor is the sign of a uniformly gapped self-adjoint dilation

Introduce the self-adjoint block operator

\[
\mathbb D_F=
\begin{pmatrix}
0&F\\
F^*&0
\end{pmatrix}.
\tag{8}
\]

Then

\[
\mathbb D_F^2
=
\begin{pmatrix}
FF^*&0\\
0&F^*F
\end{pmatrix}
\ge \gamma^2I.
\tag{9}
\]

Hence the spectrum of `\mathbb D_F` is disjoint from `(-\gamma,\gamma)`. Moreover

\[
\operatorname{sgn}(\mathbb D_F)
=
\begin{pmatrix}
0&U\\
U^*&0
\end{pmatrix}.
\tag{10}
\]

Let `E_+` and `E_-` be the positive and negative spectral projections of `\mathbb D_F`. Thus

\[
\operatorname{sgn}(\mathbb D_F)=E_+-E_-=2E_+-I.
\tag{11}
\]

For a bounded operator `W`, put

\[
Y=E_+WE_-.
\]

Writing `D_+=\mathbb D_F|_{E_+}` and `D_-=\mathbb D_F|_{E_-}`, one has

\[
D_+Y-YD_-
=E_+[\mathbb D_F,W]E_-.
\tag{12}
\]

Since `D_+\ge\gamma I` and `D_-\le-\gamma I`, the Sylvester equation has the explicit solution

\[
Y
=
\int_0^\infty
 e^{-tD_+}
 E_+[\mathbb D_F,W]E_-
 e^{tD_-}
\,dt,
\tag{13}
\]

and therefore

\[
\boxed{
\|E_+WE_-\|
\le
\frac1{2\gamma}\|[\mathbb D_F,W]\|.
}
\tag{14}
\]

The same bound holds for `E_-WE_+`. Relative to `E_+\oplus E_-`, the commutator `[E_+,W]` has only these two off-diagonal blocks, so

\[
\|[E_+,W]\|
\le
\frac1{2\gamma}\|[\mathbb D_F,W]\|.
\tag{15}
\]

Using (11),

\[
\boxed{
\|[\operatorname{sgn}(\mathbb D_F),W]\|
\le
\gamma^{-1}\|[\mathbb D_F,W]\|.
}
\tag{16}
\]

This is the only abstract estimate needed below.

## 2. Diagonal localizers give the polar commutator bound

Take

\[
W=X\oplus X.
\]

If `X=X^*`, then

\[
[\mathbb D_F,W]
=
\begin{pmatrix}
0&[F,X]\\
[F^*,X]&0
\end{pmatrix},
\qquad
[F^*,X]=-[F,X]^*.
\tag{17}
\]

Hence

\[
\|[\mathbb D_F,W]\|=\|[F,X]\|.
\tag{18}
\]

The upper-right block of the left side of (16) is `[U,X]`, which proves (2).

If `V` is unitary, then

\[
[F^*,V]=V[F,V]^*V,
\]

so the two off-diagonal blocks of `[\mathbb D_F,V\oplus V]` again have the same norm and

\[
\|[\mathbb D_F,V\oplus V]\|=\|[F,V]\|.
\]

Equation (3) follows in the same way.

The point is not merely continuity of the polar decomposition. The constant depends only on the lower singular-value gap `\gamma`. For the completed Prime-Flute low block, that gap is uniformly one because the seam-normalized diagonal energy is exactly `I+K_{LL}` with `K_{LL}\ge0`.

## 3. Spatial leakage through the polar factor is controlled by the whitening-map commutator

Let `P` project onto an input packet window, let `R` project onto a separated output region, and choose a bounded spatial cutoff `\chi` with `\chi P=P` and `R\chi=0`. Then

\[
R[U,\chi]P
=RU\chi P-R\chi UP
=RUP.
\]

Equation (2) gives (5). Decomposing any unit packet as

\[
\psi=P\psi+(I-P)\psi
\]

and using `\|U\|=1` gives (6).

This is the form directly relevant to the PF-323--PF-328 critical packets. Those packets already have controlled fixed-window concentration before completed normalization. If one can prove, for cutoffs adapted to the same fixed physical windows,

\[
\|[F_n,\chi_{n,t}]\|\to0
\]

uniformly on a positive-measure family of critical centers, then (6) transfers their concentration through `U_{L,n}`. No separate theorem about an unstable polar orientation is needed.

Likewise, for the PF-330 translation formulation `\psi_t=\tau_t\psi_0`, equation (3) gives

\[
\boxed{
\|U_L\psi_t-\tau_tU_L\psi_0\|
\le
\|[F,\tau_t]\|.
}
\tag{19}
\]

This does not by itself prove that the reference profile `U_L\psi_0` is localized; the cutoff estimate (5)--(6) is the stronger spatial statement. Together they identify exactly what must be controlled on the concrete completed DtN square-root map.

## 4. Relation to the earlier Robin polar obstruction

PF-254 isolates a polar partial isometry for the normalized Robin injection and PF-257 warns that this naked polar factor can be unstable when singular values approach zero. That warning remains correct.

The present `F` lies in a different spectral regime. Its modulus satisfies

\[
|F|^2=F^*F=I+K_{LL}\ge I.
\]

Therefore the self-adjoint dilation (8) has a fixed gap around zero, and the sign/polar operation is uniformly commutator-Lipschitz on the exact finite sections used by the direct-angle program. The PF-257 small-singular-value failure mode is absent here.

This comparison matters strategically. PF-330 correctly identified `U_L` as the only possible reshaping between normalized packets and raw total-energy packets, but the remaining work should now be aimed at the locality of `F=A_0^{1/2}Q_L^{-1/2}` itself. Treating `U_L` as an additional uncontrolled operator would double-count a difficulty that the positive completion has already regularized.

## Prior-art and novelty audit

The abstract mathematics is classical spectral-subspace and polar-factor perturbation theory. A targeted audit found the Davis--Kahan spectral-gap framework and later perturbation bounds for unitary polar factors, as well as general commutator-Lipschitz functional-calculus literature. No new general operator theorem is claimed here.

The proof above is self-contained on the finite sections used by PF-317--PF-330: it derives the needed estimate directly from the gapped self-adjoint dilation and the elementary Sylvester integral (13). No external theorem is imported, so `SOURCES.md` acquires no new theorem dependency.

The project-specific contribution is the observation that the **exact completed Prime-Flute factor automatically has `\gamma=1`**, because the seam-normalized low diagonal is `I+K_{LL}`. That removes polar instability as an independent obstruction and turns the packet-locality gate into a concrete commutator estimate for the completed DtN square-root whitening map.

## Boundaries and falsification

1. **No locality estimate for `F` is proved.** Equations (2)--(7) only show that polar extraction cannot make an existing locality defect worse by more than the inverse singular-value gap, which is one here.
2. **No completed-angle lower bound is proved.** The PF-323--PF-328 packet obstruction still requires a positive-measure family whose completed raw correlation remains non-negligible.
3. **Translation compatibility alone is not enough.** Equation (19) preserves a translated profile if `[F,\tau_t]` is small, but a spatial obstruction also needs the reference profile itself to remain concentrated. Equations (5)--(6) state the appropriate cutoff version.
4. **Finite sections are the safe statement.** Passing to the full infinite boundary problem still requires the finite-section-compatible limiting realization already used by PF-317--PF-330.
5. **The upper-bound route is unchanged.** PF-330's basis-free Hilbert--Schmidt trace can still be estimated directly without proving any packet locality theorem.
6. **No scattering/determinant theorem, zeta-zero correspondence, critical-line result, or RH implication is established.**

## Consequence for the research line

The negative/obstruction branch of the accepted direct-angle clue now has a sharper next gate. Instead of asking for locality of the polar unitary as a separate black-box theorem, estimate

\[
F_n=A_{0,n}^{1/2}Q_{L,n}^{-1/2}
\]

against physical translations and, more importantly, fixed-window spatial cutoffs. Any uniform small commutator/off-diagonal estimate for `F_n` transfers to `U_{L,n}` with constant one. If such an estimate holds on the PF-328 critical interval, test the completed raw correlation separately in the two PF-324 arithmetic boundary regimes. If it fails, the failure is already present in the concrete completed-energy square-root map rather than being created by polar normalization.