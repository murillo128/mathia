# MI-041 — Wang's arithmetic escape, if any, must be collective and must survive derivative repayment

**Evidence level:** exact/literature-backed synthesis from VIS-313--[VIS-337](../../findings/VIS-337-wang-prime-power-jump-derivative-channel.md). No prime-pair asymptotic or RH consequence is claimed.

VIS-330--VIS-334 classify the fixed-source transform: no real log-frequency is annihilated, high frequencies are attenuated by one order, and exact inversion charges one derivative plus memory. VIS-335--VIS-336 show that this derivative tax is sharp generically, including on one increasing-frequency trajectory.

VIS-337 now tests the actual squared-von-Mangoldt source. Distributionally, for `F(u)=e^{-u}E_A(e^u)` one has `(1+D)F=mu-u du`, and Wang's output satisfies `(4-D^2)Q=4(mu-u du)`. Every prime-power jump is copied exactly into the derivative channel: `Delta Q'(log n)=-4 Lambda(n)^2/n`. Thus the arithmetic staircase really does populate the carrier that the inverse charges.

But an individual prime-power atom has size at most `u^2 e^{-u}`, exponentially below the current Korobov--Vinogradov normalized envelope. A bounded number of isolated jumps therefore cannot realize the useful scale migration exhibited by the abstract chirps. Any source-specific gain must come from a **collective signed organization of many prime-power atoms against the continuous baseline**, large enough to matter at the live envelope scale.

The remaining burden has two independent halves: exhibit such a collective arithmetic packet/phase/multiscale imbalance, and then verify that Wang's complete destination consumes the smaller `Q` without requiring `Q'` or equivalent unsmoothed information that reconstructs the larger source scale.

**Boundary.** Fine staircase singularity by itself is not evidence of useful frequency migration. VIS-337 neither bounds collective blocks nor proves a Wang gain; it only removes isolated prime-power jumps as the scale-carrying mechanism.