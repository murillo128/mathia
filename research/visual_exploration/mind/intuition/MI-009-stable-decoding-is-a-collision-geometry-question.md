# MI-009 — Stable analytic novelty must beat the dimension-dependent held-out-prime collision budget

**Evidence level:** proved representation criterion plus quantitative matched null; zeta separation remains open

## Core intuition

Exact finite prime phases can identify height while stable decoding remains impossible. More importantly, large collision complexity, divergent moments, and even some polynomial finite-window growth are already produced by an ordinary omitted prime. With growing support there is a second control: high dimension makes the matched collision event itself exponentially scarce.

A meaningful zeta-facing statistic must therefore beat the held-out-prime null **while remaining in a population regime with enough matched mass to measure**.

## Strongest justified claim

VIS-161--VIS-165 identify the exact collision quotient for stable decoding and give the fixed-support omitted-prime null: anchored exceedance tails are `c_d L^(-d)` and finite Diophantine type transfers that law to a polynomially growing threshold range.

VIS-166 gives the corresponding moment classification. For retained dimension `d`, the Haar collision moment `E[C^s]` is finite exactly for `s<d`; at `s=d` capped moments grow logarithmically and above `d` polynomially. Divergent high moments are therefore a dimension singularity of the null, not evidence of zeta structure.

VIS-167 transfers these capped-moment asymptotics to the deterministic prime-log orbit for explicit polynomial cap ranges. The generic control already reproduces critical and supercritical moment growth.

VIS-168 adds the growing-support population gate. Uniformly for `L>=1`, `log mu_d(L)=-(d/2)log d-d log L+O(d)`. With `Q` anchored samples, fixed positive-power thresholds `L=Q^gamma` have vanishing expected null exceedance mass as soon as `d->infinity`. At fixed threshold and `d~c log Q/loglog Q`, the population transition occurs at `c=2` up to lower-order terms.

## Synthesis of evidence

Growing support is not a free way to suppress the null. It changes the experiment's sample-complexity budget. A valid source separation should predeclare `d(Q)` and `L(Q)`, verify that `Q mu_d(L)` remains nonnegligible in the matched control, and then show a zeta statistic exceeds or structurally differs from that dimension-coded law.

Equivalently, if one wants a positive-power threshold while `d` grows, the exponent must shrink roughly on the `1/d` scale, with an additional high-dimensional volume penalty near `log Q/loglog Q`.

## Counterevidence / boundary cases

VIS-168 is a Haar population theorem, not a growing-dimensional discrepancy theorem for the deterministic prime-log orbit. Even when `Q mu_d(L)` is large, uniform equidistribution in growing dimension still needs proof.

A zeta observable could separate in another representation or regularity class, but that class needs its own matched null and population budget.

## Epistemic status

**Exact matched-null/sample-budget boundary:** fixed-support collision tails and moments are dimension-driven; growing support suppresses the null only by also suppressing observable population mass. Source sensitivity requires separation in a jointly feasible dimension/threshold/sample regime.

## Novelty/prior-art status

Kronecker--Weyl, linear forms in logarithms, discrepancy, layer-cake moments, and high-dimensional ball-volume estimates retain their finding-level classifications.

## Falsification criterion

Invalidate the fixed-support Haar tail/moment laws, the VIS-167 transfer regime, or the VIS-168 two-sided population bounds. Strategically, exhibit a zeta-facing collision law separated from the matched null in a regime with controlled growing-dimensional discrepancy and nonvanishing matched sample mass.
