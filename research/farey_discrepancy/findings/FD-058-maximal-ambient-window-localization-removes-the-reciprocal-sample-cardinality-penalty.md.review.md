---
type: adversarial-review
target: research/farey_discrepancy/findings/FD-058-maximal-ambient-window-localization-removes-the-reciprocal-sample-cardinality-penalty.md
---

# Adversarial review

## Adversary

The maximal-localization idea is plausible, but the transfer from the cited almost-all Möbius theorem to equations (10)--(13) currently mixes **Lebesgue measure of real starts** with **cardinality of integer starts** in a way the theorem does not justify. Theorem 1.1(i) of Matomäki--Radziwiłł--Shao--Tao--Teräväinen states that the bad set of `x in [X,2X]` has small *measure*. FD-058 then applies `y -> floor(y/d)` and argues that every exceptional scaled start has at most `d` integer preimages, treating that measured exceptional set as though it were a finite set of bad integer starts. A small-measure subset of the real line can contain every integer, so the displayed measure bound alone gives no such cardinality estimate. The same distinction is implicit earlier when (1)--(3) count integer containing starts but the load-bearing literature input later supplies a measured exceptional set.

This is a proof gap in the source-level maximal statement (13), not presently a refutation of the corridor-threshold conclusion. There appears to be a natural repair, but it must be made explicitly: either keep the ambient start `y` real throughout, pull measured exceptional sets back under the real scaling `y -> y/d` (paying the Jacobian factor `d`) and use maximality plus endpoint rounding to embed every required `m`-interval; or discretize the theorem at suitable integer ambient lengths and prove that failure at an integer start persists on a unit interval, so the measure bound really controls the number of bad integer starts. In either version the argument must also be made simultaneous for all `d <= D` with the claimed polylogarithmic union cost.

Until that measure/cardinality bridge is supplied, equations (10), (13), and hence the invocation of the published theorem as a rigorous source-level maximal estimate are stronger than the written derivation supports. The abstract implication “a maximal source theorem with exceptional measure `o(R_X)` gives a good containing ambient start” can remain, but the literature-to-source transfer needs this correction before the claimed current quantitative boundary is fully justified.