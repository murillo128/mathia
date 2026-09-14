# PL-307 — Fractional Pohozaev identity recovers the completed-Weil boundary stress without a mixed Hadamard theorem

**Evidence:** `LITERATURE+EXACT-DERIVED + HADAMARD-GATE-REDUCTION + CONDITIONAL-POHOZAEV-REGULARITY`

**Status:** `SCALAR-STRESS-VIA-POHOZAEV + MIXED-HADAMARD-NOT-INDEPENDENT + BRANCH-REGULARITY-OPEN + ARITHMETIC-SIGN-OPEN`

## Claim

`PL-306` showed that, **if** the fractionalized localized-Weil eigenbranch admitted both a fixed-domain Feynman--Hellmann formula and a moving-domain mixed Hadamard formula, then the renormalized squared endpoint stress would be forced by the same lower-order aperture derivative already isolated in `PL-305`. The shape derivative is not actually needed to obtain that scalar stress identity.

Ros-Oton--Serra's fractional Pohozaev identity applies to any zero-exterior function satisfying their Proposition 1.6 regularity hypotheses; it does not require the right-hand side to be a scalar semilinearity once those hypotheses are available. Applied directly to a sufficiently regular eigenstate of the natural fractionalized localized-Weil operator, and combined only with the exact dilation covariance of the lower-order global Weil form, it yields the same finite-`s` virial identity that `PL-306` obtained conditionally from two eigenvalue-derivative representations.

Work on the fixed interval

\[
I=(-1,1)
\]

and on a source-static aperture interval. Let

\[
q_{a,s}(w)
=
\frac{a^{-2s}E_s(w)-\|w\|_2^2}{2s}
+c\|w\|_2^2+b_a(w),
\qquad
E_s(w)=\int_{\mathbb R}|\xi|^{2s}|\widehat w(\xi)|^2\,d\xi,
\]

be the regularization used in `PL-306`, where `b_a(w)=\langle B_aw,w\rangle` is the pulled-back prime/completion part of the global localized Weil form and `c` is aperture-independent. Let `w=w_{s,a}` be a real normalized eigenstate with eigenvalue `lambda_s(a)`. Assume:

1. `w` satisfies the hypotheses of Ros-Oton--Serra Proposition 1.6 on `I`, so its fractional boundary traces

\[
\tau_{s,a,\pm}
=
\left.\frac{w}{\delta_I^s}\right|_{\pm1}
\]

exist and the fractional Pohozaev identity is valid;
2. the lower-order form is differentiable at this fixed state and its dilation generator can be paired with `w`, equivalently

\[
\boxed{
2\operatorname{Re}\langle xw',B_aw\rangle
=-b_a(w)-a\,\partial_ab_a(w).
}
\tag{1}
\]

Then, without differentiating the eigenvalue branch and without assuming any Hadamard theorem for the mixed fractional/prime-shift operator,

\[
\boxed{
\frac{\Gamma(1+s)^2}{2s}
\Bigl(|\tau_{s,a,+}|^2+|\tau_{s,a,-}|^2\Bigr)
=
E_s(w_{s,a})
-a^{2s+1}\partial_ab_a(w_{s,a}).
}
\tag{2}
\]

Equation (2) is exactly equation (3) of `PL-306`, but its provenance is now different: it is a direct fractional Pohozaev/virial identity for the state, not a consequence of comparing Feynman--Hellmann and a mixed moving-boundary Hadamard law.

Consequently, if the regularized branch has a finite zero-order eigenvalue limit and the already-isolated source-structured derivative convergence holds,

\[
\partial_ab_a(w_{s,a})
\longrightarrow
\partial_ab_a(w_{0,a}),
\tag{3}
\]

then `E_s(w_{s,a}) -> 1` and

\[
\boxed{
\lim_{s\downarrow0}
\frac{|\tau_{s,a,+}|^2+|\tau_{s,a,-}|^2}{2s}
=
1-a\,\partial_ab_a(w_{0,a}).
}
\tag{4}
\]

If the zero-order simple branch also has the fixed-domain Feynman--Hellmann identity from `PL-305`, then

\[
\boxed{
1-a\partial_ab_a(w_{0,a})=-a\lambda_0'(a).
}
\tag{5}
\]

