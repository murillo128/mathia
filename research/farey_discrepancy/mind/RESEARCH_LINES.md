# Farey-discrepancy research lines

This file records the current mathematical questions that survive the Farey-discrepancy evidence. It is not a roadmap, task queue, status page, or history.

## Force one-sided repair variation past the positive-capacity boundary

FD-255--FD-264 separate the signed exact-omission threshold from the physical nonnegative-source boundary. The positive switched-response cone has a genuine capacity loss, while canonical full-grid inversion supplies only `O(D log D)` repair mass after explicit forcing terms are removed. Dense deep blocks or a negative signed mean therefore do not by themselves produce the one-sided amplification required by the physical destination.

The live deterministic source question remains a theorem on **one-sided or `l^1` within-band repair variation** under the exact replication kernel, or a genuinely different switched-only repair whose intermediate motion changes the source demand. Any such theorem must be proved for the physical nonnegative geometry rather than inferred from signed telescoping.

## Prove near-linear remainder-good zero-gap occupation at a fixed inverse-polylog scale

FD-282--FD-287 show that the grouped strict-right Perron collar retains a prime witness unless an order-`L` near-one `zeta'/zeta` phase event occurs. FD-288--FD-289 make those events sparse uniformly in translated polynomial windows, and FD-290 shows phase-good and zero-safe cluster-complete heights coexist. FD-291 then uses the exact constancy of the complete hard complementary remainder on each zero gap: a remainder-good gap can be trimmed internally by reciprocal-log collars and stays remainder-good throughout its safe core.

FD-292 removes any distinguished inverse-polylog exponent from the phase side. Applying the same Montgomery--Vaughan mean-square theorem to fixed powers of the strict-right logarithmic derivative gives, for every prescribed fixed `P>0`, phase-bad measure `O_P(H/L^P)` on polynomial windows. It is therefore enough, in principle, to prove reciprocal-log-safe occupation `Omega_B(J)>=delta_P H/L^P` for the **complete physical hard remainder** at one convenient fixed `P`.

FD-293 shows that this apparently weak measure target has a strong population cost under RH. The classical RH zero-gap cap

`gamma_(j+1)-gamma_j <= (pi+o(1))/log log H`

implies that any such occupation certificate forces at least

`K_B(J) >= (delta_P/pi-o(1)) H log log H/L^P = H^(1-o(1))`

remainder-good gaps in the relevant polynomial window. Finitely many good gaps, a sparse exceptional sequence, or `O(H^alpha)` good gaps for fixed `alpha<1` cannot close the FD-292 route. The count is only necessary, not sufficient: the safe cores must still contribute enough total length.

FD-293 also closes the tempting gap-by-gap reuse of the current phase selector. The FD-292 Montgomery--Vaughan estimate on an interval of length `R` requires `R/L^(2m(m+2))->infinity` for fixed moment order `m`, whereas every individual RH zero gap has `R<<1/log log H`. The present phase theorem is therefore intrinsically aggregate at zero-gap scale. This is a limitation of that implementation, not a theorem that finer local phase control is impossible.

The live gate is now a genuinely aggregate theorem: prove that the complete divisor-replicated physical remainder is good on a near-linear population of zero gaps with enough reciprocal-log-safe occupation, prove the occupation measure directly without enumerating gaps, or replace the current phase/remainder intersection architecture by a mechanism that couples them at zero-gap scale. A theorem producing only isolated favorable cutoffs cannot suffice within the present route.

This sharpening is one-sided and conditional where stated. FD-293 does not prove that even one remainder-good gap exists, its population floor uses RH, and many good gaps need not give enough occupation. FD-292 still gives no uniformity in a growing `P`. Any attempt to replace the physical grouped remainder by a generic Möbius/Mellin estimate must re-prove that it controls the exact gapwise destination quantity; if it loses the Farey divisor-replication geometry, the natural ownership moves to `mobius_cancellation`.