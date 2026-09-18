# MI-051 — Non-reversible positivity can carry orientation without forcing it

**Evidence level:** exact synthesis from [WP-354](../../findings/WP-354-bi-invariant-matrix-metric-cannot-couple-scalar-phase-orientation.md) and [WP-355](../../findings/WP-355-bi-invariant-randers-positivity-carries-central-orientation-only-as-a-free-closed-boundary-term.md). The classification of invariant quadratic forms, Randers construction, closed-one-form mechanism and bi-invariant Finsler background are classical; the Mathia content is the matched-control consequence for the scalar scattering-phase sign problem.

WP-354 shows that ordinary finite-dimensional bi-invariant quadratic geometry is too symmetric for the Weil sign. A conjugation-invariant positive quadratic form on `Herm(m)` splits the scalar center from the traceless directions, so the determinant-phase velocity enters only through an even square. Reversing the common scalar phase leaves the positive energy unchanged.

Non-reversible Finsler geometry removes that particular information loss, but WP-355 shows that this is not yet a sign theorem. For any Minkowski norm, restriction to the central line is necessarily

`F(qI)=c|q|+dq`, `c>|d|`.

The odd coefficient `d` records orientation, yet positivity constrains only its magnitude. The reverse norm `F(-H)` is equally positive and replaces `d` by `-d`. Thus allowing a non-reversible positive geometry can make the desired signed coordinate visible while leaving its orientation completely free.

The canonical bi-invariant Randers family makes the boundary especially sharp:

`F_epsilon(H)=sqrt(tr(H^2))+epsilon tr(H)/sqrt(m)`, `|epsilon|<1`.

Along a unitary path, its odd term is the determinant-phase one-form

`-(i/sqrt(m)) tr(U^* dU)=d arg det(U)/sqrt(m)`.

This one-form is closed. On a chosen lift its contribution to the action depends only on the endpoint determinant phase, and globally it records determinant winding. It therefore does not modify the fixed-endpoint local geodesic equation. The two signs of `epsilon` have the same reversible positive core and local unparameterized geodesics while carrying opposite scalar orientations.

The reusable distinction is between **retaining a signed coordinate and deriving its sign**. Reversible positivity may erase orientation completely; non-reversible positivity may preserve it but only as an extra odd datum. If reversing that datum preserves every positive/source-independent hypothesis, the construction has not produced destination-selective sign. Antisymmetrizing the two positive norms recovers the oriented scalar term only as a difference of positive quantities, which again carries no sign implication.

For the scattering/Weil interface, the next admissible question is therefore not merely whether a positive nonquadratic geometry can contain the scalar logarithmic derivative. It can. The question is whether the arithmetic source canonically fixes the asymmetry coefficient and orientation **before** the target sign is read, or whether a more global operator/order structure couples that orientation to an independently positive object. A source-defined non-reversible metric remains logically possible, but its irreversibility must be derived rather than selected to match the desired Weil sign.

**Boundary.** This does not classify all conjugation-invariant Finsler couplings between central and traceless directions, and it does not rule out a source-forced non-reversible metric. It proves only that positivity plus conjugation invariance cannot determine the central orientation: reversal is an equally admissible matched control, and in the canonical Randers realization the odd phase is a free closed boundary term rather than a positivity-generated bulk sign.
