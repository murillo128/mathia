---
title: "WP-437: Prime-ray heat restriction retains a noncompact limit, but vacuum-null energies cannot repair the Weil sign"
type: research-finding
status: verified
research_question: "Can a prime-ray restriction of the critical coanalytic heat energy evade the full-space Mosco collapse and repair the negative Weil defect after the regulator is removed?"
claim_strength: exact_failure_of_mosco_commutation_with_prime_ray_restriction_and_two_state_vacuum_null_positivity_no_go
scope: standard positive-energy Bost--Connes representation on ell2(N), a fixed prime-power ray, logarithmic half-density coanalytic coefficients, positive fractional heat, and additive nonnegative forms whose domain includes the vacuum and first prime state and whose vacuum energy is zero; not a no-go for nonadditive, globally constrained, cancellation-bearing, or finite--archimedean Weil completions
finding_id: WP-437
related_findings:
  - WP-436
  - WP-435
  - WP-432
  - WP-218
  - WP-216
  - WP-001
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-13
updated: 2026-10-13
tags:
  - weil-positivity
  - bost-connes
  - prime-ray
  - heat-regularization
  - mosco-convergence
  - operator-compression
  - vacuum-null
  - noncompact-limit
  - sign-obstruction
---

# WP-437: Prime-ray heat limits and vacuum-null positivity

## Precise result and evidence

**EXACT-DERIVED; NEGATIVE/LOCAL SIGN OBSTRUCTION.** On
\(\mathcal H=\ell^2(\mathbb N)\), take the canonical multiplicative shifts
\(\mu_p e_n=e_{pn}\), Hamiltonian \(He_n=(\log n)e_n\), and the minimal
coanalytic field
\[
 R_\kappa e_m=\sum_{r\mid m,\ r\ {\rm prime}}
                 \overline{a_{\kappa,r}}e_{m/r},
 \qquad a_{\kappa,r}=\frac{(\log r)^\kappa}{\sqrt r},
 \qquad \kappa\ge0.
\]
For \(\alpha>0\) and \(t>0\) let
\[
 B_t=R_\kappa e^{-tH^\alpha},\quad
 K_t=B_t^*B_t,\quad q_t(f)=\lVert B_tf\rVert^2.
\]
WP-435 proves that \(B_t\) extends compactly; WP-436 proves that
\(q_t\) **Mosco-converges to zero on the full Hilbert space**
as \(t\downarrow0\).

Fix a prime \(p\), write \(L=\log p>0\) and \(r=p^{-1/2}\), and let
\(\mathcal H_p=\overline{\mathrm{span}}\{e_{p^j}:j\ge0\}\).
With \(P_p\) its orthogonal projection, the restricted heat energies
\[
 q_{p,t}(f)=q_t(f)\quad(f\in\mathcal H_p),\qquad
 K_{p,t}=P_pK_tP_p|_{\mathcal H_p}
\]
have a **nonzero, noncompact** strong-operator and Mosco limit:
\[
 \boxed{\quad
 K_{p,t}\xrightarrow[t\downarrow0]{\rm strong}
 K_{p,0}=|a_{\kappa,p}|^2
       (I-|e_1\rangle\langle e_1|),\qquad
 q_{p,t}\xrightarrow{\rm Mosco}q_{p,0}.
 \quad}                                                     \tag{1}
\]
Consequently the restriction of the full-space zero Mosco limit differs
from the Mosco limit of the restricted forms:
\[
 \boxed{\quad(\operatorname{Mosco}\!-\!\lim q_t)|_{\mathcal H_p}
       =0\ne\operatorname{Mosco}\!-\!\lim(q_t|_{\mathcal H_p}).\quad} \tag{2}
\]
The convergence in (1) is not in operator norm.

