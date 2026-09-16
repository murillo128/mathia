# PL-329 — The endpoint source amplitude has a sharp square-root-log threshold for first-prime reflection

**Evidence:** `LITERATURE+EXACT-DERIVED + SOURCE-SELECTED-MECHANISM + SHARP-THRESHOLD + ROUTE-NARROWING`

**Status:** `UNIFORM-SOURCE-BOUND-ORIENTS-FIRST-PRIME-REFLECTION + SQRT-LOG-SOURCE-GROWTH-IS-CRITICAL + ACTUAL-EIGENBRANCH-SOURCE-GATE-OPEN + NO-RH-CONSEQUENCE`

## Precise claim

`PL-326` and `PL-327` isolate the first-prime activation

\[
a_\delta=\frac{\log2}{2}+\delta,
\qquad
L_\delta=\log\frac{a_\delta}{\delta}\to\infty,
\]

and show that the canonical critical boundary scale by itself does not orient the newly active reflected correlation

\[
H_\delta(g)=\int_0^{2\delta}g(t)g(2\delta-t)\,dt.
\]

A critical half-log moving-layer perturbation can reverse its sign while remaining small in the natural endpoint norms. The missing input was therefore not another generic regularity estimate, but a source-specific mechanism suppressing that antisymmetric layer.

The exact endpoint source equation from `PL-319`, together with the positive comparison mechanism of `PL-323`, supplies such a mechanism with a sharp quantitative threshold.

Fix `Q_0>log 4`. For each small `delta`, let a real endpoint profile `g_delta` on `[Q_0,infinity)` obey the exact logarithmic-Laplacian source identity

\[
F_\delta(Q)
=
2Qg_\delta(Q)
-\int_{Q_0}^{Q}g_\delta(P)\,dP
+H_{Q_0}g_\delta(Q)
+c_{Q_0}(Q)g_\delta(Q),
\tag{PL329-1}
\]

where `H_{Q_0}` and `c_{Q_0}` are exactly those of `PL-319`, and assume the uniform critical envelope

\[
|g_\delta(Q)|\le A Q^{-1/2}.
\tag{PL329-2}
\]

Set

\[
S_\delta:=\sup_{Q\ge Q_0}|F_\delta(Q)|.
\tag{PL329-3}
\]

Then there is a coefficient `C_delta`, determined by the source family itself, such that on a fixed sufficiently large tail

\[
\boxed{
|g_\delta(Q)-C_\delta Q^{-1/2}|
\le
\frac{K(1+S_\delta)}{Q}
+K e^{-\eta(Q-R)}
}
\qquad(Q\ge R),
\tag{PL329-4}
\]

with `K,eta,R` independent of `delta`. In particular `|C_delta|<=A`.

On the newly active physical layer `0<t<2delta`, with

\[
Q_\delta(t)=\log\frac{2a_\delta}{t},
\qquad
Q_\delta(t)\ge L_\delta,
\tag{PL329-5}
\]

write

\[
g_\delta(t)
=C_\delta Q_\delta(t)^{-1/2}+r_\delta(t).
\]

Then

\[
\boxed{
\|r_\delta\|_{L^2(0,2\delta)}
\lesssim
\sqrt\delta
\left(
\frac{1+S_\delta}{L_\delta}
+e^{-\eta L_\delta}
\right).
}
\tag{PL329-6}
\]

Since the positive critical profile has norm of order

\[
|C_\delta|\sqrt{\frac\delta{L_\delta}},
\]

the first-prime reflection is eventually positive whenever

\[
\boxed{
\frac{1+S_\delta}
{|C_\delta|\sqrt{L_\delta}}
\longrightarrow0.
}
\tag{PL329-7}
\]

Thus an aperture-uniform bounded source immediately orients the first crossing provided the leading coefficient does not collapse. More generally, source growth strictly below the scale `|C_delta| sqrt(L_delta)` is sufficient.

