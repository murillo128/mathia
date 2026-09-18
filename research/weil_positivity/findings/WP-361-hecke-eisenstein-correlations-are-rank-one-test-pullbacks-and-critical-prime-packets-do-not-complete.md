---
id: WP-361
title: Hecke--Eisenstein correlations are rank-one test pullbacks and critical prime packets do not complete
branch: weil_positivity
status: supported
kind: hecke-eisenstein-maass-selberg-rank-one-obstruction
claim_strength: exact finite-Hecke Gram rank-one and Maaß--Selberg test-pullback reduction; prime-number-theorem obstruction to the unrenormalized critical all-prime Eisenstein multiplier
created: 2026-09-18
related: [WP-237, WP-345, WP-356, WP-357, WP-358, WP-359, WP-360]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - Henryk Iwaniec, Spectral Methods of Automorphic Forms, 2nd ed., AMS, 2002
  - Claire Burrin, Uri Shapira, and Shucheng Yu, Translates of rational points along expanding closed horocycles on the modular surface, Mathematische Annalen 382 (2022), 655-717
  - Tian An Wong, Explicit formulas for the spectral side of the trace formula of SL(2), Acta Arithmetica 195 (2020), 149-175, DOI 10.4064/aa190115-9-10, arXiv:1608.02296
  - classical Hecke amplification and the prime number theorem with partial summation
---

# WP-361 — Hecke--Eisenstein correlations are rank-one test pullbacks and critical prime packets do not complete

## Claim

`WP-360` leaves one especially natural escape from the nonconstant cusp-core obstruction: an Eisenstein series is already an infinitely correlated Fourier state and a simultaneous Hecke eigenfunction, so perhaps the source-forced correlations of that global state can assemble critical prime amplitudes before positivity is taken. On the ordinary modular Eisenstein line, that escape has an exact two-part obstruction.

Let

\[
E_t(z):=E\!\left(z,\frac12+it\right),
\qquad t\in\mathbb R,
\tag{1}
\]

for the level-one nonholomorphic Eisenstein family, and use the self-adjoint Petersson-normalized Hecke operators from `WP-358`. Classically,

\[
T_nE_t=\lambda_t(n)E_t,
\qquad
\lambda_t(n)=\sum_{d\mid n}\left(\frac{n}{d^2}\right)^{it}.
\tag{2}
\]

In particular, for a prime `p`,

\[
\boxed{
\lambda_t(p)=p^{it}+p^{-it}=2\cos(t\log p).
}
\tag{3}
\]

For a finite prime set `F` and coefficients `a_p`, put

\[
A_F:=\sum_{p\in F}a_pT_p,
\qquad
L_F(t):=\sum_{p\in F}a_p\lambda_t(p).
\tag{4}
\]

Arthur truncation is linear, so simultaneous Hecke diagonalization gives the exact identity

\[
\boxed{
\Lambda^T A_FE_t=L_F(t)\Lambda^T E_t.
}
\tag{5}
\]

Consequently, if

\[
N_T(t):=\|\Lambda^T E_t\|_2^2,
\tag{6}
\]

then the full finite-prime Hecke Gram on the truncated Eisenstein eigenline is

\[
\boxed{
G_F(t)_{p,q}
:=\left\langle\Lambda^TT_pE_t,\Lambda^TT_qE_t\right\rangle
=N_T(t)\lambda_t(p)\lambda_t(q).
}
\tag{7}
\]

Thus `G_F(t)` has rank at most one. Every inherited positive quadratic form is only

\[
\boxed{
\left\|\Lambda^TA_FE_t\right\|_2^2
=N_T(t)|L_F(t)|^2.
}
\tag{8}
\]

This is genuine cross-prime coherence, but it is maximally scalar: the entire finite-prime packet multiplies the same Maaß--Selberg norm. The scattering logarithmic derivative, Gamma/polar terms and the zero-divisor carrier contained in `N_T` are not coupled to independent Hecke directions.

After spectral averaging, the reduction is even sharper. Wong's positive Maaß--Selberg distribution for a positive-type seed has the form

\[
J^T(g_0*g_0^*)
=\int_{\mathbb R}N_T(t)
\left|H_0(t)\right|^2\,d\mu(t),
\tag{9}
\]

with `H_0(t)` the centered Mellin/Fourier transform of the seed, up to the source normalization of spectral measure. Inserting the finite Hecke packet gives

