# WI-370 — Desogus's existing MASTER scalar reserve cannot finance the corrected gamma floor

**Status:** `EXACT-DERIVED + PRIMARY-SOURCE-CRITICAL-AUDIT + DECISIVE-REPAIR-BARRIER + NON-ESTABLISHED-RH`.

## Claim

WI-368 showed that the gamma cancellation used in Section 5 of Marco Desogus's *The Three Gates: A Rooted-Operator Approach to Weil Positivity* (`arXiv:2609.20367v1`) has the wrong quadratic-form sign. WI-369 then reconstructed the exact gamma-corrected odd archimedean block and proved the sharp full-core semibound

\[
\mathcal A_A\succeq -C_\Gamma I,
\qquad
C_\Gamma=\frac\pi2+\gamma+\log(8\pi)
=5.37218341922566558\ldots .
\tag{1}
\]

The most conservative repair of the printed Gate-II argument would be to keep its downstream source/Feshbach/MASTER estimates unchanged and pay the missing corrected archimedean channel only through the uniform debit in (1). That repair cannot close with the scalar reserve already proved in the preprint.

Indeed, the paper's exact direct target-ground coefficient is

\[
\mathfrak B_k=\frac12+\log\frac1{w_k},
\qquad
w_k=\log\left(1+\frac1k\right),
\tag{2}
\]

and every later MASTER scalar coefficient is obtained from this reserve by subtracting nonnegative arithmetic/source penalties. At the bottleneck step `k=33`, even the **unspent direct target diagonal itself** is smaller than the sharp gamma debit:

\[
\boxed{\mathfrak B_{33}<C_\Gamma.}
\tag{3}
\]

This inequality is elementary and does not depend on replaying any numerical certificate. Since

\[
\log(1+x)>\frac{x}{1+x}\qquad(x>0),
\tag{4}
\]

we have `w_33>1/34` and hence

\[
\mathfrak B_{33}<\frac12+\log 34.
\tag{5}
\]

On the other hand `\pi>3` and `\gamma>1/2` give

\[
C_\Gamma>2+\log24.
\tag{6}
\]

Finally

\[
2+\log24-\left(\frac12+\log34\right)
=\frac32-\log\frac{17}{12}
>\frac12,
\tag{7}
\]

because `17/12<2` and `\log2<1`. Thus in fact the coarse analytic comparison already yields

\[
\boxed{C_\Gamma-\mathfrak B_{33}>\frac12.}
\tag{8}
\]

Numerically the actual scalar difference is much larger,

\[
C_\Gamma-\mathfrak B_{33}
=1.3607122431514167\ldots .
\tag{9}
\]

The same obstruction is visible still more directly in the paper's final aligned MASTER coefficient

\[
\mathfrak g_k^{\rm M+}
=\frac12+\log k
-\frac{439}{250\log2}\sum_m V_{k,m}
-\frac52 W_k.
\tag{10}
\]

Here `V_{k,m}` is a squared mismatch variance and `W_k` is the nonnegative aligned-forcing penalty. Therefore

\[
\mathfrak g_{33}^{\rm M+}
\le \frac12+\log33
<C_\Gamma.
\tag{11}
\]

The paper's own outward-rounded finite sweep reports the much smaller positive lower margin

\[
\mathfrak g_k^{\rm M+}
\ge 1.87814156017033534419\ldots
\tag{12}
\]

with the minimum at `k=33`; this is consistent with (11), but (3)--(8) show that the repair barrier is analytic and does not rest on that computation.

Consequently, **the gamma-cancellation error cannot be repaired by simply inserting the sharp uniform debit `-C_Gamma I` into the existing scalar MASTER budget.** The scalar channel is already too small before the downstream mismatch and aligned-forcing costs are paid.

This does not prove that the full rooted/Schur strategy is impossible and does not disprove any statement about RH. It identifies what a viable repair must use: the positive operator-valued remainder in WI-369 on the *actual source-conditioned harmonic vectors*, an additional arithmetic/source/polar coercive term not already spent in `mathfrak B_k`, or a structural theorem excluding the bulk quasimodes that make the bound (1) sharp. Scalar bookkeeping alone is now ruled out as a repair mechanism.

## 1. Why this is the correct comparison

The printed Section 5 transport removes the regular gamma channel and feeds the resulting gamma-free one-cell collar into the source/Feshbach machinery. Sections 6 and 8 then use `mathfrak B_k` as the primal target-ground diagonal from which the mismatch, inherited-response and aligned-forcing debits are charged. In Theorem 8.5 the surviving target-ground coefficient is exactly `mathfrak g_k^{M+}`.

WI-368 shows that the premise of that bookkeeping is false: the regular gamma channel survives with the quadratic-form sign fixed by the closed difference form. WI-369 gives an exact decomposition of the corrected channel as

