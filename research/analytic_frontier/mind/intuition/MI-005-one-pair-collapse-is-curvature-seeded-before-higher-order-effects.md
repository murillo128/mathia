# MI-005 — One-pair scalar reversal is curvature-seeded through ten points, and six-point danger is confined to a notch boundary layer

**Evidence level:** exact and source-validated through ANF-071, with the ANF-070 spatial floor supported by an explicit interval certificate plus analytic continuation of the bound

## Core intuition

For a nonnegative one-pair spectrum with at most eight real anchors, finite-height collapse reversal is not an independent higher-order phenomenon: it can occur only when the quadratic curvature already points downward. In the Montgomery--Taylor six-point case even that full curvature-seeded descent is screened by positive spatial affine slack. A small central notch can create a new reversal only by perturbing a base configuration lying within a shrinking neighborhood of the curvature boundary `D=0`, and the corresponding height is forced toward zero.

The conceptual separation is therefore sharper than “curvature is not the affine verdict.” **Base curvature decides whether the one-pair scalar energy wants to collapse; spatial slack screens the complete base reversal branch; and the only residual six-point notch problem is a singular perturbation layer where curvature, notch size, and affine multiplicity slack must be compared on their common shrinking scale.**

## Strongest justified principle

ANF-069 gives the all-order one-pair coefficient theorem. Through eight real anchors, higher coefficients have the favorable sign, so a finite-height reversal is seeded by negative quadratic curvature and has at most one positive crossing.

ANF-070 then proves the missing Montgomery--Taylor spatial comparison. Its certified lower bound `F(t) >= r(t)/8`, with a strict surplus on the active-deficit region, forces a uniform positive six-point affine margin for every four-anchor configuration with `D(T)<0` at every height. Thus the complete base-profile reversal branch is affine-safe; sufficiently small admissible central notches also preserve a fixed margin on the branch where the base profile actually reverses.

ANF-071 treats the complementary base-nonreversing regime. If `D(T)>=0` but the notched profile reverses, then necessarily `0 <= D(T) < s b_eta eta^3`, the notched curvature defect is at most the same scale, and every reversing height satisfies the explicit `O(sqrt(s b_eta eta^3))` bound. Outside that strip the notched profile cannot reverse at any height.

## What remains possible

The complete one-pair six-point central-notch inequality is not yet proved. The remaining base-nonreversing branch is a local problem near `D=0, y=0`: the collapsed real-multiplicity affine slack must be compared against the small negative notch-induced collapse defect. A vanishing first-order slack on the curvature boundary could still expose a genuine notch obstruction.

At total cardinality eleven and above, higher-order coefficients may in principle create a one-pair reversal not seeded by negative quadratic curvature. Multiple nonreal pairs, ordered carriers, other source profiles, and non-scalar information remain outside the one-pair theorem.

## Status / novelty

The coefficient expansion, curvature-strip reduction, and six-point affine screening are persisted exact results; the one-dimensional spatial-floor certificate has a documented computer-assisted finite step. The analytic ingredients are classical and no publication-level novelty claim is inferred. The durable synthesis is the gate structure: **through ten points the one-pair scalar dynamics are curvature-seeded; at six points the entire base reversal is already screened, leaving only a notch-induced boundary layer rather than a global finite-height search.**

## Falsification criterion

Produce a one-pair configuration with at most eight real anchors whose finite-height reversal occurs while its quadratic coefficient is nonnegative for the same nonnegative profile; invalidate ANF-070's certified spatial floor or its affine consequence; or produce a base-nonreversing six-point notch reversal outside ANF-071's curvature/height layer.