The scale is sharp in the class isolated by `PL-327`. Its critical sign-reversing bump has source amplitude

\[
\boxed{S_\delta\asymp\sqrt{L_\delta}}
\tag{PL329-8}
\]

when `C_delta` stays fixed and nonzero. The endpoint equation therefore amplifies exactly the dangerous half-log layer from state amplitude `L_delta^{-1/2}` to forcing amplitude `L_delta^{1/2}`. The obstruction of `PL-327` does not survive a sub-square-root-log source bound.

This is a source-selected sign mechanism, but it is not yet a theorem about the actual completed-Weil eigenbranch. The remaining branch-specific gate is to prove (PL329-7), or any stronger uniform source estimate implying it, across the operator-norm-discontinuous first-prime activation.

## 1. Integrating the exact source equation selects a unique critical coefficient

Put

\[
U_\delta(X)=\int_{Q_0}^{X}g_\delta(P)\,dP,
\qquad
V_\delta(X)=\int_{Q_0}^{X}U_\delta(Q)\,dQ.
\]

Move the bounded zeroth-order correction to the source,

\[
R_\delta(Q)=F_\delta(Q)-c_{Q_0}(Q)g_\delta(Q),
\]

and write

\[
A_\delta(X)=\int_{Q_0}^{X}R_\delta(Q)\,dQ,
\qquad
J_\delta(X)=\int_{Q_0}^{X}H_{Q_0}g_\delta(Q)\,dQ.
\]

Integrating (PL329-1) and using `U_delta'=g_delta` gives the exact identity

\[
\boxed{
2XU_\delta(X)-3V_\delta(X)
=A_\delta(X)-J_\delta(X).
}
\tag{PL329-9}
\]

The critical envelope (PL329-2) is exactly the regime treated by the conservative singular-kernel flux estimate in `PL-322`: the integrated `H_{Q_0}` contribution is bounded at a scale negligible compared with a linear source primitive. Since `c_{Q_0}` is bounded on every fixed tail,

\[
|A_\delta(X)-J_\delta(X)|
\le K_A(1+S_\delta)X
\tag{PL329-10}
\]

for `X` large, with the geometric constant independent of `delta`.

Because `V_delta'=U_delta`, (PL329-9) becomes

\[
\left(X^{-3/2}V_\delta(X)\right)'
=
\frac{A_\delta(X)-J_\delta(X)}{2X^{5/2}}.
\tag{PL329-11}
\]

The right side is absolutely integrable at infinity by (PL329-10). Therefore a finite coefficient `L_delta^*` exists and

\[
V_\delta(X)
=L_\delta^*X^{3/2}
+O\!\left((1+S_\delta)X\right),
\tag{PL329-12}
\]

uniformly in the family apart from the displayed source amplitude. Returning to (PL329-9),

\[
U_\delta(X)
=\frac{3L_\delta^*}{2}\sqrt X
+O(1+S_\delta).
\tag{PL329-13}
\]

Define

\[
C_\delta=\frac{3L_\delta^*}{4}.
\tag{PL329-14}
\]

Then

\[
U_\delta(X)=2C_\delta\sqrt X+O(1+S_\delta).
\tag{PL329-15}
\]

The original envelope forces `|C_delta|<=A`: otherwise the asymptotic primitive `2C_delta sqrt(X)` would eventually exceed the primitive allowed by `|g_delta(Q)|<=A Q^{-1/2}`.

This coefficient is not inserted by hand. It is selected by the integrated source equation. That distinction is important: `PL-326` allowed arbitrary families sharing a fixed endpoint germ, whereas here the zero-order source controls the primitive strongly enough to select the leading `Q^{-1/2}` mass.

## 2. Subtracting the selected profile produces a uniformly coercive residual equation

Set

\[
b_\delta(Q)=C_\delta Q^{-1/2},
\qquad
m_\delta(Q)=g_\delta(Q)-b_\delta(Q).
\]

