# PL-301 — Suzuki's exact lower-order remainder is uniformly BV-stable; only the finite prime shifts recycle variation

**Evidence:** `EXACT-DERIVED + POSITIVE-ROUTE-REFINEMENT + GATE-NARROWING`

**Status:** `BV-STABLE-REMAINDER + ARCHIMEDEAN-SMOOTHING + NO-BRANCH-BV-CLAIM`

## Claim

`PL-300` shows that generic norm-small bounded perturbations of the normalized fractional/logarithmic principal operator can inject arbitrarily large variation into an otherwise convergent simple ground branch. The exact bounded remainder in Suzuki's localized completed-Weil operator does **not** belong to that rough perturbation class.

Work on the scaled fixed interval

\[
I=(-1,1)
\]

and let `E` denote zero extension to `R`. As in `PL-291` and `PL-294`, Suzuki's localized operator can be written, after separating a scalar term,

\[
A_a=T+c_a I+P_a+R_a,
\]

where `T` is the one-dimensional logarithmic principal operator, the arithmetic term is the finite prime-power shift comb

\[
P_a u
=-\sum_{n\le e^{2a}}
\frac{\Lambda(n)}{\sqrt n}
\bigl(C_{h_n}u+C_{-h_n}u\bigr),
\qquad
h_n=\frac{\log n}{a},
\]

with

\[
C_hu(x)=1_I(x)\,(Eu)(x+h),
\]

and the continuous completion term is

\[
R_a u(x)
=-a\int_I r''(a(x-y))u(y)\,dy.
\]

Define

\[
BV_0(I)=\{u\in L^1(I):Eu\in BV(\mathbb R)\}.
\]

Then the following exact bounds hold.

For every `h` with `|h|<=2`,

\[
\boxed{
\|C_hu\|_{L^1(I)}\le \|u\|_{L^1(I)},
\qquad
\operatorname{TV}(EC_hu)
\le \operatorname{TV}(Eu).
}
\]

Consequently

\[
\boxed{
\operatorname{TV}(EP_au)
\le
2W(a)\operatorname{TV}(Eu),
\qquad
W(a)=\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n}.
}
\]

The archimedean completion is strictly better from the BV point of view. For every compact aperture interval `J=[a_-,a_+] subset (0,infinity)` there is `C_J<infinity` such that

\[
\boxed{
\|R_au\|_{L^1(I)}+
\operatorname{TV}(ER_au)
\le C_J\|u\|_{L^1(I)}
\qquad(a\in J).
}
\]

Thus, after absorbing `c_a` into the spectral parameter, the exact lower-order remainder satisfies the Lasota--Yorke-type estimate

\[
\boxed{
\operatorname{TV}\!\bigl(E(P_a+R_a)u\bigr)
\le
2W_J\operatorname{TV}(Eu)+C_J\|u\|_1,
}
\]

where

\[
W_J=\sum_{n\le e^{2a_+}}\frac{\Lambda(n)}{\sqrt n}.
\]

The estimate is uniform across prime-power activation thresholds as a **boundedness** statement: inactive lags have disjoint support and give the zero operator. It does not assert BV-operator-norm continuity at an activation.

This removes the rough-remainder mechanism used in `PL-300`. The actual completion cannot create arbitrarily fine variation from a bounded `L^1` input, and each active arithmetic channel can only transport/truncate variation already present. The remaining uniform-BV problem is therefore genuinely a coupled problem for the logarithmic/fractional principal operator and the finite shift comb; it is not an uncontrolled regularity problem in Suzuki's archimedean completion.

## 1. A compressed translation is total-variation nonexpansive

Let `U=Eu in BV(R)` and first take `0<=h<=2`. The function

\[
x\mapsto U(x+h)
\]

is a translate of `U`, hence has the same total variation. Multiplication by `1_I` removes the part with `x<-1`. After the change of variable `y=x+h`, this is exactly a one-sided truncation of `U` at

\[
y=-1+h.
\]

A one-sided truncation of a BV function that vanishes at `-infinity` cannot increase total variation. Indeed, the new jump from zero to the retained right trace is bounded by the variation of the discarded part plus the original jump at the cut, while the variation on the retained half-line is unchanged. Therefore

\[
\operatorname{TV}(EC_hu)\le\operatorname{TV}(U).
\]

