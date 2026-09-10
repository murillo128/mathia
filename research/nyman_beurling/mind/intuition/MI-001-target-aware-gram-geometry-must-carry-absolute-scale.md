# MI-001 — Nyman progress requires source-specific graph energy in a scale-coupled quotient

**Evidence level:** exact target-aware Gram/semigroup reductions, visibility budget, multiplication-table sparsity, all-depth reciprocal kernel, and fixed-section deep-mixing asymptotic through NB-018

## Core intuition

The Nyman target supplies information that generator geometry alone does not, and the latest quotient analysis shows why this source dependence is unavoidable. The compressed dilation frame is never generically coercive: its blind modes have an exact multiplicative structure, so the remaining question is how the **actual residual field** sits relative to them as section and depth grow together.

This is a quantitative graph-energy problem rather than a search for a better source-independent frame constant.

## Strongest justified principle

NB-014--NB-015 express useful enrichment through the source-visible defect divided by compressed new-section frame cost and show that a nonzero limiting residual forces a summable scale-coupled budget. NB-016 identifies multiplication-table range and vanishing relative rank on the maximal `M=N` diagonal.

NB-017 gives the all-depth normal form. The quotient channel is a rooted multiplicative incidence graph; its invisible future pairings are exactly `q_k=a_C/k` on unrooted components, and rough cores guarantee a nontrivial kernel for every finite depth. Increasing `M` cannot restore full-space coercivity.

NB-018 solves fixed `N`, very deep `M`: periodic harmonic shells mix to one mean `mu_N`, producing explicit logarithmic visibility asymptotics. The convergence pays the exponentially large shell period `Lambda_N`, so this does not supply the polynomial scale-coupled estimate needed by NB-015.

## Program consequence

Prove source-specific lower control on the anchored multiplicative Dirichlet energy of `s_k=k<r_N,g_k>` relative to its quotient mass along one admissible growth path, with frame cost tracked in the same inequality. An anchored Poincare/expansion statement is useful only if it applies to this actual field and remains strong enough after summation.

## Counterevidence / boundary

Generic vectors can lie exactly in reciprocal blind sectors, and fixed-section eventual mixing occurs on the wrong depth scale. None of NB-016--NB-018 proves that the actual Nyman residual avoids approximate blind modes in the diagonal regime, nor do they improve the Nyman distance.

## Epistemic status

**Exact all-depth obstruction to generic coercivity plus a precise source-specific graph-energy target; no new closure or RH result is established.**

## Falsification criterion

Produce a finite depth with source-independent positive quotient coercivity contrary to NB-017, invalidate the reciprocal-component kernel, or show that the proposed source field can shadow those modes while still violating the claimed energy lower bound. A positive continuation should prove the scale-coupled source estimate itself.
