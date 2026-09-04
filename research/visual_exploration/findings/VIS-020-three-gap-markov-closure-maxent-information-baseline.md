# VIS-020 — adjacent-pair-preserving three-gap closure is the maximum-entropy baseline

## Claim

Let `X,Y,Z` be finite-valued random variables; for the visual application they are bins containing three consecutive unfolded gaps. Fix compatible adjacent-pair marginals `P_XY` and `P_YZ`, with common middle marginal `P_Y`, and define

`Q(x,y,z) = P_XY(x,y) P_YZ(y,z) / P_Y(y)`

on fibers with `P_Y(y) > 0`, and `Q=0` when `P_Y(y)=0`.

Then `Q` is not merely a convenient first-order Markov surrogate. It is the **unique maximum-entropy joint distribution with those two adjacent-pair marginals**. For every joint distribution `P` with the same `XY` and `YZ` marginals,

`D(P || Q) = I_P(X;Z | Y) = H(Q) - H(P) >= 0`.

**Evidence/status:** `CLASSICAL-IDENTITY + EXACT-DERIVED`.

For the three-gap visual program this fixes the information accounting exactly. The tensor `Delta = P-Q` localizes where conditional dependence beyond the two overlapping pair marginals occurs, while conditional mutual information is the canonical nonnegative scalar KL distance from the corresponding Markov closure for the chosen finite partition. Neither quantity is arithmetic-specific by itself; the live zeta question remains the residual relative to a matched finite-size random-matrix/arithmetic baseline.

## Exact derivation

First, `Q` has the prescribed pair marginals. On every `y` with `P_Y(y)>0`,

`sum_z Q(x,y,z) = P_XY(x,y)`

and similarly `sum_x Q(x,y,z) = P_YZ(y,z)`. Fibers with `P_Y(y)=0` carry no mass under any compatible joint distribution.

Now let `R` be any other joint distribution with the same two adjacent-pair marginals. The entropy chain rule and the fact that conditioning cannot increase entropy give

`H_R(X,Y,Z) = H(X,Y) + H_R(Z | X,Y)`

`<= H(X,Y) + H_R(Z | Y)`

`= H(X,Y) + H(Y,Z) - H(Y)`.

All three quantities on the last line are fixed by the prescribed marginals. Under `Q`, `X` and `Z` are conditionally independent given `Y`, so equality holds and

`H(Q) = H(X,Y) + H(Y,Z) - H(Y)`.

Equality in the conditioning step requires `Z` to be conditionally independent of `X` given `Y`. Because the two pair marginals already fix `P(X|Y)` and `P(Z|Y)` on every positive-mass middle fiber, that conditional-independence completion is exactly `Q`. Hence the entropy maximizer is unique on the support of `P_Y`.

Finally, direct substitution gives

`D(P || Q) = sum_{x,y,z} P(x,y,z) log( P(x,y,z) P_Y(y) / (P_XY(x,y) P_YZ(y,z)) )`,

which is precisely `I_P(X;Z|Y)`. Since `P` and `Q` share the same two pair marginals, the same algebra also yields `D(P||Q)=H(Q)-H(P)`.

## What this changes for the visual test

The proposed three-gap experiment now has an exact null geometry before any zeta data are rendered. A raw three-gap cloud, a nonzero `Delta`, or positive conditional mutual information does not establish an arithmetic signal: a determinantal CUE gap process is not expected to be first-order Markov, so its own `P` can sit a positive information distance from its pair-marginal-preserving closure.

The meaningful comparison is therefore two-stage. Within each zeta or control window, build **its own** `Q` from that window's adjacent-pair marginals and measure the departure `P-Q` or `D(P||Q)`. Only after this lower-order information has been removed should the zeta departure be compared with the corresponding matched finite-size CUE/arithmetic departure. This prevents a visual residual from being driven simply by different one-gap or adjacent two-gap marginals.

For visualization, `Delta` and the cellwise log-ratio `log(P/Q)` remain useful because they retain *where* the conditional dependence sits; conditional mutual information is their nonnegative scalar information summary, not a substitute for the full residual shape. Estimation bias, sparse cells, bin choice, and unfolding remain empirical issues and are not solved by the identity.

## Prior art and novelty assessment

The entropy, relative-entropy, conditional-mutual-information, chain-rule, and maximum-entropy ingredients are standard information theory; Cover and Thomas are recorded in `research/visual_exploration/SOURCES.md` as the canonical textbook anchor. No novelty is claimed for the Markov factorization or maximum-entropy identity.

Higher-order consecutive-spacing correlations are also not a new random-matrix object. Herman et al. (2007) explicitly develop random-matrix formulas involving correlations between two and three consecutive level spacings, while Nishigaki (2026) supplies the sharper two-consecutive-spacing finite-size CUE/zeta baseline already used in `VIS-019`.

The Mathia contribution is therefore a **falsification boundary and exact experimental normalization**: the local three-gap clue should not search for generic non-Markov dependence, but specifically for a reproducible zeta-minus-matched-RMT difference after each process has been projected against its own adjacent-pair-preserving maximum-entropy closure.

## Boundary conditions

This result is exact only for the probability distribution actually supplied to it. With empirical finite partitions, changing the partition changes `P`, `Q`, `Delta`, and the numerical conditional mutual information. Continuous-variable versions require the usual density/absolute-continuity care and are not established here by merely taking a finer histogram.

The result also does not claim that matching adjacent-pair marginals makes two point processes otherwise comparable. Long-range correlations, higher-order determinantal structure, finite-size effects, arithmetic corrections, unfolding drift, and sampling noise can all remain. Those are precisely why the zeta test needs a matched CUE/arithmetic control rather than the bare Markov closure alone.

## Visual consequence

No new PNG is retained for this finding. The main progress in this pass is an exact information-theoretic normalization that should precede rendering: without data and a matched finite-size control, a synthetic `Delta` heatmap would be illustrative rather than evidence. The next retained image should therefore visualize an empirical **zeta-minus-matched-baseline conditional residual**, with the pair-marginal closure applied separately on both sides.

## Research consequence

`CLUE-zeta-three-gap-conditional-residual` is mathematically well posed and survives this baseline audit. It should be accepted as a live experiment, with `I(G_{n-1};G_{n+1}|G_n)` interpreted exactly as KL distance to the adjacent-pair-preserving maximum-entropy closure and with the full residual tensor retained for localization.

The unresolved content is entirely empirical/arithmetic: whether high zeta zeros show a reproducible conditional-dependence residual **beyond** the correctly matched finite-size CUE and known arithmetic corrections. A null result there would close the next natural local extension beyond `VIS-019`; a positive result would still require estimator, partition, height, and prior-art stress tests before promotion.