# PL-233 — Full prime-permutation symmetry collapses every normal state to the vacuum and forbids interacting Gibbs repair

## Claim

Let

\[
\mathcal H_{\mathrm{int}}
=\ell^2\!\left(\mathbb N_0^{(\mathcal P)}\right)
\cong \ell^2(\mathbb N)
\]

be the integer occupation Hilbert space, with basis `e_alpha` indexed by finite-support prime-exponent vectors and vacuum `e_0=e_1`. Let `S_fin(P)` be the group of finite permutations of the prime coordinates, acting unitarily by

\[
U_\pi e_\alpha=e_{\pi\alpha}.
\]

Then every positive trace-class operator `T` satisfying

\[
U_\pi T U_\pi^*=T
\qquad(\pi\in S_{\mathrm{fin}}(\mathcal P))
\]

is supported only on the vacuum:

\[
\boxed{T=cP_0,\qquad c\ge 0,}
\]

where `P_0=|e_0><e_0|`. Consequently the **unique prime-permutation-invariant normal state** on `B(H_int)` is the vacuum state.

In particular, let `H` be any self-adjoint Hamiltonian on `H_int` that is invariant under every finite prime permutation in the strong sense that the unitary symmetry preserves its domain and commutes with `H`. The Hamiltonian may be non-diagonal and may contain arbitrary interactions among exponent coordinates. If for some finite `beta>0` the Gibbs operator `exp(-beta H)` were trace class, functional calculus would make it a positive prime-permutation-invariant trace-class operator. The classification above would force

\[
e^{-\beta H}=cP_0.
\]

But `e^{-\beta H}` is injective because the scalar function `e^{-\beta x}` never vanishes on the real spectrum of a self-adjoint operator, whereas `P_0` annihilates every non-vacuum vector. Hence

\[
\boxed{
\text{no fully prime-permutation-symmetric self-adjoint Hamiltonian on }\mathcal H_{\mathrm{int}}
\text{ has a normal finite-temperature Gibbs state.}
}
\]

This strictly strengthens `PL-232`: the obstruction is not a peculiarity of additive diagonal energies. **Nonadditive interactions cannot repair the Gibbs problem while exact full prime-coordinate permutation symmetry is retained in the same finite-support integer representation.**

**Evidence/status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

## 1. Every non-vacuum exponent vector has an infinite symmetry orbit

The vacuum `0` is fixed by every coordinate permutation. Now let `alpha != 0`. Its support is finite, so choose a prime `p` with `alpha_p>0`. There are infinitely many primes `q` outside `supp(alpha)`. For each such `q`, let `pi_q` exchange `p` and `q` and fix every other prime. Then

\[
\pi_q\alpha
\]

has the same occupation multiplicities as `alpha` but carries the nonzero occupation `alpha_p` at the new coordinate `q`. Distinct choices of `q` give distinct vectors. Therefore

\[
|S_{\mathrm{fin}}(\mathcal P)\cdot\alpha|=\infty
\qquad(\alpha\ne0).
\]

This orbit fact is the only symmetry input required below. It is stronger than the equal-one-particle-energy argument in `PL-232`: it applies to arbitrary interactions and to any invariant positive density operator, without requiring a diagonal Hamiltonian.

## 2. Positive trace class plus an infinite orbit forces zero weight

Let `T>=0` be trace class and invariant under every `U_pi`. For any basis vector `e_alpha`, set

\[
d_\alpha=\langle e_\alpha,T e_\alpha\rangle\ge0.
\]

Invariance gives

\[
d_{\pi\alpha}
=\langle U_\pi e_\alpha,TU_\pi e_\alpha\rangle
=\langle e_\alpha,U_\pi^*TU_\pi e_\alpha\rangle
=d_\alpha.
\]

For a positive trace-class operator, the trace is the sum of its diagonal entries in any orthonormal basis:

\[
\operatorname{Tr}T
=\sum_{\gamma\in\mathbb N_0^{(\mathcal P)}}d_\gamma<\infty.
\]

If `alpha != 0` and `d_alpha>0`, the infinite orbit of `alpha` contributes the same positive number infinitely many times, contradicting finiteness of the trace. Thus

\[
d_\alpha=0
\qquad\text{for every }\alpha\ne0.
\]

Positivity now upgrades zero diagonal weight to zero operator action. Since

\[
d_\alpha
=\|T^{1/2}e_\alpha\|^2,
\]

we have `T^(1/2)e_alpha=0`, hence `Te_alpha=0`, for every non-vacuum basis vector. Therefore `T` vanishes on the whole orthogonal complement of the vacuum. Its only possible component is

\[
T=cP_0,
\qquad c=\langle e_0,T e_0\rangle\ge0.
\]

If `Tr T=1`, necessarily `c=1`. This proves uniqueness of the invariant normal state.

The classical diagonal shadow is equally stark: a probability measure supported on finite-support exponent vectors and invariant under all finite coordinate permutations must assign zero mass to every non-vacuum orbit, hence is the point mass at the zero vector. `PL-232`'s escape of a symmetric thermodynamic law to infinite-support configurations is therefore not an accident of independent geometric occupations; it is forced already by exchangeability plus normality on the finite-support representation.

## 3. Arbitrary symmetric interactions do not restore a Gibbs trace

Assume `H` is self-adjoint and strongly invariant under the finite prime permutations. By spectral functional calculus,

\[
U_\pi e^{-\beta H}U_\pi^*=e^{-\beta H}
\]

whenever the heat operator is defined as a bounded operator. If it were trace class, Section 2 would imply

\[
e^{-\beta H}=cP_0.
\]

For a self-adjoint `H`, however,

