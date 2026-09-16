# MI-032 — Adaptive reserve lifting needs a bounded retained tail; saturating the tail floor can collapse the comparison back to the source

**Evidence level:** exact-derived operator redirect from [WI-307](../../findings/WI-307-exterior-reserve-lifting-removes-the-fixed-essential-obstruction.md), strengthened by the source-exact clipped-tail decomposition [WI-308](../../findings/WI-308-clipped-source-tail-gives-a-coercive-fredholm-witness.md), the aperture-uniform endpoint-singular construction [WI-309](../../findings/WI-309-endpoint-singular-localizers-give-a-uniform-clipped-tail-gap.md), the bounded-tail correction [WI-310](../../findings/WI-310-capped-clipped-tail-preserves-gap-without-endpoint-overcharge.md), and the smooth frequency-multiplexing saturation theorem [WI-311](../../findings/WI-311-smooth-frequency-multiplexing-flattens-capped-tail-to-source-shift.md), refining the frozen-reserve essential-band results WI-304--WI-306.

WI-307 shows that the negative essential band of the frozen `beta_0=1/16` comparison is not invariant. At every fixed aperture, the unbounded unit-window archimedean symbol allows the exterior reserve to be raised so that the essential spectrum of the bounded comparison is strictly positive and only a finite discrete negative sector remains.

WI-308 keeps the clipped-away source rather than replacing it by an arbitrary patch. The omitted positive tail becomes an exact Fourier multiplier. WI-309 then chooses an aperture-adaptive compactly supported localizer whose endpoint singularity approaches the `L^2` boundary, obtaining the uniform lower floor

`T_(chi_B,B) >= c_0 I`,  `c_0=1/(64 pi e)`.

Taken alone, that looked as if the only remaining price were the degrading compact correction. WI-310 shows that the uncapped split has a more basic representation instability. The reserve gate forces `B->infinity`, while the full clipped excess `q_B=(sigma_1-B)_+` produces a localized multiplier that grows on every fixed bounded frequency region. Since the exact source form `Q` stays fixed in

`Q=D_(L,chi_B,B)+T_(chi_B,B)`,

fixed-test Rayleigh quotients of `D` tend to `-infinity`. The adaptive uncapped comparison therefore acquires arbitrarily deep **discrete negative modes independently of RH**. Asking for a uniform lower bound on that `D` confuses a bookkeeping overcharge with source geometry.

The exact repair is to cap the retained positive excess:

`qhat_B=min(q_B,1/2)`.

Sliding localization remains source-exact,

`Q=Dhat+That`,

and WI-310 gives

`c_0 I <= That <= (1/2) I`.

The upper bound is as important as the lower floor: it prevents the positive summand from diverging and forcing its complement negative by construction. Since `Dhat>=D`, the reserve gate still gives finite negative index at each aperture.

WI-311 adds a second adversarial correction. The endpoint-singular localizer is **not** necessary for a uniform floor. At every fixed aperture, a finite cosine--sine family of smooth unit-window localizers with widely separated carrier frequencies can satisfy

`1/2(1-1/(2N)-epsilon) I <= That_(N,epsilon) <= (1/2) I`.

Hence `That_(N,epsilon)` can converge in operator norm to `(1/2)I`. But the exact source identity then gives simultaneously

`Dhat_(N,epsilon) -> Q-(1/2)I`.

The tail floor can therefore be made almost maximal while the complementary comparison becomes almost exactly the original unknown source shifted by a scalar. A stronger positive remainder is not independent information when the identity forces the negative-sector problem to track it one-for-one.

The reusable operator lesson has two parts. **First, an exact positive remainder must be controlled from both below and above if the complementary operator is to carry meaningful spectral information uniformly. Second, even a bounded remainder can become vacuous if it approaches a scalar multiple of the identity and the complement correspondingly approaches `Q-cI`.** Representation quality must be judged by whether the complement becomes easier for a source-specific reason, not by the size of the positive summand alone.

WI-311 also relocates rather than removes the localizer cost. Smooth frequency multiplexing avoids endpoint singularity, but the carrier frequencies become large and the compact correction acquires high modulation/oscillation complexity. Endpoint regularity and carrier scale are alternative degeneration parameters; neither has yet yielded uniform control of the finite negative sector.

Under an RH failure, the first-crossing argument still forces a negative capped-comparison direction, and the smooth multiplexed family can make its depth approach `1/2`. That is not progress unless the same family admits an independent theorem excluding such negative modes without simply reproving `Q>=0`.

**Boundary.** WI-310--WI-311 are not positivity theorems. They remove two misleading coordinate narratives—unbounded retained-tail overcharge and the apparent necessity of endpoint singularity—and isolate the remaining problem: source-valid uniform control of the finite compact/discrete sector under the actual representation degeneration, followed by the signed-density quotient of WI-241.
