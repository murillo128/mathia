# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable Prime-Lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Find a genuinely global continuation mechanism inside the Liouville-rigid class

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability` through `MI-041-complete-multiplicativity-can-make-a-filter-zero-sensitive-without-making-the-witness-easier`.

PL-345--PL-368 close the obvious completion, multiplicativity, functional-equation, coefficient-topology and positive-summation escapes. Finite filters give periodic continuations, unrestricted filters are programmable, `ell^p` geometry manufactures arbitrary summatory walls, and scalar Dirichlet Hardy geometry manufactures a generic `1/2` absolute-convergence boundary without selecting zeta zeros.

PL-369 identifies the source-forced nonlinear escape and classicalizes it. Venturini's theorem says that if `a` is bounded and completely multiplicative, `L(a,s)` extends holomorphically to `Re(s)>sigma_0`, and `L(a,1)=0`, then zeta is zero-free in that half-plane. At `sigma_0=1/2`, Liouville gives the converse through `L(lambda,s)=zeta(2s)/zeta(s)`, so existence of the critical witness is RH-equivalent.

PL-370 then makes pole neutrality locally rigid. A holomorphic zero at `s=1` is simple and forces

`sum_p (1+Re a(p))/p < infinity`.

Thus every admissible witness is at finite prime-harmonic distance from Liouville; in a fixed finite phase alphabet, non-`-1` values can occur only on a reciprocal-prime-summable exceptional set.

PL-371 proves that this local rigidity gives **no uniform continuation gain to the left of `1`**. For every `sigma_0<1`, choose `alpha in (max(sigma_0,1/2),1)` and a sparse prime set `E_alpha` with

`sum_(p in E_alpha) 1/p < infinity`

but

`sum_(p in E_alpha) p^(-alpha) = infinity`.

Flipping Liouville from `-1` to `+1` exactly on `E_alpha` produces a `{+1,-1}`-valued completely multiplicative function whose Dirichlet series has the required simple zero at `1`, yet whose Euler correction blows up at the real point `s=alpha`. It therefore cannot extend holomorphically to `Re(s)>sigma_0`.

The live question is no longer whether finite prime-harmonic distance can bootstrap continuation. It cannot. A surviving witness theorem must control the exceptional-prime tail on the exponent scales actually crossed, or supply another genuinely global source-native structure—such as a functional equation, trace/positivity identity, or rigidity principle—that sparse reciprocal-prime perturbations cannot reproduce while remaining independent of the zero-free region to be proved.

## Treat coefficient algebra, local pole neutrality and global continuation as separate budgets

The divisor-convolution identity `b=c*1` is coefficient algebra. Complete multiplicativity is a nonlinear prime-axis law. A local zero at the Euler-product boundary is a further source restriction. Holomorphic continuation through a half-plane is a genuinely global analytic property.

PL-369--PL-371 now separate these layers exactly. Complete multiplicativity makes continuation plus pole neutrality zero-sensitive. PL-370 proves that local pole neutrality collapses generic phase freedom to a Liouville neighbourhood. PL-371 then shows that the same neighbourhood still contains functions with a prescribed real continuation obstruction arbitrarily close to `1`. The hard step has not merely moved from a norm to a smaller source class; it requires information that controls the sparse tail across subunit exponents.

A proposed Prime-Lattice mechanism should therefore specify the admissible prime perturbations, the origin of pole cancellation, which Dirichlet-exponent tails are controlled, the independent continuation theorem, and why that theorem is not simply another form of the desired zeta zero-free region. Rewriting Liouville's quotient, invoking finite pretentious distance, or imposing a generic Hardy/`ell^p` topology does not supply that missing global input.