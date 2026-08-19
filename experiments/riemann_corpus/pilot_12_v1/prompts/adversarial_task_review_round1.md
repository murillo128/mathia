# Fresh adversarial review of the behavioral discriminator

Review every record in `candidate_behavioral_tasks.json` and `candidate_transfer_tasks.json` in a fresh isolated context. Treat the candidate author's rationale as a claim to attack, not as an answer key to endorse.

For each candidate, inspect the exact source unit (including the three versioned external repair artifacts) or the stated standard mathematics and decide `accept` or `reject`. Reject rather than rewriting a weak task into a longer explanation.

Check all of the following:

1. Can the core answer be recovered from stylistic cues, option length, generic calibration language, or Mathia vocabulary without using the mathematical mechanism?
2. Is the expected answer genuinely fixed by the source or standard mathematics?
3. Is at least one wrong option plausible to a model that has memorized wording but missed the mechanism?
4. Does the cosmetic perturbation preserve the semantic answer without leaking it?
5. Does the structural perturbation change the answer for the stated mathematical reason?
6. Is the task secretly a calculation exercise, a theorem-name lookup, or an ordinary logic question rather than a conceptual behavior probe?
7. Do prompt or option asymmetries reveal the answer?
8. For Riemann tasks, would success remain meaningful after removing source-specific proper nouns where the prompt permits it?
9. Does the source-grounded justification stay within the frozen unit, with v1 evidence used only for the three repaired units?
10. Can the answer be scored by the discrete core without treating agreement with Codex prose as truth?

Write one JSONL record per candidate in the exact candidate-file order with these fields:

- `candidate_id`
- `decision`: `accept` or `reject`
- `mathematical_determination`: concise evidence for whether the keyed answer is correct
- `style_shortcut_risk`: concrete cue analysis
- `cosmetic_pair_check`
- `structural_pair_check`
- `calculation_or_recall_confound`
- `source_or_standard_basis_check`
- `subjective_judgment_required`: boolean
- `reason`: concise final basis for the decision

Do not edit candidate tasks, source units, v0 artifacts, reports, or GitHub state. Do not treat agreement with the candidate author as independent mathematical validation.
