# Arithmetic Fidelity

## Research mandate

### Primary object

The line studies how mathematically meaningful structure survives, collapses, or becomes recoverable under transformations that forget or compress information. Its basic object is a map

\[
T:X\to Y
\]

between structured mathematical spaces together with a class of properties, relations, markings, invariants, or discriminators carried by objects in `X`.

The central distinction is not merely whether `T` is injective. The line asks whether a specified structural discriminator remains observable after `T`, whether it can be reconstructed from `T(X)`, and what minimal additional structure is required when it cannot. Typical transformations include quotients, averaging, scalarization, spectra, traces, determinants, Gram/autocorrelation maps, positivity projections, asymptotic limits, coarse graining, and passages from marked to unmarked data.

The line begins independently of the rational primes. Arithmetic objects enter only after a sufficiently precise theory of structural survival, collapse, and recovery has been developed on general mathematical examples.

### Objective

Develop a rigorous theory of structural fidelity under compression: determine which properties survive a transformation, which become indistinguishable, which remain recoverable, and which require a minimal lift or retained marking.

The long-term arithmetic objective is to use that theory to determine which mathematical representations and downstream operations can preserve a discriminator specific to the rational primes, and which classes of proposed RH mechanisms are doomed because the relevant arithmetic structure has already been erased before the final analytic, spectral, positivity, or asymptotic step.

A valuable result need not mention RH. General no-go theorems, recovery theorems, minimal-lift principles, composition laws for information loss, or natural examples separating different notions of fidelity are first-class targets.

### Priority questions

Study in particular:

- precise notions of structural discriminator, fidelity, indistinguishability, recoverability, sufficient representation, and minimal lift;
- how those notions differ from ordinary injectivity, entropy, dimension, or raw information quantity;
- equivalence relations induced by a transformation, and which classes of properties factor through the resulting quotient;
- composition laws for chains `X -> Y -> Z`: what can be certified lost at an intermediate stage and therefore cannot be recreated downstream;
- marked versus unmarked data, provenance, orientation, phase, sign, transverse structure, boundary data, and relational structure as possible carriers of information that scalar or canonical summaries erase;
- classification of common mathematical compressions such as averaging, quotienting, spectralization, quadratic/Gram maps, positivity, traces/determinants, scalarization, and asymptotic limits by the discriminators they necessarily preserve or destroy;
- construction of explicit non-isomorphic or semantically distinct pairs `A != B` with `T(A)=T(B)`, followed by identification of the smallest natural enrichment that separates them;
- general no-go theorems for whole classes of transformations and corresponding rigidity or recovery theorems for minimally enriched representations;
- whether apparently different loss mechanisms in geometry, harmonic analysis, operator theory, probability, statistics, and arithmetic are instances of one reusable abstraction;
- only after the abstract theory is mature enough to make falsifiable predictions, application to rational primes, Beurling/generalized-prime controls, explicit-formula data, and the compression bottlenecks exposed by other Mathia research lines.

### Scope and exclusions

This line is not another direct formulation of RH and should not begin by inventing a new zeta function, operator, geometry, or spectral wrapper around the primes.

Do not assume that every many-to-one map is mathematically interesting information loss, that every preserved invariant is a useful discriminator, or that vocabulary borrowed from information theory, statistics, category theory, or physics automatically supplies the required theorem. Analogies must be converted into exact definitions and results in the mathematical category being studied.

Prime-specific constructions should be deferred when the same structural question can first be tested on cleaner general examples. Conversely, once an abstract claim is precise, do not avoid arithmetic stress tests merely to preserve generality.

### Line-specific falsification controls

For candidate definitions and theorems, test specifically whether:

- the proposed notion distinguishes nontrivial structural survival from ordinary injectivity or tautological recoverability;
- the result is invariant under harmless reparameterization or equivalent presentation of the same mathematical object;
- matched pairs with the same compressed image genuinely differ in the claimed upstream discriminator rather than only in irrelevant labeling;
- a purported minimal lift is actually minimal, natural, and not just a hidden copy of the original object;
- a claimed no-go theorem survives alternative encodings or factorizations of the same transformation;
- composition claims correctly distinguish information lost at an earlier map from structure newly introduced downstream;
- phase, sign, marking, boundary, transverse, or provenance data are necessary rather than convenient coordinates;
- examples from different fields instantiate the same formal mechanism rather than merely sharing suggestive language;
- arithmetic applications distinguish rational primes from matched generalized-prime, composite, randomized, twisted, or otherwise non-prime controls at the same information layer.

### Prior-art domains

- sufficient statistics, Blackwell sufficiency, statistical experiments, and comparison of information channels;
- data-processing inequalities, recoverability, and Petz-type recovery in operator/quantum information settings;
- inverse problems, rigidity, marked versus unmarked spectra, and reconstruction from partial invariants;
- Gassmann equivalence, arithmetic equivalence of number fields, Sunada-type isospectrality, and related indistinguishability constructions;
- phase retrieval, autocorrelation, homometry, diffraction, and loss of phase/orientation under quadratic measurements;
- invariant theory, quotient constructions, categorical forgetful/factor maps, and sufficient or universal properties when they give exact control of what factors through a compression;
- coarse graining, factors and extensions in ergodic/dynamical systems, and symbolic dynamics;
- operator algebras, spectral invariants, traces, determinants, and compression/dilation theory;
- information geometry and mathematical notions of distinguishability when they yield structural rather than purely quantitative criteria;
- Beurling/generalized primes and arithmetic-equivalence phenomena as later adversarial test beds for prime-specific fidelity.

### Relationship to other lines

This line is transversal rather than a replacement for the existing RH lines. `prime_circle`, `prime_flute`, `prime_lattice`, `weil_positivity`, and `weil_inertia` may supply concrete examples where an arithmetic discriminator appears to be lost under canonicalization, local-to-global passage, positivity, scalarization, averaging, limiting, or analytic aggregation.

Arithmetic Fidelity should abstract such examples only when a genuinely reusable theorem or definition emerges. In the opposite direction, a general no-go, recovery, or minimal-lift result may constrain or sharpen an existing line, but the concrete line remains responsible for proving that its own mathematical construction satisfies the hypotheses.

The eventual rational-prime application is downstream: first understand structural survival under compression in general, then ask which retained structures can distinguish the rational primes from matched non-prime controls before any RH-relevant analytic or spectral conclusion is attempted.