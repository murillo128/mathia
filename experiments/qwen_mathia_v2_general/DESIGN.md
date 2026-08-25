# Qwen-Mathia v2 general design (`#55`)

## Decision

`QWEN_MATHIA_V2_GENERAL_DESIGN_READY`

Issue #55 is resolved at the design and CPU-materialization boundary. The frozen
workload is `G-v2`, and its content-bound identifier is:

```text
g_v2_72d7565e29afa2df28fdd2b994d7d3e077f044bd1654133847f4d84981e94b0c
```

This decision authorizes a separate GPU train/publish execution issue. It does
not report an SFT run, a published adapter, theorem-proving improvement,
conceptual-transfer improvement, or downstream formal-worker result.

## Exact ancestor and scope

The authoritative amendment on issue #55 supersedes every older 9B reference.
Both the model and tokenizer are frozen to:

```text
Qwen/Qwen3.5-4B-Base@1001bb4d826a52d1f399e183466143f4da7b741b
```

The exact-revision upstream model card and Apache-2.0 license are hash-bound in
`config.json`. The card identifies this Base checkpoint as a fine-tuning parent
and states that its control tokens support LoRA-style PEFT with the official
chat template. The design selects the text-only `Qwen3_5ForCausalLM` path from
the upstream multimodal configuration; the vision encoder is not instantiated,
targeted, or trainable.

Qwen-Mathia v1 is not a weight parent. Riemann-Mathia releases, records, and
specialization are not inputs. The only allowed parents are the two exact
general releases below.

## G-v2 parent bindings and selection

| Parent | Exact freeze | Selected targets |
|---|---|---:|
| `agnostic-mathia-full-v1` | `freeze_eeeeb89af3d2ac75d1ff5dad5623b63d1d24dfbddb965beca2f1c4aac9f9867f` and reviewed-content freeze `review_content_d1d1d7152fa2c2ddd3a4f6d26a4fa4b3f6d64129392b7c79ea72f125b5d95c0b` | 98 interpretations + 18 syntheses |
| `agnostic-mathia-openalex-supplement-v1` | `agnostic_openalex_supplement_a1aa591df034db64d5ce0271df0da570e3aaf470ac49e5cc4014b66181bf0e33` | 295 interpretations |

The historical #44 counts reproduce rather than being assumed. The supplement's
595 eligible objects comprise 300 context/provenance sources and 295 optimizer
interpretations; 595 is therefore never treated as the supervised-target count.
All `source` objects remain context only. The selected 411 rows are all accepted
and eligible, with zero selected rejected, quarantined, evaluation-only, source,
or foreign-lineage records.

The supplement source-unit text remains outside Git under its original licensing
boundary. CPU materialization requires the preserved external artifact and
validates every referenced unit against the `content_sha256` already frozen in
the release. The committed optimizer manifest contains hashes, IDs, lineage,
token ranges, and counts, not restricted source text.

### Cross-parent dedupe

The deterministic order is:

1. require identical canonical records for a repeated `object_id`;
2. deduplicate equal `content_sha256` plus equal source/version-lineage hash;
3. retain and report equal content with different lineage;
4. run a non-deleting near-duplicate diagnostic on normalized supervised
   assistant content.

The materialized result has zero repeated identities, zero exact
content-and-lineage collisions, zero equal-content/distinct-lineage groups, and
zero pairs at or above the frozen lexical-token-trigram Jaccard threshold of
0.8. No example was deleted. The manifest records counts by parent, role, and
source ID, while the original parent records retain full lineage.

## Official chat-template and loss boundary

The canonical `mathia-interchange-v1` renderer still determines the mathematical
material, task, and exact accepted response. The model wrapper removes only the
serialization-only `## Response` heading and the response from the user message;
it does not rewrite mathematical content. The pinned official template is then
applied with no system message, `enable_thinking=false`, and one user/assistant
exchange.

Conceptually, the exact boundary is:

```text
MASKED
<|im_start|>user
{canonical mathematical material and Mathia task}<|im_end|>
<|im_start|>assistant
<think>

</think>

SUPERVISED
{exact accepted interpretation or synthesis}<|im_end|>\n
```

The empty official assistant prefix is masked; it is not an optimizer target.
The accepted content and official assistant-end sequence are supervised. On the
pinned tokenizer, `<|im_end|>\n` is `[248046, 198]`. No extra
`<|endoftext|>` token is appended after the complete official template. Every
row records exact visible-byte hashes, token counts, and three label ranges:
masked prompt, supervised assistant content, and supervised assistant end.
Full tokenization must reproduce the prefix boundary exactly, so cross-boundary
token merges fail materialization.

The later Base-vs-Mathia comparison must use this same public template lane for
both checkpoints.

## CPU token audit and sequence bound

The following entries are `p50 / p90 / p95 / p99 / max` and include the official
assistant boundary. Exact distributions and longest object IDs are in the
manifest.

| Group | Examples | Prompt | Supervised | Total |
|---|---:|---:|---:|---:|
| All G-v2 | 411 | 1045 / 2846 / 3801 / 6283 / 9332 | 83 / 144 / 157 / 196 / 215 | 1129 / 2926 / 3899 / 6494 / 9429 |
| #44 interpretation | 98 | 192 / 224 / 243 / 257 / 257 | 115 / 152 / 157 / 196 / 196 | 322 / 364 / 384 / 448 / 448 |
| #44 synthesis | 18 | 249 / 584 / 599 / 599 / 599 | 105 / 142 / 147 / 147 / 147 | 348 / 716 / 741 / 741 / 741 |
| OpenAlex interpretation | 295 | 1435 / 3151 / 4244 / 7319 / 9332 | 75 / 126 / 160 / 211 / 215 | 1509 / 3208 / 4353 / 7400 / 9429 |

