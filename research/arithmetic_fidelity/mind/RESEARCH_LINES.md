# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify conditioning inside a fixed source-law fiber after sparse collisions are excluded

**Linked intuitions:** `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`, `MI-005-test-family-fidelity-has-scale-and-dimension-gates`, and `MI-007-stable-fidelity-is-distance-from-collision`.

AF-439--AF-445 separate rigid support, movable-support collision fibers, unit-weight Newton certificates and variable-weight Hankel certificates. AF-446 then shows that even a known total mass changes the exact certificate: one affine source law removes one degree of freedom and shifts the sharp positive-moment threshold. AF-447 removes the accidental dependence on consecutive monomials by identifying the corresponding Chebyshev-system mechanism. AF-448--AF-449 make the geometry explicit: positivity filters kernel relations by sign, and fixed mass converts the relevant collision problem from conic to affine/Radon geometry.

AF-450 supplies the strongest exact source-law formulation. For fixed mass and a prescribed affine source statistic `u`, sparse injectivity is controlled not by the worst circuit of the augmented feature map but by the balanced signed circuits whose two positive sides have source-law barycenter exactly `u`. A source law can therefore remove the collision relevant to one fiber without making the whole augmented dictionary sparse-injective.

The next load-bearing question is quantitative. Once the prescribed arithmetic source fiber avoids every low-support exact Radon collision, what coordinate-invariant margin separates it from **near-collisions inside the same fiber**? The useful statement must price perturbations in the physical source/observation geometry, survive the remote-atom degeneration already seen in AF-444--AF-446, and distinguish an arithmetic source law from a generic constraint or a target-encoding assumption.

## Keep observation family, source-law value, circuit orientation, exact injectivity and robustness separate

Observation count and latent dimension remain useful local diagnostics, but AF-446--AF-450 show why they are not the final invariant. Known mass, positivity and further affine source laws change which signed kernel relations are actually admissible; the same global augmented map can contain a sparse Radon circuit that is irrelevant to the particular source-law value under study.

Uniform fidelity over every source-law value is recovered by the global augmented affine criterion, whereas one-fiber fidelity is the finer barycenter-localized criterion of AF-450. Neither exact criterion supplies a stable margin by itself. Future arithmetic claims should therefore state the observed feature family, the independently justified source law and its value, the admissible sign/support class, the exact collision criterion and only then the conditioning scale consumed downstream.