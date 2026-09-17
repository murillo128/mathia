# MI-039 — Phase-uniform almost-all control shares one exceptional bow start set

**Evidence level:** exact/literature synthesis from [WI-327](../../findings/WI-327-signed-source-subtraction-kills-generic-cubic-resonance-but-not-exceptional-bows.md) through [WI-329](../../findings/WI-329-phase-uniform-nilsequence-control-covers-the-natural-bow-dephasing-scale.md).

WI-328 identifies the first source length where varying height across a surviving bow can produce order-one phase motion: `J asymp X^(1-2 theta)`. Moving to that scale does create genuine height dephasing, but WI-329 shows that the matching almost-all arithmetic theorem is already uniform over the resulting phase family.

On a natural bow interval, the logarithmic carrier `n^(iU)` with `|U| lesssim X^2` is uniformly approximated by a polynomial phase of fixed degree once `theta` is fixed. At every surviving `theta<=3943/12011`, the natural exponent `1-2theta` lies strictly above the published `1/3+epsilon` threshold. The Matomäki--Radziwill--Shao--Tao--Teravainen theorem then takes a supremum over all bounded-complexity polynomial nilsequences before declaring the start good.

Therefore one density-one set of starts controls **all relevant bow heights simultaneously**. Varying the ordinate changes the phase values but does not create independent exceptional sets. If the distinguished source start is exceptional, sampling more heights in the same bow cannot force it into the good set.

This separates two resources that are easy to conflate: phase diversity and source-start diversity. Dephasing can create many analytically different twists while leaving the arithmetic quantifier obstruction unchanged when the source theorem is phase-uniform.

**Boundary.** The almost-all bound is still a linear-amplitude statement. Even an all-start bound of that size would not provide the diagonal-scale `L^2` variance required by the exact BOW/Weil covariance. The live route therefore needs a pointwise theorem at the distinguished start, a mechanism moving through genuinely different source starts, a source/bow incompatibility with the exceptional locus, or stronger `L^2` arithmetic information.