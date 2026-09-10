# MI-023 — Local completeness can preserve a root-rate discriminator at zero output density

**Evidence level:** exact finite-exponential sampling theorem from AF-244

## Core intuition

Asymptotic density is not the right measure of how much output sampling a root-rate discriminator needs. A set of indices can have density zero and still preserve the dominant exponential rate if it contains arbitrarily long consecutive blocks, because those local blocks can capture every phase of each finite exponential mode.

This is an output-side economy only. It does not make the arithmetic source for a retained coefficient cheaper.

## Strongest justified principle

AF-244 proves that thick zero-density sampling sets preserve the limsup root discriminator for finite sums of exponential modes, and therefore preserve the Li root-rate criterion in the stated setting. The result separates two notions that were easy to conflate: global sampling density and local phase completeness.

The same theorem does not reduce the depth needed to compute a retained Li coefficient. Sparse output sampling can therefore coexist with the deep source-access obstruction isolated by AF-234--AF-243.

## Program consequence

When optimizing the Li route, treat source depth and output index count as independent resources. Explore sampling geometries defined by local completeness or recurrence rather than positive density, but require an independent accounting of the source work needed for every retained coefficient.

## Counterevidence / boundary

Thickness is a sufficient condition, not a proved necessary one. The finite-exponential argument does not automatically control arbitrary infinite spectral superpositions, numerical conditioning, or the cost of constructing the sampled coefficients.

## Epistemic status

**Exact separation between zero-density output sampling and source compression for the finite-mode/root-rate discriminator; the minimal sampling geometry remains open.**

## Falsification criterion

Find a finite exponential family whose root limsup changes on a thick sampling set, or prove that the relevant Li criterion requires positive density despite AF-244's hypotheses. A positive continuation should characterize weaker sampling conditions while preserving the same root-rate endpoint.