The `L^1` bound is immediate because only part of a translate is retained. The case `-2<=h<=0` is the reflected argument. At `|h|=2` the supports meet only on a null set, so the operator is zero on `L^1`; for `|h|>2` it is also zero.

This argument uses the total variation of the **zero extension**, so endpoint jumps are already included. No continuity or zero trace of `u` at `+-1` is required.

Applying the bound to every channel in Suzuki's finite arithmetic sum and using the triangle inequality gives

\[
\operatorname{TV}(EP_au)
\le
\sum_{n\le e^{2a}}
\frac{\Lambda(n)}{\sqrt n}
\left(
\operatorname{TV}(EC_{h_n}u)
+
\operatorname{TV}(EC_{-h_n}u)
\right),
\]

which is the stated `2W(a)` estimate.

## 2. The continuous completion maps `L^1` directly into `BV`

The regularity needed here is already implicit in the decomposition audited in `PL-291`. Suzuki writes `r=r_0+r_1`, with `r_0` smooth and, for `t>0`,

\[
r_1''(t)
=
\frac{e^{-t/2}}{1-e^{-2t}}-\frac1{2t},
\]

whose expansion at the origin is

\[
r_1''(t)
=
\frac14-\frac{t}{48}-\frac{t^2}{32}+O(t^3).
\]

The kernel entering the Weil form is even. Hence its continuation through zero has at worst a finite `|t|` cusp in `r''`; in particular `r''` is locally Lipschitz. Away from zero it is smooth.

Fix `J=[a_-,a_+] subset (0,infinity)`. There are therefore finite constants

