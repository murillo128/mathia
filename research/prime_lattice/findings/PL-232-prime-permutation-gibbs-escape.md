# PL-232 — Prime-permutation-symmetric lattice energy has infinite degeneracy and no normal finite-temperature equilibrium on the integer lattice

## Claim

The most intrinsic way to alter the `log p` dynamics after `PL-231` so that distinct prime directions are energetically degenerate is to forget the rational-prime labels and use the unweighted graph energy of the exponent lattice,

\[
H_{\Omega}e_n=\Omega(n)e_n,
\qquad
\Omega(n)=\sum_p v_p(n).
\]

More generally, let

\[
H_{\epsilon}e_n=E_{\epsilon}(n)e_n,
\qquad
E_{\epsilon}(n)=\sum_p v_p(n)\epsilon_p,
\qquad \epsilon_p>0,
\]

on the occupation-number Hilbert space `ell^2(N) ~= ell^2(N_0^(P))`. Then for every real `beta>0`,

\[
\boxed{
\operatorname{Tr}(e^{-\beta H_\epsilon})<\infty
\iff
\sum_p e^{-\beta\epsilon_p}<\infty.
}
\]

Equivalently, the bosonic Gibbs partition function is

\[
Z_\epsilon(\beta)
=
\prod_p\left(1-e^{-\beta\epsilon_p}\right)^{-1},
\]

with the product finite exactly under the displayed one-particle summability condition.

If the additive Hamiltonian is invariant under all finite permutations of the prime coordinates, then all one-prime energies are equal, `epsilon_p=c`. Consequently the one-particle level `c` already has infinite multiplicity, `H_epsilon` has noncompact resolvent, and

\[
\operatorname{Tr}(e^{-\beta H_\epsilon})=\infty
\]

for every finite `beta>0`. In particular the canonical coordinate-symmetric choice `H_Omega` has no normal finite-temperature Gibbs state on the Hilbert space whose basis is the positive integers.

There is an exact geometric version of the same obstruction. For finite prime sets `F`, the Gibbs law has independent geometric occupations

\[
\Pr(v_p=k)=(1-x_p)x_p^k,
\qquad x_p=e^{-\beta\epsilon_p}.
\]

The infinite product law is supported on the finite-support exponent lattice precisely when `sum_p x_p<infinity`. When that sum diverges, the formal product equilibrium on the completed product `N_0^P` has infinitely many occupied prime coordinates almost surely; it therefore assigns probability zero to the actual integer lattice `N_0^(P)`.

Thus there is a structural tension relevant to the escape left open by `PL-231`:

\[
\boxed{
\text{full prime-coordinate symmetry / all-prime energy degeneracy}
\Longrightarrow
\text{infinite degeneracy and escape from the integer Fock representation}.
}
\]

The rational norm energy `epsilon_p=log p` avoids the obstruction because `sum_p p^(-beta)<infinity` for `beta>1`; it does so precisely by breaking the abstract lattice's prime-permutation symmetry with prime-specific metric data. This does **not** characterize `log p`: many other growing energy sequences satisfy the same summability condition. It shows instead that an RH-relevant thermodynamic/spectral construction cannot obtain all-prime coupling merely by making the bare exponent directions energetically indistinguishable.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

The bosonic Fock-space trace criterion is standard second-quantization theory. The prime-lattice specialization, the coordinate-permutation obstruction, and the finite-support/thermodynamic-support interpretation are elementary consequences recorded here as a research-line negative. No novelty is claimed for Fock factorization, geometric distributions, or Borel--Cantelli.

## 1. The positive integers are exactly the finite-particle occupation basis

Let the one-particle Hilbert space be

\[
\mathfrak h=\ell^2(\mathcal P),
\]

with basis vectors indexed by rational primes. Its bosonic Fock occupation basis is indexed by finite-support vectors

\[
\alpha=(\alpha_p)_p\in\mathbb N_0^{(\mathcal P)}.
\]

Unique factorization identifies

\[
\alpha=v(n)
\longleftrightarrow
n=\prod_p p^{\alpha_p}.
\]

For a positive one-particle energy operator

\[
h_\epsilon e_p=\epsilon_p e_p,
\]

second quantization gives

\[
H_\epsilon=d\Gamma(h_\epsilon),
\]

and on the integer basis

\[
H_\epsilon e_n
=
\left(\sum_p v_p(n)\epsilon_p\right)e_n.
\]

This is the general diagonal additive Hamiltonian compatible with multiplication of integers and independent prime occupations. The classical primon gas is the specialization `epsilon_p=log p`, for which the total energy is `log n`.

## 2. Exact trace criterion

Write

\[
x_p=e^{-\beta\epsilon_p}\in(0,1).
\]

Because all terms are nonnegative, summing first over configurations supported in a finite prime set `F` and then increasing `F` to all primes gives by monotone convergence

