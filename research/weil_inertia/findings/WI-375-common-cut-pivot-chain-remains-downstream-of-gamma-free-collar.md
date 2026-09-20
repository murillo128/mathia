# WI-375 — the common-cut pivot chain remains downstream of the gamma-free collar

**Status:** `EXACT-DEPENDENCY-AUDIT + PRIMARY-SOURCE-CRITICAL-AUDIT + DECISIVE-REPAIR-BARRIER + NON-ESTABLISHED-RH`.

## Claim

The strengthened same-vector/common-cut machinery in Marco Desogus's *The Three Gates: A Rooted-Operator Approach to Weil Positivity* (`arXiv:2609.20367v1`) does **not**, as printed, provide a non-additive repair of the gamma-cancellation failure isolated in WI-368.

The reason is an exact dependency, not a size estimate. The common-cut source metric used in Theorem 6.53 is built from the gamma-free one-cell form

\[
\mathfrak b[u]
=\frac14\iint_{(0,1)^2}\frac{|u(x)-u(y)|^2}{|x-y|}\,dx\,dy
-\frac12\int_0^1\log(x(1-x))|u(x)|^2\,dx,
\tag{1}
\]

through the split

\[
\boxed{\mathfrak b=\mathfrak l_0+\mathfrak r,\qquad \mathfrak r\ge0.}
\tag{2}
\]

Theorem 6.53 then takes the common-complement short of this form and obtains the simultaneous source-ground/transverse lower model. Lemma 6.58 obtains the positive inherited pivot

\[
\boxed{P^{\rm ex}_{k,m}\ge \Pi_m^{(0)}>0}
\tag{3}
\]

by monotonicity of shorted operators from the same analytic one-defect lower form. Lemma 8.1's exact row identity and Theorem 8.5's final harmonic-graph coercivity subsequently use that already-positive pivot.

WI-368, however, proves that Lemma 5.2 does not transport the complete localized Weil form to the gamma-free form (1): the closed difference form reverses the off-diagonal sign used in the printed kernel cancellation, so the regular gamma channel survives in the true transported quadratic form. Therefore the lower-form order used to obtain (2)--(3) has not been proved for the corrected localized form.

The later same-vector identity is algebraically useful but conditional. It places the inherited response in the same Schur metric **after** a positive exact source metric and pivot have been supplied; it does not itself create the missing lower-form order. Thus the printed common-cut/Feshbach chain cannot currently be invoked to neutralize the inherited gamma negative sector identified in WI-371--WI-374.

This finding is deliberately narrower than saying that no rooted-Schur repair can work. A repaired proof could still exploit genuinely source-conditioned old--new coupling. But it must establish a corrected common-cut inequality directly for the true gamma-retaining form; the published positive pivot cannot simply be inherited from the gamma-free collar.

## 1. The upstream transport used by the paper is exactly the disputed step

Section 5 first proves the unsigned kernel identity

\[
\frac12\bigl(K_{\rm Cauchy}^{(A)}+K_{\rm Carl}^{(A)}\bigr)
=\frac1{2|u-v|}+A\rho(A|u-v|).
\tag{4}
\]

Lemma 5.2 then subtracts the explicit gamma kernel `A rho(A|u-v|)` and concludes that no regular-gamma kernel remains in the one-cell collar. Proposition 5.3 is invoked downstream as the transport of the complete quadratic form.

WI-368 independently polarized the closed difference form and showed that its off-diagonal operator kernel carries the opposite sign:

\[
-\frac12\bigl(K_{\rm Cauchy}^{(A)}+K_{\rm Carl}^{(A)}\bigr)
=-\frac1{2|u-v|}-A\rho(A|u-v|).
\tag{5}
\]

Hence the source transport reconstructs the gamma-retaining cross-kernel, not the gamma-free collar (1). No multiplication or endpoint term can remove that discrepancy because disjointly supported tests kill all diagonal cross-polarizations while the `rho` kernel remains nonzero.

