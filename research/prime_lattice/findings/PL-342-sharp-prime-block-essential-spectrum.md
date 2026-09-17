# PL-342 — Kronecker modulation makes the sharp PNT prime-block edges entirely essential

**Evidence:** `EXACT-DERIVED + SHARP-ESSENTIAL-SPECTRUM + DECISIVE-NEGATIVE + PNT/KRONECKER-MATCHED-CONTROL`

**Status:** `PRIME-BLOCK-ESSENTIAL-EDGES-PLUSMINUS-E^A + POLE-COMPACT-INVARIANCE + FULL-WEIL-FREQUENCY-GATE-REMAINS + NO-RH-CONSEQUENCE`

## Precise claim

Use the fixed-domain prime block from `PL-341` on `I=(-1,1)`,

\[
K_a:=\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\bigl(S_{\log n/a}+S_{\log n/a}^*\bigr),
\qquad
P_a:=-K_a,
\]

and put

\[
W_a:=\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
=2e^a(1+o(1)).
\]

`PL-341` proves the ordinary spectral-edge asymptotics

\[
\sup\sigma(K_a)=e^a(1+o(1)),
\qquad
\inf\sigma(K_a)=-e^a(1+o(1)).
\tag{PL342-1}
\]

The same asymptotics hold for the **essential** spectral edges:

\[
\boxed{
\sup\sigma_{\rm ess}(K_a)=e^a(1+o(1)),
\qquad
\inf\sigma_{\rm ess}(K_a)=-e^a(1+o(1)).
}
\tag{PL342-2}
\]

Equivalently,

\[
\boxed{
\|K_a\|_{\rm ess}=e^a(1+o(1)),
\qquad
\frac{\sup\sigma_{\rm ess}(P_a)}{W_a}\to\frac12,
\qquad
\frac{\inf\sigma_{\rm ess}(P_a)}{W_a}\to-\frac12.
}
\tag{PL342-3}
\]

Thus the sharp `+/-1/2` prime-block scale of `PL-341` is not carried merely by isolated smooth endpoint modes. At leading PNT scale, **both spectral edges already survive in the Calkin quotient**.

The mechanism is exact. The PNT-adapted endpoint vectors that asymptotically saturate the ordinary spectral edges can be multiplied by arbitrarily high common oscillations. At each fixed aperture only finitely many rational primes are active. Rational independence of their logarithms and Kronecker recurrence allow a sequence of oscillation frequencies for which every active prime-power translation recovers its original phase simultaneously. The modulated vectors are weakly null, so their limiting Rayleigh values belong to the essential numerical range. Since `PL-341` already gives matching ordinary spectral upper and lower edges, the essential edges are forced to the same asymptotic values.

This also sharpens the completion statement of `PL-059`. Let `E_a` denote the bounded pole operator in the localized completed Weil form. Its quadratic form factors through the two Laplace functionals `V_{1/2}` and `V_{-1/2}`, hence

\[
\operatorname{rank}E_a\le2.
\]

Therefore, for every fixed `a`,

\[
\boxed{
\sigma_{\rm ess}(E_a-K_a)=\sigma_{\rm ess}(-K_a),
}
\tag{PL342-4}
\]

and in particular

\[
\boxed{
\|E_a-K_a\|_{\rm ess}=e^a(1+o(1)).
}
\tag{PL342-5}
\]

The same statement survives addition of any bounded compact completion term, including the continuous-kernel remainder appearing in Suzuki's fixed-domain decomposition. Hence the zeta pole can and does cancel the universal smooth PNT boundary mode of `PL-059`, but **it cannot lower the sharp prime-block scale in essential spectrum at all**.

This is not a statement about the essential spectrum of the full self-adjoint completed-Weil operator `A_a`. The logarithmic principal operator is unbounded and the full localized realization has compact resolvent. The high oscillation frequencies used below pay an increasing archimedean/logarithmic energy cost. The surviving RH-facing question is precisely whether that unbounded frequency penalty, together with source-selected branch information, suppresses the recurrent Calkin edge in the relevant low spectral states. No such suppression is proved here.

