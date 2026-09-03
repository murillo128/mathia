---
id: CLUE-weil-inertia-higher-zero-correlations-horizontal-rigidity
type: research-clue
status: accepted
origin: master-researcher
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-001-two-moment-bandwidth-one-barrier.md
  - research/weil_inertia/findings/WI-002-density-one-moment-tower-needs-audit.md
  - research/weil_inertia/findings/WI-005-critical-lattice-screening-defeats-depth-only-negative-mass.md
  - research/weil_inertia/findings/WI-006-critical-lattice-screening-is-matrix-equivalent-to-doubles.md
  - research/weil_inertia/findings/WI-007-support-one-is-screening-threshold-for-cross-scale-depth.md
  - research/weil_inertia/findings/WI-043-maximal-pair-discrepancy-does-not-control-locked-four-point-covariance.md
  - research/weil_inertia/findings/WI-115-tsang-pair-horizontal-signal-is-cancelled-by-critical-lattice-screening.md
  - research/weil_inertia/findings/WI-116-tsang-tail-needs-microscopic-density-slope-two.md
  - research/weil_inertia/findings/WI-117-tsang-admissibility-forces-screening-endpoint-taper.md
  - research/weil_inertia/findings/WI-118-termwise-positive-support-one-pair-kernels-are-screened.md
  - research/prior_art/montgomery-pair-correlation.md
---

# Can richer zero correlations turn horizontal information into a stronger critical-line inertia bound?

## Observation

`WI-001` isolates the first-two-moment support-one barrier, while `WI-005`--`WI-007` show a stronger horizontal-information obstruction: at critical vertical spacing, off-line mirror pairs can be matrix-equivalent to on-line doubles for every Alpöge--Furman-type compression of support at most one. `WI-043` separately shows that even strong pair-discrepancy control need not determine a locked four-point covariance. These facts leave open whether a different zero-correlation observable can retain horizontal information that survives the screening quotient.

`WI-115` materially narrows the question using the current v3 Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh Tsang-kernel method. A complex **pair** statistic already detects horizontal displacement on a same-height mirror pair, so genuine `k>=3` information is not needed merely for local detectability. But on the WI critical screening lattice the complete support-one Tsang statistic cancels that same-height excess exactly; long natural finite blocks retain only `O(log M)=o(M)` discrepancy, and the unconditional Montgomery weight changes the block comparison only by `O(1)`. The horizontal power of the published box argument instead comes from a microscopic **termwise positivity** condition that allows the same-height sub-sum to be extracted before cross-height cancellation.

`WI-116` closes the cheapest zero-density repair of that mechanism. In the published BGSTB tail reduction, normalized horizontal depth `a=(beta-1/2) log T` carries kernel weight `e^(2a)`, so discarding the complement by zero counts needs the strong-density scale `N(1/2+a/log T,T)=o(T e^(-2a))`. Published Selberg--Jutila/Maples--Rodgers microscopic density gives only fixed-factor suppression `O(T log T e^(-c a))` with `c<1`, while Ingham's exponent has microscopic slope `4/3<2`; neither supplies the needed weighted `o(T log T)` tail. The same finding also records Lagarias--Rodgers' classical Alternative-Hypothesis point process: all currently proved band-limited higher **vertical** correlations remain compatible with exact half-lattice support. That does not model the WI off-line multiplicities, but it rules out treating the known Montgomery--Hejhal--Rudnick--Sarnak package as a generic anti-lattice theorem.

`WI-117` closes ordinary kernel optimization **inside the BGSTB/Tsang positive-definite support-one construction**: compact support together with its nonnegative-Fourier admissibility forces endpoint taper. `WI-118` removes the remaining loophole that another support-one kernel might recover the same deterministic extraction through a different proof of positivity. For every real-even support-one profile, universal real-axis termwise nonnegativity already makes the profile positive definite, forces the same endpoint taper, and makes the mirror-pair-versus-double block difference `o(M)` by a Fejer-kernel identity. Under standard `C^2` regularity the exact Montgomery weight remains only an `O(1)` perturbation on `M=O(log T)` screening blocks. A boundary alias can survive at order `M` only by leaving universal termwise positivity; the box profile gives an exact sharp example and its sinc kernel changes sign.

## Research question

Can one obtain an unconditional information carrier or inequality that quantitatively prevents the compensating cross-height cancellation identified in `WI-115`, and then feed that control into the Weil-inertia certificate to force a strictly larger proportion of zeros onto `Re s=1/2`?

The established zero-density theorems are no longer a live **black-box** way to discard the Tsang bad-pair reservoir: `WI-116` identifies the missing microscopic density slope and little-`o` saving. Universal termwise-positive support-one pair extraction is now also closed, not merely the explicit Tsang construction: `WI-118` shows that the positivity property itself forces screening. A pair-level support-one route therefore remains live only if it estimates the actual **signed** weighted reservoir more efficiently than zero counting, or proves positivity only on a rigorously controlled non-universal set of separations using new zeta-specific information. Otherwise it must justify a support-`>1` alias. If the search escalates to mixed moments or genuine finite `k`-point statistics, it must use information beyond the already-known band-limited **vertical** correlations and must be checked explicitly against the same screening configuration.

