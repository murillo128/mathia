# PF-330 — completed low normalization rotates the packet frame instead of damping its total-energy mass

**Status:** `EXACT-DERIVED + UNITARY-TIGHT-FRAME + RAW-TOTAL-ENERGY-REFORMULATION + ROUTE-NARROWING`.

PF-329 identifies the raw low trace represented by a unit packet `\psi_t` of the completed intrinsic angle as

\[
g_t=S_LA^{-1/2}\psi_t,
\qquad
A=S_LA_0S_L,
\]

where `A_0=Q_L+\Lambda_{LL}` is the raw completed low energy and `S_L=Q_L^{-1/2}`. It also constructs the unitary

\[
U_L=A_0^{1/2}S_LA^{-1/2}
\]

and proves

\[
A_0^{1/2}g_t=U_L\psi_t.
\]

Combining this with the exact PF-325 translation-frame identity gives a sharper interpretation of the remaining packet gate.

The completed diagonal inverse square root does **not** destroy packet mass in the intrinsic total-energy Hilbert space. It converts the physical translation frame into a unitary-rotated tight frame. What can be lost is the packet's **spatial interpretation relative to the critical physical window**, because the polar unitary `U_L` need not commute with physical translations.

This separates two questions that were previously mixed together:

1. the global/direct-channel Hilbert--Schmidt accounting is exactly invariant under the completed low normalization; and
2. transferring the PF-328 positive-measure geometric obstruction requires a locality or translation-compatibility theorem for `U_L`, not a scalar lower bound on `A^{-1/2}`.

## Claim

Work on one finite shear-deleted local direct `L/H` section in the notation of PF-329. Let

\[
M^{\rm raw}=
\begin{pmatrix}A_0&B_0\\B_0^*&C_0\end{pmatrix},
\qquad
M=S M^{\rm raw}S=
\begin{pmatrix}A&B\\B^*&C\end{pmatrix},
\]

with `S=S_L\oplus S_H`, and let

\[
T_0=A_0^{-1/2}B_0C_0^{-1/2},
\qquad
T=A^{-1/2}BC^{-1/2}.
\]

Let `\{\psi_t:0\le t<L\}` be the PF-325 unit translation frame on the `m`-dimensional retained low band, so that

\[
\boxed{
\frac mL\int_0^L |\psi_t\rangle\langle\psi_t|\,dt=I_L.
}
\tag{1}
\]

Define

\[
\phi_t:=U_L\psi_t,
\qquad
U_L:=A_0^{1/2}S_LA^{-1/2},
\qquad
g_t:=A_0^{-1/2}\phi_t.
\tag{2}
\]

Then:

1. `U_L` is unitary and `\{\phi_t\}` is again the same-constant continuous tight frame,
   \[
   \boxed{
   \frac mL\int_0^L |\phi_t\rangle\langle\phi_t|\,dt=I_L;
   }
   \tag{3}
   \]
2. every `g_t` has unit raw completed low energy,
   \[
   \boxed{\langle g_t,A_0g_t\rangle=1;}
   \tag{4}
   \]
3. the family `\{g_t\}` is a tight frame in the raw low energy Hilbert space `\mathcal H_{A_0}` with inner product `\langle x,y\rangle_{A_0}=\langle A_0^{1/2}x,A_0^{1/2}y\rangle`, namely
   \[
   \boxed{
   \frac mL\int_0^L
   |\langle x,g_t\rangle_{A_0}|^2dt
   =\|x\|_{A_0}^2
   \qquad(x\in\mathcal H_{A_0});
   }
   \tag{5}
   \]
4. the completed direct-angle Hilbert--Schmidt mass has the exact raw total-energy packet formula
   \[
   \boxed{
   \|T\|_{\mathcal S_2}^2
   =\|T_0\|_{\mathcal S_2}^2
   =\frac mL\int_0^L
   \|C_0^{-1/2}B_0^*g_t\|^2dt;
   }
   \tag{6}
   \]
5. equivalently, on every finite section,
   \[
   \boxed{
   \|T\|_{\mathcal S_2}^2
   =\operatorname{Tr}
   \bigl(A_0^{-1}B_0C_0^{-1}B_0^*\bigr).
   }
   \tag{7}
   \]

Thus the low completed normalization cannot win the PF-318 Hilbert--Schmidt budget merely by reducing the total-energy norm of the PF-325 frame: that norm is exactly one for every raw packet and the entire frame remains tight. The only packet-level effect relevant to the PF-328 spatial obstruction is the possible nonlocal rotation `\psi_t\mapsto\phi_t=U_L\psi_t` before raw energy whitening.

## 1. Unitary rotation preserves the PF-325 tight frame exactly

PF-329 proves

\[
U_L^*U_L=I_L.
\]

Applying `U_L` to both sides of (1) gives

\[
\frac mL\int_0^L
|U_L\psi_t\rangle\langle U_L\psi_t|dt
=U_LI_LU_L^*=I_L,
\]

which is (3).

Since `A_0^{1/2}g_t=\phi_t`, equation (4) follows immediately. For every raw low vector `x`,

\[
\langle x,g_t\rangle_{A_0}
=\langle A_0^{1/2}x,\phi_t\rangle.
\]

Applying the tight-frame identity (3) to `A_0^{1/2}x` proves (5). Therefore `A_0^{-1/2}` is an isometry from the ordinary normalized low coordinate into the raw completed-energy Hilbert space; it is not an independent scalar damping mechanism there.