The primitive of the residual satisfies, by (PL329-15),

\[
M_\delta(X):=\int_{Q_0}^{X}m_\delta(P)\,dP
=O(1+S_\delta).
\tag{PL329-16}
\]

The model profile has the exact cancellation

\[
2Qb_\delta(Q)
-\int_{Q_0}^{Q}b_\delta(P)\,dP
=2C_\delta\sqrt{Q_0}.
\tag{PL329-17}
\]

Subtracting it from (PL329-1) yields

\[
H_{Q_0}m_\delta(Q)+2Qm_\delta(Q)
=
F_\delta(Q)
-2C_\delta\sqrt{Q_0}
+M_\delta(Q)
-H_{Q_0}b_\delta(Q)
-c_{Q_0}(Q)g_\delta(Q).
\tag{PL329-18}
\]

On a fixed large tail the right side is bounded by

\[
K(1+S_\delta).
\tag{PL329-19}
\]

Indeed `|C_delta|<=A`, the model singular remainder `H_{Q_0}b_delta` is uniformly bounded there, (PL329-16) controls the residual primitive, and both `c_{Q_0}` and the critical envelope are harmless.

Now use the positive maximum-principle comparison from `PL-323`. Its proof uses the barrier `p(Q)=1/Q`, for which

\[
H_{Q_0}p(Q)+2Qp(Q)\ge1
\]

on a sufficiently large fixed tail, plus an exponentially decaying past-boundary barrier. The same argument is quantitative: if

\[
|H_{Q_0}m+2Qm|\le E,
\qquad m(Q)\to0,
\]

then

\[
|m(Q)|
\le \frac{K E}{Q}+K e^{-\eta(Q-R)}.
\tag{PL329-20}
\]

Here `m_delta(Q)->0` follows directly from the critical envelope and `b_delta(Q)->0`. Taking `E=K(1+S_delta)` proves (PL329-4).

This is the gain that generic logarithmic boundary regularity could not provide. Universal Dirichlet logarithmic-Laplacian theory naturally gives the critical `Q^{-1/2}` scale; the exact source relation improves the **residual after subtracting the selected critical profile** to `O((1+S_delta)/Q)`.

## 3. The source bound gives exactly the moving-layer estimate required by `PL-327`

On `0<t<2delta`, relation (PL329-5) implies that (PL329-4) is uniformly evaluated only at `Q>=L_delta`. Therefore

\[
|r_\delta(t)|
\lesssim
\frac{1+S_\delta}{L_\delta}
+e^{-\eta L_\delta},
\]

and hence (PL329-6).

For the critical base profile

\[
B_\delta(t)=C_\delta Q_\delta(t)^{-1/2},
\]

`PL-327` gives

\[
\|B_\delta\|_2^2
=(2+o(1))|C_\delta|^2\frac\delta{L_\delta},
\qquad
H_\delta(B_\delta)
=(2+o(1))C_\delta^2\frac\delta{L_\delta}>0.
\tag{PL329-21}
\]

Since reflection about `delta` is unitary,

\[
|H_\delta(B_\delta+r_\delta)-H_\delta(B_\delta)|
\le
2\|B_\delta\|_2\|r_\delta\|_2
+\|r_\delta\|_2^2.
\tag{PL329-22}
\]

The ratio of the leading error to the positive reserve is therefore

\[
O\!\left(
\frac{1+S_\delta}
{|C_\delta|\sqrt{L_\delta}}
\right)
+o(1),
\tag{PL329-23}
\]

and the quadratic residual error is smaller under the same hypothesis. Condition (PL329-7) proves eventual positivity.

This answers the precise generic obstruction of `PL-327`: the dangerous antisymmetric component can live at the canonical boundary scale only if the source is allowed to grow at least at square-root-log scale relative to the leading coefficient.

## 4. The square-root-log threshold is saturated by the critical sign-reversing family

