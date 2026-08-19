# Issue #42 behavioral continuation report

## Preserved v0 and repaired units

The original pilot remains immutable at freeze `riemann_pilot12_60d97cc4b13673cfcebf65f4d31e96f7533835a6ae1b50442fb6831a4d28af02`. `v0_snapshot.json` binds all 17 committed v0 files under snapshot `riemann_pilot12_v0_snapshot_a04f67d75b9625482de6736c558195529af3768b4fef620b44ea6e873453a466`. None of the original units, four pass files, synthesis, audit, or report was rewritten.

Three new unit versions repair only the defects named by the owner directive:

| v1 unit | v0 parent hash | v1 revision | v1 unit hash | Status |
| --- | --- | --- | --- | --- |
| `conrey1989_u02_variational_freedom_v1` | `5a785aef00f5d7ba5c338e4944292cf41cd8c94d8b65cdad9fb252a889220dc2` | `riemann_unit_v1_35aac8fdf7efa5ba790c9db07472e5a6fd2762f25bb5524ebd91172f3cb21955` | `9792a4fe0763c1ec14be24032007568a3e3ca8572f75a970434d0983b1099b52` | Careful transcription from frozen PDF page 2 recovers the coefficient family, endpoint conditions, zero-counting objective, and variational relation. |
| `lagarias2002_u01_elementary_equivalence_v1` | `a17a7f70dc235a6289592ffa3fa585e2a83a5809ab0907bd98cbf43e46c8ac15` | `riemann_unit_v1_b2597056bdd9f5acaf2e612564ab88aa0cfdd13874a85df564a8edaa7ef53f26` | `058dabbfeb3bbd844235d3693639df0912bc6e6681f6d9d30c393fc210c8b2e3` | The contiguous span now includes displayed Problem E, its inequality and equality case, and the dependence on Robin's criterion. |
| `rodgers2020_u02_equilibrium_contradiction_v1` | `96059cb68b533316acd705154b22e319596a00e2b75a2e5f58980c42414eba7d` | `riemann_unit_v1_086d76419439ab096331d20839e30238566c47e2c4d002408135b3e0c7ca82df` | `a4d2477aef908b12a6070eb26e71db0424a8d8892989cb15bf8a72f020743dba` | The contiguous span now reaches the time-zero local-equilibrium conclusion and the Montgomery-type contradiction. |

The softer Montgomery and Báez-Duarte boundaries remain at v0. Accepted tasks use only Montgomery's displayed transform and Báez-Duarte's explicit norm failure; they do not import the absent later gap/simplicity consequences or a missing proof of discrete-family sufficiency.

## Behavioral microtasks and perturbations

Three candidate rounds are preserved rather than overwritten. Fresh isolated review accepted 2 of 20 RH candidates in round one, 6 of 14 in round two, and 9 of 14 in the bounded third round. The accepted final RH subset contains nine tasks across nine sources: Riemann, Bombieri, Lagarias, Báez-Duarte, Keating-Snaith, Platt-Trudgian, Conrey 2003, Conrey 1989, and Montgomery.

Representative accepted tasks include:

- `rh2_b01_local_factor_intervention`, which distinguishes two locally identical first-order encodings by their logarithmic repeat term;
- `rh2_b03_frobenius_coordinate_role`, which tracks reciprocal magnitude under `det(I-tF)` versus `det(vI-F)`;
- `rh2_b07_target_topology_controls_evidence`, which changes the norm defining closure;
- `rh3_b08_mollifier_range_bottleneck`, which separates an off-diagonal range theorem from coefficient optimization;
- `rh3_b09_fourier_spike_scale`, which chooses a frequency regime from the two asymptotic transform terms.

Representative rejects include an orbit prompt whose mismatch names map directly to its options, a local-statistics prompt with explicit local/global cues, generic heat-threshold bookkeeping, and a positivity-extension checklist. Earlier rounds also preserve unsupported source imports and favorable-prose options. These are not silently repaired into accepted explanations.

Each final candidate has a cosmetic and structural pair. Examples:

- renaming the local contribution leaves `rh2_b01` at A, while adding `u^2/2` to the exponential encoding changes the answer to C;
- renaming the Frobenius coordinate leaves `rh2_b03` at B, while changing from `det(I-tF)` to `det(vI-F)` changes it to A;
- reordering the topology statement leaves `rh2_b07` at C, while changing the target closure to `L1` changes it to A;
- renaming the frequency leaves `rh3_b09` at B, while asking for the diagonal transition scale changes it to A.

The nine accepted prompts and keys are frozen as evaluation-only material. Because the target was 12–20 tasks, this is a preserved accepted subset and negative result, not a completed training discriminator.

## Held-out transfer panel

Six of nine out-of-Riemann candidates survived all three reviews. They cover six mechanisms:

1. class invariance as the condition for quotient factorization;
2. topology/norm dependence of closure;
3. sign-change witnesses versus exhaustive Sturm-style root counts;
4. normality as the boundary for transferring an orthogonal spectral basis;
5. translation invariance as the boundary for Fourier diagonalization;
6. compactness upgrading weak convergence to norm convergence.

The rejected transfer items are also retained. The recurrence prompt exposes its generating-function key, the finite-exhaustion prompt is generic calibration, and the tensor-power item has a false expected answer because mixed tensor modes prevent the claimed full-spectrum ratio amplification. No transfer prompt is eligible for later learner training.

## Fresh adversarial evidence and scoring

The three isolated reviews rejected 18, 8, and 5 RH candidates respectively. This progression shows that recurring Codex cadence was not an acceptance criterion: direct formula copying, generic implication logic, favorable prose, source overreach, and even a mathematically false key caused rejection. The final nine accepted RH tasks use discrete answers and exact minimal-pair behavior rather than the v0 nine-field prose schema.

All selected RH and transfer tasks are objectively scored by A/B/C core answer. No selected or rejected final-round task was flagged as requiring subjective LLM judgment. This establishes inspectable task/scoring artifacts only; it does not establish learner improvement, mathematical truth by reviewer agreement, or out-of-domain transfer performance.

## Next decision

`REVISE_BEHAVIORAL_TASKS`

The source repairs are adequate and the six-mechanism transfer panel is credible, but the bounded final review accepted only nine RH tasks. A later continuation may replace the five shortcut-prone probes, but this issue does not authorize training, GPU work, Qwen inference, qwen-lean proof search, or a training-design issue on the current evidence.
