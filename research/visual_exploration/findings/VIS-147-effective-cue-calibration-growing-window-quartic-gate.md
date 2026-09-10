# VIS-147 — effective-CUE calibration absorbs the displayed low-order pair-correlation terms but does not control the growing-window quartic coefficient

## Claim

The standard finite-height two-point expansion for Riemann zeros does **not** yet supply the quartic source coefficient `A_4(L)` required by the accepted moment-cancelled companion clue.

Forrester and Mays record the smoothed, unit-density Riemann-zero two-point correlation in the form

`rho_R(E,E+s)`
` = rho_infty(s)`
`   - [Lambda/(pi^2 rho_bar^2)] sin^2(pi s)`
`   - [Q/(2 pi^2 rho_bar^3)] s sin(2 pi s)`
`   + O(rho_bar^-4)`,

where `rho_infty(s)=1-(sin(pi s)/(pi s))^2`. They then rewrite the displayed correction as

`rho_R(E,E+s)`
` = rho_infty(s)`
`   - [Lambda/(pi^2 rho_bar^2)] sin^2(pi alpha s)`
`   + O(rho_bar^-4)`,

with `alpha=1+C/log(E/(2*pi))`, `C=Q/Lambda`, and identify it with the leading finite-`N` CUE correction after choosing

`N=(12 Lambda)^(-1/2) log(E/(2*pi))`

and applying the scale change `s -> alpha s`.

Thus, at the level and in the fixed-spacing regime of this classical expansion, the displayed `rho_bar^-2` and `rho_bar^-3` terms are already tangent to an effective finite-CUE calibration: matrix size supplies the `sin^2(pi s)` direction and the small coordinate stretch supplies the `s sin(2*pi s)` direction. They cannot simultaneously be treated as a source-specific residual **after** the finite-CUE size/scale calibration has been admitted into the null.

For the present Visual Exploration route there is a second, independent obstruction. `VIS-146` shows that after imposing `m_2(nu_b)=0`, the desired deterministic companion coefficient is

`A_4(L)=-(2/3) pi^4 mu_4(H_L)`,

where `H_L` is the actual frozen zeta-minus-finite-CUE correction in the source-difference coordinate and

`mu_4(H_L)=integral x^4 H_L(x) dx`.

But the bounded-source null of `VIS-130` uses a source window of unfolded radius `M_L=Theta(L)` rather than a fixed compact spacing interval. A fixed-`s` remainder `O(rho_bar^-4)` therefore gives no usable control of `mu_4(H_L)` by itself. Even the much stronger hypothetical bound

`sup_(|x|<=cL) |H_L(x)| = O(L^-4)`

would yield only the crude estimate

`integral_(|x|<=cL) |x|^4 |H_L(x)| dx = O(L)`.

Consequently, the standard low-order effective-CUE matching neither identifies the needed `A_4(L)` nor provides the weighted uniformity required to test the `VIS-146` gate. The next source-side object must be the **windowed residual after size/scale calibration**, controlled in a norm strong enough for its fourth spatial moment on the growing source window.

**Evidence/status:** `LITERATURE+DERIVED + CALIBRATION-IDENTIFIABILITY OBSTRUCTION + GROWING-WINDOW NONUNIFORMITY GATE + NO-NOVELTY-CLAIM`.

No new pair-correlation theorem, finite-height error estimate, arithmetic quartic coefficient, covariance result, or RH implication is claimed.

## 1. The first two displayed corrections are finite-CUE calibration directions

For `CUE_N`, the unit-density two-point function has the classical expansion

`rho_CUE,N(s)`
` = rho_infty(s) - [1/(3N^2)] sin^2(pi s) + O(N^-4)`.

Forrester--Mays compare this with the finite-height zero expansion above and give the effective-size rule and the scale rescaling `s -> alpha s`. The mechanism can also be seen directly by Taylor expansion. If `alpha=1+delta`, then on every fixed compact `s`-set,

`sin^2(pi alpha s)`
` = sin^2(pi s) + pi delta s sin(2 pi s) + O(delta^2 s^2)`.

Since the effective-size correction is already of order `rho_bar^-2` and `delta=Theta(rho_bar^-1)`, the scale derivative generates an order-`rho_bar^-3` term with exactly the `s sin(2*pi*s)` shape. This is the same structural decomposition recorded explicitly in their equations (2.3)--(2.6).

This does **not** mean that the Riemann-zero finite-height correction contains no arithmetic. `Lambda` and `Q` themselves arise from arithmetic lower-order structure, and the full finite-height pair-correlation formulas retain prime-dependent information. The point is narrower: once an effective finite-CUE null is calibrated using these coefficients, the two displayed shapes are no longer identifiable as a residual channel distinct from that null.

That distinction matters for the current companion. Computing a fourth spatial moment of the raw difference from the infinite sine-kernel law would mix the proposed source-specific carrier with exactly the finite-size and coordinate-stretch directions that the null is already allowed to absorb.

## 2. The bounded-source observable changes the required uniformity

The exact finite-CUE control in `VIS-130` is not a fixed-spacing point evaluation. Its connected expectation is integrated against a bounded physical source taper whose unfolded support grows as

`M_L = H_src L/(2*pi) = Theta(L)`

for fixed nonzero `H_src`, together with Montgomery's weight and the finite-CUE kernel. The current low-frequency companion then probes moments of the resulting source-coordinate correction.

