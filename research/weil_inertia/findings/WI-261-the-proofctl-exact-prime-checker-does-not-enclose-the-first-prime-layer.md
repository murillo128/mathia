# WI-261 — the proofctl exact-prime checker does not enclose the exact first-prime layer

**Status:** `EXACT-CODE-AUDIT + EXACT-RATIONAL-COUNTERCERTIFICATE + CERTIFICATION-BARRIER`.

WI-260 showed that the post-fix public `scripts/reproduce_fp035.py` at `telleroutlook/weil-first-prime` commit `e66f467bc4447c5b2491577cbb6c3ae0e721fb43` does not yet certify the exact `L=7/20` first-prime matrix. A second, nominally stricter path exists in the same repository: `checker/first_prime/check_first_prime_certificate.py` advertises an independent `exact_prime_split_v1` replay whose obligations include `J-E-matrices-exact`, `F-matrix-assembled`, and positive `LDL^T` pivots.

A source-level reconstruction shows that this path also does **not** certify the exact FP-0.35 matrix as written. The failure is stronger than a floating-point hygiene concern: the checker computes an exact-prime metadata object and then does not use it in the matrix assembly; the actual prime matrices are rebuilt at a rational midpoint `TAU_MID`, and one of the resulting advertised intervals can be proved by exact rational arithmetic to exclude the true matrix entry. In addition, the positivity judge substitutes `c_L=0` for the nonzero Weil constant used by the FP-0.35 Schur criterion.

This is an evidence barrier, not evidence that `lambda_(7/20) <= 0`. The repository's independent numerical calculations may still be pointing at a true positive statement. What fails is the claimed exact certification path.

## 1. The checker recomputes a prime-layer object but does not feed it to the judge

The top-level checker executes

`prime = recompute_prime_layer(contract["sector"], CHECKER_PRECISION)`

and then separately calls

`certify_with_archimedean_base(contract["sector"], base, CHECKER_PRECISION)`.

The local variable `prime` is never passed into the second call and is never otherwise consumed. In `checker/first_prime/exact_split.py`, `certify_with_archimedean_base` calls `assemble_o1b_matrices`, and that function imports `build_M2_S2` from `src/assemble/o1b_gate.py` and rebuilds the prime matrices there.

Thus the comment that the checker has recomputed the “complete exact prime layer” is not a data-flow statement about the matrix on which positivity is judged. The object returned by `recompute_prime_layer` is dead with respect to the Schur matrix.

This matters because `build_M2_S2` does not use the exact

\[
\tau=\frac{20\log 2}{7}.
\]

Instead it sets

\[
\tau_{\rm mid}=\frac{\tau_{\rm lo}+\tau_{\rm hi}}2
\]

from the coarse rational bounds

\[
\frac{842}{1215}<\log2<\frac{23581}{34020},
\]

then evaluates `prime_legendre_matrices(indices, TAU_MID)` at that single rational point. Only the scalar `c_2` and `c_2^2` factors are subsequently widened. There is no interval evaluation of the `Q[tau]` matrices themselves.

Primary source paths at the pinned commit:

- `checker/first_prime/check_first_prime_certificate.py`;
- `checker/first_prime/exact_split.py`;
- `src/assemble/o1b_gate.py`;
- `src/prime_layer/legendre_shift.py`.

## 2. Exact rational countercertificate: the claimed `S2[0,0]` interval misses the true value

The missing `tau` enclosure is not merely formal. The simplest even-sector entry gives an exact counterexample to the interval claim.

For the `(0,0)` Legendre entry,

\[
E_{00}(\tau)=4-2\tau.
\]

The checker constants give

\[
\tau_{\rm mid}
=\frac{20}{7}\frac12\left(\frac{842}{1215}+\frac{23581}{34020}\right)
=\frac{15719}{7938},
\]

hence

\[
E_{00}(\tau_{\rm mid})=\frac{157}{3969}.
\]

Its lower coefficient for `c_2^2=(log 2)^2/2` is

\[
C_{2,\mathrm{sq},\mathrm{lo}}
=\frac12\left(\frac{842}{1215}\right)^2
=\frac{354482}{1476225}.
\]

Therefore `build_M2_S2` assigns the lower endpoint

\[
S^{\rm checker}_{2,00,\mathrm{lo}}
=\frac{55653674}{5859137025}
=0.009498612809793435\ldots.
\]

The exact entry is instead, with `ell=log 2`,

\[
S^{\rm exact}_{2,00}
=\frac{\ell^2}{2}\left(4-\frac{40\ell}{7}\right)
=:f(\ell)
=2\ell^2-\frac{20}{7}\ell^3.
\]

Use the positive atanh series

\[
\log2=2\sum_{k\ge0}\frac{1}{(2k+1)3^{2k+1}}.
\]

Its first four terms give the exact strict lower bound

\[
\ell>\ell_4:=\frac{53056}{76545}>\frac7{15}.
\]

Moreover

\[
f'(x)=4x-\frac{60}{7}x^2<0
\qquad(x>7/15).
\]

Hence

\[
S^{\rm exact}_{2,00}=f(\ell)<f(\ell_4)
=\frac{5917002063872}{627882701010075}
=0.009423737991751195\ldots.
\]

The gap is itself an exact positive rational:

