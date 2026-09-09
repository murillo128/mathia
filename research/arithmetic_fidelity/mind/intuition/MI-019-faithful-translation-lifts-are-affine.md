# MI-019 — Faithful translation lifts pay a sharp source-information price for separating the prime tail

**Evidence level:** exact affine rigidity, stable approximate rigidity, and exact prime-tail marking phase laws through AF-227

## Core intuition

If a representation preserves the dense source translation law and its observation remains injective or uniformly resolvable, geometric freedom cannot desingularize the prime tail for free. Unmarked lifts are affine, approximate lifts remain near affine, and marked lifts must pay explicitly in source information.

The new quantitative point is that **alphabet complexity and information complexity are not the same resource**. A shrinking source radius can make the required mark alphabet sublinear in the number of primes while the mark entropy still carries asymptotically the full prime identity.

## Strongest justified principle

AF-221 proves scalar affine rigidity, AF-222 shows vector-valued faithful translation lifts still lie on one affine line, and AF-223 makes the conclusion stable under approximate fidelity. AF-224 reduces uniformly separated, uniformly resolvable marked repairs to coloring a one-dimensional source-proximity graph.

AF-225 makes that reduction exact: the chromatic number equals maximal local occupancy, and at every fixed positive prime-tail resolution the required alphabet is asymptotic to `pi(Q)`. AF-226 gives the moving-resolution cardinality law. With `c_Q=r_Q log Q`, the normalized minimum alphabet tends to `1-e^{-c}` when `c_Q -> c`; in particular sublinear alphabet size occurs exactly in the regime `r_Q log Q -> 0`.

AF-227 shows that the entropy threshold is much harsher. If `beta_Q=log^+(1/r_Q)/log Q -> beta`, then minimum marking entropy divided by `log pi(Q)` tends to `(1-beta)_+`. Polylogarithmically shrinking resolution can therefore use a vanishing fraction of the source cardinality as marks while still carrying asymptotically full source entropy.

## Program consequence

Every proposed translation-coordinate repair should declare the resolution scale and separately price alphabet size, mark entropy, inverse conditioning, and representation error. A useful source-specific side channel must reduce the resource consumed by the final theorem, not merely relabel the prime identity more compactly in cardinality.

Genuine exits include mark-dependent sample geometry, a non-translation relation, controlled loss of injectivity, or a quantitatively favorable error/conditioning tradeoff. Higher dimension, nonlinear coordinates, and a growing label set are not by themselves evidence of information gain.

## Counterevidence / boundary

The marking theorems apply to the declared proximity-separation model with one shared source coordinate. They do not classify arbitrary variable-length codes, source distributions other than the stated prime model, mark-dependent geometry, nontranslation group laws, or deliberately lossy target-specific quotients.

## Epistemic status

**Exact category boundary with separate cardinality and entropy phase laws; no universal coding theorem or RH consequence is claimed.**

## Falsification criterion

Construct a faithful lift violating AF-221--AF-223, or an `r_Q`-proper prime-tail marking beating the AF-226 cardinality or AF-227 entropy law. A successful escape should instead identify which fidelity assumption changes and quantify the resulting destination benefit.