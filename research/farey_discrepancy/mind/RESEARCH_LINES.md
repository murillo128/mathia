# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Upgrade power-dense frontier records to logarithmic/ordinary recurrence of protected blocks

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-072 supplies a source-selected positive mechanism: at a `sigma`-power record with `sigma>1/2`, the causal horizon `T=4X`, `D=3` confines the complete denominator to the record-controlled prefix and forces fixed positive nonsquarefree occupation and Schur defect. FD-073 turns each such episode into an amplitude-length protected block. FD-074 constrains the center, and FD-075 forces a growing same-parity large-radical population inside the block.

FD-076 now removes arbitrary power-scale sparsity. For every fixed `lambda in (0,1)`, the physical source has a `Theta`-order value inside `[X^(1-lambda),X]`. Hence, for every `0<sigma<Theta`, strict `sigma`-records occur in every sufficiently large fixed power window, consecutive records satisfy

`log X_(j+1)/log X_j -> 1`,

and their amplitudes satisfy `|H(X_j)|=X_j^(Theta+o(1))`.

Under false RH (`Theta>1/2`) the protected block radius is therefore `X_j^(Theta+o(1))`, while the FD-075 arithmetic cloud has size at least `X_j^(2Theta-1-o(1))` and radical scale `X_j^(Theta-o(1))`.

The remaining theorem is narrower: improve the subpower gap freedom `X_(j+1)=X_j^(1+o(1))` to enough ordinary or logarithmic recurrence that these shrinking-relative-width protected blocks force a global same-horizon occupation statement, or find another exact aggregation mechanism that uses the power-dense frontier records without requiring block overlap.

## Keep local protection, host multiplicity, frontier amplitude and global recurrence as separate currencies

FD-071 explains why arbitrary-later persistence can be normalized away; FD-072 protects a causal record; FD-073 thickens it; FD-074 constrains its center; FD-075 forces a growing arithmetic population inside the same block; FD-076 fixes the amplitude to the actual zero-frontier exponent and excludes fixed power gaps between strict records. None of these yet controls bounded multiplicative spacing or positive logarithmic density. Any negative model must now reproduce the exact local cloud **and** frontier-sized records at power-dense scales while keeping the protected blocks globally too sparse to accumulate.