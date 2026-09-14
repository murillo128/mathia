# RE-127 — hiding a strong subedge atom forces a logarithmically comparable cancelling-phase companion

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + NONISOLATED-EDGE + SPECTRAL-LOCALIZATION + PHASE-SECTOR + LOCAL-ZERO-COUNT + CANCELLING-PHASE-NECESSITY + CA-PHASE-TRANSFER + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

Assume the attained finite-edge branch and notation of `RE-121`--`RE-126`,

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad
\frac12<\sigma_0<\Theta,
\]

and fix `K>=0`, `A>0`, and `0<eta<1`. For a positive-ordinate subedge zero

\[
\rho=\beta+i\gamma,
\qquad
\sigma_0\le\beta<\Theta,
\qquad
\gamma>0,
\]

write

\[
a_{\rho,K}(u)
:=
 e^{-(\Theta-\beta)u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}
\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right]
\tag{1}
\]

and

\[
\mathcal S_K(u)
=
2\Re
\sum_{\substack{\zeta(\rho)=0\\
\sigma_0\le\Re\rho<\Theta\\
\Im\rho>0}}
 a_{\rho,K}(u)e^{i\gamma u}.
\tag{2}
\]

Let `rho_0=beta_0+i gamma_0` satisfy

\[
|a_{\rho_0,K}(U)|\ge cU^{-A}
\tag{3}
\]

for fixed `c>0`, and let `c_*>0` be the reinforcing inner-radius constant from `RE-125`. Define the reciprocal annulus

\[
\mathcal A_\eta(\rho_0;U)
:=
\left\{
\rho\ne\rho_0:
\sigma_0\le\Re\rho<\Theta,
\ \Im\rho>0,
\ \frac{c_*}{U}<|\Im\rho-\gamma_0|\le U^{-1+\eta}
\right\}.
\tag{4}
\]

Then there are constants `epsilon_*>0`, `c_1>0`, and `U_0` depending only on the fixed parameters such that, whenever `U>=U_0` and

\[
\sup_{|u-U|\le U^{1-\eta/2}}
|\mathcal S_K(u)|
\le
\epsilon_*|a_{\rho_0,K}(U)|,
\tag{5}
\]

there exists a zero

\[
\rho_1=\beta_1+i\gamma_1
\in\mathcal A_\eta(\rho_0;U)
\tag{6}
\]

whose **signed center-phase projection is genuinely cancelling**:

\[
\boxed{
-\Re\!\left(
 a_{\rho_1,K}(U)e^{i(\gamma_1-\gamma_0)U}
\right)
\ge
c_1\frac{|a_{\rho_0,K}(U)|}{\log U}.
}
\tag{7}
\]

In particular,

\[
|a_{\rho_1,K}(U)|
\ge
c_1\frac{|a_{\rho_0,K}(U)|}{\log U}
\gg
\frac{U^{-A}}{\log U},
\tag{8}
\]

so `RE-126`'s logarithmically comparable companion follows, but now with the missing sign/phase information.

Let

\[
\vartheta_1(U):=\arg a_{\rho_1,K}(U)
\]

on the principal branch. Equation (7) implies

\[
\boxed{
\cos\!\left((\gamma_1-\gamma_0)U+\vartheta_1(U)\right)<0,
}
\tag{9}
\]

and quantitatively

\[
\cos\!\left((\gamma_1-\gamma_0)U+\vartheta_1(U)\right)
\le
-c_1\frac{|a_{\rho_0,K}(U)|}
{|a_{\rho_1,K}(U)|\log U}.
\tag{10}
\]

The coefficient-sector calculation of `RE-125` gives

\[
-\frac{C_K}{U}
\le
\vartheta_1(U)
\le
\omega_*+\frac{C_K}{U},
\qquad
0<\omega_*<\frac\pi2,
\tag{11}
\]

where

\[
\omega_*
=
\arctan\!\left(
\max_{\sigma_0\le\beta\le\Theta}
\frac{2\beta-1}{2\sqrt{\beta(1-\beta)}}
\right).
\]

Hence the scaled signed gap itself must enter a fixed cancellation arc. Modulo `2pi`,

\[
\boxed{
(\gamma_1-\gamma_0)U
\in
\left[
\frac\pi2-\omega_*-o(1),
\frac{3\pi}{2}+o(1)
\right]
\pmod{2\pi}.
}
\tag{12}
\]

Thus a hidden strong atom does not merely require a very close near-edge companion. At least one logarithmically comparable companion must already point into the **opposite half-plane after target-frequency demodulation at the central phase `U`**.

As in `RE-126`, the companion also satisfies

\[
\Theta-\beta_1
\le
\frac{A\log U+\log\log U+O(1)}{U},
\qquad
\gamma_1\ll_A U^{A/2},
\tag{13}
\]

and

\[
\frac{c_*}{U}
<
|\gamma_1-\gamma_0|
\le
U^{-1+\eta}.
\tag{14}
\]

Along an unbounded hidden-atom sequence,

\[
|\gamma_1-\gamma_0|\log(2+\gamma_0)\to0.
\tag{15}
\]

