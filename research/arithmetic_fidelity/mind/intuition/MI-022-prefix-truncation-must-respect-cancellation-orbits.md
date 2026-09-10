# MI-022 — Prefix truncation must respect the cancellation orbits of the destination transform

**Evidence level:** exact Li-binomial truncation asymptotics and completed-germ obstruction through AF-238

## Core intuition

Source depth is not the only fidelity cost of a coarse target. If the destination is produced by a global transform with large internal cancellations, a locally accurate or linearly deep prefix can leave the target class entirely by interrupting those cancellation orbits.

For the Li root-rate criterion this failure is exact: a truncation can manufacture exponential growth from singularities that are harmless in the full transform. Completion removes known trivial-zero contamination but does not repair the structural problem.

## Strongest justified principle

AF-235 shows that the full Li sequence is RH-sufficient at the coarse root-rate threshold `<=1` and is insensitive to subexponential additive perturbations. AF-236 shows that every sublinear initial zeta jet contributes only subexponentially, so decisive source information lies deeper than every `o(n)` prefix in that reconstruction.

AF-237 studies the first linear regime `K_n=floor(alpha n)`. For `0<alpha<1/4`, truncating the ordinary local `eta` jet gives an unconditional root rate `exp(H(alpha))/3^alpha>1`, caused by the first trivial zero at `w=-3`; the full binomial transform cancels that artifact.

AF-238 repeats the test after absorbing the entire gamma/completion structure into `xi'/xi`. The nearest singularities are then the first nontrivial zero pair, already known to lie on the critical line, yet for `0<alpha<1/(1+|rho_1-1|)` the completed initial jet again has root rate `exp(H(alpha))/|rho_1-1|^alpha>1`. A target-compatible zero is therefore turned into a false root-rate violation solely by stopping its binomial orbit early.

## Program consequence

Treat cancellation coherence as a separate representation invariant from source depth and output tolerance. A candidate source compression for a global transform should identify which singularity/orbit contributions must be completed together before truncation and prove that the discarded remainder is small **after** those cancellations, not coefficientwise before them.

For the Li route, search for a blockwise/orbit-complete, contour-based, or otherwise non-prefix source representation whose approximation error is subexponential in the final Li sequence without assuming the zero location conclusion being tested.

## Counterevidence / boundary

AF-237 and AF-238 concern canonical Taylor-prefix reconstructions and a specific binomial destination transform. They do not prove that every linear-depth or local representation is unfaithful, nor that a different grouping cannot preserve the root-rate class cheaply. The exact thresholds are sufficient artifact regimes, not universal minimum depths.

## Epistemic status

**Exact demonstration that both uncompleted and completed local prefixes can create false exponential target signals by breaking global cancellation; a cancellation-coherent cheap source bridge remains open.**

## Falsification criterion

Produce a prefix scheme inside the stated regimes whose full contribution has root rate at most one despite the derived nearest-singularity asymptotics, or invalidate the Li-binomial transform used in AF-237/AF-238. A positive continuation should construct a source approximation with a proved subexponential error after the necessary cancellation orbits are completed.
