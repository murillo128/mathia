# MI-052 — Cubic filtering pushes subleading Ramanujan mass to a moving square-free boundary

**Evidence level:** exact spectral/localization synthesis from [PL-408](../../findings/PL-408-cubic-ramanujan-moving-boundary.md), refining the source-replacement calibration in PL-404--PL-407. Ramanujan expansions, Poisson summation and Fourier moment identities are classical; the line-specific content is the denominator/exponent localization created by the already-fixed cubic filter.

For the cubic kernel `K_eta`, truncate the model singular series to Ramanujan denominators `q<=Q`. PL-408 proves, uniformly for `2<=Q<=H`,

`A_(eta,<=Q)^[2](H) = W_(1,eta) + O_eta(H^(-7) Q^6 (log log(3Q))^2)`.

Therefore a fixed fractional interior of denominator space cannot carry the subleading model terms. If `Q=H^kappa` with any fixed `kappa<1`, the truncation error is `o(H^(-1))`, so the nonzero deterministic `H^(-1)` correction comes from denominators escaping every range `q<=H^(1-epsilon)`. At the finer zero-sensitive resolution, every fixed `kappa<7/8` gives `o(H^(-7/4))`; thus the current seventh-order Fourier-decay argument forces that layer beyond `q<=H^(7/8-epsilon)`.

Because the Ramanujan spectrum here is supported on square-free `q`, the cutoff is an exponent-lattice energy bound `log q<=kappa log H`. The cubic observable suppresses every fixed nontrivial mode and, quantitatively, every fixed interior of this square-free energy ball. The interesting correction is therefore a **moving rational-frequency boundary effect**, not something recoverable from finitely many local Euler/Ramanujan channels.

The `7/8` threshold is method-relative, not an asserted arithmetic phase transition: it comes from the seventh-order Fourier decay available for this exact Abel kernel plus absolute summation in `q`. The stronger structural statement is that even the deterministic `H^(-1)` term lives arbitrarily close to the full `q~H` exponent-energy boundary on every fixed-power scale.

This reframes the live source bridge. The actual prime problem need not approximate the whole critical Ramanujan measure; it is enough, but still unproved, to compare the single signed filtered spectral functional at the required `H^(-7/4)` precision while handling the infinite-energy endpoint and source conventions. That is distinct from the PL-407 route that first bounds a source-subtracted variance remainder in absolute value.

**Boundary.** This is a model-side localization theorem. It neither proves the needed prime-source replacement nor shows that the moving boundary has favorable sign. A successful route must control that filtered boundary contribution in the actual prime spectral measure, or exploit the signed cubic multiplier directly.