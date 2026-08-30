---
id: CLUE-prime-lattice-mesoscopic-weil-boundary-topology
type: research-clue
status: accepted
origin: mind
target_line: prime_lattice
based_on:
  - research/prime_lattice/findings/PL-044-localized-weil-prime-free-spectral-reality.md
  - research/prime_lattice/findings/PL-050-rescaled-weil-prime-boundary-escape.md
  - research/prime_lattice/findings/PL-051-weil-boundary-rank-one-pnt-model.md
  - research/prime_lattice/findings/PL-052-weil-boundary-kronecker-norm-gap.md
  - research/prime_lattice/findings/PL-053-weil-boundary-essential-norm-obstruction.md
  - research/prime_lattice/findings/PL-054-weil-threshold-delta-hankel-essential-channel.md
  - research/prime_lattice/findings/PL-055-fixed-sobolev-weil-boundary-smoothing.md
  - research/prime_lattice/findings/PL-056-critical-sobolev-endpoint-det2-weak-trace.md
  - research/prime_lattice/findings/PL-057-growing-depth-boundary-tightness.md
  - research/prime_lattice/findings/PL-058-spatial-tail-recentering-exact-self-similarity.md
  - research/prime_lattice/findings/PL-059-weil-pole-pnt-boundary-cancellation.md
  - research/prime_lattice/findings/PL-060-pnt-resolution-moving-smoothing.md
---

# Is there a canonical mesoscopic topology between Weil boundary homogenization and essential recurrence?

## Observation

The localized Weil operator has now been analyzed in several incompatible topologies. At sufficiently short localization scale, self-adjoint spectral reality can occur before any prime-power contribution appears. Under the natural boundary rescaling, every fixed window converges strongly to zero, while a fixed-depth blow-up yields a universal rank-one Hankel model governed by the prime number theorem. In contrast, operator norm and essential norm do not converge away: Kronecker recurrence in the prime logarithms leaves an order-one gap, and each individual prime-power threshold creates a partial-reflection channel with `+/-1` of infinite multiplicity.

Fixed smooth probes suppress the recurrence, but the surviving fluctuation is then the familiar explicit-formula zero contribution. The currently audited topologies therefore separate into three regimes: universal strong bulk, noncompact essential arithmetic recurrence, and classical explicitly zero-resolved smoothing.

`PL-059` adds an important completion effect: the zeta pole itself produces, at the natural `exp(-L)` boundary scale, exactly the same rank-one profile as the universal PNT prime shell and cancels it with the opposite sign in the completed Weil form. Thus the first-order PNT subtraction is not an arbitrary renormalization to be chosen by this clue; it is already forced by completion. The resulting pole-minus-prime sector tends strongly to zero but retains the full `PL-053` essential-norm gap because the pole correction is finite rank.

## Research question

Is there a geometrically forced intermediate scale or topology — for example a depth `R=R(L)` growing with the localization parameter together with a canonical smoothing, relative norm, or weighted operator ideal — in which the **canonically completed/centered residual** has a nontrivial zero-sensitive limit?

The desired object should not be defined by inserting the explicit formula or the zeta zero divisor. Its topology and normalization must come from the localized completed Weil construction itself, and it should distinguish the rational-prime system from matched Beurling controls. After `PL-059`, a successful construction must treat the archimedean frequency cost and the noncompact atomic prime recurrence on a common moving scale rather than invent another PNT counterterm.

## Why it may matter

`PL-050`--`PL-054` show that the arithmetic signal is real but sits in a bad category for ordinary Fredholm spectral flow: it escapes fixed strong limits while remaining order one in the Calkin algebra. `PL-059` shows that completion already performs the canonical first-order PNT centering, so the remaining obstruction is not an ambiguity in which universal term to subtract. If a canonical mesoscopic topology exists for that centered family, it could isolate the first scale at which prime-log recurrence stops being a universal/essential artifact and becomes a stable relative spectral invariant.

Conversely, proving that every natural intermediate scaling collapses to one of the already-audited regimes would close a broad class of localized Weil Hamiltonian constructions without testing them one at a time.

## Decisive test

Define a candidate family entirely from the localized **completed** Weil operator and its natural localization parameter. Before using zero information, specify:

1. the moving depth or frequency/regularity scale and why it is canonical;
2. how the already-forced pole/PNT cancellation of `PL-059` is represented, without adding a free rank-one counterterm;
3. the topology or relative operator/form category in which convergence is claimed;
4. how the archimedean logarithmic frequency behavior is controlled on the same moving states that can witness prime-log recurrence.

Then prove convergence and compute a nontrivial limiting or spectral-shift invariant. Test the same construction on Beurling systems or another matched prime-frequency control. A useful positive outcome must retain information beyond the universal residue/PNT cancellation without inheriting the unsmoothed essential partial-reflection obstruction and without merely rewriting the classical explicit formula.

A negative outcome would show that every canonical candidate either universalizes in strong topology, remains noncompact in essential norm, or becomes explicitly zero-driven only after a smoothing that imports the known formula.

## Evidence boundary

No mesoscopic topology with the desired properties is currently established. `PL-055`--`PL-056` rule out every fixed `L`-independent compact/Sobolev smoothing, including the static critical `det_2` endpoint. `PL-057` additionally rules out raw spatial decompactification `R(L)->infinity` under the natural `exp(-L)` normalization: the family is exponentially tight in boundary deficit, has the same universal half-line PNT strong limit, and retains the same order-one Calkin recurrence defect.

