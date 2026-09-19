# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable Prime-Lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Find a genuinely global continuation mechanism outside finite-alphabet Liouville corrections

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability` through `MI-041-complete-multiplicativity-can-make-a-filter-zero-sensitive-without-making-the-witness-easier`.

PL-345--PL-368 close the obvious completion, multiplicativity, functional-equation, coefficient-topology and positive-summation escapes. Finite filters give periodic continuations, unrestricted filters are programmable, `ell^p` geometry manufactures arbitrary summatory walls, and scalar Dirichlet Hardy geometry manufactures a generic `1/2` absolute-convergence boundary without selecting zeta zeros.

PL-369 identifies the source-forced nonlinear escape and classicalizes it. Venturini's theorem says that if `a` is bounded and completely multiplicative, `L(a,s)` extends holomorphically to `Re(s)>sigma_0`, and `L(a,1)=0`, then zeta is zero-free in that half-plane. At `sigma_0=1/2`, Liouville gives the converse through `L(lambda,s)=zeta(2s)/zeta(s)`, so existence of the critical witness is RH-equivalent.

PL-370 then makes pole neutrality locally rigid. A holomorphic zero at `s=1` is simple and forces

`sum_p (1+Re a(p))/p < infinity`.

Thus every admissible witness is at finite prime-harmonic distance from Liouville; in a fixed finite phase alphabet, non-`-1` values can occur only on a reciprocal-prime-summable exceptional set.

PL-371 proves that this local rigidity gives **no uniform continuation gain to the left of `1`**. Sparse reciprocal-prime perturbations can preserve the exact zero at `1` while placing a real continuation obstruction at any prescribed exponent in `(1/2,1)`. Local pole neutrality and global continuation are separate resources.

PL-372 shows that a genuine Venturini continuation itself forces much stronger scale-by-scale rigidity. Venturini's positive logarithmic Dirichlet series has nonnegative coefficients, so Landau's theorem implies that for every `sigma>sigma_0`,

`sum_p (1+Re a(p))/p^sigma < infinity`

and therefore

`sum_p |1+a(p)|^2/p^sigma < infinity`.

For a fixed finite prime alphabet, this forces the exceptional set `E={p:a(p)!=-1}` to satisfy `sum_(p in E)p^(-sigma)<infinity` at every crossed exponent. The relative Euler product then converges normally and gives

`L(a,s)=[zeta(2s)/zeta(s)] C_a(s)`,

where `C_a` is holomorphic and zero-free on `Re(s)>sigma_0`. For `1/2<=sigma_0<1`, every finite-alphabet witness therefore has exactly the Liouville divisor: it cannot cancel or move a zeta zero and supplies no independent continuation mechanism.

The live question has narrowed accordingly. A genuinely different source-forced witness must exploit structure that survives the scale-by-scale Liouville constraint but is not an absolutely convergent finite-alphabet correction. The clearest remaining source class is an **infinite alphabet approaching `-1` whose first-order prime information is only conditionally organized**, because PL-372 supplies quadratic weighted closeness but not absolute first-order convergence there. The alternative is a genuinely global source-native functional equation, trace/positivity identity or rigidity principle that constructs continuation without merely assuming or repackaging the desired zeta zero-free region.

## Treat coefficient algebra, local pole neutrality, scale-by-scale rigidity and global continuation as separate budgets

The divisor-convolution identity `b=c*1` is coefficient algebra. Complete multiplicativity is a nonlinear prime-axis law. A local zero at the Euler-product boundary is a further source restriction. Holomorphic continuation through a half-plane is a genuinely global analytic property, and once present it feeds back into a whole family of weighted prime constraints.

PL-369--PL-372 now separate these layers exactly. Complete multiplicativity makes continuation plus pole neutrality zero-sensitive. PL-370 proves that local pole neutrality collapses generic phase freedom to a Liouville neighbourhood. PL-371 shows that the same neighbourhood still contains functions with a prescribed real continuation obstruction arbitrarily close to one. PL-372 then shows the converse diagnostic: true continuation forces Liouville closeness at every crossed exponent, and in a finite alphabet this makes the witness a zero-free Euler correction of `zeta(2s)/zeta(s)`.

A proposed Prime-Lattice mechanism should therefore specify the admissible prime perturbations, the origin of pole cancellation, which Dirichlet-exponent tails are forced or controlled, the independent continuation theorem, and why that theorem is not simply another form of the desired zeta zero-free region. Finite alphabets are now divisor-equivalent to Liouville under the continuation hypothesis; any surviving novelty must live in conditional infinite-alphabet structure or another genuinely global mechanism.
