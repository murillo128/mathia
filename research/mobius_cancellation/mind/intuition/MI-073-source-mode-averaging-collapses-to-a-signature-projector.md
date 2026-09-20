# MI-073 — Formal averaging, incidence algebra and quotient fibers collapse unless independently controlled signed structure survives

**Evidence level:** exact synthesis from MC-397--[MC-408](../../findings/MC-408-signed-pnt-error-correlation-is-rh-equivalent.md), interpreted against the source-rank/codimension framework of MC-385--MC-396.

MC-397 shows that averaging squared source modes Fourier-collapses to a signature-subgroup projector. MC-398 shows that the Selberg divisor pair collapses through its lcm fibre coefficient, MC-399 removes the surviving lcm character scalar at first additive correlation, and MC-400--MC-402 consume moving endpoints, the complete endpoint and generic truncation through exact inversion/factorization.

MC-403 identifies what remains when the whole source family is retained. If `B_omega(X)` is the signed lcm coefficient mass in source-signature class `omega`, Parseval gives

`sum_(I!=0) |A_I(X)|^2 = H sum_omega |B_omega(X)-B_bar(X)|^2`.

After truncation inversion, the nonprincipal family energy is exactly the squared norm of a Mertens-weighted signed signature-discrepancy vector. Collective source averaging is therefore not a second cancellation resource beyond that vector. MC-404 strengthens the audit algebraically: every finite Boolean, polynomial or higher-degree observable built only from divisor incidences lies in the finite lcm join-semilattice algebra.

MC-405 supplies a matched control outside the lcm fibres. The exact Möbius--Mangoldt quotient family retains a prime-power label, but its aggregate is a first-order transform of `M`. MC-406 identifies the finest downstream statistic as the floor-quotient mass `W_k`; the PNT main component of that family is exactly classical harmonic Möbius cancellation, so the reduction to only `O(sqrt(x))` quotient coordinates creates no automatic saving.

MC-407 then removes the apparent independence of the prime-error increment representation. Discrete Abel summation turns the `M(k)`/increment pairing into the scalar Möbius--PNT-error correlation

`C(x)=sum_(a<=x) mu(a)(psi(x/a)-x/a)`

plus the endpoint term. This is an exact coordinate change, not a new source of cancellation.

MC-408 closes the scalar escape at the target exponent. The Mellin transform of `C` is

`-zeta'(s)/(s zeta(s)^2)-1/((s-1)zeta(s))`.

A zeta zero of multiplicity `m` creates a pole of order `m+1` in the first term, while the second has order only `m`; the highest-order singularity cannot cancel. Consequently `C(x)=O_epsilon(x^(1/2+epsilon))` for every positive `epsilon` is equivalent to RH. At finite level the map is also information-complete: `C_N-C_(N-1)=-m_(N-1)-(1+log N)mu(N)`, so the sequence `C_1,...,C_N` recursively determines `mu(1),...,mu(N)`.

The reusable audit now has four gates. First ask whether a proposed index/tuple/family survives exact Fourier, lcm, inversion and incidence reductions. Second compute whether the retained family self-couples back to the original quantity after aggregation. Third identify the finest statistic still distinguished by the downstream observable. Fourth ask whether the resulting scalar coordinate is analytically cheaper rather than merely invertible or target-equivalent. A coordinate can survive all earlier reductions and still buy no leverage because its endpoint estimate is exactly the original RH-scale problem in another norm or transform.

For the current frame, the useful exits are therefore pre-scalarization ones: exploit source-specific coefficient laws that generic lcm incidence does not possess, or retain phase/congruence/translation/bilinear structure inside quotient fibers and prove a theorem before the final exact aggregation. Attacking `C(x)` directly remains a legitimate RH strategy, but it is not evidence that quotient/error enrichment produced an easier intermediate observable.

**Boundary.** MC-403 is an exact `L^2` identity and lower-bound obstruction, not an upper bound. MC-404 is an algebraic collapse theorem for finite incidence-only observables. MC-405--MC-407 give exact representations without an improved Mertens estimate. MC-408 classifies the scalar signed correlation only at the square-root `O_epsilon(x^(1/2+epsilon))` scale; finite invertibility is not a stable norm equivalence. None of these results proves RH.