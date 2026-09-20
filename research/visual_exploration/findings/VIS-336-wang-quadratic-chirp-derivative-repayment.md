# VIS-336 — a single quadratic chirp realizes Wang high-frequency attenuation with derivative repayment

## Claim

Use the physical half-line Wang source transform from `VIS-333` and `VIS-335`. Let

`F(u)=exp(i u^2/2)` for `u>=0`,

so the instantaneous log-frequency is the single increasing trajectory

`omega(u)=u`.

Define

`Q(u)`
` = - integral_0^u e^(-2(u-v)) F(v) dv`
`   + 3 integral_u^infinity e^(-2(v-u)) F(v) dv`.

Then, as `u->infinity`,

`Q(u)/F(u)`
` = 4i/u + 4/u^2 + (4-16i)/u^3 + O(u^-4)`,

and therefore

`|Q(u)| = 4/u + O(u^-2)`.

At the same time,

`Q'(u)/F(u) = -4 + 4i/u + O(u^-2)`,

so

`|Q'(u)| = 4 + O(u^-1)`.

Thus the `Q`-small / `Q'`-large regime isolated by `VIS-334` and realized in `VIS-335` by a family of fixed-frequency modes also occurs on one nonstationary source trajectory whose local frequency tends to infinity. The one-order high-frequency attenuation is not an artifact of comparing different sources indexed by `omega`; a single chirp can continuously move its scale into the derivative channel.

The adiabatic ratio for this control is

`omega'(u)/omega(u)^2 = 1/u^2 -> 0`.

This identifies a clean generic model for the remaining arithmetic question: increasing log frequency can produce pointwise Wang attenuation while differentiation repays the hidden scale, but nothing here shows that the actual squared-von-Mangoldt remainder has such a chirp-like decomposition or that Wang's final destination avoids the derivative cost.

**Evidence/status:** `EXACT-DERIVED ASYMPTOTIC + SINGLE-TRAJECTORY NONSTATIONARY CONTROL + FILTER-BOUNDARY RESULT + NO-ARITHMETIC-CLAIM + NO-NOVELTY-CLAIM`.

## 1. Reduce the two tails to endpoint Fourier integrals

Write `v=u-s` in the past tail and `v=u+s` in the future tail. Since

`F(u-s)/F(u)=exp(-ius+i s^2/2)`

and

`F(u+s)/F(u)=exp(ius+i s^2/2)`,

put

`a(s)=exp(-2s+i s^2/2)`.

Then

`Q(u)/F(u)`
` = - integral_0^u a(s)e^(-ius) ds`
`   + 3 integral_0^infinity a(s)e^(ius) ds`.

Because `|a(s)|=e^(-2s)`, extending the first integral from `u` to infinity changes it by only `O(e^(-2u))`. Hence, with

`J_+(u)=integral_0^infinity a(s)e^(ius) ds`,

`J_-(u)=integral_0^infinity a(s)e^(-ius) ds`,

one has

`Q(u)/F(u) = -J_-(u)+3J_+(u)+O(e^(-2u))`.

All derivatives of `a` are a polynomial in `s` times `a(s)`, hence are integrable on the positive half-line. Repeated endpoint integration by parts therefore gives a full inverse-power expansion.

The standard prior-art boundary is NIST DLMF §2.3(i), "Integration by Parts", especially the endpoint Fourier-integral expansion in Eq. 2.3.4 and its infinite-endpoint variant: <https://dlmf.nist.gov/2.3>.

## 2. The chirp sees the same leading Wang multiplier at its local frequency

At the endpoint,

`a(0)=1`,

`a'(0)=-2`,

`a''(0)=4+i`.

The endpoint expansions are therefore

`J_+(u)`
` = i/u + 2/u^2 + (1-4i)/u^3 + O(u^-4)`,

and

`J_-(u)`
` = -i/u + 2/u^2 + (-1+4i)/u^3 + O(u^-4)`.

Substitution yields

