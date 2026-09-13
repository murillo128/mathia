# WI-275 — a harmonic minimax reserve is the sharp mass-only strengthening of simultaneous cuts

## Status

- **Evidence:** `EXACT-DERIVED + ELEMENTARY-MINIMAX + SOURCE-SPECIFIC-RIGIDITY + PRIOR-ART-AUDITED`.
- **Scope:** exact strengthening of the simultaneous-cut reserve in `WI-274` at the same attained first unrestricted localized Weil crossing. It uses the two cut inequalities of `WI-274` simultaneously through their pointwise minimax envelope instead of averaging them before integration.
- **What it does not claim:** this is not RH, does not yet show that the strengthened reserve exceeds the positive archimedean budget, does not force a prime-lag autocorrelation on a sign-changing mode, and does not assert that an actual first-crossing null mode realizes the minimax equality profile.
- **Novelty boundary:** the scalar inequality `max(Ax,B(1-x)) >= AB/(A+B)` is elementary. The Mathia deduction is its source-specific application to the complementary Suzuki cut energies, the resulting integrated harmonic reserve, its strict comparison with `WI-274`, and the identification of the exact barrier of the mass-partition relaxation. Targeted searches found no matching zeta/Weil first-crossing formulation. Search absence is not a priority claim.

## Claim

Use the notation and hypotheses of `WI-274`: `a=a_*` is an attained first unrestricted localized Weil crossing, `v` is a normalized real null mode, `Q_t` is the common energy of the two complementary sharp truncations, and

\[
M_L(t)+M_R(t)=1.
\]

For almost every `t\in(-a,a)`, put

\[
A_t:=\lambda_{(a+t)/2},
\qquad
B_t:=\lambda_{(a-t)/2}.
\]

Firstness and the two complementary truncations give the simultaneous inequalities

\[
Q_t\ge A_t M_L(t),
\qquad
Q_t\ge B_t M_R(t).
\tag{1}
\]

Since `A_t,B_t\ge0`, these imply the pointwise minimax bound

\[
\boxed{
Q_t\ge
\frac{A_tB_t}{A_t+B_t}
}
\tag{2}
\]

whenever `A_t+B_t>0`, with the right side defined as zero when both vanish.

Integrating and using the exact cut-counting identity from `WI-274`,

\[
\int_{-a}^{a}Q_t\,dt=\mathcal S_v,
\]

gives the strengthened saturated-source reserve

\[
\boxed{
\mathcal S_v\ge R_{\rm harm}(a)
:=2\int_0^a
\frac{\lambda_r\lambda_{a-r}}
{\lambda_r+\lambda_{a-r}}\,dr.
}
\tag{3}
\]

By symmetry,

\[
R_{\rm harm}(a)
=4\int_0^{a/2}
\frac{\lambda_r\lambda_{a-r}}
{\lambda_r+\lambda_{a-r}}\,dr.
\tag{4}
\]

This always dominates the reserve proved in `WI-274`:

\[
\boxed{
R_{\rm harm}(a)
-2\int_{a/2}^{a}\lambda_s\,ds
=
2\int_0^{a/2}
\frac{\lambda_{a-r}(\lambda_r-\lambda_{a-r})}
{\lambda_r+\lambda_{a-r}}\,dr
\ge0.
}
\tag{5}
\]

The inequality is strict whenever `\lambda_{a-r}>0` and `\lambda_r>\lambda_{a-r}` on a set of positive measure in `(0,a/2)`.

## 1. Exact pointwise minimax

Let `A,B\ge0` and `x\in[0,1]`. Then

\[
\max\{Ax,B(1-x)\}
\ge\frac{AB}{A+B}
\tag{6}
\]

for `A+B>0`. If

\[
x\ge\frac{B}{A+B},
\]

then `Ax\ge AB/(A+B)`; otherwise `B(1-x)>AB/(A+B)`. Equality occurs exactly at

\[
\boxed{x_* = \frac{B}{A+B}}
\tag{7}
\]

when `A,B>0`.

Applying this to

\[
A=A_t,
\qquad
B=B_t,
\qquad
x=M_L(t),
\]

and using `M_R(t)=1-M_L(t)` proves (2). This retains information discarded by the arithmetic averaging step

\[
2Q_t\ge A_tM_L(t)+B_tM_R(t)
\]

used in `WI-274`.

## 2. Integration gives the harmonic reserve

Set

\[
r=\frac{a+t}{2},
\qquad dt=2\,dr.
\]

Then `A_t=\lambda_r` and `B_t=\lambda_{a-r}`. Integrating (2) therefore gives

\[
\mathcal S_v
=\int_{-a}^{a}Q_t\,dt
\ge
2\int_0^a
\frac{\lambda_r\lambda_{a-r}}
{\lambda_r+\lambda_{a-r}}\,dr,
\]

which is (3). The integrand is invariant under `r\mapsto a-r`, giving (4).

