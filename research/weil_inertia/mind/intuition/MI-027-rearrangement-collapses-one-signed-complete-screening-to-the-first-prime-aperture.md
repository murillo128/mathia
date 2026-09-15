# MI-027 — Rearrangement collapses one-signed complete screening to the first-prime aperture, where only a finite low-mode certificate remains

**Evidence level:** exact rearrangement/structural-rigidity theorem from [WI-298](../../findings/WI-298-rearrangement-collapses-complete-one-signed-screening-to-first-prime-aperture.md), with the analytic tail barrier removed through the exact aperture by [WI-299](../../findings/WI-299-smooth-kernel-tail-bound-reaches-the-first-prime-aperture.md)

For a nonnegative completely screened Weil null mode `v`, the powers of the first prime imply that its positivity set is a measurable selector modulo `log 2`, hence has measure at most `log 2`. Symmetric decreasing rearrangement therefore compresses `v` into the centered interval of radius

`r_2=(log 2)/2`.

WI-298 shows more than support compression. The gamma quadratic form decreases under symmetric decreasing rearrangement, while the pole term is rearrangement-invariant. Thus for the prime-deleted archimedean form

`q_arch(v^*) <= q_arch(v)=0`.

At radius `r_2` every prime-power translation term vanishes automatically: the first shift has exactly the support diameter and all larger shifts exceed it. Therefore

`Q_W^(r_2)(v^*) <= 0`,

so the supported spectral bottom satisfies `lambda_(r_2)<=0` whenever such a completely screened one-signed null mode exists. Applied to the **first** unrestricted Suzuki crossing, this forces its aperture to satisfy `a_*<=r_2`.

WI-299 removes a separate analytic-domain concern at exactly this boundary. For Suzuki's localized smooth Weil remainder `r`, the defect `delta(s)=-r''(s)-7/4` satisfies the uniform estimate

`0 <= delta(s) < 0.21621 |s|`  for `0<|s|<=log 2`,

which yields the residual bound `||R_a|| <= 0.353143 a^2` for every `0<a<=r_2`. The earlier smooth-kernel cutoff below the first-prime aperture is therefore not the obstruction to certifying `lambda_(r_2)>0`.

The branch is now concentrated at one finite aperture and one finite unresolved component. A rigorous strict positivity certificate `lambda_(r_2)>0` would exclude the entire one-signed complete-screening first-crossing scenario, and the smooth tail estimate is already valid through that endpoint. The remaining burden is an **independent finite low-mode/interval-Schur certificate** on the narrow terminal aperture region rather than another improvement of the smooth tail constant.

The reusable mechanism is that structural reduction and analytic tail control can remove all asymptotic degrees of freedom while still leaving a finite spectral sign problem. Once the tail estimate reaches the exact structural aperture, further tail sharpening is not progress unless it changes the finite low-mode certificate consumed by the positivity test.

**Boundary.** No strict positivity at `r_2` is proved. WI-299 does not certify the remaining low-mode block or import any nearby numerical/Eureka certificate as established. The argument is specific to nonnegative complete-screening modes; sign-changing and incomplete-screening branches remain separate.