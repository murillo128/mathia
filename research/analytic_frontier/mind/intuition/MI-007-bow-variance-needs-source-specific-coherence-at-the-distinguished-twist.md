# MI-007 — Bow completion is an absolute, phase-sensitive endpoint-memory problem with a deterministic critical high-pass

**Evidence level:** supported by exact matched-control boundaries through [ANF-185](../../findings/ANF-185-triangular-twist-averaging-turns-critical-aperture-into-a-universal-one-height-high-pass.md). The critical detector is exact for the sector-aligned matched-control class; no current theorem supplies the required absolute estimate for the actual prime-minus-Ramanujan residual.

Target-sized bow completion consumes a positive-real shifted correlation at the distinguished logarithmic twist, equivalently an adjacent-scale Fejer-energy defect. Prime-scale matched packets can store the required `a_X=sqrt(delta X log X)` endpoint memory while remaining invisible to broad source-blind tests.

ANF-180--ANF-182 identify a sharp local-complexity scale. Fixed finite continuous probe families collapse to rank one on a carrier-adapted band, and derivative jets remain asymptotically blind whenever `r_X a_X/K -> 0`. For sector-aligned target-sized packets, order `Theta(K/a_X)` must detect an `Omega(a_X)` discrepancy.

ANF-183 identifies the same resolution boundary in physical twist coordinates. Dangerous packets of width `Theta(a_X)` remain `o(a_X)`-flat throughout every aperture `o(X/a_X)`, while critical aperture `Theta(X/a_X)` is sufficient for a symmetric three-point curvature to detect every sector-aligned target-sized packet after packet-dependent rephasing.

ANF-185 removes those adaptive ingredients. Triangular averaging over one fixed aperture, rephased only at the deterministic base `X`, gives the exact positive multiplier

`W(y)=1-sinc^2(y/2)`

and the detector

`D_T(F_X)=A_X sum_s zeta_s W(T log(1+j_s/X))`.

Subcritical apertures still admit blind dangerous packets, but for one sufficiently large fixed constant `C`, `T=CX/a_X` gives `|D_T(F_X)|>>a_X` for every sector-aligned dangerous packet. The physical transition scale of the multiplier is exactly `X/T~a_X`.

The important source-side simplification is that the aperture average is not a simultaneous shifted-height theorem in disguise. It collapses exactly to **one weighted residual sum at the original distinguished height**, with a deterministic smooth high-pass in the physical offset. The weight has uniformly bounded total variation, so Abel summation shows that this representation does not import a stronger hidden norm than distinguished-twist prefix control.

The reusable endpoint lesson is therefore sharper: once the reciprocal-width aperture is reached, generic packet discrimination is no longer the issue. The missing theorem is an absolute source estimate for a fixed, source-faithful, one-height high-pass whose transition occurs at the minimum dangerous loading width. Adaptivity in sample location or first-active-site phase is not essential.

The live alternatives are now concrete: prove `o(a_X)` control of the ANF-185 weighted prime-minus-Ramanujan residual at `T~X/a_X`, control the signed Fejer scale difference directly at the same absolute scale, or prove that actual source placement forbids the matched sector packet before either detector is invoked.

**Boundary.** Sector alignment remains a matched-control hypothesis; the actual residual can have arbitrary phases. ANF-185 is a discrimination theorem and an exact representation change, not the bow variance estimate itself. Its bounded-variation reduction also means that a sufficiently strong distinguished-twist prefix theorem would control it automatically, but no such theorem is presently available at the required scale.