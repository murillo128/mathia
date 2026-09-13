# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Couple branchwise mass loss, horizon contraction and source descent

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`, `MI-002-odd-prime-square-reembedding-localizes-recursive-failure-to-dyadic-channel`, `MI-003-normalized-record-defect-is-the-composition-loss`, `MI-004-multiplicative-horizon-descent-can-preserve-the-source-quotient`, `MI-005-source-neutral-carrier-descent-spends-a-strict-finite-row-potential`.

FD-102 gives the sharp carrier-free source-neutral potential

`A(H,x)=log_2((H-1)/(8x-1))`,

and FD-103 shows that actual false-RH source-record ladders saturate its logarithmic coefficient. Deterministic floor geometry therefore cannot shorten the source-neutral window.

FD-104 closes the old packet-strength uniformity gap above the linear nonsquarefree-mass floor. Direct compression from one physical state gives a predecessor with

`U_C/C^(2sigma) >= b_sigma U_H/H^(2sigma)`

for every fixed `1/2<sigma<Theta` whenever `U_H>=H^(1+delta)`. FD-105 further proves that high mass is automatically source-localized: with `L_H=floor(U_H/(H log H))`, the selected predecessor can retain its mass on source arguments above `L_H/2`. The guaranteed `c log H_0` predecessor chain therefore remains at polynomial physical and source scale relative to its entry; bounded-scale collapse and loss of all source tags are no longer escapes.

The live theorem is now **branch-sensitive amortization**. The global constant `b_sigma` forgets which predecessor branch occurred, how much the horizon contracted, and whether that branch paid through head movement or source descent. Recover a joint inequality in those three currencies strong enough that a chain saturating the sharp FD-102 source-neutral budget cannot simultaneously retain the false-RH normalized mass. A scalar improvement of `b_sigma` with no branch information is not the target.

## Locate the exact boundary of the high-mass mechanism

The adaptive source threshold is intrinsic: `L_H` tends to infinity exactly when `U_H/H` does. At the linear floor `U_H=H^(1+o(1))`, neither the source-rich core nor the current error normalization gives a growing source tag. A continuation that reaches this boundary must either prove the false-RH chain stays a fixed power above the floor long enough, or introduce a different observable whose compression error is still negligible at near-linear mass.

This boundary should not be conflated with the old projective-certificate problem. FD-104--FD-105 already handle polynomially small projective quality throughout the fixed-power high-mass regime. The unresolved issue is what the **actual branch sequence** forces before that regime can be exhausted.

## Keep deterministic budget, transport mass and source progress distinct

Source records provide recurrent entry states; FD-102 supplies an index-free deterministic charge; FD-103 proves that charge sharp; FD-104 transports actual normalized mass; FD-105 transports an adaptive source tag and prevents premature scale collapse. None of these alone compares branchwise source descent to normalized-mass loss. Future arguments should preserve that joint data instead of replacing it by another carrier identity or one worst-case predecessor constant.
