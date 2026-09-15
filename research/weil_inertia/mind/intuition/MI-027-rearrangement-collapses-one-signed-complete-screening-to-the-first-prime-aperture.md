# MI-027 — Rearrangement collapses one-signed complete screening below any validated positive compact window

**Evidence level:** exact rearrangement/structural-rigidity theorem from [WI-298](../../findings/WI-298-rearrangement-collapses-complete-one-signed-screening-to-first-prime-aperture.md), with the first-prime analytic tail controlled by [WI-299](../../findings/WI-299-smooth-kernel-tail-bound-reaches-the-first-prime-aperture.md) and a conditional prior-art redirect through [WI-300](../../findings/WI-300-l08-compact-window-certificate-would-kill-complete-one-signed-screening.md)

For a nonnegative completely screened Weil null mode `v`, the powers of the first prime imply that its positivity set is a measurable selector modulo `log 2`, hence has measure at most `log 2`. Symmetric decreasing rearrangement therefore compresses `v` into the centered interval of radius

`r_2=(log 2)/2`.

WI-298 shows more than support compression. The gamma quadratic form decreases under symmetric decreasing rearrangement, while the pole term is rearrangement-invariant. Thus for the prime-deleted archimedean form

`q_arch(v^*) <= q_arch(v)=0`.

At radius `r_2` every prime-power translation term vanishes automatically: the first shift has exactly the support diameter and all larger shifts exceed it. Therefore

`Q_W^(r_2)(v^*) <= 0`,

so the supported spectral bottom satisfies `lambda_(r_2)<=0` whenever such a completely screened one-signed null mode exists. Applied to the **first** unrestricted Suzuki crossing, this forces its aperture to satisfy `a_*<=r_2`.

WI-299 removes a separate analytic-domain concern at exactly this boundary. For Suzuki's localized smooth Weil remainder `r`, the defect `delta(s)=-r''(s)-7/4` satisfies the uniform estimate

`0 <= delta(s) < 0.21621 |s|`  for `0<|s|<=log 2`,

which yields the residual bound `||R_a|| <= 0.353143 a^2` for every `0<a<=r_2`. Thus the smooth-kernel cutoff is not the obstruction to certifying strict positivity at the structural endpoint.

WI-300 exposes a stronger finite-threshold route using recent prior art. Zhu's v2 compact-window theorem reports

`Q(f) >= 8.9e-18 ||f||_2^2`

for arbitrary complex `f` supported in `[-0.8,0.8]`. WI-300 audits the theorem surface and shows that, **if this computer-assisted certificate is independently replayed and validated**, it is exactly a positive lower bound for Suzuki's localized form: `lambda_0.8>0`. Monotonicity would then force the first crossing to satisfy `a_*>0.8`, contradicting the rearrangement consequence `a_*<=r_2≈0.3466` for complete one-signed screening.

The reusable mechanism is therefore broader than “prove positivity at the smallest structural aperture.” Once a source-side theorem compresses an entire failure branch below a finite aperture `r`, **any independently validated positive compact window at a larger aperture kills that branch by monotonicity**. The structural reduction and the positivity certificate can be developed independently; they meet only through the ordering of localized ground-state energies.

For the current line, the shortest evidence-changing test is the independent replay of the reported `L=0.8` certificate, not further optimization of the `r_2` low-mode calculation. A failed replay would not invalidate WI-298--WI-299; it would simply restore `lambda_(r_2)>0` as the direct fallback certificate.

**Boundary.** WI-300 does not itself establish `lambda_0.8>0` as independently verified Mathia evidence; its unconditional content is the exact implication from a valid published certificate to exclusion of the screened branch. Even successful validation would be specific to one-signed complete screening. It would not settle sign-changing modes, incomplete screening, unrestricted positivity beyond `0.8`, spectral simplicity, or RH.
