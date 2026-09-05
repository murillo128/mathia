# MI-013 — Approximate fidelity is witness-relative recovery geometry; composition needs quotient-compatible transport

**Evidence level:** supported through AF-133; exact for the finite statistical experiments, convex witness classes, Wasserstein recovery models, and composition bounds stated in AF-126--AF-133

## Core intuition

Approximate fidelity is not one scalar property of a representation. It is the smallest recovery error seen by a declared class of downstream witnesses, so changing the witness class changes the quotient geometry being preserved. Full bounded decision tests recover Le Cam deficiency; convex restricted witnesses can ignore a nontrivial kernel; metric-local witnesses recover Wasserstein geometry.

Composition is stricter than stagewise recovery. A residual that is invisible to the downstream witness class can become visible after an upstream map, and scalar recovery errors then fail to compose. A useful multistage fidelity statement therefore needs a **source-forced transport law for witnesses/quotients**, such as a Lipschitz modulus or naturality condition, not only a small defect at each stage.

## Strongest justified principle

AF-126 identifies one-sided Le Cam recovery deficiency as the operational approximate-fidelity cost of reconstructing an experiment for all bounded decisions. AF-127--AF-128 show that, in finite experiments, positive deficiency has exact bounded decision witnesses and optimal witnesses can be calibrated against the identity experiment. The defect is therefore not merely existential: it has a concrete reconstructive decision meaning.

AF-129 restricts the witness family and makes the quotient explicit. A convex class of observables induces a seminorm/pseudometric whose kernel is observationally invisible; recovery is faithful only modulo that kernel. AF-130 specializes this to metric-local `1`-Lipschitz witnesses, where the resulting recovery error is normalized Wasserstein-1 distance.

AF-131 shows why stagewise scalar errors are insufficient: Wasserstein recovery across changing metric spaces does not compose without controlling how the intermediate recovery transports Lipschitz witnesses. AF-132 gives the positive replacement. The optimal profile `Phi(t)=inf_R(e(R)+t kappa(R))` records recovery error together with transport regularity and obeys a functional composition bound.

AF-133 generalizes the obstruction beyond metrics. Restricted-witness recovery composes only when the recovery maps are compatible with the induced observational quotients. If a residual killed by the downstream seminorm can be mapped into a direction visible upstream, the cross-stage transport coefficient is infinite even when both stagewise recovery defects vanish.

## Evidence synthesis and boundaries

The result does not say that one universal recovery category is preferred. The relevant witness class, quotient, and transport regularity must be imposed by the actual downstream use. Enlarging the witness family can strengthen fidelity but also change the problem; shrinking it can make recovery cheap by declaring distinctions irrelevant.

This complements MI-009 and MI-012 rather than replacing them. MI-009 separates finite exactness from bounded categorical accessibility, while MI-012 tracks multiscale information cost. The new principle concerns the **operational quotient and its functorial transport across composed representations**.

## What remains possible

Concrete arithmetic applications should derive their admissible witness class and show that the proposed representation admits recovery maps that are natural or quantitatively regular for that class. A useful positive theorem would identify a source-forced quotient whose recovery profile composes across the actual pipeline. A useful negative would show that a proposed compression has zero stagewise error yet necessarily turns an invisible residual into a visible one at a later stage.

## Status / novelty

Le Cam deficiency, integral probability metrics, Wasserstein distance, Lipschitz transport, and quotient seminorms are classical. The persisted synthesis is the categorical rule: **approximate fidelity is witness-relative, and stagewise small defects become compositional only when recovery respects the witness-induced quotient with quantitative transport regularity**.

## Falsification criterion

Construct a multistage recovery satisfying the AF-131/AF-133 hypotheses in which the relevant quotient-transport coefficient is uncontrolled but a uniform composition bound depending only on the stagewise defects still holds; or violate the AF-132 profile composition inequality in its stated setting.

## Lean-formalizable core

- Finite one-sided deficiency and decision witnesses.
- Witness-class pseudometric/quotient construction.
- Kantorovich--Rubinstein specialization.
- Recovery profile `Phi` and its composition inequality.
- Quotient-compatibility obstruction to restricted-witness composition.
