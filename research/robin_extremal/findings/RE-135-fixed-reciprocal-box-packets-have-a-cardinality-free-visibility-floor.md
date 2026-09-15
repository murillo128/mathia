# RE-135 — fixed reciprocal-box packets have a cardinality-free visibility floor

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + RECIPROCAL-BOX + CARDINALITY-FREE-VISIBILITY + MACROSCOPIC-WINDOW + REAL-PACKET-OBSERVABILITY + TIGHTNESS-OBSTRUCTION + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-134` proves a fixed-relative visibility floor for a Robin subedge packet when both its scaled reciprocal-box diameter and its cardinality are bounded. The live zero-counting clue asked whether actual-zeta zero counts could supply a growing occupancy budget `B(U)` for that theorem. The answer is stronger than that route suggests: **inside one fixed reciprocal box the occupancy bound is unnecessary.**

The Robin coefficient law aligns every atom in such a box to the same orientation up to `O(U^-1)`. After division by the number of atoms, an arbitrary finite packet is therefore the Fourier--Laplace transform of an empirical probability measure on one fixed compact set, plus a uniform `O(U^-1)` perturbation. Probability measures on that compact set form a compact family, and none of their transforms can vanish on a real interval because the transform equals `1` at the origin. This gives a visibility floor independent of local cardinality.

Consequently the concentration--compactness alternative of `RE-134` sharpens: **growing occupancy inside a fixed `R/U` box is not by itself an escape mechanism. Uniform hiding forces order-one cancellation to escape every fixed scaled reciprocal box.** The growing scaled diameter in the formal control of `RE-133` is therefore load-bearing, whereas its growing cardinality alone is not.

Fix

\[
\frac12<\sigma_0<\Theta<1,
\qquad K\ge0,
\qquad 0<\kappa<\frac12,
\qquad R>0,
\qquad \gamma_*>0.
\tag{1}
\]

For a positive-ordinate strict-subedge coordinate

\[
\rho=\beta+i\gamma,
\qquad
\sigma_0\le\beta<\Theta,
\tag{2}
\]

use the same finite-order coefficient law as `RE-134`,

\[
a_{\rho,K}(u)
:=e^{-(\Theta-\beta)u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right].
\tag{3}
\]

For every sufficiently large `U`, choose a target

\[
\rho_0=\beta_0+i\gamma_0,
\qquad
\gamma_0\ge\gamma_*,
\tag{4}
\]

and let `C_U` be **any finite nonempty multiset**, counted with multiplicity, containing `rho_0` and satisfying

\[
|\beta-\beta_0|\le\frac RU,
\qquad
|\gamma-\gamma_0|\le\frac RU
\quad(\rho\in C_U).
\tag{5}
\]

There is no cardinality restriction. Write

\[
N_U:=\#C_U
\tag{6}
\]

and define the real local packet

\[
\mathcal S_{C_U,K}(u)
:=2\Re\sum_{\rho\in C_U}
a_{\rho,K}(u)e^{i\gamma u}.
\tag{7}
\]

Then there exist constants `c_0>0` and `U_0`, depending only on the fixed parameters in (1) and on `gamma_*`, such that for every `U>=U_0`,

\[
\boxed{
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C_U,K}(u)|
\ge
c_0 N_U\,|a_{\rho_0,K}(U)|.
}
\tag{8}
\]

In particular,

\[
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_{C_U,K}(u)|
\ge
c_0|a_{\rho_0,K}(U)|
\tag{9}
\]

with a constant completely independent of `N_U`.

No simplicity assumption is needed in this packet model. Coincident coordinates simply contribute repeated equal atoms to the empirical measure below.

## 1. Normalize the arbitrary packet by its cardinality

Put

\[
d_\rho:=\frac1{\rho(1-\rho)},
\qquad
I_\kappa:=[1-\kappa,1],
\qquad
u=Ux.
\tag{10}
\]

Exactly as in `RE-134`, uniformly for `x in I_kappa` and every coordinate satisfying (5),

\[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}\frac{(-1)^k k!}{(Ux)^k(1-\rho)^{k+1}}
=
d_\rho\left(1+O_K(U^{-1})\right),
\tag{11}
\]

and

\[
\frac{d_\rho}{d_{\rho_0}}
=1+O_{R,\sigma_0,\Theta,\gamma_*}(U^{-1}).
\tag{12}
\]

The constants in (11)--(12) are per-atom uniform and do not depend on `N_U`.

Introduce the scaled offsets

\[
\lambda_{\rho,U}
:=U\bigl((\beta-\beta_0)+i(\gamma-\gamma_0)\bigr),
\tag{13}
\]

so

\[
\lambda_{\rho,U}\in
\mathcal K_R
:=\{z\in\mathbb C:|\Re z|\le R,\ |\Im z|\le R\}.
\tag{14}
\]

After factoring the target damping and carrier, divide the positive-frequency packet by `N_U`:

\[
\frac1{N_U}
\sum_{\rho\in C_U}
a_{\rho,K}(Ux)e^{i\gamma Ux}
=
e^{-(\Theta-\beta_0)Ux}
d_{\rho_0}e^{i\gamma_0Ux}
\bigl(Q_U(x)+E_U(x)\bigr),
\tag{15}
\]

where

\[
Q_U(x)
:=\frac1{N_U}
\sum_{\rho\in C_U}e^{\lambda_{\rho,U}x}
\tag{16}
\]

and, crucially,

\[
\boxed{
\sup_{x\in I_\kappa}|E_U(x)|
\ll_{R,K,\sigma_0,\Theta,\gamma_*}U^{-1}
}
\tag{17}
\]

**with no factor `N_U`.** Each summand has a relative `O(U^-1)` coefficient error, and averaging by `N_U` averages those errors as well.

Thus the cardinality issue in `RE-134` is reduced to understanding the normalized functions `Q_U`.

## 2. Empirical measures compactify every cardinality at once

Associate to the packet the empirical probability measure

\[
\mu_U
:=\frac1{N_U}
\sum_{\rho\in C_U}\delta_{\lambda_{\rho,U}}
\tag{18}
\]

on the fixed compact square `K_R`. Then

\[
Q_U(x)
=
\int_{\mathcal K_R}e^{\lambda x}\,d\mu_U(\lambda).
\tag{19}
\]

For an arbitrary Borel probability measure `mu` on `K_R`, define

\[
F_\mu(z)
:=\int_{\mathcal K_R}e^{\lambda z}\,d\mu(\lambda).
\tag{20}
\]

The function `F_mu` is entire and

\[
F_\mu(0)=1.
\tag{21}
\]

There is a constant

\[
m=m(R,\kappa)>0
\tag{22}
\]

such that

\[
\boxed{
\int_{I_\kappa}|F_\mu(x)|^2\,dx\ge m
}
\tag{23}
\]

for **every** probability measure `mu` on `K_R`.

To prove this, suppose the infimum in (23) were zero. Choose probability measures `mu_j` with the integrals tending to zero. Probability measures on the compact metric space `K_R` are weakly sequentially compact, so after a subsequence `mu_j` converges weakly to a probability measure `mu_infty`.

The kernel

\[
(\lambda,x)\mapsto e^{\lambda x}
\tag{24}
\]

is continuous on the compact product `K_R x I_kappa`. Weak convergence therefore gives

\[
F_{\mu_j}\longrightarrow F_{\mu_\infty}
\quad\text{uniformly on }I_\kappa.
\tag{25}
\]

Hence `F_(mu_infty)` vanishes on `I_kappa`. By analyticity it vanishes identically, contradicting

\[
F_{\mu_\infty}(0)=1.
\tag{26}
\]

This compactness argument is the key strengthening of `RE-134`. Bounded cardinality is not needed because the normalized coefficients are positive empirical masses and all scaled exponents remain in one fixed compact set.

The same family has cardinality-free derivative bounds

\[
|F_\mu(x)|\le e^R,
\qquad
|F_\mu'(x)|
\le \sqrt2\,R e^R
\qquad(x\in I_\kappa).
\tag{27}
\]

These will transfer the complex floor to the real Robin packet.

## 3. The fast target carrier preserves a cardinality-free real floor

Write

\[
d_{\rho_0}=|d_{\rho_0}|e^{i\theta_0},
\qquad
\omega_U:=\gamma_0U.
\tag{28}
\]

Since `gamma_0>=gamma_*`,

\[
\omega_U\ge\gamma_*U\longrightarrow\infty.
\tag{29}
\]

First ignore the perturbation `E_U` and set

\[
G_U(x)
:=\Re\left(
e^{i(\omega_Ux+\theta_0)}Q_U(x)
\right).
\tag{30}
\]

The elementary identity

\[
G_U(x)^2
=
\frac12|Q_U(x)|^2
+
\frac12\Re\left(
e^{2i(\omega_Ux+\theta_0)}Q_U(x)^2
\right)
\tag{31}
\]

gives, after integration over `I_kappa`,

\[
\int_{I_\kappa}G_U(x)^2\,dx
\ge
\frac m2
-
\frac12
\left|
\int_{I_\kappa}e^{2i\omega_Ux}Q_U(x)^2\,dx
\right|.
\tag{32}
\]

By (27), one integration by parts yields

\[
\left|
\int_{I_\kappa}e^{2i\omega_Ux}Q_U(x)^2\,dx
\right|
\ll_{R,\kappa}\omega_U^{-1}
\ll_{R,\kappa,\gamma_*}U^{-1}.
\tag{33}
\]

Therefore, for all sufficiently large `U`,

\[
\int_{I_\kappa}G_U(x)^2\,dx\ge\frac m4.
\tag{34}
\]

The perturbation in (17) changes the corresponding real function by `O(U^-1)` uniformly. Increasing `U_0` if necessary gives

\[
\left\|
\Re\left(
e^{i(\omega_Ux+\theta_0)}(Q_U(x)+E_U(x))
\right)
\right\|_{L^2(I_\kappa)}
\ge c_1(R,\kappa)>0.
\tag{35}
\]

Again, there is no dependence on `N_U`.

Finally `x<=1` and `Theta-beta_0>0`, so

\[
e^{-(\Theta-\beta_0)Ux}
\ge
e^{-(\Theta-\beta_0)U}
\qquad(x\in I_\kappa).
\tag{36}
\]

Using (15), (35), and `|I_kappa|=kappa`,

\[
\sup_{x\in I_\kappa}
|\mathcal S_{C_U,K}(Ux)|
\gg_{R,K,\kappa,\sigma_0,\Theta,\gamma_*}
N_U e^{-(\Theta-\beta_0)U}|d_{\rho_0}|.
\tag{37}
\]

But (11) at `rho=rho_0`, `u=U` gives

\[
|a_{\rho_0,K}(U)|
=
e^{-(\Theta-\beta_0)U}|d_{\rho_0}|
\left(1+O_K(U^{-1})\right).
\tag{38}
\]

Equations (37)--(38) prove (8).

## 4. The `RE-134` occupancy branch disappears

Let `M_K(U)` denote the magnitude of a distinguished dominant strict-subedge atom at `rho_0`, and suppose the full real strict-subedge residual satisfies

\[
\sup_{(1-\kappa)U\le u\le U}
|\mathcal S_K(u)|=o(M_K(U)).
\tag{39}
\]

For a fixed `R>0`, let `C_U(R)` contain the target and every positive-frequency atom in the reciprocal box

\[
|\beta-\beta_0|\le R/U,
\qquad
|\gamma-\gamma_0|\le R/U.
\tag{40}
\]

Whenever the coefficient law (3) applies to that local packet, (8) gives

\[
\sup_I|\mathcal S_{C_U(R),K}|
\ge
c_R\,\#C_U(R)\,M_K(U)
\ge c_R M_K(U).
\tag{41}
\]

Hence at some point of the same fixed-relative window, the complement of the box must contribute at least

\[
\Omega_R(M_K(U))
\tag{42}
\]

in order for (39) to hold. More strongly, if `#C_U(R)` grows, the required exterior cancellation at the point supplied by (41) grows proportionally to that occupancy before any global amplitude constraint is imposed.

