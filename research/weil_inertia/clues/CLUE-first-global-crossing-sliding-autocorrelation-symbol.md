---
id: CLUE-weil-inertia-first-global-crossing-sliding-autocorrelation-symbol
type: research-clue
status: accepted
origin: research-watch
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-253-first-global-crossing-has-a-sliding-autocorrelation-flux-constraint.md
  - research/weil_inertia/findings/WI-254-sliding-aperture-profile-is-invertible-but-small-scale-firstness-is-saturated.md
  - research/weil_inertia/findings/WI-255-first-small-aperture-correction-is-universal-and-cannot-bootstrap.md
  - research/weil_inertia/findings/WI-256-next-small-aperture-remainder-is-a-local-translation-defect-modulus.md
  - research/weil_inertia/findings/WI-257-bounded-perturbation-zero-modes-do-not-upgrade-translation-regularity.md
  - research/weil_inertia/findings/WI-258-phase-modulation-couples-firstness-slack-to-localized-cosine-defect.md
  - research/weil_inertia/findings/WI-259-first-prime-finite-scale-positivity-is-the-gate-for-the-phase-defect-program.md
  - research/weil_inertia/findings/WI-260-public-fp035-generator-does-not-yet-certify-the-exact-first-prime-matrix.md
  - research/weil_inertia/findings/WI-261-the-proofctl-exact-prime-checker-does-not-enclose-the-first-prime-layer.md
  - research/weil_inertia/findings/WI-262-the-fp035-interval-ldl-judge-double-updates-off-diagonal-schur-entries.md
  - research/weil_inertia/findings/WI-263-full-span-autocorrelations-can-null-the-first-prime-and-screen-the-localized-phase-defect.md
---

# Can the sliding autocorrelation symbols exclude a first global Weil zero mode?

## Observation

`WI-253` shows that under RH failure the first unrestricted localized Weil zero mode `v` must satisfy, for every `0<r<a_*`,

\[
\frac1{2\pi}\int_{\mathbb R}\Sigma_r(z)|\widehat v(z)|^2\,dz
\ge r\lambda_r>0,
\]

where `Sigma_r` is an explicit finite-prime plus archimedean cosine symbol and `|vhat|^2` is a nonnegative spectral density. This sliding-center formulation bypasses the reflected half-line Hankel obstruction of the first-odd-mode route because arbitrary translated windows are allowed at the first global crossing.

`WI-258` adds a second exact parameter without changing support. If

\[
d\mu_v(h)=C_v(h)\left[
\sum_{\log n<2a_*}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}(dh)
+w(h)\,dh
\right]
\]

is the source-weighted autocorrelation object of `WI-254`, then phase modulation `v_t(x)=e^{itx}v(x)` gives

\[
\int_0^{2a_*}(1-\cos(th))\,d\mu_v(h)\ge0
\qquad(t\in\mathbb R),
\]

and, after the same translated-window averaging,

\[
\mathcal F_v(r)+J_v(r,t)\ge r\lambda_r,
\]

where

\[
J_v(r,t)=\int_0^{2r}(2r-h)(1-\cos(th))\,d\mu_v(h).
\]

Thus any source-forced negative value `J_v(r,t)<=-epsilon` gives at least `epsilon` of strict firstness slack at that radius.

`WI-259` identifies the missing gate before this can genuinely use a prime atom at every hypothetical first crossing. The first prime enters only for `r>(log 2)/2`. A validated finite-scale theorem `lambda_{7/20}>0` would force `a_*>7/20`; then the fixed radius `r=7/20` is admissible and, because `log 2<7/10<log 3`, its discrete source contains exactly the single atom `n=2`.

`WI-260`--`WI-262` sharpen the certification boundary for that gate. The public `telleroutlook/weil-first-prime` candidate does not yet supply a rigorous exact theorem: the reproduction route uses point/rationalized surrogates and an invalid residual aggregation; the nominal exact proofctl route rebuilds the prime matrix at a rational `TAU_MID`, uses the wrong `c_L=0` surrogate, and can be shown by exact rational arithmetic to miss the true `S2[0,0]` entry; and the shared `_min_pivot_mpmath` positivity judge double-updates off-diagonal Schur entries, with an explicit indefinite rational matrix on which it returns all-positive pivots. The gate therefore requires an independent exact theorem-object enclosure **and** a mathematically valid positivity judge, not another replay of either public verdict.