When `A<K+1`, absence of such a cancelling-phase companion forces the continuum excursion to survive, and `RE-123` transfers it to actual regular CA states. The separate diffuse-cloud branch, where no individual coefficient reaches (3), remains open.

## 1. The matched filter preserves the sign of the local positive-frequency packet

Use the `RE-125` cutoff with

\[
0\le\widehat\phi\le1,
\qquad
\widehat\phi(\xi)=1\quad(|\xi|\le1/2),
\qquad
\widehat\phi(\xi)=0\quad(|\xi|\ge1),
\tag{16}
\]

and set

\[
L=U^{1-\eta},
\qquad
H=U^{1-\eta/2},
\qquad
\phi_L(t)=L^{-1}\phi(t/L).
\tag{17}
\]

For the target-demodulated average

\[
I_{\rho_0}(U)
:=
\int_{1-U}^{\infty}
\phi_L(t)\mathcal S_K(U+t)
 e^{-i\gamma_0(U+t)}\,dt,
\tag{18}
\]

the horizontal split, amplitude-freezing estimates, physical-tail control, and negative-frequency separation already proved in `RE-124`--`RE-125` give

\[
I_{\rho_0}(U)
=
\sum_{|\gamma-\gamma_0|\le U^{-1+\eta}}
 w_\rho(U)\,
 a_{\rho,K}(U)e^{i(\gamma-\gamma_0)U}
+o(U^{-A}),
\tag{19}
\]

where

\[
w_\rho(U)
:=
\widehat\phi\!\left(L(\gamma-\gamma_0)\right)
\in[0,1].
\tag{20}
\]

The target has `w_(rho_0)=1`. Moreover, throughout the reinforcing inner ball

\[
|\gamma-\gamma_0|\le\frac{c_*}{U},
\tag{21}
\]

we have `L|gamma-gamma_0|<=c_*U^-eta<1/2`, so `w_rho=1` for all sufficiently large `U`.

The phase-sector result of `RE-125` therefore supplies a fixed `q_*>0` such that every inner contribution, including the target itself, obeys

\[
\Re\!\left(
 a_{\rho,K}(U)e^{i(\gamma-\gamma_0)U}
\right)
\ge
q_*|a_{\rho,K}(U)|.
\tag{22}
\]

This is the key extra information that was discarded when `RE-126` pigeonholed only absolute annular mass.

## 2. A hidden target forces negative projected mass in the annulus

The observation-window hypothesis (5) and Schwartz-tail estimate give

\[
|I_{\rho_0}(U)|
\le
\|\phi\|_1\epsilon_*|a_{\rho_0,K}(U)|
+o(U^{-A}).
\tag{23}
\]

Choose `epsilon_*` sufficiently small that

\[
\|\phi\|_1\epsilon_*<\frac{q_*}{4}.
\tag{24}
\]

Since (3) makes `o(U^-A)=o(|a_(rho_0,K)(U)|)`, equations (19), (22), and (23) imply, for all sufficiently large `U`,

\[
\Re
\sum_{\rho\in\mathcal A_\eta(\rho_0;U)}
 w_\rho(U)\,
 a_{\rho,K}(U)e^{i(\gamma-\gamma_0)U}
\le
-\frac{q_*}{2}|a_{\rho_0,K}(U)|.
\tag{25}
\]

Only annular atoms with negative real projection can contribute to the negative side. Define

\[
\mathcal N_\eta(\rho_0;U)
:=
\left\{
\rho\in\mathcal A_\eta(\rho_0;U):
\Re\!\left(
 a_{\rho,K}(U)e^{i(\gamma-\gamma_0)U}
\right)<0
\right\}.
\tag{26}
\]

Because `0<=w_rho<=1`, equation (25) yields

\[
\sum_{\rho\in\mathcal N_\eta(\rho_0;U)}
-\Re\!\left(
 a_{\rho,K}(U)e^{i(\gamma-\gamma_0)U}
\right)
\ge
\frac{q_*}{2}|a_{\rho_0,K}(U)|.
\tag{27}
\]

Thus the annulus is not merely required to carry comparable absolute mass. It must carry comparable **negative signed projection** against the common right-half-plane source sector.

## 3. Local zero count turns signed mass into one cancelling companion

`RE-126` already established that the annulus (4) contains only

\[
\#\mathcal A_\eta(\rho_0;U)
\ll_A\log U
\tag{28}
\]

zeros, counted with multiplicity. Pigeonholing the signed mass (27) through (28) produces some `rho_1` satisfying (7). Since the annulus excludes `|gamma_1-gamma_0|<=c_*/U`, the companion has distinct ordinate and cannot be supplied by multiplicity of the target.

Taking absolute values in (7) gives (8), so the horizontal and polynomial-height localization (13), the shrinking annular spacing (14), and the vanishing normalized gap (15) follow exactly as in `RE-126`.

Writing

\[
a_{\rho_1,K}(U)
=|a_{\rho_1,K}(U)|e^{i\vartheta_1(U)}
\]

