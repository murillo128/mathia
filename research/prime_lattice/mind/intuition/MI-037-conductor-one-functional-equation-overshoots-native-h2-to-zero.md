# MI-037 — The conductor-one Riemann functional equation overshoots native Dirichlet `H^2` to zero

**Evidence level:** classical converse theorem plus exact line-specific consequence from [PL-359](../../findings/PL-359-hamburger-functional-equation-h2-triviality.md), read together with [PL-357](../../findings/PL-357-complete-multiplicativity-collapses-to-bohr-kernels.md) and [PL-358](../../findings/PL-358-ordinary-multiplicativity-local-zero-programmability.md).

A global arithmetic relation can be too strong for the topology in which it is imposed. In native Dirichlet `H^2`, the exact conductor-one Riemann functional equation with the standard finite-order continuation hypotheses does not select a useful intermediate family: it annihilates it.

Hamburger's converse theorem says that two ordinary Dirichlet series satisfying the exact conductor-one Riemann functional equation and the usual finite-order regularity must be the same scalar multiple of `zeta`. But native `H^2` has square-summable coefficients and is holomorphic throughout `Re s>1/2`. The unshifted zeta vector `(1,1,1,...)` is neither square-summable nor holomorphic at `s=1`. Hence the only native `H^2` solution is zero.

This sits on the opposite side of the PL-357--PL-358 bracket. Ordinary multiplicativity is too weak because one prime-power factor can program a zero. Complete multiplicativity is too rigid because it collapses the source to a zero-free reproducing kernel. The exact Riemann functional equation is globally coupled but, in the same native topology, is stronger still: the nonzero conductor-one solution lies outside the space.

The reusable lesson is that **global coupling must be audited together with the completion topology**. It is not enough that a relation is canonical, arithmetic or even uniquely characterizes zeta in its classical category. If the chosen Hilbert completion excludes the characterized object, the relation provides no intermediate discriminator at all.

Weighted or shifted spaces illustrate the tradeoff. One can move a zeta-like coefficient vector into `H^2` by sufficient decay, but the corresponding functional-equation reflection center moves as well. More generally, changing conductor, Gamma data, source spectrum or completion can create nonzero families, but then Hamburger's conductor-one uniqueness no longer applies and the destination geometry must be re-established from scratch.

For Prime Lattice, a viable global source law must therefore satisfy two gates simultaneously: it must leave a nontrivial completed family, and it must couple primes/degrees strongly enough to defeat the local zero programmability of ordinary multiplicativity without collapsing to the zero-free complete-multiplicative manifold.

**Boundary.** The finite-order converse-theorem regularity, ordinary integer Dirichlet spectrum, conductor-one Gamma factor and native unweighted `H^2` topology are load-bearing. The statement does not classify generalized Dirichlet series, altered conductors, weighted/distributional completions or target-relative source spaces, and it has no RH implication by itself.