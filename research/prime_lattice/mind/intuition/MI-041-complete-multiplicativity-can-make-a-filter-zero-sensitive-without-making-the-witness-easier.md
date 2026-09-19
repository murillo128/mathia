# MI-041 — Complete multiplicativity makes pole neutrality zero-sensitive but does not supply continuation

**Evidence level:** literature-backed exact synthesis from [PL-369](../../findings/PL-369-venturini-completely-multiplicative-zero-free-witness.md) through [PL-371](../../findings/PL-371-sparse-liouville-real-continuation-obstruction.md), interpreted against the ambient filter controls PL-363--PL-368.

PL-363--PL-368 show that linear filter classes can manufacture critical-looking convergence walls without selecting zeta zeros. Finite filters are periodic continuations, unrestricted filters are programmable, `ell^p` geometry produces the exponent ladder `1-1/p`, and scalar Dirichlet Hardy spaces produce a generic absolute-convergence wall at `1/2`. Pole neutrality inside those ambient classes is therefore not a zero-selection mechanism.

PL-369 identifies a qualitatively different regime already present in the literature. Let `a` be bounded and completely multiplicative. Venturini proves that if `L(a,s)` is holomorphic on `Re(s)>sigma_0` and `L(a,1)=0`, then zeta has no zero in that half-plane. Complete multiplicativity fixes the entire exponent-lattice source from its prime-axis values, and conjugate symmetrization produces a nonnegative logarithmic Dirichlet series. The theorem interface is genuinely source-rigid rather than an ambient norm artifact.

The Liouville function gives the exact adversarial control:

`L(lambda,s)=zeta(2s)/zeta(s)`.

At the critical half-plane, witness existence is therefore RH-equivalent. The nonlinear source law creates a valid zero-sensitive criterion, but the hard step moves into proving continuation independently.

PL-370 sharpens the **local** source class before any critical-half-plane continuation is assumed. If `L(a,s)` extends holomorphically across a neighbourhood of `s=1` and vanishes there, then the zero is simple and

`sum_p (1+Re a(p))/p < infinity`.

Thus a pole-neutral witness lies at finite prime-harmonic distance from Liouville. In a fixed finite phase alphabet it equals `-1` outside a reciprocal-prime-summable exceptional set. Local boundary cancellation already removes generic Helson-phase freedom.

PL-371 supplies the decisive control on what that rigidity buys. Fix any `sigma_0<1`. One can choose a reciprocal-prime-summable set `E_alpha` whose prime Dirichlet series diverges at a prescribed `alpha in (max(sigma_0,1/2),1)`, flip Liouville from `-1` to `+1` on exactly that set, and preserve a simple holomorphic zero at `s=1`. Yet the Euler correction

`H_alpha(s)=product_(p in E_alpha) (1+p^(-s))/(1-p^(-s))`

blows up as real `s` decreases to `alpha`, while `zeta(2alpha)/zeta(alpha)` is finite and nonzero. The resulting completely multiplicative witness therefore cannot extend holomorphically to `Re(s)>sigma_0`.

This makes the separation exact: **source rigidity, local boundary selection and global continuation are independent gates**. Finite prime-harmonic distance is a strong necessary condition for pole neutrality, but it controls only the `1/p` geometry. Sparse prime defects can carry a different Dirichlet abscissa and place a continuation obstruction arbitrarily close to one without violating any local PL-370 diagnostic.

The next continuation mechanism must therefore control the exceptional-prime tail on every exponent scale needed to cross the strip, or invoke a genuinely global source-native structure that those sparse flips cannot preserve. Merely narrowing the source to a Liouville neighbourhood is real classification progress, but it is not analytic proof advantage by itself.

**Boundary.** PL-371 is a negative control, not a natural-boundary theorem. It shows that finite reciprocal-prime distance plus the exact simple zero at `1` gives no uniform holomorphic half-plane beyond `1`. It does not rule out stronger continuation hypotheses derived from additional arithmetic structure, and it has no independent RH consequence.