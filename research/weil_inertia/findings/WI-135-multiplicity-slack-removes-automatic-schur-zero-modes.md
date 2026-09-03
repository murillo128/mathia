# WI-135 — multiplicity slack removes the automatic zero modes from the Lamzouri Schur bootstrap

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + BOOTSTRAP-INTERFACE`. WI-134 obtains a depth-weighted spectral obstruction by expanding each off-line conjugate-pair representative according to its multiplicity. That expansion is count-correct, but it creates `m_j-1` exact zero eigenvalues whenever an off-line pair has multiplicity `m_j>1`. The exact `U`-slack already reconstructed in WI-126 charges precisely that same multiplicity excess. Combining the two remainders removes those artificial zero modes completely.

For the **distinct** off-line pair representatives, let

\[
S=U^*(I-P_V)U\succ0
\]

be the normalized odd Schur complement from WI-132, let

\[
r_\tau(S):=\#\{i:\lambda_i(S)<\tau\},
\]

and for a fixed depth cutoff `A>0` put

\[
D_{2,A}:=\sum_j m_j\min(y_j^2,A^2).
\]

Then for every `A,\tau>0` Lamzouri's finite inequality has the exact strengthening

\[
\boxed{
 n\ge 2N-Q
 +4\min(\tau,A^{-2})
 \bigl(D_{2,A}-A^2r_\tau(S)\bigr)_+.
}
\tag{A}
\]

Thus multiplicity cannot be used to manufacture the macroscopic low-energy sector required by WI-134. If the Lamzouri baseline is asymptotically sharp and `D_{2,A}\ge\delta N`, then for every fixed `\tau>0`,

\[
\boxed{
\liminf\frac{r_\tau(S)}N\ge\frac{\delta}{A^2}.
}
\tag{B}
\]

The near-null sector in (B) belongs to the positive-definite Schur matrix indexed by **distinct off-line conjugate pairs**. It is therefore genuine geometric screening, not the tautological nullity produced by repeating a column for multiplicity. Critical-line doubles remain a separate zero-cost exceptional population and are not represented in `S`.

No unconditional zeta-zero percentage changes in this finding.

## 1. Exact inputs from WI-126 and WI-134

Use Lamzouri's finite conjugation-invariant multiset notation. Choose one representative

\[
z_j=x_j+iy_j,\qquad y_j>0,
\]

from each of the `k` distinct non-real conjugate pairs and let `m_j` be its multiplicity. Define the normalized odd divided-difference columns

\[
u_j=\frac{h_{z_j}}{y_j},
\qquad
Ue_j=u_j,
\]

and

\[
S=U^*(I-P_V)U.
\tag{1}
\]

WI-132 proves that `S` is positive definite for every finite collection of distinct off-real pairs. WI-126 gives the exact slack identity

\[
\Delta:=n-(2N-Q)=R_B+R_U+R_M+R_H,
\qquad R_\bullet\ge0,
\tag{2}
\]

and the horizontal estimate

\[
R_H\ge4H,
\qquad
H=\sum_jm_jy_j^2S_{jj}.
\tag{3}
\]

WI-134 expands each column `u_j` exactly `m_j` times. If

\[
K:=\sum_jm_j,
\qquad
\widetilde S=\widetilde U^*(I-P_V)\widetilde U,
\]

and

\[
\widetilde r_\tau:=\#\{i:\lambda_i(\widetilde S)<\tau\},
\]

then for every `A,\tau>0`,

\[
H\ge \tau\bigl(D_{2,A}-A^2\widetilde r_\tau\bigr)_+.
\tag{4}
\]

The only issue is that `\widetilde S` deliberately includes exact duplication modes when `m_j>1`.

## 2. The expanded nullity is exactly the off-line multiplicity excess

Let

\[
D=\operatorname{diag}(m_1,\ldots,m_k)
\]

and let `J:C^K->C^k` sum the occurrence coefficients belonging to the same distinct pair. Then

\[
\widetilde U=UJ,
\qquad
\widetilde S=J^*SJ,
\qquad
JJ^*=D.
\tag{5}
\]

Since `S\succ0` and `J` has rank `k`,

\[
\boxed{
\operatorname{nullity}(\widetilde S)=K-k
=\sum_j(m_j-1)=:E.
}
\tag{6}
\]

The nonzero eigenvalues of `\widetilde S` are the eigenvalues of

\[
S^{1/2}DS^{1/2}.
\tag{7}
\]

Because `D\succeq I`,

\[
S^{1/2}DS^{1/2}\succeq S.
\tag{8}
\]

The min--max principle therefore gives, for every `\tau>0`,

\[
\boxed{
\widetilde r_\tau\le E+r_\tau(S).
}
\tag{9}
\]

So after the `E` automatic zero modes are removed, multiplicity can only move the remaining expanded eigenvalues **upward** relative to the distinct-pair Schur spectrum.

This uses only the standard facts that `J^*SJ` and `S^{1/2}JJ^*S^{1/2}` have the same nonzero spectrum and that Hermitian eigenvalues are monotone under Loewner order.

## 3. Lamzouri's `U`-slack charges the same `E`

WI-126 gives, with `d=r+k` and its scalar coefficient sum denoted there by `A_U`,

\[
R_U
=\sum_{j\in U}\left(\alpha_j-\frac{A_U}{d}\right)^2
+\frac{A_U(A_U-2d)}d,
\qquad A_U\ge2d,
\tag{10}
\]

and the exact decomposition

\[
A_U-2d
=\text{nonnegative terms}
+2\sum_j\left[(m_j-1)+m_j\|P_{U^\perp}h_{z_j}\|^2\right].
\tag{11}
\]

In particular

\[
A_U-2d\ge2E.
\]

Since `A_U/d\ge2`, equations (10)--(11) imply

\[
\boxed{
R_U\ge2(A_U-2d)\ge4E.
}
\tag{12}
\]

Thus the exact duplicate nullity in (6) is not free in Lamzouri's proof: every extra occurrence of a non-real pair already pays at least four units of `U`-slack.

## 4. Eliminate the multiplicity variable

Combine (2)--(4), (9), and (12):

\[
\frac{\Delta}{4}
\ge
E+\tau\bigl(D_{2,A}-A^2(E+r_\tau(S))\bigr)_+.
\tag{13}
\]

Set

\[
X=D_{2,A}-A^2r_\tau(S).
\]

For `X<=0` the desired bound is trivial. For `X>0`, minimize the right-hand side of (13) over the larger continuous range `E>=0`. If `E>=X/A^2`, the value is at least `X/A^2`. If `0<=E<X/A^2`, it equals

\[
\tau X+E(1-\tau A^2).
\]

Hence its minimum is exactly

\[
X\min(\tau,A^{-2}).
\tag{14}
\]

Substitution into (13) proves (A).

The point is not merely asymptotic. Equation (A) is a finite inequality and no longer contains the multiplicity-expanded spectrum. It couples Lamzouri's two previously separate nonnegative remainders so that off-line multiplicity cannot masquerade as horizontal screening.

## 5. Near-sharpness now forces genuine distinct-pair spectral collapse

Suppose along a sequence of finite configurations

\[
\Delta=o(N)
\tag{15}
\]

and, for some fixed `A,\delta>0`,

\[
D_{2,A}\ge\delta N.
\tag{16}
\]

Fix any `\tau>0`. The coefficient `4\min(\tau,A^{-2})` in (A) is positive, so (15)--(16) force

\[
D_{2,A}-A^2r_\tau(S)=o(N),
\]

which is (B).

Because `r_\tau(S)<=k`, this also yields the necessary distinct-pair count

\[
\boxed{
\liminf\frac{k}{N}\ge\frac{\delta}{A^2}.
}
\tag{17}
\]

For the transparent equal-depth case, suppose `K=pN+o(N)` off-line pair occurrences all have normalized depth `b>0`. Taking `A=b` gives `D_{2,A}=Kb^2`, so (B) yields

\[
\frac{r_\tau(S)}N\ge p-o(1).
\]

But `r_\tau(S)<=k<=K=pN+o(N)`. Therefore near-sharpness forces simultaneously

\[
\boxed{
K-k=o(N),
\qquad
\frac{r_\tau(S)}k\to1
\quad\text{for every fixed }\tau>0.
}
\tag{18}
\]

So an equal-depth near-extremizer cannot hide behind high multiplicity. Almost all off-line pair occurrences must be distinct, and essentially the entire Schur spectrum of those distinct pairs must collapse toward zero.

## 6. Relation to the exceptional complement

The refinement separates three populations more cleanly.

**Off-line multiplicity.** Multiplicity `m_j>1` creates exact zero modes only in the occurrence-expanded matrix, but (12) charges the same excess in `R_U`. Equation (A) removes those modes from the bootstrap invariant.

**Simple off-line pairs.** These are indexed by the positive-definite distinct-pair matrix `S`. If they retain density-scale bounded square depth while the baseline is sharp, a positive-density part of the genuine `S` spectrum must approach zero by (B).

**Critical-line multiplicity.** A real double creates no normalized odd coordinate and can still realize Lamzouri's zero-cost real-double equality pattern from WI-126. Equation (A) deliberately does not conflate that population with off-line screening. Real multiplicity above two is separately charged by `R_U`, but critical-line doubles remain a live exceptional branch.

Pure proof slack remains separate as well: if any of `R_B`, `R_M`, or the unused portions of `R_U,R_H` are extensive, then the baseline already has positive slack and no screening explanation is needed.

## 7. Prior-art and novelty audit

Literature-backed input is unchanged: Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1, supplies Proposition 2.1 and the conjugation-adapted Hilbert-space decomposition. The exact remainder decomposition and multiplicity formula are Mathia WI-126; the normalized odd Schur matrix is WI-132; the occurrence-expanded depth--spectrum rearrangement is WI-134.

The spectral facts used in (5)--(9) are standard finite-dimensional linear algebra: equality of the nonzero spectra of `AB` and `BA`, Loewner monotonicity, and the min--max principle. No novelty is claimed for them.

A targeted search around Lamzouri's new preprint, Schur complements, multiplicity, divided differences, and spectral stability found no external application combining the multiplicity slack with the occurrence-expanded Schur spectrum. Absence from that search is not evidence of priority and no priority claim is made. The durable line-specific deduction is only the exact coupling (A) and its consequence that the WI-134 macroscopic near-null sector can be taken on the **distinct-pair** Schur matrix.

## 8. Research implication

WI-134 left a bookkeeping loophole: its expanded matrix had exact multiplicity zero modes even though it correctly identified them as non-geometric. Equation (A) closes that loophole quantitatively. A near-extremal off-line population with bounded nonvanishing square depth must now create a macroscopic low-energy sector in a matrix that is positive definite at every finite stage and has one coordinate per distinct pair.

This sharpens the next source-side target. A successful arithmetic or nonharmonic-Fourier input need only rule out positive-density collapse of `r_\tau(S)` for the **distinct normalized divided-difference quotient**; it no longer has to disentangle automatic column repetitions. Conversely, a source-compatible countermodel to this bootstrap must produce genuinely many distinct off-line pair directions that become jointly almost contained in Lamzouri's retained space. Critical-line doubles remain outside this target and must still be handled by an independent simplicity mechanism.