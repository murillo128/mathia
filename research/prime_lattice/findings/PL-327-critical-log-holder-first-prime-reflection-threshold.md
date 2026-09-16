# PL-327 — Half-log Hölder regularity is the exact generic threshold for orienting the first-prime reflection

**Evidence:** `LITERATURE+EXACT-DERIVED + SHARP-REGULARITY-THRESHOLD + ROUTE-NARROWING`

**Status:** `CRITICAL-HALF-LOG-REGULARITY-INSUFFICIENT + SUPERCRITICAL-RESIDUAL-MODULUS-SUFFICIENT + SOURCE-SELECTED-BOUNDARY-CONTROL-REQUIRED`

## Precise claim

`PL-326` proves that the fixed-aperture endpoint law `Qm(Q)->0` does not orient the newly active `p=2` reflection as the aperture approaches the first-prime threshold. The remaining natural regularity question is whether the **sharp logarithmic boundary modulus** of the Dirichlet logarithmic Laplacian can supply the missing moving-layer uniformity.

It cannot at its canonical exponent, and the failure is sharp.

Put

\[
b=\log2,
\qquad
a_\delta=\frac b2+\delta,
\qquad
L_\delta=\log\frac{a_\delta}{\delta},
\]

and write the odd-sector first-prime reflection in endpoint distance as

\[
H_\delta(g)
=\int_0^{2\delta}g(t)g(2\delta-t)\,dt.
\tag{PL327-1}
\]

Let

\[
\ell(r)=\frac1{\left|\log(\min\{r,0.1\})\right|}
\]

be the standard logarithmic modulus used in the sharp boundary theory, and define

