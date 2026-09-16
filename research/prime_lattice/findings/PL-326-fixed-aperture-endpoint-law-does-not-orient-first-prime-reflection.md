# PL-326 — Fixed-aperture endpoint asymptotics do not orient the first-prime reflection across threshold

**Evidence:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + MOVING-THRESHOLD-UNIFORMITY-GATE`

**Status:** `POINTWISE-ENDPOINT-LAW-INSUFFICIENT + FIRST-PRIME-ORIENTATION-REQUIRES-UNIFORM/SOURCE-COUPLED-CONTROL`

## Precise claim

`PL-319`--`PL-323` close the fixed-aperture logarithmic endpoint-transfer problem for the actual source-coupled localized-Weil branch: after subtraction of the forced critical profile, the residual satisfies the pointwise moving-tail law `Qm(Q) -> 0`. `PL-324`--`PL-325` show that immediately after the first prime threshold the odd sector acquires an indefinite reflected `p=2` channel.

Those two facts do **not** combine into a sign theorem for that channel without an aperture-uniform estimate.

Let

\[
b=\log 2,
\qquad
a_\delta=\frac b2+\delta,
\qquad \delta>0,
\]

and let the odd-sector first-prime reflection functional on the positive half interval be

\[
H_\delta(f)
:=\int_{b-a_\delta}^{a_\delta}f(b-y)f(y)\,dy.
\tag{PL326-1}
\]

With endpoint distance `t=a_delta-y`, this is exactly

\[
\boxed{
H_\delta(g)=\int_0^{2\delta}g(t)g(2\delta-t)\,dt,
}
\tag{PL326-2}
\]

where `g(t)=f(a_delta-t)`. In Suzuki's odd half-line form the corresponding `p=2` arithmetic term is a positive scalar multiple of `H_delta`.

Fix any nonzero real boundary coefficient `C`. There exist two real continuous families `g_delta^+` and `g_delta^-` such that, for every sufficiently small fixed `delta`, both have **exactly the same endpoint germ**

\[
g_\delta^\pm(t)
=
C\left(\log\frac{2a_\delta}{t}\right)^{-1/2}
\qquad (0<t<c\delta)
\tag{PL326-3}
\]

for one fixed `c>0`, and hence both satisfy the strongest fixed-aperture version of the `PL-323` residual law: after subtracting the displayed critical profile, the residual is identically zero for all sufficiently large endpoint coordinate

\[
Q=\log\frac{2a_\delta}{t}.
\]

Nevertheless, for all sufficiently small `delta`,

\[
\boxed{
H_\delta(g_\delta^+)>0,
\qquad
H_\delta(g_\delta^-)<0.
}
\tag{PL326-4}

Moreover the perturbation changing the sign can be chosen with

\[
\|g_\delta^- - g_\delta^+\|_{L^2(0,2\delta)}^2=O(\delta)\to0
\tag{PL326-5}
\]

and with vanishing endpoint-potential cost

\[
\int_0^{2\delta}
\left|g_\delta^- - g_\delta^+\right|^2
\log\frac{a_\delta}{t}\,dt
=O\!\left(\delta\log\frac1\delta\right)\to0.
\tag{PL326-6}
\]

Thus neither the fixed-aperture `Qm(Q)->0` law nor absolute smallness in the natural endpoint-localized `L^2`/logarithmic weight controls the sign of the newly active prime reflection as the aperture approaches its threshold. A first-crossing argument must use a **uniform moving-layer estimate**, the actual source/eigen-equation, or another constraint that couples the state to the arithmetic channel.

## 1. The moving first-prime layer is a shrinking reflection interval

For `a_delta=b/2+delta`, the active odd reflection interval is

\[
b-a_\delta<y<a_\delta,
\]

which has width `2delta`. Put

\[
t=a_\delta-y.
\]

Then

\[
a_\delta-(b-y)=2a_\delta-b-t=2\delta-t,
\]

so the first-prime involution is simply

\[
J_\delta g(t)=g(2\delta-t)
\qquad(0<t<2\delta),
\tag{PL326-7}
\]

and `H_delta(g)=<g,J_delta g>`. The `+1` and `-1` reflection sectors of `PL-325` are therefore compressed into a layer whose physical width tends to zero, but whose sign geometry remains exact.

The boundary coordinate used in `PL-319`--`PL-323` after scaling the endpoint to `1` is

\[
Q=\log\frac{2a_\delta}{t}.
\tag{PL326-8}
\]

Hence the canonical critical boundary profile with coefficient `C` is

\[
B_\delta(t)
:=C\left(\log\frac{2a_\delta}{t}\right)^{-1/2}.
\tag{PL326-9}
\]

On the entire first-prime layer, if

\[
L_\delta:=\log\frac{a_\delta}{\delta},
\]

then `L_delta -> infinity` and

\[
|B_\delta(t)|\le \frac{|C|}{\sqrt{L_\delta}}
\qquad(0<t\le2\delta).
\tag{PL326-10}
\]

The pure boundary profile has positive reflected correlation. In fact

\[
H_\delta(B_\delta)>0,
\qquad
H_\delta(B_\delta)\asymp_C\frac{\delta}{L_\delta}.
\tag{PL326-11}
\]

The upper bound follows immediately from (PL326-10). For the lower bound, restrict to `t in [delta/2,3delta/2]`; both reflected distances then have logarithms `L_delta+O(1)`, uniformly as `delta->0`.

## 2. An antisymmetric interior bump reverses the sign without changing the endpoint germ

Choose a nonzero real function

\[
\eta\in C_c^\infty((0,2))
\]

with

\[
\eta(2-s)=-\eta(s).
\tag{PL326-12}
\]

For example, take a smooth bump `psi` supported in `(1/4,3/4)` and put `eta(s)=psi(s)-psi(2-s)`. There is a fixed `kappa>0` such that

\[
\operatorname{supp}\eta\subset[\kappa,2-\kappa].
\tag{PL326-13}
\]

For a fixed nonzero real amplitude `A`, define

\[
h_\delta(t)=A\eta(t/\delta),
\qquad
g_\delta^-(t)=B_\delta(t)+h_\delta(t),
\qquad
g_\delta^+(t)=B_\delta(t).
\tag{PL326-14}
\]

Because `h_delta(t)=0` for `0<t<kappa delta`, the two families agree **identically** in a full endpoint neighborhood at each aperture. In the coordinate (PL326-8), the residual of `g_delta^-` relative to `B_delta` is therefore exactly zero once

\[
Q>\log\frac{2a_\delta}{\kappa\delta}.
\tag{PL326-15}
\]

In particular it satisfies `Qm(Q)->0` much more strongly than merely asymptotically.

The reflection antisymmetry gives

\[
h_\delta(2\delta-t)=-h_\delta(t)
\]

and hence the exact negative contribution

\[
\int_0^{2\delta}
 h_\delta(t)h_\delta(2\delta-t)\,dt
=-A^2\delta\|\eta\|_2^2.
\tag{PL326-16}
\]

The mixed term is

\[
A\int_0^{2\delta}
\eta(t/\delta)
\bigl(B_\delta(2\delta-t)-B_\delta(t)\bigr)\,dt.
\tag{PL326-17}
\]

Using (PL326-10),

\[
|\text{mixed term}|
\le
\frac{2|AC|\delta\|\eta\|_1}{\sqrt{L_\delta}}
=o(\delta),
\tag{PL326-18}
\]

while

\[
0<H_\delta(B_\delta)
\le \frac{2C^2\delta}{L_\delta}=o(\delta).
\tag{PL326-19}
\]

Combining (PL326-16)--(PL326-19),

\[
H_\delta(g_\delta^-)
=-A^2\delta\|\eta\|_2^2+o(\delta)<0
\tag{PL326-20}
\]

for all sufficiently small `delta`, whereas `H_delta(g_delta^+)>0`. This proves (PL326-4).

A harmless cutoff away from `t=0` can extend both profiles to continuous functions on the full half interval with zero value at the odd center `y=0`; for small `delta` the cutoff is identically one on `0<t<2delta`, so none of the displayed reflection identities changes.

## 3. The sign-changing perturbation is absolutely small in the endpoint layer

Direct scaling gives

\[
\|h_\delta\|_2^2
=A^2\delta\|\eta\|_2^2,
\]

which proves (PL326-5).

On the support of `h_delta`, both `t/delta` and its reflected value stay in a compact subset of `(0,2)`. Therefore

\[
\log\frac{a_\delta}{t}
=\log\frac1\delta+O(1),
\]

uniformly there, and

\[
\int_0^{2\delta}|h_\delta(t)|^2
\log\frac{a_\delta}{t}\,dt
=O\!\left(\delta\log\frac1\delta\right)
\to0.
\tag{PL326-21}
\]

After scaling to `(-1,1)`, the endpoint potential used in `PL-325`,

\[
V(x)=-\frac12\log(1-x^2),
\]

has exactly this logarithmic size on the shrinking edge strip. Thus the counterfamily is compatible with the distinction already exposed there: a perturbation may disappear in absolute endpoint-localized mass while still dominating the much smaller signed correlation of the critical boundary profile.

No claim is made here that the perturbation is small in the **full** localized-Weil graph norm. The obstruction only needs the weaker and more precise statement that endpoint germ information plus absolute layer smallness does not determine the reflection orientation.

## 4. What uniform estimate would actually be strong enough

The calculation also identifies a quantitative sufficient scale. On `L^2(0,2delta)`, `J_delta` is unitary, so for

\[
g_\delta=B_\delta+r_\delta
\]

one has

\[
|H_\delta(g_\delta)-H_\delta(B_\delta)|
\le
2\|B_\delta\|_2\|r_\delta\|_2
+\|r_\delta\|_2^2.
\tag{PL326-22}
\]

Since

\[
\|B_\delta\|_2^2\asymp_C\frac{\delta}{L_\delta},
\qquad
H_\delta(B_\delta)\asymp_C\frac{\delta}{L_\delta},
\tag{PL326-23}
\]

a sufficient aperture-uniform condition for the positive boundary orientation to survive is

\[
\boxed{
\|r_\delta\|_{L^2(0,2\delta)}
=o\!\left(
|C|\sqrt{\frac{\delta}{L_\delta}}
\right).
}
\tag{PL326-24}
\]

The counterexample has `||h_delta||_2 asymp sqrt(delta)`, which tends to zero but misses (PL326-24) by a factor of order `sqrt(L_delta)`. This makes the missing quantifier explicit. A theorem proved separately at each fixed aperture is not enough; one needs control at the **moving first-prime layer scale**.

For an actual aperture-dependent boundary coefficient `C_delta`, the right-hand side of (PL326-24) must be scaled by `|C_delta|`. If that coefficient is not bounded away from zero at the threshold, even the leading critical profile supplies no uniform sign reserve.

## 5. Consequence for the live first-crossing program

The endpoint analysis of `PL-319`--`PL-323` remains valid and useful: it gives the correct fixed-aperture critical profile and closes the moving Green transfer for the actual eigenstate. The present result only blocks an unjustified quantifier exchange.

One cannot argue

\[
\text{fixed-}a\text{ endpoint law}
\quad\Longrightarrow\quad
\text{sign of the }p=2\text{ reflection as }a\downarrow\tfrac12\log2.
\]

The shrinking layer can carry an antisymmetric component that is invisible to the eventual endpoint germ at every fixed aperture but dominates the reflected correlation. Therefore a useful theorem must add at least one of:

- aperture-uniform boundary-layer control at a scale such as (PL326-24);
- a source/eigen-equation estimate that suppresses the antisymmetric moving-layer component;
- a different signed identity that controls `H_delta` directly rather than inferring it from endpoint asymptotics.

This sharpens the `PL-325` redirect. The missing information is not another description of the first-prime involution and not the existence of the critical logarithmic boundary law. It is a **uniform source-selected orientation theorem on the shrinking arithmetic overlap layer**.

## Adversarial and novelty audit

- **Not an eigenstate counterexample.** The families above are comparison functions. They do not solve Suzuki's eigen-equation and therefore do not show that the actual first-prime ground branch has either sign. Their purpose is exactly to prove that the endpoint law alone cannot decide that sign.
- **No conflict with `PL-323`.** For each fixed `delta`, the perturbation vanishes identically sufficiently close to the endpoint, so the `PL-323` pointwise residual law holds in its strongest possible form. The obstruction is the lack of uniformity as the aperture and the sampled boundary depth move together.
- **No conflict with endpoint absorption in `PL-325`.** The perturbation has vanishing absolute `L^2` and endpoint-potential mass. The reflection of the critical base profile is smaller, of order `delta/log(1/delta)`, so absolute smallness is not a relative sign estimate.
- **No analytic continuation is used.** The argument is entirely inside the finite first-prime layer of the already-localized Weil form.
- **No broad novelty claim.** Reflection involutions and logarithmic-Laplacian boundary profiles are established structures. A targeted literature search around logarithmic-Laplacian boundary asymptotics, localized Weil operators, and reflected/Hankel boundary correlations did not locate this moving-threshold counterfamily. The durable content is the exact line-specific quantifier obstruction and the sufficient scale (PL326-24), not a claim of a new general theorem about nonlocal operators.

## Sources

- `PL-319`--`PL-323`: fixed-aperture logarithmic endpoint source law, critical `Q^{-1/2}` profile, residual moment, and the exact pointwise `Qm(Q)->0` closure.
- `PL-324`: exact odd-sector Beurling--Deny threshold at the first rational-prime event.
- `PL-325`: first-prime reflection algebra, operator-norm jump, and near-threshold endpoint-potential absorption.
- Víctor Hernández-Santamaría, Luis Fernando López Ríos, Alberto Saldaña, *Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian*, Discrete Contin. Dyn. Syst. 45 (2025), 1--36, arXiv:`2401.18033`: established logarithmic-Laplacian boundary scale used upstream by `PL-319`--`PL-323`.
- Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:`2606.09096`: localized completed Weil form and finite prime-power translation source used upstream by `PL-324`--`PL-325`.
