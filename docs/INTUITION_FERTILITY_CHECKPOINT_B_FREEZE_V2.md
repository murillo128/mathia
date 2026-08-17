# Intuition-fertility Checkpoint-B freeze v2

Status: `FROZEN`. Checkpoint B v2 is complete. Checkpoint B v1 remains exact
historical evidence. Checkpoint C, qwen-lean inference, Lean verification,
merge, and auto-merge remain unauthorized.

The content-addressed source of truth is
`experiments/intuition_fertility/checkpoint_b_v2.json`:

```text
checkpoint_b_v2_7c9e79db2be94f2e8aa5907b1918e63c407fd435954e315f28e75315aa3904c9
```

It binds the accepted Checkpoint-A v2 freeze and the merged Checkpoint-B v1
source on Mathia main `f29c4388a8eb4cf88c03f1810a96a03a2f8aa1dc`.

## Prospective prompt amendment

For both generator roles and every A–G target, the v1 theorem statement and
semantic intuition request remain byte-identical. B v2 inserts exactly one
common sentence after that request and before the unchanged `Strategy:`
delimiter:

```text
Keep the entire strategy to at most 45 words.
```

Removing that one inserted line reconstructs every B-v1 generator prompt
byte-for-byte. The artifact records both complete templates and all seven old
and new prompt hashes. The instruction is not a post-generation repair or a new
eligibility calculation: the unchanged eligibility gate remains at most 96
qwen-lean-tokenizer tokens after deterministic Lean-comment escaping.

## Generation

Exactly 14 new sample-index-0 outputs were generated and preserved: one
Qwen-base and one Codex-reference output for every standard public A–G
presentation. No B-v1 sample was mixed, selected, or substituted.

Qwen used the same `Qwen/Qwen3-8B-Base` model/tokenizer revision
`49e3418fbbbca6ecbdf9608b4d22e5a407081db4`, vLLM 0.10.2, bfloat16,
no quantization or chat template, exact pretokenized amended prompts, greedy
decoding, seed 0, and `max_new_tokens=96`. All seven prompts ran once in one
batch on the project-controlled local Ada and stopped at EOS.

Codex used the unchanged CLI 0.147.0 executable, SHA-256
`cb0a15567e9a60a5820d54b0f6ae86d504dc3805c1eab21a47f70e3eb7b73a40`,
`gpt-5.6-sol`, reasoning effort `xhigh`, and one fresh empty, ephemeral,
read-only, tool-free session per theorem. All seven sessions completed validly.

No output was regenerated, selected by expected quality, rewritten, padded, or
semantically truncated. A first system-Python invocation failed at import time
because that interpreter had no `torch`; it occurred before tokenizer/model
loading, created no capture, and performed no sample attempt. The actual frozen
Qwen environment was then validated before the single generation batch. This
preflight incident and zero-retry disposition are explicit in the artifact.

## Token and leakage eligibility

All 14 new raw outputs are within the unchanged 96-token post-escape limit:

- Qwen-base: 32–67 tokens;
- Codex-reference: 57–67 tokens;
- over-budget samples: 0.

The overt-Lean-marker rule did not trigger. Every sample received two fresh,
blind Codex leakage-only reviews. The 28 sessions saw only public theorem
statement plus candidate guidance and completed without tools or invalid
output. Their raw labels were 26 `strategic`, one `borderline`, and one
`proof_like`.

The two non-strategic reviews both concern Codex-reference G and disagree.
Under the unchanged resolution rule, the frozen sample decision is therefore
`borderline`, disputed, and ineligible. The other 13 samples are `strategic`
and eligible. Nothing was reclassified, replaced, or imputed.

## Historical preservation, evidence, and boundary

Checkpoint B v1 remains byte-identical:

- freeze ID:
  `checkpoint_b_3236405f0e7ac34ff7bfa1e8f90c27dc29e4a59374bb523ff26c3976e035d640`;
- artifact SHA-256:
  `31bf0a493ef19560777c85936dba1362c6b6ebcd48df0a268b2276fadd789068`.

`experiments/intuition_fertility/checkpoint_b_evidence_v2/` contains 106
hash-bound files: the Qwen batch record, seven Codex generation records, 28
review records, their JSONL transcripts, and stderr captures. The B-v2 freeze
also retains exact raw texts, capture identities, prompt hashes, post-escape
token IDs/counts, individual reviews, final decisions, and ineligibility
reasons.

- B-v2 runner SHA-256:
  `e05cbe535d4b950ca954d36b8679b18c3b9156999bca10d1e811837fd714fdab`;
- unchanged reviewer schema SHA-256:
  `616312c41934b1b3ad654fab72a327bb7cf358250c542342a197ed4aac172734`;
- B-v2 artifact SHA-256:
  `4ad38162d14f9301689878675d1c699eb9a108e80d0462a5eece288f37cca45a`.

No qwen-lean inference or Lean verification was executed. The four historical
B/seed-0 formal-worker draws remained sealed and unopened. This freeze does not
materialize or authorize Checkpoint C.

## Validation

From the repository root:

```bash
python3 -m experiments.intuition_fertility checkpoint-b
python3 -m experiments.intuition_fertility checkpoint-b-v2
python3 -m unittest discover -s experiments/intuition_fertility/tests -v
python3 -m compileall -q experiments/intuition_fertility
```
