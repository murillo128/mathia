# MI-060 — Separable depth penalties do not rescue fixed-power phase control at the Ford boundary

**Evidence level:** exact matched-control synthesis from [NB-225](../../findings/NB-225-sublinear-ford-shells-remain-population-blind.md) through [NB-227](../../findings/NB-227-separable-depth-penalties-do-not-rescue-fixed-power-phase-bounds.md), using the zeta-population inputs audited there.

NB-225 shows that at exact Ford scale a sublinear logarithmic source shell `H=o(R)` cannot be closed from the currently used zero-free and population information alone. An admissible near-one packet can retain an order-one moving-shell residue while staying within those population budgets.

NB-226 proves that generic phase cancellation of any fixed positive power is still insufficient. For every fixed `0<vartheta<1`, the packet can satisfy `O(m^vartheta)` cancellation on every consecutive vertical subpacket while horizontal depth is chosen so the Ford damping compensates the remaining global phase bias.

NB-227 closes the natural separable depth-sensitive repair. Let `Q(D)>=1` be any predetermined function finite at every fixed integer depth and suppose raw phase information has the form

`|sum_I e^(iX(gamma-t))| << 1 + |I|^vartheta/Q(D)`.

The matched packet can choose a slowly diverging depth `D=D(M)` with

`Q(D)e^(YD) <= M^(vartheta/2)`,

distribute a total phase bias `~e^(YD)` while respecting the strengthened bound on every consecutive subpacket, and still leave an order-one weighted residue after multiplication by `e^(-YD)`. This works no matter how rapidly the fixed function `Q(D)` grows.

The mechanism is a diagonal escape: a theorem may become arbitrarily strong at each fixed depth and still fail uniformly because the packet lets depth diverge more slowly than that improvement becomes effective relative to population. **Depth sensitivity is therefore not enough when it factorizes from a fixed positive population power.**

The surviving theorem surface must be nonseparable. Useful inputs include a depth-window population theorem in which the admissible `M` shrinks with `D`, a phase bound whose effective population exponent itself changes with depth, simultaneous constraints across nested depth slabs, or direct cancellation of the actual residue-weighted sum.

**Boundary.** NB-227 is a logical insufficiency result for the audited information package, not a construction of actual zeta zeros. It does not rule out genuinely joint depth-population-phase theorems, direct weighted-residue cancellation, or additional arithmetic correlations of the real zero set.
