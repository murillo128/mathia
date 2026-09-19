---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-283-wang-fixed-source-cross-frequency-separation.md
  - research/visual_exploration/findings/VIS-293-wang-source-dirichlet-rh-half-plane.md
  - research/visual_exploration/findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md
  - research/visual_exploration/findings/VIS-301-wang-zero-free-localization-log-squared-window.md
  - research/visual_exploration/findings/VIS-302-wang-weighted-mean-value-log-boundary.md
  - research/visual_exploration/findings/VIS-303-wang-odd-shift-power-two-sparsity.md
  - research/visual_exploration/findings/VIS-304-wang-prime-power-spacing-loglog-boundary.md
  - research/visual_exploration/findings/VIS-305-cramer-parity-control-loglog-spacing-norm.md
  - research/visual_exploration/findings/VIS-306-bernoulli-signed-shell-hilbert-cancellation.md
  - research/visual_exploration/findings/VIS-307-prime-power-random-phase-hilbert-cancellation.md
  - research/visual_exploration/findings/VIS-308-base-prime-harmonic-phase-cancellation.md
  - research/visual_exploration/findings/VIS-309-wang-bohr-time-haar-equivalence.md
  - research/visual_exploration/findings/VIS-310-wang-hard-truncation-global-gap-quintic-horizon.md
  - research/visual_exploration/findings/VIS-311-wang-weighted-gap-cubic-horizon.md
  - research/visual_exploration/findings/VIS-312-wang-dense-ratio-spectrum-no-nearest-spacing.md
  - research/visual_exploration/findings/VIS-313-wang-dyadic-ratio-shell-linear-horizon.md
  - research/visual_exploration/findings/VIS-314-selberg-prime-pair-sieve-wang-shell-log-square.md
  - research/visual_exploration/findings/VIS-315-prime-ratio-local-density-natural-window-criterion.md
  - research/visual_exploration/findings/VIS-316-wang-weighted-shell-occupancy-criterion.md
  - research/visual_exploration/findings/VIS-317-wang-determinant-projection-loses-prime-sieve-dimension.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The fixed-power branch is already reduced to a classical arithmetic envelope: `VIS-283`--`VIS-293` isolate the source channel and show that half-plane pole exclusion for the squared-von-Mangoldt transform is RH-equivalent rather than a new continuation mechanism. `VIS-294`--`VIS-298` remove the apparent moving lower-source barrier by exact gamma recentering.

For the moving upper pointwise branch, `VIS-301`--`VIS-304` move the first generic error wall to the weighted Hilbert bound `R_(x,H)(T)=O(x log log(3x))`. `VIS-305`--`VIS-309` then show that density, exact prime-power support, same-base harmonic phase structure, and even the true deterministic long-time quadratic mean do not by themselves explain an `H`-scale obstruction at `H asymp x log log x`.

`VIS-310`--`VIS-312` expose hard-cutoff/global-gap and full-spectrum nearest-neighbor artifacts. `VIS-313` replaces them by a cutoff-free dyadic ratio-shell decomposition and obtains, with `L=log(3x)`,

`V^(-1) integral |R_(x,H)(T)|^2 dT`
` << x^2 + x L^3 + x^3 L^3/V`,

so at `H asymp x ell`, `ell=log log(3x)`, the mean square is `o(H^2)` for

`V >> x L^3/ell^2`.

`VIS-314` removes one of those logarithms without changing the representation. Retaining two-prime sparsity and applying the classical dimension-two Selberg upper-bound sieve gives

`E_M << M v_x(M)^4 log^2(4M)`,

and therefore

`V^(-1) integral |R_(x,H)(T)|^2 dT`
` << x^2 + x L^2 + x^3 L^2/V`,

with sufficient scale

`V >> x L^2/ell^2`.

`VIS-315` identifies the missing many-frequency input. For the ordinary-prime frequencies in a dyadic shell, let `kappa_M(V)` be the maximum number of prime-ratio frequencies in a Fourier cell of width `1/V`. A coloring plus the classical separated-frequency large sieve gives

`V^(-1) integral |F_M^pp(T)|^2 dT << kappa_M(V) E_M^pp`.

A nonempty frequency cluster is, up to absolute constants, exactly a thin determinant strip

`|qv-ur| << M^2/V`

around another represented prime ratio `u/v`.

`VIS-316` sharpens the global criterion without proving a new density theorem. If shell-dependent excesses satisfy

`kappa_M(V) << 1 + A_M M^2/[V log^2(4M)]`,

then the Wang taper only sees

`B(x,V)=sum_(M dyadic) w(M/x) sqrt(A_M)`,

with `w(r)=r^(7/2)` below the central scale and `w(r)=r^(-1/2)` above it. At `V asymp H asymp x ell`, the natural-window mean square follows from the weaker aggregate condition

`B(x,x ell)=o(ell^(3/2))`.

`VIS-317` now rules out one tempting compression of that determinant-strip problem. For every odd prime `p` away from the fixed source factors and every determinant residue `h mod p`, there are nonzero residues `q,r mod p` with `qv-ur=h`; in fact the exact count is `p-1` for `h=0` and `p-2` otherwise. Thus the scalar determinant coordinate preserves ratio closeness but has **no odd-prime forbidden residue classes inherited from the two primality conditions**. A direct one-dimensional sieve of `h` cannot manufacture the missing `1/log^2 M` density factor by residue exclusion. The relevant sieve/local-density argument must retain the pair coordinates, an equivalent two-linear-form parametrization of each determinant slice, or use the coefficient-weighted/additive-energy alternative.

