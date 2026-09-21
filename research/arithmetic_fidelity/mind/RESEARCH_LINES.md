# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source-mixture complexity to target geometry before tracing downstream gain

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-056-bounded-hilbert-marks-have-sharp-sqrt-k-sparse-mixture-tv-fidelity`, `MI-057-paired-sign-cubes-transfer-banach-type-to-source-relative-mixture-fidelity`, `MI-058-boundary-geometry-can-protect-anchored-fidelity-without-pairwise-fidelity`, `MI-059-source-point-cubes-block-stable-nonlinear-hilbert-recovery-unless-the-source-geometry-changes`.

AF-451--AF-457 identify the completed source-law secant carrier and the target-category obstruction: full-simplex TV fidelity under bounded linear/barycentric observation requires an `ell^1` copy in the target, while Hilbert sparse-mixture gain falls at the sharp `Theta(k^(-1/2))` scale. AF-458--AF-461 transfer that obstruction to restricted sources through paired-cube completion and show that bounded finite-rank laws and regular finite-dimensional `C^1` equality fibers remain cube-complete.

AF-462 identifies a real but one-sided boundary escape. At a finite-support simplex law `mu_0`, anchored directions may be negative only on `supp(mu_0)`, giving `D_k >= (1-s/k)_+` for `s=|supp(mu_0)|`; the canonical one-hot Hilbert embedding has exact anchored TV gain `1/sqrt(s)`.

AF-463 classifies why that escape cannot be promoted to arbitrary nearby pairs inside a convex source class under bounded linear observation. For convex `C`, the moving-secant paratingent cone at every base point is `closure(span(C-C))`, so pairwise local linear fidelity is exactly the minimum modulus on the affine direction space.

AF-464 now closes a broader operator-category escape when the source itself contains large metric cubes. The paired-mixture vertices form a scaled Hamming cube in TV, so every nonlinear encoder with finite upper TV-Lipschitz modulus into an Enflo-type `p` target obeys `kappa <= T_p^E L k^(1/p-1)`; in Hilbert space, `kappa <= L/sqrt(k)`. Nonlinearity therefore does not restore complexity-independent pairwise conditioning on unrestricted sparse mixtures, or on any restricted source that actually contains the same source-point cubes.

The live arithmetic question is consequently source-relative and metric-relative. If the downstream theorem needs pairwise stable recovery, one must prove that the physical source excludes growing `ell^1` metric cubes or distorts their metric, move to a target/operator category outside the metric-type obstruction, justify complexity-growing upper sensitivity, or use a genuinely narrower comparison task. If the theorem is anchored, the one-sided provenance of AF-462 can still matter.

## Keep identifiability, anchored provenance and pairwise stability separate

Exact injectivity, atom separation and anchored discrimination can each coexist with zero pairwise inverse margin. AF-462 shows that a convex boundary can stay macroscopically far from large paired cubes for anchored directions; AF-463 shows that moving two comparison points symmetrizes the same convex boundary back to its full affine direction space; AF-464 shows that even an arbitrary nonlinear Lipschitz destination is constrained once the source contains actual Hamming cubes.

A fidelity theorem must therefore state the source metric, admissible comparison class, whether the claim is anchored or pairwise, the relevant secant/paratingent or source-point metric carrier, target/operator category, upper sensitivity budget and positive lower gain actually consumed downstream. Cube-poorness of an anchored cone is not pairwise stability, while pairwise failure for convex or cube-rich models does not negate a genuinely anchored or singular-source theorem.