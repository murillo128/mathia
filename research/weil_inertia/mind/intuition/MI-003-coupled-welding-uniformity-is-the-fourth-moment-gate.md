# MI-003 — The fourth-moment welding difficulty survives every source-agnostic reboxing

**Evidence level:** supported for the exact source reductions, sparsity/density theorems, and controlled power region; the remaining weighted-energy/multivariate analytic bridge is open

## Core intuition

The unresolved Yang--Yang fourth-moment obstruction is now a source-faithful representation problem with a quantitative conservation law. Keeping the physical lock pays growing coefficients; freeing the shifts pays a power-sparse two-dimensional incidence selector; fixed finite `L^p` control still pays a power through duality; coordinate-wise pruning cannot densify the long-shift relation; scalar LCM projection loses the incidence sparsity and in fact has near-linear effective support; and aggregating the bases produces a fixed-coefficient multivariate polynomial system outside the audited quantitative theorem interface. None of these source-agnostic changes removes the hard part.

## Strongest justified principle

WI-047--WI-054 separate the deterministic local main from the analytic residual and establish a genuine controlled power region. WI-055--WI-057 show that marginal pair discrepancy and one-sided dispersion do not automatically control the conditioned four-prime covariance.

WI-068--WI-070 identify the original three representations. Free independent shifts make finite-complexity prime-pattern input available only after projecting back to the exact slope slice `(h_1,h_2)=(rk,qk)`, while varying-base aggregation produces a source-faithful degree-two multivariate polynomial system with anisotropic boxes and outer source weights.

WI-071 shows that even after aggregating all primitive slopes, the physical shift incidence support lies inside `lcm(|h_1|,|h_2|) << X` and the maximally enlarged envelope has only `O(X(log X)^2)` points in an ambient `X^2` square. WI-072 makes the resulting norm cost exact: a selector of density `delta` has dual norm at least `delta^{-1/p}` against every fixed finite `L^p` ambient estimate. WI-073 closes separate coordinate pruning: on long-shift shells the same source has `gcd(|h_1|,|h_2|)=|k|`, and extremal GCD/LCM theory prevents subpolynomially dense Cartesian reboxing from making the relation positive-density.

WI-075 correctly warns that projecting incidences to the scalar `L=lcm(|h_1|,|h_2|)` need not preserve two-dimensional sparsity. WI-076 now resolves the missing weighted-support cardinality in the opposite direction. On one fixed source slope `(b_1,b_2)=(5,7)`, Bienvenu's finite-complexity prime-pattern asymptotic plus a trivial slice multiplicity bound gives

\[
\#\mathcal L^{\rm eff}(X)\gg X/(\log X)^4.
\]

Thus the **actual nonzero weighted scalar LCM support is not power-sparse**. A scalar sparse-large-sieve strategy cannot obtain the needed power localization gain from support cardinality. The useful scalar structure, if any, must be subtler: weighted cancellation, additive energy, factorization labels, or another theorem exploiting the source weights rather than mere set size.

The conservation law is therefore sharper than before. The two-dimensional incidence is power-sparse and expensive to restrict from ambient boxes; its scalar projection is near-linear and loses that cheap sparsity asset; the multivariate representation preserves the source but crosses a theorem boundary. Difficulty moves between coefficient size, incidence sparsity, weighted scalar structure, and multivariate polynomial complexity.

## What remains possible

The surviving interfaces are precise: a Yang-specific weighted incidence/rectangle estimate; a scalar theorem exploiting the actual weights/additive energy rather than support cardinality; a labelled scalar transform retaining reduced-slope factorization; or a quantitative multivariate polynomial von-Mangoldt theorem with the actual anisotropic boxes and outer weights. The base-aggregated polynomial representation remains especially important because it avoids projecting an ambient theorem back onto a sparse slice.

A generic free-shift theorem, fixed-`L^p` ambient bound, Cartesian reboxing, or scalar support-counting argument is insufficient. Any scalar route must now prove a nontrivial **weighted** property beyond the near-linear support forced by WI-076.

## Status / novelty

The lock identities and source reductions are persisted findings. Hölder/Parseval, GCD/LCM extremal theory, Bienvenu's prime-pattern theorem, and sparse-modulus large-sieve theory are classical/prior-art inputs. The synthesis is a sharpened theorem-interface statement, not a proof that the Yang route is impossible.

## Falsification criterion

Produce a source-agnostic fixed-`L^p` or Cartesian restriction avoiding the proved sparsity costs, or a scalar support-cardinality theorem giving a power saving despite WI-076's `X/(log X)^4` lower bound. A positive advance should instead close one weighted/source-faithful interface with every normalization and source condition explicit.

## Lean-formalizable core

- Locked-to-free lcm/gcd identities.
- LCM-sublevel incidence cardinality bound.
- Sharp selector dual-norm lower bound.
- Cartesian large-GCD density implication.
- Multiplicity conversion from positive weighted first moment to near-linear effective scalar support.
