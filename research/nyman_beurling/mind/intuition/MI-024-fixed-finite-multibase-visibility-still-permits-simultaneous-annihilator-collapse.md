# MI-024 — Fixed finite multibase visibility still permits simultaneous annihilator collapse

**Evidence level:** exact matched-control route boundary from [NB-134](../../findings/NB-134-fixed-multibase-visibility-still-permits-simultaneous-superpolynomial-annihilator-collapse.md), strengthening [NB-133](../../findings/NB-133-zero-count-visibility-and-vinogradov-korobov-depth-still-permit-superpolynomial-annihilator-collapse.md)

NB-133 shows that one visible recurrence can be catastrophically ill-conditioned when `Theta(log R)` sampled roots cluster near the missing target root. NB-134 shows that replacing that scalar certificate by any **fixed finite family of geometric bases** does not remove the matched-control escape.

For every fixed finite set of integer bases `Q={q_1,...,q_m}`, simultaneous Diophantine recurrence supplies unbounded center ordinates `G` with all phases `e^(iG log q)` close to `1`; after reparameterizing by a cutoff `R`, these centers can lie at polynomial height. A formal packet of rank `d_R=c log R+O(1)` can then be placed inside the same numerical zero-count allowance and on the allowed side of the Vinogradov--Korobov boundary while its full recurrence is visible at every fixed base.

Nevertheless, at every base the sampled roots cluster near that base's missing harmonic root and the normalized NB-124 annihilator margin is smaller than every fixed power of `R`. Any standard finite aggregation of those scalar margins therefore still collapses simultaneously.

The reusable boundary is stronger than “one base loses angular information”: **finitely many fixed phase clocks can recur together, so finite multiview scalarization does not by itself create coercivity.** A repair must use information genuinely joint across representations, a number of bases growing with scale, a source-specific arrangement law for actual zeta zeros, or a target functional whose conditioning does not multiply the same cluster of rootwise distances.

**Boundary.** The packet is formal, not an asserted zeta-zero configuration. The result excludes fixed finite scalar-annihilator repairs under the current coarse source constraints; it does not exclude growing-base schemes, non-scalar joint certificates, or additional actual-zero spacing/arrangement theorems.