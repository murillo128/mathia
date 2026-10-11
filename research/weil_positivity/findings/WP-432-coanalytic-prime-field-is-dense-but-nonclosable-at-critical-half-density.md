---
title: "WP-432: Coanalytic prime field is densely defined but nonclosable at critical half-density"
type: research-finding
status: verified
research_question: "Does taking prime-shift adjoints, or the positive form of their coherent sum, restore a valid critical Bost--Connes operator after the one-sided domain collapse of WP-431?"
claim_strength: exact_coanalytic_closability_threshold_and_dense_graph_no_go
scope: standard positive-energy Bost--Connes representation on l2(N); algebraic domain c00(N); coefficientwise adjoint field and its norm-square form; no assertion about mixed bidirectional cancellations or other GNS/archimedean completions
finding_id: WP-432
related_findings:
  - WP-431
  - WP-430
  - WP-268
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-10-11
updated: 2026-10-11
tags:
  - weil-positivity
  - bost-connes
  - coanalytic
  - prime-shifts
  - closability
  - quadratic-form
  - domain
  - no-go
---

# WP-432: Coanalytic prime field is densely defined but nonclosable at critical half-density

## Exact claim and status

**EXACT-DERIVED; NEGATIVE/OBSTRUCTION.** Let \(\mathcal H=\ell^2(\mathbb N)\), let \(c_{00}(\mathbb N)\) be its finite-support subspace, and let the canonical multiplicative isometries act by \(\mu_p e_n=e_{pn}\). For any complex prime coefficients \(a=(a_p)\), consider the *minimal coanalytic field*

\[
R_a=\left.\sum_{p\in\mathbb P}\overline{a_p}\,\mu_p^*\right|_{c_{00}(\mathbb N)}.
\]

This definition is valid and densely defined for **every** \(a\), because \(\mu_p^*e_n=e_{n/p}\) if \(p\mid n\) and zero otherwise; the sum is finite on every finitely supported vector.

The sharp dichotomy is

\[
\boxed{ R_a\text{ is closable }\iff a\in\ell^2(\mathbb P). }
\]

If \(a\notin\ell^2(\mathbb P)\), the stronger statement holds:

\[
\boxed{\overline{\operatorname{Graph}(R_a)}
       =\mathcal H\oplus\mathcal H.}
\]

In that regime the nonnegative quadratic form \(q_a(f)=\|R_af\|^2\), \(f\in c_{00}\), is **not closable** either. If \(a\in\ell^2(\mathbb P)\), both the operator and its norm-square form are closable (not necessarily bounded).

Thus the KMS half-density \(a_p=p^{-1/2}\) at \(\beta=1\), and the Weil-log-amplified \(a_p=(\log p)/\sqrt p\), have a dense algebraic domain but no closable Hilbert-space limit. Taking the adjoint of the collapsed one-sided field of `WP-431` restores domain *density*, not a viable closed source operator or positive energy.

## Proof by the exact adjoint domain

Use the convention that the inner product is linear in its first variable. Directly on basis vectors,

\[
R_ae_m=\sum_{p\mid m}\overline{a_p}\,e_{m/p}.
\]

For \(g\in\mathcal H\), the formal adjoint coefficient at \(m\) is

\[
(T_ag)(m)=\sum_{p\mid m}a_p\,g(m/p),
\qquad
T_a=\sum_p a_p\mu_p.
\]

Testing against all basis vectors shows

\[
R_a^*=T_a^{\max},
\]

where \(T_a^{\max}\) is the maximal coefficientwise Hilbert-domain operator defined and classified in `WP-431`. That finding proves

\[
D(T_a^{\max})=
\begin{cases}
\{0\}, & \sum_p|a_p|^2=\infty,\\
\text{a dense domain containing }c_{00}, & \sum_p|a_p|^2<\infty.
\end{cases}
\]

Since a densely defined operator is closable exactly when its adjoint has dense domain, this gives the claimed if-and-only-if criterion. In the non-square-summable case \(D(R_a^*)=\{0\}\); the orthogonal complement of the graph of \(R_a\) in \(\mathcal H\oplus\mathcal H\) is then zero, so its graph is dense in the whole product.

## Constructive falsification certificate

The failure does not depend on abstract adjoint theory. Given a finite set of primes \(F\) with \(S_F=\sum_{p\in F}|a_p|^2>0\), define

\[
x_F=\frac1{S_F}\sum_{p\in F}a_p e_p.
\]

Each \(x_F\) belongs to \(c_{00}(\mathbb N)\), and unique factorization gives

