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
- Next audited target: `02f57212d1bfdd60367059fafcb7408debdaed42`

## Cycle 2

- Audited commit: `02f57212d1bfdd60367059fafcb7408debdaed42`
- Verdict: **REVISE**
- Material findings:
  - Coprime CRT T2 still asked for the constant scalar stated by the structural
    uniqueness context.
  - Sequential situation-level shuffled assignments associated some source
    passages uniquely with unit/nonunit or coprime/noncoprime subtypes.
  - The cycle-1 constant-template regression compared literal prompts and did
    not protect number-bearing non-Boolean families as claimed.
- Corrections made:
  - Replaced CRT T2 with four varied coordinate-subset consequences whose exact
    counts require applying the representation to instance-specific sets.
  - Use one common mechanism-orthogonal shuffled passage for every situation,
    eliminating source identity as a cluster, subtype, difficulty, or answer-kind
    correlate.
  - Require full answer diversity for every corrected cluster/task family,
    independent of prompt literals, and assert the new coprime CRT task type.
- Validation after correction:
  - `python3 validate.py` passed: 20 situations, 80 tasks, and semantic witness
    scoring.
  - `python3 materialize.py` completed.
  - `python3 -m unittest discover -s experiments/pre_rl_signal/tests -v`
    passed all 16 tests.
  - Independent probes recomputed all four CRT subset counts and verified the
    common shuffled source and every protected family's answer diversity.
- Next audited target: the published commit containing this cycle entry. Its
  exact SHA is fixed in the cycle-3 audit request and recorded in the next entry.