`Q(u)/F(u)`
` = 4i/u + 4/u^2 + (4-16i)/u^3 + O(u^-4)`.

The first two terms agree with the large-frequency expansion of the fixed-mode multiplier from `VIS-333`,

`m(omega)=4(1+i omega)/(4+omega^2)`:

`m(u)=4i/u+4/u^2-16i/u^3+O(u^-4)`.

The quadratic phase curvature first changes the displayed expansion at order `u^-3`, adding the real `4/u^3` term. Thus, at leading order, the filter tracks the instantaneous frequency `omega(u)=u`; the nonstationarity does not destroy the one-order attenuation.

## 3. The derivative still carries the source scale

Split the transform into

`P(u)=-integral_0^u e^(-2(u-v))F(v)dv`,

`R(u)=3integral_u^infinity e^(-2(v-u))F(v)dv`,

so `Q=P+R`. Direct differentiation gives the exact identities

`P'=-F-2P`,

`R'=-3F+2R`,

and hence

`Q'=-4F+2(R-P)`.

The same endpoint expansions give `P=O(u^-1)` and `R=O(u^-1)`. Therefore

`Q'(u)=-4F(u)+O(u^-1)`.

Keeping one more term gives

`Q'(u)/F(u)=-4+4i/u+O(u^-2)`.

So the source has unit modulus, the Wang output decays like `4/u`, and the derivative remains asymptotically at amplitude four. The inverse derivative term from `VIS-334` is again load-bearing.

Taking real parts gives a real-valued control `cos(u^2/2)`: its Wang output is `O(u^-1)`, while the derivative retains order-one oscillation. The complex form is used only to keep phase bookkeeping transparent.

## 4. What this control settles

`VIS-335` proved that a frequency-indexed family `e^(i omega u)` can make `Q` small while leaving `Q'` at source scale. The present result removes the remaining generic objection that this phenomenon might disappear when frequency migration must occur along one source rather than across a family of sources.

The quadratic chirp provides exactly such a single trajectory. Its local frequency grows monotonically, the relative variation over one oscillatory scale satisfies `omega'/omega^2 -> 0`, and the Wang transform follows the local high-frequency multiplier to leading order.

This is still only a matched filter control. It does not identify a chirp decomposition of the arithmetic remainder, prove a Korobov--Vinogradov improvement, or show that the downstream Wang statistic depends only on `Q`. In particular, an argument that obtains a small `Q` but later requires `Q'` at its natural order-one scale has merely postponed the source cost.

## 5. Prior art and novelty boundary

The endpoint expansion used above is standard oscillatory-integral asymptotics by repeated integration by parts; DLMF §2.3(i) is an authoritative reference. Likewise, the broad signal-processing statement that a smooth linear filter responds locally according to its frequency response on a slowly varying chirp is standard background.

No general chirp theorem, pseudodifferential theorem, or new filter principle is claimed. The durable content here is the explicit specialization to the exact Wang half-line kernel, including its physical boundary truncation, the first curvature correction, and the derivative-repayment balance needed by the active Mathia clue.

## Dependencies

- `VIS-333`: exact Wang real log-frequency multiplier.
- `VIS-334`: exact causal inverse and derivative tax.
- `VIS-335`: fixed-frequency high-frequency matched control.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose surviving route requires nonstationary frequency migration without downstream repayment.

## Research consequence

The accepted Wang clue should no longer spend effort asking whether a **single** scale-migrating trajectory can realize the filter-level asymmetry. It can: the quadratic chirp has `Q=O(u^-1)` and `Q'=-4F+O(u^-1)`.

The next meaningful step must add arithmetic or destination information. Either prove that the actual normalized squared-von-Mangoldt remainder contains a quantitatively useful increasing-log-frequency component under a decomposition strong enough to control the residual, or show directly that Wang's complete downstream error budget necessarily reintroduces the derivative-sized carrier. Further generic chirp examples would not by themselves advance the active question.