`PL-058` closes the most direct amplified spatial-tail repair. Moving the two endpoint layers inward by total depth `D` and multiplying by the compensating factor `exp(D/2)` is exactly unitarily equivalent to the original boundary family with smaller effective half-length `L-D/2`; the identity uses only finite-section translation geometry and survives matched generalized-prime systems. Thus neither raw growing depth nor pure spatial recentering with the natural PNT-scale amplitude compensation creates an intermediate topology.

`PL-059` closes a different ambiguity: the universal rank-one PNT term does not require an externally chosen subtraction. In the completed Weil form, the zeta-pole contribution converges in norm to exactly the same boundary operator and cancels the prime PNT mode. The bounded pole-minus-prime residual therefore tends strongly to zero while its essential norm stays bounded below by the same `1-exp(-R)` recurrent gap. On each fixed smooth boundary profile, the scalar and archimedean terms are lower order after the `exp(-L)` normalization, but this does **not** give a uniform full-operator statement at moving boundary frequency.

A useful moving topology would therefore need additional `L`-dependent frequency/regularity structure or a genuinely global full-Weil scaling. Its existence remains a research question, not evidence. In particular, the archimedean sector cannot simply be discarded: its logarithmic frequency growth is negligible on each fixed smooth profile at the first boundary scale but can compete on precisely the high-frequency states that witness the Calkin defect.

## Research disposition

Accepted for active investigation, but narrowed by `PL-055`--`PL-059`. Every fixed `L`-independent compact Sobolev sandwich suppresses the high-frequency recurrence and upgrades the `PL-051` PNT boundary limit to norm/Schatten convergence. For fixed order `s>1/2`, the trace-class Fredholm determinant converges to the elementary rank-two determinant of the universal PNT mode. `PL-056` closes the static endpoint `s=1/2` as well: the full smoothed family converges in `S_2`, so the canonical `det_2` has the same universal rank-two limit, while the critical full-reflection atom has only the generic `1/k` weak-trace residue `R/pi` (twice that in the two-end absolute channel) and an elementary hyperbolic-sine `det_2` ladder. The apparent smoothing threshold is therefore ordinary one-dimensional ideal geometry, not zeta-critical rigidity.

`PL-057` closes a second natural escape: letting the raw boundary depth grow, by itself, does not create an intermediate order-one regime. Uniform Chebyshev tightness confines the naturally normalized operator mass to an `O(1)` deficit layer, so every `R(L)->infinity` has the same half-line PNT strong limit, while fixed-depth compression embeds the `PL-053` recurrence obstruction and keeps the centered residual at essential norm at least `1` asymptotically. Growing spatial depth therefore neither stabilizes the recurrent defect nor exposes a new rational-prime-specific limit.

`PL-058` closes the corresponding **pure spatial amplification** escape. For inward depths `d_-`, `d_+`, total depth `D=d_-+d_+`, and effective half-length `L'=L-D/2`, the canonically amplified interior-layer operator is exactly `B_(L',R)`. Hence any regime with `L'->infinity` inherits the same strong/norm/Calkin and fixed-smoothing results already proved for the outer boundary, while bounded `L'` contains only a uniformly finite prime-power lag set. The factor `exp(D/2)` is therefore only the scalar needed to restore the smaller window's natural normalization, not a new arithmetic counterterm.

`PL-059` now identifies the **canonical centering inside the completed Weil object itself**. The zeta pole cancels the universal PNT rank-one boundary mode in norm, so the pole-minus-prime sector tends strongly to zero, but finite-rank pole completion cannot alter the `PL-053` essential recurrence. The research target is therefore no longer to discover a natural PNT subtraction. It is specifically to find, or rule out, a simultaneously moving frequency/regularity topology for this already-centered completed residual in which the archimedean logarithmic frequency cost and the atomic prime-log recurrence balance nontrivially. Candidate forms include a boundary-frequency cutoff tending to infinity, a Sobolev order `s(L)` weakening with `L`, or another full-Weil form-domain scaling that is not conjugate to the spatial recentering of `PL-058`. Any surviving invariant must distinguish the rational-prime system from matched generalized-prime controls and must not obtain its zero divisor merely by smoothed insertion of the classical explicit formula.

`PL-060` now closes a first **genuinely moving** regularization regime. If `r_(L,R)` denotes the relative PNT remainder on the fixed-ratio boundary shell, then compression of the canonically centered pole-minus-prime residual to the first `N` Dirichlet modes is `O_R(N^2 r_(L,R)+exp(-L))`. Hence every growing cutoff with `N(L)^2 r_(L,R)->0` still collapses in operator norm. Likewise, a moving Sobolev order `s_L->0` still gives full norm collapse whenever `s_L log(1/r_(L,R))->infinity`. These conditions are sufficient rather than sharp, and they do not yet control the archimedean form on the moving states. The accepted target is therefore narrowed to the transition where the frequency cutoff reaches the quantitative PNT-resolution scale, or the Sobolev order weakens at least as fast as the inverse logarithmic PNT accuracy, **together with** a simultaneous treatment of the archimedean logarithmic-frequency cost. Merely allowing `N(L)->infinity` or `s(L)->0` is no longer a surviving mechanism.