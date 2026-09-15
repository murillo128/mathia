# MI-026 — Upper zero-density cannot improve the rightmost transfer exponent

**Evidence level:** exact matched-control/non-implication boundary from [RE-142](../../findings/RE-142-upper-zero-density-envelopes-cannot-improve-the-rightmost-robin-gain.md), sharpening the full-packet budget of [RE-140](../../findings/RE-140-full-packet-turan-certificate-pays-gain-complexity-tail-budget.md) and the source-weighted tail improvement of [RE-141](../../findings/RE-141-zero-density-improves-the-robin-full-packet-tail-budget.md).

RE-141 shows that upper zero density is useful when it is spent on the **coefficient-weighted exterior tail**. The Robin coefficient contributes `gamma^-2`, so density reduces the omitted tail to roughly `T^(-2+nu(Theta))`. But the finite witness still pays an amplitude transfer from the original strong atom to the rightmost retained atom.

RE-142 shows that the generic transfer loss `G(U,T)~T^-2` is sharp relative to all currently imported upper-envelope source laws. It constructs one infinite formal zero-like spectrum satisfying the relevant upper zero-density bounds, the zero-free region, symmetry and a Riemann--von Mangoldt-compatible critical-line background, while along lacunary cutoffs

`G(U_j,T_j)=T_j^(-2+o(1))`

and the strict-subedge core has only `N_(T_j)=o(log T_j)` modes.

Thus the two-power loss is not an artifact of paying a crude polynomial zero count inside Turán. The complexity coefficient can vanish and the rightmost atom can still occur only near the truncation height with essentially no compensating horizontal displacement. Stronger **upper** zero-density estimates may further improve the tail, but they do not couple the ordinate of a rightmost atom to the ordinate/amplitude of the strong atom.

The reusable distinction is **population sparsity versus relational recurrence**. An upper bound on how many rightward zeros exist does not say that a strong off-critical atom has a farther-right companion below a controlled height, nor that a large ordinate separation must be paid for by enough horizontal gain. The certificate needs a two-attribute source law, not another one-point envelope.

The next proof obligation is therefore one of the following kinds: force rightward recurrence/first occurrence from a strong atom; couple horizontal extremality to ordinate; obtain a lower-population theorem in the relevant strip; use signed tail cancellation strong enough to tolerate the transfer loss; or replace rightmost anchoring by a target-aware/infinite-packet observable that never makes this transfer. Merely improving the exponent in an upper density theorem is now known to attack the wrong term.

**Boundary.** The RE-142 spectrum is a matched formal source, not an asserted zeta-zero configuration. It proves only that the listed coarse upper envelopes do not imply a transfer exponent `<2`. It does not show that actual zeros realize the bad geometry, that the full packet is small, or that no stronger theorem derived from the Euler product/explicit formula can couple horizontal position and height.