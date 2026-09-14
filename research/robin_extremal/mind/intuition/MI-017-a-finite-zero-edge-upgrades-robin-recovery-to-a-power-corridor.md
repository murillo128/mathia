# MI-017 — The attained-edge selector and its macroscopic recovery are one stable-filter lobe

**Evidence level:** exact consequence of RE-112--[RE-117](../../findings/RE-117-finite-edge-robin-recovery-profiles-collapse-to-stable-filter-positive-lobes.md). No contradiction with false RH or density theorem for actual selected CA blocks is claimed.

Let `Theta=sup Re(rho)` be attained with `1/2<Theta<1`, write `c=1-Theta`, and use the edge profiles `F=F_Theta`, `G=G_Theta`, `J=F+G`. RE-114--RE-116 show that fixed mixed rays, the adaptive edge-normalized ray and its exact self-consistent moving exponent are all realized at positive syndetic phases.

RE-117 shows that the later recovery corridor does not add another leading state. For an adaptive witness `C`, put `Y=log C`, `U=log Y`; for a later CA state with `X=log N` and `t=log(X/Y)` in a fixed bounded interval,

`Y^c log Y (h(C)-h(N)) = int_0^t e^(-cs) F(U+s) ds + o(1)`.

Because the stable filter satisfies

`J(U)=int_0^t e^(-cs)F(U+s)ds + e^(-ct)J(U+t)`,

the selector normalization collapses the complete recovery profile to

`Y^c log Y h(N)=e^(-ct)J(U+t)+o(1)`.

Hence a first later nonpositive CA state is, at leading edge scale, a first zero at the end of a positive `J`-lobe. This looks stronger than the endpoint ray but is still spectrally noncoercive: RE-117 proves that for every fixed admissible selector parameter there are syndetically many exact selector roots with `J(u)` bounded below, followed at a bounded positive distance by the first zero of `J`.

The key representation lesson is that **macroscopic recovery is reconstructible from the same stable-filter state that already controls the endpoint**. Integrating the edge profile over a fixed multiplicative corridor does not manufacture a new source coordinate; it only compares two shifted samples of `J`.

The live obstruction must therefore be arithmetic rather than spectral-existence at this scale: actual CA selector placement inside the compatible positive lobes, a sharper law for the exact recovery endpoint, or lower-order/discrete information invisible to the leading almost-periodic state. Another fixed stable linear filtering of `F` cannot by itself escape this closure.

**Boundary.** Syndetic compatible lobes do not show that the arithmetic selectors land in them. The `Theta=1` branch remains separate, and RE-117 concerns fixed multiplicative recovery corridors on an attained finite edge.
