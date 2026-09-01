# MI-001 — Preserve the discriminating structure and its stability before compressing

**Evidence level:** supported by exact deterministic, analytic, statistical, interaction-kernel, fusion-frame, and algebraic closure theorems

## Core intuition

Across Mathia, the recurring failure is applying a transformation whose induced indistinguishability relation already identifies states or models that the later arithmetic claim needs to distinguish. The newer Arithmetic-Fidelity results add a second warning: even when the target survives in the closed retained space, the reconstruction may become arbitrarily ill-conditioned. A useful pipeline must therefore audit the **complete statistic, interaction support, admissible algebraic closure, and stability modulus** before optimization, spectralization, positivity, or completion.

## Strongest current principle

AF-030 gives the linear gate: scalar tests retain exactly their closed span `V_F`, with signed-measure kernel `V_F^perp`. AF-031--AF-033 give the first interaction gate: complete marginals can forget joint coupling, and on the Boolean cube the exact kernel is the set of missing Walsh faces.

AF-034--AF-038 extend that picture beyond Boolean marginals. Independent product sources have an exact Hoeffding interaction decomposition; bounded multiplicative channel degree is exactly channel-cover number; and arbitrary dependent sources have a source-dependent degree filtration given by closed fusion spans of joins of the retained sigma-fields. Linear join and generated-sigma closure are therefore genuinely different information operations. AF-039 then separates exact and stable recovery: for two closed channel subspaces the sharp stability constant is controlled by the Friedrichs angle, so injectivity can survive while uniform inversion fails.

The earlier analytic and programmable controls remain essential. Infinite test families can be complete or sharply aliased depending on parameter geometry; source-tunable finite classes can locally program recovery and therefore do not prove intrinsic specificity. Prime Circle supplies an algebraic analogue: arbitrary finite cotangent-network topology, fixed-support depth, and canonical complete-preimage growth remain inside endpoint/fixed-state closures, while PC-105 shows that even fixed translation-invariant nonlocal kernel statistics of the cumulative primitive-root cloud reduce to classical Mertens/Fourier data.

The order of operations is therefore

`derive admissible category -> compute complete linear/joint/multiplicative statistic -> compute source fiber and stability -> test matched controls -> only then optimize, spectralize, complete, or prove positivity`.

## Consequence for synthesis

A canonical lift is useful only if it reduces the actual indistinguishability fiber **and** remains quantitatively usable in the limit. Perfect low-order marginals can miss a high-order target interaction; multiplicative closure can recover information absent from a linear span; dependence can change the interaction grading itself; and an exact decoder can still become unbounded as channel subspaces approach a common direction.

Conversely, increasing nonlinear depth, graph rank, number of tests, or numerical precision does not help when the complete retained algebra has not changed. The mathematical question is always what the final theorem actually receives and with what condition number.

## Status / novelty

The component closed-span, Hoeffding, conditional-expectation, fusion-frame, Friedrichs-angle, local-programming, and Prime-Circle reduction results use classical ingredients and are persisted findings. Their synthesis as a complete-statistic-plus-stability gate is supported rather than a universal theorem for every nonlinear observation category.

## Falsification criterion

Find a pipeline where the target varies inside the complete admissible measured/fusion fiber, no later stage receives new information, yet the final invariant recovers the target. Or produce a family with collapsing Friedrichs/fusion lower bound but a uniformly bounded decoder in the same norm. A positive construction should identify both the exact retained discriminator and the quantitative stability that survives the intended limit.

## Lean-formalizable core

- Fiberwise factorization and post-processing monotonicity.
- Closed-span/annihilator measurement kernel.
- Hoeffding/fusion interaction-support kernels.
- Channel-cover multiplicative filtration.
- Friedrichs-angle stability criterion.
- Finite cotangent/Fourier classicalization controls.
