# MI-027 — Rearrangement collapses one-signed complete screening below a validated positive compact window

**Evidence level:** exact rearrangement/structural-rigidity theorem from [WI-298](../../findings/WI-298-rearrangement-collapses-complete-one-signed-screening-to-first-prime-aperture.md), with endpoint control from [WI-299](../../findings/WI-299-smooth-kernel-tail-bound-reaches-the-first-prime-aperture.md) and the independently replayed compact-window certificate [WI-300](../../findings/WI-300-l08-compact-window-certificate-would-kill-complete-one-signed-screening.md)

For a nonnegative completely screened Weil null mode `v`, the powers of the first prime imply that its positivity set is a measurable selector modulo `log 2`, hence has measure at most `log 2`. Symmetric decreasing rearrangement compresses `v` into the centered interval of radius

`r_2=(log 2)/2`.

WI-298 shows more than support compression. The gamma quadratic form decreases under symmetric decreasing rearrangement, while the pole term is rearrangement-invariant. Thus the prime-deleted archimedean form does not increase. At radius `r_2` every prime-power translation vanishes automatically, so a one-signed completely screened first-crossing null mode would force

`lambda_(r_2)<=0`

and hence `a_*<=r_2` for the first unrestricted Suzuki crossing.

WI-299 removes the analytic-domain concern at exactly this endpoint by controlling the smooth-kernel remainder throughout `a<=r_2`.

The external verification gate exposed by the earlier version of WI-300 is now discharged. Mathia issue #152 independently reconstructed and interval-certified Zhu's pinned v2 compact-window pipeline, giving

`Q_W(f) >= 8.9e-18 ||f||_2^2`

for every complex `f` supported in `[-0.8,0.8]`, with the normalization dictionary to Suzuki checked to have scalar factor one. Therefore

`lambda_0.8 >= 8.9e-18 > 0`.

Monotonicity gives `a_*>0.8`, while complete one-signed first-crossing screening gives `a_*<=r_2≈0.3466`. The branch is therefore excluded, subject only to the ordinary computer-assisted-evidence boundary of the independently replayed finite certificate.

The reusable mechanism is **structural compression plus an independently validated finite positivity window**. One need not prove positivity at the smallest source-forced aperture if the branch theorem compresses every counterexample below `r` and any rigorously validated positive window exists at a larger aperture. Structural reduction and numerical/interval verification remain separate evidence objects, but once both are established they combine through monotonicity without an asymptotic step.

WI-301 strengthens the lesson further: first-crossing minimality is not essential for the screened class. Dyadic screening and one-sign positivity already force a uniform archimedean reserve after rearrangement. That stronger aperture-independent statement is recorded separately in MI-028.

**Boundary.** The exclusion is specific to the one-signed completely screened branch. It does not settle sign-changing modes, incomplete screening, unrestricted large-aperture Weil positivity, spectral simplicity or RH. The `8.9e-18` lower bound is computer-assisted interval evidence rather than a Lean theorem.