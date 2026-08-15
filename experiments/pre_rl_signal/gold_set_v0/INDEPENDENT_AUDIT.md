# Independent audit of gold-set-v0

Audited target: `96b7a08f8c5b31c3c844a1f2d467b9aadb2b4db8`

Issue: #8

## Verdict: REVISE

Do not freeze `gold-set-v0` or use it for the first Qwen run yet. All 80 stored
answers are mathematically correct, but the fixture does not pass the required
leakage and control-quality audit. Its witness representation also does not yet
support semantic scoring of alternative valid answers.

This was a read-only audit of the fixture. No model run was performed, and the
ceiling assessment below is a risk estimate rather than observed model behavior.

## Material findings

### Public material leaks scored answers

The public/private modules are physically separate, but several public examples
semantically disclose hidden answers:

- R02, R04, R06, and R08 show both inputs of the exact stored T4 collision
  witness in `sample_mapping`. Those rows also prove T1 and T2 false; R02 and
  R04 additionally expose the decisive gcd.
- G09--G12 expose `before_gcd`, which is exactly the answer to both T2 and T3
  once invariance is recognized. G10--G12 also visibly demonstrate the
  non-Euclidean or signed remainder behavior asked about in T4.
- C13 shows `[4, [1, 4]]`, the exact reconstruction requested by T3.
- M19 exposes `g(f(x)) = 1x+0`, making T3 an identity-map recognition task.

The validator's check for the strings `ground_truth` and `correct_answer` catches
literal key leakage, not these semantic disclosures.

### Alternative witnesses are not scoreable

Five tasks use `answer_kind="witness_pair"` and private truth stores one example
pair. The existing scorer instead implements `collision_pair` and
`crt_collision_pair`, each backed by mechanism parameters. It raises
`ValueError: unsupported answer kind: witness_pair` for the gold-set kind.

Alternative pairs such as R02 `[1,4]`, R04 `[1,9]`, R06 `[1,4]`, R08 `[1,8]`,
and C16 `[1,13]` are valid but cannot currently be accepted semantically.

### Controls do not isolate the intended comparison reliably

- Cross-cluster source IDs pass validation, but some shuffled text is still
  mechanism-adjacent. Unit/inverse text helps with coprime CRT reasoning;
  common-divisor text cues C16's shared-factor failure and M18/M20's
  noninvertible affine coefficients. Repeated source assignment by subtype can
  also correlate the shuffled source with answer structure.
- The G sterile context describes reduction to smaller pairs and a terminal
  form, so it is partly procedural rather than operationally empty.
- For coprime C13--C15, the wrong context gives the correct local conclusions
  for T1/T2 and the correct uniqueness premise for T3; it becomes adversarial
  only for T4.
- Structural contexts are not roughly length-matched to the controls in the
  R and G clusters: they contain 32--34 words versus 16--24 for the other
  conditions. This weakens the intended distinction between useful structure
  and simply receiving more context.

### Ceiling and discrimination risk is high

Of the 80 tasks, 51 have Boolean answers. Several templates are deterministically
redundant: R has T1 = T2 in all eight situations, G has T2 = T3 in all four, and
M has T3 equal to the conjunction of T1 and T2 in all four. Small gcd checks,
direct theorem restatements, and repeated answer patterns may leave little room
for a context effect under `none`, even where no specific answer leaks.

## Per-situation findings

