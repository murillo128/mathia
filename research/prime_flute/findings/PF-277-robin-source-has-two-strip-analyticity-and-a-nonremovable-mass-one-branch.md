# PF-277 — Robin source has two-strip analyticity and a nonremovable mass-one branch

**Status:** `EXACT-DERIVED + ENDPOINT-REGULARITY + FOURIER-STRIP-ANALYTICITY + NONREMOVABLE-THRESHOLD-BRANCH + ROUTE-NARROWING`.

PF-276 proves that the fixed-axis Robin-normalized source column retains a finite strictly positive generalized zero-mode moment, and PF-274 identifies that moment with the corridor Fourier coefficient functional at the two mass-one branch points `xi=±i`. One analytic ambiguity remained: the threshold value was known as an absolutely convergent coefficient functional, but it had not yet been shown that the normalized source itself extends through a full complex neighborhood of those points before multiplication by the square-root seam symbol.

That ambiguity can be removed directly from PF-276's weighted conservation law. In one parity chain, the normalized source coefficients have a summable `3/2` moment. The normalized Gegenbauer basis then forces the physical source to vanish like distance-to-endpoint to the power `3/2`. After the PF-274 compactification this gains the Jacobian half-power and gives

\[
Z_i(\tau):=(U^*z^{(i)})(\tau)=O(e^{-2|\tau|}).
\tag{1}
\]

Consequently `\widehat Z_i` is holomorphic throughout the open strip `|\operatorname{Im}\xi|<2`, while

\[
\widehat Z_i(-i)=T_i^{(\varepsilon)}>0,
\qquad
\widehat Z_i(i)=(-1)^\varepsilon T_i^{(\varepsilon)}\ne0.
\tag{2}
\]

Since PF-273 gives

\[
g_w(\lambda)=\sqrt w\,\lambda^{1/2}(1+O(\lambda)),
\qquad \lambda\to0,
\tag{3}
\]

the transformed normalized source

\[
\widehat{g_w(L)z^{(i)}}(\xi)
=g_w(1+\xi^2)\widehat Z_i(\xi)
\tag{4}
\]

has a **nonremovable square-root branch germ** at each of `xi=±i`, with nonzero leading coefficient. Robin normalization therefore cannot hide the mass-one edge by a failure of source analyticity or by a zero that appears only after passing from the coefficient functional to the actual Fourier transform.

This still does not prove the large-degree continuous-Hahn/Gegenbauer coefficient asymptotic. The remaining fixed-axis gate is narrower: transfer the genuine nonzero branch germ in (4) to the corridor coefficients and determine whether it forces the critical mass-one leakage scale.

## 1. PF-276 gives a summable `3/2` coefficient moment

Fix a parity `\varepsilon\in\{0,1\}` and write

\[
\varphi_j=e_{2j+\varepsilon},
\qquad
\kappa_j=2j+\varepsilon+\alpha,
\qquad
\alpha=\frac{1+\sqrt5}{2}.
\tag{5}
\]

Use PF-276's notation

\[
u^{(i)}=(I+R)^{-1}\varphi_i,
\qquad
z^{(i)}=A^{-1/4}u^{(i)},
\qquad
z_j^{(i)}=\kappa_j^{-1/2}u_j^{(i)}.
\tag{6}
\]

Its positive generalized-harmonic weight is

\[
q_j=\kappa_j^{1/2}c_j\asymp j+1.
\tag{7}
\]

PF-276 proves both `u_j^(i)>0` and the exact conservation law

\[
\sum_{j\ge0}q_j u_j^{(i)}=q_i<\infty.
\tag{8}
\]

Because `\kappa_j\asymp j+1`, equations (6)--(8) imply

\[
\boxed{\sum_{j\ge0}(j+1)^{3/2}|z_j^{(i)}|<\infty.}
\tag{9}
\]

Indeed `(j+1)^{3/2}z_j^(i)\asymp(j+1)u_j^(i)\asymp q_j u_j^(i)`. No Hilbert-space pairing with the non-`ell^2` zero mode is introduced here; (9) is only a consequence of the already justified positive finite-section conservation in PF-276.

## 2. The normalized Gegenbauer basis converts (9) into endpoint vanishing

PF-274 uses

\[
e_n(\theta)
=h_n^{-1/2}\sin^\alpha\!\theta\,C_n^{(\alpha)}(\cos\theta),
\qquad 0<\theta<\pi.
\tag{10}
\]

Let `d(\theta)=\min(\theta,\pi-\theta)`. Standard endpoint/interior Gegenbauer estimates with this normalization give

