---
title: "WP-436: Critical prime-field heat energies Mosco-collapse to zero despite divergent operator norms"
type: research-finding
status: verified
research_question: "Can removing a positive fractional-heat regulator recover a nonzero closed positive energy from the nonclosable critical coanalytic Bost--Connes prime field?"
claim_strength: exact_zero_mosco_and_strong_resolvent_limit_from_dense_graph_with_nonzero_fixed_vector_energies
scope: standard positive-energy Bost--Connes representation on l2(N); critical coanalytic prime fields with logarithmic half-density weights; unscaled positive fractional-heat norm-square forms; no claim about t-dependent renormalization, cancellation before squaring, constrained prime rays, other representations, or archimedean/global Weil completions
finding_id: WP-436
related_findings:
  - WP-435
  - WP-434
  - WP-433
  - WP-432
  - WP-218
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-12
updated: 2026-10-12
tags:
  - weil-positivity
  - bost-connes
  - fractional-heat
  - coanalytic
  - mosco-convergence
  - quadratic-forms
  - strong-resolvent
  - singular-limit
---

# WP-436: Removing heat collapses the critical positive energy in the Mosco topology

## Exact claim and evidence

**EXACT-DERIVED; NEGATIVE/VARIATIONAL-LIMIT OBSTRUCTION.** In the standard positive-energy Bost--Connes representation let
\[
\mathcal H=\ell^2(\mathbb N),\qquad
\mu_p e_n=e_{pn},\qquad H e_n=(\log n)e_n,
\]
and on the dense algebraic domain \(D=c_{00}(\mathbb N)\) define the coanalytic field
\[
R_\kappa e_m
 =\sum_{p\mid m}\overline{a_{\kappa,p}}e_{m/p},
\qquad a_{\kappa,p}=\frac{(\log p)^\kappa}{\sqrt p},
\qquad \kappa\ge0.
\tag{1}
\]
For any fixed \(\alpha>0\), set, initially on \(D\),
\[
B_t=R_\kappa e^{-tH^\alpha},\quad
K_t=B_t^*B_t,\quad q_t(f)=\|B_tf\|^2,\qquad t>0.
\tag{2}
\]
By WP-435 each \(B_t\) extends uniquely to a bounded compact operator on all of \(\mathcal H\), so \(K_t\) is bounded, compact, self-adjoint and positive, and \(q_t\) is a closed bounded nonnegative form with domain \(\mathcal H\).

**Nevertheless**, as \(t\downarrow0\),
\[
\boxed{q_t\xrightarrow{\mathrm{Mosco}}0
\quad\text{on }\mathcal H,\qquad
(I+\lambda K_t)^{-1}\xrightarrow{\mathrm{strong}}I
\quad\text{for every }\lambda>0.}
\tag{3}
\]
The limiting form is the zero form on the whole Hilbert space, **not** the nonclosable fixed-vector expression \(f\mapsto\|R_\kappa f\|^2\) on \(D\). Indeed, for every \(g\in D\),
\[
B_tg\to R_\kappa g,\qquad
q_t(g)\to\|R_\kappa g\|^2;
\tag{4}
\]
in particular, for every fixed prime \(p\),
\[
q_t(e_p)=|a_{\kappa,p}|^2e^{-2t(\log p)^\alpha}
\longrightarrow |a_{\kappa,p}|^2>0.
\tag{5}
\]
Thus the fixed-vector limit remains nontrivial even though every vector has arbitrarily close heat-dependent recovery vectors with vanishing energy.

The resolvent convergence is **not in operator norm**:
\[
\boxed{\big\|I-(I+\lambda K_t)^{-1}\big\|
=\frac{\lambda\|K_t\|}{1+\lambda\|K_t\|}
\longrightarrow1.}
\tag{6}
\]
WP-435 proves \(\|B_t\|\to\infty\), hence \(\|K_t\|=\|B_t\|^2\to\infty\). Both the strong/variational collapse and this norm obstruction are simultaneous; neither is an assertion of an RH-related positive sign.

## General dense-graph variational lemma and direct proof

The mechanism is independent of a special heat formula. Let \(D\) be a dense linear subspace of a Hilbert space \(\mathcal H\), and let \(R:D\to\mathcal H\) be linear with
\[
\overline{\operatorname{Graph}(R)}=\mathcal H\oplus\mathcal H.
\tag{7}
\]
Suppose \(B_t\) are bounded operators on \(\mathcal H\) satisfying \(B_tg\to Rg\) for every \(g\in D\) as \(t\downarrow0\). Then the nonnegative forms \(\|B_t\cdot\|^2\) Mosco-converge to zero and the resolvents \((I+\lambda B_t^*B_t)^{-1}\) converge strongly to \(I\) for every \(\lambda>0\).

To prove this, fix \(f\in\mathcal H\), \(\lambda>0\), and put
\[
u_t=(I+\lambda B_t^*B_t)^{-1}f.
\]
Because \(B_t\) is bounded, \(u_t\) is the unique minimizer over \(x\in\mathcal H\) of the strictly convex functional
\[
J_t(x)=\|x-f\|^2+\lambda\|B_tx\|^2.
\]
Consequently, for every \(g\in D\),
\[
0\le J_t(u_t)\le J_t(g)
\longrightarrow \|g-f\|^2+\lambda\|Rg\|^2.
\tag{8}
\]
By (7), the graph of \(R\) approximates \((f,0)\) arbitrarily closely: there are \(g_j\in D\) such that \(g_j\to f\) and \(Rg_j\to0\). Taking the limsup in (8) at fixed \(g_j\), then \(j\to\infty\), yields
\[
J_t(u_t)\to0.
\tag{9}
\]
In particular \(u_t\to f\) and \(\|B_tu_t\|\to0\), establishing strong resolvent convergence and a recovery family for **every** \(f\in\mathcal H\).

