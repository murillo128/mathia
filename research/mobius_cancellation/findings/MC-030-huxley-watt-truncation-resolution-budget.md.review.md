---
type: adversarial-review
target: MC-030-huxley-watt-truncation-resolution-budget.md
---

## Adversary

The Fourier-side resolution conclusion overstates what the `O_\varepsilon(N^{1+\varepsilon})` target forces. From (4), taking `H=N^{1-\delta}` gives a source remainder `O(N^{1+\delta}\operatorname{polylog}N)`. For each fixed target `\varepsilon>0`, choosing any fixed `0<\delta<\varepsilon` (for example `\delta=\varepsilon/2`) makes that remainder `O_\varepsilon(N^{1+\varepsilon})`, since the logarithmic factors fit inside the remaining power margin. The `O_\varepsilon` quantifier permits the truncation choice to depend on the fixed `\varepsilon`.

Therefore ordinary RH-compatible control does not require a single schedule `H=N^{1-o(1)}` as `N\to\infty`, nor does it by itself force an almost-linearly growing frequency family for each fixed `\varepsilon`. What the displayed remainder does prove is the weaker uniform statement: no one fixed exponent `\theta<1`, independent of `\varepsilon`, certifies the whole family of `O_\varepsilon(N^{1+\varepsilon})` bounds, and the required exponent may approach `1` as `\varepsilon\downarrow0`. This matters because the finding promotes that uniform-in-`\varepsilon` observation into the headline bottleneck "near-linear frequency resolution forced" and then conditions (8)--(9) on `H=N^{1-o(1)}`. The separate spectral-truncation obstruction (2)--(3) is not affected by this objection.

**Required-action:** Rephrase the Fourier-resolution conclusion to respect the `\varepsilon` quantifiers. Either state an additional reason a single truncation schedule uniform in `\varepsilon` is required, or replace (7) and the associated "almost linearly growing" / "near-linear frequency resolution" claims by the precise statement that, for each fixed `\varepsilon`, one may take `H=N^{1-\delta(\varepsilon)}` with `0<\delta(\varepsilon)<\varepsilon` (up to the explicit logarithmic margin), while no `\theta<1` independent of `\varepsilon` works for all `\varepsilon`.

**Check refs:** MC-030 (1), (4), (6)--(9), especially the paragraph following (14); Huxley--Watt `MC-S24`, Fourier truncation remainder used in (4). Direct check: `H=N^{1-\varepsilon/2}` makes the source remainder `N^{1+\varepsilon/2}\operatorname{polylog}N=O_\varepsilon(N^{1+\varepsilon})` for every fixed `\varepsilon>0`.
