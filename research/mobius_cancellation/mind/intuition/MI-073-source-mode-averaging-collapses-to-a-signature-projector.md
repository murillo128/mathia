# MI-073 — Formal averaging dimensions can collapse to an exact signed-discrepancy problem

**Evidence level:** exact synthesis from [MC-397](../../findings/MC-397-source-mode-averaging-collapses-to-signature-projector.md)--[MC-403](../../findings/MC-403-source-family-energy-is-signature-discrepancy.md), interpreted against the source-rank/codimension framework of MC-385--MC-396.

MC-397 shows that averaging squared source modes Fourier-collapses to a signature-subgroup projector. MC-398 shows that the Selberg divisor pair collapses through its lcm fibre coefficient. MC-399 shows that the surviving lcm character scalar disappears at the first additive correlation, MC-400 that the remaining moving-endpoint family is Möbius-invertible, and MC-401 that the complete endpoint is exactly a signed gcd/divisor energy.

MC-402 extends the audit to genuine truncation. The cutoff `1_([d,e]<=X)` has an exact divisor-incidence resolution with outer weight `M(floor(X/n))`; inside each incidence fibre the same signed gcd factorization survives. Hence the incomplete mask is not itself a new cheap arithmetic dimension. Exact resolution transfers the missing cancellation into the Mertens staircase rather than eliminating it.

MC-403 then identifies what is left when the **whole source family** is retained. If `B_omega(X)` is the signed lcm coefficient mass in source-signature class `omega`, the source-mode partial sums are its finite Fourier transform, and Parseval gives exactly

`sum_(I!=0) |A_I(X)|^2 = H sum_omega |B_omega(X)-B_bar(X)|^2`.

Collective source-family cancellation is therefore not a second averaging resource beyond the signatures. It is precisely signed equidistribution of one coefficient-mass vector. In particular, sparse signature support is not automatically favorable: unless the principal signed mass is already small, Cauchy--Schwarz forces energy into nontrivial source modes.

Combining this Fourier identity with the incidence inversion of MC-402 sharpens the obstruction further. Each signature mass becomes a Mertens-weighted sum of signature-incidence coefficients, so the nonprincipal family energy is exactly the squared norm of a **Mertens-weighted signed signature-discrepancy vector**. The surviving lcm question is no longer “can averaging the modes help?” but whether the actual Selberg/source arithmetic forces this vector to cancel without first assuming the Mertens estimate one is trying to reach.

The reusable test is staged: before crediting a formal index, cutoff or family average as new cancellation information, perform exact Fourier/regrouping reductions, the first correlation intended to exploit it, explicit inversion when available, endpoint factorization, incidence resolution of residual masks, and finally Parseval on any surviving source family. **A variable counts only if a source-specific relation survives these audits and makes the resulting exact discrepancy smaller.**

For the current frame, the remaining possibilities are correspondingly narrow: prove signed near-equidistribution of the actual lcm coefficient across source signatures, obtain a genuinely joint estimate for the Mertens-weighted discrepancy vector, or leave the lcm-factorable quadratic frame before the information is collapsed to `[d,e]`.

**Boundary.** MC-403 is an exact `L^2` identity and lower-bound obstruction, not an upper bound. It does not prove the signed signature discrepancy is large or small, and the lower bound can be weak when the principal mass cancels. MC-402--MC-403 do not prove a bound for `M`, an RH equivalence, or uselessness of structured truncated lcm sums. A source-specific discrepancy theorem would be genuine new information.