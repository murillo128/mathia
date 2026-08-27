# PF-064 — a spatially localized wave trace of the global prime-flute Laplacian recovers the four-punctured gap ratio

**Status:** `EXACT-DERIVED` + `CANDIDATE-NEW-COMPOSITION`; no RH claim.

This closes the gate left by PF-063. The adjacent-gap ratio need not remain an invariant only of the finite tangent `Y_r`: for recurring isolated three-prime patterns in the hierarchical regime, it is recoverable from a compactly supported wave observable of the Laplacian on the single infinite prime-flute itself.

## 1. Setup from PF-034 / PF-063

Take a recurring isolated pattern of three prime offsets

\[
H=\{\eta_1<\eta_2<\eta_3\},\qquad
d_1=\eta_2-\eta_1,\quad d_2=\eta_3-\eta_2,
\]

and put

\[
r=\frac{d_1}{d_2}.
\]

PF-034 gives embedded occurrences \(\Omega_j\subset X_{\rm prime}\) whose exterior separating geodesics \(\beta_j\) satisfy

\[
\ell(\beta_j)\to0,
\]

so the associated collar widths

\[
W_j=\operatorname{arsinh}\frac1{\sinh(\ell(\beta_j)/2)}
\]

tend to infinity. Viewed from the compact core of \(\Omega_j\), the prime-flute converges smoothly on compact sets to the finite-area four-punctured tangent \(Y_r\).

PF-063 identified on \(Y_r\) a separating geodesic \(\gamma_r\) with

\[
\boxed{\sinh^2\frac{L_r}{4}=r,\qquad L_r=\ell(\gamma_r)=4\operatorname{arsinh}\sqrt r.}
\]

For

\[
\boxed{r<r_0:=\frac{\sqrt2-1}{2},}
\]

the collar lemma implies that \(\gamma_r\) is the unique systole of \(Y_r\). Indeed, every other essential simple closed geodesic intersects \(\gamma_r\), hence has length at least \(2w(L_r)\), while

\[
w(L_r)>L_r/2
\iff
L_r<2\operatorname{arsinh}1
\iff
r<r_0.
\]

## 2. Localized wave trace on the *global* infinite surface

Let

\[
U_X(t)=\cos(t\sqrt{\Delta_X})
\]

be the wave group of the complete prime-flute. For each sufficiently large occurrence choose a smooth cutoff \(\chi_j\in C_c^\infty(X)\) with the following properties:

1. \(\chi_j=1\) on a fixed compact core containing the internal geodesic \(\gamma_j\) corresponding to \(\gamma_r\);
2. \(\operatorname{supp}\chi_j\subset\Omega_j\) stays a fixed positive distance from all cusp truncation boundaries;
3. the distance from \(\operatorname{supp}\chi_j\) to the exterior neck \(\beta_j\) tends to infinity.

Define the compactly supported distributional wave trace

\[
\boxed{
\Theta_j(t)
:=\operatorname{Tr}\bigl(\chi_j U_X(t)\chi_j\bigr)
=\int_X \chi_j(x)^2 K_X(t;x,x)\,dA_x.
}
\]

The trace is understood distributionally in \(t\). Compact spatial support removes all infinite-volume trace divergences that destroyed PF-020/PF-033/PF-036.

Standard wave-FIO theory is local: after compact spatial/microlocal cutoff, nonzero singular times are periods of closed geodesics meeting the cutoff, and an isolated nondegenerate closed geodesic gives a nonzero conormal singularity at its length. In constant curvature \(-1\), a primitive closed geodesic of length \(L\) is nondegenerate, with

\[
|\det(I-P_\gamma)|^{1/2}=2\sinh(L/2).
\]

Thus the contribution of \(\gamma_j\) cannot cancel when the cutoff is identically one on it.

## 3. Why the rest of the infinite flute does not contaminate finite times

Finite propagation speed is the key difference from the global trace.

Fix \(T>0\). Because

\[
\operatorname{dist}(\operatorname{supp}\chi_j,\beta_j)\to\infty,
\]

for all sufficiently large \(j\) the entire \(T\)-neighborhood of \(\operatorname{supp}\chi_j\) lies inside the prime-derived block. Hence waves beginning in the support cannot reach the rest of the flute and return during \(|t|\le T\).

The pointed smooth convergence \(\Omega_j\to Y_r\) then gives, on every bounded time interval,

