---
id: CLUE-farey-discrepancy-ordered-plucker-refinement-transfer
type: research-clue
status: proposed
origin: visionary-researcher
target_line: farey_discrepancy
based_on:
  - research/farey_discrepancy/README.md
  - research/farey_discrepancy/clues/CLUE-farey-gap-order-bridge-suppression.md
  - research/visual_exploration/findings/VIS-026-gap-permutation-discrepancy-bridge-covariance.md
  - research/visual_exploration/findings/VIS-034-farey-low-band-suppression-factorization.md
---

# Do ordered two-level Plücker defects retain Farey cancellation beyond scalar discrepancy?

## Observation

The current Farey program already separates total discrepancy suppression from spectral allocation and requires every candidate to survive same-gap, reflection, endpoint, local-order, denominator, mediant, Franel--Landau/Möbius, amplitude, and matched-null controls. `VIS-026` establishes that the actual ordering contains information not present in the gap multiset, while `VIS-034` shows that a small low-band statistic can still factor through the global scalar discrepancy amplitude. The present proposed clue therefore changes the retained object before scalarization rather than adding another norm of the same discrepancy path.

At nested Farey orders, fix the common parent/mediant/child refinement ancestry and the same predeclared control subtraction used by the existing Farey clue. Let `u_j` and `u_{j+1}` denote the resulting consecutive controlled refinement-increment vectors. Retain the full ordered antisymmetric minor field

\[
P_{ab}(j)=u_j^{(a)}u_{j+1}^{(b)}-u_j^{(b)}u_{j+1}^{(a)}
\]

across coordinate pairs, with the ancestry orientation fixed before inspecting outcomes, and aggregate these signed minors along the refinement tree before taking any norm or band-energy scalarization. The proposed information carrier is this ordered exterior/Plücker field, not the raw Farey determinant `ad-bc=\pm1` and not a scalar spectral statistic.

## Research question

Does this controlled ordered Plücker field retain a quantitative Farey-specific cancellation signal after the same gap multiset is preserved but its admissible order is destroyed, and is that signal genuinely unavailable from the classical scalar Farey discrepancy or equivalent Möbius/totient data?

The exact control subtraction and coordinate set must be fixed from the existing Farey definitions before evaluation. A positive finite diagnostic is useful only if the same invariant is then defined unchanged at larger orders and remains nontrivial at the RH-critical normalization.

## Why it may matter

The line's unresolved possibility is that a multiscale signed relation survives precisely where total amplitude and one-scale spectral allocation collapse to classical scalar information. An antisymmetric two-level carrier can in principle retain orientation and cross-scale allocation that disappear under norms, squared energies, or gap-multiset statistics. If it survives the existing matched controls, it would give the Farey line a concrete non-scalar object on which to ask for a new quantitative theorem rather than another reformulation of the Franel--Landau criterion.

## Decisive test

First derive the exact finite-order identity for the complete Plücker aggregate, without asymptotics. Kill the route if the minors telescope, factor through the classical scalar Farey/Möbius discrepancy, reduce to the elementary Farey unimodularity relation, form a modular-symbol/cohomological coboundary, or are uniformly determined by the predeclared realizable local-order/denominator/mediant controls.

If that algebraic gate survives, compare the unchanged statistic with a realizable same-gap-multiset order-destruction control and then with the stronger controls already required by `CLUE-farey-gap-order-bridge-suppression.md`. Kill it if the ordered field is invariant under those controls or if any surviving magnitude is quantitatively too weak at the critical exponent. Do not tune the coordinate set, orientation, aggregation rule, or normalization after inspecting the control outcomes.

## Evidence boundary

Determinants, orientation, mediant refinement, modular cocycles, and signed Farey transfer structures are classical. The closest literature located in the campaign audit includes Morier-Genoud--Ovsienko, *Farey boat I* (Jahresber. DMV 121, 2019; DOI `10.1365/s13291-019-00197-7`, arXiv:`1811.01229`), Bruggeman--Muehlenbruch, *Eigenfunctions of transfer operators and cohomology* (J. Number Theory 129, 2009; DOI `10.1016/j.jnt.2008.08.003`, arXiv:`0707.1203`), and Bonanno--Isola, *A thermodynamic approach to two-variable Ruelle and Selberg zeta functions via the Farey map* (Nonlinearity 27, 2014; DOI `10.1088/0951-7715/27/5/897`, arXiv:`0907.1471`). No novelty is claimed for those ingredients, and failure to locate the exact controlled discrepancy-increment Plücker residual is not evidence of novelty.

Nothing here proves that the proposed field is nonzero, independent of scalar discrepancy, asymptotically stable, or RH-relevant. The first task is deliberately a kill test: establish the exact finite-order algebra and matched-control behavior before any asymptotic or spectral interpretation.

## Research-watch disposition after `FD-112`

`FD-112` kills the minimal local realization in which a refinement vector consists only of the two Euclidean child gaps created by one Farey mediant, with parent size removed as the nuisance coordinate. After normalization the child vector is

\[
\left(\frac{d}{b+d},\frac{b}{b+d}\right)
=\frac12(1,1)
+\frac{d-b}{2(b+d)}(1,-1),
\]

so the controlled residual is one-dimensional and every centered Plücker minor vanishes. Even the uncentered determinant is only a first difference of the scalar split imbalance `(d-b)/(d+b)`.

The clue therefore remains `proposed`, not `accepted`: its broader carrier is still plausible only if the predeclared refinement vector contains **at least two independent residual coordinates after nuisance removal**. A next test must define those coordinates self-containedly inside the Farey line—e.g. by coupling ancestry with a discrepancy/source residual—and derive their exact finite-order reduction before any diagnostic is inspected. Merely enriching the notation around left/right child gaps, or applying a nonlinear feature map to their single imbalance scalar, does not pass the representation gate.

## Research-watch disposition after `FD-113`

`FD-113` extends the representation kill test from one mediant split to any fixed or predeclared finite Stern--Brocot descendant template. After affine normalization of a parent edge `a/b<c/d`, every descendant position and selected descendant gap is a rational function of `r=b/d`, hence of the same root split imbalance `s=(d-b)/(d+b)`. Retaining a deeper Euclidean fan therefore increases ambient dimension without adding a second scalar shape parameter.

Unlike `FD-112`, deeper normalized gap vectors can have nonzero centered Plücker minors because the one-scalar image is a nonlinear curve in the gap simplex. Such a minor is still only a two-point kernel of the ordered scalar split sequence; nonzero exterior area is not evidence of an independent local residual coordinate. The clue remains `proposed` only for carriers whose second coordinate is not reconstructible from the declared parent scale, root split, and predeclared ancestry control. A state-dependent ancestry/template choice may count as a separate combinatorial channel and an independently defined discrepancy/source residual remains live, but either must be declared explicitly and tested against the classical local-order/index reductions. Fixed deeper ancestry, more descendant gaps, or nonlinear re-embeddings of those gaps do not pass the representation gate by themselves.