## 2. The endpoint average can be written without tracking `A^{-1/2}\psi_t` pointwise

PF-329 gives

\[
T=U_L^*T_0U_H
\]

with `U_H` unitary. Hence

\[
\|T^*\psi_t\|
=\|T_0^*\phi_t\|
=\|C_0^{-1/2}B_0^*g_t\|.
\tag{8}
\]

Apply PF-325 to the tight frame `\phi_t`. This proves (6). Taking the Hilbert--Schmidt trace of

\[
T_0T_0^*
=A_0^{-1/2}B_0C_0^{-1}B_0^*A_0^{-1/2}
\]

and using cyclicity of the finite-dimensional trace gives (7).

Consequently the positive endpoint route does not require a pointwise description of `A^{-1/2}\psi_t` merely to recover the integrated PF-318 budget. One may instead estimate the basis-free raw canonical-correlation trace (7). Pointwise packet control becomes essential only when one wants to transfer **spatially localized** information such as the PF-328 critical interval into a lower bound or regime distinction.

## 3. The exact missing geometric theorem is locality of the polar unitary

The operator

\[
F:=A_0^{1/2}S_L
\]

satisfies

\[
F^*F=S_LA_0S_L=A.
\]

Therefore

\[
\boxed{F=U_LA^{1/2}}
\tag{9}
\]

is the polar decomposition of `F`; the packet-reshaping map `U_L` is exactly its unitary polar factor.

Let `\tau_t` denote physical translation on the retained low band and write `\psi_t=\tau_t\psi_0`. Then

\[
\phi_t=U_L\tau_t\psi_0.
\]

If `U_L` commuted with the translations, one would have

\[
\phi_t=\tau_t(U_L\psi_0),
\]

so the completed frame would remain a translated fixed profile and the PF-328 positive-measure interval could be tested in the same physical coordinate after replacing the profile. More generally, the exact defect from that picture is

\[
\boxed{
\phi_t-\tau_t\phi_0
=[U_L,\tau_t]\psi_0.
}
\tag{10}
\]

Thus a useful transfer theorem is not a scalar lower bound on `A^{-1/2}`. It is a locality/commutator estimate for the polar unitary `U_L` on the PF-328 critical packet family, strong enough to show that a positive-measure set of centers remains concentrated in the corresponding raw geometric region.

Conversely, if `U_L` is strongly nonlocal on that family, the parameter `t` remains a valid tight-frame label for Hilbert--Schmidt accounting but no longer identifies a raw packet centered near the physical point `t`. In that case the two PF-324 boundary regimes cannot be distinguished by simply inserting the PF-328 seam-local packet into the completed angle.

## 4. Consequence for the live direct-angle clue

The live direct-angle question therefore splits cleanly.

For an **upper-bound/endpoint proof**, estimate either the raw canonical-correlation operator

\[
A_0^{-1/2}B_0C_0^{-1/2}
\]

or the trace (7) directly. No spatial theorem for `U_L` is logically required if the raw total-energy correlation can be bounded by other means.

For a **PF-328 obstruction/lower-bound proof**, first control the polar-unitary locality defect (10), or an equivalent concentration statement for `g_t`, on a positive-measure subset of the critical interval. Only after that step can finite-boundary versus escaping-boundary geometry be transported into the completed angle response.

This rules out a misleading intermediate target: proving merely that `\|A^{-1/2}\psi_t\|` is not small does not recover the geometric obstruction. The relevant property is where the unit-energy packet goes, not whether its coordinate norm survives.

## Prior-art and novelty audit

The abstract ingredients are classical. Unitary images of tight/Parseval frames remain tight, and canonical correlations are invariant under nonsingular coordinate changes. A targeted literature check found standard finite-frame treatments of unitary equivalence and standard canonical-correlation invariance; no new frame-theoretic or CCA theorem is claimed here.

The project-specific contribution is the exact identification of the **completed Prime-Flute packet family** as a unitary-rotated tight frame in raw total-energy coordinates, together with the polar-factor formula (9) and commutator identity (10). These sharpen the PF-329 gate: diagonal completion does not erase the PF-325 Hilbert--Schmidt accounting, but it can erase the raw spatial meaning needed to exploit PF-328 unless the polar unitary is shown to be local enough.

No additional external theorem is imported into the proof, so `SOURCES.md` does not acquire a new dependency.

## Boundaries and falsification

1. **No endpoint bound is proved.** Equations (6)--(7) are exact reformulations of the local direct-angle Hilbert--Schmidt mass.
2. **No packet obstruction is proved.** Tightness in total-energy coordinates does not imply spatial localization of `g_t`.
3. **No translation invariance is assumed.** Equation (10) identifies its failure exactly through the commutator of the polar unitary with physical translation.
4. **The PF-328 parity scales remain pre-angle data.** This finding does not promote them to completed-angle amplitudes.
5. **Finite sections are the safe statement.** Infinite-tail conclusions still require the finite-section-compatible limiting realization already used by PF-317--PF-329.
6. **The two arithmetic boundary regimes remain conditional at the completed level.** They become relevant only after locality/concentration of the rotated total-energy frame is established.

No scattering/determinant theorem, zeta-zero correspondence, critical-line result, or RH implication is established.
