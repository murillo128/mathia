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

The curator may derive and publish graph-only changes, but it must not perform new mathematical/literature research or modify findings, mind, or canonical prior-art notes.

## Obsidian

Open the repository root (`mathia/`) as an Obsidian vault. The committed `.obsidian/graph.json` configures the built-in Graph View to show only `research/` by default.

For a line-specific view, open that line's `graph/index.md` and use Obsidian's **Open local graph** command. No community plugin is required.