For completeness, the two Mosco conditions are immediate: if \(f_t\rightharpoonup f\), then \(\liminf q_t(f_t)\ge0\), the value of the candidate zero form at \(f\); for each \(f\), choose the just-constructed \(f_t=u_t\) (with \(\lambda=1\)) to obtain \(f_t\to f\) and \(\limsup q_t(f_t)=0\). This argument proves (3) **without** assuming a priori a general Mosco--resolvent equivalence or monotonicity of \(t\mapsto K_t\). It works along every sequence \(t\downarrow0\).

## Why the prime field satisfies the lemma

WP-432 establishes (7) for the critical coanalytic field \(R_\kappa\): the coefficient vector \(a_{\kappa,p}\notin\ell^2(\mathbb P)\), so the adjoint of \(R_\kappa\) has zero domain and the closure of its graph fills \(\mathcal H\oplus\mathcal H\). The divergence follows from the classical reciprocal-prime divergence, enhanced by \((\log p)^{2\kappa}\).

The second hypothesis is also exact. Since \(e^{-tH^\alpha}\) is diagonal and each basis vector \(e_m\) has only finitely many prime divisors, for every finitely supported \(g\) the action \(R_\kappa e^{-tH^\alpha}g\) is a finite sum and converges to \(R_\kappa g\). WP-435 separately supplies the crucial **boundedness of each \(B_t\)**, despite divergence of their norms as \(t\to0\). Therefore the lemma applies directly to (2).

This distinction is not a paradox: the limsup/recovery part of Mosco convergence permits the input \(f_t\) to vary with \(t\), whereas (4) holds for the fixed input \(g\). The recovery states may involve arbitrarily many prime coordinates and need not stay in a prescribed prime-power ray or any other fixed closed subspace. The claim is on the **full** \(\ell^2(\mathbb N)\), not on independently compressed rays.

## Sharp controls, boundaries, and Weil consequence

A finite-support prime coefficient vector is an instructive matched control. If \(a_p\ne0\) for only finitely many primes, then \(R_a=\sum_p\overline{a_p}\mu_p^*\) is bounded. The heat-preconditioned operators \(R_ae^{-tH^\alpha}\) tend strongly to \(R_a\) with a uniform bound; their positive energies tend strongly to \(R_a^*R_a\), and
\[
(I+\lambda K_t)^{-1}
\xrightarrow{\mathrm{strong}}
(I+\lambda R_a^*R_a)^{-1}\ne I
\quad (R_a\ne0).
\tag{10}
\]
Thus the zero variational limit is genuinely tied to the **maximal nonclosability/dense-graph** threshold, rather than to heat smoothing of every prime-shift model.

Equation (3) excludes recovering a **nonzero closed positive form by simply sending \(t\to0\)** in the unscaled canonical heat energies, despite (4). It does **not** rule out a \(t\)-dependent subtraction, an independently justified renormalization, bidirectional cancellations before taking a norm square, a different operator/GNS category, or a genuinely coupled finite--archimedean operation. It also does not claim that an isolated prime-ray compression has the same Mosco limit. For each fixed \(t>0\) the energy remains compact, and the unchanged negative essential prime-ray defect of WP-218 still cannot be repaired by adding its compact compression.

The source-specific geometry required by the canonical Weil-positivity mandate remains absent: there is no derived all-prime Mangoldt selector with its archimedean Gamma and polar counterparts, nor a global geometric sign theorem independent of the Weil target. This is a **local operator-category obstruction**, not a proof of RH or global Weil positivity.

## Prior art and novelty audit

Mosco's original 1969 convergence framework distinguishes weak lower bounds from strong recovery sequences. The regular/singular decomposition of nonnegative forms is classical (Hassi--Sebestyén--de Snoo, 2009), as is the theory of singular/closable linear relations (same authors, 2018). The variational lemma above is a short direct application of these familiar ideas and **is not claimed as a novel general theorem**. Its specific mathematical contribution to this research line is the zero-Mosco/strong-resolvent classification for the WP-432 critical field after the WP-435 fractional-heat regularization, including the nontrivial fixed-vector versus vanishing-relaxation mismatch and the failure of norm-resolvent convergence.

The same lemma applies to nonarithmetic Hilbert-space examples with dense graph and bounded algebraically convergent regularizers. Thus the collapse, by itself, has no arithmetic selectivity. Its usefulness here is to close the naive zero-heat-limit branch of the accepted Bost--Connes completion clue, **not** to promote a universal singular-form phenomenon into an intrinsic Weil sign mechanism.

## References

- research/weil_positivity/findings/WP-435-fractional-heat-prime-field-schatten-phase-transition.md
- research/weil_positivity/findings/WP-432-coanalytic-prime-field-is-dense-but-nonclosable-at-critical-half-density.md
- research/weil_positivity/findings/WP-433-thermal-coanalytic-prime-regularization-is-compact-and-sign-inert.md
- research/weil_positivity/findings/WP-218-bost-connes-weil-defect-has-negative-essential-spectrum-stable-under-compact-completion.md
- research/weil_positivity/clues/CLUE-bost-connes-affiliation-conditioning-boundary.md
- research/weil_positivity/SOURCES.md
