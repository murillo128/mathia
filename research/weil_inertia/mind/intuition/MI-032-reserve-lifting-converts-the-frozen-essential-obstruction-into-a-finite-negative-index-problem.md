# MI-032 — Adaptive reserve lifting yields a uniform clipped-tail gap; the remaining bill is the finite compact sector

**Evidence level:** exact-derived operator redirect from [WI-307](../../findings/WI-307-exterior-reserve-lifting-removes-the-fixed-essential-obstruction.md), strengthened by the source-exact clipped-tail decomposition [WI-308](../../findings/WI-308-clipped-source-tail-gives-a-coercive-fredholm-witness.md) and the aperture-uniform endpoint-singular construction [WI-309](../../findings/WI-309-endpoint-singular-localizers-give-a-uniform-clipped-tail-gap.md), refining the frozen-reserve essential-band results WI-304--WI-306.

WI-307 shows that the negative essential band of the frozen `beta_0=1/16` comparison is not invariant. At every fixed aperture, the unbounded unit-window archimedean symbol allows the exterior reserve to be raised so that the essential spectrum of the bounded comparison is strictly positive and only a finite discrete negative sector remains.

WI-308 keeps the clipped-away source rather than replacing it by an arbitrary patch. The omitted positive tail becomes an exact Fourier multiplier `T_(chi,B)` with strictly positive scalar bottom `c_(chi,B)`. Fixed-aperture positivity is therefore the finite-sector inequality `lambda_min(D)>=-c_(chi,B)`.

WI-309 makes that source-tail margin uniform. For each clipping level, choose a compactly supported localizer whose endpoint singularity exponent approaches the `L^2` boundary. Its Fourier tail has the form `|F_chi(s)|^2` comparable from below to `eta s^(-1-eta)` at large `s`; integrating from the exponentially remote clipping radius cancels the small factor `eta`. With `B_L=P_L+1`, this yields the aperture-independent bound

`T_(chi_L,B_L) >= c_0 I`,  `c_0=1/(64 pi e)`,

while `sigma_ess(D_(L,chi_L,B_L)) subset [1,infinity)`. A first RH-failure crossing at any finite aperture must therefore force

`lambda_min(D_(L,chi_L,B_L)) <= -c_0`.

The tail reserve is no longer the quantitatively vanishing part of the argument. The price has moved into the adaptive localizer itself. As its endpoint singularity approaches the square-integrability threshold, the localization-defect compact correction loses regularity. Compactness survives at every finite aperture, but WI-309 does not uniformly control the depth or multiplicity of the finite negative spectrum.

The reusable operator lesson is that **a uniform coercive remainder can be bought by adapting the representation, but the cost may reappear in the compact sector rather than in the essential spectrum**. The correct global comparison must price both sides of that trade simultaneously; optimizing only the tail floor is incomplete.

**Boundary.** WI-309 is not a proof of Weil positivity and does not show `lambda_min(D)>=-c_0`. The endpoint-singular localizers are legal in the closed logarithmic form domain and preserve the Fredholm decomposition, but the finite compact sector may still defeat the fixed gap. Frozen-reserve obstructions remain valid for their own comparison but no longer characterize the adaptive architecture.
