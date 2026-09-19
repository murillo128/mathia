# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable Prime-Lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-forced intermediate filter class that is neither programmable nor merely limit-periodic

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability` through `MI-040-shift-filter-rigidity-is-squeezed-between-programmability-and-limit-periodicity`.

PL-345--PL-362 progressively close the obvious completion, multiplicativity, functional-equation, coefficient-topology and positive-summation escapes. The common lesson is that a representation or topology does not gain zero-selective content merely by moving the formal boundary: canonical coefficient cutoffs rebuild the ordinary convergence wall, exact conductor-one symmetry overshoots native `H^2`, and coefficientwise-positive recovery cannot cross the real divergence barrier.

PL-363 gives the first finite signed control. A fixed finite lattice-shift filter `T=sum_m c_m S_m` sends the coefficient-one zeta vector to the periodic divisor-filter sequence `b_k=sum_(m|k)c_m`. If the finite Dirichlet polynomial `P(s)=sum_m c_m m^-s` satisfies `P(1)=0`, the output series has ordinary convergence on `Re(s)>0` and classical Hurwitz continuation, with `B(s)=P(s)zeta(s)`. Sign-indefinite filtering crosses the positive cone, but only by manufacturing a classical periodic continuation whose extra zeros belong to the chosen filter.

PL-364 closes the naive infinite-support escape at the opposite extreme. For an unrestricted fixed infinite filter `c`, the coefficientwise output is

`b=c*1`.

Classical Möbius inversion makes `c -> b` an algebraic bijection on all arithmetic functions, with inverse `c=mu*b`. Thus arbitrary infinite signed support is maximally non-rigid: any desired output coefficient sequence can be programmed. Infinite support by itself is not additional arithmetic structure.

PL-365 then tests the first natural nonprogrammable analytic restriction. If `c in ell^1`, the shift series defines a genuine bounded operator, and the output remains `b=c*1`, but now `b` is uniformly limit-periodic. Writing `C(s)=sum c_n n^-s` and `A=C(1)`, one has the exact summatory estimate

`sum_(n<=x)b_n=xA+O(||c||_1)`.

Under the pole-cancellation condition `C(1)=0`, every nonzero such output has exact ordinary convergence abscissa `sigma_c=0` and absolute convergence abscissa `sigma_a=1`. The class removes arbitrary programmability but preserves exactly the same `0/1` convergence geometry as the finite periodic filters; it still supplies no distinguished `Re(s)=1/2` mechanism.

The viable regime is therefore not obtained by monotonically adding more signed shifts. Finite support is rigid but classically periodic; unrestricted infinite support is universal and circular; `ell^1` support is a genuine bounded-operator class but still collapses to limit-periodic cancellation. A useful intermediate family must be **independently source-forced** and restrictive for a reason tied to the arithmetic construction rather than the desired output.

The live possibilities include weaker bounded-multiplier classes whose restriction is not equivalent to arbitrary coefficient programming, scale-dependent families with a canonical limiting law, non-coefficientwise mixing, a counterterm or finite-part prescription forced by a functional equation or trace identity, target-relative quotient geometry, rigged/distributional evaluation, or another global correlation whose continuation and zero-sensitive destination theorem are independently justified. The first test for any candidate is now whether its admissible coefficient law escapes both Möbius programmability and the limit-periodic `sigma_c=0`, `sigma_a=1` collapse.

## Treat completeness radius, coefficient topology, cutoff protocol, filter admissibility and zero selection as separate budgets

Beurling--Malliavin density measures how far a restricted modulation family tests the localized Weil form. PL-353--PL-356 show that algebraic coefficient restrictions may disappear under completion. PL-357--PL-361 show that nonlinear multiplicative constraints, exact global symmetry or topology changes can be too local, too rigid or incapable of crossing the scalar convergence wall. PL-362--PL-365 add a separate **summation/filter axis**.

On that axis, positivity is too rigid to cross the wall; finite signs cross it but only periodically; unconstrained infinite signs destroy all rigidity; and the first operator-norm constraint restores rigidity only as limit-periodicity. These are distinct failures. “Allow signs,” “allow infinite support,” or “make the operator bounded” is incomplete unless the admissible class is fixed independently of the output, the source vector/domain is specified, the continuation mechanism is explicit, and filter zeros are separated from inherited zeta zeros.

## Keep coefficient algebra, analytic continuation and critical selection distinct

The formal divisor-convolution identity `b=c*1` is coefficient algebra. Product identities such as `B=C zeta` require a legitimate common analytic domain or an independently justified continuation. Neither layer explains why a zero should lie on the critical line.

The next Prime-Lattice mechanism must therefore exhibit a source-native admissible family and a continuation/readout protocol simultaneously, then show why the same restriction supplies a genuinely zero-sensitive destination statement. A coefficient law chosen after the desired output, a pole-cancelling condition imported from known zeta continuation, or a bounded class whose outputs remain limit-periodic should be treated as controls rather than selectors.