Thus the scalar squared boundary stress has a strictly shorter route than previously recorded. The live analytic gate is not "prove a new mixed fractional Hadamard theorem and independently compactify the boundary trace square." It is: establish enough **source-structured regularity for the actual completed-Weil regularized branch** to justify the existing fractional Pohozaev identity and the lower-order dilation derivative, then pass `partial_a b_a` through `s -> 0`. A signed/pointwise boundary trace, if desired, remains a separate and stronger object.

This does not prove the required branch regularity, does not prove an intrinsic logarithmic boundary trace, and supplies no rational-prime-specific sign law.

## 1. Ros-Oton--Serra supplies the required state identity

Ros-Oton and Serra prove the following general form of the fractional Pohozaev identity. If `u in H^s(R^n)` vanishes outside a bounded `C^{1,1}` domain, has the boundary/interior regularity listed in their Proposition 1.6, and `(-Delta)^s u` is bounded in the domain, then

\[
\int_\Omega (x\cdot\nabla u)(-\Delta)^s u\,dx
=
\frac{2s-n}{2}
\int_\Omega u(-\Delta)^su\,dx
-
\frac{\Gamma(1+s)^2}{2}
\int_{\partial\Omega}
\left(\frac{u}{\delta^s}\right)^2
(x\cdot\nu)\,d\sigma.
\tag{6}
\]

This is Proposition 1.6 of their 2014 paper. Its statement is a theorem about a function satisfying analytic hypotheses, rather than a theorem restricted to the semilinear equation used for their principal application.

For `I=(-1,1)` one has `n=1` and `x nu=1` at both endpoints, so (6) becomes

\[
\boxed{
\operatorname{Re}\int_I xw'(x)(-\Delta)^sw(x)\,dx
=
\frac{2s-1}{2}E_s(w)
-
\frac{\Gamma(1+s)^2}{2}
\Bigl(|\tau_{s,a,+}|^2+|\tau_{s,a,-}|^2\Bigr).
}
\tag{7}
\]

The real part is harmless for the present real eigenstate and records the form needed for a complex-state extension.

Equation (7) is the crucial bridge. Unlike a Hadamard theorem, it is a **fixed-domain state identity**. No differentiability of `a -> lambda_s(a)`, no Kato branch theorem, and no moving-domain shape derivative enter it.

The hypotheses matter. The theorem cannot be applied merely because `w` belongs to the fractional form domain. In particular, Suzuki's translated prime terms can transport the exterior boundary profile into interior source fronts, so the higher interior regularity in Proposition 1.6 must be verified for the actual eigen-equation rather than inferred from the pure fractional ground state. This is why (2) is classified conditionally on Pohozaev-admissibility rather than as an unconditional regularity theorem for the completed branch.

## 2. The eigen-equation converts Pohozaev into the Weil virial residual

The operator associated with `q_{a,s}` satisfies

\[
\left[
\frac{a^{-2s}(-\Delta)^s-I}{2s}
+cI+B_a
\right]w
=
\lambda_s(a)w.
\tag{8}
\]

Multiplying by `2s a^{2s}` gives

\[
(-\Delta)^sw
=
a^{2s}\bigl[1+2s(\lambda_s(a)-c)\bigr]w
-2s a^{2s}B_aw.
\tag{9}
\]

Set

\[
\alpha=a^{2s}[1+2s(\lambda_s-c)].
\]

Because the zero-exterior fractional state vanishes at the endpoints in the ordinary continuous representative supplied by the Pohozaev hypotheses and is normalized,

\[
\operatorname{Re}\int_I xw'w\,dx=-\frac12.
\tag{10}
\]

The lower-order global Weil form is aperture-independent before spatial dilation. If `u_a(y)=a^{-1/2}w(y/a)` is the physical state on `(-a,a)`, differentiating its lower quadratic form at fixed `w` gives the standard virial relation

\[
a\partial_ab_a(w)
=-b_a(w)-2\operatorname{Re}\langle xw',B_aw\rangle,
\tag{11}
\]

which is (1). This is simply the generator of the unitary dilation, not a prime-specific identity. It may equally be taken as the explicit regularity hypothesis needed for the following calculation.

Pairing (9) against `xw'` and using (10)--(11) yields

