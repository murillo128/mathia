# MI-027 — Rearrangement collapses one-signed complete screening to the first-prime aperture

**Evidence level:** exact rearrangement/structural-rigidity theorem from [WI-298](../../findings/WI-298-rearrangement-collapses-complete-one-signed-screening-to-first-prime-aperture.md), using the complete-screening packing law of WI-281 and the prime-deleted form of WI-284

For a nonnegative completely screened Weil null mode `v`, the powers of the first prime imply that its positivity set is a measurable selector modulo `log 2`, hence has measure at most `log 2`. Symmetric decreasing rearrangement therefore compresses `v` into the centered interval of radius

`r_2=(log 2)/2`.

WI-298 shows more than support compression. The gamma quadratic form decreases under symmetric decreasing rearrangement, while the pole term is rearrangement-invariant. Thus for the prime-deleted archimedean form

`q_arch(v^*) <= q_arch(v)=0`.

At radius `r_2` every prime-power translation term vanishes automatically: the first shift has exactly the support diameter and all larger shifts exceed it. Therefore

`Q_W^(r_2)(v^*) <= 0`,

so the supported spectral bottom satisfies `lambda_(r_2)<=0` whenever such a completely screened one-signed null mode exists.

Applied to the **first** unrestricted Suzuki crossing, this forces its aperture to satisfy `a_*<=r_2`. Hence the remote-satellite/local-to-global escape left by the pole-MGF analysis is unnecessary for the one-signed complete-screening branch above the first-prime threshold: rearrangement already pushes any such mode down to a nonpositive prime-free test at `r_2`, contradicting firstness.

The branch is now concentrated at one finite aperture. A rigorous strict positivity certificate `lambda_(r_2)>0` would exclude the entire one-signed complete-screening first-crossing scenario; below `r_2` complete screening is vacuous because no prime-power shift has positive-measure overlap.

The reusable mechanism is that **one-signed screening plus rearrangement converts a global support-geometry problem into a single extremal aperture test** when the prime-deleted form is monotone under rearrangement. This is stronger than tail/core control because it removes the distant-support degree of freedom altogether.

**Boundary.** No strict positivity at `r_2` is assumed or proved here. Existing public finite-scale candidates remain subject to their certification boundary. The argument applies to nonnegative complete-screening modes; sign-changing and incomplete-screening branches remain separate.