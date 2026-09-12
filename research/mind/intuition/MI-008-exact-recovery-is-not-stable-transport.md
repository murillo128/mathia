# MI-008 — Exact recovery, source normalization, representation distortion, and target-conditioned robustness are different resources

**Evidence level:** supported by AF-282--AF-293 and PF-303--PF-307; no universal target modulus or full mixed-response theorem is claimed.

Arithmetic Fidelity separates acquisition from the final analytic target. AF-282--AF-289 classify mixed finite-prefix recovery, frame conditioning, and timing perturbations after removing the common-clock gauge. AF-290 then identifies a different resource: the exact coefficient perturbation radius preserving a finite zero count is distance to the boundary-zero discriminant.

AF-291 shows that this target radius can shrink with breadth even while eta truncations converge correctly on the boundary. AF-292 rules out diagonal Hilbert repair. AF-293 extends the classification to arbitrary dense Hilbert metrics under a condition-number budget: with `kappa(G)<=K`, the best normalized margin is comparable to

`min(1, sqrt(K)/(sqrt(N) H_N(alpha)))`.

An order-one repair therefore requires representation condition number at the reciprocal scale of the raw target margin. Dense mixing can move the instability, but it does not erase the bill unless the anisotropy has an independent mathematical justification.

Prime Flute supplies the complementary normalization-and-conversion picture. PF-303--PF-305 make the scalar Green reservoir a norm-one positive contraction after killing normalization. PF-306 then locates the first post-scalar instability exactly at the normalized constant-to-nonconstant Schur angle `K_N`; its squared norm is the maximal constant-energy fraction screened by nonconstant relaxation.

PF-307 shows that even this normalized conversion cannot be controlled by a global gap. On canonical seam-cut tail blocks there are finite sections with

`1-||C_(M,L(M))||^2 -> 0`.

Thus the full Schur resolvent is necessarily ill-conditioned in operator norm along the tail. The live quantity is not another global norm but **source-accessed conditioning**: whether the physical forcing/reassembly maps overlap the nearly screened directions, with what multiplicity, and in which ideal norm.

The cross-line lesson is concrete: **remove exact nuisance symmetries, normalize by the source's coercive currency, then price every representation and conversion map only on the directions the destination actually consumes**. A repair may relocate instability from target margin to representation distortion, or from scalar return to a nearly singular conversion angle. Once the global norm is forced to be bad, source-restricted geometry becomes part of the theorem rather than an optimization detail.

**Boundary.** AF-293 concerns finite eta zero-count geometry under linear Hilbert metrics; PF-307 concerns the canonical finite seam-cut block response. Their operators do not transfer. The synthesis is the accounting principle that no favorable intermediate normalization counts as transport until the reached directions at the next interface are controlled.