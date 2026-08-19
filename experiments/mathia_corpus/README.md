# Shared Mathia corpus interchange v1

This directory defines the smallest common training boundary required by
Mathia issues #42 and #44. It is an experiment-local compatibility interface,
not a mathematical ontology, dataset language, or prescription for how an
interpretation must be written.

## Trainable roles and private metadata

The contract has three trainable object roles: `source`, `interpretation`, and
`synthesis`. A representation such as a figure can be attached to any role by
`representation_dependencies`; it does not create a second corpus dialect.

Every record uses the same required metadata fields:

- `contract_version`, `corpus_release_id`, `object_id`, and `object_role`;
- private `corpus_origin`;
- `source_ids`, `source_unit_ids`, and exact `span_lineage`;
- `content_sha256` plus exactly one of inline `content` or `content_ref`;
- `parent_ids` and `derivation_ids`;
- `teacher_provenance`;
- `quality_state`, `training_eligibility`, and `exclusion_reason`;
- `licensing_boundary`, `representation_dependencies`, and
  `canonical_source_keys`.

The four shared quality states are:

- `accepted`: eligible positive training material;
- `quarantined`: potentially useful, but source, context, or representation
  quality is not sufficient;
- `rejected`: unsuitable as positive Mathia training material;
- `evaluation_only`: QA or behavioral material that must not enter training.

Only `accepted` records may be `eligible`. Rejected, quarantined, and
evaluation-only artifacts remain auditable but are excluded from the trainable
manifest.

`content_ref` is resolved relative to the release's declared content roots by
the corpus-specific release validator. It may point to an external artifact
store when redistribution is restricted. The common interface never assumes
that source text may be committed.

## Stable identity and lineage

`object_id` is derived from role, exact content hash, canonical source lineage,
and parent identities. It does not include corpus origin or release name. Thus
an identical source unit can retain the same identity across releases, while a
different interpretation of that unit receives a distinct identity. The
validator also groups exact content hashes and canonical source keys so a
future mixer can detect duplicates without making duplication an implicit
training weight.

## One model-visible renderer

`interchange.render_training_example` is the only default renderer. It
normalizes Unicode, line endings, trailing whitespace, and repeated blank
lines, then uses the same Markdown wrappers and requests for every release:

- source-only: mathematical material;
- source plus request to interpretation: mathematical material, common task,
  response;
- multiple sources to synthesis: numbered mathematical materials, common
  synthesis task, response.

The renderer does not inspect or print corpus origin, release name, quality,
teacher, acceptance, licenses, IDs, or provenance. This is verified by
counterfactually changing private metadata and requiring byte-identical
rendering. Mathematical content itself is not censored: a source may naturally
mention Riemann, geometry, its author, or its own title.

PDF-extraction C0 bytes are never silently guessed or deleted: form feeds
become page-break newlines and undecodable control bytes become visible Unicode
replacement markers. Source formulas, Unicode, Markdown, and internal headings
otherwise remain verbatim after whitespace normalization; the renderer alone
supplies the outer wrappers.

## Representation sidecars

Each dependency records `asset_id`, `relationship`
(`essential`, `useful`, or `provenance_only`), `availability`, `content_ref`,
and `content_sha256`. Available assets need a reference and hash. An unavailable
essential asset makes an object ineligible, so a text-only release cannot imply
that an omitted essential diagram was preserved.

Cross-release duplicate groups carry both release and object identities and are
reported only when a hash or canonical key actually crosses release boundaries.
Mixed-manifest selections likewise retain private release identity so the dry
run proves that both releases were sampled without exposing origin in rendered
training text.

The representative agnostic fixture is deliberately small. It exercises the
same source, interpretation, and synthesis roles used by #42 while #44 is still
under construction. A synthetic mixed manifest is a compatibility dry run,
not a training mix or authorization to train.
