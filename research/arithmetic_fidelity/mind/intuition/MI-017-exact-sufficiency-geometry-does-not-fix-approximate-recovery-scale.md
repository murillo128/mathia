# MI-017 — Exact sufficiency geometry does not fix the scale of approximate recovery

**Evidence level:** exact finite-experiment and decision-theoretic results through AF-156

## Core intuition

A representation can have the correct exact zero set and still be badly calibrated as an approximate fidelity metric. The Shtarkov likelihood ray is an exact sufficient coordinate: its full conditional variance vanishes exactly when the experiment is recoverable without loss. But when the experiment family grows, the natural Shtarkov aggregation can weight the union of many individually rare alternatives so strongly that its aggregate defect remains macroscopic while worst-case recovery deficiency tends to zero.

Approximate fidelity therefore needs two independent choices: a source-natural coordinate/reference and a destination-relevant aggregation whose normalization and constants match the decision or recovery class at the effective family complexity.

## Strongest justified principle

AF-155 identifies Shtarkov mass contraction exactly with the Bayes defect for the source-induced envelope decision problem. Its zero set says that each compressed fiber has a common envelope winner, which is strictly weaker than full experiment sufficiency. With a positive winner margin it calibrates winner-label recovery, while near ties show that no margin-free label interpretation is stable. The full Shtarkov likelihood-ray variance instead equals the Bayes squared-error risk for reconstructing the whole ray and vanishes exactly at sufficiency.

AF-156 supplies the quantitative obstruction. In the private-label family, the one-sided recovery deficiency is `rho(1-1/m)`, whereas both the radial defect and the normalized whole-ray aggregate equal `(m-1)rho/[1+(m-1)rho]`. Taking `rho -> 0` with `m rho` nonvanishing makes recovery asymptotically exact while the aggregate defect stays positive; with `rho=m^{-alpha}`, `1/2<alpha<1`, every individual Shtarkov-reference Pearson certificate also vanishes while the aggregate defects tend to one.

Thus **exact-zero sufficiency, coordinate-wise small loss, and family-uniform approximate recovery are three different properties**. The missing normalization is not determined by exact identifiability alone.

## What remains possible

A source-specific arithmetic family may have bounded effective complexity, sparse likelihood-ray support, a canonical destination weighting, or another structural restriction that prevents the private-label accumulation mechanism. A target-relative projection or normalized aggregate may also control exactly the decision class needed downstream. Such a theorem must expose its complexity parameter and prove a uniform recovery/decision modulus from source structure rather than choose a normalization only to defeat one control example.

## Status / novelty

Shtarkov/NML geometry, Bayes decision theory, sufficiency, and Le Cam recovery are classical ingredients. The exact private-label phase diagram is persisted Mathia evidence with no publication-level novelty claim. The durable synthesis is the topology distinction: **an exact sufficient coordinate does not canonically determine the approximate metric in which a growing family is recoverable.**

## Falsification criterion

Derive a dimension-free modulus forcing the AF-156 Shtarkov aggregate defects to zero whenever its recovery deficiency tends to zero under the stated general finite-experiment hypotheses, invalidate the private-label identities, or prove that the intended source class has an independent complexity bound that excludes the separating regime.
