# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Bridge exact permanent-source rigidity to stable partial observation and destination coupling

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-024-complete-farey-field-inversion-is-uniformly-conditioned-on-the-square-root-prefix`.

FD-145--FD-163 reduce finite-`L^q` binary ancestry recovery to anchored cut exposure and show that bounded-resource anchor geometry cannot make the exposed squarefree mass disappear merely by sparse holes, terminal-core migration or one omitted small prime. Under the stated expansion/distortion/leakage hypotheses a positive-density source surface remains visible.

FD-164 then separates visibility from orientation. At one horizon the complete Farey discrepancy field is exactly equivalent to the floor-quotient Mertens staircase, yet finitely many macroscopic quotient-shell sign flips can preserve that entire field while changing a dense fraction of squarefree orientations. FD-165 extends the finite-cutoff ambiguity to arbitrary horizon bundles of size `J_T` whenever `J_T M_beta(T)=o(T)`; Davenport's log-power cancellation therefore leaves every polylogarithmic bundle inside the dense-kernel regime.

FD-166 closes the exact **permanent-source** version. Every quotient set `Q_H` contains the consecutive prefix `1,...,floor(sqrt(H))`. A complete exact field at horizon `H` fixes the cumulative source, and hence every coefficient, on that prefix. If one fixed source matches complete fields on any unbounded horizon set, however sparse or non-nested, those prefixes exhaust the source and force `a=mu` identically. A first source defect at `n_0` is exposed by every `H>=n_0^2`.

FD-167 closes the corresponding **complete-field conditioning** question in unnormalized `L^2`. If `E_H` is the difference between a real source-controlled field and the physical Farey field, the `FD-117` divisor inversion and Parseval give the uniform modulus

\[
\max_{1\le r\le\lfloor\sqrt H\rfloor}|A(r)-M(r)|
\le \sqrt{30}\,\|E_H\|_2.
\]

There is no loss with `H` or with the recovered prefix coordinate. For integer-valued sources, `||E_H||_2<1/sqrt(30)` snaps the entire square-root prefix to Möbius exactly; a fixed first defect at `n_0` therefore remains at least `1/sqrt(30)` away in complete-field `L^2` for every `H>=n_0^2`. The finite-cutoff kernels are noncompact rather than poorly conditioned: their freedom must drift outward, not hide in a vanishing full-field perturbation.

The live bridge has therefore narrowed to **partial observation and destination coupling**. Determine how much of the full Farey field or Fourier spectrum can be discarded while retaining stable recovery of a growing source prefix, and quantify the conditioning loss for sampled, sparse or coarsened observations. Complete-field `L^2` conditioning itself is no longer the bottleneck. A separate source-native route may exploit multiplicative or Farey-order coherence without reconstructing the full Möbius staircase.

## Apply the information-budget gate only after the observation-family kernel is understood

FD-144 remains a later lower bound: even after geometric exposure and orientation are solved, `o(r_T)` arbitrary source-independent normalized ancestry tests can be fooled along a subsequence. FD-164--FD-167 sharpen the order of obligations. First quotient the kernel of the declared observation family and determine its stable inverse on the coordinates it exposes; only then count how much source information the surviving architecture actually carries.

## Keep coefficient coercivity and destination coercivity separate

Exact or uniformly subcritical complete-field errors on an unbounded hierarchy identify an integer-valued permanent source, but source identification does not by itself prove the RH-critical discrepancy estimate. A useful continuation must either retain stable coefficient coercivity under substantially incomplete observation or connect source-native structure directly to the nonlocal Franel--Landau norm. These remain distinct mathematical gates.