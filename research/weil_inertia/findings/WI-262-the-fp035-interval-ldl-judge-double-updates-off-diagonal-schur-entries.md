# WI-262 — the FP-0.35 interval LDL judge double-updates off-diagonal Schur entries

**Status:** `EXACT-CODE-AUDIT + EXACT-RATIONAL-COUNTERCERTIFICATE + CERTIFICATION-BARRIER`.

WI-260 and WI-261 established two independent problems with the public FP-0.35 certification paths in `telleroutlook/weil-first-prime` at pinned commit `e66f467bc4447c5b2491577cbb6c3ae0e721fb43`: the post-fix reproduction script does not provide a valid exact positivity certificate, and the proofctl path does not assemble an enclosure of the intended first-prime Schur matrix. A further source-level audit finds a separate load-bearing defect in the positivity judge itself: `_min_pivot_mpmath` in `src/assemble/o1b_gate.py` does not implement the LDL Schur update it claims to certify.

The defect is exact and independent of floating-point accuracy, `tau`, or `c_L`: every off-diagonal Schur entry is updated twice. There is an explicit rational symmetric matrix for which the routine's algebra reports three positive pivots although the matrix has negative determinant. Thus neither fixing the exact matrix object nor increasing numerical precision is enough; the judge must also be repaired before the public FP-0.35 route can count as a certification.

## 1. The Schur update is applied twice off diagonal

After computing a pivot `d_k` and interval multipliers `L_col`, `_min_pivot_mpmath` loops over **all ordered pairs** `(i,j)` in the trailing block. For each pair it performs the interval analogue of

\[
A_{ij}\leftarrow A_{ij}-l_i d_k l_j
\]

and then immediately mirrors the result with `A[j][i] = A[i][j]`.

For a diagonal entry this is correct. For an off-diagonal pair `i != j`, however, the later ordered pair `(j,i)` reads the value already updated and mirrored by `(i,j)`, subtracts the same rank-one term a second time, and mirrors it back. On point intervals the implemented update is therefore

\[
A_{ij}\leftarrow A_{ij}-2l_i d_k l_j
\]

for every off-diagonal trailing entry, instead of the LDL identity

\[
A_{ij}\leftarrow A_{ij}-l_i d_k l_j.
\]

This is not an interval-overestimation issue. It changes the center algebraically and destroys the factorization invariant whose positive pivots would imply positive definiteness.

The affected routine is used by the `CERTIFY` tier of `run_o1b_gate`, and `checker/first_prime/exact_split.py` also imports and calls `_min_pivot_mpmath(C, dps=100)` for the proofctl exact-prime path discussed in WI-261.

## 2. Exact rational false positive

Consider

\[
A=\begin{pmatrix}
1&1/2&1/2\\
1/2&1/2&3/5\\
1/2&3/5&1/2
\end{pmatrix}.
\]

Its first LDL pivot is `1`. The correct first Schur complement has diagonal entries

\[
\frac12-\frac14=\frac14
\]

and off-diagonal entry

\[
\frac35-\frac14=\frac7{20}.
\]

Hence the correct second pivot is `1/4`, while the third is

\[
\frac14-\frac{(7/20)^2}{1/4}
=\frac14-\frac{49}{100}
=-\frac6{25}<0.
\]

Equivalently, direct exact arithmetic gives

\[
\det A=-\frac3{50}<0,
\]

so `A` is indefinite.

The buggy ordered-pair update instead changes the first trailing off-diagonal to

\[
\frac35-2\left(\frac12\right)(1)\left(\frac12\right)=\frac1{10}.
\]

It therefore obtains pivots

\[
1,\qquad \frac14,\qquad
\frac14-\frac{(1/10)^2}{1/4}
=\frac{21}{100}>0.
\]

All three are positive even though the input is indefinite. Their product is `21/400`, not the true determinant `-3/50`, directly witnessing that the routine is no longer computing an LDL factorization of its input.

This countercertificate uses only rational arithmetic. It survives arbitrary precision and zero-width input intervals.

## 3. The advertised interval arithmetic has a second rigor gap

Even after correcting the double update, `_min_pivot_mpmath` would still need a rounding repair before serving as a rigorous interval certificate. The routine converts rational endpoints through ordinary `mpmath.mpf` values and then performs ordinary `mpf` arithmetic; it does not use directed rounding or `mpmath` interval objects for the Schur operations. Calling the resulting endpoints “outward-rounded” is therefore not justified by the implementation alone.

This second issue is not needed for the countercertificate above. The ordered-pair bug already invalidates the positivity predicate at the exact algebraic level.

## 4. Relation to WI-260 and WI-261

This finding is logically independent of the earlier public-certificate failures.

WI-260 concerns the inverse/residual certificate used by `scripts/reproduce_fp035.py`; that script does not rely on `_min_pivot_mpmath`. WI-261 concerns the nominal proofctl exact path assembling a midpoint surrogate in `tau` and using `c_L=0` rather than the intended FP-0.35 operator. The present finding says that **even for a correctly assembled matrix**, the common LDL judge can return a false positive.

Consequently an independent recertification of FP-0.35 now has two distinct gates: first assemble a rigorous enclosure of the intended theorem matrix, with exact `tau`, prime terms, and correct `c_L`; then pass that enclosure to a mathematically valid positivity judge. Repairing either gate alone does not establish `lambda_(7/20)>0`.

Nothing here is evidence that FP-0.35 is false. The numerical candidate may still be correct. What is ruled out is treating the current `_min_pivot_mpmath` positive-pivot output as a proof of positive definiteness.

## Prior-art and novelty assessment

The finite-scale operator, FP-0.35 candidate, public checker architecture, and all surrounding analytic work belong to `telleroutlook/weil-first-prime`. The correct rank-one Schur update in LDL factorization is classical numerical linear algebra. Mathia's contribution here is only the code audit and exact rational false-positive witness; no priority claim is made.

No newer public commit than `e66f467bc4447c5b2491577cbb6c3ae0e721fb43` was present in the external repository during this audit, so no public repair of this routine was located before recording the finding.

## Falsification and repair test

Falsify this finding by identifying a different load-bearing public positivity routine for FP-0.35 that does not call the defective update, or a newer public revision that repairs it and is actually used by the certification path.

A direct repair should process each symmetric trailing entry exactly once — for example one triangle followed by mirroring — and then use genuine directed/outward interval arithmetic throughout division, multiplication, subtraction, and pivot propagation. The repaired checker should first pass exact rational regression cases including the matrix above, reproducing the true pivots `1, 1/4, -6/25` rather than `1, 1/4, 21/100`. Only after that judge-level test should the exact FP-0.35 matrix from the WI-261 repair target be replayed.

## Research consequence

The WI-259 finite-scale gate remains mathematically attractive:

\[
\lambda_{7/20}>0
\Longrightarrow a_*>7/20
\Longrightarrow
\text{the fixed }r=7/20\text{ phase window contains exactly the }n=2\text{ source atom}.
\]

But the public artifacts audited so far do not certify its premise. WI-260 blocks the reproduction-script certificate, WI-261 blocks exact identification of the proofctl matrix, and WI-262 independently blocks the interval-LDL positivity judge used by the O1-B/proofctl path. The next productive step remains an independent exact recertification, now explicitly requiring both **operator identity** and **judge correctness** rather than only a repaired matrix assembly.