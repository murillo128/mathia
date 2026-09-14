# PL-306 — Any Suzuki-compatible zero-order Hadamard law forces the boundary stress from the virial residual

**Evidence:** `EXACT-DERIVED + CONDITIONAL-HADAMARD-GATE-REDUCTION + NO-TRACE-EXISTENCE-CLAIM`

**Status:** `SQUARED-STRESS-NOT-INDEPENDENT + FIXED-DOMAIN-VIRIAL-MATCHING + BV-DERIVATIVE-GATE-REMAINS + SOURCE-SIGN-UNRESOLVED`

## Claim

The accepted zero-order Hadamard route has treated two small-order tasks as logically separate: control the derivative of the pulled-back Suzuki form, and independently prove compactness/uniqueness of the renormalized fractional boundary traces. They are not independent at the level that enters a Hadamard eigenvalue formula.

Let `I=(-1,1)` and, for `s>0`, consider the natural small-order regularization of the logarithmic principal form after unitary dilation from `(-a,a)` to `I`,

\[
q_{a,s}(w)
=
\frac{a^{-2s}E_s(w)-\|w\|_2^2}{2s}
+c\|w\|_2^2
+b_a(w),
\qquad
E_s(w)=\int_{\mathbb R}|\xi|^{2s}|\widehat w(\xi)|^2\,d\xi,
\]

where `b_a` denotes the exact lower-order pulled-back localized-Weil part and `c` is the aperture-independent scalar needed for the canonical normalization. For normalized `w`, the principal term converges to

\[
\int\log|\xi|\,|\widehat w(\xi)|^2d\xi-\log a,
\]

which is the logarithmic principal scaling used throughout `PL-285`--`PL-305`.

Fix an aperture `a` in a source-static interval and suppose a normalized simple regularized eigenbranch `w_{s,a}` satisfies the two identities that the Hadamard clue is trying to establish:

1. a fixed-domain Feynman--Hellmann identity

\[
\lambda_s'(a)
=
-a^{-2s-1}E_s(w_{s,a})
+\partial_a b_a(w_{s,a});
\tag{1}
\]

2. a moving-domain fractional Hadamard identity in which the ambient lower-order Weil term creates no independent boundary singularity,

\[
\lambda_s'(a)
=
-\frac{\Gamma(1+s)^2}{2s}
 a^{-2s-1}
\Bigl(|\tau_{s,a,+}|^2+|\tau_{s,a,-}|^2\Bigr),
\tag{2}
\]

where

\[
\tau_{s,a,\pm}
=
\left.\frac{w_{s,a}}{\delta_I^s}\right|_{\pm1}
\]

are the endpoint traces in fixed coordinates. The factor `a^{-2s-1}` is forced by unitary dilation: the physical trace on `(-a,a)` is `a^{-s-1/2}tau`.

Then comparison of (1) and (2) gives the exact finite-`s` virial identity

\[
\boxed{
\frac{\Gamma(1+s)^2}{2s}
\Bigl(|\tau_{s,a,+}|^2+|\tau_{s,a,-}|^2\Bigr)
=
E_s(w_{s,a})
-a^{2s+1}\partial_a b_a(w_{s,a}).
}
\tag{3}
\]

Consequently, if the regularized branch has a finite zero-order eigenvalue limit and the lower-order derivative converges,

\[
\partial_a b_a(w_{s,a})
\longrightarrow
\partial_a b_a(w_{0,a}),
\tag{4}
\]

then normalization and boundedness of `q_{a,s}(w_{s,a})` force `E_s(w_{s,a})->1`, and (3) yields

\[
\boxed{
\lim_{s\downarrow0}
\frac{|\tau_{s,a,+}|^2+|\tau_{s,a,-}|^2}{2s}
=
1-a\,\partial_a b_a(w_{0,a}).
}
\tag{5}
\]

`PL-305` gives, for every normalized zero-order state in `C_0 cap BV_0`,

\[
\partial_a q_a(w)
=-\frac1a+\partial_a b_a(w).
\tag{6}
\]

Thus, whenever the zero-order simple branch also satisfies Feynman--Hellmann,

\[
\boxed{
\lim_{s\downarrow0}
\frac{|\tau_{s,a,+}|^2+|\tau_{s,a,-}|^2}{2s}
=
-a\lambda_0'(a).
}
\tag{7}
\]

For the even branch relevant at `a=0.8`, `|tau_+|=|tau_-|`, so

\[
\boxed{
\lim_{s\downarrow0}
\frac{|\tau_{s,a}|^2}{s}
=
-a\lambda_0'(a)
=
1-a\,\partial_a b_a(w_{0,a}).
}
\tag{8}
\]

