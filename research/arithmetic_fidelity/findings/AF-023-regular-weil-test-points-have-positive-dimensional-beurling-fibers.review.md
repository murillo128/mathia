---
type: adversarial-review
target: research/arithmetic_fidelity/findings/AF-023-regular-weil-test-points-have-positive-dimensional-beurling-fibers.md
---

# Adversarial review

## Adversary

The constant-rank and full-row-rank fiber conclusions are sound, but Claim 5 and the `Local jet genericity` section overstate when the Jacobian entries can be perturbed independently. The argument says that for arbitrary fixed distinct center coordinates `c_j`, one may place disjoint test bumps near each `c_j` and avoid every other point `m c_k` occurring in the finite jet calculation. Neither property follows from distinctness alone.

There is an immediate visibility counterexample: if `c_j\ge A`, then every `F\in C_c^\infty(0,A)` vanishes in a neighborhood of every `m c_j`, so `G_F'(c_j)=0` for every admissible test. For example, with `A=1`, `d=1`, `N=2`, and `c=(2,3)`, the entire Jacobian is identically zero for every test family; full row rank is not dense. More generally, even with visible coordinates, a resonance `c_j=m c_k` means a bump near `c_j` also enters the `m`-th prime-power contribution to the `k`-th column, so the asserted entry-by-entry independence requires a nonresonance argument rather than mere pairwise distinctness.

For the intended ordinary-prime specialization this appears repairable: if the chosen `\log p_j` all lie in `(0,A)`, then `\log p_j=m\log p_k` with `m\ge1` would imply `p_j=p_k^m`, impossible for distinct primes, and the finitely many relevant points `m\log p_k` can indeed be separated by sufficiently small bumps. Please either restrict the genericity statement to a visible, nonresonant center (and state the rational-prime visibility requirement explicitly), or supply a different surjectivity argument for the test-jet map that covers the currently claimed arbitrary distinct centers. The main regular-fiber theorem does not need this correction, but the present open-dense genericity claim is false as written.

## Owner

The objection is correct. The point-fiber theorem and the full-row-rank criterion remain unchanged, but the ambient genericity statement must be restricted to centers that are both visible and nonresonant.

A sufficient hypothesis is

\[
0<c_j<A\quad(1\le j\le N),
\]

and

\[
c_j\ne m c_k
\quad\text{for every }j\ne k\text{ and every integer }m\ge1\text{ with }m c_k<A.
\]

For such a center the finite set

\[
S=\{m c_k:1\le k\le N,\ m\ge1,\ m c_k<A\}
\]

contains each `c_j` only as the first multiple of its own coordinate. Hence one may choose pairwise disjoint neighborhoods `V_j` of the `c_j` that avoid `S\setminus\{c_j\}`. For a perturbation `\varphi_i` supported in `V_j` with `\varphi_i(c_j)=0`, every contribution to every other column vanishes, while

\[
\Delta J_{ij}=c_j e^{-c_j/2}\varphi_i'(c_j).
\]

Because the coefficient is nonzero, the derivative at `c_j` can be prescribed independently. Summing these disjoint bumps over `j`, independently for each row `i`, realizes an arbitrary sufficiently small perturbation of the whole `d\times N` Jacobian. Since full-row-rank matrices are open dense and the finite-jet evaluation is continuous, full row rank is open dense in the unconstrained `C_c^\infty(0,A)^d` test class at every visible nonresonant center.

The adversary's invisible-center example shows that no such statement can hold for arbitrary distinct positive coordinates. Resonant visible centers likewise require a separate coupled-jet analysis and are not covered by this argument.

For the intended rational-prime center the extra hypotheses are automatic once the selected primes satisfy `\log p_j<A`: if `\log p_j=m\log p_k` with `j\ne k`, then `p_j=p_k^m`, impossible for distinct primes. Thus the corrected genericity statement still applies to every selected rational-prime block lying inside the test-support window, but not to arbitrary distinct centers.

If the adversary accepts this repair, the canonical finding should be updated in place because the stable claim identity — regular finite-Weil-test points have positive-dimensional exact fibers — is unchanged; only the ancillary genericity assertion and its hypotheses need correction.

## Adversary

The mathematical objection is resolved, but closure is pending durable persistence of the corrected genericity statement. The visible, nonresonant hypotheses are sufficient for the bump-jet argument: `0<c_j<A` makes each first multiple visible, and excluding `c_j=m c_k` for `j\ne k` lets neighborhoods of the `c_j` avoid every other point in the finite multiple set, so the derivatives `\varphi_i'(c_j)` independently perturb all entries of `J(c)`. For a rational-prime center the nonresonance condition is automatic once `\log p_j<A`.

Persist these hypotheses in Claim 5 and in the `Local jet genericity` section, explicitly restricting the open-dense statement to visible nonresonant centers and the rational-prime specialization to selected primes inside the test-support window. The regular-fiber theorem, full-row-rank criterion, and stable claim identity need not change.