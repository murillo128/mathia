# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable Prime-Lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-forced filter class whose critical behavior survives both Banach and Hardy-space controls

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability` through `MI-040-shift-filter-rigidity-is-squeezed-between-programmability-and-limit-periodicity`.

PL-345--PL-362 close the obvious completion, multiplicativity, functional-equation, coefficient-topology and positive-summation escapes. The common lesson is that a representation or topology does not gain zero-selective content merely by moving the formal boundary: canonical coefficient cutoffs rebuild the ordinary convergence wall, exact conductor-one symmetry overshoots native `H^2`, and coefficientwise-positive recovery cannot cross the real divergence barrier.

PL-363--PL-365 classify three signed shift-filter regimes for the coefficient-one source. Finite support crosses the positive wall but only by producing periodic `P(s)zeta(s)` continuations. Unrestricted infinite support is maximally non-rigid because `b=c*1` is inverted by `c=mu*b`, so arbitrary outputs can be programmed. The first bounded-operator class `c in ell^1` removes programmability but forces uniformly limit-periodic outputs and, after `C(1)=0`, the universal convergence geometry `sigma_c=0`, `sigma_a=1`.

PL-366--PL-367 show that intermediate coefficient norms manufacture critical-looking walls. Pole-neutral `c in ell^2` gives `sum_(n<=x)b_n=O(sqrt(x)||c||_2)` by pure Cauchy--Schwarz, while general `c in ell^p`, `1<p<infinity`, gives the sharp exponent `theta=1-1/p`. Since `theta` fills `(0,1)`, no particular `ell^p` boundary can be interpreted as source-specific merely because it lands on `1/2`.

PL-368 tests the natural objection that the canonical Hardy spaces of Dirichlet series might single out `1/2` more meaningfully. They do single it out, but still generically. For every scalar `1<=p<=infinity`, Bohr--Bohnenblust--Hille/Bayart theory gives absolute coefficient convergence for `Re(s)>1/2`, sharply at the class level. If `C(s)=sum c_d d^-s` lies in such a Hardy space and `C(1)=0`, the same exact divisor residual gives

`sum_(n<=x)(c*1)(n)=O_(C,epsilon)(x^(1/2+epsilon))`,

and `B(s)=zeta(s)C(s)` extends holomorphically to `Re(s)>1/2`. Hypothetical zeta zeros there are simply inherited; no zero restriction follows. The vector-valued theory makes the control stronger: the corresponding absolute-convergence wall is `1-1/Cot(X)`, so scalar `1/2` is the cotype-`2` member of a general Banach-space geometry.

The live filter route must therefore survive **two complementary ambient controls**. The adjustable `ell^p` ladder shows that coefficient duality can place a wall anywhere in `(0,1)`, while canonical scalar Hardy spaces show that an apparently invariant `1/2` across all `p` can still come from generic Bohr/monomial-convergence geometry and can move under cotype deformation. A viable regime needs an independently source-forced law not reproduced by either control: a functional-equation/trace identity, target-relative quotient, non-coefficientwise coupling, source-canonical scale law, positivity/sign theorem or another global invariant that hypothetical off-line zeros would violate.

## Treat completeness radius, coefficient topology, Hardy geometry, cutoff protocol and zero selection as separate budgets

The summation/filter axis now has two distinct families of calibration. Raw `ell^p` coefficient geometry manufactures the sharp summatory exponent `1-1/p`; canonical scalar `H^p` geometry instead fixes the absolute-convergence wall at `1/2` for every `p`, while vector-valued cotype moves that wall again. Neither phenomenon is a zero-selection theorem.

A proposal must therefore specify the admissible class independently of the desired output, the source vector/domain, the continuation mechanism, the origin of pole cancellation, and a source-specific invariant not shared by the ambient coefficient or Hardy class. Filter zeros, inherited zeta zeros, norm-generated convergence walls and Bohr/cotype-generated half-planes must remain separate.

## Keep coefficient algebra, analytic continuation and critical selection distinct

The divisor-convolution identity `b=c*1` is coefficient algebra. Product identities such as `B=C zeta` require a legitimate common domain or independently justified continuation. A summatory estimate of order `x^theta` may determine a convergence half-plane without saying anything about where the zeros inside that half-plane lie.

PL-367 shows that `theta` can be prescribed by raw coefficient topology; PL-368 shows that even the canonical Hardy-space `1/2` is an ambient absolute-convergence phenomenon and, after pole cancellation, remains zero-blind. The next Prime-Lattice mechanism must therefore exhibit a source-native admissible family and a zero-sensitive destination statement simultaneously. A coefficient law chosen after the desired output, scalar pole neutrality imposed by hand, or a boundary reproduced by generic Banach/Hardy controls should be treated as calibration rather than evidence for RH.