`WI-263` then closes a weaker analytic continuation after the gate. In the entire one-prime window `7/20<a<log(3)/2`, there are full-span normalized autocorrelations that are positive-definite, satisfy `C(log2)=0`, and pair with Suzuki's continuous source so that `w(h)C(h)>=0` at every lag. For those models `J_v(r,t)>=0` for every `r,t`. Therefore compact support, full support span, positive-definiteness, and the explicit one-prime source **alone cannot force a negative localized cosine defect**. Any surviving phase argument must use quantitative firstness or the actual zero-mode equation, not merely source signs plus Bochner constraints.

## Research question

Can the actual first-crossing constraints rule out the source-screened autocorrelation geometries left open by `WI-263`? More precisely, after independently establishing `lambda_{7/20}>0`, can the exact one-prime identity at `r=7/20` together with the quantitative aperture inequalities

\[
\mathcal F_v(r)\ge r\lambda_r
\]

across radii and/or the exact null-vector equation `A_{a_*}v=0` force a negative localized cosine defect, a nonzero lower bound on the first-prime overlap, or another quantitative incompatibility?

This is deliberately narrower than asking for generic zero-mode regularity or immediately introducing several prime powers. `WI-257` proves that an abstract bounded self-adjoint perturbation can realize arbitrary domain vectors as zero modes, `WI-259` shows that prime activation is not presently guaranteed without a finite-scale positivity theorem past `(log 2)/2`, and `WI-263` shows that support plus positive-definiteness still permits exact first-prime screening even after activation.

## Why it may matter

The scalar aperture family is information-complete only when its **exact** profile is known; firstness supplies merely a lower envelope. `WI-258` adds an independent inequality cone on profiles compatible with that lower envelope. At the abstract transform level the extra cone is genuinely nonredundant: a signed measure can have positive `min`-transform at every radius while violating the cosine-defect inequality.

At `r=7/20`, once the positivity gate is established, the discrete part becomes maximally simple:

\[
\frac{\log2}{\sqrt2}
\left(\frac7{10}-\log2\right)
(1-\cos(t\log2))C_v(\log2),
\]

with no `n>=3` atom. But `WI-263` proves that this simplicity does not by itself create rigidity: a full-span positive-definite autocorrelation can have `C_v(log2)=0` exactly while matching the sign change of the archimedean density. The useful question is therefore whether **first-crossing information forbids that screening geometry**, not whether the first prime merely appears in the formula.

## Decisive test

First close the finite-scale gate in the **exact** localized-Weil normalization used by WI-238. The current external `FP-0.35` state is not upgraded by rerunning either public checker unchanged. A valid gate-closing artifact must assemble an enclosure of the intended theorem matrix using exact/enclosed `tau=20 log2/7`, `c_2=log2/sqrt2`, exact harmonic data, the theorem's nonzero `c_L`, and the correct archimedean/tail terms; then it must certify positivity using genuine directed/outward interval `LDL^T`/Cholesky or a rigorously submultiplicative residual theorem. It must also reject the exact WI-262 false-positive matrix and enclose the true WI-261 `S2[0,0]` entry. An independent analytic or formal proof of `lambda_{7/20}>0` is equally decisive.

If the gate validates, freeze `r=7/20` and study the exact identity

\[
\begin{aligned}
J_v(7/20,t)
={}&\frac{\log2}{\sqrt2}
\left(\frac7{10}-\log2\right)
(1-\cos(t\log2))C_v(\log2)\\
&+\int_0^{7/10}
\left(\frac7{10}-h\right)(1-\cos(th))w(h)C_v(h)\,dh
\end{aligned}
\]

under the full first-crossing constraints. Do not attempt to force negativity from compact support and positive-definiteness alone: `WI-263` supplies an exact countermodel to that weaker implication. Instead test whether the family `\mathcal F_v(r)\ge r\lambda_r`, the null equation `A_{a_*}v=0`, or a source-specific consequence of that equation quantitatively excludes the two-bump screening pattern, forces `C_v(log2)` away from zero, or yields another multi-frequency incompatibility.

