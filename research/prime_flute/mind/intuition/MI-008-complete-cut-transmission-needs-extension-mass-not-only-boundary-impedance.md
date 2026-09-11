# MI-008 — Complete-cut transmission needs the invariant matched to the consumed projection

**Evidence level:** proved

## Core intuition

Local corridor attenuation does not determine **unprojected** transmission after embedding in variable reservoirs. The exact scalar Schur invariant includes endpoint-normalized extension mass as well as boundary impedance, and that mass can erase an isolated edge gain.

For the physical Prime-Flute low/high leakage, however, same-sector reservoir amplification is not automatically the relevant invariant. After the `P/H` split, the mixed inverse block is controlled by the cross-frequency form itself. The correct source-side target is the energy-normalized cross operator, not an unprojected scalar cut norm.

## Strongest justified claim

PF-228 computes the isolated corridor attenuation and PF-229 shows that a translation-invariant scalar serial completion preserves it up to a fixed factor. PF-279 gives the exact general two-reservoir formula: complete-cut norm depends on boundary impedances and their spectral derivatives, equivalently the squared norms of endpoint-normalized harmonic extensions. A positive variable scalar family can make the isolated transmission small while the complete unprojected cut remains bounded away from zero.

PF-280 then separates the mixed physical-frequency quantity. If the boundary space splits as `P+H`, the exact block resolvent identities give

`PDH=-A^(-1) B (HDH)=-(PDP) B C^(-1)`.

The outer full-resolvent blocks are contractions, so same-sector reservoir completion cannot worsen the symmetric-ideal class of either one-sided decoupled `P/H` transfer. A PF-279 amplifier confined to one frequency sector therefore contributes no mixed block by itself.

PF-281 removes the assumption that the raw cross block `B` is bounded. Positivity of the closed form defines the canonical energy-normalized cross operator

`T=A^(-1/2) B C^(-1/2)`, with `||T||<=1`.

If `T` lies in a compact symmetric ideal `J`, then `||T||<1` and the mixed inverse block factors through `T`, hence `PDH in J`; the reciprocal-prime commutator inherits the same ideal membership. Conversely positivity alone does not force compactness: valid positive block examples can have `T_j->1` and noncompact mixed inverse.

## Synthesis of evidence

PF-279 remains the exact warning against extrapolating a local seam coefficient to an unprojected complete cut. PF-280--PF-281 show why that warning must be matched to the statistic actually consumed downstream. For the coefficient-transfer route, the unresolved invariant is the singular-value decay of the **physical energy-normalized cross form `T`**. Same-sector extension mass matters only insofar as it feeds that mixed channel.

This is a more precise reservoir theorem than “bound all extension norms.” One may prove weak-trace or stronger ideal decay of `T` directly in the physical energy spaces, including finite-pant and neighboring-cell completion, even if some unprojected same-sector cut norms are large.

## Counterevidence / boundary cases

PF-279 is a scalar matched control, not the physical flute. PF-280 assumes the physical split is compatible with the stated block structure, and PF-281 gives only a sufficient ideal criterion; no finding yet proves the actual Prime-Flute `T` is weak trace class.

Energy normalization is not automatically compactifying. The positive block counterexample in PF-281 shows that a genuine low/high conversion channel may survive with order-one strength.

## Epistemic status

**Exact operator-theoretic boundary:** unprojected complete-cut transmission needs extension mass, while the projected physical route is controlled by an energy-normalized cross-frequency operator whose ideal decay is stable under same-sector reservoir completion but is not automatic from positivity.

## Novelty/prior-art status

Schur complements, block resolvent identities, form normalization, and symmetric ideals are standard operator theory as recorded in PF-279--PF-281. This intuition records their exact role in the Prime-Flute frontier.

## Falsification criterion

Show that the PF-280/PF-281 factorization fails for the actual form domain/split, or construct a same-sector reservoir completion that preserves the hypotheses yet worsens the ideal class of `PDH` beyond that of `T`. Conversely, proving the physical `T` belongs to the required weak-trace ideal would close the present gate.