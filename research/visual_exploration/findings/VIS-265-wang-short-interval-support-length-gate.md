# VIS-265 — Wang's short-interval Montgomery theorem forces a support-length tradeoff and does not reach the bounded-tent edge regime

## Claim

Biao Wang's 2026 short-interval pair-correlation theorem gives a new local-height prior-art boundary for the accepted Montgomery support-edge thread, but it does not supply the transfer needed by the bounded-source-tent construction of `VIS-128` or the lower-order arithmetic carrier of `VIS-260`--`VIS-264`.

Let

`I=(T,T+H]`, `H=T^theta`, `L=log T`,

with fixed `0<theta<1`. Wang's Theorem 2.2 states that for every fixed `0<lambda<theta` and fixed real even `g in C_c^infinity(R)` with

`supp(g) subset [-lambda,lambda]`,

one has

`sum_(gamma,gamma' in I) hat g(i(rho-rho')L/(2*pi)) w(rho-rho')`
` = (H L/(2*pi)) [g(0)+ integral_R |alpha| g(alpha) d alpha]`
`   + O_g(H + T^lambda L^2)`,

where `w(z)=4/(4-z^2)` and the theorem is unconditional.

After normalization by the natural main scale `H L`, the certified error is therefore

`O_g(1/L + T^(lambda-theta) L)`.

This produces two exact application gates.

First, **frequency support consumes source-window exponent**: a pair-frequency test reaching radius `a>0` can be covered only after choosing a fixed `lambda>=a` and then a strictly larger interval exponent `theta>lambda`. In particular, a probe approaching the Montgomery edge `a=1-epsilon` requires

`theta > 1-epsilon`

with a positive fixed support margin. As `epsilon -> 0`, the theorem forces `theta -> 1`; the admissible source interval becomes nearly macroscopic in exponent.

Second, the theorem's normalized `O(H)` remainder already contributes `O(1/L)`. Consequently Theorem 2.2 by itself cannot identify a deterministic lower-order coefficient whose normalized size is only `c/L`: its stated error is on the same scale. A sharper local theorem is required before a `1/log T` arithmetic residual can be assigned a coefficient from this result alone.

The bounded tent of `VIS-128` has fixed physical source width `H_src`, so its effective power exponent satisfies

`log(H_src)/log(T) -> 0`.

The same is true for any polylogarithmic physical window. Wang's theorem assumes a fixed positive `theta` and requires `lambda<theta`; it therefore gives no fixed positive pair-frequency support for the `VIS-128` bounded-window regime. The new short-interval theorem genuinely narrows the old global-versus-local gap, but it does not close the specific localization gate used by the visual support-edge statistic.

**Evidence/status:** `LITERATURE+DERIVED + NEW PRIOR-ART BOUNDARY + SUPPORT/LOCALIZATION TRADEOFF + NEGATIVE TRANSFER GATE + NO-NOVELTY-CLAIM`.

No new pair-correlation theorem, short-interval theorem, lower-order arithmetic term, moving-edge estimate, or RH implication is claimed.

## 1. Wang supplies genuine local-height pair correlation

The relevant new source is:

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918 (submitted 7 September 2026), especially Theorem 2.2.

The theorem works with zeros whose ordinates lie in the actual short interval `I=(T,T+T^theta]`, rather than only a global average up to height `T`. This is materially closer to the source-window question left open in `VIS-128` and `VIS-260` than the global fixed-weight Rodgers theorem.

Its main term is Montgomery's leading pair-correlation functional on the fixed Fourier-support class `supp(g) subset [-lambda,lambda]`, and its error is explicit:

`O_g(H + T^lambda L^2)`.

Dividing by `HL/(2*pi)` gives, up to a fixed constant,

`O_g(1/L + T^(lambda-theta)L)`.

Because `lambda<theta` is fixed, the second term tends to zero. Thus the theorem genuinely resolves the leading Montgomery statistic in every fixed power-length interval once the frequency support stays strictly below the interval exponent.

## 2. The theorem encodes a support-length uncertainty law

The condition `lambda<theta` is not cosmetic. It is exactly what makes

`T^lambda L^2 = o(T^theta L)`.

Suppose a predeclared pair-frequency test has support reaching some fixed radius `a`. To place the whole test inside Wang's theorem one needs a fixed `lambda>=a`, hence necessarily

`theta>a`.

For a support-edge probe at

`a=1-epsilon`,

this becomes

`theta>1-epsilon`.

Therefore shortening the source-height interval and approaching the Montgomery support edge pull in opposite directions under this theorem. A theorem-valid probe with `theta=1/2`, for example, cannot reach pair-frequency support beyond any fixed `lambda<1/2`. Conversely a test with support arbitrarily close to `1` requires intervals whose power exponent is arbitrarily close to `1`.

This is a theorem-specific design law, not a claim that all possible pair-correlation methods must obey the same boundary. It says exactly what the current short-interval Montgomery theorem certifies.

## 3. The bounded tent lies outside the power-length regime

`VIS-128` deliberately chose a bounded physical source support `H_src` so that its unfolded length is

`M=H_src L_T/(2*pi)`

and the corresponding finite-CUE arc remains capacity-compatible. Here `H_src` is fixed independently of fresh zero data.

A fixed physical interval is not `T^theta` for any fixed `theta>0`. Its effective exponent

`theta_eff(T)=log(H_src)/log T`

tends to zero. A polylogarithmic physical width likewise has `theta_eff(T)->0`.