The primary source itself makes the dependency explicit: equation (60) displays the exact localized operator with `-K_{gamma,a}`, while Lemma 5.2 is the step that claims this regular term is canceled in the collar used by the later CMC/common-cut estimates. There is no second independent cancellation inserted between Section 5 and the Section 6 common-cut construction.

## 2. Theorem 6.53 shorts `mathfrak b`, not the corrected gamma-retaining form

Lemma 6.51 defines

\[
\mathfrak l_0[u]
=\log2\,\|u\|_2^2
+\frac14\iint |u(x)-u(y)|^2\,dx\,dy,
\tag{6}
\]

whose operator is

\[
L_0=(\log2+\tfrac12)I-\tfrac12|\mathbf1\rangle\langle\mathbf1|,
\tag{7}
\]

and proves (2) by subtracting (6) from the gamma-free form (1). The proof of Theorem 6.53 then starts, for every common extension, from

\[
\mathfrak b[u]
\ge \mathfrak l_0[u]
+\left(\log\frac1{2\varepsilon_{k,m}}-d_0\right)
\sum_n\|Q_{k,n}f_n\|^2,
\tag{8}
\]

and only afterwards takes one common-complement infimum. Its output is

\[
\mathfrak C^{\rm short}_{k,m}
\succeq
D^{(0)}_{k,m}|_{\mathcal G_m}
\oplus\bigoplus_n\widehat L_{k,n}Q_{k,n}.
\tag{9}
\]

The no-double-spend algebra in this step is exact **for (1)**; this agrees with WI-362. What WI-368 changes is the input form. The corrected transport contains the surviving nonlocal gamma channel, and neither Lemma 6.51 nor Theorem 6.53 proves an analogue of (8) after that channel is restored.

This distinction matters because one cannot infer the corrected short by treating the missing gamma term as a harmless diagonal perturbation. WI-369--WI-373 show that the corrected gamma contribution has a genuine bulk spectral profile with extensive negative index. The required repair is operator-valued.

## 3. The positive inherited pivot is inherited from that same lower form

The dependency becomes completely explicit in Lemma 6.58. The paper defines `D^ex_{k,m}` as the exact source-ground metric after the simultaneous common-complement short and then shorts the mismatch space. It claims

\[
P^{\rm ex}_{k,m}\ge\Pi_m^{(0)}>0.
\tag{10}
\]

The proof is one sentence at the load-bearing point: the analytic one-defect lower form is an operator inequality on the whole one-cell space, so monotonicity of shorted operators preserves it through the common-complement short and the mismatch short.

That monotonicity principle is correct. The missing premise is the corrected lower-form inequality. The operator order being transported is the one generated from `mathfrak b >= L_0`; after WI-368, `mathfrak b` is not the complete transported localized Weil form. Therefore (10) is not presently a proved lower bound for the source-ground metric of the corrected form.

This is stronger and more specific than WI-370's scalar-budget obstruction. WI-370 ruled out the conservative repair that simply pays the sharp floor `-C_Gamma I` from the existing MASTER scalar reserve. The present finding rules out a different apparent escape: interpreting the paper's later non-additive common-cut/same-vector construction as if it had already replaced the invalid gamma-free lower model. It has not; its positive pivot is downstream of that model.

## 4. Lemma 8.1 is exact response placement, not a repair of the metric

Lemma 8.1 writes the surviving inherited-line quadratic form as

\[
\mathcal Q^{\rm red}_{k,m}(a)
=P^{\rm ex}_{k,m}|a|^2
-2\operatorname{Re}(\bar a\,\omega^{\rm ex}_{k,m})
+\mathcal Q^{\rm rest}_{k,m}
\tag{11}
\]

with `P^ex_{k,m}>0`. The exact Schur minimizer satisfies

\[
P^{\rm ex}_{k,m}a_m=\omega^{\rm ex}_{k,m},
\tag{12}
\]

so the source-coupling contribution is the negative energy in that same metric. This correctly prevents the comparator surplus from being counted as an unrelated positive term.

But (12) begins after positivity of `P^ex` has been supplied by Lemma 6.58. It says where the response debit lives; it does not prove that the corrected source metric dominates `D^(0)` or that its surviving pivot is positive.

