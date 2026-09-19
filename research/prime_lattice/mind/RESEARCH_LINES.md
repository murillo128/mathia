# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable Prime-Lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-forced filter class whose critical behavior is not an ambient norm artifact

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability` through `MI-040-shift-filter-rigidity-is-squeezed-between-programmability-and-limit-periodicity`.

PL-345--PL-362 close the obvious completion, multiplicativity, functional-equation, coefficient-topology and positive-summation escapes. The common lesson is that a representation or topology does not gain zero-selective content merely by moving the formal boundary: canonical coefficient cutoffs rebuild the ordinary convergence wall, exact conductor-one symmetry overshoots native `H^2`, and coefficientwise-positive recovery cannot cross the real divergence barrier.

PL-363--PL-365 classify three signed shift-filter regimes for the coefficient-one source. Finite support crosses the positive wall but only by producing periodic `P(s)zeta(s)` continuations. Unrestricted infinite support is maximally non-rigid because `b=c*1` is inverted by `c=mu*b`, so arbitrary outputs can be programmed. The first bounded-operator class `c in ell^1` removes programmability but forces uniformly limit-periodic outputs and, after `C(1)=0`, the universal convergence geometry `sigma_c=0`, `sigma_a=1`.

PL-366 tests the next natural Hilbert/multiplier regime and closes its most tempting signal. For every `c in ell^2`, the pole-neutrality functional `C(1)=sum c_d/d` is well defined. If `C(1)=0` and `b=c*1`, then

`sum_(n<=x) b_n = O(sqrt(x)||c||_2)`.

The proof is pure Hilbert duality: after subtracting the cancelled main term, the summatory function is the `ell^2` pairing of `c` with a floor-function residual of norm `O(sqrt x)`. Consequently the output Dirichlet series converges on `Re(s)>1/2`; on that half-plane the identity `B(s)=zeta(s)C(s)` follows by continuation from `Re(s)>1`. Bounded multipliers are included because applying a multiplier to `1` gives an `H^2`/`ell^2` coefficient vector.

This is superficially RH-shaped but is a decisive control: the exponent `1/2` is generated automatically by Cauchy--Schwarz and the chosen Hilbert geometry, independently of the zeta zero divisor. Hypothetical off-line zeros would simply be inherited by `B`; nothing localizes them. The next filter route therefore cannot be justified merely by belonging to an intermediate Banach/Hilbert class that happens to manufacture the square-root exponent.

The viable regime must add an **independently source-forced constraint** beyond pole cancellation and ambient norm membership: a functional-equation/trace identity, target-relative quotient, genuinely non-coefficientwise coupling, source-canonical scale dependence, positivity/sign law or another global invariant that hypothetical off-line zeros would violate. The first test for any proposal is now twofold: does the coefficient law escape both programmability/periodicity, and is its critical exponent/selectivity stronger than what the ambient norm guarantees for generic controls?

## Treat completeness radius, coefficient topology, cutoff protocol, filter admissibility and zero selection as separate budgets

The summation/filter axis now has four distinct controls. Positive coefficientwise recovery cannot cross the real wall; finite signs cross it but only periodically; unrestricted infinite signs destroy rigidity; `ell^1` restores rigidity as limit-periodicity; and pole-neutral `ell^2` automatically reaches square-root summatory scale for generic Hilbert reasons. None of these facts is a zero-selection theorem.

A proposal must therefore specify the admissible class independently of the desired output, the source vector/domain, the continuation mechanism, the origin of pole cancellation, and a source-specific invariant not shared by the ambient class. Filter zeros, inherited zeta zeros and norm-generated critical exponents must remain separate.

## Keep coefficient algebra, analytic continuation and critical selection distinct

The divisor-convolution identity `b=c*1` is coefficient algebra. Product identities such as `B=C zeta` require a legitimate common domain or independently justified continuation. A square-root summatory estimate may determine a convergence half-plane without saying anything about where the zeros inside that half-plane lie.

The next Prime-Lattice mechanism must therefore exhibit a source-native admissible family and a zero-sensitive destination statement simultaneously. A coefficient law chosen after the desired output, a pole-neutrality condition imposed by hand, or a function-space boundary reproduced by generic controls should be treated as calibration rather than evidence for RH.
