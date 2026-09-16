# MI-032 — Adaptive reserve lifting needs a bounded retained tail; flattening that tail forces compact-sector complexity

**Evidence level:** exact-derived operator redirect from [WI-307](../../findings/WI-307-exterior-reserve-lifting-removes-the-fixed-essential-obstruction.md), strengthened by the source-exact clipped-tail decomposition [WI-308](../../findings/WI-308-clipped-source-tail-gives-a-coercive-fredholm-witness.md), the aperture-uniform endpoint-singular construction [WI-309](../../findings/WI-309-endpoint-singular-localizers-give-a-uniform-clipped-tail-gap.md), the bounded-tail correction [WI-310](../../findings/WI-310-capped-clipped-tail-preserves-gap-without-endpoint-overcharge.md), the smooth frequency-multiplexing saturation theorem [WI-311](../../findings/WI-311-smooth-frequency-multiplexing-flattens-capped-tail-to-source-shift.md), and the anti-concentration/Hilbert--Schmidt obstruction [WI-312](../../findings/WI-312-anti-concentration-forces-archimedean-hs-blowup.md), refining the frozen-reserve essential-band results WI-304--WI-306.

WI-307 shows that the negative essential band of the frozen `beta_0=1/16` comparison is not invariant. At every fixed aperture, the unbounded unit-window archimedean symbol allows the exterior reserve to be raised so that the essential spectrum of the bounded comparison is strictly positive and only a finite discrete negative sector remains.

WI-308 keeps the clipped-away source rather than replacing it by an arbitrary patch. The omitted positive tail becomes an exact Fourier multiplier. WI-309 then chooses an aperture-adaptive compactly supported localizer whose endpoint singularity approaches the `L^2` boundary, obtaining a uniform positive tail floor.

Taken alone, that looked as if the only remaining price were the degrading compact correction. WI-310 shows that the uncapped split has a more basic representation instability. The reserve gate forces the retained excess to diverge on fixed frequency regions, and because the exact source form stays fixed in `Q=D+T`, fixed-test Rayleigh quotients of the complement tend to `-infinity`. The repair is to cap the retained positive excess at `1/2`, keeping the source-exact split

`Q=Dhat+That`,

with a positive lower floor and the crucial upper bound `That<=(1/2)I`.

WI-311 adds a second adversarial correction. Endpoint singularity is **not** necessary for a uniform floor. At every fixed aperture, a finite family of smooth real unit-window localizers with widely separated carrier frequencies can satisfy

`1/2(1-1/(2N)-epsilon) I <= That_(N,epsilon) <= (1/2) I`.

Hence `That_(N,epsilon)` can converge in operator norm to `(1/2)I`, while the exact source identity simultaneously forces

`Dhat_(N,epsilon) -> Q-(1/2)I`.

A stronger positive remainder can therefore be representationally empty: its complement approaches the original unknown source after a scalar shift.

WI-312 makes the hidden compact-sector price quantitative and representation-independent within the smooth multiplexed route. Let `mu` be the normalized aggregate frequency-energy law of the localizers, `R(a)=int cos(as) mu(ds)` its autocorrelation, and `Q_mu(h)` its concentration function. For the continuous archimedean localization correction

`C_R=int_0^(2L) (1-R(a)) kappa(a) J_a da`,

with `kappa(a)~1/a` near zero, anti-concentration `Q_mu(h)<=eta<=1/8` gives

`||C_R||_HS^2 >= (2L-delta)/2 * (pi h/(128 eta)-1/delta)`

for fixed admissible `delta`. Thus the same frequency spreading that flattens the capped tail forces `||C_R||_HS->infinity` as `eta->0`. In WI-311's family, making the retained tail arbitrarily close to `(1/2)I` therefore necessarily drives the continuous archimedean compact component to infinite Hilbert--Schmidt complexity.

This is stronger than the earlier qualitative statement that carrier frequencies and derivatives become large. The trade is structural: **tail flattening by frequency anti-concentration spends compact-sector Schatten complexity.** The exact energy-distance identity behind WI-312 shows that this is not an artifact of the explicit cosine--sine windows.

The reusable operator lesson now has three parts. First, an exact positive remainder must be bounded both below and above if the complementary operator is to carry meaningful spectral information uniformly. Second, even a bounded remainder can become vacuous if it approaches a scalar multiple of the identity and the complement approaches `Q-cI`. Third, a representation that achieves that flattening by frequency spreading may necessarily make a compact component large in `S_2`, so “smooth localizers” do not imply controlled compact complexity.

WI-312 closes only a componentwise Hilbert--Schmidt route. It does not prove divergence of the full compact correction, operator norm, negative index, or negative depth: continuous and discrete pieces may cancel, and another invariant may control the finite sector without uniformly bounding each component. The same lower bound rules out uniform `S_p` control for `p<=2` whenever those norms are finite, but it leaves weaker/non-componentwise control logically open.

The live theorem is therefore an **independent source-specific control of the recombined finite negative sector** that survives the actual localizer degeneration without becoming equivalent to proving `Q>=0` or demanding uniform componentwise `S_2` bounds contradicted by WI-312. Any useful invariant must exploit cancellation/structure of the full correction rather than merely shrinking the retained-tail error.

**Boundary.** WI-310--WI-312 are not positivity theorems. They remove misleading coordinate narratives—unbounded retained-tail overcharge, apparent necessity of endpoint singularity, and the hope that smooth frequency flattening keeps the compact archimedean component uniformly simple. They do not rule out cancellation between compact pieces, uniform negative-index control, a useful operator-norm theorem, or a different source-valid decomposition. The signed-density quotient of WI-241 remains downstream.
