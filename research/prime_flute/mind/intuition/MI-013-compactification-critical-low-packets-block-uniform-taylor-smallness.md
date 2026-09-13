# MI-013 — Critical packet geometry can be priced exactly in the final Hilbert–Schmidt budget

**Evidence level:** exact for the unprojected compactified cuff-cell form through [PF-322](../../findings/PF-322-physical-low-packets-retain-critical-compactified-transverse-energy.md), the interior recentering through PF-323, the arithmetic terminal geometry through [PF-324](../../findings/PF-324-critical-packet-seam-distance-remembers-consecutive-prime-gap-ratio.md), and the translation-frame/Hilbert–Schmidt identity through [PF-325](../../findings/PF-325-physical-translations-convert-the-local-hilbert-schmidt-gate-into-a-packet-position-integral.md). None of these is yet a lower bound for the completed shear-deleted intrinsic `L/H` angle.

PF-322--PF-324 show that the compactification-critical low packet cannot be dismissed by a uniform Taylor argument or as a seam artifact. For fixed `0<lambda<1`, the packet can be recentered at the interior point `s_n cosh tau_(n,lambda)=lambda`, where its scaled transverse energy stays nontrivial. The outgoing seam seen from this coordinate satisfies

`D_(n,lambda)=log((1+r_n)/lambda)+o(1)`,

with `r_n` asymptotic to a consecutive prime-gap ratio, so the same local witness occurs along both finite-boundary and escaping-boundary subsequences.

PF-325 supplies the exact accounting bridge to PF-318. In a fixed physical-low band of dimension `m~(kappa/pi)L`, the translated equal-amplitude packets `psi_t` form a continuous tight frame. For every local low/high block `B`,

`||B||_(S_2)^2 = (m/L) integral_0^L ||B^* psi_t||^2 dt`.

Since `m/L` stays comparable to a constant, passing from Fourier rows to physical packet centers causes **no logarithmic dilution**. The required squared Hilbert–Schmidt estimate is equivalent, up to fixed cutoff constants, to an integrated packet-response estimate over the cuff coordinate. A fixed-width set of centers carrying order-one completed leakage would already violate the target budget.

This turns the critical packet from a qualitative obstruction into a quantitative falsification family. The remaining direct-angle theorem can be proved in the physical representation natural to PF-323--PF-324: build the translation orbit in the exact normalized low Hilbert space, pull it back through the Fourier-diagonal seam normalization, and integrate the actual completed pant response. The non-translation-invariant completion stays inside `B`; the Parseval identity requires no commutation.

**Boundary.** The raw `L^2` Dirichlet packet is not automatically unit-normalized after seam/angle normalization, and PF-325 does not prove that PF-323 survives the pant quotient or common completion. It says precisely how any surviving response is charged to the final PF-318 ideal budget, uniformly across the two arithmetic boundary regimes.