\[
J_F^T(g_0)
=\int_{\mathbb R}N_T(t)
\left|L_F(t)H_0(t)\right|^2\,d\mu(t).
\tag{10}
\]

Because `L_F` is a finite exponential polynomial in the log-prime shifts, `L_FH_0` is the transform of a finite source-allowed linear combination of log-translates of `g_0`. Therefore

\[
\boxed{
J_F^T(g_0)=J^T(g_{0,F}*g_{0,F}^*)
}
\tag{11}
\]

for the corresponding transformed seed `g_{0,F}`. Finite Hecke amplification creates no new positive cone and no new sign theorem: it is an exact pullback of the already-positive Maaß--Selberg distribution to another admissible positive-type test.

The remaining possibility is to take an actual all-prime limit before the square. For the two critical coefficient placements isolated in `WP-360`,

\[
a_p=p^{-1/2}
\qquad\text{or}\qquad
 a_p=\frac{\log p}{\sqrt p},
\tag{12}
\]

the natural prime-cutoff eigenvalue packet has no finite spectral multiplier limit. More generally, let

\[
L_X^{(\alpha)}(t)
:=\sum_{p\le X}
\frac{(\log p)^\alpha}{\sqrt p}
\left(p^{it}+p^{-it}\right),
\qquad \alpha\in\{0,1\}.
\tag{13}
\]

The prime number theorem and partial summation give, for every fixed real `t`,

\[
\sum_{p\le X}p^{-1/2+it}
=
\frac{X^{1/2+it}}
{(1/2+it)\log X}
+o\!\left(\frac{\sqrt X}{\log X}\right),
\tag{14}
\]

and

\[
\sum_{p\le X}(\log p)p^{-1/2+it}
=
\frac{X^{1/2+it}}
{1/2+it}
+o(\sqrt X).
\tag{15}
\]

Hence for every fixed `t\ne0`, both real symmetric combinations in (13) have unbounded oscillatory subsequences; for `t=0` the scalar sums diverge positively. In particular, for every fixed nonzero Eisenstein parameter,

\[
\boxed{
L_X^{(\alpha)}(t)\ \text{does not converge as }X\to\infty,
\qquad \alpha=0,1.
}
\tag{16}
\]

Since `N_T(t)>0` for `t\ne0`, equation (8) then shows that the corresponding truncated critical Hecke packet has unbounded norm along subsequences. The source-forced Fourier correlations of an Eisenstein eigenstate therefore do **not** rescue the critical all-prime packet as the ordinary unrenormalized limit of its finite Hecke amplifiers.

This complements rather than repeats `WP-360`. There the critical packet fails because different prime outputs are orthogonal on the finite-Fourier cusp core, forcing an `l2` threshold. Here the maximally correlated Eisenstein state makes all prime channels collapse onto one scalar eigenline; the price is the opposite extreme, a coherent prime Dirichlet polynomial which itself does not converge at the critical half-density. Moving from an uncorrelated core to the canonical fully correlated Hecke eigenstate does not produce the missing global positive form.

**Classification:** `CLASSICAL-HECKE-EIGENLINE + EXACT-DERIVED + MAASS-SELBERG-TEST-PULLBACK + PNT-ASYMPTOTIC + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM-FOR-CLASSICAL-INGREDIENTS`.

## 1. The full Hecke Gram is rank one before any scalar readout

Equation (2) is the standard Hecke action on the continuous spectrum. In the normalization used throughout `WP-358`--`WP-360`, Burrin--Shapira--Yu record the same formula

\[
\lambda_t(n)=\sum_{d\mid n}(n/d^2)^{it},
\tag{17}
\]

so there is no hidden `p^{\pm1/2}` left in the prime eigenvalue. The critical half-density, if desired, must therefore enter through the packet coefficients `a_p`, not through a normalization mismatch.

For each fixed `t`, the vectors `T_pE_t` are all collinear already before truncation. Applying the linear operator `Lambda^T` preserves that collinearity. This proves (7) without assuming that Hecke operators commute with truncation. That distinction matters: `T_p Lambda^T E_t` need not equal `Lambda^T T_pE_t`, and the commutator/boundary defect of that different ordering is exactly the category studied by `WP-356`--`WP-360`.

For any coefficient vector `a=(a_p)`, positivity of the Gram gives

\[
a^*G_F(t)a
=N_T(t)\left|\sum_{p\in F}a_p\lambda_t(p)\right|^2.
\tag{18}
\]

