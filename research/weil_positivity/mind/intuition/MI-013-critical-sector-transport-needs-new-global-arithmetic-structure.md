# MI-013 — Critical half-density needs an infinite-dimensional closable source correspondence

**Evidence level:** supported by the exact Fock coefficient carrier, symmetric-sector criticality, canonical-Hessian mismatch, and the finite-dimensional boundary nonclosability theorem through WP-261; Weil orientation/completion remain open.

The Fock branch now separates coefficient sourcing from target geometry very sharply. WP-256 produces the exact positive Mangoldt half-density from prime-word multiplicity and arithmetic energy. WP-259 removes the free-Fock thermodynamic mismatch by passing canonically to the permutation-fixed sector: the Gibbs boundary is then `beta=1` while the prime-power diagonal `Lambda(n)/sqrt(n)` survives.

That still does not create the Weil pairing. WP-260 shows that the canonical bosonic Gibbs/Fisher Hessian inserts an extra occupation factor, so canonical convexity has the wrong prime-power coefficient law even in finite-prime truncations.

WP-261 tests a more relational operation. The compressed symmetric-Fock backward shifts send every first-layer prime state to a common vacuum. After the source-derived mean-energy and half-density weights, the resulting positive Gram form has exactly

\[
q_{1/2}(e_{p^k},e_{p^k})=\frac{\Lambda(p^k)}{\sqrt{p^k}},
\]

and genuinely nonzero cross-prime entries on the first layer. But that coherent boundary collapse is nonclosable throughout `0<sigma<=1`. More generally, no fixed finite-dimensional boundary Hilbert space can receive all prime-layer vectors with squared norms `(log p)p^{-sigma}` through a closable operator in that regime: closability would force bounded finite rank and hence the impossible summability `sum_p (log p)p^{-sigma}<infinity`.

The matched control exposes the tradeoff. Keeping the prime boundary label orthogonal gives a bounded exact Mangoldt carrier for every positive `sigma`, but restores prime separability. Collapsing the labels into finite dimension creates cross-prime coherence but becomes nonclosable at and well beyond the Weil exponent.

The missing object is therefore narrower than “some global positivity.” It must be a source-forced **infinite-dimensional closable correlation/correspondence** (or a rigorously justified different operator category) that retains the critical Mangoldt half-density while creating the off-diagonal Weil orientation and incorporating the Gamma/polar sectors. Finite-dimensional coherent scalarization cannot supply that bridge.

**Boundary.** WP-261 excludes finite-dimensional boundary reception with the exact critical prime norms in the ordinary Hilbert-space closability category. It does not exclude infinite-dimensional correspondences, renormalized constructions with an independently justified domain, or other non-equivalent operator categories. The exact diagonal and cross-prime positivity obtained in finite truncations are not themselves evidence for completed Weil positivity.