\[
\operatorname{Re}\int_I xw'(-\Delta)^sw
=-\frac{\alpha}{2}
+s a^{2s}\bigl(b_a(w)+a\partial_ab_a(w)\bigr).
\tag{12}
\]

The eigenvalue identity itself is

\[
\lambda_s
=
\frac{a^{-2s}E_s(w)-1}{2s}+c+b_a(w),
\tag{13}
\]

so

\[
\alpha
=E_s(w)+2s a^{2s}b_a(w).
\tag{14}
\]

Substitution in (12) cancels `b_a(w)` exactly:

\[
\boxed{
\operatorname{Re}\int_I xw'(-\Delta)^sw
=-\frac12E_s(w)
+s a^{2s+1}\partial_ab_a(w).
}
\tag{15}
\]

Equating (15) with the Ros-Oton--Serra right-hand side (7) gives

\[
-\frac12E_s+s a^{2s+1}\partial_ab_a
=
\frac{2s-1}{2}E_s
-
\frac{\Gamma(1+s)^2}{2}T_s,
\]

where

\[
T_s=|\tau_{s,a,+}|^2+|\tau_{s,a,-}|^2.
\]

Rearranging proves (2):

\[
\Gamma(1+s)^2T_s
=2s\left(E_s-a^{2s+1}\partial_ab_a\right).
\tag{16}
\]

No derivative of `lambda_s(a)` has appeared anywhere in the proof.

## 3. The zero-order stress limit now depends only on the existing state-side gate

For a normalized eigenstate,

\[
\lambda_s(a)
=
\frac{a^{-2s}E_s(w_{s,a})-1}{2s}+c+b_a(w_{s,a}).
\]

If `lambda_s(a)` and `b_a(w_{s,a})` stay bounded as `s downarrow 0`, then

\[
a^{-2s}E_s(w_{s,a})=1+O(s),
\]

hence

\[
E_s(w_{s,a})\to1.
\tag{17}
\]

Therefore (2) plus (3) gives (4) directly. The renormalized **sum of endpoint squares** is determined without first proving convergence of the individual quantities `s^{-1/2}tau_{s,a,pm}`.

`PL-305` already identifies the zero-order lower derivative on `C_0 cap BV_0`:

\[
\partial_ab_a(w)
=
2\sum_{\log n<2a}
\frac{\Lambda(n)\log n}{a^2\sqrt n}
\operatorname{Re}C_w'\!\left(\frac{\log n}{a}\right)
-
\iint_{I^2}
\kappa(a(x-y))w(y)\overline{w(x)}\,dx\,dy.
\tag{18}
\]

Thus the difficult `s -> 0` passage is exactly the state-side problem already isolated in `PL-299`--`PL-305`: obtain source-structured derivative-measure/BV control strong enough to pass the finitely many active autocorrelation slopes. The completion term is controlled by its bounded derivative kernel once the states converge strongly enough.

This is a genuine reduction of the accepted clue. `PL-306` still left the mixed Hadamard identity itself as an independent analytic obligation. For the scalar eigenvalue-relevant stress, (7)--(16) remove that obligation. A Pohozaev theorem already exists; what must be proved is that the completed-Weil state falls inside its admissible class and that the lower dilation pairing survives the zero-order limit.

## 4. What has and has not been removed

The reduction is deliberately narrow.

**The mixed Hadamard theorem is removed only for the scalar squared stress.** If one wants a signed boundary coefficient, a pointwise shape derivative for arbitrary deformations, or an intrinsic logarithmic boundary measure, the Djitte--Fall--Weth / Djitte--Sueur shape calculus remains relevant. Equation (2) sees only the sum of endpoint squares.

**Pohozaev regularity is not free.** Ros-Oton--Serra Proposition 1.6 asks for more than membership in `H^s_0(I)`: it includes global `C^s`, controlled interior Hölder regularity, a Hölder boundary quotient `w/delta^s`, and bounded `(-Delta)^sw`. The pure fractional principal branch has the required classical regularity, but the actual completed-Weil equation contains translated boundary profiles. No finding in this line currently proves the full hypotheses uniformly for `s -> 0`.

**The virial pairing is a real gate.** Formula (11) is exact when the unitary dilation generator can be paired with the lower-order operator. At zero order `PL-305` proves fixed-state aperture differentiability from `C_0 cap BV`; it does not by itself prove the finite-`s` pairing for every regularized completed-Weil state. A successful branch theorem must justify this pairing or an equivalent form-level dilation derivative.

