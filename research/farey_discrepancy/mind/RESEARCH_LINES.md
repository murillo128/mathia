# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Bridge exact permanent-source rigidity to restricted partial observation and destination coupling

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-025-mobius-inverse-row-support-is-the-coordinate-minimal-stable-prefix-sampler`.

FD-145--FD-163 reduce finite-`L^q` binary ancestry recovery to anchored cut exposure and show that bounded-resource anchor geometry cannot make the exposed squarefree mass disappear merely by sparse holes, terminal-core migration or one omitted small prime. Under the stated expansion/distortion/leakage hypotheses a positive-density source surface remains visible.

FD-164 then separates visibility from orientation. At one horizon the complete Farey discrepancy field is exactly equivalent to the floor-quotient Mertens staircase, yet finitely many macroscopic quotient-shell sign flips can preserve that entire field while changing a dense fraction of squarefree orientations. FD-165 extends the finite-cutoff ambiguity to arbitrary horizon bundles of size `J_T` whenever `J_T M_beta(T)=o(T)`.

FD-166 closes the exact **permanent-source** version. Every quotient set `Q_H` contains the consecutive prefix `1,...,floor(sqrt(H))`. If one fixed source matches complete fields on any unbounded horizon set, those prefixes exhaust the source and force `a=mu` identically. A first source defect at `n_0` is exposed by every `H>=n_0^2`.

FD-167 gives the corresponding **complete-field conditioning** theorem in unnormalized `L^2`:

`max_(r<=floor(sqrt H)) |A(r)-M(r)| <= sqrt(30) ||E_H||_2`.

The modulus is independent of `H` and the recovered coordinate. For integer-valued sources, error below `1/sqrt(30)` snaps the entire square-root prefix exactly.

FD-168 solves the raw Fourier-coordinate partial-observation problem. For a target prefix `r<=R`, the union `S_(H,R)` of nonzero Möbius inverse-row supports is exactly the coordinate-minimal raw sampler over the full formal source space and retains the same localized `sqrt(30)` inverse modulus. Since `R<=|S_(H,R)|<=R H^(o(1))`, every fixed-power sub-square-root prefix can be recovered from a vanishing fraction of the positive Fourier skeleton.

FD-169 now closes the unrestricted mixed-linear branch. If an arbitrary linear acquisition `L` and arbitrary decoder may be designed specifically for the target prefix, exact recovery is possible iff `ker L` lies inside the kernel of the rank-`R` target map. The target then factors linearly through `L`, so `m>=R`, with equality attained by taking the measurement operator to be the target itself. Arbitrary mixing therefore does not reveal a deeper compression law; it relocates the Möbius inverse into the sensor and collapses measurement count to target rank.

The live observation problem is consequently **restricted acquisition**: spatial/coarsened Farey observations, geometrically local or bounded-weight mixtures, horizon-uniform/source-oblivious measurement rules, explicit noise geometry, or compression that exploits a genuinely arithmetic source class smaller than the formal real space. Near the full square-root prefix, the raw-coordinate support asymptotics also remain open. Separately, coefficient recovery still needs a destination coupling to the nonlocal Franel--Landau norm.

## Apply the information-budget gate only after the observation-family kernel and normalization are fixed

FD-144 remains a later lower bound: even after geometric exposure and orientation are solved, `o(r_T)` arbitrary source-independent normalized ancestry tests can be fooled along a subsequence. FD-168--FD-169 sharpen the order of obligations. First declare the observation family, identify its kernel relative to the target and fix the norm/noise normalization; only then count measurements or price inverse stability.

For raw Fourier selectors, FD-168 gives a nontrivial coordinate-minimal support because the basis is fixed. For unrestricted linear acquisition, FD-169 shows that the target row space itself is the minimal measurement space, so count alone is tautological. A new scarcity theorem must therefore constrain what the acquisition operator is allowed to know or mix rather than merely reduce its output dimension.

## Keep coefficient coercivity and destination coercivity separate

Exact or uniformly subcritical complete-field errors on an unbounded hierarchy identify an integer-valued permanent source, and FD-168 preserves coefficient coercivity under a sharply reduced raw Fourier skeleton for sub-square-root prefixes. FD-169 does not strengthen that destination bridge; it only classifies unrestricted exact acquisition in the formal source model. None of these statements proves the RH-critical discrepancy estimate. A useful continuation must control a genuinely restricted observation family or connect source-native structure directly to the nonlocal Franel--Landau norm.