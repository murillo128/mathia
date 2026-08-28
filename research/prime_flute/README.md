# Prime-flute research notes

This directory preserves high-signal findings from the exploratory **prime-circle / hyperbolic prime-flute** line so they can be reused later by Mathia, independent review, and Lean formalization.

It is intentionally separate from `experiments/riemann_corpus/`: the frozen Riemann corpus records sourced mathematical literature, while this directory records **our derived observations, candidate theorems, obstructions, and research dead ends** about one particular geometric construction.

Nothing here should silently be treated as a proved result. The strongest custom claims remain research notes until independently checked and, where practical, formalized.

## Geometric convention

For consecutive odd primes `p_n`, write

```text
g_n     = p_{n+1} - p_n
u_n     = cot(pi / p_n)
Delta_n = u_{n+1} - u_n
h_n     = log(u_n / u_{n-1})
```

The zero-twist tight flute is the Fuchsian surface obtained from the increasing endpoint sequence `u_n`. The `p=2` endpoint is degenerate under this coordinate, so formulas involving ratios normally start at `p=3`.

## Evidence labels

- **EXACT-DERIVED** — algebraic/hyperbolic identity derived directly from the explicit generators; intended to be checkable without prime-distribution input.
- **LITERATURE+DERIVED** — combines a published theorem with a new consequence for this construction.
- **NEGATIVE/OBSTRUCTION** — shows that a tempting route loses the prime information or cannot support the hoped-for spectral mechanism.
- **CONJECTURAL** — depends on an unproved prime-statistics model or conjecture.
- **NEEDS-AUDIT** — promising claim from the exploration whose exact hypotheses or source bridge still need independent checking.

These labels describe provenance, not mathematical importance.

## Files

- [`findings/`](findings/) — canonical positive and negative research findings, including derivations, evidence status, prior-art audits, and failure modes.
- [`LEAN_CANDIDATES.md`](LEAN_CANDIDATES.md) — a deliberately small queue of statements worth formalizing first.
- [`SOURCES.md`](SOURCES.md) — literature anchors used by the current notes.
- [`graph/index.md`](graph/index.md) — derived navigation and relation view; it is not a source of mathematical truth.

## Intended reuse

For **Mathia**, the most useful objects are not only successful bridges. Negative results expose reusable conceptual moves: identify a coboundary, detect telescoping, separate intrinsic from imported structure, recognize a universal invariant, or find a degenerating mode that invalidates a spectral analogy.

For **Lean**, priority should go first to finite algebraic/hyperbolic identities. Analytic-number-theory and infinite-surface spectral consequences should be split into a formalizable local lemma plus a clearly named external theorem assumption rather than encoded as an opaque monolith.

## Current high-level picture

The exploration repeatedly separates three regimes:

```text
one-dimensional / local reductions
    -> telescope, universalize, or recover a known prime Dirichlet series

projective multi-gap / tangent data
    -> retain genuinely relational gap information and can drive real spectral effects
    -> but are invariant under global integer dilation p_n -> K p_n
       and therefore have an all-composite clone (PF-099)

exact finite-scale cotangent geometry
    -> breaks that dilation gauge through the nonprojective endpoint defect
    -> first four-point Möbius-invariant correction appears at order P^-4 (PF-082)
    -> but the leading P^-4 normalized local scattering response is reproduced by
       any matched smooth endpoint control x - a/x + O(x^-3) (PF-101)
```

The exact cross-ratio of four endpoints remains the cleanest intrinsic bridge from several gaps to an actual separating geodesic. PF-099 sharpens its arithmetic interpretation: **the projective/tangent limit encodes gap shape, not primality specificity**. PF-101 adds a second control: although the exact cotangent geometry breaks the dilation gauge, **a finite asymptotic endpoint jet does not by itself supply a distinguished RH scale**. Matching the `1/x` jet moves the first local direct-scattering distinction from `P^-4` to `P^-6`, and matching further jets can postpone it again. Any viable exact-geometry mechanism must therefore use more than a fixed finite perturbative jet, most naturally a genuinely nonperturbative/global property of the exact endpoint geometry coupled to the actual prime sampling.

The major negative lessons remain that ordinary Selberg/Ruelle products, uniformly expanding Bowen--Series operators, modular/Hecke inheritance, raw global scalar Laplace data, featureless relative backgrounds, and finite-jet scattering phase scales encounter structural obstructions before they can plausibly encode the Riemann zeros.