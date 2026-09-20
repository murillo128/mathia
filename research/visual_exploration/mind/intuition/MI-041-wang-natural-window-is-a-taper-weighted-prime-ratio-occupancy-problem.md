# MI-041 — Wang's generic nonstationary escape is real; the open burden is arithmetic frequency migration plus downstream derivative repayment

**Evidence level:** exact/literature-backed synthesis from VIS-313--[VIS-336](../../findings/VIS-336-wang-quadratic-chirp-derivative-repayment.md). No prime-pair asymptotic or RH consequence is claimed.

VIS-313--VIS-329 close the natural moving-upper occupancy problem at the required upper-bound scale. The fixed-source route has a different boundary. VIS-330--VIS-334 show that the normalized source-to-Wang map has no real-frequency zero, transmits coherent low-frequency structure, attenuates high log frequencies by only one order, and has an exact inverse containing one derivative plus exponentially weighted memory. A simultaneous smooth gain for both `Q` and `Q'` therefore transfers back to the source.

VIS-335 proves that this derivative tax is sharp on exact fixed-frequency controls. For `F_omega(u)=e^{i omega u}`, the Wang output is `O(omega^{-1})` while `Q'_omega` retains order-one amplitude; the attenuated scale has simply moved into the derivative channel.

VIS-336 removes the loophole that this separation might require choosing a different source for every frequency. The single chirp `F(u)=e^{iu^2/2}` has instantaneous frequency growing like `u`, with `Q(u)=F(u)(4i/u+4/u^2+O(u^-3))` and `Q'(u)=-4F(u)+O(u^-1)`. One nonstationary trajectory can therefore become pointwise small after Wang smoothing while keeping the source scale in its derivative.

The generic filter question is now closed sharply enough. The live question is arithmetic: does the actual normalized squared-von-Mangoldt summatory remainder exhibit a comparable, quantitatively controlled migration in log frequency? If it does, the second burden is destination-level: does Wang's final statistic use the small `Q` without paying back the large derivative or an equivalent unsmoothed channel?

**Boundary.** VIS-335--VIS-336 are matched controls, not evidence that the arithmetic source is chirp-like or frequency-migrating. They also do not show that Wang's complete destination avoids derivative-sensitive terms. Further generic chirp examples are not a substitute for either missing theorem.