Hence Wang's fixed-parameter condition `0<lambda<theta` cannot certify any fixed positive pair-frequency support in this regime. In particular it cannot be invoked to justify the bounded-tent statistic merely because it is a theorem "in short intervals".

The distinction is structural. `VIS-128` chose bounded source support precisely to control finite-CUE capacity and universal source-window leakage. Wang's theorem localizes the zero set substantially relative to a global interval, but only to power-length windows; it does not reach the bounded or polylogarithmic localization used by that null construction.

## 4. Its stated error does not resolve a `1/log T` coefficient

Even in the admissible power-length regime, the normalized theorem remainder contains

`O(H)/(HL)=O(1/L)`.

The accepted support-edge clue explicitly treats `1/L_T` as one natural candidate scale after universal finite-size, Montgomery-weight, and source-taper effects are matched. Therefore Wang's Theorem 2.2 alone cannot decide a coefficient at that same normalized scale. A statement

`observable = universal leading term + c/L + o(1/L)`

cannot be read from an estimate whose certified remainder is only `O(1/L)`.

This does not say the actual short-interval error is of order `1/L`, only that the published bound does not separate a deterministic `1/L` term from its remainder. The prime-power curvature channel isolated in `VIS-264` is a lower-order source-specific object, so transferring it into a local-height support-edge statistic needs a refinement that preserves lower-order arithmetic information, not merely the leading Montgomery main term.

## 5. Relation to the current visual thread

The result updates two previously separate boundaries.

`VIS-128` established that a fixed physical source tent is a clean finite-CUE design because it avoids the growing-hard-window capacity failure, while retaining an explicit universal `1/L_T` correction. `VIS-260`--`VIS-264` established, in Rodgers' fixed smooth global-average framework, that cusp-adapted low-frequency packets can survive theorem error and that the quadratic Bogomolny--Keating-minus-GUE carrier splits into a DC pole-compensation term plus discrete prime-power curvature samples.

Wang's new theorem sits between those regimes. It proves that meaningful pair-correlation localization in the source-height variable is possible on `T^theta` intervals, but its own support law `lambda<theta` and its normalized `O(1/L)` error prevent it from serving as the missing direct bridge to the fixed-width tent or to a resolved `1/L` lower-order arithmetic coefficient.

There is also a representation distinction that must remain explicit: the source-height interval/taper controls **which zeros in height are sampled**, whereas the Rodgers weight `omega(u)` in `VIS-260`--`VIS-264` weights the **pair-separation variable**. A theorem for one cannot be converted into the other by identifying the two weights. A faithful application needs both the desired source localization and a pair-separation test class, with a transfer theorem controlling them simultaneously.

## Prior-art and novelty assessment

Wang's short-interval theorem is prior art and is the load-bearing new source here. It follows the unconditional Montgomery method of Baluyot, Goldston, Suriajaya, and Turnage-Butterbaugh and is explicitly presented as a short-interval counterpart of that work.

The deductions `lambda<theta`, the normalized error `O(1/L + T^(lambda-theta)L)`, and the resulting incompatibility with a fixed physical `H_src` are direct algebraic consequences of the theorem's stated parameters. No novelty is claimed for the general principle that localization and Fourier resolution trade against one another, and no claim is made that Wang's condition is an optimal impossibility boundary for all future methods.

The Mathia-specific value is to place the newly available September 2026 theorem into the already frozen support-edge representation and show exactly which open gate it narrows and which ones it leaves untouched.

## Boundary and falsification

This finding uses Wang's Theorem 2.2 as stated for fixed `theta`, fixed `lambda`, and fixed smooth compactly supported `g`. It does not extrapolate the implied constants to `theta_T`, `lambda_T`, or an edge margin changing with `T`.

The hard interval `I=(T,T+H]` in Wang's theorem is not the same source weighting as the centered tent of `VIS-128`. A smooth-taper variant may well be derivable in a comparable power-length regime, but such a derivation would not remove the support exponent issue and is not claimed here.

The theorem is stronger than needed for some leading-order local questions and weaker than needed for the present lower-order one. Finding a later theorem with fixed/polylogarithmic height localization, support reaching the required pair frequencies, and an error `o(1/L)` after the exact statistic normalization would invalidate the present transfer obstruction for that theorem and should trigger a direct re-audit.

No untouched confirmation-zero data are used.

## Research consequence

The accepted Montgomery support-edge branch should no longer describe the localization gap as simply "global theorem versus local window": Wang now supplies a genuine power-short-interval Montgomery theorem. The remaining gate is sharper.

For the original near-edge statistic, any attempt to use Wang 2026 must expose the support radius and the source-window exponent together. Approaching `|alpha|=1` under this theorem forces a source interval with exponent approaching one, so it cannot justify the bounded `H_src` tent construction. For a lower-frequency redesign inside a power-length interval, Wang's result can be a leading-order control, but a `1/L` arithmetic residual still needs an improved remainder or a theorem carrying the lower-order term explicitly.

The next coherent source-side target is therefore a genuinely localized lower-order pair-correlation statement: either a bounded/polylogarithmic-height transfer compatible with the `VIS-128` source taper, or a power-short-interval theorem that retains the Bogomolny--Keating/prime-power correction with error smaller than the intended residual scale. Until such a bridge exists, the exact prime-power channel in `VIS-264` remains a fixed-weight calibration rather than a validated bounded-window support-edge prediction.