The sharpness test is the counterfamily already used in `PL-327`. Fix nonzero `C`, choose a nonzero real smooth function

\[
\eta\in C_c^\infty((0,2)),
\qquad
\eta(2-s)=-\eta(s),
\]

and set

\[
r_\delta(t)=A L_\delta^{-1/2}\eta(t/\delta).
\tag{PL329-24}
\]

For `A` large enough relative to `C`, `PL-327` proves that

\[
H_\delta(B_\delta+r_\delta)<0
\]

for every sufficiently small `delta`, even though the perturbation respects the canonical half-log modulus and has vanishing endpoint-potential energy.

In endpoint coordinate, because

\[
\frac t\delta=2e^{-(Q-L_\delta)},
\]

the same bump has the form

\[
r_\delta(Q)
=A L_\delta^{-1/2}\psi(Q-L_\delta)
\tag{PL329-25}
\]

for a fixed smooth compactly supported profile `psi`. On its support `Q=L_delta+O(1)`. Apply the exact source operator in (PL329-1). The coercive term gives

\[
2Qr_\delta(Q)
=2A\sqrt{L_\delta}\,\psi(Q-L_\delta)
+O(L_\delta^{-1/2}).
\tag{PL329-26}
\]

The primitive term is only `O(L_delta^{-1/2})`. Translation invariance of the singular kernel on a remote fixed-width layer, up to an exponentially small lower-boundary truncation, gives

\[
H_{Q_0}r_\delta(Q)=O(L_\delta^{-1/2}),
\]

and the bounded zeroth-order correction has the same size. Consequently

\[
\boxed{
\|\Delta F_\delta\|_\infty
\asymp |A|\sqrt{L_\delta}.
}
\tag{PL329-27}
\]

The unperturbed critical model has bounded source, so the full sign-reversing family satisfies

\[
S_\delta\asymp\sqrt{L_\delta}
\tag{PL329-28}
\]

for fixed nonzero `A,C`.

Thus the sufficient source condition is sharp in scale. A source of size `o(sqrt(L_delta))` excludes the known critical sign-reversing layer when `C_delta` remains bounded away from zero; a source of exact order `sqrt(L_delta)` can support it. The mechanism is the `2Qm` coercive term in the endpoint equation: it magnifies an endpoint-state perturbation of critical amplitude `L_delta^{-1/2}` into a source perturbation of reciprocal critical amplitude `L_delta^{1/2}`.

## 5. Prior-art and novelty audit

The universal boundary exponent is prior art, not a current discovery. Hernández-Santamaría, López Ríos and Saldaña, recorded as source 97, prove the sharp `ell(dist)^{1/2}` boundary scale and a Hopf-type lower law for the Dirichlet logarithmic Laplacian. That theory explains why a whole-state estimate better than half-log cannot be expected generically. It does not provide the source-selected two-term family estimate (PL329-4), nor a first-prime reflection threshold.

The exact endpoint normal form (PL329-1) is internal prior work from `PL-319`; the integrated-flux control is from `PL-322`; and the positive barrier/comparison argument is from `PL-323`. The current mathematical delta is their **uniform parameter-family combination**: bounded source amplitude selects a critical coefficient, forces an `O(1/Q)` residual uniformly across the moving layer, and yields the explicit sign criterion (PL329-7). The second delta is the sharpness match to `PL-327`: its sign-reversing half-log layer necessarily costs source amplitude of order `sqrt(L_delta)`.

Targeted literature searches around logarithmic-Laplacian boundary expansions, boundary Harnack/quotient asymptotics, and source-dependent endpoint remainders did not locate a theorem with this moving-layer source-amplitude threshold. Absence of a search hit is not a novelty proof. The result is therefore stored as an exact derived mechanism assembled from audited ingredients, not as a claim of priority over all logarithmic-Laplacian literature.