Therefore **compactness or pointwise convergence of the renormalized traces is not an independent gate for the squared Hadamard stress**. Once a valid fixed-`s` Hadamard formula and the source-structured convergence of the lower-order aperture derivative are proved, the squared stress and its zero-order limit are forced algebraically. What remains genuinely independent is existence of the mixed fractional/Weil Hadamard law itself, the `BV`/derivative-measure control needed for (4), and any signed or arithmetic information beyond the square in (7)--(8).

This is a gate reduction, not a logarithmic Hadamard theorem and not an RH mechanism.

## 1. The normalization and dilation factors are exact

The restricted fractional Dirichlet energy has Fourier normalization

\[
E_s(w)=\int|\xi|^{2s}|\widehat w(\xi)|^2d\xi.
\]

For the unitary dilation

\[
w(x)=a^{1/2}u(ax),
\]

one has

\[
E_s(u)=a^{-2s}E_s(w).
\]

Hence the small-order principal regularization on the moving interval is represented on the fixed interval by

\[
\frac{a^{-2s}E_s(w)-1}{2s}.
\]

Since

\[
a^{-2s}=1-2s\log a+o(s),
\qquad
|\xi|^{2s}=1+2s\log|\xi|+o(s),
\]

its zero-order limit is exactly

\[
\int\log|\xi|\,|\widehat w(\xi)|^2d\xi-\log a.
\]

Differentiating at fixed `w` gives

\[
\partial_a
\frac{a^{-2s}E_s(w)-1}{2s}
=-a^{-2s-1}E_s(w),
\tag{9}
\]

which is the first term in (1).

For the boundary quotient, if `delta_a(ax)=a delta_I(x)`, then

\[
\frac{u(ax)}{\delta_a(ax)^s}
=a^{-s-1/2}
\frac{w(x)}{\delta_I(x)^s}.
\]

A fractional Hadamard boundary square on the physical interval therefore acquires the factor `a^{-2s-1}` in (2). There is no adjustable normalization in (3).

As a control, set `b_a=0` and take the even positive principal fractional eigenstate on `I`. Exact scaling gives the familiar identity

\[
\Gamma(1+s)^2|\tau_s|^2=sE_s(w_s),
\]

so (3) reduces to the pure fractional interval formula already used to normalize the accepted Hadamard clue.

## 2. The trace-square limit follows from derivative convergence

Assume the normalized eigenvalue remains finite as `s->0` and `b_a(w_{s,a})` remains bounded. From

\[
\lambda_s(a)
=
\frac{a^{-2s}E_s(w_{s,a})-1}{2s}
+c+b_a(w_{s,a}),
\]

it follows that

\[
a^{-2s}E_s(w_{s,a})=1+O(s),
\]

hence

\[
E_s(w_{s,a})\to1.
\tag{10}
\]

If (4) holds, then the right-hand side of (3) converges to

\[
1-a\partial_a b_a(w_{0,a}).
\]

Since `Gamma(1+s)->1`, this proves (5). No compactness theorem for the endpoint quotient is used in this step. In particular, wildly oscillating signs of `s^{-1/2}tau_{s,a,pm}` would still be irrelevant to the eigenvalue Hadamard law as long as their squared sum is governed by (3).

For an even branch the endpoint magnitudes coincide, which turns (5) into (8). If the right-hand side is positive, the magnitude of the renormalized endpoint trace is therefore forced:

