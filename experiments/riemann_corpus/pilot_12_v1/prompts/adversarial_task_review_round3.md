# Fresh adversarial review of the bounded third-round discriminator

Review every record in `candidate_behavioral_tasks_round3.json` and `candidate_transfer_tasks.json` in a new isolated context. Six RH records are carried forward verbatim because round two accepted them; re-check rather than grandfather them. The first two candidate/review rounds remain immutable negative evidence and must not be reinterpreted as accepted.

Treat the candidate author's rationale as a claim to attack. Inspect the exact frozen source unit, including versioned external repair artifacts where referenced, or the stated standard mathematics. Decide `accept` or `reject`; reject rather than rewriting a weak item.

For each candidate check:

1. Can option position, lexical overlap, length, generic calibration language, or Mathia vocabulary reveal the key without the mathematical move?
2. Is the core answer uniquely determined by the source or standard theorem?
3. Is at least one wrong option plausible to a model that retained surface wording but missed the mechanism?
4. Does the cosmetic variant preserve the exact answer without leaking it?
5. Does the structural variant change the exact answer because the carrying mathematical condition changed?
6. Is the item merely calculation, theorem-name recall, elementary implication logic, or restatement of a relation supplied in the stem?
7. Does the prompt require comparing, transporting, or diagnosing a mathematical role rather than selecting the most careful-sounding prose?
8. For RH tasks, does the keyed behavior remain meaningful when unnecessary proper nouns are absent?
9. Does the justification stay within its exact frozen source evidence?
10. Is exact discrete scoring sufficient, without subjective prose judgment or Codex agreement?

Write one JSONL record per candidate in exact current file order with exactly:

- `candidate_id`
- `decision`: `accept` or `reject`
- `mathematical_determination`
- `style_shortcut_risk`
- `cosmetic_pair_check`
- `structural_pair_check`
- `calculation_or_recall_confound`
- `source_or_standard_basis_check`
- `subjective_judgment_required`: boolean
- `reason`

Do not edit candidate tasks, units, earlier reviews, reports, or GitHub state.
