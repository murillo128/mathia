# MI-041 — Complete multiplicativity can make a filter zero-sensitive without making the critical witness easier

**Evidence level:** literature-backed exact synthesis from [PL-369](../../findings/PL-369-venturini-completely-multiplicative-zero-free-witness.md), interpreted against the ambient filter controls PL-363--PL-368.

PL-363--PL-368 show that linear filter classes can manufacture critical-looking convergence walls without selecting zeta zeros. Finite filters are periodic continuations, unrestricted filters are programmable, `ell^1` filters become limit-periodic, `ell^p` geometry produces the entire exponent ladder `1-1/p`, and scalar Dirichlet Hardy spaces produce a generic absolute-convergence wall at `1/2` that moves under vector-valued cotype. Pole neutrality inside those ambient classes is therefore not a zero-selection mechanism.

PL-369 identifies a qualitatively different regime already present in the literature. Let `a` be bounded and completely multiplicative. Venturini proves that if `L(a,s)` is holomorphic on `Re(s)>sigma_0` and `L(a,1)=0`, then `zeta` has no zero in that half-plane. The source law is nonlinear in exponent-lattice coordinates:

`a(n)=product_p a(p)^(v_p(n))`.

The decisive analytic step is a conjugate symmetrization whose logarithmic Dirichlet coefficients are nonnegative multiples of `1+Re a(n)`. Thus complete multiplicativity plus pole neutrality and continuation can genuinely turn a source-forced filter into a zero-sensitive object. This is not an ambient norm artifact.

The same result also gives the adversarial control. For `1/2<=sigma_0<1`, the Liouville function supplies the converse through

`L(lambda,s)=zeta(2s)/zeta(s)`.

At the critical boundary `sigma_0=1/2`, the existence of the required witness is therefore equivalent to RH. The nonlinear source law has created a valid theorem interface, but the hard step has moved into proving the witness continuation independently.

PL-369 further separates this class from the earlier Hardy controls. A completely multiplicative witness with `L(a,1)=0` cannot belong to any finite coefficient `ell^p`: such membership would make the Euler product absolutely convergent and nonzero at `s=1`. The zero must arise only after conditional/global analytic continuation, exactly where the arithmetic difficulty lives.

The reusable lesson is that **escaping an ambient no-go can expose a genuine source-rigid theorem without producing analytic leverage**. Once a structured subclass is found, ask whether its defining existence/continuation theorem is easier than the destination or merely equivalent to it. Source-forced rigidity, zero sensitivity and proof advantage are separate properties.

**Boundary.** Venturini's criterion is classical prior art and applies beyond the rational primes; it does not uniquely select the Riemann source or explain the exponent `1/2`. PL-369 does not construct a new critical witness. A future advance must derive the necessary continuation from arithmetic information independent of the target zeta zero-free region, or impose an additional source law that makes such a derivation genuinely stronger than the Liouville converse.