Theorem 8.5 makes the dependence explicit again: its proof invokes Theorem 6.53 before the common-complement infimum, Lemma 8.1 on each parent ground block, Corollary 6.49 for the mismatch debit, and then the MASTER scalar certificate. Consequently the final implication

\[
A_{k,-}\succ0\Longrightarrow A_{k+1,-}\succ0
\tag{13}
\]

still requires the unproved corrected analogue of the Section 6 source metric. The same-vector formulation eliminates a possible bookkeeping error, but it does not bypass the Section 5 transport error.

## 5. What a genuine repair now has to prove

The next source-facing gate is no longer the abstract question "can a Schur mechanism be non-additive?". The paper already supplies exact Schur algebra conditional on its collar metric. The precise missing theorem is a corrected source-conditioned lower form.

A sufficient repair would be an inequality of the schematic form

\[
\mathfrak C^{{\rm short},\Gamma}_{k,m}
\succeq \widetilde D_{k,m}
\tag{14}
\]

for the common short of the **gamma-retaining** localized form, with enough information to show that after mismatch shorting the inherited pivot is positive and that the transverse block has the reserve consumed later by MASTER. It need not reproduce `D^(0)` exactly; a different operator lower model is allowed.

The burden is spectral rather than scalar. WI-373 gives the exact digamma negative-index profile for bounded additive repairs, while WI-374 shows that sufficiently late *fresh endpoint collars* are gamma-positive. Therefore the most plausible remaining mechanism is a genuinely source-conditioned old--new Schur coupling that transports the growing endpoint reserve into the inherited interior negative modes. To count as a repair it must be proved on the corrected form before the positive-pivot/response identities are used; importing (10) from the gamma-free metric would be circular.

A particularly sharp falsification test for this finding is straightforward: derive from the actual localized Weil form, retaining the gamma channel, an independent proof of `P^{ex,Gamma}_{k,m}>0` (or a stronger full source-ground lower model) that does not use Lemma 5.2's gamma-free cancellation. Such a result would reopen the same-vector MASTER route.

## 6. Primary-source and novelty audit

**Primary source.** Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, `arXiv:2609.20367v1`, submitted 17 September 2026, https://arxiv.org/abs/2609.20367. The load-bearing chain checked here is Lemma 5.2 / equations (59)--(61), Lemma 6.51 / equations (180)--(181), Theorem 6.53 / `MASTER-CUT`, Lemma 6.58 / equation (193), Lemma 8.1 / equations (198)--(199), and Theorem 8.5 / equations (213)--(214).

A fresh web audit on 20 September 2026 found the arXiv record still at `v1` and no public correction or independent technical discussion that supplies a gamma-retaining common-cut theorem. Search absence is not evidence of priority, and no priority claim is made.

**Internal dependencies.** WI-362 independently validated the common-cut/no-double-spend and inherited-response algebra *conditional on the normalized gamma-free one-cell form*. WI-368 later showed that the printed Section 5 cancellation does not establish that form for the complete Weil operator. WI-369--WI-373 quantified the corrected gamma debt and its negative-index profile; WI-374 localized that debt to inherited bulk rather than sufficiently late fresh endpoint collars. The new contribution here is the exact dependency audit showing that the apparent non-additive escape in Sections 6 and 8 still starts from the disputed gamma-free collar and therefore does not answer the corrected source-conditioned problem.

## Research consequence

The current Desogus v1 chain should no longer be searched for a hidden downstream payment of the gamma debt: the downstream positive source metric is constructed only after the debt has already been removed by the invalid Section 5 cancellation. The live branch is narrower and testable: rebuild Theorem 6.53/Lemma 6.58 for the corrected gamma-retaining form, or exhibit a new exact off-diagonal source identity upstream that genuinely cancels the surviving gamma channel.

This is a barrier to the printed proof and to using its current common-cut metric as a repair. It is not a proof that source-conditioned Schur coupling cannot work, and it is not a proof or disproof of RH.