\[
\left|s^{-1/2}\tau_{s,a}\right|
\longrightarrow
\sqrt{-a\lambda_0'(a)}.
\]

This does **not** select the sign or phase of the trace, identify it with the coefficient of the logarithmic `ell(delta)^(1/2)` boundary law, or prove regularization independence of any signed boundary observable.

## 3. `PL-305` identifies exactly what still has to converge

Write the zero-order normalized localized-Weil form as

\[
q_a(w)=q^{\rm prin}_a(w)+b_a(w),
\]

with the principal dilation derivative `-1/a`. `PL-305` proves on `C_0 cap BV_0` that every lower-order term is classically differentiable at fixed state, including prime-power activations. Explicitly,

\[
\partial_a b_a(w)
=
2\sum_{\log n<2a}
\frac{\Lambda(n)\log n}{a^2\sqrt n}
\operatorname{Re}C_w'\!\left(\frac{\log n}{a}\right)
-
\iint_{I^2}
\kappa(a(x-y))w(y)\overline{w(x)}\,dx\,dy,
\tag{11}
\]

where `kappa(t)=r''(t)+t r'''(t)` is bounded at the origin. New prime-power channels enter both value and derivative with zero, so (11) remains compatible across a source activation.

Thus the only nontrivial passage required on the right-hand side of (3) is exactly the one already isolated by `PL-299`--`PL-305`: obtain source-structured `C_0+BV` or derivative-measure compactness for the **actual** regularized completed-Weil branch strongly enough that

\[
C'_{w_{s,a}}(\log n/a)
\to
C'_{w_{0,a}}(\log n/a)
\]

for the finitely many active prime powers. The completion contribution in (11) is easier because its derivative kernel is bounded on the compact difference range.

The important logical refinement is therefore:

\[
\text{mixed fractional Hadamard identity}
+
\text{source-structured derivative convergence}
\Longrightarrow
\text{zero-order squared boundary stress}.
\]

A separate compactness/uniqueness theorem for the squared stress is not required after those two inputs.

## 4. Adversarial checks

1. **Equation (2) is not proved here for the completed Weil perturbation.** The classical fractional Hadamard theorem proves the boundary formula for the pure fractional Dirichlet principal problem. Extending it to the regularized localized-Weil form, with its finite atomic translations and completed remainder, is still a genuine analytic obligation. The present finding starts *after* that identity has been established.
2. **Equation (1) is also a gate, not a free Kato consequence.** The prime-translation form is not differentiable in ambient operator norm. `PL-305` gives fixed-state differentiability on `C_0 cap BV_0`; using it on an eigenbranch still requires the source-structured regularity and a legitimate simple-branch Feynman--Hellmann passage.
3. **The result controls only a square.** A signed trace, a pointwise logarithmic boundary coefficient, or a boundary measure with more information can still require compactness/uniqueness. The gate reduction applies to the scalar boundary stress that actually enters the eigenvalue Hadamard formula.
4. **No hidden `H^{1/2}` is introduced.** The right-hand side of (11) is physical-space `BV` data plus a bounded completion kernel. `PL-297` already shows that finite renormalized Hadamard stress can coexist with divergent zero-extension `H^{1/2}` norm.
5. **The nonnegativity in (7) is not new positivity.** If the hypotheses hold, the right-hand side must be nonnegative because it is a limit of squares. Equivalently `lambda_0'(a)<=0`, consistent with the elementary variational monotonicity of the lowest eigenvalue under enlargement of the support interval. This supplies no ground-state sign theorem.
6. **The mechanism is not rational-prime-specific.** The algebraic matching works for any ambient lower-order perturbation admitting the same two derivative representations. Arithmetic content can enter only through the actual value and constraints on `partial_a b_a(w)`, not through the boundary-square identity itself.

## Prior-art and novelty audit

The fixed-order fractional Hadamard boundary formula and the small-order normalization of the pure principal branch are established prior art already recorded in the accepted local clue. Suzuki's moving-support localized Weil form and fixed-domain scaling are source 56 of `SOURCES.md`; `PL-305` supplies the exact lower-order fixed-state derivative used in (6) and (11). A targeted audit also found general Hadamard formulas for other classes of nonlocal integral eigenvalue problems, but no published theorem that directly supplies the mixed restricted-fractional plus atomic-prime-shift identity (2) for Suzuki's form.

No novelty is claimed for fractional Hadamard calculus, Feynman--Hellmann, or the scaling identities separately. The durable line-specific delta is the exact comparison (3): **if** the two derivative representations required by the clue are obtained, then the renormalized squared endpoint stress is algebraically pinned by the same lower-order virial derivative whose zero-order formula is already known from `PL-305`. That removes trace-square compactness as a third independent analytic gate and prevents future work from spending effort proving more boundary compactness than the eigenvalue shape law needs.

No new durable literature dependency is introduced, so `SOURCES.md` is unchanged.

## Consequence for the research line

The accepted Hadamard clue should now be attacked in the following narrower order. First prove a fixed-`s` shape formula for the **actual** fractionalized localized-Weil form and justify simple-branch Feynman--Hellmann on the same regularization. Second prove the source-structured `BV`/derivative-measure compactness needed to pass (11) through `s->0`. If those succeed, (3)--(8) automatically provide the zero-order squared boundary stress; an additional compactness theorem for `s^{-1/2}(u_s/delta^s)` is only needed if one wants a signed or pointwise boundary object beyond the eigenvalue derivative.

The hard arithmetic question is unchanged: even a perfectly defined stress gives only `-a lambda_0'(a)`. A useful RH mechanism still has to constrain that quantity through the rational-prime source strongly enough to control the first crossing of the localized Weil ground branch.