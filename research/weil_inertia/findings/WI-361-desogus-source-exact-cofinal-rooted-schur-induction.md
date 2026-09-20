# WI-361 — Desogus supplies a source-exact cofinal rooted-Schur candidate that targets the live localization gate

**Status:** `RECENT-PREPRINT + PRIMARY-SOURCE-AUDIT + PRIOR-ART-REDIRECT + CLAIMED-RH + NEEDS-INDEPENDENT-AUDIT + NEEDS-CERTIFICATE-REPLAY + NON-ESTABLISHED-RH`.

## Claim

Marco Desogus's 17 September 2026 preprint **The Three Gates: A Rooted-Operator Approach to Weil Positivity** (`arXiv:2609.20367`) claims a proof of RH by proving non-negativity of the localized critical Weil operator in the real odd logarithmic channel for every finite support radius. Mathia does **not** accept the RH conclusion as established evidence at this stage.

The preprint is nevertheless a material prior-art redirect for the current `weil_inertia` program because its Gate II architecture attacks almost exactly the obstruction left open by WI-359 and WI-360. It does not replace the omitted arithmetic/exterior information by a scalar norm envelope or by a fixed compact repair. Instead it claims to retain simultaneously

- the exact prime-power translation/source channels;
- the full noncompact Cauchy--Carleman/exterior reserve;
- a common-complement multi-source short designed to prevent double spending of that reserve;
- the physical polar rank-one channel in the true nested metric;
- and a rooted Schur induction whose scalar debit is closed by a finite interval certificate plus an analytic tail.

Thus the research priority changes in a precise way: **before inventing another source-exact cofinal propagation mechanism, audit and independently replay the load-bearing common-cut/Schur/certificate chain in this preprint.** If that chain survives, it would supply the kind of defect-elimination mechanism the canonical mandate asks for. If it fails, the failure should identify a substantially narrower obstruction than the generic barriers already recorded in WI-358--WI-360.

The mathematical mechanism belongs to Desogus's preprint, not to Mathia. This finding records the exact claimed bridge, its relation to the existing local no-go results, the parts that can already be checked independently, and the remaining decisive audit gates.

## 1. Exact theorem surface claimed by the preprint

Let `A_a` denote the localized odd Weil operator in the physical logarithmic coordinate on `(-a,a)`. Desogus's Theorem 0.1 claims

\[
A_a\succeq 0
\qquad\text{for every }a>0.
\tag{1}
\]

The paper then uses the real-odd restricted Weil criterion to conclude RH. Its Theorem 1.2 states

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\mathcal W[f]\ge0
\quad
(f\in C_c^\infty(\mathbb R),\ f\text{ real and odd}).
}
\tag{2}
\]

The reduction from a cofinal set of support radii to all finite radii is based on the exact zero-extension compression

\[
E_{a,b}^{*}A_bE_{a,b}=A_a
\qquad(0<a<b),
\tag{3}
\]

so positivity on any unbounded sequence of radii implies positivity on every finite radius.

The computationally closed part of the claimed induction is summarized by the paper through the scalar reserve

\[
g_k^{M+}
=
\frac12+\log k
-
\frac{439}{250\log2}\sum_m V_{k,m}
-
\frac52 W_k,
\tag{4}
\]

which is claimed to satisfy

\[
\boxed{g_k^{M+}>0\qquad(k\ge7).}
\tag{5}
\]

The preprint states that the finite interval sweep reaches `k=3,594,641`, with an overlapping analytic tail for all larger `k`, and that the induction starts from an interval-certified base at `Y=7`. These numerical/certificate claims have **not** been independently replayed by Mathia.

## 2. The restricted odd criterion is not the problematic gate

The proof of (2) can be reconstructed independently from the spectral side of Weil's form. Write centered zeros as

\[
\lambda=\rho-\frac12.
\]

For a real odd logarithmic test with bilateral Laplace transform `F`, one has

\[
F(-z)=-F(z),
\qquad
F(\bar z)=\overline{F(z)},
\tag{6}
\]

and the spectral contribution may be written as

\[
\mathcal W[f]
=
\sum_\lambda
F(\lambda)\overline{F(-\bar\lambda)}
=
-\sum_\lambda F(\lambda)^2.
\tag{7}
\]