Thus uniform control of every arithmetic-height shell is stronger than the destination estimate needs, while scalar determinant-only sieving is weaker than the arithmetic structure needs. The genuinely dangerous region remains the weighted neighborhood `M asymp x`, but the next proof representation must preserve the two prime channels there.

## Research question

Two source routes remain distinct.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293` that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **moving upper pointwise layer**, can one prove a taper-weighted local-density or sparse-energy estimate strong enough that

`sum_M w(M/x) sqrt(A_M)=o((log log x)^(3/2))`

at `V asymp H asymp x log log x`, **while retaining the pair-coordinate prime structure that `VIS-317` shows is lost under scalar determinant projection**? Equivalently, can a pair-lattice/dimension-two sieve or a weighted additive-energy estimate control the central thin determinant strips at Fourier resolution, or can one exhibit represented slopes whose strip crowding and deterministic phase coherence violate the aggregate scale?

Near-average density uniformly in every shell remains sufficient, but it is no longer the minimal target, and a one-dimensional residue sieve on `h=qv-ur` is no longer a viable mechanism for obtaining it.

## Why it may matter

`VIS-301`--`VIS-317` have successively removed localization leakage, generic coefficient majorants, ambient spacing, support-sensitive absolute spacing, increasingly faithful random-phase controls, generic deterministic Bohr-time alignment, hard support truncation, global minimum-gap compression, dense-spectrum nearest-neighbor failure, one logarithm caused by discarding prime-pair sparsity, ambiguity about the relevant Fourier-cell density, unnecessary uniformity across dyadic arithmetic height, and now a representation that erases the two coordinatewise prime-sieve exclusions.

The present frontier is narrower. A determinant-strip theorem only needs to control the **taper-weighted shell profile** strongly enough for the natural window, but it cannot obtain the necessary prime-density scale by sieving the scalar determinant coordinate alone. Conversely, a putative obstruction must survive the Wang weighting: a spectacular cluster far from `M asymp x` is not structurally relevant unless its excess overcomes the shell taper and its Wang coefficients remain coherent.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all source, gamma, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the moving upper branch, start from `VIS-315`--`VIS-317`. A next useful result must do one of three things:

- prove pair-coordinate thin-strip bounds equivalent to `kappa_M(V) << 1 + A_M M^2/[V log^2 M]` with `sum_M w(M/x) sqrt(A_M)=o((log log x)^(3/2))` at `V asymp x log log x`, for example by parametrizing `qv-ur=h` as two affine linear forms and obtaining a uniform dimension-two sieve estimate over the required moving range;
- replace maximum occupancy by a coefficient-weighted/additive-energy large-sieve estimate whose dyadic recombination gives the same `o(H^2)` natural-window conclusion without first taking worst-cell density in each shell; or
- identify a family of represented slopes in the central or sufficiently weakly tapered shells whose determinant-strip crowding violates the aggregate criterion, then show that the corresponding Wang coefficient mass and deterministic phases create a quantitatively sufficient exceptional contribution rather than a large but harmless cluster.

Kill any proposed proof route that first projects to scalar `h` and then claims the two-prime `log^{-2} M` saving solely from forbidden determinant residue classes: `VIS-317` shows those odd-prime exclusions are absent. A result that merely reapplies a hard support cutoff, a global/nearest frequency gap, the same two-point fixed-shift upper sieve, or uniform shell control much stronger than the weighted destination requires is likewise no longer the sharp decision boundary.

## Evidence boundary

`VIS-304` remains only an upper bound for the actual pointwise remainder. `VIS-305`--`VIS-309` are controls or iterated long-time statements, not pointwise cancellation at every height. `VIS-310`--`VIS-314` are finite-window proof-method reductions and improvements.

`VIS-315` proves the local-density reduction but no prime-ratio occupancy theorem. `VIS-316` proves only that the shell excess may be aggregated with the existing Wang taper before imposing a sufficient condition. `VIS-317` proves an exact local representation obstruction: scalar determinant values have no odd-prime forbidden residue class coming from simultaneous nonvanishing of `q` and `r`. It does **not** disprove the occupancy estimate, bound any `A_M`, exclude singular-series dependence on `h`, or replace the missing pair-coordinate/local-energy theorem.

Nearby sparse-large-sieve and Beatty-prime literature does not, by the statements audited in `VIS-315`, automatically provide the required moving-slope two-prime strip control. No stronger RH criterion, new prime-distribution theorem, pointwise Wang asymptotic, or moving-`x(T)` theorem is established.

## Research disposition

Outcome so far: **the moving upper-source branch has progressed from a polynomial finite-window barrier to a taper-weighted prime-ratio local-density criterion at the natural window, and the determinant-only sieve shortcut has been closed**. The remaining mean-square problem is to control the weighted dyadic profile while retaining the pair-coordinate prime structure, obtain an equivalent weighted-energy bound, or turn a violating central cluster into a genuine exceptional-height obstruction.

The clue remains accepted and live. Another minimum-gap estimate, another two-point shell-mass refinement, a scalar determinant residue sieve, or a uniform density theorem that ignores the already available shell taper is not the sharp next target; the next contribution should attack the pair-preserving weighted thin-determinant/local-energy frontier or exhibit a coherent exception that survives it.