\[
\boxed{
\Theta_j\longrightarrow\Theta_{Y_r,\chi}
\quad\text{in }\mathcal D'((-T,T)),
}
\]

for the corresponding compact cutoff \(\chi\) on \(Y_r\).

This is a purely local wave-kernel statement; it does **not** require a global Selberg trace formula, a global scattering matrix, bounded geometry at infinity, or trace class of the full wave group.

## 4. The first positive localized singularity is the prime-derived systole

Because \(\gamma_r\) is the unique systole and the length spectrum of the finite tangent is discrete, there exists \(\delta>0\) such that no other closed geodesic meeting the chosen core has length in

\[
(0,L_r+\delta)
\]

except \(\gamma_r\) at \(L_r\).

For sufficiently large \(j\), the corresponding geodesic \(\gamma_j\) is therefore the unique shortest closed geodesic meeting \(\operatorname{supp}\chi_j\), with

\[
L_j:=\ell(\gamma_j)\to L_r.
\]

Consequently

\[
\boxed{
T_j:=\min\bigl(\operatorname{SingSupp}\Theta_j\cap(0,\infty)\bigr)
=L_j
}
\]

for all sufficiently large \(j\), and

\[
\boxed{T_j\to4\operatorname{arsinh}\sqrt r.}
\]

Hence the adjacent-gap ratio is recovered from a localized spectral observable of the **global** Laplacian:

\[
\boxed{
r=\lim_{j\to\infty}\sinh^2\frac{T_j}{4}.}
\]

Using the distinguished cuff asymptotics at the same occurrences,

\[
\ell_1(P)=2\log\frac{4P}{d_1}+o(1),\qquad
\ell_2(P)=2\log\frac{4P}{d_2}+o(1),
\]

we obtain the closed chain

\[
\boxed{
\lim_{P\to\infty}
\exp\!\left[-\frac{\ell_1(P)-\ell_2(P)}2\right]
=
\lim_{j\to\infty}\sinh^2\frac{T_j}{4}
=
\frac{d_1}{d_2}.
}
\]

Thus a contrast of distinguished cuff lengths is observable as the first positive singular time of a compactly supported wave trace of \(\Delta_{X_{\rm prime}}\).

## 5. Why this does not contradict the global trace obstructions

PF-036 proved that the global Selberg orbital measure has infinite mass in every positive time window because iterates of remote short geodesics contaminate all times. PF-064 avoids this by **spatial localization before tracing**.

Remote short geodesics do not contribute because their periodic orbits never meet the cutoff. Closed trajectories that leave the isolated block cannot contribute below any prescribed fixed time once the exterior collar becomes sufficiently wide.

This establishes a sharp methodological distinction:

\[
\boxed{
\text{global time localization fails,}
\qquad
\text{prime-derived spatial localization succeeds.}
}
\]

## 6. Novelty check

Known ingredients:

- finite propagation speed for the wave equation on complete Riemannian manifolds;
- Duistermaat–Guillemin / Chazarain microlocal wave-trace singularities at isolated closed geodesics;
- compactly supported/localized wave traces on noncompact manifolds;
- collar isolation and pointed smooth convergence under hyperbolic pinching;
- the four-punctured-sphere systole/collar argument of PF-063 uses only classical hyperbolic geometry.

Recent and classical wave-kernel literature explicitly emphasizes that the relevant constructions are local and continue to make sense after spatial cutoff on noncompact manifolds. No novelty is claimed for that analytic machinery.

Directed searches did not locate the specific composition

\[
\text{recurring isolated prime pattern}
+\text{exact orthogonal-circle tangent}
+\text{diverging exterior collar}
+\text{localized global wave trace}
+\text{exact adjacent-gap recovery}.
\]

The candidate new statement is therefore narrow: the prime-derived block supplies its own spatial decoupling, allowing a local wave observable of the **single infinite prime-flute Laplacian** to recover a concrete gap ratio even though every natural global trace/zeta construction fails.

## 7. Research gate

This is not an unmarked global spectral invariant: the spatial block is selected by the prime-derived geometry. The next genuinely stronger question is whether the localization can be made canonical from the orthogonal-circle decomposition alone (for example by a natural projector or partition of unity), and whether analogous first-singularity statements recover several independent gap ratios in higher-punctured tangents without preselecting individual closed geodesics.