\[
\begin{aligned}
Z_\epsilon(\beta)
&=\sum_{\alpha\in\mathbb N_0^{(\mathcal P)}}
   \prod_p x_p^{\alpha_p}\\
&=\lim_{F\uparrow\mathcal P}
  \prod_{p\in F}\sum_{k\ge0}x_p^k\\
&=\prod_p(1-x_p)^{-1},
\end{aligned}
\]

where the value is allowed to be `+infinity`.

The infinite product is finite exactly when `sum_p x_p` is finite. One direction follows from

\[
-\log(1-x)\ge x,
\]

so a finite product forces `sum_p x_p<infinity`. Conversely, if that sum is finite, only finitely many `x_p` exceed `1/2`, while for `0<=x<=1/2`,

\[
-\log(1-x)\le2x.
\]

Hence `sum_p -log(1-x_p)<infinity`, so the product converges. Therefore

\[
\boxed{
Z_\epsilon(\beta)<\infty
\iff
\sum_p e^{-\beta\epsilon_p}<\infty.
}
\]

This is the diagonal prime-lattice instance of the standard theorem that the bosonic Fock Gibbs operator is trace class exactly when the corresponding one-particle heat operator is trace class, with the usual positivity condition. A peer-reviewed modern reference is Rui Dong, Masoud Khalkhali and Walter D. van Suijlekom, “Second Quantization and the Spectral Action,” *Journal of Geometry and Physics* **167** (2021), 104285, DOI `10.1016/j.geomphys.2021.104285`, especially the second-quantization/Gibbs preliminaries; they in turn cite the classical Bratteli--Robinson treatment.

## 3. Full coordinate symmetry forces infinite degeneracy

Let `pi` be a finite permutation of the prime set and let `U_pi` permute occupation coordinates. Suppose

\[
U_\pi^*H_\epsilon U_\pi=H_\epsilon
\]

for every such permutation. Apply this to the one-prime state `e_p`. Its energy is `epsilon_p`; after permutation it is `epsilon_(pi(p))`. Transitivity of finite permutations gives

\[
\epsilon_p=c
\qquad\text{for every prime }p.
\]

If `c>0`, every one-prime state has the same eigenvalue `c`, so that eigenvalue has infinite multiplicity. Thus `H_epsilon` has no compact resolvent. Moreover

\[
\sum_p e^{-\beta\epsilon_p}
=
\sum_p e^{-\beta c}
=
\infty
\]

for every finite `beta`; the heat operator is not trace class. If `c=0`, the obstruction is stronger still.

The canonical unlabeled graph-distance Hamiltonian is exactly

\[
H_\Omega=\sum_p N_p,
\]

so this result applies with `c=1`. Every prime lies on the same radius-one shell, and there are infinitely many such basis states. The infinite shell multiplicity is not a subtle analytic-continuation problem: it prevents ordinary finite-temperature normalization before zeta or its zeros enter.

More generally, normal Gibbs equilibrium forces

\[
\sum_p e^{-\beta\epsilon_p}<\infty,
\]

hence `epsilon_p -> infinity` along the primes and only finitely many prime directions can lie below any fixed energy bound. Any normalizable additive energy must therefore break full prime-coordinate symmetry.

## 4. Thermodynamic completion leaves finite-support arithmetic exactly at the same threshold

For a finite prime set `F`, normalize the finite-volume Gibbs weight. The occupations are independent and

\[
\Pr_F(v_p=k)=(1-x_p)x_p^k.
\]

Passing to the Kolmogorov product on all prime coordinates gives independent geometric variables with

\[
\Pr(v_p>0)=x_p.
\]

If `sum_p x_p<infinity`, the first Borel--Cantelli lemma implies that only finitely many events `{v_p>0}` occur almost surely. The product law is therefore concentrated on finite-support exponent vectors and can be identified with the normalized Gibbs law on positive integers.

If instead `sum_p x_p=infinity`, independence and the second Borel--Cantelli lemma give

\[
\Pr(v_p>0\text{ for infinitely many }p)=1.
\]

The limiting local equilibrium still exists as a product probability measure on the completed space `N_0^P`, but almost every configuration has infinite support and so does **not** correspond to a positive integer. For `H_Omega`, `x_p=e^(-beta)` is constant, so this escape happens for every finite inverse temperature.

This distinction prevents a misleading repair: one may obtain an infinite-system KMS/product state after completing the configuration space, but that is not a normal Gibbs state on the original integer occupation Hilbert space. Any arithmetic significance assigned to the completed state must explain why its almost-sure infinite-support configurations retain rational-integer or zeta information rather than generic countable-product harmonic data.

## 5. Relation to the post-PL-231 frontier

`PL-231` showed that for the canonical affine `log n` dynamics, ordinary KMS energy balance kills coefficients coupling distinct multiplicative channels in the unique phase and leaves only a freely chosen replicated boundary Fourier profile in the low-temperature phase. One explicitly surviving design possibility was to change the dynamics so that distinct prime channels can become energy-compatible.