\[
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

Then the following threshold statement holds.

### Supercritical residual modulus is sufficient

Suppose

\[
g_\delta=B_\delta+r_\delta,
\qquad
r_\delta(0)=0,
\qquad
[r_\delta]_{\alpha,\ell}\le M_\delta
\tag{PL327-4}
\]

for some `alpha>1/2`. If

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

for all sufficiently small `delta`.

In particular, a uniform supercritical residual estimate `[r_delta]_{alpha,ell}<=M` with any `alpha>1/2` orients the first-prime channel whenever `|C_delta|` stays bounded away from zero.

### The exponent `1/2` is sharp

For every `alpha<=1/2`, there are real residuals `r_delta` with

\[
r_\delta(0)=0,
\qquad
\sup_\delta [r_\delta]_{\alpha,\ell}<\infty,
\tag{PL327-7}
\]

which leave the endpoint coefficient in (PL327-3) unchanged but reverse the sign of `H_delta(B_delta+r_delta)` for all sufficiently small `delta`. At the critical exponent `alpha=1/2` the perturbation can be chosen on exactly the same pointwise boundary scale as the canonical logarithmic-Laplacian law,

\[
|r_\delta(t)|\lesssim \ell(t)^{1/2},
\tag{PL327-8}
\]

with

\[
\|r_\delta\|_2^2\asymp\frac{\delta}{L_\delta}\to0
\tag{PL327-9}
\]

and vanishing endpoint-potential energy `O(delta)`.

Thus the universal `ell^{1/2}` boundary regularity is not merely quantitatively too weak: **it is exactly the generic threshold at which an antisymmetric moving-layer component can compete at leading order with the canonical positive first-prime correlation.** A regularity proof can orient that channel only by gaining beyond `1/2` on the **residual after subtracting the critical profile**, or by using a stronger source-specific signed identity.

This is consistent with the optimality theorem of Hernández-Santamaría--López Ríos--Saldaña: their Dirichlet logarithmic-Laplacian theory supplies the `ell^{1/2}` boundary scale, and their Hopf lower law shows that a nontrivial nonnegative supersolution can genuinely saturate it. Hence a generic theorem placing the whole nonzero critical state in a supercritical zero-boundary class `ell^alpha`, `alpha>1/2`, is not available; the only plausible regularity gain is after removal of the leading `ell^{1/2}` profile.

## 1. The positive base correlation is exactly of critical size

Scale `t=delta s` in (PL327-3). Since

\[
\log\frac{2a_\delta}{\delta s}
=L_\delta+\log\frac2s,
\]

we have, for fixed nonzero `C_delta` and uniformly on compact subsets of `(0,2)`,

\[
B_\delta(\delta s)
=\frac{C_\delta}{\sqrt{L_\delta}}
\left(1+O\!\left(\frac1{L_\delta}\right)\right).
\tag{PL327-10}
\]

The endpoint singularities at `s=0,2` only make the corresponding factors smaller, so dominated convergence gives

\[
\boxed{
\|B_\delta\|_{L^2(0,2\delta)}^2
=\left(2+o(1)\right)
|C_\delta|^2\frac{\delta}{L_\delta},
}
\tag{PL327-11}
\]

and

\[
\boxed{
H_\delta(B_\delta)
=\left(2+o(1)\right)
C_\delta^2\frac{\delta}{L_\delta}>0.
}
\tag{PL327-12}
\]

This identifies the sign reserve that a moving-layer perturbation must beat. It is much smaller than an `O(delta)` layer energy: the critical boundary profile itself carries only `delta/L_delta` reflected mass.

## 2. A supercritical residual modulus implies the exact `PL-326` orientation scale

Assume (PL327-4). Since `r_delta(0)=0`, for `0<t<2delta`,

\[
|r_\delta(t)|
\le
M_\delta\ell(t)^\alpha
\le
C M_\delta L_\delta^{-\alpha},
\tag{PL327-13}
\]

where the constant is uniform for small `delta`. Therefore

\[
\boxed{
\|r_\delta\|_{L^2(0,2\delta)}
\le
C M_\delta\sqrt\delta\,L_\delta^{-\alpha}.
}
\tag{PL327-14}
\]

Compare this with the base scale from (PL327-11):

\[
\|B_\delta\|_2
\asymp
|C_\delta|\sqrt{\frac\delta{L_\delta}}.
\tag{PL327-15}
\]

The reflection `J_delta r(t)=r(2delta-t)` is unitary, so

\[
|H_\delta(B_\delta+r_\delta)-H_\delta(B_\delta)|
\le
2\|B_\delta\|_2\|r_\delta\|_2
+\|r_\delta\|_2^2.
\tag{PL327-16}
\]

Relative to (PL327-12), the first error is

\[
O\!\left(
\frac{M_\delta}{|C_\delta|}
L_\delta^{1/2-\alpha}
\right),
\tag{PL327-17}
\]

and the second is the square of that quantity. Condition (PL327-5) therefore makes the entire error `o(H_delta(B_delta))`, proving (PL327-6).

This recovers the abstract sufficient scale isolated in `PL-326`,

\[
\|r_\delta\|_2
=o\!\left(
|C_\delta|\sqrt{\frac\delta{L_\delta}}
\right),
\]

from a concrete boundary modulus. The gain needed is very small but precise: **any fixed logarithmic Hölder exponent strictly above `1/2` on the residual is enough.**

## 3. Critical half-log Hölder residuals can still reverse the sign

Choose a nonzero real

\[
\eta\in C_c^\infty((0,2)),
\qquad
\eta(2-s)=-\eta(s),
\tag{PL327-18}
\]

and fix `A in R`. For an arbitrary `alpha>0`, define

\[
r_\delta(t)
=A L_\delta^{-\alpha}\eta(t/\delta).
\tag{PL327-19}
\]

Because `eta` is supported away from `0` and `2`, the perturbation vanishes identically in an endpoint neighborhood for every fixed `delta`. It therefore leaves the coefficient `C_delta` in (PL327-3) unchanged.

More importantly,

\[
\boxed{
\sup_{0<\delta<\delta_0}
[r_\delta]_{\alpha,\ell}<\infty.
}
\tag{PL327-20}
\]

To see this, let `d=|t-s|`. The smooth scaled bump satisfies

\[
|r_\delta(t)-r_\delta(s)|
\le
C|A|L_\delta^{-\alpha}
\min\left\{1,\frac d\delta\right\}.
\tag{PL327-21}
\]

For `d>=delta`, `ell(d)^alpha` is bounded below by a constant multiple of `L_delta^{-alpha}`. For `d=delta x<delta`,

\[
\frac{|r_\delta(t)-r_\delta(s)|}{\ell(d)^\alpha}
\le
C|A|x
\left(
1+\frac{\log(1/x)}{L_\delta}
\right)^\alpha,
\tag{PL327-22}
\]

and the right side is uniformly bounded for `0<x<=1`; the exponential decay of `x=e^{-u}` dominates every fixed power of `1+u`. The same estimate covers pairs crossing the edge of the bump support because `eta` is smoothly compactly supported.

The reflection antisymmetry is exact:

\[
r_\delta(2\delta-t)=-r_\delta(t),
\]

hence

\[
\boxed{
H_\delta(r_\delta)
=-A^2\delta L_\delta^{-2\alpha}\|\eta\|_2^2.
}
\tag{PL327-23}
\]

The mixed term is much smaller. On the support of `eta`, expansion of (PL327-3) gives

\[
B_\delta(2\delta-t)-B_\delta(t)
=O\!\left(
|C_\delta|L_\delta^{-3/2}
\right),
\]

so

\[
H_\delta(B_\delta+r_\delta)
=H_\delta(B_\delta)
-A^2\delta L_\delta^{-2\alpha}\|\eta\|_2^2
+O\!\left(
|A C_\delta|\delta L_\delta^{-\alpha-3/2}
\right).
\tag{PL327-24}
\]

This gives the exact trichotomy.

If `alpha<1/2`, then `L_delta^{-2alpha}` dominates `L_delta^{-1}`. Every fixed nonzero `A` eventually makes the reflection negative.

If `alpha=1/2`, then both the positive base and the antisymmetric perturbation are of order `delta/L_delta`, and

\[
\boxed{
H_\delta(B_\delta+r_\delta)
=
\left(
2C_\delta^2-A^2\|\eta\|_2^2+o(1)
\right)
\frac\delta{L_\delta}.
}
\tag{PL327-25]
\]

For a fixed nonzero limiting or bounded coefficient, choosing `A` large enough reverses the sign while preserving a uniform critical half-log Hölder seminorm.

If `alpha>1/2`, the perturbation in (PL327-19) is lower order than the base correlation, in agreement with the general sufficient theorem of Section 2.

At the critical exponent, the perturbation is also small in the natural absolute layer norms:

\[
\|r_\delta\|_2^2
=A^2\frac\delta{L_\delta}\|\eta\|_2^2\to0,
\tag{PL327-26}
\]

while on its support `log(a_delta/t)=L_delta+O(1)`, so

\[
\int_0^{2\delta}|r_\delta(t)|^2
\log\frac{a_\delta}{t}\,dt
=O(A^2\delta)\to0.
\tag{PL327-27}
\]

Thus even the **critical regularity plus vanishing endpoint-potential energy** does not orient the arithmetic reflection.

## 4. Why the regularity gain must be residual rather than whole-state

Hernández-Santamaría--López Ríos--Saldaña prove that the canonical zero-exterior Dirichlet boundary scale for the logarithmic Laplacian is `ell(dist)^{1/2}`. Their positive torsion solution on sufficiently small balls has matching two-sided order, and their Hopf-type theorem gives the same lower order for a nontrivial nonnegative supersolution at an interior-sphere boundary point.

That sharpness has an immediate consequence for the present route. If a nontrivial positive/Hopf state `u` with zero exterior data satisfied a global supercritical logarithmic Hölder estimate

\[
|u(x)-u(y)|
\le C\ell(|x-y|)^\alpha,
\qquad
\alpha>\frac12,
\tag{PL327-28}
\]

then taking `y` immediately outside the boundary would give

\[
|u(x)|
=O\!\left(\ell(\operatorname{dist}(x,\partial I))^\alpha\right)
=o\!\left(\ell(\operatorname{dist}(x,\partial I))^{1/2}\right),
\]

contradicting the Hopf lower law. The same incompatibility is automatic whenever a nonzero coefficient `C_delta` in the critical profile (PL327-3) has already been established.

Therefore the sufficient condition in Section 2 must not be interpreted as a plausible **whole-state** regularity theorem. It is a theorem about the remainder after the leading critical boundary channel has been extracted. The analytically meaningful target is

\[
\boxed{
\text{critical }\ell^{1/2}\text{ leading profile}
+\text{ uniformly supercritical residual modulus},
}
\tag{PL327-29}
\]

or an equivalent source-selected estimate on the reflection-antisymmetric residual component.

This is exactly where arithmetic/source information would have to enter. Universal logarithmic-Laplacian boundary theory naturally stops at the exponent that is still insufficient.

## 5. Relation to the current first-crossing gate

The reflection decomposition makes the surviving target especially transparent. Let

\[
P_\pm=\frac12(I\pm J_\delta).
\]

Then

\[
H_\delta(g)
=\|P_+g\|_2^2-\|P_-g\|_2^2.
\tag{PL327-30}
\]

The canonical profile has positive reflected mass of order `delta/L_delta`. The critical counterfamily above inserts an antisymmetric component with exactly the same order of squared mass while respecting the sharp logarithmic boundary scale. Hence a generic endpoint regularity theorem cannot suppress `P_-` enough.

By contrast, a residual estimate with `alpha>1/2` forces

\[
\|P_-r_\delta\|_2
\le\|r_\delta\|_2
=O\!\left(
M_\delta\sqrt\delta L_\delta^{-\alpha}
\right)
=o\!\left(
|C_\delta|\sqrt{\frac\delta{L_\delta}}
\right),
\]

under (PL327-5), exactly the scale demanded by `PL-326`.

The next RH-facing analytic question is therefore narrower than “improve endpoint regularity.” It is:

\[
\boxed{
\text{Does the actual completed-Weil eigen-equation give a uniform }\alpha>1/2
\text{ logarithmic modulus for the residual, or directly suppress }P_-r_\delta?
}
\tag{PL327-31}
\]

Such a theorem would orient the first newly active rational-prime channel. It would still not prove Weil positivity or RH; one would then need to connect that local orientation to the actual lowest-eigenvalue first-crossing mechanism.

## Adversarial and novelty audit

- **The exponent `1/2` is literature, not new.** Source 97 supplies the optimal logarithmic-Laplacian boundary scale and Hopf lower law. The present finding uses that theorem only as the canonical regularity benchmark.
- **The reflection operator is prior art.** `PL-325` independently reconstructs the first-prime flip and audits the public prior-art implementation. No novelty is claimed for `J_delta` or its `+/-` sectors.
- **The line-specific delta is the threshold calculation.** Combining the shrinking arithmetic overlap with the canonical `ell^{1/2}` boundary scale gives the exact exponent test (PL327-5), the critical counterfamily (PL327-19), and the trichotomy across `alpha=1/2`.
- **The counterfamily is not an eigenstate.** It proves only that generic regularity at or below the canonical exponent cannot determine the sign. The actual source-coupled eigen-equation may impose additional constraints.
- **No supercritical regularity of the actual residual is claimed.** Equation (PL327-31) is the new falsifiable gate, not an established property.
- **Coefficient collapse remains a separate obstruction.** If `C_delta` tends to zero too quickly, condition (PL327-5) must be measured relative to that decay; a fixed regularity bound alone then need not provide a sign reserve.
- **This is only the first-prime local channel.** Positivity of `H_delta` immediately after activation does not imply positivity of the full odd Weil form, much less RH.
- **No Euler-product continuation enters.** Everything takes place inside the compactly supported localized Weil form and the real-variable logarithmic-Laplacian boundary coordinate.

A targeted literature audit around logarithmic-Laplacian boundary regularity, reflected/antisymmetric nonlocal estimates, localized Weil operators, and shrinking translation overlaps located the established boundary and maximum-principle machinery but not this exact moving-layer exponent threshold. Search absence is not treated as proof of novelty. The durable claim is the exact route boundary and sufficient residual scale, not a broad originality claim.

## Consequence for the research line

`PL-326` showed that fixed-aperture endpoint asymptotics do not commute with the first-prime threshold. `PL-327` now identifies the **sharp generic regularity exponent** behind that failure:

\[
\alpha<\frac12
\;\Rightarrow\;
\text{moving antisymmetric defects dominate},
\]

\[
\alpha=\frac12
\;\Rightarrow\;
\text{they compete at leading order},
\]

\[
\alpha>\frac12
\;\Rightarrow\;
\text{a uniform residual modulus suppresses them}.
\]

The universal Dirichlet logarithmic-Laplacian boundary theory lands exactly at the middle, non-orienting case. The next useful theorem must therefore be **source-selected**: either prove a supercritical logarithmic modulus for the residual after subtracting the forced `Q^{-1/2}` profile, or derive a direct signed/equation-level estimate on its reflection-antisymmetric component. Another generic boundary regularity theorem at the canonical half-log scale cannot change the first-crossing problem.

## Sources

- Víctor Hernández-Santamaría, Luis Fernando López Ríos, Alberto Saldaña, “Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian,” *Discrete and Continuous Dynamical Systems* **45**(1) (2025), 1--36. DOI `10.3934/dcds.2024084`; arXiv:`2401.18033`; source 97 in `research/prime_lattice/SOURCES.md`. Load-bearing prior art for the optimal `ell^{1/2}` boundary scale and Hopf lower law.
- `PL-293`: earlier use of the same optimal boundary scale to rule out generic zero-extension `H^{1/2}` regularity.
- `PL-319`--`PL-323`: exact endpoint source equation, forced critical profile, residual moment, and fixed-aperture `Qm(Q)->0` closure.
- `PL-324`: first-prime odd-sector order threshold.
- `PL-325`: exact first-prime reflection algebra and near-threshold endpoint-potential absorption.
- `PL-326`: moving-threshold counterfamily and the `o(|C_delta| sqrt(delta/L_delta))` sufficient orientation scale sharpened here into the exact logarithmic Hölder threshold.
