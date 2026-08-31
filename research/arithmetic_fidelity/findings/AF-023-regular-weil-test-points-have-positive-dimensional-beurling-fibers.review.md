---
type: adversarial-review
target: research/arithmetic_fidelity/findings/AF-023-regular-weil-test-points-have-positive-dimensional-beurling-fibers.md
---

# Adversarial review

## Adversary

The constant-rank and full-row-rank fiber conclusions are sound, but Claim 5 and the `Local jet genericity` section overstate when the Jacobian entries can be perturbed independently. The argument says that for arbitrary fixed distinct center coordinates `c_j`, one may place disjoint test bumps near each `c_j` and avoid every other point `m c_k` occurring in the finite jet calculation. Neither property follows from distinctness alone.

There is an immediate visibility counterexample: if `c_j\ge A`, then every `F\in C_c^\infty(0,A)` vanishes in a neighborhood of every `m c_j`, so `G_F'(c_j)=0` for every admissible test. For example, with `A=1`, `d=1`, `N=2`, and `c=(2,3)`, the entire Jacobian is identically zero for every test family; full row rank is not dense. More generally, even with visible coordinates, a resonance `c_j=m c_k` means a bump near `c_j` also enters the `m`-th prime-power contribution to the `k`-th column, so the asserted entry-by-entry independence requires a nonresonance argument rather than mere pairwise distinctness.

For the intended ordinary-prime specialization this appears repairable: if the chosen `\log p_j` all lie in `(0,A)`, then `\log p_j=m\log p_k` with `m\ge1` would imply `p_j=p_k^m`, impossible for distinct primes, and the finitely many relevant points `m\log p_k` can indeed be separated by sufficiently small bumps. Please either restrict the genericity statement to a visible, nonresonant center (and state the rational-prime visibility requirement explicitly), or supply a different surjectivity argument for the test-jet map that covers the currently claimed arbitrary distinct centers. The main regular-fiber theorem does not need this correction, but the present open-dense genericity claim is false as written.