\[
|e_n(\theta)|
\le C_\alpha\min\!\left(1,((n+1)d(\theta))^\alpha\right).
\tag{11}
\]

Near an endpoint this follows from `|C_n^(\alpha)(x)|\le C_n^(\alpha)(1)\asymp n^(2\alpha-1)` and `h_n^{-1/2}\asymp n^(1-\alpha)`; once `d\gtrsim(n+1)^{-1}`, the Hilb/Darboux estimate gives a uniform bound. The reflected endpoint follows from Gegenbauer parity.

Expand the normalized source in its parity chain and put `J=d(\theta)^{-1}`. Splitting at `j\asymp J` and using (9),

\[
\begin{aligned}
|z^{(i)}(\theta)|
&\le C d^\alpha\sum_{j\le J}(j+1)^\alpha |z_j^{(i)}|
 +C\sum_{j>J}|z_j^{(i)}|\\
&\le C d^\alpha J^{\alpha-3/2}\sum_j(j+1)^{3/2}|z_j^{(i)}|
 +C J^{-3/2}\sum_j(j+1)^{3/2}|z_j^{(i)}|.
\end{aligned}
\tag{12}
\]

Since `\alpha>3/2` and `J=d^{-1}`, both terms have the same endpoint scale:

\[
\boxed{|z^{(i)}(\theta)|\le C_i d(\theta)^{3/2}.}
\tag{13}
\]

The same estimates give uniform absolute convergence of the Gegenbauer series, so (13) concerns the actual continuous representative, not merely formal coefficients.

## 3. Compactification supplies a full analytic strip around the threshold

PF-274's unitary compactification is

\[
\tau=\log\tan\frac\theta2,
\qquad
L=U(1-\partial_\tau^2)U^*,
\tag{14}
\]

with

\[
(U^*f)(\tau)=\sin^{1/2}\!\theta(\tau)\,f(\theta(\tau)).
\tag{15}
\]

Combining (13) and (15), and using `\theta\asymp e^\tau` as `\tau\to-\infty` and `\pi-\theta\asymp e^{-\tau}` as `\tau\to+\infty`, gives

\[
\boxed{|Z_i(\tau)|\le C_i e^{-2|\tau|}}
\qquad (|\tau|\ \text{large}).
\tag{16}
\]

Therefore

\[
\widehat Z_i(\xi)=\int_{\mathbb R}e^{-i\xi\tau}Z_i(\tau)\,d\tau
\tag{17}
\]

is absolutely convergent and holomorphic for

\[
\boxed{|\operatorname{Im}\xi|<2.}
\tag{18}
\]

The same bound applied to tails of the absolutely convergent Gegenbauer series gives convergence in the exponentially weighted `L^1` spaces needed at `\operatorname{Im}\xi=\pm1`. Thus PF-276's coefficient evaluations are genuine Fourier-Laplace values:

\[
\widehat Z_i(-i)=\sum_jz_j^{(i)}\widehat\psi_{2j+\varepsilon}(-i)
=T_i^{(\varepsilon)}>0,
\tag{19}
\]

\[
\widehat Z_i(i)=\sum_jz_j^{(i)}\widehat\psi_{2j+\varepsilon}(i)
=(-1)^\varepsilon T_i^{(\varepsilon)}\ne0.
\tag{20}
\]

Hence `xi=±i` lie strictly inside the source transform's analyticity domain, with a full unit of exponential margin before the boundary of (18).

## 4. The mass-one branch is an actual nonremovable Fourier germ

Under (14), the square-root seam acts by the scalar multiplier `g_w(1+\xi^2)`, where `w=rs`. PF-273 gives the exact small-`lambda` expansion (3). Since `1+\xi^2` has simple zeros at `xi=±i` and `\widehat Z_i` is holomorphic and nonzero there, in slit neighborhoods of the threshold points

\[
\boxed{
g_w(1+\xi^2)\widehat Z_i(\xi)
=\sqrt w\,T_i^{(\varepsilon)}(1+\xi^2)^{1/2}
+O((1+\xi^2)^{3/2})
}
\tag{21}
\]

near `xi=-i`, and

\[
\boxed{
g_w(1+\xi^2)\widehat Z_i(\xi)
=\sqrt w\,(-1)^\varepsilon T_i^{(\varepsilon)}(1+\xi^2)^{1/2}
+O((1+\xi^2)^{3/2})
}
\tag{22}
\]

near `xi=i`.

The leading coefficients are nonzero. Therefore no holomorphic source factor supplied by Robin normalization can remove the nearest square-root branch of the complete-axis multiplier. Further finite-seam singularities may occur at larger imaginary height; they do not affect this local mass-one statement.

