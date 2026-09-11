# MI-001 — Farey occupation is a low-row placement problem with a sharp additive-transfer threshold

**Evidence level:** supported by exact source and occupation bounds

## Core intuition

The Farey obstruction has been narrowed from generic regularity to a thin low-row placement problem. Correct zero-frontier exponents, positive terminal bulk, and logarithmic-density control do not force pointwise occupation. The newest evidence separates two very different source probes: **signed multiplicative rays can self-cancel**, even for moving hosts near the square-root boundary, while quadratic occupation can be transferred to a nearby nonsquarefree row once the host is large enough relative to the source spike.

The remaining escape is therefore not simply “rare horizons.” It is rare low-row geometry below an explicit zero-frontier-dependent additive-transfer threshold.

## Strongest justified claim

FD-049--FD-051 show that positive polynomial occupation loss is limited by the rightmost zero frontier, vanishing occupation can occur only on zero global logarithmic density, and the terminal nonsquarefree bulk is uniformly positive through quotient depth `o(sqrt H)`.

FD-052 identifies a source-specific but noncoercive multiplicative law. Jordan-weighted dilation rays cancel the `1/zeta(s)` pole structure exactly; under false RH, a large squarefree-row spike can be balanced to leading order by other squarefree rows, so the nonsquarefree **signed first moment** need not carry the spike.

FD-053 makes that obstruction robust for moving hosts. The same squarefree self-cancellation persists whenever the host cost `P_sigma(q)=o(log X)`, including primorial hosts reaching the geometric square-root-row regime. A one-dimensional multiplicative first-moment argument is therefore insufficient even at the frontier isolated by FD-051.

FD-054 shows that quadratic occupation behaves differently. For a squarefree host `q`, the nearest multiple of four lies only `O(1)` rows away. If `q |Hcal(X)|/X -> infinity`, the one-Lipschitz source law transports the spike to that nonsquarefree neighbor with relative error `o(1)`, forcing a comparable nonsquarefree quadratic-energy contribution. Along a zero-frontier spike `|Hcal(X)| >= X^(Theta-delta)`, this mechanism activates once `q` is above the scale `X^(1-Theta+delta)`.

## Synthesis of evidence

Signed dilation coherence is now a matched negative control rather than the missing theorem. The promising currency is **additive physical adjacency plus quadratic occupation**, but it only works above a host-scale threshold. The unresolved region is the low-row side at or below the zero-frontier threshold, where a large source value can change by an amount comparable to itself across an `O(1)` row move.

A closing theorem must either push additive/quadratic transference below that threshold using extra arithmetic structure, or show that the remaining low-row hosts cannot contain enough total energy to realize pointwise occupation collapse.

## Counterevidence / boundary cases

FD-054 is a sufficient transference criterion, not a pointwise lower bound for every row. It leaves hosts with `q |Hcal(X)|/X=O(1)` uncontrolled. Under RH-scale source size this is precisely a square-root-type transition, so the surviving region can still overlap the difficult geometric boundary.

The multiplicative self-cancellation results concern signed first moments and do not contradict the quadratic twin mechanism.

## Epistemic status

**Supported source-geometry boundary:** multiplicative signed rays can self-cancel through moving square-root-scale hosts, whereas sufficiently large squarefree hosts force a nearby nonsquarefree quadratic twin. Any residual occupation escape must live below the additive-transfer threshold or exploit geometry not seen by that local comparison.

## Novelty/prior-art status

No broad novelty claim is made beyond finding-level audits. This note synthesizes the exact zero-frontier, Jordan-ray, and additive occupation consequences.

## Falsification criterion

Invalidate the Jordan-ray cancellation, the moving-host bound, or the FD-054 additive twin estimate. Strategically, construct a physical-compatible low-row escape below the threshold, or prove a source law that transfers comparable quadratic energy there as well.