\[
\ker(e^{-\beta H})=\{0\}.
\]

Indeed the spectral multiplier `e^{-beta x}` is strictly positive for every finite real `x`; a self-adjoint operator does not acquire an `+infinity` spectral value that could turn a non-vacuum sector exactly off. Since `P_0` has kernel `e_0^perp`, equality is impossible on the nontrivial integer Hilbert space.

No diagonalization or additive decomposition was used. Terms coupling several coordinates, occupation-dependent energies, many-body potentials, or other nonadditive interactions are all covered provided the resulting self-adjoint Hamiltonian retains exact full finite-permutation symmetry of the prime coordinates.

This closes the explicit second boundary condition left open by `PL-232`. There, an interacting Hamiltonian was outside the additive Fock trace argument because interactions could in principle reorganize the equal-energy degeneracy. The present argument shows that reorganizing eigenvalues is irrelevant: **the obstruction occurs already at the level of any positive normal density operator commuting with the symmetry.**

## 4. Why completion can evade the theorem but the integer Hilbert space cannot

The proof depends simultaneously on two facts: every physical basis configuration in `H_int` has finite prime support, and every non-vacuum configuration therefore has an infinite orbit under coordinate relabelling. A nontrivial exchangeable equilibrium can instead live on a completed infinite-coordinate probability space, where almost every configuration may have infinite support. That is exactly the thermodynamic escape already visible in `PL-232`.

Such a state is not represented by a trace-class density matrix on `ell^2(N_0^(P))`. Operator-algebraic KMS states may likewise exist in non-type-I or non-normal representations. The theorem therefore does not conflict with Bost--Connes-type equilibrium theory; it identifies the representation change as a load-bearing ingredient rather than a cosmetic completion.

For the prime-lattice program this distinction matters. If full permutation symmetry is imposed before the rational norm `p -> log p` or another source-forced relation is introduced, then a nontrivial normal state must leave the integer occupation representation. Recovering zeta information after that move requires an independent argument showing that the completed/GNS structure retains rational-prime arithmetic rather than only generic exchangeable infinite-coordinate data.

## 5. Stress tests and exact boundaries

The result uses **positivity**. A general non-positive trace-class operator commuting with the permutation action is not classified here by the diagonal argument; density matrices and Gibbs heat operators are positive, so positivity is exactly available for the claimed application.

The result also uses **full finite-coordinate permutation invariance**. Symmetry under a subgroup with finite or otherwise controlled orbits, finite blocks of degenerate primes, or a source-forced relation that distinguishes coordinates is outside the theorem. This leaves the rational norm weights `log p`, finite degeneracy classes, and structured symmetry breaking available.

Finite-prime truncations are not obstructed: their orbits are finite and symmetric Gibbs density matrices exist normally. The obstruction appears only after the countably infinite prime set is retained inside the finite-support integer Hilbert space.

At zero temperature the vacuum projection is not forbidden. The statement concerns finite `beta` Gibbs operators, whose exponential spectral multiplier is strictly positive and hence injective. Likewise a deliberately singular limiting state or a non-normal KMS state is outside the conclusion.

Finally, the theorem is generic. Replacing rational primes by any countably infinite set of unlabeled occupation coordinates gives the same orbit/trace argument. This universality is a falsification control rather than evidence for RH: exact all-coordinate symmetry carries too little rational-prime structure to be a zeta-localization mechanism by itself.

A decisive check of the theorem is therefore finite and exact: (1) every non-vacuum finite-support configuration must have an infinite orbit; (2) invariance must make the positive diagonal coefficient constant on that orbit; (3) trace finiteness must force that coefficient to zero; (4) positivity must force annihilation of the corresponding basis vector; and (5) a self-adjoint heat exponential must be injective. Failure of any one step would invalidate the no-go. All five follow directly from the stated hypotheses.

## 6. Prior-art and novelty audit

The finitary infinite symmetric group, its unitary representations, exchangeability under finite permutations, and trace-class density operators are all classical subjects. A targeted search across infinite symmetric-group representation theory, exchangeable probability/quantum states, permutation-invariant density operators, and bosonic Fock equilibrium found broad ambient prior art but no reason to treat the orbit/trace lemma as a new theorem; **no novelty is claimed**. The proof is recorded because the exact specialization closes a live Mathia escape rather than because the underlying functional analysis is exotic.

`PL-232` already established the additive diagonal version through the bosonic partition product and identified nonadditive interactions as an open boundary. The present result is not another reformulation of that product: it removes additivity and diagonal structure entirely and classifies every invariant positive trace-class operator on the integer occupation representation. Its mathematical delta is precisely the closure of the interacting full-symmetry repair.

No analytic continuation, Euler product, zero divisor, or critical-line statement enters the proof. Accordingly the result supplies an obstruction to one operator-design route, not a positive RH mechanism.

## Consequence for the research line

After `PL-232`, the natural response was to ask whether a permutation-symmetric many-body interaction could retain all-prime channel compatibility while lifting the infinite additive degeneracy enough to recover a normal Gibbs state. It cannot. On the finite-support integer Hilbert space, **exact full prime-permutation symmetry itself**, not the particular additive Hamiltonian, is incompatible with any non-vacuum normal state and hence with every finite-temperature Gibbs density.

The surviving thermodynamic/operator route must therefore break at least one load-bearing hypothesis: introduce rational-prime/source-forced symmetry breaking before equilibrium evaluation, use only controlled finite symmetry blocks, or move to a non-normal/completed representation whose arithmetic fidelity is independently proved. Merely replacing `Omega(n)` by a more complicated prime-permutation-symmetric interaction is no longer a live escape.