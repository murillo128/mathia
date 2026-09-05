# WP-164 — positive cyclotomic radial flux is never a positive semigroup coefficient

**Status:** `EXACT-DERIVED + DECISIVE-NARROWING + PRIME-CIRCLE-BRIDGE + RADIAL-FLUX + COMPLETE-MONOTONICITY-OBSTRUCTION + POSITIVE-SEMIGROUP-EXCLUSION + PRIME-POWER-MATCHED-CONTROL + SCALE-MIXTURE-STABILITY + PRIOR-ART-CLASSICALIZATION`.

`WP-161`--`WP-163` isolate an unusually sharp finite-place object. The intrinsic inward cyclotomic radial flux

\[
\rho_n(s)
:=
-\frac{d}{ds}\log\Phi_n(e^{-s}),
\qquad n>1,\ s>0,
\tag{1}
\]

has total mass `Lambda(n)`; it is pointwise positive on the whole radial half-line exactly when `n` is a prime power; and its Mellin scalarizations preserve Mangoldt support only at the critical unweighted exponent. That leaves a natural operator-positive escape: perhaps, on the prime-power shells where (1) is already positive, the radial parameter is secretly the time variable of a nonnegative self-adjoint semigroup, so that positivity of the flux is inherited from a positive spectral measure rather than imposed shellwise.

That escape fails exactly. For every `n>1`, `rho_n` is **not completely monotone**. Indeed the boundary jet derived in `WP-161` gives

\[
\boxed{
\rho_n^{(2k-1)}(0^+)
=
-\frac{B_{2k}}{2k}J_{2k}(n),
\qquad k\ge1,
}
\tag{2}
\]

and therefore

