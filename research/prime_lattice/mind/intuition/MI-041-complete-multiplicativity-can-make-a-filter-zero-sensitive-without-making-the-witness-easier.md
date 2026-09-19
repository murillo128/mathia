# MI-041 — Complete multiplicativity makes pole neutrality zero-sensitive and locally Liouville-rigid without making critical continuation easier

**Evidence level:** literature-backed exact synthesis from [PL-369](../../findings/PL-369-venturini-completely-multiplicative-zero-free-witness.md) and [PL-370](../../findings/PL-370-pole-neutral-liouville-prime-harmonic-rigidity.md), interpreted against the ambient filter controls PL-363--PL-368.

PL-363--PL-368 show that linear filter classes can manufacture critical-looking convergence walls without selecting zeta zeros. Finite filters are periodic continuations, unrestricted filters are programmable, `ell^1` filters become limit-periodic, `ell^p` geometry produces the entire exponent ladder `1-1/p`, and scalar Dirichlet Hardy spaces produce a generic absolute-convergence wall at `1/2` that moves under vector-valued cotype. Pole neutrality inside those ambient classes is therefore not a zero-selection mechanism.

PL-369 identifies a qualitatively different regime already present in the literature. Let `a` be bounded and completely multiplicative. Venturini proves that if `L(a,s)` is holomorphic on `Re(s)>sigma_0` and `L(a,1)=0`, then zeta has no zero in that half-plane. Complete multiplicativity fixes the entire exponent-lattice source from its prime-axis values, and conjugate symmetrization produces a nonnegative logarithmic Dirichlet series. The resulting theorem interface is genuinely source-rigid rather than an ambient norm artifact.

The Liouville function gives the adversarial control:

`L(lambda,s)=zeta(2s)/zeta(s)`.

For `1/2<=sigma_0<1`, zero-freeness supplies exactly such a witness, so at `sigma_0=1/2` existence of the critical witness is RH-equivalent. The nonlinear source law creates a valid zero-sensitive criterion, but the hard step moves into proving continuation independently.

PL-370 sharpens the **local** source class before any critical-half-plane continuation is considered. If `L(a,s)` merely extends holomorphically across a neighbourhood of `s=1` and vanishes there, then the zero is forced to be simple and

`log |L'(a,1)| = sum_p sum_(k>=1) (1+Re(a(p)^k))/(k p^k) < infinity`.

In particular

`sum_p (1+Re a(p))/p < infinity`,

so `a` lies at finite prime-harmonic distance from Liouville. For a fixed finite phase alphabet, every non-`-1` prime value can occur only on a set of finite reciprocal-prime mass; an alphabet not containing `-1` is excluded entirely. Thus pole neutrality at the Euler-product boundary already collapses generic Helson-phase freedom to a Liouville neighbourhood.

This is stronger than saying that complete multiplicativity is a useful nonlinear class. It identifies the first rigid source coordinate: a pole-neutral witness must be **Liouville-like on the prime axes before one asks for continuation toward `1/2`**. The next continuation problem should therefore be posed on finite prime-harmonic perturbations of Liouville, not on arbitrary bounded completely multiplicative phases.

The reusable lesson is that **source rigidity, local boundary selection, critical continuation and proof advantage are separate gates**. PL-370 shows that a local zero at `1` already forces substantial arithmetic structure, while PL-369 shows that extending any admissible witness through the critical half-plane is still as hard as the zero-free conclusion in the Liouville control. Narrowing the source class is real progress only if that rigidity yields an independent continuation mechanism.

**Boundary.** Finite prime-harmonic distance from Liouville is necessary for a holomorphic zero at `1`, not sufficient for continuation across `1`, continuation to `Re(s)>1/2`, or RH. PL-370 controls the real/chordal prime distance and does not imply absolute convergence of the complex Euler-log difference. The finite-alphabet conclusion does not make the witness unique: finite or reciprocal-prime-summable perturbations of Liouville remain possible. Venturini's zero-free implication remains classical prior art.