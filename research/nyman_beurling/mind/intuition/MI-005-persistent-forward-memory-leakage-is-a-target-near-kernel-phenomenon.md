# MI-005 — Persistent forward-memory leakage is a target-bearing near-kernel phenomenon

**Evidence level:** supported by the exact one-cell recursion NB-063 and the spectral concentration theorem NB-064; no vanishing theorem for the canonical collective tail is claimed.

The late Nyman--Beurling quotient is not blocked by missing rank. NB-062--NB-063 show that the visible natural spaces form a full causal flag and that old visible information can enter the new logarithmic cell only through the finite-rank continuation map

\[
\Gamma_R:\mathcal G_R\to\mathcal X_R^\circ.
\]

For the distinguished target, the exact gain from enlarging the window is

\[
\delta_R^2-\delta_{R+1}^2
=\langle z_R,(I+\Gamma_R\Gamma_R^*)^{-1}z_R\rangle.
\]

NB-064 shows that if `\delta_R` converges to a positive limit, then this is much more rigid than repeated alignment with some finite-dimensional memory channel. Writing `p_R=P_{\mathcal G_R}J_Rh_*`, `u_R=p_R/\|p_R\|`, and `T_R=\Gamma_R^*\Gamma_R`, one has

\[
\langle p_R,T_R(I+T_R)^{-1}p_R\rangle\to0.
\]

Consequently, for every fixed `eta>0`, the target mass in singular values at least `eta` vanishes:

\[
\|E_R^{\ge\eta}u_R\|\to0.
\]

Equivalently, the normalized canonical target direction itself admits representatives `v_R` with

\[
\|u_R-v_R\|\to0,
\qquad
\|\Gamma_Rv_R\|\to0.
\]

Thus **bad conditioning matters only when the distinguished target occupies the bad singular directions**. A large operator norm, an abstract small singular value, or an infinite-dimensional defect sector does not by itself obstruct capture.

The useful contrapositive is correspondingly weak and target-specific. If along an unbounded sequence there exist fixed `eta,kappa>0` such that `u_R` keeps mass at least `kappa` in the `sigma(\Gamma_R)>=eta` sector, then the persistent collective tail is impossible. One does not need a uniform lower singular bound on the whole visible space.

**Boundary.** Near-kernel concentration is necessary, not sufficient. In the flat control `\Gamma_R=0`, every visible direction is a kernel direction while the actual tail still vanishes. The missing arithmetic theorem must therefore exclude near-kernel **tracking by the canonical target**, not merely prove that near-kernel vectors exist or control `\|\Gamma_R\|` globally.