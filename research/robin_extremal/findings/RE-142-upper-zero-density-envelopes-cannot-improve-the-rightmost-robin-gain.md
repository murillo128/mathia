# RE-142 — upper zero-density envelopes cannot improve the rightmost Robin gain

**Date:** 2026-09-15

**Status:** `DERIVED + MATCHED-CONTROL + SINGLE-INFINITE-SPECTRUM + RIGHTMOST-GAIN-SHARPNESS + ZERO-DENSITY-COMPATIBLE + RIEMANN-VON-MANGOLD-COMPATIBLE + ZERO-FREE-REGION-COMPATIBLE + EFFECTIVE-COMPLEXITY-NEGLIGIBLE + SOURCE-INFORMATION-GAP + NOT-A-ZETA-ZERO-CONSTRUCTION + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

`RE-141` improves the full-packet tail by using zero density where it is genuinely effective: after the Robin coefficient contributes `gamma^-2`, an upper density law turns the omitted high zeros into a tail of size approximately `T^(-2+nu(Theta))`. The remaining direct Turán budget is

\[
\frac AB+\eta+\Lambda_\kappa\alpha
<2-\nu(\Theta),
\tag{1}
\]

where `eta` measures the rightmost-amplitude loss

\[
G(U,T)\ge T^{-\eta+o(1)}
\tag{2}
\]

and `alpha` measures the effective finite-core complexity. `RE-140` has only the source-generic comparison `G(U,T) \gg T^{-2}`. The natural next question is whether the same upper source laws already present in the line — zero density, Riemann--von Mangoldt counting, the zero-free region, and functional symmetry — can force a better exponent than `2`.

They cannot. More strongly, one can build a **single infinite formal zero-like spectrum** satisfying all of those coarse envelopes, with an attained edge `Theta`, for which along a lacunary sequence of polynomial cutoffs

\[
\boxed{
G(U_j,T_j)=T_j^{-2+o(1)}
}
\tag{3}
\]

while the retained strict-subedge mode count obeys

\[
\boxed{
N_{T_j}=o(\log T_j).
}
\tag{4}
\]

Thus the exponent `2` in the generic rightmost transfer is sharp relative to these **upper-envelope inputs**, even when the Turán complexity coefficient is asymptotically zero. In particular, no argument using only such upper counting/exclusion laws can deduce a uniform bound

\[
G(U,T)\ge T^{-\eta+o(1)}
\qquad\text{with any fixed }\eta<2.
\tag{5}
\]

This is a non-implication theorem about the information content of the current source envelopes. The constructed points are **not claimed to be zeros of `zeta`**, and no counterexample to full-packet Robin visibility is claimed.

## 1. A lacunary source can make the rightmost atom appear only at the cutoff height

Fix

\[
\frac12<\sigma_0<\Theta<1,
\qquad A>0,
\qquad B>0.
\tag{6}
\]

Choose a rapidly increasing sequence `U_j` so that, writing

\[
T_j:=U_j^B,
\qquad h_j:=\log U_j,
\tag{7}
\]

we have

\[
h_{j+1}>2T_j
\tag{8}
\]

and the quantities introduced below are strictly ordered toward `Theta`. This is possible by choosing each `U_(j+1)` sufficiently large after `U_j`.

Set

\[
\delta_j
:=
\frac{A\log U_j-2\log\log U_j}{U_j},
\tag{9}
\]

and, for all sufficiently large `j`, define two right-half-strip points

\[
\rho_{0,j}
=
\beta_{0,j}+ih_j,
\qquad
\beta_{0,j}:=\Theta-\delta_j,
\tag{10}
\]

and

\[
\rho_{*,j}
=
\beta_{*,j}+iT_j,
\qquad
\beta_{*,j}:=\beta_{0,j}+U_j^{-2}.
\tag{11}
\]

Since `delta_j >> U_j^-2`, both real parts lie strictly below `Theta`. By taking the sequence sufficiently lacunary we may also ensure

\[
\beta_{*,1}<\beta_{*,2}<\cdots<\Theta.
\tag{12}
\]

Include the conjugates and functional-equation mirrors of these points. If one wants the formal source to lie in the attained-edge branch literally, also include one fixed symmetric quartet with real parts `Theta` and `1-Theta`; the edge points are excluded from the strict-subedge packet because that packet uses `beta<Theta`.

Condition (8) has a useful consequence. At the cutoff `T_j`, no pair from stage `j+1` or later has entered, because even the lower ordinate `h_(j+1)` already exceeds `T_j`. All earlier pairs have entered, and (12) makes `rho_( *,j)` the rightmost member of the strict-subedge core. Therefore the exact `RE-140` rightmost gain at `(U_j,T_j)` is anchored by the intended pair `(rho_(0,j),rho_(*,j))`, not by an accidental point from another stage.

The construction is one fixed infinite spectrum. It is not a different adversarial spectrum chosen separately for each `U_j`.

## 2. The strong atom is algebraic, but the rightmost transfer still loses two cutoff powers

For the leading Robin coefficient

\[
d_\rho:=\frac1{\rho(1-\rho)},
\tag{13}
\]

we have uniformly on the fixed strip

\[
|d_\rho|\asymp_{\sigma_0,\Theta}(1+\gamma^2)^{-1}.
\tag{14}
\]

At `rho_(0,j)`, equations (9)--(10) give

\[
\begin{aligned}
M_0(U_j)
&:=
 e^{-(\Theta-\beta_{0,j})U_j}|d_{\rho_{0,j}}|\\
&\asymp
 e^{-\delta_jU_j}h_j^{-2}\\
&=
 U_j^{-A}(\log U_j)^2(\log U_j)^{-2}.
\end{aligned}
\tag{15}
\]

Hence

\[
\boxed{M_0(U_j)\asymp U_j^{-A}.}
\tag{16}
\]

So `rho_(0,j)` satisfies exactly the algebraically strong-atom hypothesis used by `RE-140` and `RE-141`.

The rightmost atom differs horizontally by only

\[
\beta_{*,j}-\beta_{0,j}=U_j^{-2},
\tag{17}
\]

so the favorable horizontal factor is negligible:

\[
e^{(\beta_{*,j}-\beta_{0,j})U_j}
=e^{1/U_j}=1+o(1).
\tag{18}
\]

Using the exact amplitude decomposition from `RE-140`,

\[
G(U_j,T_j)
=
 e^{(\beta_{*,j}-\beta_{0,j})U_j}
 \frac{|d_{\rho_{*,j}}|}{|d_{\rho_{0,j}}|},
\tag{19}
\]

we obtain

\[
\begin{aligned}
G(U_j,T_j)
&\asymp
(1+o(1))
\frac{h_j^2}{T_j^2}\\
&=
T_j^{-2}
(\log U_j)^2\\
&=
T_j^{-2+o(1)}.
\end{aligned}
\tag{20}
\]

This proves (3). In particular, for every fixed `eta<2`,

\[
\frac{G(U_j,T_j)}{T_j^{-\eta}}
=
T_j^{-(2-\eta)+o(1)}
\longrightarrow0.
\tag{21}
\]

Thus no lower transfer exponent strictly below `2` follows from any source information that the present formal spectrum also satisfies.

The point of choosing `h_j=log U_j` rather than a fixed lower ordinate is to avoid a hidden defect in the matched control: a single infinite spectrum cannot accumulate infinitely many distinct points in a bounded ordinate interval. The lower atoms themselves escape to infinity, but only subpolynomially in their associated `U_j`, so their Robin coefficients cost merely `(log U_j)^-2`, which was exactly absorbed into the horizontal damping in (9).

## 3. All current upper source envelopes can coexist with this transfer loss

The off-critical source is extremely sparse. Up to `T_j` there are only two right-half-strip points from each completed stage, so

\[
N_{T_j}=2j+O(1).
\tag{22}
\]

Because the sequence may be chosen arbitrarily lacunary subject to (8),

\[
\boxed{
N_{T_j}=T_j^{o(1)}=o(\log T_j).
}
\tag{23}
\]

This is far below the classical Ingham density envelope and also below the stronger modern Guth--Maynard polynomial zero-density bounds already anchored in `SOURCES.md`. More generally, for every fixed `sigma<Theta`, the number of constructed right-half-strip points with `beta>=sigma` and `0<gamma<=X` is `X^{o(1)}`. For `sigma>Theta` it is zero, while at `sigma=Theta` only the optional fixed edge quartet contributes. Hence every fixed-strip upper density estimate of the form

\[
N(\sigma,X)\ll X^{\nu(\sigma)+o(1)},
\qquad \nu(\sigma)>0,
\tag{24}
\]

is respected with enormous slack.

The zero-free region also does not exclude the construction. All right-half points have real part at most the fixed number `Theta<1`. Any standard asymptotic zero-free boundary tends to `1` as the ordinate tends to infinity, so after discarding finitely many initial stages all points lie safely to its left. The fixed edge quartet, if included, can likewise be placed at a sufficiently large fixed ordinate.

Riemann--von Mangoldt supplies no missing coupling either. The off-critical points contribute only `X^{o(1)}` to the total ordinate count. If an exact formal analogue of the global counting law is desired, add a background multiset on `beta=1/2`, together with conjugates, so that the complete positive-ordinate counting function has the usual

\[
N(X)=
\frac{X}{2\pi}\log\frac{X}{2\pi}
-
\frac{X}{2\pi}
+O(\log X)
\tag{25}
\]

profile. Those critical-line background points never enter the strict packet `beta>=sigma_0>1/2` and never change (19)--(23). Thus even **global abundance of zeros plus extreme sparsity off the line** does not relate the ordinate of the rightmost strict-subedge atom to the ordinate of the algebraically strong one.

The functional symmetries are also harmless: reflecting each right-half point to `1-rho` and to its conjugate changes neither the right-half strict-subedge count nor the gain calculation.

## 4. The `RE-141` budget therefore isolates genuinely new source information

For the control above, the complexity term in the scale notation of `RE-141` satisfies

\[
\alpha_j:=\frac{N_{T_j}}{\log T_j}\longrightarrow0,
\tag{26}
\]

while the gain exponent satisfies

\[
\eta_j:=
-\frac{\log G(U_j,T_j)}{\log T_j}
\longrightarrow2.
\tag{27}
\]

Consequently the obstruction in the `RE-141` budget is not an artifact of inserting a weak polynomial density estimate into the Turán mode count. The mode count can be asymptotically negligible and the gain still sits at the geometry-free endpoint `2`.

This also shows why simply replacing Ingham by a stronger **upper** zero-density theorem cannot solve the rightmost-transfer problem. Such an improvement decreases the tail exponent `nu(Theta)` and therefore raises the right side of (1), which is useful. But an upper density theorem still says only that sufficiently rightward zeros are not too numerous. It does not say that, once an algebraically strong atom is present, a farther-right atom must occur at an ordinate comparable with it, nor that any ordinate inflation must be paid for by a horizontal displacement large enough to compensate through

\[
e^{(\beta_* - \beta_0)U}.
\tag{28}
\]

The matched control arranges exactly the missing geometry: the rightmost atom appears only near the truncation height, while its horizontal advantage is `o(1/U)`. Every upper counting law remains true because the source is sparse.

Therefore the source theorem needed after `RE-141` must be **relational**, not merely another one-point upper envelope. Examples of genuinely different information would be a theorem coupling horizontal extremality to first-occurrence height, a lower-population/recurrence statement forcing a sufficiently rightward atom below a controlled ordinate, or a target-aware certificate that never replaces the strong atom by the rightmost atom in the first place.

## 5. Representation audit and adversarial controls

The obstruction is matched inside the same leading Robin representation used by `RE-139`--`RE-141`. The coefficients are not arbitrary: every formal point carries the exact kernel

\[
\frac{e^{-(\Theta-\beta)u}e^{i\gamma u}}
{\rho(1-\rho)}.
\tag{29}
\]

The two-power loss comes from the invariant reciprocal-square ordinate decay of this coefficient together with the deliberate absence of compensating horizontal gain. It is therefore not created by switching to a poorly conditioned coordinate system or by assigning adversarial free coefficients.

What is **not** source-faithful is the zero set itself. The construction satisfies the listed coarse consequences of the zeta source but is not asserted to arise from the Euler product, the functional equation as an analytic identity, or any actual zeta zero configuration. Accordingly the conclusion is only

\[
\boxed{
\text{current upper envelopes}
\not\Longrightarrow
\text{rightmost gain exponent }<2,
}
\tag{30}
\]

not that the true zeta zeros attain the bad transfer.

Several possible loopholes have been checked explicitly. The control uses one infinite spectrum rather than a scale-by-scale replacement; the strong atom really has algebraic size by (15)--(16); the selected atom really is rightmost at the corresponding cutoff by (8) and (12); the horizontal factor cannot secretly compensate the ordinate loss because of (17)--(18); the off-critical count is `o(log T_j)` rather than merely polynomial; and an exact Riemann--von Mangoldt background can be supplied on the critical line without altering the packet. No spacing, simplicity, or phase-cancellation assumption is being smuggled into the negative conclusion.

The control also does **not** show that the full packet is small. It does not arrange destructive phase alignment at the Turán witness, and its future tail is in fact extremely sparse. The finding is a sharpness statement for the rightmost-amplitude transfer step in the current certificate architecture, not a synthetic counterexample to Robin visibility itself.

## 6. Prior-art boundary and next step

No new external theorem is load-bearing here. The source envelopes tested by the control — Riemann--von Mangoldt, standard zero-free regions, Ingham-style density bounds, and the stronger Guth--Maynard upper zero-density estimates — are already anchored in `SOURCES.md`. A targeted check of the current zero-density literature confirms that the modern improvements remain upper bounds on `N(sigma,T)`; they sharpen how many rightward zeros may occur but do not provide the lower/relational first-occurrence statement ruled out as missing above. No `SOURCES.md` update is therefore required.

The durable delta from `RE-141` is that the remaining `T^-2` gain loss is no longer merely an unattractive generic estimate. It is **optimal relative to the present envelope language**, even on a spectrum with negligible effective complexity. Further work should therefore stop asking whether another upper zero-density exponent alone can repair the gain term. The next useful splice must import source information that couples at least two attributes of the same off-critical configuration — horizontal position and ordinate, strong-atom amplitude and rightward recurrence, or target-bearing mass and the finite-core observability certificate.

A particularly clean target is now:

\[
\boxed{
\text{strong atom at scale }U
\quad\Longrightarrow\quad
\exists\rho_*\text{ farther right with }
\log\frac{1+\gamma_*^2}{1+\gamma_0^2}
-(\beta_* - \beta_0)U
\le (2-\delta)\log T
}
\tag{31}
\]

for some fixed `delta>0` in the relevant polynomial-height core, or an alternative certificate that avoids requiring such a `rho_*`. Equation (31) makes explicit the kind of **joint horizontal/height theorem** that the current one-point source envelopes cannot supply.