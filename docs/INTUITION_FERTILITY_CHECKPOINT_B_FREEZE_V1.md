# Intuition-fertility Checkpoint-B freeze v1

Status: `FROZEN`. Checkpoint B is complete; Checkpoints C/D, qwen-lean target
inference, Lean verification, merge, and auto-merge remain unauthorized.

The content-addressed source of truth is
`experiments/intuition_fertility/checkpoint_b_v1.json`:

```text
checkpoint_b_3236405f0e7ac34ff7bfa1e8f90c27dc29e4a59374bb523ff26c3976e035d640
```

It binds the accepted Checkpoint-A v2 freeze
`checkpoint_a_v2_bf521c46c79d64ac7e250989e82cb58cdadec40e08de2159839ad4c15ed688dc`
on Mathia main `a2be33433414478adf33441670bfa477a90bdf8a`.

## Generation

Exactly 14 sample-index-0 outputs were generated and preserved: one Qwen-base
and one Codex-reference output for each standard public A–G presentation.

Qwen used `Qwen/Qwen3-8B-Base` and tokenizer revision
`49e3418fbbbca6ecbdf9608b4d22e5a407081db4`, vLLM 0.10.2, bfloat16,
no quantization, no chat template, exact pretokenized public prompts, greedy
decoding, seed 0, and `max_new_tokens=96` on the project-controlled local Ada.
The seven prompts were submitted once as a single batch. Runtime-only capacity
settings (`max_model_len=2048`, `gpu_memory_utilization=0.95`,
`max_num_seqs=7`, eager execution) are recorded in the evidence; they do not
change the frozen prompt or greedy decoding contract.

Codex used CLI 0.147.0 with executable SHA-256
`cb0a15567e9a60a5820d54b0f6ae86d504dc3805c1eab21a47f70e3eb7b73a40`,
`gpt-5.6-sol`, reasoning effort `xhigh`, and one fresh ephemeral, empty,
read-only session per theorem. User config and rules were disabled. All seven
sessions exited successfully and their transcripts contain no tool events.

No output was regenerated, selected by expected quality, rewritten, padded, or
semantically truncated. Raw text, text hash, capture identity, prompt hash,
generator identity, tokenizer identity, token ids/counts, and Codex JSONL
transcript hashes are retained.

## Token eligibility

The exact qwen-lean tokenizer counted deterministic Lean-comment-escaped text,
before wrapper delimiters:

- all seven Qwen-base samples contain exactly 96 tokens and remain within the
  token budget;
- all seven Codex-reference samples contain 146–230 tokens and are preserved as
  `over_96_token_budget` ineligible samples.

The Codex samples were not shortened or regenerated. Their ineligibility is a
protected Checkpoint-B observation and a material limitation for any later
experiment materialization; this freeze does not redesign the cap or authorize a
next checkpoint.

## Blind leakage classification

The overt-Lean-marker check ran first and did not trigger. Every sample then
received two fresh Codex leakage-only reviews under the frozen JSON schema. Each
reviewer saw exactly public theorem statement plus candidate text, with no
generator identity, private metadata, other sample, or formal-worker outcome.
All 28 reviews completed without tool events or invalid output.

The frozen resolution produced:

- `strategic`: 11;
- `borderline`: 3;
- `proof_like`: 0;
- uncertain: 0;
- disputed: 3.

The disputed cells are Codex-reference D, F, and G; the exact policy maps each
disagreement to `borderline`. Combined token/leakage eligibility retains seven
eligible Qwen samples and seven ineligible Codex samples. Every label and
ineligibility reason remains present; there is no imputation or replacement.

## Evidence and boundary

`experiments/intuition_fertility/checkpoint_b_evidence_v1/` contains the
write-once Qwen capture, seven Codex generation records/transcripts, 28 reviewer
records/transcripts, and empty stderr captures. The freeze hashes every file and
also stores post-escape token ids so CPU-only validation can detect evidence,
text, count, identity, or transcript drift.

The execution runner SHA-256 is
`07cc92ad5af00adb6ccadb3ca62778024096bede1de3bab144359d337a8eeb85`;
the reviewer output-schema SHA-256 is
`616312c41934b1b3ad654fab72a327bb7cf358250c542342a197ed4aac172734`;
the frozen artifact file SHA-256 is
`31bf0a493ef19560777c85936dba1362c6b6ebcd48df0a268b2276fadd789068`.

No qwen-lean inference or Lean verification was executed. The four historical
B/seed-0 formal-worker draws remained sealed and unopened.

## Validation

From the repository root:

```bash
python3 -m experiments.intuition_fertility checkpoint-a-v2
python3 -m experiments.intuition_fertility checkpoint-b
python3 -m unittest discover -s experiments/intuition_fertility/tests -v
python3 -m compileall -q experiments/intuition_fertility
```