**Source activations are not covered by the present finite-`s` derivation.** The claim is made on source-static aperture intervals. `PL-305` proves that at zero order a `C_0 cap BV` state makes prime-power activation first-order transparent, but the corresponding finite-`s` boundary/front regularity has not been audited here.

**There is still no arithmetic sign mechanism.** The identity is universal for any aperture-independent lower global quadratic form with the same dilation covariance. Rational-prime specificity enters only through the actual value and constraints on `partial_a b_a(w)`. Equation (4) therefore cannot by itself prevent the unique first crossing from `PL-268`.

## 5. Adversarial and novelty audit

The load-bearing external theorem is classical prior art: Xavier Ros-Oton and Joaquim Serra, *The Pohozaev identity for the fractional Laplacian*, Archive for Rational Mechanics and Analysis **213**(2) (2014), 587--628, DOI `10.1007/s00205-014-0740-2`, arXiv:`1207.5986`. Proposition 1.6 is precisely the general state-level identity used above; their semilinear equation is an application supplying its hypotheses, not a restriction built into the proposition.

The dilation-generator relation is standard virial calculus. The eigen-equation elimination from (9) to (16) is elementary exact algebra. No novelty is claimed for either ingredient separately. A structure-based search around fractional Pohozaev identities, nonlocal Schrödinger equations, fractional Hadamard formulae, and Suzuki's 2026 localized Weil operator did not locate this exact completed-Weil specialization, but search absence is not evidence of novelty.

The line-local mathematical delta is a **gate reduction**: `PL-306` required a new mixed Hadamard theorem in order to identify the finite-`s` stress. The existing Pohozaev identity already supplies the needed scalar boundary term after the regularized eigen-equation and the exact lower-order dilation covariance are inserted. Future work should therefore not spend effort proving a full moving-domain Hadamard theorem merely to recover the endpoint-square quantity that enters the scalar aperture derivative.

The most important adversarial control is universality. Replace the rational-prime shift weights by any fixed locally finite translation source for which the same lower global quadratic form and regularity hypotheses make sense. The derivation survives unchanged. Therefore neither (2) nor its zero-order limit is a rational-prime rigidity statement. Any RH-facing advance must still constrain the **value or sign** of the virial residual using the actual von Mangoldt source.

## Consequence for `prime_lattice`

The accepted zero-order boundary-stress route now has a shorter dependency chain. For the scalar quantity relevant to the lowest localized-Weil level, the target is

\[
\boxed{
\text{Pohozaev-admissible completed-Weil regularized state}
+\text{lower dilation derivative convergence}
\Longrightarrow
\text{zero-order squared boundary stress}.
}
\]

The source-structured compactness problem from `PL-299`--`PL-305` remains the central analytic gate: establish regularity/derivative-measure control for the **actual** fractionalized completed-Weil branch, not for arbitrary bounded perturbations. Once that is strong enough to justify (7), (11), and the limit in (3), the scalar boundary stress follows from (2) without a separate mixed-Hadamard or trace-square compactness theorem.

The arithmetic gate is unchanged and now even more explicit. One must show that the rational-prime source constrains

\[
1-a\partial_ab_a(w_{0,a})
\]

—or equivalently, when zero-order Feynman--Hellmann is available, `-a lambda_0'(a)`—in a way that excludes the unique finite zero crossing. Generic boundary calculus, generic dilation covariance, and generic source positivity do not do this.

## Dependencies and source

- `PL-268`: strict ground-level aperture monotonicity and unique first crossing if RH fails.
- `PL-293`--`PL-299`: zero-order boundary obstruction, renormalized stress normalization, and the pure-branch BV passage.
- `PL-300`--`PL-304`: generic perturbation/gap/`L^p`/measure routes do not provide the required BV compactness.
- `PL-305`: exact zero-order fixed-state lower aperture derivative on `C_0 cap BV_0`.
- `PL-306`: the same stress identity derived conditionally by comparing two eigenvalue-derivative formulas; superseded here only in its need for a mixed Hadamard theorem for the scalar square.
- Source `99` in `research/prime_lattice/SOURCES.md`: Ros-Oton--Serra, Proposition 1.6.