\[
\boxed{
\rho_n'''(0^+)
=
\frac{J_4(n)}{120}>0.
}
\tag{3}
\]

Complete monotonicity would require every odd derivative to be nonpositive on `(0,infinity)`. Since `rho_n` is analytic through the boundary, (3) implies `rho_n'''(s)>0` for all sufficiently small positive `s`. Thus no positive Borel measure `mu_n` on `[0,infinity)` can satisfy

\[
\rho_n(s)
=
\int_{[0,\infty)} e^{-s\lambda}\,\mu_n(d\lambda),
\tag{4}
\]

and, equivalently, there are no Hilbert space `H`, vector `v`, and nonnegative self-adjoint generator `A` for which

\[
\rho_n(s)=\langle v,e^{-sA}v\rangle.
\tag{5}
\]

The obstruction is especially meaningful on prime powers. `WP-162` proves `rho_{p^a}(s)>0` for every `s>0`, yet even this everywhere-positive source-native response is not the correlation function of a positive contraction semigroup. The smallest exact control is

\[
\boxed{
\rho_2(s)=\frac1{e^s+1}>0,
\qquad
\rho_2'''(0^+)=\frac18>0.
}
\tag{6}
\]

So pointwise radial positivity and operator/semigroup positivity are genuinely different structures here.

The failure is stable under every finite positive mixture of radial scales. If `a_j,c_j>0` and

\[
F_n(s)=\sum_{j=1}^m a_j\rho_n(c_js),
\tag{7}
\]

then

\[
\boxed{
F_n'''(0^+)
=
\frac{J_4(n)}{120}
\sum_{j=1}^m a_jc_j^3
>0,
}
\tag{8}
\]

so `F_n` is not completely monotone either. Positive rescaling or finite positive averaging of the canonical radial time therefore cannot manufacture the missing semigroup-positive origin.

This does not prove or disprove global Weil positivity. It closes one precise attempt to promote the strongest positive finite-shell phenomenon currently present in Prime Circle into an independent operator sign theorem. A surviving construction must change the operator before positivity is taken, use a genuinely coupled boundary/cohomological mechanism, or retain the signed radial data through finite--archimedean assembly rather than interpreting each shell as a positive semigroup correlation.

## 1. The exact boundary jet forces the wrong third-derivative sign

`WP-161` centers the outward radial potential by

\[
\mathcal R_n(s)
=
\log|\Phi_n(e^s)|
-\frac{\varphi(n)}2s
\tag{9}
\]

and derives the convergent local expansion

\[
\mathcal R_n(s)
=
\Lambda(n)
+
\sum_{k\ge1}
\frac{B_{2k}J_{2k}(n)}
{2k(2k)!}s^{2k}.
\tag{10}
\]

Cyclotomic reciprocity gives, for the inward potential of `WP-162`,

\[
G_n(s):=\log\Phi_n(e^{-s})
=
\mathcal R_n(s)-\frac{\varphi(n)}2s.
\tag{11}
\]

Since `rho_n=-G_n'`, equations (10)--(11) yield

\[
\boxed{
\rho_n(s)
=
\frac{\varphi(n)}2
-
\sum_{k\ge1}
\frac{B_{2k}J_{2k}(n)}
{2k(2k-1)!}s^{2k-1}.
}
\tag{12}
\]

Hence (2). The first terms are

\[
\boxed{
\rho_n(s)
=
\frac{\varphi(n)}2
-
\frac{J_2(n)}{12}s
+
\frac{J_4(n)}{720}s^3
+O(s^5).
}
\tag{13}
\]

In particular,

\[
\rho_n'(0^+)=-\frac{J_2(n)}{12}<0,
\qquad
\rho_n''(0^+)=0,
\qquad
\rho_n'''(0^+)=\frac{J_4(n)}{120}>0.
\tag{14}
\]

The first derivative therefore looks compatible with a decaying positive response, but the first nontrivial higher odd derivative has the opposite sign required by complete monotonicity. The failure is not marginal: because `B_{4j}<0` for every `j>=1`, equation (2) gives the infinite family

\[
\boxed{
\rho_n^{(4j-1)}(0^+)
=
-\frac{B_{4j}}{4j}J_{4j}(n)>0,
\qquad j\ge1.
}
\tag{15}
\]

Thus the third-derivative obstruction is the first member of an infinite boundary-sign mismatch.

## 2. Positive self-adjoint semigroup coefficients are completely monotone

Let `A>=0` be self-adjoint on a Hilbert space and `v` any vector. By the spectral theorem there is a positive measure `mu_v` on `[0,infinity)` such that

\[
\langle v,e^{-sA}v\rangle
=
\int_{[0,\infty)}e^{-s\lambda}\,\mu_v(d\lambda).
\tag{16}
\]

For every `s>0` and every integer `r>=0`, differentiation under the spectral integral is legitimate because `lambda^r e^{-s lambda}` is bounded after a harmless split of the exponential. Therefore

\[
\boxed{
(-1)^r\frac{d^r}{ds^r}
\langle v,e^{-sA}v\rangle
=
\int_{[0,\infty)}
\lambda^r e^{-s\lambda}\,\mu_v(d\lambda)
\ge0.
}
\tag{17}
\]

So every same-vector coefficient of a nonnegative self-adjoint semigroup is completely monotone. Conversely, the classical Hausdorff--Bernstein--Widder theorem says that a completely monotone function is precisely a Laplace transform of a positive measure, with the usual finiteness condition at each positive `s`.

Equation (3) contradicts (17) with `r=3` on a whole interval `0<s<delta_n`. Therefore (4)--(5) are impossible for every `n>1`.

This argument is stronger than observing that the Ramanujan expansion from `WP-162`,

\[
\rho_n(s)
=-\sum_{m\ge1}c_n(m)e^{-ms},
\tag{18}
\]

already has signed coefficients. In particular `c_n(n)=varphi(n)>0`, so the source-native discrete Laplace expansion contains the negative weight `-varphi(n)` at frequency `m=n`. The derivative test rules out not merely that canonical signed expansion but **any alternative positive representing measure**.

## 3. Prime powers give the decisive matched control

For a mixed-prime shell, `WP-162` already gives a simpler obstruction to (4): `rho_n` changes sign. The new information is therefore concentrated exactly where one might have hoped to inherit positivity, namely `n=p^a`.

For a prime power,

\[
\rho_{p^a}(s)
=
\frac{p^{a-1}}{e^{p^{a-1}s}-1}
-
\frac{p^a}{e^{p^as}-1}
>0.
\tag{19}
\]

So the function is positive, starts at `varphi(p^a)/2`, decreases initially, decays to zero, and integrates to `log p`. Those are exactly the first qualitative features one expects from a positive spectral relaxation. Nevertheless (3) gives

\[
\rho_{p^a}'''(0^+)
=
\frac{p^{4a}(1-p^{-4})}{120}>0,
\tag{20}
\]

which is forbidden by (17).

The case `n=2` removes all arithmetic complexity. Here

\[
\Phi_2(x)=x+1
\]

and hence

\[
\rho_2(s)=\frac{e^{-s}}{1+e^{-s}}=\frac1{e^s+1}.
\tag{21}
\]

It is strictly positive and strictly decreasing on the whole half-line, but

\[
\rho_2'''(0^+)=\frac18.
\tag{22}
\]

Thus neither mixed-prime cancellation nor a complicated cyclotomic coefficient pattern causes the semigroup failure. It already occurs on the simplest positive prime shell.

## 4. Positive scale mixing cannot repair the semigroup sign pattern

A natural attempt is to argue that the radial coordinate has no canonical unit and average several positive time rescalings before asking for a spectral representation. Let

\[
F_n(s)=\sum_{j=1}^m a_j\rho_n(c_js),
\qquad a_j,c_j>0.
\tag{23}
\]

Every summand preserves the source geometry and, on prime powers, preserves pointwise positivity. But differentiating at the boundary gives (8). Complete monotonicity again requires `F_n'''<=0`, so every nontrivial finite positive scale mixture fails.

The same conclusion obviously survives multiplication by a positive scalar or normalization by `rho_n(0^+)=varphi(n)/2`. Thus the obstruction is not a choice of units or amplitude.

For prime powers one can also integrate the flux and define the transported mass

\[
H_{p^a}(s)
:=
\int_0^s\rho_{p^a}(u)\,du.
\tag{24}
\]

This is positive and increasing, with limit `log p`. A Bernstein function is a nonnegative function whose derivative is completely monotone. Since `H_{p^a}'=rho_{p^a}` is not completely monotone, the cumulative positive transport is **not** a Bernstein function. Hence it cannot be interpreted as the Laplace exponent of a canonical positive subordinator either.

This last statement is an operator-category boundary, not a general ban on nonlinear transforms of `H` or `rho`. A non-Bernstein transformation may produce a positive operator, but then its sign no longer follows from the standard semigroup/subordination geometry and requires a new source-forcing argument.

## 5. Relation to WP-163: scalar radial positivity and semigroup positivity fail differently

`WP-163` classifies the canonical scale-homogeneous scalar readouts

\[
M_n(\alpha)
=
\int_0^\infty s^{\alpha-1}\rho_n(s)\,ds.
\tag{25}
\]

There the tradeoff is arithmetic support: `alpha=1` alone preserves the Mangoldt zeros, while `0<alpha<1` makes every shell positive and therefore fills in all mixed-prime zeros.

The present obstruction is different. It asks whether the **unscalarized positive prime-power profile itself** belongs to a standard operator-positive cone before any Weil assembly. The answer is no even for `n=2`. Thus moving from the critical scalar mass back to the whole positive radial profile does not reveal a hidden positive semigroup whose spectral theorem could serve as the independent sign mechanism.

The two results combine to narrow the direct radial route:

\[
\boxed{
\begin{array}{ll}
\text{critical net flux:}&\text{exact Mangoldt support, but mixed shells use signed cancellation},\\
\text{subcritical Mellin mass:}&\text{positive scalar, but full shell support},\\
\text{prime-power flux profile:}&\text{pointwise positive, but not semigroup/Laplace positive}.
\end{array}
}
\tag{26}
\]

No step here uses zeta-zero data or an RH-equivalent positivity functional.

## 6. Prior-art and novelty audit

The functional-analysis criterion is classical. René L. Schilling, Renming Song, and Zoran Vondraček, *Bernstein Functions: Theory and Applications*, 2nd ed., De Gruyter Studies in Mathematics 37 (2012), DOI `10.1515/9783110269338`, gives the Hausdorff--Bernstein--Widder representation of completely monotone functions, the characterization of Bernstein functions through completely monotone derivatives, and the standard subordination framework. René L. Schilling, *Subordination in the sense of Bochner and a related functional calculus*, Journal of the Australian Mathematical Society 64 (1998), 368--396, DOI `10.1017/S1446788700039239`, is a direct semigroup/functional-calculus reference. `WP-127` already uses this classical Bernstein/subordination machinery on the separate Gamma-Markov route.

The cyclotomic derivative input is also classicalized in `WP-161`: Lehmer's derivative formulas and the Herrera-Poyatos--Moree survey express the boundary logarithmic derivatives through Euler/Jordan-totient data. A targeted literature search for complete monotonicity or Bernstein-function classifications of this exact inward cyclotomic logarithmic derivative did not identify a direct theorem. That absence is **not** used as a novelty claim.

The branch-local contribution is the exact synthesis: the Prime-Circle radial object that `WP-162` singles out as an intrinsic prime-power positivity classifier lies outside the positive Laplace/semigroup cone for every shell, and the obstruction is already encoded in its source-forced Jordan-totient boundary jet. No theorem-level novelty is claimed for complete monotonicity or cyclotomic derivative formulas separately.

## 7. Scope and falsification boundary

The result rules out only a precise inherited-sign mechanism:

\[
\rho_n(s)=\langle v,e^{-sA}v\rangle,
\qquad A\ge0,
\tag{27}
\]

and its equivalent positive Laplace-measure representation, together with finite positive mixtures of radial time rescalings and the direct Bernstein-subordinator interpretation of the cumulative prime-power transport.

It does **not** rule out cross-vector semigroup coefficients, non-self-adjoint evolution, Krein/indefinite spectral measures, matrix-valued boundary responses, signed intermediate states, nonlinear source-forced transforms, cross-shell coupling, or a finite--archimedean operator formed before scalarization. In particular, it does not say that the signed family `rho_n` cannot be an input to a larger positive form. It says only that the positivity seen shellwise on prime powers is not already the shadow of the most direct positive self-adjoint semigroup geometry.

The easiest audit is equation (3). Any claimed positive-measure or same-vector semigroup realization of the unmodified `rho_n` must have `rho_n'''(s)<=0` for every `s>0`; the exact boundary expansion instead forces `rho_n'''>0` near zero. Any proposed finite positive scale mixture is killed by (8).

## 8. Consequence for the Weil-positivity search

The radial branch now has three independently located sign failures. Local curvature is positive but has Jordan-totient full support (`WP-161`). Exact global radial mass has Mangoldt support but mixed shells require signed cancellation (`WP-162`--`WP-163`). And the one place where the whole flux is pointwise positive — prime powers — does not inherit the spectral positivity of a nonnegative self-adjoint semigroup.

Therefore the next useful radial construction should **not** search for another shellwise positive norm or reinterpret `rho_{p^a}` as a relaxation kernel. It should preserve the signed finite radial profiles until they participate in a genuinely global operation, or derive a different coupled generator/domain/boundary object whose positivity theorem acts only after finite and archimedean data have been assembled. That is exactly the remaining category allowed by the canonical research mandate.