If RH holds, every centered zero is imaginary and each term in (7) is nonnegative.

Conversely, suppose an off-line centered zero `\lambda_0` exists. Choose a real even compactly supported smooth bump `\psi` whose Laplace transform `\Psi` is nonzero at `\lambda_0`. Kill every non-target zero below a fixed height by a real even polynomial `P_T`, and use

\[
F_M(z)
=zP_T(z)R_M(z)\Psi(z)^M
\tag{8}
\]

with a real even polynomial `R_M` of degree at most two chosen so that `F_M(\lambda_0)=1`. Paley--Wiener/Fourier decay on the closed critical strip makes the contribution of all zeros above the fixed height tend to zero as `M\to\infty`. The target off-line quartet contributes `-4m(\lambda_0)` (or `-2m(\lambda_0)` in the degenerate real-pair case). Hence positivity on the real-odd test core excludes every off-line zero.

This part is an exact orbit-isolation argument and is consistent with the line's own distinction between density-one information and exclusion of every exceptional zero. It does **not** validate the preprint's positivity proof; it only confirms that the advertised final implication would indeed be strong enough if the operator estimate were established.

## 3. Why the architecture evades the local no-go results rather than contradicting them

WI-359 shows that a first-zero-mode equation plus a scalar graph-norm or `\|K_a\|` envelope cannot force cofinal continuation across prime thresholds. WI-360 then gives a sharper source-specific obstruction: after prime-power `8` activates, unit-window localization with the exterior Fourier tail dropped cannot be repaired by any fixed bounded compact operator.

Desogus's construction does not make either forbidden move. The arithmetic branches are routed as genuine translation/source intervals rather than replaced by a single scalar norm. The full-form Cauchy--Carleman transport and exterior reserve are kept in the primal form. The preprint explicitly warns that aggregating prime branches is not an ambient operator identity and introduces a simultaneous common-complement short so that several routed sources are minimized against the same reserve only once.

The claimed induction then keeps the polar channel in physical nested coordinates and uses a true-metric Schur/Feshbach recurrence. In the paper's notation the inherited response is placed in the same post-old-core/common-cut primal form as the arithmetic mismatch and folded scalar debit. This is precisely the kind of source-shape information that WI-359 identified as missing from scalar-envelope propagation.

Similarly, WI-316 shows that merely proving an asymptotically exact cofinal scalar cap would already be essentially RH-complete. Desogus does not claim such a soft cap. Its proposed extra structure is an explicit recursive source decomposition with a fixed positive reserve at every integer stage, closed by the MASTER bound (4)--(5).

Therefore the new preprint is not evidence against WI-359, WI-360, or WI-316. It is a candidate construction that attempts to pass through the narrower corridor those findings left open.

## 4. The load-bearing Gate II chain

The primary source audit isolates four dependencies that must all survive before the claimed RH theorem can enter the evidence base.

### 4.1 Coherent multi-source shorting

Theorem 6.20 and the later residual-capacity refinement claim a lower bound for several disjoint source intervals after taking **one common complement infimum**. The conceptual point is important: source-free pieces, mean-zero source interactions, endpoint pieces, and the common extension must reconstruct the missing complement charge without assigning the same positive reserve independently to several sources.

This is the first place where an apparently valid collection of one-source estimates could fail by double counting. The theorem must therefore be rederived directly from the full quadratic form, with every source-source and source-complement cross term tracked before the infimum is taken.

### 4.2 True-metric rooted Schur bookkeeping

The claimed nested Schur identity has the form

\[
\delta_{k+1}
=
\delta_k^{Q}
-
\frac{2|z_k|^2}{\Pi_k},
\tag{9}
\]

with a Green representation that rewrites the debit as the negative metric energy of the inherited response. The subsequent fold/common-cut argument is supposed to place the parent-ground debit, the arithmetic mismatch, the aligned forcing, and the transverse reserve in one common primal geometry before minimization.

The decisive issue is not the algebra of a scalar Schur complement in isolation. It is whether the same physical reserve is used exactly once after all gauges, folds, source shorts, and inherited responses are put into the common metric. Lemmas 8.1/8.4 and Theorem 8.5 are therefore load-bearing, not cosmetic bookkeeping.

