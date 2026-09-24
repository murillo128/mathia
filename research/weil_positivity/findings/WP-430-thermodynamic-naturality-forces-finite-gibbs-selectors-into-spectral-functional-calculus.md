---
title: "WP-430: Thermodynamic naturality forces finite-Gibbs selectors into spectral functional calculus"
type: research-finding
status: verified
research_question: "Can thermodynamic data alone canonically select a coherent finite-Gibbs KMS sandwich that evades the WP-428/WP-429 boundary?"
claim_strength: exact_finite_control_no_go
scope: finite-dimensional Gibbs systems; selectors canonical under all thermodynamic source automorphisms, before using extra arithmetic intertwiners or the Weil target
finding_id: WP-430
related_findings:
  - WP-225
  - WP-405
  - WP-426
  - WP-428
  - WP-429
related_clues:
  - CLUE-bost-connes-affiliation-conditioning-boundary
created: 2026-09-24
updated: 2026-09-24
tags:
  - weil-positivity
  - bost-connes
  - kms
  - modular-dynamics
  - finite-control
  - naturality
  - no-go
---

# WP-430: Thermodynamic naturality forces finite-Gibbs selectors into spectral functional calculus

## Executive summary

`WP-429` shows that an unconstrained coherent finite-Bohr sandwich can realize an arbitrary faithful target state on a finite Gibbs truncation. The remaining question is whether the thermodynamic source itself can canonically select a nonzero-Bohr mixer before any target information is supplied.

At finite dimension there is an exact obstruction. Let `H=sum_j E_j P_j` and `rho_beta=Z^{-1}exp(-beta H)`. If a selector `B` is required to be canonical from the thermodynamic pair alone in the minimal sense that every unitary source automorphism preserving `H` also preserves `B`, then

`UHU*=H  =>  UBU*=B`

forces

`B in ({H}')'={H}''=C*(H)`.

Hence `B=sum_j b_j P_j=f(H)`: it is scalar on each energy eigenspace and has only zero Bohr degree. For a positive selector all `b_j>=0`. Such a sandwich preserves every Bohr frequency, so a Gibbs/KMS state still annihilates all nonzero-frequency components. Thermodynamic naturality therefore rules out exactly the coherent cross-frequency freedom that makes `WP-429` universal.

This is a finite-control no-go, not a no-go for the full Bost--Connes source. Extra arithmetic source structure can shrink the thermodynamic automorphism group and canonically distinguish noncommuting operators. The result says only that **thermodynamics alone cannot select the coherent mixer**. The full infinite system, a source-derived arithmetic selector, and the archimedean/polar completion remain open.

## Exact theorem

Let `H` act on a finite-dimensional Hilbert space and write its spectral resolution as

`H=sum_j E_j P_j`,

with distinct energies `E_j`. Let `rho_beta=Z^{-1}exp(-beta H)` for `beta>0`. Suppose `B` is an operator assigned from the thermodynamic source `(H,rho_beta)` and satisfies the local naturality condition

`UHU*=H  =>  UBU*=B`

for every unitary `U` on the source Hilbert space. Equivalently, this condition is forced by any globally unitary-natural assignment satisfying `B(UHU*)=U B(H) U*`.

Then

`B in C*(H)`.

In particular there are scalars `b_j` with

`B=sum_j b_j P_j`.

If `B>=0`, then `b_j>=0` for every `j`. Therefore `B` commutes with the Gibbs dynamics `sigma_t(A)=e^{itH}Ae^{-itH}` and has zero Bohr degree.

For every Bohr eigenoperator `A_omega` satisfying

`sigma_t(A_omega)=e^{it omega} A_omega`,

the sandwich `B* A_omega B` has the same frequency `omega`. Consequently every Gibbs/KMS state `phi_beta` obeys

`phi_beta(B* A_omega B)=0`

whenever `omega != 0`.

Thus no selector canonical from the finite thermodynamic pair alone can generate the coherent cross-frequency expectation needed to escape the strict Bohr-diagonal boundary of `WP-428`. The associated positive sandwich map is time-covariant, so the finite-control consequence is consistent with the broader time-covariant no-orientation theorem `WP-225`.

## Proof

