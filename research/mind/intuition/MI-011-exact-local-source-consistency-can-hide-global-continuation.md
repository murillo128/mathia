# MI-011 — Exact local source consistency can hide a globally expensive or target-invisible continuation

**Evidence level:** supported by the stable-tail/finite-Schur theorems NB-066--NB-067 and the first-layer conservation/timing theorems RE-068--RE-069; no operator or contradiction is transferred between the lines.

Nyman--Beurling and Robin Extremal give two different examples of the same information boundary: **perfect local source consistency does not imply that the residual global variable is controlled or visible in the destination coordinates**.

In Nyman--Beurling, NB-066 characterizes a hypothetical stable-tail vector as globally orthogonal to the natural space while its trace is exactly natural on every finite Paley--Wiener window. The least compatible future norm nevertheless diverges. NB-067 adds that this infinite continuation cost is not inaccessible: if `A_R` is the visible prefix Gram and `S_(R,N)` the finite future Schur complement, then

\[
\lambda_{\max}(A_R^{-1/2}S_{R,N}A_R^{-1/2})
\downarrow1+\Lambda_R^2.
\]

So a bounded finite generalized-eigenvalue subsequence already excludes every stable tail. Exact local representability can coexist with catastrophic global continuation, but the relevant continuation norm has rigorous finite source-only upper certificates.

In Robin Extremal, RE-068 gives exact prime-multiset consistency for matched first-layer packets: every additive endpoint prime statistic agrees. RE-069 then follows the residual positional variable. The delayed event coordinates carry macroscopic raw transport, yet the exact Robin kernel converts each prime delay into

\[
\frac1p-\log(1+1/p)=O(p^{-2}),
\]

so all future first-layer timing contributes only `O(1/X)` after scale `X`. Here the residual variable exists and can be large, but the requested linear readout is asymptotically blind to it.

The cross-line relation is not that these mechanisms are the same. NB is a Hilbert-space extension-cost problem; RE is a source-set identity followed by kernel compression. The reusable separation has four stages:

1. exact local/source consistency;
2. identification of what remains undetermined by that consistency;
3. global cost or stability of the residual variable;
4. sensitivity of the final target/readout to that variable.

NB-067 attacks stage 3 with finite certificates. RE-069 shows stage 4 can fail even when stage 2 carries macroscopic information. Improving the already-matched local statistic attacks the wrong resource in both cases.

**Boundary.** No Nyman extension estimate transfers to Robin packets, and no Robin timing kernel transfers to Nyman traces. The common statement is only the staged information separation above. Neither line by itself proves or disproves RH.
