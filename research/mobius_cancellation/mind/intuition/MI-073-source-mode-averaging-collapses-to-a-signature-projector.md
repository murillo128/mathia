# MI-073 — Formal averaging dimensions can collapse under regrouping, correlation, inversion and incidence factorization

**Evidence level:** exact synthesis from [MC-397](../../findings/MC-397-source-mode-averaging-collapses-to-signature-projector.md)--[MC-402](../../findings/MC-402-truncated-lcm-mask-is-mertens-weighted-divisor-energy.md), interpreted against the source-rank/codimension framework of MC-385--MC-396.

MC-397 shows that averaging squared source modes Fourier-collapses to a signature-subgroup projector. MC-398 shows that the Selberg divisor pair collapses through its lcm fibre coefficient. MC-399 shows that the surviving lcm character scalar disappears at the first additive correlation, MC-400 that the remaining moving-endpoint family is Möbius-invertible, and MC-401 that the complete endpoint is exactly a signed gcd/divisor energy.

MC-402 extends the audit to genuine truncation. The cutoff `1_([d,e]<=X)` has an exact divisor-incidence resolution with outer weight `M(floor(X/n))`; inside each incidence fibre the same signed gcd factorization survives. Hence the incomplete mask is not itself a new cheap arithmetic dimension. Exact resolution transfers the missing cancellation into the Mertens staircase rather than eliminating it.

The reusable test is staged: before crediting a formal index or cutoff as new cancellation information, perform exact Fourier/regrouping reductions, the first correlation intended to exploit it, explicit inversion when available, natural endpoint factorization, and finally an incidence resolution of any residual mask. **A variable counts only if it survives these audits with a source-specific relation that cannot be reconstructed or paid for by an equally hard arithmetic weight.**

For the current frame, the surviving possibilities are structure of the actual Selberg/source-signature coefficients inside the incidence energies, collective cancellation across the weighted family, source-family cancellation unavailable mode by mode, or a pre-quadratic variable that remains genuinely joint before lcm collapse.

**Boundary.** MC-402 does not prove a bound for `M`, an RH equivalence, or uselessness of truncated lcm sums. A structured collective estimate could beat the generic incidence expansion. The obstruction is specifically to treating the cutoff mask, by itself, as a free retained resource.