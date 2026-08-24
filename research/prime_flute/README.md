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

- [`FINDINGS.md`](FINDINGS.md) — indexed positive and negative results, with derivation sketches and open verification points.
- [`LEAN_CANDIDATES.md`](LEAN_CANDIDATES.md) — a deliberately small queue of statements worth formalizing first.
- [`SOURCES.md`](SOURCES.md) — literature anchors used by the current notes.

## Intended reuse

For **Mathia**, the most useful objects are not only successful bridges. Negative results expose reusable conceptual moves: identify a coboundary, detect telescoping, separate intrinsic from imported structure, recognize a universal invariant, or find a degenerating mode that invalidates a spectral analogy.

For **Lean**, priority should go first to finite algebraic/hyperbolic identities. Analytic-number-theory and infinite-surface spectral consequences should be split into a formalizable local lemma plus a clearly named external theorem assumption rather than encoded as an opaque monolith.

## Current high-level picture

The exploration repeatedly separates two regimes:

```text
one-dimensional / local reductions
    -> telescope, universalize, or recover a known prime Dirichlet series

multi-gap Möbius invariants
    -> retain genuinely relational prime information
```

The strongest intrinsic object found so far is the cross-ratio of four prime endpoints, because it gives an exact separating geodesic length and therefore a direct route from several prime gaps to hyperbolic geometry. The most important negative lesson is that ordinary Selberg/Ruelle, a uniformly expanding Bowen-Series operator, modular/Hecke inheritance, and the raw global Laplacian all encounter structural obstructions before they can plausibly encode the Riemann zeros.