## 1. The `PL-341` endpoint pair already reaches both ordinary edges

Write

\[
I_-=(-1,0),\qquad I_+=(0,1).
\]

`PL-341` splits the outer prime block as

\[
K_a^{\rm out}
=
\begin{pmatrix}
0&T_a^*\\
T_a&0
\end{pmatrix},
\]

and introduces normalized endpoint weights

\[
f_a(y)=\left(\frac{a}{1-e^{-a}}\right)^{1/2}
 e^{-a(1+y)/2},\qquad y\in I_-,
\]

\[
g_a(x)=\left(\frac{a}{1-e^{-a}}\right)^{1/2}
 e^{-a(1-x)/2},\qquad x\in I_+.
\]

They satisfy

\[
\langle g_a,T_af_a\rangle=e^a(1+o(1)).
\tag{PL342-6}
\]

Put

\[
u_a^{\pm}=\frac1{\sqrt2}(f_a\oplus(\pm g_a)).
\tag{PL342-7}
\]

Then

\[
\langle u_a^{\pm},K_a^{\rm out}u_a^{\pm}\rangle
=\pm e^a(1+o(1)).
\]

The inner source obeys

\[
\|K_a^{\rm in}\|=o(e^a)
\]

by `PL-341`. Consequently

\[
\boxed{
q_a^{\pm}:=
\langle u_a^{\pm},K_au_a^{\pm}\rangle
=\pm e^a(1+o(1)).
}
\tag{PL342-8}
\]

These vectors were used there only to identify ordinary spectral scale. The point here is that their arithmetic Rayleigh values can be reproduced on weakly-null oscillatory copies.

## 2. Prime-log recurrence moves the same Rayleigh values into the essential numerical range

For `xi in R`, let

\[
(M_\xi u)(x)=e^{i\xi x}u(x)
\]

on `L^2(I)`. For every compressed translation,

\[
M_\xi^*S_hM_\xi=e^{-i\xi h}S_h.
\tag{PL342-9}
\]

Fix `a`. Only finitely many prime powers satisfy `log n<2a`; let `P(a)` be the finite set of underlying primes. Unique factorization gives rational independence of

\[
\{\log p:p\in P(a)\}.
\]

Hence Kronecker recurrence supplies arbitrarily large `tau_j` such that

\[
e^{-i\tau_j\log p}\to1
\qquad(p\in P(a)).
\tag{PL342-10}
\]

For every active prime power `n=p^k`, the same sequence gives

\[
e^{-i\tau_j\log n}\to1.
\tag{PL342-11}
\]

Set

\[
\xi_j=a\tau_j,
\qquad
u_{a,j}^{\pm}=M_{\xi_j}u_a^{\pm}.
\tag{PL342-12}
\]

Since `h_n(a)=log n/a`, equations (PL342-9)--(PL342-11) imply, term by term in the finite prime-power sum,

\[
\boxed{
\langle u_{a,j}^{\pm},K_au_{a,j}^{\pm}\rangle
\longrightarrow q_a^{\pm}
\qquad(j\to\infty).
}
\tag{PL342-13}
\]

At the same time `|xi_j|->infinity`, so

\[
u_{a,j}^{\pm}\rightharpoonup0
\quad\text{weakly in }L^2(I).
\tag{PL342-14}
\]

Indeed, for any fixed `v in L^2(I)`, the product `u_a^{\pm}\overline v` belongs to `L^1(I)` and the pairing is an ordinary Fourier integral; Riemann--Lebesgue applies.

For a bounded self-adjoint operator, the limits of Rayleigh quotients along weakly-null unit vectors lie in its essential numerical range, whose endpoints are the endpoints of the convex hull of the essential spectrum. Therefore (PL342-13)--(PL342-14) give

