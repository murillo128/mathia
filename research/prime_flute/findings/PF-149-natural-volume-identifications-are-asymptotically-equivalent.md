# PF-149 — the natural volume identifications are asymptotically equivalent

**Status:** `EXACT-DERIVED + LITERATURE-BACKED + NEGATIVE/BOUNDARY`. PF-125 already constructs a global marked bilipschitz comparison between the exact prime flute and the exact all-composite shift clone `p_n -> p_n+1`, with transported metric and volume density tending to the prime metric at infinity. The present finding closes a natural scattering-gauge loophole: for that fixed geometric marking, the two canonical `L^2` identifications — the trivial identity map between the two measure spaces and the density-corrected unitary map — are asymptotically equivalent in Kato's sense. Therefore, whenever wave operators exist for either of these two natural identifications, they exist for the other and are equal. No wave-operator existence, global squared-resolvent trace class, resonance equality, determinant identity, or RH consequence is claimed.

## Claim

Let `X` be the exact prime flute, let `F:X -> X_+` be the PF-125 marked bilipschitz comparison with the exact all-composite shift clone, and put

\[
g:=g_X,
\qquad
h:=F^*g_{X_+}.
\]

Write

\[
d\mu_h=\rho\,d\mu_g.
\tag{1}
\]

PF-125 gives global quasi-isometry and, in the ordinary Fréchet sense at infinity,

\[
\rho(x)\longrightarrow1.
\tag{2}
\]

Hence `rho` and `rho^{-1}` are bounded. Consider the two standard identifications

\[
\widetilde J:L^2(X,\mu_g)\longrightarrow L^2(X,\mu_h),
\qquad
\widetilde J\psi=\psi,
\tag{3}
\]

and

\[
J:L^2(X,\mu_g)\longrightarrow L^2(X,\mu_h),
\qquad
J\psi=\rho^{-1/2}\psi,
\tag{4}
\]

where `J` is unitary. Let `H_g=\Delta_g` be the nonnegative self-adjoint Laplacian and `\pi_{ac}` its absolutely-continuous projection. Then

\[
\boxed{
\operatorname*{s-lim}_{t\to\pm\infty}
(\widetilde J-J)e^{-itH_g}\pi_{ac}=0.
}
\tag{5}
\]

Thus `J` and `\widetilde J` are asymptotically `H_g`-equivalent in Kato's sense. Consequently,

\[
\boxed{
W_\pm(H_h,H_g;J)
=
W_\pm(H_h,H_g;\widetilde J)
}
\tag{6}
\]

whenever either side exists. In particular, existence and completeness are the same for the two natural identifications, and if the wave operators are complete then the scattering operator obtained from them is the same.

The conclusion is stronger than merely saying that both identifications are boundedly comparable. Their difference is dynamically invisible on every absolutely-continuous state in the scattering limit.

## 1. PF-125 turns the identification difference into a vanishing multiplier

Set

\[
f:=1-\rho^{-1/2}.
\tag{7}
\]

Then

\[
\widetilde J-J=M_f,
\tag{8}
\]

viewed as a bounded multiplication operator from `L^2(mu_g)` to `L^2(mu_h)`. Because the two metrics are globally quasi-isometric, the two measures have uniformly comparable densities. Equation (2) gives

\[
\boxed{f(x)\to0\quad(x\to\infty).}
\tag{9}
\]

No summability rate is needed here. In particular, this step does **not** require the still-open Güneysu--Thalmaier weighted `L^1` scattering integral from the accepted wave-operator clue.

The exact deep-cusp matching built into PF-125 is important indirectly: it is what makes (2) a genuine global statement along every escaping sequence rather than only a pants-index asymptotic that could fail inside a fixed cusp.

## 2. Every bounded-energy localization of `M_f` is compact

Fix a bounded Borel interval `I` and write

\[
E_I:=\mathbf 1_I(H_g).
\]

We claim

\[
\boxed{M_fE_I\text{ is compact from }L^2(\mu_g)\text{ to }L^2(\mu_h).}
\tag{10}
\]

Choose a compact exhaustion `K_m` of `X`. Split

\[
M_fE_I
=M_{f\mathbf 1_{K_m}}E_I
+M_{f\mathbf 1_{X\setminus K_m}}E_I.
\tag{11}
\]

For the compactly supported term, fix `s>0`. Local parabolic/elliptic regularity for the smooth hyperbolic metric `g` implies that

\[
M_{\mathbf 1_{K_m}}e^{-sH_g}
\]

is compact (indeed Hilbert--Schmidt by the standard heat-kernel/Grothendieck factorization used in geometric scattering theory). Since `e^{sH_g}E_I` is bounded for bounded `I`,

\[
M_{f\mathbf 1_{K_m}}E_I
=
M_fM_{\mathbf 1_{K_m}}e^{-sH_g}
\bigl(e^{sH_g}E_I\bigr)
\tag{12}
\]

is compact.

For the tail term, quasi-isometry gives a constant `C` such that