## 5. Consequence for the accepted Robin-source clue

The accepted clue `CLUE-robin-homotopy-separated-poisson-shear-estimate` was already narrowed by PF-275 and PF-276. PF-277 removes one more escape: PF-275 gives the raw mass-one fixed-row obstruction; PF-276 shows that `(I+R)^{-1}` cannot create an exact zero of the natural threshold coefficient functional; PF-277 shows that the normalized source transform is holomorphic across `±i` and that multiplication by `g_w(1+\xi^2)` produces a genuine nonremovable square-root branch germ there.

The remaining question is therefore the **discrete transfer theorem** from (21)--(22) to the large-degree corridor coefficients

\[
\langle e_{2j+\varepsilon},g_w(L)z^{(i)}\rangle.
\tag{23}
\]

A justified Darboux/Hilb/continuous-Hahn transfer should determine whether the branch germ forces the expected mass-one coefficient scale. PF-277 does not assume that implication; proving or refuting it remains the decisive step before the fixed-axis PF-271 route can be closed. The clue therefore remains `accepted`, not `resolved`.

## 6. Prior art and novelty audit

The analytic ingredients are classical. Hilb-type Jacobi asymptotics and their conversion to endpoint coefficient estimates go back to Darboux and Szegő. A modern explicit reference is Shuhuang Xiang, *Convergence Rates on Spectral Orthogonal Projection Approximation for Functions of Algebraic and Logarithmatic Regularities*, SIAM Journal on Numerical Analysis 59 (2021), 1374--1398, DOI `10.1137/20M134407X`, arXiv:2006.01522. Its Hilb formula supplies background for the normalized endpoint envelope (11); its sharper logarithmic coefficient theorems are not imported here.

General Fourier transforms connecting Gegenbauer/Jacobi systems with continuous Hahn polynomials are also established prior art; PF-274 isolates the exact equal-parameter specialization used by this line. Exponential decay implying holomorphic Fourier-Laplace continuation in a strip is classical.

A targeted search across these literatures found no source treating the PF-276 Robin-normalized column, its conserved generalized-zero-mode mass, or the deduction (9)--(22). No novelty is claimed for Gegenbauer bounds, Hilb asymptotics, Fourier-Laplace strip analyticity, or square-root branch algebra. The project-specific result is their combination with the exact PF-276 conservation law: the actual normalized source has enough endpoint decay to cross the mass-one threshold analytically, and its nonzero conserved moment becomes the nonzero coefficient of the nearest square-root Fourier branch.

No statement about zeta zeros or RH follows.

## 7. Boundaries and adversarial checks

1. **No large-degree asymptotic is claimed.** Equations (21)--(22) are local complex-frequency germs. Turning them into an asymptotic or lower bound for (23) still needs a justified continuous-Hahn/Gegenbauer Darboux or Tauberian transfer.
2. **No physical-space branch-tail theorem is smuggled in.** PF-277 does not assert an `e^{-|\tau|}|\tau|^{-3/2}` asymptotic for `g_w(L)z^{(i)}` merely from the square-root branch.
3. **The strip belongs to the source, not the full multiplier.** `\widehat Z_i` is holomorphic for `|\operatorname{Im}\xi|<2`; the finite-seam multiplier may have additional singularities above the mass-one edge.
4. **Fixed axis and fixed seam only.** No uniformity in `s`, corridor index, shear, hypercycle transport, canonical-tail parameters, or Robin homotopy follows.
5. **The `3/2` moment uses positivity.** Equation (9) depends on PF-276's positivity-improving inverse and weighted conservation law and is not asserted for an arbitrary normalized source.
6. **No cross-line evidence is used.** The derivation depends only on the local PF-273--PF-276 chain and classical external Jacobi/Fourier facts.

The result is falsified if PF-276's conserved weighted mass does not imply (9), if the normalized Gegenbauer envelope (11) fails with the PF-274 normalization, if the compactification factor in (15) has the opposite half-power, or if PF-276's threshold coefficient sums are not the Fourier-Laplace values (19)--(20) after the weighted convergence established here.

## Decisive next test

Prove or refute the coefficient-transfer theorem for the nonzero branch germs (21)--(22). The target is a two-endpoint Hilb/Darboux or continuous-Hahn statement for the special vector `z^(i)` strong enough to determine the asymptotic scale of (23), including the parity phase. The next finding must either derive the actual endpoint/coefficient asymptotic with controlled remainders or exhibit the exact mechanism by which the genuine nonzero Fourier branch fails to control the large-degree corridor coefficients.