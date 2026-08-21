# Whole-source semantic-depth review (Riemann–Mathia v2)

Inspect every assigned normalized source from first through last usable line. This is a source-depth audit and semantic segmentation task, not a request to explain the paper from memory.

Read the exact `normalized_abspath`. Treat the machine outline as navigation only; verify headings and line numbers against the file. The normalized source SHA-256 and line count are frozen in the assignment. Existing v1 units are immutable prior work: preserve their IDs and do not silently rewrite them, but identify when they need more surrounding context in v2.

For each source, emit exactly one compact JSON object on one physical line with these fields:

```text
source_id
normalized_sha256
inspection_summary
sections_inspected[]: {label,line_start,line_end,mathematical_role}
accepted_units[]: {
  local_unit_id,
  unit_type,
  title,
  line_start,
  line_end,
  why_material,
  context_note,
  representation_dependency
}
coverage_segments[]: {
  line_start,
  line_end,
  disposition,
  reason
}
carried_v1_unit_ids[]
v1_context_repairs[]: {unit_id,needed_line_start,needed_line_end,reason}
within_source_synthesis_candidates[]: {title,parent_local_unit_ids,claim,limit}
remaining_meaningful_material[]
within_source_saturation
stop_reason
```

Rules:

- `sections_inspected` must account for the whole usable mathematical text, not just the introduction and named theorems.
- `coverage_segments` must be ordered, non-overlapping, and cover lines 1 through `line_count` with no gap. Allowed dispositions are `unit-bearing`, `supporting-context`, `routine-or-repetitive`, `bibliography-or-front-matter`, `outside-rh-scope`, and `extraction-defective`.
- Select every materially useful semantic unit supported by the text. A short source may yield few; a rich paper, survey, thesis, or monograph may yield dozens or more. There is no count target or ceiling.
- Units may be definitions, motivation, theorem-plus-proof fragments, constructions, representation changes, examples/counterexamples, method comparisons, obstructions, failed routes, equivalent criteria, historical changes, or computational certification logic.
- A unit must be coherent at its exact line span. Include local setup when severing it would force reconstruction from memory. Overlap is allowed when mathematically necessary.
- Do not select title pages, contents, bibliographies, routine algebra with no reusable mechanism, repeated statements, or unreadable formula-dependent OCR merely to increase yield.
- For OCR, accept only spans whose mathematics is recoverable from checked prose; mark image/formula dependencies and request later scan verification.
- `remaining_meaningful_material` must be empty only when further segmentation would predominantly repeat represented mechanisms or select routine/defective material.
- `stop_reason` must describe source-specific evidence. A quota or batch size is never a valid stop reason.
- Do not import facts from adjacent pages, another edition, or your pretraining memory.

Write only JSONL to the requested output path. Do not modify source text, v1 artifacts, code, or any other file.
