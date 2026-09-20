# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source-mixture complexity to target geometry before tracing downstream gain

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-056-bounded-hilbert-marks-have-sharp-sqrt-k-sparse-mixture-tv-fidelity`, `MI-057-paired-sign-cubes-transfer-banach-type-to-source-relative-mixture-fidelity`, `MI-058-boundary-geometry-can-protect-anchored-fidelity-without-pairwise-fidelity`.

AF-451--AF-452 identify the exact fixed-source stability carrier as completable source-law secants. AF-453--AF-455 separate injectivity, atom separation and compact downstream processing from a positive inverse margin. AF-456 then gives the full-simplex category gate: bounded linear/barycentric TV fidelity on a countably infinite alphabet exists exactly when the target contains an isomorphic copy of `ell^1`; reflexive targets, including Hilbert spaces, cannot provide it. AF-457 makes the Hilbert sparse-mixture boundary sharp at `Theta(k^(-1/2))`.

AF-458--AF-459 transfer the obstruction to restricted sources through paired-cube completion. If `D_k(C)` is the least mean TV distance from an ideal paired `k`-cube to the normalized physical carrier, every bounded affine marking into a type-`p` Banach target obeys `kappa_C(F_phi) <= M[T_p(Y)k^(1/p-1)+D_k(C)]`. AF-460 shows bounded finite-rank linear source laws remain cube-complete, and AF-461 shows the same for regular finite-dimensional `C^1` equality laws: normalized local same-fiber secants recover the derivative-kernel sphere, so ordinary smooth finite codimension does not remove the obstruction.

AF-462 identifies the first exact boundary escape in this sequence. At a finite-support law `mu_0` in the positive simplex, normalized anchored directions may be negative only on `supp(mu_0)`. If that support has size `s`, the carrier satisfies `D_k >= (1-s/k)_+`; the canonical one-hot Hilbert embedding has exact anchored TV gain `1/sqrt(s)`. But every relative neighborhood still has zero pairwise local `ell^1`-to-`ell^2` lower gain because two sources can share the same depletion of the anchor and spread the added mass over large disjoint fresh supports.

The live arithmetic question is therefore no longer just whether positivity or boundary geometry is tangent-incomplete. Finite-support positivity can be. The next question is whether the physical arithmetic source naturally supplies a **distinguished anchored comparison with one-sided provenance**, or stronger structure that also blocks the fresh-support pairwise cancellation of AF-462. Singular fibers, hard support restrictions, genuinely infinite-dimensional laws and alternative source metrics remain candidates only after their actual completed-secant carrier is proved to have the required geometry.

## Keep identifiability, anchored provenance and pairwise stability separate

Exact injectivity, atom separation and anchored discrimination can each coexist with zero pairwise inverse margin. AF-457--AF-461 show that large paired-cube completion destroys complexity-independent Hilbert fidelity; AF-462 shows the converse warning: being far from those cubes can restore an anchored modulus without metrizing arbitrary nearby pairs.

A fidelity theorem must therefore state the source metric, admissible comparison class, whether the claim is anchored or pairwise, the completed secant/tangent carrier, target/operator category and the positive restricted lower gain actually consumed downstream. Infinite dimension, characteristic-kernel injectivity, orthogonality, finite conservation laws, regular nonlinear equalities, positivity, or finite support at one anchor do not by themselves imply the stronger pairwise statement.