Therefore a hiding sequence cannot be explained by unbounded occupancy **inside a fixed scaled box**. For every fixed `R`, order-one cancellation must remain outside radius `R/U`. Equivalently, the cancellation mechanism must fail reciprocal-scale tightness:

\[
\boxed{
\text{macroscopic hiding}
\quad\Longrightarrow\quad
\text{cancellation mass escapes every fixed scaled reciprocal box.}
}
\tag{43}
\]

This sharpens the concentration--compactness statement of `RE-134`. The only surviving noncompactness is escape in scaled diameter; cardinality growth at fixed scaled diameter is harmless for visibility because the Robin coefficients have an aligned positive-measure normalization.

`RE-133` is consistent with (43). Its stage-`j` hiding cluster has `2^j` atoms but also scaled vertical diameter `O(j)`, so no fixed `R` contains the full canceling packet. The construction uses both growing cardinality and growing diameter, but `RE-135` identifies the second feature as the unavoidable one.

## 5. What the zero-counting clue teaches after the strengthening

The authorized comparison with `NB-132` and `NB-133` remains useful as a diagnostic, but not as an input to the theorem.

If one applies an explicit zero-count estimate of the shape used in `NB-132` to a Robin reciprocal ordinate window of width

\[
W\asymp U^{-1}
\tag{44}
\]

