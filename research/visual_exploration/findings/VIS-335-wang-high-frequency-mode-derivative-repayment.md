# VIS-335 — Wang attenuation of a high-frequency mode is exactly paid by the log derivative

## Claim

Use the physical half-line Wang source transform from `VIS-333`. For a frequency parameter `omega>0`, take the bounded model source

`F_omega(u)=e^(i omega u)` for `u>=0`

and zero for `u<0`. Define

`Q_omega(u)`
` = - integral_0^u e^(-2(u-v)) F_omega(v) dv`
`   + 3 integral_u^infinity e^(-2(v-u)) F_omega(v) dv`

for `u>=0`.

Then the transform is explicit:

`Q_omega(u)=m(omega)e^(i omega u)+e^(-2u)/(2+i omega)`,

where

`m(omega)=4(1+i omega)/(4+omega^2)`.

Consequently,

`sup_(u>=0) |Q_omega(u)| = O(omega^(-1))`

as `omega->infinity`, while

`Q_omega'(u)=i omega m(omega)e^(i omega u)-2e^(-2u)/(2+i omega)`

and

`lim_(u->infinity) |Q_omega'(u)| = |omega m(omega)| -> 4`.

Thus the transform-level high-frequency escape left open by `VIS-334` is genuinely nonempty: a source family of unit pointwise size can have Wang output tending uniformly to zero while the first log derivative keeps order-one size. The inverse derivative tax is therefore sharp on the simplest high-frequency control; the missing source scale is not destroyed, it is moved from `Q` into `Q'`.

Taking real parts gives the same conclusion for the real-valued controls `cos(omega u)`: the Wang output has amplitude `O(omega^(-1))`, but the derivative has asymptotic oscillation amplitude `|omega m(omega)| -> 4` away from the exponentially decaying boundary transient.

**Evidence/status:** `EXACT-DERIVED + HIGH-FREQUENCY MATCHED CONTROL + FILTER-BOUNDARY RESULT + NO-ARITHMETIC-CLAIM + NO-NOVELTY-CLAIM`.

This is not evidence that the actual squared-von-Mangoldt remainder has frequency migration, nor that Wang's complete downstream statistic avoids derivative-sensitive terms. It proves only that the surviving asymmetry in `VIS-334` is structurally possible for the exact Wang filter and identifies its sharp scale on a canonical mode family.

## 1. Exact half-line calculation

For the past tail, set `s=u-v`. Then

`- integral_0^u e^(-2(u-v))e^(i omega v)dv`
` = -e^(i omega u) integral_0^u e^(-(2+i omega)s)ds`
` = -e^(i omega u)/(2+i omega) + e^(-2u)/(2+i omega)`.

For the future tail, set `s=v-u`. Then

`3 integral_u^infinity e^(-2(v-u))e^(i omega v)dv`
` = 3e^(i omega u) integral_0^infinity e^(-(2-i omega)s)ds`
` = 3e^(i omega u)/(2-i omega)`.

Adding them gives

`Q_omega(u)`
` = [3/(2-i omega)-1/(2+i omega)]e^(i omega u)`
`   + e^(-2u)/(2+i omega)`
` = m(omega)e^(i omega u)+e^(-2u)/(2+i omega)`.

The first coefficient is exactly the real-frequency transfer multiplier from `VIS-333`; the second term is only the physical `u=0` support transient.

## 2. One-order attenuation of `Q`

The mode multiplier has exact modulus

`|m(omega)| = 4 sqrt(1+omega^2)/(4+omega^2)`.

Hence `|m(omega)|=4/omega+O(omega^(-3))`, while

`|1/(2+i omega)| = O(omega^(-1))`.

Therefore the complete physical half-line output satisfies

`sup_(u>=0)|Q_omega(u)| = O(omega^(-1))`.

This is a genuine pointwise transform gain relative to `|F_omega|=1`; it does not rely on cancellation between separated observation points or on an `L^2` norm.

## 3. The derivative restores the source scale

Differentiating the exact expression gives

`Q_omega'(u)=i omega m(omega)e^(i omega u)-2e^(-2u)/(2+i omega)`.

The transient vanishes as `u->infinity`, and

`|omega m(omega)|`
` = 4 omega sqrt(1+omega^2)/(4+omega^2)`
` -> 4`.

Thus `Q_omega'` does not share the `omega^(-1)` gain. For the real source `cos(omega u)`, the asymptotic periodic part of the derivative has amplitude `|omega m(omega)|`, so

`limsup_(u->infinity) |(Re Q_omega)'(u)| = |omega m(omega)| -> 4`.

This is exactly the asymmetry required by the escape clause in `VIS-334`: the output can be small because the local log frequency is large, while differentiating multiplies by that same frequency and recovers the unsmoothed scale.

## 4. Sharpness of the inverse derivative tax

`VIS-334` gives, on the physical half-line,

`F(u)`
` = [Q(u)-Q'(u)]/4`
`   + [Q(0)e^(-u)]/4`
`   + (3/4) integral_0^u e^(-(u-v))Q(v)dv`.

For the present family, `Q=O(omega^(-1))` uniformly. The boundary term is also `O(omega^(-1))`, and the exponentially weighted memory of `Q` is `O(omega^(-1))`. The only order-one term in the inverse is therefore `-Q'/4`.

Equivalently, away from the support boundary and at large frequency,

`Q_omega'(u) = -4F_omega(u) + O(omega^(-1))`

at the level of the mode coefficient. The derivative term in `VIS-334` is not merely a sufficient technical device for inversion; it is asymptotically the load-bearing carrier of the source amplitude on a high-frequency control.

## 5. Prior art and evidence boundary

The underlying phenomenon is standard linear-filter frequency response: a multiplier decaying like `|omega|^-1` attenuates a high-frequency mode by one order, while one differentiation restores that order. No novelty is claimed for this generic principle. The exact constants, support transient, and derivative balance here are obtained directly from the Wang kernel already derived in `VIS-333` and the inverse boundary in `VIS-334`.

The result does not establish any high-frequency law for

`F(u)=e^(-u)E_A(e^u)`

with the actual squared-von-Mangoldt remainder. A frequency-indexed control family is also not yet a theorem about a single nonstationary arithmetic trajectory. In particular, it does not prove that arithmetic energy migrates to `omega=omega(u)->infinity`, that such migration improves the Korobov--Vinogradov envelope, or that Wang's later error decomposition depends only on the smaller `Q` rather than on derivative-sized information.

What it does settle is the filter-level possibility question: the `Q`-small/`Q'`-large regime is real and has exactly the scale predicted by the multiplier and inverse.

## Dependencies

- `VIS-333`: exact Wang summatory log-frequency transfer multiplier.
- `VIS-334`: exact causal inverse and first-derivative tax.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose surviving transform-specific route requires precisely this asymmetry.

## Research consequence

The accepted Wang clue should no longer spend effort asking whether the transform *can* suppress a sufficiently high log-frequency component while retaining its size in `Q'`; this exact control shows that it can, and that the gain is one power of the local frequency.

The live arithmetic question is now narrower. One must prove that the actual normalized squared-von-Mangoldt remainder develops suitable scale-migrating/nonstationary frequency structure, quantify the resulting pointwise reduction of `Q`, and then verify that Wang's complete destination exploits `Q` without reintroducing the order-one derivative carrier. A natural next control is a single slowly varying chirp rather than a frequency-indexed family, but that is a separate investigation and is not needed for the present exact result.