The unitary stabilizer of `H` is exactly the unitary group of its commutant `{H}'`: every unitary `U in {H}'` satisfies `UHU*=H`. By naturality, `UBU*=B` for every such unitary, hence `B` commutes with every unitary in `{H}'`. In a finite-dimensional C-star algebra the unitaries linearly generate the algebra, so `B` commutes with all of `{H}'`. Therefore

`B in ({H}')'={H}''`.

Because `H` is normal with finite spectrum, its bicommutant is precisely the finite spectral functional calculus

`{H}''=C*(H)={sum_j b_j P_j}`.

This also proves the stronger statement hidden by degeneracies: thermodynamic naturality does not merely force `B` to commute with `H`; it forces `B` to be **scalar inside each degenerate energy block**. Positivity gives nonnegative spectral coefficients.

Now let `A_omega` have Bohr degree `omega`. Since `sigma_t(B)=B`,

`sigma_t(B* A_omega B)=B* sigma_t(A_omega) B=e^{it omega} B* A_omega B`.

A Gibbs state is invariant under `sigma_t`, so for all `t`,

`phi_beta(B* A_omega B)=e^{it omega} phi_beta(B* A_omega B)`.

If `omega != 0`, this forces the expectation to vanish. No nonzero-frequency compensation is produced.

## Bost--Connes finite-prime specialization

For the standard finite-prime positive-energy truncation, basis states are indexed by finite occupation vectors `a=(a_p)` and have energies

`E(a)=sum_p a_p log p = log(prod_p p^{a_p})`.

Unique factorization gives

`E(a)=E(a')  iff  a=a'`.

Thus the finite-prime Hamiltonian has simple spectrum in the arithmetic occupation basis. In this case `C*(H)` is literally the full diagonal algebra in that basis, and every thermodynamically natural selector is diagonal. It cannot supply a hidden coherent arithmetic mixer between distinct source energies.

This specialization is useful because it separates two notions that can otherwise be conflated. The Bost--Connes source contains arithmetic semigroup/intertwiner structure beyond `(H,rho_beta)`, but none of that extra structure is recoverable merely from thermodynamic naturality. A proposal using such an intertwiner must therefore identify it as additional source data and prove its own canonical selection law.

## Why this closes the thermodynamic-only escape after WP-429

`WP-428` classified strict Bohr-diagonal sandwiches and found that they preserve source degree, so they cannot orient the Bost--Connes finite Weil defect. `WP-429` then showed that removing that diagonal restriction completely makes the finite problem universal: a coherent sandwich can be chosen to realize any faithful target density matrix.

The present theorem resolves the source-selection question between those two extremes. If the only data allowed to select the mixer are the finite Hamiltonian and its Gibbs state, naturality under their own automorphisms forces the selector back into zero Bohr degree. Hence the coherent universality of `WP-429` is not a source-forced thermodynamic mechanism; to obtain a distinguished coherent mixer one must use additional non-thermodynamic source structure.

This also sharpens `WP-426`. There, choosing a modular/interacting dynamics after a desired faithful state is known was shown to be target-programmable. Here, even before changing the dynamics, choosing a coherent sandwich from thermodynamic data alone is impossible under the weakest naturality condition that forbids arbitrary basis choices inside source symmetries.

## Scope and matched control

The theorem is deliberately narrow. It does **not** say that every source-canonical Bost--Connes operator lies in `C*(H)`. The full source contains arithmetic endomorphisms and shifts that need not be invariant under every automorphism of the bare thermodynamic pair.

A matched escape is explicit. Enrich a finite Gibbs source by a distinguished noncommuting source operator `S`. Then a positive selector such as

`B=I+epsilon(S+S*)`

is allowed whenever `epsilon ||S+S*||<1`; it is source-defined from the enlarged tuple and can contain nonzero Bohr components. The stabilizer of `(H,S)` is smaller than the stabilizer of `H`, so the bicommutant argument no longer forces `B` into `C*(H)`. This is not a counterexample to the theorem: it identifies exactly which extra datum is required to escape it.

The same theorem holds for a generic finite Gibbs model with the same spectral multiplicities. Therefore the obstruction is a matched generic thermodynamic control, not an arithmetic signature of the Riemann source. Any arithmetic significance must enter through the extra source structure that survives this control.