Suzuki's localized Weil framework, recorded in source 56, supplies the RH-facing operator context and the arithmetic source activation, but does not supply this source-amplitude threshold. The criterion here is local and real-variable; rational-prime specificity enters through the location `a_0=(log2)/2` and through the actual completed-Weil source equation that must ultimately be shown to satisfy the bound.

## 6. Adversarial checks and remaining gate

**The actual eigenbranch is not yet covered.** For a completed-Weil eigenstate, the source is a scalar state term plus the continuous completion and the finitely active prime translations. It is plausible that a sufficiently strong uniform branch bound would imply `S_delta=O(1)`, but no such bound is proved here. The theorem is conditional on the exact source identity, critical envelope and the displayed source-amplitude condition.

**Coefficient collapse is not hidden.** The condition uses `|C_delta|` explicitly. A fixed-aperture Hopf theorem can give a nonzero leading coefficient for a positive state, but continuity of that coefficient through the first-prime activation has not been established. If `C_delta` collapses, a merely bounded source need not satisfy (PL329-7).

**Operator-norm continuity is unavailable.** `PL-285` proves that the compressed prime translation turns on discontinuously in operator norm at activation, even though strong/form continuity can survive. Therefore ordinary norm-continuous Kato perturbation theory cannot simply be invoked to propagate an `L^infty` state bound or a nonzero endpoint coefficient through `delta=0`.

**The threshold is family-relative, not an absolute source theorem.** The natural invariant is `(1+S_delta)/(|C_delta| sqrt(L_delta))`, not `S_delta` alone. The additive `1` accounts for the fixed geometric/model terms in the residual equation. For a branch with `|C_delta|>=c>0`, it reduces to the clean condition `S_delta=o(sqrt(L_delta))`.

**No full Weil positivity or RH consequence follows.** The theorem controls only the first newly active prime reflection near `a=(log2)/2`. It does not orient later prime or prime-power channels, prove positivity at arbitrary aperture, or establish Weil's criterion globally.

**No generic boundary-regularity shortcut is reintroduced.** `PL-327` remains sharp: half-log regularity alone cannot orient the crossing. The gain comes from the actual source equation and disappears if forcing is allowed to grow at the critical square-root-log scale.

## Consequence for the line

The first-prime frontier is now sharper than the regularity formulation of `PL-327`. The missing quantity is not an unspecified supercritical modulus. On the exact endpoint source equation there is a concrete sufficient and scale-sharp family condition:

\[
\boxed{
1+\|F_\delta\|_\infty
=o\!\left(
|C_\delta|\sqrt{\log(a_\delta/\delta)}
\right).
}
\tag{PL329-29}
\]

Under that condition the source itself suppresses the antisymmetric moving-layer mode strongly enough to preserve the positive first-prime reflection. The PL-327 counterfamily shows that replacing `o` by unrestricted `O` at the same square-root-log scale is impossible in this class.

The next useful theorem is therefore branch-specific: derive a uniform bound on the actual completed-Weil source and prevent collapse of `C_delta` through activation, or find another identity implying (PL329-29) directly. Because of `PL-285`, that step must use structure stronger than naive operator-norm continuity. If it succeeds, the first-prime sign gate closes by source coercivity rather than by generic boundary smoothness.

## Sources

- Hernández-Santamaría, López Ríos and Saldaña, *Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian*, source 97: sharp half-log boundary scale and Hopf lower law.
- Masatoshi Suzuki, localized Weil/logarithmic-Laplacian operator framework, source 56.
- `PL-285`: operator-norm discontinuity of newly activated compressed prime translations.
- `PL-319`: exact logarithmic endpoint source identity.
- `PL-322`: conservative integrated singular-kernel flux control at the critical profile scale.
- `PL-323`: positive tail comparison and `1/Q` barrier for the residual source equation.
- `PL-326`: fixed-aperture endpoint law does not orient the moving first-prime crossing.
- `PL-327`: sharp half-log reflection threshold and the antisymmetric critical counterfamily.