No matrix direction remains in which the finite-prime part and the scattering/archimedean part can acquire different signs. Polarization can recover the rank-one cross terms `lambda_t(p)lambda_t(q)`, but every principal minor of order at least two vanishes. Thus the cross-prime coherence is source-forced but carries no additional positive dimension.

## 2. Finite Hecke amplification only changes the admissible test

On the unitary axis, (3) can be written

\[
\lambda_t(p)=e^{it\log p}+e^{-it\log p}.
\tag{19}
\]

Therefore `L_F` is the Fourier transform of the finite symmetric log-prime measure

\[
\mu_F
=\sum_{p\in F}a_p
\left(\delta_{\log p}+\delta_{-\log p}\right).
\tag{20}
\]

After the standard centering that turns the Mellin transform on `Re s=1/2` into an additive Fourier transform, multiplication by `L_F(t)` is convolution by `mu_F` in log scale. Finite convolution preserves the usual smooth/compact-support test class used to form the positive-type seed. This gives (11).

This is precisely the algebra behind classical finite Hecke amplification: a simultaneous Hecke eigenfunction is multiplied by its finite amplifier, and the positive norm sees the squared amplifier. In the present problem that familiar mechanism is a **matched control**, not an escape. Wong's unamplified Maaß--Selberg theorem already states positivity for the entire admissible positive-type class. Evaluating the same theorem on `g_(0,F)` cannot strengthen the sign projection from the positive total distribution onto the Weil zero summand.

In particular, a finite Hecke packet cannot solve the residual-sign gap of `CLUE-maass-selberg-remainder-sign-interface` merely by creating cross-prime terms. Those terms occur only inside `|L_F|^2`, which multiplies every component of the same Maaß--Selberg spectral norm. A signed linear combination of different amplified identities could algebraically cancel unwanted components, but its sign would no longer follow from the positive Gram. Any such cancellation therefore needs an additional independent positive theorem.

## 3. Critical all-prime amplification has no ordinary eigenline limit

The finite reduction leaves a possible singular limit: perhaps the desired arithmetic lives only in `F` tending to all primes with critical coefficients, outside the finite test class. Equations (14)--(16) show that the most direct version does not exist.

For `alpha=1`, write `theta(X)=sum_(p<=X) log p`. The prime number theorem gives `theta(X)=X+o(X)`. Stieltjes partial summation with `z=-1/2+it` gives

\[
\sum_{p\le X}(\log p)p^{-1/2+it}
=\int_{2^-}^Xx^z\,d\theta(x)
=\frac{X^{z+1}}{z+1}+o(X^{1/2}),
\tag{21}
\]

which is (15). For `alpha=0`, the same argument with `pi(X)~X/log X` gives (14).

Taking the sum with `t` replaced by `-t` gives (13). When `t\ne0`, the leading term has magnitude of order `sqrt(X)/(log X)^{1-alpha}` and phase `t log X-arg(1/2+it)`. Along sequences of `X` for which this phase stays near `0` or `pi`, the real part tends to `+infinity` or `-infinity` in magnitude. Thus no ordering by increasing prime has a finite scalar limit.

For `t\ne0`, `E_t` is nonzero, hence its truncated norm `N_T(t)` is strictly positive. Combining with (8), the finite packets cannot converge in the truncated Hilbert norm on that generalized eigenstate. This conclusion does not use the special central parameter `t=0`, where the standard Eisenstein normalization has its own functional-equation subtlety; every fixed nonzero `t` already supplies the obstruction.

The failure is stronger than lack of absolute convergence. It is ordinary pointwise failure of the source eigenvalue multiplier under the natural prime cutoff. An Abel, zeta, prime-zeta, distributional, or other analytic regularization may assign a continuation to a related object, but that is a new completion/renormalization step. Its domain, subtraction law and positivity would have to be source-forced and audited independently; the Maaß--Selberg norm does not supply them automatically.

## 4. Aggressive falsification and matched controls

**Could finite Hecke cross terms isolate the scattering remainder?** Not on a single level-one Eisenstein eigenline. The exact Gram (7) has rank one, so every positive compression remains `N_T(t)` times one scalar modulus square. There is no second positive Hecke direction against which the `m'/m` block could be separated.

**Could one act on the truncated series instead?** Yes, but that is a different ordering. The noncommutation of cusp truncation with Hecke correspondences is precisely where the boundary operators of `WP-356`--`WP-360` live. The present finding does not identify `T_p Lambda^T E_t` with `Lambda^T T_pE_t` and does not close noncommuting truncation-before-Hecke constructions beyond those existing results.

