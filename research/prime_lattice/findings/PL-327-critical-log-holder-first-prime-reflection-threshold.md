# PL-327 — Half-log Hölder regularity is the exact generic threshold for orienting the first-prime reflection

**Evidence:** `LITERATURE+EXACT-DERIVED + SHARP-REGULARITY-THRESHOLD + ROUTE-NARROWING`

**Status:** `CRITICAL-HALF-LOG-REGULARITY-INSUFFICIENT + SUPERCRITICAL-RESIDUAL-MODULUS-SUFFICIENT + SOURCE-SELECTED-BOUNDARY-CONTROL-REQUIRED`

## Precise claim

`PL-326` shows that the fixed-aperture endpoint law `Qm(Q)->0` does not orient the newly active `p=2` reflection as the aperture approaches its threshold. The remaining natural regularity question is whether the sharp logarithmic boundary modulus of the Dirichlet logarithmic Laplacian can supply the missing moving-layer uniformity.

It cannot at its canonical exponent, and the failure is sharp.

Put

\[
b=\log2,
\qquad
a_\delta=\frac b2+\delta,
\qquad
L_\delta=\log\frac{a_\delta}{\delta},
\]

and write the first-prime reflection in endpoint distance as

\[
H_\delta(g)
=\int_0^{2\delta}g(t)g(2\delta-t)\,dt.
\tag{PL327-1}
\]

Let

\[
\ell(r)=\frac1{\left|\log(\min\{r,0.1\})\right|},
\qquad
[r]_{\alpha,\ell}
:=\sup_{s\ne t}
\frac{|r(t)-r(s)|}{\ell(|t-s|)^\alpha}.
\tag{PL327-2}
\]

For a boundary coefficient `C_delta`, set

\[
B_\delta(t)
=C_\delta
\left(\log\frac{2a_\delta}{t}\right)^{-1/2}.
\tag{PL327-3}
\]

If

\[
g_\delta=B_\delta+r_\delta,
\qquad
r_\delta(0)=0,
\qquad
[r_\delta]_{\alpha,\ell}\le M_\delta
\tag{PL327-4}
\]

with `alpha>1/2` and

\[
\boxed{
\frac{M_\delta}{|C_\delta|}
L_\delta^{1/2-\alpha}
\longrightarrow0,
}
\tag{PL327-5}
\]

then

\[
\boxed{H_\delta(g_\delta)>0}
\tag{PL327-6}
\]

for all sufficiently small `delta`. Thus a uniform supercritical residual estimate with any fixed `alpha>1/2` orients the first-prime channel whenever `|C_delta|` stays bounded away from zero.

Conversely, the exponent `1/2` is sharp. For every `alpha<=1/2` and every fixed nonzero boundary coefficient `C`, there are real residuals `r_delta` such that

\[
r_\delta(0)=0,
\qquad
\sup_\delta [r_\delta]_{\alpha,\ell}<\infty,
\tag{PL327-7}
\]

which leave the endpoint coefficient `C` unchanged but make `H_delta(B_delta+r_delta)<0` for all sufficiently small `delta`. At the critical exponent `alpha=1/2`, the perturbation can be chosen on the same pointwise boundary scale as the canonical logarithmic-Laplacian law,

\[
|r_\delta(t)|\lesssim\ell(t)^{1/2},
\qquad
\|r_\delta\|_2^2\asymp\frac\delta{L_\delta}\to0,
\tag{PL327-8}
\]

with endpoint-potential energy `O(delta)->0`.

Therefore the universal `ell^{1/2}` boundary regularity is exactly the generic threshold at which an antisymmetric moving-layer component can compete at leading order with the canonical positive first-prime correlation. A regularity proof can orient the channel only by gaining beyond `1/2` on the **residual after subtracting the critical profile**, or by using a stronger source-specific signed identity.

## 1. Critical size of the positive base reflection

Scale `t=delta s`. Since

\[
\log\frac{2a_\delta}{\delta s}
=L_\delta+\log\frac2s,
\]

a direct dominated-convergence calculation after factoring `C_delta` gives

\[
\boxed{
\|B_\delta\|_{L^2(0,2\delta)}^2
=\left(2+o(1)\right)
|C_\delta|^2\frac\delta{L_\delta},
}
\tag{PL327-9}
\]