\[
M_0(J)=\sup_{|t|\le2a_+}|r''(t)|,
\qquad
M_1(J)=\operatorname*{ess\,sup}_{|t|\le2a_+}|r'''(t)|.
\]

For `x in I`,

\[
|R_au(x)|
\le a_+M_0(J)\|u\|_1,
\]

and almost everywhere

\[
|R_a'u(x)|
\le a_+^2M_1(J)\|u\|_1.
\]

Thus `R_au` is absolutely continuous on `I` with a uniform derivative bound. The total variation of its zero extension is its interior variation plus the two endpoint jumps, so

\[
\operatorname{TV}(ER_au)
\le
2a_+^2M_1(J)\|u\|_1
+2a_+M_0(J)\|u\|_1.
\]

The same sup-norm estimate gives the required `L^1` bound. This proves uniform `L^1 -> BV_0` smoothing of the continuous completion on compact aperture ranges.

The scalar `c_a I` is irrelevant to the regularity question and can be absorbed into the eigenvalue in the branch equation.

## 3. What this does and does not remove from the `PL-300` obstruction

The counterexample in `PL-300` exploits rank-two perturbations whose `L^2` norms tend to zero while their ranges contain packets at frequencies `K_j -> infinity`. Acting on the tracked low state they create a component with small amplitude but total variation of order `K_j` times that amplitude. Such a family is not uniformly bounded in the BV transport sense proved above.

Suzuki's exact lower-order operator has the opposite structure. The continuous completion creates a uniformly BV output from `L^1`, while the discrete prime terms are finite one-sided translations/truncations that do not increase variation channel by channel. Thus the specific high-frequency injection used by `PL-300` cannot be hidden inside the actual remainder.

This is nevertheless **not** a proof that the regularized completed-Weil ground states have uniformly bounded variation. The estimate is circular at that level: the finite prime comb is bounded by a constant times the input variation. A large-variation eigenstate is not excluded merely because the remainder is BV-stable.

The point is to locate the remaining gate. Uniform BV must now come from a coercive or variation-diminishing property of the principal fractional/logarithmic equation coupled to those finite translations, from a cancellation in the actual eigen-equation, or from a source-specific resolvent estimate. No additional regularity theorem for `r''` is needed to control the completion term.

## 4. The crude BV coefficient is not a contraction at the certified `a=0.8` endpoint

At `a=0.8`,

\[
e^{2a}=e^{1.6}<5,
\]

so the active prime powers are exactly `n=2,3,4`. Therefore

\[
W(0.8)
=
\frac{\log2}{\sqrt2}
+
\frac{\log3}{\sqrt3}
+
\frac{\log2}{2}
\approx1.4709867626,
\]

and the triangle estimate gives

\[
2W(0.8)\approx2.9419735252>1.
\]

The next source activation is

\[
a=\frac{\log5}{2}\approx0.8047189562.
\]

Hence the present estimate cannot be closed by a trivial BV contraction argument near the strongest certified positive endpoint from `PL-284`. Any useful uniform-variation theorem there must exploit the principal operator, cancellation between channels, the actual ground-state structure, or a sharper coupled norm than termwise total variation.

This numerical check is only diagnostic. The fact that the coarse coefficient exceeds one does not prove that the true branch has increasing variation or that no sharper estimate exists.

## 5. Adversarial and novelty audit

**The individual BV facts are classical/elementary.** Translation invariance of total variation, one-sided truncation estimates, and convolution regularization are standard. No novelty is claimed for those facts in isolation.

**The line-local delta is structural.** Suzuki supplies the exact completed-Weil decomposition; `PL-291` exploited it on logarithmic Fourier scales; `PL-300` then showed why generic bounded-perturbation convergence cannot provide the uniform BV compactness required by the accepted zero-order Hadamard clue. The present result checks the actual Suzuki remainder against that failure mode and proves that its two non-scalar pieces satisfy a uniform BV transport/smoothing inequality. A structure-based literature search around Suzuki's 2026 operator, bounded variation, fractional/logarithmic eigenfunction regularity, and truncated translations did not locate this specific estimate or a theorem already closing the resulting completed-Weil branch problem. Search absence is not treated as proof of novelty.

**No arithmetic rigidity follows from BV stability.** The contraction estimate for a compressed shift is independent of the special lags `log n/a` and weights `Lambda(n)/sqrt(n)`. Any finite weighted translation comb satisfies an analogous inequality. Rational-prime specificity must enter in a later cancellation, sign, activation, or coupled-resolvent argument.

**No positivity or unimodality is inferred.** `PL-294` already shows that the full localized form leaves the Beurling--Deny positivity-preserving regime long before `a=0.8`. BV stability does not restore a positive-semigroup or symmetric-decreasing ground-state theorem.

**No branch compactness is smuggled in.** The result controls `K_a u` assuming `u` has finite variation. It does not prove a uniform BV bound for the regularized eigenstates as `s->0+`; that remains the exact missing hypothesis needed by the `PL-299` autocorrelation argument.

**Activation regularity is separate.** The uniform BV bound remains valid when a lag reaches support diameter, because the channel is then zero. But the map `h -> C_h` need not be continuous in BV operator norm at the activation. Differentiability across source activation still needs the state-level endpoint cancellation from `PL-298` or stronger structure.

**No analytic-continuation issue is involved.** The statement concerns Suzuki's already established localized completed-Weil operator and exact finite prime-power decomposition. It does not continue an Euler product or infer critical-strip information from a convergence-region identity.

## Consequence for the research line

`PL-300` forced the program to use the actual source rather than abstract perturbation theory. This finding supplies the first exact source-specific regularity answer at that gate:

\[
\boxed{
\text{finite prime comb: BV transport}
\qquad+
\qquad
\text{archimedean completion: }L^1\to BV\text{ smoothing}.
}
\]

The rough high-frequency packet mechanism of the generic rank-two counterexample is therefore excluded from Suzuki's remainder itself. The accepted zero-order Hadamard route can be narrowed accordingly: the unresolved regularity theorem is now a **coupled principal-plus-finite-shifts uniform BV estimate for the actual isolated regularized ground branch**, followed by the already identified boundary-stress and arithmetic-sign gates.

Near `a=0.8`, the elementary termwise variation coefficient is larger than one, so merely placing the equation in `BV` is not enough. A substantive next step must prove a principal resolvent/variation estimate strong enough to absorb the finite shift comb, find a cancellation unavailable to the triangle bound, or control the derivative measure directly from the completed-Weil eigen-equation.

## Sources

- Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:`2606.09096`, source 56 in `research/prime_lattice/SOURCES.md`: scaled fixed-interval decomposition of the localized completed-Weil form into the logarithmic principal part, finite von-Mangoldt translations, scalar term, and the `r''` completion kernel.
- `PL-291`: exact logarithmic-space decomposition and local expansion/regularity of the completion kernel.
- `PL-294`: exact scaled Weil form and source activation structure.
- `PL-298`--`PL-300`: fixed-order physical-space differentiation, pure-branch BV compactness, and the generic norm-small perturbation obstruction that motivates the present source-specific check.
