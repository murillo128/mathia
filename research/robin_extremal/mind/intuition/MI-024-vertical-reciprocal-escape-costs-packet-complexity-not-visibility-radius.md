# MI-024 — Vertical reciprocal escape costs packet complexity, not visibility radius

**Evidence level:** literature-backed exact Turan--Nazarov splice from [RE-137](../../findings/RE-137-turan-nazarov-makes-vertical-escape-pay-in-packet-complexity.md), refining the isotropic radius law RE-136 for the leading Robin packet

RE-136 treats horizontal and vertical displacement symmetrically through one reciprocal-box radius. RE-137 shows that this is too coarse for the leading Robin coefficient law. Turan--Nazarov observability plus the common sector of the coefficients gives a lower bound

`sup |S_(C,0)| >= c_(Theta,kappa) exp(-H_C(U)-C_kappa N) |a_(rho_0,0)(U)|`,

where `H_C(U)=U max|beta-beta_0|` is the scaled **horizontal** spread and `N=#C`. No vertical-diameter term appears.

Thus a bounded-complexity packet cannot hide merely by sending ordinates far apart. Uniform suppression on a macroscopic window must pay through horizontal spread and/or the number of cooperating modes. For fixed finite order `K`, the same mechanism survives under an explicit logarithmic budget relating horizontal spread, packet size and the strength of the distinguished atom.

Matched purely vertical product packets show that the complexity term is real rather than a proof artifact: with zero horizontal spread, sufficiently many vertically organized modes can still hide. So RE-137 does not replace noncompactness by tightness; it identifies the anisotropic currency in which the escape is paid.

The source-side question is therefore sharper than bounding reciprocal radius. One needs information controlling **how many relevant off-critical modes can cooperate at comparable horizontal depth**, or forcing enough horizontal spread that the exponential tariff already defeats the target atom. Vertical height/diameter by itself is not the right variable for the leading packet.

**Boundary.** The clean vertical-diameter-free estimate is for the leading `K=0` packet; finite-order transfer has additional budget conditions. The result does not bound the actual number of zeta zeros in the cooperating packet or prove that the matched vertical constructions occur for actual zeros.