Despite this genuinely noncompact restricted limit, no such energy
changes the wrong sign of the fixed Bost--Connes Weil defect
\(W_p=L(I-G_{1,p})\), whose Toeplitz Gram has entries
\(G_{1,p}(j,k)=r^{|j-k|}\) (WP-216/218).
On \(\mathrm{span}\{e_1,e_p\}\),
\[
 \left.(W_p+K_{p,t})\right|_{\{e_1,e_p\}}
 \ \widehat{=}\ 
 \begin{pmatrix}
  0&-Lr\\[-1mm]
  -Lr&|a_{\kappa,p}|^2e^{-2tL^\alpha}
 \end{pmatrix},
 \qquad t>0,                                               \tag{3}
\]
and at \(t=0\) the lower-right entry is \(|a_{\kappa,p}|^2\).
In every case,
\[
 \boxed{\det=-L^2r^2=-\frac{(\log p)^2}{p}<0.}                \tag{4}
\]
Thus the compressed Weil defect plus the entire heat family, including
its noncompact ray limit, is indefinite. The argument requires **neither
compactness nor essential-spectrum theory**.

More generally, let \(Q\) be **any nonnegative Hermitian quadratic form**
on a complex vector-space domain contained in \(\mathcal H_p\) and
containing both \(e_1\) and \(e_p\). If \(Q(e_1)=0\), then
\(W_p+Q\) is indefinite on the two-dimensional subspace they span.
This includes bounded, unbounded, compact, noncompact and merely
form-defined corrections, provided they are finite on these two
vectors, positive, additive to the unchanged \(W_p\), and vacuum-null.
It is not a statement about arbitrary globally assembled Weil forms.

## Exact ray calculation

Because the only prime divisor of \(p^j\) is \(p\),
\[
 B_t e_1=0,\qquad
 B_t e_{p^j}
  =\overline{a_{\kappa,p}}\,
    e^{-t(jL)^\alpha}e_{p^{j-1}},\quad j\ge1.              \tag{5}
\]
Different basis inputs in this ray have mutually orthogonal images.
Consequently
\[
 K_{p,t}e_1=0,\qquad
 K_{p,t}e_{p^j}
   =|a_{\kappa,p}|^2 e^{-2t(jL)^\alpha}e_{p^j},\quad j\ge1. \tag{6}
\]
For a fixed ray vector
\(f=\sum_{j\ge0}f_je_{p^j}\), dominated convergence gives
\[
 \|(K_{p,t}-K_{p,0})f\|^2
 =|a_{\kappa,p}|^4
   \sum_{j\ge1}(1-e^{-2t(jL)^\alpha})^2|f_j|^2
 \longrightarrow0.                                       \tag{7}
\]
But for every \(t>0\) the supremum over \(j\) of
\(1-e^{-2t(jL)^\alpha}\) is exactly one. Hence
\[
 \|K_{p,t}-K_{p,0}\|=|a_{\kappa,p}|^2>0.                   \tag{8}
\]
Since \(K_{p,0}\) is a nonzero scalar multiple of an infinite-rank
cofinite projection, it is not compact.

The Mosco assertion is also direct. If \(t_n\downarrow0\) and
\(f_n\rightharpoonup f\) in \(\mathcal H_p\), then for every fixed \(M\)
\[
 \liminf_n q_{p,t_n}(f_n)
 \ge |a_{\kappa,p}|^2\sum_{j=1}^{M}|f_j|^2.
\]
Let \(M\to\infty\) for the weak-liminf condition. For the recovery
condition take \(f_n=f\); dominated convergence in (6) yields
\(q_{p,t_n}(f)\to q_{p,0}(f)\). The same argument works along every
sequence \(t\downarrow0\). In contrast, the full-space recovery
vectors from WP-436 exploit infinitely many other primes and need
not remain in the fixed ray. They are not admissible recovery
sequences for the constrained ray problem. This is the exact reason
behind (2), not a contradiction with WP-436.

## A finite certificate independent of regularity

WP-216 gives \(W_p(j,j)=0\) and
\(W_p(0,1)=W_p(1,0)=-Lr\). By (5), the heat energy annihilates
\(e_1\) and its mixed entry with \(e_p\) is zero. Equations (3)--(4)
then follow. A real test vector \(e_1+\varepsilon e_p\) has combined
quadratic energy
\[
 -2Lr\,\varepsilon+
 |a_{\kappa,p}|^2e^{-2tL^\alpha}\varepsilon^2<0
\]
for sufficiently small positive \(\varepsilon\).
This is a literal two-coordinate counterexample for every \(t>0\),
including the limit \(t=0\).

