# Mathia research graph

`research/graph/` is a **derived presentation layer** for the live Mathia research program. It is not mathematical source of truth.

Authoritative knowledge remains in:

- `research/*/findings/`;
- `research/*/mind/`;
- `research/mind/`;
- `research/prior_art/` once the prior-art projection is materialized.

The graph files are intentionally empty scaffolds. A later independent research-graph curator may regenerate their managed sections from authoritative research material without editing the underlying findings, intuitions, or prior-art notes.

## Views

- `global.md` — aggregate Mathia research graph.
- `prime-circle.md` — Prime Circle subgraph.
- `prime-flute.md` — Prime Flute subgraph.
- `prime-lattice.md` — Prime Lattice subgraph.
- `prior-art.md` — canonical prior-art subgraph.

## Obsidian

Open the repository root (`mathia/`) as an Obsidian vault. The committed `.obsidian/graph.json` configures the built-in Graph View to show only `research/` by default.

For a future line-specific view, open the corresponding graph note and use Obsidian's **Open local graph** command. Once the curator materializes links in that hub, the local graph becomes the subgraph for that research line.

No community plugin is required for this initial scaffold. Per-device workspace state and downloaded plugins/themes are intentionally ignored by Git.
