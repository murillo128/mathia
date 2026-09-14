# MI-020 — Natural-grid target visibility has a reciprocal-height defect threshold

**Evidence level:** exact deterministic inequality and sharp matched control from [NB-129](../../findings/NB-129-target-bearing-natural-grid-phase-visibility-has-a-sharp-reciprocal-height-defect-threshold.md)

NB-128 proves that the full natural prefix has a local inverse modulus for common vertical translation, but a phase witness is useful only where the primitive amplitude is not tiny. NB-129 splices this phase geometry to the NB-117 weighted first-difference energy and identifies the exact scale at which the target can force amplitude visibility.

For a height shift `|T|~m` and endpoint-matched harmonic profile, the amplitude-weighted phase energy on the matching block `[m,2m]` obeys

`V_(m,T)(P)/|A|^2 >= c/m - C(q_R(P)^(-1)-1)`.

Thus target-angle defect `q_R(P)^(-1)-1 = O(1/|T|)` forces a visible phase packet of size `gg |A|^2/|T|`. This is the missing local coupling between phase de-aliasing and target mass.

The scale is sharp for the information supplied by NB-117 alone. An explicit endpoint-preserving residual with excess Dirichlet energy `Theta(1/m)` can cancel the harmonic profile on the entire block `[m,2m]`, making the weighted phase visibility exactly zero for every shift. Therefore a fixed positive capture fraction `q_R(P)>=c<1` is far too weak at large height: its constant angle defect lies above the reciprocal-height visibility threshold.

The next bridge cannot come from reusing the same Dirichlet energy more efficiently. It must exploit extra zero-power structure—recurrence, analyticity, or another source-specific nonconcentration law—to prevent the sharp block-erasing control. The result is local in the height window and does not contradict the far-height recurrences of fixed finite base systems.
