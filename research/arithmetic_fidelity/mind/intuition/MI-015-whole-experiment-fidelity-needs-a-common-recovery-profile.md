# MI-015 — Whole-experiment fidelity needs one common recovery profile

**Evidence level:** exact finite/classical counterexamples and recovery certificate through AF-142--AF-144

## Core intuition

Local tangent fidelity and pairwise distinguishability are weaker than experiment-level recoverability. A compression can be almost Fisher-isometric, globally identifiable, and retain a fixed fraction of every pairwise total-variation distance while still admitting no single reverse channel with small deficiency.

The missing compatibility is family-wide: all parameter values must be recoverable through **one common reverse kernel**, not through pair-dependent witnesses or infinitesimal geometry.

## Strongest justified principle

AF-142 gives a smooth positive connected experiment with Fisher near-isometry but exact global aliasing. AF-143 removes that obvious defect: even with global identifiability and uniform pairwise TV retention, one-sided recovery deficiency stays bounded below.

AF-144 supplies a positive finite certificate. Fix one full-support prior/reference mixture. The Bayes/Petz reverse kernel built from that common reference satisfies a quantitative recovery bound controlled by the loss of the corresponding chi-square profile, and zero loss is exactly sufficiency. Thus a common-reference divergence profile can certify one reverse channel in a way tangent and pairwise metrics cannot.

## What remains possible

The AF-144 certificate is sufficient rather than necessary, finite/classical, and depends on an auxiliary full-support prior. A concrete arithmetic application must justify the reference from source structure, or derive another canonical family-wide compatibility object with comparable composition/recovery meaning.

## Status / novelty

Fisher information, total variation, chi-square divergence, Blackwell sufficiency, and Bayes/Petz recovery are classical. The durable synthesis is the category boundary: **fidelity becomes composable only when the retained information is organized around one family-level reverse channel or an equivalent common recovery profile**.

## Falsification criterion

Produce a source-natural class in which tangent plus pairwise fidelity alone forces small experiment deficiency, or show that the AF-144 common-reference loss fails to control the stated reverse kernel under its finite hypotheses.
