---
id: CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary
type: research-clue
status: proposed
origin: master-researcher
target_line: weil_positivity
based_on:
  - research/prime_lattice/findings/PL-225-bost-connes-weak-completion-full-bh.md
  - research/prime_lattice/findings/PL-226-bost-connes-scalar-renormalization-gns-tail-obstruction.md
  - research/prime_lattice/findings/PL-227-bost-connes-lcm-conditioned-state-collapse.md
  - research/prime_lattice/findings/PL-228-bost-connes-coprimality-conditioned-unit-boundary.md
  - research/weil_positivity/findings/WP-215-bost-connes-state-hamiltonian-filters-can-encode-prime-powers-but-critical-weil-weights-force-sharp-half-holder-threshold.md
  - research/weil_positivity/findings/WP-216-bost-connes-critical-conditioning-forces-poisson-gcd-gram-but-weil-ray-is-indefinite-defect.md
---

# Can the critical Bost--Connes divisibility Gram be completed into the Weil sign without target coding?

## Observation

The earlier form of this clue asked whether the Bost--Connes fork contained any source-forced relation stronger than affiliation, scalar filtering, scalar corner renormalization, or canonical all-prime conditioning. `WP-216` now answers that selection question positively and changes the first unsupported implication.

The canonical range projections `E_n=mu_n mu_n^*` form the divisibility semilattice `E_m E_n=E_lcm(m,n)`, and every `KMS_beta` state fixes their masses by `phi_beta(E_n)=n^{-beta}`. At the actual Bost--Connes critical inverse temperature `beta=1`, normalized conditioned vectors therefore have the exact positive Gram kernel

`G_1(m,n)=gcd(m,n)/sqrt(mn)`.

On one prime axis this is the Poisson/Toeplitz kernel `p^{-|a-b|/2}`. The same source dynamics supplies the scale `log p`. Thus the critical half-density and prime logarithmic scale are no longer being inserted by an arbitrary `F(H)` or by a Borel selector.

The obstruction has moved one step downstream. `WP-216` identifies the local finite-Weil ray as

`W_p = log p (I-G_{1,p})`.

The source-forced object is a positive Gram kernel, while the required Weil orientation is its indefinite defect. The defect symbol changes sign, and the obvious scalar diagonal compensation has the same divergent all-prime cost already exposed by the earlier local threshold. Generic mixed-prime positive completions can restore positivity only by adding a further completion operation; positivity is not inherited from the critical conditional Gram itself.

Prime Lattice still supplies useful controls on false exits. In the standard positive-energy representation, bare prime-shift affiliation is maximally programmable; canonical scalar tail renormalization has no nonzero KMS-GNS limit; lcm conditioning either collapses fixed probes or reconstructs the original KMS state after blow-up; and coprimality conditioning lands on the classical unit boundary. Those controls no longer answer the live question, because `WP-216` has already produced an additional source relation that survives them.

## Research question

Is there a **source-forced global completion or orientation operation** on the critical Bost--Connes divisibility Gram that turns the local signed defects `log p (I-G_{1,p})` into the completed Weil form while preserving a genuine positivity/coercivity theorem and incorporating the archimedean and polar sectors?

The operation must be fixed before the desired Weil sign is read off. It may use mixed-prime incidence, modular/domain data, an unbounded or closable form, or a finite--archimedean coupling, but it must do more than add an arbitrary positive bath or encode the target coefficients through scalar spectral calculus. Source selection and the destination sign theorem are now separate obligations: the former has a concrete canonical carrier, while the latter remains unsupported.

This also sharpens the comparison with Prime Lattice. Shared Bost--Connes vocabulary is not evidence that the two lines should merge. A source-selection theorem can be meaningful even when the Weil sign is an additional target-sensitive theorem; conversely, if a proposed completion reduces exactly to a Prime-Lattice source relation plus a generic positivity construction, that reduction should be stated rather than counted as an independent mechanism.

## Why it may matter

`WP-216` is the first result in this fork that simultaneously source-forces the critical magnitude `p^{-k/2}` and the logarithmic prime scale without target-programmable scalar filtering. That is a materially stronger starting point than mere affiliation or thermodynamic midpoint heuristics.

The remaining gap is also unusually sharp. The desired finite-prime object is not a vaguely related kernel but the explicit indefinite complement of the canonical positive Gram. A successful completion would therefore have to explain exactly where the missing orientation and global sign come from. A negative theorem showing that every natural source-forced completion of this Gram either remains indefinite, pays a divergent compensation, or becomes target-programmable would close a substantial Bost--Connes positivity family.

## Decisive test

Choose one concrete completion of the critical Gram and specify its full defining data before using the Weil target: representation or GNS sector, form/operator domain, finite-prime coupling, mixed-prime operation if any, archimedean contribution, polar/zero-mode normalization, and the proposed positivity mechanism.

At finite prime level, require the construction to recover the actual off-diagonal coefficients `-log p p^{-|k|/2}` rather than merely the positive Poisson kernel. Track every diagonal compensation and prove whether its all-prime mass is finite in the same topology in which positivity is claimed. If mixed-prime terms are used, test them against product/affine controls that preserve the one-prime Poisson factors but have no Riemann-specific sign law. If an unbounded or modular form is used, show that its defining relation excludes arbitrary affiliated operators and target-coded `F(H)` interpolants.

Then add the archimedean and polar sectors and state the exact destination theorem. A positive outcome requires a source-derived completed form that is positive or coercive on the declared Weil test class without inserting the desired sign by hand. Kill the candidate if its only positivity comes from a freely chosen diagonal bath, if the required all-prime compensation diverges, if the mixed-prime completion is generic for matched product controls, or if the finite/archimedean coefficients are supplied by an interpolating scalar function chosen from the target.

The strongest useful negative result would classify a broad natural completion family and prove that the indefinite defect cannot be repaired within it at finite global cost. The strongest useful positive intermediate result would be a source-forced finite-prime-plus-archimedean form whose sign is proved on a nontrivial test cone even before the full Weil criterion is reached.

## Evidence boundary

`WP-216` does **not** prove Weil positivity, RH, or even positivity of the finite-prime defect. It proves a canonical critical Gram and identifies the desired local Weil ray as an indefinite defect of that Gram. The divergence of the obvious scalar repair does not rule out every mixed-prime, modular, adelic, distributional, or finite--archimedean completion.

The Prime-Lattice findings in `based_on` remain category-specific controls, not a theorem that every Bost--Connes or noncommutative-geometric route fails. In particular, `PL-225` concerns the standard positive-energy representation and cannot be extended by assertion to all KMS GNS sectors. `PL-226`--`PL-228` classify specific canonical limits and conditionings, not every relational completion.

No source-forced sign-reversing operation, archimedean completion, or positive Weil form is established here. This clue records the new falsification surface created by `WP-216`; it is not evidence for portfolio promotion, line consolidation, or an RH consequence.