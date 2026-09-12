# WI-260 — the public FP-0.35 generator still does not certify the exact first-prime matrix

**Status:** `EXACT-CODE-AUDIT + CERTIFICATION-BARRIER + PRIOR-ART-REDIRECT`.

The live phase-defect program in WI-259 is gated on the finite-scale statement

\[
\lambda_{7/20}>0.
\]

The latest public `telleroutlook/weil-first-prime` source still does **not** establish that exact statement with a rigorous certificate as written, even after the important 12 Aug 2026 fix at commit

`e66f467bc4447c5b2491577cbb6c3ae0e721fb43`.

That commit repairs a real midpoint/radius construction error and restores positive numerical margins, but a source-level audit of the post-fix `scripts/reproduce_fp035.py` exposes two independent remaining certification gaps:

1. the prime-layer matrix is assembled with rationalized or binary-float point approximations to exact transcendental quantities, with no interval enclosure or perturbation transfer to the exact operator;
2. the advertised Arb residual `||I-B C||_inf` is not actually bounded by the code: the script takes a maximum using partial-order Arb comparisons and, even if that aggregation were repaired, it tests an entrywise maximum rather than a submultiplicative induced matrix norm.

These are proof-boundary defects, not evidence that FP-0.35 is false. The reported even-sector margin near `9.5e-4` is large compared with the obvious scalar roundoff scales, so a corrected certificate may well survive. But an independent replay of the current script would only reproduce the same logical gaps and therefore cannot by itself promote FP-0.35 into Mathia's established evidence.

## 1. The latest generator does not assemble the exact prime-layer parameters

At the pinned post-fix commit, `scripts/reproduce_fp035.py` defines

`TAU_RAT = Fraction(math.log(2) / (7/20)).limit_denominator(10_000)`

and

`C2_FLOAT = math.log(2) / math.sqrt(2)`.

The exact first-prime operator in the repository's own Theorem 4 instead uses

\[
\tau=\frac{\log2}{L}=\frac{20\log2}{7},
\qquad
c_2=\frac{\log2}{\sqrt2}.
\]

For `L=7/20`, the rationalized value is

\[
\tau_{\rm rat}=\frac{17802}{8989},
\]

whereas high-precision evaluation gives

\[
\tau-\tau_{\rm rat}
=1.9240495165047755\ldots\times10^{-9}.
\]

The size is small, but the logical issue is exact: `tau_rat` is a different number and the script supplies no enclosure containing the true `tau` and no perturbation estimate transferring positivity from the rationalized matrix to the exact one.

The loss of rigor continues inside the Arb assembly. The post-fix source uses

- `c2_arb = arb(str(C2_FLOAT))` rather than an Arb enclosure of `log(2)/sqrt(2)`;
- `T_ij = arb(str(H(nj))) * G_ij`, where `H(n)` is first summed in Python binary floating point although harmonic numbers are exact rationals;
- `arb(str(float(compute_J(...))))` and `arb(str(float(compute_E(...))))`, even though `compute_J` and `compute_E` return exact `Fraction` values for the chosen rational `tau`.

Python-flint's ball arithmetic rigorously propagates the values it is given; it cannot retroactively turn a rounded decimal surrogate into an enclosure of a different exact transcendental constant. The python-flint documentation explicitly warns that float inputs represent the supplied binary floating-point value rather than an intended nearby real constant. The repository's `src/prime_layer/legendre_shift.py` already supplies the useful structural fact that `J_ij(tau),E_ij(tau)` lie in `Q[tau]`, so there is no mathematical obstacle to evaluating those polynomials on an Arb enclosure of the exact `tau`.

For scale only, not as a proof, the direct discrepancy in the rationalized `tau` is about `1.9e-9`, while the decimal point approximation used for `c_2` differs from `log(2)/sqrt(2)` by about `3.6e-17`. Those numbers make this look repairable; they do **not** supply the missing full-Schur perturbation budget.

Primary source: `telleroutlook/weil-first-prime`, pinned commit `e66f467bc4447c5b2491577cbb6c3ae0e721fb43`, especially `scripts/reproduce_fp035.py` and `src/prime_layer/legendre_shift.py`.

## 2. The Arb residual test is not a certified matrix-norm bound

The intended inverse-residual argument is standard. Let `C` range over the symmetric interval matrix and let `B` be a numerical approximate inverse. If one rigorously proves, in a submultiplicative matrix norm,

\[
\|I-BC\|<1
\]

for every `C` in the interval enclosure, then every such `C` is nonsingular by the Neumann lemma. Combined with a positive-definite reference point and a continuous symmetric path inside the enclosure, this can freeze the inertia and certify positivity.

The post-fix script does not establish that hypothesis. It initializes

`max_resid = arb(0)`

and for each entry of `R=I-B C_arb` executes the logical pattern

`mag = abs(delta); if mag > max_resid: max_resid = mag`,

then accepts when `max_resid < arb(1)`.

There are two distinct problems.

First, Arb comparisons are **certifying partial-order comparisons**. Python-flint documents that a predicate such as `x > y` returns true only when it holds for every point represented by the input balls; overlapping balls make the comparison indeterminate and therefore false. Consequently an absolute residual ball containing zero, for example an enclosure of the form `[0,epsilon]`, need not satisfy `mag > arb(0)` and can simply be ignored by this `max` loop. The printed value `residual=0` therefore does not imply that the interval residual is the exact zero matrix; it can merely mean that the attempted total-order maximum never moved away from the exact initial zero.

Second, even a correctly computed scalar upper bound

