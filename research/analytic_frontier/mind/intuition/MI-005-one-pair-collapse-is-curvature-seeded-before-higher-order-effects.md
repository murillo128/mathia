# MI-005 — Same-profile cascades are limited by local critical-cell conditioning, not raw depth growth

**Evidence level:** supported by exact full-profile completion constraints and depth-uniform cascade geometry through ANF-136

## Core intuition

The frozen-notch problem is controlled by the mesoscopic source profile only after global completion, but the later cascade results show that repeatedly annihilating the visible critical skeleton does not automatically destroy the architecture. Positive same-profile clouds can be retuned through growing depth while keeping the macroscopic bookkeeping under control.

The decisive remaining risk has moved inward. Once copy-rate slack, physical span, chamber proliferation, and discretization error are controlled, a cascade can still fail because the recursively selected critical cell becomes **locally ill-conditioned**: it may drift too close to zeros of inherited low-density factors, making its width or source integral too small even though the global combinatorics look harmless.

## Strongest justified principle

ANF-118 replaces finite saddle jets by the complete Gaussian Gram profile, while ANF-119--ANF-120 show that a source-heavy off-notch packet inside a global near-extremizer must be excisable, force an overpolarized companion, or become profile-mirrored. ANF-121 then separates the pointwise source-efficiency ceiling from the lower fatal-notch slope, so ceiling saturation alone does not force failure.

ANF-126 and ANF-129--ANF-133 classify the positive-translation repair through fixed depth. Subexponential source budget is excisable, finite critical skeletons can be removed, and positive exponential copy rate can retune the remaining source to criticality through every fixed finite depth.

ANF-134 gives the first depth-uniform invariant: positive copy-rate slack simultaneously preserves a fixed dark notch and bounds total translation span. ANF-135 shows that origin curvature prevents that slack from collapsing faster than `exp[-O(d log d)]`, so depths with `d log d=o(log A)` retain only subpolynomial slack loss. ANF-136 controls the other obvious combinatorial explosion: the number of critical chambers is at most `exp(O(d^2 log d))`, leaving an `A^{o(1)}` chamber and floor-error budget when `d^2 log d=o(log A)`.

Thus global depth growth itself is no longer the first unresolved obstruction in this regime. The load-bearing theorem is a **critical-cell conditioning bound** strong enough to keep cell width, Hessian scale, and source integral from degenerating under the recursively inherited zero geometry.

## Counterevidence / boundary

ANF-134--ANF-136 do not construct a fatal global near-extremizer and do not prove that the required local conditioning bound holds. Their depth regimes are sublogarithmic and depend on the declared cascade architecture; a different growth law or a critical cell approaching a historical zero can still defeat the construction.

The results also do not eliminate profile-transverse or macroscopic source components. They only remove copy-rate collapse, span growth, chamber proliferation, and coefficient rounding as sufficient reasons to abandon the same-profile route before the local cell is analyzed.

## Epistemic status

**Exact full-profile/global-completion control plus quantitative depth-uniform cascade geometry; local critical-cell conditioning and final fatal exposure remain open.**

## Falsification criterion

Produce an admissible depth sequence in the stated regime for which the copy/slack/chamber estimates hold but every candidate critical cell necessarily has vanishingly inadequate width or source mass, or prove a uniform lower conditioning theorem and complete the resulting globally admissible fatal exposure. A purported depth obstruction based only on raw chamber count, translation span, or floor rounding is already excluded by ANF-134--ANF-136 in their admitted regime.