at polynomial target height `gamma_0<=U^A`, the endpoint error alone permits

\[
O(\log \gamma_0)=O(\log U)
\tag{45}
\]

zeros. Thus the direct transplant would not have supplied the fixed occupancy `B` assumed in `RE-134`. `NB-133` further warns that such logarithmic counts do not control angular arrangement in a generic annihilator certificate.

`RE-135` bypasses both issues for the local Robin packet. It allows arbitrary finite occupancy and arbitrary arrangement inside the fixed scaled square `K_R`. The load-bearing structure is instead the **aligned coefficient orientation** in (11)--(12), which turns the normalized packet into a positive empirical measure. This structure is absent from a generic exponential polynomial with arbitrary complex coefficients and from the product-type annihilator margin of `NB-133`.

The zero-counting clue therefore resolves in an unexpected direction: no source-faithful occupancy theorem is needed to make a fixed reciprocal box visible. The remaining source-specific task is exterior **tightness** or an equivalent estimate preventing order-`M_K(U)` cancellation from living at scaled radii tending to infinity.

## 6. Adversarial and representation audit

Several stronger interpretations are **not** proved.

1. Equation (8) is a theorem for the **local packet** `C_U`. It does not by itself lower-bound the full Robin residual, because atoms outside the box may cancel the visible local packet. Equation (43) identifies exactly that remaining degree of freedom rather than suppressing it.

