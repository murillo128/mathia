# VIS-417 — Beat scales defeat coarse finite-window amplitude controls

## Claim

For every integer `k>=1`, set `delta=1/(2k)` and

`F_delta(t)=1/2(cos t-cos((1-delta)t))`.

Every member of this family has maximum angular frequency `1`, exactly two cosine modes, coefficient magnitudes `1/2`, long-time mean energy `1/4`, and global supremum `1`. Nevertheless, for every fixed `0<epsilon<1`, the connected component through `t=0` of `{t: |F_delta(t)|<=epsilon}` has length at least `8 epsilon k`.

Therefore those coarse spectral/amplitude statistics do not bound finite-window low-amplitude persistence. Frequency separation, equivalently the beat scale, is an independent control variable for any matched null intended to diagnose long localized suppression in a finite window.

**Evidence/status:** `EXACT-DERIVED + ELEMENTARY BEAT MECHANISM + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

## Exact two-frequency construction

Use the elementary identity

`cos A-cos B=-2 sin((A+B)/2) sin((A-B)/2)`.

Then

`F_delta(t)=-sin((1-delta/2)t) sin(delta t/2)`.

The fast carrier is multiplied by an envelope whose characteristic scale is `1/delta`. No visual judgment is needed for the claim below.

## Fixed coarse statistics

The frequencies are `{1-delta,1}`, so the maximum angular frequency is exactly `1` and the mode count is two. The coefficient magnitudes are `1/2`.

For distinct positive frequencies,

`|F_delta(t)|^2 = 1/4(cos^2 t + cos^2((1-delta)t) - 2 cos t cos((1-delta)t))`.

Long-time averaging sends each squared cosine to `1/2` and the distinct-frequency cross term to zero, giving

`lim_(R->infinity) (1/(2R)) integral_(-R)^R |F_delta(t)|^2 dt = 1/4`.

Also `|F_delta(t)|<=1`. At `t=2 pi k`, because `delta=1/(2k)`,

`cos t=1`,

while

`(1-delta)t=(2k-1)pi`,

so the second cosine is `-1` and `F_delta(t)=1`. Hence the global supremum is exactly `1`; global-sup normalization leaves the family unchanged.

## Arbitrarily long low-amplitude window

From the product identity,

`|F_delta(t)| <= |sin(delta t/2)| <= delta |t|/2`.

Thus if `|t|<=2 epsilon/delta`, then `|F_delta(t)|<=epsilon`. The entire interval belongs to the connected low-amplitude component through zero and has length

`4 epsilon/delta = 8 epsilon k`,

which diverges with `k` while every coarse statistic above remains fixed.

## Consequence for the Wang packet control

The current visual clue `research/visual_exploration/clues/CLUE-wang-fixed-source-packet-localization.md` asks whether source-bearing fixed-source coefficients exhibit localization or persistence that survives comparison against source-free matched ensembles. This exact family supplies a minimum control requirement: a source-free null can manufacture arbitrarily long finite-window low-amplitude regions purely by collapsing a frequency gap, even when bandlimit, mode count, coefficient magnitudes, long-time mean energy, and global-sup normalization are all held fixed.

Therefore a decisive Wang null should either preserve or explicitly control the relevant frequency-gap/beat-scale information, or use a persistence statistic with a proved insensitivity to such beat scales. Matching only the coarser quantities above is insufficient to attribute a long quiet window to source-sensitive packet structure.

Finite-window empirical-max normalization needs extra care. In this family a point attaining the global maximum is `t=2 pi k=pi/delta`, so the observation scale required merely to witness the true global normalization can diverge as `delta->0`.

## Boundaries

This is a negative control on finite-window/local persistence, not a theorem about Wang's actual fixed-source packets and not evidence that their observed localization is explained by beating.

The result does not claim that frequency-gap geometry changes every infinite-time one-point amplitude statistic. Long-time phase averaging can erase information that is decisive for finite-window persistence. The finding therefore constrains the design of the matched null, not all possible observables.

Global-sup normalization is part of the exact matched family above. Replacing it by an empirical maximum over a bounded observation window changes the statistic and can itself introduce a `delta`-dependent bias.

## Prior-art and novelty audit

The product identity and the two-close-frequency beat phenomenon are elementary classical facts; no novelty is claimed for them, the mean-square calculation, or near-degenerate frequency suppression. As an explicit modern reference for the classical beat mechanism and the fact that the beat frequency is the difference of the interfering frequencies, see Marcos H. Gimenez, Juan C. Castro-Palacio, and Juan A. Monsoriu, *Direct visualization of mechanical beats by means of an oscillating smartphone*, arXiv:1605.01291 (2016).

The durable Mathia result is narrower and application-specific: this exact matched family proves that the coarse quantities named in the claim are insufficient controls for the current finite-window Wang localization question. No stronger Wang theorem, source-packet statement, or novelty claim is asserted.