\[
\sup\sigma_{\rm ess}(K_a)\ge q_a^+,
\qquad
\inf\sigma_{\rm ess}(K_a)\le q_a^-.
\tag{PL342-15}
\]

No approximate-eigenvector claim is needed: the essential numerical range is sufficient because `q_a^+` and `q_a^-` already approach the ordinary upper and lower spectral edges.

## 3. Ordinary spectral sharpness squeezes the essential edges exactly

Essential spectrum is contained in spectrum, so

\[
\sup\sigma_{\rm ess}(K_a)\le\sup\sigma(K_a),
\qquad
\inf\sigma_{\rm ess}(K_a)\ge\inf\sigma(K_a).
\tag{PL342-16}
\]

Combine (PL342-8), (PL342-15), (PL342-16), and the sharp ordinary edges (PL342-1). The positive edge is squeezed between two quantities equal to `e^a(1+o(1))`; the negative edge is squeezed between two quantities equal to `-e^a(1+o(1))`. This proves (PL342-2). Equation (PL342-3) follows from `W_a=2e^a(1+o(1))`.

This strengthens `PL-053` quantitatively and globally. `PL-053` used a fixed-depth cross-end compression to prove a positive Calkin lower bound after natural normalization. The present argument combines the same recurrence mechanism with the globally saturating Schur profiles of `PL-341`, showing that the lower bound is sharp at the level of both essential spectral edges:

\[
\boxed{
\text{ordinary prime-block edge}
\sim
\text{essential prime-block edge}
\sim e^a.
}
\]

There is no hidden isolated spectral surplus at leading PNT order.

## 4. The finite-rank pole cancellation cannot change these edges

`PL-059` factors the pole quadratic form as

\[
Q_{\rm pole}(v)
=2\operatorname{Re}
\bigl(V_{1/2}(v)\overline{V_{-1/2}(v)}\bigr),
\]

where

\[
V_s(v)=\int v(x)e^{sx}\,dx.
\]

Thus its bounded operator `E_a` has range contained in the span of the two exponential vectors associated with `V_{1/2}` and `V_{-1/2}`. In particular `E_a` is finite rank for every finite aperture.

Weyl invariance under compact perturbations gives (PL342-4) exactly. Since the essential spectrum of `-K_a` is the reflection of that of `K_a`, (PL342-2) gives (PL342-5).

The same conclusion holds after adding Suzuki's bounded continuous completion remainder at fixed `a`: its kernel is continuous on the compact fixed-domain square after the logarithmic singular principal part is split off, hence the induced bounded operator is compact. Compact terms can alter isolated eigenvalues but not the essential spectrum.

This yields a precise reconciliation of `PL-059` with `PL-341`. On fixed smooth endpoint profiles, the pole produces exactly the rank-two PNT counterterm that cancels the universal strong boundary mode. But the phase-modulated copies (PL342-12) are weakly null, so every compact correction becomes asymptotically invisible while Kronecker recurrence restores the atomic prime translations. The two statements are therefore not competing approximations; they describe complementary topologies of the same source:

\[
\text{fixed/smooth endpoint directions}
\;\Longrightarrow\;
\text{pole cancels the PNT mode},
\]

whereas

\[
\text{high-frequency weakly-null directions}
\;\Longrightarrow\;
\text{the full sharp prime edge survives modulo compacts}.
\]

## 5. Why this still does not imply a negative direction for the completed Weil operator

The full localized operator is not the bounded sector `E_a-K_a`. Suzuki's self-adjoint `A_a` contains the logarithmic principal operator, scalar terms, and the bounded completion pieces. For every finite `a`, `A_a` has compact resolvent. Therefore (PL342-2) cannot be transplanted to `A_a` by compact-perturbation language.