2. The fixed scaled diameter is load-bearing. The constant `m(R,kappa)` may collapse as `R` grows. Nothing here gives a useful rate for `R=R(U)->infinity`, and `RE-133` exploits precisely such growth.

3. Common coefficient orientation is load-bearing. Arbitrary complex coefficients do not define probability measures after normalization and can recover the usual high-degree exponential-polynomial cancellation pathologies. The result is therefore source-structure-specific even though it does not use zero counting.

4. The positive-ordinate lower cutoff `gamma_*>0` is used to make the coefficient ratios uniform and to force the carrier frequency `gamma_0 U` to infinity. This is harmless for nontrivial zeta zeros but is part of the theorem.

5. No statement is made that actual off-critical zeta zeros exist, that they realize the formal dominant packet, or that exterior cancellation is tight. The theorem only says what any such local packet would have to do under the coefficient law already isolated in the line.

The representation audit also separates the physical object from its certificate. `Q_U` is not an arbitrary bounded-degree proxy for the packet: it is the normalized empirical transform of the actual local coordinates. The compactness step retains every local atom and loses only cardinality, which becomes total positive mass outside the normalized probability measure. Aliasing inside the box is allowed completely; it cannot erase the interval transform because `F_mu(0)=1` and the spectral support remains compact.

## 7. Prior-art boundary

General Turan--Nazarov and Remez inequalities provide observability bounds for exponential polynomials, usually with constants that deteriorate with the number of terms or an effective degree. That generic framework is nearby but is not load-bearing here. The cardinality-free step comes from the stronger Robin-specific fact that, after reciprocal-box normalization, the coefficients are asymptotically aligned and the normalized spectrum is a **positive probability measure on a fixed compact set**.

The transform nonvanishing argument is the standard compact-support/analyticity mechanism behind elementary Fourier--Laplace uniqueness: a compactly supported positive measure has an entire transform, and a transform vanishing on a real interval would vanish identically, contradicting its value at zero. The proof above includes the needed compactness and carrier transfer directly, so no external theorem is imported as a load-bearing dependency and `SOURCES.md` needs no new anchor.

The literature audit found the general Turan--Nazarov observability class as the closest neighboring language, not an exact Robin/CA statement with the coefficient law (3) and reciprocal scaling (5). Novelty is therefore claimed only for this line-specific splice and the strengthened conclusion relative to `RE-134`, not for the underlying analytic uniqueness principle.

## 8. Consequence for the research line

The local-complexity bottleneck has narrowed. `RE-134` left two possible ways to hide a dominant atom: unbounded occupancy in a fixed reciprocal box, or order-one cancellation escaping that box. `RE-135` removes the first alternative under the physical Robin coefficient law.

The next source-specific target is consequently sharper than a zero-counting theorem:

\[
\boxed{
\text{prove reciprocal-scale tightness of the canceling zero mass,}
\quad\text{or quantify the minimum cost of its escape as }R\to\infty.
}
\tag{46}
\]

A fixed-`R` tightness estimate of the form

\[
\sup_I|\mathcal S_{\mathrm{outside}\ R/U,K}|
=o(M_K(U))
\tag{47}
\]

along a hypothetical hiding sequence would now contradict (9) immediately, with no occupancy or spacing hypothesis inside the box. If fixed-`R` tightness is false, the relevant obstruction is no longer local multiplicity but a genuinely multiscale cancellation cascade whose scaled radius diverges, exactly as the formal control `RE-133` suggests.
