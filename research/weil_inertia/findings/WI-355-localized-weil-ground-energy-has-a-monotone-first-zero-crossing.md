# WI-355 — localized Weil ground energy has a monotone first zero crossing under any RH failure

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECT + NON-RH`

## Claim

Masatoshi Suzuki's 2026 localized Weil-form operator framework supplies a stronger defect-localization interface than the normalized pair-correlation routes audited in WI-354. Let
\[
\lambda(a):=
\inf_{0\neq v\in C_c^\infty(-a,a)}
\frac{Q_W(v)}{\|v\|_{L^2}^2}.
\tag{1}
\]
Suzuki proves that this is the lowest eigenvalue of the localized self-adjoint Weil operator `A_a`, that `a \mapsto \lambda(a)` is continuous, that `\lambda(a)>0` for sufficiently small `a`, and that failure of RH is equivalent to `\lambda(a)<0` for some finite `a`.

There is an additional exact monotonicity which is immediate from the variational definition but is not needed in Suzuki's continuity theorem. If `0<a<b`, then
\[
C_c^\infty(-a,a)\subset C_c^\infty(-b,b),
\]
so
\[
\boxed{\lambda(b)\le \lambda(a).}
\tag{2}
\]
Consequently, under `not RH` there is a canonical first-crossing radius
\[
a_*:=\inf\{a>0:\lambda(a)\le0\},
\tag{3}
\]
with
\[
0<a_*<\infty,\qquad
\lambda(a)>0\ (a<a_*),\qquad
\lambda(a_*)=0,\qquad
\lambda(a)\le0\ (a\ge a_*).
\tag{4}
\]
Because Suzuki's `A_a` has discrete lower-bounded spectrum and `\lambda(a)` is its lowest eigenvalue, `0` is a ground-state eigenvalue of `A_{a_*}`. Thus **every RH failure forces a finite-radius localized Weil degeneracy**, rather than merely a negative direction appearing only in a cofinal or asymptotic limit.

At any fixed radius, this defect is also finite on the arithmetic side. Suzuki's screw function contains the prime-power term
\[
\sum_{n\le e^{|t|}}\frac{\Lambda(n)}{\sqrt n}(|t|-\log n),
\tag{5}
\]
and the localized kernel only samples `t=x-y` with `x,y\in(-a,a)`, hence `|t|<2a`. Equivalently, the explicit formula for the localized form only uses prime powers
\[
\boxed{n\le e^{2a}.}
\tag{6}
\]
Therefore an RH failure would have a witness at some finite `a_*` whose arithmetic part involves only finitely many prime powers `n\le e^{2a_*}`.

This materially redirects the sparse-defect program. WI-354 remains a valid barrier for **compressed, zero-count-normalized short-interval pair correlation**: a finite or sparse off-line set can disappear in that normalization. It does **not** imply that a sparse defect can stay invisible to every finite-radius **full localized Weil form**. Suzuki's theorem plus (2) shows the opposite: if RH fails, the full localized form must cross zero at a finite radius. The RH-facing target can therefore be stated source-side as a coercivity/no-crossing problem: prove `\lambda(a)>0` for every finite `a`.

## 1. Exact imported theorem and provenance

The primary source is:

Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 August 2026), DOI `10.48550/arXiv.2606.09096`.

Suzuki works with the localized closed Weil form `Q_W^a` on `L^2(-a,a)` and the associated self-adjoint operator `A_a`. Theorem 1.1 identifies `A_a` as the Friedrichs extension of the screw-function realization `B_a=D^*G_aD`. The paper recalls that `A_a` has discrete spectrum bounded below, with `+infinity` as its only accumulation point, and writes its lowest eigenvalue as
\[
\lambda_a=
\inf_{0\neq v\in\mathfrak D(Q_W^a)}
\frac{Q_W^a(v)}{\|v\|_2^2}.
\tag{7}
\]
Corollary 1.2 identifies the same infimum with the Rayleigh quotient over `C_c^\infty(-a,a)`, giving exactly the nested variational class used in (1)--(2).

Theorem 1.3 proves that `\lambda_a` is continuous in `a`. Immediately after that theorem Suzuki states that failure of RH is equivalent to existence of some `a>0` with `\lambda_a<0`; since `\lambda_a>0` for sufficiently small `a`, continuity gives a degenerating localized form at some finite radius. Theorem 1.4 strengthens the small-radius statement by proving positivity, simplicity of the lowest eigenvalue, and its small-`a` asymptotic.

The finite-prime statement is visible directly in Suzuki's equation (1.3), reproduced in (5). No zero-side conjecture is used to truncate the prime sum: compact localization makes `|x-y|<2a`, so the arithmetic data entering `G_a`, and hence the localized form, are restricted to prime powers at most `e^{2a}`.

## 2. Exact first-crossing deduction

Equation (2) follows solely from nested test spaces. It upgrades the literature's existence-of-a-degeneracy statement to a canonical threshold formulation.

Assume RH is false. Suzuki supplies `a_1>0` with `\lambda(a_1)<0`, while Theorem 1.4 supplies `a_0>0` such that `\lambda(a)>0` on `(0,a_0]`. Hence the set in (3) is nonempty and bounded away from zero. By definition and monotonicity, `\lambda(a)>0` for all `a<a_*` and `\lambda(a)\le0` for all `a>a_*`. Continuity gives
\[
\lambda(a_*)=0.
\tag{8}
\]
Since `\lambda(a_1)<0`, monotonicity also gives `\lambda(a)<0` for every `a\ge a_1`; therefore a possible zero plateau after `a_*` cannot persist indefinitely.

At `a_*`, discreteness of the spectrum means the infimum is attained: there is a nonzero ground state `v_*` with
\[
A_{a_*}v_*=0,
\qquad
Q_W^{a_*}(v_*)=0.
\tag{9}
\]
This is an exact finite-radius defect event, not a limiting statement about a sequence of ever larger finite matrices whose negative eigenvalues might drift to zero.

## 3. Consequence for the current Weil-inertia frontier

The cofinal Bombieri route recorded in WI-236 remains useful when one starts from finite zero truncations and tries to retain negative inertia as the truncation grows. Its unresolved difficulty is spectral escape: negative eigenvalues can approach zero and normalized negative vectors can lose tightness.

The localized full-form route has a different topology. Once `\lambda(a)` becomes nonpositive, domain inclusion prevents it from recovering positivity at larger radii. Under RH failure, continuity forces an actual finite zero crossing before the form becomes strictly negative. Therefore **cofinal negative-index stability is not required merely to prove detectability of an RH failure** in the full localized Weil form.

This suggests a sharper source-side program than attempting to amplify a sparse off-line population inside a zero-count-normalized statistic. One may instead seek a lower bound
\[
Q_W^a(v)\ge c(a)\|v\|_2^2,
\qquad c(a)>0,
\tag{10}
\]
for every finite `a`, using the finite prime-power ledger in (6), and understand how such lower bounds can be propagated as `a` crosses successive prime-power thresholds. Any valid propagation rule excluding the first zero crossing would be a genuine defect-to-zero mechanism.

## 4. What this does not prove

This finding does **not** prove RH and does not give an effective upper bound for `a_*` in terms of a hypothetical off-line zero. The localized operator is still infinite-dimensional even though its arithmetic coefficient data are finite at fixed `a`; "finite-prime" must not be read as "finite-dimensional" or as an automatically decidable positivity problem.

Nor does the result invalidate WI-354. Pair-correlation localization and full Weil-form localization retain different information. WI-354 shows that the currently available short-interval pair-correlation theorem loses fixed Fourier support and remains compatible with sparse defects after normalization by the local zero count. WI-355 shows that this sparse-blindness cannot be promoted to a no-go theorem for the uncompressed localized Weil form.

Finally, no priority claim is made for the localization or degeneracy theorem: those are Suzuki/Yoshida/Bombieri prior art as described by Suzuki. The exact additions recorded here are the elementary monotonicity (2), its first-crossing packaging (3)--(4), and the resulting programmatic consequence that a hypothetical RH failure has a finite-radius, finite-prime arithmetic witness in the full localized form.

## 5. Novelty audit

The local `weil_inertia` findings, mind state, clues, and `SOURCES.md` were searched for Suzuki, `arXiv:2606.09096`, screw-function localization, `lambda_a`, and a finite-radius first crossing. No existing local finding or source anchor contained this theorem surface. The closest current items are WI-236's cofinal Bombieri negative-index bridge and WI-354's short-interval pair-correlation localization barrier; the present result changes the interface rather than strengthening either compressed estimate.

The literature audit treats Suzuki's 2026 paper as the primary source and attributes the older localization/nondegeneracy line to Yoshida and Bombieri only through Suzuki's historical discussion. The first-crossing monotonicity is an exact deduction from Corollary 1.2, not a claimed new theorem of Suzuki and not a claim of external priority.

## Sources

- Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (17 Aug 2026), DOI `10.48550/arXiv.2606.09096`. Primary source for the screw-function realization of the localized Weil operator, the Rayleigh characterization of its lowest eigenvalue, continuity in the radius, small-radius positivity, and the equivalence `not RH => lambda_a<0` for some finite radius.
- E. Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers, I**, *Atti Accad. Naz. Lincei Rend. Lincei Mat. Appl.* 11 (2000), 183--233. Existing `weil_inertia` anchor for the finite-truncation inertia interpretation; Suzuki explicitly places his variational/localized framework in this line of work.