\[
S^{\rm checker}_{2,00,\mathrm{lo}}-f(\ell_4)
=\frac{9402520598}{125576540202015}
=7.48748180422407\ldots\times10^{-5}>0.
\]

Therefore

\[
\boxed{S^{\rm exact}_{2,00}<S^{\rm checker}_{2,00,\mathrm{lo}}},
\]

so the interval produced by `build_M2_S2` provably does **not** contain the exact `(0,0)` first-prime second-moment entry. This falsifies the load-bearing interpretation of the emitted obligation `J-E-matrices-exact` for the matrix actually supplied to the positivity judge.

The argument uses only rational arithmetic plus the positive-term series for `log 2`; it does not depend on floating-point evaluation or on the thin spectral margin.

## 3. The positivity judge also changes the Weil constant

There is a second exact-object mismatch in the same path. In `judge_o1b_pivot`, the checker sets

`c_L = Fraction(0)   # conservative lower bound`

before constructing both

\[
b_L=H_d-c_L-L_0-\kappa_L
\]

and

\[
F=T_N+M_0+M_2-(c_L+L_0)G.
\]

But the repository's FP-0.35 reproduction uses the nonzero Weil constant

\[
c_L=\log(2\pi L)+\gamma_E
\]

with a certified rational bound near `1.36527`. The repository README itself distinguishes the large `c_L=0` O1-B pivots (`0.529/0.560`) from the thin “FP-0.35 Schur (correct c_L=1.365)” pivots (`+0.0087/+0.053`).

Substituting `c_L=0` therefore does not assemble the same finite matrix as the advertised FP-0.35 Schur gate. No theorem transferring positivity of the `c_L=0` surrogate to the required nonzero-`c_L` matrix is invoked or checked in `exact_split.py`; the checker simply judges the surrogate. Algebraically the substitution changes both multiplicative factors in `b_L F`, so calling it “conservative” is not by itself a proof of an order relation between the two Schur matrices.

This mismatch is independent of the `tau` countercertificate above. Fixing only one does not close the exact gate.

## 4. The current proofctl attestations therefore overstate what was checked

The committed attestation `.proofctl/attestations/lem-o1b-even.json` records `outcome: accepted` and emits pass verdicts including

- `o1b-even.J-E-matrices-exact`;
- `o1b-even.F-matrix-assembled`;
- `o1b-even.R-eta-assembled`;
- `o1b-even.ldlt-all-pivots-positive`.

The proofctl trust model in the external README correctly says that proofctl guarantees which checker ran, not that the checker is mathematically correct. The exact countercertificate above is precisely a checker-correctness failure: the checker can honestly attest that its code path ran while that code path still assembled a different matrix.

The repository's earlier `docs/FP035_CERTIFICATE_BUG.md` documents different historical defects — the incomplete four-term `S0` and the copy-based checker path — and then reports positive corrected numerical signs. It does not repair the `TAU_MID` enclosure failure shown above, and no commit newer than `e66f467...` is present in the public repository as of this audit.

## Prior-art and novelty assessment

All analytic constructions, Legendre identities, Schur criteria, rational `log 2` bounds, proofctl infrastructure, and numerical FP-0.35 candidates belong to `telleroutlook/weil-first-prime`. The external repository itself explicitly records that `c_L=0` and the correct FP-0.35 `c_L` are different computational rows, and it documents earlier certificate bugs.

The Mathia contribution here is narrower: tracing the current nominally exact checker end to end, identifying that its recomputed prime object is dead with respect to the judged matrix, and giving an exact rational witness that the midpoint-built `S2` interval excludes the true first-prime entry. No priority claim is made beyond this audit result.

A GitHub issue search at the pinned public state found no open or closed issue describing this `TAU_MID` / exact-prime checker mismatch, and the repository has no newer public commit correcting it. Absence from issue search is not used as a priority claim; it only means no public repair was located during this audit.

## Falsification and repair test

Falsify this finding by exhibiting a newer or alternate public checker path whose judged Schur matrix is proved to enclose the exact theorem matrix, including the exact `tau=20 log 2/7` dependence and the correct nonzero Weil constant, or by proving a valid transfer theorem from the present surrogate matrix to the exact one.

A direct repair is conceptually small but must be complete: evaluate every `J_ij(tau)` and `E_ij(tau)` as an interval polynomial on a rigorous enclosure of the exact `tau`; propagate the correlated `c_2`/`tau` dependence safely or bound it jointly; assemble the Schur matrix with the theorem's correct `c_L`; and certify positivity by a genuine outward-rounded interval `LDL^T`, Cholesky, or another valid matrix-norm argument.

## Research consequence

The live gate from WI-259 remains unchanged:

\[
\lambda_{7/20}>0
\Longrightarrow
a_*>7/20
\Longrightarrow
\text{the fixed }r=7/20\text{ phase window contains exactly the }n=2\text{ source atom}.
\]

But neither public certification route currently closes its premise: WI-260 blocks the post-fix `reproduce_fp035.py` path, while WI-261 blocks the nominal `exact_prime_split_v1` proofctl path. The next productive step is therefore an **independent exact recertification of the actual first-prime Schur matrix**, not another replay of either public checker and not phase analysis that assumes FP-0.35 as established evidence.