The longest row is
`mathia_interpretation_af69de0ded7ddb5dc9934f8c8a0aee87f79253c9866fc2308467bbba31d05a10`
at 9,429 tokens. Therefore the frozen maximum is **9,472**, the smallest
128-token multiple containing every selected row. Packing and truncation remain
false. The design does not shorten or drop long supplement context.

One unique corpus pass contains:

```text
examples:                    411
prompt tokens:               556,227
assistant content tokens:     37,135
assistant end tokens:            822
supervised tokens total:       37,957
all tokens:                   594,184
```

## Language-only LoRA boundary

The CPU architecture audit used Transformers 5.15.1, PEFT 0.20.0,
bitsandbytes 0.50.1, Accelerate 1.14.0, and Torch 2.13.0. It loaded the pinned
multimodal configuration and tokenizer, instantiated the text-only causal LM on
the meta device, attached PEFT, and constructed the intended NF4 configuration.
It does not claim a CUDA forward/backward or memory result.

The exact anchored target expression is:

```text
^model\.layers\.\d+\.(?:self_attn\.(?:q_proj|k_proj|v_proj|o_proj)|linear_attn\.(?:in_proj_qkv|in_proj_z|in_proj_a|in_proj_b|out_proj)|mlp\.(?:gate_proj|up_proj|down_proj))$
```

| Family | Suffixes | Modules |
|---|---|---:|
| Full attention | `q_proj`, `k_proj`, `v_proj`, `o_proj` | 8 each / 32 total |
| Gated DeltaNet | `in_proj_qkv`, `in_proj_z`, `in_proj_a`, `in_proj_b`, `out_proj` | 24 each / 120 total |
| MLP | `gate_proj`, `up_proj`, `down_proj` | 32 each / 96 total |

The regex matches 248 language projections and zero vision, embedding,
normalization, or LM-head modules. With rank 16 and alpha 32:

```text
text-only base parameters:          4,841,450,496
trainable LoRA parameters:             32,464,896
PEFT-wrapped total parameters:       4,873,915,392
trainable adapter tensors:                    496
```

This is the complete fused text-projection coverage requested by the issue; it
is not the v1 Qwen3-8B suffix list copied by rote and it is not an `all-linear`
selector.

## Frozen optimizer exposure

The recipe retains the issue's NF4 QLoRA prior: BF16 compute, double
quantization, rank 16 / alpha 32 / dropout 0, `paged_adamw_8bit`, learning rate
`5e-5`, zero weight decay, max gradient norm 1, cosine schedule, micro-batch 1,
gradient accumulation 8, gradient checkpointing, packing false, truncation
false, and seed 0.

Terminal exposure is frozen to one complete pass, not four epochs. A
version-independent SHA-256 keyed order is committed and runtime sampler
shuffling is disabled. With effective batch 8, one pass is 52 optimizer steps,
close to v1's 60 steps without multiplying the larger workload by four.
The final step contains three micro-batches and must not be dropped.

| Checkpoint | Step | Examples | Prompt tokens | Supervised tokens | All tokens |
|---|---:|---:|---:|---:|---:|
| around 25% | 13 | 104 | 160,680 | 9,674 | 170,354 |
| around 50% | 26 | 208 | 296,033 | 19,374 | 315,407 |
| terminal 100% | 52 | 411 | 556,227 | 37,957 | 594,184 |

The step-52 adapter is the precommitted publication root. Steps 13 and 26 are
recoverability evidence, not candidates for subjective checkpoint selection.

## Separate GPU execution gate

The next issue must run on the intended RTX 4000 Ada 20 GB lane and stop if the
frozen contract does not fit. It must demonstrate:

- the exact base/tokenizer revision and immutable snapshot hashes;
- text-only Qwen3.5 forward/backward using a compatible DeltaNet training
  backend;
- vision exclusion and exact trainable-parameter ownership;
- finite loss and non-zero LoRA gradients;
- exact completion-only masks and no truncation at 9,472 tokens;
- adapter save/reload identity;
- peak allocated/reserved VRAM and a safe margin at the true longest row;
- coexistence and switching of Mathia, qwen-lean-planner, and qwen-lean adapters
  over one resident Base, including inference KV-cache/headroom measurements.

V1's memory headroom is not evidence for this model and sequence length. If the
20 GB lane fails, the execution must record a concrete capacity blocker and move
to more memory; it must not shrink, truncate, shorten, or silently remove G-v2
examples.

## Publication and scientific handoff

The frozen publication name is
`murillo2000/qwen3.5-4b-base-mathia-v2`. The primary artifact remains a PEFT
adapter, not merged weights. Publication must retain exact config/manifest,
checkpoint hashes, runtime evidence, role/token exposure, immutable base and
tokenizer revisions, conservative `license: other`, the no-Riemann statement,
and clean-cache immutable-revision verification. Raw/restricted sources, a base
model copy, secrets, and caches must not be uploaded.

After successful GPU execution and after the current qwen-lean SFT is complete,
the scientific experiment is the matched:

```text
Qwen3.5-4B-Base vs terminal Mathia-v2
        x
qwen-lean vs DeepSeek
        -> Lean verification
```

That A/B is not executed here. Its evidence is solver-conditional until transfer
is measured, and training loss, fluent prose, or teacher similarity remain
insufficient evidence of Mathia capability.