The quartic coefficient from `VIS-146` depends on

`mu_4(H_L)=integral x^4 H_L(x) dx`.

A pointwise asymptotic at each fixed `x` is not interchangeable with this growing-window moment. The elementary bound

`|mu_4(H_L)|`
` <= integral_(|x|<=M_L) |x|^4 |H_L(x)| dx`

shows the issue immediately. If one were granted a uniform `O(L^-4)` residual on the whole `Theta(L)` window — substantially stronger than the fixed-spacing expansion actually states — the fourth-moment bound would still be only `O(L)` because the volume-weight factor is `M_L^5`.

This does not prove that the actual moment grows. Oscillation, sign cancellation, the source taper, the Montgomery weight, or a sharper structured remainder may make it much smaller. It proves that the needed conclusion cannot be extracted from the fixed-spacing `O(rho_bar^-4)` remainder without precisely that additional structure.

Forrester--Mays themselves warn at the empirical/formula level that the truncated large-height expansion and the fuller pair-correlation expression increasingly disagree as the spacing grows. That is consistent with, though not required for, the formal nonuniformity gate above.

## 3. The full arithmetic formula is a candidate source, not the missing theorem

Keating and Smith review the finite-height pair correlation in a fuller arithmetic form. Their diagonal term contains logarithmic derivatives of `zeta`, while the off-diagonal term contains

`|zeta(1+i epsilon)|^2`

multiplying an explicit Euler product and an oscillatory phase depending on the mean zero density. They use this lower-order structure in a formal/heuristic Fourier inversion recovering Hardy--Littlewood prime-pair information.

This confirms that arithmetic information exists beyond the limiting CUE/GUE law and supplies a plausible source from which to derive a windowed correction. It does not by itself solve the present problem. The formula must first be transported into the **same unfolded difference coordinate, source taper, Montgomery weight, diagonal convention, finite-CUE effective size, and scale calibration** used by the frozen visual observable.

Moreover, the current `VIS-146` test is a robust asymptotic comparison. It needs not only a candidate arithmetic mean but a controlled error envelope in the same representation. The heuristic/conditional finite-height formulas cannot be silently promoted to the theorem-level `epsilon_L` required by that gate.

## 4. What this closes and what remains live

This finding closes one tempting shortcut: take the known `rho_bar^-2` or `rho_bar^-3` lower-order pair-correlation term, call its fourth moment the zeta-specific `A_4(L)`, and feed that value into the moment-null companion. Those terms are already absorbed by the standard effective-CUE size/stretch matching at fixed spacing, so that procedure would double-count calibration structure.

It also closes the inference

`pointwise residual = O(L^-4)`

therefore

`quartic companion coefficient = O(L^-4)`.

The coefficient is a growing-window weighted moment, and the implication is invalid without uniform weighted control.

The route itself remains open. A viable continuation may use the fuller finite-height arithmetic formula, another controlled pair-correlation representation, or a theorem with sufficiently strong uniformity to derive the post-calibration residual `H_L` directly. What is required is a statement strong enough to control

`integral x^4 H_L(x) dx`

on the actual `M_L=Theta(L)` source window, together with the corresponding transfer/theorem error after the same windowing and calibration.

Only after that quantity is established does it make sense to compare `|A_4(L)| b_L^4` with the error scale from `VIS-146`, and only after that deterministic gate survives do packet variance and four-level covariance become the next bottleneck.

## 5. Prior-art and novelty audit

Peter J. Forrester and Anthony Mays, **Finite-size corrections in random matrix theory and Odlyzko's data set for the Riemann zeros**, *Proceedings of the Royal Society A* 471 (2015), 20150436, DOI `10.1098/rspa.2015.0436`, equations (2.2)--(2.6), give the finite-CUE expansion, the finite-height Riemann-zero expansion, its rewriting by a scale factor, and the effective matrix-size identification used here. The observation that the displayed lower-order terms match finite-CUE size/scale corrections is their prior art, not a Mathia novelty claim.

J. P. Keating and D. J. Smith, **Twin prime correlations from the pair correlation of Riemann zeros**, *Journal of Physics A: Mathematical and Theoretical* 52 (2019), 365201, DOI `10.1088/1751-8121/ab3521`, review the finite-height diagonal and off-diagonal formulas and use the lower-order arithmetic structure in formal/heuristic Fourier inversion. That source bounds any claim that the existence of arithmetic lower-order pair-correlation structure is new.

The Mathia-specific consequence recorded here is only the composition with the already-persisted bounded-window companion architecture: the source coefficient needed by `VIS-146` lives **after** effective-CUE calibration and is a fourth weighted moment over a growing source window, so the familiar fixed-spacing expansion is not a sufficient input for that gate.

## Research consequence

The accepted moment-cancelled clue should next derive the zeta-minus-calibrated-finite-CUE residual in the exact `VIS-130` bounded-source representation. The target is not another packet shape and not the raw low-order pair-correlation coefficient. It is a controlled growing-window fourth-moment statement for the post-calibration residual, with any scale/effective-size uncertainty propagated before the low-frequency packet is applied.

If the strongest available source formula cannot provide that weighted uniformity or a substitute norm/cancellation estimate strong enough for `VIS-146`, the current quartic moment-null route should be rejected on an information/control boundary rather than tuned further.