| ID | Recomputed T1--T4 | Audit finding |
| --- | --- | --- |
| R01 | `true, true, 1, true` | No situation-specific mathematical or leakage defect; global shuffled-control and ceiling risks apply. |
| R02 | `false, false, 0, [0,3]` | Visible rows contain the exact T4 witness and prove T1/T2 false; gcd 5 is exposed. Alternative witness scoring is missing. |
| R03 | `true, true, 1, true` | No situation-specific mathematical or leakage defect; global shuffled-control and ceiling risks apply. |
| R04 | `false, false, 2, [0,8]` | Visible rows contain the exact T4 witness and prove T1/T2 false; gcd 2 is exposed. Alternative witness scoring is missing. |
| R05 | `true, true, 1, true` | No situation-specific mathematical or leakage defect; global shuffled-control and ceiling risks apply. |
| R06 | `false, false, 0, [0,3]` | Visible rows contain the exact T4 witness and prove T1/T2 false. Alternative witness scoring is missing. |
| R07 | `true, true, 1, true` | No situation-specific mathematical or leakage defect; global shuffled-control and ceiling risks apply. |
| R08 | `false, false, 0, [0,7]` | Visible rows contain the exact T4 witness and prove T1/T2 false. Alternative witness scoring is missing. |
| G09 | `true, 1, 1, false` | Visible gcd 1 is exactly T2/T3, making the far transfer retrieval after recognizing invariance. |
| G10 | `true, 13, 13, false` | Visible gcd 13 is exactly T2/T3; the displayed non-Euclidean step also answers T4. |
| G11 | `true, 6, 6, false` | Visible gcd 6 is exactly T2/T3; the displayed negative remainder answers T4. |
| G12 | `true, 13, 13, false` | Visible gcd 13 is exactly T2/T3; the displayed negative remainder answers T4. |
| C13 | `true, 1, 4, false` | Visible row `[4,[1,4]]` exactly answers T3. Wrong and shuffled controls are mechanism-adjacent on this task family. |
| C14 | `true, 1, 29, false` | Answers are valid and do not visibly leak; wrong and shuffled controls remain mechanism-adjacent. |
| C15 | `true, 1, 28, false` | Answers are valid and do not visibly leak; wrong and shuffled controls remain mechanism-adjacent. |
| C16 | `false, 2, [0,12], 0` | The stored witness is valid, but alternative-witness scoring is missing; shuffled common-divisor text directly cues the shared-factor mechanism. |
| M17 | `true, true, true, false` | No situation-specific mathematical defect; elementary permutation checks and adjacent shuffled text create ceiling risk. |
| M18 | `false, true, false, false` | Answers are valid; shuffled common-divisor text is useful for the coefficient-invertibility check. |
| M19 | `true, true, true, false` | The visible identity composition effectively answers T3; ceiling risk is strong. |
| M20 | `true, false, false, false` | Answers are valid; shuffled common-divisor text is useful for the coefficient-invertibility check. |

## Required corrections before freeze

1. Resample or truncate the leaking R mappings, move C13's reconstruction target
   outside its visible sample, stop exposing G's scored baseline gcds or change
   the interventions, and replace M19's identity composition.
2. Give multiplication and CRT witnesses distinct semantic answer kinds with
   private mechanism parameters, then test alternative orderings and residue
   representatives.
3. Use an audited mechanism-orthogonal shuffled pool whose deterministic
   assignment is independent of subtype and answer pattern.
4. Remove procedural content from G's sterile control, strengthen the coprime
   CRT wrong control, and roughly length-match controls.
5. Replace duplicated or constant task templates with representation-change,
   composition, diagnosis, or less direct reconstruction variants rather than
   increasing integer size.

Because no Qwen result is present, these corrections may still be made in v0.
If any Qwen result is produced first, preserve v0 and make the corrections in a
new named gold-set version, as required by the freeze rule.

## Evidence inspected

- `python3 experiments/pre_rl_signal/gold_set_v0/validate.py`: validated 20
  situations and 80 hidden tasks.
- `python3 -m unittest discover -s experiments/pre_rl_signal/tests -v`: all 16
  tests passed.
- Independent finite enumeration and integer-arithmetic checks: 80/80 stored
  answers correct; 5/5 stored and 5/5 sampled alternative witnesses valid.
- Direct scorer probe: `witness_pair` is unsupported.
- Manual comparison of every visible situation, context, shuffled source, hidden
  prompt, and private answer.

The documented `python` command was unavailable in the audit environment;
`python3` ran the same checks. This portability note does not affect the verdict.
