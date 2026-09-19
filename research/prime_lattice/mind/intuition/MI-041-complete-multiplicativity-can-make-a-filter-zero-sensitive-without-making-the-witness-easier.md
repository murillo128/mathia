# MI-041 — Complete multiplicativity plus continuation forces scale-by-scale Liouville rigidity

**Evidence level:** literature-backed exact synthesis from [PL-369](../../findings/PL-369-venturini-completely-multiplicative-zero-free-witness.md) through [PL-372](../../findings/PL-372-venturini-scale-rigidity-finite-alphabet-collapse.md), interpreted against the ambient filter controls PL-363--PL-368.

PL-363--PL-368 show that linear filter classes can manufacture critical-looking convergence walls without selecting zeta zeros. Finite filters are periodic continuations, unrestricted filters are programmable, `ell^p` geometry produces the exponent ladder `1-1/p`, and scalar Dirichlet Hardy spaces produce a generic absolute-convergence wall at `1/2`. Pole neutrality inside those ambient classes is therefore not a zero-selection mechanism.

PL-369 identifies a qualitatively different regime already present in the literature. Let `a` be bounded and completely multiplicative. Venturini proves that if `L(a,s)` is holomorphic on `Re(s)>sigma_0` and `L(a,1)=0`, then zeta has no zero in that half-plane. Complete multiplicativity fixes the entire exponent-lattice source from its prime-axis values, and conjugate symmetrization produces a nonnegative logarithmic Dirichlet series. The theorem interface is genuinely source-rigid rather than an ambient norm artifact.

The Liouville function gives the exact adversarial control:

`L(lambda,s)=zeta(2s)/zeta(s)`.

At the critical half-plane, witness existence is therefore RH-equivalent. The nonlinear source law creates a valid zero-sensitive criterion, but the hard step moves into proving continuation independently.

PL-370 sharpens the **local** source class before any critical-half-plane continuation is assumed. If `L(a,s)` extends holomorphically across a neighbourhood of `s=1` and vanishes there, then the zero is simple and

`sum_p (1+Re a(p))/p < infinity`.

Thus a pole-neutral witness lies at finite prime-harmonic distance from Liouville. In a fixed finite phase alphabet it equals `-1` outside a reciprocal-prime-summable exceptional set. Local boundary cancellation already removes generic Helson-phase freedom.

PL-371 supplies the decisive control on what that local rigidity alone buys. For any `sigma_0<1`, one can choose a reciprocal-prime-summable set whose prime Dirichlet series diverges at a prescribed `alpha in (max(sigma_0,1/2),1)`, flip Liouville on exactly that set, preserve the simple zero at `1`, and create a real continuation obstruction at `alpha`. Finite prime-harmonic distance by itself gives no uniform holomorphic half-plane to the left of `1`.

PL-372 shows what changes once the full Venturini continuation hypothesis is actually present. Venturini's positive logarithm is a Dirichlet series with nonnegative coefficients. Since it continues holomorphically throughout `Re(s)>sigma_0`, Landau's theorem forces its abscissa of convergence to be at most `sigma_0`. Consequently, for every real `sigma>sigma_0`,

`sum_p (1+Re a(p))/p^sigma < infinity`

and hence

`sum_p |1+a(p)|^2/p^sigma < infinity`.

So continuation does not merely force one boundary metric at exponent `1`; it forces **Liouville closeness at every crossed prime-power scale inside the continuation half-plane**. The direction is diagnostic rather than constructive: these weighted distances are consequences of continuation, not an independent proof of it.

For a fixed finite prime alphabet this becomes much stronger. The finite gap away from `-1` turns quadratic closeness into absolute tail sparsity:

`sum_(p in E) p^(-sigma) < infinity` for every `sigma>sigma_0`,

where `E={p:a(p)!=-1}`. The relative Euler correction

`C_a(s)=prod_(p in E) (1+p^(-s))/(1-a(p)p^(-s))`

therefore converges normally and is holomorphic and zero-free on `Re(s)>sigma_0`, with

`L(a,s)=[zeta(2s)/zeta(s)] C_a(s)`.

For `1/2<=sigma_0<1`, the finite-alphabet witness has exactly the same zero/pole obstruction as Liouville. Its correction can change amplitudes and local phases but cannot cancel or move zeros of `zeta(s)`. At `sigma_0=1/2`, the finite-alphabet witness problem collapses to the Liouville quotient times a zero-free factor.

This changes the surviving source class. **Finite-alphabet continuation is not an independent mechanism.** A genuinely different Venturini witness must use structure absent from an absolutely convergent sparse correction: for example an infinite alphabet approaching `-1` with conditionally organized first-order prime information, or a separate global functional/trace/positivity mechanism not reducible to a zero-free Euler factor multiplying Liouville.

**Boundary.** The finite-alphabet collapse is conditional on the continuation already being available and does not supply it. For a general unit-disk-valued infinite alphabet, the forced `ell^2`-type prime closeness does not imply absolute convergence of `sum |1+a(p)|p^(-sigma)`, so conditional first-order information remains open. No independent critical witness, zeta zero-free region, or RH proof is obtained.
