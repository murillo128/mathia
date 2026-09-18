# MI-037 — Laplace-null localization pays an inverse-width conditioning cost

**Evidence level:** exact/literature-transfer synthesis from [VIS-282](../../findings/VIS-282-wang-fixed-source-dirichlet-diagonal-profile.md), [VIS-283](../../findings/VIS-283-wang-fixed-source-cross-frequency-separation.md), and [VIS-284](../../findings/VIS-284-wang-fixed-source-packet-projection-bound.md).

In the fixed compact physical-source regime, the coefficient-scale arithmetic object before packet projection is

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`, with `x=e^(2*pi*q)`.

For any packet family `h_T` with uniformly bounded `L^1` norm and support in one fixed compact `K`, Wang's exact inversion plus the fixed-source field expansion gives

`(2*pi/(HL)) W_I(g_T)`
` = 4*pi (ell_T^2/L^2) <h_T,e^(-4*pi q)>`
`   + (4*pi/L^2) <h_T,Q_gamma(e^(2*pi q))>`
`   + o(L^-2)`.

Thus packetization is a bounded projection of the already isolated source profile; it is not a new coefficient-scale mechanism.

The sharper point appears after the universal Laplace mode is nulled. Put

`w_0(q)=e^(-4*pi q)`,
`R(q)=Q_gamma(e^(2*pi q))/w_0(q)`.

On every fixed compact `K`, `R` is Lipschitz. If a Laplace-null packet `h` is supported in an interval of diameter `b`, then for any point `q_0` in the support,

`<h,Q_gamma> = integral h(q)w_0(q)[R(q)-R(q_0)]dq`,

and therefore

`|<h,Q_gamma>| <= C_K b ||h||_1`.

This gives a direct inverse-conditioning law. If `b->0` while `||h||_1` stays bounded, the coefficient-scale arithmetic response vanishes. To retain a response bounded away from zero, one must pay

`||h||_1 = Omega(1/b)`.

The same norm multiplies any unresolved uniform remainder, so apparent amplification from narrowing a signed packet cannot be credited unless the remainder is quantified strongly enough to survive that amplification. Localization and conditioning are the same tradeoff here.

The remaining possible gain lies outside this compact bounded-projection regime: support approaching a source boundary, support escaping to a moving scale, or a singularly normalized family with a proven quantitative error budget. A future signal is substantive only if it contains a term absent from the established `Q_gamma` projection and remains after charging the packet norm growth.

**Boundary.** The inverse-width estimate is a fixed-compact-source statement. It does not rule out a non-Lipschitz or singular source profile on another scaling, nor does it supply a uniform asymptotic for packet families whose total variation diverges.
