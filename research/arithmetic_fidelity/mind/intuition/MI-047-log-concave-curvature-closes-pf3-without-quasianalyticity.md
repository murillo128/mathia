# MI-047 — Curvature mass turns smooth positive `PF_3` recognition into a local slope bound

**Evidence level:** exact synthesis from [AF-385](../../findings/AF-385-sampled-solid-minor-hierarchy-certifies-continuum-fixed-order-total-nonnegativity.md), [AF-388](../../findings/AF-388-shrinking-solid-pf3-excludes-quadratic-boundary-contact.md), [AF-389](../../findings/AF-389-multiscale-solid-pf3-excludes-all-finite-order-boundary-contact.md), [AF-390](../../findings/AF-390-quasianalytic-curvature-closes-multiscale-pf3-recognition.md), [AF-391](../../findings/AF-391-log-concave-logarithmic-curvature-forces-order-three-total-nonnegativity.md), [AF-392](../../findings/AF-392-adjacent-curvature-masses-exactly-characterize-smooth-order-three-fidelity.md), and [AF-393](../../findings/AF-393-positive-curvature-pf3-is-exactly-local-differential-fidelity.md).

For a positive `C^4` profile `f`, write `q=-(log f)''`. AF-392 expresses continuum order-three total positivity through every adjacent pair of curvature-mass windows. That initially looks stronger than the local differential inequality recovered from shrinking solid minors.

AF-393 shows that there is no extra positive-curvature finite-window information. On the stratum `q>0`, the translation kernel `K_f(x,y)=f(x-y)` is `TN_3` exactly when

`(log q)'' <= 2q`.

The right coordinate makes the equivalence transparent. Let `Q` be curvature mass, `dQ=q dt`, and set `r=(log q)'`. Then the condition is simply

`dr/dQ <= 2`.

The AF-392 adjacent-window inequality is the integrated form of this slope bound. Conversely, shrinking the windows differentiates it back to the same inequality. Thus local and finite-window recognition are two presentations of one intrinsic statement once position is measured by accumulated curvature rather than Euclidean distance.

This also clarifies the role of AF-391. Log-concavity of `q` is a strong sufficient condition because it makes `r` nonincreasing, but it is not the recognition variable itself. Smooth non-log-concave positive curvatures may still be `TP_3` as long as their slope in curvature mass never exceeds `2`.

The real residual fibre lies where `q=0`. There the coordinate `Q` ceases to be locally invertible, so the local slope formulation becomes singular. AF-388--AF-389 force any zero compatible with the shrinking solid hierarchy to be infinitely flat; AF-390 closes such zeros under flat-jet unique continuation, while AF-391 supplies a different global shape closure. What remains is a boundary-stratum problem: understand whether nontrivial infinitely-flat zero sets admit an exact limiting version of the curvature-mass criterion, or which weaker source hypotheses eliminate them.

**Boundary.** This synthesis does not derive the curvature inequality from arithmetic data, classify the `q=0` stratum, claim novelty over the classical `PF_3` literature, or provide a zero-selection theorem. Its durable content is the equivalence of local and finite-window recognition on `q>0` in the intrinsic curvature-mass coordinate.