## Why it may matter

`WI-115` supplies both a positive and a negative lesson. Pair correlation does contain an exact horizontal-depth defect: under the BGSTB positivity hypothesis, retaining the quadratic remainder in `cosh` controls a same-height horizontal variance in addition to horizontal multiplicity. But support-one global summation can erase that signal at leading order. The useful research question is therefore no longer whether horizontal information exists, but whether available arithmetic can isolate it from the cross-height reservoir that screens it.

`WI-116`--`WI-118` make the required information gain more precise. Merely improving an ordinary zero-count exponent, importing the established higher vertical-correlation package, selecting a different compactly supported positive-definite Tsang profile, or replacing Tsang by any other **universally termwise-positive** real-even support-one kernel is not enough. A successful controller must beat the `e^(2a)` horizontal growth in the actual weighted tail, control a genuinely signed support-one observable, activate a justified supercritical alias, or supply a statistic whose arithmetic evaluation contains new horizontally coupled information.

A successful controller would attack the exceptional complement directly rather than squeezing the same first-two trace moments harder. A broader impossibility theorem remains valuable if it controls support-one **signed** pair observables using only the unconditional Montgomery form factor, because universal positivity is now already exhausted.

## Decisive test

Start with the exact Tsang interface in `WI-115`, the density-slope ledger in `WI-116`, and the positivity/screening no-go in `WI-117`--`WI-118`. Derive a decomposition of the evaluated pair sum into the same-height horizontal-defect term and the complementary cross-height contribution. Using only established unconditional inputs, either prove a direct bound on the **signed weighted** complement strong enough that the horizontal defect survives at order `N`, or construct a zeta-count-compatible screened configuration showing that the proposed controller remains `o(N)`-blind.

A route that merely substitutes a known zero-density count into the BGSTB partial-summation argument has already failed this test unless it supplies the missing slope-two little-`o` interface. A route that merely changes the profile while requiring `K(x)>=0` for every real vertical separation has also failed: `WI-118` forces the endpoint taper and Fejer screening independently of how positivity was proved. A proposed restricted-positivity route must therefore state and prove the zeta-specific theorem that confines relevant separations to its positivity set; it cannot assume that confinement.

For any replacement pair or `k`-point statistic, repeat the same adversarial test against the WI-005/WI-006 lattice before investing in arithmetic evaluation. For higher vertical correlations, also test against the Lagarias--Rodgers half-lattice prior art rather than assuming that band-limited GUE agreement implies anti-lattice rigidity. A route counts as a substantive success only if the surviving statistic yields an explicit deterministic bound on off-line mass/depth and that bound can be inserted into the existing inertia/rank certificate using proved, not conjectural, correlation information.

## Evidence boundary

`WI-115` establishes local Tsang horizontal sensitivity, exact support-one lattice cancellation for endpoint-tapered kernels, `O(log M)` finite-block blindness, and `O(1)` stability of that block comparison under the Montgomery weight. `WI-116` establishes an interface mismatch for the direct published zero-density substitution and a prior-art barrier to generic anti-lattice conclusions from the known band-limited higher vertical correlations. `WI-117` proves that endpoint taper is automatic throughout the BGSTB/Tsang compactly supported positive-definite admissible class.

`WI-118` strengthens only the **universal termwise-positivity** branch: for a real-even support-one pair profile, `K(x)>=0` for all real `x` already forces endpoint taper and `o(M)` critical-lattice blindness; with standard smoothness the exact Montgomery weight remains screened on natural blocks. It does **not** prove that every support-one pair kernel is unusable, because sign-changing profiles can carry a nonzero boundary alias. It also does not control a signed cross-height reservoir or a kernel positive only on a zeta-specifically restricted set of separations.

The BGSTB simple-critical proportions in a fixed narrow box remain conditional on their box/positivity hypothesis (or a suitably strong zero-density hypothesis). They are not unconditional improvements to the Mathia bound. The Lagarias--Rodgers Alternative-Hypothesis process is a vertical simple point process, not an off-line zeta-zero configuration, so it cannot be used as evidence that the exact WI screening multiplicity pattern satisfies all higher-correlation constraints. The all-order trace-moment route in `WI-002` remains separately unverified and cannot be used as evidence for this clue.

## Research disposition

Accepted and narrowed by `WI-115`--`WI-118`. Pair-level horizontal detectability is established, but the raw support-one Tsang/Montgomery pair statistic is screened at density scale. The direct replacement of the box by **currently established zero-density counts** is closed at the BGSTB weighted-tail interface, the existing band-limited higher **vertical** correlations cannot be invoked as a generic anti-lattice principle, and **every universal termwise-positive real-even support-one pair kernel** is now screened at the critical lattice regardless of the proof used to obtain positivity.

The live question is therefore narrower: can one unconditionally control a genuinely signed weighted cross-height reservoir, justify positivity on a smaller zeta-specific separation set, obtain a support-`>1` alias with established arithmetic input, or construct a mixed/higher-order horizontally coupled statistic whose proved evaluation survives the canonical screening extremizer?