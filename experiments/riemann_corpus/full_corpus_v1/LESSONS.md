# Checkpoint N — extraction lessons frozen for corpus scale

The immutable pilot v0, three v1 unit repairs, three behavioral review rounds,
and accepted/rejected calibration evidence remain unchanged. Their lesson is a
change in extraction behavior, not a universal explanation template:

- a semantic unit is the smallest contiguous span at which a mathematical
  mechanism is intelligible, and may cross theorem or paragraph boundaries;
- the exact source mathematics remains a separate, hash-bound training object;
- spontaneous reading may find an unanticipated structure, while the directed
  reading uses the concepts/dimensions document only where the source supports
  it;
- the fresh critic must remove paraphrase, generic explanation, imported
  context, unsupported analogy/generalization, proof overreach, and recurrent
  teacher wording;
- the revision keeps mathematical anchors, representation gains/losses,
  boundaries, uncertainty, and marked speculation, but its prose structure is
  allowed to follow the mathematics;
- counterfactual or behavioral probes are optional QA for a concrete claimed
  mechanism, not a required field or the final product.

The full release therefore uses shared object-level interchange metadata but
does not reuse the pilot's rigid nine-field training-facing cadence.

The initial corpus-scale segmentation was deliberately retained as a coverage
pass, but its one-unit-per-source instruction was not treated as the final
segmentation. A second isolated whole-source pass made no-addition, quarantine,
and zero-to-four-addition decisions source by source. This remediation is part
of the frozen extraction lesson: broad source coverage can be deterministic
without pretending that every paper contains the same number of useful ideas.