The abstract exponent lattice suggests an especially canonical modification: replace the prime-dependent weights `log p` by a coordinate-symmetric weight, so all basis directions have the same cost. The present finding shows that this move fails at the level of spectral multiplicity and normal equilibrium. The symmetry that creates all-prime degeneracy simultaneously creates infinitely many states at the first excited energy and forces the thermodynamic mass into infinite-support configurations.

The standard `log p` energy occupies the opposite side of this tradeoff. It makes the prime energies nondegenerate and growing,

\[
\epsilon_p=\log p,
\]

so

\[
\sum_p e^{-\beta\epsilon_p}
=
\sum_p p^{-\beta}<\infty
\quad(\beta>1),
\]

and the bosonic product recovers `zeta(beta)`. But this uses the arithmetic norm map `p -> log p`; it is not forced by the unlabeled orthant geometry. The no-go therefore reinforces the mandate's matched-control requirement: **the bare coordinate symmetry is too large**, while the rational norm weights are extra arithmetic structure whose zeta partition function is already classical prior art.

## 6. Prior-art and novelty audit

The occupation-number/prime-mode dictionary with `epsilon_p=log p` is already classical in Julia's primon gas and is recorded in `PL-004`. Standard bosonic second-quantization theory gives the general equivalence between trace-class one-particle heat kernel and trace-class Fock Gibbs operator; Dong--Khalkhali--van Suijlekom provide a convenient modern peer-reviewed reference for that criterion.

A targeted search around equal-energy bosonic modes, countably infinite Fock Gibbs states, prime-factor-counting Hamiltonians, and `Omega(n)` partition functions found the general Fock-space criterion and the classical prime-gas literature, not an RH localization mechanism based on an all-prime-degenerate `Omega` Hamiltonian. No novelty is inferred from that absence. The durable content is only the line-specific audit: imposing full prime-coordinate permutation symmetry on an additive exponent-lattice energy forces constant one-particle energy, which is incompatible with compact resolvent and normal finite-temperature equilibrium on the finite-support integer representation.

The negative is also generic rather than rational-prime-specific. Replace the prime labels by any countably infinite set of independent bosonic coordinates and the same argument holds. This universality is precisely why the coordinate-symmetric thermodynamic effect cannot by itself be evidence for RH.

## 7. Boundary conditions and decisive tests

The conclusion is intentionally narrower than a no-go for alternative dynamics.

First, finite degeneracy blocks are not excluded. A weight sequence may assign equal energy to finitely many primes at each level while still satisfying `sum_p e^(-beta epsilon_p)<infinity`; such a model can retain some cross-channel degeneracies. What fails is full prime-permutation symmetry, or more generally any infinite bounded-energy prime family.

Second, nonadditive interactions can lift or reorganize the degeneracy. The proof treats Hamiltonians obtained from a one-particle prime energy by bosonic second quantization, equivalently diagonal additive energies `sum_p v_p(n) epsilon_p`. A genuinely interacting source-forced Hamiltonian is outside the result and would have to justify its interaction from arithmetic rather than tune it to a desired spectrum.

Third, singular/non-normal KMS states on a smaller `C*`-algebra are not ruled out. Bost--Connes itself demonstrates that KMS equilibrium may survive below a type-I Gibbs trace threshold. Such an escape therefore requires additional observable-algebra structure; it is no longer the bare coordinate-symmetric integer Fock model.

Fourth, the summability criterion does not select `log p`. Any sequence with sufficiently fast-growing prime energies passes. A candidate that claims rational-prime significance from trace-class normalizability alone fails the generalized-weight matched control.

The finding should be withdrawn or narrowed if any of the following fails: (1) the occupation basis of bosonic Fock space is not indexed by finite-support exponent vectors; (2) the monotone finite-prime partition products do not give the stated trace; (3) convergence of the product is not equivalent to `sum_p e^(-beta epsilon_p)<infinity`; (4) full coordinate-permutation invariance does not force constant one-prime energy; or (5) in the divergent case the independent geometric completion is not almost surely infinite-support. All five are exact elementary checks.

## Consequence for the research line

After `PL-231`, merely changing from `log p` to the unlabeled lattice radius `Omega` is not a live way to recover cross-prime equilibrium information. It restores maximal energy degeneracy only by destroying finite-multiplicity spectral geometry and normal thermodynamic support on the positive integers.

A surviving alternative dynamics must therefore thread a narrower needle: it must introduce a **source-forced prime relation** that allows informative cross-channel observables without collapsing infinitely many prime directions into a bounded energy shell, and it must remain tied to the rational norm/completion strongly enough to distinguish the ordinary primes from a generic countable bosonic lattice. This leaves finite-block degeneracies, genuinely interacting affine relations, target-relative completions, and non-normal arithmetic KMS mechanisms open, but rules out the most canonical all-prime-symmetric energy repair.