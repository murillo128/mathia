# MI-032 — Adaptive reserve lifting needs a bounded retained tail; otherwise the comparison manufactures its own negative spectrum

**Evidence level:** exact-derived operator redirect from [WI-307](../../findings/WI-307-exterior-reserve-lifting-removes-the-fixed-essential-obstruction.md), strengthened by the source-exact clipped-tail decomposition [WI-308](../../findings/WI-308-clipped-source-tail-gives-a-coercive-fredholm-witness.md), the aperture-uniform endpoint-singular construction [WI-309](../../findings/WI-309-endpoint-singular-localizers-give-a-uniform-clipped-tail-gap.md), and the bounded-tail correction [WI-310](../../findings/WI-310-capped-clipped-tail-preserves-gap-without-endpoint-overcharge.md), refining the frozen-reserve essential-band results WI-304--WI-306.

WI-307 shows that the negative essential band of the frozen `beta_0=1/16` comparison is not invariant. At every fixed aperture, the unbounded unit-window archimedean symbol allows the exterior reserve to be raised so that the essential spectrum of the bounded comparison is strictly positive and only a finite discrete negative sector remains.

WI-308 keeps the clipped-away source rather than replacing it by an arbitrary patch. The omitted positive tail becomes an exact Fourier multiplier. WI-309 then chooses an aperture-adaptive compactly supported localizer whose endpoint singularity approaches the `L^2` boundary, obtaining the uniform lower floor

`T_(chi_B,B) >= c_0 I`,  `c_0=1/(64 pi e)`.

Taken alone, that looked as if the only remaining price were the degrading compact correction. WI-310 shows that the uncapped split has a more basic representation instability. The reserve gate used by WI-307/WI-309 forces `B->infinity`, while the full clipped excess `q_B=(sigma_1-B)_+` produces a localized multiplier that grows like `1/eta_B` on every fixed bounded frequency region. Since the exact source form `Q` stays fixed in

`Q=D_(L,chi_B,B)+T_(chi_B,B)`,

fixed-test Rayleigh quotients of `D` tend to `-infinity`. The adaptive uncapped comparison therefore acquires arbitrarily deep **discrete negative modes even independently of RH**. Asking for a uniform lower bound on that `D` confuses a bookkeeping overcharge with source geometry.

The exact repair is to cap the retained positive excess:

`qhat_B=min(q_B,1/2)`.

Sliding localization remains source-exact,

`Q=Dhat_(L,chi_B,B)+That_(chi_B,B)`,

and now

`c_0 I <= That <= (1/2) I`.

The lower floor survives because the cap is already `1/2` on the exterior tail used by WI-309. The upper bound is equally important: it prevents the positive summand from diverging and forcing the complementary comparison negative by construction. Since `Dhat>=D`, the reserve gate still gives finite negative index at each aperture.

The reusable operator lesson is sharper than “adaptation moves the cost into the compact sector.” **An exact positive remainder must be controlled from both below and above if the complementary operator is to carry meaningful spectral information uniformly across the family.** A diverging positive summand can create arbitrarily deep negative spectrum in its complement while the original source form is unchanged. Only after representation stability is enforced does the compact/discrete sector become an interpretable arithmetic gate.

Under an RH failure, the first-crossing argument still forces a capped-comparison direction with depth at least `c_0`; the cap does not erase the witness. The live theorem is whether the finite negative spectrum of `Dhat` can be controlled uniformly against that fixed margin as aperture grows and the localizer approaches its endpoint-singular profile.

**Boundary.** WI-310 is not a positivity theorem. It removes an artificial large-negative-depth mechanism from the adaptive coordinates and preserves finite negative index plus the uniform RH-failure witness. The capped compact sector may still defeat the comparison, and the eventual argument must still pass the signed-density quotient of WI-241.