\[
\mathcal A_A+C_\Gamma I
=R_A,
\qquad R_A\succeq0,
\tag{13}
\]

and proves that the constant `C_Gamma` is sharp on the full normalized one-cell core as `A\to\infty`.

If one refuses to use any further structure of `R_A`, then (13) is the strongest uniform replacement available from that audit. On a normalized target-ground component of amplitude `gamma`, the conservative lower-form replacement can therefore cost `C_Gamma |gamma|^2`. The unchanged scalar proof would need at least the same amount of unspent target-ground reserve. Equation (3) shows that it does not have it already at `k=33`.

The logical scope is deliberately narrow: (3) does **not** say that the exact harmonic vector at `k=33` realizes the worst case of (13). It says that any repair which discards `R_A` and tries to finance only its uniform floor from the existing scalar ledger is impossible. To continue the proof one must retain vector-dependent information that the scalar replacement loses.

## 2. The published MASTER budget has no hidden scalar surplus large enough

The preprint's Section 8 writes the aligned scalar margin as (10). The mismatch term is nonnegative because

\[
V_{k,m}
=\sum_{n\in\mathcal N_{k,m}}\frac{\Lambda(n)^2}{n}
-\frac{\left(\sum_{n\in\mathcal N_{k,m}}\Lambda(n)\right)^2}
{\sum_{n\in\mathcal N_{k,m}}n}
\ge0,
\tag{14}
\]

by Cauchy--Schwarz; the aligned quantity `W_k` is introduced as a nonnegative forcing penalty. Hence the right side of (10) is bounded above by `1/2+log k`, not merely bounded below by the finite certificate.

At `k=33`, high-precision evaluation gives

\[
\frac12+\log33=3.9965075614664802\ldots,
\qquad
C_\Gamma=5.3721834192256656\ldots,
\tag{15}
\]

so even this pre-loss ceiling misses the corrected full-core debit by

\[
1.3756758577591853\ldots .
\tag{16}
\]

Thus improving the interval arithmetic in Certificate 8.3 cannot repair the problem. The obstruction occurs before the certificate: it is a mismatch between the size of the sharp corrected archimedean floor and the scalar reserve architecture itself.

## 3. What remains viable

There are three logically distinct repair routes left by this calculation.

First, exploit the positive remainder `R_A` in (13) quantitatively on the exact harmonic/source-conditioned vectors. WI-369 shows that `R_A` can vanish asymptotically on arbitrary fixed interior test functions, so this requires a theorem that those bulk quasimodes are incompatible with the source-conditioned harmonic graph used by Gate II.

Second, identify a genuinely additional source, arithmetic or polar coercivity term that survives the common cut and has not already been charged in `mathfrak B_k`, `V_{k,m}`, `W_k`, or the folded debit. Because the paper is explicitly organized to avoid double spending, such a term must be located in the exact same-vector decomposition rather than inferred from a separately positive comparator.

Third, replace the scalar ledger by an operator-valued estimate coupling the positive gamma remainder to the source mismatch/inherited-line geometry. This is the most natural continuation: (13) gives a screened difference term, endpoint multiplier and positive Hankel image, while Sections 6--8 give explicit source intervals and Schur responses. A successful inequality must show that these structures cannot simultaneously approach their respective worst cases.

## 4. Provenance and novelty audit

**Primary source under audit.** Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, arXiv:2609.20367v1, submitted 17 September 2026, with supplementary material DOI `10.5281/zenodo.22799713`. The load-bearing printed statements are Lemma 4.1 / equation (44) for `mathfrak B_k`, equation (203) and Certified finite computation 8.3 for `mathfrak g_k^{M+}`, and Theorem 8.5 for the final harmonic-graph coercivity assembly.

**Internal exact dependencies.** WI-368 supplies the form-sign failure of the printed gamma cancellation. WI-369 supplies the exact corrected archimedean decomposition, the sharp constant `C_Gamma`, and the bulk quasimodes showing that no smaller uniform full-core debit can replace it.

**Prior-art audit.** A targeted search of the Desogus preprint, its public abstract/supplement trail, and current public discussion located no statement comparing the corrected gamma floor with the MASTER target-ground reserve. The derivation (3)--(8) is elementary once WI-369 is available. This is recorded as an audit result, not as a claim of priority.

## Research consequence

The next repair target is now sharper than "find enough source reserve." The existing scalar reserve cannot pay the corrected archimedean floor even before its advertised arithmetic losses. Therefore a viable Gate-II repair must prove a **source-conditioned coercivity statement for the positive remainder `R_A` itself**, or exhibit a new unspent operator-valued source channel. Re-optimizing the same scalar MASTER certificate cannot close the gap.
