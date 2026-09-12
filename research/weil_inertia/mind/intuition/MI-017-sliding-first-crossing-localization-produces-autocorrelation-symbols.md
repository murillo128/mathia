# MI-017 — The phase-coupled source cone first needs exact recertification of both the first-prime operator and its positivity judge

**Evidence level:** the phase-cone identities of WI-253--WI-259 are exact. WI-260--WI-262 prove that the audited public FP-0.35 paths do not certify the required exact `lambda_(7/20)>0` premise as written. No negativity of the true operator and no incompatibility with a compactly supported global first zero mode is proved.

At a hypothetical first unrestricted localized Weil crossing, WI-253--WI-258 reduce the useful source information to phase-coupled inequalities `S_v(r)+J_v(r,t)>=0`. WI-259 identifies the activation prerequisite: if strict positivity at `r=7/20` is certified, monotonicity pushes every hypothetical first crossing beyond `(log 2)/2`, while `log 2<7/10<log 3` makes the fixed phase cone contain exactly the single Mangoldt atom `n=2`.

WI-260 shows that the post-fix FP-0.35 reproduction script is not an exact positivity certificate: load-bearing constants and matrix entries are not rigorously enclosed and its inverse-residual argument does not establish the required induced norm. WI-261 then shows that the nominal proofctl exact-prime path judges the wrong object: exact-prime metadata is not used in assembly, a rational midpoint in `tau` can produce an interval excluding the true prime entry, and the judge substitutes `c_L=0` for the required nonzero Weil constant.

WI-262 now separates **judge correctness** from object identity. `_min_pivot_mpmath` applies the LDL rank-one update twice to every off-diagonal trailing entry. On the exact rational matrix

`[[1,1/2,1/2],[1/2,1/2,3/5],[1/2,3/5,1/2]]`

the true determinant is `-3/50` and the correct last pivot is `-6/25`, yet the routine returns the positive pivot `21/100`. This is an algebraic false positive, independent of precision or interval width. The implementation also lacks a demonstrated directed-rounding discipline, so fixing only the double update would not by itself establish a rigorous interval certificate.

The first-prime activation gate therefore has two independent certification obligations. A valid path must first enclose the **same exact theorem matrix**—exact `log 2`, `sqrt 2`, `tau=20 log 2/7`, harmonic values, prime layer and correct nonzero `c_L`—and then pass that enclosure through a mathematically valid positivity algorithm with correct Schur algebra and outward rounding. Regression on exact rational indefinite examples should precede trust in the FP-0.35 margin.

The reusable lesson is now four gates: **source activation, exact-object identity, certificate-judge validity, and source-sign obstruction are distinct**. Exact data can be judged by a false positivity routine, and a perfect positivity routine can certify the wrong surrogate. Neither permits the one-prime phase theorem to start.

**Boundary.** WI-260--WI-262 do not show `lambda_(7/20)<=0`; the nominal positive margin may survive a clean independent certificate. They do not alter WI-259's conditional implication or prove a negative phase defect. Until both matrix identity and judge correctness are certified, the single-prime cone remains conditional input.