\[
\|x_F\|^2=S_F^{-1},\qquad R_ax_F=e_1.
\]

When \(a\notin\ell^2(\mathbb P)\), choose increasing finite \(F\) with \(S_F\to\infty\). Then \(x_F\to0\), \(R_ax_F=e_1\), and

\[
q_a(x_F-x_G)=0,\qquad q_a(x_F)=1.
\]

This is simultaneously a direct nonclosability witness for the operator and for its positive quadratic form.

The stronger dense-graph statement can also be checked constructively. Fix \(n\in\mathbb N\), choose \(F\) disjoint from the finite set of prime divisors of \(n\), and use

\[
x_F^{(n)}=\frac1{S_F}\sum_{p\in F}a_p e_{np}.
\]

Then \(\|x_F^{(n)}\|=S_F^{-1/2}\to0\), while

\[
R_ax_F^{(n)}=e_n+
\frac1{S_F}\sum_{q\mid n,\ q\ {\rm prime}}\overline{a_q}
                   \sum_{p\in F}a_p e_{(n/q)p}.
\]

Each inner sum has norm \(\sqrt{S_F}\), and only finitely many \(q\) divide \(n\); the remainder is therefore \(O_n(S_F^{-1/2})\to0\). Hence \((0,e_n)\) belongs to the graph closure for every \(n\). The closure is linear and closed, so it contains \(\{0\}\oplus\mathcal H\). Subtracting \((0,R_af)\) from the original graph point \((f,R_af)\) for each \(f\in c_{00}\), then closing, gives the whole \(\mathcal H\oplus\mathcal H\).

## Critical and matched controls

For the thermal family \(a_p(\beta)=p^{-\beta/2}\),

\[
\|a(\beta)\|_{\ell^2(\mathbb P)}^2=\sum_p p^{-\beta},
\]

which is finite exactly when \(\beta>1\). At \(\beta=1\), the classical divergence of \(\sum_p1/p\) therefore causes the coanalytic closability failure. Adding a factor \(\log p\) only increases this divergence. Away from the critical boundary (\(\beta>1\)), the same algebraic model *is* closable: this control shows that the statement is a sharp analytic threshold rather than a general indictment of prime shifts.

The operator-theoretic theorem applies equally to arbitrary coefficient families on a free multiplicative semigroup with the same fresh-generator geometry; hence it is **not** a Riemann-specific positivity theorem. No zeta zeros, RH assumption, Gamma normalization, or target-selected sign enter its proof.

## Prior art, novelty and boundaries

The Bohr--Hardy realization of \(\ell^2(\mathbb N)\) and the Bost--Connes shift/Hamiltonian background are classical (Hedenmalm--Lindqvist--Seip and the Bost--Connes literature already anchored in `SOURCES.md`). Fernández Vidal--Galicer--Sevilla-Peris (2025, DOI `10.5802/aif.3658`) study multiplier operators on Hardy spaces of Dirichlet series. The adjoint-domain and closable-form criteria used here are elementary standard operator theory. **No new general operator theorem or RH theorem is claimed.** The Mathia-specific mathematical delta is the exact failure of the apparently surviving *coanalytic adjoint plus positive energy* escape from `WP-431`, together with an explicit universal zero-input/nonzero-output certificate.

The conclusion is category-specific. It does **not** classify finite-prime truncations, bidirectional coherent sums with cancellations *before* positivity, renormalized/relative source forms, rigged/distributional realizations, nonstandard KMS-GNS representations, or genuine finite--archimedean couplings. A mere formally positive norm square cannot be treated as a valid Weil sign mechanism without a closable/source-forced domain and the missing global contributions.

## Consequence for Weil Positivity

`WP-431` removes the critical one-sided analytic prime field by triviality of its maximal Hilbert domain. `WP-432` removes the naive coanalytic reversal and its positive norm-square form on \(c_{00}\): the domain becomes dense but the graph becomes maximally nonclosable. A surviving mechanism needs a different, independently source-chosen coupling or completion that supplies a genuinely closed form and then recovers finite Mangoldt weights, Gamma/polar terms, and a sign theorem **independent** of RH.

## References

- `research/weil_positivity/findings/WP-431-critical-prime-coherent-semigroup-field-has-a-sharp-kms-domain-collapse.md`
- `research/weil_positivity/findings/WP-430-thermodynamic-naturality-forces-finite-gibbs-selectors-into-spectral-functional-calculus.md`
- `research/weil_positivity/clues/CLUE-bost-connes-affiliation-conditioning-boundary.md`
- `research/weil_positivity/SOURCES.md`