A meaningful positive outcome is a source-specific bound

\[
\inf_t J_v(7/20,t)\le-\varepsilon
\]

with `epsilon>0` forced for every admissible **first-crossing zero mode**, or an alternative exact inequality that rules out the screened models and gives quantitative strictness. By `WI-258` any negative defect immediately implies

\[
\mathcal F_v(7/20)-(7/20)\lambda_{7/20}\ge\varepsilon.
\]

A meaningful negative outcome is either failure of a corrected exact finite-scale positivity certificate, or a source-compatible compact-support autocorrelation model that also satisfies the **quantitative first-crossing lower envelope / null equation** strongly enough to show that the remaining rigidity still cannot distinguish it. The WI-263 two-bump construction is already sufficient to reject proposals that omit those first-crossing inputs, so do not rediscover that weaker counterexample.

Stress-test every proposed implication against the pure logarithmic-core crossing of `WI-239`, the rank-two bounded-perturbation construction of `WI-257`, and the exact source-screening construction of `WI-263`. Also respect the external first-prime operator facts audited in `WI-259`: the prime overlap has operator norm one immediately after threshold and is indefinite, while the endpoint archimedean potential can absorb it at `L=7/20`. Therefore the gain must come from the full source coupling plus first-crossing structure, not from treating `n=2` as a small or automatically destabilizing perturbation.

## Evidence boundary

No incompatibility theorem for actual first-crossing zero modes is known. `WI-253` proves only a necessary continuum of positive aperture averages and does not assert pointwise positivity of `Sigma_r`, a lower rate for `lambda_r`, parity of the global first mode, or any RH consequence. `WI-254` proves that the exact aperture profile is an invertible `min`-transform of the source-weighted real autocorrelation, but pointwise firstness cannot be differentiated to read prime-threshold signs and the small-radius lower bound is asymptotically saturated at leading order.

`WI-255` shows that the first `O(r)` correction is universal on a first-crossing null mode: the prime and regular archimedean pieces cancel against `Q_W(v)=0`. `WI-256` identifies the next remainder as the local translation-defect modulus

\[
E_v(r)=\int_0^{2r}\left(\frac rh-\frac12\right)(1-C(h))\,dh\ge0,
\]

but the available `H^log` control does not determine its quadratic coefficient. `WI-257` then proves that generic bounded-perturbation zero-modehood cannot supply the missing regularity.

`WI-258` gives the exact identities

\[
Q_W^{a_*}(e^{itx}v)=2\int(1-\cos(th))\,d\mu_v(h)\ge0
\]

and

\[
S_v(r)+J_v(r,t)\ge0,
\qquad
S_v(r)=\mathcal F_v(r)-r\lambda_r.
\]

These are stronger than scalar `min`-transform positivity as inequality constraints, but analogous modulation inequalities exist for generic translation-invariant nonnegative forms. `WI-259` further shows that the first-prime version is conditional on a positivity margin past `(log2)/2`.

`WI-260`--`WI-262` establish certification barriers, not failure of FP-0.35. The public corrected computations may still point to a true positive statement, but neither available public path currently establishes the exact theorem object with a valid positivity judge. `WI-263` is a separate analytic barrier: it does not construct a zeta zero mode, but it proves that positive-definiteness/full-span/source-sign arguments cannot force `J<0` because exact first-prime screening is compatible with all of those weaker constraints.

## Research disposition

The direction remains `accepted`, but its dependency chain is now sharper. **First obtain an exact finite-scale recertification at `L=7/20`.** If that certificate validates, do not spend the next pass on source-sign or Bochner-only attempts to make the first-prime term nonzero: `WI-263` closes that route. Instead ask whether quantitative firstness across radii or the exact zeta-specific null equation forbids the screened autocorrelation geometry.

If corrected certification fails, return to proving any rigorous positivity margin past `(log2)/2`; do not presume that a hypothetical first crossing sees a von-Mangoldt atom. If it succeeds but the stronger first-crossing constraints still admit a screened model, the one-prime phase-defect route should be regarded as blocked until genuinely new arithmetic or spectral information is added.