The obstruction is concrete. The recurrence sequence in (PL342-10) is obtained by sending the modulation frequency to infinity at fixed `a`. The logarithmic principal symbol grows like `log|xi|`, so these same weakly-null witnesses pay an unbounded archimedean frequency cost. This is exactly the unresolved coupling isolated in `CLUE-prime-lattice-mesoscopic-weil-boundary-topology`: the bounded prime sector retains a sharp recurrent Calkin edge, while any RH-relevant full-form argument must control that edge together with the logarithmic frequency penalty on the **same moving states**.

The scalar part also lies outside compact invariance: adding `c_a I` translates the essential spectrum rather than leaving it fixed. No large-`a` scalar asymptotic is asserted here. The theorem therefore makes no claim that the full completed operator has essential spectrum, no claim that its low branch follows the prime-block edge, and no claim toward RH.

## 6. Adversarial, matched-control, and novelty audit

**Not merely the fixed-depth lower bound.** `PL-053` proves an order-one essential-norm obstruction on every fixed boundary depth after normalization. That alone does not show that the sharp global spectral edge found much later in `PL-341` is essential. Equations (PL342-8)--(PL342-16) supply that missing global squeeze and both signs.

**Not a Weyl sequence for a prescribed point.** Weakly-null Rayleigh convergence only places `q_a^pm` in the essential numerical range. The argument does not claim `||(K_a-q_a^pm)u_{a,j}^pm||->0`. The spectral-edge conclusion follows because the essential numerical range of a self-adjoint operator has endpoints at the extreme essential spectral values and because the ordinary edges already have the matching asymptotics.

**The pole cancellation is not contradicted.** `PL-059` is a strong/fixed-profile cancellation theorem. A finite-rank pole term is invisible on the weakly-null recurrent sequences used here. Thus it can cancel the universal PNT mode and simultaneously leave the essential edge unchanged.

**The full completed operator is deliberately excluded.** The unbounded logarithmic principal part is load-bearing on the recurrent sequence; compact-resolvent localized Weil theory is untouched.

**Matched generalized-prime control.** The amplitude `e^a` comes from the same positive PNT mass law used in `PL-341`. The promotion from ordinary to essential edge uses only finite rational independence of the active logarithmic frequencies. A matched generalized-prime or positive atomic system with the same PNT-scale mass and rationally independent active frequencies reproduces the argument. Hence the sharp essential edge is not rational-prime RH rigidity.

**Prior art.** Kronecker recurrence, the weakly-null characterization of the essential numerical range, and invariance of essential spectrum under compact perturbations are classical. Suzuki's localized completed-Weil realization and pole term are already registered in `SOURCES.md` and used in `PL-059`/`PL-265`. A targeted search around localized Weil/von-Mangoldt translation operators and essential spectrum did not locate a published theorem stating (PL342-2)--(PL342-5). Search absence is not evidence of broad novelty; the durable contribution is the line-specific synthesis and sharp consequence of `PL-052`/`PL-053` plus `PL-341`.

## Consequence for `prime_lattice`

The current large-aperture picture is now sharper. The positive-jump sector of `PL-339`--`PL-341` cannot neutralize the scalar compensation by itself. The smooth PNT boundary mode responsible for the visible `+/-e^a` endpoint geometry is canonically canceled by the zeta pole (`PL-059`). Nevertheless, Kronecker modulation recreates the **same sharp `+/-e^a` scale inside essential spectrum**, so bounded compact completion cannot improve the worst prime-block directions even at leading order.

Therefore the next RH-facing step cannot be another bounded pole/continuous-kernel correction or another refinement of prime-block PNT coercivity. It must use the part excluded from compact invariance: the logarithmic principal energy, a scalar/completion balance tied to the exact full form, or source-selected low-branch restrictions that prevent the high-frequency recurrent witnesses from being admissible at the dangerous energy scale. Any proposed mechanism should be tested on the recurrent modulation family (PL342-12) before being treated as a genuine improvement over the PNT-universal prime block.