and

\[
\boxed{
H_\delta(B_\delta)
=\left(2+o(1)\right)
C_\delta^2\frac\delta{L_\delta}>0.
}
\tag{PL327-10}
\]

The endpoint singularities at `s=0,2` only reduce the integrand and cause no domination problem. Thus the sign reserve is of order `delta/L_delta`, much smaller than a generic `O(delta)` layer energy.

## 2. Any supercritical residual modulus implies the `PL-326` orientation scale

From (PL327-4) and `r_delta(0)=0`, for `0<t<2delta`,

\[
|r_\delta(t)|
\le M_\delta\ell(t)^\alpha
\le C M_\delta L_\delta^{-\alpha}.
\]

Hence

\[
\boxed{
\|r_\delta\|_{L^2(0,2\delta)}
\le C M_\delta\sqrt\delta\,L_\delta^{-\alpha}.
}
\tag{PL327-11}
\]

By (PL327-9),

\[
\|B_\delta\|_2
\asymp
|C_\delta|\sqrt{\frac\delta{L_\delta}}.
\tag{PL327-12}
\]

The reflection `J_delta r(t)=r(2delta-t)` is unitary, so

\[
|H_\delta(B_\delta+r_\delta)-H_\delta(B_\delta)|
\le
2\|B_\delta\|_2\|r_\delta\|_2
+\|r_\delta\|_2^2.
\tag{PL327-13}
\]

Relative to (PL327-10), the first error is

\[
O\!\left(
\frac{M_\delta}{|C_\delta|}
L_\delta^{1/2-\alpha}
\right),
\]

and the second is the square of that quantity. Condition (PL327-5) therefore makes the perturbation `o(H_delta(B_delta))`, proving the sign claim.

This recovers the sufficient scale isolated abstractly in `PL-326`,

\[
\|r_\delta\|_2
=o\!\left(
|C_\delta|\sqrt{\frac\delta{L_\delta}}
\right),
\tag{PL327-14}
\]

from a concrete boundary modulus. Any fixed logarithmic Hölder exponent strictly above `1/2` on the residual is enough.

## 3. The half-log exponent is genuinely critical

Fix `C_delta=C ne 0`. Choose a nonzero real

\[
\eta\in C_c^\infty((0,2)),
\qquad
\eta(2-s)=-\eta(s),
\tag{PL327-15}
\]

and define, for fixed `A in R`,

\[
r_\delta(t)
=A L_\delta^{-\alpha}\eta(t/\delta).
\tag{PL327-16}
\]

Because `eta` is supported away from `0` and `2`, the perturbation vanishes identically in a neighborhood of the endpoint for every fixed `delta`, so it leaves the critical coefficient `C` unchanged.

It also satisfies

\[
\boxed{
\sup_{0<\delta<\delta_0}
[r_\delta]_{\alpha,\ell}<\infty.
}
\tag{PL327-17}
\]

Indeed, with `d=|t-s|`, smooth scaling gives

\[
|r_\delta(t)-r_\delta(s)|
\le
C|A|L_\delta^{-\alpha}
\min\left\{1,\frac d\delta\right\}.
\]

For `d>=delta`, the denominator `ell(d)^alpha` is at least a constant multiple of `L_delta^{-alpha}`. For `d=delta x<delta`, the quotient is bounded by

\[
C|A|x
\left(1+\frac{\log(1/x)}{L_\delta}\right)^\alpha,
\]

which is uniformly bounded because `x=e^{-u}` beats every fixed power of `1+u`. Smooth compact support handles pairs crossing the edge of the bump.

The reflection antisymmetry is exact:

\[
r_\delta(2\delta-t)=-r_\delta(t),
\]

so

\[
\boxed{
H_\delta(r_\delta)
=-A^2\delta L_\delta^{-2\alpha}\|\eta\|_2^2.
}
\tag{PL327-18}
\]

On the support of `eta`, expansion of the base profile gives

\[
B_\delta(2\delta-t)-B_\delta(t)
=O\!\left(|C|L_\delta^{-3/2}\right),
\]

and therefore

