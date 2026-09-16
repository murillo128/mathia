# MC-332 — Unrestricted mode-dependent weights erase character oscillation

**Status:** `EXACT-DERIVED` · `DECISIVE-NEGATIVE` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-331` shows that one common prime coefficient vector cannot improve the reciprocal endpoint's fixed-common-modulus contradiction beyond the quartic horizon, and leaves mode-dependent coefficients `w_{a,r}` as a possible pre-compression escape. There is an immediate but important boundary on that escape: **arbitrary mode dependence is too permissive to encode cancellation at all**.

Let `\mathcal A` be a finite set of `A` primes, all coprime to a modulus `q`, and let `\Xi` be any finite family of Dirichlet characters modulo `q`. For an arbitrary coefficient matrix

\[
W=(w_{\chi,r})_{\chi\in\Xi,\ r\in\mathcal A},
\]

define rowwise character sums

\[
T_W(\chi):=\sum_{r\in\mathcal A}w_{\chi,r}\chi(r).
\tag{1}
\]

Then

\[
\boxed{
\sum_{\chi\in\Xi}|T_W(\chi)|^2
\le
A\sum_{\chi\in\Xi}\sum_{r\in\mathcal A}|w_{\chi,r}|^2,
}
\tag{2}
\]

and the constant `A` is exact. Indeed, for any target vector `c=(c_\chi)_{\chi\in\Xi}`, choose the phase-matched matrix

\[
w_{\chi,r}=c_\chi\,\overline{\chi(r)}.
\tag{3}
\]

Since `|\chi(r)|=1`, this gives

\[
T_W(\chi)=A c_\chi,
\qquad
\sum_{\chi,r}|w_{\chi,r}|^2=A\sum_\chi|c_\chi|^2,
\tag{4}
\]

so equality holds in `(2)` whenever `c\ne0`.

Thus a hypothetical prime-family estimate that is uniform over **all** mode-dependent matrices and charges them only by Frobenius `L^2` norm cannot retain any large-sieve/Halász--Montgomery cancellation gain: each row can simply multiply by the conjugate character and dephase itself pointwise. The normalized family problem collapses to independent copies of the trivial one-row Cauchy bound.

At the exact reciprocal endpoint this obstruction remains strong even after imposing a seemingly severe low-rank condition. Let

\[
G=\mathbf F_2^R,
\qquad
\Xi=G\setminus\{0\},
\]

and let the shell primes occupy the `R` one-defect sign cells

\[
S=\{\mathbf1+e_j:1\le j\le R\}
\]

as in `MC-331`, with evaluation matrix

\[
B_{a,r}=\chi_a(r)=(-1)^{a\cdot s(r)}.
\tag{5}
\]

Then

\[
\boxed{\operatorname{rank} B=R.}
\tag{6}
\]

Consequently the phase-erasing choice

\[
W=B
\tag{7}
\]

has matrix rank only `R`, while the number of nonprincipal modes is `2^R-1`, yet it forces

\[
T_W(a)=A
\qquad(a\ne0).
\tag{8}
\]

More generally `W=\operatorname{diag}(c)B` has the same rank `R` whenever all `c_a\ne0` and realizes `(4)` on every nonprincipal endpoint mode.

Therefore **"use a mode-dependent coefficient matrix" is not yet a meaningful analytic escape from `MC-331`**, and neither is the restriction "use a matrix of rank at most `R`" at this endpoint. A viable joint/pre-compression theorem must impose a structural restriction that genuinely prevents or quantitatively penalizes the matched filter `(3)`—for example a restricted dependence of the coefficients on `(\chi,r)` whose analytic cost cannot be reduced to unconstrained rowwise `L^2`. Merely allowing mode dependence, or merely requiring low rank relative to the exponential family size, makes the desired cancellation theorem false at the trivial scale.

No estimate for `M(x)` follows.

## 1. The unrestricted matrix norm is exactly the rowwise Cauchy norm

For each fixed `\chi`, Cauchy--Schwarz gives

\[
|T_W(\chi)|^2
\le
\left(\sum_{r\in\mathcal A}|w_{\chi,r}|^2\right)
\left(\sum_{r\in\mathcal A}|\chi(r)|^2\right).
\tag{9}
\]

Every shell prime is coprime to `q`, so the second factor is exactly `A`. Summing `(9)` over the character family proves `(2)`.

Now take `(3)`. Pointwise,

\[
w_{\chi,r}\chi(r)
=c_\chi |\chi(r)|^2
=c_\chi,
\]

which proves the first identity in `(4)`. The second follows from `|\chi(r)|=1`. Hence

\[
\frac{\sum_\chi|T_W(\chi)|^2}
{\sum_{\chi,r}|w_{\chi,r}|^2}
=A
\tag{10}
\]

for every nonzero target vector `c`, proving sharpness.

This is not a subtle character-sum phenomenon. Once every mode receives its own arbitrary coefficient row, the coefficients can contain the inverse phase of that exact mode. The character oscillation that a large-sieve estimate is supposed to exploit has been cancelled before the theorem starts.

## 2. Why the standard shared-coefficient architecture is load-bearing

The classical large sieve and the prime Halász--Montgomery theorem used in `MC-329`--`MC-331` allow an arbitrary coefficient sequence, but the **same sequence is tested against every character**. In the notation of `MC-331`, one controls

\[
T_w(\chi)=\sum_r w_r\chi(r)
\tag{11}
\]

with a single vector `w=(w_r)`.

That shared-input condition couples the family: one choice of `w` cannot simultaneously conjugate all distinct character phases. This is exactly the resource exploited by orthogonality/duality and large-sieve-type estimates. Equation `(3)` removes the coupling by supplying one phase-matched input per row.

Accordingly, replacing `(11)` by `(1)` is not a harmless strengthening of the coefficient class. It changes the mathematical problem from controlling one source vector under many character observations to controlling unrelated source vectors mode by mode. Any future theorem with mode-dependent coefficients must recover a nontrivial coupling condition in some other form.

## 3. The reciprocal endpoint admits phase erasure at rank `R`

For the endpoint rank statement, collapse repeated prime columns according to their sign cell. Let `V` be the `(2^R-1)\times R` matrix

\[
V_{a,s}=(-1)^{a\cdot s},
\qquad
a\in G\setminus\{0\},\ s\in S.
\tag{12}
\]

The full Walsh matrix on all `a\in G` has orthogonal columns, so

\[
\sum_{a\in G}(-1)^{a\cdot(s+t)}
=2^R\mathbf1_{s=t}.
\tag{13}
\]

Deleting the principal row `a=0`, whose entries are all `1`, gives the exact Gram matrix

\[
\boxed{
V^*V=2^R I_R-\mathbf1\mathbf1^*.
}
\tag{14}
\]

Its eigenvalues are

\[
2^R\quad\text{with multiplicity }R-1,
\qquad
2^R-R\quad\text{on the constant direction}.
\tag{15}
\]

For every `R\ge2` these are positive, hence

\[
\operatorname{rank}V=R.
\tag{16}
\]

The full prime-column matrix `B` in `(5)` is obtained from `V` only by repeating each of the `R` cell columns `A/R` times, so `(6)` follows.

Now choose the coefficient matrix `W=B`. Since every endpoint character is real-valued on the shell,

\[
w_{a,r}\chi_a(r)=\chi_a(r)^2=1,
\]

and `(8)` follows. Yet by `(6)`,

\[
\operatorname{rank}W=R.
\tag{17}
\]

Thus a rank constraint that looks tiny compared with the `2^R-1` row population does not stop exact dephasing. The endpoint evaluation matrix itself is already a low-rank matched filter because all shell primes occupy only `R` sign-cell types.

This also shows why generic low-rank language can be misleading here. What matters is not rank by itself, but whether the admissible coefficient class contains the character evaluation geometry that it is supposed to test.

## 4. Relation to the quartic frontier

`MC-330` proves that signed linear or quadratic processing **after** the character family has been compressed to total bias energy cannot beat the quartic horizon. `MC-331` moves the operation to the prime side and proves that **one common** arbitrary coefficient vector still cannot help, because Schlage-Puchta's theorem is already uniform in that vector and the endpoint operator norm is asymptotically saturated by the unweighted shell.

The remaining phrase "mode-dependent coefficients" must therefore be read with care. Equations `(2)`--`(4)` show that the fully unrestricted class is not a stronger analytic route; it is a programmable matched filter that destroys the oscillatory content. The endpoint calculation `(14)`--`(17)` further shows that an exponential-versus-polynomial rank comparison does not repair the problem.

The next legitimate linear question is consequently narrower:

> Is there a **source-natural restricted joint coefficient class** that couples mode and prime strongly enough to retain information absent from common weights, but weakly enough to exclude phase matching, and for which one can prove an analytic family estimate with a better endpoint-normalized exponent balance than the common-weight `L^2` theorem?

This finding does not answer that question. It supplies an admission test for proposed classes: before attempting a new large-sieve estimate, verify that the class does not already contain `(3)` or an asymptotically equivalent dephasing sequence at comparable norm cost.

## 5. Prior art and novelty boundary

No novelty is claimed for Cauchy--Schwarz, matched filtering by conjugate phases, finite Fourier/Walsh orthogonality, matrix rank, or the operator interpretation of large-sieve inequalities. These are elementary or classical mechanisms.

The relevant classical coefficient architecture is exemplified by H. L. Montgomery and R. C. Vaughan, *The large sieve*, Mathematika **20** (1973), 119--134, DOI `10.1112/S0025579300004708`: the arbitrary complex coefficients form one common sequence evaluated against the family. The prime-supported family theorem already audited in `MC-329`--`MC-331` is Jan-Christoph Schlage-Puchta, *Primes in short arithmetic progressions*, Acta Arithmetica **106** (2003), 143--149, DOI `10.4064/aa106-2-4`; it likewise charges one arbitrary prime-supported coefficient sequence through its quadratic norm.

A targeted literature check on 16 September 2026 found standard large-sieve/operator-duality formulations and matrix viewpoints, but no external theorem is needed for `(2)`--`(17)`. No claim is made that the unrestricted-matrix observation is new. The durable Mathia delta is its application as a **frontier restriction** immediately after `MC-331`: it prevents the research program from mistaking unrestricted mode dependence, or low rank alone, for unexplored arithmetic leverage.

## Boundaries and falsification tests

- **Coprimality is load-bearing for `(3)`--`(4)`.** If `r` is not coprime to `q`, a Dirichlet character can vanish. The reciprocal endpoint shell uses primes outside the source modulus, so its evaluations have unit modulus.
- **The general sharpness theorem does not use equal endpoint cells.** Equations `(2)`--`(4)` hold for any finite coprime prime set and any character family.
- **Equal one-defect endpoint geometry is used only for the rank-`R` strengthening.** Without the exact cell support, the matched matrix may have larger rank.
- **Rank `R` is not claimed minimal.** The result only shows that allowing rank up to `R` is already enough to dephase every endpoint mode simultaneously.
- **Structured mode dependence remains open.** A coefficient class that forbids `(3)` through locality, factorization, algebraic restrictions, shared latent parameters, or another audited constraint may still admit a nontrivial family theorem.
- **Higher-order statistics remain open.** Bilinear, multilinear or nonlinear arithmetic estimates are not reduced to `(2)` unless their control factors through the same unrestricted rowwise `L^2` norm.
- **No circular zero information is used.** The proof is finite linear algebra on character values plus the exact endpoint cell support.
- **No RH-scale conclusion is claimed.** This is a no-go/admission theorem for one proposed escape from the quartic method boundary.

## Consequence for the research line

`MC-331` narrowed the pre-compression escape from arbitrary common weights to genuinely joint mode-prime information. `MC-332` narrows it again: **joint dependence must be structured, not arbitrary, and low rank relative to the character population is not by itself enough structure.**

Any next linear proposal should specify its admissible coefficient class before invoking analytic estimates, exhibit why that class excludes the conjugate-character matched filter, and account for the cost of whatever cross-mode coupling remains. Otherwise the proposed improvement is either already covered by the common-weight no-go or becomes trivial through exact phase erasure.