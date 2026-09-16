# MI-019 — Faithful translation lifts pay a sharp source-information price for separating the prime tail

**Evidence level:** exact affine rigidity and prime-tail marking laws from AF-221--AF-227, sharpened by the coordinate-transport rigidity of [AF-378](../../findings/AF-378-order-reparameterization-preserves-sampling-fibres-but-not-translation-geometry.md).

## Core intuition

If a representation preserves the dense source translation law and its observation remains injective or uniformly resolvable, geometric freedom cannot desingularize the prime tail for free. Unmarked lifts are affine, approximate lifts remain near affine, and marked lifts must pay explicitly in source information.

The quantitative point is that **alphabet complexity and information complexity are not the same resource**. A shrinking source radius can make the required mark alphabet sublinear in the number of primes while the mark entropy still carries asymptotically the full prime identity.

AF-378 adds a complementary coordinate warning: an order reparameterization can make displayed sample gaps arbitrarily small without changing the observation experiment. If the kernel is transported faithfully with the coordinate map, every sampled determinant and every false-positive fibre is preserved. For the full translation-kernel class, a common coordinate change preserves the difference-only form `f(u-x)` exactly only when it is positive affine. Reimposing a fresh translation kernel after a nonlinear change is therefore a **source-model change**, not a free geometric repair.

## Strongest justified principle

AF-221 proves scalar affine rigidity, AF-222 shows vector-valued faithful translation lifts still lie on one affine line, and AF-223 makes the conclusion stable under approximate fidelity. AF-224 reduces uniformly separated, uniformly resolvable marked repairs to coloring a one-dimensional source-proximity graph.

AF-225 makes that reduction exact: the chromatic number equals maximal local occupancy, and at every fixed positive prime-tail resolution the required alphabet is asymptotic to `pi(Q)`. AF-226 gives the moving-resolution cardinality law. With `c_Q=r_Q log Q`, the normalized minimum alphabet tends to `1-e^{-c}` when `c_Q -> c`; in particular sublinear alphabet size occurs exactly in the regime `r_Q log Q -> 0`.

AF-227 shows that the entropy threshold is much harsher. If `beta_Q=log^+(1/r_Q)/log Q -> beta`, then minimum marking entropy divided by `log pi(Q)` tends to `(1-beta)_+`. Polylogarithmically shrinking resolution can therefore use a vanishing fraction of the source cardinality as marks while still carrying asymptotically full source entropy.

AF-378 closes the coordinate-only loophole. Conjugating the order and the kernel leaves the sampled observation fibre unchanged even when the new coordinate picture has vanishing gaps. The only coordinate changes that preserve the whole translation category itself are positive affine maps.

## Program consequence

Every proposed translation-coordinate repair should declare the resolution scale and separately price alphabet size, mark entropy, inverse conditioning, representation error, and **source-category covariance under the coordinate change**. A useful source-specific side channel must reduce the resource consumed by the final theorem, not merely relabel the prime identity more compactly in cardinality or redraw the same observation fibre in denser coordinates.

Genuine exits include mark-dependent sample geometry, a non-translation relation justified intrinsically by the source, controlled loss of injectivity, or a quantitatively favorable error/conditioning tradeoff. Higher dimension, nonlinear coordinates, and a growing label set are not by themselves evidence of information gain.

## Counterevidence / boundary

The marking theorems apply to the declared proximity-separation model with one shared source coordinate. They do not classify arbitrary variable-length codes, source distributions other than the stated prime model, mark-dependent geometry, nontranslation group laws, or deliberately lossy target-specific quotients. AF-378 does not forbid nonlinear coordinates; it says only that faithfully transporting the original experiment preserves its fibres, while reimposing translation geometry after a nonlinear change must be justified as a new mathematical model.

## Epistemic status

**Exact category boundary with separate cardinality, entropy and coordinate-covariance laws; no universal coding theorem or RH consequence is claimed.**

## Falsification criterion

Construct a faithful lift violating AF-221--AF-223, an `r_Q`-proper prime-tail marking beating the AF-226 cardinality or AF-227 entropy law, or a non-affine common reparameterization that preserves the full translation-kernel class while changing the sampled observation fibre. A successful escape should instead identify which fidelity/source-category assumption changes and quantify the resulting destination benefit.