\[
H_\delta(B_\delta+r_\delta)
=H_\delta(B_\delta)
-A^2\delta L_\delta^{-2\alpha}\|\eta\|_2^2
+O\!\left(
|AC|\delta L_\delta^{-\alpha-3/2}
\right).
\tag{PL327-19}
\]

This yields the sharp trichotomy. If `alpha<1/2`, the negative term `delta L_delta^{-2alpha}` dominates the positive `delta/L_delta` base term, so every fixed nonzero `A` eventually reverses the sign. If `alpha=1/2`, the two terms have the same order and

\[
\boxed{
H_\delta(B_\delta+r_\delta)
=
\left(
2C^2-A^2\|\eta\|_2^2+o(1)
\right)
\frac\delta{L_\delta}.
}
\tag{PL327-20}
\]

Choosing `A^2||eta||_2^2>2C^2` makes the reflection negative for all sufficiently small `delta` while preserving a uniform critical half-log Hölder seminorm. If `alpha>1/2`, the same fixed-amplitude perturbation is lower order, in agreement with Section 2.

At `alpha=1/2`, the perturbation is small even in the natural absolute endpoint norms:

\[
\|r_\delta\|_2^2
=A^2\frac\delta{L_\delta}\|\eta\|_2^2\to0,
\]

and, because `log(a_delta/t)=L_delta+O(1)` on its support,

\[
\int_0^{2\delta}|r_\delta(t)|^2
\log\frac{a_\delta}{t}\,dt
=O(A^2\delta)\to0.
\tag{PL327-21}
\]

Thus critical regularity plus vanishing endpoint-potential energy still does not orient the arithmetic reflection.

## 4. The gain has to be on the residual, not on the whole critical state

Hernández-Santamaría--López Ríos--Saldaña prove that the canonical zero-exterior Dirichlet boundary scale for the logarithmic Laplacian is `ell(dist)^{1/2}`. Their positive torsion solution on sufficiently small balls has matching two-sided order, and their Hopf-type theorem gives the same lower order for nontrivial nonnegative supersolutions at an interior-sphere boundary point.

If such a positive/Hopf state `u` satisfied a global zero-boundary estimate

\[
|u(x)-u(y)|
\le C\ell(|x-y|)^\alpha,
\qquad
\alpha>\frac12,
\tag{PL327-22}
\]

then choosing `y` immediately outside the boundary would give

\[
|u(x)|
=O\!\left(\ell(\operatorname{dist}(x,\partial I))^\alpha\right)
=o\!\left(\ell(\operatorname{dist}(x,\partial I))^{1/2}\right),
\]

contradicting the Hopf lower law. The same incompatibility is automatic for any state already known to have a nonzero leading coefficient in (PL327-3).

Therefore Section 2 must not be read as a plausible generic **whole-state** regularity theorem. The useful target is

\[
\boxed{
\text{critical }\ell^{1/2}\text{ leading profile}
+\text{ uniformly supercritical residual modulus},
}
\tag{PL327-23}
\]

or an equivalent source-selected estimate on the reflection-antisymmetric residual component. Universal logarithmic-Laplacian boundary theory naturally stops exactly at the exponent that remains non-orienting.

## 5. The surviving first-crossing target

Let

\[
P_\pm=\frac12(I\pm J_\delta).
\]

Then

\[
H_\delta(g)
=\|P_+g\|_2^2-\|P_-g\|_2^2.
\tag{PL327-24}
\]

The canonical profile has positive reflected mass of order `delta/L_delta`. The critical counterfamily inserts an antisymmetric component with the same order of squared mass while respecting the sharp logarithmic boundary scale. A generic endpoint regularity theorem therefore cannot suppress `P_-` enough.

A residual estimate with `alpha>1/2`, by contrast, forces

\[
\|P_-r_\delta\|_2
\le\|r_\delta\|_2
=O\!\left(M_\delta\sqrt\delta L_\delta^{-\alpha}\right)
=o\!\left(
|C_\delta|\sqrt{\frac\delta{L_\delta}}
\right)
\]

under (PL327-5), exactly the scale demanded by `PL-326`.

The next RH-facing analytic question is therefore narrower than “improve endpoint regularity”:

