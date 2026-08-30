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
---

# Is there a canonical mesoscopic topology between Weil boundary homogenization and essential recurrence?

## Observation

The localized Weil operator has now been analyzed in several incompatible topologies. At sufficiently short localization scale, self-adjoint spectral reality can occur before any prime-power contribution appears. Under the natural boundary rescaling, every fixed window converges strongly to zero, while a fixed-depth blow-up yields a universal rank-one Hankel model governed by the prime number theorem. In contrast, operator norm and essential norm do not converge away: Kronecker recurrence in the prime logarithms leaves an order-one gap, and each individual prime-power threshold creates a partial-reflection channel with `+/-1` of infinite multiplicity.

Fixed smooth probes suppress the recurrence, but the surviving fluctuation is then the familiar explicit-formula zero contribution. The currently audited topologies therefore separate into three regimes: universal strong bulk, noncompact essential arithmetic recurrence, and classical explicitly zero-resolved smoothing.

## Research question

Is there a geometrically forced intermediate scale or topology — for example a depth `R=R(L)` growing with the localization parameter together with a canonical smoothing, relative norm, or weighted operator ideal — in which the universal PNT boundary component can be removed while a nontrivial zero-sensitive residual converges?

The desired object should not be defined by inserting the explicit formula or the zeta zero divisor. Its topology and normalization must come from the localized Weil construction itself, and it should distinguish the rational-prime system from matched Beurling controls.

## Why it may matter

PL-050--PL-054 show that the arithmetic signal is real but sits in a bad category for ordinary Fredholm spectral flow: it escapes fixed strong limits while remaining order one in the Calkin algebra. If a canonical mesoscopic topology exists, it could isolate the first scale at which prime-log recurrence stops being a universal/essential artifact and becomes a stable relative spectral invariant.

Conversely, proving that every natural intermediate scaling collapses to one of the three already-audited regimes would close a broad class of localized Weil Hamiltonian constructions without testing them one at a time.

## Decisive test

Define a candidate family entirely from the localized Weil operator and its natural localization parameter. Before using zero information, specify:

1. the moving depth or smoothing scale and why it is canonical;
2. the universal PNT term to be removed, if any, using an independently forced normalization;
3. the topology or relative operator category in which convergence is claimed.

Then prove convergence and compute a nontrivial limiting or spectral-shift invariant. Test the same construction on Beurling systems or another matched prime-frequency control. A useful positive outcome must retain information beyond the universal PNT rank-one model without inheriting the unsmoothed essential partial-reflection obstruction and without merely rewriting the classical explicit formula.

A negative outcome would show that every canonical candidate either universalizes in strong topology, remains noncompact in essential norm, or becomes explicitly zero-driven only after a smoothing that imports the known formula.

## Evidence boundary

No mesoscopic topology with the desired properties is currently established. `PL-055`--`PL-056` rule out every fixed `L`-independent compact/Sobolev smoothing, including the static critical `det_2` endpoint. `PL-057` additionally rules out raw spatial decompactification `R(L)->infinity` under the natural `exp(-L)` normalization: the family is exponentially tight in boundary deficit, has the same universal half-line PNT strong limit, and retains the same order-one Calkin recurrence defect. A useful moving topology would therefore need additional `L`-dependent frequency/regularity structure or a genuinely new renormalization. Its existence remains a research question, not evidence.

## Research disposition

Accepted for active investigation, but narrowed by `PL-055`--`PL-057`. Every fixed `L`-independent compact Sobolev sandwich suppresses the high-frequency recurrence and upgrades the `PL-051` PNT boundary limit to norm/Schatten convergence. For fixed order `s>1/2`, the trace-class Fredholm determinant converges to the elementary rank-two determinant of the universal PNT mode. `PL-056` closes the static endpoint `s=1/2` as well: the full smoothed family converges in `S_2`, so the canonical `det_2` has the same universal rank-two limit, while the critical full-reflection atom has only the generic `1/k` weak-trace residue `R/pi` (twice that in the two-end absolute channel) and an elementary hyperbolic-sine `det_2` ladder. The apparent smoothing threshold is therefore ordinary one-dimensional ideal geometry, not zeta-critical rigidity.

`PL-057` closes a second natural escape: letting the raw boundary depth grow, by itself, does not create an intermediate order-one regime. Uniform Chebyshev tightness confines the naturally normalized operator mass to an `O(1)` deficit layer, so every `R(L)->infinity` has the same half-line PNT strong limit, while fixed-depth compression embeds the `PL-053` recurrence obstruction and keeps the centered residual at essential norm at least `1` asymptotically. Growing spatial depth therefore neither stabilizes the recurrent defect nor exposes a new rational-prime-specific limit.

The unresolved question is now specifically whether the localized Weil construction forces a **simultaneously moving frequency/regularity topology or a canonically amplified tail renormalization** — for example a boundary-frequency cutoff tending to infinity, a Sobolev order `s(L)` that weakens with `L`, a joint `R(L)`/frequency scaling, or another normalization forced by the full Weil geometry — for which the PNT layer can be removed while a nontrivial rational-prime-specific residual converges and fails matched Beurling controls. Fixed smoothing, the fixed critical `det_2` endpoint, static weak-trace residues, compact/Schatten counterterms, raw threshold Fredholm flow, and raw growing depth are excluded by `PL-053`--`PL-057`; no surviving moving topology is currently established.