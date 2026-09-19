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
  - research/visual_exploration/findings/VIS-318-wang-fixed-determinant-slices-bounded-lattice-length.md
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

`VIS-317` rules out one tempting compression of that determinant-strip problem. For every odd prime `p` away from the fixed source factors and every determinant residue `h mod p`, there are nonzero residues `q,r mod p` with `qv-ur=h`; in fact the exact count is `p-1` for `h=0` and `p-2` otherwise. Thus the scalar determinant coordinate preserves ratio closeness but has no odd-prime forbidden residue classes inherited from the two primality conditions. A direct one-dimensional residue sieve of `h` cannot manufacture the missing `1/log^2 M` density factor.

`VIS-318` closes the opposite slice-by-slice shortcut. For a represented same-shell center `u/v`, every exact determinant equation `qv-ur=h` has all integer solutions `(q,r)=(q_0+ut,r_0+vt)`, but the step vector `(u,v)` is already of size `asymp M`. Inside `M/2<q,r<=2M` the affine parameter has fewer than three units of range, so each exact `h` contains at most three lattice candidates. The full strip has `O(1+M^2/V)` candidates only after aggregating many short slices. Therefore a long dimension-two sieve cannot be obtained by freezing `h` and sieving the affine parameter separately.

Thus uniform control of every arithmetic-height shell is stronger than the destination estimate needs, scalar determinant-only sieving is weaker than the arithmetic structure needs, and fixed-determinant affine slicing is too short to supply the missing density factor. The genuinely dangerous region remains the weighted neighborhood `M asymp x`, but the next proof representation must preserve both prime coordinates **and** aggregate across the family of determinant slices, or bypass worst-cell density through weighted energy.

## Research question

Two source routes remain distinct.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293` that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **moving upper pointwise layer**, can one prove a taper-weighted local-density or sparse-energy estimate strong enough that

`sum_M w(M/x) sqrt(A_M)=o((log log x)^(3/2))`

at `V asymp H asymp x log log x`, while retaining the pair-coordinate prime structure and aggregating over the complete thin determinant strip rather than projecting to scalar `h` or freezing one exact `h`-slice? Equivalently, can a two-coordinate sieve over the strip, a rational/Beatty-type formulation of the selected pair process, or a weighted additive-energy estimate control the central Fourier-resolution clusters; or can one exhibit represented slopes whose strip crowding and deterministic phase coherence violate the aggregate scale?

Near-average density uniformly in every shell remains sufficient, but it is no longer the minimal target. Neither a one-dimensional residue sieve on `h=qv-ur` nor a long affine-form sieve on a fixed determinant slice is a viable source of the required two-prime density saving in the represented same-shell geometry.

## Why it may matter

`VIS-301`--`VIS-318` have successively removed localization leakage, generic coefficient majorants, ambient spacing, support-sensitive absolute spacing, increasingly faithful random-phase controls, generic deterministic Bohr-time alignment, hard support truncation, global minimum-gap compression, dense-spectrum nearest-neighbor failure, one logarithm caused by discarding prime-pair sparsity, ambiguity about the relevant Fourier-cell density, unnecessary uniformity across dyadic arithmetic height, a scalar projection that erases the two coordinatewise prime-sieve exclusions, and now a slice parametrization whose averaging variable has only bounded length.

The present frontier is narrower. A determinant-strip theorem only needs to control the taper-weighted shell profile strongly enough for the natural window, but it must obtain its prime-density saving from the **joint family of candidate pairs across the strip** or from an equivalent energy formulation. Conversely, a putative obstruction must survive the Wang weighting: a spectacular cluster far from `M asymp x` is not structurally relevant unless its excess overcomes the shell taper and its Wang coefficients remain coherent.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all source, gamma, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the moving upper branch, start from `VIS-315`--`VIS-318`. A next useful result must do one of three things:

- prove pair-coordinate thin-strip bounds equivalent to `kappa_M(V) << 1 + A_M M^2/[V log^2 M]` with `sum_M w(M/x) sqrt(A_M)=o((log log x)^(3/2))` at `V asymp x log log x`, using a sieve or distribution argument over the **whole strip/family of slices** rather than an asymptotic sieve on one fixed `h`;
- replace maximum occupancy by a coefficient-weighted/additive-energy large-sieve estimate whose dyadic recombination gives the same `o(H^2)` natural-window conclusion without first taking worst-cell density in each shell; or
- identify a family of represented slopes in the central or sufficiently weakly tapered shells whose determinant-strip crowding violates the aggregate criterion, then show that the corresponding Wang coefficient mass and deterministic phases create a quantitatively sufficient exceptional contribution rather than a large but harmless cluster.

Kill any proposed proof route that first projects to scalar `h` and then claims the two-prime `log^{-2} M` saving solely from forbidden determinant residue classes: `VIS-317` shows those odd-prime exclusions are absent. Also kill a route that fixes one exact determinant and claims the saving from a long two-linear-form Selberg sieve in the affine parameter: `VIS-318` shows that parameter has only bounded length for represented same-shell centers. Another hard support cutoff, global/nearest frequency gap, the same two-point fixed-shift upper sieve, or uniform shell control much stronger than the weighted destination requires is likewise not the sharp decision boundary.

## Evidence boundary

`VIS-304` remains only an upper bound for the actual pointwise remainder. `VIS-305`--`VIS-309` are controls or iterated long-time statements, not pointwise cancellation at every height. `VIS-310`--`VIS-314` are finite-window proof-method reductions and improvements.

`VIS-315` proves the local-density reduction but no prime-ratio occupancy theorem. `VIS-316` proves only that the shell excess may be aggregated with the existing Wang taper before imposing a sufficient condition. `VIS-317` proves an exact local representation obstruction: scalar determinant values have no odd-prime forbidden residue class coming from simultaneous nonvanishing of `q` and `r`. `VIS-318` proves that each represented same-shell exact determinant slice contains only `O(1)` candidate lattice points, so the fixed-slice affine parameter is not a long sifting variable. Neither finding disproves the occupancy estimate, bounds any `A_M`, or supplies the missing joint strip/energy theorem.

Nearby sparse-large-sieve, Beatty-prime, linear-form sieve, and binary-form sieve literature does not, by the statements audited so far, automatically provide the required moving-slope two-prime strip control. No stronger RH criterion, new prime-distribution theorem, pointwise Wang asymptotic, or moving-`x(T)` theorem is established.

## Research disposition

Outcome so far: **the moving upper-source branch has progressed from a polynomial finite-window barrier to a taper-weighted prime-ratio local-density criterion at the natural window, while two tempting determinant-coordinate shortcuts have been closed**. The remaining mean-square problem is to control the weighted dyadic profile with a pair-preserving argument that aggregates over the strip, obtain an equivalent weighted-energy bound, or turn a violating central cluster into a genuine exceptional-height obstruction.

The clue remains accepted and live. Another minimum-gap estimate, another two-point shell-mass refinement, a scalar determinant residue sieve, a fixed-`h` long affine-form sieve, or a uniform density theorem that ignores the already available shell taper is not the sharp next target; the next contribution should attack the joint pair-preserving weighted thin-strip/local-energy frontier or exhibit a coherent exception that survives it.