For the general form claim, nonnegative sesquilinear forms satisfy
the Cauchy--Schwarz inequality
\[
 |Q(u,v)|^2\le Q(u,u)\,Q(v,v).
\]
Thus \(Q(e_1,e_1)=0\) forces \(Q(e_1,e_p)=0\) and the matrix of
\(W_p+Q\) on this span is
\[
 \begin{pmatrix}0&-Lr\\-Lr&Q(e_p,e_p)\end{pmatrix},
\]
with the same strictly negative determinant as (4). No bound on
\(Q(e_p,e_p)\) can fix the sign as long as it is finite and the
vacuum remains a null vector. This extends the older zero-diagonal
argument of WP-001 **to additive positive corrections** of a
zero-diagonal but nonzero-cross-term defect; the correction is
required to vanish at only the single vacuum state, not at every
ray basis state.

## Stress tests, novelty, and exact boundary

There are two distinct effects, and neither should be inflated
into a global Weil theorem. WP-436 closed the unscaled full-space
heat-limit route by zero Mosco relaxation, but explicitly did not
classify a constrained ray limit. Equations (1)--(2) settle that
remaining limit: a fixed ray retains a noncompact positive energy
even as the ambient variational limit is zero. WP-218 closed
*compact* additive repairs via negative essential Toeplitz
spectrum. Equations (3)--(4) close this **noncompact**
heat-ray survivor without needing the essential spectrum, under
the more structural assumption that the positive repair is
vacuum-null.

The ingredients are standard: the Bost--Connes prime shifts and
critical KMS Gram, the elementary Cauchy--Schwarz/null-vector
property of positive forms, diagonal strong convergence, and Mosco's
weak-liminf/strong-recovery definition. The classical operator and
variational anchors are already recorded in this line's SOURCES.md
(Mosco 1969; Bost--Connes 1995; Toeplitz theory through WP-218).
WP-001 already uses the elementary two-state obstruction for
the **unrepaired** finite Weil block. No general new theorem or
historical novelty is claimed; the line-specific contribution is
the exact mismatch between the global and ray-constrained
regularized limits, coupled with the vacuum-null sign certificate
for that newly surviving noncompact category.

Matched free-semigroup shift models with the same single-generator
ray algebra and parameter \(0<r<1\) obey the identical argument,
so this obstruction is not selective for rational primes.
The negative conclusion holds only if the unchanged \(W_p\)
is tested on a domain containing \(e_1,e_p\) and the added positive
form kills \(e_1\). A genuine global Weil test class may not admit
those two basis states separately; a finite--archimedean or
mixed-prime assembly may alter their cross term; a form may
couple/cancel the coanalytic and analytic sectors *before*
positivity; an independently source-selected form may charge
the vacuum or have a different domain. None of those categories
is classified here. In particular, (2) does not say Mosco
convergence never commutes with restriction, only that it does
not commute for this specific singular family and fixed ray.

Thus removing heat **after fixing a prime ray** supplies no
Weil sign theorem despite yielding a noncompact limit. A
surviving construction must modify the source-derived
off-diagonal defect or its global admissible domain, and
still derive the finite Mangoldt coefficients, archimedean
Gamma term, polar normalization and an independent sign law.

## References

- research/weil_positivity/findings/WP-436-critical-prime-heat-energy-mosco-collapse.md
- research/weil_positivity/findings/WP-435-fractional-heat-prime-field-schatten-phase-transition.md
- research/weil_positivity/findings/WP-432-coanalytic-prime-field-is-dense-but-nonclosable-at-critical-half-density.md
- research/weil_positivity/findings/WP-218-bost-connes-weil-defect-has-negative-essential-spectrum-stable-under-compact-completion.md
- research/weil_positivity/findings/WP-216-bost-connes-critical-conditioning-forces-poisson-gcd-gram-but-weil-ray-is-indefinite-defect.md
- research/weil_positivity/findings/WP-001-prime-local-positive-rays-cannot-be-weil-summands.md
- research/weil_positivity/clues/CLUE-bost-connes-affiliation-conditioning-boundary.md
- research/weil_positivity/SOURCES.md
