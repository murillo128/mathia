# MI-005 — The scalar pair frontier is quotient-aware conditioning, not raw Gram complexity

**Evidence level:** exact projection-tax and cross-metric reductions through ANF-090; a separable-quotient conversion to destination geometry remains open

## Core intuition

The fixed central-notch scalar frontier has narrowed beyond generic nonseparability and beyond raw exponential-system conditioning. ANF-081, ANF-083, and ANF-085 control every real finite multiset, a fixed complex-height strip independent of pair count, and all-height separable center-height occupations. ANF-086 adds a fixed destination-Hilbert tube around the separable cone, while ANF-087--ANF-088 identify the exact equality locus and decompose near extremality into explicit nonnegative projection and spectral taxes.

ANF-089 then quantifies the first conditioning-to-geometry bridge: a source Gram minimum `a(W)` and destination pair-collapse Gram maximum `b_s(W)` give `d_sep(W)^2 <= [b_s(W)/(2q_s a(W))] Delta(W)/L(W)`. But ANF-090 proves that this raw ratio can diverge exponentially on configurations that are themselves exactly separable. Ill-conditioning of a particular real-collapse comparison is therefore not the invariant obstruction.

The surviving loophole is **conditioning after the already-safe separable directions have been quotiented out**. A fatal family must be nonseparable in the destination geometry and must concentrate its near-null source direction in a component that retains destination mass after the nearest safe product component is removed.

## Strongest justified principle

ANF-086 shows that certificate failure requires `d_sep(W)>=kappa_crit>0` together with sufficiently small Montgomery--Taylor excess. ANF-088 decomposes that excess exactly into nonnegative taxes and rules out hidden exact rank loss. ANF-089 proves that every uniformly bounded raw cross-metric ratio `chi_s=b_s/a` forces near extremizers toward the separable cone.

ANF-090 supplies the adversarial control that changes the interpretation of this estimate. Fixed-height, fixed-separation product families can have `chi_s(W_n)->infinity` exponentially while `d_sep(W_n)=0` identically. The small source Gram eigenvalue comes from high-order finite differences on the observation window, not from dangerous nonseparable geometry. Consequently a global theorem cannot use raw `chi_s` as an intrinsic distance-to-failure parameter.

The decisive theorem is now either a direct estimate from the ANF-088 projection taxes to `d_sep` that projects away exact product-fiber directions, or a quotient-aware cross-metric condition number whose null directions are measured only after the safe cone is removed. Only a growing family that remains far from that quotient while keeping the exact taxes small would establish a genuine scalar escape.

## Counterevidence / boundary

ANF-089 remains a valid one-sided estimate and is useful on subclasses where its raw conditioning ratio is controlled. ANF-090 does not construct a fatal configuration and does not show that quotient-aware conditioning diverges. It only proves that raw source Gram singularity can be completely benign.

The separable cone is nonlinear and may have collisions or several nearby product representatives, so “quotienting” cannot be replaced by an unsupported orthogonal projection without a precise theorem. Higher-order carriers are not justified merely because the raw ratio diverges; the divergence must survive the destination-safe quotient.

## Epistemic status

**Proved exact near-equality reduction, proved raw cross-metric bound, and proved raw-conditioning false positive on the safe cone; quotient-aware conditioning-to-destination geometry remains open.** No RH consequence is asserted.

## Falsification criterion

Construct a normalized sequence with Montgomery--Taylor excess tending to zero and `d_sep` bounded below while satisfying the exact ANF-088 taxes, and show that the ill-conditioned direction retains destination mass after every admissible separable comparison. Conversely, a source-faithful quotient-aware estimate forcing `d_sep->0` from the near-extremal taxes would close the remaining scalar pair frontier.