\[
m\ge\max_{i,j}|R_{ij}|
\]

would not justify the test `m<1`. The induced infinity norm required for the usual Neumann argument is

\[
\|R\|_\infty=\max_i\sum_j|R_{ij}|.
\]

From an entrywise maximum one only gets

\[
\|R\|_\infty\le n m,
\]

so `m<1` alone is insufficient in dimensions `n=8` and `n=6`. One must rigorously upper-bound the row sums themselves, or use another verified submultiplicative norm / interval factorization.

This matters especially because the script's float eigenvalue is not an interval proof. The repository README says that the PASS contract requires positivity to be verified by interval `LDL^T`, while the advertised reproduction script instead relies on this inverse-residual calculation. The current code therefore does not meet the mathematical burden suggested by its own public PASS description.

Python-flint comparison semantics: <https://python-flint.readthedocs.io/en/stable/general.html>. Arb representation and exact/inexact inputs: <https://python-flint.readthedocs.io/en/stable/arb.html>.

## 3. This is separate from the already acknowledged certificate bugs

The external repository already documents two earlier defects in `docs/FP035_CERTIFICATE_BUG.md`: an `S0=S_KK` omission that inflated the even-sector spectral margin by about a factor of sixteen, and a copy-based certificate/checker path that did not genuinely recompute its obligations. The repository correctly retracts an intermediate negative diagnosis and reports that two corrected finite computations recover a positive sign.

Commit `e66f467...` then fixes another real issue: python-flint's two-argument `arb(mid,rad)` constructor had been fed lower/upper endpoints. The corrected `_enc(lo,hi)` function now converts certified endpoint intervals to midpoint-radius balls properly, and the regenerated output reports approximately

\[
0.00094994\quad\text{(even)},
\qquad
0.01895967\quad\text{(odd)}.
\]

The present audit does not dispute those numerical observations. It identifies proof obligations that remain **after** that fix and are not addressed by the repository's bug note: exact enclosure of the first-prime constants/polynomials and a logically valid interval residual/inertia certificate.

There is also still a public status mismatch at the pinned head: `README.md` says `FP-0.35 HOLDS`, while `docs/THEOREMS.md` says that FP-0.35 itself remains a conjecture. WI-259 already treated that as an evidence-boundary warning; the source defects above now show that the warning is not merely metadata freshness.

## 4. Consequence for WI-259 and the live clue

WI-259's exact implication remains unchanged:

\[
\lambda_{7/20}>0
\Longrightarrow
a_*>7/20
\Longrightarrow
\text{the fixed phase radius }r=7/20\text{ contains exactly the }n=2\text{ atom}.
\]

What changes is the gate condition. The next step is **not** simply to cold-replay the current `reproduce_fp035.py`. A replay would be valuable for reproducibility, but it would certify only what that script actually checks.

Before FP-0.35 can enter Mathia as established evidence, one of the following must happen:

1. the external generator is repaired so that all exact first-prime constants are enclosed rigorously and the residual/inertia test is mathematically valid, followed by an independent replay; or
2. an independent certificate/proof establishes the same `lambda_{7/20}>0` statement without relying on this checker path.

A minimal repair path is concrete: enclose `log2`, `sqrt2` and `tau=20 log2/7` directly in Arb; evaluate the exact `Q[tau]` Legendre polynomials on that enclosure; insert harmonic numbers exactly; compute rigorous upper bounds for every residual row sum and require the induced norm to be `<1`, or replace the inverse-residual step by a certified interval `LDL^T`/Cholesky argument. The final certificate should expose the nonzero residual upper bound rather than reporting a partial-order artifact as exact zero.

Because the nominal even-sector margin is about `9.5e-4`, the corrected theorem may well survive. The substantive conclusion here is therefore an **evidence barrier**, not a mathematical negative result about finite-scale Weil positivity.

## Prior-art and novelty assessment

The finite-scale operator, Legendre algebra, split-residual criterion, numerical candidate, and earlier bug history belong to `telleroutlook/weil-first-prime`. The Neumann residual criterion and induced matrix norms are standard numerical linear algebra; Arb comparison semantics belong to FLINT/python-flint. No novelty is claimed for any of those ingredients.

The Mathia contribution is the source audit against the exact gate required by WI-259: the latest public post-fix generator still replaces load-bearing exact constants by nearby point surrogates and its residual loop is not a rigorous implementation of the matrix-norm condition it names. This materially changes the research action because **replay alone is no longer a sufficient gate-closing experiment**.

## Falsification and audit test

Falsify this finding by showing, at the pinned post-fix commit or a clearly newer corrected commit, that the exact `tau`, `c_2`, harmonic and `J/E` quantities used in the theorem are enclosed by the constructed Arb objects, and that the positivity step uses a valid certified matrix norm or interval factorization rather than the current partial-order entrywise maximum.

The natural positive audit is to patch those points and record a rigorous lower margin for both parity sectors. If the repaired exact certificate remains positive, WI-260 becomes a historical certification barrier and WI-259's one-prime phase program can proceed. If the margin disappears, FP-0.35 remains open and the line must seek another positivity theorem past `(log2)/2`.

## Research consequence

Keep the first-prime gate as the highest-leverage live target, but narrow it from “independent replay” to **independent exact recertification**. Do not spend phase-defect effort assuming `r=7/20` is available until that recertification is complete. Conversely, do not abandon FP-0.35 on the basis of this audit: the discovered defects are proof-engineering gaps with apparently small scalar perturbations, not a counterexample to the underlying positivity claim.
