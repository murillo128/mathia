# MI-051 — Cubic source replacement has a variance power-saving curve

**Evidence level:** exact quantitative synthesis from [PL-407](../../findings/PL-407-cubic-variance-power-saving-threshold.md), building on the exact triangular variance representation in PL-406. The prime-variance/pair-correlation framework is classical; the line-specific content is the exponent calibration for the already-fixed cubic `H^(-7/4)` layer.

Let the source-subtracted short-interval triangular remainder obey, on the range sampled by the cubic kernel,

`|Delta T_X(L)| << X L (L/X)^mu * logs`.

The exact representation then gives cubic source error

`|E_eta(X,H)| << H^(-1) (H/X)^mu * logs`.

For `H=X^theta`, preserving the zero-sensitive `H^(-7/4)` layer by this absolute-value route requires

`mu > 3 theta / (4(1-theta))`.

Equivalently, a given saving `mu` certifies `theta < 4mu/(3+4mu)`. A square-root relative saving `mu=1/2` reaches every `theta<2/5`; the endpoint needs an additional logarithmic saving. This is a calibration of the method, not an unconditional prime-variance theorem and not a universal `2/5` barrier.

The key distinction is between **source precision** and **kernel cancellation**. The exponent curve is what one pays after taking absolute values against `K_eta''`. A structured estimate for the single signed functional can beat it without improving the pointwise/absolute variance remainder itself.

**Boundary.** Existing unconditional almost-all-shift estimates do not supply the required positive power in this source-subtracted form. Any application must also align diagonal/main terms and interval conventions exactly. The live fork is therefore either a genuinely power-saving variance theorem in an intersecting range or a direct use of the oscillatory sign of `K_eta''`/zero-pair structure that avoids the absolute-value tariff.