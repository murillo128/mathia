# Model and compute constraints for the first Mathia experiment

This note records two provisional experimental constraints that improve comparability with `qwen-lean` and avoid competing for the same project GPU. They are execution choices for the first experiment, not permanent architectural decisions.

## Shared model ancestor

For the first trainable Mathia experiment, use the same exact base model revision already pinned by `qwen-lean`:

```text
model:     Qwen/Qwen3-8B-Base
revision:  49e3418fbbbca6ecbdf9608b4d22e5a407081db4
tokenizer: Qwen/Qwen3-8B-Base
revision:  49e3418fbbbca6ecbdf9608b4d22e5a407081db4
```

The purpose is experimental comparability. Starting both projects from the same weights and tokenizer makes later comparisons between formal and conceptual post-training substantially cleaner:

```text
                         same Qwen3-8B-Base revision
                           /                  \
                          /                    \
                         v                      v
                 qwen-lean formal        Mathia conceptual
                  post-training           post-training
                         |                      |
                         v                      v
                        MF                     MC
```

This preserves meaningful future tests such as formal-first versus conceptual-first training, independent adapters, sequential post-training, agent cooperation, and possible model/adaptor merging without introducing a different base checkpoint as a confounder.

The choice should be revisited if the 8B model makes the conceptual RL experiment impractical on the available single GPU. A smaller model is preferable to a broken experiment, but should be treated as a deliberate deviation rather than silently changing the common ancestor.

## Single-Ada resource gate

The project currently shares a single Ada-class GPU resource with `qwen-lean`.

Mathia should **not compete with qwen-lean for that GPU** during the current qwen-lean execution. GPU-dependent Mathia work should begin only when one of the following becomes true:

1. qwen-lean has completed the GPU work that currently needs the machine; or
2. the GPU is otherwise explicitly free for a bounded Mathia run.

This is a resource-scheduling constraint, not a research dependency. Mathia does not require qwen-lean to finish conceptually before continuing.

## Work that may proceed without the GPU

While the Ada remains occupied, Mathia can continue with CPU/API/repository work that reduces uncertainty before training, including:

- expanding the first mathematical world and its exact verifiers;
- hand-designing visible situations and hidden interventions;
- generating competing conceptual/control contexts with external teacher models;
- auditing context leakage and task difficulty;
- preparing deterministic evaluation manifests;
- designing paired statistical comparisons;
- implementing model-agnostic prompt/result serialization;
- generating a small cold-start candidate corpus without committing to it as training truth;
- checking that the pre-RL signal study is capable of discriminating context conditions using external/API solvers where useful.

Avoid building GPU-specific training machinery merely to stay busy. The important precondition for post-training remains evidence that the proposed conceptual signal is worth optimizing.

## GPU entry gate

When the Ada becomes available, the first GPU work should still be diagnostic rather than immediate RL.

The intended order at that point is:

```text
Qwen3-8B-Base exact pinned revision
        |
        v
run unchanged base model on pre-RL context study
        |
        v
establish base/context-condition measurements
        |
        v
only if the signal is credible: cold-start / post-training experiment
```

Do not start conceptual SFT or RL merely because the GPU becomes free. The pre-RL study should first show that structural conceptual contexts produce a measurable and interpretable effect relative to no-context, factual, procedural, sterile, wrong, and shuffled controls.

## Why waiting is useful rather than lost time

Using the same GPU sequentially is experimentally useful. qwen-lean will exercise much of the common Qwen/QLoRA/TRL/vLLM stack first, while Mathia can focus meanwhile on the part that is genuinely different: the mathematical environment and reward signal.

When Mathia begins GPU work, it can reuse lessons from qwen-lean without coupling the conceptual research hypothesis to Lean. The two projects remain separate experiments that share a model ancestor, compute environment, and potentially generic ML infrastructure.
