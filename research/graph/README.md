# Research graph views

This directory owns only the **global derived research graph**.

Line-local graph views live beside their source knowledge:

- `research/prime_circle/graph/`
- `research/prime_flute/graph/`
- `research/prime_lattice/graph/`
- `research/prior_art/graph/`

The global graph may aggregate those local views and cross-line relationships, but it must not become a source of mathematical truth. Findings, mind notes, and prior-art notes remain authoritative; graph content is regenerable presentation state for Obsidian and recurring graph curation.

The procedural authority for the scheduled Research Graph Curator watch is:

```text
.agents/skills/mathia-research-graph-curator/SKILL.md
```

The curator may derive and publish graph state, resolve source-backed prior-art dependencies, and perform only the bounded external prior-art lookup allowed by its skill. It must not perform new mathematical derivations or modify findings/mind as graph presentation state.

## Obsidian

Open the repository root (`mathia/`) as an Obsidian vault. The committed `.obsidian/graph.json` configures the built-in Graph View as a focused research graph rather than a graph of every Markdown file in the repository.

The default global filter includes only graph-relevant research paths (`findings/`, `mind/`, `graph/`, `prior_art/`, and `clues/`), excludes structural files such as `README.md`, `FINDINGS.md`, `SOURCES.md`, `COVERAGE.md`, and `LEAN_CANDIDATES.md`, hides unresolved links, and hides orphan notes. A canonical note therefore appears in the global graph only when it participates in the research knowledge graph.

### Color groups

Obsidian's built-in graph gives a node one effective group color, so the committed groups use this priority:

1. finding polarity/status;
2. canonical prior art;
3. mind and clues;
4. research-line color for remaining structural graph nodes.

The default palette is:

- red: findings whose persisted status line marks a negative, obstruction, branch closure, novelty downgrade, or prior-art closure;
- green: findings whose persisted status line marks a positive/exact/literature-derived/proved result and that were not already classified negative;
- gray: other or unclassified findings;
- purple: canonical prior art and its graph view;
- gold: durable `mind/` synthesis;
- yellow: research clues;
- blue: remaining Prime Circle graph nodes;
- orange: remaining Prime Flute graph nodes;
- teal: remaining Prime Lattice graph nodes;
- dark gray: global graph nodes.

The status colors are derived from the persisted `**Status:**` / `**Evidence/status:**` line. A new finding normally requires no Obsidian configuration change. If its vocabulary is not covered by the stable status queries it simply remains in the neutral finding group until the visualization contract is intentionally extended.

For a line-specific view, open that line's `graph/index.md` and use Obsidian's **Open local graph** command. No community plugin is required.

### Curator maintenance boundary

The Graph Curator should **not** rewrite color groups on every run or for every new finding. The path/status queries are intentionally declarative so ordinary research updates classify themselves automatically.

The curator only needs to update `.obsidian/graph.json` when a durable visualization-level change occurs, especially when a genuinely new research line is created and should receive its own base color, or when a new stable node/status class is intentionally added to the graph model. Such a change is presentation state and must not be used as mathematical evidence.