**Could a finite amplifier select a favorable subclass of tests?** It can, but Weil positivity requires the full admissible positive-type class. Since the amplified norm is exactly the unamplified positive distribution evaluated on another admissible seed, positivity on that subclass supplies no new implication for arbitrary tests. Restricting tests until the residual term happens to have the right sign would fail the quantifier in the canonical mandate.

**Could a different spectral channel avoid rank one?** A genuinely vector-valued/many-channel Eisenstein family, higher-rank truncation, ramified sector, or source-defined coupling between distinct global representations may have a nontrivial matrix Gram. The present claim concerns the level-one scalar Eisenstein line and finite Hecke algebra acting on it. Any surviving multichannel proposal must show that its extra matrix directions retain the Riemann arithmetic before normalization and that positivity fixes the required orientation rather than merely diagonalizing into independent scalar `L`-factors.

**Could a renormalized all-prime packet still work?** Not ruled out. Equations (14)--(16) only kill the ordinary unrenormalized cutoff limit. A renormalized or rigged/distributional completion is a genuine category change and remains admissible only if the renormalization is canonical before inspecting the desired Weil sign and comes with its own positive theorem.

**Generic translation control.** Replace `log p` in (19) by any finite symmetric displacement set `ell_j` and define `lambda_j(t)=2cos(t ell_j)`. The Gram is still `N_T lambda lambda^*`, and finite amplification is still only test convolution. Prime arithmetic chooses the displacement set but does not cause the rank-one positivity theorem. This shows why finite amplified positivity is too universal to be the sought Riemann-specific sign mechanism.

## 5. Prior-art and novelty audit

No novelty is claimed for simultaneous Hecke diagonalization of Eisenstein series. Iwaniec's standard treatment gives the continuous-spectrum Hecke theory, and Burrin--Shapira--Yu explicitly record

\[
T_nE(z,1/2+it)=\lambda_t(n)E(z,1/2+it),
\qquad
\lambda_t(n)=\sum_{d\mid n}(n/d^2)^{it},
\tag{22}
\]

in the same self-adjoint normalization used here. Squaring a finite scalar Hecke amplifier on a common eigenfunction is classical amplification technology.

No novelty is claimed for the Maaß--Selberg relation or for positivity of the truncated continuous spectral distribution. Wong supplies the exact positive distribution, the logarithmic-derivative/explicit-formula decomposition and the residual lower-bound gap that motivates the local clue. No novelty is claimed for the PNT asymptotics (14)--(15), which are standard partial summation consequences.

A targeted literature search around Hecke-amplified Eisenstein series, Maaß--Selberg truncation, Hecke eigenvalues in the continuous spectrum, arithmetic amplification and trace-formula positivity found these ingredients as standard but did not identify a separate theorem asserting the Mathia-specific conclusion needed here. That conclusion is intentionally a **route classification**, not a new general Hecke theorem: the canonical fully correlated Eisenstein escape left open by `WP-360` either remains a finite rank-one pullback of ordinary Maaß--Selberg positivity, or, with the critical all-prime coefficients, fails to form an unrenormalized eigenline multiplier under natural prime cutoff.

## Consequence for `weil_positivity`

The two extreme ways of assembling the nonconstant Hecke boundary data are now both controlled in the ordinary Hilbert setting. On the finite-Fourier cusp core, distinct primes remain orthogonal and critical amplitudes fail the `l2` completion (`WP-360`). On the canonical simultaneous Eisenstein eigenstate, all primes correlate maximally but collapse to a single scalar amplifier; finite packets add no new positivity, while critical all-prime packets do not converge without an extra renormalization.

Therefore the surviving automorphic route cannot simply be

\[
\text{choose the correlated Eisenstein Hecke eigenstate}
\to
\text{insert critical prime amplifier}
\to
\text{truncate and square}
\to
\text{Weil positivity}.
\tag{23}
\]

A viable construction must introduce additional source-defined structure **before** the Hecke arithmetic is reduced to a scalar eigenvalue: a genuinely noncommuting truncation/operator coupling, a nontrivial multichannel global form, or a canonical renormalized/distributional completion with an independent positivity theorem. It must then still recover the finite-prime coefficient together with the Gamma/polar terms and isolate the Weil zero form without assuming RH or importing its kernel by hand.