No sign assumption on `v` enters. As in `WI-274`, all source signs and all prime/archimedean cancellation remain inside the exact saturated source `\mathcal S_v`; the new step concerns only how much firstness forces that source to carry.

## 3. Strict comparison with `WI-274`

For `0<r<a/2`, domain monotonicity gives

\[
A:=\lambda_r\ge B:=\lambda_{a-r}\ge0.
\]

The old reserve can be written

\[
2\int_{a/2}^{a}\lambda_s\,ds
=2\int_0^{a/2}B\,dr.
\]

Subtracting it from (4) yields pointwise

\[
4\frac{AB}{A+B}-2B
=2B\frac{A-B}{A+B},
\]

and hence (5).

Thus `WI-274` is recovered exactly in the flat case `A=B`, while any genuine asymmetry between the paired radii creates additional reserve. In the strongly asymmetric regime `A\gg B`, the local harmonic contribution approaches twice the old local contribution `2B`.

## 4. Equality profile and the mass-only barrier

The minimax step is sharp if the cut mass is allowed to vary subject only to the complementary-mass constraint. Its pointwise equality profile is

\[
\boxed{
M_L^*(t)
=
\frac{\lambda_{(a-t)/2}}
{\lambda_{(a+t)/2}+\lambda_{(a-t)/2}}.
}
\tag{8}
\]

As `t` increases, `\lambda_{(a+t)/2}` is nonincreasing and `\lambda_{(a-t)/2}` is nondecreasing. Therefore `M_L^*(t)` is nondecreasing. The basic CDF monotonicity requirement on a left-mass profile is consequently compatible with the minimax equality profile.

This gives a precise barrier statement: **monotonicity of the mass partition alone cannot improve the harmonic envelope.** If the spectral profile has jumps, the equality profile may fail to be the absolutely continuous CDF `M_L(t)=\int_{-a}^t v^2`; at the monotonicity-only relaxation level it can nevertheless be approximated in the integrated objective by monotone absolutely continuous profiles. Thus this statement is not an existence claim for a Suzuki null mode.

Any improvement beyond (3) must use information absent from the relaxation, for example regularity or differential constraints on the actual mass profile, the exact Suzuki null equation, the signed-source multiplier identities, or correlations between cuts that constrain `Q_t` beyond the two scalar lower bounds in (1).

## 5. Consequence for the active first-crossing clue

For a one-signed mode, `WI-274` bounded the prime-overlap contribution from below by its saturated-source reserve minus the finite positive archimedean budget

\[
K_+=\int_0^{h_0}h\,w(h)\,dh.
\]

The same argument now gives the sharper exact implication

\[
\boxed{
\mathcal P_v\ge R_{\rm harm}(a)-K_+.
}
\tag{9}
\]

Hence complete prime-lag screening on the one-signed branch is possible only if

\[
\boxed{R_{\rm harm}(a)\le K_+.}
\tag{10}
\]

The immediate quantitative target is therefore no longer the area `2\int_{a/2}^a\lambda_rdr`, but the paired-radius harmonic functional `R_{\rm harm}(a)`. If this still does not cross `K_+`, further progress cannot come from rearranging only the two complementary mass inequalities; it must use additional source/eigenfunction coupling.

## 6. Prior art and provenance

The localized Weil operator, first-crossing framework, and domain monotonicity come from Suzuki's localized Weil-form program, as already anchored in `WI-274` and `SOURCES.md`. The exact cut identities and simultaneous inequalities (1) are inherited from `WI-269`, `WI-270`, and `WI-274`.

The scalar minimax inequality (6) is elementary and is not claimed as new. A targeted audit around Suzuki/localized Weil first crossings, simultaneous cuts, harmonic-mean/minimax eigenvalue bounds, and source-saturation inequalities found no matching zeta-specific statement of (3)--(5) or the mass-relaxation barrier (8). No priority claim is made from search absence.

## 7. Audit and failure modes

The claim should be corrected or withdrawn if any of the following fails under the exact conventions of `WI-274`:

1. the two complementary inequalities in (1) are not simultaneously valid for almost every cut;
2. `\lambda_r` is not nonnegative for `0<r<a` or is not nonincreasing under domain inclusion;
3. the exact identity `\int Q_tdt=\mathcal S_v` used in `WI-274` has an omitted boundary or normalization term;
4. the change of variables introduces a missing factor of two;
5. the comparison in (5) fails because the paired-radius ordering is reversed.

All five checks are algebraic consequences of the already established `WI-274` setup, and the factor bookkeeping in (3)--(5) has been independently rederived. The finding remains only a strengthened necessary condition for a hypothetical first crossing; the decisive next test is whether rigorous information on `r\mapsto\lambda_r` makes `R_{\rm harm}(a)>K_+`, or whether an admissible spectral/mass profile can keep the harmonic reserve below that budget.