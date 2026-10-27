---
id: RGR-prime-flute-cuff-window-concentration-cancellation
type: research-graph-relation
scope: prime_flute
relation: scoped-obstruction
derived: true
---

# Cuff-window concentration and cancellation

The [[research/prime_flute/graph/prime-flute|Prime Flute graph]] separates concentration of individual traces from concentration relative to the norm of their difference. Write `H[f]=integral_R |f(t)|² sech(t) dt`, with a subscript restricting the integration region. [[research/prime_flute/mind/intuition/MI-018-nearly-equal-cuff-periods-can-hide-their-difference-outside-the-window|MI-018]] synthesizes the distinction; the findings below provide its evidence.

[[research/prime_flute/findings/PF-361-finite-corridor-windows-preserve-the-narrow-band-model-angle|PF-361]] controls the combined two-cuff difference when the entire transition/retained strip is sufficiently narrow. Its relative Turán–Nazarov estimate does not require frequency separation and survives the specified straight-coordinate model's transition infimum. Actual boundary transport and omitted pant/seam energies remain separate obligations.

[[research/prime_flute/findings/PF-367-exact-cuff-lattice-packets-obstruct-broad-band-corridor-comparison|PF-367]] constructs a single-lattice packet escaping sufficiently short windows. Its actual-window comparison needs a power-sized neighboring gap jump; such exceptional prime subsequences remain unproved. [[research/prime_flute/findings/PF-368-fixed-single-cuff-bands-concentrate-in-actual-windows-in-density|PF-368]] strengthens the positive side to all coefficient combinations in every fixed finite single-cuff frequency span. Its bound is

\[
H_{>T}[f]/H[f]\le(4N^2/\pi)e^{c(W)L-T},\qquad c(W)<1/2.
\]

Thus prescribed prime windows concentrate each such band in prime-index density. Neither source bounds a two-lattice tail by the norm of the difference.

[[research/prime_flute/findings/PF-369-nearly-equal-cuff-lattices-hide-broad-band-residual-mass-beyond-actual-windows|PF-369]] supplies the counterexample to that inference. For `n=ceil(alpha L)`, `alpha>1/log(16)`, and distinct periods `L'=L+delta_L` with `|delta_L|=o(L²e^(-L/2))`, exact-lattice traces on indices `n,...,3n` have difference `g_L` satisfying

\[
\frac{H_{[-L/2,L/2]}[g_L]}{H[g_L]}
\le C_\alpha\left(\frac{e^L}{n^2 16^n}
+\frac{\delta_L^2e^L}{L^4}\right)\longrightarrow0.
\]

The proof's [[research/prior_art/incremental/PA-exponential-divided-differences|classical divided differences]] approximate a periodic Fourier remainder with a linear factor. PF-369 explicitly controls that approximation against `H[g_L]>=cL²e^(-L)`, rather than relying on a fixed-period confluent limit. The [[research/prime_flute/findings/PF-001-exact-cuff-coordinate|exact cotangent cuff formula]] realizes `delta_L~8e^(-L/2)` on the composite-label flute `6m+3`. Its prescribed window has `L/2-T=1+log(2/vartheta)+o(1)>0`. With `alpha=1/2`, the window fraction is `O(L^(-4))` even though each individual trace concentrates there by PF-368.

This obstructs a broad-band scalar comparison from those geometric assumptions alone. Separate bounds have denominator `H[f_L]+H[f_(L')]`, which can dwarf `H[g_L]`. Individual coefficient sums grow like `L/|delta_L|`; common scaling does not remove their relative energy cost. Equal periods collapse to one lattice and do not admit this divided-difference construction. Realification preserves the obstruction with real zero-mean traces, with both frequency signs included when applying a single-cuff span bound.

PF-361's narrow combined-band theorem survives. No prime subsequence, minimizing residual, full pant-energy comparison, completed-operator compactness or RH obstruction is established. The possible arithmetic/energy repair is already explicit in PF-369 and is not promoted here to a new clue or a proved graph edge. This is one scalar-comparison frontier episode, not a closure of the localized-scattering Atlas territory.