### 4.3 Certified base at `Y=7`

The induction starts from a computer-assisted interval certificate for the localized odd operator at the endpoint `Y=7`. The paper describes a finite low-mode block, a rigorously controlled complement, interval preconditioning, and a final small Hermitian interval matrix.

Mathia has not replayed this certificate independently. A successful replay must reconstruct the matrix and all complement bounds from the declared analytic formulas and verify positive definiteness with outward rounding; reproducing only printed decimal margins is insufficient.

### 4.4 MASTER finite sweep and analytic tail

The cofinal step additionally depends on the global positivity of (4). The paper claims an outward-rounded finite sweep through `3,594,641` and an analytic continuation of the estimate beyond that cutoff. The finite and analytic regions overlap.

This should be replayed independently from the supplementary artifact (`10.5281/zenodo.22799713`) with a separate implementation or interval stack. The required output is not merely a matching minimum: the audit must confirm that the computed `V_{k,m}` and `W_k` are exactly the quantities entering the proved Gate II inequality and that the analytic tail uses the same normalization.

## 5. What has and has not been checked

The following pieces survive a first independent mathematical pass:

- the real-odd restricted Weil criterion (2) has a direct orbit-isolation proof;
- the zero-extension strategy is structurally compatible with the localized explicit formula: the singular exterior-harmonic change is cancelled by the endpoint potential, old arithmetic branches are unchanged on the old support, and newly activated translations have no old--old overlap before their activation threshold;
- the claimed architecture genuinely retains the kinds of noncompact/source-exact information that WI-359--WI-360 say a viable continuation argument must retain.

None of those observations proves Gate II. No independent reproduction of the base certificate, finite MASTER sweep, or analytic tail has been completed here, and no independent end-to-end verification of the common-source short or the no-double-spend Schur placement has been completed. No established theorem of RH is therefore recorded.

A search for immediate public follow-up located the fresh arXiv submission and mirrors of its abstract, but no independent mathematical validation or published referee report. Absence of a critique two days after submission is not evidence for correctness.

## 6. Prior-art and novelty assessment

The preprint is primary prior art dated 17 September 2026 and is newer than the local WI-359--WI-360 frontier. No existing `weil_inertia` finding or source anchor mentioned Desogus before this audit.

Mathia makes **no novelty claim** for the source-exact common-cut, rooted Schur, restricted-odd, or MASTER mechanisms. The durable Mathia contribution of this finding is the program-level audit result:

\[
\boxed{
\text{the exact source/noncompact corridor left open by WI-359--WI-360 now has a concrete claimed construction,}
}
\tag{10}
\]

and its validity can be reduced to a small number of explicit proof/certificate gates instead of being treated as an unspecified future mechanism.

This is a prior-art redirect, not an endorsement of the preprint's main theorem.

## 7. Decisive audit / falsification test

The candidate mechanism should be accepted into the established evidence base only if all of the following succeed independently:

1. rederive the simultaneous common-cut/source-capacity inequality from the full localized form and verify that every positive reserve is charged at most once;
2. reconstruct the true-metric rooted Schur recurrence through the fold/aligned-forcing step and verify the exact placement of the inherited response;
3. independently replay the `Y=7` interval base certificate with outward rounding from the declared analytic inputs;
4. independently replay the finite MASTER sweep and its analytic tail, including the overlap and normalization bridge;
5. verify that the cofinal integer-endpoint positivity passes through the exact zero-extension compression and closed-form limit without a domain change.

A failure of any one gate blocks the RH conclusion. Conversely, if these gates survive, the result would be qualitatively stronger than another improvement of the simple-critical-zero proportion: it would provide the canonical line's required individual-exception elimination mechanism.

## Consequence for the research line

Until the audit is resolved, the established `weil_inertia` evidence is unchanged: no proof of RH is imported. The practical frontier does change. The highest-value next work is no longer a generic search for some way of combining source-exact arithmetic with noncompact reserve; it is an adversarial reconstruction of the particular common-cut/rooted-Schur mechanism now claimed in the literature, together with an independent certificate replay.

If that mechanism fails, the exact point of failure should be compared against WI-359--WI-360 to decide whether it exposes a new no-go theorem. If it survives, the line should promote only the independently verified components and then assess the full RH implication.