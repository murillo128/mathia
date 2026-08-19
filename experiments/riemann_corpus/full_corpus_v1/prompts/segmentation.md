# Isolated semantic-unit selection

You are selecting one mathematically coherent semantic unit from every assigned
normalized source for the full Riemann–Mathia corpus. Read each whole normalized
file named by the assignment. Do not select by title or abstract alone when the
paper contains a clearer mechanism later.

For each source choose exactly one contiguous line span at the smallest scale
where a concrete definition, result, construction, comparison, proof mechanism,
obstruction, historical shift, computation contract, or explicit limitation is
intelligible. Usually 35–140 normalized lines is appropriate, but mathematical
coherence controls. Include adjacent setup or conclusion when separation would
erase the mechanism. Avoid references, publisher boilerplate, isolated formula
fragments, and generic introductory praise.

For OCR sources, prefer prose-rich spans and do not rely on a damaged formula.
If no trustworthy span exists, use `quarantined` and explain why. For the partial
book preview, use only its retained pages and state the limit. Do not reconstruct
missing mathematics from memory. A figure must be recorded as `essential`,
`useful`, `provenance_only`, or `none`; text that depends on an unavailable
essential figure must be quarantined.

Write JSONL in exact assignment order, one object per source, with exactly:

```text
source_id
segmentation_decision        # accepted | quarantined | excluded
line_start                   # integer for accepted, otherwise null
line_end                     # integer for accepted, otherwise null
source_pages                 # page marker numbers inside/adjacent to span
unit_type                    # compact mathematical role, not a fixed ontology
selection_reason             # source-specific mechanism visible in the span
context_limit                # exact missing/adjacent context limit, or null
representation_dependency   # essential | useful | provenance_only | none
segmentation_provenance      # isolated-codex-semantic-selection
```

Check line numbers directly against the normalized file. Do not write source
text into Git. Do not edit any pilot file or any file besides the requested
batch output.