## Evidence classification

**Result class:** unconditional proof in the stated finite-dimensional category.

**Hypothesis burden:** finite-dimensional Gibbs source; selector fixed from thermodynamic data alone; invariance under every unitary automorphism preserving that thermodynamic source. No Weil coefficient, desired sign, prime-power mask, or target state enters the selector definition.

**Proof dependence:** finite-dimensional commutant/bicommutant and spectral functional calculus, followed by KMS invariance of nonzero Bohr modes. No numerical evidence or asymptotic assumption is used.

**Theorem debt:** reduced but not discharged. The result removes the thermodynamic-only coherent-selector branch. It does not classify selectors canonically built from the full Bost--Connes arithmetic algebra, prove an infinite-volume/critical-domain statement, construct the Gamma or polar sectors, or prove positivity of the completed Weil form.

## Prior-art and novelty audit

No novelty is claimed for the algebraic fact that invariance under the full stabilizer of a finite normal operator forces membership in its spectral functional calculus. That is standard finite-dimensional operator algebra.

The new repository-level content is the exact application to the open selector gap left by `WP-428` and `WP-429`: the same thermodynamic naturality condition that makes a selector source-canonical also removes the coherent Bohr mixing that would be needed to exploit `WP-429` without target programming.

This is distinct from `WP-225`, which starts with time-covariant positive maps and proves that time covariance cannot orient the Bost--Connes Weil defect; it does not classify why thermodynamic source selection forces a sandwich map into that covariant class. It is distinct from `WP-428`, which studies a chosen Bohr-diagonal sandwich family, and from `WP-429`, which studies unrestricted coherent finite-Bohr sandwiches. It is also distinct from `WP-405`, whose fixed-point collapse uses a different analytic/gauge positivity hypothesis.

The internal novelty audit found no existing `weil_positivity` finding asserting this thermodynamic-stabilizer-to-spectral-functional-calculus classification. The result therefore advances the accepted Bost--Connes conditioning clue without claiming a new general operator-algebra theorem.

## Reproducibility

A minimal finite-prime check uses primes `{2,3}` and occupation cutoffs, for example `a_2 in {0,1,2}` and `a_3 in {0,1}`. The six energies are

`log(2^{a_2}3^{a_3})`,

and are pairwise distinct by unique factorization. Every diagonal phase unitary preserves `H`. Requiring `UBU*=B` for all such phases immediately kills every off-diagonal matrix entry of `B`, so `B` is diagonal. Sandwiching a matrix unit that changes energy by nonzero `omega` keeps it off-diagonal and its Gibbs trace is zero.

For a degenerate control, replace two equal-energy basis vectors by a two-dimensional energy block. The stabilizer then contains the full unitary group on that block. Invariance under all of it forces the corresponding block of `B` to be scalar, confirming the stronger `B in C*(H)` conclusion rather than only `[B,H]=0`.

## Implication

The live Bost--Connes branch is now more specific. A coherent finite-Gibbs mixer can matter only if it is selected by **extra arithmetic source structure that breaks the bare thermodynamic stabilizer**, not by `(H,rho_beta)` alone. Any proposed selector should therefore identify that extra datum before comparison with the Weil target and show that its selection survives matched generic controls.

Even a successful finite arithmetic selector would still have to pass the infinite-domain, critical-limit, archimedean/Gamma, polar normalization, and global positivity gates of the canonical research mandate.

## References

- `research/weil_positivity/findings/WP-225-time-covariance-alone-forbids-positive-orientation-of-bost-connes-weil-defect.md`
- `research/weil_positivity/findings/WP-405-pointed-analytic-gauge-positivity-collapses-to-fixed-points.md`
- `research/weil_positivity/findings/WP-426-state-selected-modular-dynamics-is-target-programmable.md`
- `research/weil_positivity/findings/WP-428-bohr-diagonal-noncommuting-kms-sandwiches-cannot-orient-bost-connes-weil-defect.md`
- `research/weil_positivity/findings/WP-429-coherent-kms-sandwiches-are-state-universal-on-finite-gibbs-truncations.md`
- `research/weil_positivity/clues/CLUE-bost-connes-affiliation-conditioning-boundary.md`
