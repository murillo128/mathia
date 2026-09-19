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
  - research/visual_exploration/findings/VIS-319-wang-bezout-strip-restores-prime-sieve-dimension.md
  - research/visual_exploration/findings/VIS-320-wang-bezout-strip-subperiod-rational-rotation.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The fixed-power branch is already reduced to a classical arithmetic envelope: `VIS-283`--`VIS-293` isolate the source channel and show that half-plane pole exclusion for the squared-von-Mangoldt transform is RH-equivalent rather than a new continuation mechanism. `VIS-294`--`VIS-298` remove the apparent moving lower-source barrier by exact gamma recentering.

For the moving upper pointwise branch, `VIS-301`--`VIS-304` move the first generic error wall to the weighted Hilbert bound `R_(x,H)(T)=O(x log log(3x))`. `VIS-305`--`VIS-309` then show that density, exact prime-power support, same-base harmonic phase structure, and even the true deterministic long-time quadratic mean do not by themselves explain an `H`-scale obstruction at `H asymp x log log x`.

`VIS-310`--`VIS-312` expose hard-cutoff/global-gap and full-spectrum nearest-neighbor artifacts. `VIS-313` replaces them by a cutoff-free dyadic ratio-shell decomposition and obtains, with `L=log(3x)`,

`V^(-1) integral |R_(x,H)(T)|^2 dT << x^2 + x L^3 + x^3 L^3/V`,

so at `H asymp x ell`, `ell=log log(3x)`, the mean square is `o(H^2)` for `V >> x L^3/ell^2`.

`VIS-314` removes one of those logarithms without changing the representation. Retaining two-prime sparsity and applying the classical dimension-two Selberg upper-bound sieve gives

`E_M << M v_x(M)^4 log^2(4M)`,

and therefore

`V^(-1) integral |R_(x,H)(T)|^2 dT << x^2 + x L^2 + x^3 L^2/V`,

with sufficient scale `V >> x L^2/ell^2`.

`VIS-315` identifies the missing many-frequency input. For the ordinary-prime frequencies in a dyadic shell, let `kappa_M(V)` be the maximum number of prime-ratio frequencies in a Fourier cell of width `1/V`. A coloring plus the classical separated-frequency large sieve gives

`V^(-1) integral |F_M^pp(T)|^2 dT << kappa_M(V) E_M^pp`.

A nonempty frequency cluster is, up to absolute constants, exactly a thin determinant strip `|qv-ur| << M^2/V` around another represented prime ratio `u/v`.

`VIS-316` sharpens the global criterion without proving a new density theorem. If shell-dependent excesses satisfy

`kappa_M(V) << 1 + A_M M^2/[V log^2(4M)]`,

then the Wang taper only sees

`B(x,V)=sum_(M dyadic) w(M/x) sqrt(A_M)`,

with `w(r)=r^(7/2)` below the central scale and `w(r)=r^(-1/2)` above it. At `V asymp H asymp x ell`, the natural-window mean square follows from the weaker aggregate condition `B(x,x ell)=o(ell^(3/2))`.

`VIS-317` rules out scalar determinant-only sieving: the projection `h=qv-ur` preserves ratio closeness but erases the two coordinatewise odd-prime exclusions. `VIS-318` closes the opposite fixed-slice shortcut: every represented same-shell exact determinant fibre contains only `O(1)` lattice candidates, so there is no long affine sifting variable inside one `h`-slice.

`VIS-319` resolves the apparent missing sieve dimension without solving the density problem. Choosing `a,b` with `au-bv=1` and writing

`q=ut-bh`, `r=vt-ah`

is a unimodular bijection of `Z^2`, so modulo every prime the joint `(t,h)` coordinates retain exactly the two-prime local factor `(1-1/ell)^2`. The shell preimage is nevertheless a long thin domain: `h` has length `D asymp M/log log M`, while each `h`-fibre has fewer than three `t` values. The remaining issue is distribution across this thin moving domain, not recovery of a lost local sieve dimension.

`VIS-320` makes that domain substantially more rigid. In the natural strip `D<M/2`, the active shell boundaries never switch, the strip width is affine and below three, and all lattice points lie on at most three exact branches `t_j(h)=floor(U(h))-j`. The mask `{U(h)}+j<W(h)` is a rational rotation of exact period `m=max(u,v) asymp M`. Since the Wang determinant interval has length `D asymp M/log log M=o(m)`, the relevant sample sees less than one full period. Thus the live worst-cell problem is no longer a generic two-dimensional lattice-distribution problem: it is simultaneous primality on at most three moving rational mechanical branches over a subperiod orbit, followed by the taper-weighted aggregation of `VIS-316`.

## Research question

Two source routes remain distinct.

