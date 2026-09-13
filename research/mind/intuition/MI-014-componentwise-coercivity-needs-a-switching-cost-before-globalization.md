# MI-014 — Globalization needs either a component budget or an index-free coercive potential

**Evidence level:** supported by Arithmetic Fidelity through [AF-325](../../arithmetic_fidelity/findings/AF-325-bounded-support-height-uniformizes-prime-antipodal-conditioning.md) and Farey Discrepancy through [FD-103](../../farey_discrepancy/findings/FD-103-power-dense-record-ladders-saturate-the-logarithmic-source-budget.md). The two mechanisms are logically analogous but mathematically distinct.

The earlier version of this note isolated a common failure mode: componentwise coercivity need not survive free switching between source components. Current evidence sharpens that diagnosis because the two lines have now resolved it in **different ways**.

Arithmetic Fidelity retains the component parameter. Fixing a prime support gives a time-height modulus; letting supports vary freely destroys every time-only gap. AF-324--AF-325 show that bounding the component family by maximum prime `H` restores a uniform but degenerating two-resource envelope. The cost of changing support is therefore recorded by an explicit source-size resource rather than eliminated.

Farey Discrepancy instead removes the component index from the coercive quantity. FD-102 replaces per-carrier row inventory by

`A(H,x)=log_2((H-1)/(8x-1))`,

which survives arbitrary retagging. A carrier switch can replenish potential only by paying through a smaller source quotient, so the local termination theorem globalizes without tracking carrier identity. FD-103 then proves that this index-free logarithmic budget is sharp on actual record ladders.

These are two reusable globalization architectures. One may **retain and price the component label** in a destination-visible parameter, as Arithmetic Fidelity does with support height, or derive an **index-free potential** whose dissipation already absorbs switching, as Farey does with `(H,x)`. Asking for an extra switching cost is necessary only when neither architecture is available.

The adversarial test is consequently stronger than “is the fixed-component estimate uniform?” If not, identify whether the degeneration can be parameterized by a source resource that the final theorem can keep. Independently ask whether the component index can be quotiented out by a coercive state variable that telescopes across switches. Only if both fail is an explicit switch-count/variation penalty still the missing theorem.

**Boundary.** AF support height does not determine exact support provenance and its current upper/lower moduli are far from sharp. FD's carrier-free potential controls deterministic source-neutral depth, not packet energy. No numerical potential transfers between the lines.