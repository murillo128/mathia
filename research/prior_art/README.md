# Canonical prior art

`research/prior_art/` is a human-readable projection of mathematical entities and
mechanisms that Mathia or qwen-lean already processed. It is not a new corpus, a
literature search, or the source of truth for the historical evidence. The frozen
experiment releases and the pinned qwen-lean revision remain authoritative.

This directory deliberately sits beside the separately curated `graph/` subtree.
Issue #63 does not change live findings, mind notes, or graph state.

## Checkpoint A: inventory and projection design

The inventory was taken from Mathia revision
`676855531b75ee145fced8facebe70812e327df2` and the local qwen-lean checkout at
`3364b508595a71b34a2efcf964ba1200f153ad84`. The qwen Riemann data files were last
changed by `61175c1b212a1b3fed1b227cc6967762a35f31be` and are pinned by their Git
blob identities in the coverage report that will accompany the completed
projection.

### Artifact families found

| Family | Authoritative binding | Retained material inspected | Role in this projection |
| --- | --- | ---: | --- |
| Riemann–Mathia v2 (#42) | `riemann_mathia_v2_cd92907b9bc4565cffc138110faceb21c77d4bf71388d75536a8e640af3ba5f0` | 423 relevant bibliographic records; 8,264 interchange objects, of which 8,003 are accepted | Primary accepted semantic evidence and source/object provenance |
| Riemann–Mathia v1 | `riemann_mathia_full_e9f9f663e6f3a777ab7545f088f39d0662462f5da622364204e52be6fcf42cd6` | 568 immutable parent objects, carried into v2 where eligible | Parent lineage only; v2 governs overlaps and corrections |
| OpenAlex Riemann graph (#46) | practical-saturation graph in `experiments/openalex_discovery/run_v1/graph_summary.json` | 11,753 accepted discovery candidates, 37,943 citation edges, 104 duplicate groups | Identity, discovery, citation, and duplicate/version evidence only |
| OpenAlex Riemann full-text handoff (#46 → #42) | `riemann_fulltext_v2`, freeze `openalex_handoff_89e50c9a268c116f9ca85d457e4cae8e3efa6f7feed64fbd1f815f0ded9d0dc6` | 25 immutable full-text handoff records | Source identity and exact v2 handoff lineage; v1 is superseded |
| Domain-agnostic Mathia v1 (#44) | `freeze_eeeeb89af3d2ac75d1ff5dad5623b63d1d24dfbddb965beca2f1c4aac9f9867f` | 222 interchange objects, of which 214 are accepted | Cross-domain mechanisms already accepted by #44 |
| Agnostic OpenAlex supplement (#42/#46) | `agnostic_openalex_supplement_a1aa591df034db64d5ce0271df0da570e3aaf470ac49e5cc4014b66181bf0e33`; handoff `agnostic_mathia_fulltext_v2` | 600 interchange objects, of which 595 are accepted | Later accepted cross-domain semantic evidence |
| qwen-lean Riemann atlas | `murillo128/qwen-lean@3364b508595a71b34a2efcf964ba1200f153ad84` | 234 atlas entries, 226 typed relationships, 18 atlas bibliographic sources | Canonical names, aliases, RH relation, source IDs, and formalization status |
| qwen-lean formal-source manifest | same qwen-lean revision | 22 accepted external records and one accepted project | Formalization provenance, not mathematical proof beyond the recorded status |

The v2 Riemann release contains 3,694 source, 3,694 interpretation, and 876
synthesis objects before quality filtering. Its eligible projection surface is
3,694 source, 3,630 interpretation, and 679 synthesis objects. Rejected,
quarantined, evaluation-only, and superseded evidence is never positive support.

The OpenAlex graph is not a mathematical truth layer. Its 11,753 accepted works
are therefore considered for identity and coverage, but only records that passed
the later #42/#44 semantic quality gates may support mathematical prose.

### Local artifact availability

The roots below were derived from retained manifests before being checked. They
were present at inventory time:

- `/workspace/mathia-artifacts/riemann-corpus-v0`
- `/workspace/mathia-artifacts/riemann-corpus-v2`
- `/workspace/mathia-artifacts/agnostic-mathia-openalex-supplement-v1`
- `/mnt/openalex/openalex/handoffs/riemann_fulltext_v2`
- `/mnt/openalex/openalex/handoffs/agnostic_mathia_fulltext_v2`

Raw or normalized source bytes may be consulted only to resolve the identity,
citation, version, or ambiguity of an already-analyzed object. They are not mined
for new claims and are not copied into Git.

### Canonicalization calibration cases

These cases define the intended granularity before the full projection is
materialized:

| Canonical ID | Historical records to collapse | Boundary retained |
| --- | --- | --- |
| `PA-baez-duarte-criterion` | Mathia coefficient/decay analyses and qwen atlas entry `baez-duarte-criterion` | The sequence criterion remains distinct from the discrete strengthening of Nyman–Beurling |
| `PA-nyman-beurling-criterion` | Repeated Mathia units about the functional-analytic closure criterion and qwen entry `nyman-beurling-criterion` | No constructive approximating sequence or Lean proof is inferred |
| `PA-baez-duarte-strengthening-of-nyman-beurling` | Mathia source `baezduarte2003_nyman` and qwen source `baez-duarte-2002`, both bound to arXiv `math/0202141` | Preprint/publication identity is merged, but this theorem is not merged with the Báez-Duarte sequence criterion |
| `PA-de-bruijn-newman-deformation` | Repeated heat-flow/threshold analyses and qwen entry `debruijn-newman` | The proved lower bound and RH-equivalent upper-bound condition remain distinct |
| `PA-montgomery-pair-correlation` | Mathia zero-statistics interpretations and qwen entry `montgomery-pair-correlation` | Conjectural/statistical evidence is not promoted to an RH implication |
| `PA-hilbert-polya-program` | Spectral-program and quantum-chaos source units | A program/conditional mechanism is not a constructed operator or proof |
| `PA-mertens-conjecture` | qwen entry `mertens-conjecture` plus any accepted Mathia historical discussion | A disproved stronger conjecture is not treated as an open RH criterion |

Identity is merged only when the retained records establish the same mathematical
entity. Similar mechanisms remain separate, and unresolved cases are recorded
rather than guessed.

### Stable note format

Every canonical note uses this small frontmatter contract:

```yaml
---
id: PA-canonical-slug
type: prior-art
canonical_name: Human-readable mathematical name
aliases:
  - Supported alias
kind: criterion
topics:
  - riemann-hypothesis
---
```

`id` is exactly `PA-` plus the deterministic lowercase ASCII slug of
`canonical_name`; punctuation becomes a hyphen, consecutive hyphens collapse,
and leading or trailing hyphens are removed. A rare intentionally stable ID that
cannot equal that slug must be listed in the explicit canonicalization decisions
with a rationale.

The body contains `What it is`, `Relation to RH / Mathia research`, `Known scope
and limits`, `Related prior art`, and `Evidence and provenance`. Provenance uses
exact repository paths plus object/unit/source IDs, or a qwen-lean repository,
revision, path, and atlas/source ID. Related-note links are ordinary relative
Markdown links; no graph ontology is introduced here.

## Checkpoint B: calibration audit

The first materialized set contains 17 heterogeneous nodes: six criteria, one
criterion plus partial result, two research programs, one theorem family, two
partial-result families/methods, one proved analogue, one conjecture, one
disproved conjecture, one heuristic framework, and one mathematical system. It
includes nine notes with a strong or conditional RH relation, ten manual
canonicalization decisions, and eight notes that combine Mathia and qwen
provenance.

Every calibration note was checked for identity, status, claim strength,
granularity, provenance, and usefulness. The audit found one material initial
over-merge: the Báez-Duarte sequence criterion had been conflated with
Báez-Duarte's discrete strengthening of Nyman–Beurling. They are now separate
nodes. Only the 2002 preprint / 2003 publication identity for arXiv
`math/0202141` is merged. The audit also removed an unsupported relation between
the Bost–Connes system and the adele-class trace program, and corrected the
function-field explicit-formula relation from a historical claim to an analogy.

The calibration passed deterministic rendering, accepted-evidence resolution,
exact qwen blob/ID checks, stable-ID checks, and link checks. The small schema was
sufficient; scaling continues without adding an ontology or changing the note
contract.

## Status

Checkpoints A and B are complete. The remaining work is full retained-family
coverage, final deterministic validation, and the required fresh independent
review.