\[
\|M_{f\mathbf 1_{X\setminus K_m}}E_I\|_{L^2(\mu_g)\to L^2(\mu_h)}
\le
C\sup_{X\setminus K_m}|f|.
\tag{13}
\]

By (9), the right-hand side tends to zero. Hence (10) follows because `M_fE_I` is a norm limit of compact operators.

This argument is insensitive to the piecewise-smooth nature of the transported metric in PF-125: compact localization is taken with respect to the source hyperbolic Laplacian `H_g`, while the target measure enters only through the globally bounded density ratio.

## 3. Compact bounded-energy localizations imply Kato asymptotic equivalence

Let `\psi` lie in the absolutely-continuous subspace of `H_g`. For a large bounded spectral interval `I`, decompose

\[
\psi=E_I\psi+(1-E_I)\psi.
\]

The second term is uniformly small after applying `M_f e^{-itH_g}` because `M_f` is bounded and `E_I\psi -> \psi` in norm as `I` exhausts the real line.

For the first term, `M_fE_I` is compact by (10). The absolutely-continuous spectral theorem/Riemann--Lebesgue argument gives weak escape of `e^{-itH_g}E_I\psi`; applying a compact operator turns this into norm convergence to zero. Therefore

\[
\|M_fe^{-itH_g}\psi\|_{L^2(\mu_h)}\longrightarrow0,
\qquad t\to\pm\infty,
\]

which is exactly (5).

Kato's two-Hilbert-space scattering theory then gives (6): asymptotically equivalent identification operators define the same wave operators whenever one of the limits exists.

## 4. Prior art and novelty audit

The general notion and invariance statement are classical. Kato's *Wave operators and unitary equivalence* (Pacific J. Math. 15 (1965), 171--180, DOI `10.2140/pjm.1965.15.171`) is the foundational source for asymptotic equivalence of identifications in two-Hilbert-space scattering.

A directly relevant modern source is Batu Güneysu, *Asymptotic equivalence of identification operators in geometric scattering theory*, Documenta Mathematica 29 (2024), 1367--1379, DOI `10.4171/DM/968`. Güneysu studies precisely the pair consisting of the trivial identification and the density-corrected unitary identification. His Theorem 3.1 proves equality of the wave operators under a heat-kernel weighted square-integrability criterion for the density mismatch, and Theorem 4.1 shows that the Güneysu--Thalmaier geometric scattering criterion implies this identification equivalence on complete quasi-isometric Riemannian manifolds.

Accordingly, **no new general scattering theorem is claimed here**. The project-specific content is that PF-125 already supplies a simpler route for this particular pair: the density ratio tends to `1` at infinity, while the prime Laplacian is locally compact after bounded spectral localization. The compact-exhaustion argument above therefore proves asymptotic equivalence without first solving the stronger global weighted metric-integrability gate required for wave-operator existence.

Directed searches found the expected Kato/Güneysu identification theory and the existing Güneysu--Thalmaier/Hempel--Post--Weder geometric scattering literature, but no additional arithmetic or infinite-flute mechanism. The result is best classified as a literature-backed project specialization that removes a gauge ambiguity, not as novel scattering theory.

## 5. Boundaries and adversarial checks

This finding does **not** establish wave operators. Equation (6) says only that the two canonical volume identifications rise or fall together; the accepted `CLUE-shift-clone-wave-operator-equivalence.md` still requires either a globally coherent Güneysu--Thalmaier metric comparison or a global trace-class squared-resolvent comparison.

It also does not identify arbitrary markings. If one replaces the PF-125 geometric marking `F` by a genuinely different asymptotic diffeomorphism, the resulting transported Laplacian and identification operator must be audited separately. The present argument closes only the natural choice between `psi -> psi` and `psi -> rho^{-1/2}psi` **after the marking is fixed**.

Nor does asymptotic equivalence imply equality of resonances, discrete spectra, Selberg/Ruelle objects, relative determinants, or meromorphic scattering matrices. It only removes the possibility that a future difference between the two natural wave-operator constructions is an artifact of whether the volume-density correction was inserted into the `L^2` identification.

Finally, the proof does not need `M_f` itself to be compact. On a noncompact surface multiplication by a nonzero decaying function need not be compact on `L^2`. The required object is the bounded-energy localization `M_fE_I`; the Laplacian smoothing/local compactness is essential in (12).

## Consequence for the prime-flute program

For the exact prime/shift pair under the already-constructed PF-125 marking, the unresolved scattering problem can be stated without a natural-volume-identification caveat:

\[
\boxed{
\text{trivial and density-unitary }L^2\text{ identifications have the same wave operators.}
}
\]

Thus any surviving obstruction to complete relative wave operators must come from the actual global geometry/operator perturbation — body/interface assembly, true thin channels, or failure of a sufficient scattering/Schatten gate — rather than from this elementary `L^2` gauge choice. Conversely, if either current route eventually proves complete wave operators, their absolutely-continuous scattering equivalence is already canonical with respect to these two standard volume identifications.