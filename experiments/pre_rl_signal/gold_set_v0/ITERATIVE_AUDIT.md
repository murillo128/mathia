# Iterative audit log for gold-set-v0

Issue: #21

This log preserves the closed audit/correction loop after the issue-8 audit and
`REMEDIATION.md`. No Qwen, API solver, or other model inference was used to
select or tune these corrections.

## Cycle 1

- Audited commit: `d4838cba60b6a41ebf1d3f3b1f1b9fe234d57a0c`
- Verdict: **REVISE**
- Material findings:
  - G10--G12 visible examples and the G/M structural contexts settled repeated
    Boolean theorem-restatement tasks instead of supporting unseen consequences.
  - G T3/T4, coprime CRT T4, and M T4 contained constant-answer templates; the
    three coprime CRT reconstructions also all encoded `x = mn - 2`.
  - M17--M20 T3 accepted only one integer representative of a modular
    coefficient even though the prompt did not define a canonical interval.
  - Python/JSON Boolean values were accepted as integer components of collision
    witnesses.
- Corrections made:
  - Replaced the leaking G conclusions with varied unseen inverse-reconstruction
    and two-step transformation consequences.
  - Replaced constant coprime CRT and composition tasks with varied numeric
    counterfactuals, and assigned unrelated CRT reconstruction targets.
  - Added semantic `mod_int` scoring for composition coefficients.
  - Rejected Boolean witness components explicitly and added validator
    regressions for equivalent modular representatives, witness types, fixed CRT
    offsets, repeated constant prompts, and constant Boolean templates.
- Validation after correction:
  - `python3 validate.py` passed: 20 situations, 80 tasks, and semantic witness
    scoring.
  - `python3 materialize.py` completed.
  - `python3 -m unittest discover -s experiments/pre_rl_signal/tests -v`
    passed all 16 tests.
  - Independent arithmetic probes passed for the new reconstruction, two-step
    gcd, CRT, composition, modular-scoring, and witness-type cases.
- Next audited target: the published commit containing this cycle entry. A commit
  cannot contain its own SHA; the exact published SHA is therefore fixed in the
  cycle-2 audit request and recorded in the next cycle entry.
