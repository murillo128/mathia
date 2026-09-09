# MI-019 — Faithful translation lifts cannot nonlinearly stretch the prime tail for free

**Evidence level:** exact and stable affine rigidity plus finite-mark quantitative obstruction through AF-224

## Core intuition

If a representation preserves the dense source translation law and the observation remains injective or uniformly resolvable, then apparent freedom to repair a collapsing prime-tail mesh by nonlinear coordinates, higher dimension, or a bounded source label is illusory. The unmarked representation is forced onto an affine line; approximate fidelity is forced near that affine model; and finitely many well-conditioned marked decoders still cannot uniformly separate an arbitrarily dense source tail.

## Strongest justified principle

AF-221 proves scalar affine rigidity from the prime-tail difference source. AF-222 shows that vector-valued faithful translation lifts do not gain extra geometric directions: all source points lie on one affine line. AF-223 makes the conclusion stable in Banach space under approximate translation fidelity, with deviation controlled by the admitted representation error.

AF-224 adds the first explicit side-information budget. With one shared continuous sample coordinate and finitely many mark-specific decoders, same-mark source points remain close whenever their source coordinates are close, up to the decoder's inverse-resolution error. Uniform hidden separation therefore requires at least as many marks as the source proximity graph needs colors. For the rational-prime log-log tail that local density is unbounded on every fixed scale, so a fixed finite mark alphabet cannot desingularize the tail under uniform conditioning.

## Program consequence

A coordinate repair should state exactly which resource grows or degrades. Genuine improvement must come from source-specific side information whose complexity grows with the tail, mark-dependent sample geometry, a non-translation relation, controlled loss of injectivity, or an error/conditioning tradeoff quantitatively favorable to the target. Dimension, nonlinear parametrization, and bounded labels alone are not new arithmetic information.

## Counterevidence / boundary

The rigidity does not classify growing mark alphabets, mark-dependent sample maps, nonlinear group laws, deliberately non-injective quotients, or observation maps whose conditioning/error is paid elsewhere. AF-224 is a lower-bound principle for the declared marked-translation category, not a universal coding theorem.

## Epistemic status

**Exact category boundary with stable approximate and finite-mark quantitative forms; no claim is made against source-specific growing-complexity representations.**

## Falsification criterion

Construct a faithful lift violating AF-221--AF-223, or a uniformly well-conditioned finite-mark representation of the prime log-log tail that achieves fixed hidden separation while satisfying AF-224's hypotheses. A valid escape should instead identify the growing complexity, changed relation, or explicit error budget that leaves those hypotheses.