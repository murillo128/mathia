# MI-065 — Signed carrier cost must be measured after quotienting unresolved microscopic dipoles

**Evidence level:** exact source-side synthesis from [NB-255](../../findings/NB-255-signed-scalar-carriers-pay-a-total-variation-coherence-tax.md) and [NB-256](../../findings/NB-256-microscopic-dipoles-can-inflate-signed-total-variation-without-buying-carrier-cancellation.md). The conclusion is a representation/conditioning obstruction, not an identification of the final Nyman--Beurling norm.

A signed scalar carrier can have arbitrarily large Euler-normalized coefficient total variation while being arbitrarily close to a low-variation carrier at every resolution currently used by the source and Ford-scale transform. The explicit control is a microscopic dipole

`N delta_0 - N delta_epsilon`, `epsilon=H/N^2`.

Its raw total variation is `2N`, but smooth-shell synthesis turns it into a difference of two almost coincident translates. The perturbation is `o(1)` in `L^1` and in the natural shell-scaled `L^2` norm. On the carrier side,

`N(1-exp(i epsilon z)) = O(N epsilon |z|)`

is also `o(1)` uniformly for `|z|=O(1/W)` when `H/W->0`. Hence neither the physical source nor the relevant carrier window resolves the large opposite coefficients.

This identifies the defect in raw coefficient variation: it prices amplitude without separation. The first absolute offset moment

`M_1(lambda)=int |xi| d|lambda|(xi)`

already improves the elementary coherence estimate to

`|B_lambda(z)-1| <= |z| exp(W|Im z|/2) M_1(lambda)`.

For the dipole control, `M_1` stays `Theta(W)` while total variation diverges. This does not make `M_1` canonical; it demonstrates that any useful signed-carrier conditioning quantity must be **resolution-sensitive** and invariant under adding coefficient structures that disappear after shell synthesis at the working scale.

Two mathematically distinct ways to remove the degeneracy are now visible. One can quotient coefficient measures by a transport/flat-type seminorm tied to shell resolution, so that a large near-cancelling dipole is cheap, or restrict the carrier dictionary to centers separated at a scale comparable to `H` and then seek coercivity of the synthesis map on that separated class. The second route is especially concrete because NB-256's counterexample uses separation `epsilon/H=1/N^2->0`.

The resulting research question is not “can large signed variation be hidden after projection?” Raw variation can already be hidden *before* projection. The question is whether there exists a source-native, scale-sensitive coefficient geometry for which destroying the Ford coherence window necessarily incurs a comparable cost after smooth-shell synthesis and the legal Hardy/Nyman projection.

**Boundary.** NB-256 does not prove that a minimum-`H` separation condition is sufficient, that a flat/transport norm is the correct final invariant, or that every useful signed mixture admits a separated reduction. Higher multipoles may evade low-order moments. Any proposed replacement norm must still control the actual arithmetic error ledger and destination map; no RH consequence follows.