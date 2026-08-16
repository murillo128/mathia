# Pre-RL conceptual signal experiment

Implement the smallest executable version of `docs/PRE_RL_SIGNAL_STUDY.md` here.

Initial implementation should focus on deterministic finite-arithmetic generation and verification for a small subset of the seed situations in `docs/FIRST_MATHEMATICAL_WORLD.md`.

The first code should make it possible to:

1. generate visible mathematical situations and hidden interventions separately;
2. deterministically compute hidden ground truth;
3. serialize small fixtures for inspection;
4. evaluate externally supplied solver answers without an AI judge;
5. keep conceptual context generation separate from task generation/evaluation.

Do not add RL training or model-specific serving infrastructure in this first implementation.

## Gold-set-v0 prompt/result runner

`runner.py` provides the CPU-only, provider-neutral plumbing for issue #12. It
does not load a model, call a provider, or choose the final execution order and
generation configuration owned by issue #9.

Materialize the canonical public prompt JSONL and its provenance sidecar:

```bash
python3 -m experiments.pre_rl_signal.runner materialize \
  --output /tmp/gold-set-v0-prompts.jsonl
```

External responses use one JSON object per line. Only `prompt_id` and a string
`raw_response` are required; additional fields are retained opaquely:

```json
{"prompt_id":"gold-set-v0/R01/T1/none","raw_response":"1","provider":{"request_id":"example"}}
```

Import and score a complete response file with caller-supplied provenance:

```bash
python3 -m experiments.pre_rl_signal.runner score \
  --manifest /tmp/gold-set-v0-prompts.jsonl \
  --responses /tmp/responses.jsonl \
  --output /tmp/results.jsonl \
  --model-id example/model \
  --model-revision example-revision \
  --generation-settings '{"temperature":0}'
```

`--allow-partial` is an explicit plumbing-only escape hatch; its summary and
sidecar report missing responses and `complete: false`. Unknown IDs, duplicate
IDs, missing/non-string responses, and prompt/manifest hash mismatches remain
fatal. Responses are parsed as one complete JSON value with no Markdown or
prose cleanup, and format failures remain distinct from mathematical failures.

Run the private-answer oracle only as a synthetic end-to-end check:

```bash
python3 -m experiments.pre_rl_signal.runner oracle \
  --manifest /tmp/gold-set-v0-prompts.jsonl \
  --output /tmp/oracle-results.jsonl
```

The expected summary is 560 imported, 560 parsed, and 560 correct. Oracle
results are labeled `synthetic/oracle`; they are plumbing evidence, not model or
mathematical-reasoning evidence. Prompt manifests never contain oracle answers
or private scoring parameters.