turns (7) into (9)--(10). Finally, `RE-125` proves

\[
a_{\rho,K}(U)
=
\frac{e^{-(\Theta-\beta)U}}{\rho(1-\rho)}
\left(1+O_K(U^{-1})\right)
\tag{29}
\]

uniformly on the fixed strip, while the leading coefficient has argument in `[0,omega_*]`. Hence (11) follows. The left-half-plane condition (9) then gives the coefficient-free cancellation arc (12).

The arc in (12) is intentionally broad. The theorem forces opposition in one real projection, not a nearly antipodal two-mode configuration.

## 4. CA consequence and the sharper strong-atom frontier

The contrapositive is now phase-sensitive. If every zero in the reciprocal annulus either has

\[
-\Re\!\left(
 a_{\rho,K}(U)e^{i(\gamma-\gamma_0)U}
\right)
<
c_1\frac{|a_{\rho_0,K}(U)|}{\log U}
\tag{30}
\]

or has nonnegative projection, then (5) cannot hold. Therefore

\[
\sup_{|u-U|\le U^{1-\eta/2}}
|\mathcal S_K(u)|
\gg
|a_{\rho_0,K}(U)|
\gg U^{-A}.
\tag{31}
\]

When `A<K+1`, `RE-123` samples this continuum excursion on the superalgebraically fine regular-CA phase mesh, so the same algebraic anomaly appears at an actual regular CA state.

`RE-126` left the strong-atom escape as a near-edge pair with vanishing normalized gap **plus an unspecified phase relation**. The phase relation is no longer unspecified: at least one logarithmically comparable companion must have negative target-demodulated center projection, equivalently its scaled signed gap plus the source-coefficient phase must lie in the left half-plane. What remains open is whether an attained off-critical edge can support infinitely many such near-edge pairs with enough negative projection to suppress the residual, and the genuinely different diffuse-cloud regime.

## 5. Representation and adversarial audit

No new coordinate is introduced. The theorem keeps the same absolutely convergent subedge packet, the same Robin/CA coefficient, and the same matched filter as `RE-124`--`RE-126`. The only new step is to preserve the **sign** of the filtered real projection instead of replacing the annular contribution immediately by its absolute mass.

The main adversarial checks are as follows. The time-domain cutoff `phi` need not be nonnegative; the argument uses only `0<=hat(phi)<=1`, which makes every surviving frozen-frequency weight real and nonnegative. The global amplitude-freezing and physical-tail errors are already `o(U^-A)`, hence `o(|a_(rho_0,K)(U)|)` under (3), so they cannot manufacture the negative mass in (27). The conjugate negative-frequency packet remains separated by compact Fourier support exactly as in `RE-125`.

The conclusion is deliberately about the phase at the central point `U`. It does not assert that the chosen companion remains oppositely phased over the whole observation window, nor that this one companion alone cancels the target. Since `|a_(rho_1,K)(U)|` can be much larger than the lower bound (8), equation (10) does **not** give a fixed angular margin inside the left half-plane; the cosine may approach zero. Accordingly, (12) is a half-plane arc, not an antipodal `pi+o(1)` law. Multiplicity still cannot serve as the companion because equal ordinates lie inside the reinforcing ball.

A separate adversarial reconstruction of the filter sign, inner-sector positivity, shell decomposition, local-count pigeonhole, phase conversion, multiplicity boundary, and CA transfer found no material objection. No `.review.md` sidecar is opened.

## 6. Prior-art boundary

The nearest modern prior art remains the literature on unusually close or vertically isolated zeta zeros. Bui--Goldston--Milinovich--Montgomery, *Small gaps and small spacings between zeta zeros* (Acta Arithmetica **210** (2023), 133--153, DOI `10.4064/aa220731-15-2`), proves small-spacing phenomena but does not attach the Robin/CA coefficient or the phase `U` appearing here. Maynard--Pratt, *Half-Isolated Zeros and Zero-Density Estimates* (International Mathematics Research Notices **2024** (19), 12978--13014, DOI `10.1093/imrn/rnae191`), develops zero detection sensitive to vertical isolation, again without this residual-phase implication.

No new external theorem is load-bearing. The local zero-count input was already anchored and used in `RE-126`; the new signed-projection step is elementary once the `RE-125` positive coefficient sector and nonnegative Fourier weights are retained. A targeted search by close-zero spacing, vertical isolation, explicit-formula cancellation, and phase localization found no prior result asserting this finite-edge Robin/CA cancelling-phase necessity. The novelty claim is therefore restricted to this line-specific splice.

## 7. Research effect

The strong-atom obstruction is now more rigid than a small-gap condition. Hiding an algebraically strong subedge atom requires a second near-edge atom that is simultaneously logarithmically comparable, vanishingly close on the normalized zero-spacing scale, and in the correct left-half-plane phase sector at the relevant CA height.

This does not rule out the configuration. It converts the remaining strong-atom question into a joint **zero-pair geometry plus scaled phase** problem rather than an unspecified cancellation possibility. The diffuse branch remains logically separate because it never supplies the individually strong target needed for the matched-filter localization.