\[
\boxed{
\text{Does the actual completed-Weil eigen-equation give a uniform }\alpha>1/2
\text{ logarithmic modulus for the residual, or directly suppress }P_-r_\delta?
}
\tag{PL327-25}
\]

Such a theorem would orient the first newly active rational-prime channel. It would still not prove Weil positivity or RH; a separate argument would have to connect that local orientation to the actual lowest-eigenvalue first-crossing mechanism.

## Adversarial and novelty audit

- **The exponent `1/2` is prior art.** Source 97 supplies the optimal logarithmic-Laplacian boundary scale and Hopf lower law. The present finding uses that theorem only as the canonical regularity benchmark.
- **The reflection algebra is prior art.** `PL-325` reconstructs the first-prime flip and audits the public prior-art implementation. No novelty is claimed for `J_delta` or its `+/-` sectors.
- **The line-specific delta is the moving-layer threshold calculation.** Combining the shrinking arithmetic overlap with the canonical `ell^{1/2}` scale gives the sufficient condition (PL327-5), the critical counterfamily (PL327-16), and the exact trichotomy across `alpha=1/2`.
- **The counterfamily is not an eigenstate.** It proves only that generic regularity at or below the canonical exponent cannot determine the sign. The actual source-coupled eigen-equation may impose additional constraints.
- **No supercritical actual residual regularity is claimed.** Equation (PL327-25) is the new falsifiable gate.
- **Coefficient collapse remains separate.** If `C_delta` tends to zero, the residual bound must beat the relative scale in (PL327-5); a fixed modulus alone may not provide a sign reserve.
- **This is only the first-prime local channel.** Positivity of `H_delta` immediately after activation does not imply positivity of the full odd Weil form, much less RH.
- **No analytic-continuation shortcut occurs.** Everything takes place inside the compactly supported localized Weil form and its real-variable endpoint coordinate.

A targeted literature audit around logarithmic-Laplacian boundary regularity, reflected/antisymmetric nonlocal estimates, localized Weil operators, and shrinking translation overlaps located the established boundary and maximum-principle machinery but not this exact moving-layer exponent threshold. Search absence is not treated as proof of novelty. The durable claim is the exact route boundary and sufficient residual scale, not a broad originality claim.

## Consequence for the research line

`PL-326` showed that fixed-aperture endpoint asymptotics do not commute with the first-prime threshold. `PL-327` identifies the sharp generic regularity exponent behind that failure:

\[
\alpha<\frac12
\Rightarrow
\text{moving antisymmetric defects dominate},
\]

\[
\alpha=\frac12
\Rightarrow
\text{they compete at leading order},
\]

\[
\alpha>\frac12
\Rightarrow
\text{a uniform residual modulus suppresses them}.
\]

The universal Dirichlet logarithmic-Laplacian boundary theory lands exactly at the middle, non-orienting case. The next useful theorem must therefore be source-selected: either prove a supercritical logarithmic modulus for the residual after subtracting the forced `Q^{-1/2}` profile, or derive a direct signed/equation-level estimate on its reflection-antisymmetric component. Another generic boundary regularity theorem at the canonical half-log scale cannot change the first-crossing problem.

## Sources

- Víctor Hernández-Santamaría, Luis Fernando López Ríos, Alberto Saldaña, “Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian,” *Discrete and Continuous Dynamical Systems* **45**(1) (2025), 1--36. DOI `10.3934/dcds.2024084`; arXiv:`2401.18033`; source 97 in `research/prime_lattice/SOURCES.md`. Load-bearing prior art for the optimal `ell^{1/2}` boundary scale and Hopf lower law.
- `PL-293`: earlier use of the same optimal boundary scale to rule out generic zero-extension `H^{1/2}` regularity.
- `PL-319`--`PL-323`: exact endpoint source equation, forced critical profile, residual moment, and fixed-aperture `Qm(Q)->0` closure.
- `PL-324`: first-prime odd-sector order threshold.
- `PL-325`: exact first-prime reflection algebra and near-threshold endpoint-potential absorption.
- `PL-326`: moving-threshold counterfamily and the `o(|C_delta| sqrt(delta/L_delta))` sufficient orientation scale sharpened here into the exact logarithmic Hölder threshold.
