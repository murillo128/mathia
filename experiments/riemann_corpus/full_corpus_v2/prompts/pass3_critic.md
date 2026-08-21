# Riemann–Mathia v2 fresh adversarial criticism

This is a fresh isolated critic context. For every assigned unit, independently read the exact source artifact and then inspect the supplied pass-1/pass-2 output. The source span is the evidence boundary. Do not reward agreement, fluency, famous-theorem familiarity, or recognizable Codex style.

Emit one compact JSON object per unit, in exact assignment order, on one physical JSONL line, with exactly:

```text
unit_id
critic_decision: accept_as_is | revise | reject | quarantine
supported[]
inference[]
unsupported_or_imported[]
paraphrase_or_style_risk[]
context_or_ocr_risk[]
missed_mechanism[]
revision_instructions[]
```

Attack these failure modes explicitly: claims not present in the frozen span; conclusions imported from adjacent pages or pretraining; formula reconstruction from OCR; generic “representation exposes structure” templates; restatement without a non-paraphrase operation; false or content-free analogies; unsupported counterfactuals or generalizations; lost hypotheses, directions of implication, normalization, or proof burden; and semantic-unit boundaries that are too narrow to support the output.

Use `quarantine` when source/context/OCR quality prevents a reliable interpretation, and `reject` when the proposed output is materially false or style/paraphrase dominated. Criticism is teacher-generated audit evidence, not mathematical truth.

Write only the requested JSONL output. Do not modify any other file.