For the **fixed-power real-axis source**, is there a property of `mu=sum Lambda(n)^2/n delta_(log n)` strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293` that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **moving upper pointwise layer**, can one control the simultaneous-prime occupancy of the at-most-three rational mechanical branches from `VIS-320` over intervals `|h|<=D`, with `D asymp M/log log M` and rotation denominator `m asymp M`, strongly and uniformly enough that

`sum_M w(M/x) sqrt(A_M)=o((log log x)^(3/2))`

at `V asymp H asymp x log log x`? The required theorem may be an upper-bound sieve/discrepancy estimate on these subperiod branches, or a coefficient-weighted/additive-energy estimate that bypasses worst-cell occupancy. A counterexample route should instead exhibit represented slopes whose subperiod masks produce excessive prime-pair crowding in central or weakly tapered shells and whose Wang coefficient mass and phases survive aggregation.

Near-average density uniformly in every shell remains sufficient but is stronger than necessary. Full-period rational equidistribution is unavailable at the natural scale because the observed branch segment ends before one period; scalar determinant sieving and fixed-determinant long affine sieving are already excluded by `VIS-317`--`VIS-318`.

## Why it may matter

`VIS-301`--`VIS-320` have progressively converted a vague localization/spacing problem into a sharply represented arithmetic one. The sequence of reductions has removed generic coefficient majorants, ambient-spacing artifacts, hard support truncation, nearest-gap compression, unnecessary shellwise uniformity, scalar determinant information loss, fixed-slice false averaging length, and finally the apparent need for a generic two-dimensional thin-domain theorem.

The remaining representation simultaneously preserves the genuine two-prime residue exclusions and exposes the exact short geometry that must be controlled. This is useful because a proof can now target only what Wang actually needs: subperiod simultaneous-prime occupancy on at most three rational mechanical branches, aggregated through the known taper. Conversely, a negative result has an equally concrete target: produce branch segments whose arithmetic crowding is too large and remains relevant after Wang weighting.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all source, gamma, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the moving upper branch, work in the exact `VIS-319`--`VIS-320` coordinates. A next useful result must do one of three things:

- prove, uniformly in represented same-shell coprime `u,v`, an upper-bound sieve or congruence-discrepancy estimate for the at-most-three subperiod rational mechanical branches of length `D asymp M/log log M` that yields `kappa_M(V) << 1 + A_M M^2/[V log^2 M]` with `sum_M w(M/x) sqrt(A_M)=o((log log x)^(3/2))`;
- replace maximum occupancy by a coefficient-weighted/additive-energy estimate on the same branch representation whose dyadic recombination gives the `o(H^2)` natural-window conclusion without first controlling every worst cell; or
- identify a family of represented slopes whose subperiod branch masks have quantitatively excessive simultaneous-prime occupancy, then show that the associated Wang coefficient mass and deterministic phases create a sufficient exceptional contribution after tapering.

Any proposed proof should preserve both prime coordinates. Kill routes that project first to scalar `h`, freeze one determinant fibre and invoke a long one-variable sieve, or use full-period rational-rotation balance without controlling the shorter `D=o(m)` segment. Likewise, do not replace the sharp weighted destination by a much stronger uniform shell theorem unless the stronger theorem is genuinely what the available arithmetic naturally proves.

The most direct falsification experiment for the new representation is to compute, over growing same-shell coprime centers `(u,v)`, the exact three branch masks and their simultaneous-prime counts on `|h|<=D`, normalize against the local two-prime sieve density, and measure the maximal and taper-weighted excess as functions of `D/m`. A persistent central-shell excess large enough to violate the `VIS-316` aggregate scale would kill the optimistic occupancy route; absence of such excess is only motivation for a theorem, not evidence of one.

## Evidence boundary

`VIS-304` remains only an upper bound for the actual pointwise remainder. `VIS-305`--`VIS-309` are controls or iterated long-time statements, not pointwise cancellation at every height. `VIS-310`--`VIS-314` are finite-window proof-method reductions and improvements.

`VIS-315` proves the local-density reduction but no prime-ratio occupancy theorem. `VIS-316` proves only that shell excess may be aggregated with the existing Wang taper before imposing a sufficient condition. `VIS-317` and `VIS-318` rule out two lossy or too-short sieve parametrizations. `VIS-319` proves that the joint Bézout coordinates preserve the exact dimension-two local residue factor but does not control the thin-domain sieve remainder. `VIS-320` proves the at-most-three-branch rational-rotation decomposition and the subperiod relation `D=o(m)`; it does not prove prime counts, discrepancy, pseudorandomness, or a Wang natural-window estimate.

Nearby Beatty/mechanical-sequence and short-interval prime-sieve literature establishes that floor/rotation structure plus primality is classical, but the sources audited in `VIS-320` do not directly supply this moving rational, denominator-`asymp M`, subperiod, simultaneous-two-prime regime. No stronger RH criterion, new prime-distribution theorem, pointwise Wang asymptotic, or moving-`x(T)` theorem is established.

## Research disposition

Outcome so far: **the moving upper-source frontier is now an explicit subperiod simultaneous-prime branch problem rather than an unspecified strip-density problem**. The correct representation has at most three rational mechanical branches, exact period `m=max(u,v)`, natural observation length `D=o(m)`, and the full two-prime local sieve factor still present before restriction to the short branch segment.

The clue remains accepted and live. The sharp next target is uniform subperiod branch discrepancy/sieve control, an equivalent Wang-weighted energy theorem, or a coherent violating branch family that survives the taper. Re-deriving sieve dimension, using full-cycle rational balance, projecting again to `h`, or returning to fixed-fibre long-sieve arguments would not advance the remaining obstruction.