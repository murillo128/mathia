# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable Prime-Lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Find an independent continuation mechanism inside the Liouville-rigid pole-neutral class

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability` through `MI-041-complete-multiplicativity-can-make-a-filter-zero-sensitive-without-making-the-witness-easier`.

PL-345--PL-362 close the obvious completion, multiplicativity, functional-equation, coefficient-topology and positive-summation escapes. The common lesson is that a representation or topology does not gain zero-selective content merely by moving the formal boundary: canonical coefficient cutoffs rebuild the ordinary convergence wall, exact conductor-one symmetry overshoots native `H^2`, and coefficientwise-positive recovery cannot cross the real divergence barrier.

PL-363--PL-365 classify three signed shift-filter regimes for the coefficient-one source. Finite support crosses the positive wall but only by producing periodic `P(s)zeta(s)` continuations. Unrestricted infinite support is maximally non-rigid because `b=c*1` is inverted by `c=mu*b`, so arbitrary outputs can be programmed. The first bounded-operator class `c in ell^1` removes programmability but forces uniformly limit-periodic outputs and, after `C(1)=0`, universal convergence geometry.

PL-366--PL-367 show that intermediate coefficient norms manufacture critical-looking walls: pole-neutral `ell^p` filters give the sharp exponent `1-1/p`. PL-368 then tests the canonical Dirichlet Hardy scale. Every scalar `H^p` has the same sharp absolute-convergence wall `1/2`, while vector-valued cotype moves it again. A pole-neutral Hardy filter can therefore produce an RH-shaped half-plane without excluding hypothetical zeta zeros there.

PL-369 identifies the source-forced escape and classicalizes it. Venturini's theorem says that if `a` is bounded and completely multiplicative, `L(a,s)` extends holomorphically to `Re(s)>sigma_0`, and `L(a,1)=0`, then zeta is zero-free in that half-plane. Complete multiplicativity fixes every lattice coefficient from the prime axes, and conjugate symmetrization produces a nonnegative logarithmic Dirichlet series whose continuation forces nonvanishing.

At `sigma_0=1/2`, however, Liouville gives the converse through `L(lambda,s)=zeta(2s)/zeta(s)`, so existence of the required critical witness is RH-equivalent. PL-369 also separates this class from the earlier Hardy controls: a completely multiplicative pole-neutral witness cannot lie in any finite coefficient `ell^p` class, so its zero at `s=1` must arise through conditional/global analytic continuation rather than ordinary Hardy-space convergence.

PL-370 now makes pole neutrality itself substantially more rigid. If `L(a,s)` merely extends holomorphically across `s=1` and vanishes there, the zero is simple and

`log |L'(a,1)| = sum_p sum_(k>=1) (1+Re(a(p)^k))/(k p^k) < infinity`.

Hence

`sum_p (1+Re a(p))/p < infinity`,

so every admissible witness is at finite prime-harmonic distance from Liouville. In a fixed finite phase alphabet it must equal `-1` outside a reciprocal-prime-summable exceptional set; alphabets not containing `-1` are excluded. Generic Helson phases are therefore no longer plausible pole-neutral candidates.

The live filter question has narrowed to an **independent continuation mechanism for Liouville-like prime-axis perturbations**. Does finite prime-harmonic distance from Liouville, together with another genuinely source-native condition, force continuation into a half-plane beyond `1` without already importing the desired zeta zero-free region? Rewriting Liouville's quotient, rediscovering Venturini's criterion, or invoking generic multiplicative-phase flexibility does not answer that question.

## Treat completeness radius, coefficient topology, boundary rigidity, continuation and zero selection as separate budgets

Raw `ell^p` geometry can manufacture any summatory wall in `(0,1)`, scalar Hardy geometry can pin a generic wall at `1/2`, and complete multiplicativity can create a genuine zero-sensitive theorem interface. PL-370 inserts a fourth phenomenon: a local holomorphic zero at the Euler-product boundary forces finite harmonic distance to Liouville before any critical continuation is assumed.

These are distinct currencies. A proposal must specify the admissible class independently of the desired output, the origin of pole cancellation, the source restriction imposed by that cancellation, the continuation mechanism, and whether zero-freeness is a consequence or a hidden hypothesis. A source-forced nonlinear law deserves credit only after its required continuation is derived from information not already equivalent to the target zero-free region.

## Keep coefficient algebra, local pole neutrality and critical continuation distinct

The divisor-convolution identity `b=c*1` is coefficient algebra. Complete multiplicativity is a stronger nonlinear lattice law. Product identities and Euler logarithms are valid first on their absolute-convergence domain; continuation into the critical strip requires a separate theorem.

PL-370 shows that local continuation through `s=1` plus a zero there already has arithmetic content: it forces a simple zero and Liouville-like prime-axis data. PL-369 then shows that extending such a witness throughout the critical half-plane is still the RH-facing step. The next Prime-Lattice mechanism must therefore exploit the newly narrowed Liouville neighbourhood to obtain an independent continuation theorem or another source-native invariant, not merely another norm-generated boundary or a quotient whose holomorphy restates the desired conclusion.